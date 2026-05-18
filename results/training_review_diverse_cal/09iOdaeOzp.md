Now I have a complete picture of the paper and all the review inputs. Let me compose the final consolidated review.

---

## Summary

This paper proposes Sheared-LLaMA, a two-stage pipeline that (1) uses *targeted structured pruning* with learned masks and Lagrange multiplier constraints to compress a large model (LLaMA2-7B) into a user-specified target architecture, and (2) continues pre-training with *dynamic batch loading* — an online algorithm that adjusts domain sampling proportions based on deviation from reference losses. The resulting Sheared-LLaMA-1.3B and 2.7B models outperform equivalently-sized open-source LLMs (Pythia, INCITE, OpenLLaMA, TinyLlama) across standard benchmarks and instruction-tuned evaluation, while using only a fraction (~3%) of the training compute of from-scratch approaches.

## Strengths

- **Sheared-LLaMA models are empirically competitive with much larger-training-budget alternatives.** Table 3 shows Sheared-LLaMA-1.3B outperforming TinyLlama-1.1B (trained on 3T tokens), Pythia-1.4B (300B tokens), and OPT-1.3B across multiple downstream tasks. Sheared-LLaMA-2.7B outperforms INCITE-Base-3B and OpenLLaMA-3B-v2. This directly supports the paper's central claim that pruning + continued pre-training is a cost-effective route to small LLMs.

- **Targeted structured pruning delivers practical inference-speed advantages over non-uniform pruning.** The throughput comparison (Table 5) shows the targeted-pruned model achieving 126.2 tokens/s vs. 97.9 tokens/s for CoFiPruning at the same sparsity, demonstrating that enforcing a uniform target architecture has real-world deployment benefits.

- **Dynamic batch loading demonstrably balances domain loss reduction and improves downstream accuracy.** Figures 4a/4b show reduced variance in loss differences across domains compared to static data proportions, and Figure 5 shows that dynamic loading yields better downstream accuracy over training steps. The effect is cleanly isolated in the comparison controlling for the same pruning initialization.

- **Ablation on budget allocation between pruning and continued pre-training (Table 6).** The paper varies the token split while holding total tokens fixed, showing that increasing pruning budget consistently improves perplexity, justifying the design choice of 0.4B tokens for pruning despite its 5× slowdown.

## Weaknesses

### Fatal
None.

### Major

