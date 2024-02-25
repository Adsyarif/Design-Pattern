class CPU:
    def start(self):
        print("CPU is starting")


class Memory:
    def load(self):
        print("Memory is loading data")


class HardDrive:
    def read(self):
        print("HardDrive is reading data")


class PowerSupply:
    def turn_on(self):
        print("Powersupply is turning on")


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
        self.power_supply = PowerSupply()

    def start_computer(self):
        print("Starting the computer")
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        self.power_supply.turn_on()


computer_fascade = Computer()
computer_fascade.start_computer()
