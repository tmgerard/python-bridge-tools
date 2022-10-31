from StructuralShapes.RolledShapes.rolled_shape_factory import create_rolled_shape


CONFIG_FILE = 'rolled_shape_config.json'


def get_rolled_shape():
    try:
        shape_name = input('Shape Name: ').upper()
        shape = create_rolled_shape(shape_name)
        properties = shape.properties

        for k, v in properties.items():
            print('{0}: {1}'.format(k, v))

        input('\nPress \'Enter\' to close')
    except ValueError as e:
        print(e.args[0])
