# Rethinking Pre-Training in Tabular Data:  A Neighborhood Embedding Perspective

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
Pre-training is prevalent in deep learning for vision and text data, acquiring knowledge from other datasets to improve the downstream tasks. However, when it comes to tabular data, the inherent heterogeneity in the attribute and label spaces among datasets makes it hard to learn shareable knowledge and encode it in a model. We propose **Tab**ular data **P**re-**T**raining via **M**eta-representation (TabPTM), aiming to pre-train a general tabular model over a set of heterogeneous datasets. The key is to embed data instances from any dataset into a common feature space, in which an instance is represented by its distance to a fixed number of nearest neighbors and their labels. Such a meta-representation standardizes heterogeneous tasks into homogeneous local prediction problems, enabling training a model to infer the label (or the score to each possible label) of an input instance based on its neighborhood information. As such, the pre-trained TabPTM can be directly applied to new datasets without further fine-tuning, regardless of their diverse attributes and labels. Extensive experiments on 72 tabular datasets validate TabPTM's effectiveness (with and without fine-tuning) in both tabular classification and regression tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes to perform supervised learning on tabular data with a shared model that takes a proposed "meta-representation" as input instead of original sample features. 

Samples are represented as distances to prototypes (K the closest samples of particular classes in terms of weighted p-norm distance). 

The proposed approach called TabPTM is compared to classical ML models (GBDTs, KNN, SVM) and some contemporary tabular DL models on a set of 36 datasets showing improved performance in the particular setup.

### Strengths
- The paper is well written, it clearly describes the method (visualizations also help)
- The goal of learning a shared model for a set of heterogeneous tabular problems is hard and intriguing. This may open up performance and usability gains to tabular models if done right

### Weaknesses
The experimental setup is the core weakness of the paper. I expand on main points for improvement below:

- The process behind dataset selection for evals should be more detailed. This is one of the major problems in new method papers in tabular ML: method papers introduce new arbitrary benchmarks with no clear dataset selection criteria making it very hard to assess and compare method performance (many questions regarding dataset quality, baseline performance arise and should be answered when introducing a benchmark) 
- The above issue may be minimized by using an established benchmark that is proven in some way (e.g. the benchmark from Grinsztajn et. al. [https://arxiv.org/abs/2207.08815]) -- this also helps ensure comparisons against strong baselines (as established benchmarks often already have results for properly tuned baselines and SoTA algorithms -- see e.g TabR or ModernNCA [https://arxiv.org/abs/2307.14338]).
- Many very relevant baselines are missing (methods that are also heavily relying on the nearest neighbors of the sample)
  - Modern tabular DL versions of the K-NN algorithm that are the current SoTA in the field (ModernNCA [https://arxiv.org/abs/2407.03257], TabR [https://arxiv.org/abs/2307.14338])
  - K-NN based improvements for TabPFN. Very similar ideas stemming from https://arxiv.org/abs/2305.11097 Localized PFN e.g.: https://arxiv.org/abs/2405.16156  https://arxiv.org/abs/2311.10609 https://arxiv.org/abs/2402.11137
  - Properly tuned standard algorithms like XGBoost and MLP. Experimental setup description in the appendix mentions 30 trial hyperparameter budget -- in my experience, methods such as XGBoost and baseline neural networks are considerably undertuned with this budget. You should consider tuning baselines more thoroughly for a fairer comparison. (adopting an established benchmark may help mitigate the costs)
- Ablations should be done on more than two datasets. Tabular datasets are highly diverse, the effect is best measured on a multitude of datasets, improvement on two dataset (that are seemingly arbitrarily chosen) may be not representative (I've seen many ideas and methods shine on a few datasets but fail to generalize and be useful on average)
- Overall, the necessity and usefulness of a shared model is very debatable. The results in table 9 show that fine-tuning is necessary (e.g. no zero-shot generalization is happening), strong nearest-neighbors based baselines are missing, classical baselines are seemingly undertuned and the dataset selection is not justified

### Questions
- How does TabPTM compare to existing strong nearest-neighbors based baselines on an established tabular benchmark?
- What is the most compelling evidence **for** the shared model pretraining?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
The authors propose a pre-training strategy for tabular data. Due to the inherent heterogeneity of tabular data, it is difficult to learn shareable knowledge across different datasets. To address this issue, the authors propose Tabular Data Pre-training via Meta-representation (TabPTM) to embed data instances from any dataset into a common feature space. The pre-trained TabPTM can be directly applied to new datasets without further fine-tuning, no matter how diverse their attributes and labels are. Extensive experiments on 72 tabular datasets validate the effectiveness of TabPTM.

### Strengths
1) The author proposes a pre-training method for the tabular data, which can reduce attribute heterogeneity, and enable the pre-training of a general model over tabular datasets.
2) The proposed method achieves effectiveness among different datasets and tasks.
3) The paper presents the details of the proposed method.

### Weaknesses
1) Lack of novelty. I admit that we should try to find shareable vocabulary, which is important for the pre-training. However, using the distances among instances serve as the shareable vocabulary, which is not novelty enough. The author should detail analyze the advantages of using distances regardless of other semantic information.
2) In sec 4.3, to verify the high quality of the meta-representation, the author should also visualize the representation of other methods. For example, the author can visualize the distribution of $x$ for comparison. 
3) Since the author emphasizes the ability of "without further fine-tuning", this experiment's analysis should be reported in the main body.
4) The parameters that need to be optimized is the MLP, which is three layers only. What is the meaning of exploring the pre-training on such a small network? Moreover, the reported performance gain on the classification benchmark is incremental compared with XGBoost.

