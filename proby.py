
from typing import List
# from M07projekt import Expense
import click
from dataclasses import dataclass


# class Expense:
#     def __init__(self, id:int, amount:float, desc:str) -> None:
#         self.id = id
#         self.amount = amount
#         self.desc = desc
@dataclass 
class Expense:
    id:int
    amount:float
    desc: str


# def generate_id(expenses: List[Expense]) -> int:
#     ids = [exp.id for exp in expenses]
#     counter = 1
#     while counter in ids:
#         counter += 1
    
#     id = counter

#     return id


@click.group()
def cli():
    pass

@cli.command()
@click.argument("desc", required=1)
def remove(desc:str) -> None:
    expenses = [
    Expense(2, 3.60, 'mleko'),
    Expense(1, 4.50, "chleb")
    ]
    for exp in expenses:
        if exp.desc == desc:
            expenses.remove(exp)
    # return expenses

    print(expenses)

cli()

#     expenses = load_expenses()
#     for e in expenses:
#         if e.desc in e:
#             expenses.remove(e)
#     dump_exp(expenses)
#     print('expense removed')