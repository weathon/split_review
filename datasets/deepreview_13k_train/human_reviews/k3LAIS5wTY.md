# Rethinking Evaluation for Temporal Link Prediction through Counterfactual Analysis

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
In response to critiques of existing evaluation methods for temporal link prediction (TLP) models, we propose a novel approach to verify if these models truly capture temporal patterns in the data. Our method involves a sanity check formulated as a counterfactual question: "What if a TLP model is tested on a temporally distorted version of the data instead of the real data?" Ideally, a TLP model that effectively learns temporal patterns should perform worse on temporally distorted data compared to real data. We provide an in-depth analysis of this hypothesis and introduce two data distortion techniques to assess well-known TLP models.
Our contributions are threefold: (1) We introduce two simple techniques to distort temporal patterns within a graph, generating temporally distorted test splits of well-known datasets for sanity checks. These distortion methods are applicable to any temporal graph dataset. (2) We perform counterfactual analysis on six TLP models JODIE, TGAT, TGN, CAWN, GraphMixer, and DyGFormer to evaluate their capability in capturing temporal patterns across different datasets. (3) We introduce two metrics -- average time difference (ATD) and average count difference (ACD) -- to provide a comprehensive measure of a model's predictive performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors of this work propose an approach to apply counterfactual analysis in the evaluation of dynamic link prediction. To this end, they first introduce the idea to use distorted versions of the test set in a temporal graph, where temporal information is (partly) removed. They argue - based on formal logics - that a model trained on an undistorted temporal graph that generally performs as well or better on a temporally distorted test set does not actually learn temporal patterns in the training set. Building on this idea, the authors introduce two different temporal distortion approaches, along with two temporal distortion metrics that can be used to quantitatively compare distorted and undistorted temporal graphs. They then apply their approach to five temporal graph data sets and six state-of-the-art dynamic link prediction techniques, concluding that the majority of state-of-the-art temporal graph learning methods actually does not learn temporal patterns in common data sets.

### Strengths
[S1] The authors address an important open issue in the evaluation of dynamic link prediction

[S2] The authors combine the approach of counterfactual analysis from causal inference and apply it to the evaluation of temporal graph learning. To the best of my knowledge, this is a novel combination (even though comparisons to shuffled temporal graphs have been considered in other works). 

[S3] The results are interesting and important as they suggest that the majority of temporal graph learning architectures actually do not learn temporal information (at least for the link prediction task and considering the random shuffle distortion).

[S4] The paper is exemplary in terms of its clarity. It is a joy to read it.

### Weaknesses
[W1] I would have expected a more detailed description of the experimental evaluation in section 3, including the hyperparameters used to train the models, batch sizes, negative sampling strategy etc. Specifically, the batch size used during training is a crucial parameter that can significantly affect the performance of dynamic link prediction models, especially those that aggregate information within a batch. The lack of detail regarding this parameter makes it difficult to assess the validity of the experimental results.

[W2] The analysis does not take into account some of the issues outlined in recent works (and also mentioned in this paper), in particular the influence of the negative sampling strategy on the evaluation of dynamic link prediction. The choice of negative sampling strategy can introduce bias and affect the ranking of different models, and this aspect should be carefully considered in the evaluation.

[W3] I am not convinced that the specific verbal description of proposition 3.1 holds in this generality (see question below) and I would appreciate if this crucial aspect (which also influences the interpretation of results for one of the distortion methods) could be clarified by the authors. The current verbalization of the proposition is too strong, as it does not account for the specific type of temporal distortion applied to the test set. The implication that a model cannot learn temporal patterns based on its performance on a distorted test set is only valid if the specific distortion method effectively removes the temporal patterns that the model is supposed to learn. 

[W4] I did not understand the motivation of the Intense distortion function, and what we can learn from it about the ability of a model to learn temporal patterns (see my question below). This somehow limits the contribution of the work to an - albeit interesting - analysis of dynamic link prediction in test sets with randomly permuted timestamps. The Intense distortion method, which creates duplicate edges in a temporal neighborhood, does not necessarily destroy temporal patterns. Therefore, the fact that models perform similarly on the original and intensely distorted test sets is not surprising and does not provide strong evidence that the models fail to learn temporal patterns.

### Questions
Referring to [W1], please report all details of the experimental evaluation, especially which hyperparameters were used. Also, the batch size used to train the models is known to influence the  of dynamic link prediction, especially for those models aggregating links within batches.

Regarding [W2], if I understood the experimental evaluation correctly, a simple random negative sampling was used. Referring to Porsafaie et al. 2022, I wonder whether the negative sampling strategy used to train the models will also affect the results in table 3? What is your expectation? Did you evaluate this?

