import os
import vk_api
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

VK_LOGIN = os.getenv("VK_LOGIN")
VK_PASSWORD = os.getenv("VK_PASSWORD")

vk_session = vk_api.VkApi(VK_LOGIN, VK_PASSWORD)
vk_session.auth()

# vk api intance
vk = vk_session.get_api()


def groups():
  global vk
  return vk.groups.get()