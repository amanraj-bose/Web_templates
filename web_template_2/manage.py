
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pyttsx3
import time
from plyer import notification

def activate_notification():
    notification.notify("Server", "Server has Started at {}".format(time.asctime()), app_name="School Server", app_icon="Chromatix-Aerial-Web.ico", timeout=1)
    time.sleep(1)
    engine = pyttsx3.init()
    engine.setProperty('rate', 177)
    engine.say("Activating the Server")
    engine.runAndWait()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    activate_notification()
    time.sleep(1)
    main()
