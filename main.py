#
#   ██╗░░░░░██╗████████╗███████╗░░░░░░
#   ██║░░░░░██║╚══██╔══╝██╔════╝░░░░░░
#   ██║░░░░░██║░░░██║░░░█████╗░░░░░░░░
#   ██║░░░░░██║░░░██║░░░██╔══╝░░░░░░░░
#   ███████╗██║░░░██║░░░███████╗██╗██╗
#   ╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═╝
#
#              © Copyright 2022
#
#          https://t.me/litecodes
#
#         Licensed under the GNU GPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html

from aiogram import Bot, types, Dispatcher, executor
token = "токен твоего бота"
bot = Bot(token=token)
dp = Dispatcher(bot=bot)

@dp.chat_join_request_handler()
async def start1(req: types.ChatJoinRequest):
    try:
        await req.approve()
        await bot.promote_chat_member(chat_id=req.chat.id, user_id=req.from_user.id, can_post_messages=True)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
