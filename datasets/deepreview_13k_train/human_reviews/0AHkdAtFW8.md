# Sum-of-Squares Programming for Ma-Trudinger-Wang Regularity of Optimal Transport Maps

- Decision: Reject
- Scores: 6, 6, 6, 5, 5

## Abstract
For a given ground cost, approximating the Monge optimal transport map that pushes forward a given probability measure onto another has become a staple in several modern machine learning algorithms. The fourth-order Ma-Trudinger-Wang (MTW) tensor associated with this ground cost function provides a notion of curvature in optimal transport. The non-negativity of this tensor plays a crucial role for establishing continuity for the Monge optimal transport map. It is, however, generally difficult to analytically verify this condition for any given ground cost. To expand the class of cost functions for which MTW non-negativity can be verified, we propose a provably correct computational approach which provides certificates of non-negativity for the MTW tensor using Sum-of-Squares (SOS) programming. We further show that our SOS technique can also be used to compute an inner approximation of the region where MTW non-negativity holds. We apply our proposed SOS programming method to several practical ground cost functions to approximate the regions of regularity of their corresponding optimal transport maps.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a computational approach using Sum-of-Squares (SOS) programming to verify and approximate regions of regularity for optimal transport maps, specifically focusing on the Ma-Trudinger-Wang (MTW) tensor. Regularity of optimal transport maps is critical in many machine learning applications, and this regularity can be assured by the non-negativity of the MTW tensor. However, verifying this condition analytically for general cost functions is challenging. The authors propose using SOS programming to generate certificates of non-negativity for the MTW tensor across a broader range of cost functions, potentially providing computationally verified regions of regularity. Their method is applied to both verifying non-negativity conditions (the "forward problem") and to computing inner approximations of regularity regions (the "inverse problem") for several ground cost functions, demonstrating the effectiveness of SOS programming in this context. This computational framework contributes a systematic approach to certifying regularity in optimal transport, potentially facilitating its application in various machine learning tasks. The paper concludes by applying the proposed framework to several common examples in the literature.

### Strengths
The paper’s strength lies in its innovative application of Sum-of-Squares (SOS) programming to address the longstanding challenge of verifying the regularity of optimal transport (OT) maps through the Ma-Trudinger-Wang (MTW) tensor. SOS programming is a well-established tool in optimization and control, but this work extends it to OT regularity, opening new possibilities for computational verification of the MTW conditions in general cases where analytic approaches are intractable. The paper also showcases the practical efficacy of the approach by applying it to various cost functions, demonstrating its flexibility and adaptability across different scenarios.

### Weaknesses
A missing key aspect in the paper is the time complexity analysis for the proposed framework. What's the computational efficiency of SOS programming in verifying regularity of the different OT problems? While the authors showcase the method’s application to specific examples and shared the wall-clock time, a time complexity discussion could be a good addition to the paper. Specifically, the paper lacks a detailed analysis of how the computational cost scales with the problem size, such as the dimension of the input space and the degree of the polynomial approximations used in the SOS program. This is crucial for understanding the practical applicability of the method to larger and more complex optimal transport problems. Furthermore, the paper should discuss the limitations of using off-the-shelf SDP solvers for the SOS programs, as these solvers do not exploit the specific structure of the problem, which could lead to suboptimal performance. A more in-depth analysis of the computational bottlenecks and potential strategies for improving efficiency, such as exploiting sparsity or problem-specific structure, would be beneficial.

### Questions
1. What are some other regularity verification methods? how does the SOS programming compare to them in terms of accuracy and efficiency?

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
4

### Summary
The paper presents a sum-of-squares programming based approach to verifying the Ma-Trudinger-Wang (MTW) condition. Precisely, both the forward problem of identifying if a given cost function and domains satisfy the MTW condition and the inverse problem of finding the largest semialgebraic domain on which the MTW condition holds are considered. The corresponding problems can be solved via standard SOS solvers on modest hardware. The paper concludes with a numerical study which validates the theoretical findings.

### Strengths
To my knowledge, this is the first paper which explores the question of numerically verifying the MTW condition. The paper is overall written well, and the theoretical details look correct.

### Weaknesses
The limitation of the paper regards the assumption that the cost function is rational or that the elements of the MTW tensor are rational. While the authors provide some examples, it remains unclear how restrictive this assumption is in practice. Specifically, it would be beneficial to have a more thorough discussion of the types of cost functions that are excluded by this assumption, and whether these excluded cases are common in applications. For instance, are there well-known cost functions used in optimal transport that would not be amenable to this approach? Further, the paper could benefit from a more detailed analysis of the approximation error introduced when a non-rational cost function is approximated by a rational one. The paper also does not fully explore the implications of this work. While the authors mention the connection to regularity of the optimal transport map, the practical impact of numerically verifying the MTW condition is not fully fleshed out. It is not clear how this verification would be used in practice, or what advantages it would provide in the context of solving optimal transport problems.

