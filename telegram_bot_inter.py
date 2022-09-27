from abc import abstractmethod


class TelegramBotInterface:

    @abstractmethod
    def open_services_command(self, update, context):
        pass

    @abstractmethod
    def operating_system_command(self, update, context):
        pass

    @abstractmethod
    def vulners_command(self, update, context):
        pass
