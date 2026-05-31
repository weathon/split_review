Now let me do the calibration search across score bands.Now I have enough information to write the consolidated review.

---

## Summary

SteadyThought (ST) proposes a three-stage preference optimization framework to address "under-thinking" in Large Reasoning Models (LRMs) — the phenomenon where models abandon promising reasoning trajectories in favor of excessive thought-switching. The pipeline segments model responses into thoughts via entropy-based detection, completes each thought without switching using logit suppression to generate "chosen" training responses, and then applies a new thought-level preference optimization objective (STPO, derived from SimPO) conditioned on a shared promising-thought prefix. Experiments across three model sizes and four benchmarks (including an OOD code generation task) show consistent accuracy improvements (+1.9% to +3.12%) and token reductions (17–25%).

---

## Strengths

1. **Consistent accuracy gains and token reduction across diverse models and benchmarks**: Table 1 reports ST improves overall accuracy by +1.9%, +3.12%, and +2.52% across DeepSeek-R1-Distill-Qwen-1.5B, Qwen3-8B, and DeepSeek-R1-Distill-Qwen-14B, while simultaneously reducing token counts by 17–25%. The gains hold on the OOD LiveCode dataset (+5.3% accuracy for Qwen3-8B with 19.0% fewer tokens), providing evidence of genuine generalization rather than dataset memorization.

2. **Well-motivated formal problem framing**: Section 2.1 formalizes under-thinking as a preference optimization problem over a "commit trajectory" vs. "switch trajectory" using the Bradley-Terry model (Equation 2). This principled framing motivates the entire pipeline in a clean, mathematically coherent way, distinguishing the paper from ad hoc suppression heuristics.

3. **STPO objective is technically sound and validated**: The STPO loss (Equation 7) conditions on the shared promising-thought prefix and uses length-normalized rewards (inherited from SimPO) to avoid length bias. Table 4 confirms STPO outperforms both SFT (which memorizes rather than generalizes) and standard DPO (which fails to reduce tokens due to length-bias sensitivity), with AIME2024 accuracy of 31.2% vs. 22.9%/30.8%, validating the design choices.

4. **Behavioral evidence of reduced under-thinking**: Figure 2 and Table 2 show reduced average thoughts, a larger proportion of the final thought in total response length, and decreased proportion of correct intermediate thoughts (PCT) — e.g., from 54.90% to 40.40% on MATH500 for the 1.5B model — directly corroborating the paper's claims about more purposeful thought commitment.

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained inconsistency in AIME2024 behavioral pattern for the 1.5B model** — For DeepSeek-R1-Distill-Qwen-1.5B on AIME2024, Figure 2 shows the *number of thoughts increases* from 12.87 to 18.21 post-ST training, while response length decreases and accuracy improves. The paper's explanation (Section 4.4.1): *"when smaller models tackle high-difficulty problems, they tend to increase the frequency of thought transitions"* is post-hoc and does not follow from the proposed mechanism (commitment to promising thoughts should reduce switching). Additionally, the proportion of the last thought *decreases* (18.96% → 15.66%), also contradicting the general mechanism. The paper does not analyze why ST produces qualitatively different behavior on this one model/dataset combination. This is the most substantive gap: the mechanism is not uniformly supported by the data reported in the paper.

### Minor

- **PCT metric is partly circular** — Section 4.4.2 uses the same segmentation method (Section 3.1) and completion method (Section 3.2) to measure "proportion of correct thoughts" (PCT) after training. Since training changes how the model generates responses, and the segmentation depends on token-level entropy from the model, the measurement tool and the trained system are partially coupled. Changes in PCT post-training may partly reflect changes in how the model's outputs interact with the entropy-based segmenter, not purely changes in reasoning behavior. An independent measurement (e.g., human annotation on a subset) would strengthen this analysis.

- **Trigger word list not fully specified** — Section 3.2 gives "wait" and "alternatively" as examples but states these are a set of *predefined trigger words* without providing the complete list. Since Qwen3-8B differs architecturally from the DeepSeek-R1 distillations, it's unclear whether the same trigger word vocabulary applies across models. This is a reproducibility gap for the thought completion stage.

### Trivial
None beyond the above.

---

## Nice-to-Haves

