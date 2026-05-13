# Cross-Entropy Is All You Need To Invert the Data Generating Process

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
Supervised learning has become a cornerstone of modern machine learning, yet a comprehensive theory explaining its effectiveness remains elusive. Empirical phenomena, such as neural analogy-making and the linear representation hypothesis, suggest that supervised models can learn interpretable factors of variation in a linear fashion. Recent advances in self-supervised learning, particularly nonlinear Independent Component Analysis, have shown that these methods can recover latent structures by inverting the data generating process. We extend these identifiability results to parametric instance discrimination, 
then show how insights transfer to the ubiquitous setting of supervised learning with cross-entropy minimization. We prove that even in standard classification tasks, models learn representations of ground-truth factors of variation up to a linear transformation. We corroborate our theoretical contribution with a series of empirical studies. First, using simulated data matching our theoretical assumptions, we demonstrate successful disentanglement of latent factors. Second, we show that on DisLib, a widely-used disentanglement benchmark, simple classification tasks recover latent structures up to linear transformations. Finally, we reveal that models trained on ImageNet encode representations that permit linear decoding of proxy factors of variation.
Together, our theoretical findings and experiments offer a compelling explanation for recent observations of linear representations, such as superposition in neural networks. This work takes a significant step toward a cohesive theory that accounts for the unreasonable effectiveness of supervised deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a theoretical framework to further advance the linear identifiability of self supervised learning, and further to extend to general supervised classification tasks where cross-entropy loss is used.  The theoretical framework is constructed on a clever data generating process on the clusters of von-Mises-Fisher distribution.  Experimental results are included to empirically demonstrate the validity of the theoretical analysis. Empirical experiments on ImageNet-X dataset are also included.

### Strengths
The framework poses significant progress towards better theoretical understanding on machine learning tasks, particularly classification tasks. If the theory holds, it may have a substantial influence on theories of adjacent research areas as well as many applications. Although this is a theoretical paper, the author(s) have made efforts to make the writing approachable, e.g., drawing from practical observations such as interpretable embeddings across input pairs from Mikolov 2013, and linear superposisiton in Elhage 2022.

### Weaknesses
My main concern is on how the author(s) conduct empirical validation. Table 2 and 3 appears to be the main empirical validation of the proposed hypothesis. The author(s) have devised a clever method for validation. However the statstics in Table 2 and 3 only shows that when the Assumptions 1 is true, the DIET method can successfully recover the cluster vectors with high probability. Another set of the experiments should be conducted to demonstrate that the hypothesis can be "falsified" when the assumptions are no longe true. This can be easily done with the current experiment setup:
1. After the data in each cluster are generated, choose 2 clusters, and random swap a percentage of the samples between the two, report the statistics of the recovery of all clusters. If the hypothesis holds, the outcome should be clear
2. Increase the percentage of the samples randomly swapped, the trend should be clear. 
3. Repeat 1 and 2, but with more clusters involved. The trend represented by the statistics should also be quite clear

### Questions
Reiterate the need of additional experimental results, please consider doing the following:

1. After generating data in each cluster, randomly swap a percentage of samples between two clusters and report recovery statistics for all clusters.
2. Increase the percentage of randomly swapped samples and observe the trend.
3. Repeat this process with more clusters involved.

This would provide a more comprehensive evaluation by demonstrating both when the hypothesis holds and when it breaks down under violations of the clustering assumptions.  I'd like to see the experimental results discussed in the section above. In my view, it should be easy to conduct and will strengthen the paper. 

The details of the experiments on DisLib and ImageNet-X should be included in appendix and/or a open github repo. DisLib (or at least a subset of it) has been widely used in many disengagement papers. The code or details explanation of the experiments should be provided for other researchers to compare, it is understandable that this experiment is not the main focus of this manuscript, including:

1. Hyperparameters used
2. Data preprocessing steps
3. Evaluation metrics
4. Any modifications made to standard implementations

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
4

### Summary
- This paper extends identifiability results for self-supervised learning techniques to include classifiers trained with cross entropy, under certain Assumptions.
- The Assumptions include a strong condition on the underlying data generating process that is unlikely to hold in practice: a clustering model with von Mises-Fisher samples around the cluster centers to yield the latent factors.
- Under their Assumptions, they present a theorem claiming that such cluster-center-plus-vMF latents are identifiable up to a linear transformation using the DIET objective (which is cross entropy where the labels are training sample indices).
- The paper validates the theoretical results on synthetic data where the latent factor is known, showing that in many of the settings covered by the theory, the R^2 score between the true and predicted latents are over 98%.
- It further explores empirical applicability of the theory on the DisLib, a disentanglement benchmark with known factors of variation. While the data generating process does not match with the theoretical model in this setting, they still demonstrate generally strong Pearson correlations between the learned representations and the factors of variation.
- A more challenging study using human-labeled factors of variation in the ImageNet-X dataset gives much weaker, but still positive, correlations between the factors and the learned representations.

