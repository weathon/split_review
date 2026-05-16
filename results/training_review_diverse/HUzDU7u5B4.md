Now I have all the information verified. Here is my consolidated final review.

---

## Summary

This paper proposes RLFH (Reinforcement Learning for Hallucination), an online reinforcement learning framework that mitigates hallucination by constructing token-level dense rewards from atomic-fact verification. The method decomposes model responses into atomic facts, evaluates each fact's truthfulness (five-class veracity) and informativeness (five-point scale) using an LLM-based assessment pipeline, converts these statement-level judgments into token-level rewards via LCS mapping, and optimizes the policy model with PPO. Experiments on HotpotQA, SQuADv2, and Biography benchmarks show consistent FactScore improvements over both aligned models (e.g., +17.9% over Vicuna) and prior learning-based methods (e.g., +2.0% over FACT).

## Strengths

1. **Novel on-policy fine-grained token-level reward framework.** Prior learning-based methods for hallucination mitigation rely on off-policy data and instance-level rewards, leading to distribution shift and imprecise signals. RLFH samples responses online, decomposes them into atomic facts, assigns statement-level evaluations, and traces these back to individual tokens. This is a genuine methodological contribution that directly addresses the limitations of coarse-grained feedback (Section 3.2, Figure 3).

2. **Consistent improvement across all three datasets.** RLFH achieves the highest FactScore on HotpotQA (0.655), SQuADv2 (0.683), and Biography (0.474) compared to all baselines including strong aligned models (Vicuna, Zephyr, Llama2 Chat, Orca2) and learning-based methods (ITI, DOLA, FACT). The gains generalize out-of-distribution despite training only on HotpotQA (Table 1).

3. **Atomic-fact decomposition with hierarchical verification.** The paper introduces a structured pipeline that extracts atomic facts hierarchically (response → sentences → statements), classifies each into five veracity labels (*Correct*, *Hedged Correct*, *Vague*, *Hedged Wrong*, *Wrong*), and jointly assesses informativeness. This fine-grained decomposition allows the model to receive distinct signals for different types of content, avoiding the side effects of monolithic rewards (Section 3.1, Figure 2).

4. **Automated LLM-based fact assessment enabling online use.** The Mixtral-8x7B-based annotation pipeline can be deployed without human annotation, making the online RL loop practical and scalable. The ablation on annotation models (Table 3) shows that several open-source LLMs can provide useful supervision, demonstrating the framework's accessibility.

5. **Behavioral analysis demonstrates learned calibration.** Post-training analysis shows the model generates more statements in high-accuracy ranges and fewer in low-accuracy ranges, and selectively refuses questions where it originally performed poorly (Figures 4–6). This supports the claim that RLFH helps align generation with the model's knowledge boundaries.

## Weaknesses

### Fatal
None.

### Major

1. **FactScore is not validated for QA datasets, and no standard QA metrics are reported.** FactScore was designed for evaluating factuality in *biography* generation by decomposing text into atomic facts. Applying it wholesale to HotpotQA and SQuADv2 is questionable: a correct short answer (e.g., "Paris") yields few atomic facts, while a verbose but partially incorrect answer could score higher on raw fact count. The paper does not report standard QA metrics (F1, EM) for these datasets, nor does it discuss whether FactScore correlates with them. Since the reported improvements over FACT are small (0.008–0.017), this metric choice makes the evaluation hard to interpret. The paper claims FactScore is "a well-established metric for assessing the factuality of long-form generation" (line 226), which is true, but applying it to QA datasets where responses are not necessarily long-form requires justification that is absent.

2. **The annotation model ablation reveals a concerning inconsistency.** When Vicuna-7b is used as the annotation model (for training), the trained model achieves the *highest* FactScore (0.697 vs. 0.655 with the default Mixtral) but generates the *fewest* correct statements (4.207 vs. 13.05 with Mixtral). The paper mentions this briefly (lines 367–369) but does not adequately explain why a weaker annotation model yields a higher evaluation score. This suggests that FactScore can be inflated by shorter, more conservative responses, which directly undermines confidence in the metric as a reliable indicator of overall quality. The FactScore for the Vicuna-7b-supervised model (0.697) also exceeds all baselines in Table 1, which would imply RLFH with a cheap annotation model outperforms the full pipeline — an implausible conclusion that the paper should have discussed in depth.

3. **Drop in response ratio is not properly accounted for in evaluation.** RLFH's response ratio drops markedly (0.645 vs. 0.910 for Vicuna, 0.945 for FACT on HotpotQA; 0.692 vs. 0.830 for Vicuna on Biography). FactScore is computed only on responded questions (refusals yield no facts), so the model can achieve higher scores by selectively answering easier questions. The paper acknowledges this (lines 233–239) and introduces an informativeness reward (line 136) to counter the "trivial hack," but it does not provide a combined metric that penalizes refusals (e.g., assigning zero FactScore to refused questions). As a result, it is unclear whether the reported FactScore improvements reflect better generation or increased selectivity. Figure 6 helps by showing the model refuses questions where it originally performed poorly, which is a reasonable behavior, but the net utility of the trade-off between selectivity and accuracy is unresolved.

### Minor

4. **No statistical significance testing or variance reporting.** The evaluation sets are small (256 for HotpotQA, 191 for SQuADv2), the improvements over the strongest learning-based baseline (FACT) are tiny (0.008–0.017), and no confidence intervals, standard deviations, or multiple-run results are reported. Without this information, the claimed improvements may be within the noise of the evaluation pipeline itself. This is especially concerning given that FactScore is an LLM-based metric with inherent variability.

