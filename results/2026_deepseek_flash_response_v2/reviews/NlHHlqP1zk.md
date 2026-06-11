Now I have all the information I need. Let me compile the final review.

## Summary

This paper proposes the Fast and Slow Effect (FSE) framework for evaluating whether LLM/VLM-generated concept annotations are semantically sufficient for classification. The framework has two components: (1) a progressive concept-gathering process (Background → Superclass → Salient Features → Detailed Features → Auxiliary Features) that transitions from "fast mode" (direct visual inference) to "slow mode" (text-only concept-based reasoning); and (2) the Class Representation Index (CRI) metric that measures whether the model can correctly classify using only its generated concepts. Experiments across 6 models and 5 datasets show that on fine-grained datasets, slow mode underperforms fast mode by ~25%, while on general datasets slow mode succeeds. The paper also demonstrates that fused (image+concepts) mode achieves ~90% CRI while slow mode alone achieves ~50%, challenging the utility-as-proxy assumption for validating annotation quality.

## Strengths

1. **Important problem and timely contribution.** Automatically validating concept annotations is a critical underexplored problem in XAI. The FSE framework is a fully automated approach requiring no human supervision, addressing a real bottleneck in deploying concept-based models at scale.

2. **Empirical disconfirmation of "Slow Mode Superiority" with cross-dataset contrast.** The paper hypothesizes that slow (concept-based) reasoning should outperform fast (visual) inference, but Table 2 shows the opposite on fine-grained datasets (CRI-Gap of -25% to -27%). Crucially, Table 3 shows that on general datasets (CIFAR-100, Caltech-101), slow mode *does* outperform fast mode — reaching >90% CRI at t=5. This cross-dataset contrast is the paper's strongest evidence: the failure is specific to fine-grained distinctions, not a general reasoning deficit.

3. **Exposing the utility-as-proxy fallacy quantitatively.** Table 4 shows fused mode (image + concepts) achieves ~93% CRI for GPT-4o on Car while slow mode alone achieves only ~61%. The large gap directly and quantitatively demonstrates that end-to-end downstream performance does not imply annotation sufficiency — a widely used validation assumption in prior work.

4. **Systematic evaluation across diverse settings.** 6 models (3 families, 2 sizes each), 5 datasets (3 fine-grained, 2 general), two annotation paradigms (post-hoc textual, visual-grounded), and multiple annotation stages. The breadth strengthens the empirical contribution.

5. **Well-motivated distractor selection.** The preliminary experiment (Table 1) showing semantically related distractors yield 34-45% contradiction rates vs. 14-20% for random distractors provides rigorous methodological grounding for the evaluation protocol.

## Weaknesses

### Fatal

None.

### Major

1. **CRI confounds annotation sufficiency with model reasoning ability, and the paper does not fully acknowledge this.** CRI(t>0) measures whether the *same model that generated the concepts* can predict the class using only those concepts as text. A low CRI could mean (a) the concepts are genuinely insufficient, or (b) the model is poor at text-based reasoning from its own textual outputs, even when those outputs are adequate. This is a structural confound in the metric itself.

The paper's *cross-dataset comparison partially mitigates this concern* — on general datasets (CIFAR-100, Caltech-101), slow mode *does* outperform fast mode (e.g., GPT-4o: 84.84%→94.07% on CIFAR-100), showing the model *can* reason effectively from concepts on those datasets. This makes it more likely that the failure on fine-grained datasets is due to insufficient annotations rather than a global reasoning deficit. **However, the paper does not make this argument explicitly.** It does not frame the general-dataset results as a control for the reasoning confound, nor does it acknowledge the confound as a limitation. Claims throughout the paper — "current annotation methods fail to provide sufficient semantic coverage" (abstract), "the annotator fails in the second stage" (Figure 1 caption) — lean entirely on the annotation-insufficiency interpretation without caveat.

**Impact:** The headline claim overreaches what the experimental design cleanly supports. The paper should either (a) explicitly frame the general-dataset results as evidence that the model can reason from concepts *when annotations are adequate*, strengthening the interpretation, or (b) add experiments using human-written "gold-standard" concepts to show that models achieve high CRI with those, isolating the annotation quality signal. This is the paper's most significant weakness and the primary reason it falls short of a clear acceptance.

### Minor

2. **The dramatic V-shaped trajectory is not analyzed.** In Table 3, CRI on general datasets drops precipitously from fast mode (84-91%) to t=1 (29-34%), then recovers to >90% by t=5. This is a strikingly large and non-monotonic effect. Understanding why t=1 is so much worse than t=0 (the model *sees the image* at t=0 but not at t=1 — this is the cleanest measure of the reasoning confound) and how recovery happens would strengthen the paper substantially. The pattern is also visible in the fine-grained results (Figure 3 shows dips at early t before partial recovery).

3. **No qualitative analysis of annotation failures.** The paper mentions a visual case study in the appendix but does not discuss it in the main paper. Showing what kinds of semantic information are missing from generated concepts (e.g., do they lack discriminative features entirely, or do they include them but the model fails to use them?) would substantially strengthen the empirical contribution and help distinguish the confound.

4. **The dual-process theory framing is superficial.** The "Slow Mode Superiority" hypothesis relies on a questionable analogy to Kahneman's System 1/System 2. Comparing visual classification to text-based reasoning from the model's own concepts is not a valid application of dual-process theory. The paper would be better off simply stating the empirical null hypothesis: "if the concepts are sufficient, the model should be able to recover the correct class from them." The dual-process framing adds rhetorical weight to a hypothesis that the paper then disproves, but this framing is itself questionable.

### Trivial

