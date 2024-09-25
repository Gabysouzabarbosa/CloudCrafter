# CloudCrafter

CloudCrafter é um projeto desenvolvido para automatizar o fluxo de integração e entrega contínua (CI/CD) utilizando GitHub Actions e Docker. O projeto foi projetado com foco na entrega ágil e monitoramento automatizado de commits e merges, com notificações integradas no Discord.

Funcionalidades Principais
Integração Contínua (CI): Configuração de workflows para executar testes automatizados e validações de código sempre que novos commits são enviados ao repositório.
Entrega Contínua (CD): Automação do processo de build e deploy utilizando Docker, garantindo que a aplicação esteja sempre pronta para ser implantada.
Dockerização: Criação de um container Docker para a aplicação FastAPI, facilitando a execução e a implantação do projeto em diferentes ambientes.
Notificações no Discord: Integração de alertas via Discord para notificar sobre cada commit e merge realizado, facilitando o monitoramento das atividades no repositório.
Branch Management: Criação e gerenciamento de múltiplas branches com a devida integração e revisão de pull requests, promovendo um fluxo de desenvolvimento colaborativo e organizado.
Tecnologias Utilizadas
FastAPI: Framework para desenvolvimento de APIs com Python.
Docker: Containerização da aplicação para facilitar o desenvolvimento, teste e deploy.
GitHub Actions: Automação dos fluxos de CI/CD.
Discord Webhooks: Notificações em tempo real sobre o status do projeto e atividades realizadas no repositório.

