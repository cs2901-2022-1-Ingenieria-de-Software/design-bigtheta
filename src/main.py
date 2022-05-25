from command import CommandTurnOn, CommandTurnOff, CommandSwitch
from fan import Fan
from light import RedLight, YellowLight, WhiteLight
from remote_control import Remote_control

def main():
    rc = Remote_control(CommandTurnOn, CommandTurnOff, CommandSwitch)
    rc.add_device('fan', Fan())
    rc.add_device('red', RedLight())
    rc.add_device('yellow', YellowLight())
    rc.add_device('white', WhiteLight())

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
