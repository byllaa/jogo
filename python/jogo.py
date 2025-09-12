import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import matplotlib.pyplot as plt
import math
import sys

# Tentar carregar sons se possível (opcional)
try:
    from playsound import playsound
    SOM_ATIVO = True
except ImportError:
    SOM_ATIVO = False

# Sons personalizados (adicione seus próprios arquivos .mp3 ou .wav se quiser)
SOM_ACERTO = "acerto.mp3"
SOM_ERRO = "erro.mp3"

# ========== Funções utilitárias ==========
def tocar_som(acertou=True):
    if SOM_ATIVO:
        try:
            if acertou:
                playsound(SOM_ACERTO)
            else:
                playsound(SOM_ERRO)
        except:
            pass  # Falha silenciosa se som não estiver presente

def mensagem_resposta(correta, resposta_certa):
    if correta:
        tocar_som(True)
        messagebox.showinfo("Resultado", "✅ Parabéns! Você acertou!")
    else:
        tocar_som(False)
        messagebox.showinfo("Resultado", f"❌ Ops! A resposta correta era {resposta_certa}.")

# ========== Operações ==========
def operacao_adicao():
    a, b = random.randint(1, 50), random.randint(1, 50)
    resposta_correta = a + b
    resposta = simpledialog.askinteger("Adição", f"Quanto é {a} + {b}?")
    if resposta is not None:
        mensagem_resposta(resposta == resposta_correta, resposta_correta)

def operacao_subtracao():
    a, b = random.randint(10, 50), random.randint(1, 10)
    resposta_correta = a - b
    resposta = simpledialog.askinteger("Subtração", f"Quanto é {a} - {b}?")
    if resposta is not None:
        mensagem_resposta(resposta == resposta_correta, resposta_correta)

def operacao_multiplicacao():
    a, b = random.randint(1, 12), random.randint(1, 12)
    resposta_correta = a * b
    resposta = simpledialog.askinteger("Multiplicação", f"Quanto é {a} × {b}?")
    if resposta is not None:
        mensagem_resposta(resposta == resposta_correta, resposta_correta)

def operacao_divisao():
    b = random.randint(1, 10)
    resposta_correta = random.randint(1, 10)
    a = b * resposta_correta
    resposta = simpledialog.askinteger("Divisão", f"Quanto é {a} ÷ {b}?")
    if resposta is not None:
        mensagem_resposta(resposta == resposta_correta, resposta_correta)

# ========== Plano Cartesiano ==========
def plano_cartesiano():
    x, y = random.randint(-10, 10), random.randint(-10, 10)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 11)
    ax.set_xticks(range(-10, 11, 1))
    ax.set_yticks(range(-10, 11, 1))
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.plot(x, y, 'ro', markersize=10)
    ax.set_title("📊 Onde está o ponto vermelho?")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_aspect('equal')

    plt.show(block=False)

    entrada = tk.Toplevel()
    entrada.title("Digite as coordenadas")
    entrada.geometry("300x200")
    entrada.lift()
    entrada.grab_set()

    tk.Label(entrada, text="Qual é o valor de X?").pack(pady=5)
    entrada_x = tk.Entry(entrada)
    entrada_x.pack(pady=5)

    tk.Label(entrada, text="Qual é o valor de Y?").pack(pady=5)
    entrada_y = tk.Entry(entrada)
    entrada_y.pack(pady=5)

    def verificar_resposta():
        try:
            palpite_x = int(entrada_x.get())
            palpite_y = int(entrada_y.get())
            correta = (palpite_x == x and palpite_y == y)
            resposta_certa = f"({x}, {y})"
            mensagem_resposta(correta, resposta_certa)
            entrada.destroy()
            plt.close()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira apenas números inteiros.")

    tk.Button(entrada, text="Verificar", command=verificar_resposta).pack(pady=10)

# ========== Adivinhe o Ângulo ==========
def gerar_figura_angulo(angulo):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot([0, 1], [0, 0], 'b', linewidth=2)
    ax.plot([0, math.cos(math.radians(angulo))], [0, math.sin(math.radians(angulo))], 'r', linewidth=2)
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.2, 1.2)
    ax.axis('off')
    ax.set_aspect('equal')
    plt.title("📐 Adivinhe o Ângulo", fontsize=14)
    plt.tight_layout()
    return fig

def adivinhe_angulo():
    angulo = random.choice([30, 45, 60, 90, 120, 135, 150])
    fig = gerar_figura_angulo(angulo)
    plt.show(block=False)

    resposta = simpledialog.askinteger("Adivinhe o Ângulo", "Qual é o valor do ângulo em graus?")
    if resposta is not None:
        mensagem_resposta(resposta == angulo, f"{angulo}°")
    plt.close(fig)

# ========== Interface ==========
def iniciar_jogo():
    janela = tk.Tk()
    janela.title("🎮 Jogo Matemático Interativo")
    janela.geometry("440x580")
    janela.resizable(False, False)

    tk.Label(janela, text="Jogo Matemático", font=("Arial", 20, "bold")).pack(pady=15)

    # Operações básicas
    tk.Label(janela, text="Operações Básicas:", font=("Arial", 14)).pack(pady=5)

    botoes_operacoes = [
        ("➕ Adição", operacao_adicao),
        ("➖ Subtração", operacao_subtracao),
        ("✖ Multiplicação", operacao_multiplicacao),
        ("➗ Divisão", operacao_divisao),
    ]

    for texto, funcao in botoes_operacoes:
        tk.Button(janela, text=texto, command=funcao, width=30, height=2, bg="#e1f5fe").pack(pady=4)

    # Outros desafios
    tk.Label(janela, text="Outros Desafios:", font=("Arial", 14)).pack(pady=15)

    tk.Button(janela, text="📊 Plano Cartesiano", command=plano_cartesiano, width=30, height=2, bg="#dcedc8").pack(pady=4)
    tk.Button(janela, text="📐 Adivinhe o Ângulo", command=adivinhe_angulo, width=30, height=2, bg="#ffe0b2").pack(pady=4)

    # Sair
    def confirmar_saida():
        if messagebox.askokcancel("Sair", "Tem certeza de que deseja sair do jogo?"):
            janela.destroy()

    tk.Button(janela, text="❌ Sair", command=confirmar_saida, width=30, height=2, bg="#ffcdd2", fg="red").pack(pady=20)

    janela.mainloop()

# ========== Iniciar ==========
if __name__ == "__main__":
    iniciar_jogo()
