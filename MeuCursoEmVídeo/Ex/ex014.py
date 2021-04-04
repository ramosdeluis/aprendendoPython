c = float(input('Informe a temperatura em °C: '))

print('{:.2f} °C em °F são {:.2f} °F e em °K são {:.2f} °K'.format(c, ((c*9/5)+32), c + 273.15))
