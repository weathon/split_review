Now I have all the evidence I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

Let me now construct the full review.

---

Let me verify one more thing about the "3-wise independence" claim when m is fixed, to make sure I'm correctly evaluating the severity.

When m is fixed and only r is random:
- z^(1) = [m + R·r (mod 2), r] for first N*l_m entries and last l_r entries respectively
- The randomness comes only from r (l_r bits of entropy)
- With l_r = 512, there are 2^512 possible values of z^(1)

Now, does z^(1) have 3-wise independence when m is fixed? Let me think...

For any triple of coordinates of z^(1), the distribution depends on whether the coordinates involve the watermark bits or padding bits. If all three are in the padding part (last l_r entries), they're independent Bernoulli(1/2) by construction. If any are in the watermark part, they involve R·r which is a function of r.

Since R·r maps r (l_r bits) to a vector in F_2^{N*l_m}, and the coordinates of R·r are not necessarily independent (they're linear combinations of r), 3-wise independence may not hold. Each coordinate of R·r is the XOR of s entries of r, and since each coordinate of r is independent Bernoulli(1/2), each XOR is also Bernoulli(1/2). But are triples of such XORs independent? Not necessarily - they share coordinates of r.

So the critic's point about the theoretical gap is valid: when m is fixed, z^(1) cannot be 3-wise independent because all randomness comes from only l_r bits, and there are l_x > l_r coordinates. The 3-wise independence property requires 3l_x bits of entropy, which isn't available.

However, it's worth noting that 2^512 is still astronomically large, and the empirical results suggest the method works. The gap is real but may not affect practical performance.

OK, I'm confident in my assessment now. Let me write the final review.Now I have thoroughly verified all claims. Let me construct the final review.

## Summary

This paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models that converts binary watermarks into Gaussian noise via binary embedding (mixing watermark bits with random padding using a sparse matrix) and spherical mapping (projection onto the unit sphere, orthogonal rotation, and chi-square scaling). The method eliminates per-image key storage required by prior lossless schemes (Gaussian Shading, PRC Watermark) by using a single fixed secret signature, while achieving extraction speeds ~4 orders of magnitude faster than PRC Watermark. Experiments on Stable Diffusion v1.5/v2.1 demonstrate competitive FID, strong robustness under adversarial attacks, and near-chance classifier accuracy, indicating practical undetectability.

## Strengths

1. **Novel and principled mapping from binary watermarks to Gaussian noise via spherical 3-designs.** The paper establishes a theoretical chain (Theorem 3.1 → Theorem 3.2 → Lemma 3.3 → Lemma 3.4) connecting binary embedding, spherical 3-designs, orthogonal rotation, and chi-square scaling to show that the final watermarked noise matches the standard Gaussian distribution up to third-order moments. This theoretical framework is a genuine conceptual advance over prior lossless schemes that rely on cryptographic primitives (stream ciphers, PRC).

2. **Elimination of per-image key storage with practical benefits.** Unlike Gaussian Shading (which requires a unique key+nonce per image) and PRC Watermark (which incurs heavy cryptographic overhead), the proposed method uses a fixed secret signature (T, C) stored once. This design is validated by Figure 4, showing extraction is ~4 orders of magnitude faster than PRC Watermark (~0.0003s vs ~10s), and by the ablation studies showing that parameter choices do not harm undetectability.

3. **Strong empirical robustness, especially under adversarial attacks.** Table 2 shows that under adversarial attacks, lossy schemes (DwtDct, DwtDctSvd, RivaGan, Tree-Ring) drop to near-50% ACC and ≤27% TPR, while Spherical Watermark maintains 98.12% ACC and 99.83% TPR. The method also achieves FID values (46.8132 on COCO SD v2.1) nearly identical to the original (46.8146), confirming that watermarking introduces no measurable distributional shift—unlike lossy methods such as Gaussian Shading (49.4379).

4. **Thorough ablation studies and parameter analysis.** The paper systematically ablates each module (binary embedding, spherical mapping), hyperparameters (sparsity s, repetition N, padding length l_r, watermark capacity l_m), and diffusion sampling configurations (ODE solvers, timestep schedules), providing a clear picture of how each component contributes to undetectability and robustness.

## Weaknesses

### Major

1. **Theoretical analysis assumes random watermark messages, but deployment uses fixed messages — the gap is unaddressed.** Theorem 3.1 states: "If m and r consist of independent Bernoulli(1/2) bits, then z^(1) is both 2-wise and 3-wise independent." In practice, the watermark m is a fixed metadata string (e.g., user ID), and only the padding r is drawn randomly per image. When m is fixed, the distribution of z^(1) = T[m_repeated, r]^T has support size at most 2^{l_r} (not 2^{l_x}), and the 3-wise independence proof no longer applies. Since the spherical 3-design property (Theorem 3.2) depends on the 3-wise independence of z^(1), the theoretical guarantee of undetectability does not extend to the fixed-m case without additional argument. The paper should either (a) prove that the conditional distribution (fixed m) retains the design property, (b) provide a rigorous bound on the divergence between the conditional and unconditional distributions, or (c) honestly qualify the claim as applying to the unconditional setting only and provide stronger empirical evidence for the fixed-m case. As written, the paper's central claim of "provably lossless" is overstated relative to what the theory actually supports. *(This is a major weakness because it affects the core claim, not because the method is wrong — the empirical results are strong, and l_r = 512 means the support is enormous.)*

### Minor

1. **"Encryption-free" framing is somewhat misleading.** The method uses a secret signature K = {T, C} that must be kept confidential to prevent removal. This is functionally equivalent to a secret key — the advantage is that it is a single static key rather than a per-image key+nonce, not that it eliminates secret assumptions. The paper's phrasing ("encryption-free design") could be clarified to avoid implying zero secret material is needed.

2. **Classifier-based undetectability experiments do not fully substantiate the cryptographic indistinguishability definition (Eq. 2).** The paper defines undetectability in cryptographic terms (indistinguishability against any PPT adversary) but evaluates it using only a two-layer MLP and ResNet-18. While near-50% accuracy on these classifiers is a reasonable sanity check, it falls short of a cryptographic argument. Stronger tests — such as maximum-mean-discrepancy (MMD) between batches of watermarked and unwatermarked latents, or training higher-capacity classifiers — would better support the claim. The paper already has strong FID evidence; this point is about the gap between the formal definition and the empirical verification.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- The paper could report exact numerical values for extraction times (not just log-scale bars) and confirm that both methods use comparable implementation optimization levels. *(The critic's concern about PRC using unoptimized Python is speculative — the paper states both are evaluated on the same hardware, and the log-scale values are clear enough.)*
- A brief discussion of the minimum padding length l_r needed to maintain undetectability would be instructive. Currently l_r = 512 is used but no analysis of the trade-off is given.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"T^(-1) = T is incorrect"**: The harsh critic claimed T^(-1) = T "is trivially true only if R = 0" and that the correct inverse would be [I, R; 0, I]. This is factually wrong. Over F_2, T = [I, R; 0, I] satisfies T^2 = [I, R+R; 0, I] = I because R+R = 0 in F_2. So T^(-1) = T is correct. **REMOVED** (factually incorrect).

- **"99.99% vs 100% accuracy is a concern"**: The paper achieves ACC = 99.99% for Clean setting (std 0.01), while some baselines hit 100%. This difference is within one standard deviation and is explicitly attributed to the sparsity parameter s. **REMOVED** (trivial nitpick).

- **"Figure 4 needs more explanation about implementation differences"**: The paper already states both methods use the same hardware and reports values on a log scale with an explicit comparison and explanation of PRC's belief-propagation overhead. The critic's concern about "unoptimized Python" is speculation. **REMOVED** (speculative, paper already explains the comparison).

- **"Missing appendix proofs"**: The critic notes proofs are in the appendix and cannot be verified. Per hard rules, missing appendix content is a parser artifact from the PDF extraction. **REMOVED** (parser artifact).

- **"Missing related works"**: Per hard rules, I cannot mention missing related works as I have no external sources to confirm their existence. **REMOVED**.

- **"PRC implementation may be unoptimized"**: Speculative claim with no evidence in the paper. **REMOVED**.

- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem"): Generic/superficial strengths removed per filtering rules.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a genuinely interesting tension: the paper uses a *cryptographic* definition of undetectability (computational indistinguishability) but provides a *statistical* guarantee (matching up to third-order moments) and *ML-based* empirical verification (classifier accuracy). This mismatch between the definition and the evidence is common in the watermarking literature but rarely discussed explicitly. The paper would benefit from clarifying which type of guarantee it actually provides: it is *statistically lossless up to third order* and *empirically indistinguishable* against reasonable classifiers, rather than *cryptographically provably undetectable*. Resolving this framing would strengthen the paper and better align its claims with its evidence.

## Suggestions

1. **Acknowledge and address the fixed-message gap.** Replace "provably lossless" with a more precise claim (e.g., "provably lossless when averaged over random messages, and empirically indistinguishable for any fixed message"). Provide an argument (theoretical or strong empirical) for why the fixed-m case still works — e.g., noting that l_r = 512 bits of randomness still yields 2^512 possible watermarked latents, making the conditional distribution practically indistinguishable even if the spherical 3-design property is not strictly preserved.

2. **Add two-sample statistical tests for undetectability.** Reporting MMD or coordinate-wise Kolmogorov-Smirnov statistics between batches of watermarked and unwatermarked latents would provide stronger evidence than classifier accuracy alone and address the gap between the cryptographic definition and the empirical evaluation.

3. **Clarify the "encryption-free" terminology.** Replace "encryption-free" with "single-key" or "static-key" to accurately convey that the method uses one fixed secret key rather than per-image keys, avoiding the implication that no secret material exists.

## Score and Decision

**Calibration procedure:**

- **Round 1 (Bracketing):** Three queries each returned anchors in the weak (avg_score < 3.5), middle (3.5–7.5), and strong (>7.5) bands. The weak band returned papers scoring 2.0–3.0 (withdrawn/rejected). The strong band returned irrelevant papers scoring 8.0 (unrelated topics). The middle band was the only relevant band.

- **Round 1 bracket:** 4.0 – 6.5 (narrowest plausible range based on middle-band anchors).

- **Round 2 (Narrowing):** Two queries targeting 4.5–6.5 and 6.0–8.0. The relevant results were:
  - NoisePrints (avg 4.50, Poster): Weaker theoretical foundation, logical inconsistencies in protocol. Current paper is stronger theoretically.
  - PQIM/Hiding in the Phase (avg 5.00, Reject): Similar provable-robustness claims; weaknesses included overclaimed performance and missing cryptographic guarantees. Current paper has similar profile but stronger empirical validation.
  - Guidance Watermarking (avg 5.00, Poster): Clean idea but limited attack scope. Current paper has broader evaluation.
  - SERUM (avg 5.00, Poster): Simple approach, strong robustness, but multi-user scaling concerns. Current paper compares favorably.
  - DLM Watermarking (avg 5.00, Poster): First-move advantage, but marginal gains over baselines and high computational cost.
  - SIGMark (avg 5.33, Poster): Video diffusion watermark with blind extraction.

The current paper is comparable to these 5.0-level papers: it has a stronger theoretical framework than most, thorough experiments, and a clear practical advantage (eliminating per-image key storage). However, the unaddressed theoretical gap (fixed-m case) is a more fundamental limitation than the typical weaknesses of the anchor papers (which tend to be about scope or incremental gains). Weighting the genuine theoretical contribution against the unaddressed gap, the paper sits at the same level as the anchor set — a clear contribution with a non-trivial issue that should be resolved.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>