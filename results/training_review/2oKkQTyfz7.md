Now I have all the information needed. Here is the consolidated review.

## Summary

This paper introduces GSA-VLN, a new task requiring VLN agents to adapt to a persistent environment over multiple episodes. The authors construct GSA-R2R, a large evaluation dataset spanning 150 buildings (including 75 OOD non-residential buildings) with 600 instructions per building across three speaking styles (Basic, Scene, User). They propose GR-DUET, a memory-based method that maintains a global topological graph across episodes within an environment and uses environment-specific fine-tuning. On GSA-R2R, GR-DUET consistently outperforms existing VLN models and adaptation baselines across all instruction types.

## Strengths

- **Well-motivated and formally defined task (GSA-VLN).** The gap between standard one-shot VLN evaluation and real-world persistent environments is clearly articulated. The formalization in Section 3.2 — with the environment-specific memory bank $\mathcal{M}_E$, the distinction between memory retrieval and parameter updates (Eqs. 1–4), and the differentiation from lifelong learning and IVLN — provides a principled foundation that the community can build upon.

- **Large-scale, diverse evaluation dataset (GSA-R2R).** With 150 evaluation buildings (vs. 29 in R2R), 600 instructions per building across three speaking styles, and explicit OOD categorization (75 non-residential buildings), this dataset is a significant resource. Table 1 and Figure 2 demonstrate substantially greater scene and instruction diversity than existing VLN evaluation datasets. The t-SNE analysis (Figure 4) quantitatively verifies that the Scene/User instructions occupy distinctly different embedding space from R2R training data.

- **Creative three-stage instruction orchestration pipeline.** The pipeline — speaker generation, VLM-based refinement guided by path visualization, and LLM role-playing for stylistic rewriting — is methodologically sound and addresses a real limitation. Human evaluation (Table 2) confirms ~80% path-instruction alignment and distinct speaking styles, validating the pipeline's effectiveness despite the intentional OOD divergence.

- **GR-DUET consistently outperforms baselines across all splits.** The global topological graph mechanism yields substantial improvements over DUET (up to 11% SR). The paper further demonstrates via ablation (Tables 7, 8) that both the graph-based pretraining and the PREVALENT augmented data contribute to this gain, and that the memory-based graph simulation strategy outperforms the proportion-based alternative.

