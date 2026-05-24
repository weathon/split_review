Now I have enough calibration data. Let me write the consolidated review.

## Summary

This paper formalizes experimental studies in machine learning using rankings, defines a quantifiable notion of generalizability based on the Maximum Mean Discrepancy between distributions of rankings, and proposes a sample-size estimation algorithm. Two case studies (categorical encoders and BIG-bench) demonstrate the framework. The core contribution is a principled formalization of experimental studies (Section 3) and a definition of generalizability (Definition 4.1) that operationalizes the informal definitions from the literature.

## Strengths

1. **First principled formalization of experimental studies in ML (Section 3).** The paper provides rigorous, self-contained definitions of experiments, experimental conditions (with the design/held-constant/allowed-to-vary factor taxonomy), ideal vs. empirical studies, and study results as distributions over rankings. This fills a clear gap — prior work discussed generalizability informally but had no mathematical foundation to build on.

2. **Quantifiable generalizability definition (Definition 4.1).** The definition captures the probability that two empirical studies of size \(n\) from the same ideal distribution yield similar results, measured via MMD. This makes generalizability directly testable, unlike prior informal definitions (Pineau et al., 2021; National Academies of Science, 2019).

3. **Goal-specific similarity via kernels (Section 4.1).** Three kernels (Borda, Jaccard, Mallows) encode different research goals (best alternative, top-\(k\) set, full ordering) into the similarity measure. This is a significant advance over a one-size-fits-all distance and is essential for the framework's applicability.

4. **Actionable insights from case studies (Section 5).** The framework identifies non-generalizable design-factor combinations — e.g., the SVM + full tuning + balanced accuracy combination requires 34 datasets but only 30 were used (Section 5.1) — and detects cases where even a single experiment suffices (Section 5.2). These demonstrate the framework can produce concrete, interpretable recommendations.

5. **Analysis of preliminary experiment sensitivity (Section 5.3, Figure 4).** The paper analyzes how the number of preliminary experiments \(N\) affects the accuracy of the \(n^*\) estimate, showing that 20–30 preliminary experiments suffice for stable estimates with the Borda kernel. This gives practical guidance to future users.

## Weaknesses

### Fatal
None.

### Major

