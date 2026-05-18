Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes OSA (One-step Anti-Noise), a noise mitigation method that uses a pretrained multimodal model (CLIP/ALIGN) as an estimator to compute cosine similarity scores between input pairs, then applies a scoring function to convert these similarities into learning weights. The core idea is that the cosine-similarity distribution of clean and noisy pairs exhibits a stable intersection boundary in the estimator's embedding space, which the authors attribute to a "shifted orthogonal boundary" caused by the cone effect. OSA is computationally lightweight (21 min overhead vs. 226 min for NPC), model-agnostic, and achieves SOTA results across image-text matching, image classification, and image retrieval under various noise ratios.

## Strengths

1. **Strong empirical results across multiple benchmarks.** OSA outperforms all prior noise-mitigation methods by substantial margins. On MS-COCO 5K with 50% noise, it surpasses NPC by 8.6% i2t R@1 and 7.0% t2i R@1 (Table 1). On Flickr30K at 60% noise, OSA improves CLIP by 20.9% i2t R@1 and 22.3% t2i R@1 (Table 2). Performance degradation as noise increases is minimal (1.275% drop vs. ~5% for NPC).

2. **Computational efficiency.** OSA adds only 21 minutes of overhead vs. 226 minutes for NPC (Table "Overhead Comparison"), and scales to 1B data points with ~75 hours on a single GPU. This is a genuine practical advantage for large-scale training.

3. **Model-agnostic and task-transferable.** OSA is demonstrated on different target architectures (ResNet-152, VGG-19, ViT) and improves diverse tasks (image-text matching, classification, retrieval). It also boosts NPC's own performance when applied on top of NPC (Table "Adaptability to Other Anti-Noise Models").

4. **Near-perfect noise detection.** The mean noise rank is nearly optimal (1809.1 vs. optimal 1815.5 at 20% noise; 1520.7 vs. 1524.0 at 50% noise), and recall exceeds 99% in high-noise settings, confirming the scoring function's precision.

5. **Real-world noisy dataset validation.** On CC120K (3%-20% real-world noise), OSA outperforms NPC, demonstrating effectiveness beyond synthetic noise.

## Weaknesses

### Major

1. **Theoretical proof does not apply to the actual models used.** Theorem 1 assumes neural network layers have *random Gaussian weight matrices* (each element ~ N(0, 1/d_out)). The estimator models (CLIP, ALIGN) are trained, not random — their weights are highly structured from contrastive learning on millions of samples. The paper's two-step argument (Section 2.2) claims (i) contrastive learning separates clean/noisy pairs across the orthogonal boundary, and (ii) the relative ordering is preserved through the narrow cone space (proved by Theorem 1 for random networks), concluding that the intersection boundary in the *trained* estimator space is the shifted orthogonal boundary. Step (ii) is only proven for random networks with no argument that a trained network preserves the same ordering property. The paper invokes the cone-effect literature (mindthegap, conebert) which documents the phenomenon in trained models empirically, but does not provide a theorem covering trained networks. This means Contribution 1 — "provide a theoretical framework that proves and elaborates the stability and precision of this boundary" — is not established by the proof as written. The empirical evidence (Figure 1, Table mean_var) still supports the existence of the boundary, but the claimed *theoretical* contribution is unsupported. The method's practical value is unaffected; this weakness undermines the explanatory framework, not the empirical results.

### Minor

1. **The source of improvement is not fully disentangled.** OSA combines (a) a powerful pretrained estimator's zero-shot discriminability with (b) the specific scoring function and boundary principle. The ablation in Table 4 shows that zero-shot CLIP (w/o DA) already performs very well, suggesting much of the gain comes from the estimator's inherent ability to distinguish clean from noisy pairs — a form of transfer from web-scale pretraining. The paper frames OSA as a "general principle of noise mitigation," but does not isolate how much the boundary principle vs. the estimator's raw capability drives performance. A fairer framing would acknowledge that OSA's strength comes from combining a pretrained cross-modal estimator with a simple scoring function. This does not invalidate the method but moderates the claimed generality of the "boundary principle."

