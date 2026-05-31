Now I have enough information to write the review.

## Summary
PIRN is a few-shot multimodal (RGB + surface-normal) anomaly detection framework built around a vector-quantized prototype codebook and a ViT encoder–decoder. The contributions are three modules: Balanced Prototype Assignment (BPA) using Sinkhorn-OT to mitigate codebook collapse, Adaptive Prototype Refinement (APR) using a GRU to update prototypes at inference from test-image context, and Multimodal Normality Communication (MNC) using GAT-aligned prototypes and gated cross-attention. The paper reports SOTA on MVTec-3D-AD and Eyecandies across 5/10/50/all-shot settings and the best localization on Real-IAD D3 (full-shot), at substantially lower FLOPs than FIND.

## Strengths
- **Consistent few-shot AUROC gains over the listed baselines.** Table 1 shows clear margins over INP-Former at 5- and 10-shot on both MVTec-3D-AD (+3.9 / +3.7 AUROC_I) and Eyecandies (+3.6 / +4.0 AUROC_I).
- **Strong accuracy/efficiency trade-off.** Table 4 reports 103.36 G FLOPs / 17.49 ms latency for PIRN versus 728.46 G / 76.09 ms for FIND while matching FIND's AUROC_I (0.922 vs 0.921). This is the paper's most compelling concrete result.
- **BPA mechanism is principled and visually substantiated.** Section 3.2 formalizes Sinkhorn-OT with the equal-mass constraint **b** = (N/K)·**1**_K, and Fig. 1(b) shows visibly more uniform prototype coverage than softmax assignment.
- **MNC's cross-modal benefit shows up where it should.** Table 3 shows the largest RGB+SN improvement over either single modality at 5-shot (0.854 / 0.794 → 0.900 AUROC_I), consistent with the claim that cross-modal communication helps most when per-modality normal coverage is poorest.
- **Generalization to Real-IAD D3 for localization.** PIRN reaches 0.961 AUROC_P, ahead of tri-modal D³M (0.937), with leads in 13/20 categories.

## Weaknesses

### Fatal
None — no verified weakness invalidates the core method.

### Major
- **The strongest cited baseline (FIND) is absent from the main accuracy tables.** Table 4 explicitly labels FIND as "SOTA" with 0.921 AUROC_I at 10-shot — essentially tied with PIRN's 0.922 — yet Table 1 omits FIND across all four shot settings on both datasets. The headline framing "improves AUROC_I by +3.7 (10-shot)" and "consistently achieves superior performance" depend on comparing against INP-Former (0.885), not FIND (0.921). The actual marginal improvement against the paper's own claimed SOTA on the one shot setting where it is reported is +0.1 AUROC_I. This is the single most important presentational issue: it does not invalidate the method, but it materially weakens the empirical case as currently written. Including FIND across the 5/10/50/all-shot grid would resolve this directly.

- **Table 2 is internally inconsistent with the surrounding text.** Setting aside the duplicated ✓ marks (likely a parsing artifact), the numerical row "0.967 / 0.998 / 0.947" exceeds the full-model row "0.922 / 0.991 / 0.966" on AUROC_I and AUROC_P. Section 4 explicitly states "Removing each component from the full model results in a consistent performance drop, validating the contribution of every component" — but at least one row in the same table shows a substantial *increase* over the full model on two of three metrics. As presented, the table does not support the claim that all three modules are jointly best; this needs labeling clarification.

- **APR is presented as a central contribution but is the weakest-supported one empirically.** Table 7's "wo APR module" row drops AUROC_I only from 0.922 to 0.916 — within the range of expected few-shot seed variance — and the paper offers no direct probe of APR's claimed gating behavior (§3.3 states the GRU "leaves p_k essentially unchanged" under anomalous context, but no measurement of prototype drift on normal vs. anomalous inputs is reported). Given that APR's stated role is to bridge the train-test gap, a direct measurement (e.g., ‖Δp_k‖ distributions on normal vs. anomalous patches) would substantiate the mechanism rather than relying on a 0.6-point AUROC delta.