1. **The algorithm for estimating \(n^*\) is heuristic and its validation is partly circular.** Proposition 4.2 asserts a linear relationship between \(\log(n)\) and \(\log(\varepsilon_n^{\alpha^*})\) based on a proof in the appendix (stripped — cannot be verified). The algorithm in Section 4.3 uses this log-log linearity as a general extrapolation tool. The validation in Section 5.3 treats \(n_{50}^*\) (the algorithm's own estimate at \(N=50\)) as ground truth, which is methodologically circular — it only checks that the estimate is stable with more data, not that it converges to the correct value. The paper promises synthetic-data validation in Appendix C.1, but the content of that appendix is absent. **Why this matters:** The paper's core practical claim — that it can "estimate the number of experiments needed" — rests on this algorithm. Without proper calibration or convergence guarantees against known ground truth, the reliability of the \(n^*\) values reported in the case studies is unclear.

2. **The framework assumes a known probability measure \(\mu\) over experimental conditions without discussing how practitioners should specify it.** The entire formalization (Definition 3.3, Definition 4.1, the i.i.d. sampling in Section 3.2.2) depends on a probability space \((C, \mathcal{F}, \mu)\). The paper does not discuss how an experimenter should construct \(\mu\) in practice. In the case studies, it is implicitly treated as uniform over the available datasets/subtasks, but this choice is neither justified nor acknowledged as a modeling decision. **Why this matters:** If \(\mu\) is arbitrary, then generalizability is only defined relative to that arbitrary choice. This doesn't invalidate the framework, but without guidance on specifying \(\mu\), the practical applicability for planning new studies is limited. The paper itself acknowledges no limitations about \(\mu\) in Section 6.

### Minor

3. **The definition captures within-distribution replicability, not generalizability to shifted distributions.** Definition 4.1 measures the probability that two studies sampling i.i.d. from the *same* ideal distribution \(\mathbb{P}\) yield similar results. This is replicability under the same population of conditions. The common ML concern — that findings on one set of datasets may not hold on a *different* distribution (e.g., a different domain) — corresponds to transportability, which the paper acknowledges as future work. The framing in the title and introduction could mislead readers into expecting the broader notion. This is a scope-clarity issue, not a technical flaw.

4. **Missing-value imputation by worst rank may inflate apparent stability.** In Section 5.1, missing values are imputed by assigning the worst rank. This can create artificial ties and reduce variance, potentially making results appear more generalizable than they are. A sensitivity analysis (e.g., best-rank imputation or complete-case analysis) is needed to assess the impact.

5. **BIG-bench data filtering could introduce selection bias.** Section 5.2 filters to conditions where ≥80% of LLMs have results and LLMs with ≥80% condition coverage. The number of retained conditions/LLMs is not reported, and the results (e.g., \(n^*=1\) for "arithmetic, 2 shots") may be driven by this selection. The paper should report the filtering statistics and discuss potential bias.

6. **Kernel bandwidth recommendations lack sensitivity analysis.** The recommended bandwidths (\(\nu = 1/n_a\) for Borda, \(\nu = 1/\binom{n_a}{2}\) for Mallows) are stated without justification or sensitivity analysis. Since bandwidth directly affects MMD values and thus the estimated \(n^*\), the paper should show how sensitive results are to this choice.

### Trivial

7. Definition 3.2 (research question) does not include \(\mu\) in the tuple, even though \(\mu\) is essential for sampling (Section 3.1) and appears in Definition 4.1 via \(\mathbb{P} = S(\mathcal{Q})\). This is a minor inconsistency.

## Nice-to-Haves

- Replace the heuristic log-log linear extrapolation with a bootstrap or confidence-bound approach that directly computes the empirical quantile of MMD for increasing \(n\) without assuming a parametric form.
- Compare the framework's \(n^*\) recommendations against simpler heuristics (e.g., "use 10 datasets") to show when the additional complexity buys meaningful differences.
- Explore the framework's behavior with larger numbers of alternatives (\(n_a > 100\)), where the ranking space grows super-exponentially and MMD may become uninformative.

## Removed Points

These points were flagged during consolidation but removed for the reasons given. Treat with caution if referenced elsewhere.

- **Criticism that the Borda kernel is unsuitable because "Borda count is an absolute measure, not a relative one":** This misunderstands the kernel. The Borda kernel compares the Borda count of a specific alternative \(a^*\) across two rankings, which directly measures consistency in how many alternatives \(a^*\) dominates — a perfectly valid way to answer "is \(a^*\) consistently ranked the same?"
- **Criticism that "the algorithm's own rule is violated in the n*=1 example":** The paper explicitly acknowledges this limitation in the same paragraph ("this estimate relies on 10 preliminary experiments. Of course, however, one cannot trust an estimate of \(n^*\) based on only one experiment."). The transparency undermines the criticism.
- **Criticism about missing appendix/proofs:** The parser strips appendices from all papers; they exist in the original submission.
- **Reproducibility criticism about GENEXPY repository:** The paper provides a footnote URL (anonymous.4open.science), which is standard for double-blind submissions.
- **Pure formatting/style nitpicks** (vague abstract phrasing, notational preferences).
- **Strength about the algorithm being a core strength:** Demoted because the algorithm is a contribution but its validation concerns (Weakness 1) override unqualified praise.

## Novel Insights

None beyond the paper's own contributions. The reviews surface real weaknesses (algorithm validation, \(\mu\) specification) but do not identify any novel connection or implication the paper itself missed.

## Suggestions

1. **Validate the algorithm on synthetic data** where the true distribution \(\mathbb{P}\) (and hence the true \(n^*\)) is known. This is essential to establish that the log-log linear extrapolation actually yields correct estimates, breaking the circularity of the current validation.
2. **Add a subsection on how to specify \(\mu\)** in practice. Even a simple rule — "use the empirical distribution over available datasets" — makes the framework directly applicable and clarifies the assumptions.
3. **Conduct sensitivity analysis** for: (a) worst-rank vs. best-rank vs. complete-case imputation; (b) the 80% filtering threshold in BIG-bench; (c) kernel bandwidth choices.
4. **Clarify scope** in the abstract and introduction: the paper measures within-distribution replicability, not transportability to different populations of conditions. This sets accurate reader expectations.
5. **Report filtering statistics** (how many conditions/LLMs retained at each threshold) for the BIG-bench case study.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak anchors (avg ≤3.5): lZRRfupxYn (3.00), FaL6aTuXod (1.50), fvTaoyH96Z (2.33), P2AD80rFNu (3.00) — papers with very weak or flawed contributions.
- Middle anchors (3.5–7.5): lf8QQ2KMgv (3.75), lWN2aGg8qJ (4.00), 8FxELTdwJR (4.67), 8wAL9ywQNB (6.60) — range of papers with mixed strengths/weaknesses.
- Strong anchors (≥7.5): d8w0pmvXbZ (8.00), pISLZG7ktL (8.00), SctfBCLmWo (8.00), EUSkm2sVJ6 (7.60) — strong, well-executed papers with clear contributions.

**Round 1 bracket:** Between 4.0 and 7.0.

**Round 2 (Narrowing):**
- QzR7Jfe8Tz (5.33, sim 0.69), w0es2hinsd (5.25, sim 0.69), PCXvcULwiI (5.50, sim 0.68), PHkUNcno9n (4.67, sim 0.68) — benchmarking/formalization papers, mostly rejected.
- NkmJotfL42 (7.00, sim 0.71), 8wAL9ywQNB (6.60, sim 0.70), MF7ljU8xcf (6.00, sim 0.68), qFZnAC4GHR (6.67, sim 0.68) — generalizability/bound analysis papers, accepted as posters.

**Comparison to anchors:** The paper under review is stronger than the benchmarking/formalization papers (5.0–5.5 range) — its formalization contribution is genuinely novel and well-motivated, whereas those are primarily engineering. It is weaker than the accepted theory papers (6.0–7.0 range) — those have rigorous proofs and validation, while this paper's algorithm is heuristic and not properly validated. The paper falls between these bands: its formalization contribution is solid, but the key practical output (the \(n^*\) algorithm) lacks sufficient support.

**Final placement:** 5.5 — a paper with a genuine formalization contribution that advances the foundations for studying generalizability, but whose practical tool (the algorithm) is not yet adequately validated, and whose key assumptions about \(\mu\) are underspecified for practitioners.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>