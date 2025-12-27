# Instruções do Sistema de Gastos e Subsídio

## Orientação de uso para senhorito

- Todas as respostas e interações devem tratar o usuário como "senhorito".
- Sempre que o senhorito responder "Fiat Lux", considere como uma afirmativa ou autorização para prosseguir.

## Visão geral

- `planilha_gastos.csv`: lançamento diário de receitas e despesas.
- `proposta_subsidio.md`: texto-base da proposta a partir dos valores consolidados.

## Como usar a planilha de gastos (Excel/Google Sheets)

1. Abra Excel ou Google Sheets e importe `planilha_gastos.csv` (delimitador: vírgula, codificação UTF-8).
2. Mantenha cabeçalhos originais: `Data, Categoria, Descricao, FormaPagamento, Valor, Tipo, CentroDeCusto, Status, Observacoes`.
3. Regra de sinal: despesas em valor positivo com `Tipo=Despesa`; receitas podem ser negativas ou `Tipo=Receita` com valor positivo (se preferir, use só positivo e ajuste nos relatórios).
4. Crie validação de dados para colunas:
   - `Tipo`: lista {Despesa, Receita}
   - `Status`: {Pago, Pendente}
   - `Categoria`: ajuste à sua realidade (Transporte, Alimentacao, Moradia, Saude, Educacao, Lazer, Outros).
5. Sugestão de tabela dinâmica (pivot) de resumo:
   - Linhas: Categoria
   - Colunas: Tipo
   - Valores: Soma de Valor
   - Filtro: Status = Pago
6. Total rápido em fórmula (Excel/Sheets):
   - Total despesas pagas: `=SOMASES(Valor;Tipo;"Despesa";Status;"Pago")`
   - Total receitas recebidas: `=SOMASES(Valor;Tipo;"Receita";Status;"Pago")`
   - Saldo: receitas - despesas.

## Boas práticas de lançamento

- Preencha `Data` no formato ISO (AAAA-MM-DD) para evitar erros regionais.
- Use `CentroDeCusto` ou projeto para separar iniciativas (ex.: ProjetoX, Administrativo).
- Registre observações quando algo depender de reembolso ou aprovação.
- Feche o mês: filtre por mês, Status=Pago e gere resumo para a proposta.

## Como gerar a proposta de subsídio

1. Consolidar orçamento: use o resumo de categoria e copie totais para a tabela do `proposta_subsidio.md`.
2. Preencher seções: contexto, objetivos, entregas, público-alvo, cronograma, indicadores e riscos.
3. Evidenciar contrapartidas: se houver recursos próprios/terceiros, destaque-os na tabela.
4. Exportar: salve em PDF via editor Markdown ou ao converter para Word/Google Docs.

## Adaptação rápida do modelo

- Acrescente novas categorias na tabela dinâmica sem mudar o cabeçalho.
- Se precisar de múltiplos projetos: duplique a planilha em abas diferentes ou use a coluna `CentroDeCusto` como filtro.
- Para acompanhar pendências: filtre `Status=Pendente` semanalmente e atualize.

## Checklist de envio do subsídio

- Orçamento conferido e datas coerentes.
- Indicadores mensuráveis definidos.
- Riscos principais listados com mitigação.
- Cronograma com marcos e responsáveis.
- Anexos mencionados e acessíveis.
