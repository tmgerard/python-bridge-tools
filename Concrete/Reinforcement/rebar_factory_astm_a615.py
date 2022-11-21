import json
import pkg_resources

from Concrete.Reinforcement.deformed_rebar import DeformedRebar


class RebarFactoryASTM_A615:
    def __init__(self):
        bar_file = pkg_resources.resource_string(__name__, 'rebar_astm_a615.json')
        self.bars = json.loads(bar_file)

    def get_rebar_designation(self, bar_designation: int):
        rebar = None
        for bar in self.bars:
            if bar['Bar Designation'] == bar_designation:
                rebar = bar

        if not rebar:
            raise ValueError(f'Bar Designation {bar_designation} does not exist')

        return DeformedRebar(
            rebar['Bar Designation'],
            rebar['Nominal Weight'],
            rebar['Diameter'],
            rebar['Area'],
            rebar['Perimeter']
        )