- **Informative benchmarking of adaptation strategies.** The evaluation of TTA (TENT, SAR), Back-Translation, proxy tasks, and memory-based methods (TourHAMT, OVER-NAV) on this new task reveals that optimization-based methods achieve ≤1% SR gains and TourHAMT can degrade performance. This finding — that naive adaptation approaches fail — is a non-obvious insight that motivates the need for structured memory (like GR-DUET's global graph) and justifies the paper's design choices.

## Weaknesses

### Fatal
None.

### Major
None that threaten the paper's core claims. The following issues are substantive but addressable.

### Minor

1. **Slight mismatch between task framing and method: GR-DUET does not perform online parameter updates.** The task definition (Section 3.2) lists parameter updates via unsupervised learning as one of two primary distinctions of GSA-VLN, and the introduction states agents should "continuously update their model parameters." GR-DUET, however, is purely memory-based during evaluation — the environment-specific fine-tuning occurs before evaluation, not as an online adaptive process. The paper is transparent about this (categorizing GR-DUET as memory-based alongside TourHAMT), but the framing overreaches relative to what the method actually delivers. The paper would benefit from clarifying that GR-DUET addresses one axis (memory-based adaptation) of the two-axis GSA-VLN task, and that online parameter updates remain an open direction.

2. **Dataset quality validation is quite limited.** The human evaluation (Table 2) uses only 15 participants and 20 instructions for a dataset of 90,000 instructions (150 buildings × 600). While the ~80% alignment rate is encouraging, the sample is too small to confidently assess dataset-wide quality, especially across diverse building types and instruction styles. The filtering stage of the instruction pipeline (using a navigation model to detect infeasible instructions) could also encode systematic biases favoring certain navigation model architectures; this concern is not discussed. A larger-scale human evaluation or a held-out model analysis would strengthen confidence in the dataset.

3. **The SOTA claim is slightly overclaimed for the scope of comparisons.** The paper states GR-DUET achieves "state-of-the-art results on all GSA-R2R splits." For Basic instructions, this is fully supported by Table 4 (comparison against TENT, SAR, TourHAMT, OVER-NAV, etc.). For User and Scene instructions, the paper does compare against TTA methods and Back-Translation (as the text on line 228 confirms: "TTA methods achieve 1% SR increase in Scene instructions"), so the claim is supported. However, the claim would be more robust if the paper explicitly enumerated which baselines appear in Tables 5–6 rather than leaving the reader to infer from the surrounding text, and if memory-based baselines (TourHAMT, OVER-NAV) were explicitly called out on these splits alongside the TTA methods.

4. **Some implementation and analysis details are underspecified.** The $\alpha=50$ threshold (max episodes in the graph) is stated but not justified beyond the ablation in Table 8, which explores values. The environment-specific training strategy ("assign individual graphs to each training environment") is described at a high level — it is unclear whether this means training separate model copies per environment or using environment-specific graph embeddings in a shared model. Ablating the environment-specific training itself (e.g., shared vs. per-environment graphs while keeping the global graph mechanism) would help isolate the main contribution.

5. **Analysis of performance drops across splits is shallow.** Table 3 shows large performance drops on GSA-R2R vs. R2R, but the paper does not disentangle whether these are driven by the environment distribution shift (ID→OOD buildings), the instruction style shift (Basic→Scene/User), or interaction effects. The observation that models perform worse on User than Basic instructions is reported but not explained mechanistically (e.g., via per-instruction OOD word frequency analysis or vocabulary overlap statistics).

### Trivial
None that warrant listing beyond the parser-induced artifacts.

## Nice-to-Haves

- An ablation that isolates the effect of the global graph vs. per-episode history (e.g., DUET with a larger history buffer, without the graph structure) would clarify the mechanism behind GR-DUET's gains.
- Learning curves (SR vs. episode number) for a few environments would visually demonstrate that the agent actually improves over time, directly supporting the adaptation narrative.
- A case study figure showing the global graph growing across episodes (overlaid on a floor plan) would make the mechanism intuitive.
- Examples of the same path's instruction through all three pipeline stages (speaker→VLM-refined→LLM-rephrased) would help illustrate the style diversity achieved.

## Removed Points

These points from the source reviews were removed with justification:

- **"Tables 5 and 6 compare only DUET and GR-DUET for User/Scene instructions — why are other adapted baselines missing?"** (Harsh Critic, Critical Issue #1) → **REMOVED (factually wrong).** The paper's text (line 228) explicitly states "TTA methods achieve 1% SR increase in Scene instructions" and "the improvement from Back-Translation diminishes," confirming that these baselines were evaluated on User and Scene splits. Tables 5 and 6 do include adaptation baselines.

- **"The primary comparison in Table 3 is against non-adapted baselines, making the SOTA claim unsupported"** (Harsh Critic, Critical Issue #1, rest) → **REMOVED (misunderstands paper structure).** Table 3 is explicitly scoped as evaluating "methods without adaptation techniques to determine whether they can maintain the same performance" — it is a dataset difficulty benchmark, not the method's main results table. The adaptation comparisons are in Tables 4–6, which do cover all instruction types.

- **"The memory bank vs. executed-path ambiguity"** (Section-by-Section Notes) → **REMOVED (paper addresses this).** The paper states in Section 3.2: "The stored memories in the memory bank represent the execution history of agents, although there may exist misalignment between instructions and paths due to navigation errors, all the memories are treated as unlabeled data." The potential for error propagation is acknowledged.

- **"α=50 chosen without justification"** (Section-by-Section Notes) → **REMOVED (paper addresses via ablation).** Table 8 systematically explores the effect of different α values.

- **"ScaleVLN data leakage concern"** (Section-by-Section Notes) → **REMOVED (paper already notes this).** The paper marks ScaleVLN results with † and explicitly states "Data leakage exists since ScaleVLN uses HM3D as training data."

- **Various formatting/style nitpicks and missing appendix concerns** → **REMOVED per hard rules** (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The core findings — that standard VLN models degrade substantially on OOD environments and instructions, that existing adaptation methods (TTA, memory-based) provide minimal gains, and that structured global graph retention with environment-specific training is effective — are the paper's own empirical contributions. The reviews do not surface an additional novel perspective beyond what the paper already establishes.

## Suggestions

1. Strengthen the SOTA claim by providing an explicit structured table or text block showing that GR-DUET outperforms *all* adaptation baselines (TENT, SAR, TourHAMT, OVER-NAV, etc.) on *each* of the five splits (Test-R/N × Basic/User/Scene), not just on Basic. The information appears to be present in the paper but is scattered across tables and text; consolidating it would eliminate any ambiguity.

2. Scale up the human evaluation of the dataset (e.g., 50–100 instructions across diverse building types) to provide more robust quality assurance. Acknowledging and discussing potential biases from the navigation-model-based filtering step would also strengthen the dataset contribution.

3. Clarify the relationship between the GSA-VLN task definition and GR-DUET: explicitly state that the method addresses the memory-based adaptation axis, while online parameter updates remain an open challenge. This would resolve the current framing mismatch without diminishing the contribution.

4. Add learning curves (SR vs. number of episodes) for representative environments to empirically demonstrate that the agent's performance improves with experience, directly supporting the adaptation claim.

5. Provide a deeper analysis of which factors drive the performance drops on GSA-R2R (environment OOD, instruction OOD, or both), e.g., via per-building-type breakdowns or vocabulary-overlap statistics.

## Score and Decision

The paper makes genuine contributions: a well-motivated new task, a large and diverse evaluation dataset, and a method that clearly outperforms existing approaches on it. The weaknesses are matters of framing precision, validation scale, and analysis depth — not fatal flaws. The paper would benefit from a pass that tightens the method/task alignment and expands the dataset validation, but its core contributions are solid and well-supported by the experiments presented.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>