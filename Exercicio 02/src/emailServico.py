# src/email/email_servico.py

class EmailSMTP:
    def send_email(self, to, subject, body):
        """
        Simula o envio de um e-mail.
        Para fins de teste, retorna True como se o e-mail tivesse sido enviado com sucesso.
        """
        print(f"Enviando e-mail para {to} com o assunto '{subject}'")
        return True
