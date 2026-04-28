# IMPROVING FLOW FIELD PREDICTION OF COMPLEX GEOMETRIES USING SIMPLE GEOMETRIES

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3

## Abstract
In this study, we address the challenge of computationally expensive simulations of complex geometries, which are crucial for modern engineering design processes. While neural network-based flow field predictions have been suggested, prior studies generally exclude complex geometries. Our objective is to enhance flow predictions around complex geometries, which may often be deconstructed into multiple single, simple bodies, by leveraging existing data on these simple geometry flow fields. Using a case study of tandem-airfoils, we introduce a method employing the directional integrated distance representation for multiple objects, a residual pre-training scheme based on the freestream condition as a physical prior, and a residual training scheme utilising smooth combinations of single airfoil flow fields, also capitalising on the freestream condition. To optimise memory usage during training in large domains and improve prediction performance, we decom- pose simulation domains into smaller sub-domains, each processed by a different network. Extensive experiments on four new tandem-airfoil datasets, comprising over 2000 fluid simulations, demonstrate that our proposed method and techniques effectively enhance tandem-airfoil prediction accuracy by up to 96%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a neural PDE approach for predicting CFD velocity fields around complex geometries using domain decomposition and blending techniques. The neural network is first pre-trained to predict the velocity field for a single geometry, and these predictions are then combined using a weighted approach for different velocity fields. Additionally, the method explores techniques to aid training, such as incorporating freestream velocity fields or leveraging pre-trained fields.

### Strengths
- The authors explore how to decompose the problem to enhance the current neural PDE method, which is a underexploited direction.
- The paper also introduces a new set of datasets, which would represent a valuable contribution to the community if made available as open-source.
- The method and process are presented with sufficient clarity to allow for a good understanding of the model.
- The method once again demonstrates the efficiency of gradually building results by incorporating prior information, such as freestream velocity fields or knowledge learned from simpler problems, like fields involving a single geometry.

### Weaknesses
 - The multi-NN approach is applied with a highly specific dependency, as illustrated in Fig. 3 (p. 6). It would be helpful to explain the rationale behind this dependency. Additionally, it appears that this dependency is closely tied to the geometric setting introduced in the paper. The authors should either discuss this as a limitation or specify the prior information required to determine this dependency.
- Please clarify how the features, including prior information (e.g., inlet velocity, DID) and previous predictions (e.g., front/back prediction), are input into the network. Specifically, the dimensionality and nature of the input features, and how they are concatenated or otherwise processed by the network, needs to be explicitly stated. The description should also clarify how the overlapping predictions are incorporated, including which nodes receive these inputs and how this varies across the different sub-networks.
- Recently, some works have addressed the challenges of complex geometry and domain decomposition, such as Mao et al. (2024). I suggest that the authors include a discussion of these studies.

### Questions
See Weaknesses for questions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a method to improve flow field prediction in complex geometries by leveraging a decomposition into simpler ones, specifically for tandem-airfoil configurations. The core idea of the framework is to train two neural networks, one to predict the flow field around individual airfoils, and the second one to predict the flow field around the tandem airfoil (i.e. the combination of the two). The authors adopt a two-step straining approach, where they first train the network on simple geometries and then train the network on the more complex ones. In both cases, the models are formulated with a residual approach, i.e. the output is expressed as $U= U_{est} + U$. In the first step, $U_{est} = U_{\infty}$ and in the second step $U_{est} = \tilde{U}$, where   $\tilde{U}$ is the smooth combination of the two predictions of the first model. The authors detail a multi-NN inference procedure to predict the flow field successively at the front, back, upper, lower regions before predicting the final predictions. This helps reduce memory needs. They train the models on 4 different datasets that encompass varying Reynolds and angle of attack (AoA) configurations.

