# RMB: Comprehensively benchmarking reward models in LLM alignment

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Reward models (RMs) guide the alignment of large language models (LLMs), steering them toward behaviors preferred by humans. Evaluating RMs is the key to better aligning LLMs. 
However, the current evaluation of RMs may not directly correspond to their alignment performance due to the limited distribution of evaluation data  and evaluation methods that are not closely  related to alignment objectives. 
To address these limitations, we propose RMB, a comprehensive RM benchmark that covers over 49 real-world scenarios and includes both pairwise and Best-of-N (BoN) evaluations to better reflect the effectiveness of RMs in guiding alignment optimization.
We demonstrate a positive correlation between our benchmark and downstream alignment task performance.
Based on our benchmark, we conduct extensive analysis on the state-of-the-art RMs, revealing their generalization defects that were not discovered by previous benchmarks, and highlighting the potential of generative RMs.
Furthermore, we delve into open questions in reward models, specifically examining the effectiveness of majority voting for the evaluation of reward models and analyzing the impact factors of generative RMs, including the influence of evaluation criteria and instructing methods.
    \textcolor{red}{WARNING: This paper may contains texts that are offensive in nature.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents RMB, a benchmark evaluating reward models (RMs) across 49 real-world scenarios, improving alignment assessments for LLMs. RMB reveals generalization issues in current RMs and explores factors affecting generative RM effectiveness.

### Strengths
1. The paper is written well and is easy to understand.
2. The studied problem is significant..
3. The results seem to outperform the SOTA datasets of the reward model evaluation.

### Weaknesses
1. The paper currently includes some discussion related to benchmark comparisons in Section 5.2, particularly with RewardBench. However, a more explicit comparison of the features and approaches of existing benchmarks early in the paper would better highlight the novelty of this work. Rather than relying on experimental results to convey superior performance, detailing how our model’s capabilities differ from those of previous benchmarks would strengthen the paper's contribution.
2.  In the conclusions about evaluation results, statements like “It is hard for an RM to be both competitive in judging helpfulness and harmlessness” and “Generative models show great promise in reward modeling” could be enhanced by including an explanation of the underlying reasons for these findings. Adding these insights may help the community engage more deeply with the work, offering valuable perspectives that could inspire further exploration beyond the results alone.

### Questions
Please refer to the weakness, I'm happy to modify my rate based on the response of the authors and refer to other reviewers' comments.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes RMB (Reward Model Benchmark) which is a benchmark for evaluation of reward models used in LLM alignment. It consists of 49 real–world scenarios between the two proposed categories “helpfulness” and “harmlessness”. They use two methods of evaluation: pairwise comparison and best-of-N evaluation, which tests the models’ ability to choose the best response from multiple candidates. Another key finding is that generative models show strong performance, often outperforming discriminative models. Further, they show positive correlation between benchmark performance and downstream alignment tasks.

### Strengths
RMB presents many strengths, especially against its main predecessor, RewardBench. Primarily, the dataset size is much larger than any similar datasets used to evaluate reward models. The paper does thorough investigation of best-of-N evaluation, which related papers had proposed as a future direction of research. The authors do a good job of categorization and subcategorization, to ensure broad coverage across different tasks. The benchmark shows good progress towards a useful proxy for downstream model performance. Further, the paper is clearly written and has good formatting.

### Weaknesses
There are a couple of weaknesses in the paper. The human annotator sample size is small relative to the size of the dataset. The correlation analysis focuses mainly on the best-of-N sampling rather than RLHF, which is acknowledged in the paper as a limitation. While mentioning that it is hard for a model to be both competitive in judging helpfulness and harmlessness, the authors don’t deeply explore the trade-offs between the two metrics. The authors used various models in the categorization and filtering steps, but the scoring was only done by GPT4, which might introduce bias. There are also a few styling errors and typos throughout the paper that would need to be cleaned up prior to approval.

### Questions
- Were any alternatives to GPT-4 scoring considered? How might the benchmark differ if using other models (or ensembles) or human annotators? (I understand human annotation is costly) 

- Did you observe any patterns when best-of-N evaluation diverged significantly from pairwise evaluation?

- What recommendations would you make for effectively using RMB during the reward model development process? Is it simply meant to be used as a validation set? 

- What tradeoffs between helpfulness and harmlessness exist? Why do you think they seem to be mutually exclusive? 

- Do you see any negative impacts or possible misuses of the benchmark?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes RMB, a comprehensive benchmark for evaluating reward models (RMs) in LLM alignment. The dataset contains comprehensive real-world scenarios on helpfulness and harmfulness and responses generated by different LLMs. The paper validates the benchmark's effectiveness by showing a correlation with downstream alignment performance.

### Strengths
- The paper is well-structured and clearly written, explaining the methodology and results effectively.
- RMB effectively addresses the limitations of developing reward models that align with the objective, whether helpfulness or harmlessness. Correlation evaluations show that the reward model's performance on RMB can reflect the performance of the downstream aligned model more accurately. This would enable researchers to evaluate and iterate on reward models more efficiently before training a more computationally challenging model alignment.
- The paper provides solid empirical evidence supporting the effectiveness of RMB. The experiments on pairwise and best-of-N accuracy cover different generative and discriminative reward models and provide a good insight into their usefulness as judges.

### Weaknesses
 - The reliance on LLM-generated response in the dataset curation may pose potential long-term limitations. As reward models are often used to align newer LLMs, using responses from current LLMs to evaluate them could create a circular dependency. In other words, this benchmark may not be able to differentiate reward models that could guide LLMs that are beyond current capabilities. In the next iterations, it would be nice to incorporate human-generated responses to ensure more diverse sources of responses.
- The correlation evaluation is leveraging best-of-N as an alignment, which is not the only way people are using the reward models. Would it be possible to gather a set of reward models and aligned model pairs that leverage the reward model during training and see the correlation there?
- nit: Mu et al.. citation is missing a year (L229)

### Questions
See Weakness.

### Soundness
3

### Presentation
4

### Contribution
3