Considering [W3], I believe that the specific verbalization of proposition 3.1 is too strong. Let me explain: In proposition 3.1 the counterfactual question is used to imply that a model f cannot learn the temporal patterns in E_{train}. However, since the counterfactual question depends on a *specific method* to temporally distort the test set, I would argue that this aspect must also appear in the sentence after the implication. As an example, we may temporally distort a graph such that the temporal patterns that are learned by a model are preserved, in which case the probability P(y_x | x', y') can be zero. But this does not necessarily imply that the model cannot learn temporal patterns. It only implies that it cannot learn those temporal patterns that are destroyed by this specific distortion approach. It would be much appreciated if the authors could clarify this aspect, or show me why my argument above is wrong.

Finally - and referring to [W4] - this may also explain why in table 3 none of the methods can distinguish the real temporal graphs from those where the Intense distortion has been applied. This could simply be due to the fact that the Intense method leaves crucial temporal patterns untouched, in which case this result is neither surprising nor interesting. In this sense, I find the results on the Shuffle distortion much more convincing, as it guarantees that temporal patterns are destroyed (and the implication above becomes valid). Could the authors clarify their motivation to study the Intense distortion function?

In light of my open questions and suggestions above, I have assigned an overall rating of 6 for now, but would be willing to raise it if my concerns are adequately addressed.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This study presents a method to verify whether existing temporal link prediction (TLP) models effectively capture temporal patterns in data. To this end, the authors propose a counterfactual question: "What if a TLP model is tested on a temporally distorted version of the data instead of the real data?" They argue that, ideally, TLP models that capture temporal patterns well on the training set should perform worse on temporally distorted data compared to the original data. Specifically, the authors introduce two simple techniques for distorting temporal graphs and create a distorted test dataset to conduct counterfactual analysis on six existing TLP models.

### Strengths
•	S1. Well Motivated: Traditional evaluation methods for temporal link prediction often assess whether an edge exists between two nodes at a specific time. However, these methods are limited to timestamps within the ground truth, constraining the evaluation to specific query times. This study highlights the need for alternative evaluation metrics for temporal link prediction.

•	S2. Originality: By using evaluation methods beyond the standard metrics in temporal link prediction, the study provides a diverse and new assessment of model performance on the temporal link prediction task.

•	S3. Clarity: The paper is generally well-structured and easy to follow. It addresses issues with current evaluation methods, introduces new evaluation metrics, explains them in detail, and then applies them to analyze existing TLP models.

### Weaknesses
•	W1. Logical Structure: While the paper identifies issues with existing evaluation metrics, the proposed counterfactual question may not fully address these issues. The connection between the shortcomings of current metrics and the model's ability to capture temporal patterns is not adequately explained. Additionally, there is insufficient support for Proposition 3.1 in the counterfactual analysis. The reasoning behind why models that perform well on the distorted test set have failed to learn temporal patterns is unclear based on the provided proof. Specifically, the paper does not adequately explain why a model that performs well on distorted data necessarily implies a failure to learn temporal patterns, rather than simply indicating a model that is robust to temporal distortions or has learned some other underlying pattern that is not specific to the original temporal ordering. The link between the binary classification objective and the inability to capture temporal patterns is also not sufficiently established.

•	W2. Experimental Support: The counterfactual analysis posits that if TLP models perform similarly or better on the distorted test set compared to the original test set, they have not learned temporal patterns in the training set. However, the experiments in Table 3 simply show that many TLP models perform similarly or even better on the distorted test set, with some results deviating from the expected trend. This limited experimental evidence does not conclusively support the claim that TLP models fail to learn temporal patterns from the training set. The experiments do not explore the sensitivity of the results to different distortion parameters or the degree of distortion applied. Furthermore, the analysis does not consider the possibility that models might be learning some form of structural information that is invariant to the applied temporal distortions, leading to similar performance on both original and distorted test sets.

•	W3. Definition of Key Terms: The paper lacks clear definitions for several crucial terms. Key concepts like "temporal pattern" and "learnability of a temporal graph" in the Proposition 3.1 are not adequately defined or explained, which makes it difficult to interpret the claim that TLP models fail to learn temporal patterns. The definition of 'learnability' is particularly vague, and it is unclear how this relates to the specific task of temporal link prediction. The paper does not provide a formal definition of what constitutes a temporal pattern, making it difficult to assess whether the proposed counterfactual analysis is actually measuring the ability to learn such patterns.

### Questions
•	Q1. How does the counterfactual question relate to the issues with existing evaluation methods in the introduction for temporal link prediction? The previously mentioned issues are limited to the timestamps within the ground truth and performance variation due to negative sampling. How does the counterfactual question address each of these concerns?

•	Q2. In the introduction section, it is stated that the counterfactual question tests a TLP model's ability to capture temporal patterns in a temporal graph. Could you clarify the definition of "temporal patterns"? Additionally, why should a TLP model capable of learning temporal patterns perform worse on temporally distorted data? In my opinion, if a model generalizes well, it might perform better even on temporally distorted data, depending on the distortion method.

