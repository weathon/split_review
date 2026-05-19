- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 8, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces MotionDreamer, a generative masked transformer for one-to-many motion synthesis from a single reference motion sequence. The key innovations are (a) a codebook distribution regularization technique (KL divergence toward a uniform prior) that mitigates codebook collapse under extreme data scarcity, and (b) a localized transformer architecture with sliding window attention (SlidAttn) and overlap attention fusion (AttnFuse) that prevents overfitting by narrowing the receptive field. Experiments on the SinMotion benchmark show that MotionDreamer achieves the best harmonic mean across five metrics (30.0 vs. 27.4 for the next best, SinMDM), and ablation studies convincingly demonstrate that both proposed components are individually necessary.

## Strengths

1. **Codebook distribution regularization demonstrably mitigates codebook collapse (Section 3.1.1, Table 2, Figure 5).** The addition of \(\mathcal{L}_{\mathrm{token}}\) (KL divergence to uniform prior) raises VQ perplexity and improves generation quality. Figure 5 provides clear qualitative evidence: without regularization, fine-grained local patterns (e.g., details in "house dancing") are blurred or lost; with it, patterns are faithfully preserved. This is a clean, well-ablated contribution.

2. **Sliding window local attention (SlidAttn + AttnFuse) is essential for avoiding overfitting (Section 3.2.1, Table 3, Figure 6).** Table 3 shows that a standard global-attention transformer collapses entirely (diversity of 0.0), while the proposed SlidAttn backbone achieves balanced metrics. Figure 6 visually demonstrates that AttnFuse produces coherent transitions (e.g., "blackflip" → "handstand") whereas average pooling yields unnatural artifacts. The ablation is clear and directly supports the core claim.

3. **State-of-the-art harmonic mean on the SinMotion benchmark (Table 1).** MotionDreamer achieves the highest harmonic mean (30.0) among GAN-based (Ganimator: 4.6), diffusion-based (SinMDM: 27.4), and non-parametric (GenMM: 15.9) baselines. The user study (Figure 4) further shows MotionDreamer scoring highest in perceptual coverage and diversity. The ablation study (Table 3, standard transformer collapse → 1.0 harmonic mean) provides compelling evidence that the proposed architecture is necessary for the observed performance.

4. **Applications demonstrate versatility beyond unconditional generation (Section 4.5).** The paper shows plausible results for crowd animation, temporal editing (in-painting a subpart), and beat-aligned dance synthesis — all from a single reference motion and without task-specific re-engineering of the core model.

## Weaknesses

### Fatal
None.

### Major

1. **Inference process is critically underspecified (Section 3.2.2, one sentence).** The entire inference description reads: *"At the inference stage, we synthesize the novel motion ... using Local-M in a sliding window based auto-regressive manner, by progressively fill in a fully-masked template token sequence."* This mixes two different paradigms: iterative masked prediction (progressive filling, as in MaskGIT) and autoregressive decoding (window-by-window). These operate under different context assumptions — masked decoding is bidirectional, while "auto-regressive" implies causal. How the sliding-window bidirectional attention (SlidAttn) operates during autoregressive decoding is not explained. There is no pseudocode, no step-by-step description, and no discussion of how sequence length is handled or how the fully-masked template is initialized and updated. This makes the generation process non-reproducible as presented.

### Minor

1. **Overclaimed quantitative result (Section 4.2).** The paper states: *"Our method achieves state-of-the-art results on individual metrices (1)-(5)"* — implying it is best on all five individual metrics. Yet in the very same paragraph the paper acknowledges *"GenMM reaches higher coverage."* Since Coverage is metric (1), the claim is contradictory. This should be corrected to reflect the actual standing (best harmonic mean, and best or competitive on most individual metrics).

2. **Coverage metric weighting is not adequately justified (Section 4.1).** The paper gives highest weight to the Coverage metric in the harmonic mean, yet also acknowledges that GenMM achieves higher coverage than MotionDreamer while qualitatively failing to preserve complex patterns (Pattern A in Figure 3). This suggests the metric may reward superficial patch-level matches rather than genuine structural preservation. The paper does not validate the metric (e.g., by correlating with user-study coverage ratings) or justify the weighting choice. This does not invalidate the results, but it weakens the claim that a 19% harmonic mean improvement cleanly measures real gains.

