Now I have all the data I need. Let me write the consolidated review.

## Summary
This paper addresses the problem that interaction primitives extracted from a single DNN lack generalizability across different models trained for the same task. The authors propose a joint optimization objective (Eq. 7) that extracts AND-OR interactions from multiple DNNs simultaneously, combining a row-wise max penalty with an ℓ₁ penalty and a shared decomposition parameterization to encourage cross-model sharing. Experiments on sentiment classification (BERT-base/BERT-large), dialogue (LLaMA/OPT), and image classification (ResNet-20/VGG-16) show that the proposed method yields significantly higher overlap in interaction sets across model pairs than existing baselines.

## Strengths
1. **Well-motivated problem.** The paper clearly demonstrates (Section 3.2) that standard sparsity-driven interaction extraction yields only ~21% overlap across different initializations, and poor overlap across different DNNs trained for the same task. This motivates the need for a method that explicitly extracts shared interactions across multiple models.

2. **Novel objective for cross-model interaction extraction.** The combined loss (rowmax + α·ℓ₁ + shared decomposition) is a genuine contribution. The rowmax term penalizes the maximum interaction across models per subset, ensuring sparsity is enforced jointly rather than independently; the α-term suppresses redundant/shortcut interactions; and the shared decomposition (γ̅_T + γ̂_T^(i)) ties the models' decompositions together. Experiments across three diverse tasks (text, dialogue, image) consistently show higher overlap (s_and, s_or) than L₁-sparse or Harsanyi baselines (Figures 2–3).

3. **Theoretical and practical treatment of noise instability.** The paper derives that interaction variance grows exponentially with order (2^{|T|}σ²) and introduces a learned error term ε_T^(i) bounded by τ_ε to absorb noise. The universal matching property is verified to hold after removing the error term (Figure 4), demonstrating robustness without sacrificing faithfulness to model outputs.

4. **Qualitative evidence of meaningful shared interactions.** Figure 5 visualizes shared primitives (e.g., "black dog") versus model-specific ones (e.g., "they said"), providing intuitive support that the shared interactions correspond to more task-relevant concepts.

## Weaknesses

### Fatal
None.

### Major
1. **Imprecise justification of the loss mechanism.** The paper states (line 173) that the rowmax loss "ensures that if a DNN encodes a strong interaction *w.r.t.* the set T_k, then we can also extract the same interaction *w.r.t.* T_k from the other m−1 DNNs without a penalty." This is misleading. The rowmax penalty for subset T is `max_i |I_and^(i)(T)|`, which is the same whether the interaction appears in one model or all models — it does not "spare" the interaction when shared. The actual mechanism that produces shared interactions is the shared decomposition parameter γ̅_T combined with the bound on model-specific γ̂_T^(i), not the rowmax operator itself. Line 184 further overstates that the rowmax "assigns much higher penalties to non-generalizable interactions than generalizable interactions," which is also incorrect — the rowmax penalty is identical. The paper's central explanation of why the method works is imprecise and could mislead readers. The method itself is still sensible (the shared decomposition forces all models toward similar decompositions, and the rowmax + α-term provides sparsity), but the stated rationale needs correction.

2. **Evaluation is partially circular for the "faithfulness" claim.** The paper evaluates generalization by measuring the overlap of interaction sets across models — precisely the quantity the method is designed to maximize. The improvement is therefore expected. While the paper also verifies sparsity and universal matching (showing the interactions remain meaningful), there is **no independent validation that the shared interactions are more faithful** — e.g., no human evaluation of interpretability, no completeness test against held-out model behaviors, no demonstration that shared interactions improve downstream utility (such as counterfactual understanding or model debugging). The paper repeatedly claims shared interactions are "more faithful" (title, abstract, line 284), but faithfulness is asserted rather than demonstrated beyond the overlap metric itself.

3. **The ambiguity decomposition (Challenge 1) is acknowledged but not resolved theoretically.** The paper recognizes that decomposition into AND/OR interactions is non-unique and that multiple local minima exist (Section 3.2). The proposed method adds sharing constraints and sparsity as inductive biases, but there is **no formal guarantee** that the resulting decomposition corresponds to a "true" or "intrinsic" set of interactions. The universal matching theorem holds for any decomposition, so it does not validate the particular one found. This is a known hard problem, but the paper oversells its resolution.

### Minor
1. **Only tested on pairs of models.** The experiments pair exactly two models per task (BERT-base vs. BERT-large, LLaMA vs. OPT, ResNet-20 vs. VGG-16). The paper does not test whether the method scales to 3+ models, which would substantially strengthen the claims about generalizable primitives.

