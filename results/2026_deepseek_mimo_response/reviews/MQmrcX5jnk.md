## Summary
This paper introduces Constrained Mass Transport (CMT), a variational framework for learning molecular Boltzmann generators that constructs intermediate distributions by iteratively solving constrained optimization problems with both trust-region (KL-bound) and entropy-decay constraints. The authors derive closed-form solutions for the optimal intermediate densities (Propositions 2.1–2.3), characterize the resulting annealing paths as geometric, tempered, or geometric-tempered (Theorem 2.4), and demonstrate the method on four molecular systems up to d=219.

## Strengths
- **Closed-form analytical solutions for all constraint variants (Propositions 2.1–2.3):** The paper derives exact expressions for optimal intermediate densities under trust-region (Eq. 5), entropy (Eq. 8), and combined constraints (Eq. 10), reducing the Lagrangian dual to low-dimensional (1D or 2D) concave optimization. These are non-trivial results that make the framework computationally tractable.

- **Rigorous connection to annealing paths (Theorem 2.4):** The theorem (Eq. 12) shows the iterative constrained optimization naturally induces geometric, tempered, and geometric-tempered annealing paths with monotonically increasing, automatically terminating schedules — a principled alternative to hand-tuned geometric schedules. The proof that the combined constraint (Prop. 2.3) reduces to the trust-region-only solution (Prop. 2.1) when η=0 and to the entropy-only solution (Prop. 2.2) when λ=0 confirms internal consistency.

- **Strong empirical results on EUBO and ESS across all four systems (Table 1):** CMT achieves the best EUBO and ESS on all four benchmarks (d=60 to d=219). On the largest system (ELIL tetrapeptide, d=219), CMT attains 26.06% ESS vs. 13.75% (TA-BG) and 7.21% (FAB), demonstrating that the performance gap widens substantially for larger, more complex systems.

- **Compelling ablation study (Figures 2–3):** Demonstrates that both constraints are necessary: omitting the trust-region constraint causes rapid entropy decrease and mode collapse; using only the entropy constraint yields unstable training with entropy decay violations; only the combined geometric-tempered formulation avoids all identified failure modes. Ramachandran plots provide direct visual confirmation.

- **Well-motivated training algorithm with negligible overhead:** Importance-weighted forward KL (Eq. 15) encourages mode coverage, enables sample reuse via replay buffers, and the trust-region constraint bounds importance weight variance (Appendix C.3). The dual optimization adds only ~0.01% of total training time (Section 3).

- **New benchmark (ELIL tetrapeptide, d=219):** Introduces the largest molecular system studied without MD samples, featuring more complex side chain interactions than alanine hexapeptide, extending the frontier for variational approaches.

## Weaknesses

### Fatal
None.

### Major
- **Overclaimed "2.5× higher effective sample size" in abstract and conclusion:** The abstract (line 9) claims "more than 2.5× higher effective sample size" and the conclusion (line 263) repeats "over 2.5× higher effective sample size." Against the strongest energy-only baseline (TA-BG), the actual ratios from Table 1 are: 1.02× (dipeptide), 1.04× (tetrapeptide), 1.63× (hexapeptide), and 1.89× (ELIL). The 2.5× threshold is only reached against FAB on ELIL (26.06/7.21 ≈ 3.6×), but the paper never specifies this particular comparison. The body text in Section 5.2 more honestly states "approximately twice the ESS of competing approaches," which is defensible. The inflated headline claim appears in three prominent locations and should be corrected.

### Minor
- **"Consistently surpasses across all metrics" is contradicted by own results:** The abstract claims CMT "consistently surpasses state-of-the-art variational methods," and Section 5.2 states "across all systems and metrics, our method outperforms the baselines." However, on the largest system (ELIL tetrapeptide), TA-BG achieves lower RAM TV (2.54×10⁻²) than CMT (3.13×10⁻²) — the paper itself bolds TA-BG's result as best in Table 1. CMT wins on EUBO and ESS on all four systems and on RAM TV for three of four, which is strong overall. But the blanket "across all metrics" claim is not what the table shows.

- **Limited statistical evidence on the key benchmark:** TA-BG on ELIL had only 2 successful runs out of 4 due to numerical instabilities (disclosed in Table 1 caption). The most important comparison rests on weaker statistical evidence than the other benchmarks.

### Trivial
None.

## Nice-to-Haves
- A brief discussion of why CMT does not improve RAM TV on ELIL despite winning on EUBO and ESS would strengthen the analysis. Is this a metric artifact (ESS/EUBO measure global distributional quality while RAM TV measures a specific 2D projection)? Could TA-BG's lower RAM TV on ELIL reflect mode collapse elsewhere?
- A sentence in the main text explaining why the trust-region constraint controls importance weight variance (the scalability claim at line 144) would improve accessibility without requiring readers to find Appendix C.3.