3. **User study would benefit from statistical rigor (Section 4.2).** The study involves 20 participants × 3 reference motions × 3 samples per method = 180 ratings per dimension. The paper reports average scores and distributions but does not report whether the observed differences (e.g., coverage: 4.1 vs. GenMM's 3.2) are statistically significant. Given the modest sample, significance testing (e.g., Wilcoxon signed-rank) would strengthen the perceptual claims.

4. **No per-sequence breakdown or failure case analysis.** Results are averaged over 60 diverse sequences (human and animal, long and short). There is no discussion of where MotionDreamer might struggle (e.g., very short sequences, highly irregular patterns). Characterizing failure modes would strengthen the paper's contribution.

5. **No runtime or parameter count comparison.** For a method that trains a VQ codebook + transformer, it would be useful to compare training/inference speed against the non-parametric GenMM and the diffusion-based SinMDM. This is a minor omission.

### Trivial
None.

## Nice-to-Haves

- A pseudocode or explicit step-by-step of the inference procedure (this is actually a Major weakness above, not merely nice-to-have).
- Correlation analysis between the automated Coverage metric and user-study coverage ratings.
- Runtime/compute comparison with baselines.
- Confidence intervals or statistical significance tests for the user study.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Criticism about missing hyperparameters (window size W, stride S, codebook size K, etc.).** Removed per the instruction to remove nitpicks about undisclosed hyperparameters. These details may also reside in the supplementary material (stripped by the parser). The paper describes the method at the architectural level clearly enough; precise values, while helpful, do not prevent understanding the contribution.

2. **Criticism that the "state-of-the-art" claim is factually incorrect based on specific table values (SinMDM 42.6 vs. MotionDreamer 41.0 on Local Diversity).** The specific numerical claim cannot be independently verified from the text alone (the table is rendered as an image). The retained weakness (#1 under Minor) captures the verifiable contradiction in the paper's own text (claiming SOTA on all five metrics while acknowledging GenMM has higher coverage), which is sufficient.

3. **Criticism that the coverage metric "risks inflating metric standing."** This is an area-of-concern speculation rather than a specific identified flaw. The retained weakness (#2 under Minor) captures the substantiated concern (metric weighting not justified; paper itself notes disconnect between coverage score and qualitative fidelity), stripped of the speculative language.

## Novel Insights

The two reviews converge on a key observation: the paper's core contribution is well-supported by strong ablation evidence (standard transformer collapses, codebook regularization improves perplexity), but the evaluation section contains a tension between ambitious claims and the actual evidence. The "19% improvement on harmonic mean" is impressive, but the paper over-reaches by claiming best on all five individual metrics. The inference section is a genuine gap — a one-sentence description is unusual for a method paper and cannot be dismissed as a formatting artifact. The paper would be significantly strengthened by resolving this tension: correct the overstated claim, flesh out the inference description, and acknowledge the limitations of both the coverage metric and the user study. The underlying method and its empirical support are solid.

## Suggestions

1. **Correct the claim in Section 4.2.** Replace "state-of-the-art results on individual metrices (1)-(5)" with an honest summary (e.g., "best harmonic mean overall, best or competitive on most individual metrics, with GenMM leading on coverage but sacrificing diversity and qualitative fidelity").
2. **Expand Section 3.2.2 (Inference) substantially.** Provide a step-by-step algorithm or pseudocode explaining: (a) how the fully-masked template is initialized, (b) how tokens are progressively predicted (are all [MASK] tokens predicted in parallel each step, or is it truly autoregressive?), (c) how the sliding window handles the changing mask pattern, and (d) how the generation length \(L_g\) is managed.
3. **Validate or clarify the coverage metric weighting.** Either show correlation between the automated Coverage metric and user-study coverage ratings, or re-weight the harmonic mean and verify the conclusions are unchanged.
4. **Add significance tests to the user study.** A simple paired test (e.g., Wilcoxon signed-rank) for pairwise comparisons between MotionDreamer and each baseline on each dimension would substantially strengthen the perceptual claims.
5. **Add a brief discussion of failure modes or per-sequence variance.** Even a sentence acknowledging cases where the method underperforms would improve scientific transparency.
