# DynFrs: An Efficient Framework for Machine Unlearning in Random Forest

- Decision: Accept
- Scores: 8, 5, 8, 5

## Abstract
Random Forests are widely recognized for establishing efficacy in classification and regression tasks, standing out in various domains such as medical diagnosis, finance, and personalized recommendations. These domains, however, are inherently sensitive to privacy concerns, as personal and confidential data are involved. With increasing demand for \textit{the right to be forgotten}, particularly under regulations such as GDPR and CCPA, the ability to perform machine unlearning has become crucial for Random Forests. However, insufficient attention was paid to this topic, and existing approaches face difficulties in being applied to real-world scenarios. Addressing this gap, we propose the $\dynfrs$ framework designed to enable efficient machine unlearning in Random Forests while preserving predictive accuracy. $\dynfrs$ leverages subsampling method $\occ(q)$ and a lazy tag strategy $\lzy$, and is still adaptable to any Random Forest variant. In essence, $\occ(q)$ ensures that each sample in the training set occurs only in a proportion of trees so that the impact of deleting samples is limited, and $\lzy$ delays the reconstruction of a tree node until necessary, thereby avoiding unnecessary modifications on tree structures. In experiments, applying $\dynfrs$ on Extremely Randomized Trees yields substantial improvements, achieving orders of magnitude faster unlearning performance and better predictive accuracy than existing machine unlearning methods for Random Forests.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel unlearning approach for random forests. The authors employ a variant of bootstrapping, named OCC(q), to control the number of trees that each sample is used to train. This bootstrapping technique significantly decreases the number of trees that require unlearning, addressing a gap in existing random forest unlearning methods. Additionally, the authors propose lazy tagging, LZY, to defer re-training of subtrees until needed, enabling batched deletion and speeding up addition and deletion requests. The authors theoretically prove the exactness of their algorithm and analyze its time complexity. They conclude with comprehensive experiments demonstrating their method's superior performance compared to existing approaches.

### Strengths
* The method is simple yet effective, yielding an exact unlearning method for random forests.
* The approach reduces required re-training from the source by limiting the number of trees each data point influences.
* The method defers subtree re-computation until queries require that portion, making it suitable for online settings.
* Theoretical proofs demonstrate the algorithm's exactness and time complexity.
* Comprehensive experiments show superior performance compared to baselines, which suffer from numerical value binning.
* The algorithm demonstrates significantly faster performance than baselines.

### Weaknesses
 * Standard bootstrapping should be included as a baseline for performance comparison. The method involves two key changes: fixing the number of trees each sample is used in and using extremely randomized trees. Including separate comparisons would provide insights towards the impact of each modification.
* Space complexity analysis is missing from the paper. While the authors mention what additional information is stored for each node in Section 4.3, an explicit discussion would be valuable. Specifically, the analysis should include the space overhead of storing the lazy tags and how this scales with the number of data points and trees.
* The evaluation lacks testing on regression datasets. This is a significant gap, as random forests are commonly used for both classification and regression tasks. The absence of regression results limits the generalizability of the findings.
* Line 204: \in -> \subset

### Questions
* Can the authors address the points raised in the weakness section above?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on the unlearning of random forests and proposes the DYNFRS framework. DYNFRS is based on extremely randomized trees and includes subsampling and lazy tagging to improve the efficiency of unlearning procedures. This paper also proves the efficiency advantages of DYNFRS in both theoretical and experimental results.

### Strengths
1. The motivation and the contributions of this paper are clearly shown.
2. This paper provides both theoretical and experimental results to show the huge efficiency improvements compared with the retrained model.

### Weaknesses
1. This paper targets the unlearning in random forests. However, the proposed method relies on extremely randomized trees instead of the general decision trees, which limits the applicability.

2.  The technical part, as well as the pseudo-code in the appendix, are hard to follow. An overall pipeline or workflow can be better used to understand the proposed method.

3. The experiment, especially the performance comparisons, lacks many essential results, and it cannot prove the effectiveness of the proposed methods. Please refer to questions 3, 4, and 5.

### Questions
1.  What are the performance comparisons on the sequential unlearning, batch unlearning, and mixed online stream unlearning settings? The current draft only provides efficiency comparisons.

2. How the proposed method handles the changes of optimal split is not clear. This is the key point about the soundness of the proposed method.
 
3. In the experiment, what are the detailed settings for the unlearning request in each dataset? 

4. In the baselines, this paper chooses four methods corresponding to different tree construction approaches. Thus, does it mean such baselines also contain different initialized well-trained models? In addition, does the random forest stand for the retrained model?
 
5. In the experiment results in Table 2, why does higher prediction performance stand for better unlearning performance? In addition, in the unlearning of a tree-based method, which has more transparent structures, is it a better way to prove the success of unlearning by showing that the unlearned trees have the same structures as the retrained trees?

