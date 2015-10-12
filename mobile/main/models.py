from django.db import models

class Context(models.Model):
    """ the current context of the game """

    """ the current quest or null """
    quest = models.ForeignKey('Quest', null=True)

    PASSWORD = 'PWD'
    SUCCESS = 'SUC'
    HACKING = 'HAK'
    STATE_CHOICES = (
        (PASSWORD, 'Password'),
        (SUCCESS, 'Success'),
        (HACKING, 'Hacking'),
    )

    """ the current state or null """
    state = models.CharField(max_length=3, choices=STATE_CHOICES, null=True)

    def __str__(self):
        if self.quest is None:
            return "No quest started"
        else:
            return "Current quest: " + self.quest.name

    @staticmethod
    def get_context():
        """ return the context (it should be a singleton) """
        context, created = Context.get_or_create(defaults={
            'quest': None, 'state': None
        })
        return context;

class Quest(models.Model):

    name = models.TextField()

    PASSWORD = 'PWD'
    ENIGMA = 'ENI'
    HACK = 'HAK'
    TYPE_CHOICES = (
        (PASSWORD, 'Password'),
        (ENIGMA, 'Enigma'),
        (HACK, 'Hack'),
    )
    quest_type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    password = models.CharField(max_length=512, blank=True,
        help_text='the password the player has to type if any,' + \
        ' left it blank for hacking quest')

    enigma = models.TextField(blank=True,
        help_text='the enigma to display to user, left it blank for no enigma quest')

    mini_game = models.ForeignKey('MiniGame', null=True,
        help_text="the mini-game, don't set it for no hacking quest")

    def __str__(self):
        return self.name

class MiniGame(models.Model):

    name = models.TextField()

    def __str__(self):
        return self.name
