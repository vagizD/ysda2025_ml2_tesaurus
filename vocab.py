import pandas as pd


def render_md_table(in_path: str, out_path: str):
    df = pd.read_csv(in_path, sep=';')
    df.fillna("", inplace=True)
    df.to_markdown(out_path)


if __name__ == "__main__":
    in_path  = "vocab.csv"
    out_path = "tesaurus.md"
    render_md_table(in_path, out_path)
