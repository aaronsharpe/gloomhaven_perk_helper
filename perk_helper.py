from itertools import combinations
from collections import defaultdict
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
        self.add_target = 0 if add_target is None else add_target
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

    def merge(self, card):
        card_merged = ModCard()
        card_merged.damage_mod = self.damage_mod + card.damage_mod
        card_merged.multiplier = self.multiplier * card.multiplier

        card_merged.rolling = self.rolling and card.rolling
        card_merged.gen_air = self.gen_air or card.gen_air
        card_merged.gen_dark = self.gen_dark or card.gen_dark
        card_merged.gen_earth = self.gen_earth or card.gen_earth
        card_merged.gen_fire = self.gen_fire or card.gen_fire
        card_merged.gen_ice = self.gen_ice or card.gen_ice
        card_merged.gen_light = self.gen_light or card.gen_light
        card_merged.poison = self.poison or card.poison
        card_merged.muddle = self.muddle or card.muddle
        card_merged.wound = self.wound or card.wound
        card_merged.invisible = self.invisible or card.invisible
        card_merged.immobilize = self.immobilize or card.immobilize
        card_merged.strengthen = self.strengthen or card.strengthen
        card_merged.regenerate = self.regenerate or card.regenerate
        card_merged.refresh = self.refresh or card.refresh
        card_merged.disarm = self.disarm or card.disarm
        card_merged.stun = self.stun or card.stun
        card_merged.add_target = self.add_target + card.add_target
        card_merged.heal = self.heal + card.heal
        card_merged.push = self.push + card.push
        card_merged.pull = self.pull + card.pull
        card_merged.pierce = self.pierce + card.pierce
        card_merged.shield = self.shield + card.shield
        card_merged.apply_bless = self.apply_bless + card.apply_bless
        card_merged.apply_curse = self.apply_curse + card.apply_curse

        return card_merged


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

        self.stats = self.compute_stats(self.rolls)

    def compute_stats(self, rolls):
        rolls_merged = []
        for roll in rolls:
            card_merged = ModCard()
            for card in roll:
                card_merged = card_merged.merge(card)
            rolls_merged.append(card_merged)

        stats_merged = defaultdict(list)
        for roll in rolls_merged:
            for key, val in roll.__dict__.items():
                stats_merged[key].append(val)

        stats = {}
        for key in stats_merged.keys():
            stats[key] = np.mean(stats_merged[key])

        stats['crit'] = stats_merged['multiplier'].count(
            2)/len(stats_merged['multiplier'])
        stats['miss'] = stats_merged['multiplier'].count(
            0)/len(stats_merged['multiplier'])
        return stats
