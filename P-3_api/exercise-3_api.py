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
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [{"role": "user", "content": userInput}]
    }

    response = requests.post(url, headers=headers, json=data)

    # if response.status_code == 200:
    #     reply = response.json()["choices"][0]["message"]["content"]
    #     print(f"AI: {reply}\n")
    # else:
    #     print(f"Error {response.status_code}: {response.text}")
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