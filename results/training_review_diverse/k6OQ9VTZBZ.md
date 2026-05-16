Now I have a complete picture of the paper. Let me compose the final review.

## Summary

This paper introduces SPG (Sketch-Plan-Generalize), a neuro-symbolic framework for learning inductive program representations of grounded spatial concepts from few human demonstrations. The pipeline factors concept learning into three stages: (1) Sketch — using an LLM to generate a coarse program signature from natural language, (2) Plan — MCTS-based search over grounded action sequences accelerated by a neural action predictor and macro-actions from a concept library, and (3) Generalize — using an LLM to abstract the grounded plan into a general Python program. The approach supports continual learning through modular reuse of learned concepts.

## Strengths

- **Principled factorization of inductive concept learning**: The decomposition into Sketch, Plan, and Generalize directly addresses the entanglement of high-level program postulation, grounded plan validation, and program abstraction that the authors correctly identify as a key limitation of prior monolithic approaches (Section 5). The modular pipeline is clearly defined and provides a structured approach to a challenging problem.

- **Formalization of inductive spatial concepts**: Section 4 provides a recursive formulation (Eq. 1) with explicit induction, composition, and base terms, together with a Bayesian learning objective (Eq. 2). This formalization gives a precise hypothesis space that supports both modular reuse and continual learning, distinguishing the work from prior efforts that lack such structure.

- **Well-designed evaluation setup**: Section 6 defines three challenging evaluation datasets (in-distribution, label-swapped to test pre-training reliance, and out-of-distribution with larger concept sizes), multiple baselines (neural, LLM, VLM), and three model ablations. The metrics (program accuracy, IoU, MSE) are appropriate for the task. This design, if executed, would convincingly test the paper's claims.

## Weaknesses

### Fatal

1. **Section 7 (RESULTS) contains no actual results.** The section lists four evaluation questions (Q1–Q4) but provides no tables, figures, numerical values, program-accuracy scores, IoU numbers, MSE values, or comparisons to any baseline. The paper jumps directly to the conclusion after listing these questions. The abstract, introduction, and conclusion all make strong empirical claims ("significantly improving over the baselines," "stronger inductive generalization," "accurate program learning"), yet zero supporting evidence appears anywhere in the extracted text. The evaluation setup section (Section 6) describes what *would* be evaluated, but no results are actually reported.

This is not a formatting artifact or a missing-appendix issue — Section 7 exists in the main body and its textual content consists solely of four questions. Without any experimental evidence, the paper's central claims are unsubstantiated. The contribution cannot be evaluated, and the paper is fundamentally incomplete.

### Minor

1. **Training details of the neural action predictor π_neural are underspecified.** Section 5.2 (line 100) states that π_neural is trained to predict primitive actions from the current and next expected state, but provides no information about its architecture (e.g., MLP, CNN, transformer), training data size, supervision signal, whether it is trained per concept or globally, or how many demonstrations are used. This makes the "action space pruning" component difficult to reproduce or assess.

2. **Lack of concrete examples of learned programs.** The paper describes the Generalize stage as producing Python programs, but shows only a sketch example ("Tower(height=3, objects=[1,2,3])"). Providing actual learned programs for a few concepts (tower, row, staircase) would help readers understand the inductive form the approach discovers.

3. **The reward computation during MCTS search requires clarification.** Section 5.2 states that IoU between "the attained state and the expected state in the demonstration" is used as reward. During search, the agent may explore sequences that deviate from the demonstration's trajectory — it is unclear how intermediate expected states are determined for branches not present in the demonstration keyframes, and how the search handles partial construction states that don't match any demonstration keyframe.

### Trivial

None.

## Nice-to-Haves

- Including an ablation that removes each of the three stages (skip MCTS, skip LLM generalization) would strengthen the claim that each component contributes measurably.
- Showing the continual learning effect quantitatively — e.g., as the concept library grows, do later concepts require fewer MCTS steps or achieve higher accuracy?
- Reporting statistical significance (multiple seeds, variance across demonstrations).

## Removed Points

- **"Section 4 formalism is never referenced again"**: Factually incorrect. The paper references Equation 1 at line 88: "determining the concepts, their respective grounded parameters, and the order of composition as specified in the Equation 1." Removed as factually wrong.
- **"LLM baseline assumes absence of distractors (too generous)"**: The paper transparently states this assumption (line 127), and it favors the baseline, not the author's method. Per guidelines, removed as an asymmetric-baseline complaint that advantages the competitor.
- **"Expected state not explained"**: The paper explicitly states that expected states come from the demonstration (lines 92, 100). The reviewer's concern is partially addressed in the text; the remaining ambiguity about search deviations is kept as Minor weakness #3 above.
- **"Missing experimental results is due to missing appendix"**: Not an appendix issue — Section 7 is the main body RESULTS section and its text contains only four questions. This is a fatal flaw, not a missing-appendix artifact.
- **"Demonstration of embodied instruction following" (Strength Finder)**: This strength claims the paper demonstrates embodied instruction following with learned concepts, but no experimental evidence for this is presented. Removed as it conflicts with the verified weakness that results are missing.
- **Pure formatting/style nitpicks, typos, and parser artifacts**: Removed per guidelines.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no insight about the paper's factorization approach or formalism that the paper does not already articulate — the main issue is the absence of evidence, not a failure of the idea.

## Suggestions

The paper's methodology is well-conceived and the evaluation design is thorough. To make the paper publishable, the authors must add the complete results section with quantitative comparisons (program accuracy, IoU, MSE) for all three datasets and all baselines, including the ablation variants. Without this data, the paper's central empirical claims are unsupported and the submission is incomplete. If the results exist but were stripped during PDF extraction, a resubmission that includes them would be needed for evaluation.

## Score and Decision

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>