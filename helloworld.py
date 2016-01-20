# Joshua McKnight

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

print('Hello!')
print('Choose one of these languages for a greeting!:')
print(' 1. German.')
print(' 2. French.')
print(' 3. Portuguese')

response = input()

if response == '1':             #if user selects 1, displays German greeting
        print('Hallo!')
if response == '2':             #if user selects 2, displays French greeting   
        print('Salut!')
elif response == '3':           #if user selects 3, displays Portuguese greeting
        print('Olá!')

