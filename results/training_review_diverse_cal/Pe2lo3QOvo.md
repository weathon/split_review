Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes two randomized algorithms for RL with preference-based feedback (RLHF): a model-free algorithm for linear MDPs (Algorithm 1) and a model-based Thompson sampling algorithm for general function approximation (Algorithm 2). The key idea is to inject random Gaussian noise (for linear MDPs) or sample from posteriors (for TS) instead of using computationally intractable UCB-style oracles. This enables simultaneous sublinear regret, polynomial-time computation, and a near-optimal tradeoff between regret and query complexity — the first such result for RLHF.

## Strengths

1. **First computationally efficient algorithm with sublinear regret for RLHF in linear MDPs.** Prior work (Chen et al. 2022, Saha et al. 2023) achieved statistical efficiency but relied on intractable oracles (e.g., policy-space elimination, optimal-design-based argmax) that are computationally infeasible even for tabular MDPs. Algorithm 1 uses only standard dynamic programming, least-squares regression, and (for the BTL model) convex MLE. The paper clearly documents this gap in Section 2 and justifies why randomization avoids prior bottlenecks.

2. **Near-optimal tradeoff between regret and query complexity in T.** Theorem 4.1 shows that with threshold ε = T^{-β}, Algorithm 1 achieves regret Õ(T^{1-β}) and query complexity Õ(T^{2β}). Theorem 4.2 cites a matching lower bound (Sekhari et al. 2023): any algorithm with regret O(T^{1-β}) must have query complexity Ω(T^{2β}). This establishes the first near-optimal tradeoff in the RLHF setting, with matching T-dependence.

3. **Extension to nonlinear function approximation with tighter eluder dimension.** Algorithm 2 provides Bayesian regret and query bounds that can scale with the ℓ₁-norm eluder dimension (Theorem 5.2), which is provably ≤ the ℓ₂-norm eluder dimension used in prior TS analyses. The regret decomposition in Eq. (17) separates model and reward misspecification, adapting TS to preference-based feedback — a nontrivial extension.

4. **Computationally tractable active learning procedure.** The query condition (Eq. 4 and 5) uses the expected absolute reward difference under random reward models, which can be efficiently estimated via Monte Carlo sampling. This avoids constructing version spaces or computing confidence intervals — the dominant computational bottlenecks in prior active learning work. The paper notes this can be implemented using standard bootstrapping approximations already used in empirical TS work (Osband et al. 2016, 2023).

5. **New regret decompositions tailored to preference-based feedback.** The analysis introduces a decomposition that separates regret into terms involving reward differences between πₜ⁰ and πₜ¹ (Eq. 13 for linear MDPs, Eq. 17 for TS), rather than per-step regret. This is necessary because preference feedback only provides trajectory-wise comparisons, and is cleanly handled through the use of the comparator policy πₜ¹ = πₜ₋₁⁰.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Computational efficiency claim for the MLE step is conditional on the link function.** The abstract and introduction claim "polynomial running time" without qualification, but the body (lines 127, 257) correctly notes that the MLE's tractability depends on the link function Φ — it is concave (hence poly-time) for the BTL model but not guaranteed for general Φ satisfying Assumption 1. The paper does not provide a computational oracle assumption that would cover the general case. This does not invalidate the contribution (the BTL model covers most practical RLHF), but the unqualified claim in the abstract is slightly disproportionate relative to the more careful discussion in the body. The authors should either state the result under the BTL setting or add an explicit computational oracle assumption.

2. **The TS query bound does not simultaneously achieve optimal T-scaling and ℓ₁-eluder dimension in a single term.** The query bound in Theorem 5.2 is a minimum of two terms: term (i) scales as T^{β+1/2} · eluder₁(·) (better eluder dependence, worse in T) and term (ii) scales as T^{2β} · eluder₂(·) (optimal T-dependence, worse eluder dependence). The paper honestly acknowledges this gap (lines 341-343) and leaves a unified bound as future work. However, the "near-optimal" claim is then supported only by term (ii)'s T-dependence, meaning the tighter ℓ₁-eluder dimension does not fully manifest in a T-optimal bound. This deserves a clearer qualification when stating the tradeoff.

