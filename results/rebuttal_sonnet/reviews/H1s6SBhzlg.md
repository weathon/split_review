## Summary

The paper proposes OW (Bayesian-optimal under conditional independence and symmetric noise) and ISP (a counterfactual variant of the surprising popularity rule), along with two unsupervised variants OW-L and OW-I that estimate agent accuracies from second-order moments. Methods are validated on simulated data and three real-world datasets (UltraFeedback, MMLU, ARMMAN), consistently outperforming majority voting.

---

## Rebuttal Assessment

### Weakness: OW-L and OW-I produce bit-identical results with no explanation

- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author points to Section 5.4 text: "OW-L attains the highest accuracy in 66.67% of the cases, OW-I in 72.92%." I verified this in the paper (line 313). This is genuine in-paper evidence that the two methods *diverge* across the broader 16-ensemble evaluation, meaning the coincidence in Table 3 and Table 4 is regime-specific to the four strongest models. The rebuttal's proposed explanation — that both methods converge to similar weight estimates in the high-accuracy regime of the four strongest models — is plausible and partially substantiated by this existing data. However, the actual explanation is a revision promise ("we will add a paragraph"), not currently in the paper. The original reviewer's complaint was that *no* explanation is offered; the evidence cited does not substitute for the explanation.
- **Score impact:** Weakness downgraded from major to minor (the Section 5.4 win-rate divergence is real in-paper evidence that the methods are not globally equivalent; the concern was overweighted).

---

### Weakness: No aggregation baselines other than majority voting

- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a defense, though the structural argument has merit. The author argues that confidence-weighted baselines require log-probabilities unavailable from black-box GPT-4o, and calibration-set baselines require labeled data excluded by design. This is a reasonable structural constraint, but it is not explicitly stated in the paper—the rebuttal extrapolates from the unsupervised framing. More importantly, open-weight models (Qwen, Llama, Phi) do provide log-probabilities, and a calibration-set comparison on even one dataset would be informative. The resolution is entirely a revision promise.
- **Score impact:** Weakness unchanged (still major).

---

### Weakness: Formal gap between expected-advantage improvement and accuracy improvement

- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author cites Section 4.2 (line 205): "effective aggregation requires the correct label s* to attain the largest advantage." I verified this is in the paper. The argument that a rightward-shifted advantage distribution for s* implies higher selection probability under the symmetric model is logically sound and partially closes the gap. However, it remains informal; the paper does not bound the variance of advantage distributions or formally show the ordering transfers from expectation to probability. The simulation (Table 2) validates the ordering under model assumptions. The formal bridge is still promised as a revision.
- **Score impact:** Weakness unchanged (still minor, as originally assessed).

---

### Weakness: Appendix C extension under correlated agents not summarized in main text

- **Author's response:** Acknowledge
- **Assessment:** Honest but not resolved. The author confirms Section 2, Assumption 1 already contains the pointer ("extend all our theoretical results to a more general setting in Appendix C"), verified at line 63 of the paper. The failure to summarize what those results actually show remains. Resolution is a revision promise.
- **Score impact:** Weakness unchanged (minor).

---

### Weakness: Simulation validates model assumptions rather than robustness

- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly notes that Section 2 explicitly anticipates the limitation ("this assumption may not hold perfectly in the LLM setting"), and that the three real-world datasets are intended robustness proxies. This is verified in the paper (line 63). The consistent improvements across 16 ensembles (97.92% win rate for OW-L) provide meaningful empirical evidence of robustness. However, a targeted simulation under correlated agent errors would be more diagnostic. The point stands as a minor limitation.
- **Score impact:** Weakness unchanged (minor).

---

### Weakness: Bradley-Terry justification overstated

- **Author's response:** Acknowledge
- **Assessment:** Honest. The paper text at line 92 reads "thereby providing a theoretical justification for the validity of the BT model" — confirmed overstatement. The author promises to revise to "...providing a theoretical justification for the inverse-logistic weighting scheme that underlies the Bradley–Terry model in this aggregation setting." Resolution is a revision promise.
- **Score impact:** Weakness unchanged (trivial).

---

## Strengths

