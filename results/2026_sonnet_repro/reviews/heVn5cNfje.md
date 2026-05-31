Now let me perform the calibration search with bracket queries.**Round 1 Bracket**: Based on comparison with middle-band (4.25-5.75) and upper-band (8.0) papers, this paper sits between 5.5 and 7.5. It's more comprehensive than SpTzsQjgxF (5.75) — it covers three training paradigms, has thorough baselines, and has cleaner findings — but potentially below DiSF's theoretical rigor (8.0).

**Round 2 Narrowing**:Now I have enough calibration information. Let me write the final consolidated review.

---

## Summary

This paper proposes High-Entropy Sum (HES), a training-free data selection metric for LLM reasoning. HES sums the token-level entropy of only the top 0.5% highest-entropy tokens in a reasoning path, motivated by the observation that these tokens correspond to critical "forking points" that drive reasoning quality. The paper validates HES across three training paradigms — SFT, RFT, and RL — on competition-math benchmarks (AIME24/25, HMMT, OlympMATH, GPQA), showing in particular that pruning the lowest-HES 20% of training data consistently improves upon full-dataset training, with a 35.36% average vs. 32.61% for full dataset (Table 1).

---

## Strengths

- **Clear discriminative power of HES** (Figure 1): On 512 responses per problem from Qwen3-14B on AIME 2025, HES achieves correct/incorrect normalized means of 0.29 vs. 0.68, while global average entropy yields 0.52 vs. 0.53 — flat and useless. The comparison also shows that Entropy Sum (total sum, not peak-focused) gives a weaker separation (0.28 vs. 0.58), confirming the value of focusing on high-entropy tokens specifically.

- **Strong and reproducible SFT sample efficiency**: Training on only the top 80% of HES-ranked data consistently surpasses full-dataset training across multiple models and datasets — 35.36% vs. 32.61% on Open-Math-Reasoning (Table 1); 32.35% vs. 30.22% on OpenR1-Math-220k (Table 2). Crucially, Lowest-HES-20% yields only 14.90% average, far below even Random-20% (25.89%), providing unusually clean evidence that low-HES samples are actively harmful rather than merely uninformative.

- **Thorough baseline ablation** (Table 1): HES is compared against 11 variants — Difficulty (medium and hard), Length, Forking-Only, AvgE, AvgHE, ES, HES_absolute, Lowest-HES, Random, and Full-Dataset — providing a comprehensive evaluation context rather than cherry-picked baselines.

- **Multi-domain generalization**: Highest-HES-20% outperforms Full-Dataset on code (39.54% vs 36.28%, Table 3) and STEM (49.56% vs 44.42%, Table 4) domains with different base models and datasets, supporting the claim that the signal is domain-agnostic.

- **Cost-effective cross-model transfer** (Table 1): Computing HES with a Qwen3-0.6B proxy model achieves 32.12% average vs. 31.14% from the 8B model's own entropy — comparable performance at >10× lower inference cost, enabling practical deployment.

- **RFT global-pool finding**: In the global-pool selection setting (Table 5), Length and Difficulty fail to beat Random, while HES consistently does (+2.35 points at k=2). This demonstrates HES captures a genuine quality signal beyond simple heuristics in a harder discrimination task.

---

## Weaknesses

### Fatal
None.

### Major

- **Length confounding not cleanly resolved.** Since HES_relative sums the top 0.5% of tokens by entropy, a response with N tokens contributes ⌊0.005·N⌋ tokens to the sum. All else equal, HES grows roughly linearly with sequence length — making it a joint signal of length × peak-entropy intensity. The paper compares against Length as a baseline (Table 1: Length-20% = 30.67 vs. HES-20% = 31.14) and HES does win. However, the AvgHE baseline — which divides out the count of high-entropy tokens — performs substantially worse (27.97%), sharpening the interpretive question: is it the forking-point signal, or the compounding of length and entropy intensity that drives gains? No length-controlled ablation (e.g., comparing HES vs. Random within a fixed length band) is provided. The paper's mechanistic claim that HES targets "critical forking points" is asserted more strongly than the current evidence can support.

