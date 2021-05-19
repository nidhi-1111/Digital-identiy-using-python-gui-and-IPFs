# Digital-identiy-using-python-gui-and-IPFs
abi will be the same if you are using this contract.

    abi = json.loads(
            '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"string","name":"hashOfIpfs","type":"string"},                 {"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"addHash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"hashOfIpfs","type":"string"},{"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"deleteHash","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"destroy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"displayHash","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"hashOfIpfs","type":"string"},{"internalType":"string","name":"currentHash","type":"string"},{"internalType":"uint16","name":"hashNo","type":"uint16"}],"name":"updateHash","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
    );
Use ganache to connect with remix or use directly to connect with python file

Change the contract address every time you deploy contract

    address = web3.toChecksumAddress("0x833d405d12b7260f351FfD9037Fb4Fa8b67F13Fd");
