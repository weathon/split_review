Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes LARP, a video tokenizer that uses learned holistic queries (instead of patchwise encoding) to produce discrete tokens, and jointly trains a lightweight autoregressive prior model that is discarded at inference. The key ideas are: (1) decoupling tokens from local patches via learned queries, enabling flexible token counts, and (2) co-training an AR prior that shapes the latent space to be more amenable to AR generation, as evidenced by a dramatic gFVD drop from 190→107 in the ablation when the prior is included.

## Strengths

- **Holistic tokenization via learned queries is a novel and well-motivated design.** Unlike patchwise tokenizers where each token corresponds to a fixed spatial location, LARP's query-based approach (Sec. 3.2) decouples tokens from patch positions. This enables flexible token counts (Fig. 2b shows graceful degradation from 1024→256 tokens) and allows tokens to capture more global/semantic information. The design is clearly explained and its benefits are demonstrated.

- **Co-training with a lightweight AR prior delivers a substantial and cleanly isolated improvement.** The ablation study (Table 2) is the paper's strongest evidence: removing the AR prior raises gFVD from 107 to 190 on UCF-101 (LARP-B), while reconstruction metrics actually improve (rFVD 23 vs. 31, PSNR 27.95 vs. 27.88). This directly validates the core thesis that optimizing for reconstruction alone does not yield a generation-friendly latent space, and that the AR prior effectively bridges this gap. Crucially, the prior is discarded at inference (Sec. 3.3, lines 46, 217), adding zero cost.

- **State-of-the-art FVD on UCF-101 among published models.** Table 1 reports LARP-L-Long (632M generator) achieving gFVD 57 on UCF-101, surpassing MAGVIT-v2-MLM (58) and all AR methods by a large margin (e.g., MAGVIT-v2-AR at 109, OmniTokenizer at 191). The improvement over prior AR methods is substantial and robust.

- **Scheduled sampling and SVQ both contribute meaningfully.** The ablation (Table 2) shows removing scheduled sampling raises gFVD from 107→142, and switching from SVQ to deterministic VQ raises it from 107→149, while reconstruction metrics remain similar. These ablations validate the design choices cleanly.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The SOTA claim on UCF-101 (gFVD 57 vs. 58) lacks any measure of uncertainty.** The paper reports no confidence intervals, multiple-seed runs, or variance for any FVD values. On a dataset with ~9k test samples across 101 classes, FVD has non-trivial variance, and a 1-point margin could shift with a different seed or evaluation protocol. While the paper's core contribution (the method and its ablation evidence) does not depend on this 1-point margin, the claim is prominently featured in the abstract, introduction, and contributions list. The authors should either report variance (e.g., 3-run mean and std) or soften the claim to acknowledge the margin is within typical noise. The internal evidence from the ablation (107→190) is far more convincing and should be more prominently positioned.

- **The "automatic token ordering" claim is asserted but not directly validated.** The paper states (lines 48, 379) that the AR prior "automatically determines an order for latent discrete tokens" and "defines an optimal token order," presenting this as a benefit over patchwise tokenizers that require manual flattening. However, no experiment isolates whether the ordering itself matters versus the prior's broader effect of shaping the latent space. For example, one could train an AR generator on top of the same tokenizer with the token sequence shuffled, or compare with a fixed ordering on the holistic tokenizer trained without the prior. Without such an experiment, the ordering claim remains a speculation rather than a supported finding. The paper would be stronger by either adding this experiment or reframing the claim more modestly (e.g., "the prior shapes the latent space for AR generation; the ordering is a byproduct whose independent contribution we do not isolate").

- **No inference-cost comparison.** The paper correctly notes the prior is discarded at inference. However, the holistic tokenizer itself uses a transformer encoder processing 2048 tokens (1024 patches + 1024 queries) for the default configuration, which is larger than typical patchwise encoders processing only 1024 tokens. Reporting tokens/second or wall-clock inference speed would help practitioners assess the practical trade-off. This is a mild omission given the paper's focus on quality.

- **No limitations section.** The paper operates at 128×128 resolution and 16 frames. Scalability to higher resolutions or longer videos is not discussed. A brief honest discussion of limitations would improve the paper without weakening it.

### Trivial
- The paper uses "is is" (line 217: "Since $\alpha$ is is typically set to a small value"), a minor typo.

## Nice-to-Haves

- A controlled comparison with a patchwise ViT-VQGAN trained in the same framework (same backbone, codebook size, training loss, AR generator) would cleanly isolate the benefit of the holistic + prior combination from the general advantage of using a ViT architecture. The current comparison is against published methods with different architectures and training setups.
- Visualizing the learned token order (e.g., which queries attend to which spatial regions, or whether early tokens encode static backgrounds and later tokens capture motion) would deepen the narrative around the ordering claim.

## Removed Points

- **Strength from Strength Finder: "The AR prior automatically defines an optimal token order, eliminating manual flattening heuristics."** Removed per the conflict rule: this claimed strength conflicts with the verified weakness that the ordering claim is not directly validated. The paper's strong results support the prior's overall value but do not specifically validate the ordering sub-claim.
- **Harsh Critic's observation about rFVD metrics not being in the main table:** The paper's rFVD values are in Table 1 (24 and 20 for LARP variants). PSNR/LPIPS are in the ablation table. This is a description of the table formatting, not a weakness.
- **Harsh Critic's framing of the SOTA issue as "critical":** Downgraded to minor because (a) the 1-point margin does not threaten the core contribution, and (b) the ablation evidence (107→190) independently supports the method's value. The paper would be stronger with variance reporting but is not fatally harmed by its absence.

## Novel Insights

The most striking finding from this review is the clean separation the ablation study reveals between reconstruction quality and generation quality. The "No AR prior" variant achieves the best reconstruction metrics (PSNR 27.95, LPIPS 0.0830, rFVD 23) but the worst generation (gFVD 190), while the full model has worse reconstruction but dramatically better generation (gFVD 107). This 83-point gFVD swing with essentially no reconstruction penalty is a particularly clean demonstration of the reconstruction-generation gap that has been noted in prior work (Yu et al., 2024; Zhang et al., 2023). The paper's design of co-training a prior that is discarded at inference is an elegant way to address this gap without inference cost — a principle that could generalize beyond video tokenization.

## Suggestions

1. Report FVD with variance (e.g., 3-run mean and std) for the best configuration on UCF-101, or soften the SOTA claim if the variance is high.
2. Either add an ablation testing the ordering claim (e.g., shuffling token order at generator training time) or reframe the claim to match what is actually shown.
3. Add a brief limitations paragraph discussing resolution/duration constraints and known limitations of FVD as a metric.
4. Fix the typo on line 217 ("is is").

## Score and Decision

The paper presents a genuinely novel combination of holistic tokenization via learned queries and co-training with a lightweight AR prior. The method is well-motivated, cleanly designed, and supported by strong ablation evidence. The weaknesses — lack of variance reporting for a thin SOTA margin and an unvalidated ordering claim — are real but minor relative to the core contribution. The paper would benefit from addressing these but does not require major revision.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>