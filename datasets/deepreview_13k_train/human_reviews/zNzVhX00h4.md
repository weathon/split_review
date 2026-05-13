# Mildly Overparameterized ReLU Networks Have a Favorable Loss Landscape

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
We study the loss landscape of both shallow and deep, mildly overparameterized ReLU neural networks on a generic finite input dataset for the squared error loss. We show both by count and volume that most activation patterns correspond to parameter regions with no bad local minima. Furthermore, for one-dimensional input data, we show most activation regions realizable by the network contain a high dimensional set of global minima and no bad local minima. We experimentally confirm these results by finding a phase transition from most regions having full rank Jacobian to many regions having deficient rank depending on the amount of overparameterization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the optimization landscape of mildly over-parameterized 2-layer ReLU networks. By looking at the rank of Jacobian in different activation regions, the authors claim that for most activation regions there are no bad differentiable local minima.

### Strengths
- The theoretical finding of this paper is rigorous and interesting. It provides good insight on the optimization landscape of mildly overparameterized NNs. 
- The writing of this paper is easy to follow and the presentation is clear.

### Weaknesses
 - The assumption of 2-layer network with fixed last layer weights $v$ is restrictive and impractical. This limits the applicability of the theoretical results to real-world scenarios where the last layer weights are also optimized. Furthermore, fixing the last layer weights may significantly alter the optimization landscape compared to the case where they are also learned, potentially invalidating the conclusions drawn.
- The paper only discusses differentiable critical points, but there can be a lot of indifferentiable critical points depending on network settings. In fact generic deep ReLU networks with cross-entropy loss will have non-differentiable sub-optimal local minima [1]. This means that GD can still fall into bad non-differentiable local minima, even if the differentiable local minima are good. The analysis should consider the impact of these non-differentiable points on the optimization process. The presence of such points could lead to gradient descent getting stuck in regions with poor performance, even if the differentiable landscape is well-behaved. So it's still not clear to me that 'most of the landscape is favorable to optimization'.


### Questions
- Continued on bad local minima. It seems to me that in figure 9(b) GD does not converge to good local minima when network is only mildly overparameterized, despite at initialization the Jacobian has full rank. Can you explain this? Does this contradict your theoretical findings? 
- Numerical experiment. 
-- How do you determine whether a Jacobian matrix is full rank? 
-- For figure 9(a) is the network overparameterized at all? The experiment setting for figure 9 is not clear to me. Can you elaborate on this, just like what you did for other figures?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the loss landscape of two-layer ReLU networks. Following the observation that critical points where Jacobian is full rank are global minimizers, the authors show that most activation regions have no bad differentiable local minima. When the input is one-dimensional, they further proved that most regions contain a high-dimensional set of global minimizers. Experiments support that most regions of the loss landscape have full rank Jacobian in overparametrized networks.

### Strengths
-	Understanding the loss landscape of neural networks is a fundamental and important problem. This paper contributes a new angle by bounding the number of activation regions with no bad local minima.
-	The results are general as they are independent of specific choice of initialization of parameters or distribution of dataset.
-	The paper provides a rigorous definition for generic points using the fact that algebraic subset of $\mathbb{R}^n$ has measure 0. This method could be useful in various areas beyond studying landscape properties.

### Weaknesses
 - The setting described at the beginning of section 3 is different from a typical 2-layer ReLU network in that only one weight matrix is considered as parameters. It would be helpful to clarify whether including $v$ in the parameter space changes the conclusions in Theorem 5.
- While smooth critical points are global minima in most of the activation regions, it is not clear what the volume of these regions are. In particular, results in this paper do not rule out the possibility that the small number of regions with bad local minima make up most of the parameter space. Quantifying the size of the activation regions appears difficult since the setting considered is independent of the distribution of dataset.
- Despite interesting theoretical results, there is not much discussion on the implication on neural network training. As the authors also mention, this paper has not formalized how most regions having not bad local minima in their interior leads to gradient descent’s success in finding the global minima.

### Questions
-	The beginning of the second paragraph of section 6 states that a ReLU with one input with bias is equivalent to a ReLU with two input dimensions and no bias. Could the authors add a bit more explanation, as this equivalence does not seem straightforward?
-	Are the constants in the bound known? Can they be quantified in experiments?
-	This paper shows that most activation regions do not have bad local minima in their interior. Do there exist non-differentiable points that are local minimizers? If so, will these points cause problems for gradient descent?

### Soundness
3 good

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
This paper studies the loss landscape of the 1-hidden-layer ReLU network. The authors consider the partition of parameter space into different *activation regions*, defined by the activation patterns of ReLU neurons for different data points in the training dataset. 

