from persistent_messages import notify
from persistent_messages import constants
from django.contrib.messages.storage.base import BaseStorage


def add_message(request, level, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None, storage=None):
    """
    """
    if email:
        notify.email(level, message, extra_tags, subject, user, from_user)

    if storage is None:
        storage = request._messages

    assert isinstance(storage, BaseStorage), "Incompatible message storage type."

    return storage.add(level, message, extra_tags, subject, user, from_user, expires, close_timeout)


def info(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.INFO
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)


def warning(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.WARNING
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)


def success(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.SUCCESS
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)


def error(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.ERROR
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)


def debug(request, message, extra_tags='', fail_silently=False, subject='', user=None, email=False, from_user=None, expires=None, close_timeout=None):
    """
    """
    level = constants.DEBUG
    return add_message(request, level, message, extra_tags, fail_silently, subject, user, email, from_user, expires, close_timeout)
