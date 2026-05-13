# Towards Real World Debiasing: A Fine-grained Analysis On Spurious Correlation

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Spurious correlations in training data significantly hinder the generalization capability of machine learning models when faced with distribution shifts in real-world scenarios.
To tackle the problem, numerous debias approaches have been proposed and benchmarked on datasets intentionally designed with severe biases.
However, it remains to be asked: \textit{1. Do existing benchmarks really capture biases in the real world? 2. Can existing debias methods handle biases in the real world?} To answer the questions, we revisit biased distributions in existing benchmarks and real-world datasets, and propose a fine-grained framework for analyzing dataset bias by disentangling it into the magnitude and prevalence of bias. 
We observe and theoretically demonstrate that existing benchmarks poorly represent real-world biases. 
We further introduce two novel biased distributions to bridge this gap, forming a nuanced evaluation framework for real-world debiasing.
Building upon these results, we evaluate existing debias methods with our evaluation framework. Results show that existing methods are incapable of handling real-world biases.
Through in-depth analysis, we propose a simple yet effective approach that can be easily applied to existing debias methods, named Debias in Destruction (DiD).
Empirical results demonstrate the superiority of DiD, improving the performance of existing methods on all types of biases within the proposed evaluation framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper examines whether existing benchmarks can effectively capture biases present in real-world datasets. To address this, the authors introduce a new evaluation framework that assesses dataset bias from the perspectives of magnitude and prevalence. Experimental results indicate that current real-world datasets primarily exhibit a low magnitude, low prevalence distribution, highlighting a gap compared to synthetic benchmarks. Furthermore, the authors discuss the debiasing effects of existing DBAM methods under three different bias distributions. They also propose a new debiasing method, DiD, which enhances the bias capture module and improves the accuracy of bias feature learning through a feature destruction approach.

### Strengths
1. The motivation for this research is sufficient, as there is widespread concern about whether existing benchmarks can truly reflect the biases present in real-world datasets.
2. This paper presents a fine-grained framework that evaluates dataset bias through the metrics of magnitude and prevalence, offering a multi-dimensional approach.
3. The authors highlight unique characteristics of real data distribution, which is essential for understanding the effectiveness of debiasing methods in practical scenarios.
4. They enrich the diversity of synthetic datasets, adding valuable resources for further research in debiasing.

### Weaknesses
1. **Clarity and Presentation Issues**
    * Line 160: Are you referring to "measure spurious correlation according to the probability of the correlated class $a_t$ within samples with biased feature $a_s$"?
    * Figure 2b may contain a scaling error on the x-axis that could impact result interpretation.
    * Some descriptions are ambiguous. For instance, the term “realistic” in Table 2 might misleadingly imply real-world data, whereas it refers to synthetic datasets. Clarifying this distinction would improve reader understanding. In Appendix D.2, the BAR dataset is described as "a real-world dataset," while in Section 2.1, it is referred to as a "semi-synthetic dataset."
2. **Limitations in the Scope of the DiD Method**
   *  The feature destruction in DiD method has a limited scope of applicability. While we acknowledge its rationale in visual contexts, identifying or destructing target features is challenging in more general scenarios. Could the authors provide potential solutions for feature destruction in structured real-world datasets (e.g., Adult and COMPAS) or within the NLP domain?
3. **The experiments are insufficient**
    * The selection of baselines is limited. Why are comparisons made only with DBAM methods? Would it not be beneficial to include comparisons with data generation methods as well?
    * As mentioned in Section 2, real-world data is primarily characterized by LP bias distributions. In the results presented in Table 1, why does the DiD method underperform compared to the ERM method under LP distribution?
    * Considering the importance of BC samples in debiasing, why does the DiD method exhibit negative transfer in accuracy on BC samples in some experiments?

### Questions
1. In Section 4.2, although BN samples have lower weights under LP conditions, is it possible that, due to their being learned more frequently than other samples, the model still captures the information contained in BN samples without overlooking it?
2. As mentioned, real-world data primarily exhibits LMLP bias distributions. Are there experimental results for Emphasis on BN samples under LMLP conditions?
3. Could the authors provide experimental results for the DiD method on real-world datasets to validate its effectiveness on actual data?

If the authors are willing to address our concerns, we are open to revising the scores during the rebuttal stage.

