def risk_score(people):

    score = min(int((people / 100) * 100),100)

    if score <30:
        alert="GREEN"

    elif score<60:
        alert="YELLOW"

    elif score<80:
        alert="ORANGE"

    else:
        alert="RED"

    return score,alert