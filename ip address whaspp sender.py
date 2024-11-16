import pywhatkit as pwk
import requests

# Function to get the IP address
def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']
    return ip_address

# Function to send WhatsApp message
def send_whatsapp_message(phone_number, message):
    pwk.sendwhatmsg_instantly(phone_number, message)

# Main function
if __name__ == "__main__":
    ip_address = get_ip()
    message = f"Host IP Address: {ip_address}"
    phone_number = "+91XXXXXXXXXX"  # Replace with the recipient's phone number

    send_whatsapp_message(phone_number, message)
    print("Message sent successfully!")
