Now I have all the data I need. Let me produce the consolidated final review.

---

## Summary

This paper introduces Dig-DEC (dual information gain decision-estimation coefficient), a new model-free complexity measure for decision making with structured observations (DMSO) that removes the optimism principle used in prior work and drives exploration purely through information gain. The paper develops a unified framework (Algorithm 1) based on general divergences and a Bregman-based analysis that recovers prior results more simply. Its main contributions are: (1) improved estimation procedures that tighten regret bounds over [FGQ+23] for both average and squared estimation error; (2) the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback under linear rewards and several general transition structures, resolving an open problem from [LWZ25]; and (3) for Bellman-complete MDPs, achieving √T regret that matches optimism-based methods—a first for DEC-based approaches.

## Strengths

- **First model-free regret bounds for hybrid MDPs with bandit feedback.** The paper establishes the first sublinear regret guarantees for model-free learning in hybrid bilinear classes and Bellman-complete coverable MDPs with linear rewards and bandit feedback, resolving the open question left by [LWZ25]. This is stated clearly in the abstract and developed in Section 5.2 with results in Table 2.

- **Improved estimation procedures with unbiased estimators.** The paper refines the online function-estimation procedure by constructing an unbiased estimator via split-sample cross-fitting (Section 4.2.1), improving the rate of Est from √T to T^{1/2} for average estimation error, and further to O(log²|Φ|) for squared estimation error under Bellman completeness (Theorem 11). For Bellman-complete MDPs, this yields an end-to-end √T regret, matching optimism-based methods for the first time in DEC-based work.

- **A genuinely new complexity measure with flexible analysis.** Dig-DEC incorporates a KL information-gain term that allows exploration without optimism, which is essential for handling adversarial/hybrid environments. The analysis (Section 4) uses a first-order optimality condition and Bregman divergences, handling general divergences without the "constructive minimax theorem" that constrained prior work. This recovers results of [XZ23] and [LWZ25] easily (Appendix C) and avoids the two-level algorithm of [LWZ25].

- **Dig-DEC is never worse than optimistic DEC and can be strictly better.** Theorem 13 shows Dig-DEC ≤ o-dec + η in the stochastic setting, so any setting handled by optimistic E2D is also handled by Dig-DEC. Theorem 14 demonstrates a 3-armed bandit where Dig-DEC achieves constant regret while optimistic DEC suffers Ω(√T), showing that the improvement can be arbitrarily large in special cases.

## Weaknesses

### Fatal
None.

### Major

- **The strict improvement over optimistic DEC is demonstrated only on a trivial bandit, not on any structured MDP.** Theorem 14 considers a 3-armed bandit (H=1, no state transitions), which is a trivial subclass of MDPs. The paper does not exhibit any non-trivial MDP (bilinear class, Bellman-eluder, coverable) where Dig-DEC yields a strictly better rate than optimistic DEC. Theorem 13 shows the two complexities are equivalent up to an additive η, so in all the settings where new bounds are claimed (Tables 1 and 2), the improvement is not quantified. The paper acknowledges this is a "toy example" (line 311), but given that the claimed advantage over optimistic DEC is a central selling point, the absence of a non-trivial example is a significant gap.

- **The hybrid MDP bounds are achieved at relatively high polynomial exponents with no discussion of optimality.** The hybrid regret bounds (Table 2) are in the T^{3/4}–T^{13/16} range (parser artifacts in the extracted text produce T^{3/2} and T^{13/8}, but these correspond to ~T^{0.75} and ~T^{0.8125}). No lower bounds are provided, so there is no indication whether these rates are near-optimal or far from it. The paper claims to "resolve the main open problem left by [LWZ25]" (abstract), but for a problem to be meaningfully resolved, some context on the gap to optimality is needed. Without a single lower bound or comparison to the full-information rates from [LWZ25], the reader cannot assess whether these bounds are competitive or merely sublinear.

### Minor

- **Inconsistency between the abstract and introduction regarding claimed regret exponents.** The abstract (line 19) states improving "regret bounds from T^{3/4} to T^{3/5} (on-policy) and from T^{5/6} to T^{7/8} (off-policy)" for average estimation error. The introduction (line 39) states "improve the T^{3/2}/T^{5/8} regret of [FGQ+23] to T^{3/2}/T^{5/6}"—the fractions do not match (3/2 vs 3/4, 5/8 vs 5/6), and T^{3/2}=T^{1.5} is implausible as a prior bound. The final regret bounds in Table 1 (stochastic setting) are T^{2/3}, which also do not match either set of claimed exponents. While the abstract's T^{3/4}→T^{3/5} claim refers specifically to the estimation sub-problem rather than the end-to-end regret, the inconsistency between the abstract and introduction creates confusion about exactly what is being improved and by how much.

- **Algorithm 1 requires solving a minimax optimization over Δ(Π) × Δ(Ψ) each round with no polynomial-time implementation.** As the paper acknowledges (line 43), "model-free" here refers only to regret independence from |M| and does not imply computational efficiency. However, the practical value of the framework is limited without any discussion of how the minimax problem (3) can be approximated, or which concrete MDP classes admit efficient implementations. The paper compares to optimism-based approaches [JLM21, XFB+23] that are often computationally efficient for their settings, but does not address whether Dig-DEC can be similarly instantiated.

