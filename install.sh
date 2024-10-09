#!/bin/bash

# Color Codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Emojis
INSTALLING="🔧"
SUCCESS="✅"
MOVING="📦"
MAKING="⚙️"
LINKING="🔗"

show_progress() {
    local duration=$1
    local interval=1  # Use integer for interval (in seconds)
    local total_steps=$((duration / interval))
    
    echo -n "${INSTALLING} Installing"
    for ((i=1; i<=total_steps; i++)); do
        sleep $interval
        echo -n "."
    done
    echo ""  # New line after progress bar
}

echo -e "${MOVING} ${YELLOW}Moving the source code to /usr/local/bin...${NC}"
cp -r ./src/* /usr/local/bin/
show_progress 5

echo -e "${MAKING} ${YELLOW}Making main.py executable...${NC}"
chmod +x /usr/local/bin/main.py
show_progress 5

echo -e "${LINKING} ${YELLOW}Creating a wrapper script for easy access...${NC}"
cat << 'EOF' > /usr/local/bin/ddojo
#!/usr/bin/env bash
exec python3 /usr/local/bin/main.py "$@"
EOF

chmod +x /usr/local/bin/ddojo
show_progress 5

echo -e "${SUCCESS} ${GREEN}dDojo installed successfully! You can now start withthe command 'ddojo --help'.${NC}"

