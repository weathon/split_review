Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces FedMPDD, a federated learning algorithm that encodes client gradients via multi-projected directional derivatives to simultaneously reduce uplink communication from O(d) to O(m) (m ≪ d) and provide inherent privacy against gradient inversion attacks. The key idea is that each client computes directional derivatives along m random Rademacher vectors and transmits only these m scalars plus a seed; the server reconstructs a projected gradient estimate. The paper provides convergence analysis (Theorem 2, O(1/√K) matching FedSGD), gradient reconstruction error (Lemma 1), an attempted data-reconstruction lower bound (Lemma 2), and extensive empirical validation showing large communication savings (up to 356×) while keeping reconstructed image SSIM below 0.22.

## Strengths

1. **Novel joint communication-privacy mechanism.** FedMPDD compresses each client's gradient to m+1 scalars per round (Algorithm 2), reducing uplink cost from O(d) to O(m) with m ≪ d. Privacy arises from the rank-deficient projection (1/m)UU^T, which prevents unique gradient recovery. The use of dynamic (per-client, per-round) random projections—as opposed to static-subspace methods like lp-proj or structured updates—is a clear conceptual advance (Section 2, Algorithm 2).

2. **Sound convergence analysis.** Theorem 2 proves FedMPDD attains O(1/√K) convergence under standard assumptions, with the compression penalty controlled by the JL-distortion parameter ε. The rate matches uncompressed FedSGD asymptotically when m = O(log(d)/ε²). The analysis correctly captures how averaging m projections overcomes the dimension-dependent slowdown of single-projection methods.

3. **Valid gradient-level privacy bound.** Lemma 1 establishes that the expected relative squared error between the reconstructed and true gradient is (d−1)/m, independent of gradient magnitude. This is a clean, rigorous result that quantifies the fundamental ambiguity introduced by the projection. Unlike LDP, where privacy degrades with large gradients, FedMPDD provides uniform gradient-level protection regardless of gradient size (explicitly contrasted with LDP in Remark 5 / Appendix C).

4. **Strong empirical results.** Under a fixed communication budget (Table 2), FedMPDD reaches 40.8% test accuracy while baseline compression methods (QSGD, Top-k, lp-proj, SA-FedLora) cap at 12.9%–38.1%. To reach 60% accuracy, FedMPDD uses 1.32 GB (356× less than FedSGD) while keeping SSIM ≤ 0.14. Figures 1–2 show reconstructed images are unrecognizable, consistent with the gradient-level ambiguity guarantee.

5. **Composition bound and tunable trade-off.** Remark 2 gives a worst-case multi-round guarantee (T×m < d prevents unique gradient recovery), providing practical guidelines for selecting m and the number of rounds. The JL-based logarithmic dependence of m on d (Equation 4) explains why savings grow for larger models.

## Weaknesses

### Major

1. **Lemma 2 overclaims a formal data-reconstruction guarantee.** The loss analyzed in Lemma 2 compares the *projected* true gradient (⅟m UU^T g_i(v)) against the *unprojected* dummy gradient (g_i(v̂)). Under the honest-but-curious threat model (Definition 2), the adversary knows the protocol and the projection matrix U (via the transmitted seed). A competent adversary would match the observed projected gradient against a *projected* dummy gradient: ‖⅟m UU^T g_i(v) − ⅟m UU^T g_i(v̂)‖. With this correct loss, the adversary can drive the matching error to zero for many different inputs (the projection is non-injective), collapsing the Lipschitz-based lower bound to the trivial bound of zero.  

   **Why it matters:** The paper consistently frames this result as a "rigorous theoretical analysis" providing a "formal defense against GIAs" and "concrete privacy guarantee" (abstract, Section 1, Section 2 discussion surrounding Lemma 2). Lemma 2 is cited repeatedly as proof of inherent data-level privacy (e.g., "rigorously established in Lemmas 1 and 2," line 200). The bound as stated is mathematically correct *for the specific loss defined*, but the paper's interpretation of it as a general privacy lower bound against gradient inversion attacks is not supported. This is not a minor technical gap but a structural overclaim in the paper's theoretical privacy argument.  

   **What would fix it:** Either (a) correct Lemma 2 to analyze the projected-dummy-gradient loss and update claims based on the resulting bound (which likely reduces to the gradient-level guarantee of Lemma 1), or (b) honestly state that the formal guarantee is on gradient reconstruction (Lemma 1) and that data-level protection is an empirical observation supported by the strong experimental results.

### Minor

