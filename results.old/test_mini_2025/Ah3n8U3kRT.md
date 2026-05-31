Now I have all the information needed. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper introduces median-based gradient estimation for zeroth-order (ZO) convex optimization and multi-armed bandits under symmetric heavy-tailed noise. The key theoretical advance is proving that the median estimator has bounded second moment for any κ>0 (including κ≤1, where no existing ZO method applies), yielding convergence and regret bounds that match optimal rates for bounded-variance noise and do not degenerate as κ→1. The authors present three algorithms (ZO-clipped-med-SSTM, ZO-clipped-med-SMD, Clipped-INF-med-SMD) with corresponding theory and supporting experiments.

## Strengths

- **Non-degenerating convergence for previously unattainable noise regime (κ>0)**: Lemma 1 proves the median estimator is unbiased with bounded second moment under symmetric noise with any κ>0, including cases where the noise has unbounded expectation. This is the paper's central technical novelty. Prior work [20] required κ∈(1,2] and their rates degenerate as κ→1.

- **Convergence rates matching bounded-variance optimality for all κ>0**: Theorem 1 (Table 1) shows ZO-clipped-med-SSTM achieves iteration complexity that does not blow up as κ→0, matching Õ(d²ε⁻²) for Lipschitz oracles — directly contrasted with prior ZO-clipped-SSTM whose complexity scales as (√d/ε)^{κ/(κ-1)} and is undefined for κ≤1.

- **Optimal Õ(√(dT)) regret for MAB under heavy-tailed rewards**: Theorem 3 proves that Clipped-INF-med-SMD achieves regret matching the Ω(√(dT)) lower bound for bounded variance, while prior heavy-tail MAB bounds scale as T^{1/κ}. The bound holds with controlled large deviations, not just in expectation.

- **Unified algorithmic framework**: The median clipping technique is cleanly applied across three settings (unconstrained ZO, constrained ZO, and MAB), demonstrating versatility.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Insufficient support for "convergence in probability" claim in MAB experiments**: Section 5.1 states "HTINF and APE do not have convergence in probability, while our Clipped-INF-med-SMD does." The text only reports mean regret values (~0.1 for HTINF vs ~0.2 for Clipped-INF-med-SMD) and success probabilities (~0.9 vs ~0.6), which do not by themselves support the convergence-in-probability claim. The shaded 0.05–0.95 percentile bands in Figure 1 would be the relevant evidence, but their implications are not discussed. This creates a disconnect between the claim and what the text describes. The authors should explain what the percentile bands show and why they support the claim, or moderate the claim.

- **Limited experimental scale and replication**: ZO experiments report results over only 3 launches (Section 5.3). While appendix D.2 mentions additional experiments, the main paper's evidence is thin. The MAB experiment uses only d=2 arms. The synthetic ZO problem (min ‖Ax−b‖₂ + ⟨ξ, x⟩) is a single problem instance. Stronger conclusions would require more runs and problem variations.

- **Cryptocurrency experiment is a full-information setting, not bandit**: Section 5.2 describes a portfolio optimization task where "we observe the whole income vector r_{t,i} for each asset i" — this is full-feedback, not the bandit setting that Theorem 3 addresses. While adapting the algorithm is fine, the experiment does not validate the bandit theoretical claims. The baselines (hold ETH, efficient frontier) are also very simple, making it hard to extract meaningful conclusions.

- **ZO experiments compare median-clipped vs. non-median only within each algorithm class**: The ZO experiments (Figure 3) compare ZO-clipped-med-SSTM vs ZO-clipped-SSTM and ZO-clipped-med-SGD vs ZO-clipped-SGD. The comparisons are within-family (SSTM vs med-SSTM, SGD vs med-SGD), which is appropriate, but there is no comparison against other principled heavy-tail ZO methods (e.g., truncation-based estimators) beyond the ones from [20].

### Trivial
None.

## Nice-to-Haves
- An intuitive explanation of why the median estimator works for any κ>0 while clipping fails for κ≤1, beyond the formal Lemma 1, would help readers.
- Ablation on the median size m in the ZO setting, not just the MAB setting, to complement the claim that tuning is easy.
- Clarifying whether the "convergence in probability" claim for MAB is about concentration of the regret distribution (which the percentile bands would show) vs. convergence of the mean.