- **Thin RL evidence relative to the "unified" claim.** The RL section (Section 4.3) uses only one model (DeepSeek-R1-Distilled-Qwen-1.5B) on one dataset (DeepScaleR). The headline average improvement from Full-Batch (20.63%) to Pos-High, Neg-Rand (21.30%) is 0.67 points, while HMMT25 moves in the *wrong* direction (15.21% → 11.88%). The paper includes this as part of the unified claim but provides notably weaker evidence than the SFT results. Including even one additional model or dataset would substantially strengthen this claim.

### Minor

- **No statistical significance reporting on small benchmarks.** AIME24 and AIME25 each contain 30 problems. While 16 samples per problem helps, 30-problem accuracy still carries substantial variance. Several RFT comparisons in Table 5 (e.g., +1.01 average points for per-query k=2) and the RL headline gain (+0.67) are well within plausible noise ranges. No confidence intervals, standard deviations, or multi-seed results are reported anywhere in the paper. The SFT results (e.g., +4.39 points in Table 2) are large enough to be credible without formal tests, but the smaller RFT and RL margins warrant reporting uncertainty.

- **Which model computes HES is underspecified for the main SFT experiments.** For the Qwen3-8B-Base SFT experiments, the paper does not explicitly state which model generates the entropy values used to rank the 100,000 samples. The cross-model transfer experiment (Section 4.1.2) establishes that a 0.6B proxy works, but the default setup — whether the 8B model itself or a separate model — is never stated clearly. This affects reproducibility and the "training-free" framing's practical cost assessment.

- **Figure 1 motivational evidence uses a different data distribution.** Figure 1, which motivates the metric, is computed on 512 responses per problem from Qwen3-14B on AIME 2025. The main SFT experiments use Qwen3-8B or DeepSeek-R1-Distilled-7B on Open-Math-Reasoning and Open-R1-220k. Whether the clean correct/incorrect separation in Figure 1 holds on the actual training data used in experiments is not demonstrated. A similar discriminability plot on the SFT training datasets would strengthen the motivational claim.

### Trivial

- The claim in footnote 1 that HES_relative's "adaptive nature makes it more robust across diverse entropy distributions" is post-hoc rationalization rather than independent motivation; the paper doesn't explain *why* relative thresholding should outperform absolute beyond pointing to the empirical results.

- MMLU STEM and LiveCodeBench (Figure 4) show identical average scores across all token ratios (0.855 and 0.544 respectively), suggesting these benchmarks are insensitive to the selection method. This limitation is not acknowledged and worth a brief remark.

---

## Nice-to-Haves

- A token-level analysis on a small sample of high-HES vs. low-HES responses showing that the high-entropy tokens cluster at genuine reasoning decision points (branching, strategy switches, self-correction) rather than at random linguistic positions would directly validate the mechanistic story rather than relying on outcome-based discrimination.

- A length-controlled ablation — comparing HES vs. Random within a matched-length band (e.g., 2,000–3,000 token responses) — would cleanly separate the entropy signal from the length signal.

- Expanding the RL experiment to at least one additional model or dataset would meaningfully strengthen the "unified" framing.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh Critic: "Post-hoc rationalization for $HES_{relative}$ superiority"** — Removed as a weakness. The footnote adequately acknowledges this is empirically derived; it does not represent a flawed argument, only a modest hedging of interpretive scope. Kept as a trivial note.

- **Harsh Critic: "Section 4.2 per-query vs. global-pool analysis is not deeply analyzed"** — Removed. The paper offers a reasonable hypothesis (query diversity) and the finding is noted as an observation rather than a claimed mechanism. Not a substantive weakness.

- **Strength Finder: "Training-free and lightweight — negligible computation"** — Partially removed/demoted. The claim of "negligible computation" overstates the case when the default model (8B) may need a full forward pass over 100,000+ long-CoT sequences. Kept partially in context of the cross-model transfer result which does substantially reduce cost.

