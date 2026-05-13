# Privacy Breach Detection by Non-Parametric Two-Sample Tests

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
With the proliferation of machine learning services, the risk of privacy breaches has never been higher, owing to the need for collecting -- sometimes by any means necessary -- valuable, yet sensitive training data. When an unsanctioned data access occurs, it may become apparent after the fact, in the predictive models that have been trained on compromised data. This calls for effective membership inference methods, enabling an evaluator to identify privacy breaches. Distinct from traditional membership inference attacks (MIAs), which focus on determining whether individual data records were used in training, this study centers on the evaluation of sets of records, particularly when only a small proportion of the set are training members. In this scenario, traditional MIAs often suffer from non-ideal evaluation reliability. To address this issue, from a privacy evaluator's perspective, we propose a novel approach for membership inference, applicable not to individual records but to sets thereof. It relies on a non-parametric two-sample test, which leverages the differences between high-level representation to infer membership. Based on extensive experiments, our proposed High-level Representation-based MMD (HR-MMD) test exhibits high sensitivity in distinguishing between the training and non-training sets, with ideal type I error, making it a powerful membership detection tool. Our study offers insights into an alternative privacy breach detection scenario and opens up a promising avenue for privacy evaluation based on membership inference tests.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study introduces a method for evaluating the occurrence of membership inference using a two-sample test on a set rather than individual data points, taking into account the reliability of membership inference evaluation. The proposed method is experimentally shown to be highly sensitive to the distinction between data used for learning and data not used for learning.

### Strengths
- Introduced statistical inference into the membership inference and established statistical significance guarantee on the inference of membership
- Proposed a deep kernel function that is useful for membership inference for deep classification models and analyzed the test statistics and asymptotic behavior of the test statistics
- Evaluated performance through experimental evaluation

### Weaknesses
 - The explanation of the experimental setup and evaluation criteria is insufficient, so it is difficult to determine whether the experimental results show the superiority of the proposed method.

 - The comparison between the proposed method and existing membership inference attacks (MIAs) is unclear, particularly regarding how the evaluation metrics (TPR, Type I error, and Type II error) are computed. The proposed method outputs decisions for a given dataset, while some existing methods output decisions for each data point. It remains unclear how these different output granularities are reconciled for a fair comparison. Specifically, it is not clear if all methods in Fig 1(a) follow the set-based MIA scheme, and how the evaluation is conducted for statistical baselines versus traditional MIAs.

 - The experimental setup lacks sufficient detail to assess the validity of the results. For instance, the consistent use of a 10% training data to evaluation data ratio, as noted in Appendix G.6, raises concerns about the generalizability of the findings. It is unclear how the method performs under different data distributions and varying ratios of member to non-member samples.

### Questions
Line 429: Could you explain why the maximization of J improves the power? I could not understand from the explanation in the manuscript.

Line 443: If parameters of k_w are optimized under the setting of the alternative hypothesis, can we say this is also appropriate under H_0?  

Sec 6: 
- According to Appendix G.6, the ratio of training data to evaluation data is consistently set to 10% in the experimental results, which seems unreasonable. This ratio must be changed to evaluate the proposed and comparison methods' performance.

- A clear explanation of the evaluation metric is necessary. The proposed method outputs decisions for the given dataset, while some existing methods output decisions for each data point. Since I could not find an explanation on how TPR, type 1 error, and type 2 error are evaluated, it is difficult to determine whether the proposed method was compared correctly with the comparison method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies the usage of non parametric two-sample tests for membership inference attacks. These enable set-based membership inference attacks with a much stronger performance than existing per-sample membership inference attacks. Empirical results are conducted over standard image datasets and include a text dataset and a tabular dataset. The results show an attack that is significantly stronger than existing MIAs.

Edit: Raised score after rebuttal to 5, but still leaning reject (perhaps, more a 4).

### Strengths
- Strong empirical results indicating perfect TPR at low FPR.

- Generic protocol that can accommodate various input statistics.

- Motivation is clear and the work is important.

- The organization is relatively clear.

### Weaknesses
 - It is unclear what the performance improvement of representations is. Often, this threat model is not possible in practice, e.g., for the detection scenario mentioned. Specifically, the paper does not adequately address the practical limitations of assuming access to high-level representations, such as those from the last layer of a neural network, in real-world threat models. This is particularly concerning in scenarios where the adversary might not have direct access to these internal representations. Furthermore, the paper lacks a clear explanation of how these high-level representations are obtained and what impact different choices of representation have on the attack performance. There is no ablation study in the main body to justify the choice of using representations from the last layer.

