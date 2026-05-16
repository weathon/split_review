Now I have all the verification I need. Let me produce the consolidated review.

## Summary

HiRA proposes a parameter-efficient fine-tuning method that uses the Hadamard product (element-wise product) between the frozen pre-trained weight matrix \(W_0\) and a low-rank product \(AB\) to produce update matrices \(\Delta W\). This formulation yields updates with substantially higher rank than LoRA (empirically ~2837 vs. ~32) while keeping the same number of trainable parameters and supporting seamless inference-time merging. Experiments across commonsense reasoning (8 tasks), dialogue generation (ConvAI2), and mathematical reasoning (GSM8K) show consistent improvements over LoRA, DoRA, and MoRA on Llama-2-7B and Llama-3-8B.

## Strengths

- **Novel, well-motivated methodology**: The paper is the first to apply the Hadamard product between the frozen pre-trained weight and a low-rank factor for PEFT. This design is theoretically grounded by the rank inequality \(\operatorname{Rank}(P\odot Q) \leq \operatorname{Rank}(P) \times \operatorname{Rank}(Q)\), which the paper correctly identifies and leverages. LoRA becomes a special case when \(R = \mathbf{1}\) (all-ones matrix).

- **Consistent empirical gains across diverse tasks**: HiRA with \(r=32\) achieves average accuracy of 86.72% vs. best-baseline DoRA at 85.20% on Llama-3-8B commonsense reasoning (Table 1), 47.80% vs. 46.62% on ConvAI2 (Table 2), and 70.81% vs. 67.98% on mathematical reasoning (Table 3). The gains are consistent across both model families (Llama-2-7B and Llama-3-8B) and across rank settings (\(r=16\) and \(r=32\)).

- **Efficient inference with zero overhead**: Like LoRA, HiRA supports pre-computation and merging of the update into \(W_0\) via \(W' = W_0 + W_0 \odot (AB)\), yielding no additional inference latency. This is a practical advantage over methods like MoRA, which cannot easily merge their compression/decompression functions.

- **Comprehensive ablation studies**: The paper systematically ablates design choices — the choice of fixed matrix \(R\) (Table 4: \(W_0\) vs. random), rank sensitivity (Figure 6), component placement (Table 5), and combination with LoRA (Table 6: HiLoRA). These studies support the design decisions and provide practical guidance.

- **Clean formulation with low total parameter count**: HiRA uses the same \(d \times r + r \times k\) trainable parameters as LoRA, making it directly comparable. The forward-pass complexity is \(O(drk)\), equivalent to LoRA.

## Weaknesses

### Fatal
None.

### Major

1. **No measures of variance reported despite multi-seed runs.** The paper states (line 194) that HiRA is "evaluated over 5 runs with different random seeds," yet all tables report only point estimates. Without standard deviations, confidence intervals, or min/max ranges, the reader cannot assess whether HiRA's improvements (e.g., HiRA 86.72% vs. DoRA 85.20%, a 1.5% absolute gap) are statistically reliable or within noise. This is a significant methodological gap for an empirical PEFT paper, especially given that PEFT methods can exhibit non-trivial seed-to-seed variance and the reported gains are sometimes modest in absolute terms.

2. **Theoretical expressiveness claim is unsupported.** Theorem 1 provides a bound on HiRA's approximation error: \(\min \|W_0 \odot W_{hi} - \overline{E}\|_2 \leq \sigma_{r+1}(\overline{E} \oslash W_0) \|W_0\|_2\), while LoRA's bound is \(\sigma_{r+1}(\overline{E})\). The paper does **not** compare these two bounds analytically or demonstrate that HiRA's bound is tighter under any realistic condition. It merely notes they depend on different matrices and asserts that \(W_0\) "aids the adaptation process." The theorem is presented as evidence of HiRA's "enhanced expressiveness," but it does not deliver that evidence — there is no formal comparison that would justify the superiority claim. This gap between the theoretical framing and what is actually proven weakens the paper's core narrative.

### Minor

1. **Potential data irregularity in mathematical reasoning results (Table 3).** On Llama-2-7B with \(r=16\), the text reports LoRA at 15.16% accuracy (line 222). The paper's phrasing groups DoRA and MoRA as "its variants" achieving similar numbers. If the table image indeed shows all three baselines at the identical value of 15.16% (as the critic claims), this would be a strong signal of a copy-paste error. The text only explicitly states LoRA = 15.16%, so the issue is ambiguous without the table image, but the authors should clarify the exact numbers for all baselines in this setting and explain the 31.7-point gap to HiRA (46.85%). This needs correction/clarification.

2. **Attribution of gains conflates "high rank" with "content of \(W_0\)."** The HiRA vs. HiRA\(_{\text{rand}}\) ablation (Table 4) compares \(W_0\) against a random uniform matrix \(R\). Since the random matrix also has full rank (with high probability), the large performance gap (86.72% vs. 84.82%) demonstrates that content of \(W_0\) is the primary driver, not rank per se. The paper's title and framing emphasize "high-rank adaptation," but the evidence shows the specific structure of \(W_0\) is key. An additional control (e.g., permuting \(W_0\)'s entries to preserve rank while destroying content) would cleanly separate these factors. This does not invalidate the method but weakens the interpretive claim that "high rank" is the mechanism.