### Questions
My main question pertains to how the authors see this work fitting within the broader optimal transport literature. In effect, though some results require regularity of the optimal transport map to hold, these results typically pertain to questions of statistical estimation. In these settings, population measures are estimated based on samples and so (i) absolute continuity cannot be verified a priori, (ii) upper and lower bounds for the density cannot be verified, and (iii) the support of the distributions are unknown. It is thus unclear to me how the content of the current paper fits within the previous context.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors propose the first computational approach to certify the regularity of the Monge map for optimal transport problems with specific conditions on the transport cost and the state spaces. To be more precise, they evaluate the non-negativity of the fourth-order Ma-Trudinger-Wang (MTW) tensor associated to the transport cost, which has been proved to be a sufficient condition to establish the continuity of the Monge transport map under proper conditions on the marginals of the transport plan. In this work, they consider three versions of this non-negativity condition, previously considered by related works. Their method consists in reformulating the MTW condition (for each of the three versions) into a sum-of-squares program defined on a semialgebraic setvia Putinar's Positivstellansatz, which can then be solved with efficient software. In particular, their approach assumes that the transport cost (or at least the corresponding MTW tensor) is a rational function defined over a two-state semialgebraic space (or at least, a two-state space that contains a semialgebraic space). They apply their framework to verify if the transport cost verifies the MTW condition or to find the largest semialgebraic set on which the transport cost verifies the MTW condition. They propose several convincing numeric experiments in small dimension for a large variety of non-trivial transport costs.

### Strengths
- Although I am no expert of SOS programming, the paper is well written so that it can be read by a large audience. In particular, the notation is easy to understand and Section 2 provides the most essential theoretical elements from OT and SOS programming domains to introduce the method.
- Given the elements of Section 2, the idea of proving the MTW non negativity via SOS programming seems to be a very good (and natural) idea. This work seems to be the first to answer this question with relatively moderate theoretical and computational frameworks.
- The formulation of the inverse problem is very interesting and once again well introduced and explained.
- The diversity of numerical experiments (i.e. non trivial transport costs) definitely proves the theoretical statements.

### Weaknesses
 - As it seems crucial to apply SOS programming, the transformation of the non-negativity condition into a SOS representation in Equation (8) would deserve more explanation, in the appendix for example. For non expert readers, this relation is hard to understand. Specifically, the paper does not clearly articulate the connection between the non-negativity of a polynomial and its representation as a sum of squares, which is a critical step in their methodology. The assumption that non-negativity can be directly translated into a sum-of-squares program via Putinar's Positivstellansatz needs more justification, especially for readers not deeply familiar with real algebraic geometry. The paper should clarify the conditions under which this equivalence holds, and how it is ensured in the context of their problem.
- The dimension of the numerical experiments is relatively low, while OT aims at solving large-scale problems. While the authors demonstrate their approach on several non-trivial transport costs, the spatial dimensions considered are quite limited. This raises concerns about the scalability of the proposed method to higher-dimensional problems, which are common in real-world applications of optimal transport. The paper should discuss the computational complexity of their approach with respect to the problem dimension and provide some analysis of the expected performance for larger-scale problems. It would be beneficial to see some experiments in higher dimensions, even if they are computationally intensive, to provide a better understanding of the practical limitations of the method.
- Although the problem tackled in this paper is interesting from a theoretical perspective, I am quite concerned by the effective application of this work to OT problems. The paper does not sufficiently address the practical implications of verifying the MTW condition for real-world optimal transport problems. While the theoretical contribution is clear, the paper lacks a discussion on how the proposed method can be integrated into existing OT algorithms or how it can lead to more efficient or accurate solutions for practical applications. The connection between the regularity of the Monge map and the performance of numerical OT algorithms is not clearly established, leaving the reader wondering about the practical value of this work.

### Questions
- Could you please provide examples of real-world OT applications where the knowledge of the regularity of the Monge map is crucial ?
- Could you please bring more details on the equivalence between non-negativity on polynomial terms and SOS representation ?
- I think it would be of interest to provide the results on the regularity of the Monge transport map given the three types of non-negativity conditions given in the paper.
- Have you considered experiments with higher dimension ? Is there any computational burden ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In the context of OT, the fourth-order Ma-TrudingerWang (MTW) tensor associated with this ground cost function provides a notion
of curvature. The non-negativity of this tensor plays a crucial role for establishing continuity for the Monge optimal transport map. In general, it is difficult to analytically verify this condition for any given ground cost. This paper proposes a provably correct computational approach which provides certificates of non-negativity for the MTW tensor using Sum-of-Squares (SOS) programming. The authors further show that their SOS technique can also be used to compute an inner approximation of the region where MTW non-negativity holds. They apply this proposed SOS programming method to several practical ground cost functions to approximate the regions of regularity of the corresponding OT maps. They also evaluate the proposed SOS computational framework for both the forward and the inverse problems.