### Questions
1) How the hyper-parameter $K$ influence the performance?

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
2

### Summary
In the present work, the authors put forward a general pre-training model for tabular data akin to foundation models for vision or language modalities. Their approach, inspired from approaches found in the literature of dimensionality reduction or manifold learning, produces representations that can be used for different datasets with various number of features, type of features, task (regression or classification) and number of classes (if classification).

The proposed approach produces meta-representations for each sample based on the relation of the sample to its closest neighbours for each class (in case of classification) and its overall closest neighbour for regression. The obtained representation is then used to train a final transformation that will serve for both classification and regression purposes. The transformation is agnostic to the number of classes, type of task (regression or classification) and can be applied in a straighforward manner.

### Strengths
- The paper is well written, easy to follow and well organized. This facilitates the understanding of both the thinking process and experimental setting of the authors. 
- The authors have identified significant lakings and weaknesses in existing methods found in the literature, and propose a method based on their diagnosis to circumvent those identified issues.
- The extensives experiments are convincing. Their approach obtains interesting results on both classification and regression tasks and proves to be quite versatile.
- Their finding that the inter-sample relation between instances within a dataset is relevant for supervised tasks in tabular data is in line with recent work in the literature of deep learning for tabular data [1] or [2].

### Weaknesses
 - The proposed method requires an initial pairwise distance computation within datasets which might restrain the proposed approach to reasonnably large datasets.
- For multilabel classification with $C$ classes, the proposed representation requires $C$ separate predictions which also increase the overall complexity during training (and inference).
- Categorical features are encoded using one-hot encoding which may restrain the applicability of the meta-representation approach to datasets with categorical features with reasonnable cardinality. (Have the authors considered trying other categorical encoding?)

### Questions
- **(i)** While the datasets used in the experiments are very diverse per Table 4. in the appendix, it might be interesting to investigate the impact of imbalance between class on the obtained representations. **(i-1)** Do dataset present in the benchmark present imbalancing between classes? If so, **(i-2)** are there notable difference in performance on the downstream tasks between balanced and imbalanced datasets in comparison to competing methods ?

- **(ii)** I may need clarififaction on section 4.2., paragraph **Vanilla meta-representation**, in particular on the way the the label $\hat{y_j}$ is defined on line 261-262. If I understand corretly, for each sample $x_i$, one can obtain its $\phi_c(x_i)$ representation using the subset of a dataset $ \mathcal{D}_{y=c}= \\{(x_i,y_i)\mid y_i=c\\}$ and selecting among this subset the $K$ sample closest to $x_i$. Given that each sample in this subset of the dataset has as a label $y_j=c$, then given how $\hat{y_j}$  is derived, each $\hat{y_j}$ would have value 1. I am not sure when the $y_j = -1$ will intervene. Could the authors clarify?

- **(iii)** As mentionned by the authors at the end of section 4.2., there are occurences where $K$, the number of closest samples within a class is too high in comparison with the available number of samples within this class. To adress this problem, authors rely on padding the largest value. Have the authors investigated the impact of such padding on the performance of their representation?

- **(iv)** Computing the meta-representation before applying the transformation $\mathbf{T}_\Theta$ requires to compute the pairwise distance between each sample in the training set, which has a complexity of $\mathcal{O}(n^2)$. While less constrained than TabPFN [3], this still requires significant training time. Could the authors report meta-representation training time and compare to existing method?
- **(v)** While explicitely targeted for tabular datasets, the proposed approach could also be applied to different data modalities (e.g. audio, image, etc).  Have the authors considered experimenting on author data modalities, to see whether their approach is relevant only for tabular data?
- **(vi)** Figure 3 displays two dimensional data representations of breast-cancer-wisc and dermatology datasets. How did the authors reduce the original dimension of the samples to a two-dimensional representation ?

Overall the proposed method is novel, well motivated and is shown, through significant experiments, to have strong performance on tabular datasets. The paper is well structured and written. Also, the extensive appendix demonstrates the rigor of the authors in conducting the experiments. All those arguments point towards **accepting the paper**. Nevertheless, some points need clarifications/further investigation (see questions listed above). I would be happy to increase my score would the authors address my questions.

[1] Jannik Kossen, Neil Band, Clare Lyle, Aidan N Gomez, Thomas Rainforth, and Yarin Gal. Self-attention between datapoints: Going beyond individual input-output pairs in deep learning.Advances in Neural Information Processing Systems, 2021.

[2] Yury Gorishniy, Ivan Rubachev, Nikolay Kartashev, Daniil Shlenskii, Akim Kotelnikov, Artem Babenko. TabR: Tabular Deep Learning Meets Nearest Neighbors. In The Twelfth International Conference on Learning Representations, 2024.

[3] Noah Hollmann, Samuel Müller, Katharina Eggensperger, and Frank Hutter. Tabpfn: A transformer that solves small tabular classification problems in a second. In The Eleventh International Conference on Learning Representations, 2023.

### Soundness
3

### Presentation
3

### Contribution
3
