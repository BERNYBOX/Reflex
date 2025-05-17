import reflex as rx

AFP = 0.0287  
SFS = 0.0304  
SEGURIDAD_SOCIAL = AFP + SFS  
ISR = 0.15  
BONIFICACION = 0.0833  

class Estado(rx.State):
    sueldo_bruto: float = 0.0
    otros_descuentos: float = 0.0
    resultado: str = ""

    def set_sueldo_bruto(self, value: str):
        try:
            self.sueldo_bruto = float(value)
        except ValueError:
            self.sueldo_bruto = 0.0  # O manejarlo de otra forma si es necesario

    def set_otros_descuentos(self, value: str):
        try:
            self.otros_descuentos = float(value)
        except ValueError:
            self.otros_descuentos = 0.0  # O manejarlo de otra forma si es necesario

    def calcular(self):
        if self.sueldo_bruto <= 0:
            self.resultado = "Error: El sueldo bruto debe ser positivo"
            return
        if self.otros_descuentos < 0:
            self.resultado = "Error: Los descuentos no pueden ser negativos"
            return

        descuento_ss = self.sueldo_bruto * SEGURIDAD_SOCIAL
        descuento_isr = self.sueldo_bruto * ISR
        bonificacion = self.sueldo_bruto * BONIFICACION
        sueldo_neto = self.sueldo_bruto - descuento_ss - descuento_isr - self.otros_descuentos + bonificacion

        self.resultado = (
            f"Sueldo Bruto: RD${self.sueldo_bruto:.2f}\n"
            f"Descuento por Seguridad Social: RD${descuento_ss:.2f}\n"
            f"Retención ISR: RD${descuento_isr:.2f}\n"
            f"Otros Descuentos: RD${self.otros_descuentos:.2f}\n"
            f"Bonificación: RD${bonificacion:.2f}\n"
            f"Sueldo Neto: RD${sueldo_neto:.2f}"
        )

def index():
    return rx.center(
        rx.vstack(
            rx.heading("Calculadora de Sueldo - RD", size="3"),
            rx.input(placeholder="Sueldo Bruto", on_change=Estado.set_sueldo_bruto),
            rx.input(placeholder="Otros Descuentos", on_change=Estado.set_otros_descuentos),
            rx.button("Calcular", on_click=Estado.calcular),
            rx.text(Estado.resultado),  # Directamente mostrando el resultado
            spacing="4",
        ),
        padding="4",
    )

app = rx.App()
app.add_page(index)
app._compile()
