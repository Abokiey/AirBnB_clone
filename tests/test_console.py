#!/usr/bin/python3
"""Console Tests"""
import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO

class TestConsole(unittest.TestCase):
    """Test Calls"""
    def test_help(self):
        """Test the help instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual('Prints the string representation of an \
instance based on the class name and id.\n', f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        self.assertEqual('Creates a new instance of a given \
class, save it (to the JSON file) and prints the id.\n', f.getvalue())
        
    def test_create(self):
        """Test Create instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertIsInstance(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

    def test_show(self):
        """Test show instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1111")
        self.assertEqual(f.getvalue(), '** no instance found ** \n')

    def test_destroy(self):
        """Help destroy instances"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("detroy MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand.onecmd("destroy BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1111")
        self.assertEqual(f.getvalue(), '** no instance found ** \n')

    def test_all(self):
        """Test all functions"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertEqual(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertEqual(f.getvalue(), str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')

    def test_update(self):
        """Test Updates Methods"""
        with patch('sys.stdout', new=StringIO()) as f:
             HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(f.getvalue(), '** instance id missing ** \n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1111")
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        model_id = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {model_id}")
        self.assertEqual(f.getvalue(), '** attribute name missing ** \n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {model_id} first")
        self.assertEqual(f.getvalue(), '** value missing **\n')

    def test_quit(self):
        """Test Quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        """Test End of the file"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), '')