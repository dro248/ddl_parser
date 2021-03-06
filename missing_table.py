##############################
#	btg_pbc_new_mkt_loc
##############################
op.create_table(
    'btg_pbc_new_mkt_loc',
    sa.Column('cust_id', sa.INT()),
    sa.Column('nme', sa.VARCHAR(35)),
    sa.Column('loc_prod_nme', sa.VARCHAR(35)),
    sa.Column('loc_prod_mu_nme', sa.VARCHAR(35)),
    sa.Column('dely_adr_strt1', sa.VARCHAR(35)),
    sa.Column('dely_adr_zip', sa.VARCHAR(9)),
    sa.Column('dely_adr_city', sa.VARCHAR(28)),
    sa.Column('dely_adr_cnty', sa.VARCHAR(25)),
    sa.Column('dely_adr_state', sa.VARCHAR(2)),
    sa.Column('hrchy_id', sa.INT()),
    sa.Column('hrchy_nme', sa.VARCHAR(50)),
    sa.Column('hrchy_owner_nme', sa.VARCHAR(50)),
    sa.Column('av_lbl_id', sa.INT()),
    sa.Column('av_lbl_nme', sa.VARCHAR(50)),
    sa.Column('ref_org_id', sa.INT()),
    sa.Column('ref_org_type', sa.VARCHAR(3)),
    sa.Column('hq_id', sa.INT()),
    sa.Column('hq_nme', sa.VARCHAR(50)),
    sa.Column('hq_type', sa.VARCHAR(3)),
    sa.Column('hq_ref_id', sa.INT()),
    sa.Column('bu_id', sa.INT()),
    sa.Column('bu_nme', sa.VARCHAR(50)),
    sa.Column('bu_type', sa.VARCHAR(3)),
    sa.Column('bu_ref_id', sa.INT()),
    sa.Column('reg_id', sa.INT()),
    sa.Column('reg_nme', sa.VARCHAR(50)),
    sa.Column('reg_type', sa.VARCHAR(3)),
    sa.Column('reg_ref_id', sa.INT()),
    sa.Column('mu_id', sa.INT()),
    sa.Column('mu_nme', sa.VARCHAR(50)),
    sa.Column('mu_type', sa.VARCHAR(3)),
    sa.Column('mu_ref_id', sa.INT()),
    sa.Column('area_id', sa.INT()),
    sa.Column('area_nme', sa.VARCHAR(50)),
    sa.Column('area_type', sa.VARCHAR(3)),
    sa.Column('area_ref_id', sa.INT()),
    sa.Column('loc_id', sa.INT()),
    sa.Column('loc_nme', sa.VARCHAR(50))
)