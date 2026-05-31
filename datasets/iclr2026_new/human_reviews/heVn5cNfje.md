## Human Reviewer 1

### Summary
This paper introduces High-Entropy Sum (HES), a training-free metric that quantifies reasoning quality by summing the entropy of only the top 0.5% highest-entropy tokens in reasoning sequences. The authors validate HES across three training paradigms (SFT, RFT, and RL), demonstrating that selecting data based on HES can match or exceed full-dataset performance with significantly less data.

### Strengths
1. HES provides a training-free approach to data selection that focuses on critical decision points in reasoning paths, offering a practical alternative to expensive reward models or gradient-based selection methods.
2. The paper systematically evaluates HES across three major training paradigms (SFT, RFT, RL) with consistent improvements, demonstrating the metric's versatility and robustness.
3. Training on just 20% of HES-selected data achieves comparable performance to full datasets, while the top 80% consistently outperforms full-dataset training, suggesting effective noise filtering.

### Weaknesses
1. Figure 1 demonstrates that HES distinguishes between correct and incorrect samples, but this is not equivalent to identifying high- and low-quality samples. High entropy from a language modeling perspective indicates uncertainty, while from an RL perspective it suggests exploration potential, both are model-centric properties. Sample quality, however, should be evaluated based on intrinsic properties like conceptual coverage and reasoning complexity, not just model confidence.
2. The experiments focus exclusively on mathematical reasoning tasks. The generalizability to other domains requiring complex reasoning (e.g., medical reasoning benchmarks like HealthBench, legal reasoning, or scientific domains) remains unexplored.
3. Different models are used across experiments (Qwen3-8B/4B for SFT, DeepSeek-R1-Distilled-Qwen7B for RFT, DeepSeek-R1-Distilled-Qwen-1.5B for RL) without clear justification. This inconsistency makes it difficult to isolate the effects of HES from model-specific behaviors and complicates fair comparison across paradigms.

### Questions
1. Why does the bottom 20% of data cause such dramatic performance degradation? Tables 1-3 consistently show that removing the lowest-HES 20% improves performance significantly. Is this due to annotation errors in the original datasets, or does low HES genuinely identify harmful training samples? Have you investigated the characteristics of these low-HES samples qualitatively?
2. Can you provide empirical evidence for the claim in Line 147 that high-quality reasoning paths navigating multiple challenging forks may receive similar scores to straightforward, low-complexity approaches? This seems counterintuitive to the HES design principle.
3. Why does k=4 outperform k=8 in RFT experiments (Table 4)? Both Global Pool and Per-Query Selection show this pattern. Theoretically, more high-quality samples should not hurt performance.
4. What is the computational overhead of HES in online RL settings? Since each on-policy sampling requires HES calculation, how does this impact training efficiency? Have you explored the trade-off between sampling more trajectories versus the computational cost of HES selection?
5. How does HES perform on out-of-distribution tasks? Table 5 shows HES underperforming Full-Batch on GPQA after RL training. Could you provide more analysis on whether HES-based selection might lead to overfitting to specific reasoning patterns at the cost of generalization?
6. Could you clarify the rationale for using different models across experiments? Was this due to computational constraints, or were certain models specifically chosen for each paradigm? A unified evaluation would strengthen the conclusions about HES's effectiveness.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes High-Entropy Sum (HES) as a data selection metric for reasoning tasks. HES is a training-free metric calculated by summing the entropy of only the highest-entropy tokens(top 0.5\%) within each reasoning sample. The authors comprehensively validate the effectiveness of HES as a selection criterion across three experimental settings(RL, SFT, and RFT), demonstrating its utility for efficiently developing advanced reasoning capabilities in LLMs.

### Strengths
1. Data selection is a fundamental problem in LLM reasoning. If the method proposed in this work is proved effective, it provides a valuable contribution to the community.

2. The proposed HES metric is simple to compute, which facilitates the reproducibility of the experimental results.

3. The paper's experiments are comprehensive, covering SFT, RFT, and RL, which represent three common training paradigms for LLM reasoning.

### Weaknesses
1. The proposed HES metric is computed by directly summing token entropies. For reasoning tasks, high-entropy tokens often represent divergence points or "reasoning branches" [1]. This suggests that HES is likely positively correlated with the response length. Therefore, an analysis of the correlation between HES and response length is essential. In Table 1, after accounting for potential evaluation noise, the performance of the top 20% of data selected using **length** (30.67 average) is very close to that selected using **HES** (31.14 average). Given the significant computational overhead required to calculate entropy over large datasets, it is necessary for the authors to provide a comparison against length as a baseline with a detailed correlation analysis.

2. Following the previous point, the authors must quantify the computational overhead required to calculate HES. This information is necessary to assess the method's practical utility. Generally, computing entropy for a single sample requires a full forward pass, making the overhead comparable to that of a single inference step. If this significant overhead fails to deliver substantial improvements over a simple heuristic-like length, the practical value of HES must be reassessed.

3. The HES metric is inherently model-dependent, as it requires model-specific entropy calculations for each sample. This computational requirement could be expensive for very large-scale models. This raises a question: Can HES derived from a smaller (and computationally cheaper) model be effectively used to select data that yields consistent performance gains for larger models?

