# A Structured Matrix Method for Nonequispaced Neural Operators

- Decision: Reject
- Scores: 8, 8, 5

## Abstract
The computational efficiency of many neural operators, widely used for learning solutions of PDEs, relies on the fast Fourier transform (FFT) for performing spectral computations. However, as FFT is limited to equispaced (rectangular) grids, this limits the efficiency of such neural operators when applied to problems where the input and output functions need to be processed on general non-equispaced point distributions. We address this issue by proposing a novel method that leverages batch matrix multiplications to efficiently construct Vandermonde-structured matrices and compute forward and inverse transforms, on arbitrarily distributed points. An efficient implementation of such *structured matrix methods* is coupled with existing neural operator models to allow the processing of data on arbitrary non-equispaced distributions of points. With extensive empirical evaluation, we demonstrate that the proposed method allows one to extend neural operators to very general point distributions with significant gains in training speed over baselines,  while retaining or improving accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a generalisation of the Fourier and Spherical Fourier Neural Operators to arbitrary point clouds. The paper is fairly well-written, and generalises these methods to arbitrary grids via the utilisation of Vandermonde matrices and quadrature on unstructured grids. The authors apply this approach to a range of examples and provide good empirical evidence for the effectiveness of the method. I wish that the authors had stressed more that this is essentially the realisation of FNO/SFNO on arbitrary grids, something that the literature has promised but never delivered so far. As such, I believe that this paper is valuable to the community.

### Strengths
* The paper is well-written and well-motivated. The literature review is sufficient and mostly achieves to put the method into perspective (See my remarks in the Questions section)
* The authors address an interesting gap in the literature: the formulation of FNOs on arbitrary grids. To the best of my knowledge, this has been discussed in the literature, but has not been applied in practice.
* Ample benchmarks are provided

### Weaknesses
 * The experimental results and the result tables would benefit from additional information (See my remarks)
* The text in the results section is a bit misleading and makes it sound as if the proposed method outperforms FNO and SFNO on the regular grid. If I understand correctly, this is the method on the irregular grid, which requires an interpolation step.
* It would have been better if the provided metrics were put into context by showing the approximation results of the vanilla FNO/SFNO methods on their respective grids. This would provide a good baseline both for timing and performance results.
* The given setting would allow to test operators tested on another grid to be evaluated on this unstructured grids. As I imagine this to be one of the main applications of this method, I would have like to see such results.
* Classical methods typically can not perform arbitrarily well on unstructured grids. I expect the same to be true here as the projection will have quadrature errors and you won't be able to evaluate the integrals to high accuracy on arbitrary grids. Have you performed any analysis on how sensitive results are to the choice of collocation points? It would be good to mention this in the paper.

### Questions
* (Question) Classical methods typically can not perform arbitrarily well on unstructured grids. I expect the same to be true here as the projection will have quadrature errors and you won't be able to evaluate the integrals to high accuracy on arbitrary grids. Have you performed any analysis on how sensitive results are to the choice of collocation points? It would be good to mention this in the paper.
* (Remark) Related to the above question. it would be great to have both timings and L2/L1 errors of the FNO/SFNO on their respective grids to quantify the error of the method and put it into perspective. I expect these results to be better, but I would still welcome this to show the grid-dependence and avoid wrong conclusions for cases where the data is readily available on structured grids.
* (Remark) In both of the original FNO/SFNO papers, it is mentioned that the generalization to arbitrary grids is straightforward by formulating the DFT/SHT on the respective domain. I wish that the authors had stressed this aspect more in the theoretical introduction, as the presented method is essentially a realization of the FNO/SFNO, just on an unstructured grid. This is one of the significant advantages of FNOs, and it is great to see this done in practice.
* (Question) In line with what I wrote above, one of the advantages of Neural Operators is that they can be trained on one grid and evaluated on another. Have you experimented with such settings. I would be especially curious in the presented FNO/SFNO case how such an operator would perform compared to one trained on the unstructured grid

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method to widen the applicability of current efficient neural operator learning methods. Current Fourier neural operator learning method works efficiently by frequency domain transformation via Fourier transform. However, this requires that data is sampled at equispaced intervals. The authors propose a structured matrix method using Vandermonde-structured matrices, which can be used on data sampled at arbitrary locations. Through experiments, the authors show that the proposed method shows high accuracy in solving partial differential equations and can be trained efficiently.

