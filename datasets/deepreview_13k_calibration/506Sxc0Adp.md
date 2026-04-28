# Beyond Scale: the Diversity Coefficient as a Data Quality Metric Demonstrates LLMs are Pre-trained on Formally Diverse Data

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 1, 6

## Abstract
Current trends to pre-train capable Large Language Models (LLMs) mostly focus on scaling of model and dataset size. However, the of pre-training data is an important factor for training powerful LLMs, yet it is a nebulous concept that has not been fully characterized. Therefore, we use the recently proposed Task2Vec diversity coefficient to understand formal aspects of data \textit{quality} that go beyond scale alone. Specifically, we measure the diversity coefficient of publicly available pre-training datasets to demonstrate that their formal diversity is high when compared to theoretical lower and upper bounds. In addition, to build confidence in the diversity coefficient, we conduct interpretability experiments and find that the coefficient aligns with intuitive properties of diversity, e.g., it increases as the number of latent concepts increases. We conclude the diversity coefficient is reliable and conjecture it can be used to build useful diverse datasets for LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper extends the diversity coefficient metric [1] to textual pre-training datasets. To be more specific, the approach first estimates the Task2Vec embeddings [2] for batches of sequences in the dataset, followed by computing the expected distance between two random batches. This diversity metric is then computed on various existing pre-training datasets (and their combination), followed by some analysis of the same.

[1] Brando Miranda, Patrick Yu, Yu-Xiong Wang, and Sanmi Koyejo. The Curse of Low Task Diversity: On the Failure of Transfer Learning to Outperform MAML and Their Empirical Equivalence.

[2] Alessandro Achille, Michael Lam, Rahul Tewari, Avinash Ravichandran, Subhransu Maji, Charless C. Fowlkes, Stefano Soatto, and Pietro Perona. Task2vec: Task embedding for meta-learning.

### Strengths
- The motivation behind building data quality metrics is an important direction for building better language models.
- The paper is well written and easy to follow along.

### Weaknesses
 - Unclear practicality of the proposed metric: while the metric is shown to reasonably estimate the inherent “diversity in a dataset,” I’m quite unsure about its extrapolation to measuring “dataset quality.”
- Limited novelty: The paper directly builds on two existing lines of work [1, 2], and is also limited by its application to different practical scenarios (more in questions).
- The proposed diversity metric is model-dependent (GPT-2 is used in the paper), while the downstream effect of the probe model on the diversity metric isn’t studied (more in questions).

### Questions
- What are some practical use-cases for the proposed diversity metric? 
- Keeping aside the vague intuition, why do you think data diversity should be a good indicator of data quality?
- The considered scenario for estimating the utility of a larger batch-size is also debatable: a larger batch-size in addition to providing diverse data also directly affects the optimization. Nonetheless, in addition to showing a saturating diversity with increasing batch size, how does the model performance change with increasing batch size?
- Assuming data diversity is a good indicator of data quality, do you think data diversity estimated using GPT-2 as the probe-model would translate to better training of (1) models with different architectures (e.g., encoder-decoder, encoder-only), and (2) different model-sizes (e.g., GPT-3, …)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper begins by observing that current trends in pre-trained large language models (LLMs) mostly focus on scaling model and data size, while ignoring the quality of pre-training data. The author proposes that the quality of pre-training data is also an important factor for training powerful LLMs. To this end, they propose using the recently proposed Task2Vec diversity coefficient to ground and understand formal aspects of data quality. The authors also validate the diversity coefficient by demonstrating its interpretability and correlation with intuitive diversity properties aligned with human intuitions, and provide ways to evaluate the diversity coefficient for a given dataset.

### Strengths
1. This paper is well-written and rigorous.
2. I find the idea of improving the performance of pre-trained large language models from a data quality perspective meaningful. Considering the increasing pre-training cost, using small and high-quality data and avoiding the scaling of model and data size is a good way.
3. The authors demonstrate that the public datasets for LLM pre-training have high formal diversity using well-motivated lower and upper bounds. They also provide practitioners with simpler ways to evaluate the diversity coefficient. It is more important.

### Weaknesses
1. The definitions in sections 2.1 and 2.2 are essential to understanding the paper’s main argument. However, they are somewhat difficult to comprehend. To make these definitions more accessible, I suggest providing more illustrations in addition to citing related papers.

2. More experiments should be conducted to investigate the correlation between diversity coefficient and LLM performance. For example, on more models and datasets with multiple runs. The end goal of this research should be to improve the performance of LLMs.

### Questions
N/A

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the quality of data used for training Large Language Models. It introduces the Task2Vec diversity coefficient as a metric to evaluate this quality. By analyzing public datasets and conducting interpretability experiments, the authors claim that a higher diversity coefficient indicates better data quality. They suggest that this coefficient could serve as a useful tool for constructing high-quality datasets for training models.

### Strengths
1. **Addressing an Important Problem**: The paper tackles the significant issue of data quality metrics for large language models. 
2. **Introduction of Diversity Coefficient in Context**: The paper brings the concept of a diversity coefficient into the discussion of data quality for large language models. 
3. **Reference to Existing Literature**: The paper builds upon existing work, particularly on Task2Vec and Fisher Information Matrix.

### Weaknesses
1. **Limited Novelty and Insight**: The paper largely relies on existing methodologies, including Task2Vec diversity coefficient and latent concept analysis, and does not offer new or noteworthy findings. 
2. **Issues with Model Updates and Task2Vec**: It's not clear if the model weight is updated after computing the Task2Vec embedding for each batch. This is crucial as it affects the validity of the reported results, especially those in Section 4.
3. **Unexplained Necessity for Task2Vec in Measuring Data Quality**: The paper uses token distribution as a metric for dataset diversity but fails to clarify why Task2Vec coefficients are needed instead of direct token distribution metrics. The lack of this clarification adds confusion and questions the relevance of using Task2Vec for data quality measurement.
4. **Unclear Practical Utility of Data Quality Metric**: The paper suggests the diversity coefficient as a potential data quality metric but does not empirically validate this claim. This is a significant concern, especially considering the emphasis on Task2Vec and model diversity in the paper.
5. **Methodological Ambiguities and Undefined Concepts**: The paper contains unclear statements and undefined notations, particularly in the methods section.

