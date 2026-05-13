# Class-Imbalanced Graph Learning without Class Rebalancing

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Class imbalance is prevalent in real-world node classification tasks and poses great challenges for graph learning models.
Most existing studies are rooted in a \emph{class-rebalancing} (CR) perspective and address class imbalance with class-wise reweighting or resampling.
In this work, we approach the root cause of class-imbalance bias from an topological paradigm.
Specifically, we theoretically reveal two fundamental phenomena in the graph topology that greatly exacerbate the predictive bias stemming from class imbalance.
On this basis, we devise a lightweight topological augmentation framework \alg{} to mitigate the class-imbalance bias \textit{without class rebalancing}.
Being orthogonal to CR, \alg{} can function as an \ul{\textit{efficient plug-and-play module}} that can be seamlessly combined with and significantly boost existing CR techniques.
Systematic experiments on real-world imbalanced graph learning tasks show that \alg{} can deliver up to 46.27\% performance gain and up to 72.74\% bias reduction over existing techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study delves into the challenge of imbalanced node classification on graphs. The authors explore two phenomena in the underlying graph topology that intensify predictive bias due to class imbalance, both theoretically and empirically. They introduce a model called ToBE, designed to alleviate class-imbalance bias without the need for class rebalancing. Through experiments conducted on various datasets, the effectiveness of the proposed model is demonstrated.

### Strengths
1. Class imbalance is an important issue in the field of graph imbalance learning, which requires deep investigation.

### Weaknesses
1. The AMP and DMP phenomena are studied in many previous works. The AMP is basically the heterophily issue studied in previous heterophily GNN and graph anomaly detection literature. The DMP is basically the information insufﬁcient issue studied in previous topology imbalance literature.

2. I find the theoretical analysis has nothing to do with the model design. In the theoretical analysis, this work only analyzes the relation between the imbalance ratio and the severity of AMP and DMP. However, in the model design, this work directly uses model prediction uncertainty to estimate nodes’ risk of being misclassified and simply claims that this risk of being misclassified is due to AMP/DMP, which is not verified in the theoretical part. From my view, there is not any relationship between these two parts. Even without the theoretical part, the model design part looks self-contained.

3. In the model design, this work claims that, for high-risk nodes, the most possible prediction is unreliable, and instead uses the second possible prediction as the estimated label. Why choose the second possible prediction? Why not the third possible? As this part is critical to model performance, I would expect authors to further clarify this.

4. In Figure 2(b), it seems that there is still a large discrepancy between the performance of the minority class and the majority class, even if the AMP/DMP score is the same. That indicates that there are some other factors that influence the performance discrepancy. I would expect the authors to further clarify this.

5. The existing baselines lack comprehensiveness, and there is a lack of thorough comparison with recent approaches, such as [1, 2, 3, 4, 5].

### Questions
Please see the Weaknesses.

### Soundness
2 fair

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The study introduces a post-processing module for semi-supervised vertex classification models in the presence of class imbalance. The module aims to mitigate prediction errors and biases caused by class imbalance by incorporating virtual vertices and establishing connections with original vertices exhibiting high prediction errors or low confidence (referred to as high-risk vertices in the paper). Through long-range message propagation, the proposed approach effectively addresses the challenges posed by class imbalance in semi-supervised vertex classification tasks. Experimental results demonstrate its relative improvement over existing models under real-world scenarios characterized by class imbalance.

### Strengths
S1. Formulas that accurately describe the AMP and DMP problems were derived, providing precise definitions for these problems.

S2. Extensive experiments consistently show that the proposed post-processing module significantly enhances the learning effectiveness of the current model across multiple metrics and base models.

S3. The writing style is smooth and coherent.

### Weaknesses
W1. The lack of comparison with other post-processing modules for class imbalance graph learning, such as the classical Residual Propagation method, undermines the persuasiveness of the proposed method's effectiveness. 

W2. The study lacks a comparison between the proposed method and the predictive performance of the base model on balanced data, which diminishes its persuasiveness.

W3. The absence of a comparison with the predictions of the base model on balanced data weakens the persuasiveness of the results.

W4. The use of "relative improvement rate" may not be the most comprehensive measure to evaluate the model's performance, as some base models may inherently perform poorly in addressing highly imbalanced class semi-supervised vertex classification tasks.

W5. The details of how this module collaborates with other base models are not adequately explained, lacking formulas and clear visual representations.

W6. The study's focus is not novel, and the problem scope is narrow. The proposed method has the potential for broader applications, such as imbalanced edge prediction, and should also consider the module's inductive capabilities. Otherwise, solely emphasizing the relative improvement of the existing model's transductive ability may not hold significant practical significance.

### Questions
Similar to what was mentioned in the weaknesses:

Q1. How does the effectiveness of this module compare to post-processing modules of other class imbalance graph learning methods?

Q2. How does the performance of this module compare to the base model combined with data balancing during prediction?

Q3. What are the specific formulas and graphical representations illustrating the collaboration between this module and the base model?  Can it be independently developed as a foundational model rather than a post-processing module?

