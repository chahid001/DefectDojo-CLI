# dDojo 🛠️

**dDojo** is a Command-Line Interface (CLI) tool designed to simplify interactions with Defect Dojo. With this tool, you can easily create products, engagements, and upload scan results for various tools such as OWASP Dep Check, OWASP ZAP Scan, SonarQube, OSV-Scanner, and Gitleaks.

## Demo 💻
![ddojo-cli](https://github.com/chahid001/DefectDojo-CLI/blob/main/assets/ddojo-cli.png)

## Features ✨

- **Create Product**: Create new products in Defect Dojo. 🆕
- **Create Engagement**: Add engagements to existing products. 🔗
- **Upload Scan Results**: Upload scan results for: 📊
  - OWASP Dep Check 🛡️
  - OWASP ZAP Scan 🔍
  - SonarQube 📈
  - OSV-Scanner 🔎
  - Gitleaks 💧

## Installation 🚀
To install `dDojo`, clone the repository and run the installation script:

```bash
git clone https://github.com/chahid001/DefectDojo-CLI
cd DefectDojo-CLI
bash install.sh
```
## Usage ⚙️

```bash
# Basic usage
ddojo --help

# Creating a new product, engagement & uploading Gitleak scan report

ddojo --project <Project name> -type <index> \
        -tags "tag1, tag2" -eng <name> \
        --scan gitleaks -f gitleaks-report.json \
        --token <your token>
```


