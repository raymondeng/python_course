#!/bin/bash

# Check if port 1883 is open and listening
if netstat -tuln | grep -q ':1883\b'; then
  echo "Port 1883 is open and listening"
else
  echo "Port 1883 is not open or not listening"
fi
