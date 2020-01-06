import os
import vk_api
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

VK_LOGIN = os.getenv("VK_LOGIN")
VK_PASSWORD = os.getenv("VK_PASSWORD")

vk = None

try:
    vk_session = vk_api.VkApi(VK_LOGIN, VK_PASSWORD)
    vk_session.auth()
    vk = vk_session.get_api()
except Exception as e:
    print("Cannot authorize")

# vk api intance

def groups():
  global vk
  return vk.groups.get()

def get_friends(user_id):
    global vk
    return vk.friends.get(user_id=user_id)
