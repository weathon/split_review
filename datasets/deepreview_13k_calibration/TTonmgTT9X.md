# Fast Hyperboloid Decision Tree Algorithms

- Decision: Accept
- Avg Score: 6.60
- Scores: 8, 6, 8, 6, 5

## Abstract
Hyperbolic geometry is gaining traction in machine learning due to its capacity to effectively capture hierarchical structures in real-world data. Hyperbolic spaces,
where neighborhoods grow exponentially, offer substantial advantages and have consistently delivered state-of-the-art results across diverse applications. However, hyperbolic classifiers often grapple with computational challenges. Methods reliant on Riemannian optimization frequently exhibit sluggishness, stemming from the increased computational demands of operations on Riemannian manifolds. In response to these challenges, we present \hyperdt, a novel extension of decision tree algorithms into hyperbolic space. Crucially, \hyperdt eliminates the need for computationally intensive Riemannian optimization, numerically unstable exponential and logarithmic maps, or pairwise comparisons between points by leveraging inner products to adapt Euclidean decision tree algorithms to hyperbolic space. Our approach is conceptually straightforward and maintains constant-time decision complexity while mitigating the scalability issues inherent in high-dimensional Euclidean spaces. Building upon \hyperdt\ we introduce \hyperrf, a hyperbolic random forest model. Extensive benchmarking across diverse datasets underscores the superior performance of these models, providing a swift, precise, accurate, and user-friendly toolkit for hyperbolic data analysis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an extension of standard decision trees to the data situated in hyperbolic spaces. Certain types of data are better modeled by sets of recursive splits (decision trees), and also currently there is a growing attention to data analysis in hyperbolic spaces, due to development of hyperbolic embedding models. While there was HoroRF, a way to recursively split data in hyperbolic space, the proposed approach uses a different spliting model that is much simpler to operate and train, and this finding contains a valuable theoretical insight. Practically it also outperforms previously available methods.

### Strengths
The paper significantly advances the sub-field of decision tree models for hyperbolic spaces by presenting a novel decision tree model, that produces the splits in a different way, compared to previous state of the art, and leads to asymptotically faster computation times and better practical evaluation.

### Weaknesses
What is lacking in my opinion is a theoretical analysis of different decision boundaries and their performance for certain kinds of data (certain kinds of distributions of the data, that we may consider natural in certain classes of problems). For example, in case of regular decision trees, it may be observed that tabular data (where regular decision trees are best performers) is usually situated on axis-parallel hyperplanes and is easily separated by similar axis-parallel splits (due to naturally repeating nature / distribution of the data in tables along some dimensions)

The paper contains an interesting (and possibly simple to further analyze) case of synthetic data in hyperbolic space consisting of a sample from a mixture of Gaussians. It was observed empirically, that proposed method consistently outperforms the previous HoroRF/HoroDT. Providing a theoretical analysis of why it is the case would fill in the gaps and justify a choice of the proposed subset among all possible decision boundaries in hyperbolic space.

### Questions
- Considering the proposed method and HoroRF, we know two ways of splitting the hyperbolic space, which correspond to an inductive bias that we impose on the data. Are there any other inductive biases / splits that can be considered, but perhaps are currently infeasible or otherwise unsuitable?
- Particularly, there is an inherent asymmetry of the hyperbolic space towards the center of the Poincare ball - and embeddings usually automatically (without being instructed to do so, during regular optimization) utilize this asymmetry to represent well the hierarchical data. Can we use this asymmetry in designing the splitting method?
- Following from the previous question, consider the following baseline (should be worse than directly working in hyperbolic space, but better than the straightforward use of regular decision trees):
-- Transform the data into the Poincare ball. After that, ignore the hyperbolic nature of the data (as in regular decision trees) and transform the data into spherical coordinate system. Now run the regular decision tree on such data.
-- In this baseline the splits will be concentric spheres which are further split into spherical sectors and sub-sectors.
-- Would be nice to see a comparison between proposed approach and some approach (such as suggested above) that lies in between the Hyperbolic Trees and Regular Decision Trees.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a decision tree algorithm: HYPERDT. It leverages inner products to adapt Euclidean decision tree algorithms to hyperbolic space by characterizing Euclidean decision tree algorithms in terms of inner products, offering a natural modification of these algorithms to hyperbolic space. This approach works for all negative curvatures and eliminates the necessity for pairwise comparisons between data points. HYPERDT eliminates the need for computationally intensive Riemannian optimization, numerically unstable exponential and logarithmic maps, or pairwise comparisons between points by leveraging inner products to adapt Euclidean decision tree algorithms to hyperbolic space.

