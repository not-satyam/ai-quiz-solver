import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:7860"
# TODO: Replace these with your actual credentials from .env file
EMAIL = "your.email@example.com"  # Replace with your actual email
SECRET = "your_secret_string"     # Replace with your actual secret

# Quiz URLs to test
quiz_urls = [
    "https://tds-llm-analysis.s-anand.net/demo",
    "https://tds-llm-analysis.s-anand.net/demo2", 
    "https://tdsbasictest.vercel.app/quiz/1",
    "https://p2testingone.vercel.app/q1.html"
]

def send_quiz_request(url):
    """Send a quiz solving request to the server"""
    payload = {
        "email": EMAIL,
        "secret": SECRET,
        "url": url
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/solve",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )
        
        print(f"URL: {url}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        print("-" * 50)
        
        return response.status_code == 200
        
    except requests.exceptions.RequestException as e:
        print(f"Error sending request for {url}: {e}")
        return False

def main():
    print("Testing LLM Analysis Quiz Solver")
    print("=" * 50)
    
    # Test server health first
    try:
        health = requests.get(f"{BASE_URL}/healthz", timeout=10)
        print(f"Server health: {health.json()}")
        print("-" * 50)
    except:
        print("Server not responding! Make sure it's running on localhost:7860")
        return
    
    # Send requests for each quiz
    for i, url in enumerate(quiz_urls, 1):
        print(f"Request {i}/4:")
        success = send_quiz_request(url)
        
        if success:
            print("✅ Request sent successfully!")
        else:
            print("❌ Request failed!")
        
        # Wait between requests to avoid overwhelming the server
        if i < len(quiz_urls):
            print("Waiting 5 seconds before next request...")
            time.sleep(5)
    
    print("\nAll requests completed!")
    print("Check your server logs to see the agent's progress.")

if __name__ == "__main__":
    main()