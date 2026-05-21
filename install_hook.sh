#!/bin/bash
# Copy hook script and grant executable permissions
cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

echo "Hook setup completed: .git/hooks/pre-commit"
