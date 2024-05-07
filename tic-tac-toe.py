#MEKNI Salim le 08/09/2021
from tkinter import *
import tkinter.messagebox as msg

root= Tk()
root.title('MEKNI-EILCO')
# Étiquettes
Label(root,text="Joueur 1 : X",font="times 15").grid(row=0,column=1)
Label(root,text="Joueur 2 : O",font="times 15").grid(row=0,column=2)

digits = [1,2,3,4,5,6,7,8,9]

# Pour le joueur 1, le signe est X et pour le joueur 2, le signe est O
mark = ''

# Comptage du nombre de clics
count = 0

panels = ["panel"]*10

def win(panels,sign):
    return ((panels[1] == panels[2] == panels [3] == sign)
            or (panels[1] == panels[4] == panels [7] == sign)
            or (panels[1] == panels[5] == panels [9] == sign)
            or (panels[2] == panels[5] == panels [8] == sign)
            or (panels[3] == panels[6] == panels [9] == sign)
            or (panels[3] == panels[5] == panels [7] == sign)
            or (panels[4] == panels[5] == panels [6] == sign) 
            or (panels[7] == panels[8] == panels [9] == sign))

def checker(digit):
    global count, mark, digits

    # Vérifier quel bouton a été cliqué 
    if digit==1 and digit in digits:
        digits.remove(digit)
## Le joueur 1 jouera si la valeur de count est paire, sinon le joueur 2 jouera
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark

        button1.config(text = mark)
        count = count+1
        sign = mark

        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Résultat","Le Joueur 1 gagne")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Résultat","Le Joueur 2 gagne")
            root.destroy()

    # Les blocs if suivants pour les autres boutons sont similaires au premier bloc if.

    if digit==2 and digit in digits:
        digits.remove(digit)

        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark

        button2.config(text = mark)
        count = count+1
        sign = mark

        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Résultat","Le Joueur 1 gagne")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Résultat","Le Joueur 2 gagne")
            root.destroy()

    # Les blocs if suivants pour les autres boutons sont similaires au premier bloc if.
    
    # Si count est supérieur à 8, alors le match est nul
    if(count>8 and win(panels,'X')==False and win(panels,'O')==False):
        msg.showinfo("Résultat","Match nul")
        root.destroy()

#### Définir les boutons
button1=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(1))
button1.grid(row=1,column=1)
button2=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda:checker(2))
button2.grid(row=1,column=2)
button3=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(3))
button3.grid(row=1,column=3)
button4=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(4))
button4.grid(row=2,column=1)
button5=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(5))
button5.grid(row=2,column=2)
button6=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(6))
button6.grid(row=2,column=3)
button7=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(7))
button7.grid(row=3,column=1)
button8=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(8))
button8.grid(row=3,column=2)
button9=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(9))
button9.grid(row=3,column=3)

root.mainloop()