## Removed Points
- **Harsh critic's "critical contradiction" about MAB results**: The harsh critic claimed the MAB experiment "contains a critical contradiction" because HTINF has lower mean regret and higher success probability than Clipped-INF-med-SMD, yet the paper claims HTINF does not have convergence in probability. This confuses two distinct concepts: mean regret (a point estimate of average performance) does not determine convergence in probability (whether the distribution concentrates). A method with lower mean regret but wide percentile bands may not converge in probability. The paper's claim is about the latter. The real issue is insufficient textual explanation, not a logical contradiction. **Removed because the criticism misunderstands the claim.**

- **Harsh critic's "cannot be accepted without major revision to experimental reporting"**: The harsh critic escalated this to a fatal flaw. Since the theoretical core is the paper's primary contribution and the MAB claim is about convergence in probability (which the percentile bands could support), this characterization is disproportionate to the actual weakness. **Removed because the criticism overstates the severity — the issue is insufficient exposition, not falsification.**

- **Strength Finder's "Practical tuning simplicity"**: The claim that median size m "only slightly affects convergence" is based on a brief qualitative comment in Section 5.3 with limited evidence. While likely true, this is a weak, unsupported strength. **Moved here because the evidence is thin.**

- **Strength Finder's "Superior performance for extremely heavy tails (κ≤1)"**: The experiments do show improvement for κ≤1, but only on one synthetic problem with 3 runs. This strength is valid in spirit but should be tempered given limited experimental scope. **Removed because it overlaps with the properly listed theoretical strengths and the empirical evidence is too thin to be a standalone strength.**

- **Strength Finder's "Novel noise assumption"**: The paper introduces Assumption 3 (symmetric noise with scale function), which is indeed novel. However, this is subsumed by the "median estimator works for any κ>0" strength since the assumption enables that result. **Merged into the first listed strength.**

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Rewrite Section 5.1 to clearly explain what the percentile bands (0.05 and 0.95) in Figure 1 show, and how they support the convergence-in-probability claim. If the data supports it, show the inter-percentile range over time to make the argument visible.
2. Increase the number of random seeds/runs for the ZO experiments and report variability (error bars or percentiles).
3. Add a simple baseline or ablation in the ZO experiments that uses symmetric-noise-only methods (if any exist) to isolate the benefit of the symmetry assumption.
4. Clarify that the cryptocurrency portfolio experiment is a full-feedback setup and not a bandit problem, or replace it with a proper bandit experiment with real data.

## Score and Decision

Let me now do calibration searches to finalize the score.

**Round 1 bracket**: From the first calibration call, I searched for papers on zeroth-order optimization with heavy-tailed noise. The weak band (avg < 3.5) returned papers on unrelated topics with scores 2.5–3.0. The middle band (3.5–7.5) returned relevant papers with scores 5.33–7.0. The strong band (>7.5) returned papers on other topics with scores 7.67–8.0. The paper clearly does not belong in the weak band. It is not clearly in the strong band either (the strong-band papers are on different topics and have cleaner, more complete contributions). **Initial bracket: between 4.0 and 7.0.**

**Round 2 narrowing**: I searched for more targeted anchors.
- B21c9hT1D7 (heavy-tailed regression, avg 6.33) — similar heavy-tail topic, good individual scores but rejected overall. This paper has stronger theory
but our paper has broader algorithmic scope.
- z7JBs8UOLI (robust OCO, avg 5.75, reject) — relevant corruption-robust setting, similar theoretical depth but rejected.
- SrGP0RQbYH (adaptive line search, avg 6.25, poster) — clean empirical+theory paper. Our paper has stronger theory but weaker experiments.
- ywFOSIT9ik (ZO optimal perturbations, avg 6.80, spotlight) — close topical match. Similar theory-first structure, better experiments and presentation than our paper.
- AfhNyr73Ma (ZO stability, avg 7.0, poster) — clean theory paper. Better presented than our paper.

Comparing concretely: ywFOSIT9ik (6.8, spotlight) had a nice theoretical idea with clean experiments and good presentation. Our paper has a more significant theoretical advance (handling κ≤1 is a genuine barrier that prior work could not cross) but significantly weaker experiments and less polished presentation of the MAB results. The current paper is slightly below that anchor's quality level when considering the full package. Anchors in the 5.75–6.33 range (z7JBs8UOLI, B21c9hT1D7, SrGP0RQbYH) are comparable in overall quality — each has a solid core contribution but some weakness in either theory rigor, experiments, or presentation. Our paper fits into this band with the distinction that its theoretical advance is arguably more significant than any of those.

**Final score**: 6.0

**Decision**: Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>