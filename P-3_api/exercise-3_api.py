import requests

apiKey = "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"
url = "https://openrouter.ai/api/v1/chat/completions"


headers = {
    "Authorization": f"Bearer {apiKey}",
    "Content-Type": "application/json"
}

while True:
    userInput = input("Hi, what do you want? ").strip()
    if userInput.lower() == "exit":
        print("bye")
        break
    if not userInput:
        continue

    data = {
        "model": "openai/gpt-oss-20b:free",
        "messages": [{"role": "user", "content": userInput}]
    }

    response = requests.post(url, headers=headers, json=data)

    print("Status code:", response.status_code)
    print("Raw response:", response.text)

    if response.status_code == 200:
        try:
            reply = response.json()["choices"][0]["message"]["content"]
            print(f"AI: {reply}\n")
        except Exception as e:
            print("JSON parse error:", e)
    else:
        print(f"Error {response.status_code}: {response.text}")