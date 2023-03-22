import unittest

from rustsim import jaccard_similarity

from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.selector import get_implementation_from_shorthand
from tests import ENDOMEMBRANE_SYSTEM, INPUT_DIR, VACUOLE

DB = INPUT_DIR / "go-nucleus.db"


class TestRustSimImplementation(unittest.TestCase):
    """Implementation tests for SqlDatabase adapter."""

    def setUp(self) -> None:
        """Set up"""
        oi = get_implementation_from_shorthand(f"rustsim:sqlite:///{str(DB)}")
        self.oi = oi

    # def test_pairwise_similarity(self):
    #     pass

    def test_rustsim_jaccard(self):
        """Tests Rust implementations of Jaccard semantic similarity."""
        subj_ancs = set(self.oi.ancestors(VACUOLE, predicates=[IS_A, PART_OF]))
        obj_ancs = set(self.oi.ancestors(ENDOMEMBRANE_SYSTEM, predicates=[IS_A, PART_OF]))
        jaccard = jaccard_similarity(subj_ancs, obj_ancs)
        calculated_jaccard = len(subj_ancs.intersection(obj_ancs)) / len(subj_ancs.union(obj_ancs))
        self.assertAlmostEqual(calculated_jaccard, jaccard)
        # self.assertTrue(True)