# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 Amano Team

from typing import Union

from pyrogram import Client, filters
from pyrogram.helpers import ikb
from pyrogram.types import CallbackQuery, Message


@Client.on_message(filters.sudoers & filters.regex("/help"))
async def on_help_m(c: Client, m: Message):
    await on_help_u(c, m)


@Client.on_callback_query(filters.sudoers & filters.regex("^help"))
async def on_help_cq(c: Client, cq: CallbackQuery):
    await on_help_u(c, cq)


async def on_help_u(c: Client, u: Union[Message, CallbackQuery]):
    is_query = hasattr(u, "data")
    lang = u._lang
    keyb = [
        [(lang.about_userlixo, "about_userlixo")],
        [(lang.commands, "about_commands"), (lang.plugins, "about_plugins")],
        [
            (lang.chat, "https://t.me/UserLixoChat", "url"),
            (lang.channel, "https://t.me/UserLixo", "url"),
        ],
    ]
    keyb = ikb(keyb)
    await (u.edit if is_query else u.reply)(lang.help_text, keyb)
