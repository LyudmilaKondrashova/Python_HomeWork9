from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
from spy import *

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - Приветствие\n')
    await update.message.reply_text(f'/time - Текущая дата и время\n')
    await update.message.reply_text(f'/help - Вызов справки\n')
    await update.message.reply_text(f'/sum - Сложение двух целых чисел\n')
    await update.message.reply_text(f'/diff - Разность двух целых чисел\n')
    await update.message.reply_text(f'/mult - Произведение двух целых чисел\n')
    await update.message.reply_text(f'/div - Частное двух целых чисел\n')
    await update.message.reply_text(f'/sumc - Сумма двух комплексных чисел\n')
    await update.message.reply_text(f'/diffc - Разность двух комплексных чисел\n')
    await update.message.reply_text(f'/multc - Произведение двух комплексных чисел\n')
    await update.message.reply_text(f'Для комплексных чисел нужно ввести 4 числа через пробел:\n')
    await update.message.reply_text(f'X1 Y1 X2 Y2 - числа вида X1+Y1i   X2+Y2i\n')
    
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{time.asctime()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/sum 10 45
    x = int(items[1])
    y = int(items[2])
    if y > 0: znak ='+'
    else: znak ='-'
    await update.message.reply_text(f'{x} {znak} {abs(y)} = {x+y}')

async def division_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/diff 10 45
    x = int(items[1])
    y = int(items[2])
    if y == 0: await update.message.reply_text('Делить на ноль нельзя!')
    else: await update.message.reply_text(f'{x} : {y} = {x/y}')

async def multy_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/mult 10 45
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x*y}')

async def diff_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/diff 10 45
    x = int(items[1])
    y = int(items[2])
    if y > 0: znak ='-'
    else: znak ='+'
    await update.message.reply_text(f'{x} {znak} {abs(y)} = {x-y}')

async def sum_compl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/sumc X1 Y1 X2 Y2 - НУЖНО ВВЕСТИ 4 ЧИСЛА ЧЕРЕЗ ПРОБЕЛ
                         #X1+Y1i   X2+Y2i 
    x1 = int(items[1])
    y1 = int(items[2])
    x2 = int(items[3])
    y2 = int(items[4])
    x = x1 + x2
    y = y1 + y2
    if y1 > 0: znaky1 = '+'
    else: znaky1 = '-'
    if x2 > 0: znakx2 = '+'
    else: znakx2 = '-'
    if y2 > 0: znaky2 = '+'
    else: znaky2 = '-'
    if y > 0: znaky = '+'
    else: znaky = '-'
    await update.message.reply_text(f'{x1} {znaky1}{abs(y1)}i {znakx2}{abs(x2)} {znaky2}{abs(y2)}i = {x} {znaky}{abs(y)}i')

async def diff_compl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/diffc X1 Y1 X2 Y2 - НУЖНО ВВЕСТИ 4 ЧИСЛА ЧЕРЕЗ ПРОБЕЛ
                         #X1+Y1i   X2+Y2i
    x1 = int(items[1])
    y1 = int(items[2])
    x2 = int(items[3])
    y2 = int(items[4])
    x = x1 - x2
    y = y1 - y2
    if y1 > 0: znaky1 = '+'
    else: znaky1 = '-'
    if x2 > 0: znakx2 = '-'
    else: znakx2 = '+'
    if y2 > 0: znaky2 = '-'
    else: znaky2 = '+'
    if y > 0: znaky = '+'
    else: znaky = '-'
    await update.message.reply_text(f'{x1} {znaky1}{abs(y1)}i {znakx2}{abs(x2)} {znaky2}{abs(y2)}i = {x} {znaky}{abs(y)}i')

async def multy_compl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  #/multc X1 Y1 X2 Y2 - НУЖНО ВВЕСТИ 4 ЧИСЛА ЧЕРЕЗ ПРОБЕЛ
                         #X1+Y1i   X2+Y2i
    x1 = int(items[1])
    y1 = int(items[2])
    x2 = int(items[3])
    y2 = int(items[4])
    x = x1 * x2 - y1 * y2
    y = x1 * y2 + x2 * y1
    if y1 > 0: znaky1 = '+'
    else: znaky1 = '-'
    if y2 > 0: znaky2 = '+'
    else: znaky2 = '-'
    if y > 0: znaky = '+'
    else: znaky = '-'
    await update.message.reply_text(f'({x1} {znaky1}{abs(y1)}i) * ({x2} {znaky2}{abs(y2)}i) = {x} {znaky}{abs(y)}i')