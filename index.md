# Acompanhamento de Gastos e Subsídio

## Resumo financeiro
- Alimentacao diaria (x30 dias): R$ 840.00
- Despesas Fixas - Casa: R$ 889.00
- Despesas Medicas: R$ 1400.00
- Desenvolvimento Pessoal (itens com valor preenchido): R$ 0.00
- Subtotal conhecido: R$ -956.00

## Tabela de recorrencias
| Dia | Categoria | Descricao | Valor | Status | Observacoes |
|----:|------------|-----------|------:|--------|-------------|
| 11 | Despesas Fixas - Casa | Agua | 80.00 | Pendente | Recorrente mensal; vencimento dia 11 |
| 11 | Despesas Fixas - Casa | Luz | 300.00 | Pendente | Recorrente mensal; vencimento dia 11 |
| 11 | Despesas Fixas - Casa | Internet Fixa | 110.00 | Pendente | Recorrente mensal; vencimento dia 11 |
| 11 | Despesas Fixas - Casa | Internet Movel | 99.00 | Pendente | Recorrente mensal; vencimento dia 11 |
| 11 | Despesas Fixas - Casa | Faxina mensal | 300.00 | Pendente | Recorrente mensal; vencimento dia 11 (250 faxineira + 50 produtos) |
| 05 | Despesas Medicas | Natacao | 400.00 | Pago | Dezembro 2025 - Pago; Recorrente mensal; 5o dia util |
| 05 | Despesas Medicas | Tratamento dermatologico | 600.00 | Pendente | Recorrente mensal; 5o dia util |
| 05 | Despesas Medicas | Farmacia | 300.00 | Pago | Dezembro 2025 - Pago R$300; Ainda faltam R$200; Litio; ansiolíticos; analgésicos; anti-inflamatórios; protetor solar |
| 05 | Despesas Medicas | Oxigenio | 100.00 | Pendente | Recorrente mensal; 5o dia util |
| 15 | Desenvolvimento Pessoal | Assinatura do Github |  | Opcional | OPCIONAL - somente se sobrar recursos; ajustar valor |
| 15 | Desenvolvimento Pessoal | Assinatura do Copilot |  | Opcional | OPCIONAL - somente se sobrar recursos; ajustar valor |
| 15 | Desenvolvimento Pessoal | Assinatura do Gemini |  | Opcional | OPCIONAL - somente se sobrar recursos; ajustar valor |
| 15 | Desenvolvimento Pessoal | Registro de Obras Autorais |  | Opcional | OPCIONAL - eventual; somente se sobrar recursos |
| 15 | Desenvolvimento Pessoal | Divulgacao do Livro e dos Albuns |  | Opcional | OPCIONAL - campanhas somente se sobrar recursos |
| 01 | Alimentacao | Marmitex diario | 22.00 | Pago | Dezembro 2025 - Gasto R$290 até agora; multiplicar pelos dias do mes |
| 01 | Alimentacao | Agua 3L diaria | 8.00 | Pendente | Valor diário; multiplicar pelos dias do mes |
| 01 | Alimentacao | Frutas; Leite e Ingredientes diários | 20.00 | Pendente | Valor diário; multiplicar pelos dias do mes |
| 01 | Receita | Subsidio Familiar | -1000.00 | Pago | Contribuição familiar mensal |
|  |  |  |  |  |  |
|  | SITUACAO FINANCEIRA ATUAL |  |  |  |  |
|  | Conta | Descricao | Saldo | Status | Observacoes |
|  | PicPay | Saldo disponivel | 10.00 | Atual | Saldo atual em dinheiro (Entrada R$1000 subsídio - R$400 natação - R$300 farmácia - R$290 alimentação) |
|  | PicPay | Cartao de credito | -1100.00 | Pendente | Divida cartao |
|  | PicPay | Emprestimo Aviva | -355.00 | Pendente | Emprestimo para ir na Aviva |
|  | Will Bank | Saldo disponivel | 0.00 | Atual | Conta corrente |
|  | Will Bank | Cartao de credito | -700.00 | Pendente | Divida cartao |
|  | Nu Bank | Saldo disponivel | 0.00 | Atual | Conta corrente |
|  | Nu Bank | Cartao de credito | -103.00 | Pendente | Divida cartao |
|  | Receita Federal | MEI + Declaracao Anual | -900.00 | Pendente | Divida com Receita Federal |
|  |  |  |  |  |  |
|  | ESTOQUES VITAIS ATUAIS |  |  |  |  |
|  | Recurso | Quantidade | Dias Restantes | Prioridade | Observacoes |
|  | Agua potavel | 12 litros | 4 | CRÍTICA | 12 litros; consumo ~3L/dia |
|  | Comida (geral) | Variada | 7 | CRÍTICA | Leite; ovos; arroz; feijão; fubá; bananas |
|  | Medicacao (Litio + outros) | Quantidade ok | 30 | CRÍTICA | Medicamentos essenciais - próxima compra farmácia |
|  |  |  |  |  |  |
|  | PRIORIDADE MÁXIMA |  |  |  |  |
|  | Item | Valor | Vencimento | Status | Observacoes |
|  | Cartao PicPay | 1100.00 | Até 15/dez | Crítico | Usar crédito do cartão para pagar contas e se alimentar |
|  | Contas da Casa | 589.00 | Até 11/dez | Crítico | Água (80) + Luz (300) + Internet (209) |
|  | Alimentacao até 15/dez | ~700.00 | Contínuo | Crítico | Depois dia 7 estoques viram críticos |

## Downloads
- [Planilha CSV](./planilha_gastos.csv)
- [Proposta de Subsídio](./proposta_subsidio.md)
- [Instruções do Sistema](./instrucoes_sistema.md)

## Como atualizar
1) Ajuste valores e datas no CSV (mes/ano se precisar).
2) Para valores diários, defina `--days` ao gerar. Por padrão uso 30.
3) Rode este script para recriar o index: `python generate_index.py --days 30`.
