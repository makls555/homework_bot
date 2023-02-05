class NoResponseError(Exception):
    """Вызывается если status_code != 200."""


class ParseMissStatusError(Exception):
    """Вызывается при недокументированном статусе домашней работы."""


class ListKeyError(Exception):
    """Неверный ключ словаря."""


class NotaListError(Exception):
    """Не является списком."""


class SendMessageError(Exception):
    """Ошибка при отправке сообщения."""

class JsonError(Exception):
    """Исключение для ошибок при соединении с енд-поинт"""
