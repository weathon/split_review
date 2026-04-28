# Wigner kernels: body-ordered equivariant machine learning without a basis

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Machine-learning models based on a point-cloud representation of a physical object are ubiquitous in scientific applications and particularly well-suited to the atomic-scale description of molecules and materials. 
Among the many different approaches that have been pursued, the description of local atomic environments in terms of their neighbor densities has been used widely and very succesfully. 
We propose a novel density-based method which involves computing ``Wigner kernels''. These are fully equivariant and body-ordered kernels that can be computed iteratively with a cost that is independent of the radial-chemical basis and grows only linearly with the maximum body-order considered. This is in marked contrast to feature-space models, which comprise an exponentially-growing number of terms with increasing order of correlations.
We present several examples of the accuracy of models based on Wigner kernels in chemical applications, for both scalar and tensorial targets, reaching state-of-the-art accuracy on the popular QM9 benchmark dataset, and we discuss the broader relevance of these ideas to equivariant geometric machine-learning.

\iffalse
Machine-learning models based on a point-cloud representation of a physical object are ubiquitous in scientific applications and particularly well-suited to the description of molecules and materials in terms of their atomic-scale components. 
Among the many different approaches that have been pursued, one that has been particularly successful involves decomposing structures into a collection of local environments, that are further described in terms of the neighbor density.
By taking symmetrized correlations of this density, one achieves an increasingly detailed description of the structure, corresponding to a body-ordered expansion of the target property. 
The number of density correlation coefficients, however, grows exponentially with the body order, which makes it necessary to resort to heuristics or data-driven schemes to choose an optimal basis and to truncate the expansion. 
We introduce an alternative approach that is equivalent to taking the complete limit of a linear body-ordered expansion, but does not require the explicit definition of a basis. 
Our method involves computing ``Wigner kernels'', that are nothing but scalar products of the density-correlation vectors, but can be computed iteratively with a cost that is independent on the radial and element bases, and grows only linearly with the maximum body order considered. 
We present several examples of the accuracy of models based on Wigner kernels in chemical applications, for both scalar and tensorial targets, reaching state-of-the-art accuracy for the popular QM9 benchmark dataset, and we discuss the broader relevance of these ideas to equivariant geometric machine-learning.
\fi

\iffalse
............

Over the past few years, data-driven techniques have been used extensively as a surrogate model for quantum mechanical calculations of molecular and condensed-matter systems. 
Among the many different approaches that have been pursued, one that has been particularly successful involves mapping an atomic structure onto a set of atom-centered environments, described by the neighbor density symmetrized over a suitable basis.
By taking symmetrized correlations of this density, one achieves an increasingly detailed description of the structure, corresponding to a body-ordered expansion of the target property. 
The number of density correlation coefficients, however, grows exponentially with the body order, which makes it necessary to resort to heuristics or data-driven schemes to choose an optimal basis and to truncate the expansion. 
We introduce an alternative approach that is equivalent to taking the complete-basis limit of a linear body-ordered expansion, but does not require the explicit definition of a basis. 
Our method involves computing ``Wigner kernels'', that are nothing but scalar products of the density-correlation vectors, but can be computed iteratively with a cost that is independent on the radial {\color{teal} and element} bas{\color{teal}e}s, and grows only linearly with the maximum body order considered. 
We present several examples of the accuracy of models based on Wigner kernels, for both scalar and tensorial targets, and discuss the broader relevance of these ideas to equivariant geometric machine-learning.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Decorated 3D point-cloud representations provide a way to describe molecules and take into account the complexity of the interactions between atoms. Kernels are especially well suited to include by design wishable properties such as equivariance with respect to symmetry operations in the group of 3D rotations SO(3). In particular, symmetry-adapted kernels under the form of body-ordered kernels have been proposed in the literature. However computing these kernels with high order \nu > 2 is impractical. This paper proposes a single to compute iteratively high-\nu kernels by relying on lower-order kernels. This computation is backed up by a proof given in Appendix. A numerical section is devoted to test the so-called Wigner kernels in the context of  Kernel Ridge Regression on datasets where a high body-order is needed (random methane dataset, QM9 and RM17 datasets).

### Strengths
Soundness: In the context of molecule representation, the paper focuses on body-ordered kernels and proposes a new way to compute it based on them. The contribution undoubtedly opens the door to application of these kernels in atomistic properties prediction tasks. Moreover even if it does not insist on that point, it also gives a nice example of geometrical learning where the hypothesis space induced by a kernel inherits by definition of geometrical properties.

Originality: While this work follows in the footsteps of many recent works about kernels for molecules based on 3D point-cloud presentations and symmetry-adapted kernels, it proposes a new way of computing them and as so, is original.
Clarity: the paper awfully lacks of clarity for a machine learning reader (see weaknesses). The general message which is not too complex in itself is made noisy by a lot of implicit statements.

