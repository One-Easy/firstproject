from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname', 'location', 'univesity']
        # university를 처음부터 오타내고 migrate 해버려서 일단 이렇게 적었습니다ㅠ