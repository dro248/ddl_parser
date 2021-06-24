##############################
#	dx_fl_trade_chnl_lkp
##############################
op.create_table(
    'dx_fl_trade_chnl_lkp',
    sa.Column('trade_chanl_descp', sa.VARCHAR(100)),
    sa.Column('dx_include_flg', sa.VARCHAR(3)),
    sa.Column('dx_trade_chanl_descp', sa.VARCHAR(100)),
    sa.Column('dx_store_format', sa.VARCHAR(100)),
    sa.Column('last_updt_dt', sf.TIMESTAMP_TZ())
)

##############################
#	dx_msa_xref
##############################
op.create_table(
    'dx_msa_xref',
    sa.Column('file_index', sa.BIGINT()),
    sa.Column('dx_id', sa.VARCHAR(50)),
    sa.Column('fl_msa_id', sa.VARCHAR(50)),
    sa.Column('pbc_msa_id', sa.VARCHAR(50)),
    sa.Column('last_updt_dt', sf.TIMESTAMP_TZ())
)

##############################
#	dx_pbc_trade_chnl_lkp
##############################
op.create_table(
    'dx_pbc_trade_chnl_lkp',
    sa.Column('bus_type_desc', sa.VARCHAR(100)),
    sa.Column('dx_include_flg', sa.VARCHAR(1)),
    sa.Column('dx_trade_chanl_descp', sa.VARCHAR(100)),
    sa.Column('last_updt_dt', sf.TIMESTAMP_TZ())
)