### Strengths
1. Novelty: The paper introduces a novel approach to decision tree algorithms by extending them into hyperbolic space. This is a new and innovative idea that has not been explored extensively in the machine learning community.

2. Performance: The authors demonstrate that hyperbolic decision trees and random forests can outperform their Euclidean counterparts in certain scenarios. This suggests that hyperbolic geometry has the potential to improve the performance of machine learning algorithms.

3. Clarity: The paper is well-written and easy to understand, even for readers who are not familiar with hyperbolic geometry. The authors provide clear explanations of the concepts and algorithms presented in the paper.

### Weaknesses
However, I have the following concerns:
1. All datasets seem to be better suited for the algorithm proposed by the authors. The authors do not provide the performance of the algorithm for other different types of datasets.
2. How about the deeper tree (T>3 or even 7)? 
3. What is the scalability of the algorithm? The author only tested the datasets of samples within 1000 and dimensions within 16. 
4. There are many other new decision tree training algorithms proposed these years. What is the performance of HYPERDT when compared with other advanced decision tree algorithms? (e.g., [1], [2])

### Questions
Please refer to Strengths and Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the task of creating decision tree models for hyperbolic data. To do so, the splitting rule for axis-aligned (parallel) splits is considered as the function of an inner product and thus a hyperplane. To translate decision trees to the hyperbolic geometry, the equivalent inner product and hyperplanes are used to define a hyperbolic decision boundary. This approach is utilized to create a random forest-style algorithm and is tested on various hyperbolic datasets.

### Strengths
- The visual presentation is very good. Figures 1 & 2 provide a nice intuition on how axis-align splits are generalized to the hyperbolic regime.
- The simplicity of the approaches mechanism for lifting decision trees to hyperbolic geometry allows for an efficient alternative than prior baselines (further explored in the experimental setting).
- Competitive empirical results showing its practicality.

### Weaknesses
 - Some sections on parameterizing decision boundaries are unclear. (See questions below)
- It maybe worth adding explicit clarification in the contributions that the data input for HyperDT are hyperbolic data / representations, ie, a separate embedding process is needed to apply such a model to Euclidean data.

### questions:
 "Parameterizing Decision Boundaries"

I find that the stated motivation and reasoning for Eq. (11) & (12) unclear. This further extends to the corresponding appendix sections:

- Language in the description of Eq. (11) seems imprecise. "... the hyperplane parameterized by $d$ and $\theta$ will intersect $\mathbb{H}^D$ at: [ Eq.(11)]". This seems to suggest there is only one point of intersection. I assume that the point characterized by Eq (11) is the closest point to the origin in said intersection? The lack of clarity here makes it difficult to understand the subsequent parameterization of the decision boundary. Specifically, it is not clear how the intersection point is used to define the geodesic.
- As a general suggestion, it may be useful to the reader to have both Eq. (7) and Eq. (11) in Figure 1. This would help clarify the relationship between the Euclidean and hyperbolic parameterizations.
- In the set up of Appendix A.2, a vector $\mathbf{u}$ is defined. It is unclear exactly what this is. From the combined definition in A.2.2 and Eq. (24), I believe that it is a unit vector pointing in a spacelike direction? What exact is its role? It is not clear how this vector contributes to the construction of the geodesic, and why it is necessary for defining the decision boundary.
- I am unsure how you went from Eq. (24) to Eqs. (25-27). From what I am guessing, $\mathbf{u}$ defines the direction of the intersecting geodesic, but I am unsure about the "\sinh" parameterization given. The connection between the vector $\mathbf{u}$ and the hyperbolic sine parameterization is not explicitly stated, making it difficult to follow the derivation.
- What is the connection between dimension $d'$ in Eq. (12) and the normal vector characeterization of Eq. (8/9)? It is unclear why the dimension $d'$ is introduced, and how it relates to the normal vector used to define the Euclidean hyperplane. This lack of clarity makes it difficult to understand the connection between the Euclidean and hyperbolic decision boundaries.

