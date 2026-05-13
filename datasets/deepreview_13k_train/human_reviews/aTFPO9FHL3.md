# Todyformer: Towards Holistic Dynamic Graph Transformers with Structure-Aware Tokenization

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
Temporal Graph Neural Networks have garnered substantial attention for their capacity to model evolving structural and temporal patterns while exhibiting impressive performance. 
However, it is known that these architectures are encumbered by issues that constrain their performance, such as over-squashing and over-smoothing. 
Meanwhile, Transformers have demonstrated exceptional computational capacity to effectively address challenges related to long-range dependencies.
Consequently, we introduce Todyformer—a novel Transformer-based neural network tailored for dynamic graphs. It unifies the local encoding capacity of Message-Passing Neural Networks (MPNNs) with the global encoding of Transformers through i) a novel patchifying paradigm for dynamic graphs to improve over-squashing, ii) a structure-aware parametric tokenization strategy leveraging MPNNs, iii) a Transformer with temporal positional-encoding to capture long-range dependencies, and iv) an encoding architecture that alternates between local and global contextualization, mitigating over-smoothing in MPNNs. 
Experimental evaluations on public benchmark datasets demonstrate that Todyformer consistently outperforms the state-of-the-art methods for downstream tasks.
Furthermore, we illustrate the underlying aspects of the proposed model in effectively capturing extensive temporal dependencies in dynamic graphs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes TODYFORMER, a novel Transformer-based neural network tailored for dynamic graphs. It unifies the local encoding capacity of Message-Passing Neural Network with the global encoding of Transformers.
Experimental evaluations on public benchmark datasets demonstrate that Todyformer consistently outperforms the state-of-the-art methods for the downstream tasks.

### Strengths
1. The paper is clearly written and easy to follow.
2. The results of different downstream task prove the validity and superiority of model, especially the results on large scale datasets.

### Weaknesses
1.	This paper does not provide the mathematical form of the overall loss function, which leads to an incomplete explanation of the model in Section 3.
2.	In the detail of three main components, many ideas are not novel. For instance, in encoding Module, the Transformers is very basic model. The window-based encoding paradigm is from DyG2Vec. The positional-encoding idea is also from previous work.

### Questions
1.	Could you add mathematical form of the overall loss function?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a novel graph transformer method for dynamic graph. This model is an encoder-decoder architecture, started from patch generation and based on alternating between local and global message-passing as graph transformer. Authors perform two downstream tasks including future link prediction and dynamic node classification.

### Strengths
(1). This paper presents a graph transformer method on the dynamic graph, with enough experiments and ablation to show its performance.
(2). The purpose of using graph transformer is clearly discussed in Section Introduction and Related Work.

### Weaknesses
(1). Some presentations need improvement. Some notations need to be clear and some formulas need to be written for clarity. For example, what is the notation a,b means in E = |{e_a,...,e_b}| in section 3.2? What is the specific formula for positional encoding o() in section 3.4? For the transformer formula (6), could you specify whether there are LayerNorm and Feed-Forward modules as transformer? Could you give the formula of Q, K, V, and their dimension for clarity?

(2) I wonder about the results of Wikipedia and Reddit you mentioned in Section 4.1 datasets as it’s not shown in Table 1. As for the results shown in the Appendix, it seems they are not strong enough in the Inductive setting, especially for the Reddit dataset, which makes the statement in section 4.2“Todyformer consistently outperforms the baselines’ results on all datasets.” misleading.

(3) The patch generation method lacks sufficient justification. The paper does not adequately explain why this specific method was chosen over alternatives like METIS used in Graph ViT/MLP-Mixer or graph coarsening in COARFORMER. The advantages of the proposed method are not clearly articulated, especially in the context of dynamic graphs.

(4) The discussion on over-smoothing in dynamic graphs is not convincing. The paper states that the issue is magnified in dynamic graphs but does not provide concrete examples or references to support this claim. This weakens the motivation for the proposed method.

(5) There is a lack of efficiency comparison against other methods, particularly CAW and Dyg2Vec. The computational cost of applying a graph transformer on each node could be high, and this is not analyzed. The paper should provide a detailed analysis of time complexity and empirical runtime comparisons.

(6) The paper does not adequately analyze the weaker experimental results. Specifically, the paper needs to discuss why the method underperforms on the two smaller datasets in the second set of experiments. This lack of analysis makes the experimental evaluation less convincing.

### Questions
(1). In Section 3.2 PATCH GENERATION, could you please give more analysis of why you use this patch generation method, rather than other existing methods such as METIS in Graph ViT/MLP-Mixer or Graph coarsening in COARFORMER? What’s the advantage of your patch generation method?

