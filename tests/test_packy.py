import tempfile
import pytest
from packy import Packy


def test_get_info():
    pmgr = Packy()
    info = pmgr.get_info('jquery')
    
    assert isinstance(info, dict)
    assert 'version' in info
    assert 'files' in info
    assert isinstance(info['files'], list)


def test_install_single():
    with tempfile.TemporaryDirectory() as temp_dir:
        pmgr = Packy(installdir=temp_dir)

        assert len(pmgr.install('anchor.js')) == 1
        assert len(pmgr.install('anchor.js')) == 0


def test_install_multiple():
    with tempfile.TemporaryDirectory() as temp_dir:
        pmgr = Packy(installdir=temp_dir)

        assert len(pmgr.install('anchor.js\nparticles.js')) == 2
        assert len(pmgr.install('anchor.js\nparticles.js')) == 0


def test_invalid():
    with tempfile.TemporaryDirectory() as temp_dir:
        pmgr = Packy(installdir=temp_dir)

        with pytest.raises(KeyError):
            installed = pmgr.install('invalid__1234')

        with pytest.raises(KeyError):
            installed = pmgr.install('jquery==0.0.1')
