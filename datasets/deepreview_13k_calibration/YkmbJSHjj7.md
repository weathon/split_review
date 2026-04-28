# W-PCA Based Gradient-Free Proxy for Efficient Search of Lightweight Language Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 8, 6

## Abstract
The demand for efficient natural language processing (NLP) systems has led to the development of lightweight language models. Previous work in this area has primarily focused on manual design or training-based neural architecture search (NAS) methods. Recently, zero-shot NAS methods have been proposed for evaluating language models without the need for training. However, prevailing approaches to zero-shot NAS often face challenges such as biased evaluation metrics and computational inefficiencies.
In this paper, we introduce weight-weighted PCA (W-PCA), a novel zero-shot NAS method specifically tailored for lightweight language models. Our approach utilizes two evaluation proxies: the parameter count and the number of principal components with cumulative contribution exceeding $\eta$ in the feed-forward neural (FFN) layer.  Additionally, by eliminating the need for gradient computations, we optimize the evaluation time, thus enhancing the efficiency of designing and evaluating lightweight language models.
We conduct a comparative analysis on the GLUE and SQuAD datasets to evaluate our approach. The results demonstrate that our method significantly reduces training time compared to one-shot NAS methods and achieves higher scores in the testing phase compared to previous state-of-the-art training-based methods. Furthermore, we perform ranking evaluations on a dataset sampled from the FlexiBERT search space. Our approach exhibits superior ranking correlation and further reduces solving time compared to other zero-shot NAS methods that require gradient computation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces W-PCA, a novel zero-shot NAS method specifically tailored for light weight language models.

### Strengths
1.The method is simple but achieves both better latency and accuracy on NLU tasks.

### Weaknesses
1.The format of this paper is confusing. The gap between figures and text(e.g. Figure 2) seems to be abnormal. Table 4 is also not placed correctly.

2.Poor writing and low-quality figures. For example, I have no idea on the pipeline and implementation of W-PCA until the experiement section. the lines representing dimensions are not straight lines in figure 4. The comparison in the conclusion part(e.g. Kendall score and Spearman score) seems to be inconsistent with experiment results. 

3.Although authors claim that W-PCA achieves SOTA, their results are based on their own version of BERT model. They compare their methods with others, whose results are directly copied from their original papers. The comparison is unfair and may mitigate the reliability of their results, especially on the GLUE benchmark.

4.The experiments only focus on BERT models and they only have are around 100M. This limits the applicability of W-PCA to current LLMs, which typically have several billion parameters.

### Questions
1.Could you provide results of some other methods based on your BERT models?

2.I am curious about the applicability of W-PCA on current LLMs(e.g. LLama).

3.How do you calculate GPU days in table 3 and estimate that AutoBERT-Zero-small requires around 1,000 GPU days on GLUE dev set?

4.You claim in the conclusion that W-PCA achieves a Kendall score and a Spearman Score that surpass previous methods by 0.207 and 0.325 respectively. However in table 1, the differences are 0.220 and 0.334. Could you clarify how do you calculate the score differences?

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
The authors present a gradient-free method of evaluation of performance of candidate neural networks as part of neural architecture search. Their approach relies on estimating model's performance on target dataset through the PCA-score of FFN layers weighted by the number of parameters. The benefits of this approach include: strong correlation with target metric, gradient-free approach and the need for only a single forward pass on candidate network. Authors conduct experiment to evalaute the proposed method by sampling and evaluating 500 structures from FlexiBERT benchmark. The structures are evaluated as part of student model in distillation setup. The datasets are GLUE and SQuAD.

### Strengths
1) Authors propose a simple yet effective-enough method for evaluating candidate networks during NAS. It helps achieve networks with lowest latency and high performance on target datasets.
2) The method itself is highly efficient and allows for reasonably fast NAS iterations without compromising on quality as shown in Table 1.

### Weaknesses
1) Parts of paper appear to be LLM-written (for instance: L281-L304). Itself it is not a bad thing, yet those parts of paper lack substance and sometimes repeat the same information.
2) This paper would benefit from more experiments on decoder models (in addition to existing experiments on encoder models). This would make the paper even more relevant. Indeed, in the introduction, authors cite OpenAI's techincal report as evidence that LLMs have shown substantial performance across domains. It would be naturally to include said LLMs (maybe not OpenAI's LLMs, but generally) into the scope of this paper.
3) A reasonably-sized limitations section would also benefit the paper.
4) L075-L081 - a lot of empty space here
5) Figure 3 - legend is very small, not easy to read
6) Do you always compute PCA scores at epoch 0, i.e right after models parameters are randomly initialized?
7) L461 - Actual values of reduced CO2 footprint would be more convincing.
8) Table 1 and subsection 5.2 - I suggest clarifying between what values do you compute correlation.
9) If answer to 6 is yes: does W-PCA score depends on the random seed that is used during initialization? If so, have you considered computing W-PCA as an average of scores from different initializations?

