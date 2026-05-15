Now I have all the evidence needed. Let me synthesize the final review.

---

## Summary

This paper presents the first polynomial-query algorithm (DistEstimate) for estimating the total variation distance between two high-dimensional distributions over $\{0,1\}^n$ in the SUBCOND (subcube conditioning) oracle model. The algorithm uses a chain-rule factorization to express probabilities as products of marginals, estimates each marginal via negative binomial sampling (SubToEval), and boosts success probability via the median trick. The authors claim a query complexity of $\tilde{O}(n^3/\varepsilon^5)$ and demonstrate the algorithm on CNF sampling benchmarks with $n$ up to 70.

## Strengths

- **First polynomial distance estimator in the SUBCOND model.** Prior work on distance estimation in SUBCOND (or even the more powerful COND model) required exponential queries. Theorem 1 breaks this barrier with a polynomial bound, which is a genuine theoretical advance. (Lines 24–32, Section 2)

- **Creative use of negative binomial sampling with Dyer–Frieze variance reduction.** The SubToEval subroutine ingeniously estimates each marginal via the reciprocal of the number of trials needed to observe $k$ successes. The variance computation (Lemma 5) leverages the tractable moments of the negative binomial distribution to obtain a multiplicative approximation guarantee. (Lines 117–119, 144–168)

- **Practical implementation demonstrated on real CNF samplers for $n$ up to 70.** The algorithm is prototyped against STS, CMSGen, and WAPS samplers. Table 1 and Figure 1 show that DistEstimateCore terminates on all benchmarks, providing distance estimates where naive methods would require $\simeq 10^{18}$ queries. This validates feasibility. (Section 5)

- **Taming technique to control marginal probabilities.** The $\theta$-taming construction (Definition 2) bounds all conditionals away from zero, preventing unbounded query complexity from arbitrarily small marginals. Lemma 2 shows the tamed distribution is within TV distance $\theta n$ of the original. (Lines 77–88)

## Weaknesses

### Fatal
None. The core ideas are sound, and no verified criticism invalidates the paper's central claim.

### Major

- **Lemma 3's proof uses an average-case query bound to derive a per-instance guarantee — a gap in the analysis.** Lemma 6 states $\mathbb{E}_{\sigma\sim\mathcal{D}}[\mathbb{E}[\mathsf{QC}]] = \lceil 8n^2\varepsilon^{-2}\rceil$, which is the *average* over $\sigma\sim\mathcal{D}$. Lemma 3's proof applies Markov's inequality using this expectation to bound $\Pr[\mathsf{QC} \ge 15\lceil 8n^2\varepsilon^{-2}\rceil] \le 1/15$ for a *fixed* input $\sigma$ (line 184). This step is unjustified for worst-case $\sigma$: the conditional expectation $\mathbb{E}[\mathsf{QC}\mid\sigma]$ could be much larger than the average. For the overall algorithm DistEstimateCore, which draws $\sigma\sim\mathcal{Q}$, the average-case analysis may suffice, but Lemma 3 as stated makes a per-call claim that its proof does not support. This needs to be clarified or corrected. (Lines 174–184)

- **The adaptation of Lemma 1 (Bhattacharyya et al. 2020) to samples drawn from $\mathcal{Q}$ rather than $\mathcal{P}$ is not justified.** Lemma 1 explicitly states it uses "a set of samples $S$ from $\mathcal{P}$" (line 68), but Algorithm 3 draws $\sigma\sim\mathcal{Q}$ (line 104). The proof of Theorem 2 applies Lemma 1 as-is without addressing this mismatch. While the estimator $Z$ remains unbiased for $\mathcal{Q}$-samples ($\mathbb{E}_{\sigma\sim\mathcal{Q}}[1_{q>p}(1-p/q)] = d_{\mathrm{TV}}$), the variance and concentration analysis may differ. The paper should verify that the sample complexity bound from Lemma 1 carries over or provide an adapted derivation. (Lines 68, 104, 207)

