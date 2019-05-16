import pytest
import brightwind as bw

def test_export_tab_file():
    df = bw.load_campbell_scientific(bw.datasets.demo_campbell_scientific_site_data)
    graph, tab = bw.freq_table(df.Spd40mN, df.Dir38mS, return_data=True)
    bw.export_tab_file(tab, name='campbell_tab_file', lat=10, long=10)