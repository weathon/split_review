## Summary

This paper introduces a nonlinear, multimodal encoding model for naturalistic speech fMRI that combines semantic features from LLaMA and audio features from Whisper via a single-hidden-layer MLP applied over PCA-compressed voxel responses. Compared to the standard unimodal linear encoding baseline (Antonello et al., 2024), the model achieves 17.2%/17.9% improvement in r²/CC_norm, supported by careful ablations (MLLinear and DIMLP) that isolate contributions from dimensionality reduction, within-modality nonlinearity, and cross-modal nonlinear interactions. Beyond prediction accuracy, the authors present RED-based spatiotemporal clustering and variance partitioning analyses to reveal cortex-wide multimodal integration patterns consistent with neurolinguistic theories.

---

## Strengths

- **Verified performance gains with controlled ablation**: Table 1 directly verifies the headline numbers (MLP PCA: 4.29% r², 34.32% CC_norm vs. linear baseline 3.66%, 29.12%). The DIMLP ablation cleanly separates within-modality nonlinearity (gain from 4.10% to 4.18%) from cross-modal nonlinear interactions (4.18% to 4.29%), providing a principled decomposition rare in this field.

- **Substantial, unusually large gains for speech fMRI**: The combined 17.2%/17.9% improvement using only 5.64M parameters (vs. 1.31B for linear) is quantitatively large by the standards of incremental fMRI encoding work, as the paper notes in Appendix N.2. This provides practical value for downstream applications like decoding and in-silico experimentation.

- **Neuroscientific findings are specific and appropriately hedged**: The variance partitioning analysis (Figure 3) showing joint audio-semantic dominance in 68.5% of voxels, with systematic hierarchical variation from AC → Broca → sPMv → M1M along the dorsal pathway, is a concrete finding. The paper appropriately hedges motor/somatosensory interpretations in Section 3.3.2: *"an alternative possibility is that the observed effects reflect quasi-semantic factors such as lexical frequency, predictability, or articulatory demands rather than concept-specific embodied simulation."*

- **Parameter-efficient design**: The PCA output compression (512 components) is well-motivated as a strategy to make nonlinear mapping tractable over 80–90k cortical voxels, an explicit engineering challenge the paper distinguishes from the vision encoding case (Section 1).

---

## Weaknesses

### Fatal
None.

### Major

- **Multimodality, not nonlinearity, is the primary driver of the headline gains — but the abstract and introduction do not reflect this**: From Table 1, switching from unimodal text-linear to multimodal text+audio linear yields a 12.0% r² improvement; switching from multimodal linear to multimodal MLP adds only ~4.6%. The abstract states the 17.2% gain alongside claims that "incorporating both nonlinearity and multimodality is crucial," but the decomposition in the actual ablations shows multimodality contributes roughly three times as much as nonlinearity. The paper does provide the right numbers in Table 1 and Section 3.2.1 — *"DIMLP yields a 2.0% gain...standard MLP achieves a further 2.6% gain"* — but this hierarchy is absent from the abstract and the introduction, which emphasize nonlinearity prominently without clearly communicating that multimodality dominates the effect. The framing should align with what the ablations demonstrate.

### Minor

- **PCA variance explained is not reported in the main text**: The entire approach depends on PCA-compressing responses to 512 components and then reconstructing voxel-space predictions via the inverse transform. Section 2.3 states this enables "reconstruction...back into voxel space," but the fraction of response variance captured by 512 components is never stated in the main text. If 512 components capture only 60–70% of variance, predictions back in voxel space will systematically underestimate signal in the remaining components — a point that matters for interpreting absolute r² values.

- **Anomalous result in Table 1 requires more explanation**: The text+audio Linear PCA model achieves 28.92% CC_norm (-0.7% relative to baseline), *worse* than the text-only Linear all-voxels baseline (29.12%). That adding audio modality to a linear model with PCA compression hurts CC_norm is counter-intuitive and the current explanation in Section 3.1.1 ("likely due to overfitting") is insufficient — PCA should reduce, not induce, overfitting in linear regression. Since this result shapes the claim that PCA helps MLP but not linear models, a more careful analysis is warranted.

