# Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models

- Decision: Accept
- Scores: 3, 8, 8, 6

## Abstract
In pretraining data detection, the goal is to detect whether a given sentence is in the dataset used for training a Large Language Model LLM). Recent methods (such as Min-K % and Min-K%++) reveal that most training corpora are likely contaminated with both sensitive content and evaluation benchmarks, leading to inflated test set performance. These methods sometimes fail to detect samples from the pretraining data, primarily because they depend on statistics composed of causal token likelihoods. We introduce Infilling Score, a new test-statistic based on non-causal token likelihoods. Infilling Score can be computed for autoregressive models without re-training using Bayes rule. A naive application of Bayes rule scales linearly with the vocabulary size. However, we propose a ratio test-statistic whose computation is invariant to vocabulary size. Empirically, our method achieves a significant accuracy gain over state-of-the-art methods including Min-K%, and Min-K%++ on the WikiMIA benchmark across seven models with different parameter sizes. Further, we achieve higher AUC compared to reference-free methods on the challenging MIMIR benchmark. Finally, we create a benchmark dataset consisting of recent data sources published after the release of Llama-3; this benchmark provides a statistical baseline to indicate potential corpora used for Llama-3 training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the Infilling Score, a method developed based on Min-k% and Min-k%++ to detect whether a given text sequence was part of a language model’s pretraining data, which is the traditional MIA setting. This method builds on existing approaches for membership inference attacks by using non-causal token likelihoods to improve detection accuracy. The authors propose a ratio test-statistic for efficient computation, and demonstrate its effectiveness on various benchmarks such as WikiMIA and MIMIR, where the proposed method performs slightly better than the compared baselines, especially on longer text sequences.

### Strengths
1. The motivation of combining the exisitng method and likelihood probability is straightforward and easy to understand.
2. This paper presents extensive experiments to demonstrate the effectiveness of the proposed method. And the case study with the newly-released model Llama 3 could be useful for real practices.

### Weaknesses
1. The contribution in this paper is quite marginal. The propose framework is more like an extension of the previous methods like Min-k% and Min-k%++, which utilizes token probabilities to make predictions. The token probabilities approach have been shown to be less effective for white-box settings in MIA studies. While I understand the grey-box access might raise more challenges, the modifications of previous methods in this paper can hardly contribute to new insights into this direction.

2. It seems that the complexity of the proposed framework is proportional to the number of tokens considered in the method. As shown in Sec. 4.5, the runtime of the proposed method is indeed much higher than the previous Min-k%++ methods. Would this become a concern when using such method in real practices?

3. Despite the increased complexity, the improvements over the baseline models in terms of performance in these benchmarkes are also not obvious. In many cases, Infiling Score can only achieve similar performances with Min-k% and Min-k%++.

### Questions
See the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In pre-training data detection, this paper proposed Infilling Score, a new test-statistic based on non-causal token likelihood. This paper also proposed a ratio test-statistic whose computation is invariant to vocabulary size. Experiments showed the method achieves an accuracy gain over state-of-the-art methods, including Min-K%, and Min-K%++ on the WikiMIA benchmark. Finally, the paper constructed a benchmark dataset that consists of recent data sources published after the release of Llama-3; this benchmark can provide a statistical baseline to indicate potential corpora used for Llama-3 training.

### Strengths
It is natural but good idea to introduce a new test-statistic that is based on non-causal token likelihood. Empirically, the method achieved an accuracy gain over state-of-the-art methods.

### Weaknesses
1. While the method empirically achieved an accuracy gain over state-of-the-art methods in Tables 1 and 3, I wonder the differences are really significant. If so, it is better to mention in what significance test the authors found they are significant.

2. While the computation can be invariant to the vocabulary size in the proposed method, it seems that there exists a tradeoff in terms of the sequence length. The performance is lower for shorter instances than longer ones. However, for longer instances, the computation is higher. In Sec. 4.5, since the authors did not show the size of the datasets with different lengths, it is difficult to judge whether the differences in the speed in Table 5 are negligible or not. It is better to clearly mention the number of instances for each dataset. 

It is more convincing when, if possible, the authors can try to estimate the runtime for actual settings where we try pre-training data detection for a specific dataset of a certain size, rather than for the standard benchmark dataset.

### Questions
1. I wonder \tau in Sec. 3.2 is also a hyperparameter to be fixed. The value and how the authors fixed it were not mentioned in the experiments  Please explain them.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a pretraining data detection approach that utilizes the non-causal token likelihoods which depend on both preceding and succeeding token probabilities.

### Strengths
1. The paper has enough novelty. 
2. It includes all the previously related works and lists the differences.
3. It has detailed experiments and results analysis.
4. The paper writing is clear, and the visuals are good.

### Weaknesses
The proposed approach has a slower speed compared to the previous best approach. However, I believe it has little effect on the impact because contamination detection may not need to be so fast.

### Questions
N/A

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies algorithms to detect whether a given sentence is the pretraining data used for training an LLM. The paper proposes “Infilling Score”, a test-statistic score based on non-causal token likelihoods. The proposed score works by computing the infilling probability of a token based on both its past and future tokens, whereas similar existing methods, such as MIN-K% and MIN-K%++, rely on a statistic based on past tokens only.

The motivation for Infilling Score is that incorporating future tokens should yield a more indicative measure. While the most intuitive method to incorporate future tokens is based on the Bayes rule, the paper argues that it would involve marginalising over all possible tokens in the vocabulary at each time step (i.e., each token in the test sequence). Therefore, this paper proposes an approximation (in Equation 6) to circumvent the expensive marginalisation, requiring 2 * the number of test tokens calls instead of the number of vocab size * the number of test tokens calls.

Experiments are conducted on standard datasets, including WikiMIA and MIMIR, and the proposed method is compared against other reference-free methods (e.g., Min-K% and Min-K%++) as well as other reference-based methods. Experimental results show that Infilling Score outperforms existing methods in the majority of tasks. In addition, the paper complies a more recent data from book excerpts and applies the detection algorithm on Llama3.

### Strengths
- The idea is simple, yet novel and effective. The method extends the existing reference-free pretraining data detection algorithm (Min-K++%) by incorporating the information from future tokens, and the proposed method yields improved performance.
- While it is not as efficient as Min-K%, the proposed algorithm is more efficient than the implementation of the naive Bayes rules. This is noted and examined in the paper.
- Comprehensive experiments on both standard datasets as well as a case study on new datasets (to avoid likely contamination).

Overall, this paper improves the understanding in the field of contamination/training data detection.

### Weaknesses
 - It is not clear in Section 4 (experiments) how Infilling Score (Equation 6) performs compared to the naive Bayes rule (Equation 5). The paper provides run-time in Section 4.5, but I cannot find the performance comparison. Specifically, while the paper argues that the naive Bayes approach is computationally expensive, it would be useful to see at least a comparison on a smaller subset of the data to understand the trade-off between the approximation and the exact computation. This would help to quantify the performance loss due to the approximation.
- [nitpick] similar to Min-K% & Min-K%++, this method is limited to grey-box scenarios.

### Questions
In the of data contamination detection, I wonder how this method works if the example to be tested (x) is partially contaminated. Would it be more or less sensitive to partial changes compared to other methods?

### Soundness
4

### Presentation
3

### Contribution
3
