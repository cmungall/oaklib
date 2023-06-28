import os
import unittest
import tempfile

from oaklib.datamodels.text_annotator import TextAnnotationConfiguration
from oaklib.implementations.ontobee.ontobee_implementation import OntobeeImplementation
from oaklib.implementations.pronto.pronto_implementation import ProntoImplementation
from oaklib.implementations.sparql.sparql_implementation import SparqlImplementation
from oaklib.implementations.sqldb.sql_implementation import SqlImplementation
from oaklib.implementations.gilda import GildaImplementation
from oaklib.implementations.ubergraph import UbergraphImplementation
from oaklib.interfaces.association_provider_interface import (
    AssociationProviderInterface,
)
from gilda.resources import GROUNDING_TERMS_BASE_NAME
from oaklib.selector import get_adapter, get_resource_from_shorthand
from tests import INPUT_DIR


class TestResource(unittest.TestCase):
    def test_from_descriptor(self):
        # no scheme
        resource = get_resource_from_shorthand("foo.obo")
        assert resource.implementation_class == ProntoImplementation
        self.assertEqual("foo.obo", resource.slug)
        resource = get_resource_from_shorthand("foo.owl")
        # this may change:
        assert resource.implementation_class == SparqlImplementation
        resource = get_resource_from_shorthand("foo.ttl")
        # this may change:
        assert resource.implementation_class == SparqlImplementation
        resource = get_resource_from_shorthand("pronto:foo.owl")
        assert resource.implementation_class == ProntoImplementation
        resource = get_resource_from_shorthand("foo.db")
        assert resource.implementation_class == SqlImplementation
        assert resource.slug.startswith("sqlite")
        # with scheme
        resource = get_resource_from_shorthand("pronto:foo.obo")
        assert resource.implementation_class == ProntoImplementation
        self.assertEqual("foo.obo", resource.slug)
        resource = get_resource_from_shorthand("ubergraph:")
        assert resource.implementation_class == UbergraphImplementation
        self.assertIsNone(resource.slug)
        resource = get_resource_from_shorthand("ontobee:")
        assert resource.implementation_class == OntobeeImplementation
        self.assertIsNone(resource.slug)

    def test_input_specification(self):
        os.chdir(INPUT_DIR.parent.parent)
        adapter = get_adapter(str(INPUT_DIR / "example-g2d-input-specification.yaml"))
        if not isinstance(adapter, AssociationProviderInterface):
            raise ValueError("adapter is not an AssociationProviderInterface")
        # test that normalization of IDs happens
        expected = [("NCBIGene:1131", "MONDO:0007032"), ("NCBIGene:57514", "MONDO:0024506")]
        assocs = []
        for a in adapter.associations():
            print(a)
            assocs.append((a.subject, a.object))
        self.assertCountEqual(expected, assocs)

    def test_gilda_from_descriptor(self):
        from gilda.term import Term, dump_terms

        config = TextAnnotationConfiguration(matches_whole_text=True)

        descriptor = "gilda:"
        adapter = get_adapter(descriptor)
        self.assertIsInstance(adapter, GildaImplementation)
        results = list(adapter.annotate_text("nucleus", configuration=config))
        self.assertLessEqual(1, len(results))

        terms = [
            Term(
                norm_text="nucleus", text="Nucleus",
                db="GO", id="0005634", entry_name="Nucleus", status="name", source="GO"
            )
        ]

        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "test_terms.tsv.gz")
            dump_terms(terms, path)

            descriptor = f"gilda:{path}"
            adapter_custom = get_adapter(descriptor)
            self.assertIsInstance(adapter, GildaImplementation)
            results = list(adapter_custom.annotate_text("nucleus", configuration=config))
            self.assertEqual(1, len(results))

            results = list(adapter_custom.annotate_text("nope", configuration=config))
            self.assertEqual(0, len(results))
