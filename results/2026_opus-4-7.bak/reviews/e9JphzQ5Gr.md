## Summary
CaPT is an asymmetric-modalities co-training framework for SSL: a fully fine-tuned unimodal vision network is paired with an adapter-tuned CLIP, and their pseudo labels are fused via entropy-based weighting. The paper motivates the design with an analytic nearest-prototype error bound (Theorem 1.1) showing how SSL's reliance on labeled-data quality/quantity grows under scarcity, and reports large gains in extreme low-label regimes (e.g., +21.38% over RegMixMatch on CIFAR-100 at 1 label/class).

## Strengths
- **Large empirical gains in extreme label scarcity (Table 3):** 82.51% vs 61.13/60.49% on CIFAR-100 at 1 label/class; competitor methods collapse 17–20 points 2→1, while CaPT only loses ~2 points. Concrete evidence for the "label-decoupling" claim.
- **Thorough ablations (Table 6)** isolate each component: CaPT-Ada (−16.4%), CaPT-Deb (−12.7% on EuroSAT), CaPT-Uni (−0.9/−1.5%), only-UPM, only-MPM, w/o feature aug, equal-weights — each design choice carries real weight.
- **Reasonable efficiency profile (Table 4):** +8% memory and +11% wall time over FreeMatch is modest given the CLIP branch; dominates RegMixMatch on all three axes.
- **Asymmetric-modalities motivation is supported** by Figure 3 attention patterns and by the CaPT-Uni / only-MPM ablations both regressing, consistent with the bidirectional-co-training story.

## Weaknesses

### Fatal
None.

### Major
- **Adapter-tuned CLIP outperforms CaPT on STL-10 (Table 1: 96.86/97.15 vs 96.07/96.34).** The very baseline introduced in the paper undermines the headline "CaPT > everything" framing on the dataset where CLIP is already competent. Combined with Table 5 (CaPT trails FreeMatch on FGVCAircraft: 50.12 vs 51.43 at 5/cls; 64.33 vs 66.21 at 10/cls), the picture is "CaPT helps mostly where CLIP is strong-but-not-saturated." The paper acknowledges the rows but does not engage with the implication that on CLIP-saturating datasets the co-training mechanism adds nothing over PEFT-tuning CLIP on labels.
- **Comparison fairness in Tables 1–3.** Main-results SSL baselines are all CLIP-free while CaPT uses CLIP. The natural CLIP-using competitor, DebiasPL, appears only as the CaPT-Deb ablation row, not as the original DebiasPL system run head-to-head at the same label budgets. The most informative central experiment — a bake-off among CLIP-integration recipes (zero-shot CLIP, adapter-tuned CLIP, DebiasPL, CaPT) — is partly avoided, leaving open how much of the gain is the co-training mechanism vs. simply having CLIP.
- **Theorem 1.1 is about nearest-prototype classification, not SSL dynamics.** Eq. 1 bounds the error of a static nearest-prototype classifier under a Gaussian mixture in terms of prototype bias B and n_min. Section 1 then uses it to assert a "fundamental limitation of existing SSL methods," but consistency regularization, adaptive thresholding and pseudo-label propagation are not modeled. The bound describes *initial* pseudo-label noise, which is uncontested. As a contribution it is overclaimed; as motivation it is acceptable.

### Minor
- Table 1 reports variance, but Tables 2, 3, 5 do not. For 1-shot settings — where seed variance is largest — the absence of error bars slightly weakens the headline +21.38% claim.
- The co-pseudo label (Eq. 13) mixes one-hot pseudo labels with continuous weights Γ^a, Γ^b, giving a 2-mode mass distribution rather than a soft posterior; using soft predictions directly is not ablated.
- §4.4 frames fine-grained datasets as ruling out CLIP corpus overlap, but Flowers102/StanfordCars/SUN397/DTD are reasonably represented in CLIP's training; SVHN is the only clean out-of-domain test.
- The "label dependency" framing as a first contribution overstates novelty — that SSL degrades with fewer/worse labels is the explicit motivation of the extremely-scarce-labels line of work since FixMatch.

### Trivial
None.

