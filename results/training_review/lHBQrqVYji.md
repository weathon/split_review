Now I have all the information I need to produce the final consolidated review. Let me carefully synthesize.

---

## Summary

The paper addresses post-deployment deterioration (PDD) monitoring of ML models when test-distribution labels are unavailable. It formalizes a disagreement-based notion (D-PDD), proposes a two-stage algorithm (D-PDDM) that pre-trains a hypothesis subset and threshold distribution off-line and then monitors disagreement on deployment data without accessing training data, and provides finite-sample theoretical guarantees alongside experiments on synthetic, CIFAR10.1, and the GEMINI healthcare dataset.

## Strengths

- **Novel two-stage protocol that eliminates the need for training data during monitoring.** The decoupling of pre-training (compressing information into $\mathcal{H}_p$ and $\Phi$) from deployment (using only $f$, $\mathcal{H}_p$, and $\Phi$) cleanly satisfies the paper's three desiderata — unsupervised, training-data-free, and provably robust. This is a genuine algorithmic innovation over prior disagreement-based methods (Chuang et al., Jiang et al., Ginsberg et al.) that require training data at test time.

- **Principled theoretical analysis that characterizes both success and failure regimes.** The paper does not claim universal guarantees: it proves FPR control under non-deteriorating shifts (Theorem 4.2 / Corollary 4.3), TPR under deteriorating shifts in Regime 1 (Theorem 4.4), and — refreshingly — an honest characterization of Regime 2 where the algorithm fails (Theorem 4.5) together with a geometric illustration (Fig. 3) and practical guidance on improving the base classifier. This transparency is a strength, not a weakness.

- **Proposition 4.1 linking $\xi$ (degree of D-PDD) to TV distance and approximation error $\eta$.** This provides a principled explanation for when non-deteriorating shifts occur (large $\eta$ for simple function classes) and when detection is easier (small $\eta$), offering useful insight into the model-expressivity trade-off.

- **Validation on a large-scale real-world healthcare dataset (GEMINI).** The inclusion of both a temporal (non-deteriorating) split and a controlled age-based subpopulation (deteriorating) shift demonstrates practical relevance beyond synthetic benchmarks. D-PDDM's low FPR on the temporal split and competitive TPR on the age shift are credible evidence of its practical utility.

## Weaknesses

### Fatal

None.

### Major