### Trivial
- The paper uses "ALR" in Eq. (1) and (2) where it likely intends "AIR" (Algorithmic Information Ratio), suggesting a minor typo in the LaTeX macros.

## Nice-to-Haves
- A generalization of Theorem 14 to a non-trivial MDP (e.g., a 2-state MDP) would substantially strengthen the claim that Dig-DEC strictly improves over optimistic DEC in meaningful settings.
- A discussion of lower bounds for the hybrid setting, or at minimum a comparison to the full-information rates of [LWZ25], would help contextualize the hybrid results. The paper's claim of "resolving" an open problem would be more credible if it argued why the achieved exponents are reasonable.
- A brief discussion of how the minimax optimization in Algorithm 1 might be approximated for concrete MDP classes (e.g., via online no-regret learners) would improve practical relevance.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Abstract misrepresents results — structural failure"** (from Harsh Critic Issue 1): Removed because the abstract's claimed improvements (T^{3/4}→T^{3/5}, T^{5/6}→T^{7/8}) refer to improving [FGQ+23]'s bounds for the estimation sub-problem, not the end-to-end regret in Table 1. The abstract is not internally contradictory in context. The inconsistency between abstract and introduction exponents is a real weakness (retained under Minor above), but characterizing it as a "structural failure" or saying "readers cannot trust which claims are genuine" is disproportionate. The paper's core results in Tables 1 and 2 are clearly presented.
- **"Hybrid MDP bounds too weak to resolve claimed open problem"** (from Harsh Critic Issue 2): Partially kept as a Major weakness (lack of optimality discussion). The critic's characterization that the bounds are "too weak" is removed because first bounds for a hard problem being in the T^{0.75} range is a meaningful contribution; the open problem is genuinely "resolved" in the sense of being addressed for the first time. The lack of lower bounds is the real issue.
- **"Computationally intractable" as a serious weakness** (from Harsh Critic Issue 4): Removed as a framing overstatement. The paper explicitly defines "model-free" in the regret-bound sense (line 43) and acknowledges this. The computational issue is real but downgraded to Minor.
- All pure formatting/style nitpicks and parser artifacts (missing appendix sections, garbled fractions, etc.).
- Generic/superficial strengths from the Strength Finder (e.g., "important problem," "valuable contribution") that lack specific evidence anchors.
- Criticisms about missing experiments (not applicable to theory papers) or missing related work (cannot be verified).

## Novel Insights

None beyond the paper's own contributions. The key conceptual insight—replacing optimism with a KL information-gain regularization term (which splits into a regularization component and an information-gain component)—is the paper's own contribution and is well explained in Section 6. The Bregman-based analysis technique that handles general divergences without the constructive minimax theorem is also genuinely novel. The reviews did not surface any observation that goes beyond what the paper states itself.

## Suggestions

1. **Reconcile the abstract and introduction exponent claims.** The current introduction (line 39) contains fractions (T^{3/2}, T^{5/8}) that are inconsistent with the abstract and with any plausible prior bound. These should be corrected to match the abstract or clarified to indicate what is being improved.
2. **Add a non-trivial MDP example to Theorem 14.** The strict improvement over optimistic DEC is currently only shown on a 3-armed bandit. Adding even a 2-state MDP example would significantly strengthen the claim.
3. **Add a brief discussion of optimality (or the gap to optimality) for the hybrid bounds.** Even a paragraph noting that the hybrid rates are the first of their kind and that closing the gap to √T or providing a matching lower bound is future work would give readers the necessary context.
4. **Include a short discussion of computational considerations.** While the paper's definition of "model-free" is clear, noting whether the minimax problem (3) can be solved efficiently for specific MDP classes (bilinear, coverable, etc.) or citing a standard approximation approach would improve the paper's completeness.

## Score and Decision

**Originality:** The Dig-DEC formulation and the Bregman-based analysis are genuinely novel. The unbiased estimation refinement is a clean contribution. **8/10**

**Importance of research question:** The open problem of model-free learning in hybrid MDPs with bandit feedback is well-motivated and timely. The paper advances the DEC framework in a meaningful direction. **8/10**

**Claims supported:** The theorems are stated formally with references to appendix proofs. The main results are tabulated clearly. The abstract/intro exponent mismatch introduces some confusion but does not invalidate the core claims. **7/10**

**Soundness of experiments/theory:** The theoretical framework appears sound. The analysis techniques (first-order optimality, Bregman divergences, unbiased cross-fit estimation) are well-grounded. The reliance on appendix-deferred proofs is standard for this type of paper. **7.5/10**

**Clarity of writing:** The main body is generally well-structured. The tables are dense but functional. The inconsistency between the abstract and intro fractions and the minor ALR→AIR typo are distractions. **7/10**

**Value to the research community:** The Dig-DEC framework, improved estimation procedures, and first hybrid model-free bounds will be of interest to the RL theory community. The analysis techniques may find broader application in the DEC literature. **8/10**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>