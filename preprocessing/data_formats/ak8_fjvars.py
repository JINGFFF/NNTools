'''
Description on how to produce metadata file.
'''

input_filter = None
treename = 'deepntuplizer/tree'
reweight_events = -1
reweight_bins = [list(range(200, 2051, 50)), [-10000, 10000]]
metadata_events = 1000000
selection = '''jet_tightId \
&& ( !label_H_cc )'''
# && ( (sample_isQCD && fj_isQCD) || (!sample_isQCD && !fj_isQCD)) \
var_groups = {
    # 'group_name': ( ('regex1', 'regex2', ...), list_length )
    'fjvars': (('fj_sdmass',), None),
    }
var_blacklist = [
    'fj_gen_pt',
    'fj_gen_eta',
    ]
var_no_transform_branches = [
    'fj_labelJMAR', 'fjJMAR_gen_pt', 'fjJMAR_gen_eta', 'fjJMAR_gen_pdgid',
    'fj_label',
    'fj_isQCD', 'fj_isTop', 'fj_isW', 'fj_isZ', 'fj_isH',
    'npv',
    'n_pfcands', 'n_tracks', 'n_sv',
    'fj_pt', 'fj_eta', 'fj_phi', 'fj_mass',
    'fj_n_sdsubjets',
    'fjPuppi_tau21', 'fjPuppi_tau32', 'fjPuppi_corrsdmass',
    'fj_doubleb', 'pfCombinedInclusiveSecondaryVertexV2BJetTags',

    "fj_tau21",
    "fj_tau32",
    "fj_sdmass",
    "fj_sdsj1_pt",
    "fj_sdsj1_eta",
    "fj_sdsj1_phi",
    "fj_sdsj1_mass",
    "fj_sdsj1_csv",
    "fj_sdsj1_ptD",
    "fj_sdsj1_axis1",
    "fj_sdsj1_axis2",
    "fj_sdsj1_mult",
    "fj_sdsj2_pt",
    "fj_sdsj2_eta",
    "fj_sdsj2_phi",
    "fj_sdsj2_mass",
    "fj_sdsj2_csv",
    "fj_sdsj2_ptD",
    "fj_sdsj2_axis1",
    "fj_sdsj2_axis2",
    "fj_sdsj2_mult",
    "fj_ptDR",
    "fj_relptdiff",
    "fj_sdn2",

    'fj_z_ratio',
    'fj_trackSipdSig_3',
    'fj_trackSipdSig_2',
    'fj_trackSipdSig_1',
    'fj_trackSipdSig_0',
    'fj_trackSipdSig_1_0',
    'fj_trackSipdSig_0_0',
    'fj_trackSipdSig_1_1',
    'fj_trackSipdSig_0_1',
    'fj_trackSip2dSigAboveCharm_0',
    'fj_trackSip2dSigAboveBottom_0',
    'fj_trackSip2dSigAboveBottom_1',
    'fj_tau1_trackEtaRel_0',
    'fj_tau1_trackEtaRel_1',
    'fj_tau1_trackEtaRel_2',
    'fj_tau0_trackEtaRel_0',
    'fj_tau0_trackEtaRel_1',
    'fj_tau0_trackEtaRel_2',
    'fj_tau_vertexMass_0',
    'fj_tau_vertexEnergyRatio_0',
    'fj_tau_vertexDeltaR_0',
    'fj_tau_flightDistance2dSig_0',
    'fj_tau_vertexMass_1',
    'fj_tau_vertexEnergyRatio_1',
    'fj_tau_flightDistance2dSig_1',
    'fj_jetNTracks',
    'fj_nSV',

    ]
# label_list = ['fj_isQCD', 'fj_isTop', 'fj_isW', 'fj_isZ', 'fj_isH']
label_list = ['label_Top_bcq', 'label_Top_bqq', 'label_Top_bc', 'label_Top_bq',
              'label_W_cq', 'label_W_qq',
              'label_Z_bb', 'label_Z_cc', 'label_Z_qq',
              'label_H_bb', 'label_H_qqqq',
              'label_QCD_bb', 'label_QCD_cc', 'label_QCD_b', 'label_QCD_c', 'label_QCD_others',
              ]
reweight_var = ['fj_pt', 'fj_sdmass']
reweight_classes = ['fj_isTop', 'fj_isW', 'fj_isZ', 'fj_isH', 'fj_isQCD']
reweight_method = 'flat'
var_img = None
var_pos = None
n_pixels = None
img_ranges = None
