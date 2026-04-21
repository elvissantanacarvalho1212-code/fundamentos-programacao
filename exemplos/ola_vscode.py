"""Exemplo simples para rodar no VS Code.

Este arquivo mostra entrada de dados, função e saída formatada.
"""


def saudacao(nome: str) -> str:
    """Monta uma mensagem de boas-vindas."""
    return f"Olá, {nome}! Bem-vindo ao VS Code 🚀"


if __name__ == "__main__":
    nome_usuario = input("Digite seu nome: ").strip() or "estudante"
    print(saudacao(nome_usuario))
