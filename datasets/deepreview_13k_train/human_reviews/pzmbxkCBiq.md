# Understanding Likelihood Over-optimisation in Direct Alignment Algorithms

- Decision: Reject
- Scores: 6, 3, 8, 3

## Abstract
Direct Alignment Algorithms (DAAs), such as Direct Preference Optimisation (DPO) and Identity Preference Optimisation (IPO), have emerged as alternatives to online Reinforcement Learning from Human Feedback (RLHF) algorithms such as Proximal Policy Optimisation (PPO) for aligning language models to human preferences, without the need for explicit reward modelling.
These methods generally aim to increase the likelihood of generating better (preferred) completions while discouraging worse (non-preferred) ones, while staying close to the original model's behaviour.
In this work, we explore the relationship between completion likelihood and model performance in state-of-the-art DAAs, and identify a critical issue of likelihood over-optimisation.
Contrary to expectations, we find that higher likelihood of better completions and larger margins between better and worse completion likelihoods do not necessarily lead to better performance, and may even degrade it.
Our analysis reveals that while higher likelihood correlates with better memorisation of factual knowledge patterns, a slightly lower completion likelihood tends to improve output diversity, thus leading to better generalisation to unseen scenarios.
Moreover, we identify two key indicators that signal when over-optimised output diversity begins to harm performance:
\textit{Decreasing Entropy over Top-$k$ Tokens} and \textit{Diminishing Top-$k$ Probability Mass}.
Our experimental results validate that these indicators are reliable signs of declining performance under different regularisation schemes, helping prevent over-optimisation and improve alignment with human preferences.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
* The paper studies how completion likelihood affects model performance in Direct Alignment Algorithms (DAAs) like DPO, IPO and Hinge loss, using 7B and 35B models.
* Key finding shows that higher likelihood of better completions and larger margins between better/worse completions don't necessarily improve performance. Higher likelihood helps with factual recall but can hurt diversity.
* Authors propose two metrics for detecting likelihood over-optimization: Decreasing Entropy over Top-k Tokens and Diminishing Top-k Probability Mass. These metrics help prevent over-optimization while maintaining good performance.

### Strengths
* The work provides comprehensive experiments across multiple dimensions including likelihood, diversity and performance. The ablation studies are systematic and well-documented.
* The paper challenges common assumptions about likelihood optimization in DAAs. The trade-off between memorization and generalization is clearly demonstrated with empirical evidence.
* The proposed metrics for detecting over-optimization are concrete and actionable. The findings provide clear guidance for practitioners working on DAA training.

### Weaknesses
 * The paper only studies single epoch training when DPO typically needs 2-3 epochs for best performance. This important limitation is not well justified or analyzed. The lack of multi-epoch analysis raises concerns about the practical applicability of the findings, as real-world DPO training often involves multiple epochs to achieve convergence and optimal performance. The paper should provide a more thorough justification for this design choice, or at least acknowledge the potential impact on the generalizability of the conclusions.
* The BINARIZEDPREF dataset lacks crucial details about its construction and preference collection. If preferences come from GPT-4 rather than humans, the generalization of findings is questionable. The absence of detailed information about the annotation process, including the expertise of the annotators, the specific instructions provided, and the validation procedures used, makes it difficult to assess the reliability and validity of the dataset. This is particularly important given the potential for biases in LLM-generated preferences. The paper should include a comprehensive description of the dataset creation process.
* The primary evaluation uses GPT-3.5-turbo as baseline which feels dated. Testing against stronger models like LLaMA-3 would strengthen the findings. Using a relatively weaker model as a baseline makes it difficult to assess the true impact of the proposed metrics and training strategies. The paper should include evaluations against more recent and powerful models to demonstrate the robustness of the findings.

### Questions
* Could you provide more information about BINARIZEDPREF construction, including how preferences were collected and validated? The source of preferences is particularly important.
* Why was single-epoch training chosen when DPO typically needs more epochs? Do these patterns persist in multi-epoch training?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a detailed analysis of contemporary offline alignment methods, focusing on DPO, IPO, and Hinge. A comprehensive set of metrics, gathered during the alignment process for both a proprietary 7B model and the Cohere Command R 35B model, is employed to investigate the issue of over-optimization. Furthermore, the paper proposes using the entropy of the top-k tokens during generation for DPO and IPO, as well as the aggregate mass of the top-k tokens for Hinge, as indicators of over-optimization.

### Strengths
- Evaluation details are comprehensive.
- This work is useful for the community as it could be used to determine offline metrics to identify the best model at various steps.

### Weaknesses
 - Over-optimization itself is already well-studied in [1]. Some results, like Figure 1, seem to be consequences of the high KL divergence. I think NLL for y_w and KL are highly correlated metrics. It would be useful to see a figure with KL on the x-axis and NLL(y_w) on the y-axis. The absence of this plot makes it difficult to assess the novelty of the findings, especially given the similarity of Figure 1 to results in prior work.
