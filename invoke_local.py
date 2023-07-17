from dotenv import load_dotenv
load_dotenv()
from src.dynamo import insert_item,item_in_table
from src.bot import send_message


send_message({},{})

# print(item_in_table({
#     "id":  "abc123",
#     'name': 'song',
#     'artist': 'artist',
#     'url': 'test.com'

# }))
