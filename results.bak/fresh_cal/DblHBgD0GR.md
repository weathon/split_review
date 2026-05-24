Now I have a thorough understanding of the paper. Let me verify my findings against the reviewer claims and produce the final consolidated review.

**Verification check on the clean baseline criticism**: The paper states the clean IMS is -0.13 (Table 1). The IMS is a *weighted average* of two face embedders (antelopev2 and VGG-Net, λ=0.7 weighting the former). The paper measures cosine similarity between *generated* DreamBooth images and *reference* images of the same identity. With only 4 identities × 8 images each for DreamBooth fine-tuning, the generated images may not achieve high cosine similarity against the reference set. The relative comparison (Ours > baselines across 7 protections) is the primary result, and it is clean. However, the paper does not provide the per-embedder breakdown or explain why Clean = -0.13 specifically, which is a gap.

**Verification check on adaptive attack**: Line 366 reads: "adaptive perturbation crafted against the image purification part." The paper only attacks CodeSR, not CDL. The claim of "resilience against adaptive perturbations" is therefore partially supported — it holds against attacks on purification but hasn't been tested against attacks designed to thwart CDL. This is a genuine limitation.

**Verification check on CDL single token**: The paper (line 162) introduces one noise token V*_N to absorb "all the noise components." This is indeed a strong assumption given per-image PGD-optimized perturbations. The empirical results show it works, but the mechanism is underspecified.

Let me now write the consolidated review.

Score decision: The paper has real contributions (causal analysis of latent mismatch, systematic defense framework, comprehensive evaluation), and the weaknesses are real but addressable. The clean baseline issue does not invalidate the primary comparison (Ours vs baselines). Score: 7.0. Decision: Accept.## Summary

This paper identifies a causal mechanism for why protective perturbations degrade personalized diffusion model fine-tuning: adversarial perturbations cause a latent-space misalignment between image embeddings and text prompts in CLIP space, leading the model to learn spurious correlations between noise patterns and the unique identifier token. Based on this analysis, the authors propose a systematic defense framework combining (1) image purification via off-the-shelf restoration (CodeFormer + super-resolution, termed CodeSR), (2) Contrastive Decoupling Learning (CDL) that uses a learnable noise token to explicitly separate personalized concepts from noise patterns, and (3) quality-enhanced sampling with negative prompting. The method is evaluated against 7 protection methods and 9 purification baselines, demonstrating strong improvements in identity similarity (IMS) and image quality (Q), a 10× speedup over IMPRESS in purification time, and robustness to adaptive attacks on the purification pipeline.

## Strengths

- **Causal analysis of protective perturbation effectiveness.** Section 4.1 provides empirical evidence (2D latent visualizations using TSNE/UMAP, zero-shot CLIP classification) that adversarial perturbations shift image embeddings away from their semantic concept region in CLIP space, while random perturbations of equal magnitude do not. This goes beyond prior work that only examined text-encoder vulnerability (Zhao et al., 2024) and provides a principled foundation for the defense design.

- **State-of-the-art defense performance across a comprehensive range of protections.** Table 1 shows the proposed method achieves the highest IMS (0.09–0.38) and Q (0.58–0.67) under all 7 protection methods (FSMG, ASPL, EASPL, MetaCloak, AdvDM, PhotoGuard, Glaze), while all prior purification baselines (GrIDPure, IMPRESS, DiffPure variants, etc.) yield negative IMS scores across the board. The margin is substantial and consistent.

- **10× purification efficiency with better faithfulness.** Table 2 reports CodeSR requires 51s per sample (lowest among diffusion-based purifications) with LPIPS = 0.271 (best), compared to IMPRESS at 675s and LPIPS = 0.451. This is a practical engineering contribution — existing methods are too slow for real-world deployment.

- **CDL as a standalone effective defense mechanism.** The ablation study (Table 3) shows that CDL alone (without any purification) achieves IMS = 0.160 and Q = 0.038, surpassing all baseline purification methods. This provides evidence that CDL offers a genuinely new mechanism beyond input purification.

