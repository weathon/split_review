# Synergistic Approach for Simultaneous Optimization of Monolingual, Cross-lingual, and Multilingual Information Retrieval

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Information retrieval across different languages is an increasingly important challenge in natural language processing. Recent approaches based on multilingual pre-trained language models have achieved remarkable success, yet they often optimize for either monolingual, cross-lingual, or multilingual retrieval performance at the expense of others. This paper proposes a novel hybrid batch training strategy to simultaneously improve zero-shot retrieval performance across monolingual, cross-lingual, and multilingual settings while mitigating language bias. The approach fine-tunes multilingual language models using a mix of monolingual and cross-lingual question-answer pair batches sampled based on dataset size. Experiments on XQuAD-R, MLQA-R, and MIRACL benchmark datasets show that the proposed method consistently achieves comparable or superior results in zero-shot retrieval across various languages and retrieval tasks compared to monolingual-only or cross-lingual-only training. Hybrid batch training also substantially reduces language bias in multilingual retrieval compared to monolingual training. These results demonstrate the effectiveness of the proposed approach for learning language-agnostic representations that enable strong zero-shot retrieval performance across diverse languages.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a hybrid batch training approach for multilingual information retrieval by combining monolingual and cross-lingual training data. The core methodology relies on mixing different types of training data using probability weights α and β. While the implementation is straightforward, the novelty of the contribution is limited.

### Strengths
1. Addresses a relevant challenge in multilingual information retrieval.
2. Provides comprehensive experimental validation across multiple benchmark datasets (XQuAD-R, MLQA-R, MIRACL).

### Weaknesses
1. The primary contribution merely combines two existing training approaches with probability weights, presenting a straightforward and obvious solution.
2. The paper employs translated QA pairs as data augmentation, creating an unfair comparison with baseline methods that do not utilize this advantage.

### Questions
None.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies information retrieval tasks where monolingual, cross-lingual, and multilingual setups are examined. The paper studies different batch sampling approaches at the training time without modifying existing training loss (e.g., contrastive learning loss) or model architectures. Specifically, the paper argues that existing approaches either use (i) monolingual batching where the languages of query and documents are matched, but they can be of different languages, or (ii) cross-lingual batching where the languages of query and documents are different. Based on this, the paper proposes hybrid batching, which is the mixing of these two batching methods.

Experiments are conducted on two base models (XLM-R and LaBSE) and evaluated on two tasks (XQuAD-R, MLQA-R, MIRACL). To train systems with data in various languages, the paper employs in-house machine translation to translate existing training corpora (described in Section 3.1). The experimental results show that hybrid batching, generally, outperforms monolingual-only and cross-lingual-only in a range of setups, including monolingual, cross-lingual, and multilingual.

### Strengths
The paper shows that two standard batching strategies are complementary for information retrieval tasks, as the combination of them shows improvements.

### Weaknesses
1. Limited evaluations are only QA datasets (e.g., the main text only shows XLM-R and LaBSE). Also, the main text consists of many large tables where each does not present as much information as the space it takes, e.g., the authors could summarize how many languages/scenarios the proposed method shows improvements instead of providing large tables like Table 3, Table 4, Table 5, etc.

2. It is not clear if the proposed method is actually effective. In many cases, the improvements appear rather small. For example, in Table 1, on XQuAD-R for XLM-R (0.792 vs 0.798; 0.705 vs 0.700; 0.593 vs 0.593). Are they even statistically significant?

3. As this paper mainly provides empirical observations, it would be stronger if the paper provides insights on which scenario (e.g., what kind of base model or dataset) where hybrid batching is expected to show significant improvements and when it does not. The current paper pretty much reports experimental findings which could limit its usefulness. Several questions remain, for example, what is the size and mixed of training data does one need to see the impact of this hybrid batching? I expect that if there is limited training data, the impact would be marginal.

### Questions
1. Related to weakness1, could this proposed method be extended to other tasks in addition to QA?
2. Can you discuss my weakness 2.
3. Can you discuss my weakness 3.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a simple method called hybrid batch training, which involves translating to obtain parallel data in multiple languages, and sampling these data to construct a multilingual training dataset. The model is trained by inputting monolingual or multilingual training data with a certain probability, thereby balancing its performance in both scenarios.

### Strengths
1.  This paper proposes a hybrid batch training strategy to simultaneously improve zero-shot retrieval performance across monolingual, cross-lingual, and multilingual settings while mitigating language bias.
2.  The hybrid batch training strategy simply modifies the training data batches without necessitating the introduction of loss functions or new architectural components.

### Weaknesses
1. The proposed hybrid batch training strategy only modifies the input training data, which lacks novelty.
2. This paper lacks sufficient analysis to the field of multilingual information retrieval. It does not adequately demonstrate the shortcomings of existing work nor the importance and necessity of this study.
3. The experiments only compare the performance of different input strategies but not various multilingual information retrieval methods.

### Questions
1. What are the advantages of hybrid batch training strategy in terms of convenience, overall efficiency, and experimental effectiveness compared to existing multilingual information retrieval methods?

### Soundness
3

### Presentation
2

### Contribution
1
