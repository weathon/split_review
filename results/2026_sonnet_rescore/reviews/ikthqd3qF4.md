---

## Summary

This paper proposes a method for evaluating unsupervised anonymous record linkage **without labeled data**, by deriving observable lower bounds on precision and relative recall using a structural constraint: individuals can achieve at most one positive outcome (e.g., a single first-lien mortgage origination). The framework is instantiated using hierarchical agglomerative clustering on 65.5 million confidential HMDA mortgage applications to detect "cross-applicants" who submit multiple applications, achieving an estimated precision lower bound of 92.3%. Theorem 1 and its corollaries provide a compact theoretical foundation; simulation results confirm the bound closely tracks true precision; and the application demonstrates practical feasibility at scale.

---

## Strengths

- **Novel, non-obvious precision bound from structural constraints (Theorem 1):** The core result that Pr[False] ≤ Pr[Mult]/p² enables fully label-free evaluation using only the empirical rate of multi-origination clusters and the unconditional origination rate. Corollaries 1–2 extend this to relative recall and weighted F-scores, enabling principled hyper-parameter search without ground truth (Section 2.2).

- **Tight simulation validation:** At ε = 0.06 in the "with date" specification, the computed precision lower bound is 93.7% while true simulated precision is ~95%, demonstrating that the bound is informative and not vacuously loose (Figures 3a vs. 4a, Section 3.1). The close resemblance between the observable bound curve and the true precision curve is the paper's central empirical validation.

- **Large-scale application achieves high estimated precision without labels:** On 65.5 million confidential HMDA applications, the preferred specification yields 314,344 clusters with 92.3% estimated precision, selected solely from the observable precision–sample-size frontier (Section 4, Figure 5). The practical scale is impressive.

- **Post-hoc precision improvement via identifiable false positives:** Equation (1) and Equation (2) show that excluding clusters with multiple originations (known false positives) tightens the bound further, yielding a refined estimator ᾱ(θ) that strictly improves on the raw Theorem 1 bound (Section 2.2).

- **Domain- and method-agnostic framework:** The three required data properties are generic—single-transaction records, possible repeat submissions per individual, and a structural cap on positive outcomes—making the framework applicable to insurance, college admissions, job offers, and other privacy-constrained settings (Section 1).

---

## Weaknesses

### Fatal
None.

### Major

- **The independence assumption (Assumption 1) may not close the selection concern for false positives.** Theorem 1 rests on the inequality Pr[Mult|False] ≥ p², which the paper proves in Appendix Lemma 1 under Assumptions 1 and 2. Assumption 1 imposes unconditional independence: Pr[O_im = 1 | O_jl = 1] = Pr[O_im = 1] for i ≠ j (stated verbatim in Section 2.2). However, false positive clusters are precisely those pairs of applications that look similar on census tract, race, sex, age, loan type, date, income, loan amount, FICO, and LTV — many of which are strong predictors of origination probability. Applications in false positive clusters therefore oversample pairs from similar origination-rate strata, not random pairs from the marginal distribution. Whether the conditional quantity Pr[Mult|False], over this selected population, still satisfies ≥ p² depends on the joint distribution of origination rates across look-alike pairs. If similar-looking applications tend to come from lower-p borrowers (e.g., borderline applicants sharing modest FICO and LTV values), the direction of the inequality could reverse. The paper does note, helpfully, that for size-2 clusters "it may be reasonable to assume that Pr[Mult|False] = p²" (Remark 1), which would make the bound exact rather than merely valid — but this is presented as an informal heuristic rather than a proved claim. The formal resolution is entirely deferred to Appendix Lemma 1. Since the appendix is not available to reviewers, the load-bearing inequality cannot be independently verified. The paper would benefit substantially from bringing the key step of Lemma 1 into the main text, or providing an empirical check (e.g., comparing the origination rate within the identifiable subset of false positives — clusters with multiple originations — against the population p̂, to confirm the selection effect runs in the right direction).

### Minor

- **Size-2 cluster restriction limits the scope of recall.** Footnote 4 states: "we drop all clusters with more than two applications in both our simulation results and our application." This means genuine cross-applicants who submitted three or more applications are excluded from the detected set and from precision/recall computations. Corollary 1 defines P_tot as the total number of cross-applicants, which includes those with 3+ applications; the reported 92% relative recall in simulation is thus only over the 2-application subset, not P_tot as defined. The paper does not estimate what fraction of true cross-applicants are 3+ application submitters, nor how much absolute recall is sacrificed by this restriction. This is a legitimate scope limitation that deserves explicit quantification.

- **Abstract and conclusion conflate the lower bound with a point estimate.** The abstract states "our preferred specification identifies cross-applicants with 92.3% precision" and the conclusion repeats "achieving an estimated precision of 92.3%." The body of the paper more carefully calls this a "lower bound" and refers to ᾱ(θ) as a bound estimator. The framing in the abstract and conclusion should consistently describe 92.3% as "at least 92.3% precision" to reflect the bound's nature, since Theorem 1 is an inequality.

