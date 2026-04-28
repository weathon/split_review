# Online Gradient Boosting Decision Tree: In-Place Updates for Adding/Deleting Data

- Decision: Reject
- Avg Score: 6.33
- Scores: 8, 8, 3

## Abstract
Gradient Boosting Decision Tree (GBDT) is one of the most popular machine learning models in various applications. But in the traditional settings, all data should be simultaneously accessed in the training procedure: it does not allow to add or delete any data instances after training. In this paper, we propose a novel online learning framework for GBDT supporting both incremental and decremental learning. To the best of our knowledge, this is the first work that considers an in-place unified incremental and decremental learning on GBDT. To reduce the learning cost, we present a collection of optimizations for our framework, so that it can add or delete a small fraction of data on the fly. We theoretically show the relationship between the hyper-parameters of the proposed optimizations, which enables trading off accuracy and cost on incremental and decremental learning. The backdoor attack results show that our framework can successfully inject and remove backdoor in a well-trained model using incremental and decremental learning, and the empirical results on public datasets confirm the effectiveness and efficiency of our proposed online learning framework and optimizations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to deal with the online learning task via optimized gradient boosting decision tree, which is an interesting research topic. And a novel online learning framework for GBDT supporting both incremental and decremental learning has been proposed. The whole paper is well organized with detailed formulation and theoretical analysis. Sufficient experiments have been given for model evaluation.

### Strengths
1. The research topic of optimizing the GBDT model is interesting, and the proposed method shows its novelty and performance.
2. The theoretical analysis of the proposed method in this paper is well expressed and proofed.

### Weaknesses
1. A detailed runtime complexity analysis of the proposed method is needed.
2. It is necessary to add an analysis on the impact of the number of base learners of the proposed model on the learning performance.

### Questions
1. There are also Online Boosting methods have been proposed, like OnlineBoost [1], OnlineAdaC2Classifier [1], and OnlineRUSBoost [1] have been proposed before, what is the difference between the proposed method and previous methods?

[1] B. Wang and J. Pineau, “Online Bagging and Boosting for Imbalanced Data Streams,” in IEEE Transactions on Knowledge and Data Engineering, vol. 28, no. 12, pp. 3353-3366.

2. The experiment results of the proposed method seem not the best on some datasets, please give a detailed explanation.
3. Although the parameter setting has been given, the parameter sensitivity analysis is still required.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes an online learning framework for Gradient Boosting Decision Tree (GBDT) that supports both incremental and decremental learning. Instead of adding and removing trees, this paper considers an in-place update of decision trees to add or delete a small fraction of data. In detail, the proposed framework detects the changes in the best split of tree nodes and retrains the subtrees accordingly. The authors introduce a split candidate sampling and robust LogitBoost to avoid frequent retraining. Extensive experiments show that the proposed framework outperforms the existing methods regarding efficiency and effectiveness. Other experiments are also conducted, including verification of backdoor attacks, performance on extremely high-dimensional datasets, and ablation studies.

### Strengths
- The proposed framework, specifically the in-place update of decision trees, is novel and interesting. It represents a significant departure from traditional GBDT online learning, which often focuses on adding or removing entire trees. This can be computationally expensive and may lead to model instability. By contrast, this paper's in-place update mechanism offers a more granular and efficient approach by directly modifying existing tree structures. This granularity potentially allows for finer adaptation to data changes, leading to better performance with fewer resources.
- This paper demonstrates a high level of completeness in the experimental evaluation, not only including the running time, running memory, and test error but also the batch addition and deletion of data, data addition with more classes, verification using backdoor attacks, and so on. Experiments from various aspects show the effectiveness and efficiency of the proposed framework.
- The paper is well-written and easy to follow.

### Weaknesses
 - While the proposed framework is undeniably novel and effective, its reliance on multiple heuristics and associated hyperparameters introduces complexity. Techniques like split candidate sampling and robust LogitBoost, while aimed at efficiency, require careful tuning, and should be studied case-by-case. The paper does not provide sufficient guidance on how these parameters should be tuned for different datasets or problem settings, making the practical application of the method challenging.
