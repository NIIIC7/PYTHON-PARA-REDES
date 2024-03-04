a = int(input("Valor uno: "))
b = int(input("Valor segundo: "))

try:
    res = a / b
    print(res)

except ZeroDivisionError:
    print("No se puede dividir por cero.")
    
except Exception as e:
    print("Se ha producido una excepción:", e)

