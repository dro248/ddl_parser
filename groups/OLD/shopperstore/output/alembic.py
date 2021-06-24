##############################
#	fsv_sp_zip9_drivetime
##############################
op.create_table(
    'fsv_sp_zip9_drivetime',
    sa.Column('cv_living_unit_id', sa.BIGINT()),
    sa.Column('cv_city_name', sa.VARCHAR(28)),
    sa.Column('cv_zipcode_5', sa.VARCHAR(5)),
    sa.Column('cv_zipcode_9', sa.VARCHAR(9)),
    sa.Column('usps_zip9', sa.VARCHAR(9)),
    sa.Column('cv_latitude', sa.DECIMAL(9, 6)),
    sa.Column('cv_longitude', sa.DECIMAL(9, 6)),
    sa.Column('hh_size', sa.VARCHAR(11)),
    sa.Column('hoh_age', sa.VARCHAR(28)),
    sa.Column('hoh_lifestage', sa.VARCHAR(23)),
    sa.Column('hoh_ethnicity', sa.VARCHAR(27)),
    sa.Column('hoh_hispanic', sa.VARCHAR(1)),
    sa.Column('hh_income', sa.VARCHAR(18)),
    sa.Column('hh_presence_of_child', sa.VARCHAR(3)),
    sa.Column('hh_presence_of_gender', sa.VARCHAR(10)),
    sa.Column('hh_urban_suburban_rural', sa.VARCHAR(10)),
    sa.Column('dx_id', sa.VARCHAR(100)),
    sa.Column('drive_minutes', sa.DECIMAL(8, 2)),
    sa.Column('drive_miles', sa.DECIMAL(8, 2))
)

##############################
#	fsv_store_dim
##############################
op.create_table(
    'fsv_store_dim',
    sa.Column('fsv_key', sa.TINYINT()),
    sa.Column('fsv_chain', sa.VARCHAR(50)),
    sa.Column('curr_prior_flag', sa.VARCHAR(10)),
    sa.Column('key_kpi_nm', sa.VARCHAR(50)),
    sa.Column('geo_fsv_kpi_nm', sa.VARCHAR(100)),
    sa.Column('is_fsv_cap_kpi_nm', sa.VARCHAR(100)),
    sa.Column('is_fsv_decile_kpi_nm', sa.VARCHAR(100)),
    sa.Column('is_avbl_adj_fsv_kpi_nm', sa.VARCHAR(100)),
    sa.Column('is_avbl_adj_fsv_decile_kpi_nm', sa.VARCHAR(100))
)

##############################
#	fsv_store_dim_temp1
##############################
op.create_table(
    'fsv_store_dim_temp1',
    sa.Column('fsv_key', sa.TINYINT()),
    sa.Column('fsv_chain', sa.VARCHAR(50)),
    sa.Column('curr_prior_flag', sa.VARCHAR(10))
)

##############################
#	fsv_store_dim_temp2
##############################
op.create_table(
    'fsv_store_dim_temp2',
    sa.Column('fsv_key', sa.TINYINT()),
    sa.Column('fsv_chain', sa.VARCHAR(50)),
    sa.Column('curr_prior_flag', sa.VARCHAR(10)),
    sa.Column('key_kpi_nm', sa.VARCHAR(50))
)

##############################
#	fsv_store_fact_temp1
##############################
op.create_table(
    'fsv_store_fact_temp1',
    sa.Column('cv_living_unit_id', sa.BIGINT()),
    sa.Column('cv_city_name', sa.VARCHAR(28)),
    sa.Column('cv_zipcode_5', sa.VARCHAR(5)),
    sa.Column('cv_zipcode_9', sa.VARCHAR(9)),
    sa.Column('cv_latitude', sa.DECIMAL(9, 6)),
    sa.Column('cv_longitude', sa.DECIMAL(9, 6)),
    sa.Column('fsv_key', sa.TINYINT()),
    sa.Column('fsv_chain', sa.VARCHAR(50)),
    sa.Column('geo_fsv_proximity', sa.VARCHAR(50)),
    sa.Column('is_fsv_cap', sa.DOUBLE()),
    sa.Column('is_fsv_decile', sa.TINYINT()),
    sa.Column('is_avbl_adj_fsv_cap', sa.DOUBLE()),
    sa.Column('is_avbl_adj_fsv_decile', sa.TINYINT())
)

