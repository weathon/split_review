# TiC-LM: A Multi-Year Benchmark for Continual Pretraining of Language Models

- Decision: Reject
- Scores: 6, 8, 5, 6

## Abstract
Large language models (LLMs) are trained on data crawled over many years from the web. We investigate how quickly LLMs become outdated as the world evolves with time and how to best update them with newer data. Specifically, we simulate a world where the latest dump of Common Crawl (CC), the most prominent public source of pre-training data, is used every month to *continually* train an LLM. We design various dynamic evaluations from the CC data, Wikipedia, StackExchange, and code documentations to measure continual learning metrics such as forgetting and forward transfer. Notably, our TiC-CC training data is more than 100 times larger compared with prior continual learning benchmarks for language modeling. We discover that recent DataComp-LM models trained on data before 2023 have already become outdated, incurring up to 45\% larger noun-perplexity on 2024 Wikipedia articles compared to pre-2023 articles. Further, we use our setup to evaluate the effectiveness of several large-scale continual learning methods and find that replaying older data is most effective for combating forgetting: for previously seen CC dumps, it can reduce the regret on held-out loss by 60\% compared to other optimizer and loss-based interventions. However, some domains evolve more quickly than others, favoring different trade-offs between mixing old and new data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the continual training of LLMs. In general LLMs are pretrained on a time snapshot of the data and do not get retrained very often. As a result, as new data become available, the knowledge of model become outdated and does not cover new information. This paper offers benchmarks to evaluate this effect and also offer some solutions on how to update the model with the new data while avoiding forgetting the previous data.

### Strengths
- the paper is well written and the datasets, steps, and evaluations are clearly explained
- the paper tackles an important problem: how to continuously update LLMs without needed to fully retrain

### Weaknesses
My main concern is the contribution of the paper. Although the authors have tried to extensively quantify the effect of model not being trained on the new data, it is a known fact that training in distribution is always better. So if we evaluate the model on the same data from future, there would be degradation. The more interesting question is the remediation recipe for this problem and more importantly how the model can be adopted to new domains. Authors study few methods of updating the model and show some work better than the other however, all lacking behind the oracle and they leave it to future work. I believe emphasizing on the benchmark by itself does not bring enough novelty to warrant acceptance.

### Questions
- Authors mention that they do only fuzzy deduplication within each shard. How do they guarantee that there is no leakage between the shards especially for the evaluation sets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel benchmark, TiC-LM, for evaluating continual pretraining of large language models (LLMs). The benchmark is structured around a dataset called TIC-CommonCrawl (TIC-CC), which aggregates 114 monthly snapshots from Common Crawl from 2013 to 2024. The authors simulate a continual training environment by sequentially feeding data from each monthly snapshot to an LLM and exploring various continual learning methods. The key contributions include evaluating the temporal relevance of language models over time, assessing forgetting and forward transfer across domains, and determining effective methods for balancing the retention of old knowledge with learning new information. This paper is a huge engineering project that provides a benchmark that thorougly evaluates existing methods for continual LLM pretraining and can allow the field to quantify progress in developing better methods.

### Strengths
Originality: The work introduces a unique benchmark for continual language model pretraining.
Quality: The authors have employed a thorough and robust experimental methodology, including multiple baselines and diverse continual learning techniques, demonstrating the rigor of their approach.
Clarity: The problem is well-motivated, with clear research questions and systematically presented results.
Significance: The findings provide insights into temporal dynamics in LLMs, especially the trade-offs between data replay and learning rate adjustments for preserving knowledge across time. This work has strong potential to serve as a reference benchmark for the community.

### Weaknesses
Lack of novel findings: The paper lacks novel findings not explored in previous works. However, it does improve upon previous benchmarks and can serve as a better indicator for quantifying progress towards developing better methods for this problem.
Complexity of Setup: The continual pretraining process as described may be challenging for broad adoption without substantial compute resources, making it difficult for smaller research groups to replicate the study.
Hyperparameter Sensitivity: The paper does not fully address how sensitive different strategies (like cyclic cosine schedules) are to hyperparameters, which could impact reproducibility.

