def add_label_to_device_id (glueContext, dfc) -> DynamicFrameCollection:
    from neptune_python_utils.glue_gremlin_csv_transforms import GlueGremlinCsvTransforms
    df = dfc.select(list(dfc.keys())[0])
    df = DropNullFields.apply(frame = df)
    df_withlabel = GlueGremlinCsvTransforms.addLabel(df, 'DeviceID')
    dataframe = df_withlabel.toDF().dropDuplicates().repartition(1)
    df_deduplicated = DynamicFrame.fromDF(dataframe, glueContext, 'df_deduplicated')
    return(DynamicFrameCollection({"device_id_vertex_transform": df_deduplicated}, glueContext))
    