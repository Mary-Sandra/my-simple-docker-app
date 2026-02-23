<<<<<<< HEAD
print("Hello from Docker!")
=======
import requests
import json
import sys

def fetch_and_process_data(url):
    try:
        # 1. Network Communication: Send a GET request with a timeout
        print(f"Connecting to: {url}...")
        response = requests.get(url, timeout=10)
        
        # 2. Error Handling: Check for HTTP errors (4xx or 5xx)
        response.raise_for_status()
        
        # 3. Data Processing: Parse JSON response into a Python dictionary
        # The built-in .json() method decodes the JSON string
        data = response.json()
        
        # Example processing: Extract specific fields
        processed_data = {
            "id": data.get("id"),
            "title": data.get("title").upper(),
            "completed": data.get("completed")
        }
        
        print("Data processed successfully:")
        print(json.dumps(processed_data, indent=4))
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Network error: Failed to connect to the server. Check your internet.")
    except requests.exceptions.Timeout:
        print("Timeout error: The request took too long.")
    except json.JSONDecodeError:
        print("Error: Failed to decode the JSON response.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    # URL to fetch a sample 'To Do' item
    TARGET_URL = "https://jsonplaceholder.typicode.com/todos/1"
    fetch_and_process_data(TARGET_URL)
 
