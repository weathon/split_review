Now I have all the context I need. Let me write the consolidated review.

## Summary

The paper proposes VQ-Transplant, a framework that enables plug-and-play replacement of the VQ module in pre-trained visual tokenizers (e.g., VAR) without costly end-to-end retraining. The VQ module is substituted while the encoder-decoder is frozen, followed by lightweight decoder adaptation (5 epochs on ImageNet-1k) to realign the decoder with the new quantized space. The paper also introduces MMD-VQ, which uses maximum mean discrepancy for distribution alignment between features and codebook. Experiments show that MMD VAR (VQ-Transplant with MMD-VQ on VAR) achieves 0.81 r-FID vs the original VAR's 0.92 r-FID with a 21.8× reduction in GPU-hours.

## Strengths

- **Novel and practical framework**: VQ-Transplant decouples VQ module development from expensive tokenizer retraining. This is the paper's primary contribution and is genuinely useful for the community — it enables rapid iteration on VQ algorithms without the 100s of GPU-hours typically required. The framework is demonstrated across 5 different VQ algorithms and two tokenizer architectures (VAR, LDM).

- **Extensive and transparent ablation**: The paper provides unusually thorough ablation of the decoder adaptation cost (Tables 4-5 tracking r-FID from epochs 0-20), a direct from-scratch training comparison (Table 6 showing VQ-Transplant significantly outperforms from-scratch even with more training hours), and both multi-scale and fixed-scale VQ configurations. This gives a clear picture of the method's behavior.

