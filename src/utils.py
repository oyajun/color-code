import decimal

def convert_to_MKG(value):
    if value < 1000:
        return delete_zero(value)
    elif value < 1000000:
        return delete_zero(value/1000) + 'K'
    elif value < 1000000000:
        return delete_zero(value/1000000) + 'M'
    elif value < 1000000000000:
        return delete_zero(value/1000000000) + 'G'

def delete_zero(value):
    if value % decimal.Decimal('1') == 0:   # the value has .0
        return str(int(value))
    elif value % decimal.Decimal('0.1') == 0:
        return str(value.quantize(decimal.Decimal('1.0')))
    elif value % decimal.Decimal('0.01') == 0:
        return str(value.quantize(decimal.Decimal('1.00')))
    elif value % decimal.Decimal('0.001') == 0:
        return str(value.quantize(decimal.Decimal('1.000')))
    else:
        return str(value)
