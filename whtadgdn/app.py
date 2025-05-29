from django.core.management import execute_from_command_line
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    execute_from_command_line(sys.argv)

#Final

if __name__ == "__main__":
    main()

