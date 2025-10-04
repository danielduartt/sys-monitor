from dashing import HSplit, VSplit, HGauge, VGauge, Text
from psutil import virtual_memory, swap_memory
from time import sleep

ui = HSplit(
    VSplit(
        HGauge(border_color=2), 
        HGauge(border_color=4), 
        border_color=3, 
        title = "Memória RAM"
    )
) 

while True:
    ## Memória RAM
    mem_tui = ui.items[0].items[0]
    mem_tui.title = f"RAM: {virtual_memory().percent:.2f}"
    mem_tui.value = virtual_memory().percent

    ## Swap
    mem_swap_tui = ui.items[0].items[1]
    mem_swap_tui.title = f"Swap: {swap_memory().percent:.2f}"
    mem_swap_tui.value = swap_memory().percent
    try: 
        ui.display()
        sleep(.5)
    except KeyboardInterrupt:
        print("Saindo...")
        break
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break


