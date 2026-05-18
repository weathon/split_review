Now I have thoroughly verified the reviewer claims against the paper. Let me compose the final consolidated review.

## Summary

This paper proposes two algorithms for Reinforcement Learning from Human Feedback (RLHF) with preference-based feedback: PRLSVI (model-free, for linear MDPs) and PTS (model-based Thompson sampling, for general function approximation). The central idea is to use **randomization** to simultaneously achieve efficiency in three dimensions — statistical complexity (regret), computational complexity, and query complexity — and to obtain near-optimal tradeoffs between regret and query complexity. For linear MDPs, PRLSVI is the first RLHF algorithm to achieve sublinear worst-case regret with polynomial running time; for general function classes with small eluder dimension, PTS obtains near-optimal Bayesian regret and query bounds.

## Strengths

1. **First computationally efficient algorithm with sublinear regret for RLHF in linear MDPs.** The paper proposes PRLSVI (Algorithm 1) and proves in Theorem 1 that it achieves sublinear worst-case regret while having polynomial running time. Prior work (Chen et al., Saha et al., Zhan et al.) obtains sublinear regret but is computationally intractable even for tabular MDPs due to non-standard oracles (e.g., argmax over policy pairs under a norm). The paper's use of randomization to inject noise into value iteration (inspired by RLSVI) avoids these intractable oracles and enables standard dynamic programming. (Section 4, Theorem 1, and the five key differences listed after the theorem.)

2. **Near-optimal tradeoff between regret and query complexity.** Theorem 1 shows that by tuning the threshold \(\epsilon = T^{-\beta}\), the regret scales as \(\tilde{O}(T^{1-\beta})\) and the query complexity as \(\tilde{O}(T^{2\beta})\). The paper cites a lower bound from Sekhari et al. (Theorem 4) establishing that this tradeoff in \(T\) is optimal. (Section 4, after Theorem 1; Theorem 4.)

3. **First TS-based algorithm for RLHF with Bayesian regret and query guarantees under general function approximation.** The PTS algorithm (Algorithm 2) and Theorem 3 provide Bayesian regret and query complexity bounds that depend on the \(\ell_1\)-norm eluder dimension (strictly tighter than the \(\ell_2\)-norm used in prior work). The analysis introduces a novel regret decomposition tailored to preference-based feedback and constructs version spaces via MLE generalization bounds rather than optimism/UCB. (Section 5, Theorem 3, and analysis points (1)–(4) after the theorem.)

4. **Computationally tractable active learning procedure.** The query condition is based on a variance-style uncertainty (expected absolute reward difference under the randomized reward distribution) that avoids intractable version-space construction. This expectation can be estimated by drawing i.i.d. samples from the reward distribution, making the active query procedure computationally efficient. (Section 4, paragraph after Equation (2); Section 5, analogous paragraph; Section 2, comparison to prior active learning.)

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The abstract and introduction claim "polynomial running time" and "computational efficiency" without qualifying the dependence on the link function.** The abstract states the algorithm "has polynomial running time" (line 5), and the introduction bullet claims "computational efficiency" (line 24). The paper later clarifies (Section 4, line 127; Running time paragraph, lines 256–257) that the MLE step is not guaranteed to be concave for arbitrary \(\Phi\) satisfying Assumption 1, and polynomial time holds for specific cases such as the BTL/logistic link where the MLE objective is concave. This qualification is correctly stated in the body but should be reflected in the headline claims — e.g., "polynomial running time for common link functions such as the BTL model." This is a standard caveat for this type of work and does not undermine the contribution, but it would improve precision.

### Trivial

None.

## Nice-to-Haves

- The query condition expectation in Equation (2) has a closed form (\(2\sigma_r/\sqrt{\pi} \cdot \|\phi(\tau_t^0)-\phi(\tau_t^1)\|_{\Sigma_{t-1}^{-1}}\)). The paper could note this to avoid any ambiguity about the gap between the theoretical algorithm and a sampling-based implementation — though the paper already states "We simply use expectation here for analytical simplicity" (line 160), which makes clear that the theoretical analysis is of the exact-expectation version.
- A brief discussion of sensitivity to the choice of prior in the Thompson sampling algorithm would strengthen the presentation, though this is not expected for a first analysis.
- Clarifying the effect of scaling \(\|\phi(\tau)\|_2 \leq 1\) on the bound parameters (the paper mentions this on line 123 but could be more explicit about the resulting factor in \(\gamma\)).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Query condition approximation introduces a gap in theoretical guarantees"** — The harsh critic argues that the regret and query bounds assume the exact expectation is used, while the algorithm description mentions a sampling-based approximation. However, the paper explicitly states (line 160): *"We simply use expectation here for analytical simplicity."* This means the theoretical analysis is conducted on the algorithm **as written** (with the exact expectation). The sampling note is a practical implementation comment. The closed-form nature of the expectation further confirms this. No theoretical gap exists. **Removed: strawman that misunderstands the paper.**

- **"Bayesian regret analysis conflates exact posterior sampling with bootstrapping"** — The harsh critic claims the paper conflates exact posterior sampling (analyzed) with bootstrapping (practical approximation). In reality, Algorithm 2 explicitly uses exact posterior sampling (line 284: *"Sample \(P_t \sim \text{post}_t^P\) and \(r_t \sim \text{post}_t^R\)"*), and bootstrapping is mentioned only in a separate computation note (line 384) as something *prior TS works* have used empirically — not as part of the algorithm or its guarantees. No conflation exists. **Removed: strawman that misreads the paper.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the paper itself does not articulate.

## Suggestions

1. Add a one-sentence qualifier to the abstract and introduction bullet noting that the polynomial running time guarantee holds for common link functions (e.g., BTL/logistic) and may depend on convexity of the MLE objective for general \(\Phi\).
2. (Optional) Note the closed-form expression for the query condition expectation as a footnote for completeness.

## Score and Decision

This is a strong theoretical paper that makes a clear, well-supported advance in the theory of RLHF. The core contributions — computationally efficient algorithm design via randomization, near-optimal regret–query tradeoffs, and extension to nonlinear function classes — are significant, timely, and backed by sound analysis. The only identified weakness is a presentation issue in the headline claims about computational efficiency, which is minor and easily addressable.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>