2. **Missing experimental details.** The value of \(K\) (number of random pairs for spatial debiasing, Eq. 5) is not specified in the main text. Whether the estimator is frozen during target model training is implied (separate scoring and training phases) but never explicitly stated. These details are important for reproducibility.

3. **Noise detection analysis uses a hard threshold.** The accuracy/recall analysis (Table "ACC and recall") uses 0 as a hard threshold. Since the scoring function is continuous, reporting AUROC would be more informative and remove any dependence on threshold choice. This is a relatively minor methodological point.

### Trivial

- The claim "first work to explore anti-noise in practical large-scale training scenarios" (Conclusion) is qualified with "to the best of our knowledge" but could be seen as overstated given prior work on data filtering in large-scale web datasets.

## Nice-to-Haves

- Ablation of alternative scoring functions (e.g., sigmoid, linear clipping) to empirically justify the cubic function in Eq. 6.
- AUROC for noise detection rather than hard-threshold accuracy/recall.
- A controlled experiment isolating the scoring function's contribution from the estimator's zero-shot capability (e.g., comparing OSA against directly using the estimator's raw similarity as a weight).
- Explicit clarification of \(K\) and estimator frozen status in the main text.

## Removed Points

- *Criticism that Theorem 1's random-weight assumption is never mentioned by the paper as a limitation.* **Retained as Major (above)** — this is the core theoretical gap, but the severity is properly contextualized.
- *Criticism that the paper lacks comparison to methods using CLIP for data filtering / missing related work.* **Removed** — cannot verify presence/absence of external work, per instructions.
- *"Missing proofs in appendix" / "missing appendix"* — the parser strips these sections; they exist in the original submission.

## Novel Insights

The reviews surface a key tension that the paper itself does not fully resolve: the theoretical justification (shifted orthogonal boundary via random-network theorem) and the empirical evidence (strong performance with trained CLIP/ALIGN) operate at different levels of rigor. The cone-effect literature provides empirical support for the shifted boundary in trained models, and the paper's own empirical observations are convincing. The genuine novel insight here — and one the paper could lean into more — is that a simple, estimator-derived cosine-similarity threshold with spatial debiasing suffices for near-perfect noise identification, and that this works because contrastive pretraining naturally separates positive and negative pairs across the high-dimensional orthogonal boundary. The practical insight (one inference pass → effective noise mitigation) is stronger than the theoretical scaffolding built around it.

## Suggestions

1. **Revise the theoretical section** to either (a) drop the claim of a formal proof for trained models and reframe Theorem 1 as a mechanism that *explains* why the cone effect preserves relative ordering in an *idealized* setting, supported by the empirical observations in Figure 1 and the cone-effect literature, or (b) provide a more rigorous argument for why the boundary property extends to trained networks (e.g., connecting to properties of contrastive learning objectives).
2. **Disentangle the sources of improvement** by adding an ablation that compares OSA to directly using the estimator's raw cosine similarity as a weight (without the cubic scoring function), which would isolate the scoring function's contribution.
3. **Add explicit details** for \(K\) (number of random pairs for spatial debiasing) and a clear statement of whether the estimator is frozen during target model training.
4. **Report AUROC** alongside (or instead of) hard-threshold accuracy/recall.

## Score and Decision

This paper makes a strong empirical contribution with a practical, efficient, and broadly applicable noise mitigation method. The experimental validation is thorough across tasks, architectures, noise types, and datasets. The theoretical contribution is the paper's main weakness: Theorem 1 assumes random weights that do not describe the trained estimator models used, so the claimed "proof" of the boundary's origin is not established. However, the method works independently of this theoretical gap, and the cone-effect intuition is plausible and supported by empirical evidence. The paper is a solid empirical/systems contribution that would be strengthened by a more honest framing of its theoretical claims.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**