- **The claimed overall query complexity $\tilde{O}(n^3/\varepsilon^5)$ is not clearly supported by the component bounds.** Tracing through the stated components: SubToEval uses $O(n^2/\varepsilon^2)$ queries per call (Lemma 3), $m = O(1/\varepsilon^2)$ outer samples (from Lemma 1's sample complexity), and $T = O(\log m)$ inner repetitions for the median trick. This yields $\tilde{O}(n^2/\varepsilon^4)$, not $\tilde{O}(n^3/\varepsilon^5)$. The paper offers no explanation for the extra factor of $n/\varepsilon$. This discrepancy between the claimed and derivable bound should be reconciled. (Theorem 1, Theorem 2, Section 4.2)

- **Experimental evaluation lacks ground-truth validation and baseline comparison.** The experiments compute distances between samplers but cannot verify accuracy because no ground truth is known. No comparison against a simple baseline (e.g., a naive sampling estimator on small $n$, or the equivalence tester of Bhattacharyya & Chakraborty 2018) is provided. The tolerance $\varepsilon=0.5$ is very large — the algorithm could return any value within $\pm 0.5$ of the truth and still be "correct." The "# Samples" column in Table 1 is ambiguous (outer samples vs. total SUBCOND queries). These issues weaken the empirical claims. (Section 5, Table 1, Figure 1)

### Minor

- **Lemma 1 has a sign error** — the inequality has $+4\theta/(1-\theta)$ on both sides (line 68), making the statement formally nonsensical. The intention (a two-sided bound) is clear from the paper's use in Theorem 2, but the mathematical statement should be corrected.

- **Lemma 6 is stated without proof or derivation** (lines 174–178). While a straightforward derivation exists ($\mathbb{E}[x_j] = k/p_j$, and $\mathbb{E}_{\sigma\sim\mathcal{D}}[1/\mathcal{D}^m_{\sigma_{<j}}(\sigma_j)] = 2$ for the untamed case), the paper provides neither argument nor reference. The proof of Lemma 3's citation also incorrectly references "Lemma 5" instead of Lemma 6 for the query complexity bound (line 184).

- **The proof of Lemma 2 (taming distance guarantee) is omitted.** The lemma that $d_{\mathrm{TV}}(\mathcal{D},\mathcal{D}') \le \theta n$ is stated without proof (line 87). While perhaps standard, it should be sketched since $\theta = \varepsilon/(10n)$ directly enters the error budget.

- **Section-by-section clarity gaps.** The value $\theta = \varepsilon/(40/9+\varepsilon)$ appears in the proof of Theorem 2 without derivation (line 207). The relationship between the inner-loop parameter $T$ and the required confidence boost is described textually but no closed-form expression is given.

### Trivial
- "$\pm\varepsilon$ estimate" in Lemma 5 describes a multiplicative $(1\pm\varepsilon)\mathcal{D}(\sigma)$ guarantee but reads ambiguously as additive error — the text could be clearer.
- The high-level overview claims SubToEval returns a "$\pm\varepsilon$ estimate" (line 111) but Lemma 3 states multiplicative $(1\pm\varepsilon)\mathcal{D}(\sigma)$ — consistent upon careful reading but could confuse.

## Nice-to-Haves
- Validation on small synthetic distributions ($n=10$–$20$) with known ground truth, for several $\varepsilon$ values including small ones, would significantly strengthen the experimental evidence.
- An ablation study removing the taming step would clarify whether it is necessary in practice or primarily a theoretical tool.
- A scalability plot of total SUBCOND queries vs. $n$ with the claimed $\tilde{O}(n^3)$ trend overlaid would help verify the asymptotic claims empirically.

## Removed Points

These points were raised by reviewers but are factually incorrect, are formatting artifacts, or misunderstand the paper:

1. **"Lemma 5's variance computation assumes unjustified independence of $x_j$."** — This criticism is wrong. For a *fixed* input $\sigma$, each $x_j$ is computed from *independent* sequences of SUBCOND queries (different conditioning strings $\sigma_{<j}$, fresh random bits per position). The $x_j$'s are therefore independent, and the product factorization of expectations is justified. The harsh critic incorrectly conflated sequential generation with statistical dependence. (Lines 117–119, 136–138)

2. **"Existence/status of cited models, datasets, or benchmarks."** — The paper cites STS, CMSGen, WAPS as existing samplers; these are well-known in the constrained-sampling literature. Following the hard rules, any criticism doubting their existence or release status is removed.

3. **Formatting nitpicks, typos, missing appendix content.** — Removed per instructions; the original submission does not contain these issues.

## Novel Insights

The reviews surface one observation not explicitly made in the paper: Lemma 3's proof contains a subtle but important gap involving the mismatch between Lemma 6's *average-over-$\sigma$* query bound and the *per-$\sigma$* guarantee that Lemma 3 requires for its Markov argument. This insight is distinct from the simpler issues (sign errors, missing derivations) and points to a genuine structural weakness in the analysis that would need to be addressed even after fixing all typographical errors. Separately, the discrepancy between the claimed $\tilde{O}(n^3/\varepsilon^5)$ and the $\tilde{O}(n^2/\varepsilon^4)$ that emerges from the stated components suggests either a hidden loop factor (perhaps from the taming) or a miscalculation — either way, it requires explanation.

## Suggestions

1. **Fix the Lemma 3 proof gap.** Either (a) use a worst-case bound on $\mathbb{E}[\mathsf{QC}\mid\sigma]$ by leveraging the taming of $\mathcal{P}'$ and an independent argument for $\mathcal{Q}$, or (b) restate Lemma 3 to only claim the bound holds when $\sigma\sim\mathcal{D}$ (matching Lemma 6's guarantee), and adjust DistEstimateCore's analysis accordingly.

2. **Justify or correct the $\tilde{O}(n^3/\varepsilon^5)$ query complexity.** Provide a clean derivation showing how each parameter ($m$, $T$, $k$, $\theta$, taming parameter) contributes to the final bound. If the correct bound is $\tilde{O}(n^2/\varepsilon^4)$, update Theorem 1 and Theorem 2.

3. **Reconcile Lemma 1's sampling requirement.** Either cite a version of the Bhattacharyya et al. result that works with $\mathcal{Q}$-samples, or provide an adapted proof showing the concentration bound still holds. The unbiasedness ($\mathbb{E}[Z] = d_{\mathrm{TV}}$) is easy to show; the variance bound is the non-trivial part.

4. **Strengthen the experiments.** Include a small-$n$ synthetic test with known TV distance, report total SUBCOND query counts (not just "# samples"), and add at least one baseline comparison (e.g., a naive estimator on small $n$).

5. **Provide proofs or sketches for Lemma 2 and Lemma 6.** Both are short derivations that would significantly improve the paper's self-containedness.

## Score and Decision

The paper presents a genuinely novel algorithm with an elegant technical core (negative binomial marginal estimation + Dyer–Frieze variance reduction). The contribution — the first polynomial distance estimator in the SUBCOND model — is significant and well-motivated. However, the analysis contains a verifiable gap in Lemma 3's proof, an unaddressed mismatch in Lemma 1's sampling assumption, an unexplained discrepancy in the claimed query complexity, and experiments that lack validation. These issues are fixable but non-trivial; they prevent the paper from being accepted in its current form. A revised version that addresses the proof gaps, clarifies the query complexity, and provides basic experimental validation would make a strong contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>