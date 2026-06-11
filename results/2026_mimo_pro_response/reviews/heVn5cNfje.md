Now I have sufficient calibration data. Let me finalize the review.

**Calibration analysis:**

- **Rethinking Data Selection at Scale (4.40, Reject)**: Finds random selection nearly sufficient; much weaker evidence than HES paper.
- **Rule-Based Rating (5.75, Reject)**: Decent methodology but limited improvements; HES has stronger SFT results.
- **3DS (5.75, Reject)**: Limited domain (medical); HES has broader coverage.
- **DELIFT (6.00, Accept)**: Data-efficient fine-tuning via submodular functions; HES paper has more paradigm coverage and broader experiments.
- **Improving Pretraining Data (6.00, Accept)**: Novel but limited to 160M models; HES has larger-scale experiments.
- **What Makes Good Data (6.33, Accept)**: More analytical but narrower evaluation; comparable contribution level.
- **Understanding CoT (6.40, Reject)**: Interesting information-theoretic analysis but limited to toy/GSM8K.
- **Combatting Dimensional Collapse (8.00, Accept)**: Clearly stronger with theoretical grounding; HES paper is below this level.

**Bracket**: Round 1 suggested 5.5-7.5. Round 2 narrows to **6.0-7.0**. The HES paper is clearly stronger than the reject papers at 5.75 and below, comparable to the accept papers at 6.00-6.33, but below 7.5+ due to motivational gap, no variance, and thin RL.

**Final score: 6.5** — slightly above the 6.00-6.33 accepts due to stronger SFT evidence, cross-model transfer, and breadth of paradigms, but held back from 7+ by the motivational inconsistency and thin RFT/RL support.

---

## Summary
This paper proposes High-Entropy Sum (HES), a training-free metric that sums the entropy of the top 0.5% highest-entropy tokens in a reasoning trace to quantify reasoning quality. The authors demonstrate HES-guided data selection across SFT, RFT, and RL paradigms, showing that training on top-HES subsets matches or exceeds full-dataset performance while the lowest-HES data is actively harmful.

## Strengths
- **Very strong SFT evidence across multiple models, datasets, and domains.** Tables 1–4 show that Highest-HES-20% matches or exceeds Full-Dataset performance across Qwen3-8B-Base (31.14% vs 32.61% AVG, Table 1), DeepSeek-R1-Distilled-Qwen-7B (34.61% vs 30.22%, Table 2), Code (Table 3), and STEM (Table 4) domains. The ablation is comprehensive with 12 selection strategies in Table 1, demonstrating clear superiority over entropy, length, and difficulty baselines.
- **Removing lowest-HES data boosts performance beyond full-dataset training.** Highest-HES-80% achieves 35.36% vs Full-Dataset 32.61% (Table 1), while Lowest-HES-20% collapses to 14.90%, confirming low-HES samples are harmful noise rather than merely uninformative.
- **Cross-model proxy selection demonstrates cost-effective curation.** Using Qwen3-0.6B to compute HES for selecting data to train Qwen3-8B achieves 32.12% AVG, closely matching 8B self-selection (31.14%) — Table 1, reducing inference cost by over an order of magnitude.
- **HES is the only training-free metric enabling RL selection to beat full-batch.** In Table 6, Pos-High, Neg-Rand achieves 21.30% vs Full-Batch 20.63%, while difficulty (20.27%) and length (20.23%) baselines do not.
- **Simple and training-free.** HES requires only a single forward pass and a sum operation — no reward model, no additional training.

## Weaknesses

### Fatal
None

### Major
- **Motivational gap between discriminative ability and selection use.** Figure 1 shows incorrect samples have *higher* mean HES (0.68) than correct samples (0.29), demonstrating HES discriminates correct from incorrect. However, the actual application ranks *correct-only* samples and selects highest-HES ones as best training data. The paper never explicitly bridges this: it should argue that among correct solutions, high HES indicates complex, navigated reasoning paths with higher learning value. The assertion "A higher HES score signifies a greater diversity and complexity of reasoning patterns, indicating a higher learning value" (line 36) is stated without connecting it to the discriminative result or validating it with analysis of what high-HES correct solutions look like. This is a gap in the logical chain, not in the experiments — the results may be valid, but the stated motivation does not explain them.

- **No variance or statistical significance reported.** All results are single-run averages. For SFT, the gains are large enough (2–5+ points) to be convincing. But for RFT (gains of ~1–2 points across Table 5) and especially RL (0.67-point difference: 21.30% vs 20.63% in Table 6), the absence of variance reporting makes it impossible to determine whether these differences are real or noise. This undermines the "unified" claim across all three paradigms.

- **RL experiments too thin to support "unified" framing.** The RL results cover a single model (1.5B), single dataset (DeepScaleR), and single algorithm (GRPO). The headline gain over Full-Batch is 0.67 points. This is insufficient evidence to claim HES works across RL in general. The paper should either expand RL experiments or soften the "unified" claim.

### Minor
- **Relationship to Forking-Only not discussed.** Table 1 includes Forking-Only (100% data, loss only on high-entropy tokens): it achieves 32.51%, nearly matching Full-Dataset (32.61%). This raises the question: does HES-based sample selection work partly because it concentrates compute on samples with more high-entropy tokens, effectively a coarser version of Forking-Only at the sample level? The paper should discuss this relationship.

