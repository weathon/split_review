I've thoroughly read the paper and verified the reviewer claims against the actual content. Let me now produce the consolidated review.

---

## Summary

This paper systematically studies redundancy in Transformer LLMs by measuring cosine similarity between module inputs and outputs, then dropping entire blocks, MLP layers, or attention layers. The central finding is that attention layers are surprisingly redundant: dropping up to 50% of attention layers in Llama-2-70B yields only a 2.4-point average accuracy drop (73.9→71.5) while achieving a 1.48× speedup. The authors propose Attention Drop and Joint Layer Drop (pruning the most redundant attention *and* MLP layers together), and show that attention layer redundancy is consistent throughout training via MAP-Neo-7B checkpoints.

---

## Strengths

1. **Well-documented cross-model evidence.** The finding that Attention Drop preserves near-baseline performance (γ ≤ 0.05) while Block/MLP Drop degrades sharply (γ ≥ 0.31 for Block-8) is replicated across Llama-2-13B, Llama-2-70B, Llama-3-8B, Llama-3-70B, and Mistral-7B (Tables 1–3). This consistency convincingly establishes the relative robustness of attention layers to removal under the used metric.

2. **Training dynamics analysis strengthens the claim.** Using MAP-Neo-7B checkpoints from 500B to 4T tokens (Figure 5), the paper shows that attention importance scores remain low throughout pre-training while MLP and Block importance scores increase. This is the best evidence in the paper that the observed redundancy is not a post-training artifact.

3. **Joint Layer Drop is well-motivated.** At high sparsity, combining redundant attention *and* MLP layers via a single importance ranking outperforms dropping either type alone (e.g., 90% MMLU retention after dropping 31 layers in Llama-2-13B). The paper clearly explains why this works: attention layers are exhausted first, then the next-most-redundant MLP layers are pruned.

4. **Practical efficiency gains are quantified.** KV-cache reductions (e.g., 52GB→26GB for Llama-2-13B, Table 3) and speedup ratios provide concrete deployment benefits beyond raw accuracy retention.

---

## Weaknesses

### Fatal
None.

### Major

1. **No comparison against existing structured pruning methods.** The paper evaluates only its own Block Drop, MLP Drop, Attention Drop, and Joint Layer Drop. There is no experimental comparison to ShortGPT (which uses the identical similarity metric for blocks), SliceGPT, Depth Pruning, or any other structured pruning baseline. Since the paper presents Attention Drop as a "simple yet effective algorithm," the reader cannot tell whether it matches, exceeds, or underperforms existing approaches at comparable speedups. This is the most significant gap — it leaves the contribution's practical value uncalibrated.

2. **The similarity-based importance metric conflates output magnitude with functional importance.** For a residual module, the output is `x + f(x)`. The metric `score = 1 - CosineSim(x, x + f(x))` will be low (flagged "redundant") whenever `f(x)` is small in magnitude relative to `x`, regardless of whether `f(x)` is critical for a specific task. The paper acknowledges the residual structure but does not validate the metric against an orthogonal importance signal (e.g., perplexity change after removal, gradient-based importance, or even random dropping of layers). Without such validation, the claim that "attention layers are highly redundant" is weaker than claimed — the paper has shown *robustness to removal* under a particular scoring function, not necessarily functional redundancy. The relative comparison (attention vs. MLP) is less affected by this concern than the absolute claim, but the paper leans heavily on the absolute interpretation.

### Minor

1. **No random dropping baseline.** The paper does not compare dropping layers by its importance score vs. dropping the same number of layers at random. Since the relative comparison (attention vs. MLP vs. block) already uses the same importance-ordered dropping procedure, the lack of a random baseline does not threaten the main finding. However, it would help disentangle whether the metric's ordering of *which* attention layers to drop matters, or whether any subset of attention layers is similarly removable.

2. **Calibration dataset for main results is not specified.** The paper mentions using multiple calibration datasets (C4, CodeAlpaca-20k, MathInstruct, LIMA) for importance score computation (Section 3.2) but does not state which was used for the main experiments (Tables 1–3). The importance score profiles vary across datasets (Figures 2–3 in the paper), so this matters for reproducibility.

3. **Evaluation is limited to short-context classification/multiple-choice tasks.** All eight benchmarks (ARC-C, BoolQ, HellaSwag, MMLU, OBQA, PIQA, RTE, WinoGrande) are short-context tasks where attention over long-range dependencies is not essential. The paper's conclusion that "attention layers are redundant" may not generalize to tasks requiring strong cross-token interactions (e.g., multi-hop QA, long-document summarization, code generation). The paper partially acknowledges this in its limitations section.

4. **Speed measurement setup for Llama-2-70B is ambiguous regarding quantization.** The paper states that 4-bit quantization is used for Llama-2-70B speed measurements "due to its large model size" but does not explicitly confirm whether the *baseline* also uses 4-bit quantization. The paper references appendix \ref{app:quant} for details (stripped in extraction). If the baseline ran at FP16 (requiring multi-GPU) while the pruned model used 4-bit on a single GPU, the reported speedup would conflate pruning gains with quantization gains.