4. While the paper addresses a core problem in LLM reasoning, the title "Unified Data Selection for LLM Reasoning" appears overly broad and ambitious for the proposed HES method. HES is a model-dependent strategy that incurs non-trivial computational overhead and, as noted above, faces methodological questions regarding its clear advantage over simpler heuristics. Describing HES as a "Unified Data Selection method" seems to be an overstatement. The authors should reconsider the framing and scope of their contribution.

[1] Wang S, Yu L, Gao C, et al. Beyond the 80/20 rule: High-entropy minority tokens drive effective reinforcement learning for llm reasoning[J]. arXiv preprint arXiv:2506.01939, 2025.

### Questions
Please see weaknesses.

The problem investigated in this paper is undoubtedly valuable. I find HES to be at least a useful metric that offers benefits for LLM data selection. Therefore, I will consider changing my score if the authors can provide convincing clarifications and a strong rebuttal to the aforementioned weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
2

---

## Human Reviewer 3

### Summary
This paper addresses the challenge of efficiently training LLMs for complex, long CoT reasoning, which is often bottlenecked by the need for massive, high-quality datasets. Existing data selection metrics are often ineffective as they average over all tokens, diluting the signal from the few, crucial decision points in a reasoning path.

To solve this, the authors propose the High-Entropy Sum, a simple, training-free metric. Instead of averaging, HES quantifies reasoning quality by summing the entropy of only the top 0.5% highest-entropy tokens in a sample. The intuition is that these few tokens represent the most critical "forking points" where the model is most uncertain and makes its most important decisions.

### Strengths
1. The paper presents HES, a new metric that is easy to compute but very effective. By considering only the top 0.5% of tokens with the highest entropy, HES effectively avoids the “signal dilution” problem found in traditional metrics like average entropy.
2. The authors rigorously test HES across the three main training methods. The experiments, including strong baselines and ablations, clearly show that HES outperforms other entropy-based metrics, as well as length and difficulty heuristics.
3. The paper demonstrates that using HES can lead to significant gains in both performance and efficiency.

### Weaknesses
1. Experiments are not comprehensive.

Based on my experience, data selection for ``Difficulty" should not use most difficult questions, but instead should choose "medium", not too hard but not too easy. Most difficult QA is not good for training, especially for RL.

2. Eval is only in-domain.

The paper’s main weakness is that, although it claims to offer a “unified data selection for LLM reasoning,” it only validates HES on math reasoning datasets. No code or other logical reasoning datasets.

3. Incomplete Competitive Analysis in RFT and RL and even SFT

The paper's experimental design is inconsistent. While the SFT experiments (Table 1) provide an excellent, comprehensive comparison against baselines, the RFT and RL experiments do not. Also, Table 2 and Table 3 for SFT have no other strong baselines.

### Questions
1. Can you conduct experiments on other domains?
2. Can you show RFT and RL experiments with "Difficulty"? Such as medium hard (avg pass rate @ 64 > 0% but < 50%)

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes High-Entropy Sum (HES), a training-free metric for data/trajectory selection in LLM reasoning. HES sums only the top-p% highest-entropy tokens in a response to capture “forking points” where the model is uncertain. The authors use HES to (i) rank SFT data, (ii) pick candidates for RFT, and (iii) design an asymmetric RL sampling scheme (select high-HES positives, random negatives). On math-reasoning datasets (Open-Math-Reasoning, Open-R1-220k) and math/STEM benchmarks (AIME24/25, HMMT23/24/25, OlymMATH, GPQA), they report that training on top-20% HES data matches or exceeds full-dataset SFT and that pruning the bottom-20% improves over full-dataset; HES also beats AvgEntropy, AvgEntropy over high-entropy tokens, and total entropy baselines. RL experiments show the “Pos-High, Neg-Rand” recipe outperforming full-batch despite using half the rollouts.

### Strengths
1. HES is easy to compute from token distributions and is used consistently across SFT/RFT/RL without training additional selectors or reward models. This practical unification is appealing for data-centric pipelines.

2. SFT/RFT ablations are thorough (top/bottom slices, per-query vs global pools, multiple k) and show sizeable gaps between High-HES vs Random/Low-HES; tables make the effect sizes easy to read.

3. The asymmetric sampling result—keep diverse negatives but focus on high-HES positives—provides a practical recipe that beats full-batch with fewer trajectories, which many practitioners would value.

### Weaknesses
1. All datasets and most benchmarks are math; models are Qwen3 variants and DeepSeek-R1 distilled families. It is unclear whether HES transfers to non-math reasoning (code, science QA, multi-modal) or to very different model families.

2. While there is a small sensitivity plot, the theoretical or data-driven rationale for the default percentile and its stability across lengths/models/tasks is limited; AvgHE vs HES comparisons help, but a more systematic hyperparameter study across domains is missing.

3. The pipeline often first filters to correct rollouts, which blurs whether HES measures quality or just difficulty/length. Tighter decontamination and simple causal checks (e.g., control for length/difficulty; test on non-math tasks) are needed to show HES truly beats global metrics.

### Questions
-- How does HES perform on non-math corpora (e.g., code generation with execution checks, GSM8K-style verbal math vs olympiad math, commonsense multi-step QA, open-ended planning)?

-- Does HES still help when the base model already produces short CoT or when responses are heavily compressed?

-- How sensitive are results to sampling temperature/max length, which change token-entropy distributions? Any normalization by length or by per-token calibration?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4