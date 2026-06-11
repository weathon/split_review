Based on calibration:

**Round 1 bracket**: paper sits between weak foundation-model anchors (~3.0) and middle applied-ML anchors (~5–7). Initial bracket: 3.5–5.

**Round 2 narrowing** anchors cluster the paper near 4.0–4.5 (VideoEval 4.0, Genomic Foundationless 4.25, Attention Head Purification 4.5, Self-TPT 5.0). The paper's methodology gaps (undefined Eq. 11, staged comparison, overclaimed "zero-shot"/"foundation model", numerical inconsistencies) push it below the prompt-tuning rejects at ~5.0, but the genuinely meaningful generalization result keeps it above the weakest 3.0 anchors.

**Anchor comparison:**
- `XhdckVyXKg.md` (3.0, R1-low) — generic FM, weaker than this paper which has a concrete generalization result.
- `7zJDTnogdG.md` (3.33, R1-low) — comparable narrow contribution.
- `ntSP0bzr8Y.md` (3.0, R1-low) — comparable overclaim.
- `DYXl6P70aH.md` (3.0, R1-low / R2) — benchmark paper, weaker than this.
- `9TClCDZXeh.md` (7.0, R1-mid) — much more rigorous wireless paper; SigMap is well below.
- `BnYJdouhkp.md` (5.83, R1-mid) — better isolated than SigMap.
- `OxrDTroSNP.md` (4.25, R1-mid) — comparable.
- `gFvRRCnQvX.md` (6.4, R1-mid) — better methodology.
- `k38Th3x4d9.md`, `j7b4mm7Ec9.md`, `25kAzqzTrz.md`, `P7KIGdgW8S.md` (R1-high) — clearly stronger than SigMap.
- `wMRFTQwp1d.md` (4.0, R2) — closest match in framing/issues.
- `kDZKEtDnT1.md` (4.25, R2) — comparable rejection.
- `sGqd1tF8P8.md` (4.17, R2) — comparable.
- `NeVbEYW4tp.md` (5.0, R2) — better-controlled prompt tuning.
- `5dcnU4gihd.md` (4.5, R2) — comparable.
- `tG5mpAM7ZK.md` (5.33, R2) — slightly above.
- `huwR9N2ea0.md` (5.5, R2) — slightly above.

SigMap most closely matches the 4.0–4.5 cluster.

## Summary
SigMap proposes a wireless localization foundation model with two contributions: (1) a cycle-adaptive masking strategy for masked-CSI pretraining that targets periodic shortcuts, and (2) a "map-as-prompt" mechanism that uses a GCN over a Delaunay-triangulated 3D building/BS graph to produce prompt tokens for a frozen Transformer. Evaluation is on DeepMIMO O1_3p5 (in-distribution) and DeepMIMO O2 / WAIR-D (generalization).

## Strengths
- Geographic prompt ablation (Table 4) is a clean 3-point comparison: 3D map reduces single-BS MAE from 2.275 → 1.564 m and ~doubles CDF@1m (31.0 → 60.5%). The 2D variant retains most of the gain (1.692 m), suggesting topological cues drive much of the benefit.
- Generalization to unseen environments with only ~100 samples (Table 4.5) is meaningful: 1.026 m on DeepMIMO O2 and 1.880 m on WAIR-D, both clearly better than LWLM, while updating only ~0.7% of parameters.
- Parameter-efficient fine-tuning is well documented (Table 5): 0.085 M trainable parameters, 30 min fine-tune, 0.83 ms/sample inference.

## Weaknesses

### Fatal
None.

