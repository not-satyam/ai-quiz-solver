# run_code.py
import subprocess
from langchain_core.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

def strip_code_fences(code: str) -> str:
    code = code.strip()
    # Remove ```python ... ``` or ``` ... ```
    if code.startswith("```"):
        # remove first line (```python or ```)
        try:
            code = code.split("\n", 1)[1]
        except IndexError:
            # If there's no newline after the fence, just return empty or original
            pass
    if code.endswith("```"):
        code = code.rsplit("\n", 1)[0]
    return code.strip()

@tool
def run_code(code: str) -> dict:
    """
    Executes a Python code 
    This tool:
      1. Takes in python code as input
      3. Writes code into a temporary .py file
      4. Executes the file
      5. Returns its output

    Parameters
    ----------
    code : str
        Python source code to execute.

    Returns
    -------
    dict
        {
            "stdout": <program output>,
            "stderr": <errors if any>,
            "return_code": <exit code>
        }
    """
    try: 
        # Clean up the code if the LLM wrapped it in markdown
        code = strip_code_fences(code)
        
        filename = "runner.py"
        os.makedirs("LLMFiles", exist_ok=True)
        with open(os.path.join("LLMFiles", filename), "w") as f:
            f.write(code)

        proc = subprocess.Popen(
            ["uv", "run", filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd="LLMFiles"
        )
        stdout, stderr = proc.communicate()
        
        # Truncate output to prevent token overflow
        if len(stdout) >= 10000:
            stdout = stdout[:10000] + "...truncated due to large size"
        if len(stderr) >= 10000:
            stderr = stderr[:10000] + "...truncated due to large size"
            
        return {
            "stdout": stdout,
            "stderr": stderr,
            "return_code": proc.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "return_code": -1
        }