# Rapid Grassmannian Averaging with Chebyshev Polynomials

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
We propose new algorithms to efficiently average a collection of points on a Grassmannian manifold in both the centralized and decentralized settings. Grassmannian points are used ubiquitously in machine learning, computer vision, and signal processing to represent data through (often low-dimensional) subspaces. While averaging these points is crucial to many tasks (especially in the decentralized setting), existing methods unfortunately remain computationally expensive due to the non-Euclidean geometry of the manifold. Our proposed algorithms, Rapid Grassmannian Averaging (RGrAv) and Decentralized Rapid Grassmannian Averaging (DRGrAv), overcome this challenge by leveraging the spectral structure of the problem to rapidly compute an average using only small matrix multiplications and QR factorizations. We provide a theoretical guarantee of optimality and present numerical experiments which demonstrate that our algorithms outperform state-of-the-art methods in providing high accuracy solutions in minimal time. Additional experiments showcase the versatility of our algorithms to tasks such as $K$-means clustering on video motion data, establishing RGrAv and DRGrAv as powerful tools for generic Grassmannian averaging

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the problem of computing the induced arithmetic mean of subspaces (points on the Grassmannian manifold). The authors focus on a decentralized setting where each agent has limited data and restricted communication with its neighbors. Their approach is based on spectral analysis of the associated optimization problem, resulting in a power-method-like algorithm. The utility of the method is demonstrated through synthetic experiments and an application to clustering video motion data via Grassmannian K-means clustering.

### Strengths
- The paper addresses an interesting problem and is generally well-written, presenting the proposed approach clearly, though it occasionally lacks detail.
- The authors prove that Chebyshev polynomials are optimal for their modified power method.
- Their experiments demonstrate that the algorithm outperforms competing methods in synthetic Grassmannian averaging and K-means clustering of subspaces spanned by video sequences for motion clustering. They have also successfully adapted related methods (such as DeEPCA) to the problem of Grassmannian averaging, which can be seen as part of their contribution.
- The authors provide code that implements the proposed approach and reproduces the experiments presented in the paper (although I have not tested the code).

### Weaknesses
1. Importance of Decentralized Grassmannian Averaging: The paper emphasizes the importance of decentralized averaging, which the authors claim is significant. However, the paper does not provide concrete examples where decentralization is essential and demonstrates it only through a single set of synthetic experiments (emulating a decentralized setup). The motivation for decentralization is weak; the paper should provide compelling examples where centralized computation is infeasible or undesirable, such as scenarios with massive datasets that cannot fit on a single machine, privacy concerns that prevent data aggregation, or real-time processing on edge devices with limited communication bandwidth. The current examples do not adequately justify the need for a decentralized approach.

2. Comparison and Relation to Existing Literature: How does RGrAv compare or relate to existing methods, such as block power methods (e.g., Chebyshev-Davidson, spectral filtering) or other similar approaches? Given that the problem in Eq. (1) is reduced to a spectral problem in Section 3.1, a more thorough exploration of relevant methods, both centralized and decentralized, would be beneficial. The paper should discuss the computational trade-offs between RGrAv and existing methods, especially in terms of convergence rate, memory requirements, and communication overhead. A more detailed analysis of how RGrAv's performance compares to methods like Chebyshev-Davidson, particularly in the context of decentralized computation, is needed. (I am not an expert in this area, but there appears to be relevant literature available.)

3. Need for Additional Explanations: While the paper is overall well-written, certain choices or statements would benefit from further explanation or justification. I was able to understand some of these upon reflection, while others remain unclear. For example:
  - Section 3.1: The definition of the optimization problem (1) and the equivalent spectral perspective are presented very densley, without references, which could be difficult for readers unfamiliar with the topic. For instance, why is (1) invariant to the choice of representatives $[U_m]$? Why is the projection on the K largest eigenvectors $[V]$ the minimizer of (1)? Additional explanations or citations would be helpful. The connection to Procrustes problems should be explicitly stated and explained.
  - Section 3.2: What is average consensus (AC)? Without prior knowledge, the proposed procedure is unclear. Why can’t AC be used directly to approximate (1)? Most importantly, why is it sufficient to approximate the lower dimensional $PX$? In what way does this guarantee an approximation of $P$? The paper should clarify that the non-convexity of the Grassmannian manifold prevents direct application of AC and that the lower-dimensional approximation is sufficient because the power method only requires matrix-vector products.
  - Section 4.1: How are the optimal polynomials $f_t$ used to recover the space $U$? This is again central to the approach, but is challenging to understand. Theorem 1 proves the optimality of $f_t$ in the sense of Eq. (2), but in what sense does this translate to the optimality of the approximate average space $[U]$? The paper should explain how the polynomial transformation effectively cancels out trailing eigenvalues, focusing the computation on the leading eigenvectors. The connection to noise cancellation should be made explicit.
  - Section 4.2: "fortunately, $f_t$ is well-approximated in terms of $f_{t-1}^*$ and $f_{t-2}^*$, in what sense does this hold? Is it an experimental observation or is there a theoretical justification? The paper should clarify that this is an empirical observation, and that while Figure 1 provides visual support, a more rigorous justification is needed.

