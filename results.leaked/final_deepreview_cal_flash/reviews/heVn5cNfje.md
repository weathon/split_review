Now I have a comprehensive understanding of the paper and the calibration landscape. Let me produce the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces High-Entropy Sum (HES), a training-free metric that computes the sum of entropy values over only the top 0.5% highest-entropy tokens in a reasoning trace, rather than averaging over all tokens. The authors argue this focuses on critical "forking points" where the model is most uncertain, and demonstrate that HES-guided data selection improves performance over baselines across three major training paradigms: Supervised Fine-Tuning (SFT), Rejection Fine-Tuning (RFT), and Reinforcement Learning (RL). Experiments across multiple models (Qwen3-8B, DeepSeek-R1-7B, Qwen3-1.5B), datasets, and domains (math, code, STEM) show consistent gains, including surpassing full-dataset performance when low-HES data is pruned.

## Strengths

- **Well-motivated metric with clear discriminative ability.** Figure 1 shows that HES produces near-separated distributions for correct (mean 0.29) and incorrect (mean 0.68) responses, while average entropy (0.52 vs. 0.53) and average high-entropy entropy (0.82 vs. 0.82) fail to distinguish them. The intuition that global averaging dilutes critical signals from a small number of high-uncertainty tokens is clearly articulated and empirically supported.

- **Consistent gains across SFT, RFT, and RL — three distinct training paradigms.** In SFT (Table 1), training on the top-80% HES samples achieves 35.36% average accuracy, surpassing the full dataset (32.61%) despite using 20% less data. In RFT (Table 5), HES-based selection consistently outperforms random, length, and difficulty baselines in both per-query and global-pool settings. In RL (Table 6), the asymmetric "Pos-High, Neg-Rand" strategy achieves 21.30%, outperforming Full-Batch (20.63%) while using only half the per-step data. This breadth is the paper's strongest asset.

- **Generalisation across models, datasets, and domains.** Core trends hold for Qwen3-8B (Table 1) and DeepSeek-R1-Distilled-7B (Table 2), extend to code generation (Table 3) and scientific reasoning (Table 4), and replicate on three different training datasets. This robustness lends credibility to HES as a general-purpose signal rather than a configuration-specific fluke.

- **Practical small-to-large model transfer.** Using a 0.6B proxy model to screen data for an 8B model achieves 32.12% average accuracy, comparable to the 8B's self-selection (31.14%) while reducing inference cost by an order of magnitude (Table 1). This is a practically valuable result that directly addresses a deployment bottleneck.

- **Non-obvious insight about negative sample diversity in RL.** Table 6 shows that constraining negative samples (e.g., "Pos-High, Neg-Low" at 19.50%) hurts performance, while pairing high-HES positives with random negatives (21.30%) works best. This finding goes beyond a simple "select the best" heuristic and provides actionable guidance for RL data selection.

## Weaknesses

### Fatal
None.

### Major

- **No measure of uncertainty or statistical significance for any result.** Every experiment is reported as a single point estimate with no confidence intervals, standard deviations, or multiple random seeds. Given the well-known sensitivity of LLM fine-tuning to initialization and data ordering, the reader cannot assess whether reported improvements (e.g., HES-80% at 35.36% vs. Full-Dataset at 32.61% in Table 1) are reliable or within noise. This is especially concerning for the Random-20% baseline (25.89%), which is far below other data-selection strategies and suggests an unlucky draw — but without replicates, this cannot be determined. The issue affects every claim in the paper and substantially weakens the evidential foundation.

- **Incomplete baseline comparisons in RFT and RL undermine the "unified" claim.** In SFT, the paper thoroughly compares HES against a full set of entropy-based alternatives: average entropy (AvgE), average high-entropy entropy (AvgHE), and entropy sum (ES), showing HES outperforms them (Table 1). In RFT (Table 5) and RL (Table 6), these same baselines are completely absent; only random, length, and difficulty are used. Without showing that HES also outperforms AvgE, AvgHE, and ES in RFT and RL, the central claim that HES is a **unified** superior metric across paradigms is unsupported for two of the three paradigms. The RFT and RL experiments only establish that HES beats weak heuristics, not that it is the best entropy-based metric.

### Minor

- **Framing of HES as a "reasoning quality" metric is inconsistent with the evidence.** Figure 1 shows that incorrect responses have significantly higher HES (mean 0.68) than correct responses (mean 0.29). If HES directly measured "quality," incorrect samples would be scored higher. The paper's actual logic — that HES measures reasoning complexity/uncertainty, and that among correct responses higher complexity implies greater learning value — is plausible but requires clearer articulation. Several passages (e.g., "represents higher quality" in Section 3.1) create unnecessary confusion.

- **The 0.5% high-entropy token threshold is validated only for SFT.** The sensitivity analysis in Section 4.4 thoroughly tests different token ratios (0.005, 0.05, 0.5, 1.0) for SFT in math, code, and STEM domains. However, no equivalent analysis is provided for the RFT or RL settings, where the optimal ratio could differ due to different data distributions or training objectives.

- **RL experiments are limited in scope.** Only a single 1.5B model (DeepSeek-R1-Distilled-Qwen-1.5B) and one dataset (DeepScaleR) are used. The absolute performance is low (e.g., AIME24 at 35.42% for the best strategy), and the improvement over Full-Batch is modest (21.30% vs. 20.63%). A second model scale or dataset would substantially strengthen confidence that the asymmetric sampling strategy generalises.

### Trivial

None.

## Nice-to-Haves

