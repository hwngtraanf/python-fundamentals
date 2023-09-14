from libs.common import *

list_invoice = []
path = './files/invoice.csv'

if __name__ == "__main__":
    while True:
        print('-'*25)
        print('WELCOME TO INVOICE MANAGEMENT PROGRAM!')
        print('-'*25)
        print('Type 1: Add new invoice')
        print('Type 2: List all invoices')
        print('Type 3: Find invoice')
        print('Type 4: Delete invoice')
        print('Type 5: Summary invoice')
        print('Type 6: Export invoices to csv file')
        print('Type 7: Read file csv')
        print('Type -1 to exit!')
        choice = input('Your option: ')
        
        if choice == '1':
            while True:
                invoice_id = input('Input invoice id: ')
                if check_valid_invoice_id(list_invoice=list_invoice, invoice_id=invoice_id):
                    invoice = add_invoice(invoice_id=invoice_id)
                    list_invoice.append(invoice)
                    cont = input('Do you want to add more invoice? Type 1 to continue, type any key to exit: ')
                    if cont != '1':
                        break
                else:
                    print('You have entered an already existed invoice id. Please enter another invoice.\n')
        
        elif choice == '2':
            print_invoice(list_invoice=list_invoice)
        
        elif choice == '3':
            invoice_id_to_find = input('Please input invoice id to find: ')
            found_invoice = find_invoice(list_invoice=list_invoice, invoice_id=invoice_id_to_find)
            if len(found_invoice) == 0:
                print('No invoice found with that id\n')
            else:
                print_invoice(list_invoice=found_invoice)
                
        elif choice == '4':
            invoice_id_to_delete = input('Please input invoice id to delete: ')
            delete_status = delete_invoice(list_invoice=list_invoice, invoice_id=invoice_id_to_delete)
            if delete_status:
                print(f'Deleted invoice with id: {invoice_id_to_delete}')
            else:
                print(f'Do not found invoice with id: {invoice_id_to_delete} to delete.')
                
        elif choice == '5':
            sum_total, sum_paid, sum_available = summarize_invoice(list_invoice=list_invoice)
            print(f'The total amount of billing is: {sum_total}')
            print(f'The total amount of paid is: {sum_paid}')
            print(f'The total amount of available is: {sum_available}')
        
        elif choice == '6':
            write_invoice_to_csv(path, list_invoice=list_invoice)
        
        elif choice == '7':
            list_invoice = read_csv_file(path)
        
        elif choice == '-1':
            break
        
        else:
            print('Invalid option. Please choose again!\n')