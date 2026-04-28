# Detecting Training Data of Large Language Models via Expectation Maximization

- Decision: Reject
- Avg Score: 3.75
- Scores: 5, 3, 1, 6

## Abstract
The widespread deployment of large language models (LLMs) has led to impressive advancements, yet information about their training data, a critical factor in their performance, remains undisclosed.
Membership inference attacks (MIAs) aim to determine whether a specific instance was part of a target model's training data.
MIAs can offer insights into LLM outputs and help detect and address concerns such as data contamination and compliance with privacy and copyright standards.
However, applying MIAs to LLMs presents unique challenges due to the massive scale of pre-training data and the ambiguous nature of membership.
Additionally, creating appropriate benchmarks to evaluate MIA methods is not straightforward, as training and test data distributions are often unknown.
In this paper, we introduce \ours, a novel MIA method for LLMs that iteratively refines membership scores and prefix scores via an expectation-maximization algorithm, leveraging the duality that the estimates of these scores can be improved by each other.
Membership scores and prefix scores assess how each instance is likely to be a member and discriminative as a prefix, respectively.
Our method achieves state-of-the-art results on the WikiMIA dataset.
To further evaluate \ours, we present \ourbenchmark, a benchmark built from OLMo resources, which allows us to control the difficulty of MIA tasks with varying degrees of overlap between training and test data distributions.
We believe that \ours~serves as a robust MIA method for LLMs and that \ourbenchmark~provides a valuable resource for comprehensively evaluating MIA approaches, thereby driving future research in this critical area.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a membership inference attack for LLMs. Their key insight is that previous work requires non-member prompts for good membership inference, so one can bootstrap good prompts from membership scores and vice versa. This leads them to iteratively improving (non-member prompts) and membership scores. Empirically, the proposed method exhibits significant improvements in the attack AUROC when compared with prior art.

### Strengths
* The idea of using prefix scores to refine membership scores and vice versa is novel.
* The empirical results are also quite strong, which leads me to believe that the proposed method will be a good benchmark for future methods.
* I commend the authors for the care they have taken to design a new benchmark. I believe it is quite significant and will be valuable for future work.

### Weaknesses
## Main concerns
These major considerations need to be addressed for acceptance, in my opinion:

