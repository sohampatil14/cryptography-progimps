import random

# value of p and g know to both users
p = random.randint(1, 1000)
g = p
while p == g:
    g = random.randint(1, p-1)

value_send_sender = 0
value_send_receiver = 0

print('\n\nValues of p generated : ', p)
print('Values of g generated : ', g)


class sender:
    x = random.randint(1, p-1)  # 3
    sender_key = 0

    def comp_mod(self):
        global p
        global g
        global value_send_sender
        global value_send_receiver
        if value_send_sender == 0:
            value_send_sender = (g**self.x) % p
            print('\nAlice : Value of R1 sent by Alice :',
                  value_send_sender)
        else:
            self.sender_key = (value_send_receiver**self.x) % p
            print('\nAlice : Value of R2 received by Alice :',
                  value_send_receiver)
        return


class receiver:
    y = random.randint(1, p-1)  # 3
    receiver_key = 0

    def comp_mod(self):
        global p
        global g
        global value_send_sender
        global value_send_receiver
        if value_send_receiver == 0:
            value_send_receiver = (g**self.y) % p
            print('\nBob : Value of R2 sent by Bob :',
                  value_send_receiver)
        else:
            self.receiver_key = (value_send_sender**self.y) % p
            print('\nBob : Value of R1 received by Bob :',
                  value_send_sender)
        return


send = sender()
receive = receiver()

send.comp_mod()
receive.comp_mod()
send.comp_mod()
receive.comp_mod()

if send.sender_key == receive.receiver_key:
    print("\n\nKKey Sucessfully Generated")

print('\nKey generated K1 by Alice : ', send.sender_key)
print('Key generated K2 by Bob : ', receive.receiver_key)
