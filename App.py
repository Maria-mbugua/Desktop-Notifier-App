import time
from plyer import notification

# Function to display a desktop notification
def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Desktop Notifier",  # Application name for the notification
        timeout=10  # Notification timeout (in seconds)
    )

# Main function
def main():
    while True:
        title = "Reminder"  # Title for the notification
        message = "It's time to take a break and stretch!"  # Message for the notification
        desktop_notifier(title, message)  # Call the notification function
        time.sleep(3600)  # Wait for the specified interval (1 hour = 3600 seconds)

if __name__ == "__main__":
    main()


