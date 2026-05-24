Now I have a clear picture. Let me compile the final review.

---

## Summary

This paper identifies, formalizes, and mitigates a failure mode in identity-consistent image generation called the *copy-paste artifact* — the tendency of models to rigidly replicate the reference face rather than synthesizing the identity under natural variation. The authors contribute (1) **MultiID-2M**, a 500K-image paired multi-person dataset with hundreds of reference images per identity; (2) **MultiID-Bench**, a benchmark that measures copy-paste via a geodesic-distance metric (ℳ_CP) and prioritizes ground-truth similarity (Sim_GT) over reference similarity; and (3) **WithAnyone**, a FLUX-based model with a GT-aligned ID loss, an ID contrastive loss with extended negatives, and a paired-tuning phase that together break the trade-off between identity fidelity and copy-paste. Quantitative results across 12+ baselines on single- and multi-person settings show WithAnyone achieves the highest Sim_GT while maintaining the lowest copy-paste artifact levels among face-customization methods.

## Strengths

- **Novel problem formalization with a concrete, measurable metric**: The paper defines copy-paste artifacts as a distinct failure mode, not merely low diversity, and introduces ℳ_CP (Eq. 2) — an angular-distance-based metric normalized by the reference-to-GT distance — that quantifies the phenomenon. Figure 5 demonstrates its diagnostic value: all baselines fall along a trade-off curve between Sim_GT and copy-paste, while WithAnyone breaks away from it.

- **Large-scale paired dataset (MultiID-2M) that enables discriminative training**: The dataset construction pipeline (Section 3) is well-documented and yields ~500K group photos with paired references across ~3K identities (~400 references per identity). This directly enables the ID contrastive loss with extended negatives (4,096 negatives, Section 6.3) — a training signal unavailable in prior reconstruction-only setups. The ablation (Table 3) shows that removing extended negatives drops Sim_GT from 0.405 to 0.368 and nearly collapses the copy-paste reduction.

- **GT-aligned ID loss that works robustly across the full noise schedule**: By aligning generated faces using GT landmarks rather than extracting landmarks from noisy latents (Eq. 4), the loss provides stable identity supervision at all timesteps. Figure 7 shows consistently lower ID loss and more informative gradients compared to prediction-aligned alternatives. Ablating this component (Table 3, w/o GT-Align) reduces Sim_GT by 0.02 and increases CP by 0.014.

- **Paired-tuning phase that explicitly breaks the reconstruction shortcut**: Phase 3 replaces 50% of training samples with pairs where reference and target are *different* images of the same identity (Section 5.2). Table 3 shows that removing Phase 3 increases CP from 0.161 to 0.239 while Sim_GT remains nearly unchanged — direct evidence that this phase, not some other factor, suppresses copying.

- **Comprehensive quantitative evaluation with a well-designed benchmark**: MultiID-Bench uses Sim_GT as the primary metric rather than Sim_Ref, explicitly penalizing models that copy the reference when natural variation is expected. The evaluation covers 12+ baselines across both single-person (Table 1) and multi-person (Table 2) settings, with CP rankings thresholded by Sim_GT (>0.40 or >0.35) to avoid interpreting low CP from failed generations as success. The scatter-plot analysis (Fig. 5) makes the trade-off visually undeniable.

- **Thorough ablation study**: Table 3 isolates the contributions of paired tuning, GT-aligned ID loss, extended negatives, and dataset quality (FFHQ-only baseline). Each component removal produces a measurable degradation that aligns with the paper's mechanistic claims.

## Weaknesses

### Fatal

None.

### Major

None. The quantitative results stand on their own against the most competitive baselines.

### Minor

