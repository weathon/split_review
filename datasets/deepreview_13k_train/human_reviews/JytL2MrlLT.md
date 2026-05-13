# Revisiting Nearest Neighbor for Tabular Data: A Deep Tabular Baseline Two Decades Later

- Decision: Accept
- Scores: 6, 8, 3, 5, 8

## Abstract
The widespread enthusiasm for deep learning has recently expanded into the domain of tabular data. Recognizing that the advancement in deep tabular methods is often inspired by classical methods, e.g., integration of nearest neighbors into neural networks, we investigate whether these classical methods can be revitalized with modern techniques.
We revisit a differentiable version of $K$-nearest neighbors (KNN) --- Neighbourhood Components Analysis (NCA) --- originally designed to learn a linear projection to capture semantic similarities between instances, and seek to gradually add modern deep learning techniques on top. Surprisingly, our implementation of NCA using SGD and without dimensionality reduction already achieves decent performance on tabular data, in contrast to the results of using existing toolboxes like scikit-learn. Further equipping NCA with deep representations and additional training stochasticity significantly enhances its capability, being on par with the leading tree-based method CatBoost and outperforming existing deep tabular models in both classification and regression tasks on 300 datasets. We conclude our paper by analyzing the factors behind these improvements, including loss functions, prediction strategies, and deep architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This study considers learning on tabular data, and proposes ModernNCA -- a deep version of the classic Neighborhood Components Analysis algorithm. Contrary to NCA, the transformation in ModernNCA is non-linear, and is powered by a neural network. To make the training of ModernNCA more efficient and more effective, the paper also proposes Stochastic Neighborhood Sampling (SNS). In experiments on 300 datasets, ModernNCA is reported to achieve the best average rank among the considered baselines, including gradient-boosted decision trees (GBDT).

### Strengths
- The method is simple.
- Generally, I tend to agree that nearest neighbors may be underexplored in the context of tabular data. While TabR seems to close this gap to some extent, ModernNCA looks like a good addition to the field.
- The SNS strategy looks simple and effective, and also differentiates the method from TabR.
- On the considered benchmark, the proposed ModernNCA achieves a better average rank and a better balance of task performance and training time compared to baselines.
- A large number of baselines and datasets.
- An ablation study is provided.

### Weaknesses
Note: regarding the "datasets" and "metrics" weaknesses, I admit that the field lacks standardized benchmarks and metrics.

**Datasets**

My understanding is that the benchmark consists of many automatically collected datasets. In the light of the recent studies about tabular datasets, it is unclear how representative the benchmark is. Examples of the studies:

- Towards quantifying the effect of datasets for benchmarking: A look at tabular machine learning
- A Data-Centric Perspective on Evaluating Machine Learning Models for Tabular Data
- TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks

Specifically, the benchmark appears to include numerous 'multi-version' datasets, such as the `BNG-*`, `Contaminant-detection-*`, and `FOREX-*` families, which are closely related or derived from the same underlying data. This inflates the effective number of datasets and introduces bias towards these specific data sources. Furthermore, the benchmark includes datasets with known label leakage issues, as identified in recent work like "TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks", and also includes datasets that are trivially solvable, achieving perfect accuracy. These issues raise concerns about the overall quality and reliability of the conclusions drawn from this benchmark. The formal number of datasets and covered domains should not be the only perspective on the benchmark; more investment in dataset filtering is needed.

**Metrics**

The metrics such as ranks or wins do not show the scale of performance gaps between methods. It is unclear how significant are the wins and losses of ModernNCA (not from statistical perspective, but from the practical perspective).

**Presentation**

- In my opinion, the presentation could be more efficient. The proposed NCA extensions are not conceptually novel, so I believe that the story on the first six pages could be more compact. Perhaps, some of the details and discussion can be moved to appendix.
- Based on my understanding of the TabR baseline
    - The explanation of TabR on L152 is not correct, since it is not a Transformer variant. Quoting the TabR paper: *"a feed-forward network with a custom k-Nearest-Neighbors-like component in the middle"*.
    - The description of TabR on L216-L226 is: (1) not complete, (2) not correct, and, if I am not mistaken, (3) not used in the story. In the light of (3), I do not go into details about (1) and (2). Perhaps, this description can be simply removed?
