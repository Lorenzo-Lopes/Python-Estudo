import math
ang = float(input('Digite o angulo'))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O angulo digitado foi {:.2f} \n O seno é {:.2f} \n O cosseno é{:.2f} \n A tangente é {:.2f}'.format(ang, seno, cos, tang))
