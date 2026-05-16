Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

EditMark proposes a training-free, harmless LLM watermarking method that uses model editing (MEMIT) to control the precision of arithmetic answers to open-ended questions. By constructing logically correct QA pairs where the answer's decimal precision encodes the watermark bits, the method embeds watermarks in ~2 minutes with near-perfect extraction success, without requiring retraining or introducing backdoors.

## Strengths

1. **Training-free and dramatically more efficient than alternatives.** EditMark embeds an 8-bit watermark in 93–110 seconds across GPT-J-6B, LLaMA-7B, and Baichuan-7B, whereas KIMark requires 9,410 seconds on LLaMA-7B for the same capacity (Table 2). This ~100× speedup directly supports the central claim.

2. **Harmless by design, with no observed performance degradation.** The watermark controls only numeric precision of correct arithmetic answers — there is no factually incorrect or malicious content. Performance on BLiMP and MMLU benchmarks remains virtually unchanged after watermarking (Tables 6, 7), and the design has no exploitable backdoor mechanism.

3. **High extraction success across models and capacities.** For 8-bit watermarks, EditMark achieves 97.9–100% ESR on three large models (Table 2). Multi-bit capacity (16-bit, 120-bit via sequence mapping) also maintains ESR above 90% (Tables 3, 9).

4. **Low false positive rate.** Non-watermarked models yield near-zero FPR (Table 4), meaning an innocent model is highly unlikely to be falsely accused.

5. **Robust to temperature variation and model-editing attacks.** ESR remains close to 100% at temperatures 0.5 and 1.0 (Table 8), and the watermark survives 10 rounds of model-editing attacks (Figure 3). Also compatible with alternative model editing techniques (EMMET, Table 10).

## Weaknesses

### Fatal

None.

### Major

1. **Fine-tuning robustness is uneven and underexplored for LLaMA-7B.** Table 5 shows EditMark's ESR on LLaMA-7B drops from 97.9% (original) to 79.1% after 3 LoRA epochs, while KIMark (100%) and BadEdit (97.7%) remain far more robust. The paper attributes this to editing higher layers (where semantic content is richer, hence more affected by fine-tuning), but provides no experimental investigation of alternative layer choices or editing strategies for LLaMA-7B. Since the method's core robustness claim depends on surviving fine-tuning, this gap bounds the method's applicability — users would not know whether the limitation is fundamental to precision-based watermarking or specific to this layer configuration.

### Minor

2. **Threat model levels are incompletely connected to experiments.** The threat model (§3.1) lists "four levels" but describes only three; Level 4 (complete knowledge) is never defined or tested. The editing-attack experiments (Figure 3) assume the attacker knows which MLP layers were edited and the template type — this is a high knowledge level, but the paper does not map these to the threat model hierarchy, making it hard to assess which threat scenarios are actually covered.

3. **Extraction robustness under realistic black-box output post-processing is untested.** The paper tests temperature variation (Table 8) but not whether extraction survives output rounding, truncated precision, or paraphrasing of the question prompt. Since the extraction method (§4.3) assumes black-box access, real-world API post-processing could affect the precision-based watermark signal. The absence of such experiments weakens the practicality claim.

4. **No hyperparameter sensitivity analysis.** The hyperparameters α=2, β=2, γ=3, and m=2 are fixed without any sweep. The choice of γ (number of QA pairs per group) is motivated only verbally (§4.2: "γ be greater than 2 to ensure robustness"), and the effects of α, β, and m on ESR, time, and fidelity are unexplored. This makes the method harder to adopt or tune for new models.

5. **False positive rate analysis lacks probabilistic grounding.** Table 4 reports empirical FPR, but the paper does not quantify the probability that a random non-watermarked model's output accidentally matches the precision watermark for a given query. Since the watermark relies on specific decimal precision (e.g., exactly 3 decimal places), a basic probabilistic bound would strengthen the security argument, especially for multi-bit watermarks where multiple QA pairs must simultaneously match.

6. **Full fine-tuning (not just LoRA) is not tested.** The robustness evaluation (§5.4) uses only LoRA fine-tuning on Alpaca. Full fine-tuning could cause more severe watermark degradation, particularly for the LLaMA-7B case where LoRA already reduces ESR to 79.1%. Testing full fine-tuning would clarify the method's limits.

