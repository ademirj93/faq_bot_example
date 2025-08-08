# faq_bot_example
Sistema com respostas estilo Perguntas frequentes

Este projeto é um exemplo de um bot de perguntas e respostas (FAQ) simples, projetado para demonstrar como um sistema de lógica central pode ser integrado a diferentes interfaces de usuário. Ele serve como uma base para projetos mais complexos.

Funcionalidades Principais
Lógica Central de FAQ: O sistema principal, em core/faq_engine.py, gerencia a lógica de busca e resposta. Ele tenta encontrar a resposta correta para uma pergunta seguindo uma estratégia de três passos:

Match Exato: A busca por uma correspondência exata da pergunta na base de dados.

Match por Palavra-Chave: Se não houver um match exato, o sistema busca por palavras-chave predefinidas na pergunta.

Match por Aproximação: Se as duas primeiras tentativas falharem, ele verifica se alguma das chaves da base de dados está contida na pergunta.

Base de Dados Simples: As perguntas e respostas estão contidas em um dicionário simples em core/faq_data.py, o que permite fácil modificação ou substituição por uma base de dados mais robusta, como JSON ou um banco de dados.

Múltiplas Interfaces: O projeto demonstra a flexibilidade da lógica central ao integrar-se a várias interfaces diferentes:

Desktop (Tkinter): Uma interface de desktop simples, criada com a biblioteca Tkinter, que permite ao usuário digitar uma pergunta e ver a resposta em tempo real.

Web (Flask): Uma aplicação web que roda com o framework Flask, oferecendo uma interface via navegador para interagir com o bot.

Bot do Discord: Um bot que responde a perguntas enviadas em um servidor do Discord usando o prefixo de comando !faq.

Bot do Telegram: Um bot para o Telegram que responde a perguntas diretamente em um chat.

Como Executar
O arquivo main.py é o ponto de entrada principal do projeto. Ele utiliza threads para iniciar várias interfaces simultaneamente.

Instalação de Dependências: Certifique-se de ter as bibliotecas necessárias instaladas. As dependências específicas para cada interface (Discord, Flask, Telegram) precisarão ser instaladas separadamente.

Configuração de Tokens (Opcional): Para os bots do Discord e Telegram, você precisará configurar os tokens de API. Estes podem ser definidos como variáveis de ambiente (DISCORD_TOKEN e TELEGRAM_TOKEN) ou inseridos diretamente nos arquivos discord_bot.py e telegram_bot.py, respectivamente.

Execução:

Para iniciar todas as interfaces (Tkinter, Flask), execute o arquivo main.py diretamente.

Para iniciar os bots do Discord ou Telegram, altere os sinalizadores start_discord_bot ou start_telegram_bot para True no arquivo main.py.

Para rodar uma interface individualmente, você pode executar o arquivo correspondente diretamente, como python interfaces/tkinter_app.py.
