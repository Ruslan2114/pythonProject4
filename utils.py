
import json

def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        file = json.load(file)
        return file


def get_all():
    result = []
    text = load_candidates()
    for i in text:
        result.append(i["name"])
    return result

def get_by_pk(pk):
    text = load_candidates()
    for i in text:
        if i["pk"] == pk:
            return i

def get_by_skill(skill_name):
    result = []
    text = load_candidates()
    for i in text:
        if skill_name.lower() in i['skills'].lower():
            result.append(i)
    return result


def all_cand(text):
    result = "<pre>"
    for i in text:
        result += f"Имя кандидата - {i['name']}\n" \
                  f"Позиция кандидата - {i['position']}\n" \
                  f"Навыки через запятую - {i['skills']}\n"

    return result + '</pre>'





