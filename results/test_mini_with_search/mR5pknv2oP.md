Now I have all the calibration data I need. Let me write the final consolidated review.

## Round-1 Bracket

I searched three bands (0-3, 4-7, 8+) and read multiple anchors. The paper clearly sits in the 4-6 range — much stronger than the 2.5-3.0 papers (which are rejected for incompleteness or lack of novelty) and clearly weaker than 8+ papers (which have thorough evaluation). **Initial bracket: 4.0 – 6.0.**

## Round-2 Narrowing

I searched within [3.5, 5.5] and [4.5, 6.5] and read more anchors. OpenSIR (4.0) has more thorough evaluation but less striking results. "LLMs as Improvement Operators" (4.5) has a similar evaluation scope weakness. RePro (6.0) has thorough experiments, baselines, and ablations. SECToR falls between OpenSIR (4.0) and RePro (6.0) — its central result is more dramatic and its idea is cleaner, but its evaluation is thinner. **Narrowed bracket: 4.5 – 5.5.**

Comparing SECToR to OpenSIR (4.0): SECToR has a stronger central result (6→30 digits, 22 steps) but weaker evaluation (single run, no baselines). Comparing to "LLMs as Improvement Operators" (4.5): similar evaluation gaps. SECToR sits at the upper end of this band due to the clean, well-motivated idea and the impressive demonstration. **Final score: 5.0.**

Now here is the full review.

---

## Summary

SECToR proposes using chain-of-thought reasoning as a "policy improvement operator" for language models: a model generates step-by-step solutions for problems beyond its direct capability, fine-tunes itself on those solutions *without* CoT, and repeats. On addition, a 582M ByT5 model trained only on ≤6-digit examples reaches 98–100% accuracy on 1–29 digit addition and 88% on 30-digit addition through 22 self-training rounds. This is a novel proof-of-concept for multi-step self-improvement in language models.

## Strengths

1. **Demonstration of sustained multi-step self-improvement without external feedback.** The paper reports that a 582M ByT5 model underwent 22 rounds of self-training and reached 98–100% accuracy on 1–29 digit addition (Table 1). This cleanly exceeds prior self-training attempts that degrade after only a few steps (cited in Related Work: STaR, Impossible Distillation, etc.). The result is striking: the model bootstraps from ≤6-digit supervised data to 30-digit addition using only self-generated training data.

2. **Empirical evidence that chain-of-thought reasoning generalizes to unseen digit lengths.** Figure 2 (supervised generalization) shows that CoT-augmented addition achieves near-perfect length generalization to N+1 digits after training on N digits, while direct (fast) addition fails. This property is the mechanism that enables the self-training loop, and the paper documents it clearly.

3. **Controlled experimental setup isolating the self-training effect.** The supervised phase provides only ≤6-digit examples. All subsequent training data is model-generated with zero access to ground truth (Section 4, Figure 1). The final accuracy on 30-digit numbers is cleanly attributable to self-training, not to seen data. This is a well-scoped design for the paper's stated goal.

4. **Quantitative documentation of the error-reduction mechanism.** Figure 4 shows that Simplify-and-Guess (ST&G) decoding with K=5 and commutativity checks substantially reduces the error rate in generated training data compared to direct sampling. The paper identifies and attempts to address the error avalanching problem that plagues prior self-training methods.

## Weaknesses

### Major

1. **Single training run with no variance reported.** The paper states explicitly: "We report the results for a single training run" (line 251). All accuracy numbers in Table 1 come from this one run. Self-training loops are inherently high-variance — the quality of early generated data strongly influences subsequent iterations. Without multiple seeds (3–5 independent runs), the reader cannot assess whether the reported success is robust or a lucky draw. This is the single most important evidential gap.

2. **No meaningful baselines.** The paper compares against no alternative method in the same experimental setup. Several obvious questions go unanswered: (a) What accuracy would the model achieve if it were simply supervised on CoT-generated data without the iterative self-training loop (one-shot distillation of CoT into direct)? (b) What if the supervised curriculum were extended directly to 7–10 digits? (c) Does SECToR outperform a model using scratchpad decoding (Nye et al., 2021) for the same training data? Even a simple comparison would help attribute the observed improvement to SECToR specifically rather than to factors like the ByT5 tokenization or the particular supervised pretraining setup.