### Strengths
* The method is targeted at a relevant engineering application, with tandem airfoils being common in aerospace and maritime engineering.
* The residual and domain decomposition techniques effectively improve performance consistently (table 3 and table 4).
* The multi-NN inference slightly helps to increase accuracy (table 4)
* The method definitely improves over the mesh graphnet baseline on the more challenging Random cruise setting (table 5).

### Weaknesses
 * The approach combines existing techniques, such as SV and DID features, pre-training, residual learning, and domain decomposition. However, the paper reads more like a catalog of these techniques rather than a cohesive, novel framework, and the overall technical contribution is weak.

* The paper lacks a clear explanation of the smooth-combining method’s validity. For example, would we expect to get an interpolating weight such as the one described by Figure 2 or is it surprising ? 

* The proposed techniques are computationally intensive at inference, particularly with 18 seconds required for geometric feature computation and 9 seconds for smooth-combining, limiting their practical applicability compared to standard solvers.

### Questions
* Could you compare the smooth-combining method to a simple linear interpolation weighted by the distance to each airfoil? What makes smooth-combining preferable, or why might it make more sense in this context?

* Why is it necessary to compute a single DID for both objects simultaneously? Would it be feasible to calculate a DID for each object independently and use these two as separate inputs instead of a combined one?

* How sensitive is the overall training procedure to the hyperparameters used at each stage? Some insights into this sensitivity could clarify stability and robustness.

* Given the multi-network setup with separate neural networks for each domain part, does this pipeline increase the risk of overfitting, particularly when applied to each sub-domain individually?

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
4

### Summary
Using a neural network that has been pre-trained on single-airfoil flow fields, the authors generate flow fields for double-airfoil configurations. The neural network for predicting flow around two airfoils is initialized with weights from the simple-geometry network. The quantity of interest is the velocity magnitude. Visual comparisons and error analysis with reference to the ground truth (i.e., CFD solution) are made.

### Strengths
The motivation of this paper is really appreciated and they approached a very important and interesting problem in CFD. They explained everything in detail. The quality of the figures is good. Training time and complexity of the network in terms of a number of trainable parameters are given. The procedure of data generation is explained in detail as well.

### Weaknesses
1. This manuscript contains fundamental wrong assumptions about fluid mechanics. I am afraid that the authors are not familiar with the Navier-Stokes equations.

2. The equation 1 does not make sense at all from a physics point of view. How do you justify that from this perspective? Please recall that fluid dynamics is not just a photo that can be easily merged.

3. I disagree with the following statement from the manuscript:
... which suggests that the in fluence of a solid body within a flow field can be conceptualised as deviation from the freestream, Hence, employing weights based on these deviations creates a combined field that effectively preserves the influences of both airfoils, resulting in a close estimate. 

4. The five steps described on page 6 do not make sense.

5. This is unsatisfying that the authors first present Alg 1. Later they claim that Alg 1 does not work for some cases, and then the authors proposed Alg 2.

6. The framework predicts only the magnitude of the velocity in 2D, which is not, indeed, a useful quantity in CFD. Instead, we are interested in the velocity component in the x and y directions and the pressure.

### Questions
1. The authors claim that the Reynolds number is equal to 500. Hence, the flow is unsteady, in principle. However, in the result, we do not see any time dependency. Did they use RANS or any other averaging method?! This has been totally missed in the manuscript. 

2. There is a lot of effort to predict the flow around two airfoils from the solution obtained for one airfoil. The main question is:  Why not simply train the network from scratch for two or three airfoils? Nowadays, neural networks are able to do so and there is no limitation in looking at the literature. Perhaps, the authors wanted to support their claims that their network is able to predict the solution for complex geometries from simple geometries. However, having two airfoils at a relatively large distance is not really a complicated geometric domain.

3. What if we reduce the distance between the two airfoils (referring to Fig. 5 in the manuscript)? Additionally, how would increasing the angle of attack impact the flow prediction? These changes lead to secondary flow, even in the steady-state regime. The question is can the network predict this scenario accurately?

### Soundness
2

### Presentation
2

### Contribution
1