##############################
#	fsv_sp_hh_all_store
##############################
op.create_table(
    'fsv_sp_hh_all_store',
    sa.Column('cv_living_unit_id', sa.BIGINT()),
    sa.Column('cv_city_name', sa.VARCHAR(28)),
    sa.Column('cv_zipcode_5', sa.VARCHAR(5)),
    sa.Column('cv_zipcode_9', sa.VARCHAR(9)),
    sa.Column('usps_zip9', sa.VARCHAR(9)),
    sa.Column('cv_latitude', sa.DECIMAL(9, 6)),
    sa.Column('cv_longitude', sa.DECIMAL(9, 6)),
    sa.Column('hh_size', sa.VARCHAR(11)),
    sa.Column('hoh_age', sa.VARCHAR(28)),
    sa.Column('hoh_lifestage', sa.VARCHAR(23)),
    sa.Column('hoh_ethnicity', sa.VARCHAR(27)),
    sa.Column('hoh_hispanic', sa.VARCHAR(1)),
    sa.Column('hh_income', sa.VARCHAR(18)),
    sa.Column('hh_presence_of_child', sa.VARCHAR(3)),
    sa.Column('hh_presence_of_gender', sa.VARCHAR(10)),
    sa.Column('hh_urban_suburban_rural', sa.VARCHAR(10)),
    sa.Column('dx_id', sa.VARCHAR(100)),
    sa.Column('fsv_chain', sa.VARCHAR(50)),
    sa.Column('store_name', sa.VARCHAR(150)),
    sa.Column('city', sa.VARCHAR(20)),
    sa.Column('county', sa.VARCHAR(20)),
    sa.Column('state', sa.VARCHAR(20)),
    sa.Column('store_zip', sa.VARCHAR(9)),
    sa.Column('latitude', sa.DECIMAL(18, 6)),
    sa.Column('longitude', sa.DECIMAL(18, 6)),
    sa.Column('drive_minutes', sa.DECIMAL(8, 2)),
    sa.Column('drive_miles', sa.DECIMAL(8, 2)),
    sa.Column('is_iri_adj_cap', sa.DOUBLE()),
    sa.Column('is_iri_adj_decile', sa.TINYINT()),
    sa.Column('is_avbl_cap', sa.DOUBLE()),
    sa.Column('is_avbl_decile', sa.TINYINT()),
    sa.Column('last_updt_dt', sf.TIMESTAMP_TZ())
)

##############################
#	fsv_sp_msa_drivetime
##############################
op.create_table(
    'fsv_sp_msa_drivetime',
    sa.Column('cv_living_unit_id', sa.BIGINT()),
    sa.Column('cv_city_name', sa.VARCHAR(28)),
    sa.Column('cv_zipcode_5', sa.VARCHAR(5)),
    sa.Column('cv_zipcode_9', sa.VARCHAR(9)),
    sa.Column('usps_zip9', sa.VARCHAR(9)),
    sa.Column('cv_latitude', sa.DECIMAL(9, 6)),
    sa.Column('cv_longitude', sa.DECIMAL(9, 6)),
    sa.Column('hh_size', sa.VARCHAR(11)),
    sa.Column('hoh_age', sa.VARCHAR(28)),
    sa.Column('hoh_lifestage', sa.VARCHAR(23)),
    sa.Column('hoh_ethnicity', sa.VARCHAR(27)),
    sa.Column('hoh_hispanic', sa.VARCHAR(1)),
    sa.Column('hh_income', sa.VARCHAR(18)),
    sa.Column('hh_presence_of_child', sa.VARCHAR(3)),
    sa.Column('hh_presence_of_gender', sa.VARCHAR(10)),
    sa.Column('hh_urban_suburban_rural', sa.VARCHAR(10)),
    sa.Column('dx_id', sa.VARCHAR(100)),
    sa.Column('fsv_chain', sa.VARCHAR(50)),
    sa.Column('store_name', sa.VARCHAR(150)),
    sa.Column('city', sa.VARCHAR(20)),
    sa.Column('county', sa.VARCHAR(20)),
    sa.Column('state', sa.VARCHAR(20)),
    sa.Column('store_zip', sa.VARCHAR(9)),
    sa.Column('latitude', sa.DECIMAL(18, 6)),
    sa.Column('longitude', sa.DECIMAL(18, 6)),
    sa.Column('drive_minutes', sa.DECIMAL(8, 2)),
    sa.Column('drive_miles', sa.DECIMAL(8, 2))
)

