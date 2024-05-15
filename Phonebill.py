class Calls():  # ----------> Clase con atributos de llamadas
    def __init__(self, number,country,city, day, hour, minutes):
        self.number = number # numero de telefono destino (id)
        self.country = country # ciudad destino (compara nacional o internacional)
        self.city = city # ciudad destino (comparar local o nacional)
        self.day = day # dia de la llamada (coparar dias habiles)
        self.hour = hour # hora que se realizo de la llamada (comparar rango horario)
        self.minutes = minutes # duracion de la llamada
    # Metodos:
    def validateDay(self):
        week = ["mon", "tue", "wed", "thu", "fri"]
        return self.day in week
    
    def validateHour(self):
        return 800 <= self.hour <= 2000
    
    def validateCountry(self):
        return self.country == "country_00"  # country_00 como el pais local
    
    def validateCity(self):
        return self.city == "city_00"  # city_00 como ciudad local
        
    def callCost(self):
        countryPrice = {"country_01": 2.5,"country_02": 1.5,} # diccionario costos paises
        cityPrice = {"city_01": 0.5,"city_02": 1} # diccionario costos ciudades nacionales 
        
        if self.validateDay() and self.validateHour():
            basic_price = 0.20
        else:
            basic_price = 0.10
        
        if self.validateCountry() and self.validateCity():
            return self.minutes * basic_price
        elif self.validateCountry():
            return self.minutes * basic_price * cityPrice.get(self.city, 1)
        else:
            return self.minutes * basic_price * countryPrice.get(self.country, 1)
# =================================================================================================================

calls = [
    Calls("3245-9878", "country_00", "city_00", "mon", 1300, 20),  # contacto local
    Calls("3245-5676", "country_00", "city_01", "sat", 00, 20),    # contacto nacional
    Calls("2377-8862", "country_00", "city_02", "mon", 2200, 20),  # contacto nacional
    Calls("44-986-565", "country_01", "", "mon", 730, 20),         # contacto internacional
    Calls("4556-3232", "country_02", "", "sun", 2200, 20)          # contacto internacional
]

def bill():
    total_basic = 0
    total_national = 0
    total_international = 0
    basic_payment = 300 # Abono basico ficticio de $300

    for call in calls:
        cost = call.callCost()
        if call.validateCountry() and call.validateCity():
            total_basic += cost
        elif call.validateCountry():
            total_national += cost
        else:
            total_international += cost

    total_general = total_basic + total_national + total_international
    payment_rest = basic_payment - total_general

    print("\n\n\tFactura de llamadas:")
    print(f"\n\tTotal llamadas locales: ${total_basic:.2f}")
    print(f"\n\tTotal llamadas nacionales: ${total_national:.2f}")
    print(f"\n\tTotal llamadas internacionales: ${total_international:.2f}")
    print(f"\n\tAbono basico: ${basic_payment:.2f}")
    print(f"\n\n\tConsumo final general: ${total_general:.2f}")
    print(f"\n\tAbono restante: ${payment_rest:.2f}\n")
    

# Llamada a la función bill para mostrar la factura en pantalla
bill()
# *** _end_ ***
    
    
    
    

    
    
    
    




    
