# Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Selecting high-quality pre-training data for large language models (LLMs) is crucial for enhancing their overall performance under limited computation budget, improving both training and sample efficiency. Recent advancements in file selection primarily rely on using an existing or trained proxy model to assess the similarity of samples to a target domain, such as high quality sources BookCorpus and Wikipedia. However, upon revisiting these methods, the domain-similarity selection criteria demonstrates a diversity dilemma, i.e. dimensional collapse in the feature space, improving performance on the domain-related tasks but causing severe degradation on generic performance.To prevent collapse and enhance diversity, we propose a DiverSified File selection algorithm (DiSF), which selects the most decorrelated text files in the feature space. We approach this with a classical greedy algorithm to achieve more uniform eigenvalues in the feature covariance matrix of the selected texts, analyzing its approximation to the optimal solution under a formulation of $\gamma$-weakly submodular optimization problem. Empirically, we establish a benchmark and conduct extensive experiments on the TinyLlama architecture with models from 120M to 1.1B parameters. Evaluating across nine tasks from the Harness framework, DiSF demonstrates a significant improvement on overall performance. Specifically, DiSF saves 98.5\% of 590M training files in SlimPajama, outperforming the full-data pre-training within a 50B training budget, and achieving about 1.5x training efficiency and 5x data efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces DiSF, a method aimed at selecting diverse training data to enhance the effectiveness of pre-training large language models (LLMs). The authors begin by analyzing recent data selection methods and identify a critical issue: the selected data often suffer from dimensional collapse in the feature space. This collapse leads to improved performance on domain-specific tasks but causes a significant degradation in general performance due to a lack of diversity.

To address this problem, the authors propose improving the diversity of the data selection process by formulating it as a submodular optimization problem. Specifically, their goal is to prevent dimensional collapse by ensuring more uniform eigenvalues in the covariance matrix of the selected samples. They employ a classical greedy algorithm for submodular optimization, combined with mini-batch sampling, to make the approach tractable.

Due to hardware limitations, the authors tested their approach on models with sizes of 120M, 560M, and 1.1B parameters. Despite the smaller scale, the DiSF method achieves superior performance over six baselines on nine standard benchmarks consistently, across different training budgets (10B and 50B tokens). The authors also provide extensive ablation studies to analyze the effects of data selection budget, different architectural backbones, feature extractors, and more.

### Strengths
+ Well-Motivated Research: The paper addresses a significant issue in data selection for LLMs—dimensional collapse due to lack of diversity—which has substantial implications for model performance.
+ Clear Presentation: The methodology is clearly explained, making the paper easy to read and understand.
+ Strong Experimental Results: The results are convincing, demonstrating that DiSF outperforms existing methods consistently across multiple benchmarks and model sizes.
+ Thoughtful Comparisons: Comparisons with six baseline methods are thorough, providing a solid context for the effectiveness of DiSF.
+ Comprehensive Ablation Studies: The extensive ablation studies offer valuable insights into the impact of various factors such as data selection budget, model architecture, and feature extractors.

### Weaknesses
 + Limited Scale of Experiments: The experiments are limited to models up to 1.1B parameters. While the results are promising, it would be beneficial to see how the method scales to larger models commonly used in current LLM research.
+ Scalability Concerns: There is uncertainty about whether the proposed method can maintain its efficiency and effectiveness when applied to larger datasets.

+ Lack of Detailed Computational Cost Analysis: The paper lacks a thorough analysis of the time and computational resources required for the data selection process. This makes it difficult to assess the practical applicability of the method, especially for large-scale datasets and models. It is unclear how the computational cost scales with the size of the dataset and the selection budget. Specifically, the paper does not provide a breakdown of the time spent on feature extraction, covariance matrix computation, and the greedy optimization process, which are all critical for evaluating the method's efficiency.

### Questions
The paper appears to lack a detailed analysis of the time and computational costs associated with the data selection process. How long does it take to complete the data selection using DiSF, and is it efficient enough to be practical for larger datasets?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the DiSF (Diversified Submodular File Selection) algorithm to combat dimensional collapse in Large-Language Model (LLM) pretraining. The DiSF algorithm is designed as a subset selection task with a goal of selecting a diverse subset from an unlabeled training corpus and is achieved by maximizing a submodular information function over the complete unlabeled set with sample interactions modeled through a normalized covariance matrix. The paper demonstrates upto 1.5x training efficiency and upto 5x data efficiency on several benchmark datasets.

### Strengths
The strengths of this paper can be summarized as below - 

1. The paper address the task of data-efficient LLM pretraining while boosting performance on several benchmark tasks by minimizing the impact of dimensionality collapse which is a critical challenge in this domain. 

2. The authors clearly demonstrate the impact of dimensionality collapse in existing approaches targeting data-efficient LLM training and establish the requirement for decorrelated text samples during the training process to minimize its effect.

