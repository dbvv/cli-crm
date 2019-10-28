import os
import vk_api
from dotenv import load_dotenv

# load envitoment variables
load_dotenv()

VK_LOGIN = os.getenv("VK_LOGIN")

print(VK_LOGIN)