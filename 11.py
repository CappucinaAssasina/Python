brainrotInput = input("Name the brainrot you want:")
rarityInput = input("Mention its rarity:")
valueInput = input("Give its value:")

class StealABrainrot:
    def __init__(self,brainrot,rarity,value):
        self.brainrot = brainrot
        self.rarity = rarity
        self.value = value
        
    def Brainrot(self):
        print(f"""
              Congrats you won this brainrot:
              Name: {self.brainrot}
              Rarity: {self.rarity}
              Value: {self.value}
              """)
        
class BrainrotUpdate(StealABrainrot):
    def __init__(self, brainrot, rarity, value):
        super().__init__(brainrot, rarity, value)

AdminAbuse = BrainrotUpdate(brainrotInput,rarityInput,valueInput)

AdminAbuse.Brainrot()

from abc import ABC, abstractmethod

class StealABrainRot(ABC):
    def BrainRot(self):
        pass

class Update(StealABrainRot):
    def Event_Start(self):
        print("The new admin update has started")

    def Event_End(self):
        print("The new admin update has ended")

Event = Update()

Event.Event_Start()
Event.Event_End()