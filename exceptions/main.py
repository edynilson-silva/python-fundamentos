# try/except: ao executar determinado bloco de código definido no try e, caso gere um erro, executa o bloco de código definido no except;
# try/finally: após try ser executado, com sucesso ou não, o código definido dentro do finally é executado;
# Raise: por algum motivo, precisarmos gerar uma exceção em nosso script, utilizamos o comando raise;
# Assert: assim como o comando raise, o assert serve para gerar exceções, porém é necessário definir uma condição para isso.

# try/except
try:
    numero = 15/0
except: # ou utilizar exceções pré-definidas no Python (except ZeroDivisionError:)
    print("Divisão por zero não existe")


# try/finally
try:
    numero = 15/0
except ZeroDivisionError:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")

# Raise
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")

# Assert
try:
    numero = 15
    divisor = 0
    assert divisor != 0
except:
    print("Divisão por zero não existe")
finally:
    print("Execução finalizada")  