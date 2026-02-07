'''
This program requires the following modules:
- python-telegram-bot==22.5
- urllib3==2.6.2
- requests
'''
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import configparser
import logging
# 新增：导入ChatGPT并定义全局变量
from ChatGPT_HKBU import ChatGPT
gpt = None

def main():
    # 配置日志，方便查看运行状态和错误
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    # 加载配置文件中的机器人密钥
    logging.info('INIT: Loading configuration...')
    config = configparser.ConfigParser()
    config.read('config.ini')

    # 新增：初始化ChatGPT客户端
    global gpt
    gpt = ChatGPT(config)

    # 创建机器人应用实例
    logging.info('INIT: Connecting the Telegram bot...')
    app = ApplicationBuilder().token(config['TELEGRAM']['ACCESS_TOKEN']).build()

    # 注册消息处理器：只处理文本消息，排除命令
    logging.info('INIT: Registering the message handler...')
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, callback))

    # 启动机器人（轮询模式）
    logging.info('INIT: Initialization done!')
    app.run_polling()

# 替换后的回调函数
async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(response)
    logging.info("UPDATE: " + str(update))
    loading_message = await update.message.reply_text('Thinking...')

    # send the user message to the ChatGPT client
    response = gpt.submit(update.message.text)

    # send the response to the Telegram box client
    await loading_message.edit_text(response)

if __name__ == '__main__':
    main()