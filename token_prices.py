from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()

trending_coins_data = cg.get_search_trending()
trending_coins = trending_coins_data["coins"][:5]
formatted_trending_coins = [f"ID:{coin['item']['id']}.\n"
                            f"Coin Name:{coin['item']['name']} \n"
                            f"Symbol:{coin['item']['symbol']}\n "
                            f"Market Cap Rank:{coin['item']['market_cap_rank']}" for coin in trending_coins]


def top_five_Coins():
    top_five_coins = f"Today's HOT Coins on Coingecko \n{formatted_trending_coins[0]}\n\n{formatted_trending_coins[1]}\n\n{formatted_trending_coins[2]}\n\n{formatted_trending_coins[3]}\n\n{formatted_trending_coins[4]} "
    return top_five_coins


def bitcoin_data():
    bitcoin_advanced_data = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=True,
                                         include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
    bitcoin = f"--BITCOIN DATAS-- \nUSD: {bitcoin_advanced_data['bitcoin']['usd']}$ \nUSD Market Cap: {bitcoin_advanced_data['bitcoin']['usd_market_cap']} \nUSD 24h Vol: {bitcoin_advanced_data['bitcoin']['usd_24h_vol']} \nUSD 24h Change: {bitcoin_advanced_data['bitcoin']['usd_24h_change']} \nLast Updated At: {datetime.fromtimestamp(bitcoin_advanced_data['bitcoin']['last_updated_at'])} \n Website: https://coinmarketcap.com/tr/currencies/bitcoin/"
    return bitcoin


def eth_data():
    eth_advanced_data = cg.get_price(ids='ethereum', vs_currencies='usd', include_market_cap=True,
                                     include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
    eth = f"--ETHEREUM DATAS-- \nUSD: {eth_advanced_data['ethereum']['usd']}$ \nUSD Market Cap: {eth_advanced_data['ethereum']['usd_market_cap']} \nUSD 24h Vol: {eth_advanced_data['ethereum']['usd_24h_vol']} \nUSD 24h Change: {eth_advanced_data['ethereum']['usd_24h_change']} \nLast Updated At: {datetime.fromtimestamp(eth_advanced_data['ethereum']['last_updated_at'])} \nWebsite: https://ethereum.org/en/"
    return eth


def sol_data():
    sol_advanced_data = cg.get_price(ids='Solana', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
    sol = f"--Solana DATAS-- \nUSD: {sol_advanced_data['solana']['usd']}$ \nUSD Market Cap: {sol_advanced_data['solana']['usd_market_cap']} \nUSD 24h Vol: {sol_advanced_data['solana']['usd_24h_vol']} \nUSD 24h Change: {sol_advanced_data['solana']['usd_24h_change']} \nLast Updated At: {datetime.fromtimestamp(sol_advanced_data['solana']['last_updated_at'])} \nWebsite: https://solana.com/"
    return sol

def bnb_data():
    bnb_advanced_data = cg.get_price(ids='binancecoin', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
    bnb = f"--BNB DATAS-- \nUSD: {bnb_advanced_data['binancecoin']['usd']}$ \nUSD Market Cap: {bnb_advanced_data['binancecoin']['usd_market_cap']} \nUSD 24h Vol: {bnb_advanced_data['binancecoin']['usd_24h_vol']} \nUSD 24h Change: {bnb_advanced_data['binancecoin']['usd_24h_change']} \nLast Updated At: {datetime.fromtimestamp(bnb_advanced_data['binancecoin']['last_updated_at'])} \nWebsite: https://www.binance.com/"
    return bnb

def ada_data():
    ada_advanced_data = cg.get_price(ids='binance-peg-cardano', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
    ada = f"--ADA DATAS-- \nUSD: {ada_advanced_data['binance-peg-cardano']['usd']}$ \nUSD Market Cap: {ada_advanced_data['binance-peg-cardano']['usd_market_cap']} \nUSD 24h Vol: {ada_advanced_data['binance-peg-cardano']['usd_24h_vol']} \nUSD 24h Change: {ada_advanced_data['binance-peg-cardano']['usd_24h_change']} \nLast Updated At: {datetime.fromtimestamp(ada_advanced_data['binance-peg-cardano']['last_updated_at'])} \nWebsite: https://cardano.org/"
    return ada

