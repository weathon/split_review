# Spurious Privacy Leakage in Neural Networks

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 8, 5, 3

## Abstract
Neural networks are vulnerable to privacy attacks aimed at stealing sensitive data. When trained on real-world datasets, these models can also inherit latent biases, which may further increase privacy risks. In this work, we investigate the impact of spurious correlation bias on privacy vulnerability, identifying several key challenges. We introduce _spurious privacy leakage_, a phenomenon where spurious groups can be up to 100 times more vulnerable to privacy attacks than non-spurious groups, and demonstrate how this leakage is connected to task complexity. Furthermore, while robust training methods can mitigate the performance disparity across groups, they fail to reduce privacy vulnerability, and even differential privacy is ineffective in protecting the most vulnerable spurious group in practice. Finally, we compare model architectures in terms of both performance and privacy, revisiting prior research with novel insights.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the finding that groups influenced by spurious correlations in datasets are more vulnerable to membership inference attacks (MIA) than other groups. The study also shows that Vision Transformers (ViTs) are not necessarily better than convolutional models at handling spurious correlations. The paper highlights how bias in neural networks affects privacy risks.

### Strengths
1. The paper attempts to undermine the relationship between bias an d privacy leakage. The key findings are well articulated via examperiments. 
2. The paper is overall well written and easy to follow.

### Weaknesses
1. The motivation is not very clear. What is the reason to assess privacy disparities between spurious and non-spurious subgroups?
2. The related work section is too brief considering the multiple topics the paper covers. Expanding it to include more of the relevant literature would strengthen the foundation. It is also unclear how the findings align with current research.
3. The experiments are not clearly explained. Including the choice of datasets and neural network models.

### Questions
Refer to the weakness section.

### Soundness
2

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
5

### Summary
This paper shows experimentally that in data with spurious correlations and imbalanced groups, the minority groups are more susceptible to membership inference attacks than the majority groups. This high level message -- that out-of-distribution examples tend to be less private -- was known before: see for example, Figure 13 in the LiRA paper, [1], where this fact is exploited to design better privacy tests, as well as [2]. However what I like about this paper is that they do a very comprehensive experimental study on real data, and show a number of additional conclusions, and hence there is value in accepting it. 
[1] https://arxiv.org/abs/2210.02912
[2] https://arxiv.org/abs/2202.05189

### Strengths
1. The paper presents highly comprehensive experiments that are quite well done. The results are well-presented, and well-supported by experimental evidence.

### Weaknesses
1. I would urge the authors to make some of the details a little bit more transparent in the main body. One difference between the standard setting and this work is that MIAs are used for fine-tuning and not pre-training data. This may mean that the fine-tuned datasets are very small per model. One of the best-kept secrets in LIRA-style membership inference is that the MIA is always carried on models that are trained on only a subset of the data, and making that subset bigger leads to worse "privacy loss". 

Since this paper is further using MIA on models fine-tuned on a small amount of data, what is the size of the data that the model is fine-tuned on?

2. I am also not sure how meaningful the differential privacy results are -- since here epsilon=128. That kind of value for epsilon offers quite negligible privacy. That being said the remaining results are quite interesting.

### Questions
See Weakness 1.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors uncover that spurious groups in datasets (i.e., groups affected by spurious correlations) are significantly more vulnerable to membership inference attacks (MIA) than non-spurious groups. Meanwhile, as the task complexity decreases (e.g., fewer target classes in the dataset), the privacy leakage for spurious groups remains constant or worsens, while leakage for other groups reduces. Moreover, despite improvements in group performance disparity through methods like DRO, DFR, and DP, these methods fail to address the privacy disparity among spurious groups. They also show that architectures like Vision Transformers (ViTs) are not necessarily more robust against spurious correlations than convolutional models under fair experimental setups.

### Strengths
- The paper focuses on the connection between spurious correlations and privacy leakage, an underdeveloped topic in trustworthy machine learning.
- The paper presents several interesting observations.
- The paper is well-organized and easy to follow.

### Weaknesses
1. The motivation behind evaluating privacy disparities among subgroups (spurious vs. non-spurious groups) is unclear. While the paper shows that existing methods (DRO, DFR, or DP-SGD) may not fully address these privacy gaps, it's unclear why privacy parity across subgroups could be a priority. Why should we care about these gaps?  Existing studies have examined the intersection of privacy and fairness, and specifically, subgroup-specific privacy vulnerabilities using MIA, demonstrating that minority subgroups experience higher privacy leakage. The manuscript should acknowledge prior contributions and clearly differentiate their findings from this existing work.

2. While the authors present technically interesting observations about privacy disparities, the results are more like experimental reports. It’s unclear how these findings can contribute to the field. For instance, could they inspire new defense strategies? Or inform advanced attack methods? 

3. The conclusions in Sections 3 to 5 are important but not well-supported as they rely on limited experiments, datasets, and methods, which is not convincing. For example, Section 4.2 states that DP fails to protect certain vulnerable groups in the data. The results contradict previous research suggesting that DP can protect sample vulnerabilities by preventing memorization. The finding comes from a single experimental setup. The scope is too narrow to fully support such a broad conclusion. More ablation studies are needed. 

4. The paper needs more detailed discussions and comparisons to better support the conclusions. It’s unclear how these findings are connected to current studies. For example, in Section 3, there is related work on subgroup evaluations of model fairness and privacy with MIA—are the findings consistent? For Section 4, previous studies have explored the utility tradeoffs of DP methods—do they also show a failure to protect samples? Similarly, in Section 5, prior research compares the model robustness of Vision Transformers and CNNs—do those results align? More discussion is needed across these sections to connect the findings with existing work.

5. The related work section feels too limited, given the paper covers multiple topics.

### Questions
see above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper examines how bias in neural networks affects privacy vulnerabilities, particularly focusing on spurious correlations. The paper has several findings after experiments.

### Strengths
The spurious privacy leakage in neural networks is an interesting topic and the paper has a good format emphasizing each finding after some experiments.

### Weaknesses
1. Current research has much more literature than what the paper presented in the related work section.
2. The authors should explain why these datasets are chosen and not the other datasets.
3. In Sec 3.1, the authors mention that "The largest privacy disparity is observed at ~3% FPR area of Waterbirds, where the samples in the most spurious group are ~100 times more vulnerable than samples in the non-spurious group." Where do "3%" and "100 times" come from? The figure does not clearly show this and the paragraph does not explain this.
4. The claim of "spurious groups can be up to 100 times more vulnerable to privacy attacks than non-spurious groups" is just a result from one data point. This is exaggeration and should not include in the abstract.
5. While the paper presents experiments for its findings, the limited number of experiments conducted for each conclusion raises questions about results. Additional experiments are needed for each finding.
6. Finding V claims that they draw the conclusion under a fair experimental setup. However, the authors use different hyperparameter settings for different models, which is not a fair comparison.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
