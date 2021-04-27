from itertools import combinations
import numpy as np


class ModCard:
    def __init__(self, multiplier=None, damage_mod=None, rolling=None,
                 gen_air=None, gen_dark=None, gen_earth=None,
                 gen_fire=None, gen_ice=None, gen_light=None,
                 poison=None, muddle=None, wound=None,
                 invisible=None, immobilize=None, strengthen=None,
                 regenerate=None, refresh=None, disarm=None,
                 stun=None, add_target=None,
                 heal=None, push=None, pull=None, pierce=None, shield=None,
                 apply_bless=None, apply_curse=None):

        self.multiplier = 1 if multiplier is None else multiplier
        self.damage_mod = 0 if damage_mod is None else damage_mod
        self.rolling = False if rolling is None else rolling
        self.gen_air = False if gen_air is None else gen_air
        self.gen_dark = False if gen_dark is None else gen_dark
        self.gen_earth = False if gen_earth is None else gen_earth
        self.gen_fire = False if gen_fire is None else gen_fire
        self.gen_ice = False if gen_ice is None else gen_ice
        self.gen_light = False if gen_light is None else gen_light
        self.poison = False if poison is None else poison
        self.muddle = False if muddle is None else muddle
        self.wound = False if wound is None else wound
        self.invisible = False if invisible is None else invisible
        self.immobilize = False if immobilize is None else immobilize
        self.strengthen = False if strengthen is None else strengthen
        self.regenerate = False if regenerate is None else regenerate
        self.refresh = False if refresh is None else refresh
        self.disarm = False if disarm is None else disarm
        self.stun = False if stun is None else stun
        self.add_target = False if add_target is None else add_target
        self.heal = 0 if heal is None else heal
        self.push = 0 if push is None else push
        self.pull = 0 if pull is None else pull
        self.pierce = 0 if pierce is None else pierce
        self.shield = 0 if shield is None else shield
        self.apply_bless = 0 if apply_bless is None else apply_bless
        self.apply_curse = 0 if apply_curse is None else apply_curse

    def __repr__(self):
        repr_items = []
        if self.multiplier != 1:
            repr_items.append('(multiplier, ' + str(self.multiplier) + ')')

        repr_items.append('(damage_mod, ' + str(self.damage_mod) + ')')

        for key, val in self.__dict__.items():
            if key != 'multiplier' and key != 'damage_mod' and bool(val):
                repr_items.append('(' + key + ', ' + str(val) + ')')

        return '['+', '.join(repr_items)+']'

    def __eq__(self, other):
        if not isinstance(other, ModCard):
            return NotImplemented
        return self.__dict__ == other.__dict__


class ModDeck:
    def __init__(self):
        self.deck = []
        self.add_card(1, ModCard(damage_mod=-2))
        self.add_card(5, ModCard(damage_mod=-1))
        self.add_card(6, ModCard(damage_mod=0))
        self.add_card(5, ModCard(damage_mod=1))
        self.add_card(1, ModCard(damage_mod=2))
        self.add_card(1, ModCard(multiplier=2))
        self.add_card(1, ModCard(multiplier=0))

    def add_card(self, quantity, card):
        for _ in range(quantity):
            self.deck.append(card)

    def remove_card(self, quantiy, card_to_remove):
        print(card_to_remove)
        for _ in range(quantiy):
            for card in self.deck:
                if card == card_to_remove:
                    self.deck.remove(card_to_remove)
                    break

    def add_bless(self, quantity):
        for _ in range(quantity):
            self.deck.append(ModCard(multiplier=2))

    def add_curse(self, quantity):
        for _ in range(quantity):
            self.deck.append(ModCard(multiplier=0))

    def compute_rolls(self):
        deck = self.deck.copy()
        self.rolls = []
        roll_check = False
        for card in deck:
            self.rolls.append([card])
            if card.rolling:
                roll_check = True

        while roll_check:
            terminating_roll = False
            for i, roll in enumerate(self.rolls):
                if roll[-1].rolling:
                    terminating_roll = True
                    new_roll = []
                    temp_deck = deck.copy()
                    for card in roll:
                        temp_deck.remove(card)
                    for card in temp_deck:
                        temp_roll = roll.copy()
                        temp_roll.append(card)
                        new_roll.append(temp_roll)
                    self.rolls[i:i+1] = new_roll
            if not terminating_roll:
                roll_check = False
