Now I have enough calibration context. Let me synthesize the final review.

**Calibration summary:**

**Round 1 (Bracketing):**
- Weak anchors (<3.5): topical but not well-matched to conformal structured prediction (avg 2.5-3.0).
- Middle anchors (3.5-7.5): "Conformal Prediction for Deep Classifier via Truncating" (4.75, reject), "Conformal Prediction Sets with Improved Conditional Coverage" (5.0, reject), "Class-Conditional Conformal Prediction" (4.6, reject), "Conformal Risk Control" (7.0, accept spotlight).
- Strong anchors (>7.5): unrelated topics (avg 8.0).

**Round 2 (Narrowing 4.5-7.5):**
- "Estimating the conformal prediction threshold from noisy labels" (5.4, reject) — solid CP paper with well-developed theory but restrictive assumptions; the paper under review is comparable in novelty but weaker in theoretical rigor.
- "Wasserstein-Regularized Conformal Prediction under General Distribution Shift" (6.67, accept poster) — stronger theoretical foundation with proofs; the current paper is weaker.
- "Conformal Risk Control" (7.0, accept spotlight) — much stronger theory and experiments.

**Initial bracket:** 4.5 - 6.5. **Narrowing:** The paper is above the ~4.75 papers (more novel contribution) but well below the ~6.5-7 papers (weaker theory). The theoretical gaps are real and the one-sentence marginal proof is insufficient. Score near 5.0.

Let me write the final review.

---

Now let me verify my key claims about the paper against the actual text. Let me re-read a couple specific sections.

The marginal guarantee proof: line 115 says "This result follows from the learn-then-test algorithm (Angelopoulos et al., 2022)."

The algorithm description (line 99): "the search halts when φ(Z, τ_i) = 0 for the first time at τ_i, and the algorithm returns τ_{i-1}"

The sentinel issue: "If the first candidate τ_1 is invalid and φ correctly rejects it, the algorithm attempts to return τ_0, which is undefined." - The paper doesn't define τ_0.

The experiments mention 5 runs (line 238): "We show averages and standard deviations over 5 runs."

For the baseline comparison (Figure 3 caption): "Figure 3: Prediction set sizes for the question answering task, with the baseline represented by dashed lines, for (a) marginal guarantee, (b) PAC guarantee with fixed δ and varying m..."

So the baseline is compared in both marginal (3a) and PAC (3b, 3c) settings. The baseline uses PAC-type guarantees by design. So comparing marginal coverage set sizes to a PAC baseline (Figure 3a) is indeed mixing guarantee types.

Let me now produce the review.## Summary

This paper proposes a general framework for conformal prediction in structured output spaces, where prediction sets are represented implicitly via structured objects (e.g., coarse labels in a hierarchy, intervals, partial programs) rather than flat label subsets. The framework defines a scoring function, a space of structured sets, and a sequential testing procedure to select a threshold τ that satisfies either a marginal or a PAC coverage guarantee. It instantiates the framework for DAG-structured sets via an integer program and evaluates it across five domains (MNIST digits, ImageNet, SQuAD years, MBPP code generation, GoEmotions). The core idea — a general, theoretically-grounded conformal prediction framework for structured outputs — is timely and well-motivated.

## Strengths

- **First general framework for conformal structured prediction.** Section 1 and the problem formulation (Section 2, Eq. 1) define a unified search space over structured prediction sets with a mapping γ: Ỹ → 2^Y and a size function σ. The framework is then instantiated across five substantively different tasks (Section 5), going well beyond the domain-specific approaches in prior work (Khakhar et al. 2023 for code, Mohri & Hashimoto 2024 and Quach et al. 2024 for QA). This generality is a genuine contribution.

- **Clean integer programming formulation for DAG-structured prediction sets.** Section 4 presents an IP (Eqs. 3–8) that encodes the optimization problem over DAG-structured sets, with Boolean variables α_v (selected node) and β_v (covered node), and constraints that propagate coverage along edges. This bridges the abstract framework to a concrete, computable algorithm applicable to hierarchical labels, intervals, and other graph-based structures.

- **Empirical validation across five diverse domains.** The experiments (Section 5.2) cover prediction of MNIST-digit integers, hierarchical ImageNet classification, interval-valued SQuAD year answers, Python code generation, and emotion prediction, demonstrating that the framework delivers coverage above the desired level (Figure 2) across domains with very different DAG structures and underlying models (CNNs, LLMs, RoBERTa).

- **Qualitative interpretability.** Table 1 provides concrete examples showing how structured prediction sets (e.g., the interval [1979,2019]) can be more concise than flat sets of individual years, illustrating the paper's motivation from Figure 1a.

