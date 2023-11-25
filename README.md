
# LightningInvoiceDecoder

## Overview
`LightingInvoiceDecoder` is a Python tool designed to decode and display Lightning Network invoices in a user-friendly format. Leveraging `lncli` from the Lightning Network Daemon (LND), this tool makes it easy to understand and interact with invoice data, enhancing usability for both developers and end-users on the Lightning Network.

## Features
- Decode Lightning Network invoices using `lncli`.
- Display invoice details in an easy-to-read table format.
- User-friendly command-line interface.
- Enhanced readability with colorful output.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed.
- Access to a Lightning Network Daemon (LND) with `lncli` configured.
- `prettytable` and `termcolor` Python packages installed.

## Installation
To install `LightningInvoiceDecoder`, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Trusttobitcoin/LightningInvoiceDecoder.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd LightningInvoiceDecoder
   ```
3. Install the required Python packages:
   ```bash
   pip install prettytable termcolor
   ```

## Usage
To use `LightningInvoiceDecoder`, follow these steps:

1. Run the script from the command line:
   ```bash
   python decode_invoice.py
   ```
2. Enter a Lightning Network invoice when prompted.


## License
`LightningInvoiceDecoder` is available under the MIT License. See the LICENSE file in the repository for more details.