### Strengths
The paper is very well written, the motivation is very clear. The experiments are comprehensive.

### Weaknesses
The authors could start their method discussion by introducing Fourier neural operator first, its mathematical formulation, and then pointing out where the structured matrix method is fitted in. At present, Figure-1 shows their workflow, however it's hard to visualize the change the proposed method is bringing about in the whole neural operator learning workflow. Specifically, the paper lacks a clear explanation of how the Vandermonde-structured matrix replaces the Fourier transform in the frequency domain. The current description makes it difficult to understand the exact mathematical operations and the computational advantages of using the structured matrix approach. It is not immediately obvious how the method handles the non-equispaced data in the frequency domain, and how this impacts the overall accuracy and efficiency compared to the standard Fourier Neural Operator (FNO).

### Questions
See weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposes that when building Fourier Neural Operators (FNOs) that have unequally spaced sample points and relatively few "modes," it is faster to simply evaluate the exponential sums directly rather than use a fast transform. The efficacy of such a method is supported by several numerical experiments.

### Strengths
The manuscript considers experiments with a relatively broad range of models and does show that if few modes are considered then evaluating the exponential sums directly is likely faster. An implementation is provided.

### Weaknesses
The primary weakness of this manuscript is in its framed contribution and presentation around the "structured matrix method" (with a secondary issue being the baselines used and some details of the numerical experiments).

For the so-called Type 1 NUFFTs the authors consider, the fact that direct evaluation of the exponential sums is more efficient if only a small number of modes are needed is well known; in fact the same comment applies to the equispaced transform as well (albeit with a different crossover point with respect to the number of modes). In fact, standard NUFFT libraries make this clear, see, e.g., the "Do I even need a NUFFT?" section of https://finufft.readthedocs.io/en/latest/. Therefore, it is not clear what the contribution is here. Moreover, the presentation of the method in Section 2 is not even particularly clear (especially when moving to general point clouds since the notation seems to reduce to the case with only 2 sampling points? There are much nicer ways to write the transform).

The section titled "Inverse Transformations" is misleading. The manuscript seems to imply the adjoint transform is what is meant—these are not the same thing. (This is used incorrectly throughout the text.) On this point, the discussion in the related work section talking about the lack of a "direct" inverse NUFFT is also misleading. In particular Type 1 and Type 2 NUFFTs are not inverses of each other (unlike in the equispaced case) and the "inverse" refereed to is in, e.g., the least squares sense for things like imaging problems; this is not something the authors provide. 

Compounding this issue, the discussion of the computational complexity is lacking. The complexity should always be written in terms of the number of modes and the number of sample points (e.g., $\mathcal{O}(mn)$ with $n$ sample points and $m$ modes)—the claim could then be made that $m$ is often "constant" as $n$ grows and in that situation the complexity is linear. (Though, this is likely a bit disingenuous since if the underlying problem got more complicated, rather than simply oversampling a simple problem, both $m$ and $n$ would likely have to grow.) Given the stress placed on the number of modes it is also somewhat surprising that, unless I missed it, the experiments do not talk about how many modes are used in each case (that seems easy to add and informative).

For the experiments it is also not clear why something like https://finufft.readthedocs.io/en/latest/ is not used as a comparison point (rather than cubic interpolation). Moreover, the "full grid" comparisons seem misleading as well; if I am understanding this point correctly the "Full Grid" baseline is using more modes rather than the reduced number. If so, shouldn't it be done with the reduced number and, if that number is small enough, directly evaluate the sums? Also, 

Lastly, some rather relevant references are missing

Related to the software references above:

A parallel non-uniform fast Fourier transform library based on an “exponential of semicircle” kernel. A. H. Barnett, J. F. Magland, and L. af Klinteberg. SIAM J. Sci. Comput. 41(5), C479-C504 (2019).

These two are some of the first formalizations of NUFFTs, so they seem relevant (certainly more so than many of the other included references):

Dutt, Alok, and Vladimir Rokhlin. "Fast Fourier transforms for nonequispaced data." SIAM Journal on Scientific computing 14.6 (1993): 1368-1393.

Beylkin, Gregory. "On the fast Fourier transform of functions with singularities." Applied and Computational Harmonic Analysis 2.4 (1995): 363-381.

### Questions
For the "Full Grid" baseline, is the model using more modes rather than the reduced number. If so, shouldn't it be done with the reduced number and, if that number is small enough, directly evaluate the sums?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
