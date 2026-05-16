Now I have all the information I need. Let me synthesize the final review.

## Summary

The paper proposes Spectral Contrastive Regression, a method for improving generalization in regression tasks through two auxiliary losses: (1) \(L_{std}\), which minimizes the standard deviation of the feature-label proportional distance to create smoother embeddings, and (2) \(L_{svd}\), which aligns the spectral norms of feature matrices from real and C-Mixup augmented distributions to bound domain discrepancy. Experiments on eight benchmark datasets (both ID and OOD) show the method achieving strong results against several baselines.

## Strengths

- **Novel approach to regression generalization.** The paper identifies a genuine limitation in prior work (RML's assumption of a constant feature-label proportion) and proposes modeling it as a variable mapping function. The \(L_{std}\) loss that minimizes variance of the proportional distance is a clean, well-motivated idea that differs from existing approaches like RML (scale-only) and RankSim (order-only).

- **Consistent empirical performance across diverse benchmarks.** On ID datasets (Table 1), the method achieves the lowest RMSE/MAPE on all three datasets. On OOD datasets (Table 2), it achieves best or second-best average/worst-domain results in 10 out of 12 reported metrics across Crimes, SkillCraft, DTI, and RCF-MNIST. On MPI3D (Tables 3&4), the full method achieves best MSE/MAE in 5 out of 6 transfer tasks, and the spectral norm alignment is shown to outperform Frobenius and nuclear norm alternatives.

- **Well-designed ablation on MPI3D comparing norm choices.** The comparison of spectral norm against Frobenius and nuclear norm for domain alignment (Tables 3&4) provides concrete empirical evidence for the design decision, and the result (spectral norm performs best) is consistent with the theoretical argument that it provides the tightest upper bound.

- **t-SNE visualizations offer qualitative support.** Figure 1 shows that \(L_{std}\) produces more discriminative and less dispersed embeddings compared to baselines including RML and RankSim, providing visual evidence that variance reduction improves feature structure.

## Weaknesses

### Fatal
None.

### Major

- **Experimental comparisons are not fully controlled for the fine-tuning protocol.** The paper's method benefits from a specialized fine-tuning strategy (freeze top layers of a C-Mixup pretrained network, fine-tune bottom layers). For ID experiments, the paper states it provides "the result of RML combined with our fine-tuning method" (line 218), but it is unclear whether RankSim, FDS, and other baselines received the same pretreatment. Tables 1 and 2 mark results with † (reported by Yao et al., 2022) and * (reproduced based on Yao et al.'s code), but it is not specified whether the reproduced baselines used the same freeze-and-fine-tune protocol. If the proposed method alone benefits from this engineering choice, the reported improvements may be partially due to the FT strategy rather than the proposed losses. An "FT only (MSE)" baseline under the same protocol is needed to isolate each loss's contribution.

- **No standard deviations or confidence intervals.** All results are averaged over three runs with no variance reported (lines 218, 240). Three seeds is too few to assess reliability, especially given that reported differences are sometimes small. Without error bars, the reader cannot determine whether observed improvements are statistically meaningful.

- **The Lipschitz continuity claim is stated without support.** The paper asserts (line 135): "Clearly, \(L_{std}\) constrains the predictor \(p\) as a Lipschitz continuous function satisfying Remarks 1 and 2." No proof or argument is given connecting the variance of a batch-level ratio to the Lipschitz constant of the predictor. While the heuristic motivation is reasonable, this is presented as a formal property without justification.

- **Incomplete ablation on OOD datasets.** On MPI3D, both \(L_{std}\) and \(L_{svd}\) are evaluated, including ablations of each individually. But on the main OOD datasets (Table 2), the combination \(L_{std}+L_{svd}\) is compared against FT+\(L_{std}\) and other baselines, while FT+\(L_{svd}\) alone is not shown. This makes it difficult to attribute gains to each component in the OOD setting.

### Minor

- **The proof of Theorem 2 contains a notational error that undermines readability.** The proof (lines 156-168) writes \(|\mathcal{L}(h'',0) - \mathcal{L}(h'',0)|\) where the intended quantities are \(\mathcal{L}_P(h'',0)\) and \(\mathcal{L}_Q(h'',0)\) — the distribution subscripts are dropped. While the intended meaning is clear from context and the theorem itself is correct (the bound follows from the definition of discrepancy distance), the sloppiness weakens the paper's theoretical presentation. This is a presentation flaw, not a fatal error.

- **The connection between Theorem 1 and the \(L_{std}\) loss is heuristic, not deductive.** Theorem 1 gives an upper bound on \(\|f_i - f_j\|_p\) in terms of \(\|y_i - y_j\|_p\) under the optimal linear predictor. The paper then proposes minimizing the standard deviation of \(d_r\) to "acquire a flatter proportion map" (line 129). The theorem shows the ratio is bounded but does not imply that minimizing its variance is the correct objective. This is a reasonable heuristic motivation but is presented as a tighter logical consequence than it is.

