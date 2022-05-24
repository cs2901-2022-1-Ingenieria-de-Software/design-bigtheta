from command import Command_turn_on, Command_turn_off, Command_switch
from fan import Fan
from light import Red_light, Yellow_light, White_light
from remote_control import Remote_control

def main():
    rc = Remote_control(Command_turn_on, Command_turn_off, Command_switch)
    rc.add_device('fan', Fan())
    rc.add_device('red', Red_light())
    rc.add_device('yellow', Yellow_light())
    rc.add_device('white', White_light())

    remote_control = Remote_control()
    if id(remote_control) == id(rc):
        print(f'Singleton works.')

    #NOTE: Commands turn on, turn off and switch
    remote_control.turn_on('fan')
    remote_control.turn_on('red')
    remote_control.turn_on('yellow')
    remote_control.turn_on('white')
    remote_control.turn_off('yellow')
    remote_control.turn_off('red')
    remote_control.switch('white')
    remote_control.switch('fan')

if __name__ =="__main__":
    main()
