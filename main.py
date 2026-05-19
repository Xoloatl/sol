from colorama import Fore, Style, init
from brain.router import route

init(autoreset=True)

SOL_COLORS = {
    "heart": Fore.MAGENTA,
    "planner": Fore.CYAN,
    "doer": Fore.GREEN
}

SOL_LABELS = {
    "heart": "SOL ♥",
    "planner": "SOL ◆",
    "doer": "SOL ⚙"
}

def print_sol(result):
    intent = result["intent"]
    color = SOL_COLORS[intent]
    label = SOL_LABELS[intent]
    print(f"\n{color}{label}: {result['response']}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{intent} | {result['model']}]{Style.RESET_ALL}\n")

def main():
    print(f"\n{Fore.YELLOW}{'='*50}")
    print("  SOL — Sympathetic Operating System")
    print(f"{'='*50}{Style.RESET_ALL}")
    print("Type 'quit' to exit\n")

    while True:
        try:
            user_input = input(f"{Fore.WHITE}You: {Style.RESET_ALL}").strip()
            if not user_input:
                continue
            if user_input.lower() in ["quit", "exit", "bye"]:
                print(f"\n{Fore.YELLOW}SOL: Take care! I'll be here when you need me.{Style.RESET_ALL}\n")
                break
            result = route(user_input)
            print_sol(result)
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}SOL: Goodbye!{Style.RESET_ALL}\n")
            break

if __name__ == "__main__":
    main()