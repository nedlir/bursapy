import communication
from paper import Paper


def send_communication(subject: str, body: str, communicate: str):
    if communicate == 'gmail':
        communication.send_gmail(subject, body)
    elif communicate == 'mail':
        communication.send_mail(subject, body)
    elif communicate == 'wapp':
        communication.send_whatsapp(body)
    elif communicate == 'sms':
        communication.send_sms(body)


def send_percentage_change(paper, target_percentage: float,
                           communicate='gmail, mail, sms or wapp'):
    paper.update_points_data()
    change = paper.get_daily_precetage_change()

    if target_percentage < 0:
        subject, body = communication.message_percentage(
            paper.name, target_percentage, change, 'decline')

        if change <= target_percentage:
            send_communication(subject, body, communicate)

    elif target_percentage > 0:
        subject, body = communication.message_percentage(
            paper.name, target_percentage, change, 'rise')

        if change >= target_percentage:
            send_communication(subject, body, communicate)

    else:  # Update daily regardless of change
        subject, body = communication.message_percentage(
            paper.name, target_percentage, change, 'change')

        send_communication(subject, body, communicate)


def send_rate_change(paper, target_rate: int, is_above=True,
                     communicate='gmail, mail, sms or wapp'):
    paper.update_points_data()
    daily_rate = paper.get_daily_rate()

    if is_above and daily_rate >= target_rate:
        subject, body = communication.message_rate(
            paper.name, target_rate, daily_rate, 'above')

        send_communication(subject, body, communicate)

    elif not is_above and daily_rate <= target_rate:
        subject, body = communication.message_rate(
            paper.name, target_rate, daily_rate, 'below')

        send_communication(subject, body, communicate)