### Minor
- **No variance over support-set draws.** Few-shot anomaly detection is sensitive to which k normal samples are sampled. Table 1 reports a single number per cell. Several gaps over INP-Former are within 1–3 AUROC points; mean ± std across multiple 5/10-shot draws would distinguish a robust improvement from a favorable split. This is standard practice in few-shot work.
- **Real-IAD D3 evaluation is full-shot only, despite few-shot being the central scope.** PIRN trails D³M on detection AUROC_J (0.873 vs 0.890) but leads on localization AUROC_P (0.961 vs 0.937). The defense that D³M uses tri-modal input is reasonable, but the paper's headline thesis is few-shot superiority; a few-shot evaluation on Real-IAD D3 would be the most natural validation and its absence is conspicuous.
- **Surface-normal-only outperforms RGB-only at every shot setting (Table 3).** This is worth discussing: it suggests the dataset's anomalies are dominated by geometric defects, which moderates how broadly the multimodal-communication claim applies to texture-only defects. A direct analysis of cases where MNC flips a prediction on texture-only defects would tighten the MNC claim.

### Trivial
None worth weighting in evaluation.

## Nice-to-Haves
- Quantitative codebook-utilization metrics (entropy of patch-to-prototype assignment, fraction of dead prototypes) comparing softmax / Top-k / BPA — this would tie the BPA mechanism directly to its claimed effect rather than relying on a t-SNE.
- A direct probe of APR's gating: distribution of ‖Δp_k‖ on normal vs. anomalous test patches, to substantiate the "GRU leaves p_k unchanged on anomalous context" claim.
- Brief description of how FLOPs are computed for memory-bank baselines (where the dominant cost is nearest-neighbor search, not the forward pass) to make the efficiency claim airtight.
- A few implementation specifics for reproducibility: Sinkhorn iteration count / entropic ε, KNN graph parameters in MNC stage-1 (k, symmetric vs. directed), and the form of the "soft mining loss (Luo et al., 2025)" used.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Cannot independently verify FIND exists / cannot reproduce."** Not raised by the harsh critic, but flagged out of caution: any criticism doubting cited tools/baselines is removed per the rules. FIND is a cited paper; existence is not in question.
- **Sinkhorn hyperparameter sensitivity / "uniform target forces hundreds of patches per prototype."** Demoted — this is a reproducibility nit and the Sinkhorn formulation in Eq. (1)–(2) is mathematically well-defined as stated; "sensitivity worth documenting" is a nice-to-have, not a flaw.
- **MNC graph specification (k, symmetric vs. directed).** Demoted to nice-to-have; this is implementation detail rather than a substantive methodological gap.
- **Loss form not written out.** Demoted; the paper cites it (Luo et al., 2025) and this is a reproducibility nit.
- **Strength Finder claim: "Ablations confirm each component's independent contribution."** Removed because it directly conflicts with the verified Table 2 inconsistency above; the verified weakness wins.
- **Strength Finder claim: "Strong generalization to a challenging real-world dataset."** Weakened — PIRN is best at localization on Real-IAD D3 but second on detection (AUROC_J), so "strong generalization" is overstated as written.
- **Duplicated checkmarks in Table 2.** Likely a PDF parsing artifact, not an author error; only the numerical inversion is kept as a substantive weakness.

## Novel Insights
None beyond the paper's own contributions. The combination — OT-balanced quantization (cf. Sinkhorn assignment in prior work), GRU-style test-time prototype update, and GAT-aligned cross-modal prototype injection — is sensibly stitched together, but the individual ingredients are each instances of patterns already used in prototype/codebook learning and multimodal alignment.

## Suggestions
- Add FIND to Table 1 across all 5/10/50/all-shot cells on both MVTec-3D-AD and Eyecandies, with the same protocol used elsewhere. This single change determines whether "consistently outperforms" survives.
- Re-typeset Table 2 with the actual subset of checkmarks per row and audit the row that currently reads 0.967/0.998/0.947 — either correct it or explain why a partial configuration beats the full model on two of three metrics.
- Report mean ± std over ≥5 sampled support sets for the 5- and 10-shot results.
- Add a few-shot block (at minimum 5- and 10-shot) on Real-IAD D3 to the experiments — this is the most natural extension of the headline thesis to a more challenging dataset.
- Add a direct measurement of APR's gating behavior: the L2 norm of Δp_k on test patches partitioned by ground-truth normal vs. anomalous. This would substantiate the §3.3 mechanism in a way Table 7 currently does not.

