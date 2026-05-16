Now I have a thorough understanding of the paper. Let me synthesize the final review after carefully verifying each claim against the actual paper text.

## Summary

This paper presents an extensive empirical benchmark of how language models internally represent mental states (beliefs of self and others). Extending prior work by Zhu et al. (2024), the authors probe 14 model variants across Pythia (70M–12B) and Llama-2 (7B–70B), studying the effects of model size, fine-tuning, prompt variations, potential probe memorisation, and activation steering via CAA. The key findings are that (1) probing accuracy for others' beliefs increases with model size and more so with fine-tuning, (2) prompt variations systematically affect representations, (3) probes do not appear to memorise, and (4) CAA improves ToM reasoning without needing trained probes.

## Strengths

- **Extensive multi-family, multi-size benchmark across conditions not covered by prior work.** The paper probes 14 model variants spanning Pythia (70M–12B) and Llama-2 (7B–70B), including base and fine-tuned versions, whereas prior work (Zhu et al., 2024) used only two 7B chat models. *Evidence: Section 3.3 (Models) and Figure 2 show consistent comparisons across architectures, sizes, and fine-tuning status.*

- **First systematic study of prompt variation effects on internal belief representations.** The paper defines four principled prompt variants (Random, Misleading, Time Specification, Initial Belief) and demonstrates that probes are sensitive to all of them, including the unexpected null finding that Time Specification fails to improve accuracy. *Evidence: Section 3.4 and Figure 3 show accuracy drops for Random and Misleading, and no benefit for Time Specification across both model families.*

- **CAA improves ToM reasoning without any trained probe and generalises across tasks.** CAA yields accuracy gains of up to +56 points (absolute) on the hardest task (Backward Belief) and consistently outperforms both no-intervention and ITI baselines across Forward Belief, Forward Action, and Backward Belief tasks, using steering vectors computed only from Forward Belief. *Evidence: Section 4.4 (Table 1) shows CAA improvements for all models and tasks with transfer to unseen task types.*

- **No strong evidence of probe memorisation despite high-dimensional representations.** Training probes on only the first 2–100 principal components recovers most of the original accuracy; for Llama-2-7B, 100 PCs (2.4% of the full 4096 dimensions) retain ~80% of accuracy. *Evidence: Section 4.3 and Figure 4 show accuracy with few PCs nearly matches full-representation accuracy across all model sizes.*

- **Fine-tuning dramatically improves probing accuracy for smaller models.** Llama-2-7B-chat improves ~29% over its base version, and Pythia-6.9B-chat improves ~26%; fine-tuned 7B models match or exceed twice-as-large base models. *Evidence: Section 4.1, Figure 2, and explicit accuracy improvements reported in text.*

## Weaknesses

### Fatal
None.

### Major

- **Over-interpretation of scaling-law fits with too few data points.** Lines 265–267 report logarithmic fits (R² = 0.98 for Llama-2 base, R² = 0.96 for Pythia base) and a linear fit (R = 1.0 for Llama-2 chat) using only 3 data points for the Llama-2 curves (7B, 13B, 70B) and 5 for Pythia. A two-parameter fit to 3 points will nearly always yield high R² regardless of the underlying relationship, making the R² values uninformative. The qualitative trend (accuracy increases with size) is well-supported by the raw plots and does not need parametric fits. The authors should remove the fitted curves and R² values or present them with explicit caveats about the tiny sample size.

### Minor

- **CAA vs. ITI comparison lacks reported variance.** Section 4.4 and Table 1 report that CAA outperforms ITI, but the paper does not provide confidence intervals, standard deviations over multiple runs, or a detailed description of whether ITI hyperparameters were tuned with the same thoroughness as CAA. While this does not undermine the core contribution (CAA works without probes), it weakens the comparative claim. *Note: the paper does reference Appendix CAA for hyperparameter details (which was stripped by the parser).*

- **Only one fine-tuned Pythia model is used (6.9B-chat).** The conclusion that "fine-tuning helps" is strongly supported by the Llama-2 family (three chat variants across sizes) but rests on a single data point for Pythia. This asymmetry should be explicitly acknowledged in the discussion of the fine-tuning results in Section 4.1.

- **No explicit discussion of why Time Specification does not help.** The paper reports the intriguing negative finding that specifying the belief refers to the story's end does not improve probing accuracy (Section 4.2, line 277), but does not discuss possible explanations. A brief discussion would strengthen the analysis.

- **Dataset statistics and train/test split proportions are not reported.** The paper does not state how many examples are in the probing datasets (D_p^P and D_o^P) or the train/test split proportions, which affects interpretability of the probing accuracy numbers.

- **Number of runs/seeds for probing is not specified.** It is unclear whether probes are trained once or with multiple random initializations / data splits. Reporting this would improve reproducibility.

### Trivial

- The paper refers to "up to +56" for CAA improvements without explicitly stating these are absolute percentage points (they are, from context, but a brief clarification would help).

## Nice-to-Haves

- The PCA memorisation check (Section 4.3) could be complemented by also reporting training-vs-test accuracy gaps or performance on shuffled labels, which are additional standard checks for probe memorisation.
- A brief note in Section 4.1 acknowledging that the PCA results (Section 4.3) confirm the size-accuracy trends hold even after dimensionality reduction would strengthen the claims about representations versus parameter count.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Time Specification variation is described only vaguely"* — **Removed.** The paper describes this variation clearly at lines 206–210 with a concrete example, and states that exact prompt templates are in the appendix (which was parsed out). The description is sufficient for a main text.
- *"The PCA experiment does not rule out memorisation by the probe in the original space"* — **Downgraded to nice-to-have.** The PCA approach is a standard and accepted method for this check. The paper's claim ("no strong evidence") is appropriately cautious. The suggestion of additional checks is a strengthening suggestion, not a weakness.
- *Criticisms about missing appendix content (prompt templates, hyperparameter details)* — **Removed per hard rule.** The parser strips these sections; they exist in the original submission.

## Novel Insights

The key novel insight beyond the paper's own contributions is the asymmetric finding about prompt variations: providing the *Initial Belief* helps, but the *Time Specification* — which should theoretically disambiguate beliefs across time frames — unexpectedly does not improve probing accuracy. This negative result is worth highlighting as it suggests current LMs may not effectively integrate temporal cues into their belief representations, opening a specific direction for future work.

## Suggestions

1. **Remove or heavily caveat the scaling-law curve fits** (lines 265–267). Report qualitative trends ("accuracy increases with size") without R² values on 3-point curves.
2. **Add explicit caveats about the single Pythia fine-tuned data point** when discussing fine-tuning benefits.
3. **Report variance estimates** for the CAA/ITI comparison table (even if just over 3 runs) and clarify hyperparameter tuning parity between methods in the appendix.
4. **Add a brief discussion** of why Time Specification does not help in Section 4.2.
5. **Include dataset statistics** (number of examples, train/test split) in the main text or a table.

## Score and Decision

The paper is a well-executed, thorough empirical benchmark that makes a solid contribution. The core findings (size and fine-tuning matter, prompt sensitivity, no memorisation, CAA works without probes) are well-supported. The scaling-fit over-interpretation is the most significant weakness but is easily fixable and does not threaten the main claims. No structural or fatal issues exist.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>