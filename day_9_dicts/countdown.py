import os, time
from typing import Coroutine, Counter
numbers = [
    """
     ██╗
    ███║
    ╚██║
     ██║
     ██║
     ╚═╝
    
""",
"""
    ██████╗ 
    ╚════██╗
     █████╔╝
    ██╔═══╝ 
    ███████╗
    ╚══════╝""",
"""
    ██████╗ 
    ╚════██╗
     █████╔╝
     ╚═══██╗
    ██████╔╝
    ╚═════╝ 
"""
]

curtain = [
    """
 █████╗ ███╗   ██╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗
███████║██╔██╗ ██║██║  ██║
██╔══██║██║╚██╗██║██║  ██║
██║  ██║██║ ╚████║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 
""",
"""
████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗  
   ██║   ██╔══██║██╔══╝  
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝
""",
"""
██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ 
██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                 
""",
"""
██╗███████╗         
██║██╔════╝         
██║███████╗         
██║╚════██║         
██║███████║██╗██╗██╗
╚═╝╚══════╝╚═╝╚═╝╚═╝

"""
]

def count_down():

    for word in curtain:
        print(f'\n\n\n{word}')
        time.sleep(1)
        os.system('clear')