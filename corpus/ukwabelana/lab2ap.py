#!/usr/bin/env python3

import sys

tag_map = {
    'aug': 'aug',
    'd1': 'cl1-2><sg',
    'd2': 'cl1-2><pl',
    'd3': 'cl3-4><sg',
    'd4': 'cl3-4><pl',
    'd5': 'cl5-6><sg',
    'd6': 'cl5-6><pl',
    'd7': 'cl7-8><sg',
    'd8': 'cl7-8><pl',
    'd9': 'cl9-10><sg',
    'd10': 'cl9-10><pl',
    'd11': 'cl11><sg',
    'd14': 'cl14><sg',
    'd15': 'cl15><sg',
    'dim': 'dim',
    'fem': 'f',
    'fut': 'fut',
    'g1': 's_cl1-2><s_sg><neg',
    'g1p': 's_p1><s_pl><neg',
    'g1s': 's_p1><s_sg><neg',
    'g2': 's_cl1-2><s_pl><neg',
    'g2p': 's_p2><s_pl><neg',
    'g2s': 's_p2><s_sg><neg',
    'g3': 's_cl3-4><s_sg><neg',
    'g4': 's_cl3-4><s_pl><neg',
    'g5': 's_cl5-6><s_sg><neg',
    'g6': 's_cl5-6><s_pl><neg',
    'g7': 's_cl7-8><s_sg><neg',
    'g8': 's_cl7-8><s_pl><neg',
    'g9': 's_cl9-10><s_sg><neg',
    'g10': 's_cl9-10><s_pl><neg',
    'g11': 's_cl11><s_sg><neg',
    'g14': 's_cl14><s_sg><neg',
    'g15': 's_cl15><s_sg><neg',
    'hort': 'hort',
    'hum': 'hum',
    'i1': 's_cl1-2><s_sg><ind',
    'i1p': 's_p1><s_pl><ind',
    'i1s': 's_p1><s_sg><ind',
    'i2': 's_cl1-2><s_pl><ind',
    'i2p': 's_p2><s_pl><ind',
    'i2s': 's_p2><s_sg><ind',
    'i3': 's_cl3-4><s_sg><ind',
    'i4': 's_cl3-4><s_pl><ind',
    'i5': 's_cl5-6><s_sg><ind',
    'i6': 's_cl5-6><s_pl><ind',
    'i7': 's_cl7-8><s_sg><ind',
    'i8': 's_cl7-8><s_pl><ind',
    'i9': 's_cl9-10><s_sg><ind',
    'i10': 's_cl9-10><s_pl><ind',
    'i11': 's_cl11><s_sg><ind',
    'i14': 's_cl14><s_sg><ind',
    'i15': 's_cl15><s_sg><ind',
    'imp': 'imp',
    'in': 'nn',
    'int': 'int',
    'locpf': 'loc',
    'locsf': 'loc',
    'n1': 'cl1-2><sg',
    'n2': 'cl1-2><pl',
    'n3': 'cl3-4><sg',
    'n4': 'cl3-4><pl',
    'n5': 'cl5-6><sg',
    'n6': 'cl5-6><pl',
    'n7': 'cl7-8><sg',
    'n8': 'cl7-8><pl',
    'n9': 'cl9-10><sg',
    'n10': 'cl9-10><pl',
    'n11': 'cl11><sg',
    'n14': 'cl14><sg',
    'n15': 'cl15><sg',
    'neg': 'neg',
    'o1': 'o_cl1-2><o_sg',
    'o1p': 'o_p1><o_pl',
    'o1s': 'o_p1><o_sg',
    'o2': 'o_cl1-2><o_pl',
    'o2p': 'o_p2><o_pl',
    'o2s': 'o_p2><o_sg',
    'o3': 'o_cl3-4><o_sg',
    'o4': 'o_cl3-4><o_pl',
    'o5': 'o_cl5-6><o_sg',
    'o6': 'o_cl5-6><o_pl',
    'o7': 'o_cl7-8><o_sg',
    'o8': 'o_cl7-8><o_pl',
    'o9': 'o_cl9-10><o_sg',
    'o10': 'o_cl9-10><o_pl',
    'o11': 'o_cl11><o_sg',
    'o14': 'o_cl14><o_sg',
    'o15': 'o_cl15><o_sg',
    'opt': 'opt',
    'p1': 's_cl1-2><s_sg><part',
    'p1p': 's_p1><s_pl><part',
    'p1s': 's_p1><s_sg><part',
    'p2': 's_cl1-2><s_pl><part',
    'p2p': 's_p2><s_pl><part',
    'p2s': 's_p2><s_sg><part',
    'p3': 's_cl3-4><s_sg><part',
    'p4': 's_cl3-4><s_pl><part',
    'p5': 's_cl5-6><s_sg><part',
    'p6': 's_cl5-6><s_pl><part',
    'p7': 's_cl7-8><s_sg><part',
    'p8': 's_cl7-8><s_pl><part',
    'p9': 's_cl9-10><s_sg><part',
    'p10': 's_cl9-10><s_pl><part',
    'p11': 's_cl11><s_sg><part',
    'p14': 's_cl14><s_sg><part',
    'p15': 's_cl15><s_sg><part',
    'past': 'past',
    'pl': 'pl',
    'pn1': 'cl1-2><sg',
    'pn1p': 'p1><pl',
    'pn1s': 'p1><sg',
    'pn2': 'cl1-2><pl',
    'pn2p': 'p2><pl',
    'pn2s': 'p2><sg',
    'pn3': 'cl3-4><sg',
    'pn4': 'cl3-4><pl',
    'pn5': 'cl5-6><sg',
    'pn6': 'cl5-6><pl',
    'pn7': 'cl7-8><sg',
    'pn8': 'cl7-8><pl',
    'pn9': 'cl9-10><sg',
    'pn10': 'cl9-10><pl',
    'pn11': 'cl11><sg',
    'pn14': 'cl14><sg',
    'pn15': 'cl15><sg',
    'pnes': 'pstv', # ???
    'pot': 'pot',
    'pstv1': 'pstv_cl1-2><pstv_sg',
    'pstv2': 'pstv_cl1-2><pstv_pl',
    'pstv3': 'pstv_cl3-4><pstv_sg',
    'pstv4': 'pstv_cl3-4><pstv_pl',
    'pstv5': 'pstv_cl5-6><pstv_sg',
    'pstv6': 'pstv_cl5-6><pstv_pl',
    'pstv7': 'pstv_cl7-8><pstv_sg',
    'pstv8': 'pstv_cl7-8><pstv_pl',
    'pstv9': 'pstv_cl9-10><pstv_sg',
    'pstv10': 'pstv_cl9-10><pstv_pl',
    'pstv11': 'pstv_cl11><pstv_sg',
    'pstv14': 'pstv_cl14><pstv_sg',
    'pstv15': 'pstv_cl15><pstv_sg',
    'r': 'rel', # ???
    'refl': 'refl',
    'rsf': 'rel', # ???
    's1': 's_cl1-2><s_sg><sub',
    's1p': 's_p1><s_pl><sub',
    's1s': 's_p1><s_sg><sub',
    's2': 's_cl1-2><s_pl><sub',
    's2p': 's_p2><s_pl><sub',
    's2s': 's_p2><s_sg><sub',
    's3': 's_cl3-4><s_sg><sub',
    's4': 's_cl3-4><s_pl><sub',
    's5': 's_cl5-6><s_sg><sub',
    's6': 's_cl5-6><s_pl><sub',
    's7': 's_cl7-8><s_sg><sub',
    's8': 's_cl7-8><s_pl><sub',
    's9': 's_cl9-10><s_sg><sub',
    's10': 's_cl9-10><s_pl><sub',
    's11': 's_cl11><s_sg><sub',
    's14': 's_cl14><s_sg><sub',
    's15': 's_cl15><s_sg><sub',
    'st': 'stab', # ???
    'vg': 'neg',
    'voc': 'voc',
    'vpg': 'perf><neg',
    'vpl': 'perf',
    'vps': 'perf',
    'vs': 'sub',
    'xa': 'appl', # ???
    'xc': 'caus',
    'xi': 'ints',
    'xn': 'nt', # ???
    'xp': 'pass',
    'xr': 'recip',
    'z1': 'px_cl1-2><px_sg',
    'z1p': 'px_p1><px_pl',
    'z1s': 'px_p1><px_sg',
    'z2': 'px_cl1-2><px_pl',
    'z2p': 'px_p2><px_pl',
    'z2s': 'px_p2><px_sg',
    'z3': 'px_cl3-4><px_sg',
    'z4': 'px_cl3-4><px_pl',
    'z5': 'px_cl5-6><px_sg',
    'z6': 'px_cl5-6><px_pl',
    'z7': 'px_cl7-8><px_sg',
    'z8': 'px_cl7-8><px_pl',
    'z9': 'px_cl9-10><px_sg',
    'z10': 'px_cl9-10><px_pl',
    'z11': 'px_cl11><px_sg',
    'z14': 'px_cl14><px_sg',
    'z15': 'px_cl15><px_sg',
}

