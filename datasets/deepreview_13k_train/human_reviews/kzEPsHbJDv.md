# One for all and all for one: Efficient computation of partial Wasserstein distances on the line

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Partial Wasserstein helps overcoming some of the limitations of Optimal Transport when the distributions at stake differ in mass, contain noise or outliers or exhibit mass mismatches across distribution modes.
We introduce PAWL, a novel algorithm designed to efficiently compute exact PArtial Wasserstein distances on the Line. PAWL not only solves the partial transportation problem for a specified amount of mass to be transported, but _for all_ admissible mass amounts. This flexibility is valuable for machine learning tasks where the level of noise is uncertain and may need to be determined through cross-validation, for example. 
By achieving $O(n \log n)$ time complexity for the partial 1-Wasserstein problem on the line, it enables practical applications with large scale datasets. 
Additionally, we introduce a novel slicing strategy tailored to Partial Wasserstein, which does not permit transporting mass between outliers or noisy data points. Through empirical evaluations on both synthetic and real-world datasets, we demonstrate the advantages of PAWL in terms of computational efficiency and performance in downstream tasks, outperforming existing (sliced) Partial Optimal Transport techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper discusses a novel algorithm and a slicing scheme to efficiently compute PArtial Wasserstein distances on a Line (PAWL) under L1 (Manhattan) cost  which is a variant of the linear assignment problem in $O(nlogn)$. The concept of "chains" that are specific patterns formed by the samples on the real line is introduced which enable fast computation of partial Wasserstein distances requiring a sorting operation as precomputation enabling fast computation of marginal and cumulative costs (sums). Authors develop a sliced partial Wasserstein (sliced-PW) scheme to enable sparse approx transport maps thus allowing identification of outliers (OOD samples) without requiring prior knowledge of the amount of noise/outliers. The proposed algorithm is then used in two applications - Wasserstein gradient flow and point cloud registration

### Strengths
- Extends several prior theoretical results to meaningfully solve partial 1-Wasserstein problem on line
- Introduces concept of chains and efficient way to calcualte marginal/cumualitve sums of cost for chains using precomputing step in O(nlogn)
- Designed scheme sliced-PW for using PAWL in real world applications like gradient flow and point cloud registration

### Weaknesses
 - More thorough experimental evaluation would be great
- Applications to PU learning or outlier detection might be a good fit
- Might not be friendly to backpropagation algorithm limiting use in context of deep learning / neural nets

### Questions
- Can you suggest some other applications and extensions for PAWL?
- Is the algorithm usable in training neural net architectures? What is the notion of gradient in this case?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces PAWL (PArtial Wasserstein on the Line), an efficient algorithm for computing partial Wasserstein distances in one-dimensional distributions. The primary motivation is to improve the performance of optimal transport (OT) in scenarios where input distributions contain noise, outliers, or mass mismatches. PAWL enables exact partial transportation, computing solutions for all possible transported mass amounts simultaneously with an optimal time complexity of O(nlogn), making it suitable for large-scale applications. 
Experiments confirm PAWL's computational efficiency and demonstrate its advantages in gradient flows and point cloud registration tasks.

### Strengths
* Paper is very-well written and clear
* Paper proposes a novel algorithm for efficiently calculating the partial 1-D Wasserstein on the lines in $O(nlogn)$

### Weaknesses
 * The proposed algorithm requires the supports of two measures having the same weight. This setup might limit the application of the proposed algorithm i.e., the proposed algorithm seems to work well only for point clouds.

* The sliced partial Wasserstein is defined based on SWGG, however, it is still possible to define many other variants of sliced partial Wasserstein by using more projections

* There is no experiment for testing the robustness of the proposed methods and other baselines.

* The application seems to be limited to low-dimension i.e., <= 3.

