Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes Adam-mini, a memory-efficient optimizer that reduces Adam's memory footprint by 50% by partitioning parameters according to the smallest dense sub-blocks of the Hessian and assigning a single learning rate per block (via the average of Adam's v within the block). The method is validated extensively on LLMs from 39M to 13B parameters across pre-training, SFT, and RLHF, showing on-par or better performance than AdamW while achieving substantial memory savings and throughput improvements.

## Strengths

- **Memory reduction of 50% (optimizer state).** The paper demonstrates that Adam-mini cuts ≥99.9% of Adam's v, saving exactly 50% of Adam's memory across models from GPT-2-1.5B to Llama 2-13B (Table 1). This is a concrete, practically significant reduction.

- **Effectiveness across LLM scales and tasks.** On pre-training (GPT-2 series, Llama series 20M–13B), supervised fine-tuning, and RLHF, Adam-mini performs on par or better than AdamW, while other memory-efficient methods (Adafactor, CAME, SM3) underperform. The loss curves closely resemble AdamW's, and the trajectory comparison shows Adam-mini's parameter updates stay close to AdamW's, unlike competitors.

- **Throughput and wall-clock improvements.** On Llama 2-7B with 2× A800-80GB GPUs, Adam-mini achieves 49.6% higher throughput and 33.1% less wall-clock time than AdamW (Table 3). The paper is transparent that this stems partly from the memory savings enabling larger per-GPU batch sizes, which is a genuine system-level benefit.

- **Principled Hessian-based partition strategy.** The paper introduces a clear principle (Principle 1: partition by smallest dense Hessian sub-blocks) and shows that violating it (PyTorch default partition) causes training instability on 1B models, while the proposed partition fixes it (Figure 7i). This provides actionable architectural insight beyond generic matrix factorization approaches like Adafactor.

- **Detailed comparison with Adafactor.** A careful head-to-head comparison shows that both the original and Zhai versions of Adafactor underperform Adam-mini on Llama 2-20M and 1B, and that Adam-mini achieves 40% higher throughput (Figure 9). The paper also notes that Adafactor has 9 tunable hyperparameters, while Adam-mini works with AdamW's defaults.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core empirical claims. The two gaps below are real but affect the strength of the theoretical narrative, not the validity of the experimental results.

### Minor

1. **Gap between the leave-one-out motivation and the actual averaging heuristic.** The leave-one-out experiment (Section 3.2, Figure 4) shows that a *grid-searched* optimal single learning rate per block can match or exceed Adam. Adam-mini instead uses a cheap averaging of v within each block. The paper never quantifies how close this averaging heuristic comes to the optimal per-block learning rate that the leave-one-out framework could identify. The paper openly acknowledges "there is great room to improve the learning rate design" (line 420), so this does not undermine the empirical contribution — but it creates a disconnect between the motivational framing and the actual method. A small-scale comparison for a few representative blocks would tighten the narrative.

2. **Limited validation of the Hessian partition principle at scale.** The Hessian analysis that motivates the partition rules (Figure 7a–h) is performed on a tiny Transformer (vocabulary 8, embedding dim 16). The paper then applies the resulting rules to models up to 13B parameters. The paper provides *indirect* evidence that the partition generalizes (the proposed partition fixes training instability on Llama 2-1B, Figure 7i), and the theoretical derivation (Eq. 1) provides a structural argument. Nevertheless, directly verifying that the same Hessian sub-block structure holds at a mid-sized model (e.g., one checkpoint of Llama 2-1B via gradient covariance or Fisher approximation) would substantially strengthen the method's foundation.

3. **RLHF results are reported without variance or replication.** The MT-Bench scores in Table 4 (5.54 vs. 5.68 for RLHF) are reported as single values without confidence intervals or multiple seeds. Given the small absolute differences, it is unclear whether these are statistically meaningful. This is a common limitation in LLM alignment papers, but it limits the strength of the RLHF claims.

4. **Scaling law extrapolation uses only 5 data points.** Figure 8 fits power-law curves from 39M to 1B. With only 5 points and no confidence intervals shown, the extrapolation to larger models is speculative. The paper appropriately hedges ("if the scaling law holds"), but the evidence is thin.

