Now I have a solid calibration base. Let me compose my final review.

## Summary

LS-Merge proposes a paradigm shift for model merging: instead of operating directly on model weights, it encodes weights into a learned latent space using a transformer VAE, performs merging operations (interpolation, soup, OT alignment) in that space, and decodes back to weights. This enables self-merging (sampling multiple codes from a single model's posterior), homogeneous expert fusion, and—critically—heterogeneous cross-architecture merging (e.g., Gemma → LLaMA) via Optimal Transport alignment of latent distributions. Experiments across Gemma, LLaMA, and LoRA experts show consistent gains over weight-space baselines, with the cross-architecture results (Table 5) being a genuinely novel capability.

## Strengths

- **First demonstration of cross-architecture LLM merging via latent-space alignment.** The OT-based latent distribution alignment (Section 3.3) is a principled solution to a problem that weight-space methods fundamentally cannot address. Table 5 shows that naive interpolation between Gemma and LLaMA latents degrades performance, while OT-aligned interpolation recovers and surpasses baselines (WinoGrande: 57.75 vs. 56.83, ARC-C: 43.34 vs. 42.78, HellaSwag: 50.10 vs. 49.07). This is a genuine research contribution.

- **Consistent and substantial empirical gains across four merging scenarios.** LS-Merge outperforms weight-space methods in self-merging (Table 2: up to ~4% improvement on Gemma-3-1B-it MMLU: 32.20→35.13), expert fusion (Table 3: LS-Merge soup achieves 56.0 MMLU vs. best baseline Greedy Soup at 50.8), representation merging (Table 4: competitive with AIM on Llama-2-13B), and cross-architecture merging (Table 5). The gains are not cherry-picked—they hold across eight diverse benchmarks.

- **Weight distribution analysis (Table 1, Figure 2) is thorough and motivates design choices.** The analysis establishing that LLM attention weights exhibit high kurtosis (up to ~15) and low-rank structure directly informs the two-stage VAE training curriculum (Section 3.2) and the choice of transformer encoder over simpler alternatives. This grounding in observed properties of the data modality is good science.

- **Non-linear manifold learning is demonstrated to be a geometric necessity, not a stylistic choice.** Table 8 directly compares PCA against the VAE at compression ratios 1.6×, 2×, and 4×. PCA collapses to near-random MMLU accuracy (~25.5%) at all ratios while the VAE retains ~96% of base performance. This clean ablation validates that pretrained weights do not lie in a linear subspace.

- **Solid ablation studies isolate the roles of different components.** Table 6 shows merging MLP and attention jointly yields the best results, while attention-only merging degrades performance, confirming these submodules encode complementary functional knowledge.

## Weaknesses

### Fatal
None.

### Major

- **Suboptimal baseline comparisons in the expert merging experiment conflate two sources of gain.** LS-Merge trains a VAE on the LoRA experts before merging them, giving it access to a learned generative model of the weight distribution. The weight-space baselines (uniform soup, SLERP, greedy soup, Dare-Ties) receive no such training signal. While the comparison is not "unfair" (the VAE is part of the method), it makes it impossible to determine how much of the gain (e.g., 56.0 vs. 50.8 on MMLU, Table 3) comes from (a) the latent-space merging operation itself vs. (b) simply having a generative model. A control experiment that encodes each expert, decodes back, and then applies weight-space merging would isolate this effect. This is a significant oversight that weakens the core empirical claim.

### Minor

- **The VAE training data is insufficiently specified.** The paper states only "pretrained weight snapshots for Gemma-3-1B-it and Gemma-3-4B-it, plus LoRA experts from Feng et al. (2024b)" (Section 4). It is unclear how many distinct weight configurations per architecture are used (one snapshot? multiple along a training trajectory?). The VAE's generalization to unseen architectures (Table 7: trained on Gemma-3-4B-it, tested on Gemma-3-1B-it and LLaMA-3.2-1B-it) suggests it learns more than single-instance memorization, but the vague description is a reproducibility concern. The chunking strategy (lines 348-350) creates many training tokens from each model's layers, but whether the VAE sees multiple *functionally distinct* weight configurations per architecture remains unclear.

- **The Gaussian approximation for OT alignment (Section 3.3) is at odds with the paper's own finding that weight distributions are heavy-tailed (Section 3.1, kurtosis up to ~15).** The paper models each layer's latent distribution as a Gaussian (mean + covariance) to derive a closed-form OT map. While this is a practical simplification and the paper acknowledges it as an "approximation" (line 480), it provides no analysis of how heavy tails in the latent space affect alignment quality or merging performance. Non-Gaussian OT alternatives (e.g., Sinkhorn without distributional assumptions) are not explored.

- **The heterogeneous layer pairing heuristic (Algorithm 1) is unvalidated.** For merging models with different depths (e.g., Gemma-3-4B-it's 34 layers into Gemma-3-1B-it's 18 layers), the paper uses a simple proportional mapping based on layer counts. There is no validation that this pairing respects functional correspondence (e.g., does layer i of 18 map to the correct functional role in a 34-layer model?). While this heuristic is reasonable, the paper's cross-architecture claims would be stronger with some validation (e.g., checking multiple pairing schemes or using attention/role alignment).

- **Self-merging (Table 2) is presented as a key contribution, but its mechanism is not fully explained.** The paper samples "multiple latent codes from its posterior distribution" and merges them, but does not specify how many samples are drawn, how they are merged (simple average? interpolation?), or why this yields improvements over the single-sample VAE reconstruction. The near-zero standard deviations for LS-Merge on some benchmarks (e.g., 0.00 on MMLU for Gemma-3-4B-it) are unusual and require explanation.

### Trivial
- The paper could benefit from t-SNE/UMAP visualizations of latent codes for multiple weight configurations, as currently only the heterogeneous case is visualized (Figure 9).
- Table 8 shows VAE maintaining performance at r=4.0, which is impressive but deserves more discussion since it contrasts with the generalization results in Table 7 where R4× causes collapse.

## Nice-to-Haves
- **Control experiment for expert merging:** Encode each expert, decode back, then apply uniform soup on the decoded weights in weight space. This would isolate the benefit of latent-space operations from the benefit of having a generative model.
- **Validation of the Gaussian OT approximation:** Reporting what fraction of latent codes fall in the tails and comparing against non-parametric OT (e.g., Sinkhorn divergence) would strengthen the OT alignment claims.
- **Analysis of decoded weight distributions after merging:** Do merged weights preserve the heavy tails or get smoothed out?
- **Training-time details for the VAE:** Clarify the number of unique weight snapshots, training steps, and data augmentation strategies used.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. "The VAE is trained on an insufficient number of weight configurations, making the manifold claim unsupported" — This is too strong. Table 7 shows the VAE generalizes to unseen architectures (trained on Gemma-3-4B-it, tested on Gemma-3-1B-it and LLaMA-3.2-1B-it), directly contradicting the claim that it merely memorizes one instance. However, the vagueness about training data is retained as a minor weakness above.

2. "The expert merging evaluation is fundamentally unfair" — Comparing a learned method against non-learned baselines is standard practice in ML. The critic's framing is too strong. However, the absence of an isolation control experiment is a real weakness (retained above as Major).

3. "Section 3.1 within-matrix heavy tails are primarily relevant for compression of a single matrix" — The paper uses these statistics to inform encoder design (allocating capacity to attention layers), which applies universally, not per-instance.

4. "Standard deviations of 0.00 are suspicious" — With deterministic evaluation and averaging over many samples, near-zero variance is expected and not suspicious.

5. "Overcomplete bottleneck adds extra computation without clear benefit" — The paper explicitly addresses this (Section 6, lines 865-869): expansion helps unfold the weight manifold and eases optimization.

6. "PCA vs. VAE comparison conflates linear vs. non-linear compression" — The comparison is exactly what the paper claims: a test of whether LLM weights lie on a linear or non-linear manifold. PCA is the natural linear baseline.

## Novel Insights

The most interesting observation across the reviews is the tension between the paper's two central claims. On one hand, the VAE must learn a meaningful latent manifold of LLM weights to make merging operations principled; on the other hand, the paper's main empirical successes (especially cross-architecture merging via OT) could be driven more by the distribution alignment step than by any manifold structure. The OT alignment essentially "registers" two latent spaces that were learned independently, and the gains might reflect mean/covariance matching rather than true manifold interpolation. The paper would be stronger if it included an experiment that ablates the manifold structure itself—e.g., replacing the VAE with a simpler encoder (like a random projection) + OT alignment to see how much of the cross-architecture gain comes from each component.

## Suggestions
1. **Specify the VAE training data clearly** — state the number and type of distinct weight snapshots per architecture (e.g., "1 released checkpoint per model, plus 10 LoRA experts"). This is essential for reproducibility.
2. **Add a control experiment for expert merging** — encode each expert, decode to weight space, then apply uniform soup. This isolates the benefit of latent-space operations from the benefit of the generative model.
3. **Report the number of latent samples used in self-merging** and explain the near-zero variance in Table 2.
4. **Validate the Gaussian OT approximation** against non-parametric alternatives, or at minimum analyze the impact of heavy tails on alignment quality.
5. **Validate the heterogeneous layer pairing** with alternative heuristics (e.g., reverse mapping, functional alignment).

## Score and Decision

### Calibration Anchors

**High-scoring anchors (≥6.0):**
- `/home/wg25r/review_agent/human_reviews_2026/ULxerRB2DF.md` — 6.00, Reject (Harnessing Optimization Dynamics for Merging). Strong curvature-aware merging method on Llama-3.1-8B only, criticized for limited architecture scope. LS-Merge evaluates across more architectures and a wider range of merging scenarios, making its empirical contribution stronger.
- `/home/wg25r/review_agent/human_reviews_2026/fOwsr1VTi8.md` — 5.50, Accept Poster (DeepWeightFlow: flow matching for weight generation). Comparable weight-space learning paper; LS-Merge has broader applicability (merging scenarios) but weaker clarity on training data.

**Medium-scoring anchors (4.0–5.9):**
- `/home/wg25r/review_agent/human_reviews_2026/C21rz8mo65.md` — 4.80, Accept Poster (MergOPT: merge-aware optimizer). LS-Merge is more novel (latent-space merging paradigm vs. optimizer modification) and evaluates more broadly. Similar level of methodological concern (MergOPT's Laplace assumption vs. LS-Merge's Gaussian OT approximation).
- `/home/wg25r/review_agent/human_reviews_2026/RU76KTF1Da.md` — 4.67, Accept Poster (optimizer implicit bias). Analysis-focused paper; less directly comparable.
- `/home/wg25r/review_agent/human_reviews_2026/S0MRfeGr5d.md` — 4.00, Reject (StatsMerging). LS-Merge is significantly more novel and has stronger experiments.

**Low-scoring anchors (≤3.9):**
- `/home/wg25r/review_agent/human_reviews_2026/ocEoHCrezd.md` — 2.50, Withdrawn (Latent Merging: representation-space merging). Despite a superficially similar name, this paper merges activations, not weight-space latents. It was criticized for 2× inference cost and narrow evaluation. LS-Merge avoids these issues (no inference overhead) and is substantially stronger.

**Comparative assessment:** LS-Merge is more novel than the accepted MergOPT (4.80) and comparable in contribution level to DeepWeightFlow (5.50). Its main weaknesses (vague training data specification, missing control experiment) are addressable in revision and do not threaten the core contribution. The cross-architecture merging capability alone is a genuine advance over existing weight-space methods. I place it firmly in the Accept (Poster) range.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>