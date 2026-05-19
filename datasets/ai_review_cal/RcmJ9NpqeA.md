- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

White-Basilisk is a 200M-parameter hybrid model for C/C++ code vulnerability detection that combines Mamba layers, a linear-complexity adaptation of Infini-attention, and Mixture of Experts in an interleaved architecture. The paper claims that this compact model achieves state-of-the-art results across five benchmark datasets (BigVul, Draper, REVEAL, VulDeepecker, PrimeVul) while supporting 128k-token contexts on a single GPU with dramatically lower training CO₂ emissions than billion-parameter alternatives. It also uses Fill-in-the-Middle pretraining and Scale-Invariant Fine-Tuning (SIFT) for robustness.

## Strengths

- **Novel hybrid architecture with clear formal specification.** The paper defines a concrete layer-composition formula (Section 3, Equation 1) interleaving Mamba, linear-complexity Infini-attention, and MoE with specified hyperparameters (attention offset 2, period 8; MoE on odd layers). This goes beyond simple alternation used in prior work like Jamba and is presented with enough detail to be reproduced.

- **Demonstrated 128k-token context on a single A100 GPU.** White-Basilisk processes sequences up to 128,000 tokens during inference on one NVIDIA A100 40GB GPU (Section 1, Section 5.1). This context length substantially exceeds the typical 4k–32k windows of many LLMs and is a concrete, practically relevant capability.

- **Resource efficiency quantified with explicit CO₂ comparison.** Training uses 2M code samples over 600 hours on a single GPU, with estimated CO₂ emissions of 85.5 kg versus 23,000,000 kg for StarCoder (Table 3). This provides direct empirical evidence supporting the paper's sustainability narrative.

- **Competitive benchmark results from a compact model.** On BigVul the model achieves F1 94.90%/accuracy 99.42%, on VulDeepecker precision 97.20%/F1 93.88%, and on REVEAL F1 49.34%/accuracy 89.88% — all with 200M parameters. Whether or not these are strictly "state-of-the-art" (see Weaknesses), they demonstrate that a small model can be competitive on these tasks.

- **Explicit equations for all architectural components.** The Mamba computation, MoE routing, Infini-attention memory update/retrieval, and the accumulation/gating mechanism are all given in full equations (Sections 3.1–3.3), supporting reproducibility.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparison invalidates the "state-of-the-art" claim.** The paper states: "The metrics for models other than White-Basilisk were sourced from their respective publications" (Section 5, line 220). Comparing against published numbers from other papers — without re-running those baselines under identical conditions — is a well-known methodological weakness. Benchmark versions (function-level vs. file-level), data splits, preprocessing pipelines, and evaluation scripts vary across studies, and reported metric differences often reflect these choices rather than genuine model superiority. The paper says it "used the same data splits as the baseline models" but does not specify how splits were obtained, verified, or what version of each dataset was used. Without a controlled apples-to-apples comparison, the central claim that White-Basilisk "outperforms larger models" is not empirically established.

2. **No ablation studies.** The paper attributes performance to the synergy of Mamba layers, linear-complexity Infini-attention, MoE, FIM pretraining, and SIFT — but does not perform a single ablation (Section 5 contains no component removal or substitution experiments). Without ablations, there is no evidence that this specific interleaving pattern is better than simpler alternatives (e.g., Mamba-only, Transformer with long context, or a Jamba-like model without the modified attention). For an architecture paper, this is a critical gap.

3. **Data contamination not addressed.** The model is pre-trained on 2M C/C++ samples from StarCoder (which scrapes GitHub), and the evaluation benchmarks (BigVul, Draper, REVEAL, etc.) are also derived from open-source GitHub repositories. There is a clear risk that benchmark code appears in the pre-training data. The paper reports no deduplication, no n-gram overlap analysis, and no contamination check. This is a well-documented concern in the vulnerability detection literature (Ding et al., 2024 specifically caution against it). Without addressing contamination, the reported performance numbers — especially the very high BigVul F1 of 94.90% — could be inflated by memorization.

### Minor

1. **Imprecise characterization of the original Infini-attention.** The paper states that the original Infini-attention "processes segments independently with bounded memory usage" (Section 3.3, line 153). This is slightly inaccurate: the original Infini-attention (Munkhdalai et al., 2024) maintains compressive memory that persists and is updated across segments, so segments are not truly processed independently — cross-segment information flows through the memory. The paper's adaptation does legitimately differ (accumulation across segments with linear memory growth vs. bounded memory), but the description of the original work should be more precise. This does not undermine the paper's own contribution but reflects a sloppy characterization.

2. **Limited metrics reported per dataset.** The paper states it uses F1 as the primary metric due to class imbalance (Section 5). For BigVul, only accuracy and F1 are reported (no precision, recall, or ROC-AUC). For Draper and REVEAL, only F1 (and accuracy for REVEAL) are reported. Given the class imbalance concern, the absence of precision and recall makes it difficult to assess whether the model is simply predicting the majority class well or achieving genuine balanced performance. The tables are images and cannot be fully verified from the text.

