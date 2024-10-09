import os
import loading.load as loading

def check_file(scan, file):
    root, ext = os.path.splitext(file)

    if scan == "gitleaks":
        if ext != ".json":
            loading.print_c("Wrong filename, GitLeaks needs a JSON report. 📬 ❌", "RED")
            exit(1)
    if scan == "owasp-dep":
        if ext != ".xml":
            loading.print_c("Wrong filename, OWASP Dependency Check needs a XML report. 📬 ❌", "RED")
            exit(1)
    if scan == "owasp-zap":
        if ext != ".xml":
            loading.print_c("Wrong filename, OWASP Zap Scan needs a XML report. 📬 ❌", "RED")
            exit(1)
    if scan == "osv-scan":
        if ext != ".json":
            loading.print_c("Wrong filename, OSV-SCAN needs a JSON report. 📬 ❌", "RED")
            exit(1)
    if scan == "sonar":
        if ext != ".html":
            loading.print_c("Wrong filename, OSV-SCAN needs a HTML report. 📬 ❌", "RED")
            exit(1)

    try:
        if not os.path.exists(file):
            loading.print_c(f"The file '{file}' does not exist. 📭", "RED")
            return False
        if not os.path.isfile(file):
            loading.print_c(f"'{file}' is not a valid file. 📭", "RED")
            return False
        return True

    except Exception as e:
        loading.print_c(f"An error occurred while checking the file '{file}' 📪: {e}", "RED")
        return False

def check_scan(scan):
    
    i = 0
    while i < len(scan.scan_):
        if not check_file(scan.scan_[i], scan.file_[i]):
            exit(1)

        match scan.scan_[i]:
            case "gitleaks":
                scan.scan_[i] = "Gitleaks Scan"
            case "owasp-dep":
                scan.scan_[i] = "Dependency Check Scan"
            case "owasp-zap":
                scan.scan_[i] = "ZAP Scan"
            case "osv-scan":
                scan.scan_[i] = "OSV Scan"
            case "sonar":
                scan.scan_[i] = "SonarQube Scan"
        i += 1
    return scan