##############################
#	mvh_hh_all_store
##############################
op.create_table(
    'mvh_hh_all_store',
    sa.Column('cv_living_unit_id', sa.BIGINT()),
    sa.Column('cv_city_name', sa.VARCHAR(28)),
    sa.Column('cv_zipcode_5', sa.VARCHAR(5)),
    sa.Column('cv_zipcode_9', sa.VARCHAR(9)),
    sa.Column('usps_zip9', sa.VARCHAR(9)),
    sa.Column('cv_latitude', sa.DECIMAL(9, 6)),
    sa.Column('cv_longitude', sa.DECIMAL(9, 6)),
    sa.Column('hh_size', sa.VARCHAR(11)),
    sa.Column('hoh_age', sa.VARCHAR(28)),
    sa.Column('hoh_lifestage', sa.VARCHAR(23)),
    sa.Column('hoh_ethnicity', sa.VARCHAR(27)),
    sa.Column('hoh_hispanic', sa.VARCHAR(1)),
    sa.Column('hh_income', sa.VARCHAR(18)),
    sa.Column('hh_presence_of_child', sa.VARCHAR(3)),
    sa.Column('hh_presence_of_gender', sa.VARCHAR(10)),
    sa.Column('hh_urban_suburban_rural', sa.VARCHAR(10)),
    sa.Column('dx_id', sa.VARCHAR(100)),
    sa.Column('retailer', sa.VARCHAR(50)),
    sa.Column('store_name', sa.VARCHAR(150)),
    sa.Column('city', sa.VARCHAR(20)),
    sa.Column('county', sa.VARCHAR(20)),
    sa.Column('state', sa.VARCHAR(20)),
    sa.Column('store_zip', sa.VARCHAR(9)),
    sa.Column('latitude', sa.DECIMAL(18, 6)),
    sa.Column('longitude', sa.DECIMAL(18, 6)),
    sa.Column('drive_minutes', sa.DECIMAL(8, 2)),
    sa.Column('drive_miles', sa.DECIMAL(8, 2)),
    sa.Column('is_cap', sa.DOUBLE()),
    sa.Column('is_decile', sa.TINYINT()),
    sa.Column('is_avbl_cap', sa.DOUBLE()),
    sa.Column('is_avbl_decile', sa.TINYINT()),
    sa.Column('last_updt_dt', sf.TIMESTAMP_TZ())
)

##############################
#	mvh_hh_all_store_dw
##############################
op.create_table(
    'mvh_hh_all_store_dw',
    sa.Column('cv_living_unit_id', sa.BIGINT()),
    sa.Column('cv_city_name', sa.VARCHAR(28)),
    sa.Column('cv_zipcode_5', sa.VARCHAR(5)),
    sa.Column('cv_zipcode_9', sa.VARCHAR(9)),
    sa.Column('usps_zip9', sa.VARCHAR(9)),
    sa.Column('cv_latitude', sa.DECIMAL(9, 6)),
    sa.Column('cv_longitude', sa.DECIMAL(9, 6)),
    sa.Column('hh_size', sa.VARCHAR(11)),
    sa.Column('hoh_age', sa.VARCHAR(28)),
    sa.Column('hoh_lifestage', sa.VARCHAR(23)),
    sa.Column('hoh_ethnicity', sa.VARCHAR(27)),
    sa.Column('hoh_hispanic', sa.VARCHAR(1)),
    sa.Column('hh_income', sa.VARCHAR(18)),
    sa.Column('hh_presence_of_child', sa.VARCHAR(3)),
    sa.Column('hh_presence_of_gender', sa.VARCHAR(10)),
    sa.Column('hh_urban_suburban_rural', sa.VARCHAR(10)),
    sa.Column('dx_id', sa.VARCHAR(100)),
    sa.Column('retailer', sa.VARCHAR(50)),
    sa.Column('store_name', sa.VARCHAR(150)),
    sa.Column('city', sa.VARCHAR(20)),
    sa.Column('county', sa.VARCHAR(20)),
    sa.Column('state', sa.VARCHAR(20)),
    sa.Column('store_zip', sa.VARCHAR(9)),
    sa.Column('latitude', sa.DECIMAL(18, 6)),
    sa.Column('longitude', sa.DECIMAL(18, 6)),
    sa.Column('drive_minutes', sa.DECIMAL(8, 2)),
    sa.Column('drive_miles', sa.DECIMAL(8, 2)),
    sa.Column('is_cap', sa.DOUBLE()),
    sa.Column('is_decile', sa.TINYINT()),
    sa.Column('is_avbl_cap', sa.DOUBLE()),
    sa.Column('is_avbl_decile', sa.TINYINT()),
    sa.Column('last_updt_dt', sf.TIMESTAMP_TZ())
)

##############################
#	fsv_store_fact
##############################
op.create_table(
    'fsv_store_fact',
    sa.Column('cv_living_unit_id', sa.BIGINT()),
    sa.Column('cv_city_name', sa.VARCHAR(28)),
    sa.Column('cv_zipcode_5', sa.VARCHAR(5)),
    sa.Column('cv_zipcode_9', sa.VARCHAR(9)),
    sa.Column('cv_latitude', sa.DECIMAL(9, 6)),
    sa.Column('cv_longitude', sa.DECIMAL(9, 6)),
    sa.Column('fsv_key', sa.TINYINT()),
    sa.Column('fsv_chain', sa.VARCHAR(50)),
    sa.Column('geo_fsv_proximity', sa.VARCHAR(50)),
    sa.Column('is_fsv_cap', sa.DOUBLE()),
    sa.Column('is_fsv_decile', sa.TINYINT()),
    sa.Column('is_avbl_adj_fsv_cap', sa.DOUBLE()),
    sa.Column('is_avbl_adj_fsv_decile', sa.TINYINT())
)