### Questions
### Major Concerns

1. **Potential Issue with Model Updates and Task2Vec**: Is the model weight updated after the Task2Vec embedding is computed for each batch? If so, doesn't this imply that the diversity should inherently be high since the information from the first batch has already been learned and therefore won't be reflected in the Task2Vec embedding for the second batch? How does this affect the importance of your results in Section 4?

2. **Task2Vec and Token Distribution: Confusion about Relevance to Data Quality**:
    - In Section 2.2.4, token distribution is used as a metric for dataset diversity. Why then is it necessary to calculate Task2Vec diversity coefficients by fine-tuning the model? How is this relevant to data quality?
    - Following from the above, Section 3.4 revisits the correlation between diversity coefficient and vocabulary size. Could you clarify why this aspect is repeatedly emphasized?

### Additional Questions
3. **Ambiguities in Section 2.1**:
    1. You mentioned "(partially) fine-tuning" the final layer of a fixed neural network to solve the "current task (or batch)". Could you clarify what you mean by "partially fine-tuning"? Also, how do you define "solving the current task (or batch)" in this context?
    2. The variable $t$ is used but not explicitly defined. Could you specify what $t$ represents and its range of possible values?
    3. When discussing the expectation over both $t$ and $\hat{x}_t$, could you elaborate on why and how this expectation is taken?

4. **Minor Formatting Issues**: The in-text citation style appears to be inconsistent across the paper.

5. **Potential Typo on Page 2**: In the contributions section, item 4 states, "...the **high** diversity of public datasets for LLM pre-training is **high**..." This appears to be a typo.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a ‘diversity coefficient’ that can measure the diversity in certain dataset and a ‘cross diversity coefficient’ that measure the difference between two datasets. Experiments show that the coefficient has three ideal characteristics: the coefficient increases as more datasets are concatenated, the number of latent concepts increases, and a richer vocabulary is used. Besides, the proposed efficient also show that the current public pre-training datasets has relatively high diversity, which could explain why we can get good LLM trained on them.

### Strengths
1) The dataset quality is a very important topic but unfortunately not well-defined and studied. It is great that this paper devotes to this novel and critical topic.

2) Measuring the dataset quality in terms of diversity is a nice and neat idea, authors also propose ideal characteristics of the diversity metric and ways to justify them.

### Weaknesses
1) I understand that authors want to show the diversity coefficient can work by comparing real data diversity with theoretical lower and upper bound. However, if we treat lower bound as baseline, it is too weak to say the dataset having better diversity is really diverse? The lower bound, representing uniform single-token sequences, is a trivial baseline and does not provide a meaningful comparison point for assessing the diversity of real-world datasets. A more informative baseline could involve a dataset with known low diversity, such as a collection of documents from a single, narrow domain.

2) Since this approach requires finetuning LM, it is actually introducing some computational overhead. I understand this overhead is not large, but it should be stated in the limitation section. The fine-tuning step, even if only applied to the final layer, introduces a computational cost that should be explicitly acknowledged. The authors should quantify the computational resources required for fine-tuning, such as the number of parameters updated and the training time, to provide a complete picture of the method's practical implications.

3) More recent data-centric related works should be added. Most related works listed are before 2022. Only two citations are after 2023, one is GPT-4, and the other is Palm 2, neither of which are references to Data Centric methods. To my knowledge, there is at least one paper about increasing data diversity from Meta AI in 2023.08. “D4: Improving LLM Pretraining via Document De-Duplication and Diversification”. Probably can add to the Related Work?

4) Since the coding data is increasing important, authors should provides more insights about the diversity of code pre-training dataset.

5) Some conclusions are not well-justified.  In appendix G, experiments conclude that ‘higher data diversity leads to higher test performance’, but fail to ablate the influence of dataset overlap. In fact, the Pile dataset itself contains both the USPTO and PubMed, so I think model trained on the ‘USPTO+PubMed’ is better than models trained on either of them cannot purely attribute to the diversity increase. It’s possible that the high diversity is not the key factor, the actual factor is high diversity increase the overlap between train and test set, and therefore increase the test performance. In addition, the table in Appendix G should be further clarified. It’s hard to get which dataset is the training dataset and which one is the eval set.

### Questions
1) The introduction of Task2Vec in the ‘method’ section is brief and should mention the further explanation in the Appendix A(I got stuck in this part for a while). Besides, I am kind of confusing about the dimension of vector’s embedding. According to the formula I think the diagonal dimension should equal to the number of model’s parameters. If that’s true the vector will be extremely large…

2) The setting “Randomly initialized GPT-2 without fine-tuning” in Section 4 makes me confused. Does that mean you only reset the LM head or the whole model? My concern is different random initialization could lead to very different results. So it’s not safe to conclude that ‘using a random probe network (always)**underestimates** diversity’.

3) What’s the relationship between the diversity efficient and the cross diversity efficient? What insight can we get by comparing them together?

4) small typo, ‘due’ should be ‘due to’ in Sec 3.4

5) In table 1, why concatenating C4 and Wikitext-103 decrease the Div Coeff? Any analysis on this exception?

6) In table 1, what does the ‘Combination of Five Datasets(MIX2)’ mean? The explanation of MIX2 setting is not very clear to me. Why only five datasets? Why 0.77 vs 0.23?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
