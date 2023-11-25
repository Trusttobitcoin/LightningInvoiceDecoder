import subprocess
import json
from prettytable import PrettyTable
from termcolor import colored

def decode_invoice(invoice):
    try:
        result = subprocess.run(['lncli', 'decodepayreq', invoice], check=True, stdout=subprocess.PIPE)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError:
        return None

def display_info(decoded_invoice):
    table = PrettyTable()
    table.field_names = [colored("Field", 'blue', attrs=['bold']), colored("Value", 'green', attrs=['bold'])]
    table.align = "l"
    table.horizontal_char = '-'
    table.vertical_char = '|'
    table.junction_char = '+'

    table.add_row(["Destination", decoded_invoice['destination']])
    table.add_row(["Amount", f"{decoded_invoice['num_satoshis']} satoshis"])
    table.add_row(["Payment Hash", decoded_invoice['payment_hash']])
    table.add_row(["Expiry", f"{int(decoded_invoice['expiry']) // 3600} hours"])
    table.add_row(["Memo", decoded_invoice.get('description', 'N/A')])
    table.add_row(["Payment Address", decoded_invoice.get('payment_addr', 'N/A')])
    table.add_row(["CLTV Expiry", f"{decoded_invoice['cltv_expiry']} blocks"])

    print(table)

def main():
    invoice = input(colored("Please enter a Lightning Network invoice: ", 'cyan', attrs=['bold'])).strip()
    
    print(colored("\nDecoding the invoice...", 'magenta'))
    decoded_invoice = decode_invoice(invoice)
    
    if decoded_invoice:
        display_info(decoded_invoice)
    else:
        print(colored("Invalid invoice or error in decoding.", 'red'))

if __name__ == "__main__":
    main()
