import logging

from mvt.ios.modules.mixed.tcc import TCC
from mvt.common.module import run_module

from ..utils import get_backup_folder

class TestManifestModule:
    def test_manifest(self):
        m = TCC(base_folder=get_backup_folder(), log=logging)
        run_module(m)
        assert len(m.results) == 11
        assert len(m.timeline) == 11
        assert len(m.detected) == 0
        assert m.results[0]["service"] == "kTCCServiceUbiquity"
        assert m.results[0]["auth_value"] == "allowed"
