Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper introduces FedMPDD, a federated learning algorithm that encodes each client's high-dimensional gradient by computing its directional derivatives along *m* random Rademacher vectors. Each client transmits only an *m*-dimensional vector of scalars plus a seed (reducing uplink from *O(d)* to *O(m)*), and the server reconstructs an aggregated gradient estimate. The key insight is that averaging multiple projections overcomes the dimension-dependent convergence of single-projection methods while the rank-deficient encoding creates a tunable barrier against gradient inversion attacks. Theorem 2 provides an *O*(1/√*K*) convergence rate under standard non-convex assumptions, and Lemmas 1–2 quantify the gradient reconstruction error as (*d*−1)/*m*.

## Strengths

1. **Novel encoding mechanism for joint communication and privacy.** The core idea — using multi-projected directional derivatives (Rademacher vectors) to simultaneously compress gradients and create a nullspace-based privacy barrier — is creative and well-motivated. The paper clearly explains why a single projection fails (dimension-dependent variance) and how averaging *m* projections overcomes this while preserving the rank-deficient structure that frustrates gradient inversion. This is a distinct departure from the fixed-subspace approaches (low-rank, Count-Sketch) that dominate the compression literature.

2. **Convergence analysis matching FedSGD's rate.** Theorem 2 (Equation 5) proves that with *m* = *O*(log(*d*/*δ*)/*ε*²), FedMPDD achieves an *O*(1/√*K*) convergence rate to a stationary point, matching the standard rate of non-compressed FedSGD. The bound explicitly decomposes the error into initialization, client-sampling, and projection-distortion terms, providing a clear picture of where each source of error enters.

