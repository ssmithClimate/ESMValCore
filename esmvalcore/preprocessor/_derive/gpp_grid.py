"""Derivation of variable `gpp_grid`."""

from ._baseclass import DerivedVariableBase
from ._shared import grid_area_correction


class DerivedVariable(DerivedVariableBase):
    """Derivation of variable `gpp_grid`."""

    # Required variables
    required = [{'short_name': 'gpp', 'fx_files': ['sftlf']}]

    @staticmethod
    def calculate(cubes):
        """Compute gross primary production relative to grid cell area.

        Note
        ----
        By default, `gpp` is defined relative to land area. For spatial
        integration, the original quantity is multiplied by the land area
        fraction (`sftlf`), so that the resuting derived variable is defined
        relative to the grid cell area. This correction is only relevant for
        coastal regions.

        """
        return grid_area_correction(cubes,
                                    'gross_primary_productivity_of_carbon')