- **The t-SNE visualization (Figure 1) is presented in the ID Generalization section (Section 4.2) but uses the DTI dataset**, which is an OOD dataset described in Section 4.3. This presentational inconsistency is confusing.

- **MPI3D baseline fairness is not fully documented.** The paper states that the fine-tuning strategy is not used on MPI3D (line 247), but comparisons against IRM, CORAL, etc. do not detail whether all methods share the same backbone, optimizer, and training schedule. The absence of this detail makes the MPI3D comparisons harder to interpret.

### Trivial

- In the proof of Theorem 2, the transition from \(\mathcal{L}(h',h) = \mathcal{L}(h-h',0)\) to the final inequality skips intermediate steps that would clarify the bound. Adding these steps would improve readability.

## Nice-to-Haves

- An "FT only (MSE)" baseline under the same freeze-and-fine-tune protocol would cleanly isolate the effect of each proposed loss.
- A comparison of full fine-tuning vs. freeze-and-fine-tune (with and without the proposed losses) would validate the claimed ID-OOD trade-off mitigation.
- A brief discussion of failure cases or conditions where the method underperforms would improve the paper's honesty and utility.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that Theorem 2's proof is invalid/fatal.** The harsh critic claims the proof writes two identical terms yielding a zero bound, "invalidating the stated theorem." In fact, the missing distribution subscripts on \(\mathcal{L}\) are a notational oversight — the intended quantities are \(\mathcal{L}_P\) and \(\mathcal{L}_Q\), and the theorem's bound follows correctly from the definition of discrepancy distance. The proof is sloppy but not incorrect. Moved to Minor.

- **Criticism that "the leap from Theorem 1 to minimizing \(L_{std}\) is unsubstantiated."** The critic treats this as a structural flaw, but the paper's framing is explicitly heuristic: "Hence, we minimize the standard deviation of \(d_r\) to acquire a flatter proportion map" (line 129). This is reasonable motivation, not a rigorous derivation. Kept in Minor with softened framing.

- **Criticism about "narrative misrepresents RML."** The critic claims the paper "slightly misrepresents" RML. This is a subjective interpretive disagreement, not a verifiable weakness. Removed.

- **Criticism that RankSim/Lipschitz claim is "unsupported speculation."** The paper explicitly uses tentative language ("This characteristic might contribute...", "which supports this hypothesis" — line 225). It is not presented as proven fact. Removed.

- **Criticism about "missing ablation on fine-tuning strategy."** This is moved to Nice-to-Haves as it is a desirable addition that would strengthen but not invalidate the contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the paper's confidently stated theoretical framing ("Clearly, \(L_{std}\) constrains the predictor \(p\) as a Lipschitz continuous function") and what is actually established (heuristic motivation plus empirical results). This suggests the paper would be stronger if it presented itself as an empirically motivated method with heuristic justification, rather than claiming rigorous theoretical grounding that does not fully hold. The most actionable insight from the reviews is that the experimental evaluation, while extensive, would benefit from tighter controls on the fine-tuning protocol across baselines and standard measures of variability.

## Suggestions

1. Provide error bars / standard deviations for all metrics (three seeds is sufficient if variance is reported).
2. Add an "FT only (MSE)" baseline under the same freeze-and-fine-tune protocol to isolate each loss's contribution.
3. Clarify in the experimental setup which baselines received the same FT pretreatment and which were taken from published results without retraining.
4. Show FT+\(L_{svd}\) alone on OOD tables to enable component-level attribution.
5. Either provide a rigorous argument for the Lipschitz continuity claim or soften the language to "encourages" or "tends to produce" rather than "constrains."
6. Fix the missing distribution subscripts in the proof of Theorem 2 and add intermediate steps to make the derivation clear.
7. Move the t-SNE visualization discussion to the OOD section since it uses the DTI dataset, or add a note explaining why it appears under ID generalization.

## Score and Decision

The paper tackles an under-explored problem (regression generalization) with a well-motivated combination of losses and shows promising results across multiple benchmarks. However, the experimental confounds regarding the fine-tuning protocol prevent clean attribution of the reported gains, the lack of variance reporting makes it difficult to assess significance, and the theoretical framing is overstated relative to what is established. These are addressable issues but non-trivial.

**Originality**: Good — the approach of modeling the proportion as a variable and using spectral norm alignment for regression OOD is novel.
**Importance of research question**: High — regression generalization is relatively underexplored.
**Claims well-supported**: Partially — the empirical evidence is suggestive but confounded by unequal baselines and missing variance.
**Soundness of experiments**: Moderate — good breadth (8 datasets) but insufficient controls and missing ablations.
**Clarity of writing**: Adequate — the method is described clearly, but the theoretical sections are sloppy.
**Value to community**: Moderate — the losses are simple and could be useful building blocks for regression tasks.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>