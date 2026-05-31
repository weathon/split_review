## Summary

This paper introduces a deletion-based probing framework to assess how much LLMs genuinely depend on their chain-of-thought (CoT) scratchpads when solving physics problems. By intercepting CoT mid-generation and removing varying fractions of tokens (via end, random, and physics-aware strategies), the authors measure downstream effects on accuracy, final answer length, and information overlap. Applied to three open-source models (Phi-4, Qwen-A3B, Magistral) across three physics benchmarks (UG Physics, PhyBench, PhysReason), they document that models remain accurate under 40–60% deletion by "cramming" reconstructed steps into final answers, and that deleted content often reappears inconsistently via surface-level recovery rather than faithful reasoning.

---

## Strengths

- **Timely and important research question.** The faithfulness gap in CoT reasoning is underexplored in AI-for-Science contexts. Physics provides a well-defined structured domain where equations and units make faithfulness partially measurable, and the paper motivates this focus clearly.
- **Concrete, replicable experimental design.** Three deletion strategies × three models × three benchmarks provides reasonable empirical coverage. The deletion framework is technically straightforward and reproducible, and the X-shaped inverse relationship between CoT length and final answer length is a well-illustrated phenomenon.
- **"Cramming" as a named, characterized phenomenon.** Documenting that models compensate for deleted reasoning by producing longer, reconstructed final answers is a useful empirical observation for both practitioners and researchers working on CoT efficiency.
- **Multi-dimensional evaluation.** Pairing accuracy with answer length and information-overlap metrics (Jaccard + Manhattan) is more informative than accuracy alone.

---

## Weaknesses

### Fatal
None.

### Major

1. **LLM-as-judge for physics creates a fundamental confound.** The paper uses Claude-4 Sonnet to judge all answers on a 0–1 scale combining correctness, derivation quality, logic, formatting, and clarity. For physics, many problems have definite numerical or symbolic answers that can be evaluated deterministically. An LLM judge that scores more elaborate text higher may systematically inflate scores for "cramming" responses (which are longer and more elaborate) compared to shorter but equally correct responses. This confound directly undermines the core claim that cramming partially recovers accuracy.

2. **Token-overlap metrics do not control for baseline physics vocabulary.** Jaccard similarity and Manhattan distance over bag-of-words representations will show high overlap whenever both the original CoT and the regenerated answer use standard physics vocabulary (e.g., "F=ma," "energy," "velocity," SI units). The paper does not establish a baseline—e.g., overlap between two independent answers to the same question that never shared a CoT—so it is unclear how much of the measured "recovery" reflects genuine reconstruction versus shared domain vocabulary.

3. **Sample size and statistical power are underspecified.** The calibration section establishes that 50 questions and 5 runs suffice for a 10% relative error on UG Physics. However, the main experiments' sample counts are not clearly stated, and Figure 7's overlap plots show very wide standard error bands across multiple panels, particularly for physics-aware deletion. Given the noisiness, the conclusion that "physics-aware deletion is most noise" may be as much an artifact of insufficient data as it is a robust finding.

4. **The "cramming" mechanism remains uninterpreted.** The paper presents cramming as reconstruction of deleted reasoning, but the observed behavior is equally consistent with the model simply reverting to direct parametric answer generation using problem context alone (i.e., never consulting the truncated CoT at all). The two hypotheses—faithful reconstruction vs. parametric bypass—make observationally similar predictions on accuracy and length. No experiment distinguishes them.

### Minor

- The information overlap is measured between original CoT (before deletion) and the new final answer content, but this baseline grows artificially as more CoT is deleted (the final answer has more room to include physics terms). A length-normalized or per-token overlap rate would be more interpretable.
- There is no comparison to a zero-shot baseline (no CoT at all), which would anchor the lower bound on the accuracy curve and clarify how much of the residual accuracy at 100% deletion is attributable to parametric knowledge.
- Figure numbers are inconsistently referenced: "Figure 6" is described in text but captioned as "From-the-end deletion-sweep visualizations" without a standard figure label in the displayed content.

### Trivial

- Minor inconsistency in model name spelling ("Magistrall" appears with a double-l in one location).

---

## Nice-to-Haves

- Establishing ground-truth accuracy (e.g., exact match for numerical answers) alongside LLM-judged scores would significantly strengthen the claim that cramming partially recovers correctness.
- Measuring overlap with a same-question, no-shared-CoT baseline would disambiguate genuine reconstruction from domain vocabulary overlap.
- A mechanistic ablation—e.g., attention attribution or probing on intermediate layers—would help distinguish cramming-as-reconstruction from cramming-as-fallback to parametric knowledge.

---

## Novel Insights

The most useful novel observation is that accuracy is more robust to end-deletion than to physics-aware deletion at low deletion fractions, but physics-aware deletion then triggers a sharper and later cramming spike. This suggests that models are more sensitive to the *type* of content deleted than to the *position* or *quantity*, and that semantically targeted deletions reveal a qualitatively different compensation mechanism than random or truncation-based ones. This asymmetry is a genuine insight beyond the baseline "CoT can be bypassed" findings of prior work, and points toward content-aware evaluation strategies.

---

## Suggestions

- Replace or supplement LLM-as-judge with deterministic evaluation (e.g., exact match, numeric proximity within tolerance) for at least a subset of benchmark questions, to validate that LLM-judged score trends are not artifacts of evaluator bias toward verbose outputs.
- Report per-benchmark sample counts explicitly in the methods; add a statistical test (e.g., permutation test) for the key claim that physics-aware deletion is more detrimental than non-annotated deletion.
- Include a simple experiment where the CoT is replaced by entirely incorrect physics reasoning (wrong equations, wrong units) rather than truncated, to test whether models blindly follow the scratchpad or override it—this would directly probe the faithfulness claim.
- Add a zero-shot (no CoT) accuracy condition to each deletion sweep plot as a horizontal reference line.

---

## Score and Decision

The paper asks the right question for the AI-for-Science community and makes a credible empirical contribution with a novel framing. However, the LLM-as-judge confound is a serious threat to the core experimental claims, the token-overlap analysis lacks a proper baseline, and the central "cramming" phenomenon is not mechanistically distinguishable from simple parametric fallback. These are not incidental; they concern the validity of the paper's main conclusions about faithfulness. The work is publishable with significant revision but is not yet ready in its current state.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>