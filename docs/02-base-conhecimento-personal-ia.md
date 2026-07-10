# Base de Conhecimento

## Dados Utilizados

A base de conhecimento do **Personal IA** foi adaptada, o agente passa a utilizar dados mockados relacionados ao perfil físico do usuário, histórico de treinos, feedbacks, exercícios disponíveis e recomendações gerais baseadas em fontes confiáveis.

Esses dados serão utilizados para personalizar as respostas do agente, permitindo que ele recomende treinos, sugira adaptações de exercícios e acompanhe a evolução do usuário de forma mais contextualizada e segura.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_usuario.json` | JSON | Armazena informações básicas do usuário, como idade, altura, peso, objetivo, nível de experiência, disponibilidade, equipamentos e limitações físicas relatadas. |
| `historico_treinos.csv` | CSV | Registra os treinos realizados anteriormente, incluindo exercícios, séries, repetições, cargas e observações. Auxilia o agente a acompanhar evolução e sugerir progressões. |
| `feedback_usuario.csv` | CSV | Armazena percepções do usuário após os treinos, como nível de fadiga, dificuldade, dor, desconforto e comentários. É utilizado para adaptar os próximos treinos. |
| `base_exercicios.json` | JSON | Contém uma lista de exercícios, grupos musculares trabalhados, nível de dificuldade, equipamentos necessários, orientações gerais e possíveis substituições. |
| `base_conhecimento.json` | JSON | Reúne diretrizes gerais de treinamento físico, princípios de progressão, descanso, volume, intensidade e segurança, com base em fontes confiáveis. |
| `fontes_confiaveis.json` | JSON | Lista referências utilizadas como apoio, como diretrizes da Organização Mundial da Saúde, ACSM, NSCA e outras instituições reconhecidas. |

> [!TIP]
> Como o projeto envolve saúde, atividade física e segurança, a base de conhecimento deve priorizar fontes confiáveis e reconhecidas. O agente não deve utilizar informações sem validação, fóruns aleatórios ou promessas de resultados rápidos.

---

## Adaptações nos Dados

Os dados mockados originais do projeto financeiro foram modificados para representar um cenário de treinamento físico personalizado. A adaptação foi feita para que o **Personal IA** consiga responder de forma coerente ao novo caso de uso.

As principais adaptações foram:

- Substituição do `perfil_investidor.json` por `perfil_usuario.json`, contendo informações do usuário relevantes para a montagem de treinos.
- Substituição de `transacoes.csv` por `historico_treinos.csv`, permitindo o acompanhamento dos treinos realizados.
- Substituição de `historico_atendimento.csv` por `feedback_usuario.csv`, registrando percepções do usuário após cada treino.
- Substituição de `produtos_financeiros.json` por `base_exercicios.json`, com exercícios, músculos trabalhados, equipamentos e alternativas.
- Criação do arquivo `base_conhecimento.json`, com princípios gerais de treinamento físico baseados em evidências.
- Criação do arquivo `fontes_confiaveis.json`, para documentar as referências utilizadas pelo agente.

Essas adaptações permitem que o agente deixe de atuar como um consultor financeiro e passe a funcionar como um assistente inteligente de treinamento físico, focado em personalização, segurança e acompanhamento contínuo.

### Exemplo de `perfil_usuario.json`

```json
{
  "nome": "Cleiton da Silva",
  "idade": 28,
  "altura_cm": 176,
  "peso_kg": 76,
  "objetivo": "hipertrofia",
  "nivel_experiencia": "intermediario",
  "dias_disponiveis_por_semana": 5,
  "tempo_por_treino_minutos": 70,
  "equipamentos_disponiveis": "academia completa",
  "limitacoes": ["desconforto leve no joelho direito"],
  "preferencias": ["priorizar musculacao", "evitar corrida"]
}
```

### Exemplo de `historico_treinos.csv`

```csv
data,grupo_muscular,exercicio,series,repeticoes,carga_kg,observacoes
2026-07-01,peito,supino reto,4,8,70,execucao boa
2026-07-01,triceps,triceps corda,3,12,25,leve fadiga
2026-07-02,costas,puxada frontal,4,10,60,sem dor
2026-07-03,pernas,leg press,4,12,120,desconforto leve no joelho
```

### Exemplo de `feedback_usuario.csv`

```csv
data,treino,dor,fadiga,dificuldade,comentario
2026-07-01,superiores,nenhuma,moderada,7,treino bem executado
2026-07-02,costas,nenhuma,baixa,6,boa recuperação
2026-07-03,inferiores,joelho direito,alta,8,desconforto no leg press
```

### Exemplo de `base_exercicios.json`

```json
{
  "agachamento livre": {
    "grupo_muscular": ["quadriceps", "gluteos", "posterior de coxa"],
    "equipamento": "barra",
    "nivel": "intermediario",
    "substituicoes": ["leg press", "agachamento no smith", "cadeira extensora"],
    "observacoes": "Exige boa mobilidade, estabilidade e controle técnico."
  },
  "supino reto": {
    "grupo_muscular": ["peitoral", "triceps", "ombros"],
    "equipamento": "barra",
    "nivel": "intermediario",
    "substituicoes": ["supino com halteres", "supino máquina", "flexão de braço"],
    "observacoes": "Importante controlar a amplitude e manter estabilidade dos ombros."
  },
  "puxada frontal": {
    "grupo_muscular": ["costas", "biceps"],
    "equipamento": "polia",
    "nivel": "iniciante a intermediario",
    "substituicoes": ["barra fixa assistida", "remada baixa", "remada curvada"],
    "observacoes": "Manter controle do movimento e evitar compensações excessivas."
  }
}
```

### Exemplo de `base_conhecimento.json`

```json
{
  "principios_treinamento": {
    "progressao": "A evolução do treino deve ocorrer de forma gradual, considerando carga, volume, intensidade e recuperação.",
    "individualizacao": "As recomendações devem considerar objetivo, nível de experiência, disponibilidade, limitações e resposta individual do usuário.",
    "recuperacao": "Descanso adequado entre sessões e grupos musculares é importante para desempenho e redução de risco de sobrecarga.",
    "seguranca": "Relatos de dor intensa, tontura, falta de ar, lesões ou sintomas persistentes devem ser direcionados a profissionais habilitados."
  }
}
```

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV da pasta `data/` serão carregados no início da execução da aplicação. No protótipo, esse carregamento pode ser feito diretamente no código da aplicação, por exemplo, utilizando Python com bibliotecas como `pandas` para arquivos CSV e `json` para arquivos JSON.

A aplicação poderá seguir o seguinte fluxo:

1. O usuário acessa o chatbot do **Personal IA**.
2. A aplicação carrega o perfil do usuário em `perfil_usuario.json`.
3. O histórico de treinos é carregado a partir de `historico_treinos.csv`.
4. Os feedbacks anteriores são carregados a partir de `feedback_usuario.csv`.
5. A base de exercícios é consultada em `base_exercicios.json`.
6. A base de conhecimento e fontes confiáveis são utilizadas para validar e fundamentar as recomendações.
7. O agente monta uma resposta personalizada com base nesses dados.

Em uma versão inicial, os dados podem ser carregados no início da sessão e enviados como contexto para o modelo. Em uma versão mais avançada, o agente pode consultar dinamicamente apenas os trechos relevantes da base de conhecimento, utilizando técnicas de busca semântica ou RAG.

### Como os dados são usados no prompt?

Os dados não devem ser inseridos integralmente no system prompt. O system prompt deve conter apenas as regras gerais de comportamento, segurança e limites do agente.

Os dados do usuário, histórico de treinos, feedbacks e exercícios disponíveis devem ser adicionados dinamicamente ao contexto da conversa, conforme a necessidade da pergunta.

Exemplo:

- Se o usuário pedir um treino completo, o agente deve consultar o perfil, objetivo, dias disponíveis, equipamentos e limitações.
- Se o usuário pedir substituição de exercício, o agente deve consultar a `base_exercicios.json` e verificar alternativas compatíveis.
- Se o usuário relatar dor, o agente deve consultar o feedback, evitar recomendações arriscadas e sugerir avaliação com profissional habilitado.
- Se o usuário pedir progressão de carga, o agente deve consultar o `historico_treinos.csv` e verificar evolução recente.

Essa estratégia reduz o risco de respostas genéricas e melhora a personalização do atendimento.

---

## Exemplo de Contexto Montado

Abaixo está um exemplo de como os dados podem ser formatados e enviados ao agente durante uma interação.

```text
Dados do Usuário:
- Nome: Cleiton da Silva
- Idade: 28 anos
- Altura: 176 cm
- Peso: 76 kg
- Objetivo: Hipertrofia
- Nível de experiência: Intermediário
- Disponibilidade: 5 dias por semana
- Tempo por treino: 70 minutos
- Equipamentos disponíveis: Academia completa
- Limitações relatadas: Desconforto leve no joelho direito
- Preferências: Priorizar musculação e evitar corrida

