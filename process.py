import sqlite3

conn = sqlite3.connect('tasks_database.sqlite3')
cur = conn.cursor()


def generate_variant(variants, counts):
    format_vars = []
    check = sorted([int(i) for i in variants.split(';')])
    for i in check:
        format_vars.append(cur.execute(f'SELECT Task, Text, Answer_options, Right_answer, Solution FROM Tasks WHERE Theme="{i}"').fetchmany(counts))
    return format_vars[0]


# print(generate_variant('1', 1))
