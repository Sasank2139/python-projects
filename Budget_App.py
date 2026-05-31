class Category:
    def __init__(self,namex):
        self.name = name
        self.ledger = []
    def check_funds(self,amount):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        if balance >= amount:
            return True
        else:
            return False
    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount,'description': description})
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount,'description': description})
            return True
        else:
            return False
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to: {category.name}')
            category.deposit(amount,f'Transfer from: {self.name}')
            return True
        else:
            return False
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            description = item['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f'Total: {self.get_balance():.2f}'
        return title + items + total
def create_spend_chart(categories):
    for category in categories:
        total_spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent += -item['amount']
        category.spent = total_spent
    total_spent_all = sum(category.spent for category in categories)
    for category in categories:
        category.percentage = (int((category.spent / total_spent_all) * 100) // 10) * 10
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for category in categories:
            if category.percentage >= i:
                chart += "o  "
            else:
                chart += "  "
                line += "\n"
        chart += line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += f"{category.name[i]}  "
            else:
                line += "   "
        chart += "\n"
    return chart
        