# havamal_bot

Telegram bot that quotes "Words if High One", Elder Edda.
Another function - rune divination(runes of Elder Futhark)

**Commands:**
- /words - get random qoute
- /word \<number\> - get specific quote (from 1 to 164) 
- /runes - get 3 random rune with short description
- /next - next word of High One, progress saved by user_id

**Used:**
- python 2.7
- [Teleport framework](https://github.com/nickoala/telepot)
- SQLite
- Redis

### TODO
- [ ] try webhook (Flask, aiohttp), more info in teleport readme
