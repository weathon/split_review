Now I have a thorough understanding of the paper. Let me write the consolidated final review.

---

## Summary

This paper identifies that existing tool-integrated math LLMs are trained on externally dictated methodology choices (CoT vs. code) and lack the ability to autonomously decide which method to use based on their own capabilities. The authors propose an Expectation-Maximization (EM) framework that treats methodology selection as a latent variable, alternating between self-exploration (E-step) to compute a reference strategy and self-refinement (M-step) to update the model via offline RL and data synthesis. Experiments on three model families (Llama-3.1, Qwen2Math, DeepseekMath) show substantial accuracy gains (e.g., DeepseekMath-7B from 45.04% → 65.28% on MATH) while reducing code executions by up to 90% on GSM8K.

## Strengths

1. **Novel and practically important problem formulation.** The paper is the first to explicitly frame *autonomous* methodology selection — where a model learns its own strategy for when to use code vs. CoT — as a distinct research problem. The contrast with SFT-based tool integration (where methodology decisions are predetermined by annotators and do not adapt to the model's capabilities) is clearly articulated (Section 1, lines 14–18). This framing opens a meaningful line of inquiry.

2. **Strong and consistent empirical results.** Across three base model families and six benchmarks, AutoCode4Math delivers substantial absolute accuracy improvements (e.g., +20 pts on MATH for DeepseekMath, +7 pts on GSM8K). The gains are consistent across in-domain and out-of-domain benchmarks (OlympiadBench, GaokaoMath, CollegeMath), demonstrating generalization beyond the training distribution. The accuracy improvements are reported with greedy decoding, avoiding test-time computation tricks.

3. **Informative ablation studies.** The paper ablates both the EM formulation (comparing against standard RL — Table 2, Fig. 3) and the self-reflective data synthesis strategy (NO REFL variant). The standard RL baseline converges to lower accuracy with higher code usage, supporting the claim that the EM structure provides benefits beyond outcome-only optimization. The NO REFL ablation shows that multi-round self-correction data is a key ingredient.

4. **Insightful alignment analysis.** The breakdown into StrictAlign, AllowCode, and MisAlign (Section 3.3, Fig. 4) provides a fine-grained understanding of how the learned methodology-selection strategy relates to an oracle. The observation that MisAlign decisions can be compensated by improved solution-generation capability (line 206) is a genuinely nuanced finding.

5. **Practical focus and transparency about limitations.** The method requires only publicly available query sets and avoids external annotations. The paper discusses limitations (Section 4, lines 219–220), including dependence on query set quality and unexplored hyperparameters — a level of candor that aids reproducibility and frames the work as an opening rather than a definitive solution.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the theoretical EM derivation and the implemented algorithm is not clearly delineated.** The paper derives an ELBO and states a monotonic improvement guarantee (lines 64–86), then replaces the E-step with Monte Carlo estimation plus a heuristic energy-based distribution (Eq. 10 with α=∞, i.e., hard-max selection) and the M-step with an off-policy RL objective (Eq. 11) with importance-sampling clipping and separate data synthesis. The paper acknowledges the practical challenges (lines 93–95) but does not clearly separate the idealized EM from the implemented variant or explain how the theoretical guarantees are (or are not) preserved. This discrepancy weakens the "principled EM framework" narrative — the method is better described as *EM-inspired iterative self-training with oracle-guided data synthesis and offline RL*. Readers expecting standard EM properties to transfer will be misled.

2. **The "autonomy gap" motivating the work is somewhat overstated.** The paper claims existing models "rely on externally dictated instructions" and "lack the autonomy to choose the most appropriate method independently" (Abstract, line 4). However, models like ToRA and DotaMath are trained on mixed CoT/code data and, during inference, implicitly decide which to generate based on context — they are not externally constrained. The real limitation is more nuanced: SFT training does not teach the model to *explore and adapt* its methodology selection to its own capabilities. The paper should acknowledge this subtlety rather than implying existing models are purely reactive. The contribution is still meaningful, but the framing is stronger than the evidence supports.

### Minor

1. **The behavior policy ξ is never specified.** Equation 11 and line 147 define an off-policy correction term Clip(p_θ/ξ, 0.8, 1.2) but do not state what ξ is — whether it is a frozen checkpoint, the data-generation policy, or some other distribution. The clipping bounds are borrowed from PPO without justification for the off-policy setting. This makes the RL component non-reproducible as described.

2. **The "Code-Driven" baseline in Table 1 is not defined in the main text.** The paper mentions "code-driven inference" only in the table caption (line 165). If this means the base model forced to use code for every query, it is an extremely weak baseline — any model that sometimes chooses CoT will trivially show reduced code usage. The paper should define this baseline explicitly and, more importantly, report code execution rates for the autonomous baselines (ToRA, DotaMath) to substantiate the efficiency claim.

3. **The standard RL ablation is underspecified.** The paper states it uses "an off-policy RL approach for computational parity" (line 178) but does not specify hyperparameters, number of rollouts, data usage, or tuning procedure. This makes it difficult to assess whether the comparison is fair or whether the standard RL baseline was adequately tuned.

4. **The "nearly 20%" improvement phrasing is ambiguous.** The abstract and introduction say "raising accuracy by nearly 20% to 65.28%." From a base of 45.04%, this is ~20 percentage points (~45% relative improvement). The phrasing could mislead readers into thinking it is a 20% relative improvement. Clarifying this (percentage points vs. relative) would improve precision.

### Trivial

- The discussion of monotonic improvement (line 86) is explicitly tied to "the evidence lower bound (ELBO) objective," but the surrounding text ("indicating a guaranteed progression toward better performance as the model iterates through the EM steps") could be read as applying to the practical algorithm. A brief caveat would resolve this.
- The notation `\bar{c}` in the clipping term (line 149) is likely a LaTeX/parser artifact and should be uniform.
- Figure 3 (training curves for the RL ablation) is referenced in text but appears only as an image; the extracted text contains garbled fragments around it (lines 188–189).

## Nice-to-Haves

- Report code execution rates for ToRA, DotaMath, and AlphaMath to ground the efficiency claim.
- Provide a version of the alignment analysis where the oracle prefers code over CoT when both succeed, to test sensitivity.
- Show accuracy and code rate as a function of EM iterations to illustrate convergence behavior.
- Discuss why the standard RL baseline converges to a suboptimal solution — is it a local optimum, insufficient exploration, or something else? The conjecture about policy search space narrowing is plausible but untested.

## Removed Points

- **Criticism about the "autonomy gap" not existing at all (Issue 1 from Harsh Critic):** The critic claims models like ToRA/DotaMath already have autonomy because they generate both CoT and code. However, the paper's core claim is about the *training paradigm* — these models are trained on data where methodology decisions are predetermined by annotators, not discovered through self-exploration. The paper's gap identification is valid, even if the framing could be more precise. The removed criticism overstates the issue.

- **Criticism about the 20% improvement being deliberately misleading:** The paper says "nearly 20%" and gives the absolute numbers (45.04% → 65.28%) in the same sentence, making the meaning clear in context. This is standard ML conference phrasing.

- **Criticism about Fig. 1 showing a query with explicit instructions (training format, not inference requirement):** The paper's Fig. 1 caption (line 27) explicitly states "Prior models are usually trained on queries with explicit instructions (Top Left)" — the paper acknowledges this is a training data format. The critic's point here is based on a misreading.

- **Criticism about missing appendix/proofs:** The parser strips such content; it exists in the original submission.

- **Criticism about the macron on c being a typo:** This is a parser artifact from LaTeX extraction, not an author error.

- **Pure formatting/style nitpicks:** Removed per instructions.

## Novel Insights

The most interesting finding in the paper is the MisAlign analysis (Section 3.3): a significant proportion of AutoCode's correct responses fall into the MisAlign category (where the model's choice diverges from the oracle), yet the model still achieves high accuracy. The paper astutely observes that a "wrong" methodology choice can be compensated by improved solution-generation capability for that choice. This suggests that optimizing methodology selection and solution generation jointly (as the EM framework does) creates a feedback loop where even suboptimal methodology choices can be rescued — a dynamic that standard RL (which only optimizes outcome) misses. This is a genuinely non-obvious insight that goes beyond the paper's main empirical results and could inform future work on learned decision-making in LLMs.

