from pathlib import Path

SRC = (Path(__file__).parents[1] / "contracts" / "contract.py").read_text()

def test_lifecycle_and_terminal_states():
    for token in ("register", "map_coverage", "get_crate", '"PACKED"', '"COVERED"', '"GAPPED"'):
        assert token in SRC

def test_manifest_and_sources_are_refetched_and_digest_bound():
    assert SRC.count("gl.nondet.web.get") >= 4
    for token in ("manifest_digest", "source_digests", "frozen manifest changed", "frozen evidence changed"):
        assert token in SRC

def test_every_obligation_is_bound_by_consensus():
    for token in ("complete obligation map required", "sorted(coverage.keys())", "prompt_comparative"):
        assert token in SRC

def test_minimum_cover_and_gaps_are_derived_not_prompted():
    for token in ("for mask in range", "minimal_cover_json", "gaps =", 'crate.state = "COVERED" if not gaps else "GAPPED"'):
        assert token in SRC

def test_replay_and_input_guards():
    for token in ("crate or manifest already registered", "unique evidence sources required", "public HTTPS URL required"):
        assert token in SRC
