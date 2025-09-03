import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import matplotlib.pyplot as plt
import math

# ======== Funções das Operações Separadas =========

def operacao_adicao():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    resposta_correta = a + b

    resposta = simpledialog.askinteger("Adição", f"Quanto é {a} + {b}?")
    if resposta is None:
        return
    if resposta == resposta_correta:
        messagebox.showinfo("Resultado", "✅ Correto!")
    else:
        messagebox.showinfo("Resultado", f"❌ Errado! A resposta certa era {resposta_correta}")

def operacao_subtracao():
    a = random.randint(10, 50)
    b = random.randint(1, a)
    resposta_correta = a - b

    resposta = simpledialog.askinteger("Subtração", f"Quanto é {a} - {b}?")
    if resposta is None:
        return
    if resposta == resposta_correta:
        messagebox.showinfo("Resultado", "✅ Correto!")
    else:
        messagebox.showinfo("Resultado", f"❌ Errado! A resposta certa era {resposta_correta}")

def operacao_multiplicacao():
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    resposta_correta = a * b

    resposta = simpledialog.askinteger("Multiplicação", f"Quanto é {a} × {b}?")
    if resposta is None:
        return
    if resposta == resposta_correta:
        messagebox.showinfo("Resultado", "✅ Correto!")
    else:
        messagebox.showinfo("Resultado", f"❌ Errado! A resposta certa era {resposta_correta}")

def operacao_divisao():
    b = random.randint(1, 10)
    resposta_correta = random.randint(1, 10)
    a = b * resposta_correta  # garante divisão exata

    resposta = simpledialog.askinteger("Divisão", f"Quanto é {a} ÷ {b}?")
    if resposta is None:
        return
    if resposta == resposta_correta:
        messagebox.showinfo("Resultado", "✅ Correto!")
    else:
        messagebox.showinfo("Resultado", f"❌ Errado! A resposta certa era {resposta_correta}")

# ======== Plano Cartesiano =========

def plano_cartesiano():
    # Gerar ponto aleatório com coordenadas inteiras
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)

    # Criar gráfico com matplotlib
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 11)
    ax.set_aspect('equal')

    # Ticks inteiros
    ax.set_xticks(range(-10, 11, 1))
    ax.set_yticks(range(-10, 11, 1))
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Ponto vermelho
    ax.plot(x, y, 'ro', markersize=10)

    # Rótulos
    ax.set_title("📊 Onde está o ponto vermelho?")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")

    # Mostrar a figura em segundo plano (sem bloquear o restante do código)
    plt.ion()  # modo interativo
    plt.show()

    # Criar uma nova janela Tkinter para entrada de resposta
    entrada = tk.Toplevel()
    entrada.title("Digite as coordenadas")
    entrada.geometry("300x200")

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

            if palpite_x == x and palpite_y == y:
                messagebox.showinfo("Resultado", "✅ Você acertou as coordenadas!")
            else:
                messagebox.showinfo("Resultado", f"❌ Errado! As coordenadas corretas eram ({x}, {y})")
        except ValueError:
            messagebox.showerror("Erro", "Digite apenas números inteiros.")

        # Fechar a janela de entrada e o gráfico
        entrada.destroy()
        plt.close()

    tk.Button(entrada, text="Verificar", command=verificar_resposta).pack(pady=10)

    # Impede que a janela principal continue até que essa seja fechada
    entrada.grab_set()

# ======== Ângulo =========

def gerar_figura_angulo(angulo):
    fig, ax = plt.subplots(figsize=(4, 4))
    x_base = [0, 1]
    y_base = [0, 0]
    x_angulo = [0, math.cos(math.radians(angulo))]
    y_angulo = [0, math.sin(math.radians(angulo))]
    ax.plot(x_base, y_base, color='blue', linewidth=2)
    ax.plot(x_angulo, y_angulo, color='red', linewidth=2)
    ax.axis('off')
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.2, 1.2)
    ax.set_aspect('equal')
    plt.title("📐 Adivinhe o Ângulo", fontsize=14)
    plt.tight_layout()
    return fig  # retorna o objeto figura, não chama plt.show()

def adivinhe_angulo():
    angulo = random.choice([30, 45, 60, 90, 120, 135, 150])
    fig = gerar_figura_angulo(angulo)
    
    plt.ion()  # modo interativo ligado
    fig.show()
    
    resposta = tk.simpledialog.askinteger("Adivinhe o Ângulo", "Qual é o valor do ângulo em graus?")
    
    if resposta is None:
        plt.close(fig)
        return
    if resposta == angulo:
        messagebox.showinfo("Resultado", "✅ Você acertou!")
    else:
        messagebox.showinfo("Resultado", f"❌ Errado! O ângulo correto era {angulo}°")
    
    plt.close(fig)

# ======== Interface com Tkinter =========

def iniciar_jogo():
    janela = tk.Tk()
    janela.title("🎮 Jogo Matemático com Tkinter")
    janela.geometry("420x500")

    titulo = tk.Label(janela, text="Jogo Matemático", font=("Arial", 18))
    titulo.pack(pady=20)

    # Operações Básicas (separadas)
    tk.Label(janela, text="Operações Básicas:", font=("Arial", 14)).pack(pady=5)

    tk.Button(janela, text="➕ Adição", command=operacao_adicao, width=25, height=2).pack(pady=5)
    tk.Button(janela, text="➖ Subtração", command=operacao_subtracao, width=25, height=2).pack(pady=5)
    tk.Button(janela, text="* Multiplicação", command=operacao_multiplicacao, width=25, height=2).pack(pady=5)
    tk.Button(janela, text="➗ Divisão", command=operacao_divisao, width=25, height=2).pack(pady=5)

    # Outros modos
    tk.Label(janela, text="Outros Desafios:", font=("Arial", 14)).pack(pady=15)

    tk.Button(janela, text="📊 Plano Cartesiano", command=plano_cartesiano, width=25, height=2).pack(pady=5)
    tk.Button(janela, text="📐 Adivinhe o Ângulo", command=adivinhe_angulo, width=25, height=2).pack(pady=5)

    # Sair
    tk.Button(janela, text="❌ Sair", command=janela.destroy, width=25, height=2, fg="red").pack(pady=20)

    janela.mainloop()

# ======== Executar o jogo =========
iniciar_jogo()
