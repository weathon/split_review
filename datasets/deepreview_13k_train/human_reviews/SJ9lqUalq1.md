# $\gamma$-Orthogonalized Tensor Deflation: Towards Robust \& Interpretable Tensor Decomposition in the Presence of Correlated Components

- Decision: Reject
- Scores: 5, 8, 5, 3

## Abstract
We tackle the problem of recovering a low-rank tensor signal with possibly correlated components from a random noisy tensor, or the so-called \textit{spiked tensor model}. When the underlying components are orthogonal, they can be recovered efficiently using \textit{tensor deflation}, while correlated components may alter the tensor deflation mechanism, thereby preventing efficient recovery. 
Relying on recently developed tools from random tensor theory, we deal precisely with the non-orthogonal case by deriving an asymptotic analysis of a \textit{parameterized} deflation procedure, which we refer to as $\gamma$-orthogonalized tensor deflation. 
Based on this analysis, an efficient tensor deflation algorithm is proposed by optimizing the parameter injected into the deflation mechanism, which in turn is proven to be optimal by construction for the studied tensor model. We perform a detailed theoretical and algorithmic analysis on the rank-2 order-3 model, and outline a general structure to tackle the problem in more generality for arbitrary ranks/orders, aiming to lead to a broader impact in machine learning and beyond.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenge of recovering a low-rank tensor signal with potentially correlated components from a random noisy tensor, which is known as the spiked tensor model. The authors propose a solution for the non-orthogonal case using a parameterized deflation procedure, referred to as γ-orthogonalized tensor deflation. Then an efficient tensor deflation algorithm is introduced, which optimizes the parameter used in the deflation mechanism. In addition, this paper provides a detailed theoretical analysis for the case of rank-2 order-3 tensor model and suggests a general structure for handling the problem for arbitrary rank/order tensors. These findings aim to have a broader impact in machine learning and beyond.

### Strengths
1. The article uses the newly proposed random tensor theory and tensor deflation method to solve the spiked tensor recovery problem when the signal components are $\gamma$-orthogonal. Basically, the proposed method has a wider range of practicality.
2. A series of numerical experiments are conducted to verify the applicability of the proposed method in different situations.

### Weaknesses
1. According to the presented analysis, expanding this method to rank-$r$ and higher-order situations seems to be very cumbersome. Although the authors state that symbolic solvers can be used to solve such higher-order and higher-rank problems, it could be beneficial to provide some more details for the readers to follow. Specifically, the paper lacks a clear explanation of how the parameterized deflation procedure scales with increasing rank and order. The computational complexity of solving the resulting optimization problems for higher-order tensors is not discussed in sufficient detail, making it difficult to assess the practical applicability of the proposed method beyond the rank-2 order-3 case. A more thorough discussion of the challenges and potential solutions for higher-dimensional tensor recovery is needed.
2. There are many figures in the text, but there are few related explanations. More explanations should be added to make such figures to be more meaningful. For example, the figures often lack detailed captions explaining the axes, data representation, and the specific insights they are intended to convey. Without sufficient context, the reader struggles to understand the significance of the presented results. The figures should be self-contained and clearly illustrate the theoretical and experimental findings.
3. The authors put too much stuff in the supplementary materials, which is not conducive for the readers' reading. For example, the proposed algorithms should be placed in the main text. The core algorithmic steps, including the optimization procedure for the deflation parameter, should be presented in the main body of the paper. Moving these essential components to the supplementary material hinders the reader's ability to follow the methodology and evaluate its effectiveness. This separation makes it difficult to understand the core contribution of the paper without constantly referring to external documents.
4. The introduction of the numerical experiments should be more detailed, such as how the simulated data is generated. The description of the data generation process is too brief, lacking crucial details about the specific distributions used, the parameter settings, and the noise model. This lack of detail makes it difficult to reproduce the experiments and verify the results. A more thorough explanation of the experimental setup, including the specific choices made for data generation, is necessary to ensure the validity and reproducibility of the findings.

