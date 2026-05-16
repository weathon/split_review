Now I have verified all reviewer claims against the paper. Let me produce the consolidated review.

## Summary

This paper introduces Generative Adapter, a method that trains a neural network (adapter generator) to produce low-rank parameter updates for a frozen base LM from input context in a single forward pass. The generator uses an outer-product formulation over hidden states, a streaming update mechanism via a compact state matrix, and SVD normalization to ensure stability. The method is evaluated on two 7B-parameter LMs across three scenarios: document-based QA (knowledge injection), in-context learning (MetaICL), and personalization (MSC). Results show competitive or superior performance compared to prompting and fine-tuning baselines, with substantial inference-cost savings in multi-query personalization scenarios.

## Strengths

- **Significant efficiency gains in personalization without accuracy loss.** On MSC, the method matches the F1 score of full-conversation prompting while reducing computation and memory by 4×, and outperforms the state-of-the-art prompt compression method UltraGist at the same storage budget (Section 4.3, Table msc). This is a clear practical advantage for edge deployment with multi-query users.

- **Effective knowledge injection into parameters via a single forward pass.** On StreamingQA with contexts up to 32K tokens, the method outperforms continual pretraining (CPT) — which requires gradient-based training on the test documents — for contexts under 8K tokens, using only a forward pass (Section 4.1, Figure document-qa). The comparison against CPT is asymmetric in favor of the baseline (CPT trains on the documents), making the result stronger.

- **Technically clean streaming formulation.** The outer-product sum with a compact state Sₜ ∈ ℝ^(dᵣ×dᵣ) (dᵣ ≪ dₕ) enables incremental adapter generation without storing all past hidden states (Section 2.2, Equations 1–4). This is a genuine technical contribution that differentiates the method from naive prompting or fine-tuning.

- **Validated across two 7B-parameter LMs and three diverse adaptation scenarios.** Experiments cover knowledge acquisition (StreamingQA, SQuAD), in-context learning (26 MetaICL tasks), and personalization (MSC), using Mistral-7B-Instruct and Llama2-7B-Chat. This breadth supports the claim of generality across different context types and base models.

- **Self-supervised pretraining with dual objectives is empirically justified.** The ablation study (Section 5, Table ablation) shows that using both reconstruction and completion tasks yields substantially better validation perplexity than either task alone, providing a principled rationale for the training design.

## Weaknesses

### Fatal
None.

### Major
None. The core claims are supported by evidence, and no weakness invalidates the main contributions.

### Minor

- **The headline result (63.5% improvement over SFT) compares against a baseline operating under fundamentally different conditions.** The abstract and introduction highlight the 63.5% F1 improvement over supervised fine-tuning on StreamingQA (from 19.5 to 31.5), but SFT is evaluated in closed-book mode without access to the test documents, while the proposed method encodes the test documents into its parameters. This is an apples-to-oranges comparison: SFT cannot answer questions about documents it has never seen. The paper also includes fair baselines (prompting, CPT) where the comparison is more meaningful, but the prominence of the SFT comparison in the abstract and introduction overstates the result. A more informative baseline would be a PEFT method (e.g., LoRA) fine-tuned on the test documents, which would directly measure whether the generated adapter preserves information compared to an actual gradient-based update from the same data.

- **Efficiency claims lack a complete accounting of the generator's own cost.** The paper claims a "4× reduction in computation and memory costs" compared to full-conversation prompting (Section 4.3), but the generator itself has ~500M parameters (~7% of the base LM's size). The 4× figure appears to count only the inference-phase savings, not the generator's parameters or the cost of its forward pass. For single-query-per-user cases, the adaptation overhead could dominate. The paper acknowledges amortization for multi-query scenarios but should present a total-cost comparison that includes generator storage and the cost of generating the adapter.

- **No variance or error bars reported for key results.** MetaICL results are reported as averages over 5 random samples (Section 4.2) but no standard deviations or error bars are shown. Similarly, the main QA results lack variance information. Without these, it is difficult to assess whether improvements (especially modest ones) are statistically reliable.

- **Hyperparameter sensitivity is not explored.** The chunk size (1024), intermediate dimension dᵣ (1024), and SVD rank r (128) are fixed without ablation or justification. Chunk size in particular could affect the quality of the generated adapter for varying context lengths. These choices control the capacity-efficiency trade-off and should be analyzed.

