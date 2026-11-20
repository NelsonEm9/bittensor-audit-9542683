# Flagship Investigation Blueprint: The Four Pathologies of Bittensor (Block 9542683)
**Core Thesis:** Across all 128 Bittensor subnets, protocol inflation (TAO emissions) functions primarily as a structural subsidy—funding R&D benchmarks with zero customers, circular token buyback loops, dead 100%-burn slots, and below-cost API wrappers sitting on top of centralized Web2 AI providers.

---

## Pathology 1: Subsidized Web2 Wrappers & Idle-Pool Accounting (The "Tier 1" Illusion)
Even among the narrow group of subnets with verifiable external USD/fiat billing, protocol emissions are used to subsidize idle hardware or undercut competitors while acting as a middleman for centralized Web2 models:
- **SN 51 (`lium.io` | Rank #1 | 16,313,099 emission | 0.0% burn):** Live GPU marketplace (`$0.48/hr` RTX PRO 4500 to `$4.35/hr` H200). Its own documentation confirms a dual-income model where an explicit *"Unrented pool"* pays idle GPUs from SN 51 token inflation when zero external renters are paying.
- **SN 28 (`SayGM` | Rank #8 | 4,199,034 emission | 0.1% burn):** Commercial LLM proxy gateway selling drop-in API access to **Claude, GPT, and Gemini** inside Intel TDX enclaves—using Bittensor inflation to subsidize an API reseller for centralized Web2 labs.
- **SN 34 (`Yugos` | Rank #16 | 1,663,957 emission | 0.0% burn):** Self-serve model router API (`$10` minimum credit top-up) that routes developer requests to **Claude, GPT, Gemini, and Qwen**.
- **SN 117 (`everyframe.studio` | Rank #61 | 888,166 emission | 0.0% burn):** Commercial video generation studio selling unified credits for centralized APIs (**Veo, Kling, Seedance, MiniMax**). Miners require **zero GPUs** and act strictly as attested API proxy workers while collecting SN 117 emissions.
- **SN 64 (`Chutes` | Rank #2 | 7,947,311 emission | 0.0% burn) & SN 53 (`engy` | Rank #4 | 4,742,811 emission | 0.0% burn):** Live serverless inference APIs (`llm.chutes.ai` and `api.engy.ai`) offering prepaid per-million-token USD pricing (`$0.02–$0.20` input) where below-market rates are offset by miner emission subsidies.
- **SN 4 (`Targon` | Rank #3 | 7,002,391 emission) & SN 56 (`Gradients` | Rank #13 | 1,853,995 emission):** Live self-serve confidential VM/GPU compute (`targon.com`) and on-demand fine-tuning (`gradients.io`) whose hardware supply is incentivized by daily TAO emissions.
- **SN 118 (`Ditto` | Rank #95 | 71,971 emission | 0.0% burn):** Cross-tool AI memory SaaS (`$19/mo` Plus, `$97/mo` Pro) operated by Omni Aura LLC; its legacy `dittobench` subnet repositories were archived in August 2026 while the commercial app plugs into Claude, ChatGPT, and Cursor.

---

## Pathology 2: Circular Token Loops & Ecosystem Recycling (The "Tier 2" Closed Economy)
Several high-profile subnets generate volume or revenue that recycles internally within Bittensor rather than bringing net-new external capital into the network:
- **SN 93 (`Bitcast` | Rank #17 | 2,214,207 emission | 2.0% burn):** Creator attention and X/YouTube promotion protocol claiming `$489.8K` in revenue, with **`75.6%` (`$370.1K`) recycled directly into SN 93 Alpha token buybacks** to prop up its own pool.
- **SN 75 (`Hippius` | Rank #11 | 2,859,746 emission | 0.0% burn):** Decentralized S3 object storage (`$6/TB`) and Drive SaaS (`$4–$50/mo`). While self-serve fiat pricing exists, every featured enterprise case study on its homepage (**Ditto SN 118, Vidaio SN 85, Minos SN 107**) is another emission-subsidized Bittensor subnet.
- **SN 79 (`MVTRX` | Rank #64 | 120,204 emission | 0.0% burn):** Operates an off-chain Bittensor Alpha/TAO limit-order-book exchange (`mvtrx.ai`) and C++ trading simulator (`τaos`). Repository docs confirm **100% of current mainnet emissions pay synthetic trading simulations (`95%`) and `GenTRX` gradient training (`5%`)**, while the mainnet exchange scoring mechanism is not yet active.
- **SN 89 (`InfiniteQuant` | Rank #72 | 87,487 emission | 0.0% burn):** Binary prediction market (`infinitequant.app/markets`) and `$199` prop challenge. Its own site disclosure admits its `$737,145.97` payout figure combines prop payouts with all SN 89 miner emissions, while market liquidity is collateralized by SN 89 Alpha vaults.
- **SN 36 (`Weir` | Rank #115 | 4,196,646 emission) & SN 90 (`KubeTEE` | Rank #55 | 4,025,259 emission | 45.9% burn):** Crypto-settled GPU/TEE marketplaces where `Weir` pays idle verified GPUs from emissions and `KubeTEE` requires hourly payment in **Alpha or TAO** while burning `45.9%` of its allocation.
- **SN 114 (`SOMA` | Rank #27 | 4,225,224 emission):** Internal MCP prompt-compression utility routing traffic through partner subnet Chutes (SN 64) with no standalone fiat SaaS revenue.

---

## Pathology 3: High-Emission R&D Sinks With Zero Customers (The "Tier 3" Subsidy Trap)
Some of the largest emission extractors on Bittensor operate purely as closed R&D benchmarks, synthetic simulations, or "Talk to Sales" landing pages with zero self-serve customer revenue:
- **SN 107 (`Minos` | Rank #18 | 7,215,343 emission | 0.0% burn):** Captures over `7.21M` in raw emissions (`~3.9%` of network emissions) to run internal 72-minute synthetic genomic mutation rounds (`HelixForge` BAM files) with zero commercial product or customer checkout.
- **SN 120 (`Affine` | Rank #6 | 6,781,304 emission | 0.0% burn):** Internal RL/model-evaluation leaderboard (`MATH-500`, `AIME`) with zero external customer billing or API checkout.
- **SN 92 (`REAX` | Rank #70 | 4,916,847 emission | 61.8% burn):** Synthetic decision-model routing probes burning **`61.8%`** of all incentives while still capturing `4.91M` in raw emissions.
- **SN 44 (`Score` | Rank #7 | 3,914,350 emission), SN 97 (`Ingot` | Rank #43 | 3,091,155 emission), & SN 9 (`iota` | Rank #9 | 2,909,267 emission):** Combined `9.91M` in raw emissions across computer-vision marketing showcases (`Score` *"Let's Talk"*), free Hugging Face GGUF quantization benchmarks (`Ingot`), and unpriced disaggregated training pitches (`iota`).
- **SN 3 (`Teutonic` | Rank #10 | 2,492,624 emission):** Internal 10B LLM loss-reduction dashboard displaying *"NO COMPLETED LOSS DATA"* and *"0 KINGS"* at snapshot time.
- **SN 8 (`Vanta` | 4,885,084 emission), SN 15 (`ORO` | 4,599,114 emission), SN 80 (`OpenRoboto` | 4,528,931 emission), SN 68 (`NOVA` | 2,164,727 emission), & SN 112 (`THOR` | 1,751,130 emission):** Quantitative signal pools, simulated Docker shopping arenas (`ORO Bench`), robotics data bounties, and molecular screening competitions lacking verified external fiat revenue.
- **SN 1 (`Apex` | Rank #33 | 77,307 emission | 53.2% burn):** Macrocosmos's flagship competition subnet displaying **`0` active competitions, `0` running today, and `0.00α` paid out** on its live dashboard while burning `53.2%` of emissions.

---

## Pathology 4: 100%-Burn Zombies, Deprecated/For-Sale Slots & Operator Clusters (Tier 4)
Beneath the active emission leaders sits a long tail of dead infrastructure, explicit slot liquidations, and multi-subnet operator clusters:
- **Explicitly Deprecated & For-Sale Slots:**
  - **SN 39 (`deprecated` | Rank #32 | 927,946 emission | 17,708.15 TAO in pool):** Literally named `deprecated` across its name, description, email (`deprecated@gmail.com`), and GitHub URL, yet still capturing `927,946` raw emissions.
  - **SN 86 (`OnSale` | Rank #125 | 665 emission | 218.81 TAO in pool):** Official chain description advertises *"Reach out @SteveJYY on Telegram for subnet sale."*
- **100% Incentive Burn / Zero-Emission Slots (`incentive_burn: 1.0`, `emission: 0`):** Over two dozen ranked slots report 100% miner incentive burn—including top-50 slots **SN 110 (`Green Compute`, Rank #14)**, **SN 95 (`Actual`, Rank #15)**, **SN 11 (`TrajectoryRL`, Rank #30)**, **SN 23 (`Trishool`, Rank #34)**, and **SN 52 (`Dojo`, Rank #35)**—plus unconfigured `Unknown` slots (**SN 57, SN 26, SN 35, SN 109, SN 78**).
- **No-Code / No-Site Outliers:** **SN 73 (`Elenost`, 42,999 emission)** lists zero GitHub repository on-chain; **SN 33 (`ReadyAI`, 42,681 emission, 25.3% burn)** lists zero website and zero product description.
- **Multi-Subnet Operator Clusters:**
  - **`macrocosm-os`:** Operates SN 1 (`Apex`), SN 9 (`iota`), and SN 13 (`Data Universe`).
  - **`qbittensor-labs`:** Operates SN 48 (`Quantum Compute`) and SN 63 (`Enigma`).
  - **`taostat`:** Listed on both SN 19 (`blockmachine`) and SN 28 (`SayGM`).
  - **`entrius`:** Listed on both SN 7 (`Allways`) and SN 74 (`Gittensor`).
  - **`Barbariandev`:** Listed on both SN 123 (`MANTIS`) and SN 125 (`Refinery`).
