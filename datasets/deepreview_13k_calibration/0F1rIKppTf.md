# Through the Looking Glass: Mirror Schrödinger Bridges

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Resampling from a target measure whose density is unknown is a fundamental problem in mathematical statistics and machine learning. A setting that dominates the machine learning literature consists of learning a map from an easy-to-sample prior, such as the Gaussian distribution, to a target measure. Under this model, samples from the prior are pushed forward to generate a new sample on the target measure, which is often difficult to sample from directly. In this paper, we propose a new model for conditional resampling called mirror Schrödinger bridges. Our key observation is that solving the Schrödinger bridge problem between a distribution and itself provides a natural way to produce new samples from conditional distributions, giving in-distribution variations of an input data point. We show how to efficiently solve this largely overlooked version of the Schrödinger bridge problem. We prove that our proposed method leads to significant algorithmic simplifications over existing alternatives, in addition to providing control over conditioning. Empirically, we demonstrate how these benefits can be leveraged to produce proximal samples in a number of application domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes mirror Schrodinger bridge (MSB), a model for conditional resampling. An alternating minimization procedure is used to solve for the MSB with a theoretical guarantee. On the empirical side, the MSB method is implemented to sample from both toy distributions and image distribution from the real world.

### Strengths
By using time-symmetry, MSB only requires a single neural network and half of the computational expense compared to other IPFP-based algorithms.

### Weaknesses
1. The theoretical results are limited to asymptotic analysis. The convergence rate is not presented; specifically, the analysis does not provide a bound on the number of iterations required to achieve a certain level of approximation error, which limits the practical applicability of the theoretical findings.
2. In the empirical evaluation, comparison to baseline methods is limited to the Gaussian example in Section 5.1. As a result, it's not clear how MSB compares to other methods in real-world image generation. The lack of comparison to established methods like diffusion models or other iterative probabilistic flow methods makes it difficult to assess the relative performance and advantages of MSB in complex, high-dimensional data scenarios.

### Questions
What's the connection and difference between the MSB method and the score-matching strategy (like Song et al. 2021)? What's the performance difference?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces the mirror Schrödinger bridge, a method for addressing the resampling problem when the initial and target distributions are identical. Unlike traditional Schrödinger bridges, which are designed for mapping between two distinct distributions, the mirror Schrödinger bridge is formulated specifically for self-mapping within a single distribution. This unique approach facilitates the generation of in-distribution variations of data points, allowing for conditional resampling that maintains the original distribution’s integrity.

The authors develop a theoretical foundation for this method, employing time symmetry and the Alternating Minimization Procedure to establish convergence in the total variation metric, even for infinite-dimensional state spaces. This achievement addresses the challenging issue of convergence in high-dimensional settings. Additionally, the algorithm capitalizes on the time symmetry inherent in the problem, enabling it to model the diffusion drift with a single neural network. This innovation significantly reduces computational costs, effectively halving the effort compared to Iterative Proportional Fitting Procedure based approaches.

Empirical evaluations underscore the practical value of the mirror Schrödinger bridge across diverse applications, highlighting its capability to produce high-quality proximal samples that are valuable for tasks like data augmentation and generative modeling. In summary, this research claims to provide a theoretically rigorous and computationally efficient solution for conditional resampling within the same distribution, combining solid theoretical contributions with practical algorithmic advancements.

### Strengths
The paper introduces the mirror Schrödinger bridge framework, an approach that differs from traditional Schrödinger bridges by focusing on mapping a distribution onto itself rather than between distinct distributions. This self-mapping approach directly addresses the challenge of conditional resampling within the same distribution, opening up new possibilities for generating in-distribution variations of data points. By incorporating time symmetry and the Alternating Minimization Procedure (AMP) to establish theoretical foundations, the paper presents an innovative solution to resampling. The algorithm also leverages time symmetry to train a single neural network for modeling the diffusion process drift, enhancing computational efficiency.

The paper includes solid theoretical foundations and provides comprehensive convergence proofs in the total variation metric, even in infinite-dimensional state spaces. The AMP is carefully developed and shown to converge to the mirror Schrödinger bridge, ensuring methodological consistency. The algorithm’s implementation is efficient, theoretically reducing computational overhead by half compared to Iterative Proportional Fitting Procedure (IPFP)-based methods. Empirical evaluations across several applications support some theoretical claims, demonstrating the method’s capability to generate high-quality proximal samples for tasks like data augmentation and generative modeling. The organized presentation of theoretical and empirical findings underscores the paper’s contribution to the field.

