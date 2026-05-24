Now I have a thorough understanding of the paper and the relevant calibration anchors. Let me write the final review.

## Summary

The paper identifies a core limitation of semi-supervised learning (SSL): pseudo-label quality degrades with the quantity and quality of labeled data, creating a self-reinforcing dependency. To address this, it proposes CaPT, an asymmetric-modalities co-training framework that integrates CLIP into SSL through three modules — a fine-tuned unimodal network (UPM), an adapter-tuned multimodal CLIP (MPM), and a prediction fusion module (PFM) that combines their outputs via entropy-based weighting. The key insight is that CLIP's independently pre-trained representations provide a reliable prior that is not subject to SSL's label dependency, and that the asymmetric vision–language modalities mitigate the pattern-homogeneity bottleneck found in standard vision-only co-training. CaPT achieves state-of-the-art results across all six USB benchmark settings, with particularly dramatic gains under extreme label scarcity (e.g., +21.38% on CIFAR-100 with one label per class).

## Strengths

- **State-of-the-art empirical results across diverse benchmarks.** CaPT outperforms 12 prior SSL methods on all six evaluated settings in the USB benchmark (Table 1), on ImageNet (Table 2), and across fine-grained datasets (Table 5). The consistency of the gains across dataset types and label budgets is impressive.

- **Dramatic improvements in extreme low-label regimes directly validate the central claim.** On CIFAR-100 with one label per class, CaPT achieves 82.51% vs. 60.49% for the second-best method — a 21.38-point improvement (Table 3). This gap is large enough that it cannot be explained away by minor experimental confounds and directly demonstrates reduced label dependency.

- **The asymmetric-modalities co-training design is well-motivated and novel.** The paper identifies that two vision-only networks (ViT(θ₁) and ViT(θ₂)) produce similar attention patterns even with different initializations, limiting the information exchange in standard co-training (Figure 3). CLIP's text-grounded representations naturally diverge from purely visual ones, providing a principled reason for the framework's advantage over prior co-training methods like CLS.

- **Practical efficiency demonstrated quantitatively.** CaPT adds only 8.00% memory overhead and 11.18% additional per-iteration time compared to FreeMatch while substantially outperforming the previous state-of-the-art RegMixMatch in both accuracy and resource consumption (Table 4).

- **Ablation study (Table 6) validates the key design choices.** The comparison between CaPT, CaPT-Deb (no adapter tuning, no feedback), CaPT-Uni (unidirectional flow), "only UPM," and "only MPM" decomposes the contributions. The gap between CaPT-Deb (81.03) and CaPT (84.83) on CIFAR-100 confirms that the full co-training mechanism — including adapter-tuning and bidirectional flow — provides meaningful benefits beyond simply having CLIP available.

- **Adapter-tuning analysis (Figure 5) provides concrete evidence of bias correction.** The empirical class distribution from raw CLIP is highly skewed, while adapter-tuned CLIP produces a markedly more uniform distribution, confirming that the lightweight fine-tuning step serves its intended purpose.

## Weaknesses

### Major

None.

### Minor

- **Theorem 1.1 is too loose to provide meaningful guarantees for real image data.** The bound contains a multiplicative factor of \(2^{d/2}\) and an additive term in \(\varepsilon_n\) that grows as \(\sqrt{d\log 2}\). For image data with \(d \ge 3072\) (e.g., CIFAR-100), the bound becomes vacuous (>> 1) unless the effective margin \(g/2 - r\) exceeds \(\sim 65\sigma\), an unrealistic condition. The bound's structure still captures the *qualitative* dependency on label quantity and quality, but the paper overclaims in presenting this as a formal theoretical proof of label dependency. The empirical motivation in Figure 1 is sufficient on its own.

- **The evaluation lacks a direct "CLIP simple fusion" baseline.** The critic's concern is valid: the paper does not include the simplest integration of CLIP into the SSL pipeline — e.g., a weighted average of UPM and frozen/adapter-tuned CLIP logits at test time, or training UPM with CLIP's predictions as a fixed regularizer. While CaPT-Deb (81.03 on CIFAR-100) and CaPT-Uni (83.95) partially address this, neither is exactly a "post-hoc fusion at test time" baseline. Adding this would cleanly isolate whether the gains come from the co-training framework itself or merely from having CLIP's predictions available in any form. Given that CaPT-Deb already underperforms CaPT by 3.80%, the missing baseline is a gap in thoroughness rather than a fatal omission, but it should be filled.

- **The pattern-homogeneity bottleneck claim relies solely on qualitative attention maps.** Figure 3 shows attention maps for 8 images, but the paper provides no quantitative metric (e.g., CKA similarity, prediction agreement rate, or disagreement on misclassified samples) to measure the divergence between the two co-trained branches over the course of training. A quantitative analysis would substantially strengthen this central claim.

