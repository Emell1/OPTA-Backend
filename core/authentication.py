from time import sleep
from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed


def is_token_expired(token):
    min_age = timezone.now() - timedelta(
        seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS)
    expired = token.created < min_age
    return expired


class ExpiringTokenAuthentication(TokenAuthentication):
    """ Token authentication with expiration
    """
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

        if not token.user.is_active:
            raise AuthenticationFailed("User inactive or deleted")

        expired = is_token_expired(token)
        if expired:
            
            # Delete all user tokens
            Token.objects.filter(user=token.user).delete()
            sleep(1)
            Token.objects.create(user=token.user)
            raise AuthenticationFailed("Token has expired")

        return (token.user, token)