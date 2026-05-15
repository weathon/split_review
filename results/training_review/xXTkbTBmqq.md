Now I have a thorough understanding of the paper and all claims. Let me synthesize the final review.

## Summary

This paper introduces OLMoE-1B-7B, a fully open Mixture-of-Experts language model with 6.9B total parameters and 1.3B active parameters, pretrained on 5.1T tokens using a mix of DCLM-Baseline and Dolma 1.7 data. It achieves state-of-the-art performance among models with ≤2B active parameters and is accompanied by comprehensive ablations of MoE design choices, novel analyses of routing behavior (router saturation, domain/vocabulary specialization), and fully open-sourced weights, data, code, and training logs.

## Strengths

- **State-of-the-art performance in its parameter regime with full openness.** Table 2 shows OLMoE-1B-7B outperforming all models with ≤2B active parameters (54.1 MMLU, 80.0 HellaSwag), despite being trained with fully open data. After adaptation (Table 3), OLMoE+DPO achieves the highest average (57.7) among chat models in its class, exceeding DeepSeekMoE-16B-Chat (57.0) and Qwen1.5-3B-14B-Chat (57.3). This is the first fully open MoE (weights, data, code, logs) to reach this performance level.

- **Systematic, controlled ablations of MoE design choices.** The paper evaluates granularity (64 small experts best), shared experts (worse), token vs. expert choice (token choice better under dropless + load balancing), sparse upcycling (catches up after ~500B), load balancing (necessary), router z-loss (improves stability), initialization, normalization, and optimizer epsilon. Each experiment varies only one hyperparameter, with W&B links for reproducibility. These provide concrete empirical guidance absent from prior open MoE work.

- **Novel, quantitative analyses of routing and expert specialization.** The paper defines and measures router saturation (up to ~60% matches final routing after only 1% of pretraining), expert co-activation (little redundancy), domain specialization (far stronger than Mixtral-8x7B), and vocabulary specialization (e.g., expert 27 at 100% on non-alphabetic Unicode, expert 7 on religious terminology). These analyses are clearly defined, measurable, and produce nontrivial findings that go beyond aggregated metrics.

- **Controlled experiments challenging prior claims with evidence.** The paper directly contradicts specific prior findings: shared experts (DeepSeekMoE) perform slightly worse; sparse upcycling loses its advantage at only ~500B tokens (25% of the compute budget reported by Komatsuzaki et al.); token choice outperforms expert choice under dropless + load balancing (reversing Zhou et al. 2022). Each claim is backed by learning curves and specific metrics.

## Weaknesses

### Fatal
None.

### Major

- **No controlled dense baseline at final scale to isolate the MoE contribution.** The controlled MoE-vs-dense comparison (Figure 4) is run for only 130B tokens on an earlier configuration. The final model (OLMoE-1B-7B) differs from prior dense models in both architecture *and* training data (DCLM-Baseline + supplements vs. Dolma 1.7), as well as hyperparameters (RMSNorm, QK-Norm, truncated normal init, AdamW eps=1e-8). The paper acknowledges that its performance over prior OLMo models is "likely a result of the dataset and modeling changes" (line 171), yet the overall framing in the abstract and results sections attributes the advantage primarily to the MoE architecture. A dense model trained on the same data mixture and recipe for a substantial portion of the 5T-token budget would be needed to cleanly isolate the MoE contribution at scale.

### Minor

- **Single-seed runs without variance reporting across all experiments.** No mention of seeds is made, and every ablation and final model is trained once. Differences as small as 1–2% (e.g., 57.7 vs. 57.1 in the adaptation ablation, Table 5; ~1–2% MMLU improvement from 32 to 64 experts) could be within noise. While multi-seed runs at this scale are expensive, the paper should acknowledge this uncertainty in its conclusions rather than treating all observed differences as reliable.

- **The contribution of non-DCLM data components is not validated by ablation.** The data mix (DCLM-Baseline + supplements) is compared against Dolma 1.7 (Figure 13), but not against DCLM-Baseline alone. Since DCLM-Baseline accounts for ~95% of tokens, the marginal benefit of the additional 5% from peS2o, arXiv, Wikipedia, StarCoder, etc. is unknown. An ablation isolating these smaller components would clarify their value.

- **The sparse upcycling comparison uses a suboptimal base checkpoint.** The upcycling experiment (Figure 9) starts from OLMo-1B (0724), which lacks QK-Norm and uses normal initialization — both shown in the paper's own ablations to hurt stability. While the paper acknowledges this limitation transparently, the conclusion that "from scratch catches up within 500B tokens" is specific to this setup and should not be overgeneralized. The experiment does not test whether upcycling from a stronger dense checkpoint with compatible hyperparameters would yield different results.

### Trivial

