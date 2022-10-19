from StructuralShapes.BuiltUpShapes.plate_girder_section import PlateGirderSection
from StructuralShapes.BuiltUpShapes.plate_section import PlateSection


def get_plate_girder_input() -> PlateGirderSection:
    top_width = float(input('Top Flange Width: '))
    top_thick = float(input('Top Flange Thickness: '))
    top_flange = PlateSection(top_width, top_thick)

    web_depth = float(input('Web Depth: '))
    web_thickness = float(input('Web Thickness: '))
    web_plate = PlateSection(web_thickness, web_depth)

    bot_width = float(input('Bottom Flange Width: '))
    bot_thick = float(input('Bottom Flange Thickness: '))
    bot_flange = PlateSection(bot_width, bot_thick)

    return PlateGirderSection(top_flange, web_plate, bot_flange)


def plate_girder_properties():
    print('Enter plate girder dimensions (inches)')
    girder_section = get_plate_girder_input()
    plate_girder_report(girder_section)
    input('\nPress enter to exit')


def plate_girder_report(girder_section: PlateGirderSection):
    print('\n-------[Properties]-------')
    print('Girder Depth: {0} in.'.format(girder_section.depth))
    print('Area: {0} in^2'.format(girder_section.area))
    print('Ix: {0} in^4'.format(girder_section.ix))
    print('Iy: {0} in^4'.format(girder_section.iy))
    print('J: {0} in^4'.format(girder_section.j))
    print('Cw: {0} in^6'.format(girder_section.cw))
    print('Rx: {0} in.'.format(girder_section.rx))
    print('Ry: {0} in.'.format(girder_section.ry))
    print('Base to Neutral Axis: {0} in.'.format(girder_section.base_to_centroid))


