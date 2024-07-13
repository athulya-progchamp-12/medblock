import json
from web3 import Web3

ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi = json.loads('[{"constant":false,"inputs":[{"name":"_companyAdd","type":"address"},{"name":"_id","type":"uint256"},{"name":"_name","type":"string"},{"name":"_mfgDate","type":"string"},{"name":"_expiry","type":"string"}],"name":"addmed","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_id","type":"address"}],"name":"getMedCenterInfo","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_id","type":"uint256"},{"name":"_medCenterId","type":"address"}],"name":"addmedToCenter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_id","type":"uint256"}],"name":"getmedInfo","outputs":[{"name":"","type":"address"},{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_id","type":"address"},{"name":"_name","type":"string"}],"name":"addCenter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

bytecode = "608060405234801561001057600080fd5b50610d8d806100206000396000f3fe60806040526004361061006d576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063137aba20146100725780634a4757b81461029257806388ae09201461035c578063a84d52ee146103b7578063f777b0431461049e575b600080fd5b34801561007e57600080fd5b50610290600480360360a081101561009557600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190803590602001906401000000008111156100dc57600080fd5b8201836020820111156100ee57600080fd5b8035906020019184600183028401116401000000008311171561011057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561017357600080fd5b82018360208201111561018557600080fd5b803590602001918460018302840111640100000000831117156101a757600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561020a57600080fd5b82018360208201111561021c57600080fd5b8035906020019184600183028401116401000000008311171561023e57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610586565b005b34801561029e57600080fd5b506102e1600480360360208110156102b557600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506106af565b6040518080602001828103825283818151815260200191508051906020019080838360005b83811015610321578082015181840152602081019050610306565b50505050905090810190601f16801561034e5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561036857600080fd5b506103b56004803603604081101561037f57600080fd5b8101908080359060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610820565b005b3480156103c357600080fd5b506103f0600480360360208110156103da57600080fd5b810190808035906020019092919050505061097c565b604051808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200180602001828103825283818151815260200191508051906020019080838360005b83811015610462578082015181840152602081019050610447565b50505050905090810190601f16801561048f5780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b3480156104aa57600080fd5b50610584600480360360408110156104c157600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803590602001906401000000008111156104fe57600080fd5b82018360208201111561051057600080fd5b8035906020019184600183028401116401000000008311171561053257600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610af0565b005b61058e610bbf565b60a0604051908101604052808773ffffffffffffffffffffffffffffffffffffffff1681526020018681526020018581526020018481526020018381525090506000819080600181540180825580915050906001820390600052602060002090600502016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550602082015181600101556040820151816002019080519060200190610669929190610c05565b506060820151816003019080519060200190610686929190610c05565b5060808201518160040190805190602001906106a3929190610c05565b50505050505050505050565b606060008090505b600180549050811015610806578273ffffffffffffffffffffffffffffffffffffffff166001828154811015156106ea57fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614156107f95760018181548110151561074757fe5b90600052602060002090600202016001018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156107ec5780601f106107c1576101008083540402835291602001916107ec565b820191906000526020600020905b8154815290600101906020018083116107cf57829003601f168201915b505050505091505061081b565b80806001019150506106b7565b50602060405190810160405280600081525090505b919050565b60008090505b600180549050811015610977578173ffffffffffffffffffffffffffffffffffffffff1660018281548110151561085957fe5b906000526020600020906002020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16141561096a576001818154811015156108b657fe5b9060005260206000209060020201600260008581526020019081526020016000206000820160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060018201816001019080546001816001161561010002031660029004610965929190610c85565b509050505b8080600101915050610826565b505050565b6000606060008090505b600080549050811015610acf57836000828154811015156109a357fe5b9060005260206000209060050201600101541415610ac2576000818154811015156109ca57fe5b906000526020600020906005020160000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600082815481101515610a0b57fe5b9060005260206000209060050201600201808054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610ab15780601f10610a8657610100808354040283529160200191610ab1565b820191906000526020600020905b815481529060010190602001808311610a9457829003601f168201915b505050505090509250925050610aeb565b8080600101915050610986565b5060008090506020604051908101604052806000815250915091505b915091565b610af8610d0c565b60408051908101604052808473ffffffffffffffffffffffffffffffffffffffff1681526020018381525090506001819080600181540180825580915050906001820390600052602060002090600202016000909192909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506020820151816001019080519060200190610bb6929190610c05565b50505050505050565b60a060405190810160405280600073ffffffffffffffffffffffffffffffffffffffff168152602001600081526020016060815260200160608152602001606081525090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610c4657805160ff1916838001178555610c74565b82800160010185558215610c74579182015b82811115610c73578251825591602001919060010190610c58565b5b509050610c819190610d3c565b5090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610cbe5780548555610cfb565b82800160010185558215610cfb57600052602060002091601f016020900482015b82811115610cfa578254825591600101919060010190610cdf565b5b509050610d089190610d3c565b5090565b6040805190810160405280600073ffffffffffffffffffffffffffffffffffffffff168152602001606081525090565b610d5e91905b80821115610d5a576000816000905550600101610d42565b5090565b9056fea165627a7a72305820c9a3a6949e35787f0f4c85aeeff244328b64982c9888f89c96d3435dac0b70990029"


Medd = web3.eth.contract(abi=abi, bytecode=bytecode)

web3.eth.defaultAccount = web3.eth.accounts[0]

tx1_hash = Medd.constructor().transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx1_hash)

contract = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)


def addmedicine(companyAdd, private_key, medicineId, medicineName, mfgDate, expiry):
    # nonce = web3.eth.getTransactionCount(companyAdd)
    tx_hash = contract.functions.addmed(web3.toChecksumAddress(companyAdd), medicineId, medicineName, mfgDate, expiry).buildTransaction()
    return tx_hash

def addCenter(medCenterId, name, private_key):
    # nonce=web3.eth.getTransactionCount(medCenterId)

    tx_hash=contract.functions.addCenter(web3.toChecksumAddress(medCenterId), name).buildTransaction()
    # signed_txn=web3.eth.account.sign_transaction(txn, private_key=private_key)
    # web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return tx_hash

def addmedicineToCenter(medicineId, medCenterId, private_key):

    nonce=web3.eth.getTransactionCount(medCenterId)

    txn=contract.functions.addmedToCenter(medicineId, medCenterId).buildTransaction({
        'chainId': 1,
        'gas': 700000,
        'gasPrice': web3.toWei('1', 'gwei'),
        'nonce': nonce
    })
    signed_txn=web3.eth.account.sign_transaction(txn, private_key=private_key)
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)

def getMedCenterInfo(centerId):
    return contract.functions.getMedCenterInfo(web3.toChecksumAddress(centerId)).call()

def getmedicineInfo(medicineId):
    return contract.functions.getmedInfo(web3.toChecksumAddress(medicineId)).call()