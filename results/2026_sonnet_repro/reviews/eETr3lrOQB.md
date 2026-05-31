Now let me run calibration searches to anchor the score.Round 1 bracket: The paper likely falls in the **5–7** range. The core idea is legitimate and useful, with solid empirical work, but has some framing/evaluation confounds. Let me narrow.Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

VQ-Transplant is a two-stage framework for replacing the VQ module in a frozen, pre-trained visual tokenizer (specifically VAR) without end-to-end retraining: Stage I substitutes the VQ module using a quantization-only loss, and Stage II adapts the decoder via lightweight adversarial fine-tuning (5 epochs on ImageNet-1k) to realign its priors with the new quantization space. The paper also contributes MMD-VQ, a distribution-matching quantization method that uses Maximum Mean Discrepancy to align feature and codebook distributions, avoiding the Gaussianity assumption of prior Wasserstein VQ. The combined system achieves better r-FID than the original VAR tokenizer (0.81 vs 0.92) at roughly 21.8× lower GPU-hour cost, under the assumption that the base pre-trained VAR tokenizer is already available.

---

## Strengths

1. **Practical, well-motivated problem formulation**: The paper identifies a concrete bottleneck — that VQ algorithm exploration is blocked by the 960 GPU-hour cost of end-to-end tokenizer training — and proposes a structurally sensible solution. The two-stage decomposition (VQ substitution → decoder adaptation) is clean and technically sound.

2. **Decoder adaptation works well**: Table 3 shows that Stage I alone leaves a large decoder-quantization mismatch (e.g., MMD VAR K=8192 r-FID degrades from 0.92 to 1.49 post-substitution), but five epochs of adversarial decoder adaptation recovers and surpasses the original baseline (0.81 r-FID), with Figure 2 providing visual confirmation. The ablation over adaptation epochs (Table 5) clearly demonstrates a consistent improvement curve extending to 20 epochs.

3. **Framework generalizes across five VQ algorithms**: Tables 3 and 7 show that Vanilla VQ, EMA VQ, Online VQ, Wasserstein VQ, and MMD VQ all integrate cleanly under the two-stage protocol in both multi-scale and fixed-scale configurations. Distribution-alignment methods (Wasserstein, MMD) achieve consistently lower quantization error and 100% codebook utilization, confirming the framework is permissive of diverse VQ designs.

4. **MMD-VQ achieves state-of-the-art reconstruction on ImageNet-1k in its setting**: Across multi-scale (Table 3) and fixed-scale (Table 7) settings with comparable token counts, MMD VQ consistently achieves lower r-FID than competing methods including Vanilla, EMA, Online VQ, and Wasserstein VQ. MMD VAR K=8192 reaches 0.81 r-FID, beating the baseline VAR of 0.92, with 100% codebook utilization.

---

## Weaknesses

### Fatal
None.

### Major

- **Token count confound in cross-dataset comparisons (Tables 8–10)**: All VQ-Transplant entries in the cross-dataset tables use **512 tokens**, while every cited baseline (RQVAE, VQGAN, VQGAN-FC, VQGAN-EMA, VQGAN-LC, VQ-WAE, MQVAE) uses **256 tokens**. Doubling the token count substantially increases representational capacity and is among the strongest predictors of lower r-FID in discrete tokenizers — for reference, on ImageNet-1k, RQVAE goes from 3.20 r-FID at 256 tokens to 2.69 at 512 and 1.83 at 1024 (Table 2). The paper's claim in Section 5.3 that "VQ-Transplant achieves state-of-the-art reconstruction performance across all three benchmarks" is thus confounded: the improvement on FFHQ (1.21 r-FID vs. baselines at 3.81+) and CelebA-HQ/LSUN-Churches cannot be attributed to the framework alone without a token-matched baseline. This is the most significant empirical weakness and directly affects the core cross-dataset generalization claim.

### Minor

- **Efficiency framing omits pre-training prerequisite**: The "95% cost reduction" claim in the abstract and "21.8× speedup" in Table 1 compare VQ-Transplant's 44 GPU-hours against VAR's 960 GPU-hours of full training, but VQ-Transplant requires a pre-trained VAR tokenizer as input (itself costing 960 GPU-hours). The legitimate efficiency claim is an **amortization argument**: if a researcher downloads or already holds a pre-trained VAR model, then each new VQ experiment costs only 44 GPU-hours rather than 960. This is genuinely useful, but Table 1's presentation makes it appear as a direct training-cost comparison between two systems that accomplish the same thing from scratch, which is inaccurate. A break-even analysis (how many VQ variants must one run for VQ-Transplant to be cheaper overall?) would make the argument more precise and honest.

