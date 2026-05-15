Now I have all the evidence I need. Let me construct the final review.

## Summary

This paper proposes LLM-QFA, a once-for-all (OFA) quantization-aware training framework for LLMs. The key ideas are: (1) decoupling weights per bit-width with separate LoRA adapters to avoid interference from weight-sharing, and (2) a resource-balanced sampling scheduler that corrects the bias of uniform sampling toward median-bit-width subnets. Experiments on LLaMA2-7B/13B with 2/3/4-bit quantization show competitive or slightly better accuracy versus QA-LoRA across MMLU and Common Sense QA benchmarks, while requiring only a single training run instead of repeated training per deployment scenario.

## Strengths

- **First OFA approach for quantized LLMs, with clear practical motivation.** The paper identifies a genuine pain point: deploying LLMs across diverse resource constraints requires repeated QAT, and proposes a one-shot solution. Figure 1's efficiency comparison makes the value proposition concrete — training cost is constant in N (number of scenarios) rather than linear. The reported 8 GPU hours for LLaMA2-7B supernet training supports the feasibility claim.

- **Decoupled weights with per-bit-width LoRA adapters are shown to outperform shared-weight alternatives.** The ablation in Figure 6 (shared-LoRA vs. separate-LoRA) directly validates the design choice: sharing one LoRA adapter across bit-widths catastrophically fails, while the proposed decoupled version maintains strong performance. This provides clear evidence that the interference problem (Tang et al., 2024) is real in the LLM quantization setting and that decoupling addresses it.

- **Resource-balanced sampling is empirically shown to improve over uniform sampling across all bit-widths.** The ablation in Figure 6 demonstrates uniform sampling underperforms the proposed scheduler not just at extreme bit-widths (where the theory predicts bias) but at 3-bit as well. While the paper's theoretical motivation focuses on under-fitting of extreme subnets, the empirical result is clean: the proposed scheduler consistently helps across the board.

## Weaknesses

### Fatal
None.

### Major

- **The core OFA value proposition for mixed-precision deployment is not validated against a fair baseline.** The paper's central claim is that training once yields optimal subnets under *diverse* (including mixed-precision) resource constraints without retraining. Yet the main experiments (Tables 1, 2, Figure 2) only compare at fixed uniform bit-widths (2, 3, 4 bits). The mixed-precision analysis (Figure 4) compares LLM-QFA subnets against a naive baseline that stitches layers from separately-trained 2/3/4-bit QA-LoRA models — an ad-hoc construction the paper itself acknowledges ("mixed-precision QA-LoRA based on the fine-tuned QA-LoRA weight at (2, 3, 4) bit"). A proper validation would compare against individual mixed-precision QA-LoRA models trained end-to-end per average-bit budget. Without this, the paper never directly demonstrates that its OFA workflow produces mixed-precision subnets that match or exceed the quality of separately-trained mixed-precision models at the same average-bit budget. The efficiency advantage of the OFA approach is moot if the quality gap is unknown.

- **The MMLU search protocol raises a validity concern.** The paper states (line 163): "For the MMLU Benchmark, we search the optimal subnets on the MMLU evaluation dataset." The methodology section (line 146) describes using a *validation set* for search. If "MMLU evaluation dataset" refers to the MMLU test set (the standard held-out evaluation split), then the reported MMLU numbers are affected by selection bias from using the test data to select subnets. If it refers to a held-out validation split of MMLU, this should be clearly stated. The paper does not disambiguate this, leaving the MMLU results open to doubt. That said, the margins over QA-LoRA are small (0.3% average), so even if contamination existed it would not dramatically change the conclusions — but the ambiguity must be resolved.

### Minor

- **Memory overhead of storing three quantized copies is asserted but not quantified.** The paper states (line 90) that storing per-bit-width quantized weights with LoRA adapters "only brings negligible extra cost compared with the size of LLMs" but provides no actual memory comparison. For a 7B model, storing three quantized copies (even at 2/3/4 bits) plus three LoRA adapters is not obviously negligible versus storing one quantized model plus one adapter. A concrete memory footprint table is needed.

- **Efficiency comparison (Figure 1) omits search time and makes an optimistic assumption.** The figure shows LLM-QFA as constant-time regardless of N (number of deployment scenarios). However, the search procedure ([100, 50] subnet evaluations + correlation analysis) takes non-zero time and its cost relative to training is not reported. Additionally, the figure assumes search cost is the same regardless of N, which is only true if the same search protocol serves all constraints simultaneously — this should be explicitly justified or the search cost should be included in the bars.

