## Summary
The paper proposes median-of-samples gradient estimators for zeroth-order non-smooth convex optimization and stochastic multi-armed bandits under symmetric heavy-tailed noise. By taking a component-wise median across (2m+1) samples that share the random smoothing direction, the estimator becomes unbiased and has bounded second moment for any tail index κ > 0 (including infinite-mean regimes), enabling clipped accelerated SSTM, mirror descent, and INF-style algorithms with rates that match the bounded-variance baselines and a Õ(√(dT)) MAB regret.

## Strengths
- **Conceptually clean and technically novel estimator (Lemma 1, §3.1.2):** Sharing one random direction **e** across the 2m+1 noise samples and taking a component-wise median yields an unbiased gradient estimate with bounded second moment for any κ > 0 — circumventing the κ > 1 barrier that previously limited [20].
- **Theoretical scope (Theorems 1–3, Table 1):** Rates of Õ(d² ε⁻²) for unconstrained ZO, an SMD analog for compact constraints, and Õ(√(dT)) regret for MAB; these match optimal bounded-variance bounds and apply in regimes (κ ≤ 1, possibly unbounded mean) not covered by prior heavy-tailed work.
- **Extensions integrate cleanly (Remarks 1, 2):** Smooth and PL objectives slot into the same scaffolding via standard restart arguments without breaking the rate structure.
- **Experimental validation in the κ ≤ 1 regime where it matters most (Fig. 3):** For α = κ = 0.75 and 1.0, median-clipped ZO methods do clearly outperform their non-median counterparts, supporting the central theoretical claim.

## Weaknesses

### Fatal
None.

### Major
- **Headline MAB experiment does not visibly support the headline claim (Fig. 1, §5.1).** Verified directly: HTINF reaches lower average regret (~0.1 vs ~0.2) and higher best-arm probability (~0.9 vs ~0.6) than Clipped-INF-med-SMD on Cauchy-like noise — exactly the κ < 1 regime the paper advertises. The text rescues this with "HTINF and APE do not have convergence in probability, while ours does," presumably referring to the percentile bands, but neither the figure caption nor the text actually demonstrates this gap quantitatively (e.g., via a CDF/percentile plot of regret across the 100 runs). The single empirical MAB plot in the body therefore looks like the proposed method losing on both metrics, while the abstract claims it "dramatically outperforms" baselines for κ ≤ 1. — This undermines the practical narrative behind §1.1.
- **Cryptocurrency experiment does not test the contribution (§5.2).** Baselines are "hold ETH," Efficient Frontier, and Random — none of them heavy-tailed bandit algorithms — and the setting is full-feedback portfolio optimization adjusted from the bandit algorithm, not the MAB problem the theory addresses. As written, this experiment cannot support any claim about the method's superiority on real heavy-tailed bandit data.
- **Worse d-dependence in the κ ∈ (1, 2] regime is not acknowledged (Table 1, §6.2).** For κ = 2 the bound from [20] reduces to Õ(d M_2'² / ε²), while the new bound is Õ(d² M_2'² / ε²) — a factor of d worse in the most common heavy-tailed regime. The paper presents the result purely as an improvement, hiding that median clipping costs a dimensional factor in the regime where prior bounds were already non-degenerate.

### Minor
- **Assumption 3 (Eq. 4) is more restrictive than "symmetry + bounded κ-th moment."** The claim that it "covers a majority of symmetric absolutely continuous distributions with bounded up to κ-th moments" is asserted without proof or characterization. Since every rate improvement leans on this single assumption, a precise statement of the distributional class would strengthen the paper.
- **Hidden κ-dependence in constants is not surfaced.** The σ² and c² bounds carry a (4/κ)^(2/κ)·(2m+1) factor that blows up as κ → 0; the slogans "Õ(d² ε⁻²)" and "Õ(√(dT)) for any κ > 0" hide this in the tilde. Reporting the κ-dependence in the constants in the contributions section would be more honest.
- **Theory–practice gap in m.** Theorems 1–3 require m = 2/κ + 1 (so m → ∞ as κ → 0), while §6.1 says "in practice take m = 3" and the experimental grid is [3, 5, 7]; the regime where the contribution is sharpest (small κ) is precisely where the practical recipe diverges from the theoretical requirement.
- **Single ZO test problem and only 3 seeds (Fig. 3).** The synthetic ‖Ax − b‖ + ⟨ξ, x⟩ instance with 3 launches is thin; no variance bands and no scan over d (the parameter the rate is in d) make it hard to read the log-scale curves.
- **Claim that Theorem 1's first term "matches the optimal bound for deterministic non-smooth problems"** is loose: that lower bound is in ε only, while the paper's term carries a d^(3/2) factor. The qualifier should be added.

### Trivial
- §4 conflates notation between "d arms" and the standard "K arms" in the MAB lower bound.