### Questions
See the weaknesses above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper deals with low rank tensor recovery under the spike model. The paper particularly focuses on a scheme named "deflation" which calculates leading singular value / vectors one by one and deflates the original tensor, i.e. subtracts the outer product of the calculated top vector times singular value. In a matrix scenario (order = 2) this method is rather straightforward, because singular vectors are orthogonal. In tensors (order >=3) orthogonality is not always satisfied. This makes deflation more challenging. This is the topic the paper addresses. The paper treats the case order=3, rank=2 in details and outlines the schema for higher order and ranks.

### Strengths
Paper addresses a very interesting and challenging question. While a series of papers have studies the rank-1 (PCA) problem for tensors, the higher rank estimation problem comes with its own challenges, mostly due to orthogonality and the deflation scheme that authors discuss here. 
Authors provide an algorithm which is backed by random tensor theory. Authors also provide numerical simulations that prove that the theoretical asymptotics are alined with empirical (finite n) values. 
Authors outline how to generalize their results to more complex scenarios. 
The works presentation is self-contained and well referenced, which makes it accessible to a wide audience, despite the topic's technicality.

### Weaknesses
Given how cumbersome notations and formalism get when working with tensors, it always helps to make simplifying assumptions to prove your point in the smallest yet representative case. Authors have done a pretty good job at it here, while I could still imagine simpler problem formulations. Two suggestions / questions below.

### Questions
1. Why did you not consider a (simpler) symmetric case where u=v=w for simplifying notations and exposing the main results more easily?
2. Did you try to express the optimization problem in gamma as an objective function minimization problem? Can the problem benefit a joint optimization in both singular value / vectors and gamma?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the tensor decomposition problem on the spiked tensor model. A novel $\gamma$-Orthogonalized Tensor Deflation that extends from the standard deflation is proposed. A random tensor theory analysis has been established for the proposed algorithm on a rank-2 case. Numerical results are aligned with the theory.

### Strengths
The paper has solid analytic results, and the proof seems overall correct (I didn't check too carefully). The numerical results on synthetic data seem convictive.

### Weaknesses
The paper is poorly presented, messily organized, and hard to follow. It seems the authors just put everything together at the last minute. The writing style of each paper component is not consistent. A complete polish must be done before the paper can be published.

Experiments on real-world applications are needed to further establish the empirical performance of the proposed method.

### Questions
See weakness

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider the problem of finding the components of the expansion of a tensor with noise into a sum of rank-one tensors. In fact, only the case of rank-2 order-3 model is considered. Emphasis is placed on the so-called non-orthogonal case when the components are correlated. For this case, the paper propose an algorithm containing the parameter $\gamma$ for the sequential construction of the desired decomposition. This parameter $\gamma$ is chosen adaptively by repeatedly running the algorithm. Asymptotics of the decomposition parameters are given as a theoretical analysis. A small number of numerical examples on synthetic data are given.

### Strengths
- Robust algorithm of tensor decomposition is build and analyzed for narrow specific case (rank-2 order-3 CP tensor with noise).

### Weaknesses
 - The writing style leaves a lot to be desired as the text is quite hard to read. The narrative is non-linear, many important things for understanding are put in the Appendix, even the notations. Section 3.2 MAIN ALGORITHM SKETCH, where the essence of the underlying algorithm is revealed, is overflowing with links to Appendix.

- The paper is widely cited following paper (Seddik et al, 2021), so it is difficult to understand what the current paper is about without reading the cited paper.

- The most important weakness, in my opinion, is too few experiments that have been conducted only on synthetic data. In general, experimental section 4 is very short, subsections 4.2 and 4.3 consist of only figures. Thus, it is not clear at all the relevance of this paper, where practically the presented results can be applied.

- Neither is there any comparison with other existing methods.

- Only rank-2 order-3 model is considered, which significantly reduces the breadth of application of the method and, as a consequence, its practical value.

### Questions
- Weighted sum of 1-rank tensors is called CANDECOMP/PARAFAC tensor Decomposition (CP) and there is quite a large theoretical basis for it. Have you used or compared with other existing approaches for approximate tensor construction in CP?

- Can your work be extended to other tensor decompositions such as Tensor Train (TT), Tucker and others?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
