## Summary

This paper addresses the problem of aggregating answers from multiple LLMs for multiple-choice questions. It proposes two new algorithms: Optimal Weight (OW), which is proven to be the Bayesian-optimal linear aggregator under a symmetric noise model, and Inverse Surprising Popularity (ISP), a second-order information method that provably dominates majority voting in expected-advantage terms. Practical unsupervised variants (OW-L, OW-I) that estimate LLM accuracies from second-order statistics without ground-truth labels are developed and validated on UltraFeedback, MMLU, and ARMMAN.

---

## Strengths

- **Bayesian-optimal aggregation (Theorem 1):** The proof that the OW algorithm with weights $\omega_i = \sigma_K^{-1}(x_i)$ is the Bayesian-optimal aggregator *among all aggregators* (not just linear ones) is rigorous and non-trivial. The closed-form is interpretable, and the connection to the Bradley–Terry model (Corollary 1) is a genuinely interesting observation that links aggregation theory to LLM post-training.

- **Provable ordering ISP ≥ MV ≥ SP (Theorem 2):** The explicit closed-form expression for $\mathbb{E}[\text{Adv}_{\text{ISP}}(s^*) - \text{Adv}_{\text{MV}}(s^*)]$ is clean. The identification that LLMs, being more accurate than human crowds, *invert* the SP correction mechanism is the most conceptually original insight in the paper. The asymptotic scaling ($\Theta(1/K)$ for ISP-MV gap vs. $\Theta(1)$ for MV-SP gap) is a useful practical implication.

- **Consistent empirical gains across diverse datasets:** Tables 3 and 4 report statistically significant improvements over MV (t-statistics of 12.53, 23.39, 3.22) on three datasets spanning preference learning, academic QA, and healthcare. OW-L outperforms MV in 97.92% of all 16 ensembles, and MV never achieves best performance in any configuration — a compelling pattern.

- **Unsupervised adaptation is practical:** The two strategies OW-L (ERM on second-order moments, Eq. 7) and OW-I (ISP pseudo-labels as ground truth) make OW applicable without any labels, directly addressing the key limitation of first-order methods.

---

## Weaknesses

### Fatal
None.

### Major

- **Formal gap between expected-advantage ordering and accuracy ordering.** Theorem 2 formally establishes $\mathbb{E}[\text{Adv}_{\text{ISP}}(s^*)] \geq \mathbb{E}[\text{Adv}_{\text{MV}}(s^*)]$, but the headline claim throughout the paper is that "ISP outperforms MV." Accuracy is $P(\arg\max_s \text{Adv}(s) = s^*)$, not $\mathbb{E}[\text{Adv}(s^*)]$. A higher expected advantage for the correct label does not directly imply higher accuracy; if the variance of $\text{Adv}_{\text{ISP}}$ is substantially larger, accuracy could go the other way in finite-sample regimes. The simulation in Section 5.1 numerically validates the accuracy ordering under the paper's exact generative assumptions, but this substitutes empirical confirmation for a formal argument. The paper's abstract and introduction repeatedly claim ISP "provably" outperforms MV, which overstates what is formally proved. This gap should be explicitly acknowledged or closed.

- **OW-L and OW-I produce completely identical results across all settings, with no explanation.** Table 3 shows OW-L = OW-I on all three datasets (73.66%, 90.37%, 85.78%), and Table 4 shows per-question discrepancy counts are *byte-for-byte identical* (e.g., 2545/1727, 1821/659, 264/195). Two methods with distinct derivations — one via ERM over second-order moments (Eq. 7), one via ISP pseudo-labels — coinciding exactly across all three datasets and even the per-question breakdown is mathematically improbable unless they are effectively equivalent or share an implementation path. This is not acknowledged or explained anywhere in the paper. If both methods converge to the same solution, this is actually an informative positive result about OW's robustness to weight-estimation method; if it reflects an implementation artifact, it raises a reproducibility concern. Either way, the paper should address it explicitly.

- **No comparison with any baseline other than majority voting.** The paper compares ISP, OW-L, and OW-I only against unweighted MV. Simple alternatives — weighting by model scale, self-reported confidence, or a small labeled calibration set — are natural and widely used in practice. Without these comparisons, it is unclear whether the proposed methods are the best way to exploit the available information, or simply better than the most naïve baseline. The improvement over weighted-by-accuracy baselines (were labels available) is also not assessed.

### Minor

- **The Appendix C extension of theoretical results to correlated agents is entirely deferred.** The main paper acknowledges in Section 2 that Assumption 1 (conditional independence) "may not hold perfectly in the LLM setting" and defers the generalization to Appendix C. LLMs trained on overlapping data with similar RLHF pipelines will exhibit correlated errors. Since the appendix was removed from the reviewed copy, reviewers cannot evaluate how robust the theoretical guarantees are to realistic correlation levels. At minimum, a summary of which main theorems survive and in what form under correlated agents would strengthen the paper's practical claims.

- **Simulated experiments (Section 5.1) are not informative tests of robustness.** The simulation uses the exact DGP assumed in the theory (conditional independence, symmetric noise, uniform prior). This confirms correct implementation, but does not test robustness to assumption violations. A simulation varying agent correlation or answer-difficulty heterogeneity would meaningfully test ISP's real-world applicability.

