from main import *
def PrintBanner():
    print(
        f"""
                {Fore.MAGENTA}UPTF - Ultimate purple-team framework
                {Fore.MAGENTA}Dev By : @JerrDeadSec{Style.RESET_ALL}
            ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⣠⣴⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢾⡇⠀⢀⣀⣀⣀⡀⢉⡽⠁⠀⠀⣿⣦⠤⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠸⡷⠀⣀⠤⠤⢤⣴⡿⠁⠀⢰⠀⣿⣿⣷⣤⠶⢶⣬⣭⣕⣒⠠⢄⣀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⡇⠀⠀⡞⣾⠁⠀⠀⠘⠀⠹⣇⣀⣙⡆⠀⠀⠈⠉⠙⠛⠷⠮⣉⠲⢄⡀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣀⢸⡀⢰⢃⣿⣧⣴⡶⣿⣿⡶⢼⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠛⠷⣤⡀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡏⠀⡇⢸⢻⣿⣿⣿⣶⣌⣻⣿⣿⣿⣥⣼⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⢱⢸⢺⣿⣿⣥⠈⠛⠣⢤⣙⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⠈⣿⣼⣿⣿⣿⡾⠆⠀⠙⣿⣿⠇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢯⠀⢻⣿⣿⣿⣿⣶⣶⣷⣾⣿⣣⣴⣾⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠖⢿⡆⠸⣏⢳⡼⣿⣿⣿⣿⣿⣟⠉⠙⠛⠋⣭⣷⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⢰⣿⣷⡄⣿⣾⣟⠬⣿⣿⣿⣿⣿⠀⢀⠀⣠⠟⠁⠀⠲⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⣼⣿⠢⠬⣭⣿⣿⣧⢸⣿⣯⡑⠦⣾⣿⡟⣡⣔⣁⠴⢟⣱⠂⠀⠀⠈⢻⡀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⣠⣾⠋⠀⣄⢀⣿⣿⢿⣷⠀⣿⢧⡙⢦⣙⣿⣿⣽⣿⣁⣹⠟⠛⢀⡇⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣰⠃⣏⣹⣦⣿⣿⡿⠁⠀⢿⣇⢘⡶⢬⣉⣿⣽⣿⣟⣻⣤⠆⣠⣺⣾⡇⡂⠀⢠⠘⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⢰⡇⢰⠃⢛⣿⣯⣉⣠⣤⣶⣿⣿⣿⣿⣿⠀⣈⣛⣿⡿⠟⢀⠜⠁⣹⣿⣷⣿⠀⣸⢰⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⣿⢣⠇⠀⣾⣿⣿⣟⣏⡜⢧⣬⣿⣿⣯⣽⣀⣿⣿⣟⣁⠔⠁⠀⠀⣽⣿⣿⠏⢀⣿⠈⡇⠀⠀⠀⠀⠀⠀
            ⠀⡼⠃⣨⣤⣴⣿⢃⢹⢻⡾⠀⠘⢿⣿⣟⠘⣿⣿⠿⣿⣏⣄⣀⡀⡀⠀⣸⡿⣿⠇⢈⡏⠀⡇⠀⠀⠀⠀⠀⠀
            ⠀⡇⣾⠿⠟⢛⠇⡸⣾⢸⡇⣀⣦⣈⣿⣿⡆⢯⣀⣲⠛⠉⠉⠑⠾⣿⢃⣿⡇⠌⠀⣼⡗⠀⡇⠀⠀⠀⠀⠀⠀
            ⢀⣧⠁⠀⣠⠊⠀⢳⠃⠘⠇⠿⣿⣿⣿⣿⡆⢸⣿⣷⣤⣀⣠⠤⠊⢀⣼⣿⡄⢀⠼⣿⡇⢸⡇⠀⠀⠀⠀⠀⠀
            ⠈⠙⣇⢻⣿⣦⣴⣃⡄⠀⢀⠀⠈⣿⡀⠹⣿⠒⡿⠟⠛⢋⡤⠒⢁⢾⣿⠙⡠⠋⠀⠛⠁⣸⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠈⠓⠾⣅⣈⣉⣀⠀⠠⢷⡀⢸⣆⣠⣿⡄⢻⣴⣾⡏⠀⠀⠀⣾⣷⣾⣷⠒⢉⡀⢀⢿⡇⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣾⣧⣸⣿⣿⣿⣧⠈⡿⣟⡠⢀⠄⣠⣿⣿⠟⢛⡉⠛⠀⡞⣼⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⡿⢸⣿⣏⣿⣿⣿⣿⣿⣽⡀⢹⠰⣚⣯⣾⣿⣿⡟⠉⠀⢀⡀⢠⢷⡇⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⣿⡿⣿⡿⣿⣿⣿⣿⣷⠈⣦⣿⡯⠀⡾⠋⠁⠰⣶⡟⢁⠎⣿⠁⠀⠀⠀⠀⠀⠀⠀
        {Style.RESET_ALL}
                -=[ UPTF v0.1-dev           ]=-
                -=[ Copyright By {Fore.BLUE}Jerr{Style.RESET_ALL}       ]=-
                -=[ Twitter : {Back.GREEN}@JerrDeadSec{Style.RESET_ALL}  ]=-
                -=[ Email : jerr@gmail.com  ]=-

                  1 for redteam 2 for blueteam
        """
    )