- **LPIPS degradation not acknowledged in fidelity claims**: In Table 3, all adapted configurations yield worse LPIPS than the original VAR tokenizer (MMD VAR K=4096: 0.108 vs. 0.100; K=8192: 0.104 vs. 0.100; Wasserstein VAR K=4096: 0.109; K=8192: 0.104). The paper claims "superior reconstruction fidelity" without scoping this to r-FID and r-IS only, creating an inconsistency. The multi-metric characterization should either explicitly note the LPIPS regression or explain why it is acceptable given r-FID/r-IS improvements.

- **Marginal and inconsistent MMD-VQ advantage over Wasserstein VQ**: At K=4096, both methods have identical quantization error (0.255) and nearly identical post-adaptation r-FID (0.91 vs. 0.93). At K=8192, differences are 0.234 vs. 0.240 in error and 0.81 vs. 0.83 in r-FID. On FFHQ (Table 8), Wasserstein VQ outperforms MMD VQ at K=32768 (1.21 vs. 1.37 r-FID). The theoretical motivation — that visual feature distributions are non-Gaussian, requiring MMD's non-parametric alignment — is not supported by any empirical characterization of feature distributions. The advantage of MMD-VQ over Wasserstein VQ is real but small and domain-dependent; overstating it as a compelling second contribution weakens the paper.

### Trivial

- The specific σ values used in the multi-Gaussian kernel (Eq. 5) are not reported in the main text, only referenced as "multiple σ values." For reproducibility, these should be stated (or at minimum, a sensitivity analysis described).

---

## Nice-to-Haves

- An explicit amortization analysis (break-even number of VQ experiments) would sharpen the democratization argument and make the efficiency contribution comparable to prior work in a principled way.
- At least one token-matched baseline in the cross-dataset tables (e.g., a fully trained VQGAN with 512 tokens on FFHQ) would resolve the main ambiguity in the cross-dataset results.
- A brief characterization of the actual distribution shape of visual encoder features (e.g., measuring excess kurtosis or fitting Gaussian models to encoder statistics) would ground the MMD-VQ motivation empirically rather than relying purely on theoretical flexibility arguments.
- Table 5 (adaptation epochs 5–20) implicitly raises the question of where "lightweight adaptation" ends and standard decoder fine-tuning begins. Clarifying this boundary, or reporting the additional GPU-hours for extended adaptation, would help practitioners scope the method correctly.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "From-scratch comparison is a strawman"**: The paper itself acknowledges in Section 5.1 that "discrete tokenizers typically require hundreds of epochs to achieve high-quality visual reconstruction when trained from scratch," so the comparison in Table 6 is offered as a same-budget (wall-clock) demonstration rather than as the primary efficiency argument. It is a weak comparison but not a strawman.

- **Harsh critic: LDM-16 failure is under-addressed**: The paper explicitly reports and acknowledges limited LDM-16 compatibility in Section 5.1 with a note that full discussion is in Appendix D. The appendix was stripped from this submission; this is a parser artifact, not an authoring omission.

- **Harsh critic: Generalization on face datasets weakened because OpenImages contains faces**: The paper itself foregrounds this concern in Section 5.3 ("Can the framework generalize to datasets structurally distinct from both ImageNet-1k and OpenImages?"), making it a known limitation rather than a blind spot.

- **Strength Finder strength "cross-dataset generalization" (strong)**: Downgraded — as shown above, the cross-dataset results have a token count confound that prevents strong claims about generalization.

- **Strength Finder: "From-scratch comparison highlights transplant efficiency"**: Downgraded — the from-scratch models only ran for 5–7 epochs, which is far below the hundreds of epochs typically needed. This comparison is not informative as a standalone efficiency baseline, only as a same-budget comparison.

---

## Novel Insights

The paper's most actionable insight is the Stage I → Stage II decomposition: quantization error reduction alone does not translate to reconstruction improvement (MMD VAR K=8192 moves from 0.92 → 1.49 r-FID post-substitution before adaptation), but a lightweight adversarial decoder adaptation (5–20 epochs) rapidly converts reduced quantization error into reconstruction gains. This suggests the decoder adaptation cost is the binding constraint for VQ research, not the quantization training itself — an observation that has implications beyond VQ-Transplant for any scenario where a fixed decoder must accommodate changes in the quantized latent space.

---

## Suggestions

