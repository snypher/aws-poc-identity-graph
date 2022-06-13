def add_label_to_domain_name (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    dataframe = df.toDF().dropDuplicates()
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, 'df_deduplicated')
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df_deduplicated, 'DomainName')
    return(DynamicFrameCollection({"domain_name_vertex_transform": df_withlabel}, glueContext))
    