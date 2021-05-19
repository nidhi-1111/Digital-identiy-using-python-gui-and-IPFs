from tkinter import *
from tkinter import filedialog
import ipfshttpclient
import json
from web3 import Web3
import numpy as np
import webbrowser


try:
    ganache_url = 'http://127.0.0.1:7545'
    web3 = Web3(Web3.HTTPProvider(ganache_url))
except:
    print('Check ganache is running or not?')
    exit(0)

web3.eth.defaultAccount = web3.eth.accounts[0]

try:
    client = ipfshttpclient.Client('/dns/localhost/tcp/5001/http')
except:
    print('check ipfs client url')
    exit(0)


abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"hashOfIpfs","type":"string"},{"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"addHash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"hashOfIpfs","type":"string"},{"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"deleteHash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"destroy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"displayHash","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"hashOfIpfs","type":"string"},{"internalType":"string","name":"currentHash","type":"string"},{"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"updateHash","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress('0xAc59fe062432B323ba47D9F7677509Bf2512EB3D')
contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.addHash('adfasf', 1).call())


class StartupWindow:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        label_file_explorer = Label(self.frame,
                            text = "IPFS oprations ",
                            width = 100, height = 4,
                            fg = "blue").pack()
        self.button1 = Button(self.frame, text = 'Upload', width = 25, command = self.upload_Hash).pack()
        self.button2 = Button(self.frame, text = 'getHash', width = 25, command = self.get_Hash).pack()
        self.button3 = Button(self.frame, text = 'updateHash', width = 25, command = self.update_Hash).pack()
        self.button4 = Button(self.frame, text = 'deleteHash', width = 25, command = self.delete_Hash).pack()
        self.button5 = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).pack()
        self.frame.pack()

    def upload_Hash(self):
        self.newWindow = Toplevel(self.master)
        self.app = UploadHash(self.newWindow)

    def get_Hash(self):
        self.newWindow = Toplevel(self.master)
        self.app = GetHash(self.newWindow)
    
    def update_Hash(self):
        self.newWindow = Toplevel(self.master)
        self.app = UpdateHash(self.newWindow)
    
    def delete_Hash(self):
        self.newWindow = Toplevel(self.master)
        self.app = DeleteHash(self.newWindow)
    
    def close_windows(self):
        self.master.destroy()

# -------------------------------------------------------------------------------------------------------------------------------------------------