4. Experimental Results Are Limited:
  - The experiments in Section 5.1 focus on the decentralized setting and raise a few questions:
    - In these experiments, DRGrAv is "sub-optimally tuned" (Line 353) while parameters for other methods are carefully tuned through parameter search (commendable effort). How would DRGrAv perform if optimally tuned? The paper should acknowledge that optimally tuning DRGrAv is not practical but that the current approach provides a more realistic comparison.
    - The experiments are conducted for a single setup (M,N,K)=(64,150,30) with two types of agent connectivity (hypercube and cycle). Is this setup representative? The paper should justify the choice of this specific setup and discuss its limitations. The paper should also include experiments with varying values of M, N, and K to assess the robustness of the method.
    - Are similar results obtained against competitive methods in different setups?
    - Is this a setup where decentralization is necessary or preferable? How would DRGrAv perform compared to competitors in a scenario with very large M or N, where decentralization is crucial? Additional experiments supporting the importance and benefits of the proposed approach for decentralized averaging would significantly strengthen the manuscript, given that this is a primary focus of the paper. The paper should include experiments that demonstrate the scalability of DRGrAv in scenarios where decentralization is essential.

  - The experiment in Section 5.2 uses Grassmannian averaging to define Grassmannian K-means for motion clustering in videos. The authors present only timing results but do not include any assessment of clustering quality for each method. The statement that "the four averaging algorithms produce clusters with similar quality across various values for K  (these results are not shown for brevity)" is unclear. Showing these results alongside runtime comparisons seems essential for evaluating each method's overall effectiveness. These results could be briefly mentioned in the main text and detailed in the appendix if space is limited. Does RGrAv produce the same results as Flag? How does RGrAv compare to the block power method, ground truth IAM? Does the spectrum gap assumption (Section 4.1) hold in these experiments? The paper should include a detailed analysis of clustering quality, comparing RGrAv to other methods, and address the validity of the spectrum gap assumption.

  - The evidence for a performance advantage is somewhat limited. The decentralized results in Section 5.1 are comparable to DeEPCA, while the centralized results in Section 5.2 are closely followed by the block power method. The paper should provide more compelling evidence of RGrAv's superiority over existing methods, especially in scenarios where its advantages are most pronounced.

### Questions
Additional issues and questions:
- Eq. 1: It would be good to add parantheses to clarify whether summation includes $UU^T$ to avoid potential confusion.
- Could you elaborate on the connection between Theorem 1 and the equioscillation theorem? Would this reproduce the best polynomial approximation of the step function?
- Please explain how the DeEPCA algorithm is adapted for decentralized Grassmannian averaging.
- Line 172: Unrolling the power method loop—could you clarify if this is straightforward or requires further justification?
- Line 198: Are you assuming that $\alpha$ and $\beta$ are known?
- Figure 1: Please elaborate on what is shown and its significance. Additionally, Figure 1 is not referenced in the main text.
- Line 264: "focuses on minimizing the error in the gradient tracking procedure" — please provide more details.
- Table 1: Are these results obtained under the hypercube or cycle setup?
- Line 438: How is the true IAM average computed? Could you include timing for this computation as well?
- Section 5.2: Please clarify that this experiment does not test the decentralized algorithm.
- $\alpha$ is used as a bound on eigenvalues in Section 4 and later as a step size parameter in Section 5, which could be confusing. Please consider revising this notation.