2. **GIA attacks may not account for the projection.** The paper evaluates privacy using the attacks of Yu et al. (2025) and DLG (Zhu et al., 2019), but does not specify whether these attacks were adapted to use the *projected* dummy gradient loss (i.e., whether the adversary accounts for the projection when matching gradients). If the attacks were run in their unmodified form (matching against the unprojected dummy gradient as in Lemma 2), the empirical privacy results—while still demonstrating protection—may overstate the difficulty for an informed adversary. The paper should clarify this implementation detail and discuss its implications.

3. **Multi-round composition bound unvalidated.** Remark 2 states that privacy is guaranteed if T×m < d, but this bound is not tested experimentally. While the bound is likely pessimistic (gradients change over rounds), its practical validity is unexamined. An empirical study (e.g., attempting multi-round reconstruction when T×m exceeds d) would strengthen the paper.

4. **Scalar precision unspecified.** The paper reports communication cost in terms of "scalars" without specifying the numerical precision (bit-width) used for the transmitted directional derivatives s_k^i[j]. Since the headline communication savings depend on the size of these scalars, the precision affects reproducibility. (The paper does specify 32-bit floats for full gradients, so this is an asymmetric omission.)

5. **Experimental setup details unclear for largest communication numbers.** The 471.96 GB reported for FedSGD on CIFAR-10 (Table 2) is very large and depends on client count, participation rate, and number of rounds, none of which are fully specified in the main text. While these details may appear in Appendix H.1 (which is stripped), the main text would benefit from a brief clarification to prevent the perception of an inflated reduction ratio.

### Trivial

6. The notation in Lemma 2 incorrectly uses U_{k,j} (scalar indexing on the matrix) rather than the consistent U_{k,i} used elsewhere.

## Nice-to-Haves

- **Correct the privacy analysis** as described in Weakness 1 above. Derive a lower bound for the correct attack loss if one exists, or explicitly downgrade the formal claim to gradient-level protection.
- **Quantize the directional derivative scalars** for further communication savings and report the resulting accuracy/privacy trade-offs.
- **Validate the composition bound** by attempting multi-round reconstruction attacks with T×m close to and exceeding d.
- **Study the effect of m on convergence empirically** across a wider range (Table A.9 in the appendix is referenced but not available in the main text).

## Removed Points

- *Criticism about the FedSGD communication cost being artificially inflated.* The paper's numbers are consistent with standard assumptions (e.g., 1.6M-param CNN, hundreds of clients over many rounds); the appendix likely contains the full setup. This is a presentation issue at most, and the core claim of communication reduction is well-supported by the algorithm's design. [Reason: speculative; the appendix might clarify this.]
- *Criticism about missing hyperparameter disclosure.* The paper references Appendix H.2 for hyperparameter tuning. [Reason: appendix stripped from parser; known limitation.]
- *Criticism about the paper not proving convergence of the multi-projection estimator.* Theorem 2 provides the convergence bound. [Reason: factually wrong; the bound is in the paper.]
- *Several generic strengths from the Strength Finder* (e.g., "the paper addresses an important problem"). [Reason: generic/superficial; removed per instructions.]

## Novel Insights

Beyond the paper's own contributions, an interesting observation that emerges from the review is that the *gradient-level* ambiguity guarantee (Lemma 1) is in some ways more robust than the attempted data-level bound. The relative reconstruction error (d−1)/m is independent of gradient magnitude and depends only on the model dimension and the projection count. This uniformity—unlike LDP's gradient-magnitude-dependent protection—is a genuine structural advantage of projection-based methods. Separating the formal guarantee (gradient-level, Lemma 1) from the empirical observation (data-level, strong SSIM results) would give a cleaner narrative.

## Suggestions

1. **Address Lemma 2 directly.** Either re-derive it for the correct attack loss or explicitly state that the formal guarantee is on gradient reconstruction (Lemma 1) and that data-level privacy is supported empirically. This is essential for the paper's credibility.
2. **Clarify GIA attack implementation**—specify whether the baseline attacks were modified to use projected gradients, and discuss the implications for the empirical privacy results.
3. **Add scalar precision details** to the communication cost analysis for reproducibility.
4. **Briefly contextualize the FedSGD communication cost** in Table 2 with the assumed client count and rounds.

## Score and Decision

**Overall assessment:** The paper proposes a novel, well-motivated algorithm with sound convergence analysis and strong empirical results. The core weakness is a significant overclaim in the theoretical privacy analysis (Lemma 2) that misaligns with what is actually proven. This does not invalidate the paper's other contributions but requires correction of the privacy claims. The paper would be suitable for acceptance after addressing this issue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>