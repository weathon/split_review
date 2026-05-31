## Summary

The paper introduces Insertion Language Models (ILMs), a new generative model class that produces sequences by iteratively inserting tokens at arbitrary positions, jointly selecting both the insertion location and vocabulary item. To enable training, the authors derive a biased-but-tractable denoising objective that replaces high-variance Monte Carlo estimates of the marginalization over insertion trajectories with a normalized token-count target distribution. The model uses a single transformer encoder parameterization augmented with a dedicated stopping classifier. Empirically, ILMs achieve dramatic improvements over ARMs and MDMs on planning-oriented tasks (star graphs, zebra puzzles) and are competitive with ARMs and superior to MDMs on unconditional text generation and arbitrary-length infilling on LM1B and TinyStories.

---

## Strengths

- **Well-motivated design with strong planning results.** The failure modes of ARMs (fixed left-to-right order) and MDMs (absolute position dependence, simultaneous unmasking, fixed infilling length) are clearly articulated and directly addressed by ILM's design. The star graph experiments are striking: ILM achieves 100% / 99.1% on Star_medium / Star_hard while MDM scores 36.5% / 21% and ARM 75% / 23%. These are large, meaningful gaps that convincingly validate the core claim about relative vs. absolute position information.

- **Elegant training objective.** The key insight—replacing the true (high-variance) denoising target with normalized within-gap token counts—is simple, implementable, and well-motivated. The loss is a weighted cross-entropy with a sparse target that is easy to compute on the CPU side of the data pipeline, and training resembles MDM training with one additional step. The stopping classifier sharing the transformer backbone is neat.

- **Genuine new capability: variable-length arbitrary infilling.** Unlike MDMs, ILMs naturally handle infilling when the number of missing tokens is unknown, a limitation the paper demonstrates clearly. The infilling results (Table 3) show consistent improvements over MDMs on all three evaluation splits, providing a practical advantage.

- **Honest ablation with the Insertion Transformer (IT) baseline.** Including the original Insertion Transformer (Stern et al., 2019) as a baseline and attributing its failure to the lack of a dedicated stopping mechanism is a useful contribution that isolates ILM's design choices.

- **Text generation broadly competitive.** On Stories (NLL 2.14 vs ARM 2.11 vs MDM 2.54) and LM1B (NLL 4.67 vs MDM 4.81), ILM outperforms MDM and closely tracks ARM. The Prometheus-judge evaluations reinforce this, showing ILM's advantage in coherence and consistency.

---

## Weaknesses

### Fatal
None. The core claims are supported by the evidence.

### Major

1. **MDM baseline uses weak inference.** The MDM is evaluated with the vanilla tau-leaping sampler. Several published techniques—greedy unmasking (Gong et al., 2024), top-k unmasking (Zheng et al., 2024), and flow-based stochastic sampling (Campbell et al., 2024)—substantially improve MDM sample quality. Using unimproved MDM inference may inflate ILM's apparent advantage on text generation tasks. At minimum, results with greedy unmasking (one token per forward pass, directly analogous to ILM's one-insertion-per-step sampling) are needed to make the comparison apples-to-apples. The planning task advantage may be structural and robust to this concern, but the language modeling tables are harder to interpret as-is.

2. **Theoretical properties of the biased objective are not characterized in the main paper.** Equation 2 is explicitly a biased approximation. The key open question—whether the model trained on this objective converges to a valid generative model that samples from the true data distribution, or converges to some other distribution—is deferred to Appendix D (not available in the parsed version). At a minimum, the main paper should state clearly whether the biased objective produces a distribution that is a lower or upper bound on the true likelihood, or whether it is simply a convenient surrogate without an obvious probabilistic interpretation. Without this, it is difficult to assess the principled soundness of the method.

3. **Experiments are limited in scale.** All language modeling experiments are conducted with ~85M-parameter models on small corpora. The authors acknowledge this, but it is genuinely unclear whether ILMs close the NLL gap with ARMs (2.14 vs 2.11 on Stories, 4.67 vs 3.94 on LM1B) at scale or fall further behind. Given that MDMs have been shown to scale competitively with ARMs (Nie et al., 2024), one might expect scaling to be informative for ILMs as well. The conclusions about real-world usability remain conditional on future scaling work.

### Minor

1. **Systematic under-length generation.** The mean lengths of ILM samples (119 for Stories, 21 for LM1B) are shorter than ground truth (205, 28) and ARM samples (201, 30). This indicates the stopping classifier is biased toward early termination. Since shorter sequences tend to achieve lower NLL under an external LLM regardless of quality, this could partially artificially improve the NLL metric. Reporting NLL conditioned on samples above some length threshold would help disambiguate.

2. **Training cost not reported.** The insertion distribution target is computed on the CPU in the data pipeline, which adds preprocessing cost. Wall-clock training time comparisons across ILM, MDM, and ARM are absent, making it hard to assess whether the improvements come at a significant overhead.

3. **The entropy metric is confounded by length.** MDM's higher entropy is explicitly attributed to generating longer sequences. A length-normalized diversity measure (e.g., type-token ratio or distinct-n) would disentangle sequence diversity from sequence length artifacts.

### Trivial

- The stopping criterion is a simple binary classifier; more expressive length distributions could likely improve performance on longer text tasks.

---

## Nice-to-Haves

- Evaluation with a stronger MDM inference baseline (greedy or top-k unmasking) to make the text generation comparison fair.
- A brief characterization in the main text of the bias introduced by the approximate objective (Eq. 2) and its relationship to the true likelihood.
- Length-controlled generation experiments to verify that quality gains are not artifacts of shorter average sequence lengths.

---

## Novel Insights

The most genuinely novel insight in the paper is the observation that MDMs' reliance on absolute token positions is a fundamental architectural limitation for tasks with variable-length dependencies, not merely an inference artifact. While prior work has addressed MDM's simultaneous-unmasking problem through inference tricks, ILMs show that the correct inductive bias—relative position information via sequential insertion—requires architectural change, not just better sampling. The star graph experiments cleanly separate these concerns (MDM gets 100% on fixed-length easy graphs but collapses to 21% when arm lengths vary). The normalized within-gap count as a training target is also a practically useful approximation insight that makes the otherwise intractable insertion model trainable without appeal to complex variational machinery.

---

## Suggestions

- Add a comparison table row for MDM with greedy (one-token-per-step) sampling to make inference cost and quality comparable to ILM's sequential generation.
- Include a short analysis of the bias in Eq. 2 in the main text—even a sentence clarifying that the stationary distribution of the learned model is not guaranteed to equal p_data and what the practical implications are.
- Report per-sample length distributions alongside NLL to disentangle quality from length effects in Table 2.
- Report wall-clock training time to help readers assess the practical overhead of the CPU-side target computation.

---

## Score and Decision

The paper addresses a genuine limitation of both ARMs and MDMs with a clean, well-motivated approach. The planning experiments are highly convincing and the text generation experiments are competitive, even if the MDM comparison has some methodological concerns. The biased objective and scale limitations are real but do not invalidate the core contribution. The work is original and well-executed within its scope.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>