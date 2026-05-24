Now I have all the information I need. Let me compile the final review.

## Summary

This paper proposes High-Entropy Sum (HES), a metric that sums the entropy of only the top 0.5% highest-entropy tokens in each LLM reasoning trace, targeting the "forking points" where reasoning decisions are made. HES is validated across three training paradigms (SFT, RFT, and RL), on multiple model families (Qwen3, DeepSeek-R1-Distilled), and across math, code, and STEM domains. The key empirical finding is that pruning the bottom 20% of HES-ranked data consistently improves SFT performance over the full dataset, and that HES-based selection in RL outperforms the full-batch baseline while using half the rollouts per update.

## Strengths

- **Consistent, practical SFT finding across multiple settings.** Training on the top 80% of HES-ranked data (i.e., pruning the bottom 20%) consistently surpasses full-dataset performance across Qwen3-8B (Table 1: 35.36% vs 32.61% avg) and DeepSeek-7B (Table 2: 32.35% vs 30.22%), and the bottom 20% of HES-ranked data actively degrades performance (14.90% vs random 20% at 25.89%). This is a clean, reproducible result with immediate practical value.

- **Small-to-large model transfer is well-demonstrated and cost-effective.** Using Qwen3-0.6B to score data and then training Qwen3-8B on the top 20% yields 32.12% avg, comparable to the 8B's own self-selection (31.14%), reducing inference cost by over an order of magnitude (Table 1). This provides strong evidence that HES captures intrinsic data complexity rather than model-specific artifacts.

- **Broad validation scope strengthens the core claim.** The metric is validated across SFT (2 models, 2 datasets), RFT (per-query and global pool), and RL (with an asymmetric sampling strategy), as well as across code (Table 3) and STEM (Table 4) domains. Most data selection papers only cover one paradigm; the unified treatment here is a genuine strength.

- **Sensitivity analysis confirms robustness.** Figures 3-4 show that the optimal high-entropy token ratio (0.005) and data selection ratio (20%/80%) are stable across math, code, and STEM benchmarks.

## Weaknesses

### Major

- **No statistical significance or variance reporting.** Every result across all tables is a single number with no standard deviations, confidence intervals, or seed information. Given the number of comparisons and the modest gains in some settings (e.g., RL: 21.30 vs 20.63 Full-Batch), the reader cannot assess whether these differences are reliable. This is the most significant missing element and should be addressed (at minimum for the main tables).

- **Figure 1 creates a conceptual tension that is left unresolved.** The figure shows that *incorrect* model responses have substantially higher HES than *correct* ones (normalized means 0.68 vs 0.29). Yet the selection strategy across all three paradigms selects the *highest*-HES samples from a *correct-only* pool. If incorrect outputs have systematically higher HES, why should highest-HES among correct outputs be the best training data? The paper states this shows "better discriminative ability" without addressing the directionality or explaining why the selection mechanism is not choosing correct samples that resemble incorrect ones in entropy pattern. A within-correct-pool analysis or a clarifying discussion is needed.

### Minor

- **The RL experiments use a substantially smaller model (1.5B) than SFT/RFT (7B/8B), and absolute performance is lower.** The HES advantage in RL (0.67 points over Full-Batch, 21.30 vs 20.63) is demonstrated at a smaller scale. It would strengthen the claims to show the pattern holds at 7B-scale RL as well.

- **The "training-free" framing slightly overstates.** Computing token entropy requires a full forward pass through the model for each sample. While there is no *additional model training*, the term "training-free" implies zero cost. The paper would benefit from acknowledging this computational cost explicitly (a sentence or a brief cost analysis), as the small-to-large transfer experiment already demonstrates how to mitigate it.

- **Some benchmarks show flat/no effect from HES selection.** Figures 3-4 show that on MMLU STEM and LiveCodeBench, HES-based selection has essentially no effect regardless of selection ratio or entropy threshold (all conditions produce identical scores). This is mentioned in passing but not discussed. A brief explanation of why HES is less discriminative on these particular benchmarks would strengthen the paper's characterization of when the method works.

### Trivial

- The table header in Table 1 has "Forcing-Only" instead of the presumably intended "Forking-Only" (from the experimental design description).
- The paper uses "High-Entropy Sum" as the metric name, but the abbreviation table header in Figure 1 alternates between the figure caption and the table — this is fine but the formatting could be cleaner.

## Nice-to-Haves

- **Analysis of what low-HES samples actually look like.** The paper convincingly shows that low-HES samples are harmful (14.90% avg), but never provides a qualitative characterization. Are they trivially short? Repetitive? Template-like? A brief qualitative analysis would strengthen the intuitive understanding of what HES captures.
- **An additional lightweight, training-free baseline** such as perplexity-based or DSIR-style selection would further strengthen the comparison set, though the existing baselines (length, difficulty, AvgEntropy, AvgHE, total entropy sum) are already reasonably broad.

## Removed Points

- **"Forking-Only is not a proper baseline"** — The paper includes Forking-Only (token-level gradient masking) as an alternative intervention, not as a direct data selection competitor. The inclusion is fine as a reference point. (Removed: the paper's text doesn't claim it as a direct data selection comparison in the same sense.)
- **"Missing DSIR baseline is critical"** — DSIR is one of many possible lightweight baselines, and the paper already compares against length, difficulty, and three entropy variants. This is a nice-to-have, not a critical omission. (Removed: downgraded to nice-to-have.)
- **"Per-query vs global-pool comparison complicates the unified narrative"** — This is an observation about the RFT design, not a weakness. The paper appropriately discusses the trade-off. (Removed: reflects a design choice, not a flaw.)
- **Strength about "addressed an important problem"** — Generic; removed.
- **Strength about "value to the research community"** — Generic; removed.

