def new_line():
  print()

def print_update(transaction, old_value, log_values):
  row = log_values[0]
  column = log_values[1]
  new_value = log_values[2]

  print('TRANSAÇÃO '+ transaction +': No registro '+ row +', a coluna ' + column +' estava ' + str(old_value) + ' e no log atualizou para ' + new_value)

    
def print_undo_transactions(started_transactions, committed_transactions, checkpoint_transactions):
  # Imprime transações do checkpoint que realizaram ou não o Undo
  # print(started_transactions)
  # print(committed_transactions)
  # print(checkpoint_transactions)
  new_line()
  for transaction in started_transactions:
      if transaction not in committed_transactions:
          if transaction in checkpoint_transactions:
              print('TRANSAÇÃO ' + transaction + ': realizou Undo com checkpoint')
          else:
              print('TRANSAÇÃO ' + transaction + ': realizou Undo')



def print_json(cursor):
  id = []
  a = []
  b = []

  # Retorna todas as tuplas da tabela
  cursor.execute('SELECT * FROM data ORDER BY id')
  tuples = cursor.fetchall()

  for tuple in tuples:
    id.append(tuple[0])
    a.append(tuple[1])
    b.append(tuple[2])

  print('''
    {
      "TABLE": {
        "id": '''+ str(id)[1:-1] +''',
        "A: '''+ str(a)[1:-1] +''',
        "B": '''+ str(b)[1:-1] +'''
      }
    }
  ''')