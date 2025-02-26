# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 Amano Team

import re

from pyrogram import Client, filters
from pyrogram.helpers import force_reply, ikb
from pyrogram.types import Message

from userlixo.config import sudoers
from userlixo.database import Config


@Client.on_message(filters.sudoers & filters.regex("^/(start )?add_sudoer"))
async def on_add_sudoer(c: Client, m: Message):
    lang = m._lang
    text = lang.add_sudoer_ask
    response = await m.chat.ask(text, filters.text, 600, reply_markup=force_reply())

    if not re.match(r"@?\w+$", response.text):
        return await m.reply(lang.add_sudoer_not_match)

    sudoers.append(response.text.lstrip("@"))
    await Config.get(key="SUDOERS_LIST").update(value=" ".join(map(str, sudoers)))

    keyb = ikb([[(lang.back, "setting_sudoers")]])
    await m.reply(lang.sudoer_added, keyb)
