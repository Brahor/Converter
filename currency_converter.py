# currency_converter.py


exchange_rates = {
    'USD_TO_EUR': 0.85,
    'EUR_TO_USD': 1.18,
    'USD_TO_JPY': 110.53,
    'JPY_TO_USD': 0.0090,
}

def convert_currency(amount, from_currency, to_currency):
    
    
    
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

   
    key = f'{from_currency}_TO_{to_currency}'

    
    if key in exchange_rates:
        
        return amount * exchange_rates[key]
    else:
        r
        raise ValueError(f"No exchange rate for {from_currency} to {to_currency}")