3. **Quantifiable, gradient-magnitude-independent privacy guarantee.** Lemma 1 gives the clean result 𝔼[‖**ĝ**ᵢ−**g**ᵢ‖²]/‖**g**ᵢ‖² = (*d*−1)/*m*, which is independent of the gradient's magnitude. Lemma 2 translates this into a lower bound on data reconstruction error. This is a genuine strength: unlike LDP where the relative noise level depends on ‖**g**ᵢ‖ (large gradients are poorly protected), FedMPDD's protection is uniform. The bound is concrete and empirically verifiable.

4. **Empirical demonstration of the joint communication-privacy advantage.** Tables 1 and 2 compare methods under a fixed communication budget and a fixed target accuracy. FedMPDD achieves competitive accuracy (e.g., 40.84% on CIFAR-10 under 0.9 GB budget) while keeping SSIM ≤ 0.22, whereas baselines that achieve similar communication efficiency (lp-proj, Top-k, SA-FedLora) have SSIM values of 0.74–0.93, indicating substantial privacy leakage. This directly validates the claim that FedMPDD delivers both compression and privacy without sacrificing one for the other.

## Weaknesses

### Fatal
None.

### Major

1. **Abstract convergence rate is inconsistent with the theorem.** The abstract (line 13) states "converges at a rate of *O*(1/*K*)", while Theorem 2 (line 118) and the introduction (line 36) both state *O*(1/√*K*). The *O*(1/√*K*) rate is the correct one — it is standard for non-convex SGD and matches the bound in Equation (5). The *O*(1/*K*) claim in the abstract is wrong and is the paper's most visible claim. This is not a minor typo; it signals carelessness in how the central theoretical result is presented.

2. **Privacy language overstates what the formal analysis provides.** The paper repeatedly uses phrases like "inherent privacy," "uniform privacy protection," and "robust and uniform privacy against GIAs" (abstract, line 35, conclusion). However, the formal support (Lemmas 1–2) provides lower bounds on reconstruction error under a specific adversary model (minimizing a particular loss with Lipschitz gradients). This is qualitatively different from the comprehensive privacy guarantees implied by the language. The paper never defines a formal privacy definition (e.g., DP, IT-privacy), and the multi-round composition bound (Remark 2, *T*×*m* < *d*) assumes static gradients, which is a substantial simplification. The empirical evaluation (only one SSIM plot for one attack family in the main text) is too thin to fill the gap between the language and the formal guarantees. The paper would be stronger if it committed to a specific threat model and privacy definition, and acknowledged the limitations of the reconstruction-error framework.

3. **The convergence bound's dependence on ε is not discussed.** Theorem 2's bound includes an *O*(*εG*²/√*K*) term, where *ε* is the JL-distortion parameter set by *m* = *O*(log(*d*/*δ*)/*ε*²). For the bound to drive the gradient norm to zero as *K* → ∞, *ε* must vanish, which would require *m* to grow with *K* (or some other schedule). If *ε* is fixed, the bound only guarantees convergence to within an *O*(*ε*) neighborhood of a stationary point. The paper does not discuss this trade-off or the implications for the asymptotic accuracy. Additionally, the probability guarantee (1−*δ*) applies per round, and a union bound over *K* rounds would increase the required *m* — this is not addressed.

### Minor

4. **Bit-width of transmitted scalars is not specified.** The paper reports "Used Bytes (GB)" in Tables 1 and 2 and states "32 bits per value" for FedSGD (line 29), but never explicitly states the bit-width used for FedMPDD's transmitted scalars (*s_kⁱ* ∈ ℝ^m and seed *r_{k,i}*). For QSGD, it is clearly stated as "8-bit." If FedMPDD's scalars are transmitted as 32-bit floats while QSGD uses 8-bit quantization, the comparison is not apples-to-apples. The "O(*m*) bits" claim in the introduction (line 35) is imprecise. The authors should state the assumed precision and, ideally, apply the same quantization scheme to all methods.

5. **Main-text experiments are limited.** Only two datasets (MNIST, CIFAR-10) and two model architectures (LeNet, a small CNN) appear in the main paper. The paper claims "three datasets and four model architectures" but references the appendix for the omitted results. While the appendix is part of the submission, the main text would benefit from at least one additional dataset/model to support the "extensive experiments" claim. The privacy evaluation relies on a single attack (Yu et al., 2025); DLG results are mentioned only for the appendix.

6. **Figure 2 label ambiguity.** The labels "Ours (m=1.0)" and "FedMPDD (m=0.01)" appear to express *m* as a fraction of the gradient dimension *d*, but this is not explained in the caption. This makes the figure difficult to interpret without cross-referencing the text.

### Trivial
- None beyond what is already listed above.

## Nice-to-Haves

- A simple experiment varying *m* and showing the convergence floor predicted by the *O*(*ε*) term would substantiate the theory and clarify the *ε*-*m*-*K* trade-off.
- Reporting per-round communication in bits (with explicit bit-widths) alongside the cumulative "Used Bytes" would improve reproducibility.
- A discussion of the union bound over rounds for the JL probability guarantee would strengthen the convergence analysis.

## Removed Points

These points from the input reviews are removed with justification:

- **"Structured/sketched updates may be unbiased"** (Harsh Critic, Section 1): The paper says these methods are "often biased" (line 52), which is correct. The claim is qualified, not absolute. Removed.
- **"Missing Assumption 1 in main text"** (Harsh Critic): The paper states "suppose that Assumption 1 holds" in Theorem 2. The assumptions were in the appendix, which was stripped by the PDF parser. This is a parser artifact, not an author error. Removed.
- **"Baseline tuning concerns"** (Harsh Critic): Speculative, no evidence that baselines were not properly tuned. Removed.
- **"Seed generation overhead"** (Harsh Critic): The seed is a standard 32-bit integer; this is negligible and standard practice. Removed.
- **"JVP computational cost not demonstrated"** (Harsh Critic): Remark 1 addresses this explicitly, citing prior work. The paper acknowledges that the experiments use the explicit gradient computation and cites a follow-up for the JVP variant. Removed.
- **"Union bound for JL lemma across rounds"** (Harsh Critic): This is a standard technical detail common to many JL-based analyses; singling it out as a major weakness without evidence that the bound fails is not justified. Moved to Nice-to-Haves.
- **"Generic strengths about importance of problem"** (Strength Finder): Removed several strengths that were generic ("Distinction from fixed-subspace methods," "Computational efficiency via JVP," "Multi-round composition") — they are either not supported by experiments or are standard framing.
- **"Human finder's similar weaknesses from other papers"**: Not relevant to this paper; removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known tensions in the privacy-vs-compression space (e.g., formal DP vs. heuristic reconstruction-error guarantees) but do not uncover new connections that the paper itself misses.

## Suggestions

1. Fix the abstract to state *O*(1/√*K*).
2. Replace "inherent privacy" / "uniform privacy protection" with precise language: e.g., "quantifiable gradient reconstruction error of (*d*−1)/*m* providing a tunable barrier against gradient inversion attacks." Acknowledge that this is not a differential privacy guarantee.
3. State the assumed bit-width for FedMPDD's scalars explicitly in the main text (ideally the same 32-bit precision used for FedSGD, or apply quantization uniformly).
4. Add a brief discussion of the *ε*-dependence in the convergence bound: what happens when *ε* is fixed, and how *m* would need to scale with *K* to drive the gradient norm to zero.
5. Move at least one additional dataset/model result into the main text (e.g., the logistic regression or Fashion-MNIST results from the appendix).

## Score and Decision

### Calibration

**Round 1 — Bracketing (3 bands):**

| Band | Paper | Avg Score | Round | Comparison |
|------|-------|-----------|-------|------------|
| Weak (≤3.5) | CORE (ER1VDuwWvB) | 3.67 | R1 | Similar concept (common random projections for gradient compression), but CORE had no experiments and no privacy analysis. FedMPDD is strictly stronger. |
| Weak (≤3.5) | WYEEWScbaM (Gradient Distillation) | 3.00 | R1 | Unclear method, weak results. FedMPDD is substantially stronger. |
| Middle (3.5–7.5) | BiCompFL (ogIFNo2bQw) | 4.80 | R1 | Both have experiments and some novelty concerns. BiCompFL's novelty is limited (extension of FedPM). FedMPDD's core idea is more novel, but its overclaiming and presentation issues are more severe. Comparable overall. |
| Middle (3.5–7.5) | LASER (TCJbcjS0c2) | 5.83 | R1 | Strong experiments (including GPT-2), but novelty concerns about low-rank compression. FedMPDD has a more novel core idea but weaker experiments and more presentation issues. Slightly weaker than LASER. |
| Strong (≥7.5) | jj5ZjZsWJe (SCALLION/SCAFCOM) | 8.00 | R1 | Clean, well-executed theory and experiments. FedMPDD is clearly weaker — overclaiming and unaddressed convergence subtleties bring it down. |

**Round 1 bracket:** between 4.0 and 6.0.

**Round 2 — Narrowing (4.0–6.0):**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| LASER (TCJbcjS0c2) | 5.83 | R2 | Multiple reviewers noted limited novelty (low-rank compression is well-known) but praised the experiments and theory. FedMPDD has a more novel core idea (directional derivatives) but weaker experiments and the unresolved abstract error. Slightly weaker than LASER. |
| GradSkip (nrctFaenIZ) | 5.75 | R2 | Strong theory, limited experiments, some novelty concerns. Comparable to FedMPDD — both have a mix of theoretical contribution and presentation issues. |
| BiCompFL (ogIFNo2bQw) | 4.80 | R2 | Both have experiments and limited novelty. FedMPDD's core concept is more novel, but BiCompFL is cleaner. Comparable. |
| FLSS (7BmSz3jE7C) | 4.75 | R2 | Streaming subspace approach with limited experiments. FedMPDD is slightly stronger. |

**Final score determination:** The paper sits between BiCompFL (4.80) and LASER (5.83). It is clearly stronger than CORE (3.67) but weaker than LASER (5.83) due to the unresolved abstract error, overclaimed privacy language, and limited main-text experiments. The core idea is genuinely novel, but the presentation issues prevent it from being a strong paper. I place it at 5.0 — marginally below the acceptance threshold, with the potential to become a solid contribution after major revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>