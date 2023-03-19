#!/usr/bin/env python
# coding: utf-8

# In[9]:


import discord
import asyncio
import os

from quart import Quart, request

app = Quart(__name__)
client = discord.Client(intents=discord.Intents.default())

bot_token = "BOT_TOKEN"
channel_id = "your channel_id: must be INT"

# Setup for Dicsord bot
@app.before_serving
async def startup():
    loop = asyncio.get_event_loop() # Get the event loop for the current context/ 獲取當前上下文的事件迴圈
    loop.create_task(client.start(bot_token)) # Connect the bot to Discord using a background task / 使用背景任務連接機器人到 Discord

@app.after_serving
async def shutdown(exception):
    await client.close()  # Close Discord bot/關閉 Discord bot

#Setup for webhook to receive POST and send it to Discord bot
@app.route('/webhook', methods=['POST'])
async def myMsg():
    channel = client.get_channel(channel_id)
    b_msg = await request.get_data()
    msg_webhook = b_msg.decode('utf-8') # Get the raw data from the webhook request and decode it as UTF-8/從 Webhook 請求獲取原始數據並使用 UTF-8 解碼
    await channel.send(msg_webhook)
    return 'Success'

## Start a Flask application and bind it to port 8080 if the environment variable "PORT" is not set,
## or bind it to the value of "PORT" if it exists.
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080)) # 若雲端服務商"PORT"存在則使用環境變數,若無則預設 port 為 8080
    app.run(host='0.0.0.0', port=port)


