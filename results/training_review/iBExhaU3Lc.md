Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper proposes Adam-mini, an optimizer that reduces AdamW's memory footprint by 50% by replacing per‑parameter learning rates (the $1/\sqrt{v}$ term) with a single learning rate per dense Hessian sub‑block. A Hessian‑guided partition principle is developed for Transformers (partitioning query/key by heads, value/MLP by output neurons, embeddings by tokens), and the per‑block learning rate is computed via the mean of Adam's $v$ within each block. Experiments on LLMs from 39M to 13B parameters show loss curves nearly indistinguishable from AdamW across pre‑training, SFT, and RLHF, while throughput increases by up to 49.6% on memory‑constrained hardware.

## Strengths

1. **50% memory reduction with performance parity across LLM scales**: Table 1 shows Adam-mini halves optimizer memory (e.g., GPT‑2‑1.5B: 12.48→6.24 GB; Llama 2‑7B: 53.92→26.96 GB), while pre‑training loss curves from 39M to 13B parameters (Figures 1, 6, 9) closely track AdamW's. This is the paper's central empirical contribution and is convincingly demonstrated.

2. **Principled Hessian‑based partition strategy**: The paper examines Transformer Hessian sub‑blocks (Figure 7) and identifies consistent block‑diagonal structure tied to architectural units (heads, output neurons, tokens). Principle 1 formalizes this into a design rule, and Figure 7(i) shows that violating it (PyTorch default partition) causes training instability on 1B models, while the Hessian‑guided partition stabilizes training. This provides a general, architecture‑aware guideline rather than an ad‑hoc heuristic.

3. **Leave‑one‑out experiments directly motivate the core idea**: On a 4‑layer Transformer (Figure 5), replacing Adam's per‑parameter learning rates in a block with a single grid‑searched learning rate matches or outperforms Adam for all tested blocks, and even for up to three simultaneously left‑out blocks. This provides direct evidence that far fewer learning rates suffice, independent of the later mean‑of‑v heuristic.

4. **Consistent performance across LLM training stages**: Adam-mini matches or exceeds AdamW not only in pre‑training but also in SFT and RLHF on Llama 2‑7B, with MT‑Bench scores showing small improvements (e.g., RLHF: 5.68 vs. 5.54; Table 3). This demonstrates robustness beyond a single training phase.

5. **Scaling‑law validation**: Pre‑training Llama 2 architectures from 39M to 1B under Chinchilla's token budget (Figure 9) shows Adam-mini's loss curves consistently align with AdamW's, with fitted scaling laws suggesting the advantage extrapolates to larger models.

6. **Favorable comparison against Adafactor**: Adam-mini outperforms both original and modified Adafactor on Llama 2‑20M and 1B (Figure 10), while also achieving 40% higher throughput. The paper documents hyperparameter tuning efforts and notes Adam-mini works with AdamW's default hyperparameters, contrasting with Adafactor's sensitivity.

## Weaknesses

### Fatal
None.

### Major

1. **Missing validation linking the Hessian analysis to the mean‑of‑v heuristic.** The paper's theoretical motivation (Section 2.1) shows that a *grid‑searched* single learning rate per dense block can match or beat Adam. But the actual Adam-mini algorithm uses the *mean of Adam's $v$* as the per‑block learning rate — a cheap but unvalidated proxy. The paper does not compare the mean‑of‑v learning rate against the grid‑searched optimal learning rate for the same blocks, even on the small Transformer used in the leave‑one‑out experiments. Section 2.5 provides an intuitive justification (shared BP error within a row), but this is heuristic, not an empirical or theoretical link. While the empirical success of Adam-mini stands on its own, the paper as written creates a gap between the theoretical narrative ("a single good learning rate per block suffices, as shown by grid search") and the actual algorithm ("we use the average of $v$"). A simple ablation study on the small Transformer would bridge this gap.

### Minor

1. **Throughput comparison conflates batch‑size and optimizer effects.** Table 2 reports 49.6% higher throughput for Adam-mini over AdamW on 2× A800‑80GB for Llama 2‑7B, but Adam-mini uses batch size 4 per GPU while AdamW uses batch size 1 (AdamW with batch size 2 runs out of memory). The paper is transparent about both efficiency sources (fewer sqrt/division ops *and* larger batch sizes from memory savings), but the headline throughput gain is primarily driven by the batch‑size difference. An ablation with both optimizers at the same per‑GPU batch size (e.g., batch size 1) would isolate the computational overhead of the optimizer itself and clarify what fraction of the 49.6% gain is algorithmic vs. systems‑level.

2. **Hessian analysis is conducted on a tiny Transformer (vocab 8, dim 16, 4 heads) at a single early training snapshot (1% of steps).** Figure 7 shows Hessian visualizations for this small model. While Figure 2 demonstrates that near‑block‑diagonal Hessian structure persists throughout training for MLPs, there is no evidence that the specific block boundaries (heads, output neurons, tokens) persist or remain stable for Transformers at larger scales or later in training. A more systematic study — even on a moderately sized Transformer (e.g., 1B) at a few checkpoints — would strengthen confidence in Principle 1.

