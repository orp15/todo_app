# -*- coding:utf-8 -*-
from odoo.tests.common import TransactionCase

class TestTodo(TransactionCase):
    def test_create(self):
        "Crea una tarea simple"

        Todo = self.env['todo.task']
        task = Todo.create({'name':'Test Task'})
        self.assertEqual(task.is_done, False)
        