•	Q3. I found Proposition 3.1 in the counterfactual analysis difficult to understand. What does it mean for a temporal graph to be "learnable," and is this a reasonable assumption? Moreover, why should statement 6 hold if statements 1 through 5 are satisfied?

•	Q4. According to the temporal distortion techniques in section 3.2, methods like INTENSE can add edges frequently appearing in the training set back into the test set. Wouldn’t TLP models that learn structural and temporal patterns still perform well by leveraging the learned structural patterns from past interactions?

•	Q5. Based on the results in section 4, most TLP models fail to capture temporal patterns across most datasets according to the counterfactual analysis. However, this conclusion is only valid if the counterfactual question itself is valid. To support the claim that models fail to capture temporal patterns, more diverse and rigorous experiments are necessary.

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
3

### Summary
This paper presents a new approach to evaluating temporal link prediction models, stating that the model should perform worse on temporally distorted test data. Two data distortion techniques are introduced, namely intense and shuffle. Two new evaluation metrics are proposed: average time difference and average count difference. Empirical experiments are carried out on six temporal graph datasets.

### Strengths
Novelty: The paper provides a new perspective to evaluate the temporal link prediction models.

Presentation: The paper is well-written and pretty understandable. The figures help demonstrate the points of the paper.

### Weaknesses
1.  The weaknesses of the binary classification approach claimed in the introduction section are not justified appropriately, especially the first and the second. Different metrics are designed for different tasks. We can imagine that when finding a temporal path between two nodes, we only care about whether an edge exists when needed, not within a time interval. For example, "Is the gate open at 9 a.m.?" instead of "Is the gate open between 7 a.m. and 3 p.m.?" when you only need to pass the gate at 9.

2. Proposition 3.1's proof is incorrect, making it vulnerable. The proposition discusses the probability that prediction accuracy drops when the test data is distorted, while s6 in the proof does not address this probability. Also, claiming that satisfying s1-s5 will result in s6 is assuming the conclusion.

3.

### Questions
Can you elaborate more about why the binary classification approach is ill-posed?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors considered the quality evaluation of the temporal link prediction (TLP) task. Two new evaluation strategies (i.e., Intense and Shuffle) based on counterfactual analysis on TLP models (with metrics of average time difference (ATD) and average count difference (ACD)) were proposed. Experiments demonstrate that under the new evaluation strategies, some SOTA TLP methods may still fail to 'capture temporal patterns' of some widely-used public dynamic graph datasets.

### Strengths
**S1**. This paper is well-written and well-motivated, which makes it easy to read.

**S2**. The limitations of existing evaluation strategies of TLP (i.e., the major topic of this paper) are seldom studied or discussed in related literature.

**S3**. The idea of using counterfactual analysis to design new evaluation strategies of TLP is interesting.

### Weaknesses
 **W1**. Some of the statements regrading the motivation and research gaps are weak, which need further interpretations.

  For instance, in Section 1, the authors claimed that 'the timestamps in the query are restricted to the timestamps present in the ground truth , which makes the evaluation biased and does not test the model’s performance in the continuous time range' but why? Further, interpretations combined with toy examples or rigorous theoretical analysis are recommended.
  

***

**W2**. From my perspective, the theoretical analysis of Proposition 2.1 is relatively weak, which cannot be considered as a rigorous analysis.
  
  The statement 'model $f$ is capable of learning patterns' is weak. It is unclear how to determine (e.g., quantitatively measure) that a model is capable or incapable of learning some patterns. It is also similar for the statement 'can(not) capture/learn temporal patterns'. These are very strong statements. From my perspective, it is insufficient to qualitatively describe them only using natural languages. Instead, rigorous quantitative analysis is required.
  
  The performance of a model on test set may also decline when it encounters the well-known over-fitting issue. There are no further discussions regarding this issue.


***

**W3**. Experiments in Section 4 are, to some extent, too simple. Some details regarding experiment results also need further clarification.

  In Section 4, only the experiments results w.r.t. the AP metric were given. In Section 1, some other metrics (e.g., AU-ROC, MAR, and MRR) were mentioned. However, there are no further experiment results based on these metrics, which cannot fully validated the motivations of this paper.
  
  The proposed evaluation metrics involve two additional sampling strategies with hyper-parameters $K$ and $\bar \tau$. However, there are no further analysis regarding the effects of these hyper-parameters.
  
  Discussions about the experiment results in Table 3 are insufficient. After reading Table 3, it is still unclear for me on each dataset, which TLP method performs the best under the new evaluation metrics.
  
  It is a good presentation to give the example in Figure 2, but the concrete definitions of $\lambda^* (t)$ and $\lambda' (t)$ are not given. It is unclear for me how the corresponding edges were generated (e.g., following what probability distributions).

***

**W4**. At the end of this paper, there is no conclusion section to discuss the limitations of this study and possible future work to address these limitations.

### Questions
See **W1**-**W4**.

### Soundness
2

### Presentation
3

### Contribution
2
