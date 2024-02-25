from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, video_title):
        pass


class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, video_title):
        print(
            f"{self.name} receive a notification: New Video uploaded - '{video_title}'")


class YoutubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self, vide_title):
        for subscriber in self.subscribers:
            subscriber.update(vide_title)

    def upload_video(self, video_title):
        print(f"uploading video: '{video_title}'")
        self.notify_subscribers(video_title)


channel = YoutubeChannel()

subcriber1 = Subscriber("Jhon")
subcriber2 = Subscriber("alice")

channel.subscribe(subcriber1)
channel.subscribe(subcriber2)

video_title = ["Cat v Dogs", "Py Tutor", "Coock Pasta"]

for title in video_title:
    channel.upload_video(title)

channel.unsubscriber(subcriber1)

channel.upload_video("New Vide for Subscriber")
