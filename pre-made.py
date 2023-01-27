import qrcode

def printqr(ele,name):
    data = ele
    img = qrcode.make(data)
    img.save(name + '.png')

def question():
    awns = input('Do You Want To Restart Yes Or No:')
    if awns == 'yes':
        qrmaker()
    if awns == 'no': 
        print('Goodbye!')
        exit()
def qrmaker():
    nm = input('What would be in the qr code:')
    nmfl = input('What would be the name of the file:')
    printqr(nm,nmfl)
    question()

qrmaker()