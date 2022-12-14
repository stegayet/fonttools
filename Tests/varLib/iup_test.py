import fontTools.varLib.iup as iup
import sys
import pytest


class IupTest:

    # -----
    # Tests
    # -----

    @pytest.mark.parametrize(
        "delta, coords, forced",
        [
            ([(0, 0)], [(1, 2)], set()),
            ([(0, 0), (0, 0), (0, 0)], [(1, 2), (3, 2), (2, 3)], set()),
            (
                [(1, 1), (-1, 1), (-1, -1), (1, -1)],
                [(0, 0), (2, 0), (2, 2), (0, 2)],
                set(),
            ),
            (
                [
                    (-1, 0),
                    (-1, 0),
                    (-1, 0),
                    (-1, 0),
                    (-1, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (0, 0),
                    (-1, 0),
                ],
                [
                    (-35, -152),
                    (-86, -101),
                    (-50, -65),
                    (0, -116),
                    (51, -65),
                    (86, -99),
                    (35, -151),
                    (87, -202),
                    (51, -238),
                    (-1, -187),
                    (-53, -239),
                    (-88, -205),
                ],
                {11},
            ),
            (
                [
                    (0, 0),
                    (1, 0),
                    (2, 0),
                    (2, 0),
                    (0, 0),
                    (1, 0),
                    (3, 0),
                    (3, 0),
                    (2, 0),
                    (2, 0),
                    (0, 0),
                    (0, 0),
                    (-1, 0),
                    (-1, 0),
                    (-1, 0),
                    (-3, 0),
                    (-1, 0),
                    (0, 0),
                    (0, 0),
                    (-2, 0),
                    (-2, 0),
                    (-1, 0),
                    (-1, 0),
                    (-1, 0),
                    (-4, 0),
                ],
                [
                    (330, 65),
                    (401, 65),
                    (499, 117),
                    (549, 225),
                    (549, 308),
                    (549, 422),
                    (549, 500),
                    (497, 600),
                    (397, 648),
                    (324, 648),
                    (271, 648),
                    (200, 620),
                    (165, 570),
                    (165, 536),
                    (165, 473),
                    (252, 407),
                    (355, 407),
                    (396, 407),
                    (396, 333),
                    (354, 333),
                    (249, 333),
                    (141, 268),
                    (141, 203),
                    (141, 131),
                    (247, 65),
                ],
                {5, 15, 24},
            ),
        ],
    )
    def test_forced_set(self, delta, coords, forced):
        f = iup._iup_contour_bound_forced_set(delta, coords)
        assert forced == f

        chain1, costs1 = iup._iup_contour_optimize_dp(delta, coords, f)
        chain2, costs2 = iup._iup_contour_optimize_dp(delta, coords, set())

        assert chain1 == chain2, f
        assert costs1 == costs2, f


if __name__ == "__main__":
    sys.exit(pytest.main(sys.argv))