(2). Section 3.5 “This issue is magnified in dynamic graphs when temporal long-range dependencies intersect with the structural patterns.” Could you please give some analysis of it or give some examples or literature to show the importance of over-smoothing problems in dynamic graphs? This can make this paragraph more convincing.

(3). Could you please show your efficiency comparison against other methods, especially CAW and Dyg2Vec? In my opinion, the computation of graph transformer on each node could have high time complexity, could you please analyze it?

(4) Could you give more analysis for the experiments weaker than the baseline? For example, in the second set of experiments, why did this method fail in these two smaller datasets?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a Transformer-based architecture for dynamic graphs, namely Todyformer. Experiments demonstrate that Todyformer outperforms the state-of-the-art methods on some datasets.

### Strengths
1. This paper is easy to follow.

### Weaknesses
1. The authors claim that Transformers demonstrate exceptional computational capacity, compared with Graph Neural Networks. However, the computational complexity of GNNs and traditional Transformers is $O(N)$ [1]  and $O(N^2)$ [2] respectively, where $N$ is the number of nodes in the input graph. I suggest reporting the complexity and runtime in experiments.
2. Todyformer is similar to Vision Transformer, while the authors do not provide the necessary analysis in terms of graph learning. Some suggestions are as follows.
	1. The authors may want to analyze the expressiveness of Todyformer in terms of sub-structure identification and the Weisfeiler-Leman (WL) test.
	2. The authors may want to analyze how and why Todyformer alleviates over-squashing and over-smoothing.
3. Please explain why the baseline results in Table 2 are different from those from Table 3 in [3].
4. The authors claim that the significantly low performance of Todyformer on the Wiki and Review datasets is due to the insufficient hyperparameter search. However, in my opinion, hyperparameter tuning is difficult to improve 3% accuracy.
5. Please report the standard deviation in Table 2 following the baselines. Moreover, I suggest reporting a statistically significant difference.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Todyformer, a novel Transformer-based neural network for dynamic graphs, to address the problems of over-smoothing/squashing caused by Dynamic Message-Passing Neural Networks and learning long-range dependencies. The experiments of future link prediction and node classification are conducted to verify its effectiveness.

### Strengths
1.	A novel Transformer-based neural network is proposed for dynamic graph representation learning. 
2.	The proposed TodyFormer achieved the best performance over 9 baselines on both transductive and inductive link prediction experiments.

### Weaknesses
1.  To the best of my knowledge, there is no study pointing out existing well-known temporal graph neural networks (TGNN) have the problem of over-smoothing. I also do not see any theoretical or experimental evidence on the over-smoothing problem of TGNN. Therefore, the motivation of this paper may be not solid. 
2.  There are some existing works studying leveraging Transformer for dynamic graph learning, e.g., APAN [1], DygFormer [2]. What are the advantages of the proposed Todyformer over these methods?
3.  The inputs of TodyFormer are edges within a temporal window. How to set the size of this window? Does it mean that the edges in the previous time will see the edges in the latter time in the window (information leakage)? How do you prevent the information leakage problem? 
4.  There are a lot of symbols used in the equations without detailed explanation, which makes it really hard to understand. For example, what is P, c in Eq. (4) ? what is positional encoding P in Eq. (5) ? what is n, e in Eq. (7) ? 
5.  From ablation study (Table 4), there is really slight difference after removing modules of TodyFormer? Even if all the modules are removed, TodyFormer still has very high performance (e.g., 0.987 on social evolution). I do not understand which modules contributes the such high performance? In addition, more ablation study on other modules should be studied, e.g. (replace node2vec encoding with others). 
6.  More sensitivity analysis on other hyper-parameters should be conducted.
7.  There is no training/testing time comparison with other baselines. 
8.  There are many spelling and grammar and Latex errors in this paper. Please check the whole paper carefully.

### Questions
1.	In section 3.2, how do you partition the input graph into M non-overlapping subgraphs?
2.	In Eq. (3), what is s^l? Why H^l is the combination M node embeddings? There seems a contradiction as the author stated M are the number of subgraphs stated in previous section. 
3.	In Figure 3, the results of left and right subgraphs seem contradict. On the left, the window size of LastFM is 144, and the AP score is larger than 0.975. On the right, when windows size of LastFM is less than 50k, it seems the AP score is less than 0.95. Why is that? Besides, as my comment 3, such large window size may cause severe information leakage.
4.	It is really wired that on 4 of 5 datasets, TodyFormer has the AP score over 0.99 (Table 1).

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
