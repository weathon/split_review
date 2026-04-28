# Continuity-Preserving Autoencoders for Learning Continuous Latent Dynamical Models from Images

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Continuous dynamical systems are cornerstones of many scientific and engineering disciplines.
While machine learning offers powerful tools to model these systems from trajectory data, challenges arise when these trajectories are captured as images, resulting in pixel-level observations that are discrete in nature.
Consequently, a naive application of a convolutional autoencoder can result in latent coordinates that are discontinuous in time.
To resolve this, we propose continuity-preserving convolutional autoencoders (CpAEs) to learn continuous latent states and their corresponding continuous latent dynamical models from discrete image frames. 
We present a mathematical formulation for learning dynamics from image frames, which illustrates issues with previous approaches and motivates our methodology based on promoting the continuity of convolution filters, thereby preserving the continuity of the latent states.
This approach enables CpAEs to produce latent states that evolve continuously with the underlying dynamics, leading to more accurate latent dynamical models.
Extensive experiments across various scenarios demonstrate the effectiveness of CpAEs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Continuity-Preserving Autoencoders (CpAEs), aimed at learning continuous latent dynamical models from discrete image data. It addresses the challenge of modeling continuous dynamical systems from image trajectories by proposing a new autoencoder architecture that promotes continuity in the latent space. CpAEs are designed to maintain continuous evolution in latent states by enforcing Lipschitz continuity in convolutional filters, with experiments demonstrating improved performance over standard methods, particularly for complex dynamical systems.

### Strengths
* The paper identifies an important problem: standard autoencoders struggle to learn continuous latent states from discrete image observations of dynamical system. 
* The paper provides rigorous mathematical formulation and theoretical analysis, and a key theorem (theorem 3.1) that establishes conditions for continuous latent state evolution. 
* Empirical results demonstrate the effectiveness across multiple datasets and clear improvements over baseline methods.

### Weaknesses
 * Theoretically, the analysis is limited to rigid body motion in 2D plane and does not fully address non-rigid motion cases. The analysis assumes simple transformations (translation and rotation) that may not capture real-world complexity. Specifically, the assumption that the mapping \mathcal{S} can be represented by simple transformations like translation and rotation is a strong limitation. This simplification may not hold for more complex systems where deformations and non-linear dynamics are present. The analysis lacks a rigorous treatment of how the Lipschitz constant of the convolutional filters relates to the complexity of the learned dynamics, especially in non-rigid scenarios.
* The Assumption 3.1 about vanishing feature maps near image boundaries may be too restrictive, which may requires significant zero padding. This assumption, while simplifying the analysis, might not be practical for real-world images where objects of interest may not be neatly confined to the center. The requirement of having feature maps vanish near the boundaries could lead to a loss of information and limit the method's applicability to more general image datasets. The impact of this assumption on the generalization capability of the model is not thoroughly investigated.
* The requirement for large filter sizes (O($1/\delta$)) could limit practical applications. The theoretical analysis suggests that the filter size needs to scale inversely with the discretization parameter \delta, which can lead to computationally expensive filters, especially for high-resolution images. The practical implications of this requirement, such as increased memory usage and computational time, are not fully addressed. This could hinder the scalability of the method to more complex and higher-dimensional datasets.
* The significant drop in performance on the swing stick task (57.4% VPT vs 99.2% for damped pendulum) is not thoroughly analyzed. The large discrepancy in performance between the damped pendulum and the swing stick tasks raises concerns about the robustness of the method. The swing stick task, with its more complex dynamics and real-world data, exposes potential limitations of the proposed approach. The paper lacks a detailed analysis of the factors contributing to this performance drop, such as the quality of the data, the complexity of the dynamics, and the sensitivity of the method to noise.

### Questions
Would the method work on more complicated mechanical system beyond rigid bodies?

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
The authors consider the setting where observations of a continuous dynamical system are captured by a sequence of images which are discrete in time and space. The challenge they claim to address is the misalignment of the evolution of images in pixel coordinates and the evolution of the underlying continuous time dynamical system. To address this challenge, the authors introduce the notion of delta-continuous, a relaxation of Lipschitz continuity where the ratio of the change in latent states and the change in continuous dynamical states is bounded by a constant. The term delta in the name delta-continuous refers to the size of the image pixels. As I understand, the claim is that if the pixels are too big then the delta-continuous condition fails and the latent states cannot be learned as a continuous dynamics. The authors subsequently introduce the continuity-preserving autoencoders (CpAEs) to encourage latent states to evolve continuously with the underlying dynamics. CpAEs do this using large filters in the first few layers, and a regularizer on the weights that encourage image continuity.

### Strengths
The paper is well organized and well written, although in some parts it might be easier to read if variable names were augmented with the concept they represent.

