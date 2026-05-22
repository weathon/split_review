Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper identifies a label-dependency bottleneck in semi-supervised learning (SSL) — the utility of unlabeled data is bounded by the quantity/quality of labeled data — and proposes CaPT, a framework that integrates CLIP into SSL via asymmetric-modalities co-training. CaPT jointly trains a fully fine-tuned unimodal ViT with an adapter-tuned CLIP model, using co-pseudo labels with entropy-based weighting to exchange supervision signals. Experiments across USB, ImageNet, fine-grained, and extreme low-label benchmarks show substantial gains (e.g., +21.38% on CIFAR-100 with 1 label/class over the second-best method). The method is efficient, adding only ~8% memory and ~11% time over FreeMatch.

## Strengths

- **Very large and consistent gains in extreme low-label regimes.** Table 3 shows CaPT exceeds the second-best method by 21.38% on CIFAR-100 (1 label/class) and by 4.05% on EuroSAT under the same setting. These are not marginal improvements but dramatic leaps, and the pattern holds across all 6 USB settings (Table 1), ImageNet (Table 2, +9.33% top-1 at 10 labels/class), and fine-grained datasets (Table 5).

- **Comprehensive ablation study that isolates each component's contribution.** Table 6 systematically ablates: adapter-tuning (-16.40%), bidirectional flow (-0.88%), feature augmentation (-0.57%), and entropy-based weighting (-0.87%). The CaPT-Deb variant (mirroring DebiasPL's approach without adapter-tuning) drops 12.73% on EuroSAT, directly showing that adapter-tuning is critical for mitigating CLIP's biased prior — supported by the distribution plots in Figure 5.

- **Efficient integration of CLIP without full fine-tuning overhead.** Table 4 shows CaPT adds only 8.00% memory and 11.18% training time over FreeMatch while gaining +6.23% on CIFAR-100. This is a practical advantage over naive CLIP integration approaches.

- **Clear and reproducible method description.** The three-module decomposition (UPM, MPM, PFM) is well-structured, and the paper states it adopts FreeMatch's adaptive thresholding for pseudo-label filtering. The efficiency mechanism (feature-level Mixup avoids feeding high-resolution images through CLIP's encoder) is principled.

## Weaknesses

### Major

- **Missing comparisons against other CLIP-augmented SSL pipelines.** The paper compares CaPT against 12 standard SSL methods that use only a unimodal ViT, while CaPT additionally uses CLIP. Although the ablation isolates CaPT's contribution over FreeMatch (+6.23%), the paper would be significantly strengthened by including systematic comparisons against other CLIP-in-SSL approaches such as DebiasPL (mentioned but not run on the same benchmarks) and CLIP-Adapter with SSL training. Without these, the framing "state-of-the-art SSL method" overclaims relative to the comparison set. The paper should be explicitly positioned as "a method for integrating CLIP into SSL" and benchmarked against other approaches in that category.

### Minor

- **Theorem 1.1 is disconnected from the method.** The theorem bounds pseudo-label error for a nearest-prototype classifier under a Gaussian-mixture model, showing that worse labeled data (higher bias B or smaller n_min) enlarges the bound. This is a formalization of the intuitive label-dependency observation but says nothing about why co-training with CLIP would break this dependency, nor does it inform the specific design choices of CaPT (adapter-tuning, entropy-based weighting, co-pseudo labels). The theorem serves as motivation but is not integrated into the method. Removing it or explicitly connecting it to the method (e.g., showing how CLIP reduces effective B) would improve coherence.

- **STL-10 results are not discussed despite CaPT's final model underperforming adapter-tuned CLIP alone.** On STL-10 (Table 1), CaPT's final accuracy (96.07% at 4 labels) comes from the unimodal ViT after co-training — and it trails adapter-tuned CLIP (96.86%) and CLIP zero-shot (97.18%). While this is not a contradiction (the final model is a ViT, not CLIP), the paper should explain why the co-trained ViT does not reach CLIP's standalone performance on this dataset, and discuss when practitioners should prefer CaPT's ViT output vs. using CLIP directly.

- **Attention-map evidence for the "pattern-homogeneity bottleneck" is qualitative.** Figure 3 shows 8 example images where CLIP attends to different regions than unimodal ViTs. This is illustrative but not rigorous. Quantitative analysis (e.g., CKA similarity between the two branches vs. between two ViTs with different seeds) would substantially strengthen the claim that asymmetric modalities provide complementary views beyond what random initialization of unimodal networks offers.

### Trivial

- None beyond the formatting artifacts from PDF extraction, which are not author errors.

## Nice-to-Haves

- Adding a variant where both branches are vision-only ViTs with different initializations would directly test the "pattern-homogeneity bottleneck" claim.
- Reporting statistical significance or confidence intervals on the largest gains would strengthen the results.
- A brief discussion of when CLIP's prior might be harmful (beyond the FGVCAircraft limitation noted) would improve completeness.

