from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, username, password):
        for user in self.users:
            if user.nickname == username:
                if hash(password) == user.password:
                    self.current_user = user
                    print(f"Вы вошли в учётную запись {username}")
                else:
                    print(f'Не правильный пароль - {password}')
                return
        print(f'Пользователь {username} не зарегестрирован')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for vid in args:
            if vid != args:
                self.videos.append(vid)

    def get_videos(self, text):
        videos = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                videos.append(video.title)
        return videos

    def watch_video(self, name):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            if self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                for video in self.videos:
                    if name in video.title:
                        for i in range(video.time_now + 1, video.duration + 1):
                            print(i, end=' ')
                            sleep(1)
                        print('Конец видео')

    def __str__(self):
        return f"{self.videos}"


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f"{self.nickname}"


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('3loy_chel', 'lolkekcheburek', 5)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('Lololowka', 'JDH993_chiken', 20)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('3loy_chel', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
