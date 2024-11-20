class Weapon:
    def __init__(self, name, damage, damage_type, weapon_type, health, properties):
        self.name = name                  
        self.damage = damage              
        self.damage_type = damage_type    
        self.weapon_type = weapon_type    
        self.health = health                            
        self.properties = properties      

    def __str__(self):

        properties_str = ', '.join(self.properties) if self.properties else "None"
        return (f"Weapon: {self.name}\n"
                f"Damage: {self.damage} {self.damage_type}\n"
                f"Type: {self.weapon_type}\n"
                f"health: {self.health}\n"
                f"Properties: {properties_str}")

weapon = Weapon()
if __name__=="__main__":

    sword = Weapon(name="Longsword", damage="15", damage_type="slashing", 
                   weapon_type="melee",
                   properties=["None"])


    sword = Weapon(name="Firesword", damage="20", damage_type="Burning", 
                   weapon_type="melee",
                   properties=["Fire"])


    sword = Weapon(name="Shortsword", damage="12", damage_type="slashing", 
                   weapon_type="melee",
                   properties=["None"])


    sword = Weapon(name="Icesword", damage="18", damage_type="Freezing", 
                   weapon_type="melee",
                   properties=["Ice"])


    sword = Weapon(name="Windblade", damage="16", damage_type="Cutting", 
                   weapon_type="melee",
                   properties=["Wind"])


    Staff = Weapon(name="Firestaff", damage="16", damage_type="Burning", 
                   weapon_type="Magic",
                   properties=["Fire_Magic"])


    Staff = Weapon(name="Windstaff", damage="16", damage_type="Cutting", 
                   weapon_type="Magic",
                   properties=["Wind_Magic"])


    Staff = Weapon(name="Icestaff", damage="16", damage_type="Freezing", 
                   weapon_type="Magic",
                   properties=["Ice_Magic"])


    Staff = Weapon(name="Waterstaff", damage="16", damage_type="Drowning", 
                   weapon_type="Magic",
                   properties=["Water_Magic"])


    Staff = Weapon(name="Earthstaff", damage="16", damage_type="Crushing", 
                   weapon_type="Magic",
                   properties=["Earth_Magic"])



    shield = Weapon(name="Absorbtionshield", damage="500", damage_type="Absorbtion", health="10",
                   weapon_type="Defense",
                   properties=["Absorb_entities"])


    shield = Weapon(name="Fireshield", damage="12", damage_type="Fire", health="20",
                   weapon_type="Defense",
                   properties=["Fire_Magic"])


    shield = Weapon(name="shield", damage="10", damage_type="Blocking", health="25",
                   weapon_type="Defense",
                   properties=["None"])


    shield = Weapon(name="Drangon-glasshield", damage="12", damage_type="Magic_protection", health="30",
                   weapon_type="Defense",
                   properties=["Ice_blocking"])


    shield = Weapon(name="Praesidium", damage="10", damage_type="Barrier", health="50",
                   weapon_type="Defense",
                   properties=["Defense_Magic"])


    Bow = Weapon(name="Longbow", damage="15", damage_type="Piercing", 
                   weapon_type="piercing",
                   properties=["Piercing"])


    Bow = Weapon(name="Flamebow", damage="20", damage_type="Flame", 
                   weapon_type="piercing",
                   properties=["Fire"])


    Bow = Weapon(name="Frostbite", damage="20", damage_type="Freezing", 
                   weapon_type="piercing",
                   properties=["Ice"])


    Bow = Weapon(name="The-crippler", damage="100", damage_type="Crippling", 
                   weapon_type="piercing",
                   properties=["Crippling"])


    Bow = Weapon(name="Boombow", damage="25", damage_type="Explosion", 
                   weapon_type="piercing",
                   properties=["Explosion"])
    
    