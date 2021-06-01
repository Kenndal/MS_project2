import csv
from pprint import pprint
import numpy as np
from copy import deepcopy
import os
import xlsxwriter

template_dict = {"number_of_legacy_sta": int,
                 "rng_run": int,
                 "throughput_sum": float,
                 "throughput_mean": float,
                 "delay_mean": float,
                }

mypath = os.path.dirname(os.path.realpath(__file__))
pprint(mypath)
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyfiles = [f for f in onlyfiles if "csv" in f]

workbook = xlsxwriter.Workbook(mypath + '/results.xlsx')
worksheet_ax = workbook.add_worksheet("ax")
worksheet_ax.write(0, 0, "Sta_num")
worksheet_ax.write(0, 1, "rng_run")
worksheet_ax.write(0, 2, "throughput_sum")
worksheet_ax.write(0, 3, "throughput_mean")
worksheet_ax.write(0, 4, "delay_mean")

worksheet_legacy = workbook.add_worksheet("legacy")
worksheet_legacy.write(0, 0, "Sta_num")
worksheet_legacy.write(0, 1, "rng_run")
worksheet_legacy.write(0, 2, "throughput_sum")
worksheet_legacy.write(0, 3, "throughput_mean")
worksheet_legacy.write(0, 4, "delay_mean")


row = 1
for file_name in onlyfiles:
    ax_dict = deepcopy(template_dict)
    legaca_dict = deepcopy(template_dict)
    ax_thr_list = []
    ax_delay_list = []
    legacy_thr_list = []
    legacy_delay_list = []
    legacy_sta_count = 0
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            # BK
            rng_run = line[2]
            if "10.1." in line[3]:
                try:
                    ax_thr_list.append(float(line[5]) if line[5] != "-0" else 0)
                    ax_delay_list.append(float(line[6]) if line[6] != "-nan" else 0)
                except ValueError:
                    pprint("No date to parse")
                    ax_thr_list.append(0)
                    ax_delay_list.append(0)
            elif "10.2." in line[3]:
                try:
                    legacy_sta_count += 1
                    legacy_thr_list.append(float(line[5]) if float(line[5]) != "-0" else 0)
                    legacy_delay_list.append(float(line[6]) if line[6] != "-nan" else 0)
                except ValueError:
                    pprint("No date to parse")
                    legacy_thr_list.append(0)
                    legacy_delay_list.append(0)
            else:
                print("First line of file")
    ax_dict["number_of_legacy_sta"] = legacy_sta_count
    ax_dict["rng_run"] = rng_run
    ax_dict["throughput_sum"] = sum(ax_thr_list)
    ax_dict["throughput_mean"] = np.mean(ax_thr_list)
    ax_dict["delay_mean"] = np.mean(ax_delay_list)
    pprint(ax_dict)
    worksheet_ax.write(row, 0, ax_dict["number_of_legacy_sta"])
    worksheet_ax.write(row, 1, ax_dict["rng_run"])
    worksheet_ax.write(row, 2, ax_dict["throughput_sum"])
    worksheet_ax.write(row, 3, ax_dict["throughput_mean"])
    worksheet_ax.write(row, 4, ax_dict["delay_mean"])
    if legacy_thr_list and legacy_delay_list:
        legaca_dict["number_of_legacy_sta"] = legacy_sta_count
        legaca_dict["rng_run"] = rng_run
        legaca_dict["throughput_sum"] = sum(legacy_thr_list)
        legaca_dict["throughput_mean"] = np.mean(legacy_thr_list)
        legaca_dict["delay_mean"] = np.mean(legacy_delay_list)
        worksheet_legacy.write(row, 0, legaca_dict["number_of_legacy_sta"])
        worksheet_legacy.write(row, 1, legaca_dict["rng_run"])
        worksheet_legacy.write(row, 2, legaca_dict["throughput_sum"])
        worksheet_legacy.write(row, 3, legaca_dict["throughput_mean"])
        worksheet_legacy.write(row, 4, legaca_dict["delay_mean"])
    row += 1

workbook.close()
"""
    bk_dict["throughput_sum"] = sum(bk_thr_list)
    bk_dict["throughput_mean"] = np.mean(bk_thr_list)
    bk_dict["delay_mean"] = np.mean(bk_delay_list)
    bk_dict["jitter_mean"] = np.mean(bk_jitter_list)
    bk_dict["tx_packets_sum"] = sum(bk_tx_packet_list)
    bk_dict["lost_packets_sum"] = sum(bk_lost_list)
    bk_dict["lost_percentage"] = sum(bk_lost_list) / sum(bk_tx_packet_list)

    pprint(bk_dict)
"""