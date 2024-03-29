from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):

        #request.user.id
        #Me trae los datos del usuario, me devuelve todos los datos del usuario que esta realizando esa peticion
        user = User.objects.get(id=request.user.id)

        #serializador que va a modificar los datos
        serializer = UserUpdateSerializer(user, request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