### Major
- **Main comparisons confound map information with method.** Tables 1, 2 and the generalization table place SIGMAP (w/ map) against baselines (OMP, CNN, SWiT, LWLM) that have no map access. The fair comparison — SIGMAP (w/o map) vs LWLM — shows much weaker gains: Table 1 MAE 2.275 vs 2.382 (~4%), RMSE 8.532 vs 5.822 (worse), CDF@1m 31.0 vs 25.3. The abstract's claim of "significantly outperforming both supervised and self-supervised baselines by considerable margins" therefore largely traces to extra side information, not the prompt mechanism. No comparison swaps the prompt for alternative map-fusion strategies (concatenation, cross-attention, separate map encoder), so "map-as-prompt" as an *architectural* claim is not isolated.
- **Methodology/experiments mismatch (Eq. 11 "NLoS-aware attention").** Section 4.2 attributes single-BS gains to an "NLoS-aware attention mechanism" (Eq. 11) that is not defined or referenced in Section 3. Section 3.5 only specifies an MLP head for single-BS and a separate cross-BS attention (Eqs. 9–10) for multi-BS. The link between method and the reported single-BS gain is therefore broken on the page.
- **Overclaimed "zero-shot generalization."** The abstract claims "strong zero-shot generalization," but Section 4.5 explicitly fine-tunes downstream heads on ~100 target samples. This is few-shot, not zero-shot; no zero-shot row appears in Table 4.5.
- **No variance reporting.** Results are "averaged over 5 independent runs" (Sec. 4.1), but no std/CI/significance is reported anywhere. Several close numbers (RMSE 5.675 vs 5.822 in Table 1; MAE 0.673 vs 0.753 in Table 3; RMSE 0.972 vs 1.099) could be within noise.

### Minor
- **Cycle-adaptive masking under-specified.** Eq. 6 produces a deterministic diagonal stripe parameterized by d_final, j_0, w, but how d_final is estimated from "row-wise cross-correlation" (which rows, threshold, how the period maps to a shift, interaction with random masking) is not formalized. Fig. 3 shows both strip and grid patterns arising from the same mechanism without reconciliation. Table 3 also shows mixed wins: strip-only beats adaptive on RMSE (0.972 vs 1.099).
- **Map ablation conflates content with mechanism.** Section 4.4 varies map fidelity (3D vs 2D vs none) rather than swapping the prompt mechanism for alternative fusion methods. The text also cites "Figure 1" (a propagation diagram) for visualizing the ablation, which is a mismatched callout.
- **Internal numerical inconsistencies.** §4.5 prose says "1.580 m on WAIR-D Scenario-2" but Table 4.5 reports 1.880. §4.5 cites "0.4%" of parameters; §4.6 says "0.7%"; Table 5 implies 0.085/11.73 ≈ 0.72%.
- **"Foundation model" / "multi-modal" framing is stretched.** Pretraining uses a single ray-traced scenario (O1_3p5); the only "modalities" are CSI plus a 3D mesh consumed by a small GCN.
- **GCN formulation inconsistency.** Algorithm 1 uses separate W and U for self/neighbors; the equation in §3.4 uses the standard normalized-adjacency formulation. The two are not equivalent.
- **Few-shot fairness for LWLM.** Not explicitly stated whether LWLM receives the same ~100 target-domain fine-tuning samples as SIGMAP.

### Trivial
- Figure 5 references "AoA," "ToA," and "oss_scenario" axes not described as evaluation tasks in the text.
- The forward expression in §3.4 drops the [CLS] token that Eq. 8 reads from.

## Nice-to-Haves
- Synthetic CSI with injected periodicities to directly demonstrate the "periodic shortcut" claim.
- A true zero-shot row in Table 4.5 to substantiate the abstract.
- A k-shot adaptation curve (k = 0, 10, 100, 1000) on WAIR-D.
- A simple map-aware baseline (concatenated map encoder, classical fingerprinting with map features) to isolate the prompt mechanism's contribution.

## Removed Points
These points are flagged to be removed; treat them with caution.
- "Pretraining and fine-tuning on the same scenario" framed as a fatal flaw — partially addressed by the cross-scenario experiments in §4.5.
- Reviewer complaints about appendix-deferred details (config in B.3, CDF curves in B.5) — appendices stripped by parser.
- Strength about "physically grounded problem formulation" — standard propagation model, not a contribution.
- Strength about "multi-BS attention fusion as principled" — vanilla additive attention head; not a meaningful contribution-level strength.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add a SIGMAP (w/o map) row everywhere, and report std across 5 runs in all tables.
- Define Eq. 11 in §3 or remove it; clarify which mechanism is responsible for single-BS NLoS gains.
- Add a map-aware baseline (concatenation or cross-attention with the same 3D mesh) to isolate prompt-mechanism contribution.
- Reconcile WAIR-D number (1.580 vs 1.880) and parameter fraction (0.4% vs 0.7%); fix the Figure-1 callout in §4.4.
- Add a true zero-shot row and a k-shot curve on WAIR-D.
- Soften "zero-shot," "foundation model," and "multi-modal" framing to match the actual evidence.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>