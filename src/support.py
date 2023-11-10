def convert_currency(row):
    chf_to_eur = 1.04
    gbp_to_eur = 1.14
    dkk_to_eur = 0.13

    if row['Currency'] == 'CHF':
        exchange_rate = chf_to_eur
        return row['Precio'] * exchange_rate
    if row['Currency'] == 'GBP':
        exchange_rate = gbp_to_eur
        return row['Precio'] * exchange_rate
    if row['Currency'] == 'DKK':
        exchange_rate = dkk_to_eur
        return row['Precio'] * exchange_rate
    if row['Currency'] == 'EUR':
        return row['Precio']
    
def separa_valor_monedas(celda):
    partes = celda.split()
    try:
        return float(partes[0]), partes[1] # Hago un try except porque no siempre el valor numerico está en la primera posición
    except:
        return float(partes[1]), partes[0]

