import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

raw_bytes = Path("subnets_snapshot.json").read_bytes()
text = (
    raw_bytes.decode("utf-16").lstrip("\ufeff")
    if raw_bytes.startswith((b"\xff\xfe", b"\xfe\xff")) or b"\x00" in raw_bytes[:20]
    else raw_bytes.decode("utf-8-sig")
)

payload = next(
    json.loads(line[2:])
    for line in text.splitlines()
    if line.strip().startswith("1:")
)

subnets = [s for s in payload.get("data", []) if int(s.get("netuid", 0)) != 0]
subnets.sort(key=lambda x: float(x.get("emission", 0)), reverse=True)

def check_github(gh_url):
    gh = (gh_url or "").strip().rstrip("/")
    if not gh or "github.com/" not in gh:
        return "No GitHub URL listed"
    parts = gh.split("github.com/")[-1].split("/")
    if len(parts) < 2 or parts[0].lower() == "orgs":
        return f"Org/profile link only (`{gh}`) — manual repo check needed"
    owner, repo = parts[0], parts[1]
    api_url = f"https://github.com{owner}/{repo}"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Bittensor-Auditor"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            info = json.loads(resp.read().decode())
            pushed = info.get("pushed_at", "")
            days_ago = (
                datetime.now(timezone.utc)
                - datetime.fromisoformat(pushed.replace("Z", "+00:00"))
            ).days
            return (
                f"Last push: **{days_ago}d ago** | Fork: `{info.get('fork')}` | "
                f"Archived: `{info.get('archived')}` | Stars: `{info.get('stargazers_count')}`"
            )
    except Exception as e:
        return f"Repo inaccessible or 404 (`{e}`)"

lines = [
    "# Bittensor Layer 2: Demand Verification Matrix (128-Subnet Investigation)",
    "**Methodology:** On-chain emission & burn triage paired with GitHub commit velocity and off-chain billing verification.\n",
    "## Evidentiary Tier Definitions",
    "- **Tier 1 (Verified External Demand):** Self-serve fiat/card/stablecoin checkout or verifiable B2B contracts with public pricing.",
    "- **Tier 2 (Circular / Token-Gated Demand):** Active product, but usage requires native tokens, TAO, or subsidized testnet credits.",
    "- **Tier 3 (Unverified / 'Trust Me' Claims):** Marketing website or 'Contact Sales' form with zero public billing, usage telemetry, or verifiable customers.",
    "- **Tier 4 (Pure Subsidy Sink / Ghost Subnet):** Zero emission, 100% incentive burn, deprecated/for-sale status, abandoned GitHub, or missing product.\n",
    "---\n",
]

auto_t4 = 0
for s in subnets:
    netuid = s.get("netuid")
    name = s.get("subnet_name") or s.get("name") or "Unknown"
    emission = float(s.get("emission", 0))
    burn = float(s.get("incentive_burn", 0))
    url = (s.get("subnet_url") or "").strip()
    gh = (s.get("github") or "").strip()
    desc = (s.get("description") or "").strip()

    reasons = []
    if emission == 0:
        reasons.append("Zero current emission (`emission: 0`)")
    if burn >= 0.99:
        reasons.append(f"100% incentive burn (`{burn * 100:.0f}%`)")
    if name.lower() in ("unknown", "onsale", "deprecated"):
        reasons.append(f"Flagged subnet name (`{name}`)")
    if not url and not gh:
        reasons.append("No website or GitHub repository listed")

    if reasons:
        tier = "Tier 4 — Pure Subsidy Sink / Ghost Subnet (Auto-Triaged)"
        gh_status = "Skipped (auto-triaged Tier 4)"
        evidence = "; ".join(reasons) + "."
        auto_t4 += 1
    else:
        tier = "[PENDING MANUAL CHECK: Tier 1 / Tier 2 / Tier 3]"
        gh_status = check_github(gh)
        evidence = "Active emission recipient. Check website pricing/checkout (fiat vs. token vs. contact-sales)."
        print(f"Checked SN {netuid} ({name}) -> {gh_status}")

    lines.append(f"### SN {netuid} — {name} (Rank #{s.get('rank', 'N/A')})")
    lines.append(f"- **Classification:** {tier}")
    lines.append(f"- **Raw Emission:** {int(emission):,} | **Incentive Burn:** {burn * 100:.1f}%")
    lines.append(f"- **Website:** {url or 'None'} | **GitHub:** {gh or 'None'}")
    lines.append(f"- **GitHub Velocity:** {gh_status}")
    lines.append(f"- **Claimed Product:** {desc or 'None provided'}")
    lines.append(f"- **Audit Evidence:** {evidence}\n")

Path("Demand_Verification_Log.md").write_text("\n".join(lines), encoding="utf-8")
print(f"\nDone! Saved Demand_Verification_Log.md | Auto-Tier 4: {auto_t4} | Remaining to check: {len(subnets) - auto_t4}")