### Weaknesses
While the ideas presented are interesting, the impact of conventional CNNs failing to be delta-continuous is not clear to me. The experiments in the main paper (e.g., Figure 6) attempt to demonstrate the importance of delta-continuity by comparing the reconstructive ability of CpAE to other networks. I am unconvinced by this experiment for the following reasons: 1) it is not clear to me that reconstructive ability is an appropriate indicator of latent continuity; 2) it is not clear to me that using a fully-connected architecture as a baseline is appropriate since ‘[FNNs] are often insufficient for … reconstructing images with complex visual patterns’ (Line 346); 3) the conventional CNN baseline has comparable reconstructive ability to the proposed model. In my view, a more appropriate experiment is presented in Figure 10, pairing this experiment with a quantitative assessment would be more convincing (also I’m not sure what ‘Neural state variables’ are). This alone however, would only demonstrate that the resulting latent structure is more smooth with the CpAE structure. An additional experiment showing that a fixed dynamical model is better able to model the dynamics of CpAE states than AE states would help.

I am unclear about the following experimental choices: 1) why do the authors compare to HNN architectures if the goal of the paper is to showcase the impact of the CpAE structure? 2) how does removing the VPNet regularizer impact CpAE performance? 3) how does using smaller weights in the initial layers impact CpAE performance? 4) if the CpAE ensures latent continuity why use a latent similarity loss (Line 399)? How much does this loss contribute to the observed performance?

### Questions
I am unclear about the following experimental choices: 1) why do the authors compare to HNN architectures if the goal of the paper is to showcase the impact of the CpAE structure? 2) how does removing the VPNet regularizer impact CpAE performance? 3) how does using smaller weights in the initial layers impact CpAE performance? 4) if the CpAE ensures latent continuity why use a latent similarity loss (Line 399)? How much does this loss contribute to the observed performance?

### Soundness
2

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
2

### Summary
This paper proposes continuity-preserving autoencoders (CpAEs) for learning continuous latent states from a series of images that represent a continuous dynamical system. The proposed autoencoders resolve problems from a naive usage of Convolutional Neural Networks due to the district nature of images. The key contributions are a mathematical formulation for learning continuous dynamics from image data, the sufficient condition for the latent states will evolve continuously with the underlying dynamics, a regularizer to promote continuity of filters and empirical results.

### Strengths
- The paper presents an interesting mathematical formulation for learning continuous dynamical systems from images.
- The method presents strong empirical results that show the proposed method works.

### Weaknesses
 - There is a lack of comparison with AEs that are not based on standard CNNs in the results.
- There are many assumptions that limit the formulation only to CNNs.
- There is a lack of ablation studies on the proposed methods parts.

### Questions
- How did you determine the filter size for Table 1?
- How much does the regularizer affect the results? Maybe the uplift in the result is just because of the filter sizes?
- In Figure 6, there is no image of CpAE on the two bodies. Why?
- Why are there no quantitative results for the two body data?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces continuity-preserving autoencoders (CpAEs) to learn continuous dynamical models and continuous latent states from the discrete pixel-based frames of a video.

First the authors present some theory showing that making the convolutional filters of the encoder Lipschitz continuous the states will evolve continuously. Then the authors introduce a regularizer to promote Lipschitz continuity.

The experiments show that by using CpAEs to learn continuous latent states, the learnt dynamical models are more accurate compared to standard CNN-based encoders that might produce discontinuous states .

### Strengths
1. Learning dynamical systems from image data is an important topic relevant in many applications.
2. Standard autoencoder are not forced to learn latent states that are continuous over time, which is a problem when trying to learn the underlying continuous model of the dynamics of the system. The paper presents an interesting theoretically grounded approach to enforce state continuity, which leads to improved performances in the considered experiments.
3. This theoretical framework could be useful for the community to build on.

### Weaknesses
1. My main concern on this paper is that I am not convinced that the proposed ideas will generalize well to more realistic tasks for which standard CNN encoders are powerful enough. While this is also noted by the authors as a limitation in section 5, I feel that for this paper to have a bigger impact on the ICLR community it would be important to apply this method to more complex architectures (e.g. VAEs, ViT) that will hopefully improve performances at least on the "swing stick" experiment.

2. The experimental section is missing some ablation studies to compare performances when varying some key parameters: 1) filter sizes and 2) regularizer parameters $\lambda_J$ and $\lambda_R$

3. The mathematical formulation proposed in section 3.1 to project states to pixels is key to understand the rest of the paper but not very easy to follow. It could benefit from using a simple running example, for example focusing on a single particle moving in space (if you add this example, you could even consider moving the example in section 3.2 to the appendix as a multi-particle extension)

4. Some notation is not introduced in the main text: $\Omega$ in section 3.1, $K$ in section 3.2, $\lambda_J$ in section 3.5, $\lambda$ and $\lambda_R$ in section 4

### Questions
I have two questions on your modelling choices. What do you mean when you say:
1. "Given our priority on ensuring the fidelity of the latent dynamical model, this work focuses on deterministic autoencoders."
2. "CpAEs are able to learn latent states that closely align with the assumed continuous dynamics. Thus, we propose to learn the latent states and their corresponding latent dynamical models separately"

### Soundness
3

### Presentation
3

### Contribution
3