- **FGVC-Aircraft failure case is noted but not analyzed.** The paper honestly acknowledges that CaPT underperforms baselines on FGVC-Aircraft (Table 5: 50.12 vs. 51.43 for FreeMatch with 5 labels). However, there is no analysis of *why* CLIP's prior is unhelpful here — e.g., a plot of the entropy weights \(\Gamma^a, \Gamma^b\) for this dataset during training, or an examination of whether the fusion mechanism correctly downweights CLIP's predictions when they are harmful. This analysis would provide useful insight into the method's failure modes.

- **Dynamic weight (\(\Gamma^a, \Gamma^b\)) evolution during training is not visualized.** The paper claims that CLIP dominates early training and the unimodal network takes over later, but no plot or analysis confirms this. A visualization of the entropy weights over training iterations (especially contrasting a success case like Flowers102 with the failure case FGVC-Aircraft) would support the claimed transition and help users understand when the framework is likely to succeed.

### Trivial

- **Framing slightly overstates the contribution.** The paper says it "breaks" the label dependency in SSL, but the solution works by introducing an *external* model (CLIP) trained independently of the labeled set. The SSL branch itself remains label-dependent; the framework circumvents the bottleneck rather than eliminating it from SSL. Phrasing like "mitigates" or "reduces" would be more precise, though this does not diminish the practical value of the approach.

## Nice-to-Haves

- A direct end-to-end comparison with DebiasPL under identical backbones in the main results tables (it is only referenced in the ablation as CaPT-Deb).
- Results with scratch-trained WideResNet backbones (currently the UPM uses a pre-trained ViT, as standard in USB) to test whether the benefits generalize to settings without pre-trained weights.
- Analysis of how CaPT's gains distribute across easy vs. hard samples, or across different confidence bins of the UPM's predictions.

## Removed Points

- *"The theoretical bound is a core claimed contribution that is unsupported."* — The bound is loose for high-dimensional data, but it still captures the correct qualitative dependencies. The paper's main contribution is the empirical framework; the theory is supplementary. Demoted from the critic's "fatal" assessment to Minor.
- *"The missing baseline makes it impossible to assign credit to CaPT vs. CLIP."* — The ablation study (CaPT-Deb, CaPT-Uni, only UPM, only MPM) does decompose the contributions. The missing "simple fusion" baseline would strengthen the paper but its absence does not invalidate the central claims. Demoted from "critical" to Minor.
- *"Framing overstates the contribution"* — Kept as Trivial.
- *"Missing DebiasPL comparison"* — Moved to Nice-to-Haves, as CaPT-Deb in Table 6 partially addresses this.
- *"Backbone sensitivity"* — Moved to Nice-to-Haves; the USB benchmark standardizes on pre-trained ViTs.
- *"Reproducibility concerns about undisclosed hyperparameters"* — Removed; the paper provides detailed configuration in Appendix F and source code in supplementary materials.
- *"Missing related works"* — Removed per instructions (cannot verify external existence).
- *"Pure formatting/style nitpicks"* — Removed per instructions.
- Strength about "theoretical proof" — Removed; the bound is too loose for this to be considered a genuine strength.

## Novel Insights

The most interesting observation that emerges from the reviews is that **the paper's central tension — using an external prior to "break" label dependency — actually mirrors a broader question in the field**: is the path forward for SSL to make SSL itself more robust, or to strategically route difficult cases to foundation models? CaPT effectively sidesteps this question by showing that a lightweight, pragmatically engineered fusion between a standard SSL model and a VLM can deliver the benefits of both without requiring fundamental advances in SSL theory. The FGVC-Aircraft failure case (5 labels) is particularly informative because it reveals a clean failure mode: when CLIP's prior is both weak *and* the labeled data is too sparse to calibrate the fusion weights, the framework can underperform a simple SSL baseline. This provides a concrete boundary condition for when VLM-assisted SSL works and when it does not, which is more useful than the across-the-board improvements often reported in SSL papers.

## Suggestions

1. **Add a simple post-hoc fusion baseline.** After training only-UPM, evaluate by averaging UPM logits with frozen/adapter-tuned CLIP logits at test time (with and without learned weighting). This is the minimal control needed to attribute the gains of the full CaPT framework.
2. **Replace or relegate Theorem 1.1.** Either derive a bound with a data-dependent complexity measure (e.g., effective dimension, margin) that avoids the exponential dependence on raw pixel dimension, or reframe it as an informal scaling-law analysis and remove the formal theorem. The empirical motivation (Figure 1) already makes the point convincingly.
3. **Add quantitative analysis of branch disagreement.** Report CKA similarity, prediction agreement, or exact/inexact agreement rates between UPM and MPM over the course of training. This would substantiate the pattern-homogeneity bottleneck claim beyond the qualitative attention maps.
4. **Analyze the FGVC-Aircraft failure case.** Visualize entropy weights \(\Gamma^a, \Gamma^b\) over training for this dataset and examine whether CLIP's predictions are correctly downweighted. This would turn a known limitation into a source of insight about the method's operating regime.
5. **Plot \(\Gamma^a, \Gamma^b\) over training iterations** for a representative success case (e.g., CIFAR-100) to visually confirm the claimed transition from CLIP-dominated early training to UPM-dominated later training.

