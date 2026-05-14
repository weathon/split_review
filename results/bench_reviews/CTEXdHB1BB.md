Now I have all the information I need. Let me write the final consolidated meta-review.

---

## Summary

This paper proposes CANON (Conditional Advantage Estimation), a method for incorporating training-metric signals (entropy, response length) into RLVR-based LLM reasoning training without presupposing whether higher or lower metric values are better. The key idea is to split sampled responses into two groups based on a target metric, then compute inter-group advantages (which metric trend yields higher accuracy) and intra-group advantages (which responses are better within the same trend). Experiments on three LLMs across math reasoning and logic tasks show that entropy-based CANON-Inter improves math accuracy (+1.9 pts over DR.GRPO) while CANON-Intra excels on complex logic (+5.2 pts on hardest subset), and CANON based on response length achieves a better Pareto frontier in the performance–efficiency trade-off.

## Strengths

- **Novel conditional regrouping mechanism**: The core idea of splitting responses by metric value and computing dual (inter/intra) advantages elegantly avoids encoding directional priors (e.g., "lower entropy is better"). This is a principled departure from prior reward/advantage shaping methods that rely on hand-crafted directional preferences. Theorem 1 provides formal backing for when the inter-group advantage yields a stronger signal than DR.GRPO.

- **Convincing evidence of complementary advantage roles**: Table 1 and Figure 2 clearly demonstrate that CANON-Inter (entropy-based) drives math reasoning gains through exploitation (higher accuracy, lower entropy), while CANON-Intra drives complex logic gains through exploration (encouraging reflection/rethinking behaviors). Figure 2f showing the reflection-gain curve crossing zero in sync with logic performance improvements is particularly compelling.

- **Genuine efficiency–performance Pareto improvement**: Section 5.3 and Figure 4c show CANON-Eff establishes a better Pareto frontier than length-clipping and length-reward baselines. At α=0.88, it achieves 2.63× higher performance at low token budgets and 45.5% token reduction at equal performance. The method also avoids the catastrophic collapse observed in the Length Reward (+) baseline (54.8→22.5 when coefficient changes from 0.004 to 0.005).

- **Multi-model, multi-task evaluation**: The method is tested on Qwen2.5-Math-7B, Qwen2.5-Math-1.5B, and Llama3.1-8B across six math benchmarks and three logic reasoning complexity levels (Section 5.2, Table 2). CANON-Dynamic consistently outperforms DR.GRPO across all models and tasks.

- **Insightful analysis of μ–metric relationship**: Figure 5 demonstrates a smooth, monotonic relationship between μ (the inter/intra weighting) and resulting entropy/length trends, showing CANON can steer behavior across a spectrum without rigid rewards. This is a genuinely novel empirical finding.

- **Validating ablation on random regrouping**: Table 12 shows that random regrouping (splitting responses arbitrarily rather than by a meaningful metric) yields no improvement over DR.GRPO, confirming that the gains come specifically from regrouping by informative metrics, not from the two-group comparison structure alone.

- **Theoretical selectivity proof (Theorem 2)**: The proof that CANON amplifies only the influence of the grouping metric and not independent conditions distinguishes it from naive numerical advantage scaling (validated by the failure of direct scaling in Table 4).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No statistical significance reporting across experiments**: All main results (Tables 1–4, Figures 2–6) present single-number accuracies without confidence intervals, standard deviations, or multiple-seed replication. While multi-seed training of 7B models with RL is expensive and single-run reporting is common in this subfield, the small size of benchmarks like AIME 24 (30 problems) combined with Avg@10 evaluation makes the modest gains (e.g., +1.9 points on math) somewhat fragile. However, the training-dynamics evidence (Figure 2) and the consistent pattern across models/tasks partially mitigates this concern.

