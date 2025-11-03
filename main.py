
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


def main():
    all_passcards = Passcard.objects.all()
    first_passcard = all_passcards[0]

    print('owner_name:', first_passcard.owner_name)
    print('passcode:', first_passcard.passcode)
    print('created_at:', first_passcard.created_at)
    print('is_active:', first_passcard.is_active)

    active_passcards = Passcard.objects.filter(is_active=True)

    print('Всего пропусков:', len(all_passcards))
    print('Активных пропусков:', len(active_passcards))


if __name__ == '__main__':
    main()
