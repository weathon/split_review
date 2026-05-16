## Summary

The paper proposes I-LoRA, a pipeline for multi-task learning that combines (1) **Routing Tuning** — a LoRA fine-tuning method that adds KL-divergence and L2-norm losses on general data to constrain LoRA activations toward zero on non-target tasks — and (2) **Iterative Merging** — a method that uses SVD truncation and max-of-absolute-values selection to merge LoRA adapters sequentially without additional parameters. The approach is evaluated on Atari games using a LLaVA-interleave-7B model, with experiments on single-task performance, routing tuning retention, and multi-task adapter fusion.

## Strengths

1. **Routing Tuning preserves single-task performance while training for composability.** The paper introduces a clean idea — constraining LoRA activations on general data via KL divergence (output-level consistency) and L2 norm (activation sparsity) — to produce adapters that interfere less when merged. Table 2 reports that all games retain >85% of original single-task performance after routing tuning, supporting the claim that the method does not degrade individual task capability.

2. **The iterative merging + max-abs function shows competitive multi-task retention.** The key quantitative result (Table 4) reports that I-LoRA merging retains 0.552 of the best single-task game's performance after fusing four tasks, compared to 0.203 for magnitude prune and lower for DARE and TIES. This suggests the max-abs operation + SVD pruning yields better parameter compatibility than existing PEFT merging baselines.

3. **Zero additional parameters for fusion.** The merging process operates purely on existing LoRA parameters via SVD and max-abs — no extra routing weights, gating networks, or task-specific parameters are introduced. This is a practical advantage over MoE-based fusion methods that add parameters per task.

4. **New dataset contribution.** The paper constructs an Atari dataset at original resolution (from APPO checkpoints) with chain-of-thought reasoning traces, which may be a useful resource for the VLM-for-games community. The paper also demonstrates that a fine-tuned VLM can effectively learn game-playing from offline data with CoT supervision.

## Weaknesses

### Fatal
None.

### Major

1. **Missing controlled experiment isolating Routing Tuning's effect on composability.** The paper's central claim is that Routing Tuning reduces interference between tasks, enabling better merging. Yet there is no experiment that compares standard LoRA fine-tuning vs. routing-tuned LoRA fine-tuning under identical merging conditions. Table 2 shows routing tuning preserves individual task scores, and Table 4 shows I-LoRA merging outperforms baselines, but neither experiment separates the contribution of routing tuning from the contribution of the merging algorithm. The reader cannot tell whether the improved multi-task retention comes from routing tuning, the max-abs merging method, or their combination. This is the single most important missing experiment and directly undermines the paper's core claim.

2. **Ambiguous baseline design in Table 4 conflates adapter training and merging method.** The paper does not clearly state whether the PEFT baselines (DARE, TIES, magnitude prune) in Table 4 were applied to routing-tuned adapters or to standard LoRA adapters. Section 3.3 describes experimenting with DARE/TIES on *standard* LoRA adapters to motivate routing tuning, but Section 4.2.2 (which contains Table 4) does not clarify what adapters the baselines used. If the baselines used standard LoRA adapters while I-LoRA used routing-tuned adapters, the entire advantage could come from the training intervention rather than the merging algorithm. A proper evaluation would apply all merging methods to the same set of adapters and cross-evaluate: (a) apply I-LoRA merging to standard LoRA adapters, and (b) apply PEFT baselines to routing-tuned adapters.

3. **Misleading comparison against RL algorithms for single-task performance (Table 1).** The paper compares a fine-tuned VLM (with massive pre-training on image-text data, chain-of-thought reasoning, and curated expert demonstrations) against RL algorithms (SPR, DreamerV3, DART) that learn from scratch with only reward signals in 100K steps. The VLM has orders of magnitude more pre-training data and supervision. The claim "twice the performance comparable to state-of-the-art RL models" inflates the apparent contribution — the model should be compared against other VLM fine-tuning approaches or the source APPO checkpoints, not against RL learners that operate under fundamentally different constraints. This does not invalidate the paper but misrepresents its significance.

4. **Overclaimed "lifelong learning" / continual learning framing.** The paper trains adapters separately on each task and then merges them all at once — this is multi-task adapter fusion, not lifelong/continual learning where a single model learns tasks sequentially and must balance plasticity against forgetting. The experiments do not compare against any continual learning baselines (EWC, replay, progressive networks), do not measure forgetting explicitly, and do not show that the model can learn tasks in sequence without access to all data. The "lifelong learning" and "continually learn new tasks" language in the abstract, introduction, and conclusion sets expectations the experiments do not meet.

### Minor

5. **No ablation of the two loss components in Routing Tuning.** The method uses two losses: KL divergence (output consistency) and L2 norm of LoRA B outputs (activation sparsity). These could conflict — the KL loss encourages the model to match the base model's outputs while the L2 norm pushes LoRA activations to zero, but zero LoRA activations would trivially satisfy the KL loss. No ablation shows the contribution of each loss or explains how the loss weights (ε₁, ε₂, ε₃) were chosen. This is important for understanding how routing tuning actually works.

