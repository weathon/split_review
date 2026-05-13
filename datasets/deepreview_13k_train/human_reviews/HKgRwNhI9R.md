# Symmetric Basis Convolutions for Learning Lagrangian Fluid Mechanics

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Learning physical simulations has been an essential and central aspect of many recent research efforts in machine learning, particularly for Navier-Stokes-based fluid mechanics.
Classic numerical solvers have traditionally been computationally expensive and challenging to use in inverse problems, whereas Neural solvers aim to address both concerns through machine learning.
We propose a general formulation for continuous convolutions using separable basis functions as a superset of existing methods and evaluate a large set of basis functions in the context of (a) a compressible 1D SPH simulation, (b) a weakly compressible 2D SPH simulation, and (c) an incompressible 2D SPH Simulation.
We demonstrate that even and odd symmetries included in the basis functions are key aspects of stability and accuracy.
Our broad evaluation shows that Fourier-based continuous convolutions outperform all other architectures regarding accuracy and generalization.
Finally, using these Fourier-based networks, we show that prior inductive biases, such as window functions, are no longer necessary.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Symmetric Fourier Basis Convolutions (SFBC), a new method for learning Lagrangian fluid simulations using graph neural networks. The key idea is to construct convolutional filters using Fourier series as separable basis functions, incorporating both even and odd symmetries. Through extensive experiments on three fluid simulation datasets, the authors demonstrate that SFBC outperforms prior methods like LinCConv and DMCF in terms of accuracy and stability. A major contribution is showing that previously used inductive biases like window functions are no longer needed with the Fourier basis. The paper provides a generalized framework for continuous convolutions, rigorous evaluation of design choices, and highlights the benefits of symmetry and smoothness in the convolutional bases.

### Strengths
1. The paper aims to tackle an important and challenging problem in ML for physics - modeling Lagrangian fluid mechanics.

2. Leveraging ideas like symmetry, smoothness, and Fourier bases to inject useful inductive biases into graph networks is logically sound and extends prior work nicely. In addition, it is nice to unify symmetry and antisymmetry under the same framework.

3. The extensive experimental methodology covering diverse design choices and evaluations on three distinct test cases is a major strength. The baselines are strong enough and the evaluation is rigorous. While the theoretical novelty is incremental, the engineering rigor and state-of-the-art results are valuable and significant contributions.

### Weaknesses
1. The theoretical novelty is somewhat limited as the core concepts like symmetric bases are adapted from prior work in other domains. Additional theoretical analysis could further strengthen the approach.

2. The evaluations are extensive but restricted to a specific type of fluid simulation problems. It is hard to extract insights that can generalize to a broader scope. Testing generalization on more diverse physical systems could better establish applicability.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study introduces a novel approach employing continuous convolution with symmetric Fourier basis functions, effectively leveraging the problem's inherent biases. The research demonstrates the superiority of using symmetric/anti-symmetric basis functions over the previously suggested explicit weight-tying mechanism. Additionally, the paper offers comprehensive ablation studies on various hyper-parameters, providing in-depth insights into their impact on the outcomes.

### Strengths
The research presents a method for acquiring symmetric/anti-symmetric basis functions successfully applied to selected problems. The study conducts a detailed ablation study to compare the proposed technique with related methods and the choice of hyperparameters. The authors also additionally present a novel dataset that can be used for the aforementioned problem.

### Weaknesses
1. The contribution of the work requires a clearer elucidation. Although the work introduces a symmetric Fourier Basis, it does not explicitly define the analytical form of the basis functions being utilized or distinguish them from Fourier sine and cosine series. Additionally, essential questions pertaining to the rationale behind the new proposed technique remain unaddressed (please refer to the listed questions).

2. I find it puzzling that the study did not incorporate "WaterRamps" and "Liquid3d" from prior research, considering their complexity. Utilizing these challenging scenarios would have been more suitable for demonstrating the model's effectiveness.

3. Improvements in some cases seem marginal.

### Questions
1. Regarding the proposed technique for obtaining symmetric/anti-symmetric basis functions (Eqn 9 and 10), it is essential to clarify whether these equations pertain to symmetry along the x-axis, y-axis, or a combined symmetry along both axes [x,y].
 Additionally, what is the assumed domain of the basis functions $b_x$ and $b_y$? Furthermore, it is crucial to determine whether a given set of orthonormal basis functions retains their orthonormality after applying this technique.

