import datetime
import pickle

def load_streaks(filename='streaks.pkl'):
    try:
        with open(filename, 'rb') as file:
            streaks = pickle.load(file)
    except FileNotFoundError:
        streaks = {}
    return streaks

def save_streaks(streaks, filename='streaks.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(streaks, file)

def update_streak(username, streaks):
    if username in streaks:
        last_login_date = streaks[username]['last_login_date']
        current_date = datetime.date.today()
        if current_date - last_login_date == datetime.timedelta(days=1):
            streaks[username]['streak'] += 1
        elif current_date > last_login_date:
            streaks[username]['streak'] = 1
        streaks[username]['last_login_date'] = current_date
    else:
        streaks[username] = {'streak': 1, 'last_login_date': datetime.date.today()}
    return streaks

def display_streak(username, streaks):
    if username in streaks:
        streak = streaks[username]['streak']
        print(f"Current streak for {username}: {streak} days")
    else:
        print(f"No streak information found for {username}")

def main():
    username = input("Enter your username: ")
    streaks = load_streaks()
    streaks = update_streak(username, streaks)
    save_streaks(streaks)
    display_streak(username, streaks)

if __name__ == "__main__":
    main()