I am not familiar with the extremely randomized trees, so I might change my assessment based on other reviewers' comments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces  DYNFRS, a framework that enables efficient machine unlearning in Random Forest models. The objective is to propose a framework that supports the unlearning of a noticeable amount of data, i.e., above 0.1% of the original training set, without harming the performance of the model. Moreover, the framework should support real-world requests, such as adding data to the training set and querying the model. This is achieved through the three components of the framework: (i) the One-Class Constraint subsampling (OCC) that restricts each data sample to appear only in a subset of trees within the forest, reducing the influence of each sample on the model and thereby simplifying the unlearning process; (ii) the Lazy Tag Strategy (LZY) that marks only the nodes affected by data deletion or addition, allowing the algorithm to defer modifications until a relevant query necessitates them; (iii) the adoption of Extremely Randomized Trees (ERTs) as base learners in the forest that enable resilience to train data variations due to their inherent randomness in split selection. The time complexity of the data deletion, data addition, and querying of the model is formally proven, as well as the exactness of the unlearning procedure.

On nine binary classification datasets, DYNFRS is evaluated against other state-of-the-art machine unlearning approaches (DaRE, HedgeCut, and OnlineBoosting). The experimental results show that forests trained with DYNFRS present predictive performance that is at least equal to the ones of the other frameworks. Moreover, DYNFRS outperforms the other methods in sequential and batch unlearning tasks, demonstrating speedups up to 10^6x over traditional retraining and low growth of the unlearning runtime with a high number of requests with respect to the competitors. DYNFRS also supports requests in dynamic environments where data deletion, addition, and querying requests interleave, achieving a very low latency for modifications and making it practical for real-world applications.

### Strengths
This is a good paper that presents a significant contribution to the unlearning field. 

The novelty of this work stands in the proposed framework. Even though DYNFRS includes some techniques already presented in DaRE, in particular the random splits and the storage of the updated statistics of the nodes involved in the unlearning phase, the combination of these two techniques with constrained subsampling (OCC) and the tagging strategy (LZY) is novel and it has never been explored in the literature. Moreover, the framework supports not only data unlearning but also data addition and can handle a mix of requests in sequence, capabilities that are not supported by the considered state-of-the-art baselines.

The significance of the framework is highlighted by its performance with respect to the baselines. In sequential unlearning and batch unlearning, DYNFRS presents a speedup of up to 10^5 times with respect to the baselines. Fast learning and unlearning make the framework directly usable in real-world applications. However, more details about the experimental methodology need to be assessed to understand if the comparison with the baselines is completely fair (see the Weaknesses Section).

Finally, the presentation of the algorithms is clear, but the presentation throughout the paper can be improved in general (see the Weaknesses Section). It is appreciable that the authors have formally proven the complexity of the data unlearning, data addition and model querying procedures.

### Weaknesses
Even though the proposal of the paper is good, the paper presents some weaknesses and unclear points that the authors should address.

**Noteworthy weaknesses**

The first point regards the presentation of the experimental methodology, which is not deepened and not clear. In Section 5.1.1., it is written that `For all baseline models, we adhere to the instructions provided in the original papers and use the same parameter settings.`. Thus, it is not guaranteed that the baselines are using the same hyperparameter values of the forests trained by DYNFRS, like the number of trees and maximum depth, since, for example, DaRE expects to tune these parameter values. While this is acceptable to compare the accuracy of the best performing models trained by different frameworks, the models should all have the same hyperparameter values when comparing the training and unlearning time cost since the complexity of training and unlearning depends on the number of trees and maximum depth of the models. I invite the authors to clarify this point and provide experimental results related to a fairer comparison. Moreover, it is unclear how often the experiments are repeated to obtain the error bars and standard deviations shown in tables and figures and what is different among each repetition.

Second, it would be appreciated if the authors could provide the space complexity of a DYNFRS forest, as done in the DaRE paper for the DaRE forests. Indeed, it is not clear if the gain in time efficiency obtained by DYNFRS comes at the cost of a higher memory consumption. The suggested analysis would allow the authors to clarify this point. Moreover, an experimental comparison of the memory consumption of DYNFRS during the training phase with the baselines and an example of the memory consumption of a DYNFRS forest during a mix of requests of different types may highlight the practicality of the proposed framework.

Finally, the framework is tested only on binary classification tasks. It is not clear from the paper if the framework supports also multiclass classification tasks. The authors should provide clarifications about this point and, if the framework supports multiclass classification tasks, replicate the presented experiments including some multiclass datasets. If the framework does not support multiclass classification tasks, it is not a big limitation, but the authors should clearly state the reason of this limitation.

**Minor points**

