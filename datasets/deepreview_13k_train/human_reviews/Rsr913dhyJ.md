# ICFI: a Feature Importance Measure For Multi-Class Classification

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Feature importance is one of the most prominent methods in explainable artificial intelligence. It seeks to score the features an artificial intelligence model relies on the most. In multi-class classification, current methods fail to explain inter-class relationships as they either provide explanations for binary classification only, or suffer from aggregation bias. In a multi-class classification scenario, features may carry discriminative power to separate some of the classes while being otherwise less relevant. State-of-the-art feature importance measures do not capture this behavior. We propose Inter-Class Feature Importance (ICFI), a measure that scores the feature importance to discriminate between an arbitrary pair of classes. ICFI is a post-hoc, model-agnostic method, independent from the machine learning architecture employed. ICFI marginalises the target output with respect to the feature of interest, leveraging the resulting change in model behavior to quantify feature importance. We present ICFI’s properties and argue its relevance, describing use cases and showing insights gained. We demonstrate through thorough experiments on real-world datasets how ICFI captures the features characteristics for specific class relationships.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission proposes Inter-Class Feature Importance (ICFI) measure, which scores the feature importance to discriminate between pairs of classes in multi-class classification (MCC). The measure is formulated in Section 3.1, and experiments are conducted in Section 4 to assess the potential usefulness of the proposed measure. 

The notion of ICFI, which is compactly described in Eq (4), is interesting (at least from the conceptual level). However, it seems that the scalability with respect to both the number of features and classes is a crucial challenge in practice.

### Strengths
S1: I think the notion of ICFI is intuitive and interesting. 

S2: Empirical results seem to be in favor of the proposed ICFI measure.

### Weaknesses
W1:  It seems that the scalability with respect to both the number of features and classes is a crucial challenge in practice.

W2:  It might be beneficial to discuss how ICFI can be adapted to enlarge the existing set of instance-level feature importance measures.

### Questions
Q/S1: For each pair of classes, for each feature of interest, did you train one model (after permuting the corresponding feature of interest)? 

Q/S2:  Could you comment on the scalability of the proposed ICFI measure? How many features and classes one might handle by using the proposed ICFI measure? Can it be scalable up to image data sets? 

Q/S3: Could you discuss how ICFI can be adapted to enlarge the existing set of instance-level feature importance measures?

### Soundness
3

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
4

### Summary
This paper focuses on the problem that in the multi-class classification scenario, current methods fail to explain inter-class relationships as they either provide explanations for binary classification only or suffer from aggregation bias. In a multi-class classification scenario, features may carry discriminative power to separate some of the classes while being otherwise less relevant. Focusing on this problem, the authors proposed an Inter-Class Feature Importance (ICFI), to score the feature's importance between an arbitrary pair of classes.

### Strengths
This paper presents an "Inter-Class Feature Importance (ICFI)" method, specifically addressing the problem of inter-class feature importance in multi-class classification, filling the gap in the measurement of inter-class relationship in existing methods. The method can provide model-agnostic explanations without the need to train additional models, addressing the limitations of existing methods in measuring feature importance in multi-class scenario.

### Weaknesses
(1)The paper lacks enough innovation. ICFI avoids the aggregation bias commonly seen in traditional global feature importance methods by introducing a feature importance assessment based on class pairs and feature permuting. At present, some relevant studies have focused on feature permuting and class pairs, such as PFI, SHAP, and LOO. The ICFI method proposed in this paper mainly evaluates the importance of features through feature permuting, and its method mechanism is similar to PFI and SHAP. Therefore, although ICFI has some potential contribution to multi-class feature importance assessment, it is not innovative enough to clearly distinguish ICFI from existing methods.

(2) The writing of this paper should be further improved. There are many writing problems in the paper, which seriously affects the reading. The following are some of the problems I found:
--- On page 2, line 67, "a ML" should be "an ML". On page 2, line 83 has the same error.
--- "Fig 3", and "Figure 3" all appear in this paper. Ensure consistent figure references.
--- On page 3, line 152, "Fig. 8 shows the decision...". "Fig. 8" should be Fig. 1.
--- On page 4, line 205, the symbol "D" lacks definition.
--- On page 8, line 395, "Figure 8 shows the global PFI feature importance...", "Fig. 8" should be Fig. 4.
--- On page 10, in the Fig. 7, the "Shap" should be consistent with "SHAP" in this paper.
--- The description of the figure title is too complicated in this paper, so it is recommended to simplify the figure title to improve readability and add a serial number to the sub-graph for easy reference and understanding.