1. **The algorithm only monitors a sufficient condition of a (probabilistically) equivalent re-definition of the target concept.** The chain is: D-PDDM detects $\epsilon_q > \epsilon_p$ (a sufficient condition for $\xi > 0$), and $\xi > 0$ is D-PDD, which is equivalent to true PDD only under assumptions (g=g', TV≤κ) and *in probability* (Lemma 2.1). So the test tracks a sufficient condition of a proxy that is itself probabilistically equivalent to the real quantity of interest under restrictive assumptions. The paper is transparent about each link (lines 101, 137, and Section 4.3.1), but this layered conditioning means the gap between what is guaranteed and what a practitioner cares about (actual performance degradation) is wider than the title "Provable Post-Deployment Deterioration Monitoring" suggests. This is a structural limitation of the approach, not a fixable presentation issue.

2. **The experimental comparison is against methods designed for a different task.** The baselines (MMD-D, H-divergence, $f$-divergences, BBSD, RMD) are distribution-shift detectors, not deterioration monitors. D-PDDM was explicitly designed to ignore benign shifts while shift detectors are designed to flag *any* shift. Consequently, the paper's main empirical advantage — low FPR on non-deteriorating shifts — is largely a consequence of this task mismatch and does not constitute a fair comparison on the deterioration-monitoring task. The paper partially acknowledges this (line 243: "it stands to reason that these methods pick up on the slightest changes") but does not include baselines designed for unsupervised performance monitoring, such as confidence- or entropy-based heuristics. The CIFAR10.1 and GEMINI-age results show D-PDDM is *competitive*, not dominant; given the baseline mismatch this is weaker evidence than claimed.

### Minor

1. **The theoretical guarantees use $\mathcal{O}(\cdot)$ notation *inside* bound expressions**, which is imprecise for finite-sample claims. Theorem 4.2 states the FPR is at most $\bar{\gamma}+(1-\gamma)\mathcal{O}(\exp(-n\bar{\epsilon}_0^2+d))$ and Theorem 4.4 states TPR is at least $(1-\beta)[1-\mathcal{O}(\exp(-n\epsilon_0^2+d))]$. These "$\mathcal{O}$ inside a bound" formulations obscure constant factors and make the guarantees hard to interpret quantitatively. Standard practice in learning theory is to state explicit constants or at minimum use $\mathcal{O}$ only for sample-complexity scaling conditions, not inside probability bounds themselves.

2. **Several implementation details needed for reproducibility are missing or vague.** The pre-training step (Algorithm 1) says "for multiple rounds" without specifying the number of rounds or the resample size $m$ per round. The posterior approximation used to sample from $\mathcal{H}_p$ is mentioned via a Bayesian perspective (line 90 and "Appendix 1") but the main text does not specify the mechanism (e.g., SWAG, MC dropout, last-layer Laplace). The neural architecture is described as "several layers of ≈32 hidden nodes" which is not precise. The number of posterior samples drawn during monitoring is not reported.

3. **Table 2 (CIFAR10.1 TPR) reports point estimates without standard deviations or confidence intervals.** The paper says "100 realizations" are used for D-PDDM but does not report variability. Since the baselines involve 500 permutation tests, the comparison is difficult to interpret without error bars.

4. **Lemma 2.1's probability expression is stated without derivation or justification.** The bound $1-2\epsilon_f-\kappa$ appears without dependence on any sample size, which is unusual for a probabilistic statement in learning theory. The lemma is central to motivating D-PDD as a proxy for PDD, but its meaning (what is the probability space? what does "equivalent" mean formally?) is left unclear to the reader without the proof. While the proof likely exists in the appendix (stripped by the parser), the statement in the main text is under-specified on its own.

5. **The claim that the GEMINI temporal split is "non-deteriorating" is supported only by visual inspection of a bar plot** (Fig. 5a: "little to no apparent trend in performance degradation"). A quantitative test (e.g., checking whether the error trend is statistically significant) would strengthen this characterization.

### Trivial

- Line 252: "deteorating" typo in the GEMINI age shift caption; "chagnes" → "changes"; "mixutres" → "mixtures".
- Line 252: "attents" → "attends".

## Nice-to-Haves

- An ablation varying the base classifier's in-distribution error $\epsilon_f$ on a controlled synthetic setup to empirically validate the claim that better training moves the system from Regime 2 into Regime 1 (currently supported only by the 2D illustration in Fig. 3).
- A comparison against a simple confidence- or entropy-based heuristic for unsupervised performance monitoring would strengthen the empirical story.
- Reporting empirical calibration: for non-deteriorating shifts, does the FPR of D-PDDM equal $\alpha$ as intended, or is it conservative?

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Lemma 2.1 is ill-posed because the assumptions leave no randomness, so 'with probability' is undefined."** This is factually incorrect: the data are random draws from $P_x$ and $Q_x$, so there is a well-defined probability space. The probability statement may be over the draw of data, not over the conditioning event. Removed as misunderstanding the paper.
- **"The proof of Lemma 2.1 is not given."** Removed per instructions: appendix proofs are stripped by the parser and exist in the original submission.
- **"The theorems say 'if the algorithm's test statistic moves in the right direction, then the test works' — circular."** This misunderstands the standard form of a hypothesis-testing guarantee: the theorems condition on the *population* parameters ($\epsilon_p > \epsilon_q$ or $\epsilon_q > \epsilon_p$) and provide sample complexity bounds for the empirical test to succeed — this is exactly how consistency results work, not circular reasoning.
- **"Missing appendix content" / "proofs not in appendix."** Removed per instructions.
- **Formatting nitpicks** about garbled characters, broken math rendering in the PDF extraction (e.g., "$\bar{\gamma}$", "$\bar{1}$", "$\dot{d}$" in Theorem 4.2). These are PDF-parser artifacts, not author errors.
- **Criticism that D-PDDM is compared to shift detectors rather than deterioration monitors is called "misaligned" without acknowledging the paper explicitly discusses this.** While the criticism is retained as Major Weakness #2, the critic's framing that the paper "does not include such comparisons" is partially addressed by the paper correctly noting that Podkopaev & Ramdas (2021) requires labels, which is outside the paper's unsupervised scope.

## Novel Insights

The harsh critic's meta-point — that the paper's guarantees cover a "sufficient condition of a sufficient condition" — is a genuine structural observation that goes beyond what the paper itself spells out in one place. The paper acknowledges each link separately (D-PDDM → sufficient condition for D-PDD, D-PDD ↔ PDD in probability), but does not explicitly enumerate the full chain: **the test monitors a sufficient condition ($\epsilon_q > \epsilon_p$) of D-PDD ($\xi > 0$), which is itself probabilistically equivalent to PDD under restrictive assumptions (g=g', TV≤κ).** This layered conditioning is the central limitation of the approach and should be stated upfront rather than distributed across Sections 2 and 4. The reviewer's other substantive insight — that the baseline comparison largely constructs the paper's advantage — is also valid, though partially acknowledged by the paper itself.

## Suggestions

1. **Restructure the theoretical presentation** to state the full monitoring chain explicitly in one place early on: what is monitored, what it is a sufficient condition for, and under what assumptions it connects to actual performance deterioration. This would preempt confusion and honestly scope the claims.

2. **Replace $\mathcal{O}(\cdot)$ inside bound expressions with explicit constants** (or at minimum state "there exists a universal constant $C$ such that..."). This is standard for learning-theoretic guarantees and would significantly strengthen the paper's theoretical contribution.

3. **Add at least one baseline designed for the same task** — e.g., a threshold on prediction confidence/entropy on $Q_x$, or a simplified disagreement method that requires training data (to quantify the cost of removing that requirement). Even a simple baseline would substantially improve the experimental contribution.

4. **Report standard errors/confidence intervals for all main results** (Table 2, Figs. 4-6). The 100-realization protocol supports this.

5. **Provide a reproducible algorithm specification** in the main text or appendix: number of pre-training rounds, resample size $m$ per round, posterior sampling mechanism and sample count, and explicit architecture details.

## Score and Decision

**Originality:** 6/10 — The two-stage decoupling and the application of disagreement monitoring to the no-training-data setting are novel, but the individual components (disagreement framework, VC-dimension bounds, permutation testing) are established.

**Importance of research question:** 8/10 — Unsupervised deterioration monitoring without training data during deployment is a timely and practically critical problem, especially for high-stakes domains like healthcare.

**Claims supported:** 4/10 — The theory uses imprecise $\mathcal{O}$-notation in bounds, the Lemma 2.1 statement is under-specified, and the experimental advantage over baselines is largely a consequence of task mismatch. The paper's claims outpace what is convincingly demonstrated.

**Soundness of experiments:** 5/10 — Good use of real healthcare data and multiple shift types, but undermined by the lack of appropriate baselines and missing error bars.

**Clarity of writing:** 6/10 — Generally readable, but the theoretical section is dense and the bound statements are marred by PDF-parser artifacts in the extracted text (these are parser, not author, issues).

**Value to research community:** 6/10 — The problem framing, desiderata, and two-stage design are valuable conceptual contributions that could influence how practitioners think about monitoring, but the technical execution needs strengthening.

**Overall:** The paper tackles a well-motivated and important problem with a clever algorithmic design. However, the theoretical guarantees are presented with imprecise $\mathcal{O}$-notation inside bounds, the core Lemma 2.1 is stated without sufficient clarity in the main text, and the experimental evaluation relies on baselines designed for a different task (shift detection rather than deterioration monitoring), which inflates the apparent advantage. The paper is transparent about its limitations (Regime 2, sufficient-condition structure), which is commendable, but the gap between the claims in the title and what is actually proven + demonstrated is too wide. Major revisions — tightening the theory, adding appropriate baselines, and scoping claims more carefully — would be needed to make this a strong paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>