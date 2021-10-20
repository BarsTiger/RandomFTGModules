from .. import loader, utils
import random


@loader.tds
class YesNoMod(loader.Module):
    """Делает выбор за тебя в самых важных ситуациях"""
    strings = {"name": "ДаНет",
               "yes_words_cfg_doc": "Слова Да",
               "no_words_cfg_doc": "Слова Нет"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            "YES_WORDS", ["Да", "Ага", "Абсолютно", "Угу"], lambda m: self.strings("yes_words_cfg_doc", m),
            "NO_WORDS", ["Нет", "Не-а", "Отрицательно", "Нееее"], lambda m: self.strings("no_words_cfg_doc", m))

    @loader.unrestricted
    async def данетcmd(self, message):
        """Выбирает жизнь"""
        yes = self.config["YES_WORDS"]
        no = self.config["NO_WORDS"]
        if random.getrandbits(1):
            response = random.choice(yes)
        else:
            response = random.choice(no)
        await utils.answer(message, response)
