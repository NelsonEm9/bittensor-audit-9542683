import json
from pathlib import Path

raw_bytes = Path("subnets_snapshot.json").read_bytes()
if raw_bytes.startswith((b"\xff\xfe", b"\xfe\xff")) or b"\x00" in raw_bytes[:20]:
    text = raw_bytes.decode("utf-16").lstrip("\ufeff")
else:
    text = raw_bytes.decode("utf-8-sig")

payload = None
for line in text.splitlines():
    line = line.strip()
    if line.startswith("1:"):
        payload = json.loads(line[2:])
        break
    elif line.startswith("{") and '"data"' in line:
        payload = json.loads(line)
        break

if not payload:
    raise ValueError("Could not locate '1:{\"data\":...}' JSON line in snapshot.")

subnets = sorted(payload.get("data", []), key=lambda x: int(x.get("netuid", 0)))
print(f"Loaded {len(subnets)} records (Block {subnets[0].get('block_number')})")

def to_tao(val):
    try:
        return f"{float(val) / 1e9:,.2f} TAO"
    except (TypeError, ValueError):
        return "N/A"

def to_pct(val):
    try:
        return f"{float(val) * 100:.2f}%"
    except (TypeError, ValueError):
        return "N/A"

batch_size = 32
for i in range(0, len(subnets), batch_size):
    batch = subnets[i : i + batch_size]
    start_id = int(batch[0].get("netuid", i))
    end_id = int(batch[-1].get("netuid", i + len(batch) - 1))
    filename = f"Ledger_{start_id:03d}_{end_id:03d}.md"

    lines = [
        f"# Bittensor Forensic Ledger: SN {start_id} to SN {end_id}",
        f"**Snapshot Block:** {batch[0].get('block_number')} | **Timestamp:** {batch[0].get('timestamp')}\n",
    ]
    for s in batch:
        netuid = s.get("netuid", "N/A")
        name = s.get("subnet_name") or s.get("name") or "Unnamed"
        lines.append(f"## SN {netuid} — {name} (Rank #{s.get('rank', 'N/A')})")
        lines.append(f"- **Description:** {s.get('description') or 'None provided'}")
        lines.append(f"- **Owner Coldkey:** `{s.get('owner', 'N/A')}`")
        lines.append(f"- **Registered:** {s.get('registration_timestamp', 'N/A')} | **Immune:** {s.get('is_immune', 'N/A')}")
        lines.append(f"- **Emission (Raw / TAO):** {s.get('emission', '0')} ({to_tao(s.get('emission', 0))})")
        lines.append(f"- **Incentive Burn:** {to_pct(s.get('incentive_burn', 0))}")
        lines.append(f"- **Market Cap:** {to_tao(s.get('market_cap', 0))}")
        lines.append(f"- **Pool Liquidity:** {to_tao(s.get('liquidity', 0))} | **TAO in Pool:** {to_tao(s.get('tao_in_pool', 0))}")
        lines.append(f"- **24h TAO Volume:** {to_tao(s.get('tao_volume_24_hr', 0))} (Buys: {s.get('buys_24_hr', 0)} / Sells: {s.get('sells_24_hr', 0)})")
        lines.append(f"- **Alpha Price:** {s.get('price', 'N/A')} TAO | **Root Prop:** {to_pct(s.get('root_prop', 0))}")
        lines.append(f"- **Active Keys / Max:** {s.get('active_keys', 'N/A')} / {s.get('max_neurons', 'N/A')}")
        lines.append(f"- **GitHub:** {s.get('github') or 'None listed'}")
        lines.append(f"- **Website:** {s.get('subnet_url') or 'None listed'}\n")

    Path(filename).write_text("\n".join(lines), encoding="utf-8")
    print(f"Created {filename} ({len(batch)} subnets)")
