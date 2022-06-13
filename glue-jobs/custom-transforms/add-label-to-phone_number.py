def add_label_to_phone_number (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    dataframe = df.toDF().dropDuplicates()
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, 'df_deduplicated')
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df_deduplicated, 'PhoneNumber')
    return(DynamicFrameCollection({"phone_number_vertex_transform": df_withlabel}, glueContext))
    