## Suggestions

1. **Rebalance the framing.** Acknowledge more explicitly that existing models *can* interleave CoT and code autonomously during inference; the real gap is that SFT training does not let them *discover* an optimal strategy adapted to their own capabilities. This would strengthen rather than weaken the contribution.

2. **Clearly separate the idealized EM from the practical algorithm.** Add a short paragraph or table contrasting the theoretical ELBO update with the implemented approximations (MC estimation + hard-max selection + off-policy RL). State explicitly which properties (e.g., monotonic improvement) are preserved and which are not.

3. **Specify the behavior policy ξ.** Even a brief sentence — "ξ(yₐ|x_q,c) is the policy used to collect the training data (a frozen copy of the model from the previous EM iteration)" — would resolve the reproducibility issue.

4. **Define the "Code-Driven" baseline explicitly and report code rates for baselines.** Add a sentence defining this baseline and, if possible, report the proportion of code usage for ToRA/DotaMath on the same test sets.

5. **Add more detail to the standard RL ablation.** Specify the algorithm, number of rollouts, reward whitening, learning rate, and data usage. This would significantly strengthen confidence in the controlled comparison.

## Score and Decision

The paper makes a genuine contribution: it identifies an important gap, proposes a practically effective solution backed by strong empirical results across multiple model families and benchmarks, and provides informative ablations and analysis. The weaknesses are real but addressable — the EM-to-algorithm gap is a framing issue more than a methodological flaw, and the underspecified details (behavior policy, Code-Driven baseline) are fixable in a camera-ready revision. No fatal flaw undermines the core claims.

**Score: 6.5**

**Decision: Accept**

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>