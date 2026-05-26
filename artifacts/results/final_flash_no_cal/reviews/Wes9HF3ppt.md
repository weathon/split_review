Now I have all the information needed to write the consolidated review.

## Summary

The paper introduces Insertion Language Models (ILMs), a new approach for sequence generation where tokens are inserted one at a time at arbitrary positions, breaking both the left-to-right lock of autoregressive models (ARMs) and the fixed-length masked constraint of masked diffusion models (MDMs). To enable training, the authors propose a denoising objective with a count-based target distribution and a transformer parameterization with a dedicated stopping classifier. Experiments on planning tasks (star graphs, zebra puzzles) show ILMs dramatically outperform both ARMs and MDMs, while on text generation and infilling tasks ILMs are competitive with ARMs and exceed MDMs.

## Strengths

1. **Clear demonstration of ILM's core advantage on planning tasks requiring out-of-order and variable-length generation.** Table 1 provides compelling evidence: on Star_medium (variable arm length), ILM achieves 100.0% accuracy vs. MDM's 36.5% and ARM's 75.0%; on Star_hard, ILM achieves 99.1% vs. MDM's 21.0% and ARM's 23.0%. These results directly validate the paper's thesis that the insertion formulation overcomes specific failure modes of both ARMs (fixed left-to-right order) and MDMs (fixed-length masks and absolute-position assumptions).

2. **Successful arbitrary-length infilling that outperforms MDMs.** The paper's claimed advantage for infilling is borne out by Table 3: on LM1B single-segment infilling, ILM achieves ΔNLL_gt of +20.47% vs. MDM's +25.31%, and on multi-segment infilling the gap persists (+23.52% vs. +25.64%). This demonstrates that ILM's ability to generate without knowing the infill length in advance translates to measurable quality gains.

3. **Pragmatic solution to the high-variance training problem.** The paper identifies that a naive denoising objective for insertion models suffers from extreme variance (Appendix D), and proposes the count-based normalized target distribution (Equation 2) as a tractable approximation. The strong empirical results across all tasks demonstrate this is a viable and effective mechanism.

4. **Diagnostic experimental design.** The three variants of the star graph task (easy/medium/hard) are well-chosen to isolate the specific failure modes of ARMs (reverse dependencies) and MDMs (variable arm lengths). The zebra puzzle results (ILM 90.0% vs. MDM 82.6% and ARM 81.2%) provide complementary evidence on a different structured task.

5. **Honest efficiency analysis.** Figure 6 provides a useful per-token time vs. quality (NLL) comparison, showing the practical trade-off: ILM is slower than ARM with KV caching but can achieve better quality than MDM at a comparable time budget.

## Weaknesses

### Fatal
None.

### Major

1. **Length bias confounds the unconditional text generation evaluation.** ILM generates sequences substantially shorter than the data average (Stories: 119 tokens vs. data avg. 205; LM1B: 21 vs. 28), while MDM produces much longer sequences (Stories: 985; LM1B: 85) and ARM matches the data length (201; 30). Per-token NLL under Llama and Prometheus scores are both sensitive to length — shorter sequences tend to have lower NLL because early tokens are easier to predict, and LLM judges may be more forgiving of concise outputs. The paper acknowledges the length disparity only to explain MDM's high entropy ("We found that to be the main reason for the high entropy") but never discusses whether ILM's shorter sequences inflate its NLL or Prometheus scores. The claim that ILM "performs on par with ARMs and better than MDMs in unconditional text generation" (abstract) is therefore not properly supported — the metric advantage could partially reflect a systematic length shift rather than genuine quality. This is the most significant weakness in the paper's empirical case. (Evidence: Table 2 shows average lengths; no length-controlled analysis is provided.)

### Minor

2. **The infilling evaluation protocol for MDM is underspecified.** The paper compares ILM and MDM on infilling (Table 3) but does not explain how MDM is adapted for this task when the number of tokens to fill is unknown. If the number of missing tokens is oracle-provided (as it would be in a controlled evaluation where segments are removed), MDM receives an exact-length signal — an advantage ILM does not have — yet ILM still outperforms it, which would strengthen the case for ILM. If MDM must guess the length, the paper should state how. The omission makes the infilling comparison difficult to interpret. (Evidence: Section 5.3.2 describes the dataset construction but not the MDM adaptation procedure.)

3. **No error bars, confidence intervals, or multiple-seed results are reported.** None of the main results (Tables 1–3, Figure 5) report standard deviations or statistics over multiple runs. Given the relatively small model sizes and training budgets, variation across seeds could be nontrivial, especially for the star-graph tasks with small synthetic datasets and the text experiments with modest compute. This limits the reader's ability to assess the reliability of the reported numbers. (Evidence: Section 5 reports single runs; no mention of multiple seeds or variance.)

