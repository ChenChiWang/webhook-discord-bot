# Webhook Discord Bot

This is a Python bot using the Discord API to receive webhook POST requests and send them to a designated channel on a Discord server.

## Features

- Receive POST requests through a webhook and send them to Discord.
- Specify the Discord channel to send the message to.
- Easy setup and deployment.

## Usage

1. Clone the repository to your local machine.
2. Create a Discord bot and get the bot token and the channel ID.
3. Edit the `bot_token` and `channel_id` variables in the `webhook-discord-bot.py` file to match your own bot token and channel ID.
4. Install the required Python packages: `discord.py` and `quart`.
5. Run the application by executing the `webhook-discord-bot.py` file: `python webhook-discord-bot.py`.
6. Create a webhook and set the URL to `http://{your-server-address}/webhook`.
7. Send a POST request to the webhook URL to see the message appear in the designated Discord channel.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


# Webhook Discord Bot

這是一個使用 Discord API 的 Python 機器人，用於接收 Webhook POST 請求並將其發送到 Discord 伺服器上的指定頻道。

## 功能

- 透過 Webhook 接收 POST 請求並將其發送到 Discord。
- 指定要發送消息的 Discord 頻道。
- 簡單易用的設置和部署。

## 使用方法

1. 將存儲庫複製到本地計算機上。
2. 創建 Discord 機器人，獲取機器人令牌和頻道 ID。
3. 在 `webhook-discord-bot.py` 文件中編輯 `bot_token` 和 `channel_id` 變數，以匹配您自己的機器人令牌和頻道 ID。
4. 安裝所需的 Python 套件：`discord.py` 和 `quart`。
5. 通過執行 `webhook-discord-bot.py` 文件運行應用程序：`python webhook-discord-bot.py`。
6. 創建 Webhook，將 URL 設置為 `http://{your-server-address}/webhook`。
7. 發送 POST 請求到 Webhook URL，即可在指定的 Discord 頻道中看到消息。

## 授權

本項目基於 MIT 授權許可 - 詳細信息請參閱 LICENSE 文件。