3. **Transition learning in Algorithm 2 only uses τₜ⁰ data, discarding τₜ¹.** The transition posterior (Algorithm 2, line 281) conditions only on transitions from τₜ⁰, not τₜ¹. While this does not affect the theoretical bounds (they are still valid), the design choice is asymmetric and potentially suboptimal in sample complexity for the transition model. The paper does not discuss this asymmetry or justify why excluding τₜ¹ transitions is intentional rather than expositional.

### Trivial

1. **Large polynomial factors in the linear MDP regret bound.** Theorem 4.1 contains terms like d^{17/2} H^{11/2} γ³. This is genuinely loose, but the paper acknowledges it (line 242) and such looseness is standard in RLSVI-style analyses with truncation tricks. It does not threaten the theoretical contribution, which is about asymptotic rates and computational tractability — not practical constants.

2. **Closed form for the query expectation.** The paper remarks that the expectation in Eq. (4) can be approximated via sampling (lines 159-160), but this expectation has a closed form (scaled half-normal) since θ₀ - θ₁ follows a zero-mean Gaussian. This is a minor oversight that does not affect the algorithm's correctness.

## Nice-to-Haves

- An empirical validation on a small tabular or linear MDP (e.g., a simple gridworld with preference feedback) would strengthen the paper's claim that its theoretical insights translate into practical guidance (e.g., the trajectory pair selection strategy). The paper mentions practical insights but provides no experiments — this is acceptable for a theory paper, but an empirical sketch would increase impact.
- A refined query bound achieving Õ(T^{2β} · eluder₁(·)) — which the paper identifies as future work — would make the TS result fully satisfying.

## Removed Points

These points were evaluated against the paper text and removed with justification:

- **"ℓ₁/ℓ₂ eluder dimension mismatch not explained"**: Removed because the paper explicitly explains this on lines 341-343: term (i) uses ℓ₁ (better eluder, worse T), term (ii) uses ℓ₂ (optimal T, worse eluder). The explanation is clear and complete.
- **"Comparison with Wang et al. (2023) is too brief"**: Removed because the paper does compare (line 47), noting that Wang et al. focus on PAC bounds while the paper focuses on regret — a meaningful differentiator. Demanding a deeper comparison is scope creep.
- **"Initial policy π₀⁰ is undefined"**: Removed because the algorithm says "Let π₀⁰ be an arbitrary policy" — this is standard for iterative RL algorithms and not a gap.
- **"Paper lacks empirical validation"**: Moved to Nice-to-Haves because this is a theoretical paper; experiments are not expected for the core contribution.

## Novel Insights

The most interesting insight from the reviews is the observation that the TS query bound's min-of-two-terms structure (ℓ₁-based with worse T, ℓ₂-based with optimal T) mirrors a fundamental tension: the ℓ₁-eluder dimension gives tighter dependence on model complexity but requires a different concentration machinery that cannot simultaneously achieve optimal T-scaling with current techniques. This suggests that unifying these two analysis styles is a nontrivial open problem, not merely a technical gap. The paper's honest identification of this as future work (rather than glossing over it) is commendable.

## Suggestions

1. Add a brief note in the abstract or introduction clarifying that the "polynomial running time" claim is established for the common BTL / logistic link function, and state the general case as requiring a computational oracle assumption.
2. Add a short discussion of the transition learning asymmetry in Algorithm 2: explain why τₜ¹ data is excluded and whether this is by necessity or for simplicity.
3. Qualify the "near-optimal" claim for the TS query bound more precisely up front (e.g., "near-optimal in T, with tighter eluder dimension dependence achieved at the cost of a worse T-factor").

## Score and Decision

This paper makes a genuine theoretical contribution — it solves a real problem (computational intractability of prior RLHF algorithms) with a clean idea (randomization), and provides the first near-optimal regret–query tradeoff for this setting. The weaknesses are minor and mostly concern presentation and acknowledged gaps. The paper is well-written for its genre (theory), the proofs are referenced to appendices, and the comparison to prior work is thorough.

**Originality**: High — first to achieve simultaneous efficiency in all three axes for RLHF.  
**Importance**: High — addresses a bottleneck in theoretical RLHF that has been open.  
**Soundness**: Good — claims are supported by rigorous analysis, and limitations are honestly discussed.  
**Clarity**: Good — the algorithmic ideas are clearly motivated, though some subtle points (MLE tractability, TS query gap) could be stated more prominently.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>