- The "~7–9B active parameters" category in Table 2 includes Gemma2-9B at 9.2B active parameters, which slightly exceeds the stated upper bound. The paper notes naming/param-count discrepancies in the caption, but the range could be adjusted for precision.

## Nice-to-Haves

- **Inference throughput benchmarks**: The paper claims inference cost parity with 1B dense models but provides no tokens/second measurements on standard hardware (A100/H100). Including throughput (tokens/s) and peak memory usage for OLMoE-1B-7B vs. OLMo-1B, OLMo-7B, and other MoEs would strengthen the practical claims.

- **Multi-seed runs for key ablations**: At minimum, 2–3 seeds for the most important comparisons (granularity, adaptation choices) would establish whether the reported differences exceed noise.

- **Ablation of DCLM-Baseline selection bias**: Training OLMoE for a shorter run on unfiltered Common Crawl (or Dolma 1.7 alone) would quantify how much of the MMLU gain comes from the data filtering procedure rather than the MoE architecture.

- **Per-domain router saturation**: Computing saturation separately on arXiv, Wikipedia, code, and math subsets (rather than just C4) would strengthen the domain specialization analysis.

## Removed Points

These points were flagged for removal; treat them with caution:

- **"Data selection inflates MMLU, no discussion"** — Factually incorrect: the paper explicitly says "DCLM-Baseline has been created through a series of dataset ablations targeting MMLU and other downstream metrics, which explains these results" (line 415). The paper does discuss this; the critic's claim of no discussion is wrong.

- **"Calling it data{} obscures near-identity with DCLM"** — The paper fully documents the 5% non-DCLM components in Table 1. There is no obscuring.

- **"Cherry-picks Llama2-7B as weakest 7B model"** — The paper says "outperforms *some* dense LMs with 7B parameters such as Llama2-7B, but falls short of others like Llama3.1-8B" (line 252). This is balanced, not cherry-picking.

- **"8-expert configuration is a degenerate MoE"** — This is a designed experimental condition for the granularity ablation, not a flaw in the paper.

- **"QK-Norm throughput cost not justified"** — The paper explicitly states "despite it reducing throughput by almost 10%" and justifies the choice with stability and quality improvements.

- **"Co-activation heatmaps are noisy/hard to interpret"** — The paper's finding *is* that there is no strong co-activation. The noisy heatmap honestly reflects this result.

- **"Router saturation on single C4 sample insufficient"** — The paper states the measurement setup; this is a standard analysis approach and the paper is transparent about it.

- **"Vocabulary specialization based on few occurrences"** — The paper filters out IDs with <10 appearances, addressing this concern directly.

## Novel Insights

The reviews surface an insightful tension: the paper's main claim (MoEs offer a superior cost-performance tradeoff) rests partly on evidence that conflates architectural changes with data and hyperparameter improvements. The 130B-token controlled experiment supports the MoE advantage in isolation, but the final model's performance relative to dense comparables is a product of multiple simultaneous improvements. This is a common challenge in systems research where later innovations (data quality, initialization, normalization) compound with the core architectural contribution. What makes this paper valuable despite this confound is the transparency of individual ablations — each component's contribution is measured independently, even if the final model combines them all. The most novel finding, from both the paper and the cross-check with the reviews, is the early router saturation (up to 60% matches at only 1% of pretraining). This has practical implications: it suggests that routing decisions are largely determined very early in training, which could inform more efficient training strategies (e.g., freezing the router after a warmup phase) and has implications for the design of load balancing and expert specialization.

## Suggestions

1. Add a dense baseline trained on the same data (DCLM-Baseline + supplements) with the same hyperparameters for at least 500B–1T tokens to isolate the MoE contribution at meaningful scale. If resource-constrained, tone down the attribution of performance to the MoE architecture in the abstract and conclusions.
2. Report variance across at least 2–3 seeds for the most critical comparisons (granularity, adaptation methods) to establish statistical reliability of the reported differences.
3. Add inference throughput benchmarks (tokens/second on A100/H100) comparing OLMoE-1B-7B against OLMo-1B, OLMo-7B, and other MoEs.
4. Explicitly discuss the implications of DCLM-Baseline's MMLU-targeted data filtering for the validity of benchmark comparisons against models trained on unoptimized data. Compare on a held-out benchmark not used in DCLM's filtering.

## Score and Decision

The paper makes a clear and impactful contribution: a fully open, competitive MoE model with extensive ablations and novel analyses. The weaknesses identified — particularly the lack of a controlled dense baseline at final scale — are real and limit the strength of the causal claims about the MoE architecture, but they do not invalidate the core contribution. The model itself is useful, and the openness sets a new standard for MoE research. The paper should be accepted, provided the authors address the attribution issues (either by adding the controlled baseline experiment at smaller scale or by substantially tempering the architectural claims in the framing) and explicitly discuss the data selection confound in the camera-ready version.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>