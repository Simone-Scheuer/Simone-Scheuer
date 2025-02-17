#!/usr/bin/env python3
import os
import re
import sys
from datetime import datetime

def get_current_streak():
    """Get the current streak from README, or start at 0."""
    try:
        if not os.path.exists('README.md'):
            print("No README.md found, starting fresh!")
            return 0
        
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to find current streak number
        streak_pattern = r"🔥 I've been coding for (\d+) consecutive days!"
        match = re.search(streak_pattern, content)
        if match:
            current_streak = int(match.group(1))
            print(f"Found current streak: {current_streak} days")
            return current_streak
        else:
            print("No streak found in README, starting fresh!")
            return 0
            
    except Exception as e:
        print(f"Error reading streak: {e}")
        return 0

def update_readme():
    """Update the README.md with an incremented streak count."""
    try:
        current_streak = get_current_streak()
        new_streak = current_streak + 1
        
        # Create or read README
        if os.path.exists('README.md'):
            with open('README.md', 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# Hi there! 👋\n\n"
            print("Created new README.md")
        
        # Update or add the streak count
        streak_pattern = r"🔥 I've been coding for \d+ consecutive days!"
        streak_text = f"🔥 I've been coding for {new_streak} consecutive days!"
        
        if re.search(streak_pattern, content):
            new_content = re.sub(streak_pattern, streak_text, content)
            print("Updated existing streak count")
        else:
            if content.strip():
                new_content = content.rstrip() + "\n\n" + streak_text + "\n"
            else:
                new_content = "# Hi there! 👋\n\n" + streak_text + "\n"
            print("Added new streak count")
        
        # Write updated content
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Successfully updated streak to {new_streak} days! 🎉")
        return True
        
    except Exception as e:
        print(f"Error updating README: {e}")
        return False

def main():
    try:
        print(f"Starting streak update at {datetime.now().isoformat()}")
        print(f"Working directory: {os.getcwd()}")
        
        if update_readme():
            print("Streak update completed successfully!")
            sys.exit(0)
        else:
            print("Failed to update streak!")
            sys.exit(1)
            
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 