- **Quantify the HES–length correlation.** The paper already compares HES against a Length baseline, showing HES outperforms it. A more direct analysis (correlation coefficient, length-residualized HES) would cleanly address the residual concern that HES partially captures length-dependent signal.
- **Report computational cost.** The paper calls HES "training-free" but does not quantify its overhead. A brief estimate (e.g., GPU-hours for computing HES on 100k samples) would help practitioners evaluate the cost-benefit tradeoff.
- **Include a learned-data-selector baseline.** While the paper's goal is to avoid costly external models, a comparison with a trained Q-value model or process reward model would establish where HES sits on the cost-performance Pareto frontier.

## Removed Points

These points were considered and removed from the main review for the reasons stated:

- **"Training-free" is an overstatement** (Harsh Critic's Section-by-Section note on Abstract/Introduction). Computing token-level entropy does require a forward pass and softmax, but the paper contrasts HES against methods requiring *additional trained models* (e.g., LLM-based selectors, reward models). In that context "training-free" means no extra training, which is accurate. Removed as a parser-level nitpick that misreads the intended contrast.

- **Random-20% may be an unlucky draw** (Harsh Critic's Section-by-Section note on SFT Experiments). This is subsumed by the broader "no statistical significance" weakness above. Keeping it as a separate point would be duplicative.

- **"Forking-Only baseline achieving 32.51 not discussed"** (Harsh Critic's Section-by-Section note). The baseline is listed in the experimental design and shown in Table 1. The paper's contribution is about data *selection*, not training mechanisms, so extended discussion of Forking-Only is outside scope. Removed as scope creep.

- **Missing comparison to learned data selectors** (Harsh Critic's Missing Parts). This is a nice-to-have, not a core weakness. The paper explicitly scopes itself as a "training-free" alternative to these costly methods. Moved to Nice-to-Haves.

- **Strength Finder's generic strengths about "important problem" or "well-addressed"**. Removed generic formulations not backed by specific evidence. Kept only concrete, evidence-anchored strengths.

## Novel Insights

The reviews surface one observation not fully developed in the paper: the asymmetric RL result (high-HES positives + random negatives > all other strategies) suggests a deeper principle. While high-HES samples are more complex and informative, the negative pool benefits from diversity rather than purity. This mirrors the "exploration vs. exploitation" tension in RL but applied to data composition rather than policy updates. The paper demonstrates the effect but does not theoretically analyze why low-HES negatives are counterproductive. A follow-up studying whether this asymmetry generalizes beyond the HES context (e.g., to difficulty-based or uncertainty-based positive selection) would be interesting.

Another observation: the small-to-large transfer result (0.6B → 8B matching 8B self-selection) implies that HES captures data-intrinsic properties, not model-specific artifacts. This is practically important because it means a single cheap screening pass can serve many downstream training runs, decoupling data quality assessment from model scale.

## Suggestions

1. **Add multiple random seeds or bootstrapped confidence intervals** to the main experimental results (at least Tables 1, 5, 6). Even 2–3 seeds with reported mean ± std would dramatically improve the reliability of the evidence.

2. **Include AvgE and AvgHE baselines in the RFT experiments** (Table 5). Since these are the paper's own competitors from SFT, their omission is the single clearest gap. Ideally also include them in the RL experiments (Table 6), though the asymmetric sampling design makes that less straightforward.

3. **Revise the framing around "reasoning quality"** to consistently say "reasoning complexity" or "learning value." Acknowledge explicitly (e.g., in Section 3.1) that HES is higher for incorrect responses because it measures uncertainty, and clarify that the selection strategy uses it as a proxy for learning value *within the pool of correct responses*.

4. **Validate the 0.5% threshold in at least one RFT or RL setting.** A small-scale sensitivity check (p = 0.005, 0.05, 0.5) on a representative subset would increase confidence that the choice is robust across paradigms.

5. **Add a second model scale or dataset to the RL experiment.** Even a smaller-scale replication (e.g., Qwen3-0.6B on a subset of DeepScaleR) would significantly strengthen the generalisability of the RL findings.

## Score and Decision

**Calibration Report**

Round 1 (bracketing) — three searches on "data selection for LLM reasoning training entropy-based metrics":
- Low band (<3.5): anchors at 2.00–3.00 (Reject). These papers had weak methodology or were off-topic. This paper is clearly stronger.
- Middle band (3.5–7.5): anchors at 3.67–6.40. Relevant papers include "Understanding Chain-of-Thought in LLMs Through Information Theory" (6.40, Reject), "Semantic Entropy Probes" (5.50, Reject), and "Pre-Memorization Train Accuracy" (4.25, Reject).
- High band (>7.5): anchors at 8.00 (Accept). These are stronger papers with more polished experimental rigor.

Initial bracket: 5.5–7.0.

Round 2 (narrowing) — two searches inside the bracket:
- DELIFT (6.00, Accept): data selection across three fine-tuning stages. Comparable scope; this paper has broader paradigm coverage (SFT+RFT+RL) but weaker baselines in two paradigms. Similar or slightly stronger.
- What Makes Good Data for Alignment (6.33, Accept): data selection for instruction tuning. Similar analysis quality; this paper has a more novel metric but less analytical depth.
- Perplexed by Perplexity (5.75, Accept): perplexity-based pruning with small models. Similar concept; this paper has broader experimental coverage across paradigms.
- Language Model-Driven Data Pruning (5.75, Reject): active learning with data pruning. Less relevant.

This paper is stronger than the 5.75 anchors (more comprehensive, more paradigms) and comparable to the 6.00–6.33 anchors. It has a genuine methodological gap (missing baselines in two paradigms, no variance) that prevents it from reaching the 7+ tier but is clearly above the 4–5 range. I place it at 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>