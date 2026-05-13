# Enhancing Decision Tree Learning with Deep Networks

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Conventional approaches to (oblique) decision tree construction for classification are greedy in nature. They can fail spectacularly when the true labeling function corresponds to a decision tree whose root node is uncorrelated with the labels (e.g. if the label function is the product of the sign of a collection of linear functions of the input). We define a new figure of merit to capture the usefulness of a linear function/hyperplane in a decision tree that is applicable even in scenarios where greedy procedures fail. We devise a novel deep neural network architecture that is very effective at seeking out hyperplanes/half-spaces/features that score highly on this metric.  We exploit this property in a subroutine for a new decision tree construction algorithm. The proposed algorithm outperforms all other decision tree construction procedures, especially in situations where the hyper-planes corresponding to the top levels of the true decision tree are not useful features by themselves for classification but are essential for getting to full accuracy. The properties of the deep architecture that we exploit to construct the decision tree are also of independent interest, as they reveal the inner workings of the feature learning mechanism at play in deep neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The provided paper introduces an oblique tree learning algorithm that integrates neural networks into its framework. This methodology adheres to a top-down approach in tree construction, where, at each split, a neural network training is employed to separate two classes (thus, applicable to binary classification only). Subsequently, a clustering algorithm is executed to extract a hyperplane from the trained neural network. This hyperplane then serves as the basis for partitioning the data into two subsets, initiating a recursive progression of the algorithm from that point onward.

To evaluate the efficacy and performance of this algorithm, experiments are conducted across various benchmarks, employing several baselines.

### Strengths
- the method is easy to understand and implement;
- the same for the paper, easy to follow.

### Weaknesses
1. In Section 2.1, when asserting that "all greedy methods would fail," it is essential to state the underlying assumptions supporting this claim. As it stands, I find it challenging to ascertain the veracity of this statement. Consider the dataset below consisting of 2 points (for simplicity):

  x | o

where x and o are data points and "|" represents the decision boundaries. Any greedy split will find | as a solution...

If this proposition is intended to be presented as a theorem, then it necessitates a rigorous formulation and a subsequent proof to establish its validity. It is crucial to uphold the highest standards of mathematical rigor when making such assertions, ensuring that they are substantiated by sound theoretical foundations.

2. **Novelty**. The method resembles soft decision trees (SDTs) [1-3] in its formulation in section 3.1. However, instead of learning hyperplane at each node, the method first fits a NN followed by clustering-based heuristics. This is a bit different since it relies on greedy tree growing procedure. However, similar "neural" tree growing technique (without clustering) was employed in Guo and Gelfand (1992). Here, the method applies "postprocessing" to transform deep NN into hyperplane.

3. **Experiments**. The experiment, as presently conducted, exhibits a notable gap in its evaluation methodology. It notably lacks a comparative analysis against well-established oblique tree learning methods, including those referenced in citations [1-5], as well as the work by Carreira-Perpinan and Tavallali from 2018. Such a comparative assessment is paramount in validating the efficacy and distinctiveness of the proposed approach.

4. The method as is only applicable to binary classification and extending it seems to be nontrivial (except, maybe, one-vs-all)?

### Questions
- What is Zan DT method? I don't see any references to it...

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper identifies a family of labelling functions that can be efficiently represented by an oblique decision trees, however existing learning algorithms fail to learn these trees. To overcome this, the paper presents a new splitting criterion (HDS) and present a deep architecture called DLGN that can be used to detect hyperplanes with low HDS to be selected as splits for the internal nodes of the oblique tree.

### Strengths
Strengths:
- Interesting and seemingly novel intuition/observation that is represented by the proposed hyperplane discontinuity score
- Experiments seem to support hypothesis on synthetically constructed datasets
- Generally well-written with useful illustrative figures

