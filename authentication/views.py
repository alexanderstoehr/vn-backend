# authentication/views.py
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.user_profile.models import UserProfile
from .authentication import ClerkAuthentication

User = get_user_model()

class SyncUserView(APIView):
    """
    Syncs Clerk user data to BasicUser + UserProfile.
    - Creates or updates BasicUser (email, username)
    - Links Clerk ID to UserProfile
    """
    authentication_classes = [ClerkAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Extract Clerk data from request.auth (provided by ClerkAuthentication)
        user_data = request.auth
        external_user_id = user_data.get('sub')
        email = user_data.get('email_address')
        username = user_data.get('username') or f'user_{external_user_id[:8]}'

        # Check if UserProfile exists for this Clerk ID
        profile = UserProfile.objects.filter(external_user_id=external_user_id).first()

        if profile:
            # Update email and username if they have changed
            user = profile.user
            updated = False
            if user.email != email:
                user.email = email
                updated = True
            if user.username != username:
                user.username = username
                updated = True
            if updated:
                user.save()
            return Response({'message': 'User already synced', 'created': False})

        # If no profile exists, create a new BasicUser and UserProfile
        user = User.objects.create_user(username=username, email=email)
        UserProfile.objects.create(user=user, external_user_id=external_user_id)

        return Response({'message': 'User synced successfully', 'created': True})