1. Under mild overparameterization, Theorem 5 in Section 3 shows that almost all activation regions have the property that every differentiable critical point of the training loss (with nonzero 2nd layer weights) is a global minimum; i.e., "no bad local minima" holds for most regions.

2. However, not all activation regions are non-empty (i.e., the inequalities defining the region are feasible). Section 4 studies the number of non-empty activation regions. For the high-dim case of $d \geq n$, for data points in general position, Theorem 5 can be extended to "almost all *non-empty* activation regions" (Corollary 8)

3. The paper then discusses the case of one-dimensional input + bias, in which stronger statements can be shown. The authors show in Theorem 10 that almost all non-empty activation regions satisfy the "no bad local minima" property. Under a stronger assumption on the 2nd layer weights, Theorem 12 shows existence of an affine set of global minima in almost all non-empty activation regions.

4. Some discussions on function space and experiments are provided in Sections 6 and 7, respectively.

### Strengths
S1. The paper shows that most linear regions in the parameter space satisfy the desirable "no bad local minima" property, which agrees with practical observations with overparameterized networks. The proof techniques (especially the one employing random sign matrices) seem to be new in the literature.

S2. The paper is relatively well-written and easy to digest.

### Weaknesses
W1. Unfortunately, the scope of this paper looks rather limited. The paper studies a single-hidden-layer model and only the first layer $W$ is trained. Hence, given an activation region, the prediction $F$ is linear in $W$, which makes the Jacobian matrix constant in the region and it makes proofs much easier. For Sections 5-6, the authors show results specialized to one-dimensional input space. I question if these proof techniques could be extended to deeper networks and higher-dimensional input space. The extension to deeper networks, as suggested by the authors, requires the last hidden layer to be at least as wide as the number of data points $n$, which is a significantly stronger requirement than the $n/d_0$ condition in Theorem 5 for the two-layer case. This highlights a limitation in the applicability of their techniques to more practical deep network architectures.

W2. The paper only considers differentiable local minima, which misses the possible existence of non-differentiable local minima. In fact, Laurent & von Brecht (2018) show that in the hinge loss case, local minima can only occur at the non-differentiable boundaries except for flat regions. Is there any hope of including non-differentiable points into the analysis? While the authors attempt to address non-differentiable points, their analysis is limited to the one-dimensional input case. This significantly restricts the scope of their results, as the behavior of non-differentiable points in higher dimensions could be substantially different and more complex.

W3. Most results in the paper only prove that for most activation regions, "all critical points are global minima". If we take a closer look at it, the theorems do not talk about the existence of critical points in these regions; they may or may not exist. Therefore, the statements cannot rule out the following pathological scenario: critical points do not exist at all in the $1-\epsilon$ fraction of the linear regions and the $\epsilon$ fraction of the regions contain bad local minima. In order to make the results stronger, a more complete characterization of the existence of critical points should be helpful. The authors' attempt to address the existence of global minimizers is also limited to the one-dimensional input case, which again severely restricts the generalizability of their findings. The paper does not provide a convincing argument or analysis for the existence of critical points in higher dimensional input spaces.

W4. Some directly relevant citations are missing. [A, B, C] show the existence of bad local minima in ReLU networks and thus are directly relevant. [D] and some other papers by the same authors also consider the partition of parameter space with respect to the sign of pre-activations. I feel there should be more missing relevant papers, so please consider reviewing the literature again and updating the paper accordingly. Lastly, the citation to Safran & Shamir (2016) in page 1 should be corrected to Safran & Shamir (2018).

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a landscape analysis for the differentiable regions of the two-layer ReLU network and proves the absence of bad local minima under mild overparameterization level.

### Strengths
1. The paper provides a novel perspective for the landscape analysis of 2-layer NN, from a geometric and combinatoric point of view. The theoretical analysis looks solid.

2. Figure 2 and 3 clearly show that the theorems are validated by numerical simulations.

### Weaknesses
1. The theoretical contribution can be better contextualized by readers if authors can provide some clarification on their intuitions. See bullet points 1 and 3 in Questions. 

2. The key contribution, mild overparameterization level is only achieved for data of dimension 1. For the data with general dimension $d$ the counting method seems intractable. The authors are welcome to elaborate more on how to generate their analysis to high dimensional data or even deeper networks.

### Questions
1. I find it very difficult to follow the logic around Corollary 8: before Corollary 8, the authors claim that under general position assumption of the dataset and d larger than n, one can show that most activation regions are non-empty. However, Corollary 8 still focuses on the "non-empty activation regions". If most activation regions are indeed non-empty, why not drop the term "non-empty"? 

2. Among the related works being provided in the first section, can you compare your work with Liu (2021)? They seem to provide a stronger result.

3. When $d_0=1$, Theorem 5 already provides some strong results, why do we bother deriving Theorem 10?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
