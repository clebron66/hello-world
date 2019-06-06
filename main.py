from undercover import *
from peanutbutter import *
from telepathy import *
from attack import *

# "Aliens Intergalactic Marvel"
TITLE = '''  

            _  _                _____         _                            _               _    _         __  __                           _ 
     /\    | |(_)              |_   _|       | |                          | |             | |  (_)       |  \/  |                         | |
    /  \   | | _   ___  _ __     | |   _ __  | |_  ___  _ __  __ _   __ _ | |  __ _   ___ | |_  _   ___  | \  / |  __ _  _ __ __   __ ___ | |
   / /\ \  | || | / _ \| '_ \    | |  | '_ \ | __|/ _ \| '__|/ _` | / _` || | / _` | / __|| __|| | / __| | |\/| | / _` || '__|\ \ / // _ \| |
  / ____ \ | || ||  __/| | | |  _| |_ | | | || |_|  __/| |  | (_| || (_| || || (_| || (__ | |_ | || (__  | |  | || (_| || |    \ V /|  __/| |
 /_/    \_\|_||_| \___||_| |_| |_____||_| |_| \__|\___||_|   \__, | \__,_||_| \__,_| \___| \__||_| \___| |_|  |_| \__,_||_|     \_/  \___||_|
                                                              __/ |                                                                          
                                                             |___/                                                                           
'''
AUTHOR = '''

 __                         ______             __              __      __        __                  _______                                
/  |                       /      \           /  |            /  |    /  |      /  |                /       \                               
$$ |____   __    __       /$$$$$$  |  ______  $$/   _______  _$$ |_   $$/       $$ |        ______  $$$$$$$  |  ______    ______   _______  
$$      \ /  |  /  |      $$ |  $$/  /      \ /  | /       |/ $$   |  /  |      $$ |       /      \ $$ |__$$ | /      \  /      \ /       \ 
$$$$$$$  |$$ |  $$ |      $$ |      /$$$$$$  |$$ |/$$$$$$$/ $$$$$$/   $$ |      $$ |      /$$$$$$  |$$    $$< /$$$$$$  |/$$$$$$  |$$$$$$$  |
$$ |  $$ |$$ |  $$ |      $$ |   __ $$ |  $$/ $$ |$$      \   $$ | __ $$ |      $$ |      $$    $$ |$$$$$$$  |$$ |  $$/ $$ |  $$ |$$ |  $$ |
$$ |__$$ |$$ \__$$ |      $$ \__/  |$$ |      $$ | $$$$$$  |  $$ |/  |$$ |      $$ |_____ $$$$$$$$/ $$ |__$$ |$$ |      $$ \__$$ |$$ |  $$ |
$$    $$/ $$    $$ |      $$    $$/ $$ |      $$ |/     $$/   $$  $$/ $$ |      $$       |$$       |$$    $$/ $$ |      $$    $$/ $$ |  $$ |
$$$$$$$/   $$$$$$$ |       $$$$$$/  $$/       $$/ $$$$$$$/     $$$$/  $$/       $$$$$$$$/  $$$$$$$/ $$$$$$$/  $$/        $$$$$$/  $$/   $$/ 
          /  \__$$ |                                                                                                                        
          $$    $$/                                                                                                                         
           $$$$$$/                                                                                                                          
                                                                                                               
                                                                                                                  

'''
INTRO = '''
  These earthlings are not using their full potential. They are eating
  peanut butter, but it is the most precious resources in the universe, since
  it allows for intergalactic travel.If our race is to survive, we must obtain
  as much of it as possible.
'''


HERO= "Zywgeh"
FIRST_PROMPT = f'''
  You are an alien named {HERO} from a galaxy far, far away. A monumental task
  has been laid ahead of you by high command. From your mission depends the
  future of our planet. You are sent to carry out a secret operation to steal
  peanut butter from the Earth.
  How will you first infiltrate Planet Earth?
'''
FIRST_PROMPT_OPTIONS='''
  1) Become an undercover earthling.
  2) Give humans the power of telepathy in the hopes they engage in civil war.
  3) Become a peanut butter jar. 
  4) Attack the humans.

>>
'''

def main():
    print(TITLE)
    print(AUTHOR)
    print(INTRO)
    print(FIRST_PROMPT)
    infiltrate_option = int(input(FIRST_PROMPT_OPTIONS))
    #choose your adventure
    if infiltrate_option == 1:
        undercover_narrative()
    elif infiltrate_option == 2:
        telepathy_narrative()
    elif infiltrate_option == 2:
        peanut_butter_narrative()
    else:
        attack_narrative()



if __name__ == "__main__":
    main()