### Soundness
2

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
3

### Summary
The authors mainly aim to address the discrepancy between benchmark datasets and real-world datasets. Specifically, they observe that real-world datasets exhibit low prevalence, while commonly used datasets have high prevalence. They theoretically support this observation by demonstrating that high prevalence can occur under two unrealistic assumptions. However, in low-prevalence scenarios, the auxiliary models might fail because bias-neutral and bias-conflicting samples constitute the majority, leading these models to learn target attributes too quickly. To address this issue, the authors propose DiD, which disrupts the auxiliary models from learning target attributes through patch shuffling. In experiments, they demonstrate that their method significantly improves upon existing methods across all settings.

### Strengths
* By analyzing the datasets from the perspective of prevalence and magnitude, the authors identify significant differences between real-world datasets and benchmark datasets.
* The authors provide theoretical support for this observation.
* The paper is well-written.

### Weaknesses
 - Although a theoretical background is provided, the experimental evidence appears limited. It would strengthen the work to demonstrate low prevalence on additional datasets, such as an NLP dataset and CelebA, commonly used in the spurious correlation domain. In particular, CelebA is not suggested for evaluating the methods for handling spurious correlations, yet it has a substantial amount of data and exhibits strong biases despite being a natural dataset. Demonstrating that its prevalence aligns with the claim would strengthen the argument. Furthermore, it would be helpful to show the performance in CelebA and NLP tasks as well.
- For B2T [1], which does not rely on the easy-to-learn property of bias, there seems to be no reason for it to fail in low prevalence settings. A discussion of the advantages of the proposed method over B2T in such scenarios would be required. Additionally, since B2T is a recent approach, it would enhance the paper to include it as a baseline on natural datasets.
- DiD lacks general applicability. Specifically, it relies on the assumption that bias will be insensitive to patch-shuffling, while the target will be sensitive to it. However, this approach may not work for other types of semantic biases beyond background or perturbation. Furthermore, this method seems to be difficult to use in NLP tasks.
- The attempt to improve the performance in low-bias settings while keeping the performance in high-bias settings is not the first [2].
- In Table 3, although the proposed method is designed to perform well in low prevalence settings, it shows lower performance than ERM in the unbiased setting.
- I couldn’t find a clear description of the metric used for Waterbird in Table 2 in the main paper. Given the reported performance, it seems that either a different metric from the commonly reported worst-group accuracy was used, or the setting doesn’t align with prior methods. It would enhance the evaluation to show whether worst-group accuracy improves when using the same experimental setup as JTT [3].

### Questions
* Including results from GroupDRO [1] as an upper bound for comparison would be helpful.

[1] Sagawa, Shiori, et al. "Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization." ICLR, 2020.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the suspicious correlation problem. The authors first identify the unrealistic suspicious correlation patterns in benchmark datasets. Based on this observation, the authors reveal that the gap between benchmark and real-world datasets mislead the development of debiased methods. The authors further propose a new debiasing method, enhancing exitsing methods across different biases.

### Strengths
1.	The authors identify a key problem in existing benchmark datasets, which mislead the development of existing methods.
2.	The analysis on existing metrics provides insight in understanding existing benchmarks and developing better methods to handle realistic bias.
3.	The authors propose a new debiasing method named bias capture with feature destruction to destroy the effect of target features.

### Weaknesses
1.	The motivation of different choices of metrics is not clear.
2.	Some of the assumptions in analysis are too strong or unrealistic.

### Questions
1.	Line 198, why choosing KL divergence here, but using total variation in later analysis.
2.	Line 198, since the KL divergence is non-symmetric (and probably ill-defined when encountering zero probability), will other metrics, e.g., JS divergence, be a better metric.
3.	Eq.(1): can you switch the role of $y^t$ and $y^s$, i.e., $KL(p(y^s), P(y^s|y^t))? What’s the difference between these two formulations?
4.	Is there any justification on whether the two proposed metrics, i.e., magnitude and prevalence, are (1) complementary/orthogonal, i.e., they depict dataset property from quite different aspects, and (2) complete, i.e., they can completely depict the dataset properties.
5.	Line 269, data distribution: the analysis assumes that both target and suspicious attributes are binary, can you analysis generalized to multi-class/non-binary settings?

### Soundness
2

### Presentation
3

### Contribution
3