## Nice-to-Haves
- Quantify branch disagreement (CKA / prediction-disagreement curves) over training to substantiate the "pattern-homogeneity bottleneck" claim beyond Figure 3's qualitative attention maps.
- Report what the vision branch achieves without CLIP fusion at the same compute, isolating the CLIP contribution from the co-training mechanism.
- Sensitivity of entropy-weighting (Eq. 11–12) to batch size and to early-training "one branch confidently wrong" pathologies.

## Removed Points
These points are flagged to be removed, treat them with caution.
- *Harsh critic: "CLIP brings hundreds of millions of image-text pairs — comparison is structurally unfair."* The paper's stated contribution is integrating CLIP into SSL; insisting on CLIP-free fairness rewrites the scope. The legitimate version (need head-to-head against DebiasPL/Adapter-tuned CLIP at matched budgets) is retained as the Major comparison point.
- *Strength Finder: Theorem 1.1 is a "non-trivial analytic model that quantifies why unlabeled data utility collapses."* Overstated — it is a standard nearest-prototype Gaussian-mixture tail bound and does not analyze SSL dynamics. Conflicts with the kept Major weakness on this theorem.
- *Strength Finder: ImageNet "scalability"* — Table 2 gives no variance and the gap shrinks markedly at 100 labels/class (74.21 vs 73.66); kept as context, not a standalone strength.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Add CaPT vs (adapter-tuned CLIP, DebiasPL, CLIP-Adapter+consistency on unlabeled data) at matched label budgets directly in the main results tables.
- Discuss the STL-10 inversion (Adapter-tuned CLIP > CaPT) and FGVCAircraft regression in the main text; quantify when the co-training adds value vs. when PEFT alone suffices.
- Either reposition Theorem 1.1 as a motivating sanity-check or extend it to iterated pseudo-labeling dynamics where the "label dependency" is actually non-trivial.
- Add error bars to Tables 3 and 5 for 1- and 2-shot settings.

## Score and Decision

**Anchors retrieved.**

Round 1 (bracketing):
- `FwkYeLovHk` (3.33, Reject) — weak-to-strong CLIP; topically related, much weaker.
- `E0UsEIRBQ8` (3.00, Reject) — semi-sup underwater detection; off topic.
- `xRi8sKo4XI` (3.00, Reject) — unsupervised prompt learning LLM; off topic.
- `HfJxXbXlYJ` (3.00, Reject) — LLM2CLIP; off topic.
- `97D725GJtQ` (5.80, Accept) — **SemiCLIP**, semi-sup CLIP training; closest analogue. Read in full.
- `1rgMkDWfYV` (4.50, Reject) — CLIP for label noise cleaning; tangential.
- `baNW94qdsU` (4.00, Reject) — self-training for VLM alignment; tangential.
- `xrazpGhJ10` (5.50, Reject) — SemCLIP retrieval stability; tangential.
- `uAFHCZRmXk`, `WyEdX2R4er`, `25kAzqzTrz`, `3i13Gev2hV` (all 8.0, Accept) — analytical/theory papers, very different scope.

Round-1 bracket: **5.0–6.0**, anchored by SemiCLIP at 5.80.

Round 2 (narrowing 4.5–7.0):
- `AEi2wyAMyb` (5.33, Reject) — BOPL bi-level pseudo-labeling.
- `eSO9quCgmz` (5.00, Reject) — DIPS data-centric pseudo-labeling, also focused on labeled-data quality.
- `WPsnH6875d` (6.00, Accept) — re-evaluating unseen-class SSL.
- `GtnNhtuVrc` (5.25, Reject) — semi-sup segmentation.
- `rkAqvDnnmO` (5.25, Reject), `88hh5GtLBJ` (5.40, Reject), `1L9vdc7BB5` (5.50, Reject), `KNtcoAM5Gy` (5.50, Reject) — adapter/prompt-tuning VLM papers.

Comparison: CaPT has stronger empirical numbers than DIPS or BOPL but a real comparison-fairness puncture (Adapter-tuned CLIP > CaPT on STL-10) and an overclaimed theorem — placing it slightly below the SemiCLIP/WPsnH (5.8–6.0) accept cluster but above the 5.0 rejects. Landing point: between DIPS (5.0) and SemiCLIP (5.8), closer to the borderline.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>