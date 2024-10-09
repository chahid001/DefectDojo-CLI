import argparse
import pyfiglet
import loading.load as loading


import tools.tools as tool

import operations.product as product
import operations.engagement as eng
import operations.finding as finding

import checker.token as check
import checker.scan as check_scan

import parser.tags as tags


class Scan:
    def __init__(self):
        self.scan_ = []
        self.file_ = []
    def add_options(self, scan, file):
        self.scan_.append(scan)
        self.file_.append(file)
    def get_scan(self, index):
        if 0 <= index < len(self.scan_):
            return self.scan_[index]
        else:
            raise IndexError("Index out of range")

    def get_file(self, index):
        if 0 <= index < len(self.file_):
            return self.file_[index]
        else:
            raise IndexError("Index out of range")


def main():
    ASCII_art_1 = pyfiglet.figlet_format("DDOJO-CLI", font="big")
    print(ASCII_art_1)
    

    parser = argparse.ArgumentParser(
                        prog='ddojo',
                        description='The program is a CLI for Defect-Dojo tool for creating & uploading product, engagement & findings',
                        epilog='🤝 We welcome contributions! Please follow the steps at https://github.com/chahid001/')
    
    group_product = parser.add_argument_group('Command line for product options')
    group_product.add_argument('-p', '--project', metavar="name", type=str, help='Add the project name (Product)')
    group_product.add_argument('-type', metavar="index", type=int, help='Index for the product type')
    group_product.add_argument('-tags', metavar="name", type=str, help='Add tags for project "tag1, tag2, ..."' )

    group_eng = parser.add_argument_group('Command line for engagement options')
    group_eng.add_argument('-eng', metavar="name", type=str, help="Add name for the engagement" )
 
    group_fin = parser.add_argument_group('Command line for adding scan reports')
    group_fin.add_argument('--scan', action="append", choices=['gitleaks', 'owasp-dep', 'owasp-zap', 'osv-scan', 'sonar'], type=str )
    group_fin.add_argument('-f', '--file', metavar="filename", action="append", type=str, help='The path of the report filename')
    
    parser.add_argument('--token', type=str, help="Add Defect-Dojo secret API token" )
    parser.add_argument('--url', type=str, help="Add Defect-Dojo url http://<IP_ADDRESS>:<PORT>/" )
    args = parser.parse_args()

    token = {
        "Authorization": f"Token {args.token}",
    }

    loading.display("[🔍] Checking Token ......", "GREEN", 2)
    if check.check_token(args.url, token):
        loading.print_c("The token is valid ✅", "GREEN")
    else:
        loading.print_c("The token is invalid ❌", "RED")
        exit(1)

    scan_op = Scan()

    i = 0
    while i < len(args.scan) and i < len(args.file):
        loading.display(f"[🔍] Checking files {i+1}/{len(args.file)}", "GREEN", 2)
        scan_op.add_options(args.scan[i], args.file[i])
        i += 1
    scan = check_scan.check_scan(scan_op)
    loading.print_c("The files are valid ✅", "GREEN")

    loading.display("[🛠️] Creating product ......", "GREEN", 2)
    project_id = product.create_product(args.url, args.project, args.type, tags.parse_tags(args.tags), token)
    loading.display("[🛠️] Creating engagement ......", "GREEN", 2)
    eng_id = eng.create_engagement(args.url, args.eng, project_id, token, tool.get_date())

    j = 0
    while j < len(scan.scan_):
        loading.display(f"[⌛] Uploading report {j+1}/{len(scan.file_)}......", "GREEN", 1)
        finding.uploadToDefectDojo(args.url, project_id, args.type, eng_id, scan.scan_[j], scan.file_[j], token) 
        j += 1
    loading.print_c("You are good to go", "BOLD")

if __name__ == "__main__":
    main()