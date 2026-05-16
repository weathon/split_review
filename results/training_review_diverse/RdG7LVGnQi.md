Now I have all the verification I need. Let me produce the final review.

---

## Summary

This paper proposes LLM-QFA, a once-for-all (OFA) quantization-aware fine-tuning framework for LLMs. It trains a single supernet that can produce optimal quantized subnets across multiple bit-width constraints (2, 3, 4 bits), eliminating the need for repeated training per deployment scenario. The key technical contributions are: (1) decoupling shared weights across quantization configurations and assigning separate LoRA adapters to avoid interference, and (2) a resource-balanced sampling scheduler that shifts the sampling distribution over training steps to ensure subnets at all bit-widths receive adequate training. Experiments on LLaMA2-7B and LLaMA2-13B show the method achieves accuracy comparable to or slightly better than QA-LoRA while requiring constant training time regardless of the number of deployment scenarios.

## Strengths

- **First OFA framework for quantized LLMs — addresses a genuine practical problem.** The paper identifies that deploying LLMs across diverse resource constraints requires repeated QAT runs, and proposes the first once-for-all approach (to the best of the authors' knowledge and verifiably) that avoids this cost. The efficiency advantage is clearly demonstrated in Figure 3 (left): LLM-QFA's training time remains constant as the number of target scenarios grows, whereas QA-LoRA scales linearly. This is a well-motivated and practical contribution.

- **Interference-less fine-tuning validated by ablation.** The decoupling of per-configuration LoRA adapters (Eq. 3) is a clean solution to the interference problem that would arise from shared weights across different quantization noise levels. The ablation study (shared-LoRA variant, Figure 6) convincingly shows this design choice is necessary — the shared variant underperforms across all resource demands.

- **Resource-balanced sampling strategy clearly motivated and ablated.** The paper identifies a non-obvious pitfall: uniform sampling over bit-width configurations concentrates samples near the mean bit-width (derivation in Eq. 4), starving extreme configurations of training resources. The proposed scheduler (Eq. 5) cyclically shifts the sampling mean from high to low bit-width. The ablation (Figure 6) confirms it outperforms uniform sampling, and the sensitivity analysis (Figure 7) shows robustness to scheduling order.

- **Comprehensive evaluation with proper controls.** Experiments span LLaMA2-7B and LLaMA2-13B, evaluated on MMLU (0-shot and 5-shot) and 7 Common Sense QA tasks. The CSQA evaluation protocol is transparent: subnets are searched on ARC-C (labeled "Eval") and results are reported separately from the test tasks; the reported average explicitly excludes the search set. Table 2 clearly separates "Eval" from "Test" columns.

- **Training efficiency is quantified.** The paper reports that only 8 GPU hours on a single A100 are needed to fine-tune a LLaMA2-7B supernet for 10K steps, demonstrating practical feasibility.

## Weaknesses

### Fatal
None.

### Major

- **MMLU evaluation protocol is ambiguous and potentially problematic.** Line 163 states: "For the MMLU Benchmark, we search the optimal subnets on the MMLU evaluation dataset." If "evaluation dataset" refers to the MMLU test set, then the search procedure leaks test-set information into model selection, giving LLM-QFA an advantage over baselines (GPTQ, QA-LoRA) that report results without such search-based selection. However, this concern does not invalidate the paper's core claims: (a) the efficiency advantage (Figure 3) is unaffected, (b) the CSQA evaluation (Table 2) is properly handled, and (c) the accuracy differences between LLM-QFA and QA-LoRA on MMLU are modest (~0.3–0.5%). The authors should clarify whether a held-out validation split was used, and if not, re-run the search using a proper validation set or remove the MMLU search claim.

### Minor

- **The sampling scheduler is underspecified for reproducibility.** Equation 5 defines the target expected average bit-width as a function of training step, but the paper does not specify *how* per-layer sampling probabilities are derived from this target. With three bit-widths {2, 3, 4} and ~32 layers, there are many ways to achieve a given expected average. The description "setting different sampling strategies for configurations across training steps" (line 135) is too vague to reproduce without guessing. The authors should provide the concrete mapping (e.g., temperature-scaled softmax over bit-widths centered at the target mean).

- **The search procedure is not validated.** The three-stage search (random → correlation → shrinkage) is described briefly, but no evidence is given that it finds near-optimal subnets. A simple comparison to random sampling or a more exhaustive search on a small model would strengthen confidence. (This is a minor concern because the main results focus on uniform-bit constraints, where the search component is less critical.)

- **Memory footprint during training is not analyzed.** Storing three quantized versions of each layer plus per-configuration LoRA adapters has a non-trivial memory cost. The paper calls it "negligible extra cost" (line 90) but does not quantify total GPU memory. This would be useful for practitioners evaluating whether the method fits their hardware.

### Trivial

- The paper uses "quantization" inconsistently in a few places (e.g., "once-for-all quantization-aware training" vs. "fine-tuning"), but this does not affect comprehension.

## Nice-to-Haves

- An additional ablation comparing the scheduler against a simpler fixed-mixture baseline (e.g., always sampling 2-, 3-, and 4-bit with fixed proportions) would help isolate the benefit of the dynamic scheduling mechanism beyond just mixing configurations.
- A validation of the search procedure (e.g., correlation between searched subnet quality and exhaustive search on a small proxy model).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic's claim: "For Common‑Sense QA, the authors search on ARC‑C and then include ARC‑C results in the average (Table 2)... Including it in the average inflates scores."* **Factually wrong.** The table clearly separates "Eval" (ARC‑C, the search set) from "Test" (6 other tasks). The "Avg." column is under the "Test" heading and excludes ARC‑C. Verified by manual computation: e.g., LLaMA2‑7B 16‑bit: (78.2+80.1+74.1+81.1+79.3+45.2)/6 = 73.0, matching the reported average of 73.0. The ARC‑C value (52.0) is not in this average. This criticism is removed in full.

- *Harsh critic's claim about the MMLU issue being "structural" and "invalidates the main quantitative claims."* **Overstated.** While the MMLU protocol is a legitimate concern, it does not invalidate the paper's core claims. The efficiency advantage (Figure 3) is unaffected, the CSQA evaluation is clean, and the accuracy differences on MMLU are modest. The concern is real but major, not fatal.

- *Strength Finder's generic strengths about "addressing an important problem" and "comprehensive evaluation."* These are valid but generic; they are subsumed by the more specific strengths listed above.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the once-for-all paradigm for quantized LLMs fundamentally changes what "fair comparison" means. In standard QAT, each bit-width configuration gets its own training run. In OFA, a single training produces all configurations, but this introduces a search phase that the baselines lack. Evaluating whether the search is "fair" (i.e., doesn't leak test information) becomes a non-trivial methodological question that the community will need to standardize. The paper's CSQA protocol — designating one task as the search set and averaging only over held-out tasks — is a reasonable template for future OFA-LLM papers.

## Suggestions

1. **Clarify the MMLU search protocol.** Either confirm that a held-out validation split of MMLU was used for subnet search (not the test set), or re-run the search on a proper validation set and report the corrected results.

2. **Specify the scheduler concretely.** Provide the algorithm that maps the target expected average bit-width (Eq. 5) to per-layer sampling probabilities at each step. A simple approach: at step *t*, sample bit-width *b* for each layer with probability proportional to exp(−(*b* − μ(*t*))²/τ²), where μ(*t*) is the scheduler output. Include this in the paper or appendix.

3. **Report GPU memory during training.** State the total memory used by the supernet (quantized weights + LoRA adapters) versus a single QA-LoRA run, to help practitioners assess hardware requirements.

## Score and Decision

The paper makes a clear, well-motivated contribution: it is the first to apply the once-for-all paradigm to quantized LLMs, demonstrates a genuine efficiency advantage over repeated QA-LoRA training, and validates its design choices through ablation. The main concern — the MMLU search protocol — is fixable and does not invalidate the core claims. The CSQA evaluation is properly handled. The scheduler underspecification is a minor reproducibility gap.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>