1. Add a 512-token baseline in Tables 8–10 (e.g., train VQGAN with 512 tokens on FFHQ) to isolate the contribution of the framework from the contribution of token count in the cross-dataset results.
2. Restructure the efficiency narrative in the abstract and Table 1 around amortization: "For a researcher already holding a pre-trained VAR tokenizer, each VQ experiment costs 44 GPU-hours vs. 960 for from-scratch; break-even is N experiments."
3. Scope "superior reconstruction fidelity" claims explicitly to r-FID and r-IS, and explain the LPIPS regression or add a note that LPIPS does not favor the adapted models.
4. Add σ bandwidth values and a brief sensitivity check for MMD in the main text.

---

## Score and Decision

**Round 1 bracket**: The paper plausibly sits between **5 and 7**. It addresses a real problem with clean experiments, but has the cross-dataset token confound and modest MMD-VQ contribution.

**Round 2 anchors**:
- **yGnsH3gQ6U** (BSQ tokenizer, 5.75, Accept): More technically novel (no explicit codebook, scalable to arbitrary dimensions, image+video), with state-of-the-art results across more benchmarks and a cleaner evaluation. VQ-Transplant is **comparable to or slightly below** BSQ — both address the VQ tokenization space; VQ-Transplant's framework contribution is useful but narrower in scope and with an evaluation confound BSQ does not have.
- **gMGUa8C0tL** (TaCA hot-plugging, 5.25, Reject): Conceptually similar (replacing a module in a pre-trained system without retraining downstream components). Rejected mainly for incremental approach and marginal improvements in its own evaluation. VQ-Transplant is **clearly stronger** than TaCA — it shows much larger performance gaps, provides more thorough ablations, and addresses a more pressing practical problem with quantitative efficiency analysis.
- **3TnLGGHhNx** (BPE on quantized visual, 6.0, Accept): Broader scope, novel tokenization paradigm, broader downstream evaluation. VQ-Transplant is **weaker** on novelty but provides more direct practical utility.

Verdict: VQ-Transplant sits above TaCA (5.25) and is comparable to BSQ (5.75), with the cross-dataset confound as the key factor preventing a higher score. The core contribution is valid and useful; the evaluation flaw in Tables 8–10 is significant but fixable.

**All anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| IqGVIU4rvM.md | 2.50 | R1 | Clearly weaker; poorly executed |
| TDzAqTqDHV.md | 3.00 | R1 | Weaker; less relevant domain |
| 6Mdvq0bPyG.md | 3.00 | R1 | Weaker; LLM quantization |
| 2HdZPEQUig.md | 3.00 | R1 | Weaker; different task |
| yGnsH3gQ6U.md | 5.75 | R1/R2 | Comparable but broader and cleaner evaluation |
| 3TnLGGHhNx.md | 6.00 | R1/R2 | Slightly stronger; broader contribution |
| FlvtjAB0gl.md | 6.25 | R1/R2 | Stronger; more comprehensive contribution |
| tNxr38vfYR.md | 5.00 | R1 | Weaker on average; high variance scores |
| GMwRl2e9Y1.md | 8.00 | R1 | Clearly stronger; rigorous theoretical + experimental |
| 2dnO3LLiJ1.md | 8.00 | R1 | Different task; much higher impact |
| gU58d5QeGv.md | 8.00 | R1 | Different task; much higher impact |
| nGiGXLnKhl.md | 8.00 | R1 | Different task; architecture paper |
| TVg6hlfsKa.md | 7.25 | R2 | Stronger; broader and cleaner evaluation |
| gMGUa8C0tL.md | 5.25 | R2 | Weaker; VQ-Transplant is more impactful |
| KxQRHOre9D.md | 6.25 | R2 | Different domain |
| pjtIEgscE3.md | 6.25 | R2 | Different domain |

**Round 1 bracket**: 5–7. **Round 2 narrowing**: Places the paper between TaCA (5.25, below) and BSQ (5.75, comparable). The cross-dataset confound is a real methodological issue but does not invalidate the core ImageNet-1k results. The paper is better than TaCA on practical merit and comparably novel to BSQ, but with a key evaluation flaw. Score: **5.5**.

**Originality**: Moderate — the two-stage "substitute-then-adapt" idea is natural given VQ-Transplant's problem setup, but the systematic empirical study and MMD-VQ extension add value.  
**Importance**: Moderate-high — reduces the compute barrier for VQ research meaningfully.  
**Claim support**: Partially adequate — ImageNet-1k results are well-supported; cross-dataset results are confounded.  
**Experiment soundness**: Good for the main results; the cross-dataset tables need a token-matched control.  
**Writing clarity**: Good — the paper is easy to follow and well-organized.  
**Community value**: Moderate — practical for researchers in discrete visual tokenization.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>