## Novel Insights

The paper's key insight — that the *sum* of only the top 0.5% of highest-entropy tokens is a more discriminative signal than average entropy, total entropy, or average high-entropy entropy — is genuinely novel and well-supported. The observation that this signal transfers across model sizes (0.6B → 8B) without retraining is practically valuable and suggests that HES captures data-intrinsic complexity rather than model-specific artifacts. The finding that harmful training data can be identified by low HES and that pruning it boosts performance is also noteworthy.

## Suggestions

1. Add standard deviations (at minimum 3 seeds) for the main results in Tables 1, 2, 5, and 6.
2. Add an analysis of HES distribution within the correct-only pool (e.g., a histogram of HES values for correct SFT samples) to resolve the Figure 1 tension.
3. Add a brief computational cost discussion (approximate FLOPs or GPU-hours for scoring 100k samples).
4. Discuss why MMLU STEM and LiveCodeBench show flat HES sensitivity.

## Score and Decision

### Round 1 — Bracketing
Three queries over the human-review corpus for topically similar papers:

**Low band (score < 3.5):** Retrieved anchors include "Entropy Proxy for LLM Memorization Score" (2.00), "Pushing LLMs to Their Logical Reasoning Bound" (3.33), "Entropy Scheduling in RL for LLMs" (3.00), "Think Just Enough: Sequence-Level Entropy" (3.00). These are clearly weaker than the HES paper — they have narrower scope, less rigorous evaluation, or less clear contributions. → The HES paper is well above this band.

**Middle band (3.5 < score < 7.5):** Retrieved anchors include "Knowledge-Centric Data Selection" (4.40), "EntropyLong" (5.50), "Rethinking Data Selection: Coverage over Difficulty" (4.00), "Enhancing Reasoning via Entropy-Aware Self-Evolution" (5.00). The HES paper is stronger than these — it has broader validation across more paradigms and more consistent results. Initial bracket: **5.5 – 7.0**.

**High band (score > 7.5):** Retrieved anchors include "LLMs Get Lost In Multi-Turn Conversation" (8.00), "Generative Universal Verifier" (8.00), "Transducing Language Models" (8.00). These are not in the same topical area (multi-turn conversation, multimodal verifiers, DNA models). The HES paper does not have the depth or novelty to compete at this level given its weaknesses. → HES is clearly below this band.

### Round 2 — Narrowing inside the bracket
Queries targeting the 4.5–6.0 and 6.0–7.5 ranges returned:

**4.5–6.0 band anchors:** "On the Entropy Dynamics in RFT" (5.50, Reject), "Enhancing Reasoning via Entropy-Aware Self-Evolution" (5.00, Reject), "Quagmires in SFT-RL Post-Training" (5.67, Accept Poster), "EntropyLong" (5.50, Accept Poster). The HES paper is stronger than all of these — it has broader scope (3 paradigms vs 1), cleaner methodology, and more consistent results across domains.

**6.0–7.5 band anchors:** "Expanding Reasoning Potential" (6.50, Accept Poster), "On Entropy Control in LLM-RL" (6.50, Accept Poster), "How to train data-efficient LLMs" (6.80, Accept Poster), "AceReason-Nemotron" (6.50, Accept Poster). The HES paper is comparable to the weaker end of this band but the lack of variance reporting and the unresolved Figure 1 tension prevent it from reaching 6.5+. It is more broadly validated than "Expanding Reasoning Potential" (which tests only math on one MoE model with a complex pipeline), but has less depth than "How to train data-efficient LLMs" (which runs 220 pre-training experiments with 22 strategies).

**Final score: 6.0.** This positions the paper at the upper end of the 5.5–6.0 band and just below the stronger 6.5+ papers. The contribution is solid and practically useful, but the missing variance estimates and the conceptual tension in the motivation figure are real shortcomings that should be addressed.

### Calibration Anchors Used

| Anchor ID | Score | Round | Comparison |
|-----------|-------|-------|------------|
| 9qA5cpZmJh | 2.00 | 1 | Much weaker: narrow memorization study |
| lUkqy21EBB | 3.33 | 1 | Much weaker: logical reasoning bound, single domain |
| fhvjv6UDAj | 3.00 | 1 | Much weaker: entropy scheduling in RL, narrow |
| doR25jEjbj | 3.00 | 1 | Much weaker: entropy as confidence signal, single task |
| 7ZRF2ZkJpt | 4.40 | 1 | Weaker: requires external LLM for concept extraction, limited eval |
| SFXX5Pjl5K | 5.50 | 1,2 | Weaker: narrower scope (long-context training only) |
| nXENWUSRMw | 5.00 | 1,2 | Weaker: 1.8B models only, one paradigm, outdated benchmarks |
| g1DiK2Yi4j | 4.00 | 1 | Weaker: limited to MCQA, coverage selection is trivial |
| 4XIfmxhTaX | 5.50 | 2 | Weaker: theoretical analysis only, no data selection experiments |
| uLM3BfKo19 | 5.67 | 2 | Comparable but different focus (SFT-RL misalignment) |
| 3FQV4JHPpY | 6.50 | 2 | Stronger in some dimensions but tested on single MoE model only |
| LqazVN5epT | 6.50 | 2 | Different focus (entropy control in RL algorithms) |
| yKUbw7q1IA | 6.80 | 2 | Stronger: extensive pre-training experiments but limited to T5 models |
| IaEqjWXd1d | 6.50 | 2 | Different focus (SFT-RL synergy recipe) |

**Initial bracket (Round 1):** 5.5 – 7.0  
**Final score (after Round 2 narrowing):** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>