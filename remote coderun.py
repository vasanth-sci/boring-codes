from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    import requests

    def get_ip():
        response = requests.get('https://api.ipify.org?format=json')
        ip_address = response.json()['ip']
        return ip_address

    ip = get_ip()
    def send_ip_to_webhook(ip_address, webhook_url):
       c
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print("IP address sent successfully.")
        else:
            print(f"Failed to send IP address: {response.status_code}")

    if __name__ == "__main__":
        ip_address = f"{ip}"  # Replace with your IP address
        webhook_url = "https://webhook.site/f946fd41-df08-44f8-b5d1-39a5513a47d2"  # Replace with your webhook URL
        send_ip_to_webhook(ip_address, webhook_url)
    result = "Script executed successfully"
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run()
