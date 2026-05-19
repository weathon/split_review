- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 3
Now I have a comprehensive understanding of the paper. Let me write the final consolidated review.

## Summary

This paper identifies extrapolation error (inaccurate estimation of rarely-visited state-action pairs) as a critical but underexplored issue in online cooperative MARL. It argues that value factorization methods succeed largely because they mitigate this error, and that monotonicity enables a self-correcting error-propagation mechanism (EPC). Building on this analysis, the paper introduces annealed multi-step bootstrapping (Peng's Q(λ) with a decaying λ schedule) and ensembled TD targets to reduce bias and variance in target estimation. Applying these techniques to QMIX (yielding AEQMIX) produces performance improvements on SMAC, GRF, and SMACv2, and the approach extends to policy-based methods (FACMAC, MADDPG).

## Strengths

1. **Identification of extrapolation error as a distinct problem in online MARL** — Section 3.1 decomposes error into TAE, TEE, and OD (following Anschel et al., 2017), and Figure 1(a) provides empirical evidence that 20%–60% of next-state joint actions are unseen during training in SMAC. This quantification of the problem and the connection to value factorization's success is a novel and useful framing for the field.

2. **EPC (Error Propagation Consistency) analysis linking monotonicity to self-correction** — Proposition 1 and the surrounding discussion (lines 122–140) provide an intuitive but principled argument for why monotonic factorizations like QMIX can self-correct overestimation errors via individual utilities, while non-monotonic structures cannot. This offers a mechanistic explanation for the empirical observation that QMIX outperforms more expressive but non-monotonic methods.

3. **Diagnostic analysis of QPLEX's failure mode** — Section 3.3 traces QPLEX's mid-training degradation to accumulating extrapolation error in its λ_i(s,a) weights. Figure 2 shows that bounding λ_i with a sigmoid stabilizes performance, directly linking extrapolation error to observed instability in a previously unexplained failure case.

4. **Controlled ablation studies isolating component effects** — Section 5.3 systematically separates the effects of λ annealing and ensemble size on both TEE (Figure 4) and task performance (Figure 5). The paper honestly acknowledges failure modes (e.g., AEQMIX with M=2 underperforming QMIX due to premature annealing), which strengthens credibility.

5. **Significant empirical improvements on challenging benchmarks** — The paper reports improvements across 15 SMAC maps, 5 GRF maps, and 15 SMACv2 maps. The strongest results are on SMACv2, where gains can be dramatic (e.g., 0% to 70% win rate). The approach extends to off-policy policy-based methods (AEFACMAC, AEMADDPG), demonstrating generality.

## Weaknesses

### Major

- **TEE empirical measurement is not specified** — The paper defines TEE theoretically as y_{s,a} − \hat{y}_{s,a}, where \hat{y}_{s,a} requires the optimal parameters \hat{θ} = arg min_θ E_π[(Q(s,a;θ) − y_{s,a})²]. However, Figures 1(b)(c) and 4 plot measured TEE values without any explanation of what proxy was used to compute \hat{y}_{s,a} in practice (e.g., Monte Carlo returns, a separately trained oracle, or an iterative approximation). Since these TEE plots are presented as primary evidence for the paper's core diagnosis (that value factorization reduces extrapolation error), the omission makes a central piece of evidence opaque and unverifiable. This does not invalidate the paper's main performance claims, which stand independently, but it does weaken the mechanistic support for the diagnosis.

### Minor

- **Proposition 1's theoretical analysis is informal** — The EPC argument (lines 128–138) is presented as intuitive text with a gradient-descent illustration, not a rigorous proof. The first-order Taylor expansion in Eq. (6) (line 107) is acknowledged to assume "errors are relatively small," but no justification is given for why this holds in the settings studied. The paper would benefit from a more precise statement of the conditions under which the Taylor approximation is valid.

- **No statistical significance reporting on main results** — The paper reports mean win rates (Table 1, Figure 3) without standard deviations, confidence intervals, or number of seeds. Given the well-known variance of MARL training, this makes it difficult to assess whether reported improvements are statistically reliable. As a point of reference, the paper does report mean and standard deviation for λ_i values in the QPLEX analysis (line 152), suggesting this information exists but was omitted for the main results.

- **Limited controlled baselines isolating the techniques** — The ablation studies (Section 5.3) compare different λ and M settings, which is good. However, the main experiments compare AEQMIX only to vanilla QMIX (and AEFACMAC/AEMADDPG to FACMAC/MADDPG). Adding baselines such as QMIX with a fixed large λ (no annealing), or QMIX with ensembled targets but no multi-step, would more clearly separate the contribution of each component from the broader class of known techniques (multi-step returns, ensembling). This is a scope-for-improvement point rather than a fatal gap, since the ablations do partially address this.

- **Policy-based extension results are thinly described** — Section 5.2 and Figure 3 present results for AEFACMAC and AEMADDPG with only the vague specification "on SMAC" and no number of maps. The text description is a single paragraph. Given that FACMAC already uses Peng's Q(λ), demonstrating that the added annealing and ensemble provide meaningful improvement requires more detail about the experimental setup and breadth of evaluation.

### Trivial

- The λ annealing schedule (Eq. 8) is described as "chosen heuristically" (line 209) with α=10/T, and the paper notes it is "not very sensitive" to the exact schedule. Providing a sensitivity analysis or even a reference to the heuristic's motivation would improve reproducibility.
- Some sections of the method description (e.g., lines 237–238) appear to contain garbled/transposed text from copy editing, making a few design choices (shared mixing network, double Q-learning integration) harder to parse than necessary.

## Nice-to-Haves

- A controlled comparison to QMIX with fixed large λ (no annealing) would cleanly separate the effect of annealing from multi-step bootstrapping alone.
- Clarifying whether the policy-based results (Figure 3) span multiple SMAC maps or a single map, and adding error bars.
- A brief sensitivity analysis of the annealing rate hyperparameter α.

## Removed Points

- **TEE as a "fatal" flaw** — The harsh critic described the unspecified TEE measurement as making the paper "not ready for acceptance" and compromising the central evidence. I downgrade this from Fatal to Major because: (1) the paper's core contribution (the techniques and their empirical performance gains) does not depend on the absolute TEE numbers — the relative ordering QMIX < centralized Q-function in TEE would likely hold under any reasonable proxy, and the performance improvements of AEQMIX over QMIX are reported as win rates, not TEE; (2) the weakness is addressable: the authors could clarify the proxy in rebuttal. A fatal flaw must be unambiguous from the paper as written, and here the performance claims remain intact.

- **Missing reproducibility details (hyperparameters, architectures)** — These are standard appendix content, and the parser strips those sections. Removed per instructions.

- **Missing related works** — Removed per instructions, as I cannot verify which works exist or not.

- **Formatting/style nitpicks** — Removed per instructions (these are parser artifacts, not author errors).

- **"Proposition 2 bound is cited"** — The harsh critic noted this is from Kozuno et al. This is correct — the paper properly cites the source (line 197). This was raised as a weakness but is not; it's standard scholarship.

- **Strawman: "FACMAC already uses PQL so the contribution is unclear"** — The paper's contribution is not that PQL is novel, but that the specific combination of *annealing* λ (rather than fixing it) and *ensembling* provides benefits. The paper acknowledges FACMAC uses PQL (line 179). This criticism misreads the contribution.

- **Claim that results on simple SMAC maps "are not significant" is a weakness** — The paper itself acknowledges this (line 248: "Due to the simplicity of some maps, the performance improvement is not significant"). An honest self-criticism should not be repeated as a reviewer-identified weakness.

- **"AEQMIX(2) underperforms QMIX"** — The paper explains this as premature λ annealing (line 276). This is an honest limitation discussion, not an unacknowledged weakness.

## Novel Insights

The reviews converge on the observation that the paper's core framing — shifting attention from representational capacity (TAE) to extrapolation error (TEE) as the primary bottleneck in MARL — is timely and well-motivated, but the empirical support for this specific diagnosis has a methodological gap (opaque TEE measurement). The harsh critic's severity assessment is softened by noting that the central performance results (AEQMIX > QMIX) do not depend on the contested TEE plots. Both reviews agree that the paper's most compelling contribution is not the individual techniques (which are adapted from single-agent RL) but the unified analysis of why they work through the lens of extrapolation error. A genuinely novel synthesizing observation: this paper is best read as an *analytical* contribution with a practical demonstration, not as a new-algorithm paper — and it should be evaluated on whether the analysis is compelling and honest, which it largely is, with the TEE specification being the one missing piece.

## Suggestions

1. **Specify the TEE measurement proxy** — In the rebuttal or revision, explain exactly how \hat{y}_{s,a} was computed for Figures 1 and 4. Even a simple description (e.g., "we used n-step Monte Carlo returns as a proxy for the true target") would resolve the most significant weakness.
2. **Add standard deviations or confidence bands** to the main win-rate results (Table 1, Figure 3) so readers can assess statistical significance.
3. **Add a fixed-large-λ baseline** (QMIX with λ=0.8 or similar, no annealing) to the main results table to isolate the effect of annealing separately from ensembling.
4. **Clarify the policy-based experiments** — specify which SMAC map(s) Figure 3 covers, and ideally extend to at least 2–3 maps to support generality claims.
5. **Tighten the language around the central claim** — phrases like "the success of value factorization methods can be largely attributed to their ability to mitigate this error" (abstract, line 7) slightly overclaim given the correlational nature of the evidence. The paper would be stronger if it said "the success of value factorization methods is *significantly aided by* their ability to mitigate this error" or similar.
