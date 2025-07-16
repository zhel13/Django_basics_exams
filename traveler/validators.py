from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NicknameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or 'Your nickname is invalid!'


    def __call__(self, value):
        if not value.isalnum():
            raise ValidationError(self.message)


