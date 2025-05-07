from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class HolaMundoApp(App):
    def build(self):
        Window.clearcolor = (0.2, 0.6, 1, 1)  # Fondo azul moderno
        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=50)
        self.boton = Button(
            text='¡Presióname!',
            size_hint=(0.6, 0.3),
            pos_hint={'center_x': 0.5},
            background_color=(0.1, 0.5, 0.8, 1),
            bold=True
        )
        self.boton.bind(on_press=self.mostrar_texto)
        self.layout.add_widget(self.boton)
        return self.layout

    def mostrar_texto(self, instance):
        self.layout.add_widget(
            Label(
                text='[b]¡Hola Mundo![/b]',
                markup=True,
                font_size='40sp',
                color=(1, 1, 1, 1)
            )
        )

if __name__ == '__main__':
    HolaMundoApp().run()