### Strengths
- The paper is clear and well-written.
- The experiments are appropriate and demonstrate that the theoretical results at least occasionally apply beyond the setting of the fairly restrictive assumptions about the data generating process.

### Weaknesses
 - Tables 2.3/Synthetic Data experiments: The identifiability suffers substantially as the dimensionality increases above 10, even if the perfect model is well-specified. This seems like potentially a major issue in practice, as the true latents of interest may often be very high-dimensional, and the model will often be misspecified. You acknowledge that this is an issue, but perhaps some additional discussion could be beneficial.
- I’m not sure that the two synthetic misspecification examples are very convincing about the broad generality of the theory. Using a Laplace distribution in place of the vMF degrades performance substantially already, and I’m not sure it should be considered a particularly bad case of misspecification. Perhaps including experiments with mixtures of Gaussians, with varying numbers of mixture components would help understand how well the theory holds up over more challenging misspecification settings?
- The results on ImageNet-X appear quite weak, which seems to indicate that violation of the Assumptions by the data generating process leads to substantial reduction in identifiability. Perhaps some additional discussion to help the reader understand why these results are weak for most of the factors of variation would help?
- Line 71: Extraneous comma after the hyphen.
- Line 457: “underlying training classification training task was solved” => “underlying training classification task was solved.” (Extra “training”, missing “.”)
- Line 527: “Conlusion” => “Conclusion”.

### Questions
- What would be the impact of repeated elements in the training data when using the sample index classification head? In this case, the representation would try to map one input to two (or more) arbitrary indices. Would this impact the identifiability results in any way?
- I’m not sure I understand the explanations for why a high concentration parameter is so detrimental to the identifiability. Could you give some additional intuition?
- Relatedly, high concentration doesn’t seem to violate any of the listed Assumptions (and you don’t mark it with a red X in the tables) – is this poor performance an indication of a missing Assumption?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work they show that under some assumptions on the distribution of the ground truth latent variables and the 
distribution of the labels then a model trained with cross-entropy is able to recover the ground truth latents up to 
a linear transformation.

### Strengths
S1: The result that under Assumptions 1C Appendix A.2 we get linear identifiable representations is both new and interesting.

### Weaknesses
W1: The article makes too strong a claim that cross-entropy on its own gives linearly identifiable representations. 
This claim is too strong, because additional assumptions (Assumptions 1C Appendix A.2) are needed to get the result. 
Places where this claim is made:
- The title
- The abstract: "We prove that even in standard classification tasks, models learn representations of ground-truth factors of variation up to a linear transformation."
- line 255-256: "Namely, supervised learning performs non-linear ICA."
- Line 304-305: "providing a theoretical explanation for the success of supervised learning in learning linearly decodable representations."
- Line 310-311: "Solving an (almost) arbitrary classification task by optimizing the cross entropy objective is sufficient to invert the DGP and identify the ground-truth representation up to a linear transformation"
- Line 521-525: The "Implications for Deep Learning" paragraph. 
- Line 534-536: "By linking self-supervised learning—via nonlinear ICA and DIET—to supervised classification, we provide a theoretical framework that explains why simple classification tasks recover interpretable and transferable representations."

W2: The assumption made that "instance label I is uniformly distributed" (Assumptions 1C, (iii)) is important 
because many classification tasks have unbalanced labels. Therefore, this assumption should be made more clear. 

W3: In line 485, 518-519, you write: "Our experimental results also suggest that our assumptions can be relaxed, 
as linear identifiability seems to hold even when some of the assumptions are violated". However, there are also 
some examples in tables 2 and 3 of $R^2$ being surprisingly low even though all the assumptions should be satisfied. 
The authors should be more clear about where this discrepancy comes from.

### Questions
Q1: In Table 2 with $N=10^3$, d=20, 100 classes, vMF($\kappa = 10$) and $N=10^3$, d=5, 100 classes, vMF($\kappa = 50$)
some of the $R^2$ values are much lower. You write that this is 
"possibly explained by the content-style partitioning of latents (von Kügelgen et al., 2021) and insufficient 
augmentation overlap (Wang et al., 2022; Rusak et al., 2024)." What do you mean by this? 
I am guessing that you would give the same explanation for table 3, d=5, 100 classes, vMF($\kappa = 50$)?  


Q2: In table 4, what is your interpretation of some of the pearson correlations being less than 0.8 and a few even 
less than 0.6?  

Q3: In fig. 3, most factors of variation are captured with better than chance performance, but a few are not and many 
seem quite close to chance. Do you have an idea of why this might be?

### Soundness
3

### Presentation
2

### Contribution
3
