# 🌦️ python-observer

## 📝 Descrição

Este projeto demonstra o uso do padrão de projeto **Observer** em Python, aplicado ao monitoramento de condições climáticas.  
A aplicação utiliza **Streamlit** para criar uma interface gráfica interativa, onde diferentes displays (observadores) apresentam dados coletados de um equipamento de monitoramento simulado.

- **Display de Condições Atuais:** mostra as últimas 10 leituras de temperatura, umidade e pressão.
- **Display Estatístico:** apresenta médias, máximas e mínimas das últimas 10 leituras.

O sistema é modular, permitindo fácil adição ou remoção de observadores.

---

## 🚀 Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/python-observer.git
   cd python-observer
   ```

2. **(Opcional) Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação Streamlit:**
   ```bash
   streamlit run src/app.py
   ```

5. **Acesse a interface:**
   - Abra o navegador e acesse o endereço exibido no terminal (geralmente http://localhost:8501).

---

## 📁 Estrutura do projeto

- `src/` — Código-fonte principal
  - `devices/` — Equipamento de monitoramento (simulador de dados)
  - `observers/` — Observadores (displays)
  - `subjects/` — Sujeito observável e monitor de dados do clima
  - `app.py` — Interface Streamlit

---

## 📄 Licença

Este projeto é apenas para fins educacionais.