# addHash
class UploadHash:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.el = None
        label_file_explorer = Label(self.frame,
                            text = "IPFS upload hash   ",
                            width = 100, height = 4,
                            fg = "blue").pack()
        self.quitButton = Button(self.frame, text = 'Open', width = 25, command = self.forOpenFileandSubmit).pack()
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).pack()
        self.frame.pack()

    
    def forOpenFileandSubmit(self):
        self.filename = filedialog.askopenfilename(initialdir="/home/zero/Desktop", title="Select A File", filetypes=(("all files", "*.*"), ("jpg files", "*.jpg")))
        print(self.filename)
        self.lbl = Label(self.frame, text="Enter IPFS file number").pack()
        self.entry = Entry(self.frame, text='Enter IPFS file number1')
        self.entry.pack()
        self.btn1 = Button(self.frame, text="Submit", width = 25, command = self.myClick).pack()
        self.my_label = Label(self.frame, text=self.filename).pack()

    def myClick(self):
        try:
            self.res = client.add(self.filename)
            print(self.res['Hash'])
            self.hashVal = self.res['Hash']
            children_widgets = self.frame.winfo_children()
            for child_widget in children_widgets:
                if child_widget.winfo_class() == 'Entry':
                    self.el = child_widget.get()
            self.elment = np.uint16(self.el)
            try:
                # contract.functions.addHash(self.hashVal, int(self.elment)).transact()
                self.tx_hash = contract.functions.addHash(self.hashVal, int(self.elment)).transact()
                self.tx_receipt = web3.eth.waitForTransactionReceipt(self.tx_hash)
                print(f'transaction hash : {self.tx_hash}  transaction receipt : {self.tx_receipt}')
            except:
                print('there is transaction error line: 98')
                exit()
            self.myLabel = Label(self.frame, text=f"{self.filename} for hash value :--> {self.hashVal}").pack()
            self.myLabel = Label(self.frame, text='file sucessfully uploaded').pack()
            print('Sucsessfully uploaded')
        except:
            print('Please turn on the IPFS Daemon Process if you are using linux run startDeamon.sh')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        # self.res = client.add(self.filename)
        # print(self.res['Hash'])
        # self.hashVal = self.res['Hash']
        # children_widgets = self.frame.winfo_children()
        # for child_widget in children_widgets:
        #     if child_widget.winfo_class() == 'Entry':
        #         self.el = child_widget.get()
        #         print(child_widget.get() + ' in my click')
        # print(self.el)
        # self.elment = np.uint16(self.el)
        # self.tx_hash = contract.functions.addHash(self.hashVal, int(self.elment)).transact()
        # self.tx_receipt = web3.eth.waitForTransactionReceipt(self.tx_hash)
        # print(f'transaction hash : {self.tx_hash}  transaction receipt : {self.tx_receipt}')
        # self.myLabel = Label(self.frame, text=f"{self.filename} for hash value :--> {self.hashVal}").pack()
        # self.myLabel = Label(self.frame, text='file sucessfully uploaded').pack()
        # print('Sucsessfully uploaded')
        # print('Please turn on the IPFS Daemon Process if you are using linux run startDeamon.sh')

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def close_windows(self):
        self.master.destroy()


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# displayHash
class GetHash:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        label_file_explorer = Label(self.frame,
                            text = "IPFS get hash   ",
                            width = 100, height = 4,
                            fg = "blue").pack()
        self.quitButton = Button(self.frame, text = 'get', width = 25, command = self.get_hash_window).pack()
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).pack()
        self.frame.pack()

    def get_hash_window(self):
        label = Label(self.frame, text='Enter your file number for retriving hash : ').pack()
        self.entry = Entry(self.frame, text='Enter IPFS file number2')
        self.entry.pack()
        self.entryBtn = Button(self.frame, text='Get hash', command=self.get_hash).pack()

    def get_hash(self):
        self.elment = 0
        children_widgets = self.frame.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                self.el = child_widget.get()
                self.elment = np.uint16(self.el)
        self.hashVal = contract.functions.displayHash(int(self.elment)).call()
#        self.hashVal = 'QmVMZ2RAU7BheQzXqfVG5x2TvcjwHyxZK1nKAcoTyY6gZD'
        webbrowser.open(f'https://gateway.ipfs.io/ipfs/{self.hashVal}', new=2)
        self.myLabel = Label(self.frame, text=f'file hash sucessfully got ---> {self.hashVal}').pack()
        # self.closeBtn = Button(self.frame, text='Quit', command=self.close_windows).pack()
        print(self.hashVal)

    def close_windows(self):
        self.master.destroy()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------

