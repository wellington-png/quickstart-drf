from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from quickstart.serializers import UserSerializer, GroupSerializer, LeadSerializer
from quickstart.models import Lead


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def list(self, request, *args, **kwargs):
        if request.query_params.get("hub.verify_token", "") == "5d6b2c04-8147-47b4-b64b-659cf4263487":
            print("Verified")
            return Response(int(request.query_params.get("hub.challenge", 0)), status=HTTP_200_OK)
        return Response({"success": False},status=HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        print("Create")
        return Response({"success": True},status=HTTP_200_OK)
