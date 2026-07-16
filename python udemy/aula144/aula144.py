from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando email com a mensagem: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando SMS com a mensagem: {self.mensagem}')
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada com sucesso!')
    else:
        print('Falha ao enviar a notificação!')

notificar(NotificacaoEmail('Olá, mundo!'))


