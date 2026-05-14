## Summary
The paper introduces Content-Aware Mamba (CAM) for learned image compression. Two mechanisms are proposed: (i) Content-Adaptive Token Permutation (CTP), which clusters tokens via an EMA-updated codebook and permutes the 1-D scan so similar tokens are contiguous, and (ii) Global-Prior Prompting (GPP), which augments the SSM output projection C with a per-cluster prompt derived from centroids. The resulting CMiC model claims SOTA BD-rate against VTM-21.0 (−15.91/−21.34/−17.58% on Kodak/Tecnick/CLIC) while using ~56% fewer parameters and 78% less peak memory than MambaIC.

## Strengths
- **CTP is empirically effective and cheap.** Adding CTP alone to the vanilla single-scan Mamba baseline gives ~2.0/2.4/1.8% BD-rate gains (Table 2), and Tab. 3 shows training throughput drops only from 23.19 → 22.05 samples/s, with decoding latency rising just 4% (0.387 → 0.405s).
- **Strong efficiency vs other Mamba LIC models.** Vs MambaIC, CMiC reduces parameters 56%, FLOPs 57%, decoding latency 39%, peak memory 78% (Tab. 1). The single-scan + codebook design is a real engineering improvement over multi-directional 2D scans.
- **Codebook + EMA clustering is a reasonable design.** It side-steps the well-known instability of per-batch K-Means and gives deterministic inference-time assignments (Sec. 3.3, Alg. 1).
- **Structural ablation (Tab. 4) is well controlled.** Replacing CAM with Conv / 2D-Mamba / Attention-only / CAM-only all degrade BD-rate at comparable parameter counts, supporting the architectural choice rather than scale.
- **Cluster visualizations (Fig. 10) corroborate the mechanism.** Centroids show consistent semantic specialization across images (edges, red textures, smooth backgrounds), backing the claim that the codebook captures dataset-level patterns.

## Weaknesses

### Fatal
None.

### Major
- **GPP's stated mechanism does not match what it implements.** Sec. 3.4 repeatedly frames GPP as "injecting sample-specific global priors" allowing "information from the entire image to influence the sequence modeling process at every step." But the construction is U = 𝒜([c₁;…;c_K]) on **dataset-level codebook centroids**, and P_i = U[g_i] is just a per-cluster prototype bias indexed by token i's cluster ID. There is no pooling, aggregation, or summary of the current image's features. Any sample-specificity enters only through Γ (the cluster-assignment one-hot), which is the same information CTP already uses for permutation. The "non-causality" demonstration in Fig. 9(c) is most parsimoniously explained by Γ being computed with knowledge of later tokens (assignment), not by the SSM gaining a global view through P. Combined with the relatively small marginal gain of GPP-only (CLIC: 0.47%; Kodak: 1.01%), the contribution narrative around GPP is over-stated and the mechanism description should be rewritten to reflect what is actually implemented.
- **The Kodak "SOTA" framing is fragile and not acknowledged.** Tab. 1 itself reports MLICv2 at −16.16% and DCAE at −15.40% on Kodak, vs CMiC's −15.91%. CMiC is *not* best on Kodak, yet the abstract, intro, and §4.3 repeatedly call the result SOTA across all three datasets without noting the tie/loss on the most widely reported benchmark. The margins on Tecnick/CLIC are decisive; the Kodak claim is not, and the paper should say so.

### Minor
- **No variance/seed information** despite Tab. 1 differences of <0.5% BD-rate carrying the central claim against MLICv2/DCAE on Kodak. Single-run reporting is standard in LIC, but here the margin really matters for framing.
- **Cross-cluster long-range modeling is not isolated.** CTP makes within-cluster tokens contiguous; image-compression redundancy is also useful *between* similar-but-different regions. The paper provides ERF visualizations but no direct measurement (e.g., conditional entropy across cluster boundaries) to show CTP doesn't hurt cross-cluster modeling.
- **K-ablation saturates quickly.** Tab. 6: K=64 (−15.91%) vs K=128 (−15.96%) — essentially flat, and K=32 already gets −14.97%. A wider sweep (16, 256) and analysis of activation-rate saturation would strengthen the codebook design argument.
- **GPP's projection 𝒜 is not ablated** — comparing P = Γ𝒜(C) vs P = ΓC (raw centroids) would isolate how much of GPP's small gain comes from the learnable projection vs the cluster-identity bias itself.

### Trivial
- The "redundancy-aware" framing in Sec. 3.4 ("prompt signal reflects how redundancy is distributed across semantic clusters, highlighting clusters with higher or lower redundancy") is not supported by U's construction — nothing in U encodes a per-cluster redundancy magnitude.
- FTIC latency >10s in Tab. 1 vs others <1s is unexplained.

