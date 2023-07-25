from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.permissions import IsAuthenticatedAndOwnerOrEmployee
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(APIView):
    def get(self, req: Request) -> Response:
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        serializer = UserSerializer(data=req.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserByIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedAndOwnerOrEmployee]

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(req, user)

        serializer = UserSerializer(user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(req, user)

        serializer = UserSerializer(instance=user, data=req.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
