- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 5, 6, 1
Now I have a thorough understanding of the paper content. Let me construct the consolidated review.

## Summary

The paper proposes SurvCG, which integrates survival analysis (CoxTime model) predictions of flight connection reliability into column generation for the crew pairing problem (CPP). The core idea is to replace deterministic planned costs with a reliability-aware cost that penalizes connections likely to fail under delays, then solve using standard column generation. On a real-world BTS On-Time Performance dataset, the approach reduces total propagated delay (TPGD) at the 99th percentile by up to ~61% compared to a nominal deterministic solution, and also reduces deadheading connection costs by up to 13.58%. A public benchmark instance and a new evaluation metric (P-index for survival models) are also contributed.

---

## Strengths

1. **Novel integration of survival analysis with column generation for CPP.** The paper is the first to use time-to-event models to predict flight connection reliability and embed those predictions into the CPP cost function within a column generation framework (Section 1, Fig. 1, Section 2.1). The motivation — that historical averages miss the long tail of delay distributions — is well-argued (Section 1.1).

2. **Clear reduction in propagated delays at high percentiles.** In the 75R,25IR-70 scenario, the 99th-percentile TPGD drops from 2928.25 mins (nominal) to 1130.47 mins (reliable), a ~61.4% reduction (Table 3, Section 4.3). The improvement is consistent across the 98th, 99th, and 100th percentiles, with at least 1000 mins saved at each (line 115).

3. **Reduced deadheading connection costs.** Reliable solutions decrease deadhead connection costs by up to 13.58% while keeping total planned costs essentially neutral (0.003% lower) (Table 2, Section 4.2). This contrasts with prior robust approaches that report 1–3% cost increases (Antolini et al., 2005).

