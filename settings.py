import os
import dotenv
# with open('.env','r') as file:
#     line = (file.readline())
#     try:
#         os.environ[line[:line.find("=")]] = line[line.find("=") +1:]
#     except ValueError:
#         print("wrong value")

dotenv.load_dotenv('.env')
bot_key = os.environ['bot_key']