- Generally, communicating the empirical nature of a study as in L108-L113 is fine. However, personally, I would change the first sentence on L108 to something more neutral.
- Perhaps, Figure 1 can be placed closer to the related experiments, but this can be subjective.

**Related work.**

There is a missing related work: "Improving Generalization via Scalable Neighborhood Component Analysis" ECCV 2018. That paper also describes how to efficiently train a deep NCA, and I think their method is more advanced than the one proposed in this submission. Though their method can be too complicated for the scope of this paper. In that case, I recommend discussing this related work and explaining why the proposed SNS is a better choice for this work compared to the method from the referenced paper.

### Questions
-

### Soundness
3

### Presentation
2

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
The paper proposes a revised take of the NCA algorithm for supervised learning on tabular data, where the neighborhood aggregation is done in a representaion space of a neural network, the model is optimized via SGD and additional stochasticity is introduced in subsetting the neighbors list. 

The resulting architecture is conceptually simpler than prior state-of-the-art tabular retrieval models, while improving in performance and eficiency as shown via an extensive experimental evaluation.

### Strengths
- The proposed method is well motivated. Attention to simple KNN-based methods in deep tabular models was limited, except TabR which is well addressed in the text.
- The method is both conceptually simple and easy to implement, without sacrificing performance
- The experimental results and ablations are extensive and insightful:
  - The step-by-step Linear-NCA ablation (table 2) is a principled and convincing way to explore a model design space
  - Stochastic Neighborhood Sampling ablation shows an interesting result (improved performance from sampling) and provides a practically important outcome for retrieval-based tabular NNs
  - Other important minor details (like the numerical feature embedding ablations), slight improvements in the distance function used, loss functions
- The writing and overall storytelling is engaging and well thought-out

### Weaknesses
 - All experimental results and ablations rely on the average ranks of a set of methods being tested. This provides some signal for which modificaitons are usefull, but other means of comparison might make this even clearer. For example, additinal relative improvement compared to a strong baseline (e.g. a well-tuned MLP) would provide usefull additional signal besides the average rank metric (e.g. what is the scale of such improvements). 