3. The DiSF algorithm models this requirement as a diversity driven selection problem and achieves this my training the underlying LLM on a subset of data selected by maximizing a submodular function $C(U, M)$ over the complete unlabeled set $\mathbb{D}$. This proposed methodology is strongly supported by experimental evidence on multiple benchmark datasets.

### Weaknesses
Although the results demonstrated in the paper are impressive the following weaknesses/ questions need to be addressed.

1. Although the subset selection mechanism in DiSF depends on submodular maximization of $F_{M}^{DiSF}(U)$ but the proof of submodularity of $F_{M}^{DiSF}(U)$ has not been provided. The paper presents only an empirical proof of monotonicity through Figure 4 but that is not deemed sufficient (Fujishige, 2005) to prove a function to be submodular. The authors must provide proof of $F_{M}^{DiSF}(U)$ demonstrating the diminishing marginal returns property described in lines 232- 234.

2. Diversity driven subset selection for data-efficient LLM pretraining is not novel to the current paper. Prior work like INGENIOUS (Renduchintala et al., 2023) have demonstrated significant improvements in model performance while being data-efficient. The authors should compare against such methods to study the impact of dimensionality collapse and the diversity selection algorithm.

3. Submodular Functions like Log-Determinant, Facility-Location etc. have been shown to model diversity in several tasks like summarization (Kumari et al., 2024, Kothawade et al., 2022) and subset selection (Jain et al., 2023, Lin and Bilmes, 2011) to name a few. What is the justification of introducing only $F_{M}^{DiSF}(U)$ (Equation 7 in the paper) rather than any known submodular functions ? The The authors should compare the performance of DiSF when the underlying function is chosen to be some/all of the popular submodular functions proven to be effective for diversity selection.

4. Although the experimental results in Table 2 show a strong average performance across datasets, when the budget increases from 10B to 50B (5x increase in number of available training examples) the performance gain (overall) is quite small. Did the authors perform any additional experiments or theoretical analysis to justify this result ?

Some minor questions/ suggestions -
1. Section 2.3 can be moved higher up in the paper or a brief explanation on the cause and effects of dimensionality collapse should be highlighted in Section 1 for better readability.

2. Phrases like "Diversified Submodular File Selection" (line 19, 88, 183-184 ...), "decorrelated text files" (line 20, 89, 184 ...) has been repeated several times in the paper which should be reduced to improve readability.

3. Do the authors plan on releasing the code for reproducing the results from the paper in the near future ?

4.  In Equation 8 the $\text{argmax}$ is applied over $\mathbb{D} \setminus U$ which seems to be redundant. To the best of my knowledge, during the course of the greedy optimization process in Algorithm 1 of the paper, DiSF selects the sample with the highest information gain which inherently excludes duplicate samples which are already selected in U.

### Questions
Please refer to the weaknesses for detailed questions.

### Soundness
3

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
4

### Summary
The authors propose a diversified submodular file selection algorithm (DiSF) to select sample set with more diverse data. It can alleviate dimensional collapse problem in feature space and enable LLM model to have generic performance.

### Strengths
The paper addresses an important problem in LLM pretraining and proposes a simple yet effective method. The writing is clear and the narrative is easy to follow, facilitating understanding of complex concepts.

### Weaknesses
No major weakness.

### Questions
1. It is recommended to provide the sample size and performance analysis experiments under the full data case and data selection case in different datasets.
2. It is suggested to provide time complexity and space complexity metrics on Table 2. The experiment in Section 'Selection scale' is not enough to illustrate the computational efficiency of the proposed method.
3. The performance improvement in Table 2 is limited, most of which are within ±0.5 (within the error range), and reasonable analysis is needed to illustrate the effectiveness of the method.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a novel file selection method for LLM pretraining to avoid the dimensional collapse issue. The method can achieve greater uniformity across feature dimensions, while the other methods usually get a long narrow feature space, limiting their performance on all the tasks.

### Strengths
1. This paper observes the drawbacks of the other file selection methods for LLM pretraining, which usually obtain quite narrow feature space, and are hard to obtain good results for all the tasks.

2. The proposed method is interesting, which converts the uniformity of the eigenvalues of the covariance matrix into minimizing the F norm of the covariance matrix, then uses a submodular optimization to solve it.

3. Experimental results on 7 tasks show the proposed method achieves a higher average perfomance than the other baselines, and is quite data efficient compared to full data pretraining.

### Weaknesses
1. The observation in figure 2 is evaluated on the SlimPajama. Do these methods have the same phenomenan on the other pretraining corpus.

2. In the efficiency analysis, comparing with full data pretraining is not enough, the comparison with the other baselines is not given.

### Questions
What does (1-e^-1) approximation mean in the abstract.

### Soundness
2

### Presentation
2

### Contribution
2
