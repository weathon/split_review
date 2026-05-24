Now I have all the evidence needed. Let me produce the final consolidated review.

---

## Summary

AdaSVD proposes two techniques for SVD-based LLM compression: **adaComp**, which alternately updates the truncated singular matrices via Moore-Penrose pseudoinverse to compensate for truncation error, and **adaCR**, which assigns layer-specific compression ratios based on the cosine similarity between each layer's input and output. On LLaMA2-7B at 60% compression, AdaSVD achieves WikiText-2 perplexity 50.33 vs. SVD-LLM's 89.90, and improvements hold across multiple LLM families and compression ratios (40–80%). The method also combines effectively with GPTQ quantization.

## Strengths

1. **Consistent and substantial perplexity reduction over prior SVD methods.** Table 1 shows that on LLaMA2-7B, AdaSVD achieves WikiText-2 PPL of 14.76, 25.58, and 50.33 at 40%, 50%, and 60% compression, vs. SVD-LLM's 16.11, 27.19, and 89.90 — relative improvements of 8%, 6%, and 44% respectively. The advantage is maintained across PTB and C4 datasets and across five zero-shot reasoning tasks.

2. **adaComp independently reduces truncation error.** Table 3a isolates the effect: on the base method (whitening + SVD truncation), enabling adaComp lowers PPL on WikiText-2 from 78.82 to 50.33 at 60% compression (36% reduction). Figure 3(a) and 3(c) further show that the MPPU update converges stably and that the output distribution after adaComp more closely matches the original model's distribution.

3. **adaCR outperforms uniform compression ratio assignment.** Table 3b shows that replacing a constant compression ratio with adaCR reduces WikiText-2 PPL from 69.46 to 50.33 at 60% compression (28% improvement). This directly demonstrates that the importance-aware allocation provides a meaningful benefit.

4. **Moore-Penrose pseudoinverse update ensures stable optimization.** Figure 3(a) plots MSE over 25 update steps: the proposed MPPU converges smoothly while the naive update (NU based on direct matrix inversion) exhibits large fluctuations, validating the numerical stability motivation.

5. **Stack-of-batch (SoBC) strategy enables more calibration data under memory constraints.** Figure 3(b) shows SoBC yields faster and more stable MSE reduction than naive concatenation. Section 3.1 explains how it pools N samples into M buckets, allowing up to 256 calibration samples on a single 80GB GPU.

6. **Orthogonal combination with weight quantization yields additional gains.** Table 4 shows AdaSVD+GPTQ-INT4 achieves 22.55 PPL at 40% compression vs. SVD-LLM+GPTQ's 33.56, and the advantage holds across 40–80% compression, confirming complementarity with quantization.

## Weaknesses

### Major

- **The adaCR importance measure (cosine similarity between X and WX) lacks theoretical justification for why high similarity implies high importance.** The paper defines I(W) = similarity(X, Y) with Y = WX and states that "the first layer always weighs the most importance, suggesting that we should retain more weight on it" (Section 3.2, Eq. 17, and Fig. 4). The connection between high cosine similarity and a layer's sensitivity to SVD truncation is not argued — it is asserted. If the output is very similar to the input (high cosine similarity), one could equally argue the layer is close to identity and could be compressed aggressively. The empirical success of adaCR suggests the measure does correlate with importance in practice, but the paper should explain *why*. Without this justification, the component rests on an intuitive leap rather than a principled foundation.

- **Inconsistent baseline comparison at 50% compression in Table 3a.** AdaSVD without adaComp (whitening + SVD truncation only) gives WikiText-2 PPL 30.00 at 50% compression, which is *worse* than SVD-LLM's 27.19. At 40% it is better (15.47 vs. 16.11), and at 60% it is better (78.82 vs. 89.90). Since both methods claim to use the same whitening and SVD truncation, this non-monotonic discrepancy suggests differences in implementation (calibration data split, random seed, or subtle whitening details). The paper states that it uses the official repository for SVD-LLM, but does not explain why the base method underperforms at one specific compression ratio. This needs investigation; otherwise, readers cannot be fully confident that the gains from adaComp are not partially artifacts of an unmatched baseline.

### Minor

- **The alternating update using the Moore-Penrose pseudoinverse is standard alternating least squares (ALS).** The paper presents this as a novel contribution, but the connection to well-established ALS / matrix-completion literature is not acknowledged. While applying ALS to SVD truncation compensation in LLMs is reasonably new, the technical machinery itself is standard. Acknowledging prior ALS work would give a more accurate picture of the contribution.

- **More iterations of adaComp can hurt performance at lower compression ratios (Table 3c).** At 40% compression, 1 iteration gives PPL 14.76 while 15 iterations give 15.84. The paper attributes this to overfitting (Section 4.3), which is plausible, but provides no analysis (e.g., a validation curve of reconstruction loss vs. iterations). Understanding why overfitting occurs with only 256 calibration samples and a low-rank structure would strengthen the paper.