5. **No human evaluation.** All evaluations rely on the same automated FactScore pipeline (run by GPT-4), which inherits the pipeline's potential biases. A small-scale human evaluation of factual accuracy and fluency (e.g., on 50–100 sampled responses) would substantially strengthen the claims. The paper explicitly states it aims to operate "without human intervention" (line 54), which is a strength of the *method*, but the *evaluation* should still include human judgment as ground truth.

6. **Framing disconnect between "internal knowledge" and external supervision.** The paper repeatedly frames hallucination as "misalignment of the models' generation and their internal knowledge" (line 34) and states that RLFH "enables LLMs to explore the boundaries of their internal knowledge" (line 7). However, the reward signal comes entirely from external ground-truth documents (line 115). While using external knowledge to improve factuality is a perfectly valid approach, the "internal knowledge exploration" narrative is misleading — the method penalizes factual errors according to an oracle, not the model's own knowledge boundaries. This conceptual gap weakens the paper's otherwise clear framing.

7. **Retrieval method for supporting contexts is underspecified.** The paper states "We retrieve the relevant supporting materials… from the external reference document set" (line 115) but does not describe how this retrieval is performed (e.g., which retriever, top-k, relevance scoring). Since the accuracy of fact verification depends entirely on whether the correct evidence is retrieved, this omission harms reproducibility.

### Trivial

8. The "+17.9% FactScore" claim (line 47) is the average of per-dataset relative improvements over the base Vicuna model. It is mathematically correct but could be misleading if read as an absolute improvement or a single aggregated FactScore. The paper should clarify this.

9. PPO hyperparameters (learning rate, batch size, KL penalty coefficient, rollout length, reward normalization) are not reported in the experimental section. TRLX (cited) provides defaults, but explicit reporting would aid reproducibility.

## Nice-to-Haves

- **Supervised fine-tuning baseline.** Comparing RLFH to supervised fine-tuning on the same atomic-fact correctness labels (without the RL objective) would isolate whether the benefit comes from the online RL or simply from the fine-grained signal itself. This is the most informative ablation the paper lacks.
- **Combined metric penalizing refusals.** Reporting FactScore with refusals scored as zero (or a comparable unified metric) would directly address the response-ratio concern.
- **Human validation of the fact assessment pipeline.** Even a small study measuring agreement between LLM and human judgments on a sample of atomic facts would calibrate confidence in the training signal.
- **Analysis of computational cost.** The pipeline uses Mixtral-8x7B to supervise a 7B model. Discussion of latency, throughput, and cost would help assess practical applicability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Does not mention recent work on token-level rewards for factuality (e.g., Self-Rewarding LMs)"** — Removed per the rule against demanding missing related works (no external sources to confirm existence).
- **"Missing appendix with Table of functions f and g"** — Removed per the rule that the parser strips appendix content; these exist in the original submission.
- **"The stray line in Table tab:anno is a typesetting error"** — Removed per the rule that formatting/parsing artifacts are not author errors.
- **"Weaknesses that demand addressing problems outside the stated scope"** (e.g., asking the benchmark/dataset paper to do X/Y/Z not relevant to its class) — Not applicable here; the paper is a methods paper and criticisms are in-scope.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension that the paper does not fully resolve: fine-grained token-level rewards demonstrably shift model behavior toward more conservative answering, which raises FactScore but at the cost of coverage. The annotation model ablation (Vicuna-7b → highest FactScore, fewest correct statements) is the starkest illustration: it suggests the evaluation metric and the method's training signal may be co-optimizing for brevity and selectivity rather than genuine informativeness. This insight — that fine-grained factual rewards can trade off against helpfulness in subtle ways — is important for future work on RL for factuality, but it is a limitation the current paper only partially acknowledges.

## Suggestions

- **Validate the FactScore metric for QA settings** by reporting standard QA metrics (F1, EM) alongside FactScore on HotpotQA and SQuADv2, or provide evidence that FactScore correlates with human judgments for these datasets.
- **Run experiments with at least 3 random seeds** and report means/standard deviations for the main results, especially given the small evaluation sizes and incremental improvements over FACT.
- **Add a combined evaluation metric** that assigns a zero FactScore to refused questions, or report FactScore×ResponseRatio to give a more complete picture of utility.
- **Conduct a small human evaluation** (50–100 samples) comparing RLFH outputs against FACT and Vicuna on factual accuracy, to validate the automated metric.
- **Discuss the Vicuna-7b annotation anomaly in detail** — analyze whether it extracts fewer statements, is more lenient, or produces different model behavior — and explain why the FactScore is higher despite lower absolute correct statements.
- **Clarify the retrieval method** used for supporting contexts in fact verification.
- **Report PPO hyperparameters** explicitly in the paper.

## Score and Decision

This paper proposes a conceptually appealing method (on-policy fine-grained token-level RL for hallucination) with a novel automated fact-assessment pipeline. The core idea is sound and the behavioral analysis provides useful insights. However, the empirical support has several gaps: the evaluation metric is used without validation on QA datasets, the annotation model ablation reveals a troubling inconsistency, the response-ratio drop is not properly factored into evaluation, and no statistical significance testing is provided. The improvements over the closest baseline (FACT) are small (0.008–0.017 FactScore). These weaknesses are addressable but collectively weaken the contribution's convincingness. The paper has genuine merit and the method is promising, but the current evidence does not rise to the level of a strong acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>