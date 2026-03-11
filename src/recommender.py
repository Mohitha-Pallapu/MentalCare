def get_recommendations(stress, sleep, exercise):

    recommendations = []

    if stress == "High":
        recommendations.append("Practice stress management techniques like meditation.")

    if sleep < 6:
        recommendations.append("Improve sleep schedule to at least 7 hours.")

    if exercise == "Low":
        recommendations.append("Try regular physical activity like walking or yoga.")

    if not recommendations:
        recommendations.append("Your lifestyle looks balanced. Keep maintaining healthy habits!")

    return recommendations