## Calibration

### Anchors retrieved
- `gTsLBDMZrL.md` — *A Prototype-oriented Fast Refinement Model for Few-shot Industrial AD* — avg **5.50**, Round 1 & 2 — Closest topical match (OT/Sinkhorn for few-shot prototype refinement); PIRN is methodologically broader (multimodal + three modules vs. one EM refinement).
- `MbtUctg3KW.md` — *Generalized AD with Knowledge Exposure* — avg **2.50**, Round 1 — Much weaker; clearly below PIRN.
- `bESxQeXTlo.md` — *CLIP-LAD few-shot logical AD* — avg **3.00**, Round 1 — Below PIRN in empirical depth.
- `7jUQHmz4Tq.md` — *D3AD diffusion AD* — avg **3.00**, Round 1 — Below PIRN.
- `ZxsKRuP0o8.md` — *Meta-Tasks few-shot* — avg **2.50**, Round 1 — Off-topic and weaker.
- `Zzs3JwknAY.md` — *One-for-All Few-Shot AD* — avg **6.40**, Round 1 — More polished few-shot AD with cleaner empirical story; above PIRN.
- `Vi6p2TeujL.md` — *PTAD tabular AD* — avg **4.25**, Round 1 — Less relevant.
- `Slr3KojVRO.md` — *PO3AD 3D point cloud AD* — avg **4.50**, Round 1 — Topically related, weaker empirical case.
- `cJs4oE4m9Q.md`, `GMwRl2e9Y1.md`, `Y6aHdDNQYD.md`, `9Cu8MRmhq2.md` — avg **8.00**, Round 1 — Strong-band anchors, clearly above PIRN.
- `Cb4YXpqBIc.md` — *Cross-Modal Few-Shot Learning* — avg **5.00**, Round 2 — Comparable territory.
- `AHgc5SMdtd.md` — *MuSc zero-shot AD* — avg **5.20**, Round 2 — Comparable; MuSc was accepted despite mid scores.
- `kS27PPs3yR.md` — *Fine-grained Abnormality Prompt Learning* — avg **5.00**, Round 2 — Comparable, weaker overall.
- `7QDIFrtAsB.md`, `HW2lIdrvPb.md`, `uizIvVBY8P.md`, `gRXLa6LS3J.md` — avg **5.67–5.75**, Round 2 — Comparable.
- `JDiER86r8v.md` — *MMAD benchmark* — avg **6.50**, Round 2 — Above PIRN.
- `buC4E91xZE.md` — *AnomalyCLIP* — avg **6.17**, Round 2 — Above PIRN.

### Bracket reasoning
**Round 1 bracket: [5.0, 6.5].** PIRN is clearly above the 2.5–3.0 band (more rigorous experiments, well-motivated design) and clearly below the 8.0 band (no theoretical contribution, evidential issues). Most similar to the 5.5 prototype-refinement paper (which was rejected) and the 6.4 one-for-all few-shot paper (which was accepted).

**Round 2 narrowing.** Compared to the 5.50 anchor (gTsLBDMZrL), PIRN has a richer architecture and broader experimental scope (3 datasets, multimodal, efficiency analysis), so it should be at least at that level. Compared to the 6.40 anchor (Zzs3JwknAY, accepted), PIRN's empirical case has clearer concrete holes — missing FIND in headline tables, the Table 2 inversion, no variance reporting — that the 6.40 anchor does not have. Compared to the 5.20 MuSc anchor (accepted), PIRN is similarly mid-strong on novelty but has weaker empirical hygiene. Final position: above the 5.50 rejected anchor (better method/experiments) but not at the 6.40 accepted anchor (cleaner empirical case there). Lands at **5.0** — the FIND-omission and Table 2 issues are real and meaningfully weaken the headline claim, pulling it just below the rejected 5.5 anchor in empirical credibility despite the broader contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>