- Almost all experiments are in the appendix, with not even a description in the main-body. This makes the paper extremely difficult to follow and assess. The lack of experimental details in the main body, such as the specific datasets used, the model architectures, and the training procedures, makes it challenging to understand the context and significance of the results. Similarly, nearly none of the empirical setup is described in the main-body, including necessary information to understand the results. For example, what are each of the attacks? The two-sample attack is a set-based attack, how is this being compared with prior non-set-based attacks? The paper needs to clearly define the baselines and explain how they are adapted for set-based comparisons.

- This work suggests using high-level representations such as those from the last layer. How are those obtained and where are these ablations?

- Theorem 1 appears convoluted. I have not understood what this brings to the paper. Though I understand that it is optimizing the kernel so as to achieve high test performance, why is this necessary? What is the baseline performance without doing this? How does this compare to the other methods for set-based inference? The paper does not clearly explain the necessity of optimizing the kernel and lacks a comparison to a baseline without this optimization. The theoretical analysis is not clearly linked to the empirical results, making it difficult to assess the practical implications of the theorem.

- Set-based MIAs have already been studied, e.g., dataset inference [https://arxiv.org/abs/2104.10706], user inference attacks [https://arxiv.org/abs/2310.09266], and dataset inference for llms [https://arxiv.org/abs/2406.06443]. All of these show significant improvements over the standard per-sample MIAs. Comparisons against these are a must, as this work employs similar techniques.

[NIT] Though confidence-based attacks may be thwarted by defenses like memguard, these are easily thwarted by label-only attacks.

### Questions
Can the authors comment on the feasibility of using this for LLMs?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies membership inference attacks (MIA) on a set of samples. Unlike the normal MIA task, which determines the membership status of individual samples, this work introduces a two-sample test to detect whether a test dataset includes any elements from the training set. The setup is as follows: the attacker has access to a black-box model, with test statistics that can be either intermediate embeddings or output loss scores, and a validation set known to have been excluded from training. The authors employ HR-MMD, a deep kernel-based two-sample test from prior work (Liu et al., 2020b). The primary improvement over prior MIA is the improved TPR, which is due to to HR-MMD’s ability to optimize test power. Experimental results confirm this improvement.

### Strengths
This paper provides a practical method for MIA, which improves TPR significantly.

### Weaknesses
I have two major concerns: 1) the experiments are only on small scaled datasets. 2) the algorithmic difference and technical contribution compared prior work Liu at el 2020b is not well-addressed. I feel like this is just one application of the prior work. 

Some other concerns: 1) typically when we compare the performance of MIA, we consider AUROC. This paper only shows type-1 and type 2 error. The trade-off is not clearly presented. 2) In the Appendix B practical settings 1, I do not think it is practical. In practice, we usually don't have access to a training set, because it is private. And this makes evaluation of FPR hard.

### Questions
1. When compared with prior MIA works, how is this FPR calculated exactly? For example, for the one experiment with 90% non-training samples, how do you convert the FPR for individual samples to FPR on a set of samples? I am a bit confused.

2. Can you use this method for auditing differential privacy?

3. In a practical setting, can we use this method to estimate how much fraction does the test set contain the training data?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In the case where data samples stolen from a larger dataset are used to train a third-party model, proving the privacy leak through membership inference attacks may return high false positive rates due to the non-stolen members of the (partly) compromised dataset weakening the audit and the case that a model was trained on a stolen data.

To resolve this, the paper proposes HR-MMD, an algorithm that requires the target model, validation data used in the target model, and the (possibly compromised) target dataset, to perform a statistical test to see whether the validation dataset and the target dataset come from the same distribution. This relies on the differences in the target model's high-level representation of training data and validation data based on the generalization gap. The test finding that the target dataset is the same in distribution as the validation set in terms of high-level representations (the null hypothesis) gives evidence that the target dataset was not used to train the target model. The alternative gives evidence that the target dataset was used to train the target model and as such was compromised, assuming that OOD data has been accounted for.

### Strengths
* The approach of this paper is novel as it does not rely on heuristics compared to some existing method which require them to achieve practical FPRs in the condition where non-training members dominate a (compromised) dataset.
  
* The method is adaptable to different current frameworks for evaluating a model such as loss functions and confidence scores.
  
* The results show that for similar FPR, the HR-MMD test achieves lower false negative errors in this problem setting.

* The writing style is clear, and the paper is pleasant to read.

### Weaknesses
 * It is not clear how robust this test is against out-of-distribution datapoints.

### Questions
* In the situation where $S_Y$ contains OOD samples (or since generally $S_Y$ may contain OOD samples) how is the HR-MMDs performance influenced by the traditional two-sample test needed to remove the OOD data. Since this "preliminary detection is crucial to ensure the integrity of the subsequent [HR-MMD]", how can one evaluate whether the chosen two sample test in the first step maintains this integrity?
  
* Practically, are there high-level representations that tend to work better with HR-MMD?

### Soundness
3

### Presentation
4

### Contribution
4
