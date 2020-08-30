# Program to define, support, and verify the form of any spherical particle in the scale of Classical Mechanics

from AtlasEyes.AtlasAPI import AtlasGeometry, constants
import astropy.constants as const
# TODO: Add function annotations
# TODO: Implement Pytest


class MacroParticleManifest:

    def __init__(self):
        self.earth_mass = constants.earth_mass

    def create_default_macroparticle(self, uniform_density_flag=True):
        """
        This function creates THE default ATLAS MacroParticle. This will be a close approximation of the Earth.
        Like all other ATLAS MacroParticles, even the default MAcroParticle will go "under review".

        :return:
        Returns a default ATLAS MacroParticle. For easy frame of reference, we're using the Earth.
        No spherical cows here, friendo
        """

        default_macro_mass = self.earth_mass
        default_macro_radius = 1.0
        default_macro_volume = AtlasGeometry.sphere_volume(default_macro_radius)

        if uniform_density_flag is True:
            default_macro_density = default_macro_mass / default_macro_volume
        else:
            # For now, let's not trouble ourselves with density gradients
            # TODO: Implement a density gradient for macro objects
            pass

        default_macro_particle = {
            'mass': default_macro_mass,
            'radius': default_macro_radius,
            'volume': default_macro_volume,
            'density': default_macro_density
        }

        return default_macro_particle


if __name__ == '__main__':
    default_macro_particle = MacroParticleManifest.create_default_macroparticle()