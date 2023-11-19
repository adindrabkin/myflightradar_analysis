import click
import csv


def find_reused_planes(rows):
    reg_to_row = {}
    skipped = 0
    for i in rows:
        reg = i[9]
        if reg == "":
            skipped +=1
            continue
        # default dict
        if reg not in reg_to_row:
            reg_to_row[reg] = []
        reg_to_row[reg].append(i)
    print(f"skipped entries missing registrations: {skipped}")
    for k,v in reg_to_row.items():
        if len(v) > 1:
            print()
            print(k)
            print()
            [print(i) for i in v]

@click.command()
@click.argument('diary', type=click.Path(exists=True))
def main(diary):
    headers = None
    rows = []
    with open(diary) as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 0:
                continue
            if headers is None:
                headers = row
                continue
            rows.append(row)
    find_reused_planes(rows)

if __name__ == '__main__':
    main()
