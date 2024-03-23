totalSegundosStr = input("Por favor, entre com o número de segundos que deseja converter: ")
totalSegundos = int(totalSegundosStr)

horas = totalSegundos // 3600
segundosRestantesHora = totalSegundos % 3600

minutos = segundosRestantesHora // 60
segundos = segundosRestantesHora % 60

dias = horas // 24
horasRestantes = horas % 24

if totalSegundos >= 86400:
    horas = horasRestantes    


print(dias, "dias," , horas, "horas,", minutos, "minutos e", segundos, "segundos.")