Now I have sufficient calibration material. Let me write the final consolidated review.

## Summary
This paper reframes DP domain discovery (set union, top-k, k-hitting set) through the lens of *missing mass* — the fraction of total item mass missed by the output — instead of the usual cardinality metric. The core theoretical contribution is showing that the simple Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass on Zipfian datasets (Theorem 3.3 with matching lower bound Theorem 3.5), along with a distribution-free ℓ∞ guarantee (Theorem 3.6). Using WGM as a domain-discovery precursor, the authors then obtain new utility guarantees for unknown-domain top-k and k-hitting set that improve on prior known-domain results by replacing dependence on the full universe size with the typically much smaller number of unique observed items. Experiments on six real-world datasets confirm that WGM-based methods are competitive with or outperform existing baselines across all three problems.

## Strengths
1. **First absolute utility guarantees for DP set union with near-optimality.** Theorem 3.3 provides a high-probability upper bound on ℓ₁ missing mass for WGM on Zipfian data, and Theorem 3.5 gives a matching lower bound showing the ε and N dependence is tight up to logarithmic factors. This pair is, as the paper correctly claims, the first provable absolute utility characterization for DP set union under any metric. The combination of upper and lower bounds is the paper's strongest contribution.

2. **Clean extension to unknown-domain top-k and k-hitting set with provably improved guarantees.** Theorems 4.3 and 4.5 replace the dependence on log(|𝒳|) in prior known-domain results with log(M) (the number of unique observed items), which can be dramatically smaller. This is a concrete, provable improvement over Mitrovic et al. (2017) and prior work. The meta-algorithm (Algorithm 2) is simple and modular: run WGM for domain discovery, then run a standard known-domain algorithm.

3. **Distribution-free ℓ∞ missing mass guarantee.** Theorem 3.6 provides a bound that holds for any dataset without the Zipfian assumption, which is essential for the downstream applications in Section 4 where no distributional assumptions are made. This is a genuinely useful theoretical result.

4. **Empirical validation on six real-world datasets.** The experiments cover all three problem settings (set union, top-k, k-hitting set) on datasets from varied domains (Reddit, Amazon Games/Magazine/Pantry, Movie Reviews, Steam Games). The results show WGM-based methods are competitive with or outperform baselines, and for k-hitting set the method even outperforms a known-domain private algorithm that assumes public knowledge of ∪ᵢWᵢ.

5. **Well-written and clearly organized.** The paper motivates the missing mass perspective clearly, states assumptions precisely, and separates the theoretical analysis from the empirical evaluation in a clean way.

## Weaknesses

### Major
None.

### Minor
1. **Missing error bars / variance information for Figures 1 and 2.** Only the k-hitting set experiments (Figure 3) report standard error. The set union (Figure 1) and top-k (Figure 2) plots report only averages over 5 trials, without any indication of variability. While the theoretical results are the paper's primary contribution, the absence of variance information makes it impossible to assess whether the observed advantages over baselines are statistically significant. The paper should add error bars or at least report min/max ranges, especially since these are 5-trial averages.

2. **No hyperparameter sensitivity analysis for the policy baseline's α parameter.** The set union baselines (Policy Gaussian, Policy Greedy) are run with a fixed hyperparameter α=3, as "suggested in those papers." No ablation or justification for why α=3 is appropriate for the missing mass metric (vs. the cardinality metric those methods were designed for) is provided. Since the baselines were originally designed for cardinality, a sensitivity analysis would clarify whether the comparison is sensitive to this choice.

3. **Only one main privacy budget (ε=1, δ=10⁻⁵) shown in the main text.** Additional budgets (ε=0.1) appear only in the appendix. The main experimental narrative would be stronger with at least two privacy budgets shown in the main figures.

