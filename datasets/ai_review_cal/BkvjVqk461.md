- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 5, 3, 3, 3
Now I have all the information needed to write the consolidated review.

---

## Summary

This paper proposes a primal-dual algorithm (PLADA) for fair classification under non-convex, non-smooth fairness constraints. It develops a variant of the Proximal-Perturbed Lagrangian (P-Lagrangian, Kim 2021) that yields a reduced Lagrangian with strong concavity in the dual variables, enabling a simple alternating primal-dual update with a closed-form multiplier step. The paper claims a convergence rate of \(\tilde{\mathcal{O}}(1/\sqrt{T})\) and provides experimental results on four fairness datasets comparing against optimization-based baselines.

---

## Strengths

- **Novel Lagrangian derivation with strong concavity (Section 3.1, Eqs. 5–9):** The paper transforms the fairness-constrained problem into an equality-constrained form and derives a reduced P-Lagrangian that is \(1/\rho\)-strongly concave in \(\lambda\) for fixed \(\mu\). This yields a unique closed-form maximizer \(\lambda(\theta,\mu) = \mu + \rho(G(\theta)+u)\) (Eq. 9), enabling a simple alternating update. This is a genuine technical contribution that goes beyond standard Lagrangian relaxations by endowing the dual with favorable structure.

- **Addresses an important, well-motivated problem:** Non-convex non-smooth fairness constraints arise naturally in practice (e.g., with neural network classifiers and sigmoid surrogates), and existing algorithms often lack convergence guarantees. The paper's focus on provable guarantees for this setting is timely and relevant.

- **Theoretical convergence guarantee stated:** The conclusion (Section 6) claims a convergence rate of \(\tilde{\mathcal{O}}(1/\sqrt{T})\) to a stationary solution, which if proven would be a meaningful contribution for this problem class. The Lagrangian framework is flexible enough to handle multiple fairness notions (demographic parity, equalized odds, intersectional groups).

---

## Weaknesses

### Fatal

None.

### Major

- **Missing quantitative experimental results (Section 5):** The experimental section presents only convergence plots (Figures 2–3, which are image references stripped by the parser). No test accuracy, fairness violation (\(\Delta(\theta)\)), or standard deviation across runs is reported in numerical form anywhere in the visible text. The reader cannot assess the magnitude of any improvement over baselines, whether results are statistically meaningful, or reproduce the claimed performance. For an algorithm whose "effectiveness" is a central claim (abstract, Section 1.2), this is a critical omission that makes the empirical contribution unverifiable from the presented content.

- **Unanalyzed gap between surrogate and original fairness guarantees (Sections 1.2, 2.2):** The abstract and contributions claim "provable fairness guarantees" and "strong performance guarantees on the fairness of its solutions." However, the paper solves the surrogate-constrained problem (3), not the original indicator-based problem (1). Section 2.2 says the two are "approximately equivalent" without any formal analysis of the approximation error. The paper does not show how a stationary point of the surrogate problem relates to the original fairness metric \(\Delta(\theta)\) (Definition 1) — e.g., via Lipschitz continuity of the surrogate \(\sigma\) and thresholding. Even accounting for the stripped theory section (Section 4), this bridge is not established in any visible part of the paper. The fairness claims therefore outpace the demonstrated theory.

### Minor

- **Unsubstantiated claim about parameter simplicity (Section 1.2):** The paper asserts a "practical advantage with fixed parameters, except for the step size of the auxiliary multiplier" but provides no ablation study, sensitivity analysis, or empirical support for this claim. The algorithm has parameters \(\alpha\) and \(\beta\) (Section 3.1) plus step sizes; how these were set in experiments and whether performance is robust to their variation is unreported.

- **Missing reproducibility details for experiments (Section 5):** No train/test splits, data preprocessing (normalization), stopping criteria, hyperparameter values (\(\alpha, \beta\), step sizes) for PLADA are reported. The baseline hyperparameter settings are said to follow Huang & Lin (2023) and Narasimhan et al., but PLADA's own settings are absent. This hampers reproducibility.

