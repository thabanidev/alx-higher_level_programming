## Working with Python Modules and Packages

### What is a Module?
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added.

### What is a Package?
A package is a way of organizing related modules. Packages are a way of structuring Python’s module namespace by using “dotted module names”.

### What is the difference between a module and a package?
A module is a single file (or files) that are imported under one import and used. A package is a collection of modules in directories that give a package hierarchy.

### How to create a module?
To create a module just save the code you want in a file with the file extension .py

### How to create a package?
To create a package, you just need to create a directory with a file named __init__.py inside it.

### How to import a module?
You can import a module using the import statement.

```python
import module_name
```

### How to import a module from a package?
You can import a module from a package using the import statement.

```python
import package_name.module_name
```