Additionally, the paper is well-written and structured, guiding the reader through complex concepts with clarity. The transition from theoretical foundations to practical algorithmic details is seamless, ensuring a coherent flow. Most definitions and problem formulations are clearly presented. Explanations of AMP and iterative schemes enhance understanding, while algorithmic pseudocode supports practical comprehension.

### Weaknesses
While the paper introduces mirror Schrödinger bridges, the framework retains substantial mathematical similarities to traditional Schrödinger bridges. Could you clarify the key mathematical distinctions between the two approaches? The theoretical analysis would benefit from an error analysis for the Alternating Minimization Procedure (AMP) outlined in equations (4) and (5), which would provide valuable insights into the convergence rate of the proposed approach. The absence of such an analysis limits our understanding of the efficiency and accuracy of the AMP.



On the practical side, the algorithm does not include comparisons with other established approaches in the literature, nor is there any discussion regarding the impact or choice of specific discretization methods, such as the Euler-Maruyama scheme, in addressing this problem. Furthermore, the paper lacks a detailed explanation of all the Figures, which hinders the reader's ability to assess how the proposed method performs relative to existing methods and to understand the extent to which halving the iterations reduces runtime quantitatively. 


The paper also lacks a quantitative flow for evaluating the equality of resampling across examples and fails to specify metrics used to assess performance. An empirical definition of "proximity" would add clarity. For instance, it is unclear whether a proximity value of 5 remains constant with $\sigma=1$ or changes to 3 with a different $\sigma$, and the way proximity is quantified in empirical examples remains vague. Although the paper claims validation across various application domains and provides some information on the experimental setup and datasets, it lacks sufficient detail on the specific metrics used for performance assessment, making it difficult to evaluate the method's effectiveness and robustness relative to existing techniques. 

Finally, while the paper emphasizes algorithmic simplifications that reduce computational costs by training only one neural network, it does not address the scalability of the method to high-dimensional data. The absence of any analysis on how the method performs as the data dimensionality increases leaves questions about its applicability to high-dimensional settings, which are increasingly relevant in practical applications.

### Questions
1. **Error Analysis for AMP**: The paper introduces the Alternating Minimization Procedure (AMP) in Equations (4) and (5) but lacks an error analysis. Could you elaborate on the convergence speed of AMP? Specifically, are there theoretical bounds or guarantees on the convergence rate that would enhance the theoretical foundation of your method?

2. **Benchmarking Against Existing Methods**: Could you clarify which algorithms you compared with your proposed method for each example case in Section 5? Benchmarking against established methods would help situate your approach within existing literature.

3. **Choice of Euler-Maruyama**: Your algorithm employs Euler-Maruyama discretization. How does this choice impact the accuracy and efficiency of solving the Schrödinger bridge problem? Have you considered alternative discretization schemes, and how do they compare in terms of performance?

4. **Iterations vs. Runtime**: How does halving the number of iterations quantitatively affect running time? A breakdown of runtime reductions relative to iteration count would provide a clearer picture of the efficiency gains.

5. **Quantitative Metrics and Proximity Definition**:
   - **Metrics for Resampling Quality**: The paper lacks specific metrics to assess resampling quality in each example case. What metrics do you use to evaluate how well the method preserves the integrity of the original distribution during resampling?
   - **Proximity Definition**: An empirical definition of proximity would clarify how closely generated samples align with input data. For example, on MNIST, how would a proximity value of a digit-5 image with \(\sigma=1\) compare to that of a digit-3 image with a different \(\sigma\)?

6. **Experimental Setup Details**: Although the paper claims empirical validation across various domains, the experimental setup lacks specificity. Could you provide more details on the datasets, experimental procedures, and metrics used to assess performance?

7. **Quantitative Results and Comparisons**: Could you include performance metrics and comparisons that demonstrate the robustness and potential advantages of mirror Schrödinger bridges over existing techniques?

8. **Scalability to High-Dimensional Data**:
   - **Performance on High-Dimensional Benchmarks**: The scalability of your method to high-dimensional data is not discussed. Could you provide insights into its performance and computational complexity on high-dimensional or large-scale datasets?
   - **Strategies for High-Dimensional Data**: What strategies do you propose to ensure the scalability and efficiency of mirror Schrödinger bridges when applied to high-dimensional data or data on manifolds? Are there modifications or optimizations that could improve performance in these scenarios?