5. **Sensitivity analysis varies only learning rate and weight decay.** The paper claims Adam-mini "performs well using the same hyperparameters as AdamW" — a claim well-supported across all experiments. However, the formal sensitivity analysis (Figure 7c) only tests learning rate and weight decay, not β₂ or ε. The practical claim is still backed by all experiments using the same defaults, so this is a minor documentation gap.

### Trivial
- The abstract's "50% less memory footprint" could be read as referring to total training memory rather than optimizer state memory. The paper is clear in context (and Table 2 explicitly labels optimizer state memory), but a small qualification in the abstract would prevent misinterpretation.

## Nice-to-Haves
- A direct comparison of the averaging heuristic against the grid-searched optimal per-block learning rate for 2–3 representative blocks would tighten the narrative.
- Hessian structure verification (via gradient covariance or diagonal Fisher) at one mid-sized checkpoint would strengthen the partition principle's scalability claim.
- Confidence intervals or multiple-seed runs for the MT-Bench RLHF results.
- Brief discussion of how bias parameters, layer norms, and other non-weight parameters are handled under the partition principle.

## Removed Points
- **"Algorithm pseudocode and partition algorithms are relegated to the appendix"** — The paper provides a high-level description and key rules in the main text. Relegating detailed pseudocode to the appendix is standard practice for optimizer papers. The parser also strips the appendix, which exists in the original submission. *Removed per parser-artifact and standard-practice rules.*
- **"Throughput comparison conflates optimizer efficiency with memory footprint"** — The paper explicitly discusses both factors (no extra computation + larger batch sizes from lower memory) and is transparent about the source of the speedup. The critic acknowledges the framing is reasonable. *Removed; the paper already addresses this.*
- **"The paper does not discuss bias parameters, layer norms"** — The paper's Principle 1 (partition by smallest dense Hessian sub-blocks) is general. The partition algorithms (in the appendix) handle these cases. The main text focuses on the weight matrices where Hessian structure is richest, which is a reasonable scope choice. *Downgraded to Nice-to-Haves.*

## Novel Insights
The harsh critic's observation that Adam-mini's practical success rests on two distinct claims — (a) the existence of good per-block learning rates (supported by grid-search) and (b) the sufficiency of the v-averaging heuristic to produce them — and that these are never directly connected, is a genuinely useful diagnostic. It reveals that the paper's theoretical framing is slightly overstated relative to its evidence: the method is best understood as "a cheap heuristic that empirically works" rather than "a principled approximation to the optimal per-block learning rate." The strength finder's emphasis on the throughput and memory numbers correctly identifies the paper's strongest selling point: the system-level advantage is more compelling than the theoretical narrative.

## Suggestions
1. Add a small-scale comparison of the v-averaging heuristic to a grid-searched optimal per-block learning rate for 2–3 representative blocks (e.g., one query block, one MLP block). This would directly connect the motivation to the method.
2. Compute approximate Hessian sub-block structure (via gradient covariance or diagonal Fisher) at one checkpoint of a mid-sized model (e.g., Llama 2-1B) to verify the small-model-derived partition rules hold at scale.
3. Add multiple seeds or confidence intervals for the MT-Bench RLHF evaluation.
4. Add a brief note in the abstract qualifying that the 50% memory saving is relative to Adam's optimizer states (m and v), not total training memory.
5. Show confidence bands on the scaling law fit in Figure 8.

## Score and Decision

This paper presents a practically useful optimizer with extensive empirical validation across multiple scales (39M to 13B) and tasks (pre-training, SFT, RLHF). The core claims — that Adam-mini matches AdamW's performance with 50% less optimizer-state memory and achieves meaningful throughput gains — are well-supported by the evidence. The weaknesses identified are real but none threaten the main empirical contribution; they predominantly affect the theoretical narrative and would be addressable with additional experiments or clarifications. The paper is clearly written and its contribution is timely given the memory constraints of LLM training.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>