1. **The reference loss used to drive dynamic batch loading rests on an unvalidated extrapolation.** The paper fits a scaling function on LLaMA2 model checkpoints evaluated on RedPajama validation sets (line 226), then uses this to predict "the loss of a hypothetical 1.3B LLaMA2 model if it were trained from scratch on the same data." However, LLaMA2 models were trained on non-public data, not RedPajama; evaluating them on RedPajama is an out-of-distribution measurement. There is no reason to expect Chinchilla-style scaling laws fit on out-of-distribution losses to accurately predict in-distribution training loss at smaller scales. The paper partially mitigates this by also experimenting with a "source reference" alternative (the source model's own domain validation loss, line 256–258), but the central method's justification — that the signed deviation from this reference is a principled signal for reweighting data — is weakened. The empirical improvement over static proportions (Fig. 5) shows the method *works*, but does not validate the specific reference choice as correct. The paper would benefit from (a) validating the scaling reference against a small model actually trained on RedPajama, or (b) reframing the reference as a heuristic and reporting sensitivity across both reference choices more thoroughly.

2. **The comparison to baselines conflates the benefit of the LLaMA2-7B initialization with the benefit of the pruning procedure itself.** Sheared-LLaMA-1.3B and 2.7B are initialized from a model pre-trained on 2T tokens (LLaMA2-7B) and then receive 50B tokens of continued pre-training. Baselines like Pythia-1.4B and INCITE-Base-3B are trained from scratch, without any such "head start." The 3% compute figure captures only the post-pruning training cost and implicitly amortizes the source model's cost. The paper's value proposition — *if you already have a large model, pruning is cheaper* — is legitimate, but the framing conflates the effect of the initialization with the effect of the pruning-and-finetuning procedure. An experiment comparing against a *randomly initialized* model of the target architecture trained for the same 50B tokens on RedPajama would isolate how much of the gain comes from the LLaMA2-7B weight inheritance versus the pruning itself.

### Minor

3. **No baseline comparing learned pruning masks to a simple heuristic truncation.** The paper spends substantial compute (0.4B tokens of 5×-slower training) learning which substructures to keep, but never compares against a zero-training baseline that simply retains the top components at each granularity by magnitude or some simple importance score at the same target shape. Without this, it is unclear whether the learned masks contribute meaningfully beyond the architectural constraint. Comparisons to CoFiPruning and LLM-Pruner partially address this (both are structured pruning methods), but the cheapest-possible baseline is missing. The paper's emphasis on the pruning optimization as a "key technical challenge" (lines 48–49) would be strengthened by showing that learned masks outperform a trivial heuristic.

4. **No error bars or variance measures on main evaluation results (Table 3, Figures 3/5).** Standard practice for LLM evaluation often omits multiple runs due to cost, but for tasks where gaps are small (e.g., Sheared-LLaMA-1.3B vs. TinyLlama on ARC-E: 72.1 vs. 72.3; MMLU: 26.1 vs. 25.5), a reader cannot assess whether the difference is statistically meaningful. This is especially notable given the paper's central claim about outperforming baselines.

5. **The benefit of dynamic batch loading is not separated across the two stages (pruning vs. continued pre-training).** The paper applies dynamic loading during both stages and only ablates it against static proportions for the whole pipeline (Fig. 5). An ablation that uses static proportions during pruning and dynamic only during continued pre-training (or vice versa) would isolate where the benefit actually accrues, strengthening the paper's claim that "Dynamic batch loading is a key to making the pruned model competitive."

### Trivial

- The paper does not explore whether a smaller pruning budget (e.g., 0.1B tokens) suffices. The authors note that "the learned masks often converge fast" (line 175), which suggests smaller budgets may work. This would further strengthen the cost argument.
- The "3% of compute" claim and the title "Accelerating Language Model Pre-training" could be more precise: the method accelerates *obtaining* a small model given a large pre-trained model, not pre-training itself.

## Nice-to-Haves

- An experiment comparing learned pruning masks against a simple magnitude-based truncation baseline at the same target shape.
- An ablation isolating dynamic batch loading's effect during the pruning stage vs. the continued pre-training stage.
- Validation of the scaling-function reference loss against a small model actually trained on RedPajama from scratch.

## Removed Points

These points were flagged but are removed after verification against the paper:

- **DoReMi under-citation claim:** The reviewer states the paper "risks under-citing" DoReMi and fails to acknowledge the similarity. In fact, the paper explicitly cites DoReMi (xie2023doremi, lines 230, 425), states "The update rule is exponential ascent following Xie et al. (2023)" (line 245), and explains the difference (line 253: "This approach differs from ... which requires a complex multi-stage process"). The paper is appropriately transparent.

- **Missing related work on prioritized data selection:** The reviewer claims Jiang et al. 2019 and Mindermann et al. 2022 are "unmentioned." In fact, the paper's related work section (lines 423–424) explicitly cites both: "Various batch selection techniques propose to prioritize data based on criteria such as higher losses (jiang2019accelerating) or a greater reducible loss (mindermann2022prioritized)."

- **Missing instruction tuning evaluation details:** The reviewer faults the paper for not specifying details of the GPT-4 evaluation. The paper states "Please refer to Appendix C for more details" (line 296). The appendix is stripped by the PDF parser; these details exist in the original submission.

- **CoFiPruning comparison at small budget is unfair:** The reviewer argues the gap might vanish given the full 50B budget. The paper explicitly acknowledges this (line 361: "Targeted structured pruning needs about 0.5B more tokens ... to match CoFiPruning's perplexity") and justifies the trade-off in terms of inference speed. The paper's own analysis addresses this concern.

- **The reference loss is the only option considered:** The reviewer's framing suggests the paper relies solely on the scaling reference. The paper explicitly experiments with an alternative "source reference" (lines 256–258) and notes that both work well, with the scaling reference being slightly better on math/coding.

## Novel Insights

The reviews collectively highlight a tension that the paper does not fully resolve: the pipeline *works* empirically (the models are strong), but the attribution of *why* it works is unclear across multiple dimensions. The reference loss that drives dynamic batch loading is built on an extrapolation that is not directly validated; the pruning masks' advantage over a trivial heuristic is not established; and the gains from pruning per se versus inherited LLaMA2-7B knowledge are not separated. This suggests the paper's contribution may be better framed as an *engineering recipe* that produces strong results rather than a precisely-characterized scientific finding about *why* structured pruning is effective. The core empirical result stands, but the paper would benefit from leaning into this engineering framing and reducing the emphasis on principled justification for each design choice.

## Suggestions

- **Add a simple heuristic baseline for pruning masks.** At the target architecture (e.g., INCITE-Base-3B configuration), simply keep the top $H_\mathcal{T}$ heads per layer and top $m_\mathcal{T}$ intermediate dimensions by weight magnitude (or some other zero-cost importance score), without any mask learning. Compare the resulting model's perplexity after the same 50B continued pre-training to Sheared-LLaMA. If the gap is small, the pruning algorithm's role should be downplayed.

- **Train a randomly initialized model of the target architecture on RedPajama for the same 50B tokens** and compare its downstream performance directly to Sheared-LLaMA. This isolates the contribution of the LLaMA2-7B weight inheritance from the contribution of the pruning-specific procedure.

- **Validate or reframe the scaling-function reference.** Either (a) train a small model (e.g., 1.3B) on RedPajama from scratch and compare its actual loss to the scaling-function prediction, or (b) explicitly reframe the reference as a practical heuristic and compare sensitivity across both reference choices quantitatively.

- **Report error bars** via bootstrapping or multiple evaluation seeds on at least the closest comparisons in Table 3.

## Score and Decision

The paper presents an effective pipeline with strong empirical results. Sheared-LLaMA models genuinely outperform similarly-sized open-source alternatives at a fraction of the training cost — the headline result is credible and practically valuable. However, the paper overclaims in its scientific attribution: the reference loss driving dynamic batch loading is built on an unvalidated extrapolation, the pruning masks' advantage over a trivial baseline is unproven, and the comparison to baselines conflates initialization quality with the pruning procedure. These issues do not invalidate the contribution (the pipeline works), but they make the paper's analysis of *why* it works less sharp than it should be. With clarifications and additional ablations (particularly the heuristic baseline and the random-initialization comparison), this would be a strong paper. In its current form, it is a solid contribution with notable analytical gaps.

**Originality:** Moderate. Targeted structured pruning to a specified architecture is novel, and the combination with dynamic batch loading is effective, but each component builds closely on prior work (DoReMi, CoFiPruning, scaling laws).

**Quality:** Good empirical results; the experimental design has gaps in attribution but the core claims are supported.

**Clarity:** Well-written and clear about the method; the paper correctly identifies limitations (line 436–437).

**Significance:** High. The practical value of producing competitive small LLMs from existing large ones is clear and timely.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>