4. **Assumption 1's role in the lower bounds could be discussed more explicitly.** The lower bounds (Theorem 3.5, Corollaries 4.4, 4.6) rely on Assumption 1 (output ⊆ ∪ᵢWᵢ), which is standard in the unknown-domain setting. The paper states this clearly. However, a brief discussion of whether relaxing this assumption (e.g., allowing a public auxiliary domain) would change the lower bounds would help readers understand the limits of the optimality claims. This is noted as a minor omission, not a flaw — the results are correct and well-scoped as stated.

### Trivial
None.

## Nice-to-Haves
- A "naive" missing-mass baseline for set union (e.g., threshold with Laplace noise after subsampling) would further isolate whether WGM's theoretical advantages translate to practice.
- The paper could discuss how to set Δ₀ in practice when no public knowledge of maxᵢ|Wᵢ| is available.

## Removed Points
- *Criticism about "WGM obtains MM within 5% of policy mechanisms" being misleading.* **Reason for removal:** Reading the paper and Figure 1 description, WGM *outperforms* the policy methods on MM (lower is better), and the paper's framing is that WGM is competitive with more expensive methods. The asymmetric comparison (methods designed for cardinality vs. MM) actually favors the baselines, not WGM, so this is not a weakness.
- *Concern about "distribution-free" terminology in Theorem 3.6.* **Reason for removal:** The term is used correctly — "distribution-free" in the statistical sense means the bound holds without distributional assumptions on the data, not that the bound is parameter-free. The bound depends on dataset-specific parameters (maxᵢ|Wᵢ|, N) but does not require Zipfian or any other distributional assumption.
- *Generalized concern that "many real-world DP systems permit outputting items not present in the data."* **Reason for removal:** The paper studies the *unknown-domain* setting where the domain is not known a priori, making Assumption 1 (output ⊆ ∪ᵢWᵢ) standard and necessary. Suggesting the algorithm could draw from a "public domain" assumes the existence of a known public domain, which contradicts the problem setting.
- *Strength Finder's generic strengths about "important problem" and "well-motivated."* **Reason for removal:** Dropped as generic/superficial per instructions. Concrete strengths (anchored to specific theorems/experiments) are retained.

## Novel Insights
None beyond the paper's own contributions. The reviewers' observations largely recapitulate the paper's stated contributions without identifying new cross-cutting patterns or limitations not visible from the paper itself.

## Suggestions
1. Add error bars (standard deviation or min/max range) to Figures 1 and 2, or at minimum report variance information in a table.
2. Include a brief discussion of whether the lower bounds (Theorems 3.5, Corollaries 4.4, 4.6) would change if Assumption 1 were relaxed to allow outputs from a public auxiliary domain.
3. Show results for at least one additional privacy budget (e.g., ε=0.5) in the main figures, not just the appendix.

## Score and Decision

**Round 1 bracket:** Based on calibration searches, papers in the (3.5, 7.5) band for DP theory + experiments topics scored 4.25–7.33. The paper's scope and quality place it in the upper half of this band. The round-1 bracket was [5.5, 8.0].

**Round 2 narrowing:** I read four anchors in detail:
- "Near-Exact Privacy Amplification for Matrix Mechanisms" (6.25) — narrower scope, weaker theory, accepted.
- "Privately Counting Partially Ordered Data" (6.75) — similar structure (DP theory + experiments), some novelty concerns, accepted.
- "Optimality of Matrix Mechanism on ℓₚᵖ-metric" (7.00) — pure theory, tight bounds, accepted with some significance concerns.
- "Efficiently Computing Similarities to Private Datasets" (7.50) — strong theory + experiments, accepted.

The current paper is **comparable to or stronger than** the 6.75–7.00 anchors: it has a clearer novelty claim (first absolute guarantees for DP set union), matching upper/lower bounds, and extensions to downstream problems. It is **slightly weaker than** the 7.50 anchor in experimental comprehensiveness (missing error bars, single main privacy budget). The weaknesses are all minor and do not threaten the core contributions.

**Final score: 7.0.** The paper makes a genuine theoretical contribution (first absolute utility guarantees for DP set union with near-optimality) and supports it with clean analysis and reasonable experiments. The weaknesses are addressable and do not undermine the central results.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>