3. **MT‑Bench score differences are reported without significance or variance estimates.** Table 3 shows small improvements (e.g., 5.54 vs. 5.68 for RLHF). These differences may be meaningful, but given the known variance of GPT‑4‑based evaluation and the absence of multiple seeds or confidence intervals, the reader cannot assess whether the improvements are reliable.

4. **Random quadratic case study uses a synthetic random dense matrix as a proxy for real neural‑network Hessian sub‑blocks (Section 2.1).** The condition‑number analysis (Figure 4) shows that Adam's diagonal preconditioner is ineffective for dense random matrices with low $\tau$ (diagonal‑over‑off‑diagonal ratio). However, the eigenvectors of real Transformer Hessian sub‑blocks may differ substantially from random eigenvectors. This weakens the direct transferability of the argument, though the paper partially mitigates this by also showing real Hessian visualizations (Figure 7).

### Trivial

None.

## Nice-to-Haves

- **Direct mean‑of‑v vs. grid‑search comparison**: On the small Transformer used in the leave‑one‑out experiments, compare the mean‑of‑v learning rate per block to the grid‑searched optimal learning rate for that block. This would directly validate the averaging heuristic.
- **Ablation over partition strategies**: Systematically compare the Hessian‑based partition with simpler alternatives (by layer, random grouping) on a model at 1B scale to quantify how much the specific partition matters.
- **Single‑run throughput ablation**: Report the throughput for both Adam-mini and AdamW at the same per‑GPU batch size (e.g., 1) to isolate the computational savings of the optimizer.

## Removed Points

- **Missing non‑LLM experiments (diffusion models, vision, GNNs)**: The abstract and introduction mention non‑LLM tasks, but the main text's experiments section focuses on LLMs. The paper states "Non‑LLM tasks including vision, graph, and diffusion model training" in the experiments section intro (line 436). These results were likely in the appendix, which the parser strips from all papers. Per the review guidelines, weaknesses about missing appendix content are removed because they exist in the original submission. *Caveat: if the non‑LLM results were genuinely absent from the full submission, this would be a significant omission — reviewers should verify against the complete submission.*
- **"≥99.9%" claim insufficiently supported**: The critic argued the 99.9% figure was unsupported. However, this is a straightforward mathematical ratio (number of parameters vs. number of blocks), not an empirical claim. The "harmlessly" qualifier is supported by the extensive LLM experiments showing performance parity.
- **Algorithms 1 and 2 not shown in main text**: The paper relegates them; this is an appendix‑content issue removed per guidelines.
- **Adafactor tuning limitation not properly acknowledged**: The paper explicitly acknowledges this limitation in Section 3.4 ("We acknowledge that it might be possible to improve these methods if we spend more resources on grid search"). This is already addressed.
- **Missing confidence intervals / statistical significance for loss curves**: Multiple seeds and confidence intervals are not the norm for large‑scale LLM pre‑training runs at the scales tested (up to 13B parameters, 300+ GPU hours). This is a nice‑to‑have, not a valid weakness.
- **"Throughput advantage comes entirely from batch size"**: The paper explicitly states two sources of efficiency: reduced computational operations (fewer sqrt/divisions) *and* larger batch sizes from memory savings. The critic's "entirely" framing is factually incorrect.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any novel observation about the method that the paper itself fails to articulate.

## Suggestions

1. **Add a direct validation of the mean‑of‑v heuristic**: On the small Transformer used in the leave‑one‑out experiments, compare the mean‑of‑v per‑block learning rate against the grid‑searched optimal per‑block learning rate. This single experiment would bridge the disconnect between the theoretical motivation and the actual algorithm and significantly strengthen the paper's narrative.

2. **Include a throughput ablation at matched batch size**: Report throughput for both Adam-mini and AdamW at the same per‑GPU batch size (e.g., batch size 1) to isolate the computational savings from reduced sqrt/division operations. This would clarify how much of the 49.6% gain is algorithmic vs. driven by memory‑enabled batch‑size increases.

3. **Provide Hessian evolution for a larger Transformer**: Show that the block‑diagonal structure and block boundaries (by heads, output neurons, tokens) persist for a model at the 1B scale at several training checkpoints, not just a tiny model at 1% training.

## Score and Decision

This paper makes a practically valuable contribution: a simple, well‑motivated optimizer that halves Adam's memory footprint while maintaining LLM pre‑training performance across scales from 39M to 13B parameters. The empirical evidence for the core claim is strong and consistent. The identified weaknesses are real but do not undermine the central finding — the gap between the Hessian analysis and the mean‑of‑v heuristic is a narrative incompleteness rather than an empirical invalidation, and the throughput criticism is mitigated by the paper's transparency about the two contributing factors. The method is simple to implement and requires no hyperparameter changes from AdamW, enhancing its practical impact.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>