## Score and Decision

### Calibration Summary

**Round 1 — Bracketing** (all on "semi-supervised learning with CLIP or vision-language model prior"):

| Anchor | Avg Score | Round | Comparison to CaPT |
|--------|-----------|-------|-------------------|
| FwkYeLovHk | 3.33 | 1 | Much weaker; superficial use of CLIP |
| HfJxXbXlYJ | 3.00 | 1 | Much weaker; different task (LLM2CLIP) |
| bESxQeXTlo | 3.00 | 1 | Much weaker; different task (anomaly detection) |
| KBSHR4h8XV | 3.33 | 1 | Much weaker; different area (robotics VLA) |
| ZaudLwn0Hm | 2.50 | 1 | Much weaker; few-shot adaptation |
| 97D725GJtQ (SemiCLIP) | 5.80 | 1 | Weaker; 1–6% gains vs CaPT's up to 21%; less novel method |
| 1rgMkDWfYV | 4.50 | 1 | Weaker; noisy labels, not SSL |
| Rc3RP9OoEJ (InCPL) | 5.00 | 1 | Different task (test-time prompt tuning) |
| ptCIlV24YZ | 5.80 | 1 | Different task (clustering) |
| G9Ea7mlqGO | 3.80 | 1 | Different task (continual learning) |
| 5Ca9sSzuDp | 8.00 | 1 | Stronger; CLIP interpretability, different genre |
| WyEdX2R4er | 8.00 | 1 | Stronger; VLM analysis, different genre |

**Initial bracket (Round 1):** 5.5 – 7.5. The paper is clearly stronger than the 3–4 point papers and SemiCLIP (5.80), but is not at the level of 8-point analytical papers about CLIP internals.

**Round 2 — Narrowing:**

| Anchor | Avg Score | Round | Comparison to CaPT |
|--------|-----------|-------|-------------------|
| 5BXWhVbHAK (co-training modalities) | 6.33 | 2 | Similar methodological novelty; CaPT has stronger empirical results |
| LuVulfPgZN | 6.00 | 2 | Different framing (out-of-modal generalization) |
| c0PnZCNY2N (Robult) | 4.75 | 2 | Weaker; multimodal SSL with missing modalities |
| Pe3AxLq6Wf (CoMM) | 6.25 | 2 | Different focus (contrastive multimodal learning) |
| EjJD16oaly (GTR) | 4.50 | 2 | Weaker; standard SSL thresholding |
| jdynlBj3b0 | 6.25 | 2 | Different area (multi-label learning) |
| Bo6GpQ3B9a (OOD unlabeled) | 7.00 | 2 | Stronger theory, weaker experiments; different approach |
| tIBAOcAvn4 | 7.50 | 2 | Different area (adversarial attacks) |
| Fk5IzauJ7F | 8.00 | 2 | Different area (partial-label learning) |
| jlEjB8MVGa | 6.50 | 2 | Different area (OOD detection) |
| HvkXPQhQvv (SSME) | 6.00 | 2 | Different area (model evaluation) |
| TjhUtloBZU | 6.25 | 2 | Different area (label noise in pre-training) |
| PhnGhO4VfF | 5.67 | 2 | Different area (pretraining granularity) |
| m50eKHCttz | 7.25 | 2 | Stronger but different area (knowledge transfer) |

**Final bracket:** After round 2, the most relevant comparisons are SemiCLIP (5.80), the co-training modalities paper (6.33), and the OOD unlabeled data paper (7.00). CaPT is clearly stronger than SemiCLIP (larger gains, more novel method) and at least as strong as the co-training paper (better results, similar methodological contribution). It is not as strong as the 7+ papers, which tend to have either stronger theoretical backing or fewer methodological weaknesses. The paper's minor weaknesses (vacuous bound, missing fusion baseline, qualitative-only bottleneck analysis) prevent it from reaching the 7+ tier.

### Final Score

**Score: 6.5**

The paper makes a genuine practical contribution with strong empirical evidence. The asymmetric-modalities co-training framework is well-motivated and the results are impressive across a broad range of settings. The weaknesses are real but minor — they concern presentation (vacuous bound), thoroughness (missing simple fusion baseline, qualitative-only bottleneck analysis), and analysis depth (FGVC failure case, dynamic weight visualization) — none of which threaten the core empirical finding that CaPT substantially improves SSL under label scarcity. The paper is a solid accept.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>