- Minor additional to the previous point: I find that providing raw unaggregated results for the core (or even for all) the experiments is very usefull for quick sanity-checks and comparisons in future work. So that others could assess results on the individual datasets by consulting the paper text.
- I believe limitation should be discussed somewhere in the main text. E.g. what are the confines of the proposed mehtod. Are there any cases where it may perform poor. 
   - Maybe some post-hock meta-analysis akin to the one in tabzilla paper (https://arxiv.org/abs/2305.02997) of what are the datasets where ModernNCA performs worse. 
   - Some recent benchmarks demonstrate that retrieval-based models might not be universaly superior (https://arxiv.org/abs/2406.19380)

### Questions
- Could you provide or point to the raw per-dataset metrics?
- Is it possible to add some other means of comparison along with average ranks (e.g. relative improvement to a baseline)? What does it show? 
- What are the methods limitations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper revisits the Neighborhood Components Analysis (NCA) and adapts it for tabular data learning, proposing ModernNCA as an enhanced approach. The modifications include (1) calculating distances in a representation space, (2) using stochastic gradient descent (SGD) instead of L-BFGS for optimization, and (3) training in a mini-batch fashion rather than on the entire dataset at once. The authors benchmarked ModernNCA against numerous methods across 300 datasets, finding that it achieved consistently superior performance, often comparable to leading models like CatBoost and outperforming many deep tabular learning methods.

### Strengths
- The approach effectively leverages modern deep learning techniques to enhance classical NCA, demonstrating strong empirical results across a large number of datasets.

- The paper provides comprehensive benchmarks, including comparisons with state-of-the-art methods in both classification and regression tasks.

### Weaknesses
 **Lack of Novelty**: While the paper shows strong empirical performance, the core modifications (using a representation space for distance calculations, employing SGD, and mini-batch training) have already been explored in prior research. This raises concerns regarding the originality of the contribution. The changes appear more like tunings of established techniques rather than introducing a fundamentally new method.

[Prior research example] J Kang et al., Deep metric learning based on scalable neighborhood components for remote sensing scene characterization, 2020.

### Questions
If my understanding is incorrect, could you please clarify what is the novel concept introduced in this paper?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the potential of modernizing the classical Nearest Neighbor approach for tabular data by leveraging a differentiable K-nearest neighbors variant, Neighborhood Components Analysis (NCA). The authors introduce MODERNNCA, an improved version of NCA that integrates deep learning techniques such as stochastic gradient descent (SGD), nonlinear embeddings, and a Stochastic Neighborhood Sampling (SNS) strategy to boost computational efficiency and model performance. They demonstrate that MODERNNCA matches or outperforms both tree-based models and current deep tabular models across 300 datasets in classification and regression tasks.

### Strengths
**Originality**
Revisiting a classic nearest-neighbor approach with contemporary deep learning techniques is a novel approach, particularly since NCA had been previously limited by computational efficiency and scalability. This approach aims to unify insights from both traditional and modern tabular prediction methods.

**Quality**
The authors conducted extensive experiments across 300 datasets, providing thorough evidence of the model’s strengths and weaknesses. 

**Clarity**
The explanation of the modifications, including SGD, nonlinear embeddings, and SNS, is detailed and clear, making the improvements accessible to the reader.

### Weaknesses
 **Marginal Contribution**  
   The paper’s contribution feels incremental rather than pioneering. The improvements in MODERNNCA rely on established techniques (SGD, SNS, and nonlinear embeddings) without introducing a fundamentally new concept or method. This makes the novelty limited, as it essentially optimizes an existing algorithm rather than providing a unique advancement. 

**Limited Novelty in Comparison to KNN Variants**  
   The paper lacks direct comparisons with other KNN-inspired deep learning methods that have similarly benefited from modern optimization strategies. This limited scope of comparison weakens the argument for MODERNNCA’s distinctiveness and impact.

**Lack of Theoretical Analysis**  
   The paper’s focus is primarily empirical, with little theoretical exploration of why the proposed enhancements lead to improved performance. A deeper theoretical perspective on the modifications—such as the effect of stochastic sampling on generalization—would provide valuable insights and strengthen the work's academic contribution.

### Questions
- MODERNNCA relies on Euclidean distance as the default metric. How adaptable is the model to other distance metrics, such as cosine similarity, and do the authors have insights on how these choices might impact performance?

- The paper discusses various deep learning modifications, but how sensitive is MODERNNCA to hyperparameter choices such as learning rate, number of neighbors (K), and embedding dimensions? Are there specific configurations where performance significantly degrades?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper re-evaluates the nearest neighbor approach for tabular data, proposing a modernized version of neighborhood component analysis (nca) called modernnca. starting from classical nn techniques, the authors incorporate current deep learning methods into nca, such as using stochastic gradient descent and adding stochastic neighborhood sampling. the experiments on 300 tabular datasets demonstrate that modernnca performs comparably to leading models like catboost, outperforming other deep learning approaches for classification and regression tasks. the authors also provide insights into how modern techniques like batch normalization and non-linear architectures improve nn performance.

### Strengths
1. the authors structure their explanation to make complex methods like nn and nca accessible and coherent. this clarity is helpful for understanding both the motivation and methodology behind the modifications to nca.

2. the paper includes an extensive evaluation on a broad range of datasets, demonstrating modernnca’s effectiveness with detailed performance metrics and statistical significance tests.


3.  The authors do a great job explaining the steps taken to modernize nca

### Weaknesses
W1: while the model shows high performance, the paper lacks specific scenarios or guidance on applying modernnca practically, such as when dealing with imbalanced datasets

### Questions
1. How does modernnca perform with different distance metrics, such as cosine similarity, especially for datasets with high-dimensional features?


2. Given that modernnca outperformed many models, have you tested its performance on imbalanced datasets?

3. Could you provide more insights into cases where modernnca significantly underperforms compared to catboost or other tree-based methods?

### Soundness
3

### Presentation
3

### Contribution
3
