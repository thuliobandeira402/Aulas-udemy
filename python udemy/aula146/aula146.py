class MeuError(Exception):
    pass

class OutroError(Exception):
    pass

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('uma nota')
    raise exception_

try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.add_note('Mais uma nota')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error