- **Missing direct GRPO/RLOO/ReMax baseline numbers in the main results**: The paper lists ReMax, REINFORCE++, RLOO, and GRPO as baselines (Section 5.1) but Table 1 only reports DR.GRPO. While DR.GRPO is the most relevant comparison (CANON builds directly on DR.GRPO's token-level loss and the paper follows its training setup), showing at least vanilla GRPO numbers would strengthen the claim of improvement over prior methods. The entropy-specific baselines (Entropy Adv, Clip-Cov) appear only in the ablation (Table 4) rather than the primary tables.

- **Scheduling strategy selection could benefit from clearer protocol**: Four scheduling strategies are tried and the best is selected per model (Appendix C.6 states selection is "based on training performance"). While this is more defensible than test-set selection, the protocol for how "strong performance in both scenarios" is determined could be more transparent. This concerns only the CANON-Dynamic results (Section 5.2), not the core CANON-Inter/CANON-Intra results in Table 1 which use fixed μ.

- **Theorems address advantage magnitude ratios, not policy improvement**: Theorems 1–2 compare the magnitude of CANON advantages to DR.GRPO advantages, but do not directly characterize how this translates to improved policy optimization. This is clearly scoped in the paper and is a reasonable level of theoretical analysis for an empirical methods paper, but limits the formal guarantees.

### Trivial

- The paper's title contains a formatting artifact ("REA## SONING") from PDF extraction; this is not an author error.
- Some table rendering in the extracted text is garbled (parser artifact, not an author issue).

## Nice-to-Haves

- Running at least 3 seeds for the main CANON-Inter/CANON-Intra vs. DR.GRPO comparison on the primary model (Qwen2.5-Math-7B) and reporting mean ± std would substantially strengthen the empirical claims, particularly for the AIME benchmarks.
- Including vanilla GRPO numbers in Table 1 (even if expected to underperform DR.GRPO) would provide a more complete picture of where CANON stands relative to the full family of group-based estimators.
- A formal description of how training-performance-based strategy selection was conducted for CANON-Dynamic would improve transparency.
- Extending the method to multiple metrics simultaneously (acknowledged as future work in the limitations section).

## Removed Points

*The following points were flagged by the harsh critic but are removed or substantially weakened after verification against the paper:*

1. **"Dynamic scheduling strategies selected directly on test benchmarks"** — **REMOVED**. Appendix C.6 explicitly states selection was "based on training performance," not test-set metrics. The main text's phrasing ("achieve strong performance in both scenarios") is ambiguous but the appendix clarifies. This criticism is based on a misreading.

2. **"No comparison with DAPO"** — **REMOVED**. DAPO is an RL training system (with importance sampling, novel training paradigms); CANON is an advantage estimation method. They address different aspects of the RLVR pipeline. The paper appropriately uses techniques from DAPO (clip-higher, length bias correction) and cites it. Demanding comparison with every RL system is scope creep.

3. **"Theorem 2's independence assumption is unrealistic"** — **REMOVED as a weakness**. The paper presents Theorem 2 as an idealized analysis showing that *under independence*, CANON selectively amplifies only the target metric. This is a standard theoretical-analysis-for-insight pattern. The paper does not claim real metrics are independent, and the empirical validation (Table 4, random regrouping) provides practical confirmation of selectivity. Moved to Nice-to-Haves as a suggestion to discuss the independence assumption's practical implications.

4. **"Stability claim relies on a single observation"** — **REMOVED**. The stability claim is supported by Figure 4c, which shows a smooth Pareto frontier across multiple α values (0.5, 0.7, 0.8, 0.88, 0.96), contrasted with the Length Reward (+) baseline's sharp collapse. The single cliff example is illustrative, not the sole evidence.

5. **"Entropy Adv and Clip-Cov appear only in ablation"** — **KEPT as a minor concern** (see Minor weakness about baseline placement) but downgraded from the harsh critic's framing as a critical methodological gap.

## Novel Insights

The most interesting finding that emerges from the reviews but goes beyond the paper's own stated contributions is the hierarchical, monotonic relationship between μ and metric trends (Figure 5). As μ increases from 0.0 to 1.0, entropy smoothly decreases — showing that the inter/intra weighting acts as a continuous "dial" for steering training dynamics. This is not merely a hyperparameter to tune; it is a principled mechanism for navigating the exploration–exploitation trade-off without needing to encode directional preferences in the reward function. This finding complements but goes beyond the paper's stated contributions about avoiding directional bias.

## Suggestions

- Add standard deviation / confidence intervals for the main Table 1 results, at minimum for the AIME benchmarks where small evaluation sets make point estimates unreliable. Even 2–3 seeds on the primary model would substantially improve credibility.
- Clarify the scheduling strategy selection protocol: state explicitly in the main text that selection is based on training-set performance (as the appendix does), and describe what metric was used for the "strong performance in both scenarios" criterion.
- Consider adding a brief discussion in Section 4.2 about the practical implications of Theorem 2's independence assumption — when might metrics be correlated enough in practice to partially violate the selectivity property?
- Report at least DR.GRPO and GRPO numbers side-by-side in Table 1, since GRPO is the foundational method that DR.GRPO and CANON both modify.

## Score and Decision

**Calibration anchors considered:**

| Path | Avg Score | Comparison to CANON |
|------|-----------|---------------------|
| ExGRPO (`701tjQXWVk`) | 6.00 | More thorough experiments (5 models, broader benchmarks), but methodologically less novel (experience replay). CANON is weaker experimentally but stronger methodologically. |
| QAE (`WDP5b3mtFV`) | 5.50 | Comparable: novel advantage estimation method, strong theory, good experiments. QAE has stronger theoretical safety guarantees; CANON has a more flexible dual-advantage framework. |
| RiskPO (`KjHB7rebQO`) | 5.50 | Comparable: principled alternative to mean-based GRPO, good benchmarks. RiskPO has more benchmarks; CANON has more task diversity (math + logic). |
| Scaf-GRPO (`bOwVr0yr7r`) | 5.50 | Comparable novelty, but Scaf-GRPO has a more severe weakness (teacher model dependency). CANON is more self-contained. |
| TP-GRPO (`LZZENDlZt9`) | 5.00 | CANON has stronger evidential support and fewer methodological gaps than TP-GRPO. |
| REPO (`E8MR8jgEeZ`) | 4.00 | CANON is clearly stronger: more novel, better experiments, more complete evaluation. |
| GRPO-λ (`iRWqcnBlLQ`) | 4.00 | CANON is methodologically richer and has more comprehensive experiments. |
| Demystifying GRPO (`8gk7qmKSRv`) | 3.00 | Not comparable (analysis-only paper). CANON has both analysis and a novel method. |
| LSPO (`2Tg9RhHsSU`) | 2.50 | CANON is substantially stronger across all dimensions. |

CANON's contribution — conditional regrouping to incorporate metric signals without directional bias — is genuinely novel and well-executed. The dual-advantage framework is principled, theoretically grounded, and empirically validated across multiple models and tasks. The experimental evaluation, while having minor gaps (no statistical reporting, some missing baselines), is thorough by the standards of this subfield and supports the core claims. The paper clearly demonstrates when and why inter-group vs. intra-group advantages matter, and the efficiency analysis shows practical value.

Compared to anchors: CANON is stronger than the 4.0-level papers (REPO, GRPO-λ) and substantially above the 2.5–3.5 rejected papers. It is comparable in quality to the 5.0–5.5 accepted posters (RiskPO, QAE, Scaf-GRPO), with real strengths in novelty and analysis balanced by minor experimental gaps that prevent it from reaching the 6.0 level of ExGRPO's experimental thoroughness.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>