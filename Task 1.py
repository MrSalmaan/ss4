# Set the PySimpleGUI theme to GreenMono
import PySimpleGUI as sg
sg.theme('GreenMono')

# Define the layout of the GUI
layout = [
    [sg.Text('City Gym Member Registration Form', font=('Arial', 20))],
    [sg.Text('Customer Details', font=('Arial', 16), justification='center')],
    [sg.Text('First Name:', size=(15,1)), sg.InputText(key='first_name')],
    [sg.Text('Last Name:', size=(15,1)), sg.InputText(key='last_name')],
    [sg.Text('Postal Address:', size=(15,1)), sg.InputText(key='postal_address')],
    [sg.Text('Mobile Number:', size=(15,1)), sg.InputText(key='mobile_number')],
    [sg.Text('Membership Details', font=('Arial', 16))],
    [sg.Text('Type of Membership:')],
    [sg.Radio('Basic ($10.00 per week)', 'membership_type', key='basic_membership')],
    [sg.Radio('Regular ($15.00 per week)', 'membership_type', key='regular_membership')],
    [sg.Radio('Premium ($20.00 per week)', 'membership_type', key='premium_membership')],
    [sg.Text('Membership Duration:')],
    [sg.Radio('3 Months', 'membership_duration', key='3_months')],
    [sg.Radio('12 Months', 'membership_duration', key='12_months')],
    [sg.Radio('24 Months', 'membership_duration', key='24_months')],
    [sg.Text('Payment Options', font=('Arial', 16))],
    [sg.Text('Direct Debit:')],
    [sg.Radio('Yes', 'direct_debit', key='yes_direct_debit')],
    [sg.Radio('No', 'direct_debit', key='no_direct_debit')],
    [sg.Text('Frequency of Payment:')],
    [sg.Radio('Weekly', 'payment_frequency', key='weekly')],
    [sg.Radio('Monthly', 'payment_frequency', key='monthly')],
    [sg.Text('Extras', font=('Arial', 16))],
    [sg.Checkbox('24/7 Access ($1 per week)', key='24_7_access')],
    [sg.Checkbox('Personal Trainer ($20 per week)', key='personal_trainer')],
    [sg.Checkbox('Diet Consultation ($20 per week)', key='diet_consultation')],
    [sg.Checkbox('Access Online Fitness Videos ($2 per week)', key='online_fitness_videos')],
    [sg.Button('Calculate', button_color=('white', 'green')), sg.Button('Submit', button_color=('white', 'blue'))]
]

# Create the GUI window
window = sg.Window('City Gym', layout)

# Run the event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Calculate':
        # Calculate the membership fee
        fee = 0
        if values['basic_membership']:
            fee += 10
        if values['regular_membership']:
            fee += 15
        if values['premium_membership']:
            fee += 20
        fee += 1 if values['24_7_access'] else 0
        fee += 20 if values['personal_trainer'] else 0
        fee += 20 if values['diet_consultation'] else 0
        fee += 2 if values['online_fitness_videos'] else 0
        if values['3_months']:
            fee *= 13
        elif values['12_months']:
            fee *= 52
        elif values['24_months']:
            fee *= 96
        window['membership_fee'].update('${:,.2f}'.format(fee))
    if event == 'Submit':
        # Data validation checks
        if not all([values['first_name'], values['last_name'], values['basic_membership'] or values['regular_membership'] or values['premium_membership'], 
                   values['3_months'] or values['12_months'] or values['24_months'], values['yes_direct_debit'] or values['no_direct_debit'], 
                   values['weekly'] or values['monthly']]):
            sg.popup_error("Please fill in all required fields.")
        elif not values['first_name'].isalpha() or not values['last_name'].isalpha():
            sg.popup_error("Please enter a valid name.")
        else:
            # Save data to a file
            with open('gym_members.txt', 'a') as file:
                file.write(f"{values['first_name']} {values['last_name']} - ${fee:,.2f} per {values['frequency']} via {values['direct_debit']}\n")
                sg.popup("Data saved successfully!")
