Now I'll write the final consolidated review.

---

## Summary

This paper proposes **Certifiably Byzantine-Robust Federated Conformal Prediction**, the first framework to address Byzantine attacks in federated conformal prediction. The method detects malicious clients by computing a "maliciousness score" based on averaged distances between histogram-based characterization vectors of conformity scores, then excludes suspicious clients from quantile estimation. The paper provides theoretical coverage guarantees (Theorem 1) showing asymptotic convergence to the desired coverage level, and a malicious client number estimator with a precision guarantee (Theorem 2). Empirical results across five datasets and three attack types show that the method maintains coverage near the target while standard FCP fails.

---

## Strengths

- **First theoretical coverage guarantees for Byzantine-robust FCP.** Theorem 1 provides both lower and upper bounds on prediction coverage in the Byzantine setting, with the guarantee that as benign sample size grows, coverage converges to the desired level $1-\alpha$. No prior FCP work offers coverage guarantees under Byzantine attacks, making this a genuine theoretical contribution.

- **Malicious client number estimator with a proven precision guarantee.** Section 4 introduces an EM-based estimator for when $K_m$ is unknown, and Theorem 2 provides a lower bound on the probability of exactly recovering the true $K_m$. This goes beyond standard Byzantine robustness literature, which typically assumes prior knowledge of $K_m$.

- **Consistent empirical robustness across five datasets and three attack types.** Table 1 shows that under 40% malicious clients, the method maintains marginal coverage within 0.899–0.928 across all attack types and datasets, while standard FCP degrades severely (e.g., coverage 0.805 on MNIST under CovAttack, or 1.000/10.00 set size under EffAttack). The improvement over the sole baseline is large and consistent.

- **Robustness across varying data heterogeneity levels.** Table 2 demonstrates that the method maintains coverage between 0.887–0.913 across Dirichlet parameter $\beta = 0.1$ to $0.9$ on four datasets, while FCP degrades to as low as 0.780.

---

## Weaknesses

### Fatal
None.

### Major

1. **No statistical uncertainty reported for any experimental result.** Tables 1 and 2 report marginal coverage and set size as single numbers with no standard deviation, confidence interval, or number of random trials. Every element of the experimental pipeline is stochastic: the Dirichlet data partitioning, which clients are designated malicious, the Gaussian noise in GauAttack, and the test set sampling. Without repeated trials, the reader cannot assess whether the results are robust or happened on a favorable draw. The paper's theoretical bounds hold "with probability $1-\beta$" but offers no way to assess empirical variability. This substantially weakens the empirical contribution.

2. **Only one baseline is compared against.** The paper compares only against standard (non-robust) FCP, which is expected to fail in a Byzantine setting. Showing that the method outperforms a broken baseline is necessary but not sufficient. The paper does not compare against adaptations of existing Byzantine-robust aggregation techniques (e.g., applying Krum, coordinate-wise median, or trimmed mean to the histogram vectors). Without such baselines, the reader cannot assess whether the specific distance-to-nearest-neighbor design is critical or whether a simpler robust aggregation would suffice. An ablation removing the detection mechanism (just using FCP on all clients) is also absent.

3. **The core method and primary experiments assume the defender knows $K_b$.** The maliciousness score computation (Eq. 5, line 164) requires $K_b$ as an input: it selects the $K_b$ clients with lowest maliciousness scores. Table 1 uses 40% malicious clients, meaning $K_b$ is known a priori. In a real Byzantine setting, the server does not know how many clients are benign. Section 4 proposes an estimator for the unknown-$K_m$ case, but it is presented as a separate module evaluated only visually (Figure 2) on two datasets without quantitative accuracy metrics (e.g., how often the estimator gets the exact count right). The paper should either make the unknown-$K_m$ version the primary method or clearly delineate which results assume known $K_b$.

### Minor

4. **Coverage bound validation is limited.** Figure 3 validates the theoretical bounds against empirical coverage on only one dataset (Tiny-ImageNet) under one attack type (Gaussian), showing a single curve without error bars. The bounds involve interdependent terms ($n_b$, $H$, $\tau$, $\sigma$) whose practical tightness is hard to assess from one figure. Validation across multiple datasets and attack types would strengthen the claim that the bounds are "tight."

5. **Mimic attack treatment is informal and not directly analyzed.** Section 3.2 argues (with reasonable intuition) that mimic attacks are less effective in the FCP score space than in gradient space for FL optimization. However, this argument is not formally analyzed, and the empirical validation is relegated to the appendix. Given that the paper positions itself as the *first* robust FCP method, the scenario where attackers try to blend in with benign behavior is critical and deserves more thorough treatment in the main paper.

### Trivial
- No limitations section is included. Several limitations are worth explicit discussion: the $K_m < K_b$ assumption, the dependency on knowing $K_b$ (or estimating it), the looseness of finite-sample bounds, and the reliance on benign vectors being separable from malicious ones in histogram space.
- The benign-client results are only in the appendix (Table 1 caption references Appendix Table tab:benign), making the main table incomplete as a standalone reference. Including the benign column in the main table would improve readability.

---

## Nice-to-Haves

- **Practical guidance on choosing $H$** (characterization granularity). Remark R6 notes the tradeoff between $H$ and bound tightness, but concrete recommendations or a sensitivity analysis in the main text would help practitioners.
- **Clarify the deployment scenario for $K_b$-known vs. $K_b$-unknown versions.** The paper should explicitly state which experimental results use each version and provide a decision rule for practitioners.
- **Benign baselines in the main table.** The caption of Table 1 references benign results only in the appendix. Including them directly would make the table self-contained.

---

## Removed Points

- **"No code release details"** — Removed per filtering rules (code release is a reasonable request but not a weakness of the paper's scientific contribution).
- **"The notation \name is never expanded"** — This is a parser artifact; the original submission contains the method name.
- **"PathMNIST results suggest data may be too simple"** — Speculative; the paper does not discuss this, and it is not a verifiable weakness from the presented data.
- **"Missing related works"** — Removed per filtering rules (no external sources to confirm existence of missing citations).
- **"Figure 1 caption does not specify attack type"** — Removed as a minor presentation nitpick.
- **Strength Finder strength "Rigorous validation of theoretical coverage bounds"** — Demoted from listed strength to the Minor weakness section since the validation is limited to one dataset/attack without error bars. The validation is not "rigorous" in the sense the Strength Finder claimed.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear structural tension: the paper's theoretical contribution is genuine (first Byzantine-robust FCP with coverage guarantees), but the empirical evaluation lacks the rigor expected at a top venue. The main insight from integrating the reviews is that this tension is not resolvable by minor revisions — the missing statistical uncertainty and narrow baselines require substantial new experimental work.

---

## Suggestions

1. **Add repeated trial statistics.** Report means and standard deviations over at least 10 independent runs (different data partitions, different malicious client selections) for all main results. This is the single most impactful improvement.
2. **Add Byzantine-robust baselines.** Adapt existing robust aggregation methods (Krum, coordinate-wise median, trimmed mean) to the histogram vector setting and compare against them.
3. **Move the estimator to a more central position.** Either make the unknown-$K_b$ version the primary method, or clearly separate the $K_b$-known results (as a proof-of-concept) from the $K_b$-unknown results (as the practical contribution) with appropriate hedging.
4. **Validate coverage bounds more broadly.** Show theoretical vs. empirical coverage across multiple datasets and attack types, ideally with error bars.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>