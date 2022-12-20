from sys import exit
import random
from textwrap import dedent

# LUCK OF THE DRAGON
# A text adventure a game

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    def enter(self):
        print("You Died! Game Over!")
        again = input("Do you want to play again? ")
        
        if again == "yes":
            game.play()
        else:
            exit(1)

class Permadeath(Scene):
    def enter(self):
        print("The End.")
        exit(1)

class Gateway(Scene):
    def enter(self):
        print(dedent("""
        You are now standing in front of Hellfire Tower, home to the treacherous
        dragon known by the name Urtho. You have been sent by the people of
        Ghadia to save their Princess and return her back safely. Your reward
        for your bravery shall be legacy and all the richest your heart desires!

        The time has come to enter the tower and complete your quest!
        """))
        print('-' * 60)

        action = input('Write "enter" to step inside and begin the game. ')

        if action != "enter":
            while action != "enter":
                action = input(dedent("""
                That wasn't an acceptable response.
                Write "enter" to step inside and begin the game.
                """))
        else:
            return 'foyer'

class Foyer(Scene):
    def enter(self):
        print(dedent("""
        As you open the front door and enter into the tower you notice that
        there are three doors that you could go through:

        The first door is made of old, rotted wood with weird lettering
        scattered all over it. Kinda of creepy.

        The second door is made of reinforced steel. For some reason it has
        hints of blue, red and orange hues at the bottom and along the sides.

        The third door is just a regular door found in most homes. Looks the
        least threatening out of the bunch.
        """))

        action = input("Pick which door to go through. Enter 1, 2, or 3. ")

        while (action != '1') and (action != '2') and (action != '3'):
            action = input(dedent("""
            That wasn't an acceptable response.
            Which door do you want to go through? Enter 1, 2, or 3.
            """))
        if action == "1":
            print("You chose Door #1...")
            return 'door1'
        elif action == "2":
            print("You chose Door #2...")
            return 'door2'
        elif action == "3":
            print("You chose Door #3...")
            return 'door3'

class CoinToss(Scene):
    def enter(self):
        print(dedent("""
        Uthro flips the coin up in the air and catches it in a closed fist.
        """))

        possibile_outcomes = ['heads', 'tails']

        result = random.choice(possibile_outcomes)
        guess = input(dedent("""
         What side do you think the coin landed on? 'heads' or 'tails'?
         """))

        print(f"\nThe coin landed on {result} amd you chose {guess}.")

        if result == guess:
            print(dedent("""
            You won the coin toss and bested Uthro! He has agreed to let you
            pass, so you head up the stairs of the tower to retrieve the
            Princess. She greets you with a kiss and the two of you travel back
            to the Kingdom of Ghadia.

            Along the way, the two of you formed a bond and a romantic
            relationship. Upon your return she has promised to make you a prince
            and the two of you shall inherit the throne together one day.
            """))

            return 'ghadia'
        else:
            return 'death'

class Door1(Scene):
    def enter(self):
        print(dedent("""
        As you open the door, you accidently walk in on what seems to be a
        secret, Illuminati-esque meeting of Witches and Wizards. Everybody stops
        and looks at you with ill intent in their eyes. You hear a wretched
        voice from the back of the room screech out, 'Kill him! Kill him now!
        He has seen too much!'

        Afraid, you try to run away, but one of them has already casted a
        paralysis spell on you. Now all you can do is watch in horror as these
        magical villians argue on the best spell to end you with.

        After a few hours of debate, they fianlly decide to just stab you with
        the sharpest wand they can find laying around.
        """))

        return 'death'

class Door2(Scene):
    def enter(self):
        print(dedent("""
        This is a tough door to open. Seems like it has been fused shut somehow.
        By putting all your might into it, you're able to pry the door open and
        walk inside. That's when you see Uthro the Dragon sitting upon a pile of
        gold and treasure.

        You call out to him to face you! Uthro slowly rises from his throne,
        and lets out a powerful roar. The sheer force of it all pushes you back
        several steps before you regain composure. You lunge at him and the two
        of you fight a long battle to the death.

        Uthro gets bored with the fight and informs you that no human can defeat
        him for he is immortal and impevious to such attacks. He then proceeds
        to proposition a wager with you. He says if you are able to quess
        correctly the winning side of a coin toss he will allow you to continue
        on and save the Princess. However, if you lose, he will eat you alive
        and burn the remains.
        """))

        action = input(dedent('''
            Do you wish to gamble your life away on a coin toss? Enter "yes" or "no". 
            '''))

        if action == "yes":
            return 'coin_toss'
        elif action == "no":
            print(dedent("""
            Since you didn't want to play Uthro's game, he got tired of you and
            ate you anyway.
            """))
            return 'death'
        else:
            print(dedent('''
            Urtho didn't like that he asked you a "yes" or "no" question and you didn't
            choose either. For that, he tail whipped you against the wall, breaking your
            back.
            '''))
            return 'death'

class Door3(Scene):
    def enter(self):
        print(dedent("""
        You open the door, take a step in through the threshold, and plummet
        down several feet into a pit of sharp, wooden spikes. Impaled on impact,
        you turn to see all the other men of valor that have met the same fate
        as you. Skewered by your own hubris, what an embarassing end to this
        journey...
        """))

        return 'death'

class Ghadia(Scene):
    def enter(self):
        print(dedent("""
        The two of you are welcomed back within the gates of Ghadia with cheers,
        fanfare, and open arms. You all party through the night until the early
        morning.

        At breakfast next morning, it has been shared that the Princess had been
        gone for a very long time, and in that time her parents have passed away.
        The throne is now vacant and needs a successor. The two of you fill the
        void and rule over the land with an iron fist for 30 years.

        One day there is an uprising among the serfs in the villages. One of
        them throws a rock through one of the castle's windows.
        The rock hits you in the head and made you fall over like a sack of
        rustic potatoes, killing you instantly...
        """))

        return 'permadeath'

class Map (object):

    scenes = {
    'death': Death(),
    'permadeath': Permadeath(),
    'gateway': Gateway(),
    'foyer': Foyer(),
    'door1': Door1(),
    'door2': Door2(),
    'coin_toss': CoinToss(),
    'door3': Door3(),
    'ghadia': Ghadia()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

game_map = Map('gateway')
game = Engine(game_map)
game.play()