- While Figure 1 supports the claim that there is no correlation between NLL(y_w) and win rate in general, Figure 2 shows that, for the given method and hyperparameters, the best step can be determined by observing NLL(y_w). More precisely, I would suggest tracking the difference between NLL from the previous and current checkpoints. If this value becomes larger than a certain threshold, one can stop training and thereby obtain the strongest checkpoint. Therefore, from the reported I would say that tracking NLL(y_w) could be sufficient to detect over-optimization across all methods (instead of proposed methodology in Section 4.4, which depends on method). The paper does not sufficiently explore the potential of NLL(y_w) as a universal indicator, particularly the bend observed in Figures 2-4, which seems to correlate with optimal performance.
- The paper presents an extensive amount of metrics during the training procedure; however, there is no clear criterion to detect over-optimization. First of all, the proposed methods in Section 4.4 are highly dependent on alignment methods, and if one were to use other popular methods (like KTO, ORPO, etc.), it is not clear which metric would serve as a flag for over-optimization. Additionally, it is unclear if these results remain the same for different models (see next weakness point). The proposed metrics for over-optimization are not only method-dependent but also lack a clear, generalizable criterion for detecting over-optimization across different alignment methods. The reliance on method-specific signals limits the practical applicability of the proposed approach.
- The choice of models is in question. Results obtained from a closed-source 7B model may not generalize to widely used open-weight models with similar sizes like LLAMA, Gemma, or Mistral. Additionally, this has a negative impact on the reproducibility of the experiments. The use of a closed-source model introduces a potential bias and limits the generalizability of the findings to the broader research community, which primarily uses open-source models.

### Questions
Lower entropy usually indicates that a model is overfitted. Could this fact indicate that the UltraFeedback dataset is not sufficiently diverse, and therefore the model could memorize patterns that are not useful in general? Does the issue of over-optimization hold across different datasets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a experimental analysis of the behaviors of margin-based alignment approaches, especially, they focus on the so-call over-optimisation issue. They claim that they are the first to explore the relationship between completion likelihood and performance in alignment algorithms. Their empirical finding is that, likelihood does not have a striong positive correlation with model performance, and it might be affected by diversity. Besides, they identify two indicators of overly generatinve diverse outputs.

### Strengths
## Originality
- Though the claim may not be novel, the systematic experiments are original and interesting.
- The reviewer appreciates the statistical metrics.

## Clarity
- This paper is well-written and densely organised.
- The figures are clearly plotted.

## Significance
- This paper may be able to clarify a controversial point, whether DAA should directly increase(decrease) the likelihood of accepted(rejected) completion? which the reviewer believes is a important question.

### Weaknesses
## Major
- The two indicators are so trivial, that people already know this before. Thus these two findings might not be counted as contributions.
- The experiments are restricted. Some DAAs with alternate objective (CPO, SimPO, ...) (such as length normalization) are not tested, making the claim less solid.

## Minor
- The curves are a bit confusing, especially Figure 4, making it hard to come to the authors' conclusion.

### Questions
- In Figure 3, why the DPO/IPO 7B ultrafeedback model cannot gain much improvement compared with initial checkpoint?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors explored the effect of increasing the probability of chosen sequences on the overoptimization of direct alignment algorithms (DAA). They concluded that an increased gap between chosen and rejected sequences could lead to overoptimization and linked overoptimization with reduced diversity of samples.

### Strengths
- The initial problem of overoptimization is important, and solving it is crucial for the field of alignment.
- Understanding signals of overoptimization is helpful and allows for faster evaluation. Instead of waiting for evaluation with LLMs, we can detect overoptimization through reduced entropy and decreasing mass in top-k tokens.

### Weaknesses
 - While the authors provided implementation details, it is unclear why they used a 7B model with closed weights when a wide range of open-source models of this size is available.
- My main concern is the limited novelty of the obtained results. From what I see in Figure 2, while the gap between chosen and rejected sequences is increasing for small $\beta$, the likelihood of chosen sequences is decreasing. This aligns with the observations of [1], as probability mass moves towards out-of-distribution (OOD) examples (and to avoid overoptimization, we should prevent leakage of mass to OOD sequences). Therefore, the findings do not seem to present new insights. When demonstrating that increased probabilities for chosen sequences can also lead to overoptimization, it is important to explore the probabilities associated with OOD examples. From this perspective, the main novelty of the paper lies in understanding the mechanism of detecting overoptimization via reduced diversity and aligning these observations with the impact on performance across various tasks, but this aspect is poorly explored.
- The presentation of results is difficult to read. The captions of large figures (2, 3, 4) do not contain useful information for understanding, making some metrics hard to interpret. Additionally, the analysis of these results is far from the figures themselves.
- The authors claim an opposing view, but the results in Figure 2, specifically around step 600, show a peak in win-rate coinciding with a slight reduction in the probability of chosen sequences. This suggests that the observed behavior is not entirely opposing, but rather a nuanced effect where initial reduction of chosen sequence probabilities can be beneficial, followed by a detrimental further decrease. The paper lacks a clear explanation for this behavior, which is crucial for understanding the underlying mechanisms of direct alignment algorithms.
- The paper lacks depth in its analysis of different tasks. The Ultrafeedback dataset, with its slightly worse rejected sequences, does not represent the full spectrum of alignment scenarios, particularly those with significantly worse rejects. This limits the generalizability of the findings. The use of the proprietary BINARIZEDPREF dataset further compounds this issue, as the lack of details on the nature of chosen and rejected sequences makes it difficult to assess the validity and generalizability of the results. The absence of open-source models and datasets for a significant portion of the experiments hinders reproducibility and limits the contribution of the work.

### Questions
See Weaknesses

### Soundness
2

### Presentation
1

### Contribution
2
