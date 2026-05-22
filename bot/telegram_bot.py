import asyncio
import os
import telegram


async def _wyslij(token: str, chat_id: str, wiadomosc: str):
    bot = telegram.Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=wiadomosc, parse_mode="HTML")


def wyslij_leady(leady: list[dict]):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("  [Telegram] Brak tokena — pomijam wysyłkę.")
        return

    for lead in leady:
        msg = (
            f"🍽️ <b>Nowy lead — {lead['zrodlo']}</b>\n\n"
            f"<b>{lead['tytul']}</b>\n"
            f"{lead['opis']}\n\n"
            f"🔗 {lead['link']}"
        )
        asyncio.run(_wyslij(token, chat_id, msg))
    print(f"  [Telegram] Wysłano {len(leady)} leadów.")