- No real-world datasets with varying data distributions are used in the experiments. The proposed framework's performance on such datasets would be interesting to see, as it would provide a more realistic evaluation of the framework's robustness and adaptability. The current experiments are limited to controlled settings, which may not fully reflect the complexities of real-world data where distributions can shift dramatically over time.
- The font sizes in Tables 1 and 2 are too small, making them difficult to read. 

**Minor Issues:**

- Lines 59 and 199: "Eq. equation" -> "Eq." or "Equation"
- Line 77: Bagging samples instances with replacement, not generating disjoint subsets.
- Line 87: "major challenges of in-place online learning": these challenges are not specific to in-place online learning.
- Line 199: "with ascending depths" -> "layer by layer from the root to the leaves"
- Lines 271 and 272: "leading to a reduction in the frequency of retraining" -> "decreasing the frequency of retraining"
- Lines 273 and 274: "reduce the online learning time" -> "accelerate the online learning process"

### Questions
- Is the training in the experiment in Section 4.1 an offline training?
- How does the proposed framework perform under rapidly changing data distributions, where frequent retraining may be required to maintain performance, while lack of retraining could lead to poor performance?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose an online learning framework that supports both incremental and decremental learning for Gradient Boosting Decision Trees (GBDT).

### Strengths
The authors have conducted an extensive set of experiments.

### Weaknesses
1. The motivation for the research is unclear. It seems to be solely because no one has studied it (line 75). If the motivation is closely related to the importance of GBDT, arguments such as *It outperforms deep learning models on many datasets in accuracy and provides interpretability for the trained models* lack supporting evidence.

2. The framework appears to be a minor improvement on existing research. Compared to traditional GBDT training methods, the difference in the new framework lies in utilizing the additivity of Formula 5 for node updates on Incremental & Decremental datasets (Section 2.3). The authors further discuss how to optimize time, which includes three parts. Section 3.1 also uses Incremental & Decremental datasets to update nodes rather than the entire dataset (this seems repetitive with the information conveyed in Section 2.3. If I'm wrong, please correct me.); Section 3.2 changes the frequency of executing Gradient Accumulation techniques, that is, update the derivatives only when retraining occurs instead of the traditional method that accumulates these gradients over multiple batches. Sections 3.3 and 3.4 reduce the time and resource consumption of online learning by changing from enumerating all potential splits to sampling a portion of the splits via introducing a sampling parameter $\alpha$. I acknowledge that these changes bring improvements to efficiency, but the inspiration provided by these minor innovations is limited.

3. The experimental section of the main text lacks discussion on important parameters and sampling. For example, there is a lack of discussion on the selection of the important parameter $\sigma$ and $\alpha$. The best split
changes in section 3.4 likely heavily depend on the distribution of the training data, as Figure 2 shows inconsistent changes in the best split points across different datasets. Therefore, whether $\sigma$ and $\alpha$  are data-dependent and how to determine them should be discussed in detail. And the main text lacks necessary conclusions of ablation studies. At the very least, the impact of the sampling method on accuracy should be pointed out. These have all been overlooked in main texts, and are replaced by a brief introduction in line 505.

4. Writing issues:

 - Citation issue in line 29.
 - Typo in Algorithm 3, line 4.
 - Incorrect citation format, such as line 29, 34, 39.
 - In line 533, it should be 'a novel'.
 - Experimental setup in section 3.4 needs more details, such as the repeated times and why 1% was chosen as the upper limit.

Overall, my main concern is that this work has very limited novelty and insight in terms of methodology (see my question 2). It appears to be an accumulation of minor modifications.I appreciate the authors' extensive experiments, but the structure of the experimental section needs significant revision. For example, while the experimental section covers various topics such as backdoor attacks (section 4.6), membership inference attack (section 4.7) and high-dimensional data (line 498), these experiments lack a progressive internal connection and convey repetitive information as section 4.3, 4.4 (i.e., the framework is effective in various scenarios). A suggestion is further insights about the stability and rationality of proposed method should be provided in the main text rather than in the appendix (see my question 3). Considering that the clarity of writing also needs improvement, I am inclined to recommend rejection.

### Questions
See my Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2
