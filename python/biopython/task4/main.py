import requests

genesIds = ["CLOCK_1", "CLOCK_2", "CLOCK_3", "CLOCK_4",
            "ARNTL_1",
            "CRY1_1", "CRY1_2",
            "CRY2_1",
            "PER1_1", "PER1_2", "PER1_3",
            "PER2_1", "PER2_2", "PER2_3",
            "NR1D1_1", "NR1D1_2", "NR1D1_3",
            "NR1D2_1", "NR1D2_2",
            "RORA_2",
            "RORB_1",
            "RORC_1", "RORC_2",
            "DBP_1", "DBP_2",
            "NFIL3_1", "NFIL3_2"]

url = "http://epd.epfl.ch/cgi-bin/get_sequence.php"
database = "epdNew_hg"
fr = "-500"
to = "100"
lc = "0"

for gene in genesIds:
    r = requests.get(url, verify=False, params={"database": database,
                                                "gene_id": gene,
                                                "from": fr,
                                                "to": to,
                                                "lc": lc
                                                })
    fileName = "./out/promoters/" + gene + ".fasta"
    with open(fileName, 'w') as f:
        content = r.text.replace("<br />", "")
        content = content[:content.index("<script>")]
        f.write(content)
