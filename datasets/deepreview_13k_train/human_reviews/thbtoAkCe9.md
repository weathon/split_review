# $\mathbb{D}^2$ Pruning: Message Passing for Balancing Diversity & Difficulty in Data Pruning

- Decision: Accept
- Scores: 5, 5, 6, 6, 6

## Abstract
In recent years, data quality has emerged as an important factor for training massive models. Analytical theories suggest that higher-quality data can lead to lower test errors in models trained on a fixed data budget. Moreover, a model can be trained on a lower compute budget without compromising performance if a dataset can be stripped of its redundancies. Coreset selection (or data pruning) seeks to select a subset of the training data so as to maximize the performance of models trained on this subset, also referred to as coreset. There are two dominant approaches: (1) geometry-based data selection for maximizing *data diversity* in the coreset, and (2) functions that assign *difficulty scores* to samples based on training dynamics. Optimizing for data diversity leads to a coreset that is biased towards easier samples, whereas, selection by difficulty ranking omits easy samples that are necessary for the training of deep learning models. This demonstrates that data diversity and importance scores are two complementary factors that need to be jointly considered during coreset selection. In this work, we represent a dataset as an undirected graph and propose a novel pruning algorithm, $\mathbb{D}^2$ Pruning, that uses message passing over this dataset graph for coreset selection. $\mathbb{D}^2$ Pruning updates the difficulty scores of each example by incorporating the difficulty of its neighboring examples in the dataset graph. Then, these updated difficulty scores direct a graph-based sampling method to select a coreset that encapsulates both diverse and difficult regions of the dataset space. We evaluate supervised and self-supervised versions of our method on various vision and NLP datasets. Results show that $\mathbb{D}^2$ Pruning improves coreset selection over previous state-of-the-art methods at low-to-medium pruning rates. Additionally, we find that using $\mathbb{D}^2$ Pruning for filtering large multimodal datasets leads to increased diversity in the dataset and improved generalization of pretrained models. Our work shows that $\mathbb{D}^2$ Pruning is a versatile framework for understanding and processing datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The $\mathbb{D}^2$ PRUNING method presented in this paper demonstrates a novel approach for selecting the most useful data from large training sets (coresets) for deep learning model training. 

It combines two key factors: data diversity and sample difficulty. The method represents the training dataset as a graph and uses a message-passing algorithm to update each data point's difficulty score by considering its neighbors. This process ensures a balance of diverse and challenging data in the selected coreset. 

$\mathbb{D}^2$ PRUNING has shown to be effective in improving model performance, particularly for image classification and natural language processing tasks, and is especially useful at low-to-medium data pruning rates.

### Strengths
1. The paper presents a novel approach - $\mathbb{D}^2$-PRUNING, which balances both data diversity and difficulty, along with its applicability to both supervised and self-supervised learning contexts. This positions it as a valuable tool in the ongoing evolution of corset selection techniques for data efficient learning.
2. The experiments are clear and the authors provide ablation experiments to support the theory and newly introduced hyper-parameters in the paper.
3. It is commendable that the paper divulges into the NLP domain and demonstrates improved performance over existing methods in coreset selection.

### Weaknesses
1. The paper demonstrates very incremental gains in performance over State-of-the-Art method (like Ash et al., 2019).
2. The experiments in section 5.1 do not compare $\mathbb{D}^2$-PRUNING State-of-the-Art methods discussed in (Guo et al., 2021) such as GLISTER (Killamsetty et al., 2021), CRAIG (Mirzasoleiman et al., 2020), GRAD-MATCH (Killamsetty et al., 2021) etc.

### Questions
1. The paper uses inconsistent numberings (A and then 2, 3) in section 1 which should be rectified.
2. An important investigation aspect for this paper would be to demonstrate performance on very small values of selection ratios $k$ as discussed in (Guo et al, 2021) and perform more than 1 message passing (K-shot setting).
3. The paper refers to additional information in the appendix section. It would greatly improve the readability of the paper if the authors point to exact section numbers in the appendix.
4. It is unclear if the parameter $\gamma$ mentioned in section 5.1 refers to $\gamma_f$ or $\gamma_r$. 
5. Although optional, including an algorithmic view of the proposed approach would be interesting to clarify how $\mathbb{D}^2$-PRUNING fits into the training and evaluation process of deep-learning models.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper starts by emphasizing the significance of maintaining a balance between the diversity and difficulty of samples used in data subset selection, for speeding up the training process. To this end, the authors initially illustrate instances in which diversity sampling can result in an excessive over-sampling (attributable to over-representation) from regions characterized by relatively low complexity. Following this, as shown in Figure~2, the authors introduce a graph-based algorithm designed to select training examples that maintain a balance between diversity and difficulty. The algorithm is based on message parsing on the constructed graph where each datapoint is a node. Subsequently, the paper provides experimental evidence in support of their proposed method, conducted across a range of datasets encompassing both vision and language domains, as well as their joint modality. The experimentation includes scenarios involving both supervised and self-supervised learning. The paper also addresses the interesting datacomp setting and evaluates its performance against the corresponding benchmarks, including VTAB and retrieval.

