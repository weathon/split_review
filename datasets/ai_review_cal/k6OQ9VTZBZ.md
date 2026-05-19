- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5
I have thoroughly verified the paper. Here is my consolidated review.

---

## Summary

This paper proposes SPG, a three-stage pipeline (Sketch–Plan–Generalize) for learning inductively generalizable neuro-symbolic program representations of grounded spatial concepts (e.g., towers, staircases) from few human demonstrations. The method factors concept learning into: (1) generating a coarse program signature via an LLM, (2) searching for a grounded action sequence via MCTS with neural pruning, and (3) distilling the plan into a general Python program that supports hierarchical reuse. The method description and formalization are well-structured and motivated.

## Strengths

- **Principled factorization of the concept learning problem (Sketch–Plan–Generalize, Section 5):** The paper decomposes the intractable joint program-search problem into three stages with clearly distinct roles. The sketch provides a coarse signature, the MCTS plan grounds the search in physical plausibility via demonstration-aligned reward, and the generalization step produces a reusable inductive program. This decomposition cleanly addresses the entanglement the paper identifies as the root cause of poor generalization in prior work (Section 1).

- **Formal definition of inductive spatial concepts (Eq. 1, Section 4):** The recursive formulation with induction, composition, and base terms provides a principled hypothesis space that explicitly captures inductive generalization to arbitrary sizes and hierarchical reuse. This formalization directly guides the search and abstraction steps and is a novel contribution relative to prior work that treats spatial assemblies as flat goal configurations.

- **MCTS with neural action pruning (Section 5.2):** The reactive policy $\pi_{\mathrm{neural}}$ reduces the branching factor from $|\mathcal{A}_c|+|\mathcal{A}_p|$ to $|\mathcal{A}_c|+1$, addressing a key scalability challenge as the concept library grows. This is a specific, well-motivated design choice that enables modular continual learning.

## Weaknesses

### Fatal

- **The paper contains no experimental results.** Section 7 (Results) is a skeleton consisting of only four evaluation questions (Q1–Q4). It presents zero data — no tables, no figures, no accuracy numbers, no IoU/MSE values, no comparisons to baselines, no ablation analyses, and no demonstration of continual learning. The Conclusion (Section 8) references "extensive evaluation" and "stronger generalization" as if results were shown, but the provided manuscript has none. Without the empirical foundation, the paper's central claims — that SPG outperforms baselines, generalizes out-of-distribution, supports continual learning, and enables instruction following — cannot be assessed. A method paper whose entire empirical evaluation is absent is not a complete research contribution. *(Note: this is not a parser-stripping artifact; Section 7 contains no references to tables, figures, or data that could have been lost.)*

### Major

- **Continual learning claim is asserted but not demonstrated even conceptually.** The paper claims that the library $\mathcal{L}$ is updated and that subsequent concepts benefit from macro-actions (e.g., learning "staircase" from previously learned "tower"). However, no experiment, ablation, or analysis is provided to substantiate this — not even in the method description. The ablation variant MCTS+P−L (without library) is listed but never discussed with results. The continual learning claim remains a design aspiration.

- **Several method components are underspecified in ways that affect reproducibility.** (a) The neural action predictor $\pi_{\mathrm{neural}}$ is said to be "trained on a corpus of pick-and-place instructions" — the size, coverage, and construction of this corpus are not described, nor is it clear whether it covers the spatial relations needed for the target concepts. (b) The generalization step uses GPT-4 to distill a Python program from the grounded plan, but the prompt template, validation procedure, and failure modes (e.g., hallucinated loops) are not discussed. (c) The quasi-symbolic visual grounding module is referenced to prior work but its architecture and training procedure (fixed or updated during continual learning) are not specified. These gaps make it difficult to assess or reproduce the method even if results were present.

### Minor

- **The MCTS reward computation is ambiguously specified.** The paper states that "IoU between the attained state and the expected state in the demonstration is provided as a reward" (Section 5.2), but it is unclear whether the reward is computed at each search step against the corresponding keyframe, only at the end against the goal state, or via some intermediate scheme. How IoU is computed for non-rectangular structures (e.g., arches, crosses) is also not discussed. This ambiguity affects understanding of a central component of the method.

- **The $\lambda$ exponent in the formal definition (Eq. 1) is said to be 0 or 1, but how it is determined for a given concept in practice is not explained.** While this is a minor clarity issue in the formalization, it would benefit from a concrete example showing how specific concepts map to the formal definition.

### Trivial

None beyond those already addressed above.

## Nice-to-Haves

- A concrete worked example tracing the full pipeline (sketch → MCTS plan → generalized program → execution) for one concept (e.g., a staircase learned from towers) would greatly improve reader intuition.
- Ablation isolating the neural pruning (MCTS+P+L vs. MCTS−P+L) with node expansions or wall-clock time would ground the claimed efficiency gains.
- Including the LLM prompt templates for the Sketch and Generalize steps in the main paper (they were likely in the stripped appendix) would improve reproducibility.

## Removed Points

- **"Baselines may be underpowered / unfair comparison"** (from Harsh Critic): This critique speculates that LLM/VLM baselines were unfairly disadvantaged, but no results exist to verify or refute this. Without actual experimental data, this is a hypothetical concern, not a verifiable weakness. Removed per the rule that speculative-fatal claims about missing results should not be retained as separate weaknesses beyond stating the core missing-results issue.

- **Various presentation/reproducibility nitpicks** (from Harsh Critic): Criticisms about undisclosed hyperparameters, missing prompt templates, architecture details of the neural predictor, etc. are largely about content that was likely in the stripped appendix (references to A.3, A.4, A.5, C.3 appear in the main text). Removed per instructions about missing appendix content.

- **Strength Finder's generic strengths about "problem importance" and "evaluation design":** The evaluation design strength (out-of-distribution datasets, curriculum learning) describes intended experiments, not demonstrated results. Since no results exist, these are descriptions of experimental plans, not validated strengths. The curriculum learning strength similarly conflates design description with demonstrated capability. Removed per rule that strengths must be concrete and supported by evidence.

- **"Statistical significance" concern** (Harsh Critic): Without any results, this is premature.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation that the paper itself does not already state or imply.

## Suggestions

1. **Complete the paper with actual experimental results** before any resubmission. This is essential — the method cannot be evaluated without data.
2. Clarify the MCTS reward computation: specify whether IoU is computed per-step or only at the terminal state, and how it handles non-rectangular geometries.
3. Provide a concrete end-to-end trace of the pipeline on one concept to build reader intuition for how the three stages interact.
4. Discuss the construction and coverage of the training corpus for $\pi_{\mathrm{neural}}$, and include prompt templates for the LLM-based stages.

---

**Evaluation on standard axes:**

- **Originality:** Good. The Sketch–Plan–Generalize factorization and the formalization of inductive spatial concepts are novel relative to prior work in program synthesis and skill learning.
- **Importance of research question:** High. Learning inductively generalizable spatial concepts from few demonstrations is a genuine and difficult problem for embodied agents.
- **Claims well-supported?** No — zero experimental results are presented.
- **Soundness of experiments:** Cannot be evaluated — no results exist.
- **Clarity of writing:** Generally clear and well-structured, despite some underspecified details (MCTS reward, $\lambda$ determination).
- **Value to the research community:** Potentially significant if the method works as described, but the current submission provides no evidence to assess this.
