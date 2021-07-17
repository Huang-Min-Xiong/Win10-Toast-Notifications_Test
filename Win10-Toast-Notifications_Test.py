import time
from win10toast import ToastNotifier

Notifier = ToastNotifier()
Notifier.show_toast("Notifier1",
                    "Hello World!",
                   icon_path = "./img.ico",
                   duration = 5)

Notifier.show_toast("Notifier2",
                    "This notification use thread!",
                   icon_path = "./img.ico",
                   duration = 5,
                   threaded = True)

while Notifier.notification_active(): 
    time.sleep(0.1)