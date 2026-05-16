Now I have a complete picture of the paper. Let me produce the consolidated final review.

---

## Summary

This paper proposes OSA (One-step Anti-Noise), a model-agnostic noisy-label mitigation paradigm. The key idea is to use a frozen pre-trained model (e.g., CLIP) as an external estimator to compute cosine similarity between input pairs, then debias this similarity by subtracting the mean similarity of random pairs (capturing the "cone effect" shift), and finally apply a scoring function to convert the debiased similarity into a sample weight that down-weights likely noisy pairs during training. The paper provides theoretical analysis linking the observed clean/noisy boundary to a shifted orthogonal boundary in high-dimensional cone space, and reports strong empirical results across image-text matching, classification, and retrieval tasks with substantial improvements over baselines and a 10× reduction in extra training overhead versus the prior SOTA (NPC).

## Strengths

- **Clear, practical paradigm with strong empirical results.** OSA consistently and substantially outperforms baselines across multiple tasks, noise ratios, and architectures. On MS-COCO 5K at 50% noise, OSA improves R@1 over the previous SOTA (NPC) by 8.6% (i2t) and 7.0% (t2i), and performance drops only ~1.3% from 0% to 50% noise versus NPC's ~5.0% drop (Table 1). The improvements at high noise ratios (60% on Flickr30K, Table 2) are particularly compelling.

- **Computationally efficient and model-agnostic.** OSA requires only one additional forward pass (no backward pass) and adds only ~21 minutes versus NPC's ~226 minutes extra (Table 6). The method works across diverse architectures (ViT, ResNet-152, VGG-19) and tasks (image-text matching, classification, retrieval) without architecture-specific modifications (Tables 3–4).

- **Accurate noise detection.** Using only a zero threshold on the debiased cosine similarity, OSA achieves >99% recall for noise detection (Table 7) and attains a Mean Noise Rank within 6 of the theoretical optimum (Table 5), showing that the similarity-based signal is highly informative.

- **Robustness without domain adaptation.** Zero-shot CLIP as an estimator performs comparably to a domain-adapted version, including on the unfamiliar SDM dataset (Table 7, Section 4.4), which simplifies deployment.

- **Adaptability as a plug-in.** Applying OSA on top of NPC further improves NPC's performance (e.g., +2.9% i2t R@1 at 50% noise, Table 4), demonstrating it can serve as a general enhancement.

## Weaknesses

### Fatal

None.

### Major

- **The scoring function (Eq. 6, \ref{eq:scoring}) is non-monotonic and contradicts its stated design goal.** Let t = s(x,y) − β for t > 0. The function simplifies to w(t) = −t²(t−1) = t²(1−t). This is zero at t=0 and t=1, reaches a maximum of ~0.148 at t=2/3, then *decreases* — so a very clean sample (t=0.9) receives a lower weight (w≈0.081) than a moderately clean sample (t=0.5, w=0.125). This directly contradicts the paper's stated requirement that "the function gradient should increase rapidly as the cosine similarity moves further from zero" (Section 2.4) and the claim that w ∈ [0, 1] (Section 3.2). The maximum of the function is ~0.148, not 1. The paper does not provide the distribution of s−β to explain why this non-monotonic function still yields near-optimal ranking results (Table 5). **This is the single most serious weakness: the core weighting mechanism does not behave as described.** The empirical results may well be robust to this — the ranking analysis suggests the binary threshold (t>0 vs t≤0) dominates — but the paper as written presents a mathematically inconsistent function as its design. The authors should either correct the function to a monotonic form (e.g., max(0, (s−β)²) or a sigmoid) or explicitly justify the non-monotonic shape and re-run experiments.

### Minor

- **Theoretical analysis does not fully support the claimed boundary in trained models.** Theorem 1 proves that cosine similarity ordering is preserved through a *random* neural network (weights drawn i.i.d. from N(0,1/d)). However, the actual estimator (CLIP, ALIGN) is *trained* via contrastive learning, and the paper provides no argument that the same property holds after training reorders the embedding space. The paper's main theoretical claim — that the observed boundary is a shifted orthogonal boundary — is thus supported by an analogy to random networks plus empirical observation (Figure 1), not by a theorem that applies to the actual model used. This is not fatal because the empirical boundary is well-documented, but the framing as "theoretical proof" overstates the rigor. The paper should acknowledge this gap more explicitly.

- **Flickr30K baseline backbone not specified.** For MS-COCO, the paper states all methods use "the same ViT-B/32 CLIP as backbone." For Flickr30K (Table 2), it is not stated whether NCR, DECL, BiCro use the same CLIP backbone or their original architectures. Since the paper's contribution is orthogonal to backbone choice, the fairest comparison is CLIP vs CLIP+OSA (which is shown and is strong), but the claim that "OSA consistently outperforms all models on the R@1 metric" across architectures is hard to interpret without backbone consistency. The paper should clarify the backbone used by each baseline.