### Questions
In addition to the weaknesses I have already listed, I have the following questions:
(1)In Section 4.3, four different datasets were selected to verify the performance of ICFI in different tasks, but the complexity of these datasets is limited, and it is recommended to further extend the experiment to complex datasets with high dimensional and larger number of categories.

(2)The idea of assessing feature importance through feature permuting of ICFI is similar to that of PFI. Please analyze the uniqueness and advantages of ICFI similarly.

(3)In the Section 4.3, ICFI was compared to SHAP, PFI, and random strategies, why not choose LIME and PDP as the comparison algorithms?

(4)In this paper, the One-vs-One strategy is used to train the model and perform majority voting, but this method may incur high computational costs when the number of categories is high. It is suggested that the authors add an analysis of the computational efficiency of ICFI .

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Inter-Class Feature Importance (ICFI), a model agnostic method to identify important features to distinguish between a pair of classes for multi-class classification tasks. ICFI is a permutation based feature selection method that measures the drop/increase in model performance when merging a pair of classes. Intuitively if permutations in values of a feature results in bigger model performance deterioration when merging two classes, the feature plays a more important role in distinguishing between those two classes.
Authors study the feature importance from ICFI for various class pairs for a couple of commonly used data sets (Iris and 20 news group) and compare them against a global method (i.e. Permutation Feature Importance). They also, study test accuracy based on number of features used in training a multi-class classifier over four data sets when features are selected based on ICFI and three alternative methods, i.e. PFI, Shapley additive explanations (SHAP), and a random feature selector and show that ICFI outperforms other methods in their studies.

### Strengths
- The paper has done a decent job covering related literature.
- The idea of merging classes, permuting a feature and measuring the delta in empirical error makes sense and is well explained.
- The XAI problem and in particular identifying important features for multi-class classification tasks by looking into features that can help distinguishing between a given pair of classes is a worthwhile problem to solve witch wide use cases.

### Weaknesses
 - The biggest weakness of the method is the lack of clarity in the proposed method. It is not clear how the top important features identified by ICFI for various pairs of classes are combined to train a multi-class classifier. For example, in Fig. 7, test accuracy is measured at different numbers of selected features and it is not explained how important features identified by ICFI across various pairs of classes are being selected. Specifically, are the top-k features selected independently for each class pair and then combined, or is there a global ranking derived from the pair-wise importance scores? The paper lacks a detailed explanation of this crucial step.
- Along the same lines of the first point, it is not clear if ICFI is expected to provide explainability at global level or in terms of distinguishing between a pair of classes only. If the goal is the former, then authors should have discussed more details about how they combine feature importance of various pairs of classes and come up with a global ranking. If it is the latter, then it's not clear why they compare ICFI with global methods such as FPI (e.g. in Fig. 4). The paper needs to clarify the intended scope of ICFI and justify the comparison with global methods if the goal is local explainability.
- Some of the fundamental assumptions/claims of the paper needs further clarification. For example, in the abstract section, authors state that "In multi-class classification, current methods fail to explain inter-class relationships as they either provide explanations for binary classification only, or suffer from aggregation bias", however, there are methods such as LIME for which none of the listed limitations applies. LIME can provide instance-level explanations for multi-class problems without suffering from aggregation bias, making the claim about existing methods inaccurate.
- Along the previous point, the alternative methods studied in the paper, do not include methods such as LIME that theoretically do not suffer from the stated limitations for existing methods. The absence of LIME as a comparison method weakens the empirical evaluation and the claims about the limitations of existing methods. The paper should include LIME to provide a more comprehensive comparison.
- Lastly, the limitations of ICFI are not discussed in the paper. For example, how can ICFI capture the interactions between two or more features, as a concrete case consider a couple of features that do not show strong performance gain on their own while their combination could play a significant role in the predictive power of the model. The paper should address the limitations of ICFI, particularly its inability to capture feature interactions, which is a known limitation of permutation-based feature importance methods.

### Questions
- I can imagine that for the 20 news group data set, since features are words, permuting a feature means replacing it with an unused token/word in the vocabulary (e.g. NULL)? It would be useful if authors can clarify.
- Other questions are captured in the first two bullets of the weakness box.

### Soundness
2

### Presentation
2

### Contribution
2
