from sys import exit
from random import randint
class Game(object):
 
    def __init__(self, start):
        self.quips = [
            "you died, you kinda suck at this."
            "you mom would be proud. if she were smater."
            "Such a loser."
            "I have a small puppy that's better at this."
        ]
        self.start = start
        
    def play(self):
        next = self.start
        
        while True:
            print ("\n-----------")
            room = getattr(self, next)
            next = room()
        
    def death(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
        
    def princess_lives_here(self):
        print ("You see a beautiful  princess with a shiny crown.")
        print ("She offers you some cake.")
        
        eat_it = raw_input("> ")
        
       if eat_it == "eat it":
           print ("You explode like a pinata full of frogs.")
           print ("The princess cackles and eats the frogs. Yum!")
           return 'death'
            
        elif eat_it == "do not eat it":
            print ("She throws the cake at you and it cuts off  your head.")
            print ("The last thing you see is her munching on your torso. Yum!")
            return 'death'
            
        elif eat_it =="make her eat it":
            print ("The princess screams as you cram the cake it her mouth.")
            print ("Then she smiles and cries and thanks you for saving her.")
            print ("She points to a tiny door and says, 'The Koi needs cake too.'")
            
        else:
            print ("The princess looks at you confused and just points at the cake.")
            return 'princess_lives_here'
            
    def gold_koi_pond(self):
        print ("There is a garden with a koi pond in the center.")
        print ("You walk close and see a smassive fin poke out.")
        print ("You peek in and a creepy looking huge koi stares at you.")
        print ("It opnes its mouth waiting for food.")
        
        feed_it = raw_input("> ")
        
        if feed_it ==" feed it":
            print ("The koi jumps up, and rather than eating the cake, eats your arm.")
            print ("You fall in and the koi shrugs than eats you.")
            print ("You are then pooped out sometime later.")
            return 'dead'
            
        elif feed_it == "do not feed it":
            print ("The koi frimaces, then thrashes around for a second.")
            print ("It rushes to the other end of the pond, braces against the wall.")
            print ("Then it *lunges* out of the water, up in the air and over your")
            print ("entire body, cake and all.")
            print ("You are then pooped out a week later.")
            return 'death'
            
        elif feed_it == "throw it in":
            print ("The koi wiggles, then leaps into the air to eat the cake.")
            print ("You can see it's happy, it then grunts, thrashes...")
            print ("And finnally rolls over and poops a magic diamond into the air")
            print ("at your feet.")
            
            return 'bear_with_sword'
            
        else:
            print ("The koi gets annoyed and wiggles a bit.")
            return 'gold_koi_pond'
            
    def bear_with_sword(self):
        print ("Puzzled, you are about to pick up the fish poop diamond when")
        print ("a bear bearing a load bearing sword walks in.")
        print ("Hey! That\'s my diamond! Where\'d you get that !?")
        print ("It holds its paw out and looks at you.")
        
        give_it = raw_input("> ")
        
        if give_it == "give it":
            print ("The bear swipes at your hand to grab the diamond dand")
            print ("rips your hand off in the process.  It then looks at")
            print (' your bloody stump and say, "oh crap, sorry about that." ')
            print (" it tries to put your hand back on, but you collapse.")
            print ("the last thing you see is the bar shrug and eat you.")
            return 'death'
            
        elif give_it ==" say no":
            print ("The bear looks shocked. nobody ever told a bear")
            print ("with a broadsword 'no'. It asks, ")
            print ('" Is it beacuse it\'s not a katana?  I cound go et one!"')
            print ("It then runs off and now you notice a big iron gate.")
            print ('"Where the hell did that come from" You say.')
            
            return 'big_iron_gate'
            
    def big_iron_gate(self):
        print ("You walk up to the big iron gate and see there's a handle.")
        
        open_it = raw_input("> ")
        if open_it == 'open it':
            print ("You open it and you are free!")
            print ("There are mountains. And berries! And...")
            print ("Oh, but then the bear comes with his katana and stabs you.")
            print ('"Who\'s laughing now!?  Love this katana."')
            
            return 'death'
            
        else:
            print ("That doesn't seem sensible,  I mean, the door's right there.")
            return 'big_iron_gate'
            
a_game = Game("princess_lives_here")
a_game. play()
