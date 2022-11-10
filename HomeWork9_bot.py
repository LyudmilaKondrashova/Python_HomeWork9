from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token('5200198370:AAEyoAAviKa3xVTe6b-z-Cg80zFYZ1wDw88').build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))  #Сумма целых чисел
app.add_handler(CommandHandler("diff", diff_command))  #Разность целых чисел
app.add_handler(CommandHandler("mult", multy_command))  #Произведение целых чисел
app.add_handler(CommandHandler("div", division_command))  #Частное целых чисел
app.add_handler(CommandHandler("sumc", sum_compl_command)) #Сумма комплексных чисел
app.add_handler(CommandHandler("diffc", diff_compl_command)) #Разность комплексных чисел
app.add_handler(CommandHandler("multc", multy_compl_command)) #Умножение комплексных чисел

print('server start')

app.run_polling()
