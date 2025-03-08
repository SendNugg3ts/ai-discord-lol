from config import get_settings
from bot.message_flow import run

def main() -> None:
    run(token=get_settings().DISCORD_BOT_TOKEN)

if __name__ == '__main__':
    main()