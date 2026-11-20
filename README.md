# Bittensor 128-Subnet Audit: Raw Ledger Telemetry & Verification Data

This repository contains on-chain data snapshots, ledger records, and verification logs supporting a multi-part audit of the Bittensor network.

## Audit Metadata

| Metric | Value |
| --- | --- |
| Snapshot block height | `9542683` |
| Snapshot timestamp | `2026-11-19T19:19:12.000Z` |
| Network scope | 129 registered slots: root subnet 0 and 128 operational subnets |
| Unit standard | 1 TAO = 1,000,000,000 Rao (10^9 Rao) |
| Data integrity | Read-only blockchain state export |

## Repository Files

```text
crypto-analysis/
|-- README.md
|-- Demand_Verification_Log.md
|-- flagship_findings.md
|-- Ledger_000_031.md
|-- Ledger_032_063.md
|-- Ledger_064_095.md
|-- Ledger_096_127.md
|-- Ledger_128_128.md
|-- build_demand_matrix.py
|-- build_ledgers.py
|-- verify_demand_log.py
|-- subnets_snapshot.json
`-- subnets_snapshot.txt
```

The ledger files cover subnet ranges 0-31, 32-63, 64-95, 96-127, and 128. The snapshot files contain the subnet data export in JSON format.

## Data Standardization and Methodology

### Rao-to-TAO Conversion

Subtensor ledger endpoints store emissions, market capitalizations, pool liquidity, and transaction volumes in Rao. Convert a raw Rao value to TAO by dividing by 1,000,000,000:

```text
Value in TAO = Raw Ledger Value (Rao) / 1,000,000,000
```

### Multi-Subnet Operator Identification

Operator links were assessed using the following on-chain metadata fields:

1. `owner`: registered coldkey wallet address.
2. `github`: source code organization or repository path.
3. `subnet_url` and `subnet_contact`: web domain and contact information.
4. `registration_timestamp`: identical or sequential registration times.

## Verification and Reproducibility

Claims, transaction ratios, and root weight allocations can be checked against the snapshot files. For example, query subnet 51 with `jq`:

```bash
jq '.data[] | select(.netuid == 51)' subnets_snapshot.txt
```

## Citation and License

The original README described this dataset as published under the MIT License. No `LICENSE` file is included in this folder; check the repository for license terms before reuse.
