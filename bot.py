from telethon import TelegramClient
import asyncio

# Your API ID and hash from my.telegram.org
api_id = '25945751'
api_hash = 'd1ae20497e05bcf0d50711d147733d9d'
phone_number = '+6289691982090'  # Your phone number with country code

# List of recipients (usernames or chat IDs)
usernames = ['@xJonat']

# The messages you want to send
messages = [
    "Hello! This is the first automated message.",
    "Hello again! This is the second automated message."
]

# Function to send messages
async def send_daily_message():
    client = TelegramClient(phone_number, api_id, api_hash)
    await client.start()
    
    for username in usernames:
        try:
            # Get the user entity
            entity = await client.get_entity(username)
            
            # Send the first and second message
            for message in messages:
                await client.send_message(entity, message)
                print(f"Message sent to {username}: {message}")
        except Exception as e:
            print(f"Failed to send message to {username}: {e}")

    await client.disconnect()

# Run the function
if __name__ == "__main__":
    asyncio.run(send_daily_message())
