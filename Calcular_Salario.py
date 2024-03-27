
from flet import *

def main(page: Page):
    page.title="Calcular Salario - Python"
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.window_width=370
    page.window_max_width=370
    page.window_height=680
    page.window_max_height=980


    edit_texto_salario = TextField(text_align="center",
                                   label="Escribe salario",
                                   disabled=False, text_size=24,
                                   width=180)
    txt_base = Text()
    txt_isss = Text()
    txt_afp = Text()
    txt_renta = Text()
    txt_suma_descuentos = Text()
    txt_devengado = Text()
    #Row para poner las cajas
    def Calcular(e):
        if edit_texto_salario.value=="":
            return False
        base = float(edit_texto_salario.value)
        txt_base.value = str(round(base,2))
        isss = ISSS(float(txt_base.value))
        txt_isss.value = str(round(isss,2))
        afp = float(edit_texto_salario.value)*0.0725
        txt_afp.value = str(round(afp,2))
        suma = float(txt_base.value)-(float(txt_isss.value)+float(txt_afp.value))
        txt_renta.value = str(round(CalcularRenta(float(suma)),2))
        sumaDescuentos = float(txt_isss.value) + float(txt_afp.value) + float(txt_renta.value)
        txt_suma_descuentos.value = str(round(sumaDescuentos,2))
        devengado = float(txt_base.value)-sumaDescuentos
        txt_devengado.value = str(round(devengado,2))
        print(f"Siiii. me presionaste....",txt_base,txt_isss)
        page.update()

    def ISSS(Monto):
        if Monto<1000.0:
            issRetorno = Monto*0.03
        elif Monto>=1000.0:
            issRetorno = 30
        return issRetorno

    def CalcularRenta(Monto):
        print(Monto)
        if Monto <= 472.00:
            rentaReturn = 0.0
        elif Monto >= 472.01 and Monto <= 895.24:
            valor = (Monto-472.0)*0.10
            valor2 = valor+17.67
            rentaReturn = valor2
        elif Monto >= 895.25 and Monto <= 2038.10:
            valor = (Monto-895.24)*0.20
            valor2 = valor+60.0
            rentaReturn = valor2
        elif Monto >= 2038.11:
            valor = (Monto-2038.10)*0.30
            valor2 = valor+288.57
            rentaReturn = valor2
        else:
            rentaReturn = 0.0
        return rentaReturn


    def _top():
        top = Container(
            width=305,
            height=655,
            bgcolor="blue",
            padding=20,
            content=Column(
                controls=[
                    Row(alignment="center",controls=[
                        edit_texto_salario
                    ]),
                    Row(alignment="center",
                        controls=[
                            ElevatedButton(text="Presioname....",on_click=Calcular)
                        ]),
                    Row(controls=[
                        Text("Sueldo base :",width=120),
                        txt_base
                    ]),
                    Row(controls=[
                        Text("ISSS :",width=120),
                        txt_isss
                    ]),
                    Row(controls=[
                        Text("AFP :",width=120),
                        txt_afp
                    ]),
                    Row(controls=[
                        Text("RENTA :",width=120),
                        txt_renta
                    ]),
                    Row(controls=[
                        Text("Suma :", width=120),
                        txt_suma_descuentos
                    ]),
                    Row(controls=[
                        Text("Devengado :", width=120),
                        txt_devengado
                    ])
                ]
            )
        )
        return top

    _c = Container(
        width=310,
        height=560,
        border_radius=15,
        bgcolor="blue",
        padding=20,
        content=Stack(
            width=300,
            height=550,
            controls=[
                _top()
            ]
        )

    )
    page.add(_c)




if __name__=="__main__":
    app(target=main,assets_dir="assets")
    pass