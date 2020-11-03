from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta


# Creating the database
engine = create_engine('sqlite:///todo.db? check_same_thread=False')

# Creating the table
Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# Create a session
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
    """ adds the input to the task database """

    new_row = Task(task=input("Enter task\n"),
                   deadline=datetime(*list(map(int, input("Enter deadline\n").split('-')))))

    session.add(new_row)
    session.commit()
    print("The task has been added!\n")


def delete_task():
    """ Prints out all tasks and lets user choose a task to delete """

    rows = session.query(Task).order_by(Task.deadline).all()

    if rows:
        strings = [f"{ind + 1}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}"
                   for ind, row in enumerate(rows)]

        print("Choose the number of the task you want to delete:")
        print('\n'.join(strings))
        del_task = int(input())
        session.delete(rows[del_task - 1])
        session.commit()
        print("The task has been deleted!")
    else:
        print("Nothing to delete!")
    print()


def print_today_tasks():
    """ Prints out today's tasks from the task database """

    today = datetime.today()
    rows = session.query(Task).filter(Task.deadline == today.date()).all()

    print(f"Today {today.day} {today.strftime('%b')}:")
    if rows:
        strings = [f"{ind + 1}. {row.task}" for ind, row in enumerate(rows)]
        print('\n'.join(strings))
    else:
        print("Nothing to do!")
    print()


def print_weeks_tasks():
    """ Prints out weeks's tasks from the task database """

    today = datetime.today()
    this_week = [today + timedelta(days=days) for days in range(7)]
    weeks_tasks = [session.query(Task).filter(Task.deadline == this_day.date()).all()
                   for this_day in this_week]

    for day in range(7):
        rows = weeks_tasks[day]
        today = this_week[day]

        print(f"{today.strftime('%A')} {today.day} {today.strftime('%b')}:")
        if rows:
            strings = [f"{ind + 1}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}"
                       for ind, row in enumerate(rows)]
            print('\n'.join(strings))
        else:
            print("Nothing to do!")
        print()


def print_all_tasks():
    """ Prints out all tasks from the task database """

    rows = session.query(Task).order_by(Task.deadline).all()

    print("All tasks:")
    if rows:
        strings = [f"{ind + 1}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}"
                   for ind, row in enumerate(rows)]
        print('\n'.join(strings))
    else:
        print("Nothing to do!")
    print()


def missed_tasks():
    """ Prints out all missed tasks from the task database """

    today = datetime.today()
    rows = session.query(Task).filter(Task.deadline < today).order_by(Task.deadline).all()

    print("Missed tasks:")
    if rows:
        strings = [f"{ind + 1}. {row.task}. {row.deadline.day} {row.deadline.strftime('%b')}"
                   for ind, row in enumerate(rows)]
        print('\n'.join(strings))
    else:
        print("Nothing is missed!")
    print()


def menu():
    """ Prints a list of possible choices and handles them """

    menu_strings = ["1) Today's tasks",
                    "2) Week's tasks",
                    "3) All tasks",
                    "4) Missed tasks",
                    "5) Add Task",
                    "6) Delete Task",
                    "0) Exit"]
    menu_actions = {'1': print_today_tasks,
                    '2': print_weeks_tasks,
                    '3': print_all_tasks,
                    '4': missed_tasks,
                    '5': add_task,
                    '6': delete_task}

    while True:
        print('\n'.join(menu_strings))
        if choice := input():
            print()
            if choice == '0':
                print("Bye!")
                break
            menu_actions[choice]()


if __name__ == '__main__':
    menu()