- **User study does not compare against the strongest ID-preserving baselines**: The study (Fig. 8, Section 6.3) pits WithAnyone (labeled "Cure") against UNO, OmniGen, iDetch, and Uniformal — general-purpose models that the paper's own Table 1 shows have substantially lower Sim_GT (UNO: 0.304, OmniGen: 0.398) than the strong face-customization baselines (InstantID: 0.464, PuLID: 0.452). Finding that a dedicated face-customization model outperforms generic editors on identity similarity is unsurprising and provides little incremental evidence for the central claim. The abstract's statement that "user studies further validate" is therefore only weakly supported. However, the quantitative evaluation (Tables 1–2, Fig. 5) already compares against all relevant baselines and carries the paper's evidentiary weight; the user study is supplementary.

- **Copy-paste metric behavior at the low-similarity boundary is under-discussed**: The paper correctly thresholds CP rankings by Sim_GT (Tables 1–2), acknowledging that low CP in isolation can be misleading. But the paper does not explicitly caution readers about this coupling. The ablation row "w/o Ext. Neg." (Table 3: Sim_GT=0.368, CP=0.074) illustrates the issue concretely — the low CP here reflects a failure to capture identity at all, not a success — and the paper misses an opportunity to discuss this case directly.

- **User study has a confusing label and lacks statistical rigor**: The method is labeled "Cure" in Fig. 8 rather than "WithAnyone," which is never explained. The study uses only 10 participants, reports no error bars or statistical tests, and states a "moderate positive correlation" between the CP metric and human judgments without providing a correlation coefficient (deferred to stripped Appendix H). These reporting gaps make the study unverifiable from the main paper alone.

### Trivial

- Figure 5's y-axis is labeled "Copy-Paste (y-axis descending order)" — the phrase "descending order" is confusing. It appears to mean lower CP is better (i.e., the axis shows CP ranked from high to low), but the phrasing could mislead readers into thinking the axis values themselves are inverted.

## Nice-to-Haves

- A controlled experiment systematically varying the degree of copy-paste (e.g., by interpolating between reference and GT) would strengthen the validation of ℳ_CP as a metric.
- Discussion of whether the GT-aligned ID loss constrains the model's ability to reposition the subject spatially (since it assumes the generated face appears where the GT face is).
- Analysis of whether the residual CP values in multi-person settings (0.161–0.171, Table 2) remain perceptible to human observers.

## Removed Points

These points were flagged for removal — treat them with caution:

- **Harsh Critic: "Dataset statistics missing — number of identities in paired subset, diversity statistics"**: The main paper states ~3K identities and ~500K paired images. More detailed statistics are likely in Appendix C (stripped by the parser). Not verifiable as a weakness from the main paper alone; standard practice to put such breakdowns in the appendix. REMOVED.

- **Harsh Critic: "Multi-person CP residue perceptibility should be discussed"**: This is a reasonable suggestion but belongs in Nice-to-Haves rather than as a standalone weakness. MOVED.

- **Harsh Critic: "CP metric depends on reliable face detection/embedding pipeline (ArcFace)"**: True of virtually all face-similarity-based metrics in the literature. Not specific to this paper. REMOVED as generic.

- **Harsh Critic: "Architecture details (SigLIP branch, negative pool, sampling) only sketched"**: These are implementation details standard to defer to the appendix. The main paper states the key number (4,096 negatives) and the architecture is diagrammed in Fig. 4. REMOVED.

- **Harsh Critic: "User study should be replaced or substantially redesigned"**: The quantitative results already address the comparison against strong baselines. The user study is supplementary; asking for a complete redesign is disproportionate. The actual weakness — misaligned baselines — is already captured in Minor. MOVED framing to Nice-to-Haves.

- **Strength Finder: "User study validates CP metric aligns with human perception"**: The harsh critic correctly identifies that the study's baselines are misaligned with the core comparison and the correlation claim is numerically unsupported. The user study provides only weak supplementary evidence, not a core strength. REMOVED as a standalone strength.

- **Strength Finder: Generic "problem is important" framing**: REMOVED as superficial.

## Novel Insights

The most genuinely novel insight emerging from this work is the identification that face-similarity metrics (Sim_Ref) create a *perverse incentive* in identity-consistent generation: models that trivially copy the reference image maximize the evaluation score. The paper diagnoses this not as a training artifact but as an evaluation failure, and solves it by re-anchoring evaluation to ground-truth similarity (Sim_GT) while quantifying the copying tendency directly via ℳ_CP. This reframing — that the problem is as much about *what we measure* as *what we train* — has implications beyond this specific domain for any generative task where metrics reward memorization over generalization.

