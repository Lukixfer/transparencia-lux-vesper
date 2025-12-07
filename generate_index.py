import argparse
import csv
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parent
CSV_PATH = ROOT / "planilha_gastos.csv"
DEFAULT_OUTPUT = ROOT / "index.md"


def parse_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def load_rows(csv_path: Path) -> List[Dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def summarize(rows: List[Dict[str, str]], daily_days: int) -> Dict[str, float]:
    totals = {
        "Alimentacao diaria": 0.0,
        "Despesas Fixas - Casa": 0.0,
        "Despesas Medicas": 0.0,
        "Desenvolvimento Pessoal": 0.0,
        "Geral": 0.0,
    }
    for row in rows:
        category = row.get("Categoria", "").strip()
        obs = (row.get("Observacoes", "") or "").lower()
        value = parse_float(row.get("Valor", "0"))

        # Trate valores em aberto como zero
        if value == 0:
            continue

        # Itens marcados como valor diário multiplicam pelos dias fornecidos
        multiplier = daily_days if "valor diário" in obs else 1
        amount = value * multiplier

        if category.lower().startswith("alimentacao") and "valor diário" in obs:
            totals["Alimentacao diaria"] += amount
        elif category.startswith("Despesas Fixas - Casa"):
            totals["Despesas Fixas - Casa"] += amount
        elif category.startswith("Despesas Medicas"):
            totals["Despesas Medicas"] += amount
        elif category.startswith("Desenvolvimento Pessoal"):
            totals["Desenvolvimento Pessoal"] += amount

        totals["Geral"] += amount

    return totals


def render_table(rows: List[Dict[str, str]]) -> str:
    header = "| Dia | Categoria | Descricao | Valor | Status | Observacoes |\n|----:|------------|-----------|------:|--------|-------------|"
    lines = []
    for row in rows:
        dia = row.get("Data", "").strip()
        cat = row.get("Categoria", "").strip()
        desc = row.get("Descricao", "").strip()
        val = row.get("Valor", "").strip()
        status = row.get("Status", "").strip()
        obs = row.get("Observacoes", "").strip()
        lines.append(f"| {dia} | {cat} | {desc} | {val or ''} | {status or ''} | {obs or ''} |")
    return "\n".join([header] + lines)


def build_markdown(rows: List[Dict[str, str]], totals: Dict[str, float], daily_days: int) -> str:
    lines = [
        "# Acompanhamento de Gastos e Subsídio",
        "",
        "## Resumo financeiro",
        f"- Alimentacao diaria (x{daily_days} dias): R$ {totals['Alimentacao diaria']:.2f}",
        f"- Despesas Fixas - Casa: R$ {totals['Despesas Fixas - Casa']:.2f}",
        f"- Despesas Medicas: R$ {totals['Despesas Medicas']:.2f}",
        f"- Desenvolvimento Pessoal (itens com valor preenchido): R$ {totals['Desenvolvimento Pessoal']:.2f}",
        f"- Subtotal conhecido: R$ {totals['Geral']:.2f}",
        "",
        "## Tabela de recorrencias",
        render_table(rows),
        "",
        "## Downloads",
        "- [Planilha CSV](./planilha_gastos.csv)",
        "- [Proposta de Subsídio](./proposta_subsidio.md)",
        "- [Instruções do Sistema](./instrucoes_sistema.md)",
        "",
        "## Como atualizar",
        "1) Ajuste valores e datas no CSV (mes/ano se precisar).",
        "2) Para valores diários, defina `--days` ao gerar. Por padrão uso 30.",
        "3) Rode este script para recriar o index: `python generate_index.py --days 30`.",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Gera index.md a partir de planilha_gastos.csv")
    parser.add_argument("--csv", type=Path, default=CSV_PATH, help="Caminho para o CSV")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Arquivo de saída (Markdown)")
    parser.add_argument("--days", type=int, default=30, help="Dias para multiplicar valores diários")
    args = parser.parse_args()

    rows = load_rows(args.csv)
    totals = summarize(rows, args.days)
    md = build_markdown(rows, totals, args.days)
    args.output.write_text(md, encoding="utf-8")
    print(f"Gerado: {args.output}")


if __name__ == "__main__":
    main()