### Questions
1) L075-L081 - a lot of empty space here
2) Figure 3 - legend is very small, not easy to read
3) Do you always compute PCA scores at epoch 0, i.e right after models parameters are randomly initialized?
4) L461 - Actual values of reduced CO2 footprint would be more convincing.
5) Table 1 and subsection 5.2 - I suggest clarifying between what values do you compute correlation.
6) If answer to 3 is yes: does W-PCA score depends on the random seed that is used during initialization? If so, have you considered computing W-PCA as an average of scores from different initializations?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces a new zero-shot approach for NAS of lightweight language models, using a score based on PCA dimensionality and the model's parameter count. Experimental results demonstrate that this method outperforms prior NAS approaches and manually designed lightweight architectures.

### Strengths
The presentation is clear and well-written. The method outperforms previous baselines, is computationally efficient, and is grounded in solid foundational insights and preliminary observations.

### Weaknesses
 
**Major Weaknesses:**
1. The models used are somewhat outdated, as BERT is rarely a focus in current research, which has largely shifted toward GPT-style models. The lack of experiments on more recent architectures limits the impact of the findings, as the community is primarily interested in the performance of methods on state-of-the-art models.
2. Reproducibility is challenging without the provision of code, making it difficult for others to replicate the study’s findings. The absence of code hinders the verification of the proposed method's effectiveness and prevents further research based on this work.
3. The procedure is a bit unclear. Are the architectures tuned during genetic search? It is not clear whether the weights of the architectures are updated during the search, or if only the architecture itself is being optimized.
4. Are the other baselines fine-tuned? Do they employ Knowledge Distillation? If not, the comparison may be unfair. It is crucial to understand the training protocol of the baselines to ensure a fair comparison with the proposed method. Specifically, the use of knowledge distillation should be clearly stated for all baselines.


**Minor Weaknesses:**

1. The term "PCA Value" is misleading, as PCA is primarily a dimensionality reduction method. It should be introduced with a brief explanation in the introduction and abstract, before discussing the preliminary experiments. The term should be more descriptive of the actual metric being used, and its connection to the PCA method should be clarified.
2. Table 5 is unclear—does it suggest that using only the parameter count as a proxy achieves better results than all previous methods? The implications of this result should be discussed in more detail, as it could suggest that the proposed method is not as effective as a simple parameter count in certain cases.

### Questions
I suggest moving the Zero-Shot NAS section to the experimental settings to provide a clearer explanation of the baselines.

Additionally, Figure 2 at the beginning needs much more explanation, as it's difficult to understand the main idea without reading the entire paper. The figure illustrating the method could also be improved, as it currently doesn’t contribute to comprehension effectively.




**Overall**, I find the paper to be a good quality and ready to reconsider the score, once the authors address all the raised concerns.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduce an approach that leverages a combination of principal component analysis (PCA) values and parameter counts as a zero-shot proxy metric to evaluate model candidates. By bypassing training and relying solely on initial weight information, W-PCA aims to efficiently estimate the potential of each candidate architecture, with significant gains in computational efficiency.

### Strengths
1. The paper provides an empirical evidence in Figure 2, showing that initial PCA scores of BERT-based candidate models correlate with their final performance, which is an interesting and effective shortcut for evaluating model quality.
2. The paper compares W-PCA with other zero-shot and one-shot NAS methods across benchmarks such as GLUE and SQuAD, demonstrating competitive performance. Moreover, the latency is drastically reduced.

### Weaknesses
1. While the paper presents a correlation between PCA values of initial weights and final performance, this correlation may be specific to the BERT architecture and the chosen search space. It remains unclear if this method would generalize well to other model architectures, such as GPT models or non-BERT Transformer variants. Specifically, the reliance on initial weight PCA might not capture the nuances of training dynamics in models with different initialization schemes or architectural features, such as varying attention mechanisms or normalization layers. This raises concerns about the robustness of W-PCA as a general-purpose proxy for model evaluation.
2. The paper show curves of PCA scores over different training epoch in Figure 3 as a motivation of using PCA in the NAS, but it is better to also show a curve of accuracy besides epoch to better claim "Tracking performance via PCA". The absence of a direct comparison between the PCA score trajectory and the actual validation accuracy trajectory makes it difficult to assess the practical utility of PCA as a performance indicator during training. A more compelling demonstration would involve showing that changes in PCA scores directly correspond to changes in validation accuracy, especially during the early stages of training, which is crucial for NAS.
3. The intuition behind combining PCA scores with parameter count to form the W-PCA metric is not well explained. While Figure 2 suggests that W-PCA achieves some gains, the performance patterns are not significantly more distinct than those observed with vanilla PCA. The paper lacks a clear justification for why a simple multiplication of PCA scores and parameter counts would yield a more effective metric. It's unclear if this combination is based on a theoretical foundation or is purely empirical. A more in-depth analysis of the relationship between model size, PCA scores, and final performance is needed to support this design choice.
4. In the ablation study, W-PCA shows only marginal improvements over baseline methods. Providing statistical significance tests on these improvements would be beneficial. The lack of statistical significance testing makes it difficult to determine whether the observed improvements are genuine or simply due to random variation. Without proper statistical validation, the claims of W-PCA's superiority remain unsubstantiated.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
