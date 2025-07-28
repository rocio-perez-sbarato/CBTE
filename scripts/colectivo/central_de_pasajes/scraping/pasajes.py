import logging 
import logging.config 

logging.config.fileConfig('logging_config/logging.conf') 
logger = logging.getLogger('root')

def obtener_precios_pasajes(data):
    viajes = []
    for trip in data:
        viaje = {
            'Origen': trip.get('departureBusStop', {}).get('name', ''),
            'Destino': trip.get('arrivalBusStop', {}).get('name', ''),
            'Empresa': trip.get('provider', {}).get('name', ''),
            'Precio': trip.get('offers', {}).get('lowPrice', '')
        }

        viajes.append(viaje)
        
    return viajes
