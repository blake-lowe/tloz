class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.inventory = []
        self.target_name = ""
        self.target_num = ""
        
    def is_alive(self):
        return self.hp > 0
    
    def is_targeting(self, Enemy):
        if self.target_name == Enemy.name and self.target_num == Enemy.num:
            return True
        else:
            return False

    def target(self, Enemy):
        self.target_name = Enemy.name
        self.target_num = Enemy.num
        
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