Additional minor issues:
- Line 51: "subsequent projections may be applied locally thereafter)." - could you please elaborate?
- Line 62: "We demonstrate merit through a theoretical guarantee on the optimality" - Theorem 1 proves optimality of the choice for the polynomial $f_t$. Does this guarantee the optimality of your approach? In what sense?
- Line 72: Define Grassmannian and Stiefel manifolds, as these terms and notations are introduced here for the first time.
- line 377: What is the parameter $\rho$?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method for computing the average of some subspaces in the standard and decentralized setting.

### Strengths
omitted.

### Weaknesses
 - The contribution at the technical level is incremental, in my opinion. Theorem 1 seems to be a basic variant of the known result for Chebyshev polynomials. The only difference seems to be that the paper adds an extra constraint $f_t(0)=0$.

- The assumption on the dual-banded spectrum is also not new. This assumption is used in the AISTATS 2022 paper: Super-Acceleration with Cyclical Step-sizes (https://proceedings.mlr.press/v151/goujaud22a/goujaud22a.pdf); see Eq. 3 there. That paper has a much deeper exploration of related aspects than the present manuscript. If NeurIPS holds the same high standard, the lack of technical depth forms a ground for rejection.

- From a practical viewpoint, the proposed method performs similarly to the baselines it compares, and there is no significant advantage in terms of acceleration or efficiency, as shown in Section 5.1

The above two points suggest Lines 60 - 62 are never-before-seen overstatements: "*Our algorithms operate similarly to the famous power method, with the distinction that Chebyshev polynomials are employed to leverage a “dual-banded” property of the problem in order to achieve never-before-seen efficiency in computation and communication.*"

- The algorithm listings (Algorithms 1 and 2) are highly repeated.
- Section 5.2 is disconnected from the prior sections of the paper, which puts emphasis on the decentralized setting. From Section 1 to Section 5.1 there is no mention of k-means clustering.

### Questions
omitted.

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
The paper provides a fast algorithm for computing a particular average on the Grassmann manifold. The algorithm is, in essence, a variant of the classic power iteration, which is tailored for projection matrices (which can, in turn, be used to represent points on the Grassmannian). The algorithm is suitable for decentralized computations, making it easy to scale across machines. Empirical results show that the algorithm is faster than a selection of baseline algorithms while providing comparable results.

### Strengths
The paper observes that the eigenvalues of projection matrices have a particular structure, which can be exploited to build a more efficient variant of the power iteration to compute eigenvalues/vectors. As far as I can tell, this contribution is novel and is potentially more widely applicable than explored in the submitted paper.

The paper is generally well-written and easy to understand.

The developed algorithm is shown to be easy to extend to a decentralized implementation. This is a quite nice practical property.

### Weaknesses
My main concern with the paper is the studied problem. The paper states that points on the Grassmann manifold are "used ubiquitously in machine learning, computer vision, and signal processing". It is true that some years ago (before deep learning took off), some work went into using subspaces (and hence Grassmannians) to represent batches of data. This approach has, however, not caught on and is quite rare today.

I do not want to argue that a paper is uninteresting because it explores a (current) niche approach. However, I consider it problematic that the paper does not demonstrate that the problem of study is relevant to solve. The paper demonstrates that the proposed algorithm is faster than alternatives, but it fails to demonstrate that the algorithm computes a quantity of interest. I would consider the paper significantly more interesting if it was demonstrated that Grassmann Averaging is useful for solving real tasks.

Some further minor comments:
* It seems to me that Theorem 1 is more generally applicable than just computing Grassmann averages. If this understanding is correct, it would have been valuable to have pointers in such directions.
* I miss references to early work on using Grassmann Averages to define principal components of data: "Grassmann Averages for Scalable Robust PCA", CVPR 2014. This relies on a crude chordal-like metric.
* While I appreciate that many algorithms are provided in the paper, I miss general explanations of what these algorithms do. On a first reading, it can be difficult to read an algorithm, so I would have appreciated more hand-holding.

### Questions
1. Can you clarify what is meant by "QR" in the first equation of Sec. 3.3? I know the QR decomposition, but this generally returns *two* values (the Q and the R matrices). In the text, only a single matrix is returned, so it would be good to clarify if this was Q or R.
2. Can you provide a citation for "StableQR"?
3. In the last experiment, you compute a Frechet mean, but use the chordal distance. Isn't the Frechet mean defined according to the geodesic distance? Can you clarify what is actually being done here?

### Soundness
4

### Presentation
3

### Contribution
2