4. **Public benchmark instance from real data.** The paper releases a CPP instance derived from BTS On-Time Performance data (https://anonymous.4open.science/r/SurvCG-Instance-67C6/), providing a reproducible benchmark for future work (Section 4.1, Contribution 3).

5. **Modular framework design.** The SurvCG architecture allows any time-to-event model or reliability cost function to be plugged in, so the contribution is not tied to the specific CoxTime model used for experiments (Section 1, Section 5).

---

## Weaknesses

### Fatal
None.

### Major

1. **No experimental comparison against existing robust/stochastic CPP methods.** The paper compares only to a nominal deterministic solution — the standard CPP solved without any robustness mechanism. The related work (Section 1.1) describes multiple uncertainty-aware CPP approaches (Yen & Birge, 2006; Ionescu & Kliewer, 2011; Dück et al., 2012; Antunes et al., 2019; Lu & Gzara, 2015). Without comparing to even one such baseline on the same dataset and evaluation protocol, the claim of "unprecedented improvements" (up to 61% relative to nominal) cannot be assessed against the actual state of the art. The 61% reduction is over a deterministic planner that is known to perform poorly under disruption, so the magnitude of this number is not informative about whether SurvCG advances beyond existing uncertainty-aware solutions.

2. **Apples-to-oranges comparison with Antunes et al. (2019) in the Discussion.** Section 5 compares SurvCG's up-to-60% TPGD reduction to Antunes et al.'s reported 18–20% reduction, but the paper reports *tail percentiles* (98th–100th) while Antunes et al. likely report *mean* or *average* TPGD. These are not the same statistic, so the cross-paper comparison is misleading. A proper comparison requires implementing Antunes et al.'s method or another robust baseline on the same instance and reporting the same metrics.

### Minor

1. **"First data-driven solution" claim is overstated.** The abstract and introduction state that SurvCG is "the first data-driven solution for uncertainty-aware reliable scheduling" and "first approach to explicitly quantify real-world uncertainties using time-to-event models." However, the related work describes robust CPP methods (Antunes et al., 2019; Lu & Gzara, 2015) that also use historical delay data. The novelty is the *specific use of survival analysis* for this task, not data-driven reliability per se. The claims should be narrowed accordingly.

2. **Only upper percentiles (98th, 99th, 100th) are reported for TPGD; means and medians are absent.** The paper focuses entirely on the far tail of the TPGD distribution. Reporting mean and/or median TPGD would clarify whether the reliable solution improves typical-case performance too or merely shifts costs to the extreme tail. The paper also does not report confidence intervals or standard errors despite running 100 simulations (Section 4.3), making it impossible to assess the statistical significance of the observed differences.

3. **The simulation assumes independent flight delays.** The KDE-based delay injection (Section 4.3) samples delays per flight independently, but real-world delays exhibit strong temporal correlation across connected flights (a delayed inbound flight delays its outbound connection). This simplifying assumption — which the paper does not discuss as a limitation — could affect the realism of the TPGD estimates. (The approach follows Antunes et al. (2019), so it is not unique to this paper, but the limitation should be acknowledged.)

### Trivial
None.

---

## Nice-to-Haves

- An ablation comparing the survival model against a simpler alternative (e.g., reliability = historical proportion of on-time connections for a given route/time window) would isolate the benefit of survival analysis over basic data-driven heuristics.
- Validating the P-index against downstream optimization outcomes (e.g., showing that higher P-index correlates with better TPGD reduction) would strengthen the case for this new metric.
- The 0.003% total cost reduction (Table 2) is essentially zero; the paper should either explain why this is meaningful or characterize it as cost-neutral rather than a cost improvement.

---

## Removed Points

These points from the reviewers were assessed and removed. Treat them with caution.

- **Criticism about the 100th percentile being worse for the reliable solution (Harsh Critic, Critical Issues #2).** The paper's text explicitly states: "showing an improvement of at least 1000 mins (TPGD) for 98th, 99th and 100th percentiles" (line 115). The critic's claim that the 100th-percentile value favors the nominal solution cannot be verified from the extracted text (the table is an image) and directly contradicts the paper's written description. Removed as unverifiable and contradicted by the paper's own reporting.

- **Criticism about missing mathematical formulation (Harsh Critic, Critical Issues #3).** Sections 2.2 and 3 are missing from the extracted text due to PDF parsing — they exist in the original submission. Per the Hard Rules, weaknesses about content stripped by the parser should not be counted against the paper.

- **Criticism about the P-index formulation being missing.** Same as above — the P-index equation was in a section stripped by the parser.

- **"Deadhead cost analysis undercuts narrative" framing.** The paper does not claim that reliability comes at zero cost; it reports that total costs are 0.003% lower, which is essentially neutral. The critic's framing imposes an external narrative not present in the paper.

- **Strength about "up to 61% reduction" being compared to Antunes et al. (2019).** This strength from the Strength Finder conflicts with the verified weakness that the comparison is apples-to-oranges (tail percentiles vs. likely averages). Per the rules, when strength and weakness disagree, the weakness wins. Removed.

- **Generic strengths from the Strength Finder** (e.g., "the paper identifies a real problem," "the idea is interesting") — removed as generic/superficial per filtering rules.

---

## Novel Insights

The harsh critic's most valuable observation is the absence of robust CPP baselines — this forces attention on what is arguably the paper's central shortcoming, and it is a concrete, fixable gap. The interplay between the two reviewers also reveals a tension in the paper's framing: the Strength Finder treats the 61% number as a headline result, while a closer look reveals it is a tail-percentile comparison against a deliberately weak baseline. The paper would be substantially stronger if it acknowledged this tension directly — i.e., clearly distinguishing between "SurvCG beats the deterministic baseline" (which the data convincingly show) and "SurvCG improves over existing robust methods" (which remains unsubstantiated).

---

## Suggestions

1. **Add at least one existing robust or stochastic CPP method as a baseline.** A natural starting point would be the delay-penalty approach from Antunes et al. (2019), which is the most closely related work and also reports TPGD. Implement it on the same instance, report the same TPGD percentiles, and compare.
2. **Report the full distribution of TPGD** — include mean, median, 25th/75th percentiles, and the 100th percentile — to give a complete picture of the trade-offs. Add bootstrap confidence intervals or standard errors over the 100 simulation runs.
3. **Narrow the novelty claims.** Replace "first data-driven solution for uncertainty-aware reliable scheduling" with "first to use survival analysis for reliability estimation in CPP column generation." This is accurate and will not invite pushback from reviewers familiar with the robust-CPP literature.
4. **Explicitly discuss the independence assumption** in the simulation and its potential impact on TPGD estimates, even if only to acknowledge it as a simplification consistent with prior work.
5. **Clarify the comparison metric when citing Antunes et al. (2019)** — specify that SurvCG improves tail percentiles by 60% while Antunes et al. reported average reductions of 18–20%, noting that these are different statistics of the TPGD distribution.

---
