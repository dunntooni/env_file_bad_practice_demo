# INSTRUCTIONS:
#
# I have created a package with malware at the root directory. It shares a name with a function (which the user will actually be trying to access) which is one folder down.
# If the user is not specific, they will get the "malware" function and run it.
#
# Run the following in this directory to install the necessary library:
# py -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-dunntooni-package-malware-demo
#
# (It's not actual malware, don't worry)

# This code will get the added malware function
# from example_package_dunntooni_package_malware_demo import example

# print(example.print_text())


# This code leads to the actual function we're trying to access

# Notice here we're more specific.
from example_package_dunntooni_package_malware_demo.example_folder import example

print(example.print_text())

# Always review the code you import!