### Weaknesses
Soundness: Overall the contribution is very technical in terms of chemistry and less informative in terms of machine learning. I assume that it will be of limited interest for a vast majority of the community in ML and would be more highlighted in a dedicated venue.

Presentation: This paper suffers a lot from its presentation. It seems to me that the writing was intended for chemists and not the machine learning community.  It cruelly lacks of definitions and notations. The reader has to read a few chemistry papers to get a clear idea of each notation: for instance in equation (3),  which space does A_i belong to ?, recall what is a Wigner D-matrix, in equation (4), define x and r. More generally please start by defining how you describe a molecule ( a set of 3D coordinates and a set of associated labels, distances between atoms, forces ??) - The numerical experiment section suffers from the same default: the comments reflect a high level of expertise in chemistry from the authors but fail to highlight the interest for machine learning.

The lack of information about definitions and notations also prevents from a careful analysis of the computations at work here: what is the (analytical) complexity in time ? memory requirements...

### Questions
(1) please define and provide your notations at eahc step of your paper (after related works)
(2) please clearly explain how body-ordered kernels were computed so far and compare the analytical complexity in time with those of the Wigner kernel.
I've read the rebuttal and raised consequently my score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a kernel that is equivariant w.r.t. SO(3) and accounts for neighbor information "body order". The kernel is computed using an iterative computation of lower body-order kernel values. Using kernel ridge regression, the paper trained the Wigner kernel model on gold clusters, random methane configurations energies, QM9 molecule energies, dipoles, and rmd17 dataset energies and forces, and compares with several other models.

### Strengths
quality+clarity: Good set of experiments. Authors tried 4 datasets and compared with many additional models. Figures and tables are high quality.
originality: I'm not familiar with literature to tell if kernel in eq 5 is novel. The iterative calculation of the kernel and application to molecule properties is novel.
significance: Kernel ridge regression with the developed kernel outperforms SOTA models in several cases.

### Weaknesses
It is not entirely obvious to me how this could be applied outside of molecule predictions. Perhaps authors can add a bit of description here?

### Questions
-can authors define terms in equation 2?

"this formulation of the high-order kernels is entirely lossless in terms of the radial basis and the dimension of composition (chemical element) space."(pg 4)
-do the kernels take into account the atom composition?

-can authors include a comparison of training time across the models, for ex. the x-axis of Figs 1 and 2?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on atomic-scale description of molecules and materials using point-cloud representations of physical objects. The authors propose a novel density-based approach using "Wigner kernels."

### Strengths
1. The proposed Wigner kernel affords computationally efficient density-based representation. 
2. Comprehensive empirical results are provided demonstrating the utility of the Wigner kernel on various datasets.

### Weaknesses
1. I found the paper hard to follow with many terminologies in 3D objects or molecules context. Perhaps the authors can improve the presentation by highlighting the ML related contributions.
2. The formulation Eq (4) seems to be limited to only three-dimensional problems.
3. The formulation Eq (1) is highly related to the kernel mean embedding (KME) (see, e.g., Muandet et al., Kernel Mean Embedding of Distributions: A Review and Beyond). However, the related work does not compare with any of the KME literature.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

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
The authors consider a density-based method for point-cloud representation. They propose a iterative method, called Wigner iteration, to compute a positive definite kernel. The computational cost grows linear with respect to the body-order.

### Strengths
The topic is relavant to kernel methods for point-cloud. The proposed method is also related to the representation of interactions between elements, which is important for various applications.

### Weaknesses
My main concern is the clarity of the paper.
- Without seeing Eq. (10) in Appendix, I could not understand the role of $\lambda$. Since the authors discuss the computational costs with respect to $\lambda$ in the main text, I think they should clarify what is $\lambda$ in the main text. It is the index of a basis functions in my understanding.  Specifically, the paper lacks a clear definition of how $\lambda$ relates to the radial basis functions used in the kernel construction. The connection between the index and the actual mathematical form of the basis function is not explicitly stated, making it difficult to assess the practical implications of the computational cost analysis.
- In addition to $\lambda$, the role of $\mu$ is not clear for me, either. Without knowing what the indexes stand for, we cannot evaluate the computational cost of the sum appeared in Eq. (6). The authors explain that in Appendix E, but it should be in the main text since the computational cost is a crucial topic in this paper.  Furthermore, the paper does not specify the range of values for $\mu$ and how these values impact the overall size of the kernel matrix. This lack of detail makes it difficult to assess the practicality of the proposed method, especially for large-scale point cloud datasets.

### Questions
For the experimnts in Seciton 4.1, what about the computational time for each case in practice?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
