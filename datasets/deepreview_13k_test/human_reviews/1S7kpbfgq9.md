# Normalized Space Alignment: A Versatile Metric for Representation Analysis

- Decision: Reject
- Scores: 8, 3, 3, 5

## Abstract
We introduce a manifold analysis technique for neural network representations. Normalized Space Alignment (NSA) compares pairwise distances between two point clouds derived from the same source and having the same size, while potentially possessing differing dimensionalities. NSA can act as both an analytical tool and a differentiable loss function, providing a robust means of comparing and aligning representations across different layers and models. It satisfies the criteria necessary for both a similarity metric and a neural network loss function. We showcase NSA's versatility by illustrating its utility as a representation space analysis metric, a structure-preserving loss function, and a robustness analysis tool. NSA is not only computationally efficient but it can also approximate the global structural discrepancy during mini-batching, facilitating its use in a wide variety of neural network training paradigms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Normalized Space Alignment(NSA), a new manifold analysis technique designed to compare neural network representations; NSA compares pairwise distances between point clouds from the same data source but with different dimensionalities. NSA is proposed as both a differentiable loss function and a similarity metric, and it is computationally efficient. The paper demonstrated the NSA's versatility in representation analysis, structure-preserving tasks, and robustness testing against adversarial attacks.

### Strengths
1) NSA can be used both as a loss function and a similarity metric across different applications 
2) NSA is designed to work efficiently in large-scale applications with a quadratic complexity that is better than some existing methods 
3) It is also effective in preserving structural characteristics and identifying vulnerabilities in neural networks, even under adversarial attacks
4) the paper provides a thorough analysis with multiple experiments and comparisons to other methods like RTD, CKA validating NSA's effectiveness

### Weaknesses
1) The reliance on Euclidean distance as a primary metric may limit performance in high dimensional spaces due to curse of dimensionality 
2) NSA is versatile but may not require careful tuning and modifications to work effectively in specific scenarios
3) The limitations of NSA are not explored beyond high-dimensionality issue

### Questions
1) How does NSA perform in extremely high-dimensional spaces where Euclidean distance is known to be problematic? Are there alternative distance metrics that could be integrated into NSA?
2) How sensitive is NSA to parameter settings, and what are the best practices for tuning it in different applications (e.g., adversarial robustness vs. dimensionality reduction)?
3) Given the versatility of NSA, do you envision any specific areas where its application would be limited or challenging?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Normalized Space Alignment (NSA), a novel metric to analyze neural network representations. NSA compares two point clouds (representing data structures within neural networks) by preserving both global and local structures, regardless of differing dimensionalities. It can be used to preserve representation structures in tasks such as suitable for diverse tasks such as dimensionality reduction, adversarial robustness assessment, and cross-layer representation analysis. NSA’s main advantage is its ability to efficiently preserve global and local structure across different dimensional spaces. The authors showcase NSA’s versatility by applying it across various tasks, demonstrating its computational efficiency and robustness, particularly in mini-batch processing.

### Strengths
- NSA introduces a new approach for representation alignment with applications in dimensionality reduction, structure-preserving autoencoders, and robustness analysis, highlighting its adaptability to multiple tasks.

- Its quadratic computational complexity improves on the cubic complexity of alternative metrics like RTD, making it suitable for large datasets and mini-batch processing in training.

- NSA is evaluated across multiple tasks and datasets, and compared with established metrics (CKA and RTD).

### Weaknesses
__Figure 1__: all 3 plots in the left column are the same.

__Specificity assumptions:__ In section 4.1.1, the authors expect that the same layers of two networks trained on the same data and differing only in the initial weights should have high structural similarity. However, the actual layer in which similar features are learned may vary, particularly in ResNets (due to their residual connections). This is a well-known phenomenon: residual connections allow networks to adapt flexibly, enabling the model to skip certain layers or distribute features across them depending on initial weights and learning dynamics. See:

[1] Veit, A., Wilber, M. J., & Belongie, S. (2016). Residual networks behave like ensembles of relatively shallow networks. Advances in neural information processing systems, 29.

Thus, instead of showing a single example result in Figure 1, the authors would make a stronger case if they (i) reported the average across multiple instances of the same networks; and (ii) used multiple architectures and datasets.

__Equation 6__: for the units of LNSA to make sense, you should take the inverse again, after computing the mean of the inverses. That's what MacKay and Ghahramani actually do -- notice the -1 power in the formulas for their estimators ($\hat{m}^{-1}$). You can also check this on the source code they provided. In their Fig. 2, the best curves are: "the inverse of the average of the inverse m-hats (orange), and our preferred maximum likelihood estimator (which is just equation (7) again."

