## Summary

This paper introduces OLMoE-1B-7B, a fully open-source Mixture-of-Experts language model with 6.9B total parameters but only 1.3B active per token, pretrained on 5 trillion tokens. Its core contributions are: (a) releasing the first fully open MoE (weights + data + code + logs) at this performance level, (b) a comprehensive set of controlled ablation experiments isolating MoE and general LM design choices, and (c) analysis of routing behavior including domain and vocabulary specialization with comparison to Mixtral. The model convincingly dominates the 1B-active-parameter class on pretraining benchmarks and achieves competitive adapted performance.

## Strengths

- **State-of-the-art results among models with ≤2B active parameters, supported by clean evidence.** Table 1 shows OLMoE-1B-7B achieving 54.1 MMLU, 80.0 HellaSwag, and 62.1 ARC-Challenge with only 1.3B active parameters, outperforming all other models in its active-parameter class including DCLM-1B (48.5 MMLU) and even larger dense models like Llama2-7B (46.2 MMLU). The comparison groups are well-chosen (by active parameter tier), and the pretraining comparison is a fair, controlled assessment of model quality.

- **Systematic ablation experiments with one-variable-at-a-time methodology, yielding credible design guidance.** Section 3 varies one factor per experiment, isolating the effect of expert granularity (Figure 5), shared experts (Figure 8), token vs. expert choice routing (Figure 9), sparse upcycling (Figure 8), load balancing loss (Figure 10), and router z-loss (Figure 11). Each experiment links to a full W&B report. Key findings — granular experts help, shared experts do not, token choice with dropless outperforms expert choice — are each backed by clean comparisons.