### Questions
* I would like to investigate the effectiveness of the proposed method in higher-dimensional experiments and settings.
* How does PAWL ensure efficiency when managing the candidate list of pairs in each step, especially as the list grows with larger datasets?
* What mechanisms are in place to handle cases where multiple candidate pairs have nearly identical marginal costs?
When several pairs have similar transport costs, selecting the best pair could become computationally challenging or introduce instability

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new algorithm to solve partial Wasserstein distance on the line which achieves the optimal complexity i.e., $\mathcal{O}(n\log n $ for $n$ is the number of supports. The key idea is to choose the best candidate set at each step of the algorithm. With the new algorithm to solve 1D partial Wasserstein, the paper proposes a new semi-metric named sliced partial Wasserstein which selects the projecting direction yielding the minimal transport cost under the lifted partial transportation plan. The paper shows that PAWL (the new algorithm) leads to faster computation than the previous unbalanced approach including optimal transport transport (OPT) and fast unbalanced optimal transport (Fast-UOT).  The paper conducts experiments in gradient flow and point cloud registration to show the efficiency of the proposed method.

### Strengths
* The paper addresses an important question in the community which is having a partial Wasserstein variant with the complexity of $\mathcal{O}(n\log n)$. Therefore, the proposed variant  can scale to more than 10000 supports.

* The proposed solution is novel including constructing and maintaining a candidacy set.

*  PAWL shows a favorable performance in computation, gradient flows, and point cloud registration compared to existing unbalanced optimal transport solver.

### Weaknesses
 1. **Regarding Complexity**:
   - 1.1 If the cost is not based on the Manhattan distance, the computational complexity of the new algorithm is \( k \cdot n^2 \). In the worst-case scenario (when \( k = n \)), this becomes \( n^3 \). Is this correct?
   - 1.2 In Section 5.1 and Figure 4, it seems the authors discuss only cases where the cost is a metric. I recommend the following:
     - (a) Include **(Sato et al., 2020)** as a baseline. The two baselines from **(Bai et al., 2023)** and **(Sejourne et al., 2023)** apply when the cost is not a metric, while Sato's method and the algorithm proposed in this paper are specifically designed for metric costs. In the one-dimensional metric cost scenario, Sato's algorithm appears to have a comparable computational cost of \( n \log^2 n \).
     - (b) Upon reviewing the anonymized repository (specifically `timing_partial.py`), it seems that only the extreme case of full mass transportation has been tested. I recommend measuring the wall-clock time for various mass transport settings, such as transporting 20%, 50%, and 100% of the total mass.
   - 1.3 In Section 5.1, the parameters for fast UOT are set as \( \rho_1 = \rho_2 = 1.0 \), and for OPT, \( \lambda = 0.001 \times \text{median} \). However, it appears that the parameter for PAWL (denoted as \( s \)) is missing, as I could not find it in the code repository. Could you clarify the missing parameter and explain why the resulting problems are equivalent or comparable under these settings?

2. **Regarding the Semi-Metric Properties of Sliced-PW**: When \( \text{sliced-PW}(\mu, \nu; k \cdot \omega) = 0 \), it implies \( \mu^k = \nu^k \), but we cannot conclude that \( \mu = \nu \) (see lines 998–1002 in the appendix). Therefore, sliced-PW does not satisfy the triangle inequality or identity properties, though it does exhibit symmetry and non-negativity. It appears that sliced-PW was not applied in the experiments, and its potential applications were neither discussed nor demonstrated.


Minor comments: 
It appears that the proposed algorithm primarily addresses cases where $\mu$ and $\nu$ are empirical measures with equal mass on each point. If this is the case, setting $\omega = 1$ makes the equations for (PAWL) and classical partial OT, i.e., Eq (PW), equivalent. Therefore, introducing the new problem (PAWL)  seems unnecessary, as it merely changes the notation of the original partial OT problem. (This comment is only about notation redundancy and does not affect my overall rating.)

### Questions
* Could elbow variant provide the true contamination percentage when the data contains additive noise?

* How could we extend the proposed approach to continuous cases and cases where measures do not having the same weight for their supports?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1. The paper presents a new algorithm for solving the partial Wasserstein problem in a straightforward manner.
2. It introduces the concept of sliced-partial Wasserstein and discusses its semi-metric properties.
3. The new algorithm is applied to shape registration experiments, and an evaluation of its performance is provided.

### Strengths
1. The classical solver for the proposed partial optimal transport (OT) problem requires $O(n^3)$ complexity for linear programming or $O(n^2 / \epsilon)$ for the Sinkhorn algorithm. This paper proposes an efficient algorithm specifically for the Manhattan distance in a one-dimensional, empirical distribution setting.  
2. The sliced-partial Wasserstein (sliced-PW) concept is introduced, and its semi-metric properties are analyzed.  
3. The authors demonstrate the application of this new algorithm in a shape registration experiment.

### Weaknesses
1. **Regarding Complexity**:
   - 1.1 If the cost is not based on the Manhattan distance, the computational complexity of the new algorithm is \( k \cdot n^2 \). In the worst-case scenario (when \( k = n \)), this becomes \( n^3 \). Is this correct?
   - 1.2 In Section 5.1 and Figure 4, it seems the authors discuss only cases where the cost is a metric. I recommend the following:
     - (a) Include **(Sato et al., 2020)** as a baseline. The two baselines from **(Bai et al., 2023)** and **(Sejourne et al., 2023)** apply when the cost is not a metric, while Sato's method and the algorithm proposed in this paper are specifically designed for metric costs. In the one-dimensional metric cost scenario, Sato's algorithm appears to have a comparable computational cost of \( n \log^2 n \).
     - (b) Upon reviewing the anonymized repository (specifically `timing_partial.py`), it seems that only the extreme case of full mass transportation has been tested. I recommend measuring the wall-clock time for various mass transport settings, such as transporting 20%, 50%, and 100% of the total mass.
   - 1.3 In Section 5.1, the parameters for fast UOT are set as \( \rho_1 = \rho_2 = 1.0 \), and for OPT, \( \lambda = 0.001 \times \text{median} \). However, it appears that the parameter for PAWL (denoted as \( s \)) is missing, as I could not find it in the code repository. Could you clarify the missing parameter and explain why the resulting problems are equivalent or comparable under these settings?

2. **Regarding the Semi-Metric Properties of Sliced-PW**: When \( \text{sliced-PW}(\mu, \nu; k \cdot \omega) = 0 \), it implies \( \mu^k = \nu^k \), but we cannot conclude that \( \mu = \nu \) (see lines 998–1002 in the appendix). Therefore, sliced-PW does not satisfy the triangle inequality or identity properties, though it does exhibit symmetry and non-negativity. It appears that sliced-PW was not applied in the experiments, and its potential applications were neither discussed nor demonstrated.


Minor comments: 
It appears that the proposed algorithm primarily addresses cases where $\mu$ and $\nu$ are empirical measures with equal mass on each point. If this is the case, setting $\omega = 1$ makes the equations for (PAWL) and classical partial OT, i.e., Eq (PW), equivalent. Therefore, introducing the new problem (PAWL)  seems unnecessary, as it merely changes the notation of the original partial OT problem. (This comment is only about notation redundancy and does not affect my overall rating.)

### Questions
1. In the 1D case, what is the difference between "Manhattan distance" and basic absolute distance?  
2. In the repository `repo/baselines/cvpr_2023_bai.icp_xp.py`, it appears that all the baseline methods are not accelerated by Numba; however, Numba acceleration is implemented in the original repository at [yikun-baio/sliced_opt](https://github.com/yikun-baio/sliced_opt). Could you test the convergence time using the original code from [yikun-baio/sliced_opt](https://github.com/yikun-baio/sliced_opt)?  
3. Can you provide a formal proposition/theorem (with a formal proof) to present the proposed solver's computational cost for solving a partial Wasserstein problem, both with and without the Manhattan metric assumption?
4. Could you print the transportation plan for the new algorithm in the following partial OT problem?

Let \(\mu = \delta_{x_1} + \delta_{x_2} + \delta_{x_3}\), where \(x_1 = 0\), \(x_2 = 1\), \(x_3 = 2\) (with support on points 0, 1, 2, and each point having a mass of 1), and \(\nu = \delta_{y_1} + \delta_{y_2} + \delta_{y_3}\), where \(y_1 = 2\), \(y_2 = 3\), \(y_3 = 4\) (with support on points 2, 3, 4, and each point having a mass of 1). 

The transported mass is set to \(k = s = 3\), with \(w = 1\). The cost function can be either the Manhattan distance or the square of the Manhattan distance. When using the squared distance, the optimal transportation plan is \(x_1 \rightarrow y_1\), \(x_2 \rightarrow y_2\), and \(x_3 \rightarrow y_3\). I am curious to see the outcome of this new algorithm.

### Soundness
2

### Presentation
2

### Contribution
3
