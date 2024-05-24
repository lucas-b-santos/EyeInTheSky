from accounts.models import User

users = {
    'lucas@gmail.com': '900.362.050-44',
    'joao@gmail.com': '363.624.310-14',
    'felipe@gmail.com': '302.964.130-97',
}

def run():
    for user in users:
        new_user = User(email=user, cpf=users[user])
        new_user.set_password('django123')
        new_user.save()