import csv

def check_valid_invoice_id(list_invoice, invoice_id):
    for invoice in list_invoice:
        if invoice['ID'] == invoice_id:
            return False
    return True

def add_invoice(invoice_id):
    date = input("Input date of invoice: ")
    customer_name = input("Input customer name: ")
    address = input("Input address: ")
    district = input("Input district: ")
    phone = input("Input phone number: ") 
    while True:
        total_billing = input("Input total billable: ")
        try:
            total_billing = float(total_billing)
            if total_billing < 0:
                print('Please enter a positive number!\n')
                continue
            break
        except:
            print('Please enter a numeric value.\n')
            continue
    
    while True:
        paid_billing = input("Input paid billing: ")
        try:
            paid_billing = float(paid_billing)
            if paid_billing < 0:
                print('Please enter a positive number!\n')
                continue
            break
        except:
            print('Please enter a numeric value.\n')
            continue
        
    while True:
        available_billing = input("Input available billing: ")
        try:
            available_billing = float(available_billing)
            if available_billing < 0:
                print('Please enter a positive number!\n')
                continue
            break
        except:
            print('Please enter a numeric value.\n')
            continue
        
    invoice_dict = {
        "ID": invoice_id,
        "Date": date,
        "Customer Name": customer_name,
        "Address": address,
        "District": district,
        "Phone": phone,
        "Total billable": total_billing,
        "Paid billing": paid_billing,
        "Available billing": available_billing,
    }
    return invoice_dict


def print_invoice(list_invoice):
    key_list = list(list_invoice[0].keys())
    print(
        f"{key_list[0]: <17}{key_list[1]: <17}{key_list[2]: <17}{key_list[3]: <17}{key_list[4]: <17}{key_list[5]: <17}{key_list[6]: <17}{key_list[7]: <17}{key_list[8]: <17}"
    )
    for invoice in list_invoice:
        value_list = list(invoice.values())
        print(
            f"{value_list[0]: <17}{value_list[1]: <17}{value_list[2]: <17}{value_list[3]: <17}{value_list[4]: <17}{value_list[5]: <17}{value_list[6]: <17}{value_list[7]: <17}{value_list[8]: <17}"
        )

def find_invoice(list_invoice, invoice_id):
    found_invoice = list(filter(lambda invoice: invoice["ID"] == invoice_id, list_invoice))
    return found_invoice

def delete_invoice(list_invoice, invoice_id):
    for i in range(len(list_invoice)):
        if list_invoice[i]['ID'] == invoice_id:
            del(list_invoice[i])
            return True
    return False

def summarize_invoice(list_invoice):
    sum_total = sum_paid = sum_available = 0
    for i in range(len(list_invoice)):
        sum_total += list_invoice[i]['Total billable']
        sum_paid += list_invoice[i]['Paid billing']
        sum_available += list_invoice[i]['Available billing']
    return sum_total, sum_paid, sum_available

def write_invoice_to_csv(path, list_invoice):
    try:
        header = list(list_invoice[0].keys())
    except:
        header = ["ID", "Date", "Customer Name", "Address", "District", "Phone", "Total billable", "Paid billing", "Available billing"]
    
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for invoice in list_invoice:
            writer.writerow(invoice)
            
def read_csv_file(path):
    list_invoice = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for invoice in reader:
            list_invoice.append(invoice)
    return list_invoice

