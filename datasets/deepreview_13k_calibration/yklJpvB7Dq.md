# Label-Free Coreset Selection with Proxy Training Dynamics

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
High-quality human-annotated data is crucial for modern deep learning pipelines, yet the human annotation process is both costly and time-consuming. Given a constrained human labeling budget, selecting an informative and representative data subset for labeling can significantly reduce human annotation effort. Well-performing state-of-the-art (SOTA) coreset selection methods require ground truth labels over the whole dataset, failing to reduce the human labeling burden. Meanwhile, SOTA label-free coreset selection methods deliver inferior performance due to poor geometry-based difficulty scores. In this paper, we introduce ELFS (Effective Label-Free Coreset Selection), a novel label-free coreset selection method. ELFS significantly improves label-free coreset selection by addressing two challenges: 1) ELFS utilizes deep clustering to estimate training dynamics-based data difficulty scores without ground truth labels; 2) Pseudo-labels introduce a distribution shift in the data difficulty scores, and we propose a simple but effective double-end pruning method to mitigate bias on calculated scores. We evaluate ELFS on four vision benchmarks and show that, given the same vision encoder, ELFS consistently outperforms SOTA label-free baselines. For instance, when using SwAV as the encoder, ELFS outperforms D2 by up to 10.2% in accuracy on ImageNet-1K.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents ELFS (Effective Label-Free Coreset Selection), a method designed to improve label-free coreset selection by estimating data difficulty scores without requiring ground truth labels. The authors tackle challenges in label-free selection by employing pseudo-labels from deep clustering to approximate training dynamics and mitigate distribution shifts with a double-end pruning technique. ELFS shows superior performance over existing label-free methods across various vision benchmarks (e.g., CIFAR10, CIFAR100, and ImageNet-1K) and achieves results close to those of supervised selection methods.

### Strengths
1. ELFS effectively addresses the limitations of previous label-free coreset selection approaches, providing a feasible solution that leverages deep clustering for pseudo-labeling.

2. By employing double-end pruning, ELFS improves the selection of informative samples, achieving consistent performance improvements over baselines, even in challenging scenarios.

3. The evaluation across multiple datasets and pruning rates, along with an ablation study, showcases ELFS's flexibility and robustness, which may benefit a range of vision tasks.

4. The authors show that including more challenging samples enhances model performance, with ELFS effectively prioritizing hard examples through double-end pruning.

### Weaknesses
1. The experiments involve numerous hyperparameters, optimized through grid search. A more in-depth analysis of the underlying reasons behind these optimal values would strengthen the understanding of how different parameters affect the measurement of sample difficulty, offering clearer insights into the importance of hard examples. Specifically, the hard pruning rate, which controls the percentage of hard examples to be removed, is determined via grid search. The paper lacks a discussion on how this rate interacts with the pseudo-label quality and the overall coreset selection process. It remains unclear how the optimal pruning rate is related to the distribution of easy and hard examples and if there is a more principled way to set this parameter rather than relying on exhaustive search.

2. The approach heavily relies on feature extractors like SwAV and DINO for clustering. It remains unclear if using more advanced encoders, such as CLIP, could further improve performance or stability, suggesting potential limits in ELFS's generalizability with different encoders. The paper does not explore the sensitivity of ELFS to the quality of the feature embeddings produced by these encoders. The performance of the method may be significantly impacted by the choice of encoder, and a more thorough investigation into this aspect is needed.

### Questions
1. Given the grid search used to determine optimal hyperparameters, could a deeper analysis reveal why certain values work best for measuring sample difficulty? Specifically, how do these parameters influence the balance between easy and hard examples selected for the coreset, and could this inform a more consistent method for tuning them?

2. ELFS currently uses SwAV and DINO as feature extractors for clustering. Would more powerful encoders, such as CLIP, improve the quality of pseudo-labels or provide more stable performance across datasets? Additionally, what effect might these alternative encoders have on the distribution of selected hard and easy examples?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new label-free coreset selection algorithm called ELFS to relieve the costly human annotation efforts. ELFS utilizes the deep clustering to generate pseudo-labels and estimate data difficulty scores. Afterwards, a double-end pruning method is introduced to mitigate the bias of data difficulty scores. Experiments show that ELFS can surpass previous label-free coreset selection baselines on several benchmarks.

### Strengths
1. It is an elegant and effective idea to estimate the data difficulty score through deep clustering. This handles the challenge to measure the prediction uncertainty and sample difficulty without any human labels.

2. The proposed method is evaluated on multiple classification benchmark, showing notable performance gain compared with state-of-the-arts.The design of each module is well justified through ablation studies.

### Weaknesses
1. My major concern lies in the selection of hyper-parameter $\beta$. I can understand they require some grid search for hyper-parameters. However, according to Fig. 5, the optimal value is different for multiple datasets or sampling ratios, which is quite inefficient. For example, if there is a large dataset with millions of images, it is infeasible to do grid search on it. The computational cost associated with this grid search, especially for large datasets, is a significant practical limitation that needs to be addressed more thoroughly. The authors should provide a more detailed analysis of the computational complexity of the grid search and explore alternative strategies for hyperparameter optimization.

