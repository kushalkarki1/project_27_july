from django.urls import path
from chat.views import user_chat, message

app_name = "chat"

urlpatterns = [
    path("chat/", message, name="user_list"),
    path("chat/<str:username>/", user_chat, name="message"),
]