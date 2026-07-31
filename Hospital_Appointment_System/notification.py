from abc import ABC, abstractmethod

class NotificationChannel(ABC):

    @abstractmethod
    def send(self, message):
        pass


class SMSNotifier(NotificationChannel):

    def send(self, message):
        print("SMS:", message)


class EmailNotifier(NotificationChannel):

    def send(self, message):
        print("EMAIL:", message)


class MockNotifier(NotificationChannel):

    def send(self, message):
        print("MOCK:", message)
