# !/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Zeroday_hunter.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()


# import os
# import sys

# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Zeroday_hunter.settings")

#     try:
#         from django.core.management import execute_from_command_line

#     except ImportError:
#         # The above import may fail for some other reason. Ensure that the
#         # issue is really that Django is missing to avoid masking other
#         # exceptions.
#         try:
#             import django  # noqa

#         except ImportError:
#             raise ImportError(
#                 "Couldn't import Django. Are you sure it's installed and "
#                 "available on your PYTHONPATH environment variable? Did you "
#                 "forget to activate a virtual environment?"
#             )

#         raise

#     # This allows easy placement of apps within the inner bootcamp directory.
#     current_path = os.path.dirname(os.path.abspath(__file__))
#     sys.path.append(os.path.join(current_path, "Zer0day-Hunters"))

#     execute_from_command_line(sys.argv)

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','Zeroday_hunter.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
         execute_from_command_line(sys.argv) # just put this in try block
    except:
         pass

if __name__ == '__main__':
     main()