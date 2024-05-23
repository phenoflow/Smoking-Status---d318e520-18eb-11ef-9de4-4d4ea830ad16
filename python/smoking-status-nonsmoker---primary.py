# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"1373.00","system":"readv2"},{"code":"137A.00","system":"readv2"},{"code":"137J.00","system":"readv2"},{"code":"137L.00","system":"readv2"},{"code":"137U.00","system":"readv2"},{"code":"1377.00","system":"readv2"},{"code":"137P.11","system":"readv2"},{"code":"137P.00","system":"readv2"},{"code":"1372.00","system":"readv2"},{"code":"1371.11","system":"readv2"},{"code":"1376.00","system":"readv2"},{"code":"1372.11","system":"readv2"},{"code":"137..11","system":"readv2"},{"code":"137O.00","system":"readv2"},{"code":"137R.00","system":"readv2"},{"code":"137H.00","system":"readv2"},{"code":"1375.00","system":"readv2"},{"code":"137N.00","system":"readv2"},{"code":"1378.00","system":"readv2"},{"code":"137S.00","system":"readv2"},{"code":"137B.00","system":"readv2"},{"code":"T512","system":"readv2"},{"code":"T5090OR","system":"readv2"},{"code":"T510 SH","system":"readv2"},{"code":"T5113","system":"readv2"},{"code":"T5093","system":"readv2"},{"code":"T5091ES","system":"readv2"},{"code":"T5116","system":"readv2"},{"code":"T513","system":"readv2"},{"code":"T510 HS","system":"readv2"},{"code":"T5090XC","system":"readv2"},{"code":"T5117","system":"readv2"},{"code":"T5114","system":"readv2"},{"code":"T5091HS","system":"readv2"},{"code":"T5115M","system":"readv2"},{"code":"T5112","system":"readv2"},{"code":"T5115","system":"readv2"},{"code":"T509","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status-nonsmoker---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status-nonsmoker---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status-nonsmoker---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