## Removed Points
No points were removed. Both the harsh critic's and strength finder's substantive claims were verified against the paper and found accurate.

## Novel Insights
The paper's most novel theoretical insight is that combining trust-region and entropy constraints in a single variational problem yields closed-form solutions that naturally induce geometric-tempered annealing paths — a family that avoids both mass teleportation (the failure mode of geometric-only paths, as illustrated in Figure 1) and insufficient initial overlap (the failure mode of tempered-only paths). This provides a principled, optimization-theoretic foundation for annealing schedule design that goes beyond the existing manual tuning approaches. The empirical novelty of introducing ELIL tetrapeptide as a large-scale benchmark for energy-only variational sampling is also a valuable community contribution.

## Suggestions
- Replace the "2.5×" claim in the abstract and conclusion with an accurate statement (e.g., "up to 1.9× higher ESS against the strongest baseline on the largest system" or "up to 3.6× against FAB on the hardest benchmark").
- Qualify "consistently surpasses across all metrics" to acknowledge the TA-BG RAM TV advantage on ELIL, perhaps with a brief discussion of why this discordance exists.
- Add a sentence in Section 3 briefly justifying the importance weight variance bound claim.
- Briefly discuss the RAM TV discordance on ELIL in Section 5.2.

## Calibration Report

**All anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| kKXIYUi8ff (DynamicsDiffusion) | 3.00 | R1 | Much weaker — no closed-form solutions, limited evaluation |
| OcTUquFXfx (Global Minima) | 2.60 | R1 | Much weaker — different domain, limited |
| SEvJfuCtPY (Phase-aware training) | 3.00 | R1 | Weaker — narrow analysis on toy setting |
| ItPYVON0mI (CG potentials) | 3.00 | R1 | Weaker — limited evaluation |
| XcAJ0qsMgh (Annealing Flow) | 3.60 | R1 | Similar topic but much weaker evaluation, high variance, rejected |
| TUvg5uwdeG (Neural Sampling from Boltzmann) | 6.40 | R1 | Very similar topic but concerns about novelty/missing prior work; CMT is cleaner and better evaluated |
| ybWOYIuFl6 (BNEM) | 6.00 | R1 | CMT evaluates on much larger systems (d=219 vs 2D) |
| pRCOZllZdT (BoPITO) | 7.00 | R1 | CMT is stronger: more systems, no pre-training assumption, better evaluation |
| NSVtmmzeRB (GeoBFN) | 8.00 | R1 | Different focus (generation vs sampling), but uniformly strong; CMT not quite at this level due to overclaiming |
| ZCOwwRAaEl (NF-BO) | 8.00 | R1 | Different domain; uniformly strong |
| uKZdlihDDn (Diffusion Graph Networks) | 7.60 | R1 | Different domain; similar quality level |
| bH6T0Jjw5y (T-IB) | 8.00 | R1 | Different domain; strong |
| P6IVIoGRRg (Annealed LMC) | 7.00 | R2 | Strong theory for annealed MCMC; CMT has better empirical evaluation alongside comparable theory |
| h8yg0hT96f (Bayesian Exp Design) | 7.33 | R2 | Different domain; comparable quality level |
| V5kCKFav9j (Constrained OT) | 5.75 | R2 | CMT is stronger: cleaner empirical validation |
| kxebDHZ7b7 (TRAM) | 6.75 | R2 | Trust region concept in different setting; CMT is more novel |
| NSlvSDQ8aE (FBM) | 7.00 | R2 | Rejected despite 7.0 avg; CMT has broader evaluation and cleaner novelty |

**Round 1 bracket:** 6.5–8.0. The paper is clearly above the 6.0–6.5 rejected anchors (BNEM, Neural Sampling) which share the same topic but have weaker evaluation or novelty concerns.

**Round 2 bracket:** 6.5–7.5. CMT is comparable to or slightly above the 7.0 anchors (BoPITO, Annealed LMC, FBM) due to more thorough empirical evaluation and cleaner novelty, but falls short of the 8.0 anchors (GeoBFN) due to the overclaiming issue.

**Final score:** 7.0. The paper has a genuine, novel theoretical contribution (closed-form constrained variational solutions with annealing path characterization) supported by strong empirical results (best EUBO and ESS on all four systems, thorough ablation, new benchmark). The main weakness — overclaimed "2.5×" headline and "consistently surpasses across all metrics" language — is a presentation issue, not a methodological one. The underlying results are strong enough to stand on their own without inflation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>