## Nice-to-Haves
- Re-train MLICv2 and MambaIC on the same Flickr2W schedule for an apples-to-apples Kodak comparison.
- Try GPP variants that *actually* inject image-global statistics (e.g., mean-pooled per-image cluster features, or attention over U weighted by the cluster histogram). If they match the current GPP, that clarifies where the gain truly comes from.
- Direct measurement of conditional-entropy reduction across vs within cluster boundaries.
- Soften "SOTA" to "SOTA on Tecnick/CLIC, competitive on Kodak."

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **"Table 2 appears corrupted"** — the harsh critic correctly noted the first column shows ✓ for the all-off row, but the text clearly states the first row is the both-disabled baseline. This is a parser/rendering artifact (per hard rules, formatting artifacts are not author errors); the numerical content is self-consistent and interpretable.
- **"Hyperparameters/training-step disclosure missing"** — removed per reproducibility-nitpick rule; standard hyperparameters are given in §4.1.
- **Strength: "GPP relaxes strict causality without multi-directional scans"** — conflicts with the verified major weakness on GPP's actual mechanism; the empirical effect exists but the causal interpretation is unsupported.
- **Strength: "GPP injects global context at every step, evidenced by Fig. 9(c) non-zero activations beyond the causal scan boundary"** — same reason; the non-causality is more cleanly attributed to Γ being computed with whole-image knowledge than to GPP carrying global statistics.

## Novel Insights
None beyond the paper's own contributions. The harsh critic's observation that GPP's "global prior" is really a per-cluster prototype bias rather than image-global pooling is a useful diagnostic but follows directly from reading the equations.

## Suggestions
- Rewrite §3.4 to describe GPP as "cluster-prototype conditioning" (what it actually is) rather than as image-global pooling. Acknowledge the limitation honestly.
- In abstract/intro/§4.3, restrict "SOTA" claims to Tecnick/CLIC; describe Kodak as competitive with MLICv2/DCAE.
- Add an experiment with a genuinely image-global prompt (mean-pooled features or attention over centroids weighted by image cluster histogram) — either it matches GPP (clarifies the gain mechanism) or it beats GPP (strengthens the paper).
- Add at least 2-seed variance for Kodak BD-rate given <0.5% margins drive the central comparison.

---

## Calibration

**Anchors retrieved:**
- `KgJwbsfN7G.md` (MambaVC) — avg 4.80, Reject. Same domain (Mamba for LIC) but a simpler first-attempt; CMiC clearly improves on it both in design and empirics.
- `iDe1mtxqK5.md` (Spatial-Mamba) — avg 7.00, Accept. More fundamental architectural contribution for 2D Mamba; CMiC is narrower in scope (compression-specific).
- `AL1fq05o7H.md` (Mamba original) — avg 6.25, Reject. Not directly comparable scope.
- `0A6f1b66pE.md` (Mamba VLM) — avg 4.60, Reject. Different domain.
- `FowFLhUTgO.md` (V2M) — avg 5.50, Reject. 2D Mamba representation learning; similar incremental flavor.
- `HKGQDDTuvZ.md` (FTIC) — avg 6.00, Accept. Closest analog: a transformer-LIC paper accepted with mid-tier scores, incremental but solid empirical gains; CMiC's empirical case is comparably strong with a similar over-claim risk.
- `foKwWau15m.md` (CMC-Bench) — avg 6.00, Reject. Different LIC area (benchmark paper).
- `GSUNPIw7Ad.md` (Compressed latents+MLLM) — avg 6.00, Accept. Less comparable.
- `U67J0QNtzo.md` (Disentangled training LIC) — avg 7.50, Accept. Stronger conceptual contribution than CMiC.
- `lnVPfgRnIV.md`, `qi7udwV66M.md`, `ZWi6RpT4mJ.md`, `7L2bpe7lfm.md` — low-scoring (3.5–4.75) papers in adjacent areas, all noticeably weaker than CMiC.
- `PQpvhUrA1C.md` (AR pretraining Mamba) — 5.75; `iWSl5Zyjjw.md` (DeciMamba) — 5.00; `UAKnJMIBwf.md` (MambaPEFT) — 6.00. Mid-tier Mamba accepts with similar incremental positioning.

CMiC sits closest to FTIC (6.00, accepted) and HKGQDDTuvZ-family: a solid empirical LIC contribution with real efficiency gains and a defensible-but-overclaimed mechanism. Stronger than MambaVC (4.80) and V2M (5.50); weaker than Disentangled Training (7.50) and Spatial-Mamba (7.00).

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>