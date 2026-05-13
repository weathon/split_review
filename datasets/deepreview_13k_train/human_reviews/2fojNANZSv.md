# Mixture of In-Context Prompters for Tabular PFNs

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Recent benchmarks found In-Context Learning (ICL) outperforms both deep learning and tree-based algorithms on small tabular datasets. However, on larger datasets, ICL for tabular learning cannot run without severely compromising performance, due to its quadratic space and time complexity w.r.t. dataset size. We propose \ours, which both extends nearest-neighbor sampling to the state-of-the-art ICL for tabular learning model and uses bootstrapping to finetune said model on the inference-time dataset. \ours is the Condorcet winner across 36 diverse tabular datasets against 19 strong deep learning and tree-based baselines, achieving the highest mean rank among Top-10 aforementioned algorithms with statistical significance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a mixture of experts approach for in-context learning on tabular data. Each expert in the mixture is a K-means cluster and the model routes the input instance to the closest cluster. This addresses the problem of context size in large datasets and provides a better selection of prompt instance than random sampling. To adapt the model to this type of routing authors also propose fine tuning by selecting a cluster of each training instance and maximizing the likelihood.

### Strengths
The paper is well written and proposes a justified solution to address the context length issue for in-context learning models such as TabPFN. Authors conduct extensive experiments on many real world dataset to demonstrate the effectiveness of the proposed approach and compare with leading tree-based and deep learning tabular methods.

### Weaknesses
There is a very related previous work "Retrieval & Fine-Tuning for In-Context Tabular Models" by Thomas et al, which proposes both nearest neighbor retrieval to improve the prompt and fine tuning with this approach to adapt the model to the target distribution. I think the authors have to compare with this work and highlight what is novel in MixturePFN.

I could not find an ablation study on the number of clusters K vs model performance, have you done these experiments?

### Questions
I could not find an ablation study on the number of clusters K vs model performance, have you done these experiments?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes the MixturePFN framework, which extends TabPFN for large tabular datasets by addressing the performance and scalability limitations of the number of table rows. The authors propose:
1. Mixture of In-Context Prompters (MICP), which optimizes inference by using a sparse mixture of experts to route test samples to specific "prompters" that create context-specific prompts to separate large training datasets into manageable clusters. 
2. Context-Aware Finetuning (CAPFN), which addresses distributional shift issues by specializing each prompter on its assigned
context via parameter efficient finetuning.

### Strengths
- The MICP strategy effectively reduces memory usage, allowing the model to handle larger datasets compared to existing TabPFN
- CAPFN bootstrapping and finetuning approach appears to be an effective way to mitigate distribution shift ICL for tabular data
- Extensive benchmarks against 19 strong baselines show good performance in both mean rank and Condorcet ranking across diverse datasets

### Weaknesses
 - While MIXTUREPFN improves dataset scalability, it still struggles with feature-rich datasets, potentially limiting its applicability in domains with high-dimensional data, such as patient healthcare data. I realize the authors leave this to future work, but this is an area where simple XGBoost performs quite well, and I would be curious about their thoughts on tackling this issue.

- MICP's reliance on K-Means clustering to segment data into meaningful clusters as the quality of clusters can vary significantly based on dataset properties / distance metric chosen. Poor clustering could lead to suboptimal routing and ineffective prompts for certain test samples. I'd be curious to see some ablations in this area.

- The CAPFN bootstrapping method might introduce biases or overfitting if the sampled subsets are not representative of the entire dataset. Bootstrapping from small clusters may fail to capture enough diversity, especially in cases with imbalanced classes or rare features. I'd be also curious to see how this method works with highly imbalanced labels e.g. 1% positive.

### Questions
See weaknesses.

Can categorical features simply be encoded as ordinal features? Is that not implying false relationships between unordered elements?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors propose MixturePFN, an extension of Sparse Mixture of Experts to TabPFN to alleviate the context size limitations of the existing TabPFN. On the TabZilla benchmark, MixturePFN outperforms state-of-the-art tabular prediction models.

### Strengths
1. The idea of Mixture of Experts blending into TabPFN seems novel.

2. The effectiveness of MixturePFN is well evaluated in well-established benchmarks against a variety of baseline methods.

3. Writing is easy to follow.

### Weaknesses
1. The biggest weakness I think is that the paper is missing a comparison with LoCalPFN [1]. Since LoCalPFN also tries to make TabPFN effective even on datasets with many-shots, I think it should be mentioned in the paper.



### Questions
1. Can you provide a comparison with LoCalPFN [1]? If not possible, I think the comparison should be done using k neighbor samples rather than random sampling, at least for TabPFN*.

2. I see that the authors say in the limitations section that they didn't do it on a dataset with a million samples, but I'm somewhat curious about the effectiveness of MixturePFN on a dataset with a million samples, since the paper is aimed at the scale-up aspect.

3. I'm also curious about the effectiveness of MixturePFN on datasets with hundreds or thousands of features, which is very practical in the real world.

----
[1] Thomas et al., Retrieval & Fine-Tuning for In-Context Tabular Models, NeurIPS 2024

### Soundness
3

### Presentation
3

### Contribution
3