### Strengths
A wide range of data modalities is considered which I particularly appreciate, unlike other papers in the community. Ablation is also done on the hyperparameters mentioned in the proposed algorithm, which include $\gamma_r$, $\gamma_f$ (kernel width), and the sparsity of the graph. The paper was pretty much straightforward and they mentioned that $D^2$ provides boosts under a low to medium "pruning" regime. Overall, I like the simplicity of writing.

### Weaknesses
I feel that the prime weakness of this work is from the angle of related works, and baselines. Highlighting the importance of balancing diversity and difficulty is not new, and indeed if one is using not well-tuned diversity selection methods, then they won't be able to give a full representation of the dataset (minor modes which are not outliers but are difficult). That being said, I need an explanation, and if possible, results on the following baselines --

For general supervised cases 

- CRAIG [1]
- GLISTER (this paper has the same motivation as mentioned in Eq1) [2]
- GradMatch [3]
- Top-k method [4]: Another graph-based sampling that downweighs the contribution based on neighbors.
- CREST (an extension of CRAIG) [5]

A combination of submodularity with difficulty has been explored in the following -- 

- FASS (two-stage procedure for active learning, but a similar two-stage procedure can be considered here) [6]
- A combination of submodularity and difficulty has been considered in CAL-SDS2 [7]
- MCL (Combination of hardness and diversity for curriculum learning) [8]
- DIHCL (another combination of hardness and diversity for curriculum learning) [9]

More recent works on diversity-based selection (for NLP) --
- MILO [10]
- INGENIOUS [11]  

On SSL: 
- See SAS [12] 

On multimodality see T-MARS [13]

Concluding thoughts: 
I believe the paper should discuss these works and should include some of them as baseline.  

