import psutil

class Sensors:
    @staticmethod
    def get_battery_info():
        """Retorna informações da bateria, se disponível."""
        try:
            battery = psutil.sensors_battery()
            if battery:
                return {
                    "percent": battery.percent,
                    "secsleft": battery.secsleft,
                    "power_plugged": battery.power_plugged
                }
        except (AttributeError, Exception):
            pass
        return {"percent": None, "secsleft": None, "power_plugged": None}

    @staticmethod
    def get_fan_info():
        """Retorna informações dos ventiladores, se disponíveis (apenas Linux)."""
        try:
            if hasattr(psutil, 'sensors_fans'):
                fans = psutil.sensors_fans()
                if fans:
                    return {fan: info for fan, info in fans.items()}
        except (AttributeError, Exception):
            pass
        return {}
    
    @staticmethod
    def get_sensors_info():
        """Retorna todas as informações de sensores."""
        battery = Sensors.get_battery_info()
        
        # Processa informações dos ventiladores (apenas em Linux)
        fans = {}
        try:
            if hasattr(psutil, 'sensors_fans'):
                fans_raw = psutil.sensors_fans()
                if fans_raw:
                    for name, entries in fans_raw.items():
                        for entry in entries:
                            fans[f"{name}_{entry.label}"] = entry.current
        except (AttributeError, Exception):
            pass
        
        return {
            "battery": battery,
            "fans": fans
        }