*   **Metric**: The paper reports the AUROC only but not [TPR @ low FPR](https://arxiv.org/pdf/2112.03570), which is the better metric per community consensus. It is fine to design the method based on AUROC but TPR @ low FPR should be reported too.

*   **Computational complexity**: * The paper lacks a precise and quantitative description of the computational complexity. I would recommend the authors to describe the complexity of the proposed method (e.g. in terms of tokens consumed by the LLM) and an apples-to-apples comparisons with baselines. Some factors to take into account are the number of iterations, number of shots, cost of computing the prefix/membership score, etc. Furthermore, reporting wall-clock times for the proposed method and baselines would be crucial for practical evaluation.

*   **Missing experiments**: While the results are strong, the coverage/ablations of the current experiments can be greatly improved. Examples:
    - Varying number of shots for the proposed method and ReCaLL. I expect the proposed method to be more robust than ReCaLL, but a plot to this effect is missing. It is unclear if the proposed method uses a single shot or multiple shots, and this needs to be clarified. If multiple shots are used, then a plot is necessary to show how performance varies with the number of shots.
    - Compare baselines in a compute-constrained setting, so that all methods receive the same computational budget.
    - Line 359 says that "EM-MIA requires a baseline sufficiently better than random guessing". How much better? I would like to see some ablations with different initialization methods to understand how good the initialization must be.
    - Vary the number of iterations of the proposed method.
    - Lines 381-395: the effect of reusing test examples for ReCaLL needs to be explored through ablations too.
These experiments are very valuable for the community. For example, how robust your method is to variations in the hyperparameters?

## Other suggestions/comments

*   **Clarity**:
    - It is not clear initially if the paper deals with MIA in the pretraining or finetuning settings. It would be helpful to clarify that upfront.
    - The authors should provide some intuition of *why* ReCaLL works, given that it is a super recent development.
    - "Prefix score" in the abstract is very ambiguous. The abstract should provide a clearer description of how the membership score is constructed using non-member prefixes, and how the prefix score measures the discriminative power of a prefix for membership inference.
    - It is hard to interpret the experimental results as the tables are full of numbers. The authors may wish to present the results for one length and relegate the rest to the appendix. It would also be helpful to use some plots to demonstrate results.

*   **OLMoMIA design not clear**: The second half of section 5 is written in a very casual manner and is ambiguous. I do not understand how the easy/medium/hard settings are designed. Further, are members and non-members clustered together or separately (Line 322)? I would recommend the use of more precise language (e.g. with equations). Alternatively, some figures here can greatly help (with pseudocode in the appendix). For instance, Fig 2 is quite nice.

*   **Missing refs**: [Kandpal et al. (EMNLP '24)](https://arxiv.org/abs/2310.09266), [Maini et al. (NeurIPS '24)](https://arxiv.org/abs/2406.06443)


### Questions
* Why use the ratio of the log-likelihoods instead of the difference? Theory (e.g. Neyman-Pearson lemma) suggests very strongly that the ratio of the likelihoods (i.e. difference of log-likelihoods) is the right operation, and the ratio of the log likelihoods can be degenerate is some circumstances. Can the authors try out a variant of ReCaLL with the difference of log likelihoods?

* The OLMoMIA benchmark only appears to work with the OLMo model. Do we have any evidence that MIA results on one model will transfer to another when factors such as distribution shift are controlled appropriately?

* Why do the authors strongly emphasize expectation maximization? This is super puzzling to me because EM is a very specific optimization algorithm used in the context of latent variable models or missing values by maximizing the ELBO (which is a provable lower bound, as described in Sec. 8.7.2 of [Murphy's book](https://probml.github.io/pml-book/book1.html)). The only resemblance I see is that there is iterative/alternating optimization, but that is very common in machine learning, optimization, statistics, etc. Unless I'm missing some deeper insight, I would suggest that the paper would be better off without a shallow and misleading comparison to EM.

* What are your plans for releasing code/software?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new MIA method called EA-MIA, based on RECALL, which iteratively improves MIA scores and prefix scores via an expectation-maximization algorithm. The authors also introduce a new dataset, OLMoMIA, derived from the OLMo dataset, featuring different levels of membership inference difficulty.

### Strengths
- The authors employed interesting clustering techniques and embedding models to design different levels of membership inference difficulty for OLMoMIA.
- The authors provide analysis over ReCaLL assumptions and weaknesses.

### Weaknesses
 - The authors used the WikiMIA dataset in different parts of the paper (for example, for observing which update rule to use for EA-MIA). However, as they mentioned in Section 2.3, wikiMIA is not a reliable dataset to be used for MIA experiments.

- The authors did not provide the results of their approach on the MIMIR dataset, a very well-known dataset in MIA literature. They provided this reason in Section 6.1: "Although EM-MIA requires a baseline sufficiently better than random guessing as an initialization, there is currently no such method for MIMIR (Duan et al., 2024). Therefore, we skip experiments on MIMIR, though this is one of the widely used benchmarks on MIA for LLMs". However, mink++ paper reported AUC-ROC scores of 61.1 and 74.2 for Pythia-12b and on MIMIR wikipedia and Github splits respectively, which could be used as good initializations for EM-MIA.

- Reporting TPR for low FPR is an important experiment results for a new MIA to be compared to other MIAs. This paper does not provide any results on TPR for low FPRs.

### Questions
- Section 3.2 contains experiments for MIA against LLaMA and OPT models using the wikiMIA dataset. I understand that these target models have not seen the non-members because of the release date. My question is: How are we sure that the members are included in their training datasets? For example, some Wikipedia articles (published before release dates) might be part of their test partition or validation partition. 

- The authors mention that the concentration of non-members sometimes produces better prefix scores. What is the impact of the prefix size on prefix scores? It would be great to see an ablation study showing how different prefix sizes impact the prefix scores. 

- What is the computation cost of the iterative approach of maximization. I mean in Alg 1, for each p in D_test and x in D_test, we are doing multiple round of refining r(p) and f(x). Is it expensive to these operations in multiple rounds?

- What is the impact of number of clusters in difficulty level of OLMoMIA? Why did the authors use k=50? it would be interesting to see more about the clustering hyperparameters impacts on the difficulty metric of membership inference?

- Why mink and mink++ in table 2 do not get better AUC-ROC when we are switching the difficulty level? And why they don't get better for larger target text (128 compared to 64)?

- The authors in section 6.3 mentioned that: " We also observed that EM-MIA is not sensitive to the choice of the initialization method and the scoring function S and converges to similar results" Could you please elaborate more on the intuition behind this? 

- It would be interesting to see n-gram overlap ratio between members and non-members (similar to ref AA) as a difficulty metric in easy, medium and hard splits of OLMoMIA.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper tackles the problem of resolving if a given data point was used to train a large language model (LLM). This work follows a long line of previous papers that tried to solve the problem, however, as we already clearly know, it is impossible to solve it based on the result of Maini et al. ICLR 2021 [1] (see Theorem 2). The authors state at the end of their introduction that also their method is also unsuccessful in detecting members vs non-members: “Throughout the extensive experiments, we have shown that EM-MIA is a versatile MIA method and significantly outperforms previous strong baselines, though **all methods including ours still struggle to surpass random guessing in the most challenging random split setting.**” This is not a surprise based on the aforementioned Theorem 2.

**References:**

1.	Dataset Inference: Ownership Resolution in Machine Learning. Pratyush Maini, Mohammad Yaghini, Nicolas Papernot, ICLR 2021 (Spotlight).

### Strengths
1.	The benchmark to assess how good the MIA methods are in distinguishing between members and non-members. However, based on the aforementioned Theorem 2, all these methods fail while we train the LLMs on more data and a given sample is seen only once during the training process.

### Weaknesses
1.  The paper considers a simple scenario where “blind baselines can beat their membership inference attack” [1].
2.  The paper also fails on the benchmarks proposed by Maini et al. 2024 based on the training and validation splits from the Pile dataset [2].
3.  The membership inference attack is clearly defined, e.g. [3] and the assumptions made in this paper violates this basic requirement, based on the following claim: “Although this setting seems theoretically appropriate for evaluating MIA, there is no truly held-out in-distribution dataset in reality because LLMs are usually trained with all available data sources.” Thus, either another attack is proposed or the proposed attack has a random performance when claimed to be the membership inference attack.
4.  This method does not work well on the standard benchmark for membership inference on LLMs MIMIR by Duan et al 2024 (as stated at the beginning of Section 5).
5.  The designed OLMoMIA benchmark (as described in Section 5) is the same as proposed in Duan et al. 2024 as well as in Maini et al. 2024 [2]. The experiments are lacking the assessment on the Pile dataset: Section 6.1: “we skip experiments on MIMIR, though this is one of the widely used benchmarks on MIA for LLMs”
6.  No source code is provided!
7.  The results in Figure 1b with TPR@5%FPR = 93.4 are worse than “Blind Baselines” (Table 1) which report 94.4%.

### Questions
1.	Section 2.3: What is expected from the recently published papers? What kind of adoption is required? Based on this statement: “Several ongoing attempts (Meeus et al., 2024b; Eichler et al., 2024) aim to reproduce setups that closely resemble practical MIA scenarios, but none are sufficiently effective to gain widespread adoption in the community.” These papers were published this year.
2.	Section 3: “Without access to non-members (or data points with high prefix scores), ReCaLL’s performance could be significantly lower.” Would you please measure it precisely? 
3.	Section 3: “We propose a new MIA framework that is designed to work robustly on any test dataset with minimal information” What is defined by working robustly? What is the minimal information?
4.	Section 4: “We target the realistic MIA scenario where test data labels are unavailable.” What are the test data labels?
5.	Section 4: “We measure a prefix score by how ReCaLLp on a test dataset D_test aligns well with the current estimates of membership scores f on D_test denoted as S(ReCaLL_p, f, D_test).” What is the D_test? How is S computed? D_test looks like the dataset for which we want to infer the membership. This should be clearly stated!
6.	What is the $\delta$ at the end of Section 5?
7.	The proposed method states that we could use something instead of clearly indicating what is used. For example, is the Kendall’s tau or Spearman’s rho used?
8.	The subsection about external data is totally not fitting to this paper. Why do you consider access to members and non-members? You make this assumption but then state that you never consider this in your experiments. If so, this subsection should be removed.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a new method to improve membership inference attacks (MIAs) on large language models (LLMs) named EM-MIA. 
EM-MIA is an iterative algorithm based on the expectation-maximization (EM) framework, which jointly refines membership and prefix scores to improve accuracy. 
The paper also introduces OLMoMIA, a benchmark allowing controlled experiments on MIA difficulty levels by adjusting training and test data distribution overlap. 
Through extensive experiments, EM-MIA achieves state-of-the-art performance on the WikiMIA dataset and outperforms existing methods (e.g., loss-based, min-k%, zlib, and ReCaLL) across various conditions in OLMoMIA.

### Strengths
S1. The proposed EM-MIA framework introduces a novel approach to MIAs on LLMs by leveraging the expectation-maximization algorithm to iteratively enhance membership and prefix scores.

S2. There is a comprehensive set of experiments/evaluations that compare EM-MIA to strong baselines, including ReCaLL, across multiple benchmarks such as WikiMIA and OLMoMIA. 

S3. Given the growing deployment of LLMs and the increased need for privacy compliance, this work addresses a highly relevant issue in model auditing and data privacy. The authors also considered recent works that criticize MIAs on LLMs, thus also considering random splits for train/test sets (where the result is similar to other methods ~50%).

### Weaknesses
Naturally, the iterative nature of EM-MIA may introduce additional computational costs compared to some baselines, especially for larger datasets or LLMs. The paper could provide an analysis of the computational complexity, with timing comparisons to baselines like ReCaLL. Highlighting any trade-offs between accuracy and computational demands would help readers assess EM-MIA's scalability and practical feasibility.



### Questions
- Can the authors please elaborate on the computational requirements of EM-MIA relative to baselines like ReCaLL?

- The paper mentions that EM-MIA’s iterative process can be initialized with different methods, yet Min-K%++ was chosen for initialization. Could the authors please provide an ablation study or justification for this choice, and discuss how EM-MIA performs when initialized with other baselines (e.g., Loss or Avg)? This information could illustrate the robustness of EM-MIA’s initialization and its dependence on a well-performing baseline.

### Soundness
3

### Presentation
3

### Contribution
3