- **Cross-dataset generalization**: VQ-Transplant with MMD-VQ and Wasserstein-VQ achieves strong reconstruction on FFHQ, CelebA-HQ, and LSUN-Churches — datasets structurally distinct from the OpenImages/ImageNet training data. The quantitative gains over fully-trained baselines (e.g., r-FID 1.21 vs VQGAN-LC's 3.81 on FFHQ) are substantial.

- **Consistent distribution-alignment advantage**: Across all codebook sizes and both multi-scale/fixed-scale settings, distribution-aligned methods (MMD-VQ, Wasserstein-VQ) consistently achieve lower quantization error and ~100% codebook utilization compared to vanilla VQ, EMA VQ, and Online VQ. This empirically validates the theoretical motivation.

## Weaknesses

### Major

- **Codebook size confounds the headline improvement**: The paper's headline claim ("0.81 r-FID outperforming VAR's 0.92") compares MMD VAR at K=8192 against original VAR at K=4096. When evaluated at the same K=4096, MMD VAR achieves 0.91 r-FID — a marginal 0.01 improvement over VAR's 0.92. The paper also does not test whether VAR's native VQ could benefit from scaling to K=8192 (which may be infeasible, but the limitation is never discussed). The main practical benefit of VQ-Transplant appears to be the ability to cheaply scale up codebook size, not that MMD-VQ is inherently a better quantizer at the same capacity. The paper's framing should separate these two contributions more clearly.

- **MMD-VQ's advantages over Wasserstein VQ are not clearly demonstrated**: The paper claims MMD-VQ is "specifically designed to enable improved compatibility with VQ-Transplant" by overcoming Wasserstein VQ's Gaussian assumption (§4.2). Yet in the cross-dataset experiments (Tables 8-10), Wasserstein VQ matches or outperforms MMD VQ on several metrics (e.g., FFHQ r-FID: Wasserstein 1.21 vs MMD 1.37 at K=32768; LSUN-Churches r-FID: Wasserstein 1.79 vs MMD 1.87). On ImageNet-1k (Table 3, K=8192), Wasserstein VAR achieves 0.83 r-FID vs MMD VAR's 0.81 — a small gap. The paper never provides direct evidence that non-Gaussian feature distributions are better handled by MMD, making the secondary contribution's novelty somewhat unclear relative to the existing Wasserstein VQ baseline.

### Minor

- **Compute comparison conflates multiple factors**: Table 1 compares VQ-Transplant (22h, 2×A100, ImageNet-1k) against the original VAR training (60h, 16×A100, OpenImages). The 21.8× speedup mixes differences in dataset, GPU count, and the method itself. The from-scratch comparison in Table 6 partially addresses this by controlling for dataset and method, but the headline claim ("95% cost reduction") is pinned to the uncontrolled comparison. A controlled experiment (re-training VAR's original setup on ImageNet-1k with similar compute) would make the claim more precise.

- **Baseline comparisons use mismatched token counts**: In Table 8 (FFHQ), MMD VQ and Wasserstein VQ use 512 tokens while the cited baselines (VQGAN-LC, RQVAE) use only 256 tokens. The advantage in expressiveness from doubling the token count is not acknowledged. This makes the headline "state-of-the-art" claim on FFHQ less definitive.

- **L_unique loss unclear for non-distributional VQ methods**: Equation 3 defines the VQ training objective with a uniqueness-enforcing loss L_unique. While clear for MMD-VQ (D²_MMD) and Wasserstein VQ (Wasserstein loss), the paper never specifies what L_unique is for Vanilla VQ, EMA VQ, and Online VQ when evaluated in the framework. The ablation (Tables 3, 7) suggests these methods may simply use γ=0 or omit the second term, but this should be stated explicitly.

### Trivial

None.

## Nice-to-Haves

- An analysis of whether the decoder adaptation causes catastrophic forgetting on OpenImages (the original training distribution of VAR) would be a useful sanity check.
- The paper mentions joint optimization (encoder+decoder+VQ) in the appendix but does not ablate whether freezing the encoder during Stage II is necessary or merely convenient.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"5-epoch framing understates adaptation cost since 20 epochs yields better results"* — Removed. The paper transparently presents the epoch-20 results in Table 5 and Figure 3 and discusses them in §5.1. The claim "only 5 epochs" is still accurate as a lightweight adaptation cost. The paper does not claim 5 epochs is optimal, just sufficient to surpass the original VAR.
- *"Cross-dataset generalization limited to constrained domains (faces, churches)"* — Removed. Scope creep. Medical/satellite imagery is not standard evaluation for visual tokenization. The three tested datasets (faces, churches) are standard benchmarks in this area.
- *"Lower quantization error does not guarantee better reconstruction"* — Removed. The paper explicitly discusses this observation and uses it to motivate decoder adaptation (§5.1, lines 229-231). This is framed as a finding, not a flaw.
- *Missing appendix content / implementation details* — Removed. The parser strips appendix content from all papers; these details exist in the original submission.
- *Generic formatting and citation nitpicks* — Removed per policy.
- *Speculative fatal claims about codebook scaling feasibility* — The claim that VAR "could" benefit from K=8192 is speculative. The paper cannot test what VAR's architecture cannot support.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disentangle the two contributions**: Reposition the paper's main contribution as "a framework that enables cheap scaling of codebook size via VQ module transplantation" rather than claiming MMD-VQ is a superior quantizer. At K=4096, the improvement over VAR is noise (0.91 vs 0.92). The real win is the ability to go to K=8192 cheaply.

2. **Add a controlled compute comparison**: Train the original VAR tokenizer from scratch on ImageNet-1k with 2×A100 for 22 hours and report its r-FID. This would directly quantify the benefit of VQ-Transplant holding dataset and compute constant.

3. **Clarify MMD-VQ's advantages over Wasserstein VQ**: Either provide synthetic experiments showing non-Gaussian distributions where MMD outperforms Wasserstein, or reframe MMD-VQ as a complementary alternative rather than a clearly superior method.

4. **Acknowledge token count mismatch in cross-dataset comparisons**: Note explicitly when MMD VQ uses more tokens than the baselines it's compared against.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Comparison to This Paper |
|--------|-----------|--------------------------|
| GMwRl2e9Y1 (Rotation Trick VQ) | 8.00 | Stronger: cleaner experimental design, principled gradient improvement, extensive controlled comparisons |
| 8ishA3LxN8 (FSQ) | 6.50 | Similar: both propose useful frameworks with some evaluation limitations; FSQ is simpler but the current paper has more thorough ablation |
| WNLAkjUm19 (Discrete Tokenization Role) | 7.00 | Different topic (MIM theory); not directly comparable on method quality |
| mb2ryuZ3wz (How Many Tokens) | 5.75 | Similar: useful idea, solid experiments, some confounds in evaluation |
| nS2DBNydCC (Wasserstein VQ) | 4.75 | Better: this paper addresses the Gaussian assumption limitation, has far more extensive experiments, and contributes a practical framework beyond just a new VQ loss |
| tFV5GrWOGm (ElasticTok) | 6.00 | Similar: both propose practical tokenization improvements with thorough but not perfectly controlled experiments |
| IqGVIU4rvM (Combining VQ-VAE and Diffusion) | 2.50 | Much better: this paper avoids fundamental misunderstandings, has competitive results, and provides rigorous empirical support |

The paper makes a genuine practical contribution (VQ-Transplant) with extensive empirical support. The main weaknesses are confounded headline comparisons and an unclear advantage of MMD-VQ over the existing Wasserstein VQ baseline — issues that are addressable through reframing rather than fatal. Relative to the anchors, the paper sits above the rejected Wasserstein VQ paper (4.75) and the weaker submissions (~2-3), and is comparable to mid-tier accepted papers (5.75-6.50). It does not reach the clarity and experimental rigor of the top-scoring Rotation Trick paper (8.00).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>