### Trivial

7. **Figure 3's y-axis ("number of successful watermarking cases") is unclear.** The caption and text do not explain how this count maps to the overall 8-bit ESR, making the figure hard to interpret without cross-referencing other tables.

## Nice-to-Haves

- **Investigate alternative layer selection for LLaMA-7B.** Testing whether editing earlier layers (as done for GPT-J and Baichuan) improves fine-tuning robustness on LLaMA-7B would directly address the most salient weakness. This is within the paper's current experimental framework and would not require broadening scope.
- **Test extraction under output post-processing.** Rounding, truncation, or paraphrasing attacks on the model's output would directly validate the method's practicality in realistic black-box API settings.
- **Provide a brief hyperparameter sensitivity study** (e.g., varying γ ∈ {1,2,3,4} or β ∈ {2,3}) to guide adoption.
- **Add the unedited model's accuracy** as a reference column in the fidelity tables (Tables 6, 7) so readers can assess the absolute cost of watermarking — if not already present in the original figures.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing reference accuracy in fidelity tables"** (reviewer's Section-by-Section Notes): The reviewer acknowledges this may be a parser artifact of stripped images. Since the parser removes figures, the original submission likely contains the tables with all relevant columns. Per the hard rule, absent table content due to parser stripping should not be treated as a paper weakness.
- **"Harmlessness conflates two properties"** (reviewer's Critical Issue 2): Re-examined against the paper's actual text. The paper's harmlessness claim rests on (a) the watermarked QA pairs being logically correct (which is definitional to the method — precision variation in arithmetic answers is inherently not malicious), and (b) model performance being preserved. The reviewer's concern that the precision mapping could be "exploited as a backdoor" is not supported by the paper's design — the mapping is specific to exact question strings (as the paper states, "if the model is posed with a slightly different query... the precision remains variable"), so there is no generalizable trigger an attacker could exploit to produce harmful behavior. The claim is well-supported; the criticism is a misreading.

## Novel Insights

The review surfaces a tension between the paper's claim of general robustness and the uneven results across models: EditMark is robust to fine-tuning on GPT-J-6B and Baichuan-7B but degrades significantly on LLaMA-7B. This suggests that the interaction between model depth, layer choice for editing, and fine-tuning sensitivity is a first-order concern for model-editing-based watermarking — one that the paper identifies but does not resolve. The reviews also highlight that the "harmless" framing would benefit from more explicit boundary testing, even though the basic argument is sound. A genuinely novel observation is that the reviewer's critique of the harmlessness claim (conflating two properties) does not withstand scrutiny against the actual paper design, which is a reminder that watermark methods based on controlling *formatting* of correct answers occupy a fundamentally different (and safer) category than backdoor-based methods, and this distinction is well-grounded in the method's definition.

## Suggestions

- **For the LLaMA-7B fine-tuning gap:** Either (a) test editing earlier layers for LLaMA-7B (matching the strategy used for GPT-J and Baichuan) to see if robustness improves, or (b) if this is not possible, add an explicit limitations paragraph stating that the method's fine-tuning robustness is model-dependent and providing guidance on when it does and does not apply.
- **Add one experiment on output post-processing:** Query the watermarked model and round/truncate the output's decimal places, then measure ESR. This is a small addition that directly addresses a practical concern.
- **Add a short hyperparameter sensitivity paragraph** showing ESR and ET for a few values of γ and β to improve reproducibility.
- **Map the threat model levels directly to the experiments** in §5.4 so it is clear which threat scenarios each attack validates.

## Score and Decision

The paper makes a clear, novel contribution: it is the first to apply model editing to LLM watermarking, achieving dramatic speedups over training-based methods while maintaining harmless watermarks and high extraction success. The main weakness — uneven fine-tuning robustness on LLaMA-7B — is honestly reported and does not invalidate the core contribution, though it bounds its applicability. The remaining issues (missing ablation on hyperparameters, untested output post-processing) are addressable and do not threaten the paper's central claims. The paper is above the acceptance threshold.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>