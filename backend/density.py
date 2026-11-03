def calculate_density(people):

    if people < 20:
        return "LOW"

    elif people < 50:
        return "MEDIUM"

    elif people < 100:
        return "HIGH"

    else:
        return "CRITICAL"