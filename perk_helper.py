class ModCard:
    '''
    TODO: add repr that returns values different than defaults
    '''

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

        arugments = locals()
        self.repr_str = '['
        count = 0
        for arg, val in zip(arugments, arugments.values()):
            if val is not None and arg is not 'self':
                if count != 0:
                    self.repr_str += ', '
                count += 1

                self.repr_str += '(' + str(arg) + ', ' + str(val) + ')'

        self.repr_str += ']'

    def __repr__(self):
        return self.repr_str


class ModDeck:
    def __init__(self):
        self.deck = []
        self.add_card(1, damage_mod=-2)
        self.add_card(5, damage_mod=-1)
        self.add_card(6, damage_mod=0)
        self.add_card(5, damage_mod=1)
        self.add_card(1, damage_mod=2)
        self.add_card(1, multiplier=2)
        self.add_card(1, multiplier=0)

    def add_card(self, quantity, multiplier=None, damage_mod=None, rolling=None,
                 gen_air=None, gen_dark=None, gen_earth=None,
                 gen_fire=None, gen_ice=None, gen_light=None,
                 poison=None, muddle=None, wound=None,
                 invisible=None, immobilize=None, strengthen=None,
                 regenerate=None, refresh=None, disarm=None,
                 stun=None, add_target=None,
                 heal=None, push=None, pull=None, pierce=None, shield=None,
                 apply_bless=None, apply_curse=None):
        for _ in range(quantity):
            self.deck.append(ModCard(multiplier=multiplier, damage_mod=damage_mod, rolling=rolling,
                                     gen_air=gen_air, gen_dark=gen_dark, gen_earth=gen_earth,
                                     gen_fire=gen_fire, gen_ice=gen_ice, gen_light=gen_light,
                                     poison=poison, muddle=muddle, wound=wound,
                                     invisible=invisible, immobilize=immobilize, strengthen=strengthen,
                                     regenerate=regenerate, refresh=refresh, disarm=disarm,
                                     stun=stun, add_target=add_target,
                                     heal=heal, push=push, pull=pull, pierce=pierce, shield=shield,
                                     apply_bless=apply_bless, apply_curse=apply_curse))

    def remove_card(self, quantiy):
        pass

    def add_bless(self, quantity):
        for _ in range(quantity):
            self.deck.append(ModCard(multiplier=2))

    def add_curse(self, quantity):
        for _ in range(quantity):
            self.deck.append(ModCard(multiplier=0))