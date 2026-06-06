## Summary

This paper demonstrates that the L0 hyperparameter in Sparse Autoencoders (SAEs) has a data-determined correct value: too low an L0 causes MSE loss to actively incentivize feature mixing (verified: Section 3.3 shows trained SAE MSE 2.73 vs. ground-truth SAE MSE 4.88 at L0=5), and too high an L0 also produces degenerate solutions. Standard sparsity-reconstruction tradeoff plots are shown to be actively misleading. The paper introduces decoder pairwise cosine similarity (c_dec) as a diagnostic metric, validated in toy models and correlated with sparse probing performance in two LLMs.

---

## Rebuttal Assessment

### Weakness 1: c_dec elbow prescription is underspecified for LLMs
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors reframe the diagnostic target as detecting the low-L0 jump (not finding a precise global minimum). Paper evidence supports this: Section 4.1 states "using the 'elbow' of the plots just before c_dec jumps due to low L0 seems to roughly correspond to peak k-sparse probing performance," and Section 6 frames c_dec as "a useful guide to avoid L0 that are clearly too low." The figure descriptions for Gemma-2-2b layer 5 confirm the curve drops sharply by L0=250 and then remains flat — the elbow is real. The reframing is legitimate and partially undercuts the original criticism. However, no formal or heuristic elbow-detection procedure exists in the paper; this gap is real and the authors acknowledge it as future work. The original review slightly over-penalized this.
- **Score impact:** Weakness downgraded (from major to minor-major borderline)

### Weakness 2: "Most commonly used SAEs have too-low L0" headline claim is bolder than evidence
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors correctly identify two convergent lines of evidence: a Neuronpedia community survey (Appendix A.13, inaccessible to verify but cited in Section 6 of the main paper which I verified: "a cursory search of open source SAEs on Neuronpedia shows L0 less than 100 is very common") and empirical results consistently showing optimal L0 near 200–300 across all three tested layer/model combinations. The directional claim is plausible given these two independent data sources. However, the authors promise to soften the framing in revision — that is a future commitment, not existing evidence. The headline claim in the abstract and Section 6 remains unqualified in the current paper.
- **Score impact:** Weakness unchanged (the promise to revise is not paper evidence)

### Weakness 3: High-L0 degradation lacks parallel mechanistic account
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a resolution — The authors honestly acknowledge the asymmetry. Section 4.2 provides only the decoder projection histogram analysis with "we suspect" language. No MSE-incentive argument parallel to Section 3.3 is provided. Honest acknowledgment does not remove the weakness.
- **Score impact:** Weakness unchanged

### Weakness 4: Width-L0 interaction entirely absent
- **Author's response:** Acknowledge
- **Assessment:** Honest acknowledgment only. No new evidence or analysis is provided.
- **Score impact:** Weakness unchanged

### Weakness 5: Absolute cosine similarity in c_dec (trivial concern)
- **Author's response:** Refute
- **Assessment:** Convincing — The paper's Section 3.5 explicitly justifies the absolute value: "This should mean that the absolute value of the cosine similarity between arbitrary latents should also increase the worse this mixing becomes." The rationale is sound: both positive and negative correlations produce mixing with increased pairwise similarity in absolute terms, and the metric correctly treats both as equivalently corrupting. This is directly in the paper, not just claimed in the rebuttal.
- **Score impact:** Weakness removed

---

## Strengths

1. **MSE actively incentivizes incorrect SAE solutions at low L0 — quantitatively demonstrated.** Section 3.3: trained SAE MSE 2.73 vs. ground-truth SAE MSE 4.88 at L0=5. This is sharp and actionable.
2. **Toy model results are clean and decisive.** Sections 3.1–3.2 with controlled ground-truth orthogonal features. Figures 2–3 show exact positive/negative correlation mixing patterns.
3. **Sparsity-reconstruction plots are shown to be misleading.** Figure 4 shows ground-truth SAE is dominated by the trained SAE below the true L0 — a direct methodological indictment.
4. **c_dec is simple, easy to compute, and validated across two LLMs and two architectures.** Figure 8 (Gemma-2-2b, Llama-3.2-1b BatchTopK) and Figure 9 (Gemma-2-2b layer 12, JumpReLU vs BatchTopK) all show the elbow at L0~200–250 coinciding with peak sparse probing F1.
5. **JumpReLU "sticking" near correct L0 is a novel and practically useful finding.** Section 3.6 and Figure 7 show L0 sticks near 11 across a wide range of λ_s values.