References
- [1] Data-efficient Training of Machine Learning Models (ICML'20) 
- [2] GLISTER: Generalization-based Data Subset Selection for Efficient and Robust Learning (AAAI'21) 
- [3] GRAD-MATCH: Gradient Matching based Data Subset Selection for Efficient Deep Model Training (ICML'21)
- [4] SELECTIVE ANNOTATION MAKES LANGUAGE MODELS BETTER FEW-SHOT LEARNERS (ICLR'23)
- [5] Towards Sustainable Learning: Coresets for Data-efficient Deep Learning (ICML'23)
- [6] Submodularity in Data Subset Selection and Active Learning (ICML'15)
- [7] Accelerating Batch Active Learning Using Continual Learning Techniques (TMLR/DMLR@ICML'23)
- [8] Minimax Curriculum Learning: Machine Teaching with Desirable Difficulties and Scheduled Diversity (ICLR'18)
- [9] Curriculum Learning by Dynamic Instance Hardness (NeurIPS'19) 
- [10] MILO: Model-Agnostic Subset Selection Framework for Efficient Model Training and Tuning 
- [11] INGENIOUS: Using Informative Data Subsets for Efficient Pre-Training of Language Models
- [12] Data-Efficient Contrastive Self-supervised Learning: Most Beneficial Examples for Supervised Learning Contribute the Least (ICML'23)
-  [13] T-MARS: Improving Visual Representations by Circumventing Text Feature Learning

### Questions
- For the difficulty-based methods, in supervised settings, methods such as forgetting-event are clear that they use the learning dynamics. However, methods such as -- entropy, EL2N (which is similar to the norm of the gradient concerning bias term), and area under margin score, can be computed during any step of training. Therefore, does the paper consider the moving average of the dynamics (of some pre-trained models, for which they've assumed the access), or is it taken at the end of the training? In case it is moving average, I am okay with it, but if it is taken at the end of the training, then the training set methods like entropy/margin/EL2N can be very wrong in judging the hardness. 


- Can authors provide standard deviation or statistical analysis in cases where the second-best technique is very close? 
- For BADGE does the author use true labels instead of pseudo labels? BADGE was proposed in Active learning and hence it is important to make sure it doesn't have a disadvantage in supervised setting comparisons. 
- k and s_k are overloaded as expressions in the paragraph above equation 6. 
- What happens when one runs message parsing for more than one round? Can authors provide an experiment on that or justification? 
- Eq. 1 theta should rather me $\theta^*(S')$ to show that it is a solution to the optimization.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a new data pruning model called D^2 pruning that balances diversity and difficulty via a message-passing algorithm.
They show the performance superiority of the proposed method on vision and NLP datasets with supervised and self-supervised variants.

### Strengths
- Clear presentation and easy-to-follow writing.
- The algorithm is straightforward and easy-to-implement.
- The evaluation is extensive, with many datasets in multiple tasks, and solid.

### Weaknesses
 - No time complexity analysis. The proposed algorithm based on message-passing seems to take quite a lot of time. The author should provide the time-complexity analysis with the exact GPU time taken because a data pruning method that takes too long time is less practical.
- No theoretical analysis. How this message-passing algorithm can guarantee better generalization than other baselines? Although the author provides some intuition (data pruning should consider both diversity and difficulty), why it should be achieved by the message-passing and how it can reduce the generalization error in Eq.(1) is missing.

### Questions
I think this work is also related but missed in discussion/comparison.

[a] Active learning is a strong baseline for data subset selection. NeurIPS workshop, 2022

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to balance both difficulty and diversity in the data sampling process. The authors argue that difficulty and diversity have been independently optimized but should be optimized together. To this end, this work proposes a graph-based method, D^2 pruning, which builds the graph based on data diversity and uses message passing to get information difficulty.

### Strengths
The authors perform extensive experiments, on both vision and NLP datasets, and compare to a well-covered set of baseline. Empirical results appear to be promising.  The methodology itself also appears to be interesting and novel, to the best of my knowledge.

### Weaknesses
The authors use distance in embedding space to construct the near-neighbor graph. However, there is a lack of support for why distance in embedding space is a good indicator of diversity. For example, what if we use another model to generate the embedding? What’s the influence between feature level embedding versus final layer embedding? Similarly, the authors use the forgetting score as the difficulty indicator. There is no discussion on why the author choose forgetting score? What would be the influence of choosing another score, such as a consistency score or loss of an approximate model?

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel coreset selection algorithm called D2 pruning (Diversity-Difficulty pruning), which leverages undirected graphs and message passing to calculate difficulty score. The algorithm's primary goal is to tackle two important aspects: example difficulty and diversity within the selected subset of data points. D2 pruning works in the following way: 1. Graph Initialization: Nodes in graph G represent dataset examples and are connected to their k-closest neighbors in the embedding space. 2. Update difficulty score: Use message passing on the graph to update difficulty scores based on neighbor distance and difficulty.  3. Coreset Selection: Iteratively select balanced samples from high-density low-difficulty and low-density high-difficulty regions. Down-weight neighbors of selected samples to promote coreset diversity.

### Strengths
1. The authors proposed a novel coreset selection algorithm that aims to unify the benefits of data diversity and data difficulty. The proposed method is intuitive.

2. The proposed method is also evaluated on NLP datasets - lacked in prior work. 

3. The evaluation compares $D^2$ with various baselines and shows that $D^2$ achieves better or comparable performance than SOTA methods.

4. The writing is good and easy to follow.

### Weaknesses
1. The performance improvement seems marginal. In most cases, the improvement is less than $1\%$. Specifically, while the method shows promise, the absolute gains in accuracy or other relevant metrics are often quite small, raising questions about the practical significance of the proposed approach. The reported improvements need to be more substantial to justify the added complexity of the algorithm.

2. With such performance differences, repeated evaluation can be suggested to mitigate the variance in the model training. Given the small performance gains, it's crucial to ensure that the observed improvements are not due to random fluctuations in the training process. Multiple runs with different random seeds, and reporting the mean and standard deviation of the performance metrics, would provide a more robust assessment of the method's effectiveness.

3. $D^2$ introduces some additional hyper-parameter, which may increase the coreset selection cost. The introduction of new hyperparameters, such as those related to the graph construction and message passing, adds complexity to the coreset selection process. This can make the method more difficult to use in practice, as it requires additional tuning and may increase the computational cost of the selection process.

### Questions
1. How many iterations will the forward message passing phase have?

2. What is the importance score in fig 2 (what metrics used)? 

3. It seems that $D^2$ can be combined with other metrics. Do you run an ablation study to see how $D^2$ performs with other importance scores?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