## Weaknesses

### Fatal
None.

### Major

1. **Marginal coverage guarantee is not adequately justified.** Theorem 3.1 states the marginal guarantee and the entire proof is: "This result follows from the learn-then-test algorithm (Angelopoulos et al., 2022)." The LTT framework relies on a multiple-testing correction (e.g., Bonferroni: test each candidate at level ε/|T|) to control the family-wise error rate. The paper's test φ_marginal uses threshold (n+1)ε without any correction or explanation of why one is unnecessary, and it explicitly states that the usual monotonicity that would obviate the need for a correction does not hold for structured prediction sets. The connection to LTT is not spelled out at all — what is the null hypothesis for each τ, what significance level is used, and how does the sequential stopping rule interact with the correction? Without this, the claimed marginal guarantee is unsupported. This is a *major* gap because the marginal guarantee is a central claim.

2. **PAC guarantee proof is incomplete.** Theorem 3.2's proof (lines 131–143) only considers what happens when the test correctly rejects the *first* invalid threshold τ_{i₀}. The proof bounds P(φ passes at τ_{i₀}) < δ and concludes that with probability ≥ 1−δ a valid τ is returned. However, if φ *passes* at τ_{i₀} (probability < δ), the algorithm continues testing. It could then pass at subsequent invalid thresholds and eventually stop at a valid threshold that is preceded by an invalid one (e.g., passes τ_{i₀}, passes τ_{i₀+1}, fails at τ_{i₀+2} which is valid, and returns τ_{i₀+1} which is invalid). The proof does not account for these failure trajectories. A union bound over all invalid thresholds would give (number of invalid thresholds)×δ, which could exceed δ. The paper needs to either address this with a more careful argument or adjust δ by the number of candidates. (This may be fixable — the bound may still hold because any failure path requires passing τ_{i₀}, which has probability < δ — but the paper does not make this reasoning, and as written the proof is incomplete.)

3. **Missing sentinel threshold (τ₀ is undefined).** The algorithm returns τ_{i−1} when the first test failure occurs at τ_i. If the first candidate τ₁ is invalid and φ correctly rejects it, the algorithm attempts to return τ₀, which is never defined. The paper should guarantee that the candidate set includes a provably valid base threshold (e.g., τ = 0, which would give full coverage) or explicitly handle this boundary case.

4. **Insufficient empirical verification of PAC guarantees.** The experiments report mean coverage over 5 runs with standard deviations. A PAC guarantee is a high-probability statement over calibration sets — it asserts that coverage ≥ 1−ε with probability ≥ 1−δ across calibration draws. With only 5 runs, one cannot assess whether the fraction of below-coverage deployments is ≤ δ. The standard deviations in Figure 2 suggest individual runs may fall below 1−ε for some settings, which would violate the PAC claim. A proper verification requires many more calibration/test splits (e.g., 1000) with a histogram or a reported fraction of below-coverage runs.

### Minor

1. **Unfair marginal vs. PAC comparison in Figure 3a.** The baseline (adapted from Khakhar et al. 2023) inherently uses PAC-type guarantees. Comparing its prediction set size to the paper's *marginal* method in Figure 3a conflates two different guarantee types — the baseline produces larger sets because it is more conservative, not necessarily because the proposed method is better. The PAC vs. PAC comparison in Figures 3b/3c is more appropriate. The paper should either remove the marginal comparison or add a disclaimer.

2. **Baseline description is vague.** The baseline is described as "adapted from Khakhar et al. (2023)" and "generalized to apply to arbitrary DAG structures" (Section 5.1). The paper does not specify which PAC algorithm is used, how monotonicity is enforced structurally, or how the set size comparison is computed. This hampers reproducibility.

3. **Qualitative claim about interpretability is not critically examined.** Table 1 and the text suggest that structured sets like [1979,2019] are "more interpretable" than listing six specific years, but this is asserted without evidence (no user study, no discussion of when structured sets might obscure important distinctions). The paper acknowledges the tradeoff briefly (line 280–281) but could be more careful.

### Trivial
None.

## Nice-to-Haves

- **Guidance on choosing m.** The paper notes that m should be chosen by practitioners (Section 5.2). A simple data-driven heuristic (e.g., compare estimated set sizes on a validation split) would improve practical utility.

- **Scalability discussion of the IP.** The integer program is NP-hard in general; the paper could briefly note the sizes of DAGs that can be practically handled or mention that approximate/greedy solvers are compatible with the framework (Section 2 states heuristics are acceptable — this is good but could be highlighted).

## Removed Points