Other questions:

- Although the construction of the decision boundaries follows from their Euclidean axis-aligned counterparts, can the construction be generalized for any hyperplane (intersecting with the $\mathbb{H}^D$)? How would this change generating the decision boundary? Especially due to fact that the assumption of letting dimension except for 0 and d being zero is used to generate the hyperplane characterization. The restriction to axis-aligned hyperplanes seems limiting, and it is not clear how the method could be extended to more general hyperplanes.
- Following from the above, why is Eqs. (25-27) restricted to having the geodesic follow an axis $d'$? The restriction to a single axis $d'$ for the geodesic seems arbitrary, and it is not clear why this is necessary. It is not clear how the geodesic is parameterized in the general case.

Minor:
- Eq. (10), "cos" missing "\cos"

### Questions
"Parameterizing Decision Boundaries"

I find that the stated motivation and reasoning for Eq. (11) & (12) unclear. This further extends to the corresponding appendix sections:

- Language in the description of Eq. (11) seems imprecise. "... the hyperplane parameterized by $d$ and $\theta$ will intersect $\mathbb{H}^D$ at: [ Eq.(11)]". This seems to suggest there is only one point of intersection. I assume that the point characterized by Eq (11) is the closest point to the origin in said intersection?
- As a general suggestion, it may be useful to the reader to have both Eq. (7) and Eq. (11) in Figure 1.
- In the set up of Appendix A.2, a vector $\mathbf{u}$ is defined. It is unclear exactly what this is. From the combined definition in A.2.2 and Eq. (24), I believe that it is a unit vector pointing in a spacelike direction? What exact is its role?
- I am unsure how you went from Eq. (24) to Eqs. (25-27). From what I am guessing, $\mathbf{u}$ defines the direction of the intersecting geodesic, but I am unsure about the "\sinh" parameterization given.
- What is the connection between dimension $d'$ in Eq. (12) and the normal vector characeterization of Eq. (8/9)?

Other questions:

- Although the construction of the decision boundaries follows from their Euclidean axis-aligned counterparts, can the construction be generalized for any hyperplane (intersecting with the $\mathbb{H}^D$)? How would this change generating the decision boundary? Especially due to fact that the assumption of letting dimension except for 0 and d being zero is used to generate the hyperplane characterization.
- Following from the above, why is Eqs. (25-27) restricted to having the geodesic follow an axis $d'$?

Minor:
- Eq. (10), "cos" missing "\cos"

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a extension of traditional Euclidean decision tree algorithms to the hyperbolic space. The proposed method HyperDT is of constant-time decision complexity while mitigating the scalability issues of Euclidean decision tree. The paper further extends HyperDT to random forests tailored for hyperbolic space. The proposed methods HYPERDT and HYPERRF show state-of-the-art accuracy and speed on classification problems compared to existing counterparts on various datasets.

### Strengths
1) Extending decision tree to hyperbolic space is of great importance as both hyperbolic space and decision tree algorithm have their own advantages. 

2) The proposed method, compared with previous counterparts, maintains constant time decision complexity.

3) A implementation adhering to standard SCIKIT-LEARN API conventions.

4) The presentation and organization of the paper is overall good.

### Weaknesses
1) It is unclear why using geodesics as decision boundary is better than using horospheres as used in [1]. Specifically, the paper does not provide a rigorous justification for the choice of geodesics over horospheres in terms of their impact on the decision regions. While geodesics maintain convexity, the practical implications of this property for classification performance need further elaboration. The paper should include a more in-depth analysis of the trade-offs between these two types of decision boundaries, considering factors such as the complexity of the resulting decision regions and their ability to capture different types of data distributions.