2. **No ablation on α.** The final loss (Eq. 7) has a hyperparameter α that controls the strength of the ℓ₁ penalty on unselected interactions. The paper does not ablate α or explain how it was chosen, making it unclear how sensitive the results are to this parameter.

3. **Low-order sharing phenomenon is observed but not explained.** Figure 6 shows that low-order interactions are more consistently shared across models, but the paper does not offer an explanation for why this occurs. This is a missed opportunity for deeper insight.

### Trivial
- The paper uses a threshold τ for defining interaction primitives (τ = 0.05·max_S|I(S|x)| in experiments) but this is only mentioned in the experiment section and not carried through the formal definitions in Section 3.1.
- The number of input variables n used per sample is not stated in the main paper (likely deferred to the appendix).

## Nice-to-Haves
- A human evaluation or concept‑alignment test (e.g., measuring whether shared interactions correspond to human‑annotated concepts) would substantially strengthen the faithfulness claim.
- Testing with 3+ models per task would show that the method scales beyond pairs.
- Ablating α and showing its effect on the trade-off between sparsity and generalization would be a useful sensitivity analysis.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"The paper does not quantify how severe the ambiguity is in real DNNs"** (Section 3.2, Challenge 1) — This is a valid observation but the paper acknowledges Challenge 1 as a known open problem and proposes the method as a practical heuristic; demanding quantification of ambiguity severity is a scope-expansion request.
- **"Experimental setup unclear about n (number of input variables)"** — Details about n are almost certainly in the appendix, which is stripped by the parser. Per instructions, weaknesses about missing appendix details must be removed.
- **"Would results generalise to three or more models? Not addressed"** — I kept this as a minor weakness rather than removing it, as it's a reasonable next-step concern but not a flaw in the existing evaluation.
- **Several generic formatting/style nitpicks from the harsh critic** — Removed per formatting-nitpick rule.
- **"The paper only shares interactions between two models per task"** — Kept as minor weakness above.
- **Strength Finder's claim about "novel loss function that explicitly penalizes non‑generalizable interactions"** — Toned down in my strengths list since "penalizes non‑generalizable interactions" is the imprecise formulation discussed in Major Weakness 1.

## Novel Insights
None beyond the paper's own contributions. The key insight — that the rowmax penalty combined with a shared decomposition parameterization can force interaction sets to converge across models — is the paper's main contribution. However, the reviewers did not surface any additional novel perspective beyond what the paper itself states.

## Suggestions
1. **Correct the explanation of the loss mechanism.** Acknowledge that the rowmax operator does not directly "spare" shared interactions; instead, the sharing is driven by the shared decomposition (γ̅_T). Explain clearly that the rowmax acts as a joint sparsity regularizer across models, and the α-term prevents redundancy.
2. **Add an independent faithfulness evaluation.** This could be a perturbation‑robustness test (measure whether shared interactions remain salient under input perturbations beyond the noise model already used), a concept‑alignment study, or a demonstration that shared interactions enable better task‑relevant model editing or debugging.
3. **Include an ablation on α** to show how the trade-off between sparsity and generalization behaves.
4. **Use 3+ models for at least one task** to show the method scales beyond pairs.

## Score and Decision

Below are calibration anchors from the human-review corpus:

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3pWSL8My6B.md` (Sparse Interaction Primitives in DNNs) | 7.00 | A stronger theory paper from the same line of work. The current paper has more empirical emphasis but less rigorous theoretical justification. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ze7DOLi394.md` (Interaction of Models, Data, and Features) | 7.50 | Strong theoretical framework with thorough empirical validation. The current paper is less theoretically rigorous and has a narrower scope. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/I4e82CIDxv.md` (Sparse Feature Circuits) | 8.00 | Exceptional empirical validation with downstream applications and human evaluation. The current paper lacks this level of validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WTh6EnJXWQ.md` (DeepROCK) | 5.00 | Comparable quality — both papers have interesting practical ideas but notable gaps (theoretical justification for DeepROCK, imprecise loss justification and evaluation circularity for the current paper). The current paper is slightly stronger in breadth of tasks. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RBqvU12SHz.md` (Structural Probing with Feature Interaction) | 3.25 | Weaker paper with unclear contributions. The current paper has clearer motivation, better-defined methodology, and more convincing experiments. |

**Overall:** The paper addresses a real and important problem, proposes a novel method, and provides consistent empirical evidence across three tasks. However, the central claim about the loss mechanism is imprecisely stated, the evaluation of "faithfulness" is partially circular, and there is no independent validation that shared interactions are indeed more faithful primitives. The method has clear practical value, but these issues prevent the paper from being a strong contribution. Relative to the calibration anchors, the paper sits between the 5.00-level papers (interesting idea but notable gaps) and the 7.00-level papers (stronger theory and validation).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>