6. **Associativity property claimed but not satisfied.** The paper lists associativity as a desired property ("(A+B)+C = A+B+C") but does not verify it holds. Because SVD truncation at each merging step depends on the singular value distribution of the current fused adapter, merging A then B then C will differ from merging all three at once. The paper should test associativity explicitly or correct the claim.

7. **No variance or confidence intervals reported.** The paper acknowledges that "Atari games exhibit randomness, leading to high variance in validation results" and states it averaged over multiple inference runs, but does not report standard deviations, confidence intervals, or the number of runs. This makes it impossible to assess the statistical significance of reported improvements (e.g., 0.552 vs. 0.203).

8. **Generalization limited to Atari games.** All experiments are on a single domain. The conclusion extrapolates to "enabling lifelong learning capabilities in models" without evidence on more diverse tasks (language understanding, VQA, robotics). This is not fatal — a focused evaluation is fine — but the conclusion should be scoped accordingly.

9. **No analysis of computational cost or scalability.** The paper does not report the number of LoRA parameters per adapter, the time for SVD and merging, or how the method scales to many tasks (e.g., 50 or 100). This makes it difficult to assess the practical claim of "flexible scalability."

### Trivial
None.

## Nice-to-Haves

- An ablation comparing I-LoRA merging applied to standard LoRA adapters vs. routing-tuned adapters (this would resolve the main ambiguity).
- Testing merging in different orders to explicitly verify/falsify the associativity claim.
- Reporting variance/confidence intervals for all main results.
- Description of how loss weights (ε₁, ε₂, ε₃) and the 80% SVD retention threshold were selected.
- Details on the chain-of-thought generation process for the Atari dataset (who wrote the traces, how were they validated).

## Removed Points

- **"Table 2 is unreadable (garbled image), and the textual description is garbled — the sentence 'we applied our Routing Tuning method nothing for all games in our scenario, so the final score is 0' suggests serious confusion."** — This is a parser artifact from PDF extraction, not an author error. The garbled phrasing ("nothing" / "score is 0") does not reflect the original submission. The surrounding text clearly refers to retention rates of 0.203 and 0.552, not a score of zero.

- **"Tables 2, 4, and 5: All are rendered as images and are unreadable in the extracted text."** — PDF parser limitation, not an author error.

- **"Pure formatting/style nitpicks, punctuation, capitalization, whitespace issues."** — Parser artifacts.

- **Strength Finder's strength about "practical continual learning pipeline with thorough experimental setup"** — conflicts with verified Weakness #4. The dataset construction is a genuine contribution but calling it a "continual learning pipeline" is overclaimed by the paper itself.

- **Strength Finder's uncritical endorsement of the RL comparison** — this conflicts with verified Weakness #3. The single-task performance is real, but the framing against RL baselines is misleading.

## Novel Insights

The reviews surface an important tension in the LoRA merging literature: methods that change how adapters are *trained* (via regularization toward the base model) are often evaluated jointly with novel merging heuristics, making it impossible to attribute gains to either component. The paper's experimental blind spot (no controlled experiment isolating routing tuning) is a recurring pattern in this sub-field. The associativity issue with SVD-based iterative merging is also a rarely-discussed problem — truncation at each step makes the operation order-dependent, which undermines the very property the paper claims to guarantee. A broader implication is that the community would benefit from a standardized evaluation protocol that always cross-evaluates (new training + new merge) vs. (standard training + new merge) vs. (new training + standard merge) to disentangle contributions.

## Suggestions

1. **Run the controlled comparison** that isolates routing tuning: train adapters on 4 games using (a) standard LoRA and (b) routing-tuned LoRA. Then apply I-LoRA merging and PEFT baselines (DARE, TIES, magnitude prune) to both sets. This single experiment would resolve whether routing tuning is necessary for the merging gains and whether I-LoRA merging itself outperforms baselines given identical adapters.

2. **Remove or heavily caveat the RL comparison in Table 1.** Either compare against other VLM fine-tuning approaches, or add a clear statement that the VLM leverages extensive pre-training and CoT supervision unavailable to RL algorithms.

3. **Tone down the "lifelong learning" language** to "iterative multi-task adapter fusion" unless the paper adds actual sequential learning experiments with forgetting metrics and continual learning baselines.

4. **Test associativity explicitly** by merging three adapters in different orders and reporting per-task performance for each ordering.

5. **Add an ablation of the two loss components** (KL vs. L2 norm) to show their individual and combined contributions.

6. **Report variance/confidence intervals** for all main quantitative results.

## Score and Decision

The paper addresses a worthwhile problem and the core ideas have merit. However, the experimental validation has significant methodological gaps: the two proposed components are confounded, the baseline comparison is ambiguous, the headline RL comparison is misleading, and the "lifelong learning" framing is overclaimed. In its current form, the evidence does not adequately support the central claims. Major revision with proper controlled experiments is needed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>