## Suggestions

- Relabel "Cure" as "WithAnyone" in Fig. 8 and add error bars or confidence intervals to the user study rankings. Report the correlation coefficient between the CP metric and human CP judgments explicitly in the main text rather than deferring it entirely to the appendix.
- Add a brief sentence in Section 4 explicitly cautioning that low CP in isolation does not indicate good generation — it must be interpreted jointly with sufficient Sim_GT, exactly as the ranking protocol already enforces.
- In the discussion of multi-person results, briefly note whether the CP levels of 0.16–0.17 are perceptually meaningful or merely residual measurement noise.

## Score and Decision

**Round 1 bracket**: The paper was placed between 6.5 and 8.0 based on comparisons with CopyMark (5.50, weaker), UIFace (6.00, weaker), and CADS (8.00, stronger).

**Round 2 narrowing**: Compared against MGFR (7.33) and One-Prompt-One-Story (7.40). WithAnyone has stronger and more comprehensive contributions than both: a larger dataset (500K vs 23K in MGFR), a novel benchmark, more baselines (12+), stronger ablations, and a well-motivated training recipe. The user study is a genuine but minor weakness that does not threaten the core quantitative evidence.

**Anchor summary**:
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| CopyMark (NWvsm2vXAM) | 3.00 | 1 | Much weaker — narrow benchmark contribution |
| ID-Booth (NWvsm2VxAM) | 3.00 | 1 | Much weaker — limited evaluation |
| DiffDeID (Bz9wjvToCS) | 4.40 | 1 | Weaker — smaller scale, less comprehensive |
| MemBench (Qg0gtNkXIb) | 5.25 | 1 | Weaker — benchmark only, no model |
| CopyMark (EE2tIwKhSW) | 5.50 | 1 | Weaker — benchmark only, limited depth |
| UIFace (riieAeQBJm) | 6.00 | 1,2 | Weaker — less comprehensive, smaller contributions |
| MS-Diffusion (PJqP0wyQek) | 6.00 | 2 | Weaker — narrower scope |
| Vec2Face (RoN6NnHjn4) | 6.00 | 2 | Weaker — face dataset only, no benchmark |
| InstantPortrait (ZkFMe3OPfw) | 6.67 | 2 | Weaker — more focused, smaller scope |
| MGFR (m9RNBZewW2) | 7.33 | 2 | Comparable profile but WithAnyone is stronger in scale and comprehensiveness |
| One-Prompt-One-Story (cD1kl2QKv1) | 7.40 | 2 | Comparable — WithAnyone has larger-scale contributions but less theoretical novelty |
| InverseBench (U3PBITXNG6) | 7.50 | 2 | Similar — both have strong benchmarks, WithAnyone adds a model |
| CADS (zMoNrajk2X) | 8.00 | 1 | Stronger — more elegant, theoretically grounded, broader applicability |
| REPA (DJSZGGZYVi) | 9.00 | 1 | Stronger — more fundamental contribution |
| Consistency Models (LyJi5ugyJx) | 9.20 | 1 | Stronger — foundational training contribution |
| IC-Light (u1cQYxRI1H) | 10.00 | 1 | Much stronger |

**Final assessment**: WithAnyone is a strong, self-contained contribution with a well-motivated problem, a large-scale dataset, a principled benchmark, and a model that demonstrably breaks the fidelity–copy-paste trade-off. The quantitative evaluation against 12+ baselines is thorough, and the ablation study convincingly isolates each component's contribution. The user study is the main weak point — it uses misaligned baselines and is thinly reported — but this does not undermine the core quantitative evidence. The paper sits above MGFR (7.33) and One-Prompt-One-Story (7.40) due to greater contribution scale and evaluation depth, but below CADS (8.00) which offers stronger theoretical grounding and broader applicability.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>