3. **Consistency checks are not ablated on the downstream metric.** Figure 4 shows that ST&G and commutativity checks reduce the error rate of *generated training data*, which is a proxy metric. The paper never shows what happens to the *final model accuracy* (Table 1) when these components are removed. It is possible that the main driver of success is something else (e.g., the curriculum schedule, the choice of K=5, or the model size) and the consistency checks are helpful but not essential. The paper's claim that these checks are "essential for mitigating error avalanching" is not directly supported by evidence of what the downstream model would achieve without them.

### Minor

1. **No analysis of error accumulation across the 22 steps.** The paper attributes eventual termination of self-training to accumulated errors but shows no data on how error rates in generated training data evolved per iteration. Plotting the accuracy of generated examples against iteration number would strengthen the causal story about error avalanching and termination.

2. **No quantification of computational cost.** The paper notes in the Discussion that SECToR is "highly compute inefficient" but does not report GPU-hours, number of forward passes per iteration, or total training cost. This would help calibrate the practical significance of the results.

3. **The "policy improvement operator" analogy is conceptual, not formally validated.** The paper draws a direct analogy between CoT reasoning and MCTS in AlphaZero but does not show that CoT satisfies any formal properties of a policy improvement operator (e.g., guaranteed improvement at each step). The paper acknowledges this in the Discussion but the title and abstract present the analogy as a central contribution. For a proof-of-concept this is acceptable, but it limits the depth of the claimed contribution.

### Trivial

- The abstract says "autonomously learn to add up to 30-digit numbers," but the supervised phase includes substantial scaffolding (curriculum learning, two task styles, generalization checks before self-training begins). The word "autonomously" slightly overstates the model's independence.

## Nice-to-Haves

- **Run STaR or a similar prior method on the same task and model** to demonstrate concretely that SECToR avoids the error avalanching that methods like STaR suffer from on this specific setup. Currently the paper only cites prior work without empirical comparison.
- **Analyze per-iteration data quality** (fraction of correct self-generated examples) to support the error-avalanching explanation for eventual termination.
- **Compute cost analysis** (GPU-hours, number of generated examples per iteration) would help researchers assess the practical overhead of the self-training loop.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Missing hyperparameter details (reference to Sec. 4.4).** The parser strips appendix sections from all papers; these details exist in the original submission. Per guidelines, this is not a valid weakness.
- **Reproducibility concerns about undisclosed implementation details or lacking full training logs.** The paper provides adequate methodological description for a proof-of-concept; complete training logs are impractical to include in a submission.
- **Missing related works.** Per guidelines, I cannot confirm the existence of missing citations and this issue is not raised from within the paper.
- **The "autonomously" phrasing nitpick from the harsh critic.** Minor phrasing — the paper is clear about the supervised scaffolding and honestly self-critical in the Discussion.
- **Criticism that the paper does not reproduce prior self-training methods (STaR, etc.).** This is scope creep; the paper is a proof-of-concept for a new method, and reproducing prior methods comprehensively is not required. Moved here from a Major weakness because it asks the authors to do work outside the paper's stated scope.
- **Strength about "replication of the AlphaZero-style self-learning loop."** The AlphaZero analogy is explanatory framing, not a replication. This strength is generic and conflates framing with contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews do not uncover a pattern or observation about the paper that the authors themselves do not discuss.

## Suggestions

1. **Add 3–5 independent runs with different random seeds** and report mean accuracy with standard deviation or min/max range. This is the single highest-impact change for strengthening the paper.
2. **Add at least one baseline:** supervised fine-tuning on self-generated CoT data *without the self-training loop* (one-shot distillation). This isolates the benefit of iteration from the benefit of using CoT to generate training data.
3. **Ablate the commutativity check and/or ST&G in terms of final model accuracy** (not just generated-data error rate). Train a version of SECToR without each component and report the number of successful self-training steps and final digit range.
4. **Show a per-iteration plot** of the accuracy of self-generated training data to support the error-avalanching narrative for eventual termination.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>