2. Based on Tab. 7, it is quite strange that ResNet50 cannot outperform ResNet18 on the selected subset. I assume it reasons from the simplicity of CIFAR10. Maybe the authors can do the transferability experiments on complex datasets like ImageNet since it is a main difference between corset selection and active learning. The lack of performance gain with a more complex architecture like ResNet50 raises questions about the robustness of the selected coreset. This suggests that the coreset might be biased towards the specific architecture used for selection, and the authors should investigate the transferability of the selected coreset to different architectures and datasets.

3. For Sec. 4.1, I assume the formulation of label-free coreset selection is already covered in previous work. It may be moved to Sec. 3 for clarity.

### Questions
Please consider responding to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a novel method called ELFS (Effective Label-Free Coreset Selection) for selecting coresets without relying on labeled data. This approach uses pseudo-labels derived from deep clustering to approximate training dynamics, enabling the estimation of data difficulty scores. These scores help identify coresets that can be labeled for training high-performance models while minimizing human annotation costs. ELFS addresses the significant performance gap typically found in label-free coreset selection by introducing a double-end pruning technique to manage the distribution shift caused by pseudo-label inaccuracies. This method shows notable improvements in various vision benchmarks over existing label-free methods, demonstrating its ability to approximate the effectiveness of supervised coreset selection.

### Strengths
ELFS presents a compelling label-free coreset selection method that reduces the need for extensive and costly labeled datasets while achieving accuracy close to supervised methods. By effectively utilizing pseudo-labels, ELFS not only significantly outperforms other label-free baselines but also exhibits strong performance despite the inherent inaccuracies and noise associated with pseudo-labels. Moreover, the method demonstrates robustness and versatility, showing good transferability across different datasets and model architectures, thereby enhancing its applicability in diverse machine learning tasks.

### Weaknesses
The ELFS method is quite effective, but it mainly builds on familiar techniques like pseudo-labeling and coreset selection. This might make it seem less novel or groundbreaking to those familiar with the field. Despite this, it does a great job using these methods to ensure high accuracy and reliability.

Moreover, to really show how well ELFS works and to expand its use, it would be beneficial to test it on a wider variety of datasets. This includes tackling larger and more complex datasets such as ImageNet, as well as datasets with uneven distributions or long tails. Testing ELFS in these contexts would help validate its effectiveness across different challenges and environments.

Potential Application Areas for ELFS: Beyond vision tasks, are there other types of data or tasks where ELFS could be effectively applied? Exploring its adaptability to different domains like text, audio, or even structured data could open up new applications.

Explanation of Hard and Easy Examples in Section 4.4.2: Could a visual representation or graph be used to clarify the difference between hard and easy examples as discussed in the section? Visual aids could help illustrate how ELFS handles these types of data, enhancing understanding of its approach.

Analysis of Data Distribution in Table 1: Is it possible to analyze further how the data distribution of the coreset selected by Random compares to that selected by ELFS? Understanding the differences in selection criteria and resulting coreset characteristics could provide deeper insights into the strengths and limitations of ELFS compared to simpler random sampling methods.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new policy to sample a core subset for deep models. It introduces a deep clustering with the pseudo-labelling to estimate the score for each sample. Meanwhile, they try to fix the bias issue of pseudo-labelling. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The motivation of this paper is solid, and the topic of this paper exactly matches ICLR.
2. The writing of introduction clearly delivered the motivation and idea.
3. The experiment result looks good. It's interesting that many methods even cannot beat random sampling as suggested in Tab.1.
4. The ablation study is extensive.

### Weaknesses
1. Some sentences are redundant, such as these two questions proposed in the paper.
2. It would be better to move sec 4.1 to sec 3 to give readers an overview of the problem you are solving.
3. My **main concern** is that more benchmarks in different distributions should be evaluated. As described in the paper, this method relies on a pretrained vision encoder to get the visual features for each sample. Then, a deep clustering algorithm is introduced to get the pseudo labels and scores. However, the evaluated datasets in this paper are too easy for pretrained vision encoders. I believe that much of the data in the evaluation datasets is included during pretraining. If we use a dataset in a different distribution, such as a medical image dataset, without a good visual feature, will this method still work?

### Questions
1. Please explain why double-end pruning helps the performance.
2. Do you fine-tune the model with the coreset? Or do you train the model from scratch?
3. Do you use only the coreset to train the model? It would be better to show the result of using the coreset as the labelled set and the rest data as the unlabelled set to train a model with a semi-supervised learning algorithm such as SemiReward[1]. If, with the help of semi-supervised learning, a randomly sampled labelled set achieves good performance, and the labelled set selected by your model yields similar performance, then the benefits of using a coreset to train the model need to be clarified.
```
[1] SemiReward: A General Reward Model for Semi-supervised Learning, Siyuan Li and Weiyang Jin and Zedong Wang and Fang Wu and Zicheng Liu and Cheng Tan and Stan Z. Li, ICLR 2024
```

### Soundness
3

### Presentation
3

### Contribution
3
