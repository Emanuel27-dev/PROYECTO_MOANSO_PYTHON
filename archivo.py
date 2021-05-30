from modulo_tkinter import *

def cerrar_ventana_padre():
    ventana_padre.destroy() # Eliminando la ventana padre definitivamente


def volver_ventana_padre_de_login():

    v_login.withdraw() # Escondiendo ventana_inicio_sesion()
    ventana_padre.iconify() # Regresando ventana padre

def volver_ventana_padre_de_registrarse():
    v_registrar.withdraw()  # Escondiendo la ventana_registrarse()
    ventana_padre.iconify() # Regresando ventana padre


def ventana_inicio_sesion():

    ventana_padre.withdraw() #Escondiendo la ventana padre

    global v_login

    v_login = crear_ventana("350x400","login","#0B7D8F")

    e1_login = crear_etiqueta(v_login,"Correo electrónico")
    e1_login.place(x=80,y=115)
    i1_login = crear_entrada(v_login)
    i1_login.place(x=80, y=140)

    e2_login = crear_etiqueta(v_login,"Contraseña")
    e2_login.place(x=80, y=200)
    i2_login = crear_entrada(v_login)
    i2_login.place(x=80, y=225)

    b1_login = crear_boton(v_login, "Iniciar Sesión",ventana_informe)
    b1_login.place(x=110, y=290)

    # Pendiente crear un boton y funcion para volver ventana padre ->(HECHO)
    b2_login = crear_boton(v_login,"Volver",volver_ventana_padre_de_login).place(x=140,y=340)
    v_login.mainloop()


def ventana_registrarse():

    ventana_padre.withdraw() # Escondiendo la ventana padre

    global v_registrar
    v_registrar = crear_ventana("350x470","Registrarse","#0B7D8F")
    e_titulo_registrar = crear_etiqueta(v_registrar,"Registrarse").place(x=135,y=20)

    e1_registrar = crear_etiqueta(v_registrar,"Nombres").place(x=20,y=70)
    i1_registrar = crear_entrada(v_registrar).place(x=20,y=95)
    e2_registrar = crear_etiqueta(v_registrar,"Apellidos").place(x=20,y=135)
    i2_registrar = crear_entrada(v_registrar).place(x=20, y=160)
    e3_registrar = crear_etiqueta(v_registrar,"Correo Electrónico").place(x=20,y=200)
    i3_registrar = crear_entrada(v_registrar).place(x=20, y=225)
    e4_registrar = crear_etiqueta(v_registrar,"Contraseña").place(x=20,y=265)
    i4_registrar = crear_entrada(v_registrar).place(x=20, y=290)


    b1_registrar = crear_boton(v_registrar,"Guardad cambios").place(x=20,y=360)
    b2_registrar = crear_boton(v_registrar, "Iniciar Sesión",ventana_informe).place(x=200,y=360)

    # Pendiente crear un boton y funcion para volver ventana padre
    b3_registrar = crear_boton(v_registrar,"Volver",volver_ventana_padre_de_registrarse).place(x=20,y=405)
    v_registrar.mainloop()

def ventana_informe():

    global v_informe

   # v_login.withdraw() # Cerrando la ventana login
   # v_registrar.withdraw() # Cerrando la ventana registrar
    v_informe = crear_ventana("600x700",back_ground="#0B7D8F")

    e1_informe = crear_etiqueta(v_informe, "Nombres").place(x=30,y=50)
    i1_informe = crear_entrada(v_informe).place(x=30,y=75)

    e2_informe = crear_etiqueta(v_informe, "Apellidos").place(x=30,y=115)
    i2_informe = crear_entrada(v_informe).place(x=30,y=140)

    e3_informe = crear_etiqueta(v_informe, "DNI").place(x=30,y=180)
    i3_informe = crear_entrada(v_informe).place(x=30,y=205)

    e4_informe = crear_etiqueta(v_informe, "Fecha de nacimiento").place(x=30,y=245)
    i4_informe = crear_entrada(v_informe).place(x=30,y=270)

    e5_informe = crear_etiqueta(v_informe, "Nro telefónico").place(x=30,y=305)
    i5_informe = crear_entrada(v_informe).place(x=30,y=330)

    e6_informe = crear_etiqueta(v_informe, "Dirección").place(x=30,y=370)
    i6_informe = crear_entrada(v_informe).place(x=30,y=395)

    e7_informe = crear_etiqueta(v_informe, "Carrera universitaria").place(x=30,y=435)
    i7_informe = crear_entrada(v_informe).place(x=30,y=460)

    e8_informe = crear_etiqueta(v_informe, "¿Cuantos años tiene de experiencia laboral?").place(x=30,y=500)
    i8_informe = crear_entrada(v_informe).place(x=30,y=525)

    b1_informe = crear_boton(v_informe,"Enviar").place(x=30,y=565)
    b2_informe = crear_boton(v_informe,"Salir",cerrar_ventana_padre).place(x=30,y=590)

    v_informe.mainloop()


if __name__ == '__main__':

    ventana_padre = Tk()
    ventana_padre.geometry("400x250")
    ventana_padre.resizable(False,False)
    ventana_padre.config(bg="#0B7D8F", cursor="hand1")

    e1 = crear_etiqueta(ventana_padre,"Bienvenido")
    e1.pack()

    b1 = crear_boton(ventana_padre,"Iniciar Sesión",ventana_inicio_sesion)
    b1.place(x=210, y=50)

    b2 = crear_boton(ventana_padre,"Registrarse",ventana_registrarse)
    b2.place(x=210, y=120)

    b3 = crear_boton(ventana_padre,"Salir",cerrar_ventana_padre).place(x=210,y=190)

    ventana_padre.mainloop()