9. **Interpretation of Figure 2**: In Figure 2, the resampling estimate with $\sigma=1$ appears to produce more concentrated samples compared to the original samples. Could you explain this behavior? Is there some form of geometric or manifold enhancement occurring in the resampling process?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies the Schrödinger bridge (SB) between a distribution and itself, unlike most of the literature which focuses on the SB between two distributions (e.g., the standard Gaussian, and the data distribution). The authors propose this model as a means for conditional resampling of a distribution, where the "noise" induced by the bridge process allows them to obtain new samples which are in-distribution. They demonstrate their approach on many experiments, and have some proofs of their technical results.

### Strengths
This paper proposes to alleviate some computation burden of training SBs by proposing a learning algorithm that learns the SB between a measure and itself. Still faithful to the generative modeling paradigm, they learn the SB from a data distribution to itself, with the goal of starting at existing samples and generating diverse ones. The writing is relatively clear, and Figure 2 is especially clear at describing the phenomenon of "starting from an existing sample" and, given enough noise, learns to go somewhere else in the distribution.

### Weaknesses
While the computational burden of having to train two neural networks instead of one is appealing, there is little comparison between MSB and DSB or DSBM in terms of quantifying sample versatility (they performed some comparisons in the Gaussian case, but these are far from conclusive). For instance, in Figure 3: is there a certain $\sigma_\star$ after which the data generated by the MSB changes classes? This is likely hard to prove theoretically, but knowing if there exists some threshold after which data stops being the same class would be very interesting.



### Questions
Comments:
- Line 053: maybe write what "\delta"-measure means (or just say Dirac measure).
- The paragraph just above figure 3 is very unclear. I'm not sure what the rows and columns are meant to refer to here..
- The ability to use one neural network is not surprising from the connection between EOT and the SB problem. Equation (24-25) in the work by Feydy et al. (2019) precisely proposes some kind of fixed-point equation on one potential function (whereas for entropic OT between two measures, there are typically two potentials to optimize over via the Sinkhorn algorithm)
- Question: Is there any hope to provide a *rule* for choosing the amount of noise added in the process of generating images?
- Question: The choice of OU process appears entirely arbitrary. Why not consider standard Brownian motion as the reference process?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors consider a modification to the original Schrödinger bridge problem where they consider the marginals to be the empirical measure of the data. This learns a coupling between two sets of the same data. The coupling is designed to optimal in the relative entropy sense. They modify the iterative proportional fitting procedure such that they project in the direction that minimizes the KL divergence in one step and then in the reverse KL divergence in the next step due to the analytical feasibility of the step. They propose a practical algorithm for computing the projections using a change of measure technique and optimizing the drifts.

### Strengths
The authors provide an interesting perspective on the Schrödinger bridge problem and provide a new technique for fitting a path measure connecting an initial condition given by itself to itself.

The method is fairly straightforward to implement and say to analyze.

The method provides optimality with respect to relative entropy, which is a nice property of the sample paths.

### Weaknesses
My main concerns come with the empirical evaluation of the method.

While the method has nice motivation, empirically the results do not seem to be impressive. In the cases of low \sigma, the variation is very small compared to the initial condition. This is likely because the method is estimating a map between itself that is effectively an OU process. Furthermore, when the $\sigma$ is large, the methods appear to be much more corrupt and lose some of the important features. The lack of significant variation in the low \sigma regime suggests the method might be overly constrained, essentially learning an identity mapping with slight perturbations. This behavior raises questions about the method's ability to capture meaningful transformations beyond simple noise addition. The corruption observed at high \sigma values indicates a potential instability or sensitivity to the parameter, which limits the practical applicability of the method across a range of noise levels. This also suggests that the method may not be robust to changes in the data distribution.

In general the performance of the method does not seem to be well studied. Since one of the motivations the authors mentioned was based on the path measure being optimal with respect to relative entropy, I would show some of these results on the regularity of the path space. The current evaluation lacks a rigorous analysis of the path measure's properties, particularly concerning its regularity. Without such analysis, the claim of optimality with respect to relative entropy remains somewhat abstract and lacks concrete empirical support. It is crucial to demonstrate that the method not only minimizes relative entropy but also produces path measures with desirable properties, such as smoothness or continuity. The absence of these results makes it difficult to assess the practical implications of the theoretical optimality.

### Questions
When training, how are the data split? Is there any pairing done between the data points? How would that affect the mapping between the two sets. 

Are there other mean reverting processes that you can consider other than OU processes? How do these affect the performance of the method?

Is there a set of results one can consider that consist of analyzing the regularity of the path measures?

### Soundness
3

### Presentation
3

### Contribution
2