- **The CR formula CR = mrr + I_n·(trr − mrr) can produce values exceeding the target retention ratio (or 1.0) when I_n is large; no clipping is mentioned.** Figure 4 shows normalized importance values can exceed 2 for some layers (e.g., first layers of several models). While in practice the resulting CR values may still be ≤ 1.0, the paper should state how out-of-range values are handled.

- **Limited model scale.** Experiments are on 7B–8B models. For SVD-based methods, which require decomposing large weight matrices, demonstrating scalability to 13B or 70B would significantly strengthen the practical contribution.

### Trivial

None.

## Nice-to-Haves

- Adding a GPTQ-only (no SVD) baseline row in Table 4 would help readers contextualize whether SVD compression is worthwhile at these rates relative to pure quantization.
- An ablation of whitening (adaComp without whitening) would help isolate where the gains come from.
- Providing validation curves (reconstruction MSE vs. iteration) for the adaComp iterations at multiple compression ratios to substantiate the overfitting explanation.

## Removed Points

- **"Narrowing the gap is overstated"** — The paper claims to "narrow" (not "close") the gap between compressed and original models. At 60% compression, improving from 89.90 to 50.33 relative to the original 5.68 constitutes genuine narrowing. The phrasing is appropriate.
- **"SoBC comparison is unfair"** — The paper compares its proposed SoBC strategy against naive concatenation (NC) to show its own method works better. This is a standard ablation, not an unfair comparison.
- **"Perplexity still high at high compression"** — This is a contextual observation about the state of SVD compression, not a specific weakness of AdaSVD.
- **"No comparison with quantization/pruning-only methods"** — The paper explicitly positions itself within the SVD compression sub-area and demonstrates orthogonality to quantization (Table 4). Scope constraints are reasonable.
- **"Missing random seed / reproducibility details"** — The paper states it uses 256 random samples from WikiText-2 following prior work. Additional seed details are a trivial request.
- **"Missing comparison with AdaLoRA"** — AdaLoRA is a fine-tuning method requiring training, which is outside the stated post-training scope.

## Novel Insights

None beyond the paper's own contributions. The two key observations — that post-truncation compensation via alternating updates of U and V improves reconstruction, and that input-output cosine similarity correlates with layer-wise compression sensitivity — are clearly presented in the paper.

## Suggestions

1. **Clarify the adaCR importance measure.** Provide a brief analysis or intuition for why cosine similarity between X and WX correlates with how much the layer degrades under SVD truncation. Alternatively, adopt a loss-based importance measure (e.g., the increase in reconstruction error when the layer's rank is reduced) and show it correlates with the cosine-similarity proxy.
2. **Investigate the 50% compression anomaly in Table 3a.** Run multiple trials with different calibration splits and random seeds for AdaSVD without adaComp and SVD-LLM. Report the variance and explain the non-monotonic behavior.
3. **Add a convergence/validation curve** for adaComp iterations across compression ratios to substantiate the overfitting claim.
4. **Mention CR clipping** for cases where I_n is large enough to push CR > trr.
5. **Acknowledge the ALS connection** in the related work or method section.

## Score and Decision

**Round 1 (Bracketing):** Three queries on "SVD compression of large language models" pulled weak anchors (AA-SVD, ERC-SVD, GFWSVD, Post-hoc LoRA compression) averaging 2.50–3.00, middle anchors (SAES-SVD, DF-SVD, SoCo, CoSpaDi, ALS-ActLR, LeSTD) averaging 4.00–5.50, and strong anchors (>7.5) on unrelated topics. The paper clearly falls in the middle band.

**Round 2 (Narrowing):** Additional queries on "adaptive SVD compression LLM layer importance" and "post-training SVD compression LLM alternating least squares compensation" returned D-Rank (4.00/reject), SAES-SVD (5.00/accept-poster), DF-SVD (5.00/reject), ALS-ActLR (5.00/reject), and LeSTD (5.50/accept-poster). AdaSVD has more comprehensive experiments (more model families and VLMs) than SAES-SVD, but weaker theoretical grounding for its adaCR component. It is comparable to DF-SVD and ALS-ActLR in overall quality. I place it at **5.0**, in the same tier as SAES-SVD (which was accepted as poster at this score).

**Final score: 5.0** — This paper makes a solid empirical contribution to SVD-based LLM compression with clear improvements over SVD-LLM, but the adaCR justification is conceptually underdeveloped and the baseline inconsistency at 50% compression needs resolution. These issues are addressable and do not invalidate the core results, but they lower confidence in the method's framing.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>