My analysis is complete. I've verified all claims against the paper text. Let me now output the final review.

## Summary
This paper studies how the standard SFT+DPO post-training pipeline performs when both task demonstrations and preference comparisons are unreliable, and proposes Iterative Label Refinement (ILR) as an alternative. The key contributions are: (1) diagnosing that DPO fails under unreliable supervision because it faces a regularization trade-off (unreliable feedback forces high KL regularization to prevent overoptimization, but this regularization prevents the large model updates needed to correct SFT errors), and (2) proposing ILR, which uses comparison feedback to iteratively improve the SFT dataset rather than update the model, thereby bypassing the trade-off. The method is evaluated on math (GSM8K), code (BIRD), and safe instruction-following (SaferPaca) at 2B–70B scales with both LM-simulated and time-constrained human supervision.

## Strengths

1. **Clear diagnosis of DPO's regularization dilemma under unreliable supervision (Section 4.1, Figure 3)**: The paper identifies a specific mechanism — unreliable comparison feedback forces high KL regularization (large β) to prevent overoptimization, but this same regularization prevents the large model updates needed to correct errors from unreliable SFT data. The controlled experiments with oracle vs. mixed vs. unreliable feedback (Figure 3a) cleanly demonstrate that only strong regularization avoids collapse with unreliable feedback, while Figure 3b shows that large KL divergence drives accuracy gains with reliable feedback. This goes beyond prior work on noisy preferences (Chowdhury et al. 2024; Fisch et al. 2024; Gao et al. 2024) by revealing how the interaction of unreliable demonstrations *and* unreliable comparisons creates this particular failure mode.

2. **Principled cross-labeling design in ILR (Section 5.1)**: The paper recognizes that SFT models memorize errors in their training data, so a model trained on the full dataset would not generate better proposals for training prompts. ILR addresses this by training two SFT models on disjoint halves of the data and having each model propose replacements for the half it was *not* trained on. This design is directly motivated by the empirical finding that SFT models outperform their training data on held-out prompts — it is a principled solution to a non-obvious obstacle.

3. **Multi-task, multi-scale empirical validation with human study**: ILR is evaluated across three distinct tasks (GSM8K math, BIRD SQL code generation, SaferPaca safe instruction-following) at three model scales (Gemma 2B, Mistral 7B, Llama 3 70B), and the LM-simulated findings are validated with a time-constrained human annotator study (Section 6) that reproduces the qualitative pattern. Figure 4 shows ILR consistently improving over multiple rounds while DPO plateaus or declines.

4. **Important ablation ruling out naive model-generated data replacement (Section 5.2)**: The paper shows that replacing SFT labels with model-generated proposals *without* comparison feedback leads to performance degradation ("model collapse"). This control experiment demonstrates that the comparison feedback in ILR is doing genuine work — improvements do not come simply from using model-generated data, and the weak-to-strong generalization phenomenon alone is insufficient without the evaluative signal.

## Weaknesses

### Fatal
None.

### Major

1. **No measures of variance or statistical significance reported for any experiment.** The paper presents all results through figures without any standard deviations, confidence intervals, or indication that results were replicated across multiple runs or seeds. The LM-simulated supervision involves stochastic processes (different random seeds produce different unreliable demonstrations, different model splits, different comparison outcomes), yet every condition appears to be evaluated from a single run. Without any measure of variability, the reader cannot assess whether the reported differences between ILR and DPO are reliable or could be within run-to-run noise. This is especially important given that ILR involves multiple stochastic steps (data splitting, training two models on halves, sampling proposals, running comparisons) that compound variance.

2. **Compute cost asymmetry between ILR and DPO is not discussed.** Each ILR round requires: (a) training two SFT models on disjoint halves of the data, (b) generating proposals from both models, (c) running comparisons, and (d) training a new full SFT model from scratch on the updated data. In contrast, DPO simply continues training the existing SFT model using comparison data. The paper does not acknowledge this cost asymmetry, nor does it attempt to control for compute budget (e.g., giving DPO more rounds or more comparison data to roughly match ILR's training cost). While a more expensive method that performs better is still valuable, practitioners need to understand the compute overhead to assess whether ILR is practical for their setting.

### Minor

1. **Missing experimental details.** (a) The number of ILR rounds *K* is never specified for the LM-simulated experiments — the text says "repeated for *K* iterations" (page 7, line 137) without stating the value. (b) The hyperparameter α=0.15 is used in all experiments without any sensitivity analysis showing how results vary with α. (c) How many proposals are sampled per prompt in ILR is not stated. (d) The "sufficiently different" criterion for SaferPaca ("large embedding distance") is not quantified — what embedding model and what distance threshold?

2. **No tables reporting concrete numerical results.** All experimental results are presented exclusively in figures. While figures convey qualitative trends, the absence of any table reporting exact accuracies, win rates, or effect sizes makes it difficult to assess the practical magnitude of ILR's improvements over DPO. A reader cannot determine from the text whether improvements are 2% or 20%, or whether ILR closes the gap to the ground-truth SFT model or only narrows it marginally.

3. **The human study has limited scope relative to the paper's strongest claims.** The study uses one task (Alpaca instruction-following), 1,000 training demonstrations, 1,000 comparisons per algorithm per round, and only 2 rounds. Moreover, the paper itself notes that "the results of ILR and DPO with the collected time-constrained human data are most similar to LM-simulated scenarios with unreliable demonstrations but reliable comparison feedback" (Section 6) — meaning the time constraints did not actually make comparison feedback unreliable for this task. The paper acknowledges this limitation, but it substantially narrows what the human study validates relative to the paper's advertised setting where *both* demonstrations and comparisons are unreliable.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing ILR with a variant that uses a single model (without cross-labeling) to directly test whether the held-out-proposal mechanism is necessary.
- Reporting which DPO β values were tested and which worked best per task, to rule out that DPO's failure is an artifact of poor hyperparameter tuning.
- Reporting GPU-hours or relative wall-clock time for ILR vs. DPO would help practitioners assess the practical trade-off.

## Removed Points
These points were raised by reviewers but are removed for the following reasons:
- *"Simulation of unreliable comparison feedback has limited ecological validity"* — The paper follows established methodology (Burns et al., 2023; Dubois et al., 2024) and validates with human annotators. This is a speculative concern about the noise model, not a concrete flaw in the paper as written.
- *"Formatting error on line 12"* — This is a PDF extraction artifact, not an author error.
- *"The 'four settings' in Figure 4 are unclear"* — The settings are reasonably inferable from context (GSM8K 7B, GSM8K 70B, BIRD, SaferPaca). The paper's description is adequate.
- *"SaferPaca GPT-4o as judge has biases"* — Using LLM-as-judge is standard practice in the field (Li et al., 2023). This is a generic concern not specific to this paper.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a table reporting exact numerical results (accuracies/win rates) for all key comparisons across tasks, models, and rounds, ideally with standard deviations from multiple random seeds.
2. Explicitly state the number of ILR rounds *K* used in LM-simulated experiments, and include a sensitivity analysis for α.
3. Add a paragraph discussing the computational cost of ILR relative to DPO, and ideally include a compute-controlled comparison (e.g., give DPO more rounds or data to match ILR's training budget).
4. Clarify implementation details: number of proposals per prompt, embedding model and threshold for SaferPaca's "sufficiently different" criterion.
5. Acknowledge more directly that the human study's time constraints did not make comparison feedback unreliable, and discuss what follow-up work would be needed to test the strongest claim with humans.

## Score and Decision
MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>