---

## Weaknesses

### Fatal
None.

### Major
- **High-L0 degradation mechanism lacks parallel quantitative account.** Low-L0 failure is mechanistically explained via the MSE incentive argument (Section 3.3). High-L0 failure is described with "we suspect" language in Section 4.2 and the formal theory is deferred to Appendix A.10. The asymmetry undermines the paper's symmetrical framing.

### Minor
- **c_dec elbow prescription lacks formal operationalization.** Even the reframed goal (detecting the low-L0 jump) requires identifying "the elbow just before the jump," which the paper does not define algorithmically. Section 6 acknowledges c_dec "can sometimes remain nearly flat for a wide range of L0" without explaining when or why this happens. Practitioners in new settings have no heuristic to rely on.
- **Headline claim ("most commonly used SAEs have too-low L0") remains unqualified in the current paper.** The evidence base is two models, three layer-model combinations, and a community survey. The revision promise does not address this in the existing text.
- **Width-L0 interaction is absent.** No characterization of how optimal L0 scales with SAE width, a practically relevant question.

### Trivial
None remaining after the rebuttal.

---

## Nice-to-Haves
- A simple elbow-detection heuristic (e.g., largest slope change in the c_dec curve at low L0) with reported success rate across the tested layers would make c_dec actionable for practitioners without a ground-truth baseline.
- A brief sweep over firing probability and correlation strength in the toy model to characterize what data properties determine the true L0 would help practitioners estimate appropriate L0 ranges.
- Softening the headline claim (promised but not yet executed in the current paper).

---

## Novel Insights

The paper's sharpest contribution is converting an empirical observation (low-L0 SAEs mix features) into a structural indictment of the standard evaluation criterion: MSE actively rewards feature mixing when L0 is below the true value, making sparsity-reconstruction plots misleading. This is established rigorously with a counterexample in which the ground-truth correct SAE is outperformed on MSE by a feature-mixing SAE. A secondary contribution is the inhomogeneous firing-threshold landscape in BatchTopK SAEs at intermediate L0 values (Section 4.2, Figure 9 right), where a bimodal decoder projection distribution suggests simultaneously over- and under-triggered latents — a mechanistically interesting finding that partly explains JumpReLU's empirical advantage at high L0 values.

---

## Suggestions
1. Formalize or at least heuristically specify the elbow-detection procedure for c_dec, and report its reliability across all tested layers.
2. Develop a parallel MSE-incentive argument for the high-L0 failure mode to match the analytical depth of Section 3.3 for the low-L0 case.
3. Soften the abstract/Section 6 headline claim to reflect the two-model, three-layer evidence base combined with the Neuronpedia survey.
4. Briefly explore how optimal L0 varies with firing probability and correlation strength in the toy model.

---

## Score and Decision

The rebuttal is honest and partially effective. The c_dec prescription for practitioners is more reasonable than the original review indicated — the low-L0 jump is a consistent, identifiable signal across all LLM experiments, and the paper's own Section 6 appropriately hedges its scope. This downgrade of one major weakness to minor is warranted by paper evidence. However:

- The headline claim weakness is unresolved in the current paper (revision promises do not count).
- The high-L0 mechanistic gap is acknowledged but not addressed.
- The width-L0 interaction is acknowledged but not addressed.
- The trivial c_dec sign concern is convincingly refuted.

Net effect: one major weakness downgraded to minor, one trivial weakness removed. The original score of 6.5 is approximately correct; a very modest upward adjustment to 6.5 is appropriate (unchanged), as the rebuttal revealed the review was slightly too harsh on the c_dec operationalization concern but did not resolve the other weaknesses. The paper remains an above-average contribution with clear practical value and strong toy-model analysis, limited primarily by the narrowness of LLM validation and the underspecified elbow heuristic.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>