3. **Missing discussion of when HiRA might underperform.** The paper has no limitations section. It should acknowledge scenarios where HiRA may be less effective — e.g., when \(W_0\) contains many zero entries (making the element-wise division in Theorem 1 problematic), when the task requires updates orthogonal to the subspace of \(W_0\), or when the Hadamard product amplifies noise in \(W_0\) entries.

4. **Element-wise division by \(W_0\) and \(AB+1\) not discussed for numerical edge cases.** The expressive power analysis uses \(\overline{E} \oslash W_0\) (element-wise division), and the merge-and-recover procedure uses element-wise division by \(AB + \mathbf{1}\). Neither the theoretical nor practical treatment discusses safeguards for zero or near-zero entries in \(W_0\) or entries of \(AB\) approaching \(-1\).

5. **Learning rate not verified for HiRA's sensitivity.** The paper uses a fixed learning rate of 0.001 for all methods, carried over from the DoRA setup. It does not comment on whether HiRA is more or less sensitive to learning rate than LoRA, or whether this rate was tuned for HiRA specifically.

6. **Hyperparameter \(r\) comparison at equal values does not control for computation.** When comparing HiRA (r=16) to LoRA/DoRA (r=16), HiRA uses \(r_0 \times r\) as the rank bound while LoRA uses \(r\). However, the number of trainable parameters is the same. The paper should clarify this in the comparison setup.

### Trivial
None.

## Nice-to-Haves

- A permuted-\(W_0\) control (shuffling entries of \(W_0\) while preserving its entry distribution and rank) would cleanly separate the effect of rank from content.
- A brief FLOPs comparison between HiRA and LoRA (the element-wise product adds \(dk\) operations per forward pass).
- An empirical comparison of the singular value bounds from Theorem 1 vs. LoRA's bound on actual trained checkpoints.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Figure resolution is poor"** — Removed as a pure formatting nitpick; this is a parser artifact.
- **"Gradient analysis adds little beyond noting W0 involvement"** — The gradient analysis is standard but provides mechanistic insight that distinguishes HiRA from LoRA. The paper does not overclaim here; this is a reasonable derivation.
- **"HiLoRA section doesn't add new evidence"** — Removed as an overly harsh judgment. The HiLoRA experiments show that allocating more capacity to the HiRA component consistently improves performance, which directly supports the paper's thesis.
- **"A zero-initialized A means gradient at step 0 is zero"** — This is standard LoRA-style initialization and works correctly; the critic even acknowledges this. Not a genuine weakness.
- **"Keyword-based answer extraction can introduce noise"** — Removed as scope-creep; this is standard practice for commonsense reasoning evaluation, as the paper notes by citing prior work (Hu et al., 2023; Liu et al., 2024).
- **"BLEU correlates poorly with human judgment for dialogue"** — Removed; BERTScore is also reported, and using both metrics is standard practice. This is a minor preference issue.

## Novel Insights

The most interesting insight emerging from these reviews is the fundamental ambiguity in what drives HiRA's gains: the Hadamard product's rank-increasing property or the informational content of \(W_0\) itself. The HiRA\(_{\text{rand}}\) ablation strongly suggests that \(W_0\)'s content — not just the high rank of \(\Delta W\) — is the primary mechanism. This reframes the contribution from "high-rank adaptation" to "content-aware high-rank scaling," which is actually a more interesting and honest characterization. It also raises a broader question for the PEFT community: if a method works because it leverages the structure of the frozen weights, should it be classified as a rank-improving method or a weight-aware adaptation method? The paper's current framing leans toward the former, but the evidence leans toward the latter. A future version that explicitly disentangles these two factors would make a stronger and more nuanced contribution.

## Suggestions

1. **Add error bars (standard deviations) to all main tables.** Without variance information, the empirical claims are not verifiable. Report std dev across the 5 seeded runs cited in the paper.
2. **Correct/clarify the mathematical reasoning numbers for Llama-2-7B \(r=16\).** Provide explicit accuracy values for LoRA, DoRA, and MoRA in this setting, and explain the large gap to HiRA if it persists.
3. **Either strengthen the theoretical comparison or explicitly scope down the claim.** Theorem 1 should either be augmented with an analytic comparison to LoRA's bound under realistic assumptions, or the paper should state clearly that the theorem provides a bound for HiRA but does not by itself prove superiority over LoRA.
4. **Add a permuted-\(W_0\) ablation** to disentangle rank from content, and reframe the narrative to reflect what the evidence actually shows.
5. **Add a limitations section** acknowledging numerical stability concerns (zeros in \(W_0\), near-zero entries in \(AB+\mathbf{1}\)) and scenarios where HiRA may underperform.
6. **Report whether the learning rate was tuned for HiRA** or inherited from the DoRA setup, and comment on HiRA's sensitivity to this hyperparameter.

## Score and Decision

The paper introduces a clean, well-motivated PEFT method with a novel formulation and consistent empirical gains across three task families. However, the absence of error/variances in all main results is a significant methodological gap that prevents verification of the central empirical claim. The theoretical analysis does not deliver the promised evidence of enhanced expressiveness. These issues are fixable, but in the current form the paper's empirical foundation is incomplete and the theoretical framing overreaches. I recommend rejection with strong encouragement to revise.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>