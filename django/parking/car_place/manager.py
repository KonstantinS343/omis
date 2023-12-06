from django.contrib.auth.models import User


class UserDAL:
    def get(self, user_id: int):
        return User.objects.get(id=user_id)

    def create(self, username: str, password: str):
        user = User.objects.create_user(username=username, password=password)
        user.save()

    def delete(self, user_id):
        User.objects.delete(id=user_id)