- A trajectory-level analysis showing what the ST-trained model does when the base model would switch away from a correct thought (i.e., directly testing whether ST has learned selective commitment vs. mere output compression) would significantly strengthen the mechanistic claims.
- A comparison of NOWAIT or SEAL applied to a model that *also* underwent fine-tuning on the same omni-math data (without STPO construction) would isolate STPO's specific contribution from the general benefit of fine-tuning on olympiad-level math. Currently Table 4 ablates SFT and DPO but not inference-time methods applied to fine-tuned models.
- The entropy threshold tuning analysis (Table 3) covers only three values for one model. A brief note on whether the threshold of 3.0 generalizes to other model families, or what the search looked like for Qwen3-8B, would add confidence to the design.
- The striking failure of NOWAIT on Qwen3-8B (token count increases from 4724 to 13274 in Table 1) is reported but not discussed. This is informative about the fragility of inference-time logit suppression for models outside its design envelope and deserves a sentence.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Conflation of training-time and inference-time comparison is "unfair"** — Under the hard rule, comparisons where the asymmetry favors the baseline (NOWAIT/SEAL require no training, are computationally cheaper) rather than the author's method are to be removed. The asymmetry here is that NOWAIT and SEAL are parameter-free inference-time methods, which is an advantage for them, and ST still outperforms. This does not constitute an unfair comparison.

- **Harsh Critic: Thought Completion stage uses the same suppression mechanism as NOWAIT** — While technically accurate (Section 3.2 does suppress trigger-word logits), this describes the *data generation* step, not the trained policy. The selectivity in the trained model comes from STPO, which pairs suppressed-completion responses as "chosen" only when they produce correct answers and pairs them against the wasteful continuation as "rejected." The critic acknowledges this is not fatal; it's more a presentation issue. Since the paper does clearly state the mechanism of Stage 2 ("sharply decrease the logits for these words"), and the subsequent preference optimization step is what differentiates ST from pure NOWAIT, this is at most a minor framing issue — not a conceptual error. This is demoted to a presentation nitpick but is already captured in the suggestion to clarify the mechanism.

- **Strength Finder: Problem importance / interesting question** — Generic. Not retained.

- **Harsh Critic: Missing training dataset size / number of successful completions** — Valid reproducibility concern but falls under "trivial implementation details" per the soft rules. The paper states it uses the omni-math dataset sampled at various difficulty levels (Section 4.1); the exact counts presumably appear in stripped appendix material.

---

## Novel Insights

The most genuinely novel aspect of SteadyThought is that it reframes "under-thinking" not as a decoding-time suppression problem but as a preference mismatch problem — one that can be addressed through fine-grained, prefix-conditional preference optimization at the *thought* level rather than the response level. The construction of preference pairs conditioned on a shared promising-thought prefix (Equation 7) is a concrete methodological contribution: it provides a learning signal at precisely the divergence point (where the model abandons a valid trajectory) rather than over the whole response. The demonstration that this approach transfers to OOD code generation despite math-only training suggests that the model is learning a structural reasoning property, not a domain-specific heuristic — a claim that would merit direct verification through trajectory-level analysis in future work.

---

## Suggestions

1. Provide a full list of trigger words used in the thought completion stage and indicate whether they differ by model family.
2. Add a trajectory-level case study for the AIME2024 1.5B scenario: examine a set of problems where ST produces *more* thoughts than the base model and explain what qualitative behavior produces shorter responses with more thoughts (e.g., shorter individual thoughts? faster convergence within each?).
3. Add one or two sentences discussing the Qwen3-8B NOWAIT failure (3× token expansion) to contextualize why inference-time suppression is fragile for this model architecture.
4. In Section 4.4.2, add a brief caveat acknowledging that PCT is measured using the same segmentation tools that generate training data; note the limitation and invite future independent validation.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| jRZ1ZeenZ6 (Rational Metareasoning) | 5.00 | R1 | Trains LLMs to selectively use reasoning steps; similar goal but simpler method and narrower evaluation than ST |
| bGGMLWAGMc (IUPO) | 5.50 | R1/R2 | Iterative DPO for reasoning improvement; comparable improvement margins (~3.6%) but no OOD evaluation and less differentiated from standard DPO |
| VNckp7JEHn (Inference Scaling Laws) | 5.75 | R1 | Empirical scaling study; different type of contribution |
| 9Hxdixed7p (3D-Properties of DPO) | 6.25 | R2 | Analytical + empirical DPO paper; stronger theoretical grounding but comparable experimental scope |
| MoJSnVZ59d (SafeDPO) | 6.40 | R2 | DPO variant with one additional hyperparameter; narrower contribution than ST's three-stage pipeline |
| trKee5pIFv (RainbowPO) | 6.00 | R2 | Unified DPO framework with comprehensive ablations; broader but less targeted than ST |

**Round 1 bracket: 5.0 – 7.0.**

**Round 2 narrowing:** ST is better than IUPO (5.5, Reject) — it has OOD generalization, a more principled three-stage pipeline, and clearer behavioral evidence. It is comparable to RainbowPO (6.0, Accept) in empirical depth and to 3D-Properties (6.25, Accept) in methodological contribution, though without the theoretical grounding. The major weakness (inconsistent behavioral pattern for 1.5B on AIME2024 being unexplained) is real but does not undermine the core empirical contribution. Overall, the paper sits just above IUPO and roughly at the level of RainbowPO/3D-Properties. I place it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>