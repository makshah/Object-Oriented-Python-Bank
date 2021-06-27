from BankAccountFactory import BankAccountFactory

factory = BankAccountFactory()
saving = factory.makeAccount('SAVING', 'Meet', 5000)

if(saving.setName('James') == True):
    print(f'Successfully changed to {saving.getName()}')
else:
    print(f'Unsuccesful, name still remains {saving.getName()}')


print(f'Welcome to your new account {saving.getName()}')
print(f'Account type is {saving.getAccountType()}')
print(f'Interest generated is {saving.getInterest()}')

checking = factory.makeAccount('CHECKING', 'Meet', 1000)

if(checking.setName('Bruce') == True):
    print(f'Successfully changed to {checking.getName()}')
else:
    print(f'Unsuccesful, name still remains {checking.getName()}')


print(f'Welcome to your new account {checking.getName()}')
print(f'Account type is {checking.getAccountType()}')
print(f'Interest generated is {checking.getInterest()}')
