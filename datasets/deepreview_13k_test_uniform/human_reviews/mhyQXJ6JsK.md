# Enabling Efficient Equivariant Operations in the Fourier Basis via Gaunt Tensor Products

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
\vspace{-4pt}
\looseness=-1 Developing equivariant neural networks for the E(3) group plays an important role in modeling 3D data across real-world applications. Enforcing this equivariance primarily involves the tensor products of irreducible representations (irreps). However, the computational complexity of such operations increases significantly as higher-order tensors are used. In this work, we propose a systematic approach to substantially accelerate the computation of the tensor products of irreps. We mathematically connect the commonly used Clebsch-Gordan coefficients to the Gaunt coefficients, which are integrals of products of three spherical harmonics. Through Gaunt coefficients, the tensor product of irreps becomes equivalent to the multiplication between spherical functions represented by spherical harmonics. This perspective further allows us to change the basis for the equivariant operations from spherical harmonics to a 2D Fourier basis. Consequently, the multiplication between spherical functions represented by a 2D Fourier basis can be efficiently computed via the convolution theorem and Fast Fourier Transforms. This transformation reduces the complexity of full tensor products of irreps from $\mathcal{O}(L^6)$ to $\mathcal{O}(L^3)$, where $L$ is the max degree of irreps. Leveraging this approach, we introduce the Gaunt Tensor Product, which serves as a new method to construct efficient equivariant operations across different model architectures. Our experiments on the Open Catalyst Project and 3BPA datasets demonstrate both the increased efficiency and improved performance of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a systematic approach to accelerate the computation of tensor products of irreps by connecting Clebsch-Gordan coefficients to Gaunt coefficients. Based on this, the authors introduce a change of basis from spherical harmonics to a 2D Fourier basis. This transformation enables efficient computation via the convolution theorem and Fast Fourier Transforms (FFT), reducing the complexity from $O(L^6)$ to $O(L^3)$.

### Strengths
- The paper is very well-structured, featuring clear and logical derivations. The authors deserve commendation for their efforts in showing the equivariance of tensor products with Gaunt coefficients (Appendix D).
- Interpreting the spherical tensor product as a multiplication of spherical functions and subsequently transforming it into a 2D convolution provides valuable insight into the underlying operations. In my opinion, this perspective is more important than the subsequent application of FFT, which is a logical extension.
- The substantial reduction in time and memory cost on the 3BPA dataset serves as compelling evidence of the method's effectiveness.

### Weaknesses
Majors:
- The current derivation and application are closely tied to $\text{O}(3)$. Is it feasible to extend this convolutional perspective beyond $\text{O}(3)$, e.g., to other Lie groups like $\text{SU}(2)$? It would be beneficial to see discussions on the aspect of its generalization.
- I would like to see the inference time of EquiformerV2 model with and without the proposed Gaunt tensor products.

Minors: 
- Please adjust Equation (23)(26)(36) as they are written in the margins of the paper.

### Questions
See weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces a new framework for calculating the equivariant operations efficiently. The key idea is to convert the Clebasch-Gordan coefficients to Gaunt coefficients, by which the tensor product of irreps can be calculated efficiently in the Fourier domain.

### Strengths
1. The paper is well-written, and the main idea is explained clearly.
2. It is smart and interesting that the basis transformation is applied to the Fourier domain. The usefulness of the proposed method for improving computational efficiency is verified with numerical experiments.

### Weaknesses
It would be better if more discussion could be given about the added value of this work. It will help the readers who are not familiar with this direction (like me) to easily understand the contribution and main differences compared with the existing works.

### Questions
1. Could you give me more explanation about the *braket* notations used in Theorem 3.1? It seems not clearly introduced in the paper.
2. Could you explain more or give the intuition about the irreducible representation?
3. How to determine in practice the truncation, ie. the degree L, in the 2D Fourier expansion (above Eq. (5))?
4. Is it possible to choose other basis systems instead of Fourier? May I know how choosing different systems affects the result of this paper?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Gaunt Tensor Product, an efficient method to compute the tensor products of (high-degree) irreps as compared to the widely-used Clebsch-Gordan (CG) product. This is established through the connection between CG coefficients and Gaunt coefficients via the Wigner-Eckart theorem, and this connection implies that tensor product can be equivalently represented as multiplication of spherical functions. Through convolution theorem and FFT, the computational cost has been reduced from $O(L^6)$ to $O(L^3)$, where $L$ is the highest-degree of the irreps.

### Strengths
1. The paper is well-structured and articulate. The authors have included most of the requisite background material to the appendix, thereby maintaining the flow of the main text.

2. The paper's approach to enhancing computational efficiency, specifically through establishing a connection between CG coefficients, Gaunt coefficients, and the FFT, is both innovative and compelling.

3. The experimental evaluations comparing the proposed tensor product with the conventionally employed CG product are both extensive and convincing.

### Weaknesses
1. One point of critique is related to the treatment of Theorem 3.1 in the manuscript. The text uses a range of specialized terms—such as "spherical tensor operator," "reduced matrix element," and "total angular momentum"—and introduces various notations that may not be readily accessible to readers unfamiliar with quantum mechanics. To enhance clarity and comprehension, I recommend that the authors elaborate on these concepts, particularly in their exposition of the Wigner-Eckart theorem.

2. Another inquiry concerns the necessity of using high-degree irreps. In most E3-NN architectures, irreps with degrees no greater than L=2 are commonly employed. Consequently, I question whether the computational overhead incurred through the FFT in implementing the proposed tensor product is actually more costly than directly using the CG product for low-degree irreps.

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
