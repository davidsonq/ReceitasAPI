from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializerrS

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer