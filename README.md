# Sistema-Banc-rio-DIO
Este projeto é um desafio proposto pela DIO.

Objetivo Geral
O objetivo principal é criar um sistema bancário simples em Python que suporte três operações básicas: depositar, sacar e visualizar o extrato. 

Funcionalidades Implementadas
1. Operação de Depósito
Permite depositar apenas valores positivos. 

Não há necessidade de identificar agência ou conta, pois a V1 do projeto opera com apenas um usuário. 

Todos os depósitos são armazenados e exibidos na operação de extrato. 

2. Operação de Saque
Permite realizar até 3 saques diários. 

O limite máximo por saque é de R$ 500,00. 

O sistema verifica se há saldo suficiente para o saque, exibindo uma mensagem caso contrário. 

Todos os saques são armazenados e exibidos na operação de extrato. 

3. Operação de Extrato
Lista todas as movimentações (depósitos e saques) realizadas na conta. 

Exibe o saldo atual da conta ao final da listagem. 

Se não houver movimentações, a mensagem "Não foram realizadas movimentações." é exibida. 

Os valores são exibidos no formato 

R$ xxx.xx. 