### Trivial

- **No statistical uncertainty reported for ᾱ̂(θ) = 0.923.** The bound is estimated from ĥat{p} and ĥat{p}_m computed over 65.5 million applications and 314,344 clusters. With samples of this size, sampling variance is almost certainly negligible, but a brief confidence interval or standard error would make the precision guarantee fully rigorous.

- **Simulation robustness:** The simulation uses a specific parametric model (E[n_i] = 1.25, origination probability 0.9 after approval). A brief sensitivity note on how the bound's tightness varies with these parameters would strengthen the validation without requiring additional full experiments.

---

## Nice-to-Haves

- Characterize analytically when the bound is tight versus conservative: from Remark 1, the gap between the bound and true precision equals 1 − p²/Pr[Mult|False]. Understanding what data properties drive this quantity (e.g., homogeneity of origination rates within false positive clusters) would help users know when to trust the bound as near-exact.
- Report precision estimates split by sub-period (e.g., pre- and post-2020 market disruption) as a robustness check for downstream users of the cross-applicant dataset.
- Sub-period or sub-market robustness of the 92.3% figure would bolster practical credibility for users who apply the identified dataset to specific time windows.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **"Circularity in knee selection / model selection across 96 specs"**: The harsh critic argues the knee criterion is subjective and that selecting from 96 specifications ex post is a form of data-snooping. However, the paper explicitly displays the full Pareto frontier (Figure 5) and chooses the knee transparently via Corollary 2's weighted-score interpretation. Choosing a knee on a published frontier is standard practice in precision-recall tradeoffs and is not meaningfully distinct from any other hyper-parameter selection method. The bound is valid for any fixed θ, and the frontier presentation allows readers to choose their own operating point. Removed as a weakness.

- **"Absolute recall is not characterized in the empirical application"**: The harsh critic notes that the conclusion's language about "precision and recall balance" could mislead, since absolute recall is not known. However, the abstract says "minimal loss in *relative* recall," the corollary section explicitly notes P_tot is unknown and only relative comparisons are meaningful, and Section 5 correctly says "relative recall." The body is accurate; the conclusion's brief mention is not an error. Removed.

- **Missing confidence intervals on ᾱ̂**: Kept but demoted to Trivial (not a meaningful concern at n = 314k).

- **Strength Finder: "domain-agnostic framework"**: Kept — this is specific and grounded in Section 1's explicit enumeration of analogous settings.

---

## Novel Insights

The most novel insight surfaced by the reviewer ensemble is the *selection argument* regarding Assumption 1: because false positive clusters arise precisely from applications that look similar on origination-relevant covariates, the marginal distribution of Pr[O|False] is not the same as the marginal distribution of p = Pr[O] in the full population. The bound's tightness therefore implicitly depends on how homogeneous origination rates are within look-alike strata. This observation suggests a potentially important diagnostic: if the paper could show empirically that the origination rate inside identified false positive clusters (those with multiple originations) is close to p̂, it would provide strong in-sample evidence that the selection effect does not invalidate the bound direction. This diagnostic is entirely feasible with the available data and would significantly strengthen the guarantee's credibility.

---

## Suggestions

1. **Bring the key step of Lemma 1 into the main text**, or add a paragraph in Section 2.2 explaining why Assumption 1 (unconditional independence) is sufficient to close the selection argument — specifically, why the conditioning on look-alike covariates does not affect the bound's direction.
2. **Add an empirical check on the bound's direction**: compare the origination rate of applications in clusters with multiple originations (identifiable false positives) against population ĥat{p}. If Pr[Mult|False] ≥ p² holds empirically, this serves as in-sample validation of the bound's validity even if the formal proof is hard to follow.
3. **Revise the abstract and conclusion** to consistently state that 92.3% is a lower bound on precision, not a direct precision estimate.
4. **Quantify 3+-application exclusion**: provide an estimate of how many true cross-applicants are excluded by the size-2 restriction, to give users a sense of the absolute recall sacrifice.

---

## Evaluation on Key Axes

- **Originality:** High. To the authors' knowledge (and consistent with my read), deriving observable, label-free lower bounds on both precision and recall via a structural outcome constraint is a genuinely novel contribution.
- **Importance of research question:** High. Privacy-constrained record linkage is broadly relevant; the HMDA application addresses real fairness, lending-standard, and shopping-behavior research questions.
- **Claims well-supported:** Mostly yes. The simulation validates the bound closely; the application demonstrates scale. The theoretical core (Lemma 1) is deferred to a stripped appendix, creating an unresolved gap.
- **Soundness of experiments:** Good. Simulation design is appropriate; application methodology is transparent; frontier visualization is honest.
- **Clarity of writing:** Good. The framework is clearly laid out, the intuition in Section 2.2 is accessible, and the structure is logical. Minor imprecision in abstract/conclusion language.
- **Value to research community:** High. The domain-agnostic framework is immediately useful to economists and ML practitioners working with privacy-constrained datasets.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>