### Weaknesses
Weaknesses:
- The main intuition behind the proposed approach is not established theoretically. Further, even the hypothesis itself is not mathematically and precisely formalized. It seems to be motivated by a specific synthetic construction that is not clear if this construction tends to appears in real problems. Specifically, the paper lacks a formal definition of the 'hyperplane discontinuity score' (HDS) and how it relates to the separability of data by oblique decision trees. The connection between low HDS and the ability of a hyperplane to effectively split data is not rigorously proven, relying instead on empirical observations from synthetic datasets. The paper should provide a more precise mathematical framework for the proposed approach.
- The empirical support for the main claim (e.g., Table 2) is also based on experiments with synthetic data. The synthetic data generation process should be described in more detail, including the specific parameters used to create the datasets. It is unclear how these parameters affect the performance of the proposed method and whether the results generalize to other types of synthetic datasets. The lack of experiments on real-world datasets makes it difficult to assess the practical applicability of the proposed approach.
- Experimental results for the proposed decision tree construction method are not very convincing: The baseline Zan DT does better on real datasets and outperforms DLGN DT in 5 datasets while DLGN DT outperforms Zan DT in only 3 datasets. The paper should include a more comprehensive comparison with other oblique decision tree algorithms. The fact that the proposed method does not consistently outperform the baseline on real-world datasets raises concerns about its effectiveness.
- The experiments could benefit from experiments with additional baselines for oblique decision trees (e.g., TAO [Carreira-Perpinan & Tavallali, 2018] and others mentioned), as well as reporting results on training accuracy. The lack of training accuracy results makes it difficult to assess whether the proposed method is overfitting the training data. The paper should also provide a more detailed analysis of the performance of the proposed method on different types of datasets.
- Also, there is no discussion or results on the differences in terms of computational resources (the proposed approach seems to require training a neural network in each node of the tree and running DBSCAN on the whole dataset which may hinder the scalability of the approach). The paper should provide a detailed analysis of the computational complexity of the proposed method, including the time and memory requirements. The scalability of the approach should be evaluated on larger datasets.
- No discussion if/how this can be extended beyond binary classification. The paper should discuss the limitations of the proposed method and how it can be extended to handle multi-class classification problems. The paper should also discuss the potential impact of the proposed method on other machine learning tasks.

Minor typos, inconsistencies:
- space before "Krishnan et al." page 2
- notation: it looks like $\gamma$ should be parameterized by D and f* as well

### Questions
I would appreciate the authors' response to the main weaknesses listed above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a decision tree construction algorithm that outperforms traditional methods, especially when dealing with uncorrelated root nodes. It also offers insights into the inner workings of deep neural networks' feature learning mechanisms.

### Strengths
The paper is easy to follow. I believe that providing an intuitive visualization of decision boundaries and explanations using figures, such as the algorithm diagram in Figure 3, would be helpful support for readers.

### Weaknesses
I believe that constructing a greedy decision tree offers significant advantages in terms of computational time. While it is possible to make the search more complex, I think there is a deliberate choice not to create overly complicated trees in order to balance computation time and performance. In this sense, it seems that the proposed method involves complex processing during tree construction, but there is no evaluation of the computational cost incurred in doing so. I think it's necessary to have a diverse range of evaluations from perspectives other than just accuracy in order to assess the usefulness of the proposed approach. 

Furthermore, since the connection between oblique trees and ReLU networks has been extensively studied, it is necessary to clarify their comparison, mention in related work, and the differences in their respective positions. Specifically, the paper should discuss how the proposed method relates to existing work on oblique decision trees and their relationship to ReLU networks, highlighting the unique aspects of the proposed approach. The current discussion lacks sufficient detail to position the work within the broader context of these related areas. 

When presenting experimental results such as in Table 1, please evaluate the errors. It is important to understand the statistical significance of the results, not just the raw accuracy values. Providing standard deviations or confidence intervals would greatly enhance the analysis. 

The mention "Even ODT construction methods that are not purely greedy in nature seem to fail for such labeling functions" is present in the text, but it appears that there is no supporting experimental or background information for this assertion. This claim needs to be substantiated with either experimental evidence or a detailed explanation of why existing methods fail in these specific scenarios.

### Questions
1: Please provide information about the training time (Check the weaknesses part).

2: I imagine that when using a single decision tree, one may not prioritize accuracy too much. If you want to push for higher accuracy, it's natural to adopt approaches that use multiple trees like Random Forest or Gradient Boosting Decision Trees. However, other factors such as interpretability and processing speed for a single tree might be important. Are there any benefits from that perspective?

3: Section 3.2 contains the mention: "A trained DLGN shows some interesting properties that are not possible to even check on ReLU networks." However, it is well-known that ReLU networks partition feature space linearly. In that sense, I believe hyperplanes can be checked, can't they? (e.g., “Neural Networks are Decision Trees, Caglar Aytekin, (2022)”)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
