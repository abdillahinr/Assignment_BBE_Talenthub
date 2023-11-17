print('SOAL 1')
# Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.

def kelvin_to_celsius(kelvin):
    """
    Konversi suhu dari Kelvin ke Celsius.

    :param kelvin: Suhu dalam Kelvin
    :return: Suhu dalam Celsius
    """
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    """
    Konversi suhu dari Celsius ke Kelvin.

    :param celsius: Suhu dalam Celsius
    :return: Suhu dalam Kelvin
    """
    kelvin = celsius + 273.15
    return kelvin

# Contoh penggunaan fungsi
temperature_kelvin = 300.0
temperature_celsius = kelvin_to_celsius(temperature_kelvin)
print(f"{temperature_kelvin} Kelvin = {temperature_celsius:.2f} Celsius")

temperature_celsius = 25.0
temperature_kelvin = celsius_to_kelvin(temperature_celsius)
print(f"{temperature_celsius} Celsius = {temperature_kelvin:.2f} Kelvin\n")

print('SOAL 2')
# Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. Tambahkan parameter
# untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin.
# Panggil function yang pertama jika diperlukan.

def celsius_to_fahrenheit(celsius):
    """
    Konversi suhu dari Celsius ke Fahrenheit.

    :param celsius: Suhu dalam Celsius
    :return: Suhu dalam Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def kelvin_to_fahrenheit(kelvin):
    """
    Konversi suhu dari kelvin ke Fahrenheit.

    :param kelvin: Suhu dalam kelvin
    :return: Suhu dalam Fahrenheit
    """
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

#Contoh penggunaan fungsi
temperature_celsius = 25.0
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius} Celsius = {temperature_fahrenheit:.2f} Fahrenheit")

temperature_kelvin = 278
temperature_fahrenheit = kelvin_to_fahrenheit(temperature_kelvin)
print(f"{temperature_kelvin} kelvin = {temperature_fahrenheit:.2f} Fahrenheit\n")

print('SOAL 3')
# Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit.
# Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin.

def fahrenheit_to_celsius(fahrenheit):
    """
    Konversi suhu dari Fahrenheit ke Celsius.

    :param fahrenheit: Suhu dalam Fahrenheit
    :return: Suhu dalam Celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    """
    Konversi suhu dari Fahrenheit ke Kelvin.

    :param fahrenheit: Suhu dalam Fahrenheit
    :return: Suhu dalam Kelvin
    """
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

#contoh penggunan funsi
temperature_fahrenheit = 77.0
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
print(f"{temperature_fahrenheit} Fahrenheit = {temperature_celsius:.2f} Celsius")

temperature_fahrenheit = 1
temperature_kelvin = fahrenheit_to_kelvin(temperature_fahrenheit)
print(f"{temperature_fahrenheit} Fahrenheit = {temperature_kelvin:.2f} Kelvin")

print("SOAL 4")
# Berikan dokumentasi pada setiap baris kode yang kalian tulis.

def convert_temperature(temperature, from_unit, to_unit):
    """
    Konversi suhu antara Celcius dan Kelvin.

    :param temperature: Suhu yang akan dikonversi
    :param from_unit: Unit awal ('C' untuk Celsius, 'K' untuk Kelvin)
    :param to_unit: Unit tujuan ('C' untuk Celsius, 'K' untuk Kelvin)
    :return: Hasil konversi suhu
    """
    if from_unit == 'C' and to_unit == 'K':
        # Jika konversi dari Celsius ke Kelvin
        return celsius_to_kelvin(temperature)
    elif from_unit == 'K' and to_unit == 'C':
        # Jika konversi dari Kelvin ke Celsius
        return kelvin_to_celsius(temperature)
    else:
        # Jika unit tidak valid atau tidak ada konversi yang diperlukan
        return None


