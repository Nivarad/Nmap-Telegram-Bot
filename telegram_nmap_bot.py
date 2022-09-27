from telegram.ext import *
from telegram_bot_inter import TelegramBotInterface
import keys
from nmap_vuln import NmapVuln


class TelegramNmapBot(TelegramBotInterface):

    def __init__(self):
        self.nm = NmapVuln()

    def start_command(self, update, context):
        update.message.reply_text('Hello there! I\'m a Nmap bot .')

    def help_command(self, update, context):
        update.message.reply_text('I can map networks for you in a single click!\n'
                                  'All you need is to give me the ip of the target machine and choose a command '
                                  'and I will do all the rest\n'
                                  'The format of the commands are :\n'
                                  '/open_services <IP_ADDRESS>\n'
                                  '/operating_system <IP_ADDRESS>\n'
                                  '/vulners <IP_ADDRESS>\n'
                                  '/nmap_god <IP_ADDRESS>')

    def open_services_command(self, update, context):
        print("lets nmap this shit")
        ip = extract_ip(update, 's ')
        self.nm.set_ip_address(ip)
        scan_res = self.nm.get_open_services()
        send_message(scan_res, update)

    def operating_system_command(self, update, context):
        print("let's find the operating system")

        ip = extract_ip(update, 'm ')
        self.nm.set_ip_address(ip)
        os = self.nm.get_operating_system()
        send_message(os, update)

    def vulners_command(self, update, context):
        print("let's find vulnerabilities")

        ip = extract_ip(update, 's ')
        self.nm.set_ip_address(ip)
        vulners = self.nm.get_vulnerabilities()
        send_message(vulners, update)

    def do_everything_command(self, update, context):

        ip = extract_ip(update, 'g ')
        self.nm.set_ip_address(ip)
        open_services = self.nm.get_open_services()
        open_services = " The open services are: \n" + open_services
        send_message(open_services, update)
        os = self.nm.get_operating_system()
        send_message(os, update)
        print("starting to check for vulners")
        vulners = self.nm.get_vulnerabilities()
        vulners = "The vulnerabilities are: \n"+vulners
        try:
            send_message(vulners, update)
        except Exception as e:
            print(e)
        print("finished")

    def handle_response(self, update, context):
        if 'hello' or 'hi' in update.message.text:
            update.message.reply_text("Hello there!\n I\'m Nmap bot , try write /help to see what i can do")
        else:
            update.message.reply_text("sorry I dont understand , please write /help")


def send_message(text, update):
    if text == '':
        update.message.reply_text("nothing found , is the host up?\n"
                                  "if you tried to search for vulnerabilities maybe there are none")
    else:
        try:
            if len(text) > 4096:
                for x in range(0, len(text), 4096):
                    part_res = text[x:x + 3000]
                    update.message.reply_text(part_res)
            else:
                update.message.reply_text(text)
        except Exception as e:
            print(e)


def extract_ip(update, command_end):
    text = update.message.text
    ip = text[str(text).find(command_end) + 1:]
    return ip


print('Starting up bot...')
# Run the program
if __name__ == '__main__':
    bot = TelegramNmapBot()

    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', bot.start_command))
    dp.add_handler(CommandHandler('help', bot.help_command))
    dp.add_handler(CommandHandler('open_services', bot.open_services_command))
    dp.add_handler(CommandHandler('operating_system', bot.operating_system_command))
    dp.add_handler(CommandHandler('vulners', bot.vulners_command))
    dp.add_handler(CommandHandler('do_everything', bot.do_everything_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, bot.handle_response))

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
