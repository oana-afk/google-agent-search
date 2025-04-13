
# 🤖 Health AI Agent

Este projeto utiliza o **Google AI Developer Kit (ADK)** para criar um sistema inteligente com múltiplos agentes de IA especializados em **treinos personalizados**, **planos alimentares** e **cálculo do Gasto Metabólico Basal (GMB)**.

## 🧠 Sobre o Projeto

O Health AI Coach é composto por:

### 🧭 Agente Principal (Orquestrador)
Responsável por interpretar a solicitação do usuário e encaminhá-la ao agente mais adequado (ex: nutricionista ou treinador). Ele também coordena respostas combinadas caso o usuário deseje, por exemplo, treino + dieta.

### 🏋️ Agente de Treino (Personal Trainer)
Gera treinos de academia personalizados com base em:
- Sexo
- Anos de experiência em treino
- Frequência semanal
- Duração de treino

### 🥗 Agente de Nutrição
Cria dietas de acordo com:
- Foco do usuário (emagrecimento, ganho de massa, manutenção, etc.)
- Sexo, idade, peso, altura, nível de atividade física

### 🔥 Cálculo do GMB
A IA utiliza a seguinte fórmula para calcular o Gasto Metabólico Basal (GMB):

```
Para homens:   88.362 + (13.397 × peso) + (4.799 × altura) – (5.677 × idade)
Para mulheres: 447.593 + (9.247 × peso) + (3.098 × altura) – (4.330 × idade)
```

A TDEE (gasto total diário) é ajustada conforme o nível de atividade informado.

## 🚀 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/scalco7/health-ai-agent.git
   cd health-ai-agent
   ```

2. Crie o ambiente virtual:
   ```bash
   python -m venv .venv
   ```
   
3. Ative o ambiente virtual:
   ```bash
   # Activate (each new terminal)
   # macOS/Linux: source .venv/bin/activate
   # Windows CMD: .venv\Scripts\activate.bat
   # Windows PowerShell: .venv\Scripts\Activate.ps1
   ```

4. Instale o ADK:
   ```bash
   pip install google-adk
   ```

5. Rode o agente principal e interaja com ele:
   ```bash
   adk web
   ```

## 💡 Exemplo de uso

```
Usuário: Quero um plano de treino.
Agente Principal: Você pode me dizer seu sexo, quantos anos treina, quantas vezes por semana você vai treinar, e quanto tempo tem disponível por sessão?

Usuário: Tenho 2 anos de treino, quero treinar 4 vezes por semana, 1 hora por dia, e sou homem.

Agente de Treino: Aqui está seu plano...
```

## 📦 Tecnologias

- Python
- Google AI Developer Kit (ADK)
