# Sistema de Agendamento

Um sistema simples e modular para gerenciamento de agendamentos, pacientes, médicos e pagamentos.
O projeto segue uma arquitetura organizada em Modelos, Serviços e Testes, facilitando manutenção, escalabilidade e testes unitários.

## Estrutura do Projeto
SistemaAgendamento_codigo/
│
├── Modelos/                 # Classes de domínio
│   ├── agendamento.py
│   ├── agenda.py
│   ├── consulta.py
│   ├── medico.py
│   ├── paciente.py
│   ├── pagamento.py
│   ├── pessoa.py
│   ├── recepcionista.py
│
│
├── Servicos/               # Regras de negócio
│   ├── agendamento_service.py
│   └── pagamento_service.py
│
├── Testes/                 # Testes unitários
│   ├── test_agendamento.py
│   └── test_pagamento.py
│
├── main.py                 # Ponto de entrada da aplicação
├── README.md               # (Este arquivo)
└── requirements.txt        # Dependências


## Funcionalidades
Cadastro de pacientes e médicos
Criação e gerenciamento de agendamentos
Vinculação de consultas com horários
Processamento básico de pagamentos
Camada de serviços separada
Testes automatizados

## Tecnologias Utilizadas
Python 3.11+
Arquitetura orientada a objetos
Testes com pytest

## Instalação
Clone o repositório:
git clone https://github.com/arthurlorenzett/ProjetoPOO.git
cd SistemaAgendamento


## Instale as dependências:
pip install -r requirements.txt

## Como Executar
Execute o arquivo principal:
python main.py

## Rodando os Testes
Use o pytest:
pytest -v

## Estrutura de Classes
Modelos
Pessoa – Classe base para Paciente e Médico
Paciente
Médico
Recepcionista
Agendamento
Agenda
Consulta
Pagamento
Serviços
AgendamentoService – Responsável por criar e organizar agendamentos
PagamentoService – Realiza validação e registro de pagamentos

## Exemplo de Uso
from Modelos.paciente import Paciente
from Modelos.medico import Medico
from Servicos.agendamento_service import AgendamentoService
paciente = Paciente("João", 30, "12345678900")
medico = Medico("Dra. Ana", 45, "CRM-1234")
ag_service = AgendamentoService()
agendamento = ag_service.criar_agendamento(paciente, medico, "10/02/2025 15:00")
print(agendamento)

## Melhorias Futuras
Persistência de dados (SQLite ou PostgreSQL)
API REST (FastAPI ou Flask)
Interface web ou mobile
Sistema de notificações