2. How does having more parameters than DMCF help here? Because even if you are learning more coefficients, the basis functions are constrained. So, in terms of expressivity, wouldn't the two methods be the same?

3. Did you directly use the even and odd Fourier Basis for symmetric and anti-symmetric basis functions (after proper modification of the 0 frequency)? If not, what is the explicit equation of the SFB? And if so, Do you think, with proper regularization, filters with Fourier basis will be able to learn proper symmetric and anti-symmetric kernel?

4. In Figure 2, we can see that with a high number of basis functions, Fourier even (or odd) is outperforming DMCF. What might be the reason for it?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a general formulation for continuous convolutions using separable basis functions and evaluated on 3 different datasets. They demonstrate that even and odd symmetry are the critical components for success. With the proposed Fourier-based network, the inductive bias, like the window function, is no longer necessary.

### Strengths
Quality: the paper is rich in detail, more than 40 pages in total and give sufficient background and relevant math for understanding the problem.

Originality: The author proposed an SFBC approach that works better than other CConv-based methods. The author also shows that with the proposed structure, the window function is not necessary.

Significance: The proposed Fouries-basis network is part of a larger group of symmetric methods that opens up future research.

Clarity: The content is self-contained and easy to follow.

### Weaknesses
Some details need to be clarified. See questions. Moreover, there are no movies for the learned dynamics to check for temporal coherence. The unique contribution compared with previous research needs to be elaborated.

1. The result of the proposed separable basis is demonstrated on the 1D and 2D tests. Since the method uses the outer product, will it cause issues with the scalability to higher dimensions?

2. What is the computational overhead compared with other baseline models?

3. What is the limitation of the current methods?

4. The author cites Fey 2018 works several times. In the cited work, the high dimensional spline basis is also the product of the 1d spline basis, sharing similar properties of the proposed separable basis. Can you elaborate on the difference between the proposed one and Fey's method?

### Questions
1. The result of the proposed separable basis is demonstrated on the 1D and 2D tests. Since the method uses the outer product, will it cause issues with the scalability to higher dimensions?

2. What is the computational overhead compared with other baseline models?

3. What is the limitation of the current methods?

4. The author cites Fey 2018 works several times. In the cited work, the high dimensional spline basis is also the product of the 1d spline basis, sharing similar properties of the proposed separable basis. Can you elaborate on the difference between the proposed one and Fey's method?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The paper proposes a generalized formulation of continuous convolution approaches using separable basis functions. The coefficients of the basis functions are learned from the training data.
- By using the Fourier series as the basis functions with both even and odd symmetry, the symmetries are built in the in the convolutions which are beneficial for accurately learning Lagrangian flow physics. 
- The method is evaluated on multiple cases:
    - The Symmetric Fourier Basis Convolution approach is compared against against other CConv approaches in a toy problem.
    - It’s compared against multiple MLP-based GNNs methods, using a compressible one-dimensional problem 
    - It’s evaluated on a two-dimensional closed domain simulation, which shows the proposed method can predict over a long time frame with inference stability. In this 2D case, the paper also explores the influence of window functions, Fourier terms, and coordinate mappings.
    - The free-surfaces is also evaluated, using a fluid blob collision scenario, to investigate how different basis terms perform with partially occupied support domains.

### Strengths
- The proposed method of using Fourier basis functions provides an inherently symmetric and smooth continuous convolution approach, which shows good results on several testing cases.
- The paper provides additional details, analysis and ablation studies in the appendix to better show case the method and the comparison with other continuous convolutional approaches.

### Weaknesses
 - Most real-world applications of fluid simulation are in 3D cases. It would be good if the paper has some 3D examples or discussions regarding how to extend the method to 3D cases.

 - When applying this method to 3D scenarios, is there a concern that the weight matrix (W) might contain too many parameters, and intermediate matrix B (in Eq. 20) might become too large, causing challenges for training?

- When comparing the proposed method with related works, it might be beneficial to include runtime performance metrics as well, which can include information such as the number of iterations required for training, the time taken for each training iteration, and the time take for generating one prediction.

### Questions
- When applying this method to 3D scenarios, is there a concern that the weight matrix (W) might contain too many parameters, and intermediate matrix B (in Eq. 20) might become too large, causing challenges for training?
- When comparing the proposed method with related works, it might be beneficial to include runtime performance metrics as well, which can include information such as the number of iterations required for training, the time taken for each training iteration, and the time take for generating one prediction.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