- **The shared-LoRA ablation conflates interference with capacity reduction.** The shared-LoRA variant uses a single LoRA adapter for all three bit-widths, which has 1/3 the total parameter count of the separate-LoRA variant. The observed underperformance could be due to insufficient rank (limited capacity) rather than interference from conflicting gradient updates. A clean test would keep total adapter parameters constant (e.g., three adapters with rank r/3 each vs. one adapter of rank r).

- **The mixed-precision QA-LoRA baseline (Figure 4) is ad-hoc and not representative.** Combining layers from separately-trained 2/3/4-bit QA-LoRA models is not how one would train a mixed-precision QA-LoRA model in practice. The paper acknowledges this construction but still uses it to claim robustness advantages. This comparison is not well-controlled.

### Trivial
- The triangular scheduler formula (Eq. 3) is stated without discussion of why this specific schedule (rather than alternatives like random scheduling, curriculum from low-to-high, or sinusoidal schedules) was chosen. The ablation only tests schedule length and order, not schedule shape.
- The paper could clarify whether the 8 GPU hours for LLaMA2-7B includes data loading, evaluation during training, or checkpointing.

## Nice-to-Haves

- Compare LLM-QFA against training independent LoRA adapters per bit-width on the same base model (no supernet), to isolate the benefit of weight sharing in the quantized base weights.
- Report a Pareto frontier of accuracy vs. average bit-width for LLM-QFA subnets vs. fixed-bitwidth models, to visually confirm the OFA advantage across the resource spectrum.
- Include a controlled training-budget comparison: run QA-LoRA per bit-width with total compute equal to LLM-QFA's total (training + search) and compare average accuracy across bit-widths.

## Removed Points

- **"The resource-balanced sampling ablation contradicts the paper's own theory"** — REMOVED as factually incorrect. The paper itself reports (line 306) that uniform sampling underperforms even at 3-bit, and acknowledges this observation. The paper's theory is about sampling *bias* and *under-fitting of extreme subnets* — it does not claim uniform sampling would be strongest at the median. The critic misread the paper's own discussion of this finding.

- **Criticism that uniform sampling underperforms at 3-bit "raises the possibility that the benefit comes from other confounds"** — REMOVED as speculation without evidence. The ablation cleanly shows the proposed scheduler outperforms uniform sampling everywhere; the paper does not require a causal explanation beyond "uniform sampling produces worse subnets overall."

- **Criticism about "storing three copies of a 7B model" making LoRA "the only trainable parameters"** — The LoRA adapters *are* the only trainable parameters, but the quantized base weights are stored in low-bit format (2/3/4 bits). Three copies of quantized weights at 2-4 bits is substantially less than one FP16 copy. The critic's framing as "three copies of a 7B model" is misleading without acknowledging quantization compression.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new observation about the method or problem that the paper itself misses.

## Suggestions

1. **Clarify the MMLU search protocol.** Explicitly state whether the MMLU "evaluation dataset" refers to the standard test set or a held-out validation split. If it is the test set, the results must be re-generated using a separate validation set for search, or clearly caveated as using the test set for architectural selection (which is non-standard).

2. **Add a proper mixed-precision validation.** Train individual mixed-precision QA-LoRA models at several average-bit budgets (e.g., 2.5, 3.0, 3.5 average bits) and compare accuracy against LLM-QFA subnets at the same budgets. This is the experiment that validates or refutes the core OFA claim.

3. **Quantify the memory overhead.** Report total GPU memory for storing the LLM-QFA supernet vs. storing three separate QA-LoRA models (at deployment, not training). This addresses a practical deployment concern.

4. **Include search time in the efficiency comparison.** Report wall-clock time for the full pipeline (training + search) and clarify whether the search cost is amortized across multiple deployment scenarios or incurred per scenario.

5. **Revisit the shared-LoRA ablation with controlled capacity.** Test a version where total LoRA parameter budget is kept constant (e.g., rank r distributed across three adapters vs. rank 3r in one shared adapter) to isolate interference from capacity effects.

## Score and Decision

The paper tackles a timely and practical problem with a sensible framework. The decoupled-weight design and resource-balanced scheduler are well-motivated, and the ablation studies support both design choices. The main weakness is that the evaluation does not fully validate the OFA value proposition for mixed-precision deployment — the central use case that differentiates this work from simply training individual QA-LoRA models. The MMLU search protocol ambiguity is a concern but not fatal given the small margins involved. These weaknesses are addressable with additional experiments rather than reflecting a fundamental flaw in the method. The paper represents a useful contribution to the LLM quantization literature.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>