5. **CRI formula notation issue.** Equation (2) writes CRI = (1/t) * Σ_{i=1}^t 1[y_i^t = y_i], where i indexes test instances (1,...,l) but t is used as the upper bound. The bound should be l, not t. This is a minor notational error.

## Nice-to-Haves

- **Validation using human-written concepts.** Having models evaluate human-collected "gold-standard" concept annotations (e.g., from CUB with expert concepts) would directly test whether the CRI confound is real: if models achieve high CRI with human concepts but low CRI with their own, the annotation-insufficiency interpretation is strongly supported.
- **Statistical significance testing** between models and conditions would strengthen confidence given the modest number of models (6) and datasets (3 fine-grained).
- **Sensitivity of distractor selection** to the choice of backbone (ResNet-18); reporting results with CLIP-based or WordNet-based distractors would strengthen robustness claims.

## Removed Points

These points were removed from the harsh critic or strength finder inputs with brief justifications:

- **Dual-process theory "misapplication" as a fatal flaw.** Removed because the paper's empirical contribution does not depend on the dual-process theory being valid. The paper states a testable hypothesis and finds it false; the empirical finding stands regardless of the motivating analogy's fidelity to Kahneman. Kept only as a Minor framing concern.
- **Utility-as-proxy experiment over-interpretation.** Removed because the paper's claim is appropriately cautious: "strong performance in downstream tasks may not correlate with adequate conceptual supervision, suggesting that high utility scores can be misleading." This is a reasonable interpretation of the data.
- **Over-reliance on Figure 1 anecdote.** Removed because the paper uses this as a standard motivating example; all subsequent analysis is quantitative.
- **Code/data availability concerns.** Removed per hard rules: cited resources are assumed to exist.
- **Strength Finder's generic/superficial strengths** (e.g., "the paper addresses an important problem"). Removed unless backed by specific evidence.
- **Candidate set sensitivity to ResNet-18 choice.** Demoted to Nice-to-have, as the preliminary experiment is a methodological design choice, not a core finding.

## Novel Insights

The cross-dataset contrast (general vs. fine-grained) and the fused-mode experiment together offer a genuinely novel insight: the failure mode of concept annotations is dataset-dependent, and downstream accuracy is a poor diagnostic because the visual modality dominates when the classification task is fine-grained. This suggests that annotation validation must be task-specific and cannot rely on aggregate metrics. The paper does not fully articulate this insight but the data supports it.

## Suggestions

1. Reframe the paper's claims to distinguish between "annotations are insufficient" and "models cannot reliably classify from their own generated concepts on fine-grained tasks." Make the cross-dataset contrast an explicit control for the reasoning confound: since the model succeeds at concept-based reasoning on general datasets, its failure on fine-grained datasets is attributable to insufficient annotations.

2. Add an experiment using human-written gold-standard concepts (e.g., from CUB) to validate that models achieve high CRI with high-quality concepts, directly isolating the annotation quality signal.

3. Analyze the V-shaped trajectory in Table 3 — the t=1 collapse is a large and unexplained effect. Comparing t=0 (image + textual prompt) with t=1 (textual concepts only, no image) would directly quantify the contribution of visual vs. textual information.

4. Drop or substantially soften the dual-process theory framing. The empirical null hypothesis is cleaner and avoids a potentially misleading analogy.

---

### Calibration Report

**Round 1 (Bracketing):** Queried for papers on "evaluating LLM-generated concept annotations for XAI" across three score bands. Weak band (<3.5) returned KLUDshUx2V (3.40, Reject) — very similar topic but clearly weaker in experimental depth and novelty. Middle band (3.5-7.5) returned RC5FPYVQaH (5.75, Accept), 0qrTH5AZVt (4.67, Reject), and others. Strong band (>7.5) returned papers on unrelated topics with scores ~8.0. **Initial bracket: 4.0–6.5.**

**Round 2 (Narrowing):** Queried for "evaluation framework for concept bottleneck model annotations LLM" within (3.5, 6.0) and "benchmark evaluating LLM concept annotation quality XAI" within (5.0, 7.0). Retrieved relevant anchors:

| Anchor | Avg Score | Decision | Comparison to This Paper |
|--------|-----------|----------|------------------------|
| KLUDshUx2V — Automating High-Quality Concept Banks | 3.40 | Reject | Much weaker: limited experiments, similar topic but less sophisticated framework |
| 5Aem9XFZ0t — Zero-shot Concept Bottleneck Models | 4.83 | Reject | Weaker: method paper with limited novelty; my paper has stronger empirical contribution |
| Q9Z0c1Rb5i — Boosting CBM with Supervised Learning | 5.00 | Reject | Comparable quality but different weaknesses; mine has more novel framework |
| 8sfc8MwG5v — Adaptive CBM for Distribution Shifts | 5.50 | Accept | Cleaner contribution (method with clear results); my paper confound is more significant |
| tZk3LnvVtK — Measuring LLM Uncertainty With Internal Concepts | 5.60 | Reject | Similar in using concepts for evaluation; had clarity issues, mine is clearer |
| RC5FPYVQaH — Concept Bottleneck LLMs | 5.75 | Accept | Stronger contribution (method with practical applications); mine more narrow |
| vJ0axKTh7t — Labyrinth of Links (MLLM Association Benchmark) | 6.25 | Accept | Clean benchmark paper with clear findings; my paper has structural confound issue |

**Final score:** My paper is stronger than the 3.40–4.83 reject anchors but the structural CRI confound makes it less compelling than the accepted anchors at 5.50–5.75. The paper sits between the weaker rejects (~4.8) and the accepts (~5.5). Score: **5.0** — borderline paper with real contributions that require addressing the confound issue before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>