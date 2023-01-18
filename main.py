import config
from config import truncate
from binance.client import Client
from binance.enums import *
import time

client = Client(config.API_KEY, config.API_SECRET, tld='com')

Cryptos = client.get_all_tickers()      # trae la nómina de todas las cryptos en un vector
Cant_cryptos = len(Cryptos)             # tenemmos la cantidad de cryptos en el vector
print(Cant_cryptos)
print(Cryptos)


habilitar_USDT=1   #habilita o no la compra de cryptos con USDT
habilitar_BNB=1
habilitar_BTC=1
habilitar_ETH=1
habilitar_BUSD=1

porcentaje_USDT_por_compra=0.4
porcentaje_BNB_por_compra=0.4
porcentaje_BTC_por_compra=0.4
porcentaje_ETH_por_compra=0.4
porcentaje_BUSD_por_compra=0.4

#Recuperamos los saldos que tenemos en cada crypto y lo imprimimos
balance_USDT=client.get_asset_balance(asset='USDT')
balance_BUSD=client.get_asset_balance(asset='BUSD')
balance_BNB=client.get_asset_balance(asset="BNB")
balance_BTC=client.get_asset_balance(asset='BTC')
balance_ETH=client.get_asset_balance(asset='ETH')

disponible_compra_USDT=float(balance_USDT['free'])*porcentaje_USDT_por_compra
disponible_compra_BUSD=float(balance_BUSD['free'])*porcentaje_BUSD_por_compra
disponible_compra_BNB=float(balance_BNB['free'])*porcentaje_BNB_por_compra
disponible_compra_BTC=float(balance_BTC['free'])*porcentaje_BTC_por_compra
disponible_compra_ETH=float(balance_ETH['free'])*porcentaje_ETH_por_compra

print("########################################")
print("Balance en USDT: ",balance_USDT['free'])  # balance_.... es un diccionario y la clave 'free' trae el valor que tenemos de esa crypto
print("Dsiponible para proxima compra: ",truncate(disponible_compra_USDT,2))
print("------------------------------------")

print("Balance en BUSD: ",balance_BUSD['free'])
print("Dsiponible para proxima compra: ",truncate(disponible_compra_BUSD,2))
print("------------------------------------")
print("Balance en BNB: ",balance_BNB['free'])
print("Dsiponible para proxima compra: ",truncate(disponible_compra_BNB,2))
print("------------------------------------")
print("Balance en BTC: ",balance_BTC['free'])
print("Dsiponible para proxima compra: ",truncate(disponible_compra_BTC,2))
print("------------------------------------")
print("Balance en ETH: ",balance_ETH['free'])
print("Dsiponible para proxima compra: ",truncate(disponible_compra_ETH,2))
print("------------------------------------")
print("########################################")


prevCryptos = client.get_all_tickers()   #vemmos la cantidad inicial de cryptos
prevLen = len(prevCryptos)
prevLen=2135


while 1:

    currentCryptos = client.get_all_tickers()       # traemos el valor actual de crytos disponibles en Binance
    currentLen = len(currentCryptos)
    #print(currentLen)

    if prevLen < currentLen:       # si el valor historico de cryptos es menor al actual -> nuevas cryptos!!!
        print("New Coins: ",currentLen)

        for actual_new_coin in range(prevLen,currentLen):

            print("-----------------------------------------")
            print("número de crypto encontrada: ", actual_new_coin)
            symbol_to_buy = currentCryptos[actual_new_coin].get('symbol')
            price_to_buy = currentCryptos[actual_new_coin].get('price')

            if symbol_to_buy[-4:] == 'USDT' and habilitar_USDT==1 and truncate(disponible_compra_USDT,2)>0:     #revisamos si el par es con USDT y vemos si habiamos habilitado la compra con USDT y a su vez tenemos crypto para comprar la nueva
                cantidad_unidades_compra=disponible_compra_USDT/float(price_to_buy)
                unidades_a_comprar=truncate(cantidad_unidades_compra,2)
                print("USDT  Ok")
                print(symbol_to_buy)
                print(price_to_buy,"USDT")
                print("Cantidad de monedas a comprar:",unidades_a_comprar)








            if symbol_to_buy[-3:] == 'BNB'and habilitar_BNB==1:     #revisamos si el par es con BNB
                print("BNB  Ok")
                print(symbol_to_buy)
                print(price_to_buy,"BNB")

            if symbol_to_buy[-3:] == 'BTC'and habilitar_BTC==1:     #revisamos si el par es con BTC
                print("BTC  Ok")
                print(symbol_to_buy)
                print(price_to_buy,"BTC")

            if symbol_to_buy[-3:] == 'ETH'and habilitar_ETH==1:     #revisamos si el par es con ETH
                print("ETH  Ok")
                print(symbol_to_buy)
                print(price_to_buy,"ETH")

            if symbol_to_buy[-4:] == 'BUSD'and habilitar_BUSD==1:     #revisamos si el par es con BUSD
                print("BUSD  Ok")
                print(symbol_to_buy)
                print(price_to_buy,"BUSD")





