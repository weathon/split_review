Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes a causal mediation framework to quantify LLMs' comprehension of deep (semantic) vs. surface (format) structure. It defines deep structure comprehension as a direct causal effect (DCE) and surface structure comprehension as an indirect causal effect (ICE), then develops estimable surrogates — ADCE and AICE — that are task-agnostic and applicable across diverse models. The paper evaluates 12 LLMs across 5 benchmarks, revealing that most models exhibit positive ADCE (indicating genuine deep structure reliance), that closed-source models lean more on deep structure while open-source models shift from surface to deep at larger scales, and that ADCE can detect spurious correlation effects that accuracy misses.

## Strengths

1. **Principled causal formalization of deep/surface comprehension.** The paper frames LLMs' comprehension abilities as causal estimands via a mediation graph (Fig. 2), addressing a key gap where prior work either measured only surface sensitivity or used ad-hoc interventions. The move from unobservable DCE/ICE to computable ADCE/AICE is conceptually clean.

2. **Comprehensive evaluation across models and tasks.** The experiments cover 12 LLMs from 4 families (Llama, Mistral, GPT, Claude) on 5 diverse benchmarks (math, logic, commonsense). The consistent positive ADCE across most models (contrasted with a random-weight baseline at zero, Fig. 3) provides tangible evidence that LLMs genuinely rely on deep structure, challenging the narrative that they are "merely surface structure learners."

3. **Theoretical connection to PS/PN.** Theorem 1 showing ADCE as a weighted combination of Probability of Sufficiency and Probability of Necessity gives the metric a rigorous grounding in causal inference and explains why ADCE can detect issues (e.g., spurious correlations) that accuracy misses — empirically demonstrated in the CivilComments case study (Fig. 6).

4. **Deep vs. surface comparison reveals interpretable trends.** The ADCE/AICE comparison (Fig. 5) uncovers a meaningful pattern: closed-source models rely more on deep structure, while open-source models become less surface-sensitive with scale. This is a genuinely novel empirical finding, even if limited to the tested models.

## Weaknesses

### Major

- **The AICE approximation (ICE ≈ AICE) lacks formal justification or empirical validation.** The paper's central identification strategy replaces the unobservable ICE — which requires the surface structure at its value under T=1 while treatment is T=0 — with AICE (T=0, s(T=0)). The authors assert that careful intervention design makes the surface structures in TE and AICE "highly similar" (lines 185–190), but provide no formal argument, synthetic-data validation, or sensitivity analysis to support this claim. Since the entire ADCE calculation depends on this approximation holding, its plausibility needs more than intuitive reasoning. The paper would be significantly stronger with a controlled experiment (e.g., on synthetic data where the true DCE/ICE are known) showing that AICE numerically tracks ICE, or at minimum a discussion of the conditions under which the approximation could break and how to detect such failures.

### Minor

- **The SFT experiment (Section 4.3) does not control for accuracy improvements.** Figure 4 shows ADCE increasing after fine-tuning Llama-3-8b on Analytic Entailment. But ADCE and accuracy are strongly correlated (Fig. 3, R² > 0.7). If SFT improves accuracy, ADCE might rise simply due to this correlation rather than indicating that "activated task knowledge" causally enables deep structure comprehension. The paper should present accuracy alongside ADCE in this experiment, or examine whether SFT shifts the ADCE–accuracy residual.

- **The closed-source vs. open-source comparison is based on only 4 closed-source models (2 GPT variants + 2 Claude variants).** The paper's claim that "closed-source models primarily rely on deep structure, while open-source models are more surface-sensitive" (line 278) is stated as a general finding but rests on a small, unpaired sample. The closed-source models are all large and proprietary; the open-source family spans a much wider size range. The observed difference could partly reflect model scale rather than an open/closed distinction. The paper should either explicitly limit the claim to the specific models tested (it largely does in the conclusion but the main-text phrasing is broader) or add a size-controlled comparison (e.g., Llama-3-70b vs. a comparable closed-source model if available).

