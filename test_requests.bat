@echo off
echo Testing LLM Analysis Quiz Solver...

echo.
echo 1. Testing demo quiz...
curl -X POST http://localhost:7860/solve ^
  -H "Content-Type: application/json" ^
  -d "{\"email\": \"your.email@example.com\", \"secret\": \"your_secret_string\", \"url\": \"https://tds-llm-analysis.s-anand.net/demo\"}"

echo.
echo 2. Testing demo2 quiz...
curl -X POST http://localhost:7860/solve ^
  -H "Content-Type: application/json" ^
  -d "{\"email\": \"your.email@example.com\", \"secret\": \"your_secret_string\", \"url\": \"https://tds-llm-analysis.s-anand.net/demo2\"}"

echo.
echo 3. Testing basic test quiz...
curl -X POST http://localhost:7860/solve ^
  -H "Content-Type: application/json" ^
  -d "{\"email\": \"your.email@example.com\", \"secret\": \"your_secret_string\", \"url\": \"https://tdsbasictest.vercel.app/quiz/1\"}"

echo.
echo 4. Testing p2 quiz...
curl -X POST http://localhost:7860/solve ^
  -H "Content-Type: application/json" ^
  -d "{\"email\": \"your.email@example.com\", \"secret\": \"your_secret_string\", \"url\": \"https://p2testingone.vercel.app/q1.html\"}"

echo.
echo All requests sent! Check server logs for progress.
pause