### Questions
How sensitive are the results to hyperparameter choices, especially for cyclic learning rate schedules and replay ratios? Additional insights here would be helpful for reproducibility.
Do the authors plan to release the TIC-LM dataset, and if so, would it include any pre-trained checkpoints for baselines to facilitate easier reproduction of results?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel dataset for continual pretraining of large langauge models that significantly expands the scale of existing datasets in the field. The provided dataset may be valuable for future studies in the continual pretraining. However, the insights are limited. The experimental results are not well-explained.

### Strengths
1. **Impressive Dataset Size**: The proposed dataset significantly surpasses existing datasets in scale, providing a robust foundation for research.

2. **Rigorous Experimental Setting**: The experimental design is thorough and well-structured, ensuring reliable results.

3. **Comprehensive Review of Related Work**: The discussion of related work is thorough and effectively contextualizes the research within the field.

### Weaknesses
1. **Limited Insights**: The paper does not provide new insights into continual pretraining. The experimental results indicate that cyclic learning rate schedules, data replay, and regularization methods are insufficient for maintaining both strong in-domain performance and reduced forgetting. A clearer explanation of why each method fails under different conditions would enhance the understanding. The experimental section reads more like a report than an analysis, which limits its usefulness for future researchers.

2. **Unconvincing Experiments**: The performance of EWC is heavily influenced by the weight of the regularization term, creating a trade-off between plasticity and stability. There is a lack of detailed discussion regarding the hyperparameter analysis of EWC. While Appendix C mentions that “λ = 10^7 performed best when tuning between 10^1 and 10^9,” the varying performance of EWC across different evaluation datasets (as shown in Table 3) raises concerns. It’s possible for EWC to perform well on one dataset while underperforming on another. This issue extends beyond EWC to other methods as well, suggesting a sensitivity to hyperparameters that warrants further exploration.

3. **Poor Presentation**: The overall presentation, particularly in the experimental section, is lacking. Important analyses are often relegated to figure captions, such as those for Figure 4 and Table 2, which detracts from the clarity of the findings.

### Questions
Please refer to limitation

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper curates a multi-year benchmark for evaluating continual training methods based off Common Crawl (CC). Moreover, it also designs various dynamic evaluations based on CC, wikipedia, StackExchange and codes, to evaluate forgetting and forward transferring. The paper contains various experiments on the top of benchmarks to measure the effect of different scheduler, regularization, and data replay methods. The main conclusion includes LLM needs to be updated continually to stay up-to-date, and data replay mitigate the issue of forgetting but not eliminate it.

### Strengths
1. This paper offers significant contribution to the community by presenting the largest continual learning benchmark for the community to evaluate and compare CL techniques. 
2. The experiment design is fairly comprehensive, offer a baseline study for CL technique evaluation. 
3. I find the paper is clear and well-displayed. The selected metric is clear and powerful; visualization is informative easy to understand. The paper is well-structured overall. 
4. The empirical insights drawn from the CL evaluation experiments are original. I believe they are beneficial to researchers working in the space of LLM continual learning.

### Weaknesses
1. Although the presentation is comprehensive dataset is valuable, the CL dataset curation and downstream evaluation dataset curation are extension of existent approaches. TiC-CC is based on the  DCLM pipelines, TiC-Code, TiC-Wiki and TiC-StackExchange are curated using fairly standard approaches.

2. The metrics used in the paper only capture the training loss (perplexity), and forgetting based on the perplexity loss. Other dimensions of forgetting is not measured. The relation between perplexity loss and model behavior (e.g., knowledge forgetting) is not studied. For example, data replay helps reduce the gap with Oracle in Figure 4 on wiki, but it doesn't help on wiki-diff in Table 3.

### Questions
1. In the bottom panel of Figure 4, all three figures exhibits that later checkpoints have smaller gap with Oracle on earlier evaluation month. For example, the checkpoint of 202402 records gap ~0 on 2014 but increases gradually to 202402 on TiC-CC and TiC-New. The trend is not as clear on Wiki but exists. Shouldn't all figures follow similar pattern with the top left figure despite with or without replay? How do you explain the observation?

2. Data replay doesn't seem help on most of the downstream evaluations and even harm the Backward performance in some cases (Tic-Wiki-Diff, StackOverflow, CodeDocs-Pytorch), but it shows clear benefits in the TiC-CC evaluations. This appears to be an anomaly, doesn't it?

### Soundness
2

### Presentation
3

### Contribution
3