- **Correlation between perplexity and downstream performance is asserted but not demonstrated.** The ablation study (Section 5) measures reconstruction and completion perplexity on a validation set and states that these "are highly correlated" with downstream performance, but no evidence is provided. While perplexity is a plausible proxy, the paper should either show the correlation or validate the main ablation conclusions on downstream tasks directly.

### Trivial

- The claim "first to explore this direction" (Section 1) is somewhat strong given related work on meta-learned amortization networks (Tack et al., 2024) and meta-learned loss scaling (Hu et al., 2023), though the paper does cite and distinguish these in the related work section. The claim could be tempered.

- The paper does not include a limitations section discussing potential failure cases (e.g., very short contexts where SVD normalization may be unstable, or contexts requiring numerical reasoning).

- The computational cost of performing SVD at each adaptation step during training is not reported; this could be a bottleneck worth documenting.

## Nice-to-Haves

- Adding a LoRA baseline fine-tuned on the test documents in the QA experiments would provide a direct comparison between generated adapters and gradient-derived adapters from the same data, making the knowledge-injection claim stronger.
- A total-cost comparison including the generator's parameters and forward pass would clarify the trade-offs for different deployment scenarios (single-query vs. multi-query).
- Reporting standard deviations / error bars on key results would improve scientific rigor.
- An ablation of chunk size would help justify the chosen value and reveal sensitivity.
- Evaluating on a held-out context type substantially different from the instruction tuning distribution (e.g., structured tables or code) would strengthen the generality claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Task contamination concern for MetaICL"** — The reviewer questioned whether MetaICL tasks overlap with instruction tuning data. The paper explicitly states (line 370): "We also ensure that none of these test tasks were seen during the training of adapter generator." The reviewer's speculation contradicts what the paper asserts and lacks evidence to the contrary.

- **"Fine-tuning baseline uses only 16 examples"** — The reviewer claimed the paper should note that 16 examples is small. The paper already discusses this (lines 384–385): "We speculate that the few-shot setting (16 shots) is insufficient for the model to learn the desired output style through fine-tuning." The paper's conclusion about fine-tuning's weakness in non-classification tasks is appropriately caveated.

- **"CPT comparison is unfair"** — The reviewer said comparing against CPT is asymmetric because CPT trains on test documents. This asymmetry **favors the baseline** (CPT does gradient training), not the author's method. Per the hard rules, weaknesses about asymmetric comparisons are removed when the asymmetry favors the baseline, as this proves a stronger point.

- **"Missing figure caption details"** — Pure formatting nitpick; parser artifacts.

- **"Unfair comparison to fine-tuning broadly"** — As analyzed above, the CPT comparison favors the baseline. The prompting comparison is intrinsically fair (both methods process the test documents). The SFT comparison is a legitimate minor concern (retained above) but the broader claim of structural unfairness across all baselines is not supported.

## Novel Insights

The most insightful observation emerging from the reviews is that the paper's strongest evidence is in the personalization scenario, where the method's advantages are clearest (matching full-context performance at 4× lower cost, outperforming prompt compression). The knowledge-acquisition scenario is weakened by comparing against a closed-book SFT baseline in the headline result, but the CPT comparison — where the baseline trains on the documents — actually provides stronger evidence for the method's efficiency. The reviews collectively highlight that the paper would benefit from repositioning its contributions: the streaming formulation and multi-query efficiency are the genuine strengths, rather than a general claim of outperforming all forms of fine-tuning.

## Suggestions

1. Reframe the abstract and introduction to foreground the method's streaming formulation and its concrete benefits in multi-query personalization, rather than leading with the 63.5% figure against SFT.
2. Add a PEFT baseline (e.g., LoRA fine-tuned on test documents with a single epoch) to the QA experiments for a direct comparison between generated and gradient-derived adapters.
3. Provide a full cost accounting that includes the generator's parameters and forward pass, with a break-even analysis for single-query vs. multi-query scenarios.
4. Report standard deviations / confidence intervals for all quantitative results, especially MetaICL where multiple samples are already collected.
5. Add a brief limitations paragraph discussing when the method may not be beneficial (short contexts, single-query cases, numerical reasoning tasks).

## Score and Decision

**Score:** 7.0

**Decision:** Accept

The paper makes a genuine technical contribution with a well-motivated method, clean formulation, and broad empirical validation across three scenarios and two base models. The weaknesses are primarily about presentation framing, incomplete cost accounting, and missing ablations — none invalidate the core claims. The personalization results (matching full-context performance at 4× lower cost) are compelling, and the streaming formulation is technically novel. The paper would benefit from the suggested revisions but is already a solid contribution in its current form.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>