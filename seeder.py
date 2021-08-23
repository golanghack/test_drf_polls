from polls.models import Choice, Poll, Vote
from django.contrib.auth.models import User
import datetime
import random
import time
from faker import Faker


fake = Faker()


def seed_users(num_entries=10, overwrite=False):
    """
    создаем новых пользователей(точнее, соответствующие им num_entries)
    """
    if overwrite:
        print("Перезаписать пользователей")
        Users.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        first_name = fake.first_name()
        last_name = fake.last_name()
        u = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=first_name + "." + last_name + "@fakermail.com",
            username=first_name + last_name,
            password="password"
        )
        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Добавление  {} новых пользователей: {:.2f}%".format(
                num_entries, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_polls(num_entries=10, choice_min=2, choice_max=5, overwrite=False):
    """
   рендомное добавление опросов от минимального числа к максимальному
    """
    if overwrite:
        print('Перезапись')
        Poll.objects.all().delete()
    users = list(User.objects.all())
    count = 0
    for _ in range(num_entries):
        p = Poll(
            owner=random.choice(users),
            text=fake.paragraph(),
            pub_date=datetime.datetime.now()
        )
        p.save()
        num_choices = random.randrange(choice_min, choice_max + 1)
        for _ in range(num_choices):
            c = Choice(
                poll=p,
                choice_text=fake.sentence()
            ).save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Довавление {} новых опросов: {:.2f}%".format(
                num_entries, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_votes():
    """
    Создает новый голос в каждом опросе для каждого пользователя
     Проголосовавший за выбор выбирается случайным образом.
     Удаляет все голоса перед добавлением новых 
    """
    Vote.objects.all().delete()
    users = User.objects.all()
    polls = Poll.objects.all()
    count = 0
    number_of_new_votes = users.count() * polls.count()
    for poll in polls:
        choices = list(poll.choice_set.all())
        for user in users:
            v = Vote(
                user=user,
                poll=poll,
                choice=random.choice(choices)
            ).save()
            count += 1
            percent_complete = count / number_of_new_votes * 100
            print(
                "Добавление {} новых голосов: {:.2f}%".format(
                    number_of_new_votes, percent_complete),
                end='\r',
                flush=True
            )
    print()


def seed_all(num_entries=10, overwrite=False):
    """
    передает перезапись.
    """
    start_time = time.time()
    # запуск
    seed_users(num_entries=num_entries, overwrite=overwrite)
    seed_polls(num_entries=num_entries, overwrite=overwrite)
    seed_votes()
    # получение времени
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Выполнение этого сценария заняло: {} минут и  {} секунд".format(minutes, seconds))