- **Unexplained RFT anomaly.** In Table 5, Global Pool k=2, Random achieves 58.35% on GPQA while Highest-HES achieves 42.30% — a 16-point reversal that is anomalous and unexplained.

- **Typo in Eq. 3 description.** Line 127: "different from AvgHE" should read "different from AvgE" since the metric being defined *is* AvgHE.

### Trivial
- **Repeated paragraph at lines 232–236.** The RFT results section has a duplicated paragraph (copy-paste error).

## Nice-to-Haves
- Qualitative analysis of what high-HES vs low-HES correct solutions look like (e.g., reasoning length, branching, self-correction patterns) would strengthen the core claim significantly.
- Sensitivity analysis (Section 4.4) is done only for SFT; extending to RFT/RL would strengthen robustness claims.
- Ablation crossing HES sample selection with Forking-Only token-level loss to disentangle the two mechanisms.
- Additional RL setups (e.g., another model size or dataset) to substantiate the "unified" claim.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Formatting/typo issues (repeated paragraph, AvgHE/AvgE typo) are minor and noted above but do not affect the core contribution.

## Novel Insights
The key novel finding is that a simple, training-free metric — summing only the top 0.5% highest-entropy tokens — outperforms more complex alternatives (total entropy sum, average entropy, difficulty-based selection) for identifying high-quality reasoning training data across SFT, RFT, and RL. The finding that the lowest-HES data is not merely uninformative but actively harmful (14.90% vs 25.89% for random 20% in Table 1) is particularly striking and practically useful for data curation. The cross-model transfer result (0.6B proxy ≈ 8B self-selection) further suggests HES captures intrinsic data complexity rather than model-specific artifacts, which has practical implications for cost-effective data pipelines.

## Suggestions
- Add variance reporting (3+ runs) for RFT and RL experiments — this is the single most impactful improvement.
- Explicitly argue why high-HES correct solutions are better training data, ideally with qualitative examples of what distinguishes them.
- Expand RL experiments to at least one additional model or dataset, or soften the "unified" claim.
- Discuss the relationship between HES and Forking-Only training.
- Explain or investigate the GPQA anomaly in RFT Global Pool k=2.

## Reporting: Calibration Anchors

| Anchor Paper | Avg Human Score | Round | Comparison |
|---|---|---|---|
| KL Divergence Optimization for GFlowNets | 1.00 | 1 | Weak, unrelated GFlowNet paper — much weaker |
| Systematic Review of LLMs | 1.00 | 1 | Survey paper, rejected — much weaker |
| Jailbreaking LLMs with CoT | 1.40 | 1 | Security paper, rejected — much weaker |
| Cross-Lingual Humanoid Robots | 1.00 | 1 | Off-topic, rejected — much weaker |
| Self-Consuming Training Loop | 3.20 | 1 | Interesting but limited LLM analysis — weaker |
| Language Models for Textual Data Valuation | 2.00 | 1 | Data valuation paper, rejected — weaker |
| Entropy of Language Models | 3.00 | 1 | Limited entropy analysis — weaker |
| Disentangling Representation and Selection | 3.00 | 1 | Data pruning study, narrower scope — weaker |
| Rethinking Data Selection at Scale | 4.40 | 1 | Finds random nearly sufficient; HES clearly stronger |
| Entropy-Guided Reliability (SREF) | 3.67 | 1 | Different application of entropy — weaker |
| Diversity Coefficient as Data Quality Metric | 4.00 | 1 | Data quality metric, limited experiments — weaker |
| Priority on High-Quality Instruction Data | 4.75 | 1 | Data selection for instruction tuning — weaker |
| Rule-Based Rating of LLM Training Data | 5.75 | 1 | DPP-based rule selection, decent but limited gains — comparable but HES stronger |
| Improving Pretraining Data Using Perplexity | 6.00 | 1 | Novel but limited to 160M models — comparable |
| Understanding CoT Through Information Theory | 6.40 | 1 | Interesting but limited to toy/GSM8K — comparable |
| 3DS: Decomposed Difficulty Data Selection | 5.75 | 1 | Domain-specific (medical), narrower — weaker |
| DELIFT | 6.00 | 2 | Submodular data selection across fine-tuning stages — comparable, HES has broader paradigm coverage |
| What Makes Good Data for Alignment (DEITA) | 6.33 | 2 | Comprehensive study, narrower evaluation — comparable |
| Combatting Dimensional Collapse (DiSF) | 8.00 | 1 | Strong theory + extensive experiments — clearly stronger than HES |

**Round 1 bracket: 5.5–7.5.** The HES paper is clearly stronger than rejects at 4.40–5.75, comparable to accepts at 6.00–6.33, and below the 8.00-level DiSF paper.

**Round 2 narrowed to 6.0–7.0.** DELIFT (6.00, Accept) and DEITA (6.33, Accept) are the closest comparisons. HES has broader paradigm coverage (SFT/RFT/RL) and stronger SFT evidence than both, but the motivational gap and thin RL hold it back from 7+.

**Final score: 6.5** — The strong SFT contribution, simplicity, cross-model transfer, and breadth across domains earn it above the 6.00-6.33 accept papers, but the motivational inconsistency, absent variance reporting, and thin RFT/RL evidence prevent it from reaching 7.0+.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>