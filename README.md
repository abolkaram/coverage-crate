# Coverage Crate

One manifest goes onto the belt. A bounded evidence map comes off the other end.

[Open the freight depot](https://coverage-crate.pages.dev/) · [Inspect the StudioNet contract](https://explorer-studio.genlayer.com/address/0xB9fbc7623e66e538572C615c013f85a00655A165)

Coverage Crate freezes a public JSON manifest containing two to six obligations and two to five evidence records. Validators retrieve the manifest and every listed source themselves, bind the bytes to ordered SHA-256 digests, and agree on the complete obligation-to-source matrix. The contract, not the model, derives uncovered obligations and the smallest source subset that covers the whole checklist.

## Route through the depot

`register(manifest_url)` creates a `PACKED` crate. `map_coverage(crate_id)` is permissionless and ends once as `COVERED` or `GAPPED`. `get_crate` returns the manifest identity, frozen digests, full matrix, minimum cover, and gaps.

Duplicate manifests, repeated crate ids, mutable evidence, missing obligation rows, unknown source ids, and replayed mapping are rejected. Public fixtures demonstrate the mechanism and are disclosed as repository-owner records, not independent authorities.

## Verify

```text
python -m pytest -q
genvm-lint contracts/contract.py
python scripts/smoke.py
```

The interface is a moving freight belt rather than a dashboard or raw contract-argument form. A visitor scans one manifest label, watches the crate move between stations, and receives a packing slip showing the derived cover.