# updateHash
class UpdateHash:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        label_file_explorer = Label(self.frame,
                            text = "IPFS update hash   ",
                            width = 100, height = 4,
                            fg = "blue").pack()
        self.quitButton = Button(self.frame, text = 'put old hash', width = 25, command = self.update_hash_oldHash).pack()
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).pack()
        self.frame.pack()

    def update_hash_oldHash(self):
        label = Label(self.frame, text='Enter your file old hash : ').pack()
        self.entry1 = Entry(self.frame, text='Enter IPFS old hash')
        self.entry1.pack()
        print(self.entry1.get())
        entryBtn1 = Button(self.frame, text='put new hash', command=self.update_hash_newHash).pack()

    def update_hash_newHash(self):
        label = Label(self.frame, text='Enter your file new hash : ').pack()
        self.entry2 = Entry(self.frame, text='Enter IPFS file new hash')
        self.entry2.pack()
        self.entryBtn2 = Button(self.frame, text='put hash number', command=self.update_hash_oldHashnumber).pack()

    def update_hash_oldHashnumber(self):
        label = Label(self.frame, text='Enter your file old hash number : ').pack()
        self.entry3 = Entry(self.frame, text='Enter IPFS file number3')
        self.entry3.pack()
        self.entryBtn3 = Button(self.frame, text='update value', command=self.updateValue).pack()

    def updateValue(self):
        self.lst = []
        children_widgets = self.frame.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                print(child_widget.get())
                self.lst.append(child_widget.get())
        self.oldHash = self.lst[0]
        self.newHash = self.lst[1]
        self.hashNo = np.uint16(self.lst[2])
        # try:
        #     # contract.functions.addHash(self.oldHash, self.newHash, int(self.hashNo)).transact()
        #     self.tx_hash = contract.functions.addHash(self.hashVal, int(self.elment)).transact()
        #     self.tx_receipt = web3.eth.waitForTransactionReceipt(self.tx_hash)
        #     print(f'transaction hash : {self.tx_hash}  transaction receipt : {self.tx_receipt}')
        #     self.myLabel = Label(self.frame, text='file sucessfully update').pack()
        #     print('Update sucessfully')
        # except:
        #     print('Execution revert')
        self.tx_hash = contract.functions.updateHash( self.newHash, self.oldHash, int(self.hashNo)).transact()
        self.tx_receipt = web3.eth.waitForTransactionReceipt(self.tx_hash)
        print(f'transaction hash : {self.tx_hash}  transaction receipt : {self.tx_receipt}')
        self.myLabel = Label(self.frame, text='file sucessfully update').pack()



    def close_windows(self):
        self.master.destroy()

# --------------------------------------------------------------------------------------------------------------------------------------------------------

# deleteHash
class DeleteHash:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        label_file_explorer = Label(self.frame,
                            text = "IPFS delete hash   ",
                            width = 100, height = 4,
                            fg = "blue").pack()

        self.quitButton = Button(self.frame, text = 'put hash', width = 25, command = self.getHash).pack()                            
        self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows).pack()
        self.frame.pack()


    def getHash(self):
        label = Label(self.frame, text='Enter your file hash : ').pack()
        self.entry1 = Entry(self.frame, text='Enter your IPFS file hash')
        self.entry1.pack()
        print(self.entry1.get())
        entryBtn1 = Button(self.frame, text='put hash number', command=self.getNumber).pack()
    
    def getNumber(self):
        label = Label(self.frame, text='Enter your file number : ').pack()
        self.entry1 = Entry(self.frame, text='Enter your IPFS file number')
        self.entry1.pack()
        print(self.entry1.get())
        entryBtn1 = Button(self.frame, text='Delete hash', command=self.hash_del).pack()
    
    def hash_del(self):
        self.lst = []
        children_widgets = self.frame.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                print(child_widget.get())
                self.lst.append(child_widget.get())
        self.hashVal = self.lst[0]
        self.hashNo = np.uint16(self.lst[1])
        try:
            self.tx_hash = contract.functions.deleteHash(self.hashVal, int(self.hashNo)).transact()
            self.tx_receipt = web3.eth.waitForTransactionReceipt(self.tx_hash)
            print(f'transaction hash : {self.tx_hash}  transaction receipt : {self.tx_receipt}')
            self.myLabel = Label(self.frame, text='file hash sucessfully delete').pack()
            print('Delete sucessfully')
        except:
            print('Transaction revert')


    def close_windows(self):
        self.master.destroy()

# --------------------------------------------------------------------------------------------------------------------------------------------------------


def main(): 
    root = Tk()
    root.geometry("700x300")
    app = StartupWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()
