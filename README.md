# 🏋️ Personal I.A — Assistente Inteligente de Treinamento Físico com IA Generativa

## Contexto

O **Personal I.A** é um projeto de agente inteligente desenvolvido com IA Generativa para apoiar a montagem, adaptação e acompanhamento de treinos físicos.

A proposta do projeto é transformar a ideia original de um agente financeiro em um assistente voltado para treinamento físico, utilizando dados mockados do usuário, histórico de treinos, feedbacks, base de exercícios e fontes confiáveis para gerar respostas mais personalizadas e seguras.

O agente foi pensado para auxiliar o usuário em dúvidas sobre treino, organização semanal, substituição de exercícios, progressão, volume, descanso e adaptações de acordo com limitações físicas informadas.

> O Personal I.A não substitui profissionais de Educação Física, médicos ou fisioterapeutas. Ele atua apenas como uma ferramenta de apoio educacional, organizacional e informativo.

---

## Objetivo do Projeto

Desenvolver um assistente inteligente capaz de:

- Criar sugestões de treinos personalizadas com base no perfil do usuário;
- Adaptar exercícios conforme limitações físicas, dores, lesões relatadas ou equipamentos disponíveis;
- Responder dúvidas gerais sobre treino, execução de exercícios, descanso, volume e progressão;
- Acompanhar a evolução do usuário por meio do histórico de treinos e feedbacks;
- Utilizar fontes confiáveis e diretrizes reconhecidas para apoiar suas recomendações;
- Evitar respostas inseguras, diagnósticos médicos ou recomendações sem embasamento;
- Personalizar sugestões com base no contexto do usuário;
- Garantir maior segurança e confiabilidade nas respostas por meio de regras anti-alucinação.

---

# O Que Foi Entregue no Projeto

## 1. Documentação do Agente

A documentação do agente define o caso de uso, funcionamento, persona, tom de voz, arquitetura e limites de segurança do Personal I.A.

### Caso de Uso

Muitas pessoas desejam treinar com mais qualidade, mas têm dificuldade para montar uma rotina adequada ao seu objetivo, nível de experiência, disponibilidade, equipamentos disponíveis e limitações físicas.

Além disso, dúvidas sobre substituição de exercícios, dores, progressão de carga, descanso e divisão de treino são comuns para usuários iniciantes e intermediários.

O **Personal I.A** resolve esse problema oferecendo um assistente virtual capaz de analisar o contexto informado pelo usuário e sugerir treinos, adaptações e explicações de forma personalizada, segura e coerente com princípios básicos de treinamento físico.

### Persona e Tom de Voz

**Nome do agente:** Personal I.A

**Personalidade:** didático, motivador, responsável, acessível e consultivo.

**Tom de voz:** claro, amigável, objetivo, profissional e cuidadoso.

Exemplo de comunicação:

> "Com base no seu objetivo e no seu nível atual, podemos ajustar esse treino para melhorar sua progressão sem aumentar excessivamente o risco de sobrecarga."

O agente deve evitar frases absolutas, promessas exageradas ou tom autoritário, como:

> "Esse treino garante resultado em 30 dias."

---

## 2. Arquitetura do Projeto

Fluxo geral da aplicação:

```text
Usuário
↓
Interface Streamlit
↓
app.py
↓
System Prompt + Contexto do Usuário
↓
Base de Conhecimento / Dados Mockados
↓
Ollama
↓
Modelo gpt-oss:20b
↓
Resposta personalizada e segura
```

A aplicação foi construída com **Python**, utilizando **Streamlit** para a interface de chat e **Ollama** para executar o modelo localmente.

---

## 3. Segurança e Prevenção de Alucinações

Para garantir respostas mais confiáveis, o Personal I.A segue algumas regras:

- Utilizar apenas informações fornecidas pelo usuário e dados presentes na base de conhecimento;
- Não inventar estudos, referências ou recomendações;
- Não diagnosticar lesões ou condições médicas;
- Não prescrever medicamentos, suplementos, anabolizantes ou tratamentos clínicos;
- Recomendar profissional habilitado em casos de dor intensa, lesões, sintomas persistentes ou condições médicas;
- Informar claramente quando não possuir dados suficientes para responder com segurança;
- Explicar as recomendações de forma simples, didática e transparente;
- Evitar promessas de resultados garantidos.

---

# 4. Base de Conhecimento

A base de conhecimento foi adaptada do contexto financeiro para o contexto de treinamento físico.

Os arquivos mockados ficam na pasta `data/` e representam o perfil do usuário teste, treinos realizados, feedbacks, exercícios disponíveis, regras de segurança e fontes confiáveis.

## Arquivos Utilizados

| Arquivo | Formato | Descrição |
|---|---|---|
| `perfil_usuario.json` | JSON | Dados do usuário teste, como nome, idade, altura, peso, objetivo, metas, frequência, limitações e preferências |
| `historico_treinos.csv` | CSV | Histórico de treinos realizados, incluindo exercícios, séries, repetições, cargas e observações |
| `feedback_usuario.csv` | CSV | Feedbacks do usuário sobre dor, fadiga, dificuldade, adaptação e ações sugeridas |
| `base_exercicios.json` | JSON | Lista de exercícios, grupos musculares, equipamentos, substituições, séries, repetições e cuidados |
| `base_conhecimento.json` | JSON | Princípios de treinamento, diretrizes gerais, parâmetros sugeridos e regras do agente |
| `fontes_confiaveis.json` | JSON | Fontes utilizadas como referência para embasar o projeto |

---

## Usuário Teste

O usuário mockado do projeto é:

```text
Cleiton da Silva
```

Ele é utilizado como base para testar as respostas personalizadas do agente.

O perfil contempla informações como:

- Idade;
- Altura;
- Peso;
- Objetivo principal;
- Frequência de treino atual e desejada;
- Nível de experiência;
- Equipamentos disponíveis;
- Preferências de treino;
- Limitações físicas;
- Metas;
- Regras de segurança.

---

# 5. Prompts do Agente

O comportamento do Personal I.A é definido por um `SYSTEM_PROMPT` presente no arquivo `app.py`.

O prompt orienta o agente a:

- Atuar como assistente de apoio ao treinamento físico;
- Responder de forma clara, amigável e didática;
- Personalizar respostas com base nos dados disponíveis;
- Respeitar limitações físicas e sinais de risco;
- Evitar diagnóstico médico;
- Evitar prescrição de medicamentos, suplementos ou anabolizantes;
- Não prometer resultados garantidos;
- Admitir limitações quando não tiver informação suficiente.

## System Prompt Resumido

```text
Você é o Personal IA, um assistente inteligente, amigável e didático de apoio ao treinamento físico.

Seu objetivo é ajudar o usuário a montar, entender e adaptar treinos físicos de forma simples, segura e personalizada, usando os dados do próprio usuário como base para exemplos e recomendações práticas.

Nunca realize diagnóstico médico, nunca prescreva medicamentos ou suplementos, não substitua profissionais habilitados e sempre priorize segurança, individualização e progressão gradual.
```

---

# 6. Aplicação Funcional

A aplicação funcional foi implementada no arquivo:

```text
src/app.py
```

Ela utiliza:

- `Python`
- `Streamlit`
- `Pandas`
- `Requests`
- `Ollama`
- Modelo local `gpt-oss:20b`

## Principais responsabilidades do `app.py`

O arquivo `app.py` é responsável por:

- Carregar os dados da pasta `data/`;
- Formatar o perfil do usuário;
- Formatar histórico de treinos;
- Formatar feedbacks recentes;
- Formatar base de exercícios;
- Formatar base de conhecimento;
- Formatar fontes confiáveis;
- Criar o contexto final do agente;
- Enviar o prompt para o Ollama;
- Exibir a resposta em uma interface de chat com Streamlit.

---

## Modelo Utilizado

O projeto foi atualizado para usar o modelo local:

```python
MODELO = "gpt-oss:20b"
```

O endpoint configurado no código é:

```python
OLLAMA_URL = "http://localhost:11434/api/generate"
```

---

# 7. Estrutura do Repositório

A estrutura final recomendada do projeto é:

```text
personal-ia/
│
├── README.md
│
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
│
├── src/
│   ├── app.py
│   └── README.md

```

---

# 8. Requirements

O projeto utiliza as seguintes bibliotecas:

```text
streamlit
pandas
requests
```

Um exemplo de `requirements.txt` seria:

```text
streamlit
pandas
requests
```

---

# 9. Pitch do Projeto

O **Personal I.A** é um assistente inteligente de treinamento físico que utiliza IA Generativa para apoiar usuários na criação, adaptação e acompanhamento de treinos personalizados.

Diferente de aplicativos que oferecem treinos genéricos, o Personal I.A considera o perfil do usuário, objetivos, nível de experiência, disponibilidade, equipamentos, histórico de treino, feedbacks e limitações físicas relatadas.

Na prática, o usuário interage com um chatbot, faz perguntas sobre treino e recebe respostas baseadas em dados mockados e regras de segurança. O agente também consegue sugerir adaptações de exercícios e orientar o usuário a procurar um profissional habilitado em situações sensíveis.

A inovação da solução está na combinação entre IA Generativa, personalização, histórico do usuário, base de conhecimento e preocupação com segurança. O Personal I.A não substitui profissionais da área da saúde ou Educação Física, mas atua como uma ferramenta de apoio para tornar o processo de treino mais organizado, acessível e individualizado.

---

# 10. Possíveis Melhorias Futuras

Algumas evoluções possíveis para o projeto:

- Criar cadastro de novos usuários pela interface;
- Permitir upload de novos históricos de treino;
- Registrar novos feedbacks diretamente pelo Streamlit;
- Salvar conversas automaticamente;
- Criar dashboard de evolução do usuário;
- Implementar busca semântica na base de exercícios;
- Permitir exportação de treinos em PDF ou CSV;
- Separar a lógica do agente em um arquivo `agente.py`;
- Separar configurações em um arquivo `config.py`;
- Criar testes automatizados para validar respostas seguras.

---

# 11. Dicas Finais

- Comece testando perguntas simples;
- Valide se o agente está usando os dados de Cleiton da Silva;
- Teste perguntas envolvendo limitações físicas;
- Verifique se o agente recusa pedidos fora do escopo;
- Observe se o agente evita diagnósticos e prescrições;
- Ajuste o prompt conforme os testes;
- Reduza o contexto caso o modelo demore muito para responder.

---

# Conclusão

O projeto **Personal I.A** demonstra como IA Generativa pode ser aplicada de forma responsável em um domínio relacionado à saúde e treinamento físico.

A solução reúne:

- Interface conversacional;
- Modelo local via Ollama;
- Dados mockados estruturados;
- Engenharia de prompt;
- Base de conhecimento;
- Regras de segurança;
- Estratégias anti-alucinação;
- Personalização baseada no perfil do usuário.

Com isso, o Personal I.A atua como um assistente educacional e organizacional para apoiar o usuário na compreensão, estruturação e adaptação de treinos físicos.