Q4. Can this module be applied to other tasks and demonstrate effectiveness? How does it perform in terms of inductive capabilities?

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the problem of class imbalance graph learning. It first revisits several remaining issues of existing methods. Then, from an orthogonal topological paradigm, they theoretically find two fundamental reasons. After that, they propose a lightweight topological augmentation framework called TOBE to mitigate the class-imbalance bias without class rebalancing. Finally, it conducts some experiments to evaluate the proposed method, showing that that TOBE can sometime outperform state-of-the-art baselines on several tasks across multiple datasets.

### Strengths
1.	The authors provide their codes.
2.	It provides some theoretical support for the proposed model.
3.	It tests on several widely-used datasets, and the proposed method can sometimes beat the existing methods.

### Weaknesses
1.  The proposed method seems to be meaningless at times. As shown in Table, sometimes the original methods (such as APPNP and GPRGNN) can beat either +ToBE0 or + ToBE1. More over, as shown in Tables 7 and 8, lots of baselines (Vanilla, Reweight, ReNode, and GSMOTE) can sometimes beat either +ToBE0 or + ToBE1. This inconsistency in performance raises concerns about the robustness and general applicability of the proposed approach. The fact that simple baselines can outperform the proposed method in certain scenarios suggests that the topological augmentation may not always be beneficial and could even introduce noise or hinder learning in some cases. A more thorough analysis of when and why TOBE fails is needed to understand its limitations.
2.  Some grammatical errors, like 1) groundtruth labels –> “ground-truth”; 2) Coauthor networks-> “co-author”; and 3) “Fig. 5 compares”  “Figure”. The inconsistent use of capitalization and hyphenation detracts from the overall professionalism of the paper. These errors, while seemingly minor, can impact the reader's perception of the work's quality and attention to detail. The lack of consistent terminology and formatting can also make the paper harder to read and understand.

### Questions
1.	As shown in Tables 7 and 8, why lots of baselines can sometimes beat both ToBE0 and ToBE1? As such, why the proposed method is useful?
2.	As we can see, the performance of ToBE0 and ToBE1 are unpredictable. So that, how to decide which one should be used for a given method or setting?
3.	“Similar analysis can extend to k ≥ 3.” --- have you ever proved this?
4.	In Table 3, why the “Node” column only has one type of results?
5.	See the weakness in the “*Weaknesses” part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of class imbalance in node classification tasks. Authors introduces ToBE (Topological Balanced augmEntation), a model-agnostic technique. The essence of ToBE is dynamic topological augmentation to identify and rectify nodes that are critically influenced by the identified challenges. Results shows promising improvements including reducing bias and enhancing performance in class-imbalanced node classification, outperforming traditional CR techniques.

### Strengths
1. Instead of the conventional class-rebalancing methods, the paper provides a topological viewpoint to address the issue.

2. The paper offers a theoretical understanding of the disparities in graph topology between majority and minority classes, leading to a deeper comprehension of the root causes of the problem.

3. ToBE is model-agnostic and efficient, and can be easily integrated with other existing techniques.

4. Experiments validate the efficacy of ToBE, showcasing its superiority in terms of performance, robustness, and versatility.

### Weaknesses
1. The augmentation method introduced in this paper could potentially escalate the computational complexity, presenting challenges for deployment in large-scale scenarios. It might be beneficial to either highlight this as a potential limitation or to delve into a theoretical analysis addressing its implications in expansive applications. Specifically, the method's reliance on topological analysis, which requires processing the entire graph structure, could become a bottleneck for very large graphs. The paper should provide a more detailed analysis of the time and space complexity of the proposed augmentation, especially in relation to the size of the graph and the number of classes.

2. As with any data modification technique, augmentation inherently brings the risk of overfitting. It's crucial to recognize this aspect and perhaps consider empirical evaluations or additional experiments to shed light on this concern, suggesting possible mitigation strategies. The paper should explore the potential for the model to overfit to the augmented topology, particularly in cases where the augmentation is too aggressive or not well-tuned. It would be beneficial to see experiments that specifically test for overfitting, such as by comparing performance on training and validation sets with and without the augmentation.

3. The manuscript remains silent on the performance of the proposed methodology in multi-class classification environments, as well as its adaptability to tasks other than node classification. Exploring these facets could provide a more comprehensive view of its applicability. The paper should clarify whether the method is directly applicable to multi-class scenarios or if modifications are needed. Furthermore, it should discuss the potential for extending the method to other graph-based tasks, such as link prediction or graph classification, and the challenges that might arise in doing so.

4. While the topological strategy presented is innovative, it seems particularly designed for graph-centric challenges. This specialized focus might limit its direct utility in varied domains, and acknowledging this could provide a more grounded perspective. The paper should discuss the limitations of the approach in non-graph settings and explore potential avenues for adapting it to other data types, such as tabular data or time series data. The current formulation seems tightly coupled to graph structures, and the paper should address how this might restrict its broader applicability.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
