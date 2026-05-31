## Summary

This paper proposes **pcLLM**, a progressive consistency distillation method that transforms autoregressive (AR) language models into efficient parallel decoders without sacrificing the causal inference property. The method introduces a progressive noise schedule and noise-aware causal attention to teach the model to predict multiple future tokens per iteration, achieving **3.6× wall-clock speedup** on coding and math benchmarks with minimal accuracy loss. Additional inference optimizations (rejection recycling and multi-block decoding) further boost speedup to nearly **4×**, outperforming current diffusion-based LLMs (dLLMs) at the same parameter scale.

## Strengths

* **Novel training paradigm.** The progressive consistency distillation with a scheduled noise ratio and multiple rounds of trajectory regeneration with increasing block sizes is a clear improvement over prior consistency distillation (CLLM). This addresses the plateau in speedup observed with fixed block sizes and enables substantially higher fast-forward token counts.
* **Strong empirical results.** On HumanEval, pcLLM achieves 3.57× speedup (3.62× with MR) over the AR baseline, while dLLM baselines at the same 7B scale achieve at most 1.77× (D2F). On GSM8K and MATH, pcLLM also reaches 3.5–3.7× speedup with only ~1% accuracy drop, convincingly showing that AR models can be faster parallel decoders than current dLLMs.
* **Well-designed inference optimizations.** The rejection recycling and multi-block decoding strategies are lossless, leverage the qualitative observation of emerging high-quality n-grams in pcLLM’s Jacobi trajectories, and are validated with systematic ablation on block size, verification size, and threshold.
* **Thorough ablation study.** The paper compares noise schedules (random, linear progressive, reverse progressive), attention mask variants, and inference configuration parameters, providing clear evidence for design choices.

## Weaknesses

### Fatal

None.

### Major

* **Missing main-text comparison with speculative decoding.** The paper states that complementary comparisons (EAGLE-3, HASS, Fast-dLLM v2, etc.) are relegated to the appendix, which is not available to reviewers. Since speculative decoding is a dominant AR acceleration paradigm, this omission weakens the claim that pcLLM offers the best efficiency among AR-based parallel decoders. A direct comparison in the main paper is necessary to fully support the title and central thesis.
* **Speedup claims are slightly overstated.** The abstract and conclusion state “up to 4× speedup” and “nearly 4× speedup”, but the main-table results show 3.62× on HumanEval (A100) and 3.95× on H200 (MR). While close, these are slightly below 4×, and the main paper should be more precise about the actual achieved speedups.
* **Clarity of noise-aware causal attention and sequence packing.** The description of the two attention mask implementations (Figure 1) and how they enable single-pass loss computation is confusing. The figure labels are identical in both subcaptions, and the distinction between “clean-context conditioned” and “noisy-context conditioned” is not clearly explained in the text. This makes it hard to assess the novelty of the training efficiency improvement.

### Minor

* **Training cost not reported.** The paper does not mention how many GPU-hours or computational resources were required for the 450k-example trajectory generation and progressive distillation training. This makes it difficult to judge the practical overhead of the method.
* **Generalization to other model families.** Experiments are limited to Qwen2.5-Coder and Qwen2.5-Math. It is unclear whether the same progressive schedule and hyperparameters transfer to other AR architectures (e.g., Llama, Gemma) or to less structured generation tasks beyond code and math.
* **Accuracy degradation on MBPP.** On MBPP, pcLLM loses 0.9–2.9% accuracy (74.3% → 71.4–73.4%), which is larger than the loss on HumanEval (87.8% → 84.8%, 3% drop). The paper should discuss this degradation.

## Nice-to-Haves

* Include speculative decoding comparisons in the main paper to fully contextualize pcLLM’s efficiency within the broader AR acceleration landscape.
* Provide a more intuitive explanation of how the noise-aware causal mask enables the progressive consistency loss to be computed in O(1) forward passes.
* Report training time and resource usage to help practitioners gauge reproducibility and deployment cost.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

* Add a column in Table 1 (or a new table) comparing pcLLM with standard speculative decoding methods like EAGLE-3 on the same benchmarks using the same base model.
* Clarify Figure 1: ensure subcaptions are distinct, add a legend that explicitly maps colors to clean/noisy, and describe in the text the exact difference between mask (a) and mask (b).
* Recalibrate the speedup claims in the abstract/conclusion to match the measured results (e.g., “up to 3.95×” or “nearly 4×”) to avoid any perception of overclaiming.
* Discuss the MBPP accuracy drop and possible mitigations (e.g., different noise schedules, additional AR loss weighting).

## Score and Decision

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>