4. **The biased training objective is acknowledged but its effects are not analyzed.** The paper states that the count-based loss (Eq. 2) is "a biased training objective" (Section 3) and notes that the naïve marginalization would have high variance. However, it provides no analysis of what the bias implies for generation quality — for instance, dependencies among multiple tokens inserted into the same gap are lost in the aggregation, and the model never sees a sequential filling process during training. It would strengthen the paper to test whether an unbiased (but higher-variance) sequential loss yields different behavior, or to discuss scenarios where the aggregation bias might cause failures (e.g., strongly correlated tokens within a gap). (Evidence: Section 3 states the objective is biased but provides no analysis of the bias.)

5. **Architecture and hyperparameter confound between ILM and MDM.** ILM and ARM use a RoPE-based transformer, while MDM uses DDiT (RoPE + AdaLN), which has slightly more trainable parameters. All models are trained with the same learning rate (1e-4), constant schedule, and same number of steps, without tuning the MDM-specific hyperparameters (e.g., noise schedule, step size). While the paper acknowledges the architectural difference, the confound makes it unclear how much of MDM's weaker performance is due to suboptimal configuration rather than an inherent limitation of masked diffusion. (Evidence: Section 5 notes the architectures differ and MDM has more parameters; same LR and steps used for all models.)

### Trivial

6. **Insertion Transformer is only evaluated on star graphs, not on zebra puzzles or text tasks.** The comparison with this baseline is therefore limited in scope. (Evidence: Table 1 shows IT results only on star graphs; no IT results in Tables 2 or 3.)

## Nice-to-Haves

- **Length-controlled analysis**: Binning unconditional generations by length and reporting per-bin NLL / Prometheus scores would directly address the length bias concern and either confirm or refute whether ILM's quality advantage is genuine.
- **Quantitative analysis of generation trajectories**: The paper mentions that ILM "tends to start the generation from both ends" (Appendix C.0.3). This qualitative observation could be quantified (e.g., statistics of insertion order on held-out data) to directly support the claim about out-of-order generation.
- **Actual model perplexity on held-out data** (rather than only NLL under an external LLM) would provide a more direct measure of how well each model fits the training distribution.
- **Ablation of the training objective**: Comparing the proposed count-based loss to a simpler loss that treats missing tokens independently (e.g., randomly sampling one gap and one token to predict) would help isolate the benefit of the aggregation heuristics.

## Removed Points

These points from the reviewers are flagged for removal based on the filtering rules; they are listed here for completeness but should not be considered weaknesses.

- **Claim that MDM "likely uses absolute positions" (for position encoding).** The paper states that DDiT inserts AdaLN "in the RoPE based transformer" (Section 5), meaning the MDM architecture also uses relative position encoding (RoPE). The critic's specific claim about absolute position encoding is factually incorrect. The broader concern about architectural differences is retained (Minor #5).
- **Request for details of Algorithm 2 (inference loop).** Algorithm 2 is in the appendix, which is stripped by the paper parser. The body text describes the two-step sampling procedure (Section 3). This is a parser artifact, not an author omission.
- **"Show per-token time vs. NLL curve for ARM with varying compute."** The ARM is a single-pass model; varying its compute in a comparable way is not standard or meaningful. This is not a genuine weakness.
- **"The description of the stop classifier is vague."** The paper explains it is a binary classifier trained with cross-entropy loss, using the output of a special `<stp>` token (Section 3.1). This level of detail is standard for a conference paper.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation to emerge from the reviews is the contrast between the clean, near-perfect results on planning tasks (where ILM's insertion mechanism is clearly decisive) and the more ambiguous text generation results (where the length confound introduces uncertainty). This suggests that the strongest argument for ILMs is not simply that they generate better text, but that they enable *structured* generation in settings where the generation order matters — a finding that aligns with the paper's thesis but is better supported by the star-graph and zebra-puzzle experiments than by the text metrics. The reviews also highlight that the field lacks standardized methodology for evaluating variable-length non-autoregressive generation, which the length-bias issue underscores.

## Suggestions

1. **(Required for strengthening the paper)** Address the length confound directly: analyze unconditional generation quality conditional on length (e.g., bin by length, or match the length distribution of the ARM), and discuss whether the stop classifier can be calibrated to match the data length distribution. Without this, the text-generation claims remain uncertain.
2. **(Required for completeness)** Clarify how MDM is adapted for the infilling evaluation in Section 5.3.2 — specifically, whether the number of masks is oracle-provided or estimated, and how the total sequence length is determined.
3. **(Recommended)** Add a brief analysis of the training objective's bias: either provide an ablation comparing the count-based loss to a simpler variant, or discuss specific scenarios where the aggregation might harm fidelity.
4. **(Recommended)** Report standard deviations or error bars for the main quantitative results (at least for Tables 1 and 2), or at minimum note that results are from a single run and discuss potential variability.
5. **(Minor)** Extend the Insertion Transformer comparison to at least the zebra puzzle task for completeness.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>