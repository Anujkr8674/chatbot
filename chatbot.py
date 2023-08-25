from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#pip from GoldCorpus import 

bot=ChatBot("Your ChatBot")

conv=[
    # Whatever user wants question and answer are add in this section between the brackets.
    'hii',
    'hi Anuj',
    'hello',
    'hello anuj',
    'good morning',
    'good morning anuj (:',
    'how are you?',
    'i am good',
    'in which city do you live',
    'ranchi'

]
trainer=ListTrainer(bot)

#training the bot
trainer.train(conv)

#answer=bot.get_response("what is your name")
#print(answer)

#while True:
#    query=input()
#   if query=='exit':
#        break
#    answer=bot.get_response(query)
#    print("Bot :",answer)

root=Tk()
def askbot():
    query=e.get()
    botans=bot.get_response(query)
    msgs.insert(END," You  :  "+query)
    print(type(botans))
    msgs.insert(END," Stella  :  "+str(botans))
    e.delete(0,END)
    msgs.yview(END)

root.geometry("480x680+420+10")
root.maxsize(480,680)
root.minsize(480,680)
root.title("ChatBot")
root.configure(background="#EAF0F1")
ti=Label(root,text="<---------------I am your Chat-Bot--------------->",fg="#2F363F",bg="#EAF0F1",font="Candara 22 bold",width="20")
ti.pack(fill="x")
img=PhotoImage(file="bot3.png")
pl=Label(root,image=img).pack()
frame=Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=15,font="candara 14 bold",yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH)
frame.pack()
l1=Label(root,text="Enter your Question ?",font="candara 15 bold",fg="#2F363F")
l1.pack()
e=Entry(root,font="consolas 18 normal",fg="#ff0606")
e.pack(pady="5",fill="x",ipady="5")
btn=Button(root,text="Ask-Bot",font="Candara 15 bold",bg="#c74747",fg="#fff",relief=GROOVE,width=35,command=askbot)
btn.pack(pady="20")

def enter_function(event):
    btn.invoke()
root.bind('<Return>',enter_function)

root.mainloop()