- **No statistical significance or variance reported.** All results are single numbers without confidence intervals or multiple seeds. Given that improvements at 0% noise are small (e.g., 82.2 vs 82.4 R@1 on MS-COCO 1K Table 1), it is unclear whether these differences are statistically reliable. Multiple seeds with mean and std would strengthen the conclusions.

### Trivial

- **Inconsistency in description vs. implementation of threshold.** Section 3.2.2 describes the threshold in terms of raw cosine similarity s(x,y), but the scoring function uses debiased similarity s(x,y)−β, and the noise detection analysis (Table 7) uses the same debiased version (with zero threshold). The description should consistently refer to debiased similarity.

- The paper states w_i ∈ [0,1] (Section 3.2) but the maximum of the scoring function is ~0.148. This numerical inconsistency should be corrected.

## Nice-to-Haves

- An ablation study varying the scoring function form (e.g., linear w = max(0, s−β), squared w = max(0, (s−β)²), or sigmoid) would be valuable to understand whether the specific cubic form (or its correction) matters, or whether the binary threshold is the dominant factor.
- A visualization of the actual distribution of debiased similarities (s−β) for clean and noisy samples, showing the effective range, would help clarify whether the non-monotonicity of the current function is empirically relevant.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper does not mention related works on missing topics."** — Per meta-reviewer instructions, I cannot verify missing related works without external sources.
- **"Cannot independently verify the existence of cited models/benchmarks."** — Per instructions, all cited references are assumed to exist; this is not a valid criticism.
- **Formatting/typo nitpicks** — These are parser artifacts from PDF extraction, not author errors.
- **"The scoring function error makes the paper unacceptable in its current form"** — This is softened from the harsh reviewer's phrasing. The issue is real (Major), but the core contribution (boundary principle + estimator-based paradigm) does not stand or fall on the exact cubic form. The near-optimal ranking results suggest the binary threshold is the dominant mechanism, making this corrigible rather than fatal.
- **"Missing appendix / proofs in appendix"** — The appendix exists in the original submission; the parser strips it.
- **"The paper should evaluate on larger-scale pre-training"** — The paper explicitly acknowledges this limitation in its conclusion. It is scope-appropriate to evaluate on benchmark datasets.
- **Strength: "Theoretical grounding for the clean/noisy boundary"** — Partially conflicts with the verified weakness about random-weight assumptions. The strength is downgraded to Minor in the review above.

## Novel Insights

The most noteworthy insight from these reviews is that the scoring function's non-monotonicity may be empirically irrelevant: the near-optimal Mean Noise Rank (within 6 of theoretical optimum, Table 5) combined with >99% recall (Table 7) suggests that the method's effectiveness comes almost entirely from the binary classification (whether s−β > 0 or not), and the exact shape of the weight function has little effect. If this is true, the paper would benefit from explicitly acknowledging that the cubic form is a design choice (perhaps replaceable by any monotonic function) rather than presenting it as a principled component. This would simplify the paper's message and make the scoring function flaw easily fixable.

## Suggestions

1. **Correct the scoring function.** Replace the current cubic w = t²(1−t) with a monotonic function such as w = max(0, t) or w = max(0, t²), then verify that the results still hold (they very likely will, and may even improve for very clean samples). Alternatively, if the non-monotonicity is intentional, explain the rationale and provide the distribution of t values to show the relevant range.

2. **Acknowledge the theoretical gap explicitly.** State that Theorem 1 applies to random neural networks and is used as *supporting intuition* for why the cone effect preserves ordering; the actual claim for trained models is empirically verified (Figure 1) and grounded in known properties of contrastive learning.

3. **Add explicit backbone information for all baselines**, particularly in Table 2 (Flickr30K). Even a footnote saying "NCR, DECL, BiCro use their original backbones as reported" would make the comparison transparent.

4. **Run 3 seeds** for at least the key result (MS-COCO 50% noise) and report mean ± std.

## Score and Decision

The paper introduces a simple, well-motivated, and empirically effective paradigm for noisy-label mitigation. The core idea — using a frozen pre-trained model's cosine similarity (debiased by the random-pair mean) as a noise indicator — is sensible, and the empirical results across multiple tasks, architectures, and noise levels are strong and consistent. The computational efficiency (10× less extra overhead than NPC) is a practical advantage.

The major weakness is the mathematically flawed scoring function, which does not behave as described. However, this is a corrigible design error: the near-optimal ranking results indicate that the method works primarily through the binary threshold s−β > 0, and a corrected monotonic function would likely preserve or improve the results. This is not a fatal flaw that invalidates the contribution.

The theoretical analysis is suggestive rather than rigorous for trained models, but the empirical evidence for the boundary is solid.

**Overall:** A solid paper with a meaningful contribution and convincingly demonstrated empirical gains. The scoring function flaw is real and must be corrected, but it does not threaten the core claims.

**Score:** 6.5 — A strong paper that should be accepted with minor-to-moderate revisions to fix the scoring function and clarify the theoretical framing.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>