3. **No runtime or memory measurements.** The paper claims efficient processing of 128k tokens (Section 5.1) but provides no actual inference time measurements, GPU memory consumption figures, or throughput numbers. This is a straightforward measurement that would substantially strengthen the efficiency narrative.

4. **No variance reporting.** The paper reports single-run metrics with no standard deviations or confidence intervals across multiple seeds. This makes it impossible to assess whether reported advantages over baselines are statistically significant.

### Trivial
None.

## Nice-to-Haves

- **Run controlled baseline re-evaluations.** Re-run CodeBERT, VulBERTa, and other baselines on the exact same data splits and preprocessing pipeline used for White-Basilisk. This is the minimal evidence needed to support a "state-of-the-art" claim.

- **Perform comprehensive ablations.** Compare White-Basilisk against: (a) Mamba-only variant, (b) Transformer-with-long-context variant, (c) variant without MoE, (d) variant without SIFT, (e) variant without FIM pretraining. This would isolate which architectural choices actually drive performance.

- **Conduct a contamination analysis.** Measure n-gram overlap between the StarCoder pre-training subset and each benchmark's test set, or retrain on a deduplicated version and report performance drops.

- **Report precision, recall, and dataset imbalance statistics** for every benchmark to provide a complete picture of model behavior.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **"The Mamba equation omits the discretization step and selective scan algorithm."** The paper explicitly says "The core computation in a Mamba layer can be summarized as" (Section 3.1, line 121). This is a high-level summary, not an error, and is appropriate for the paper's level of exposition.

- **"BigVul accuracy 99.42% with F1 94.90% implies extreme class imbalance and the model may just predict the majority class."** The paper explicitly states "we opted for F1 score as our primary evaluation metric" precisely because of class imbalance (Section 5). F1 of 94.90% with accuracy of 99.42% is consistent and not suspicious — it simply indicates the vulnerable class is the minority. Without precision/recall this is hard to fully diagnose, but the concern that the model "may" be predicting the majority class is speculation.

- **"PRIMEVUL F1 of 29.07% is quite low and suggests the model fails on hard vulnerabilities."** PRIMEVUL (Ding et al., 2024) is designed specifically to be a realistic, hard benchmark. F1 scores in the 20–30% range are typical across many models on this dataset. The paper's claim that this "significantly outperforms models with larger parameter counts" is plausible for this dataset. The reviewer's assertion that this is "quite low" is a context-free judgment.

- **"The Infini-attention adaptation is a step backward in efficiency"** and **"the key property that makes Infini-attention attractive is its bounded memory."** The paper transparently describes the trade-off: their adaptation trades bounded memory for the ability to process arbitrarily long sequences (Section 3.3, lines 158–159). Whether this trade-off is desirable is a design decision, not a flaw. The paper never claims bounded memory as a benefit of their adaptation.

- **"Tables are missing (parser issue)."** The tables are embedded as images in the original PDF and are not extractable by the text parser. This is an artifact of the review system, not a paper flaw.

- **"Missing appendix / missing related works"** and **formatting nitpicks:** These are parser artifacts or reflect content stripped by the review system.

## Novel Insights

The most interesting observation from the review process is that the paper's thesis — that a 200M model with a clever hybrid architecture can be competitive with models orders of magnitude larger — is inherently valuable and worthy of exploration, but the execution of this paper falls into a well-known trap: strong claims about beating larger models without running controlled experiments. The reviewers correctly identified that the paper's comparison methodology (citing published numbers from other papers) is insufficient, but several of the harsh critic's strongest claims (e.g., about the Infini-attention being "a step backward," about the Mamba equation being incorrect, about PRIMEVUL being a failure) turned out to be either opinions or context-free assertions that don't hold up against the paper's actual text. This highlights a broader pattern: the paper's real weaknesses — no ablations, no contamination check, no controlled comparison — are genuine and significant, but the reviewer occasionally inflated these with speculative or overly harsh judgments that go beyond what the paper actually says.

## Suggestions

1. **Rerun all baselines under controlled conditions** using the exact same data splits and preprocessing pipeline. This is the single most impactful improvement the authors could make.
2. **Add at minimum three ablations:** remove MoE, replace Infini-attention with standard attention, and remove SIFT. Report the performance drop on each benchmark.
3. **Report n-gram overlap** between the StarCoder training subset and each benchmark's test set, or train on a deduplicated version and report results.
4. **Report precision, recall, and dataset statistics** (class imbalance ratio, train/test splits) for every benchmark.
5. **Add inference-time measurements** (latency, GPU memory) for different sequence lengths to substantiate the efficiency claim.
6. **Correct the characterization of original Infini-attention** to acknowledge that it maintains cross-segment compressive memory (it does not process segments fully independently).
