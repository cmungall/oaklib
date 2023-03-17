import json
import sys
from dataclasses import dataclass
from typing import Dict

from ndex2 import NiceCXNetwork

from oaklib.converters.data_model_converter import DataModelConverter
from oaklib.datamodels.obograph import GraphDocument
from oaklib.types import CURIE


@dataclass
class OboGraphToCXConverter(DataModelConverter):
    """Converts from OboGraph to OBO Format."""

    def dump(self, source: GraphDocument, target: str = None, **kwargs) -> None:
        """
        Dump an OBO Graph Document to CX

        :param source:
        :param target:
        :return:
        """
        obj = self.convert(source)
        if target is None:
            file = sys.stdout
        else:
            file = open(target, "w", encoding="UTF-8")
        json.dump(obj, file, indent=2, sort_keys=False)

    def convert(self, source: GraphDocument, target: Dict = None, **kwargs) -> Dict:
        """
        Convert an OBO Graph Document to a CX Dictionary.

        :param source:
        :param target: if None, one will be created
        :return:
        """
        cxn = NiceCXNetwork()
        cxn.set_name(source.graphs[0].id)
        pm = {}
        for g in source.graphs:
            for pe in g.prefixes.values():
                pm[pe.prefix] = pe.expansion
        cxn.set_context(pm)
        node_id_map = {}
        for g in source.graphs:
            for n in g.nodes:
                n_iid = cxn.create_node(n.lbl, node_represents=self._id(n.id))
                node_id_map[n.id] = n_iid
                if n.meta:
                    for s in n.meta.synonyms:
                        cxn.add_node_attribute(n_iid, "altname", s.val)
            for e in g.edges:
                s = node_id_map.get(e.sub, None)
                t = node_id_map.get(e.obj, None)
                if not s or not t:
                    continue
                cxn.create_edge(s, t, self._id(e.pred))
        doc = cxn.to_cx()
        return doc

    def _id(self, uri: CURIE) -> CURIE:
        if not self.curie_converter:
            return uri
        curie = self.curie_converter.compress(uri)
        if curie is None:
            return uri
        else:
            return curie