- **"Baseline enforces monotonicity, which is an unfair comparison":** The paper's entire claim is that it avoids the monotonicity restriction, so comparing against a baseline that requires monotonicity is actually the correct comparison to demonstrate the advantage. The baseline being more restrictive is a feature of the comparison, not a bug. (But the marginal vs. PAC mix-up in Figure 3a remains a valid concern, kept under Minor.)

- **"Criticism about the method scaling":** The critic's concern that the IP "may be slow for large DAGs" is speculative; the paper acknowledges warm-starting and reports runtime in the appendix. The framework is agnostic to the optimizer (Section 2), so this is not a structural flaw.

- **"The paper should compare marginal with marginal":** Already kept as Minor (point 1 under Minor). The repeated framing that "the paper should compare marginal with marginal and PAC with PAC" is absorbed into that one point.

- **Strength Finder's claim about "novel PAC guarantee for non-monotone structured prediction":** Partially retained — it is genuine that the PAC setting for non-monotone structured prediction is novel. But the weakened version is folded into the strengths list ("first general framework").

- **"The paper should provide conditional coverage analysis":** This is scope creep — the paper targets marginal/PAC guarantees, not conditional coverage. Not raised by the reviewer as a weakness, just suggesting expansion.

- **"Error bars are missing":** The paper does include standard deviations over 5 runs — the critic's point was about insufficient runs, not missing error bars. Moved to Major (point 4: insufficient PAC verification).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide a complete proof for the marginal guarantee.** Either (a) explicitly incorporate a multiple-testing correction (e.g., test each τ at level ε/|T|, with Bonferroni or Benjamini-Hochberg) and show how LTT's FWER control applies, or (b) provide a direct exchangeability argument that avoids the multiple-testing issue altogether (e.g., by adapting the standard split conformal rank-uniformity argument to the structured setting). The one-sentence citation is insufficient.

2. **Fix the PAC proof.** Address the continuation beyond the first invalid threshold explicitly. If the bound still holds via a union bound, state it. Alternatively, incorporate a correction δ/|T| into each test. The proof currently reads as if it assumes the algorithm stops at τ_{i₀}, which contradicts the actual algorithm description.

3. **Add a sentinel threshold τ₀** (e.g., τ = 0 or some value guaranteeing full coverage) to the candidate set, or specify that τ₁ must be high enough to always be rejected.

4. **Strengthen PAC empirical evaluation.** Run at minimum 500–1000 calibration/test splits and report the fraction where coverage falls below 1−ε. This fraction should be ≤ δ. Add a histogram of coverage values.

5. **Clarify the baseline.** Specify exactly how the baseline is constructed from Khakhar et al. (2023) — which PAC algorithm, how monotonicity is enforced, and how it is generalized to DAGs. Release the baseline code alongside the method code (the paper already releases code for the proposed method, which is good).

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Conformal Prediction for Deep Classifier via Truncating | 4.75 | R1, R2 | Less novel contribution (truncation only), but stronger empirical validation. Comparable overall quality. |
| Conformal Prediction Sets with Improved Conditional Coverage | 5.00 | R1, R2 | Similar score; different weaknesses (conditional coverage vs. theoretical gaps). |
| Class-Conditional Conformal Prediction for Imbalanced Data | 4.60 | R1 | Less novel contribution. |
| Conformal Risk Control | 7.00 | R1, R2 | **Much** stronger — full proofs, clean theory, well-developed framework. Current paper is well below this. |
| Wasserstein-Regularized Conformal Prediction | 6.67 | R2 | Stronger theoretical foundation. Current paper is below this. |
| Estimating CP threshold from noisy labels | 5.40 | R2 | Comparable in quality; different weaknesses (restrictive assumptions vs. incomplete proofs). |

**Round 1 bracket:** 4.5 – 6.5.  
**Round 2 narrowing:** The paper is above the ~4.6–4.75 papers (more novel, broader contribution) but significantly below the ~6.5–7 papers (which have complete proofs and stronger empirical validation). The marginal proof gap is the key factor preventing a higher score. Score near 5.0 aligns best with the anchors.

The paper has a genuinely novel contribution — a general framework for conformal structured prediction — that fills a clear gap in the literature. The IP formulation for DAG-structured sets and the diverse experimental evaluation are strengths. However, the central theoretical guarantees are not properly established: the marginal proof is a one-sentence citation without necessary detail, the PAC proof has an identifiable gap, and the sentinel threshold is undefined. These are major issues that must be addressed before the paper can be accepted, but they appear fixable. The score reflects a paper with interesting ideas that falls short on theoretical rigor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>