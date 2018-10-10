#-----------------------------------------------------------------------------
# Name:        Discord Cyberbullying Bot
# Purpose:     To provide a streamlined process removing cyberbullying from
#              discord using a variety of techniques
#
# Author:      QiLin
# Created:     31-Sep-2018
# Updated:     01-Oct-2018
#-----------------------------------------------------------------------------

# pylint: disable=W0614

# File Setup
from botSetup import *

TOKEN = os.getenv('TOKEN')

# Module Imports
from server import extractProblem

# -------------------------------
# ------- Intialization ---------
# -------------------------------

print("Starting up...") # Notify file was run

# Notify if Bot was setup correctly
@client.event
async def on_ready():
    print("Bot is online")

# -------------------------------
# -------- Functions ------------
# -------------------------------

@client.event
async def on_message(message):
    # -------------------------------
    # ---------- Setup --------------
    # -------------------------------

    inputText = message.content # The Message Sent (str)

    # -------------------------------
    # -------- Fun Things -----------
    # -------------------------------

    if inputText == ("!help"):
        await client.send_message(message.channel, "Type in !aops problem [year] [contest] [form] [problem]")

    elif inputText.startswith("!aops problem") and inputText.count(' ') > 4:
        args = inputText.split(" ")
        # try:
        year = args[2]
        contest = args[3]
        form = args[4]
        problem = args[5]
        if form == "none":
            form = ""
        problemText = extractProblem.extractProblem(year,contest,form,problem)
        url = 'http://artofproblemsolving.com/wiki/index.php?title=%s_%s_%s_Problems/Problem_%s' % (year, contest, form, problem)
        
        await client.send_message(message.channel, "Problem: %s " % (problemText))
        await client.send_message(message.channel, "Problem %s from the %s %s %s contest" % (problem,year,contest,form))
        await client.send_message(message.channel, "Url is: %s" % url)

        # except Exception:
        #     print(str(Exception))
        #     await client.send_message(message.channel, "Type in !problem [year] [contest] [form] [problem]")

    elif inputText.startswith("!aops random"):
        mes = extractProblem.extractRandom()
        year = mes[0]
        contest = mes[1]
        form = mes[2]
        problem = mes[3]
        problemText = mes[4]
        url = 'http://artofproblemsolving.com/wiki/index.php?title=%s_%s_%s_Problems/Problem_%s' % (year, contest, form, problem)

        await client.send_message(message.channel, "Problem: %s " % (problemText))
        await client.send_message(message.channel, "Problem %s from the %s %s %s contest:" % (problem,year,contest,form))
        await client.send_message(message.channel, "Url is: %s" % url)

    elif message.content.startswith("!say"):
        args = inputText.split(" ")
        if len(args) > 1: await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

# Run the Bot
client.run(TOKEN)