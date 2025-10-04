from psutil import sensors_fans, sensors_battery

class Sensors:
    @staticmethod
    def get_battery_info():
        """Retorna informações da bateria, se disponível."""
        battery = sensors_battery()
        if battery:
            return {
                "percent": battery.percent,
                "secsleft": battery.secsleft,
                "power_plugged": battery.power_plugged
            }
        else:
            return {"percent": None, "secsleft": None, "power_plugged": None}

    @staticmethod
    def get_fan_info():
        """Retorna informações dos ventiladores, se disponíveis."""
        fans = sensors_fans()
        if fans:
            return {fan: info for fan, info in fans.items()}
        else:
            return {}