5. **SDR (γ) metric has limited interpretability.** The metric treats a 1% accuracy drop as equivalent to a 1% speedup gain. In practice, a 1% accuracy loss on a saturated benchmark is not comparable to a 1% throughput improvement. The paper also reports raw accuracy and speedup numbers, so this is supplementary, but the SDR is used as a headline summary statistic and its limitations should be noted.

### Trivial

- The abstract's "2.4% performance drop" refers to absolute percentage points (73.9 → 71.5). This is standard usage in ML papers but could be clarified as "2.4 percentage points" for precision.
- KV-cache table (Table 3) shows only one batch size per model; the claim about larger savings at larger batch sizes is not empirically supported in the paper.

---

## Nice-to-Haves

- Validate the importance metric by comparing layers dropped via cosine similarity with layers dropped at random, or by a complementary metric (e.g., change in validation perplexity). This would strengthen the claim that the ordering is meaningful.
- Add at least one external baseline (ShortGPT or random drop) to the main tables to contextualize the SDR numbers against existing work.
- Test on at least one task requiring long-range dependencies (e.g., a multi-hop QA or long-document task) to probe whether attention redundancy is a general property or a byproduct of the evaluation suite.

---

## Removed Points

These points were flagged by reviewers but are removed (with justification):

- **"Circular reasoning: deeper layers have low importance because the metric defines it."** — Removed. This is not circular; the paper makes a descriptive observation based on the metric, which is standard practice. The metric was defined independently of the layer index.
- **"The training dynamics analysis is purely correlational, not causal."** — Removed. The paper appropriately frames this as an observation ("we observed that..."), and the claim that redundancy is "inherent" is a reasonable interpretation given the evidence, not a causal assertion.
- **"Missing raw latency numbers."** — Removed. Speedup ratios are the standard reporting format in this literature (ShortGPT, SliceGPT, etc.). Raw numbers depend heavily on hardware config and are not necessary for assessing the paper's contribution.
- **"Deeper layers redundancy observation is descriptive, not a mechanistic insight."** — Removed. The paper does not claim mechanistic insight here; it reports an observation consistent with prior work (citing ShortGPT).
- **"Importance scores across datasets vary."** — Removed as a standalone weakness. The paper actually uses this observation (Figure 2-3) as a *motivation* for the study, showing that attention scores differ from MLP scores across datasets, which is evidence, not a flaw.

---

## Novel Insights

The most novel insight from the harsh reviewer is the observation that the paper's "redundancy" claim conflates *robustness to removal* (an empirical observation about the loss landscape) with *lack of functional contribution* (a mechanistic claim about what the layer computes). This distinction — structural robustness vs. functional redundancy — is a useful lens for interpreting the paper's findings. The strength finder did not surface any novel insight beyond the paper's own contributions.

---

## Suggestions

1. Add a baseline comparison to ShortGPT (block drop) and random layer dropping in the main experimental tables. This is the single highest-impact improvement — it would immediately contextualize the SDR numbers and allow the reader to assess whether importance-ordered dropping outperforms naive alternatives.

2. Clarify the 4-bit quantization setup: explicitly state whether the baseline also uses 4-bit, or present separate speedup numbers for FP16 and 4-bit settings.

3. Specify which calibration dataset was used to compute importance scores for each main experiment, or report results averaged across calibration sets.

4. Acknowledge more explicitly that the evaluation covers only short-context classification/multiple-choice tasks (all 8 benchmarks), and that generalization to long-range-dependence tasks is future work.

5. Include error bars or statistical tests for the Joint Layer Drop results, since the claimed improvement over Attention Drop alone appears modest at the sparsity levels shown.

---

## Score and Decision

**Originality**: The finding that attention layers are more robust to removal than MLP layers is an empirical observation that, to my knowledge, has not been systematically documented across multiple model families in this way. The methods themselves (cosine-similarity-based dropping) are adapted from prior work (ShortGPT), so the novelty lies in the *analysis* (comparison across module types, training dynamics) rather than in algorithmic invention.

**Importance of research question**: Understanding which components of Transformer architectures are redundant is a timely and practically relevant question for model efficiency.

**Claims support**: The core claim (attention layers can be dropped with less performance loss than MLP layers) is well-supported by the data across 5 model families. However, the broader claim that "attention layers are highly redundant" is under-validated — the metric has known limitations and no alternative importance signal is checked.

**Soundness of experiments**: Experiments are clearly described and cover multiple model sizes. The major weakness is the absence of external baselines. The limited task scope (short-context only) is a gap but not a fatal flaw.

**Clarity of writing**: Clear. Methodology, tables, and figures are well-structured.

**Value to the community**: Moderate. The empirical finding is useful for practitioners considering structured pruning, and the training dynamics analysis is genuinely interesting. The lack of baseline comparisons limits the paper's reference value.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>