Having said that, I don't think you should compute the individual residuals using the Lid inverses. The residuals should keep their units of "dimension". How do the authors justify this?

__GNSA:__ I see a problem with this dissimilarity in that it can produce large values if the geometry of the manifold changes but the topology stays the same. A classic example where this would happen is for the "swiss roll" dataset (https://scikit-learn.org/1.5/auto_examples/manifold/plot_swissroll.html): the GNSA value comparing the original roll and its unrolled counterpart would be very large since, although the first several nearest neighbors of a point $i$ would not change their distances much, points that are far away (following along the spiral) would become considerably farther after flattening the roll. I believe this would lead to large GNSA even though the two manifolds are topologically identical. Have the authors considered this? If they agree, I suggest a more thorough discussion on strengths and weaknesses of GNSA.

__Lack of ground truth__: I believe this study would greatly benefit from using toy datasets that provide some ground truth to verify the efficacy of the method proposed. E.g., Gaussian clusters of various dimensionalities, the 1-D spiral, the 2-D S-curve, a plane with a hole; these have been classically used in the manifold learning literature. Here are a couple examples of recent papers that use interesting toy datasets as ground truth for comparing low-dimensional embeddings and dimensionality:

[2] Wang, Yingfan, et al. (2021) "Understanding how dimension reduction tools work: an empirical approach to deciphering t-SNE, UMAP, TriMAP, and PaCMAP for data visualization." Journal of Machine Learning Research 22.201: 1-73.

[3] Dyballa, L., & Zucker, S. W. (2023). IAN: Iterated Adaptive Neighborhoods for manifold learning and dimensionality estimation. Neural Computation, 35(3), 453-524.

It would be informative to have some simple, intuitive examples that could be directly visualized in 2 or 3 dimensions. Such datasets could be perturbed in ways that _did_ change their topology and structural relationships vs. others that _did not_, the goal being to check whether the values produced by LNSA and GNSA would reflect the truth.

### Questions
__Figure 1:__ assuming the values being plotted are means, how many tests were performed? What are their standard deviations? This is especially important since the data is being subsampled for the computations, and training seeds will produce different networks.

__Figure 3:__ same questions here with regards to whether the curves represent means. Stating how many repetitions and the standard deviations is important to understand the significance of these curves.

__Lines 324--328__: I had trouble understanding the sensitivity test. Although the notion of testing robustness to the removal of principal components makes perfect sense to me, it was not clear how the plots in Fig. 1 demonstrated, e.g., that "NSA is more sensitive to the removal of high variance PCs compared to RTD and CKA". Moreover, I'm not sure how to interpret the values for "detection threshold", especially since the values in the main text are different than those in the figure. What are the "baselines" mentioned in the plots' legends?

__Line 435:__ "the latent embeddings are then tested on their ability to predict the existence of links between nodes". How exactly are they tested on this? Are they used as inputs in another GCN? This wasn't clear to me.

In lines 197, 199, 272, surely the authors mean dissimilarity, not similarity (since they compute distances)? There are more instances throughout the paper where these metrics are called "similarities".

__Line 497:__ "We used a GCN along with four __robust__ GNN variants...". Why robust? Robust to what exactly?

__Line 500:__ "by introducing perturbations ranging from 5% to 25%". These percentages are w.r.t. what exactly? And what is the nature of these perturbations? Removing/changing links, nodes, or both?

__Minor points:__

- I found no pointer to Figure 3 in the main text.

- Line 493: "we applied NSA in the context of GNNs, but the method __can__ be equally effective in analyzing the robustness of other architectures". I recommend changing __can__ to "might", or "could", unless the authors have actually tested this empirically.

- Line 503: I recommend saying "the __original__ graph" instead of "the _clean_ graph".

### Soundness
2

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
The paper introduces a method (NSA) for comparing two data representations of the same dataset. NSA is a weighted sum with some tuned weights of GNSA which essentially compares the pairwise euclidian distances in the two representations of the same points, and of LNSA which is a local dissimilarity measure, based on k-NN graph. Experiments are described in order to empirically validate the expected properties of the method, although no access to the source code is provided.

### Strengths
-The paper addresses an interesting problem of constructing a reasonable measure of dissimilarity of two data representations of the same dataset. 

-Different experiments are described in order to empirically validate the method, although no source code is provided making reproducibility check difficult.

### Weaknesses
1.Dependence on Euclidean distance in high-dimensional spaces. NSA uses essentially the comparison of Euclidean distances as its measure of structural similarity. This choice can be suboptimal in high-dimensional spaces due to the "curse of dimensionality," which makes Euclidean distances less informative and can lead to unreliable similarity measurements.

2.An access to the source code is not provided making the paper results reproducibility check difficult.

3.Lack of universality without parameter tuning. NSA's performance across different tasks relies heavily on parameter tuning and specific integration with other loss functions.  The choice of k in the construction of k-nn graph is essential in the definition of LNSA. The weights in front of the local and global parts of NSA clearly lead to drastically different results depending on their values. 

4.No thorough guidance is provided for the choices and tuning of these hyperparameters. For example how to do 'appropriately adjusting the number of nearest neighbors considered in each mini-batch' on line 366 remains unspecified.

5.High computational complexity for large datasets. Despite claims of efficiency, NSA has a quadratic computational complexity concerning the number of data points, \( O(N^2 D + kND) \). This can become prohibitively expensive as the dataset size grows.

6.The method's focus on structural preservation might make it less effective in scenarios where functional similarity is more relevant, limiting its applicability.

7.Absence of interpretability mechanisms for practical applications. Although NSA provides a structural similarity measure, it lacks interpretability features that could make its outputs more useful in real-world applications. For instance, it does not offer insights into which specific features or dimensions contribute most to the observed structural discrepancies.

### Questions
Why an access to the source code was not provided for reproducibility check purposes?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce the Normalized Space Alignment (NSA) method for comparing two point clouds, which is based on comparing pairwise distances. The NSA consists of the local NSA, defined through the Local Intrinsic Dimensionality, and the global NSA, defined through Representational Similarity Matrices. The final NSA is defined as the weighted sum of global and local NSA. The experimental section includes experiments where NSA is used to analyze representations, as a loss in AE and for detection of adversarial attacks.

### Strengths
* Good background section on LID.
* Good applicability of the method.

### Weaknesses
General concerns:
* Despite a wide range of applications presented in the experimental section, the paper lacks comparison to relevant existing methods to really showcase the efficiency. For example, in the link prediction and adversarial attacks experiments, the method should be compared to the relevant baselines from the respective fields to be able to fairly judge the efficiency of the method.
* Datasets used in the experiments are small and basic, and the generalization of the method is questionable. How does the method behave for large sets and more complicated cases?
* No ablation studies are provided. For example, the method relies on the k nearest neighbors selection and I believe that the choice of k does influence the results. No experiments are provided on the robustness of k, neither is mentioned what k is actually used in the experiments. There is also no info on the balancing parameters l and g, and no ablation studies on the influence of these.
* The definition of GNSA depends on the choice of the origin. For example, given two point clouds X and Y, the translated point clouds will have the same structure but not the same GSNA score which is problematic. Of course one could resolve this with selecting a different origin but that is not feasible in practice. 
* Figures are not well readable.

### Questions
Specific comments:
* Doesn’t the computation of GNSA depend on the specific order of the point clouds? For example, comparing a_i and b_i only make sense if these below to the same datapoint, otherwise you’re comparing random elements. 
* In Sec 4.1 you claim that “a good structural similarity index should show high similarity between architecturally identical neural networks with different weight initializations”.  However, different initializations produce different models and there is no reason to assume that these should have the same structures. Also, in Figure 1 all the plots on the left are exactly the same. If this is not a typo, then I also don’t believe that the experiment shows what it is claimed. Additionally, the results here should be compared to the classical methods for comparing representations like Alaa et al, How Faithful is your Synthetic Data? Sample-level Metrics for Evaluating and Auditing Generative Models, Kynkäänniemi et al,  Improved precision and recall metric for assessing generative models, NeurIPS 2019, Poklukar et al, Delaunay Component Analysis, ICLR 2022, Khrulkov et al, Geometry score: A method for comparing generative adversarial networks, ICML 2018, etc, which are also missing from the related work.
* Please add details in 4.2.1. on how GSNA is even calculated. What is X and what is Y? 
* In Sec 4.3., I do not understand why an AE is used on top of the produced embeddings. In my view, a baseline should be the classification accuracy on the embeddings of the GCN or alternatively of a NSA-GCN trained model but not of a frozen GCN model with an AE attached to it. Also, as mentioned above, this experiment lacks comparison to any SOTA graph based methods which makes the applicability questionable.

### Soundness
3

### Presentation
3

### Contribution
2