### Strengths
This is a mathematically solid paper and resolve an interesting theoretical problem. It proposes a provably correct computational framework that can certify or falsify the non-negativity of the MTW tensor associated with a given ground cost under the assumptions that the ground cost is a rational and semialgebraic function. The proposed approach is based on sum-of-squares (SOS) programming and can be of independent interests. The authors also demonstrate that the proposed computational framework can be applied to non-rational ground cost function given that the elements of the MTW tensor are rational and can be used to solve the inverse problem.

### Weaknesses
The main concern is that this paper seems irrelevant to the ICLR community. In practice, the common ground cost function would be Euclidean and I am not really sure if it is practically important to conduct the computational verification of OT regularity for a general class of non-Euclidean ground cost functions. I encourage the authors to elaborate on potential ML applications or benefits of their work on non-Euclidean optimal transport. For example, would you like to discuss how your method could enhance practical ML systems that use OT, or to provide concrete examples of where non-Euclidean costs arise in ML problems?

Another concern is the poor quality of writing. In particular, there are many advanced mathematical notations, such as semialgebraic functions and Archimedean sets, which are not accessible to the ICLR audience. Both Section 2 and Section 3 are written in a technical way without sufficient intuitive explanations or examples alongside the formal mathematical notation. In my humble opinion, the major contribution of the paper would be the SOS formulations for computing the MTW tensors, which is certainly nontrivial, but this paper would much better fit the applied mathematics oriented journal.

### Questions
1. I encourage the authors to elaborate on potential ML applications or benefits of their work on non-Euclidean optimal transport. For example, would you like to discuss how your method could enhance practical ML systems that use OT, or to provide concrete examples of where non-Euclidean costs arise in ML problems? 

2. I encourage the authors to improve accessibility of technical parts (e.g., the description of forward problems and inverse problems), such as adding more intuitive explanations or examples alongside the formal mathematical notation.

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a computational method for assessing the regularity structure of optimal transport plans. Specifically, the source and target distribution are continuous distributions on a manifold, the cost is some smooth function, and the regularity in question is the regularity of the pushforward map from source to target distributions. In addition, the computational tool computes the region where the MTW holds.

### Strengths
1. The paper presents an under-studied aspect of regularity of Monte map. Moreover, the paper contains numerical algorithm and is practical.
2. The inverse problem is well thought through. 
3. The numerics seems promising for a relatively difficult problem in OT.

### Weaknesses
1. While it is not an issue for the author per se, it is unfortunate that the SOS condition only applies to semialgebraic sets for the manifold. 

2. The writing doesn't seem to include sufficient focus on the gap between the non-negativity condition and the SOS counterpart. It doesn't seem to be clear whether SOS is too strong for this case. Specifically, the paper does not adequately address the potential for the SOS relaxation to miss regions where the non-negativity condition holds, but the SOS condition does not. This is a crucial point, as it directly impacts the reliability of the computational tool.

3. The presentation is not clear for this paper. For example, the indicting convention for something like $c_{ij, p}$ is quite confusing. The only mention of $c_{ij, kl}$ in the earlier part is too far away, and the readers can not be expected to find where the notation is and also generalize from $c_{ij, kl}$ to $c_{ij, p}$. This is too confusing for this conference.

4. Theorem 5 seems currently wrong: the function $F$ in (5) is matrix-valued. It doesn't seem correct to somehow assess if this matrix-valued rational function belongs to \sum_{SOS}[x, y]. *Unless this issue is either resolved or explained, this reviewer cannot increase the score above the acceptance threshold.*

5. The author doesn't seem to use certain terms in differentiable geometry correctly. For x, y on different points of $\mathcal{M}$, one cannot directly apply an "inner product"/contraction between the tangent plane on $x$ and the contingent plane of $y$. This issue is resolved, however, if $\mathcal{M}$ is a subset of $\R^{n'}$ and the differentiable structure comes from the Euclidean space. The author is advised to change the writing on this and make sure no further major mistake such as this is made.

Minor comments:
- The logic at line 293 is wrong: \eta(\xi) = 0 should belong to after \forall.

### Questions
1. The manuscript doesn't contain (A) a discussion on the computational complexity for checking the NNCC condition and the two types of MTW conditions. Also, the discussion on (B) the complexity of the inverse problem is missing. For (A), the author is advised to provide an analysis. For (B), the author is advised to also provide a runtime in the work, i.e. the time it takes to plot the figures.

2. What is the relationship between Monge OT map (which is Borel) and a Brenier map (which is point to point)? Is regularity of Brenier map, supposing it exists, also something that this formulation can answer?

### Soundness
3

### Presentation
2

### Contribution
3
