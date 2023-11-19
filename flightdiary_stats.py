try:
    import click
except Exception as e:
    print("Missing module 'click' - `pip3 install click`")
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
        #reg_to_row[reg].insert(0, i)
    print(f"skipped entries missing registrations: {skipped}\n")
    same_plane_count = 0
    for k,v in reg_to_row.items():
        if len(v) > 1:
            same_plane_count += 1
            for row in v:
                print_single_row_summary(row)
            print()
    print(f"total number of registrations seen >1 time: {same_plane_count}")
            

def print_single_row_summary(row):
    dt = row[0]
    fn = row[1]
    departure = row[2].split(" ")[-1].split("/")[0].strip("(")
    arrival = row[3].split(" ")[-1].split("/")[0].strip("(")
    plane = row[8]
    reg = row[9]
    print(f"{dt}: {fn} {reg} {departure} - {arrival} {plane}")

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
