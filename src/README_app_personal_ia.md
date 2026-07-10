# Código da Aplicação — Personal IA

Esta pasta contém o código da aplicação do **Personal IA**, um assistente inteligente de apoio à montagem, adaptação e acompanhamento de treinos físicos.

O agente utiliza dados mockados da pasta `data/`, como perfil do usuário, histórico de treinos, feedbacks, base de exercícios, base de conhecimento e fontes confiáveis. A aplicação é executada com **Streamlit** e se conecta ao **Ollama** para gerar respostas com o modelo local `gpt-oss`.

> O Personal IA não substitui profissionais de Educação Física, médicos ou fisioterapeutas. Ele atua como uma ferramenta educacional e de apoio.

---

## Estrutura Sugerida

```text
src/
├── app.py              # Aplicação principal em Streamlit

```

### Estrutura Geral do Projeto

```text
personal-ia/
│
├── README.md
│
├── src/
│   ├── app.py
│   └──  README.md
│
├── data/
│   ├── perfil_usuario.json
│   ├── historico_treinos.csv
│   ├── feedback_usuario.csv
│   ├── base_exercicios.json
│   ├── base_conhecimento.json
│   └── fontes_confiaveis.json
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
```

---

## Arquivo Principal

### `app.py`

O arquivo `app.py` é responsável por:

- Carregar os arquivos da pasta `data/`;
- Montar o contexto do usuário teste **Cleiton da Silva**;
- Definir o `SYSTEM_PROMPT` do Personal IA;
- Enviar a pergunta do usuário para o modelo local no Ollama;
- Exibir a resposta em uma interface de chat com Streamlit;
- Manter o histórico da conversa na tela durante a sessão.

---

## Dados Utilizados

O `app.py` utiliza os seguintes arquivos:

| Arquivo | Finalidade |
|---|---|
| `perfil_usuario.json` | Dados do usuário teste, objetivos, metas, limitações e preferências |
| `historico_treinos.csv` | Histórico recente de treinos realizados |
| `feedback_usuario.csv` | Feedbacks sobre dor, fadiga, dificuldade e ajustes |
| `base_exercicios.json` | Exercícios, grupos musculares, substituições e cuidados |
| `base_conhecimento.json` | Princípios de treinamento, diretrizes e regras do agente |
| `fontes_confiaveis.json` | Fontes utilizadas como referência no projeto |

---

## Exemplo de `requirements.txt`

```text
streamlit
pandas
requests
```

Caso queira gerar o arquivo automaticamente, crie um arquivo chamado `requirements.txt` na raiz ou dentro da pasta `src/` e adicione as dependências acima.

---

## Configuração do Ollama

O projeto foi configurado para utilizar o modelo:

```python
MODELO = "gpt-oss"
```

Antes de rodar a aplicação, confirme se o Ollama está instalado e se o modelo está disponível.

### Verificar se o Ollama está instalado

```bash
ollama --version
```

### Verificar modelos instalados

```bash
ollama list
```

### Baixar o modelo, se necessário

```bash
ollama pull gpt-oss:20b
```

### Iniciar o servidor do Ollama

```bash
ollama serve
```

Em alguns casos, o Ollama já roda em segundo plano. Se isso acontecer, não é necessário executar `ollama serve` novamente.

---

## Como Rodar

### 1. Instalar dependências

No terminal, dentro da pasta principal do projeto, execute:

```bash
python -m pip install streamlit pandas requests
```

Ou, caso esteja usando `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

---

### 2. Confirmar a estrutura de pastas

Antes de rodar o projeto, verifique se o arquivo `app.py` está dentro da pasta `src/` e se a pasta `data/` está na raiz do projeto:

```text
personal-ia/
├── src/
│   └── app.py
└── data/
    ├── perfil_usuario.json
    ├── historico_treinos.csv
    ├── feedback_usuario.csv
    ├── base_exercicios.json
    ├── base_conhecimento.json
    └── fontes_confiaveis.json
```

---

### 3. Rodar a aplicação

No Windows PowerShell, dentro da pasta principal do projeto, execute:

```bash
python -m streamlit run .\src\app.py
```

Se estiver usando Linux ou macOS, o comando pode ser:

```bash
python -m streamlit run ./src/app.py
```

---

### 4. Acessar no navegador

Depois de rodar o comando, o Streamlit deve abrir automaticamente no navegador.

---

## Exemplos de Perguntas para Teste

Após abrir a aplicação, teste perguntas como:

```text
Monte um treino de pernas para o Cleiton considerando o desconforto no joelho.
```

```text
Quais exercícios posso substituir pelo agachamento livre?
```

```text
Crie uma divisão de treino para 5 dias por semana com foco em hipertrofia.
```

```text
Senti dor forte no joelho durante o leg press. O que devo fazer?
```

```text
Com base no histórico de treinos, posso aumentar a carga no supino?
```

Esses exemplos ajudam a validar se o Personal IA está considerando corretamente o perfil do usuário, limitações físicas, histórico, feedbacks e regras de segurança.

---

## Possíveis Erros e Soluções

### `streamlit` não é reconhecido

Se o comando abaixo não funcionar:

```bash
streamlit run .\src\app.py
```

Use:

```bash
python -m streamlit run .\src\app.py
```

---

### Modelo não encontrado

Se aparecer erro informando que o modelo não foi encontrado, verifique os modelos instalados:

```bash
ollama list
```

Depois confirme se o nome no código está igual ao nome listado pelo Ollama:

```python
MODELO = "gpt-oss:20b"
```

---

### Resposta demorou demais

Modelos maiores podem demorar mais para responder. Algumas soluções possíveis:

- Verificar se o Ollama está rodando;
- Reduzir o tamanho do contexto enviado ao modelo;
- Reduzir a quantidade de registros do histórico e feedback;
- Usar um modelo mais leve;
- Aumentar o `timeout` na chamada da API.

No código, os registros recentes já podem ser limitados assim:

```python
historico_recente = historico.tail(5)
feedback_recente = feedback.tail(5)
```

---

## Observações Finais

O `app.py` representa a aplicação funcional do projeto **Personal IA**.

Ele demonstra, na prática, os principais conceitos do projeto:

- Uso de IA Generativa;
- Engenharia de prompt;
- Personalização com dados mockados;
- Integração com base de conhecimento;
- Interface conversacional;
- Prevenção de alucinações;
- Regras de segurança para um domínio relacionado à saúde e treinamento físico.

A proposta do Personal IA é atuar como um assistente de apoio, ajudando o usuário a organizar e adaptar treinos de forma mais clara, segura e personalizada.