## Nice-to-Haves
- A CDF/percentile plot of regret across runs that actually shows the "convergence in probability" advantage for Clipped-INF-med-SMD.
- A direct head-to-head with [20]'s ZO-clipped-SSTM at κ ∈ (1, 2] to quantify the practical cost of the dimensional factor.
- Asymmetric-noise robustness study moved into the main body (currently §D.2.1).
- ZO experiments varying d.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **"ZO-clipped-SGD competitive with median variants undermines the necessity of median clipping" (harsh critic #3).** Partially weakened: in the κ ≤ 1 panels of Fig. 3, the paper reports median variants do significantly outperform non-median variants ("for extremely noised data κ ≤ 1, our median clipping-based methods significantly outperform non-median versions"), which is the regime where the contribution is claimed. The SSTM-vs-SGD ordering is a separate observation about acceleration, not about median clipping, so framing it as undermining the contribution is partly a misread.
- **Generic "novel framing important problem" type strengths from the strength finder** were dropped where they were essentially restatements of the abstract.

## Novel Insights
None beyond the paper's own contributions. The genuinely novel observation is the paper's own: sharing the random direction **e** across the 2m+1 noise samples lets symmetry of the *post-smoothing* noise be inherited by each median sample, so component-wise median yields unbiasedness while moment control is bought by m > 2/κ.

## Suggestions
- Replace Fig. 1 with a percentile/CDF view that quantitatively shows the convergence-in-probability advantage, or add experiments at additional κ values where Clipped-INF-med-SMD beats HTINF on the mean as well.
- Add a heavy-tailed-bandit baseline (HTINF/APE/INF-clip) to the cryptocurrency experiment, or remove the "real-world" framing from the body.
- Acknowledge in Table 1 / §6.2 the d-factor cost at κ ∈ (1, 2]; presenting both the gain (κ → 0) and the trade-off honestly will strengthen rather than weaken the contribution.
- Characterize precisely which symmetric distributions satisfy Eq. (4); e.g., show that all symmetric stable distributions and Student-t do, and state any exclusions.
- Surface the κ-dependence in the constants of Theorems 1 and 3 in the contributions list rather than hiding it in tildes.

## Evaluation
- *Originality:* Solid — the symmetry-exploiting median-of-samples ZO/MAB construction is non-trivial and not in prior work.
- *Importance:* Moderate — heavy-tailed ZO/MAB is an active subarea, and breaking the κ > 1 barrier under symmetry is meaningful.
- *Soundness of claims:* Theory looks correct; empirical claims of "dramatically outperform" are partially unsupported by the body figures.
- *Soundness of experiments:* Weak — limited seeds, missing relevant baselines in the real-world experiment, headline MAB plot at odds with the headline claim.
- *Clarity:* Mostly clear; notational and qualifier slips noted above.
- *Value to community:* Useful technique and analysis, though acceptance hinges on the empirical story being tightened.

## Calibration
Anchors retrieved (all paths under `/home/wg25r/split_review/datasets/deepreview_13k_calibration/`):
- **NKotdPUc3L.md (avg 7.0, Accept)** — heavy-tailed nonconvex SGD without clipping; cleaner theoretical novelty than the paper under review and stronger framing.
- **jmN1zXMq0O.md (avg 6.5, Accept)** — clipping dynamics under noise; close topical match with stronger empirical/theoretical alignment.
- **AfhNyr73Ma.md (avg 7.0, Accept)** — ZO stability/generalization; topically adjacent, used as high anchor for ZO theory.
- **89EjtiGWVS.md (avg 5.75, Reject)** — robust estimation under heavy tails via LSE; closest mid anchor — solid theory, mixed empirics, similar profile.
- **yID2fdta1Z.md (avg 5.0, Reject)** — robust aggregation; mid anchor.
- **ys16t9FcLN.md (avg 5.0, Reject)** — distribution-dependent MAB; mid bandit anchor.
- **vQIVbfTMzf.md (avg 3.25, Reject)** — self-tuning robust estimation; low anchor — weaker theoretical scaffolding than the paper under review.
- **e2F0mJJeN0.md (avg 3.0, Reject)** — robust data pruning via geometric median; low anchor with limited rigor.
- **uxFme785fq.md (avg 2.5, Reject)** — DP+BLB inference; off-topic low anchor.

The paper sits above the low anchors (its theory is correct and non-trivial; Lemma 1 and Theorems 1, 3 are real contributions) but below the high anchors (89EjtiGWVS is a closer profile match — solid theory, weak/mismatched experiments, headline claim unsupported by figures, with a 5.75 Reject). Given the central empirical claim ("dramatically outperform for κ ≤ 1") is contradicted by the body's only MAB figure, the unacknowledged d-cost at κ ∈ (1, 2], and the limited experimental validation, the paper lands near the mid-anchor cluster, slightly below 89EjtiGWVS.

MY FINAL SCORE: <pineapple>5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>