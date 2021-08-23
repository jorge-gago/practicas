#contraseña 8 - 16 caracteres
#debe tener mayuscula
#y debe tener minimo un caracter /.#!(),;

def comprobar( pas):
    res = [ "", "", "", "red"]
    larg = largo(pas)
    may_min =mayus_minus(pas)
    esp = especiales(pas)
    if larg and may_min and esp:
        res[1] = ("password correcto")
        res[3] = "green"
    else:
        if larg != True: res[0] = ("debe tener entre 8 y 16 caracteres")
        if may_min != True: res[1] = ("debe tener una letra mayuscula y minuscula")
        if esp != True: res[2] = ("debe tener un caracter especial /.#!(),;")
    return res

def largo( pas):
    lon = False
    l = len(pas)
    if l >= 8 and l <= 16:
        lon = True
    return lon

def mayus_minus(pas):
    mayus = False
    minus = False
    for i in pas:

        if minus != True : minus = i.islower()
        if mayus != True : mayus = i.isupper()
        if minus and mayus :
            return True
    return False

def especiales(pas):
    con = False
    caracteres = ( '/', '.', '#', ':', '!', '(', ')', ',', ';')
    for i in pas:
        if i in caracteres:
            return True
    return False



if __name__ == "__main__":
    test = ["corta", "Correcta:", "Corta,", "MAL", "corta:"]

    for i in test:
        print("---",i,"---")
        print(comprobar(i))
       


