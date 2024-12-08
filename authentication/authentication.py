# authentication/authentication.py
import os
from clerk_backend_api import Clerk
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from apps.user_profile.models import UserProfile

from authentication.exceptions import TokenExpiredError, InvalidTokenError
import logging

logger = logging.getLogger(__name__)




clerk_client = Clerk()
clerk_client.api_key = os.environ.get('CLERK_API_KEY')
clerk_client.secret_key = os.environ.get('CLERK_SECRET_KEY')

# Log the keys for debugging
logger.info(f"CLERK_API_KEY: {clerk_client.api_key}, CLERK_SECRET_KEY: {clerk_client.secret_key}")

class ClerkAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Extract Clerk token from request headers
        clerk_token = request.headers.get('Authorization')
        if not clerk_token:
            return None

        # Validate the Clerk token and extract user data
        user_data = self.validate_clerk_token(clerk_token)
        if not user_data:
            raise AuthenticationFailed('Invalid Clerk token')

        # Get or create the user profile
        external_user_id = user_data.get('sub')
        profile, created = UserProfile.objects.get_or_create(external_user_id=external_user_id)

        # Return the user and token
        return (profile.user, clerk_token)

    def validate_clerk_token(self, token):
        try:
            user_data = clerk_client.tokens.verify(token)
            return user_data

        except TokenExpiredError:
            logger.error("Token validation failed: Token is expired")
            raise AuthenticationFailed('Invalid Clerk token: Token is expired')
        except InvalidTokenError:
            logger.error("Token validation failed: Token is invalid")
            raise AuthenticationFailed('Invalid Clerk token: Token is invalid')
        except Exception as e:
            logger.error(f"Token validation failed: {e}")
            raise AuthenticationFailed('Invalid Clerk token: Token validation failed')