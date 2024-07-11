import os
import requests

def download_serveo():
    print("Downloading Serveo...")
    url = "https://serveo.net/download"
    response = requests.get(url, stream=True)
    with open("serveo.zip", "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    print("Serveo downloaded successfully!")

def configure_authtoken():
    print("Configuring Auth Token...")
    authtoken = input("Enter your Auth Token: ")
    with open("serveo.conf", "w") as f:
        f.write(f"authtoken={authtoken}\n")
    print("Auth Token configured successfully!")

def host_port():
    print("Hosting Port...")
    port = input("Enter the port number: ")
    os.system(f"serveo --port {port}")
    print("Port hosted successfully!")

def main():
    print("Serveo Wizard")
    print("------------")
    print("1. Download Serveo")
    print("2. Configure Auth Token")
    print("3. Host Port")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            download_serveo()
        elif choice == "2":
            configure_authtoken()
        elif choice == "3":
            host_port()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