### Trivial

None.

---

## Nice-to-Haves

- Include a formal bound connecting the surrogate violation to the original indicator-based fairness violation (e.g., using the Lipschitz constant of the sigmoid surrogate and a thresholding argument). This would strengthen the "provable fairness" claim considerably.
- Report quantitative results (accuracy, \(\Delta(\theta)\), run time) in tabular form with means and standard deviations across multiple random seeds, alongside the convergence plots.
- Provide a hyperparameter sensitivity study for \(\alpha\) and \(\beta\) to substantiate the claims of practical parameter simplicity.

---

## Removed Points

These points were flagged by the reviewers but are removed or downgraded with justification:

1. **Missing Algorithm 1, equation (12), Section 4 (convergence analysis):** The paper references these but they do not appear in the extracted text. Per the instructions, the parser strips content from all papers; these existed in the original submission. **Removed** — parser artifact.

2. **Handling of the \(u\) variable never explained:** The critic questioned how \(u\) (slack variable) is updated. The visible text mentions "alternatingly optimizing parameters such as \((u, z, \lambda, \mu)\)" (line 187), suggesting the algorithm pseudocode (stripped) specifies these updates. **Removed** — likely addressed in stripped Algorithm 1.

3. **Figures have no visible axis labels / Figure 1 not visible:** These are image references stripped by the parser. **Removed** — parser artifact.

4. **No comparison to standard fairness-ML baselines (Agarwal et al., 2018 reduction; Cotter et al., 2019b):** The paper compares against optimization-specific baselines (SSG, IPP-ConEx, IPP-SSG, Narasimhan et al.) that are appropriate for non-convex non-smooth constraints. The set of baselines is reasonable for the paper's stated scope. **Removed** — not a fair criticism given scope.

5. **Strength Finder: "Superior empirical performance":** This conflicts with the verified weakness regarding missing quantitative experimental results. The paper cannot claim superior performance without numerical substantiation. **Removed** — conflicts with verified weakness.

6. **Strength Finder: "Practical parameter simplicity":** This is a claim made by the paper, not a verified strength, and conflicts with the weakness about missing ablation/sensitivity analysis. **Removed** — conflicts with verified weakness.

7. **Various formatting/style nitpicks, grammar issues, section numbering quirks:** Parser artifacts, not author errors. **Removed**.

8. **Paper "relies heavily on Kim (2021; 2023) for the P-Lagrangian concept without explaining key ideas":** The paper cites Kim as prior work extending its framework. The self-contained mathematical derivation from Eqs. (5)–(9) explains the key ideas sufficiently for a reader familiar with Lagrangian methods. **Removed** — not a substantive weakness.

---

## Novel Insights

Beyond the paper's own contributions, the reviewers' cross-examination surfaces a tension worth noting: the paper proposes a technically elegant Lagrangian framework (strong concavity in dual variables, closed-form multiplier update) but the empirical evaluation falls short of the standards needed to validate such a framework for practical fairness. The disconnect between the sophisticated optimization machinery and the minimal experimental reporting is the paper's most significant gap. A more careful mapping between the theoretical guarantees (convergence to a KKT point of the surrogate problem) and the practical fairness metric would substantially strengthen the work.

---

## Suggestions

1. Add a quantitative results table with test accuracy, fairness violation (original indicator-based \(\Delta(\theta)\)), and computational time for all methods across multiple random seeds with standard deviations.
2. Provide a formal analysis (or at minimum a clear discussion) of how the surrogate violation bounds the original indicator-based fairness violation — this is needed to justify the "provable fairness" language.
3. Include the full algorithm pseudocode in the main text, specifying update rules for all variables (\(\theta, u, \lambda, \mu\)).
4. Add an ablation or sensitivity study for \(\alpha\) and \(\beta\) to support the claim that these parameters can be fixed across datasets.
5. Report the specific hyperparameter values used for PLADA in the experiments.

---
