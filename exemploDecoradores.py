
def funcion_necesita_decorador():
    print ("Decorarme, por favor!")


def meu_decorador (funcion_a_decorar):
    def funcion_envolvente ():
        print ("Operacións antes da función a decorar")
        funcion_a_decorar()
        print ("Operacións posteriores a execución da función a decorar")
    return funcion_envolvente

def meu_decorador2 (funcion_a_decorar):
    def funcion_envolvente ():
        print (" Outras operacións antes da función a decorar")
        funcion_a_decorar()
        print ("Outras operacións posteriores a execución da función a decorar")
    return funcion_envolvente

funcion_decorada = meu_decorador(funcion_necesita_decorador)
funcion_decorada()

@meu_decorador2
@meu_decorador
def funcion2_necesita_decorador():
    print ("Eu tamén preciso que me decoren!")

funcion2_necesita_decorador()