Histórico recente de treinos:
- 01/07/2026: Peito e tríceps
  - Supino reto: 4 séries de 8 repetições com 70 kg
  - Tríceps corda: 3 séries de 12 repetições com 25 kg
  - Observação: Leve fadiga, sem dor

- 02/07/2026: Costas e bíceps
  - Puxada frontal: 4 séries de 10 repetições com 60 kg
  - Observação: Boa execução e sem dor

- 03/07/2026: Pernas
  - Leg press: 4 séries de 12 repetições com 120 kg
  - Observação: Desconforto leve no joelho direito

Feedback do usuário:
- Fadiga: Alta após treino de pernas
- Dor: Joelho direito durante exercícios de membros inferiores
- Dificuldade percebida: 8/10

Base de exercícios relevante:
- Agachamento livre:
  - Grupo muscular: Quadríceps, glúteos e posterior de coxa
  - Substituições possíveis: Leg press, agachamento no smith, cadeira extensora
  - Observação: Exige boa mobilidade e controle técnico

- Leg press:
  - Grupo muscular: Quadríceps e glúteos
  - Possíveis ajustes: Reduzir amplitude, diminuir carga, controlar execução
  - Observação: Deve ser evitado ou ajustado em caso de desconforto persistente

Instruções para o agente:
- Personalizar a resposta com base no perfil e histórico do usuário.
- Não diagnosticar a causa da dor no joelho.
- Não recomendar tratamento médico.
- Sugerir alternativas seguras e progressivas.
- Recomendar avaliação com profissional habilitado caso a dor persista ou aumente.
```

### Exemplo de resposta esperada do Personal IA

```text
Com base no seu histórico recente e no desconforto relatado no joelho direito durante o treino de pernas, a recomendação mais segura é reduzir temporariamente a intensidade dos exercícios que geram desconforto e priorizar movimentos com maior controle.