tag_skip = [
    'advpf', 'asp', 'iv', 'red', 'va', 'z',
    'pos2', 'pos3', # no idea what these are
    'der', # unless this should be <nmlz>?
    'ke', 'w',
]

tag_root = {
    'ar': 'adj',
    'adv': 'adv',
    'cj': 'conjcoo',
    'd': 'det><dem',
    'intj': 'ij',
    'mr': 'vaux',
    'nr': 'n',
    'p': 'pr',
    'prn': 'prn',
    'qr': 'det><quant',
    'vr': 'v',
}

tag_split = [
    ('iv_', ''),
    ('_iv', ''),
    ('asp_vr', 'vr>x<asp'),
    ('i6_vr', 'vr>x<i6'),
    ('p1_vr', 'vr>x<p1'),
    ('<prs', '<pstv'),
    ('<pr', '<prn>x<pn'),
    ('z6_n1', 'z6>x<n1'),
    ('z6_n3', 'z6>x<n3'),
]

def convert_analysis(label):
    lab = label
    for old, new in tag_split:
        lab = lab.replace(old, new)
    ls = [x.split('<') for x in lab.split('>') if x]
    ana = ''
    for lem, old_tag in ls:
        if old_tag in tag_root:
            s = lem + '<' + tag_root[old_tag] + '>'
            if ana and ana[0] != '<':
                ana += '+' + s
            else:
                ana = s + ana
        elif old_tag in tag_skip:
            continue
        else:
            ana += '<' + tag_map.get(old_tag, old_tag+'??') + '>'
    if ana and ana[0] != '<':
        return [ana]
    return []

for line in sys.stdin:
    surf, ana = line.strip().split('\t')
    ls = [surf]
    for a in ana.split(','):
        ls += convert_analysis(a.strip())
    print('\t'.join(ls))