- **The monotonicity assumption in Theorem 1 is not empirically checked.** The theorem assumes $\hat{Y}$ is monotonic with respect to $T$ (line 222), meaning that changing deep structure never causes some samples to flip from correct to incorrect and others from incorrect to correct. This is a strong assumption in the LLM context — a deep-structure intervention could plausibly improve some outputs while harming others. The paper neither verifies this assumption nor discusses how violations would affect the PS/PN interpretation. A simple diagnostic (e.g., inspecting whether any initially incorrect samples become correct under T=1) would address this.

- **The spurious correlation experiment (Section 4.5) is a case study on one dataset (CivilComments) and one model family (Llama-3).** While the paper transparently frames it as a case study, the claim that ADCE "provides a better measure of the model's reliance on deep structure" under spuriousness would be strengthened by testing on additional datasets with controlled spuriousness levels and comparing against alternative robustness metrics.

### Trivial

- None that survive filtering. (Reported formatting/cross-reference issues are parser artifacts, not paper problems.)

## Nice-to-Haves

- A dedicated "Assumptions and Limitations" section transparently discussing the ICE≈AICE approximation, the monotonicity assumption, and scope of the closed-source findings.
- Reporting accuracy alongside ADCE in the SFT experiment, and examining the ADCE–accuracy residual.
- A synthetic-data validation of the AICE approximation, where deep and surface components are known by construction.

## Removed Points

These points from the reviewers were deemed invalid, misinformed, or removed per filtering rules:

- "Figure numbering and cross-references are occasionally inconsistent" — Formatting artifact from PDF parsing; not present in original submission.
- "Missing appendix" / "Algorithm 1 stripped" — The appendix was removed by the PDF parser; it exists in the original submission.
- "ADCE assumes additivity and no interaction" — Standard causal mediation decomposition is an algebraic identity (TE = E[Y(1,s(1))−Y(0,s(0))] = E[Y(1,s(1))−Y(0,s(1))] + E[Y(0,s(1))−Y(0,s(0))]) and does not require an additivity assumption. The paper also states that sequential ignorability (the standard identifying assumption for mediation analysis) holds (line 141, deferred to appendix). The approximation concern is about s(T=1) vs. s(T=0), which is already covered in the Major weakness above.
- "Deep vs. surface structure is operationalized differently across tasks without a principled framework" — The paper uses different strategies (Mask vs. Rephrase) by design, because different tasks have different types of core semantics. The examples in Tables 1–2 provide clear operational definitions for each task. Cross-task comparisons are partial and the paper focuses on patterns within tasks.
- "Random-weight baseline output is random tokens, indicator comparison meaningless" — The paper acknowledges this: the random baseline achieves zero ADCE and zero accuracy (footnote, line 256). It serves as a sanity check that the metric does not produce false positives, which is a valid use.

## Novel Insights

None beyond the paper's own contributions. The reviews raise useful validation concerns but do not contribute fundamentally new interpretations not already present in the paper.

## Suggestions

1. **Validate the ICE≈AICE approximation** in a synthetic or controlled setting where ground-truth causal effects are known. If full validation is infeasible, add a sensitivity analysis showing how much ADCE would change under plausible deviations from the approximation.
2. **Control for accuracy in the SFT experiment** by reporting pre/post accuracy and examining whether the ADCE increase exceeds what the accuracy–ADCE correlation predicts.
3. **Add a dedicated assumptions discussion** (e.g., monotonicity, approximation validity, scope of model comparisons) so readers can assess the metric's limitations without hunting through the paper.
4. **Check the monotonicity assumption** empirically for the models and tasks studied, and discuss how violations affect the interpretation of ADCE as a PS/PN combination.

## Score and Decision

This paper tackles an important, timely question and offers a genuinely novel methodological contribution — a causal metric for deep-structure comprehension that is task-agnostic and model-agnostic. The empirical scope (12 models, 5 tasks) is substantial, and the theoretical framing (PS/PN connection, spurious correlation detection) goes beyond a simple correlation analysis. The primary weakness — insufficient validation of the core approximation that makes the metric computable — is real and non-trivial, but it is a gap that can be closed with additional analysis (synthetic validation or sensitivity checks) rather than a structural flaw that invalidates the approach. The paper's empirical findings are coherent and its conceptual contribution is solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>