- **Bayesian-optimal aggregator with explicit closed form (Theorem 1, Algorithm 1).** Under conditional independence and symmetric noise, $f_{OW}$ with weights $\omega_i = \sigma_K^{-1}(x_i)$ is proven MAP-optimal among all aggregators. Verified in the paper (lines 73–92).
- **Provable ordering ISP ≥ MV ≥ SP with closed-form gap expressions (Theorem 2).** Equations (209–213) give explicit gap formulas showing the ISP advantage decays $\Theta(1/K)$ while the MV-over-SP gap is $\Theta(1)$. Verified at lines 207–215.
- **Statistically significant gains across three diverse real-world datasets.** Table 3 confirms consistent improvements (+1.45%, +1.05%, +0.54% over MV); t-statistics (12.53, 23.39, 3.22) are reported in the paper (line 303).
- **Unsupervised accuracy estimation enabling label-free deployment.** OW-L and OW-I bridge theory to practice without labeled data (lines 265–275).
- **OW-L/OW-I divergence on 16-ensemble evaluation.** Section 5.4 confirms different win rates (66.67% vs 72.92%), establishing the methods are not globally equivalent and that regime-specific convergence is the cause of the Table 3/4 coincidence.

---

## Weaknesses

### Fatal
None.

### Major
- **No aggregation baselines other than majority voting.** The paper compares only against MV. The structural argument (black-box GPT-4o, no labels) is partially valid but not explicitly stated in the paper, and open-weight models in the ensemble could support confidence-weighted comparisons. The authors acknowledge this weakness but resolve it only via revision promise.

### Minor
- **OW-L and OW-I produce identical predictions on the four-model strong ensemble.** The Section 5.4 evidence (divergent win rates across 16 ensembles: 66.67% vs 72.92%) makes the overall identity less alarming, but the regime-specific convergence explanation is not stated in the paper. Downgraded from major.
- **Formal gap between expected-advantage improvement and accuracy improvement.** Theorem 2 establishes expected-advantage ordering; accuracy ordering is validated numerically but not formally bridged. The informal argument offered in the rebuttal is sound but not in the paper.
- **Appendix C extension not summarized in main paper.** The pointer exists (line 63) but no qualitative summary of the correlation-robustness results appears in the main text.
- **Simulation validates model assumptions rather than robustness.** Real-world experiments serve as proxies for robustness, but a targeted simulation under correlated errors would be more diagnostic.

### Trivial
- **Bradley-Terry justification overstated.** Corollary 1 justifies the weighting scheme in this aggregation setting, not the BT model in RLHF generally. Confirmed by the paper at line 92; author will correct.

---

## Nice-to-Haves
- A sensitivity analysis on dataset size $M$ needed for reliable second-order estimation (Theorem 3 gives $O(1/\sqrt{M})$ but the constant is uncharacterized).
- An explicit paragraph in Section 5.4 explaining why OW-L and OW-I converge in the high-accuracy regime, pointing to divergent win rates as evidence of distinctness.
- Brief characterization of Appendix C results (which theorems survive under correlation and how severely).

---

## Novel Insights

The most conceptually original contribution is the formal inversion of the SP logic in the LLM setting. SP corrects for crowds' systematic underestimation of the probability that the correct answer will be widely chosen — a bias that is small for high-accuracy LLMs relative to the raw aggregation signal, causing SP to overcorrect and underperform MV. ISP amplifies the counterfactual: it replaces each conditioning event with the complementary event, increasing the expected advantage of the correct answer. Theorem 2 makes this precise with closed-form gap expressions showing ISP's advantage over MV decays as $\Theta(1/K)$ while MV dominates SP by $\Theta(1)$.

---

## Suggestions

1. **Add the regime-specific convergence explanation in Section 5.4.** State explicitly that OW-L and OW-I converge to similar weights under the high-accuracy strong-model ensemble, while diverging on weaker configurations — cite the 66.67%/72.92% win-rate data already in the paper.
2. **Add at least one confidence-weighted or calibration-set baseline** on open-weight models (Qwen, Llama, Phi) to isolate principled unsupervised gains.
3. **Summarize Appendix C in the main text.** State which theorems survive mild correlation and how the advantage gap degrades.
4. **Add a formal or semi-formal bridge** from expected-advantage to accuracy ordering (e.g., variance-bounded argument under the symmetric model).

---

## Score and Decision

The rebuttal is honest and, critically, points to real in-paper evidence (Section 5.4's 66.67% vs 72.92% win rates) that partially resolves the most alarming concern — the bit-identical OW-L/OW-I outputs. This downgrade from major to minor is justified by the paper itself. The baseline weakness remains unaddressed (acknowledged with revision promise only). The other minor concerns are honest acknowledgments, not refutations.

Net effect: one major weakness is downgraded to minor, one major weakness remains, minor weaknesses are unchanged. The theoretical machinery is solid and uncontested, empirical gains are statistically significant, and the conceptual insight (ISP as inversion of SP logic) is original. Score should stay at **6.5** — the rebuttal neither substantially strengthens nor weakens the paper, and the partial resolution of the OW-L/OW-I concern is balanced by the confirmed BT overstatement and unresolved baselines gap.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>