- **Comprehensive evaluation framework.** Testing against 7 protection methods (spanning bi-level optimization and fixed-model approaches) and 9 purification baselines (rule-based, pixel-space diffusion, latent diffusion, grid-based, optimization-based) is more extensive than any prior defense study in this area (e.g., Van et al. 2023 tested only simple transformations; IMPRESS tested 3 protections).

## Weaknesses

### Fatal
None.

### Major

- **The clean training baseline (IMS = –0.13) is surprisingly low and not adequately explained.** The "Clean" row in Table 1 shows that training DreamBooth on *unperturbed* data yields a negative identity matching score. While this does not undermine the paper's primary comparison (Ours vs. purification baselines — which it wins decisively), the paper claims to "close the gap" and even exceed clean training. The authors offer a brief explanation (image restoration + CDL improve quality), but they do not analyze why clean DreamBooth training itself produces such low IMS. Without a breakdown of the two IMS components (antelopev2 and VGG-Net) or a discussion of the metric's expected range for this task, readers cannot assess whether the clean baseline is a reasonable reference point or artifact of the specific metric configuration. This should be addressed by reporting the per-embedder scores and contextualizing the expected IMS range for DreamBooth on 4-identity VGGFace2.

- **The adaptive attack evaluation does not target the full defense pipeline.** Section 5.3 crafts adversarial perturbations *against the image purification part only* (CodeSR). CDL is not included in the attacker's threat model. A genuine adaptive attacker could design perturbations that resist the full defense — for instance, by crafting noise patterns that are not separable by a single token in CDL. The paper's claim of "resilience against adaptive perturbations" (abstract, line 31) is therefore overstated relative to the actual evaluation. The experiments do show that CDL helps maintain performance when the attack targets purification, but the scope of the claim should be narrowed or the evaluation extended.

### Minor

- **CDL's single noise token assumption is underspecified.** The method introduces one token 𝒱*_N to absorb the "noisy pattern" across all perturbed images (line 162). However, protective perturbations are optimized per-image via PGD with different seeds, producing structurally distinct noise patterns. The paper does not analyze whether the learned token actually captures a consistent noise property, or whether it simply acts as a general-purpose "absorbing" token that still allows residual shortcut learning. The empirical success (CDL alone works) is encouraging, but the mechanism is not validated. Analysis of the learned token's embedding behavior under different perturbations would strengthen the paper.

- **Statistical significance claims lack specificity.** The caption of Table 1 states that "*" denotes "significant improvement that passes the Wilcoxon signed-rank significance test with p ≤ 0.01," but it does not specify the comparison being tested (against the best baseline? against clean? against perturbed?). The number of runs and how the test is applied across identities are also not described in the main text. The paper references the appendix (stripped), but the main text should make the comparison explicit.

- **The zero-shot CLIP-based "noise" vs. "person" classification (Section 4.1) is methodologically questionable.** "Noise" is not a standard CLIP concept, and the paper does not specify how the "noise region" classifier prompt was constructed. The latent visualization (TSNE/UMAP) showing perturbed images shifting away from "person" is informative, but the binary classifier framing adds little rigor.

- **The λ = 0.7 weighting in the IMS metric is presented without justification.** The paper assigns λ = 0.7 to the antelopev2 embedder (following IP-adapter conventions), but the effect of this weighting choice on the reported scores is not analyzed. A sensitivity analysis of λ would help establish that results are not driven by an arbitrary weighting.

### Trivial

None.

## Nice-to-Haves

- An analysis of the diversity and clustering behavior of the learned noise token 𝒱*_N under different perturbation types (AdvDM vs. ASPL vs. MetaCloak) would validate whether CDL works as claimed.
- A control experiment isolating the effect of the quality-enhanced sampling (negative prompting) from CDL would clarify each component's contribution. Currently the ablation combines CodeFormer, SR, and CDL but does not show CDL with/without quality-enhanced sampling separately.
- Quantitative results on the WikiArt domain (Table 1 currently only shows visual examples).

## Removed Points

These points are flagged to be removed; treat them with caution, as they are either factually wrong, unsupported, or reflect reviewer misunderstanding:

- **"The clean baseline implausibility invalidates the entire comparison."** — Removed as overreach. The primary comparison (Ours vs. baselines) is unaffected by the absolute value of Clean; the method clearly beats all purification baselines. The clean baseline serves as a reference point, and while it deserves more explanation, it does not collapse the paper's main results.
- **"Baseline implementations are not detailed."** — Removed. The paper references Appendix A.5 for training details; the appendix was stripped by the parser.
- **"4 identities is too small."** — Removed. This follows the established evaluation protocol in the field (Van et al. 2023, Liu et al. 2024 use identical sizes).
- **"The 10× claim depends on total pipeline time."** — Removed. The paper specifically compares *purification* time, which is a clean comparison: 51s vs. 675s.
- **"The IMS metric is ad-hoc."** — Removed. The metric follows established practice (IP-adapter weighting conventions, InsightFace/Deepface embedders used in prior work).
- **"The quality metric is not designed for identity preservation."** — Removed. Q measures *graphical/aesthetic* quality (explicitly stated), not identity — that is IMS's role.
- **"Missing limitation section."** — Removed. The conclusion (line 413) explicitly acknowledges "being mainly tested on facial data" and discusses future work on module combinations.
- **"Missing noise token initialization."** — Removed. This is a trivial implementation detail appropriate for the appendix.
- **Strengths removed from Strength Finder:** Generic framing strengths like "this paper addressed an important problem" are removed as superficial. Only concrete, evidence-backed strengths are retained.

## Novel Insights

The interesting dynamic revealed by merging these reviews is the tension between the paper's primary and secondary claims. The central claim (Ours outperforms all baselines) is well-supported and survives scrutiny. However, the secondary claim (Ours exceeds clean training) and the causal analysis framing create a higher standard of proof that the paper only partially meets. The harsh critic correctly identified that the clean baseline's low absolute value makes the "exceeds clean" result hard to interpret, but incorrectly elevated this to a fatal flaw that undermines *all* comparisons. The actual vulnerability is narrower: the main experimental results are valid, but the paper would benefit from either calibrating the IMS metric more carefully or softening the "beyond clean" framing. A second synthesized observation: both reviews agree that the CDL mechanism is empirically effective (ablation studies are strong) but theoretically underspecified — this is a common pattern in empirical ML papers where a simple technique works better than expected, and the paper would be strengthened by candidly acknowledging this gap rather than over-claiming the completeness of the causal analysis.

## Suggestions

1. **Calibrate the clean baseline.** Report the per-embedder breakdown (IMS_IP and IMS_VGG separately), include a reference for what scores are typical for DreamBooth on this setup, and either contextualize the "beyond clean" claim or temper it. This is the single change that would most strengthen the paper's credibility.

2. **Broaden the adaptive attack evaluation.** Include CDL in the attacker's objective. Even a simple extension (e.g., crafting perturbations that minimize the separability of noise vs. clean tokens) would substantially strengthen the robustness claims.

3. **Analyze the learned noise token.** Visualize the embedding of 𝒱*_N across different perturbation methods. Show whether it consistently points toward a "noise" region or varies by perturbation type. This would directly address the concern about token representational capacity.

4. **Clarify the statistical test.** Specify in the table caption or method section that the Wilcoxon test compares Ours against the best-performing baseline (and name which one), and report the number of paired samples.

5. **Provide IMS sensitivity to λ.** Show a small curve of IMS values at different λ (e.g., 0.5, 0.7, 0.9) for at least one setting to demonstrate result stability.

## Score and Decision

This paper makes two clear contributions: (1) a novel causal explanation (latent-space misalignment) for why protective perturbations degrade PDM fine-tuning, supported by empirical visualizations; and (2) an effective, efficient defense framework that substantially outperforms existing purification methods across 7 protections and 9 baselines, with additional robustness benefits from CDL. The weaknesses are real but addressable — the clean baseline issue warrants clarification but does not invalidate the core results, and the other concerns (adaptive attack scope, CDL mechanism underspecification) are limitations that can be resolved in revision. Overall, the paper is a solid contribution with well-supported primary claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>