- **OW-L optimization (Equation 7) is underspecified.** The objective is a non-convex function of $(x_1, \ldots, x_N)$ via the second-order moment expressions deferred to Appendix F.2. The paper does not describe the solver, initialization strategy, or whether convergence to a global minimum is reliable. This is a practical gap given that correctness of OW-L depends on solving this optimization reliably.

### Trivial

- The paper states in Section 5.4 that "Single Best functions as a clairvoyant oracle rather than a fair baseline" — this clarification is appropriate but could be placed earlier in the results section.

---

## Nice-to-Haves

- A bound or empirical curve relating the theoretical advantage gap $\mathbb{E}[\text{Adv}_{\text{ISP}}(s^*) - \text{Adv}_{\text{MV}}(s^*)]$ to the empirical accuracy difference would close the formal gap in Theorem 2 and strengthen the paper's core theoretical claim significantly.
- Theorem 3 provides an $O(1/\sqrt{M})$ convergence rate, but does not characterize the constant. A calibration analysis on how large $M$ must be before ISP reliably beats MV empirically would strengthen the practical utility claim.
- A simulation that tests performance under varying levels of inter-agent correlation would clarify the range of practical settings where the theoretical guarantees approximately hold.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Positional bias / symmetry assumption needing empirical validation on paper's own datasets:** The paper explicitly states the symmetry assumption and cites it to Guo & Vosoughi (2024). Criticizing a clearly stated, cited assumption without a specific violated instance in the paper's data is a scope-creep weakness. The paper acknowledges it as an assumption; the citation establishes precedent.

- **Theorem 1 is "not novel" since it follows from standard Bayesian analysis:** While the result connects to known log-likelihood-ratio weighting, the specific derivation in the LLM-symmetric-noise setting with the $\sigma_K^{-1}$ form, plus the connection to the Bradley–Terry model (Corollary 1), is a genuine contribution to the LLM aggregation literature. The reduction to "standard result" ignores the novel formalization.

- **Strength: "theoretical justification for the validity of the BT model":** This is overstated by both the paper (Section 3) and the strength finder. Corollary 1 justifies inverse-logistic weighting in a specific aggregation setup, not the full BT model used in RLHF pairwise ranking. Removed as a standalone claimed strength because the critic's qualification is correct.

- **Strength about addressing an important problem (generic):** Dropped per filtering rules — too generic to stand as a concrete strength without specific evidence.

---

## Novel Insights

The most genuinely novel insight is the inversion of the SP logic for the LLM setting: SP was designed to correct crowds that *underestimate* the ground-truth answer's popularity (a systematic conservative bias in human judgments), but LLMs are accurate enough that the crowd *over-confirms* correct answers — so the correction goes in the opposite direction, yielding ISP. This is a clean conceptual contribution that extends classical information-aggregation theory to a new domain in a non-trivial way. The formal connection between OW and the Bradley–Terry model (Corollary 1) is also a useful bridge between aggregation theory and the LLM post-training literature.

---

## Suggestions

1. **Explicitly state the formal gap between E[Adv(s*)] and accuracy, and either close it or soften the "provably outperforms" language** throughout the abstract and introduction to match what Theorem 2 actually establishes.
2. **Explain the OW-L = OW-I coincidence in Table 3 (and Table 4).** If both methods converge to the same estimates in practice, this robustness result should be claimed explicitly and explained.
3. **Add at least one weighted-voting baseline** (e.g., weights proportional to empirical accuracy on a held-out split, or self-reported confidence scores) to contextualize the improvement beyond MV.
4. **Summarize the Appendix C correlated-agent extension in the main paper** — even two to three sentences describing which theorems survive, and under what weakened guarantees, would substantially strengthen the practical relevance of the theory.
5. **Describe the OW-L solver** (optimizer, initialization, convergence check) and provide evidence that the non-convex problem in Equation (7) is solved reliably.

---

## Score and Decision

**Originality:** The ISP inversion insight is genuinely novel, and the Bayesian-optimal OW derivation is clean. Originality is solid. (4/5)

**Importance:** LLM aggregation is increasingly important for multi-agent reasoning and automated annotation. (4/5)

**Claims supported:** The formal gap between expected advantage and accuracy is real and not bridged in the paper. The identical OW-L/OW-I results are unexplained. The empirical evidence is consistent and statistically significant, but baselines are thin. (3/5)

**Soundness of experiments:** Simulation covers only the assumed DGP. Real-world results are consistent across three datasets. Identical OW-L/OW-I results raise concerns without explanation. (3/5)

**Clarity of writing:** Generally clear and well-structured. (4/5)

**Value to the research community:** Useful theoretical framing and practical algorithms for an increasingly common setting. (4/5)

The paper makes real, well-motivated contributions — a principled Bayesian-optimal aggregator, a novel ISP algorithm with theoretical backing, and consistent empirical validation. The main concerns (formal gap, unexplained OW-L/OW-I coincidence, absence of other baselines) are substantive but addressable, and do not invalidate the core contribution. The paper represents a meaningful advance in LLM aggregation theory with practical utility.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>