## Removed Points

- **Harsh critic: "Unfair experimental comparison invalidates the claimed SOTA"** — Demoted from Fatal to Major. The comparison against standard SSL methods is legitimate because the final CaPT model uses the same architecture (ViT) as the baselines; the ablation shows CaPT adds +6.23% over FreeMatch alone. However, the paper should benchmark against other CLIP-in-SSL methods. The claim "unfair and uninterpretable" overstates the problem.

- **Harsh critic: "STL-10 results directly contradict the method's advertised advantage"** — Restructured and reduced to Minor. CaPT's final model is a pure-vision ViT, not CLIP. The relevant comparison is CaPT-ViT (96.07%) vs. RegMixMatch-ViT (89.89%) — a +6.18% improvement. The fact that CLIP zero-shot achieves 97.18% is not a contradiction because CaPT's output model is architecturally different. However, the paper should discuss this and clarify when to use CaPT's ViT vs. CLIP directly.

- **Harsh critic: "Missing threshold specification"** — Removed. The paper clearly states "We adopt the adaptive threshold strategy from FreeMatch to filter pseudo labels, as in RegMixMatch" (Section 4.1). This is sufficient for reproducibility.

- **Harsh critic: "Standard deviations suspiciously low (0.05 on STL-10)"** — Removed. Using fixed seeds with 3 runs can produce low variance, especially when the method is stable. This is not inherently suspicious.

- **Strength Finder: Several generic strengths** (e.g., "consistent superiority across diverse benchmarks") — Merged into the main strengths above or demoted here as they restate results already covered.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add systematic comparisons against DebiasPL and CLIP-Adapter SSL variants** on the same benchmarks. This directly addresses the central evaluation concern.
2. **Discuss the STL-10 result explicitly**: explain why the co-trained ViT plateaus below adapter-tuned CLIP, and provide practical guidance on which output model to deploy.
3. **Either remove Theorem 1.1 or connect it to the method** by showing how CLIP reduces the effective bias B in the bound, or relegate it to the appendix and cite it purely as motivation.
4. **Add quantitative representational similarity analysis** (e.g., CKA) between the UPM and MPM branches to substantiate the "pattern-homogeneity" claim beyond qualitative attention maps.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Queried for semi-supervised learning with CLIP/vision-language co-training across three bands:
- `score < 3.5`: LLM2CLIP (3.00, Reject) — Much weaker paper, poor writing, overclaimed results. CaPT is clearly stronger.
- `score ∈ (3.5, 7.5)`: SemiCLIP (5.80, Accept), CLIPSelector (4.50, Reject), GPS-SSL (5.33, Reject), DIPS (5.00, Reject) — CaPT sits comfortably in the upper half of this band, above GPS-SSL and DIPS.
- `score > 7.5`: Papers at 7.5–8.0 are methodologically stronger and address their evaluation gaps more thoroughly. CaPT does not reach this level.

**Round 2 (Narrowing):** Pulled anchors inside the 4.5–7.5 and 6.0–8.0 ranges for finer comparison:
- SemiCLIP (5.80, Accept): Most similar topic (CLIP + semi-supervised learning), similar "unfair comparison" concern raised by reviewers. CaPT has larger empirical gains, more thorough ablations, and a clearer method. **CaPT is stronger → at or above 5.80.**
- GPS-SSL (5.33, Reject): Uses prior knowledge in SSL, similar fairness concern. Reviewers found marginal improvements and limited novelty. CaPT's gains are dramatically larger and its experiments more comprehensive. **CaPT is substantially stronger → above 5.33.**
- DIPS (5.00, Reject): Focused on data-centric improvements to pseudo-labeling. Less relevant to CaPT's core contribution. **CaPT is stronger → above 5.00.**

**Final bracket:** 5.5–6.5. CaPT is above SemiCLIP (5.80) but below the 7.0+ papers that have cleaner evaluation designs. Score positioned at **6.0**.

### Scoring Summary

**Originality:** 6/10 — The asymmetric-modalities co-training framework is novel and well-motivated, though the individual components (co-training, adapter-tuning, entropy weighting) are individually known.

**Importance of research question:** 8/10 — Label dependency in SSL is a well-recognized problem, and the extreme low-label regime is practically important.

**Claims supported:** 6/10 — Main empirical claims are well-supported by experiments and ablation. However, the "state-of-the-art" framing overclaims relative to the comparison set (missing CLIP-augmented SSL baselines). Theoretical claim is loosely connected.

**Soundness of experiments:** 7/10 — Comprehensive benchmarks, thorough ablations, honest about limitations (FGVCAircraft). Missing CLIP-in-SSL baselines is the main gap.

**Clarity of writing:** 8/10 — Clear structure, well-described method, effective figures.

**Value to the community:** 7/10 — The framework is portable and the code is provided. Results in extreme low-label settings are practically significant.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>