The paper contains a lot of typos, especially in the notation of the Section 3. I invite the authors to fix them. Examples of typos are:
- page 3, line 132, $S, <x, y>)$: $<x, y>$ is missing curly brackets.
- page 3, line 134: $A(S \cup <x, y>)$: $<x, y>$ is missing curly brackets.
- In Section 3.2, $(a^*_u, w^*_u)$ and $p$ are not properly introduced.
- page 5, line 4: $D^n$ has never been defined.
- Page 5, line 142: Is the indicator function missing?
- In Section 4.2., the sentence `Unlike OCC(q)’s reducing work across trees and believing in ensemble, LZY relies on tree structures,
dismantling requests into smaller parts and digesting them through time.` does not make any sense and should be rephrased.

**Update after authors' response**
The authors have clarified the weaknesses listed above and the questions below in a satisfactory way, so I have increased my score. I leave the weaknesses written above to keep a trace of the discussion.

**Arguments for the score**

The proposal is novel and significant. Even though the proposed framework combines existing ideas, this combination gives rise to a new solution that is more efficient and effective than state-of-the-art solutions. Moreover, the framework supports operations not supported by other unlearning frameworks in the literature and presents a notable speedup over recent baselines. The experimental results are convincing about the improved efficiency and accuracy of the trained forests with respect to state-of-the-art forests. Thus, I recommend the acceptance of the paper.

### Questions
- Do the models trained by each framework in the experimental evaluation have the same hyperparameter values, e.g., number of trees and maximum depth?
- How much memory does DYNFRS consume during training compared to the baselines? How much memory does DYNFRS consume during a stream of mixed requests?
- The tables and figures in the experimental evaluation sections show error bars. However, the description of the experimental methodology makes how these error bars are computed unclear. How many times each experiment is repeated? What differs in each repetition of the experiments?  
- Why are multiclass datasets not used in the experimental evaluation? Does DYNFRS also support multiclass classification tasks? If yes, how do models trained with DYNFRS perform in terms of accuracy, unlearning efficiency, and latency on a stream of mixed requests?
- In Section 4.1, the speedup is computed as $N_{occ}/N_{nai}$. Instead, should it be computed as $N_{nai}/N_{occ}$? Moreover, is the speedup achieved by OCC over the naive method $1/q^2$ or  $1/q$? In Section 4.1, both the values are used.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the unlearning problem in Random Forests for privacy concerns, focusing on efficient data point removal or addition. The DYNFRS framework is proposed for efficient machine unlearning in Random Forests while maintaining predictive accuracy.

### Strengths
1. The paper presents a comprehensive set of experiments, encompassing various types of unlearning scenarios.

2. The proposed method, DYNFRS, demonstrates significant efficiency improvements compared to existing baselines.

### Weaknesses
1. My primary concern is the limited novelty of this paper. DYNFRS appears to be an assemblage of components with minor modifications. The framework consists of three main components: OCC which performs subsampling on trees instead of training samples, essentially randomly selecting $k$ trees; LZY which utilizes the lazy tag concept and  replaces subtree retraining with reconstructing the tree path that connects the modified node u and a leaf; ERT which  is an existing method, with modifications like  only s candidates on one attribute instead of all possible splits. DYNFRS, therefore, seems to be a combination of existing techniques with relatively minor alterations. While the integration of these components may offer some benefits, it is questionable whether the contribution of these improvements meets the standard expected at ICLR.

2. The clarity of the paper's writing could be further improved:

- It would be better if some redundant theorems and formulas could be avoided. For instance:

  (a) Theorem 1's conclusion is trivial, especially given the assumptions of sample independence and the splitting characteristics of tree models.

    (b) Lemma 1 is also trivial, since the major difference in the complexity stems from the introduction of $s$ candidates compared to classic methods.

  If the authors could more directly and concisely highlight these key points instead of using extensive formulas and theorems, it may be further enhance the clarity of the paper.

- Section 4.2 requires a necessary introduction to the lazy tag, particularly since lazy tagging is a classic technique in segment tree problems.

- The sources of observations in Line 209 and Line 260 are unclear. These assertions need proper citations to relevant literature. For example, in point (2) in Line 260, there are considerable research demonstrating the existence of a small portion of neurons or attention heads in neural networks that also can significantly influence inference outputs during the inference phase [1,2,3].

3. The experimental section focuses solely on binary classification, neglecting multi-class scenarios. It would be beneficial to consider multi-class problems.

4. *OCC(0.2) sometimes improves the forest's predictive performance.*  Could the authors provide some insights  for  latent reasons?

5. In section 4.3, introducing consideration of only $s$ candidates, although has a higher chance to remain unchanged when adding or removing data points, it is also entirely possible to not obtain the best split in all possible splits. The authors should discuss this additional loss caused by only $s$ candidates.

### Questions
See my Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