Para o próximo treino de inferiores, uma adaptação possível seria:

- Reduzir a carga do leg press e trabalhar com amplitude confortável.
- Evitar agachamento livre pesado enquanto houver desconforto.
- Utilizar cadeira extensora com carga leve a moderada, se não houver dor.
- Incluir exercícios de glúteos e posterior de coxa com menor sobrecarga direta no joelho.

Como há relato de dor, o ideal é que um profissional de Educação Física ou fisioterapeuta avalie sua execução e sua condição individual. Caso a dor aumente ou persista, evite insistir nos exercícios que provocam desconforto.
```

---

## Considerações sobre Segurança dos Dados

Como o projeto utiliza informações relacionadas ao usuário, mesmo que mockadas, alguns cuidados devem ser considerados:

- Utilizar dados fictícios no protótipo.
- Evitar armazenar informações sensíveis reais sem consentimento.
- Não expor dados pessoais em logs públicos.
- Não compartilhar histórico de treino ou limitações físicas sem autorização.
- Deixar claro que o agente é um assistente de apoio e não substitui profissionais habilitados.

---

## Fontes Confiáveis Sugeridas

A base de conhecimento do **Personal IA** pode ser construída com apoio de fontes reconhecidas, como:

- Organização Mundial da Saúde (WHO) — diretrizes gerais sobre atividade física e comportamento sedentário.
- American College of Sports Medicine (ACSM) — recomendações sobre prescrição de exercícios e treinamento físico.
- National Strength and Conditioning Association (NSCA) — princípios de força, condicionamento e progressão.
- Artigos científicos revisados por pares disponíveis em bases como PubMed.
- Diretrizes e materiais de instituições oficiais de saúde e esporte.

Essas fontes devem ser usadas como referência geral para apoiar as respostas do agente, sem substituir avaliação individual de profissionais de Educação Física, médicos ou fisioterapeutas.