- **Strength Finder: "Well-structured experimental setup facilitating reproducibility"** — Removed as generic; replaced by specific strength about baselines.

---

## Novel Insights

The paper's most genuinely novel empirical finding is the asymmetry between removing vs. adding data: the lowest-HES 20% is not merely noise but actively harmful (14.90% avg. for Lowest-HES-20% vs. 25.89% for Random-20%), while removing that same 20% from the full dataset yields higher-than-full-dataset performance. This is a non-obvious and practically actionable observation: data curation for reasoning models should focus on *excising* the worst samples, not only adding the best ones. The RL finding that curating high-HES *negative* examples (Pos-High, Neg-Low) paradoxically *hurts* performance — while random negatives work best — also offers a counterintuitive practical insight about the value of diverse failure modes in GRPO training.

---

## Suggestions

1. Add a length-controlled ablation: within a fixed token-length band (e.g., 2,000–3,000 tokens), compare HES-selected vs. Random. If HES still wins meaningfully, the length confound is effectively ruled out.
2. Provide bootstrapped confidence intervals (even approximate ones) for all comparisons where the margin is ≤2 average points, particularly in Tables 5 and 6.
3. State explicitly in Section 4.1.1 which model computes HES for the main SFT experiments (base model self-scoring vs. proxy model), and provide an estimate of the forward-pass cost as a fraction of training cost.
4. Replicate the RL asymmetric-sampling experiment on at least one more model (e.g., DeepSeek-R1-Distilled-Qwen-7B) to validate generalizability of the RL findings.
5. Include a brief discriminability plot on the actual SFT training data to establish that Figure 1's correct/incorrect separation generalizes beyond the Qwen3-14B-on-AIME setting.

---

## Score and Decision

**Anchor papers across rounds:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| OdoS6cH8MP.md | 2.00 | R1 | Unrelated data valuation; far weaker contribution |
| EOPLy80bBm.md | 3.00 | R1 | Data pruning for NLP fine-tuning; less empirically comprehensive |
| SpTzsQjgxF.md | 5.75 | R1/R2 | Rule-based LLM data selection; less comprehensive, weaker evidence |
| qUJsX3XMBH.md | 4.40 | R1 | Rethinking data selection at scale; less targeted, weaker claims |
| 7qMrDf9zFU.md | 4.75 | R1 | Instruction data quality selection; narrower scope |
| f4gF6AIHRy.md | 8.00 | R1 | Submodular pre-training file selection; stronger theoretical grounding |
| Fty0wTcemV.md | 6.00 | R2 | DELIFT: multi-stage fine-tuning data selection; comparable scope, weaker effect sizes |
| ouRX6A8RQJ.md | 6.40 | R2 | CoT evaluation via information theory; narrower scope, weaker experiments |
| 1GTARJhxtq.md | 5.75 | R2 | Perplexity-based pruning with small reference models; similar cross-model transfer finding |
| DKkQtRMowq.md | 5.75 | R2 | Diversity-aware score curation; narrower task coverage |

**Round 1 bracket**: 5.5–7.5

**Round 2 narrowing**: The most topically similar mid-range anchors are DELIFT (6.0) and ouRX6A8RQJ (6.4). This paper is clearly stronger than both: it covers a harder application (long-CoT competition math), has larger effect sizes, more comprehensive baselines, multiple domains, and cross-model transfer. It is also more comprehensive than 1GTARJhxtq (5.75) despite sharing the proxy-model insight. The paper does not reach the theoretical rigor of DiSF (8.0). The RL evidence is thin and the length confound is only partially addressed. The paper sits meaningfully above the 6.0–6.4 cluster but the methodological gaps prevent reaching 7.0+.

**Final Score: 6.5 — Weak Accept**

The paper makes a concrete, well-validated contribution to reasoning data selection. The SFT findings are robust and the cross-paradigm coverage is meaningful. The length confound and thin RL evidence are real concerns that should be addressed in revision, but they do not invalidate the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>