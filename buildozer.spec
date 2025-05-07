[app]
title = HolaMundoPro
package.name = holamundopro
package.domain = com.kivyapp
source.dir = .
version = 2024.1.0
requirements = 
    python==3.11.6,
    kivy==2.3.0,
    kivymd==1.2.0,
    android==0.5

orientation = portrait
fullscreen = 0

# Configuración Android
android.sdk = 34
android.ndk = 25b
android.build_tools_version = 34.0.0
android.api = 34
android.minapi = 24
android.wakelock = 0
android.accept_sdk_license = True

# Optimizaciones
p4a.branch = develop
p4a.allow_backup = True
android.arch = arm64-v8a

# Recursos
icon.filename = icon.png
presplash.filename = icon.png