- **Rigorous evidence challenging prior claims about sparse upcycling.** Figure 8 shows a from-scratch MoE catches up to a sparsely upcycled MoE within 500B tokens (~25% of the dense model's 2T compute budget) and surpasses it by ~600B tokens, directly contradicting the 120% advantage reported in prior work. The paper provides concrete explanations for the discrepancy (token choice vs. expert choice routing, decoder-only vs. encoder-decoder architecture, dense model being overtrained) rather than simply asserting a different result.

- **Quantitative routing analysis revealing expert specialization absent in prior MoEs.** Section 4 defines four specific metrics (router saturation, expert co-activation, domain specialization, vocabulary specialization) with formal equations and provides evidence from the trained model. Figure 14 shows strong domain specialization (e.g., an expert in layer 0 is nearly 100% specialized for arXiv data), while the comparison with Mixtral-8x7B shows Mixtral's experts activate close to the uniform baseline. Table 4 provides compelling qualitative evidence (e.g., Expert 27 specializing in non-alphabetic scripts, Expert 43 in geographic terms).

- **Unprecedented openness for an MoE at this performance level.** The paper releases model weights, the full pretraining data composition with exact per-source counts (Table 3), intermediate checkpoints every 5000 steps, training logs via W&B, and code. Figure 1 visually contrasts this against prior MoEs (DeepSeek, Mixtral, Qwen1.5-MoE, JetMoE), showing OLMoE is the only fully open MoE by the paper's openness criteria. No prior MoE at this performance level has released training data.

## Weaknesses

### Major

- **Adaptation-stage comparative claims conflate model quality with data recipe quality.** The abstract, introduction, and conclusion claim that OLMoE-DPO "outperforms" DeepSeekMoE-16B and Llama2-13B-Chat. This claim rests entirely on Table 2, where *different models use different SFT/DPO data recipes*. The paper acknowledges this (line 248: "Models use different mixes for adaptation, e.g., OLMoE is trained on an improved version of the pipeline used for OLMo models"), but this caveat does not resolve the evidential gap. Without a controlled comparison where the same adaptation pipeline is applied to both OLMoE and a baseline model (e.g., Qwen1.5-3B-14B or a dense 1B model), the reader cannot determine whether the adapted performance advantage comes from the base model architecture or from the adaptation recipe. The pretrained comparison (Table 1) is clean and fully supports the model's quality. The adaptation claims should be substantially qualified or the controlled comparison should be added.

### Minor

- **No actual inference throughput or latency benchmarks.** The paper claims (line 43) that OLMoE has "similar inference cost as using dense models with around 1B parameters," but this claim is based entirely on active parameter count as a proxy. Active parameter count is a reasonable first-order approximation for compute-bound generation but not for memory-bandwidth-bound decoding (small batch sizes), where total parameter count matters more because all expert parameters must be loaded. The MoE-vs-dense training speed comparison (Figure 5) is well-executed; a similar figure for inference would be straightforward and valuable. The paper also accepts throughput-reducing architectural choices (RMSNorm: -15%, QK-Norm: -10%, router z-loss: -2%) without quantifying the net effect on inference cost. The memory overhead is acknowledged, but the claim about equivalent inference cost remains unevidenced.

- **The pretrained comparison groups in Table 1 could be clearer.** The table separates models by "~7-9B active," "~2-3B active," and "~1B active" tiers, but DeepSeek-3B-16B (2.9B active) and Qwen1.5-3B-14B (2.7B active) have more than 2× OLMoE's active parameters. OLMoE belongs in the 1B tier and dominates it. The comparison to the 2-3B tier shows OLMoE is competitive — a legitimate and impressive finding — but the presentation could more clearly state that OLMoE's victory is in the 1B tier.

### Trivial

None.

## Nice-to-Haves

- Performing a controlled adaptation comparison (applying the same SFT/DPO pipeline to one or two baseline models) would cleanly isolate whether the adapted performance advantage is architectural or recipe-driven. This is the single most impactful addition the authors could make.
- Measuring actual inference throughput (tokens/second at batch size 1 and at optimal batch) comparing OLMoE to a 1B dense model and a 7B dense model would anchor the inference cost discussion quantitatively.
- A brief comment on sensitivity of the "highest average" claim in Table 2 to benchmark weighting choices (AlpacaEval has known vulnerabilities and contributes large margins) would improve rigor.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **">10× gain on GSM8k after SFT" as a weakness.** The paper itself explains (line 254) this is "likely due to our inclusion of additional math data to account for the relatively small amounts of math data during pretraining." This is the authors' own transparent analysis, not a flaw.
- **"The average in Table 2 weights all benchmarks equally."** The paper reports individual scores alongside the average; the reader can see per-benchmark performance. This is standard practice and not a weakness.
- **"No discussion of expert parallelism or distributed inference."** Deployment engineering details are outside the paper's stated scope (model release and experimental analysis of design choices). The memory requirement is acknowledged.
- **"The claim that MoEs are significantly more efficient is stated without qualification."** Reading line 39 in context: "This makes MoEs significantly more efficient than dense models with a similar number of total parameters" — this is correctly qualified (similar total parameters).
- **"Missing related work."** You do not have external sources to confirm this. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The routing analysis (early saturation at 60% after 1% of training, strong domain specialization contrasting with Mixtral's near-uniform routing) is itself a novel finding that the reviewer input did not meaningfully extend.

## Suggestions

1. **Qualify or fix the adaptation-stage claims.** The simplest fix is to restrict claims about surpassing larger models to the pretraining stage (where the evidence is clean), and present adaptation results as a demonstration of what OLMoE achieves with a specific recipe — acknowledging that the recipe differs from comparators. A stronger fix is to run the same adaptation pipeline on a baseline model like Qwen1.5-3B-14B.

2. **Add inference throughput measurements.** A single table or figure comparing OLMoE to a 1B dense model and a 7B dense model at batch size 1 and optimal batch would transform the inference cost claim from a proxy-based assertion into a measured fact.

3. **Make the throughput-quality trade-off more transparent.** Acknowledge that the ~23% combined throughput penalty from RMSNorm + QK-Norm + z-loss means the net inference efficiency vs. dense models may differ from what active parameter count alone suggests.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>