- **The RED metric is presented as a major contribution but functions as a diagnostic tool**: As defined in Section 2.5, RED(v,t) = |f₁(v,t) − y(v,t)| − |f₂(v,t) − y(v,t)| is the difference of absolute prediction errors — a straightforward comparison tool. Its contribution is the application to spatiotemporal clustering, not the metric itself. The claim in the introduction ("We introduce a RED-based clustering analysis") is appropriate, but listing it as a peer contribution alongside performance improvements and variance partitioning slightly misrepresents its scope. The modularity improvement (Q: 0.145 → 0.155, a 7% relative change) is modest; the more compelling comparison is against raw functional connectivity (Q: 0.068), which any encoding model should exceed by construction.

- **Only 3 subjects from a single dataset**: The main results are averaged across three subjects. Individual-subject variation is deferred to appendices. With only 3 subjects, the confidence interval on aggregate r² and CC_norm differences can be non-trivial, and statistical significance information (Appendix C) is not surfaced in the main results discussion.

### Trivial
- The abstract uses "unnormlized" (sic), a parser artifact.

---

## Nice-to-Haves

- The DIMLP ablation is the paper's strongest scientific evidence for the source of gains; presenting it as the centerpiece (rather than as supporting evidence buried in Section 3.2.1) would make the argument considerably more compelling.

- Reporting whether the PCA-MLP advantage holds across more subjects in the LeBel et al. (2023) public dataset (which has more than three subjects) would substantially strengthen the reliability claim.

- The comparison with Antonello et al.'s multi-layer Whisper extraction (discussed in Appendix D) deserves at least a brief mention in the main results, since the paper's choice of final-layer-only Whisper is one source of the SOTA comparison gap.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh Critic — "Comparison with Antonello et al. as prior SOTA is not fully fair" (elevated to Major by harsh critic)**: The paper itself explicitly addresses this in Section 3.3.1 and Appendix D, explaining why the final-layer Whisper choice is preferable (less redundancy, enables richer integration). The choice is argued, not arbitrary. Given the explanation in the paper, this is at most a minor note for future work — not a methodological gap that undermines the comparisons.

- **Harsh Critic — "nonlinear approaches unique to speech vs. vision challenges"**: The paper explicitly defers this to Appendix N ("Appendix N"), which exists in the original submission. Per the review rules, criticisms about missing appendix content are excluded.

- **Strength Finder — "Cross-modal nonlinearity is the primary driver"**: This strength is incorrect as written. Multimodality contributes ~12% in r² and nonlinearity contributes ~4.6%; multimodality is the primary driver. The strength is removed to avoid mischaracterizing the paper's actual finding.

- **Harsh Critic — Statistical significance of aggregate Table 1 gains**: The paper states "statistical significance analysis can be found in Appendix C." Per the review rules, this is not a weakness.

---

## Novel Insights

The paper's most underappreciated finding, not foregrounded in the framing, is that the simple PCA-of-outputs trick combined with a shallow MLP is sufficient to expose widespread cross-modal integration that linear models — regardless of how many parameters they use — systematically miss. This suggests that the barrier to nonlinear speech fMRI modeling is not architectural depth but rather the response-space bottleneck: projecting 80k+ correlated voxels into a compact representation before nonlinear mapping. The DIMLP ablation, showing that even linear fusion of separately nonlinear modality-specific processing falls short of full cross-modal MLP, implies that the neural computation at stake is genuinely interactive, not merely a sum of unimodal nonlinear readouts. This is a substantive, underemphasized insight about what kind of nonlinearity matters for speech comprehension modeling.

---

## Suggestions

1. Revise the abstract and introduction to reflect the ablation-derived decomposition: multimodality accounts for ~12% of the 17.2% r² gain, nonlinearity accounts for ~4.6%, with ~2.6% specifically attributable to cross-modal nonlinear interactions. State this hierarchy explicitly.
2. Add the PCA variance-explained fraction (e.g., "512 components capture X% of total response variance") to Section 2.3 to validate the reconstruction step.
3. Provide a more mechanistic explanation for why text+audio Linear PCA underperforms text Linear all-voxels on CC_norm — this is a meaningful anomaly for the paper's conclusions about when PCA helps.
4. Surface the DIMLP comparison as the primary evidence rather than a sub-subsection.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>