2) Although the main goal is to generalzie decision tree to hyperbolic space, the paper lacks some comparisions agaist previous classification methods likes hyperbolic logistic regression and hyperbolic SVM. Without sush comparision, it is not clear whether the proposed hyperbolic decision tree has enough advantages compared with other classifiers. The paper should include a more comprehensive set of experiments that compare the performance of the proposed method against these alternative approaches. This comparison should not only focus on accuracy but also consider other factors such as training time, model complexity, and robustness to different types of datasets. Furthermore, the paper should analyze the specific scenarios where the proposed method outperforms or underperforms these alternatives, providing a more nuanced understanding of its strengths and weaknesses.

### Questions
Ref. Weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel extension of the Euclidean CART algorithm into the hyperbolic space, aptly named HyperDT. This extension involves a transformative shift from axis-aligned decision planes to geodesic submanifolds and replaces candidate thresholds with equidistance mid-angles. Notably, other components of HyperDT, including objective functions, remain consistent with the traditional CART framework. This adaptation allows HyperDT to achieve a similar asymptotic complexity as CART. Furthermore, the authors present another contribution in the form of HyperRF, a random forest model built upon the foundations of HyperDT. The paper showcases the good performance of these methods across a spectrum of datasets, including synthetic datasets like Gaussian mixtures, as well as real-world data sources such as biological sequences and graph embeddings. These empirical results underscore the effectiveness and versatility of the proposed techniques.

### Strengths
1. The utilization of a CART-like structure in the proposed methods greatly enhances efficiency, a feature that has been substantiated through a comparison with previous works like HoroRF.
    
2. The paper excels in presenting a lucid and methodical derivation of the proposed techniques. It ingeniously adapts Euclidean decision tree algorithms to the hyperbolic space by leveraging inner products. Additionally, the paper offers insightful closed-form equations for the decision boundaries and provides an in-depth explanation of the candidate hyperplane selection process.
    
3. Another notable aspect of the paper is its commitment to practicality. The authors have thoughtfully offered a Python implementation of the methods, aligning with the conventions of the scikit-learn API. This effort to bridge theory and practical application enhances the paper's value and accessibility to the research community.

### Weaknesses
My primary concerns are related to the CART-like design employed in the paper. As CART is known for its top-down, greedy approach, it tends to yield suboptimal solutions [1]. The proposed method, due to its inherent similarity to CART in its tree construction, will likely also suffer from this suboptimality. This is a significant concern, as the greedy nature of CART can lead to decision boundaries that are far from optimal, especially when dealing with complex data distributions in hyperbolic space. The authors should acknowledge this limitation and discuss its potential impact on the performance of HyperDT. For additional concerns, please refer to the questions section.

### Questions
1. In Section 3.2, the authors mentioned that the interpretation of axis-aligned hyperplanes within the hyperboloid model is unclear. Can the authors provide a more detailed explanation of why the use of axis-aligned hyperplanes lacks clarity in this context? I am considering that any geodesic could potentially be represented by two axis-aligned or oblique planes, making the use of axis-aligned planes reasonable.
    
2. Additionally, does the geodesic boundary offer advantages beyond classification scores and interpretation? One potential advantage I am considering is that geodesic trees may require fewer nodes compared to axis-aligned trees to achieve similar classification scores. Could the authors include metrics, such as the average number of nodes used in the experiments presented in Table 1, to support this claim?
    
3. For a more comprehensive evaluation, could the authors include additional comparison results? As mentioned in the weaknesses section, there are now several global optimization methods, such as [1], that have demonstrated superior performance compared to CART. It would be valuable to include a comparison with at least one of these methods to illustrate the superior performance of geodesic decision boundaries over axis-aligned boundaries.
    
4. Ablation experiments: The paper lacks ablation studies or experiments to justify the design choices made in the proposed methods, including the selection of candidate hyperplanes. Since the equidistance mid-angles in the proposed method do not have closed-form solutions and rely on numerical solvers, there may be concerns about the algorithm's efficiency. It would be informative to compare the performance and execution times of the equidistance mid-angles with those of naive mid-angles to assess the impact of these choices on the methods' performance and behavior.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
