# Neural Fourier Transform: A General Approach to Equivariant Representation Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Symmetry learning has proven to be an effective approach for extracting the hidden structure of data, with the concept of equivariance relation playing the central role. 
However, most of the current studies are built on architectural theory and corresponding assumptions on the form of data. 
We propose Neural Fourier Transform (NFT), a general framework of learning the latent linear action of the group without assuming explicit knowledge of how the group acts on data.
We present the theoretical foundations of NFT and show that 
the existence of a linear equivariant feature, which has been assumed ubiquitously in equivariance learning, is equivalent to the existence of a group invariant kernel on the dataspace. 
We also provide experimental results to demonstrate the application of NFT in typical scenarios with varying levels of knowledge about the acting group.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The main motivation behind the paper is the following: In pre-dominant approaches to equivariant learning, the underlying group and group action is assumed to be known. There are various approaches which then construct linear-equivariant layers followed by a suitable non-linearity and then stack them together. However, often the underlying group or action might not be known. The starting point of the paper is to consider the usual (and then the group) Fourier transform and its well-known equivariance relation. The idea is to construct a non-linear extension where the underlying action is not known, but has similar behaviour as the usual FT. This method dubbed as the non-linear Fourier transform affords finding a relation similar to the usual Fourier transform without having access to analytically tractable knowledge of the group action. It however, does require access to transformed versions of the data to set up a loss function that might be minimized. Various basic properties of this transform and shown. The work heavily relies on ideas from Miyakato et al. and Keller and Welling.

### Strengths
- The idea is quite natural and convincing. It does seem more suitable for time series and video data, due to the lack of availability of suitably transformed data in usual setting, but for a framework it seems reasonable. 
- It relies on the natural idea of using an invariant kernel mapping (while not cited, there is quite some work on non-neural variants of this, such as by Reisert and Bukhardt, JMLR 2007), and shows how the idea is sensible. 
- The idea of finding a data-dependent spectrum is appealing.

### Weaknesses
-- The primary weakness of this paper is that it relies on data triplets of tuples that gives a sense of the underlying group action. This is a weakness, since such data isn't easily available in most real-world settings. Specifically, the requirement for transformed versions of the input data, denoted as $(x, g \circ x)$, where $g$ represents an element of the unknown group action, poses a significant practical hurdle.  While the paper pivots to time series applications, this doesn't fully address the core issue of data availability in other domains. The method's reliance on these specific data triplets limits its applicability to scenarios where such transformations are either naturally present or can be artificially generated, which is often not the case. 
-- The applications presented don't seem compelling, and more or less follow a similar pattern as in the work of Miyato et al. 2022. The experiments, while demonstrating the method's functionality, do not showcase a significant advantage over existing techniques or address the limitations of data availability. The choice of tasks, such as time series prediction, appears to be driven more by the availability of suitable data rather than by the method's inherent strengths. 
-- Related to the above; The experimental section is relatively toy, which is a weakness, given the generality of the pitch of the paper. The experiments lack the complexity and scale required to demonstrate the method's robustness and practical applicability in more challenging scenarios. The absence of comparisons with state-of-the-art methods in relevant domains further weakens the experimental validation.

### Questions
Would appreciate if the authors could elaborate on the weaknesses mentioned.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Neural Fourier Transform for equivariant representation learning that deals with the cases in which the group action on the data may be nonlinear or implicit. The paper investigates three scenarios based on the level of prior knowledge on the group and group element that acts on each data. Experimental results are provided to demonstrate the effectiveness of the proposed method in nonlinear spectral analysis, data compression, image classification, and novel view synthesis from a single 2D rendering of a 3D object.

### Strengths
* The paper has a clear motivation
* The proposed method is accompanied with interesting theoretical results
* Limitations are properly discussed
* Codes are provied to support the main paper

### Weaknesses
 * Overall, the paper is well written but it probably needs more checks for possible typo errors (there is a minor typo at the end of Section 2 "scaler-value")

### Questions
1. With respect to the work of Miyato et al., (2022) that considers the properties of the learned model to be intra-orbital homogeneity or full equivariance, which of these properties that the proposed model owns in each setting (U-NFT, G-NFT, g-NFT) ?

### Soundness
3 good

### Presentation
3 good

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
This manuscript presents the Neural Fourier Transform (NFT), a novel framework for learning latent linear group actions without requiring explicit knowledge of how the group (or even what group) acts on the input data. The paper rigorously explores the theoretical underpinnings related to the existence of linear equivariant features. Moreover, empirical results are provided to substantiate the utility of NFT in a range of applications, each distinguished by differing levels of prior knowledge about the input group action.

### Strengths
1. The paper is well written and well structured. Many remarks and explanation are provided, making it easily comprehensible
2. The core concept—learning a latent group representation space by utilizing triples of group-acted inputs, without the need for prior information on the group—is both intriguing and innovative.
3. The empirical findings presented are both compelling and substantiate the framework's utility.

### Weaknesses
1. I have only one question/comment: in Theorem 4.2, $(\Phi^*, \Psi^*)$ is the minimizer of
$$E_{g\in G}[\|g\circ X - \Psi \Phi (g\circ X)\|^2]$$
Does this merely imply that $\Psi \circ\Phi $ is a "good" autoencoder on the group orbit, instead of transforming $X$ into a linear space on which there is a linear $G$ action? Should it be the following instead?
$$E_{g\in G}[\|g\circ X - \Psi \circ M(g) \circ \Phi ( X)\|^2]$$

### Questions
Please refer to the previous comment.

### Soundness
3 good

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
This paper proposes Neural Fourier Transform as a general approach for equivariant representation learning. The goal is to learn a latent linear action of the group, similar to how the DFT encodes linear representations of the shift group. Many symmetries (e.g. fisheye transformations) are obvious symmetries to the human eye, but there is no easy way to represent them using classic theory. The learning task is decomposed into three cases, where the network has to match using a linear action in latent space and a nonlinear action in data space. Theoretical results are verified on several tasks.

### Strengths
- The paper tackles the interesting task of representing nonlinear image transformations in a neural network as linear group actions. This is an interesting and valuable direction.
- The paper finds a simple yet effective strategy for solving the problem using tuples of $g$-transitions.
- While restricted to synthetic settings, the experiments are promising.

### Weaknesses
 - The experiments could have been detailed a bit more clearly. I.e., what are the objectives, the loss functions used, the in/outputs to the model, etc. 
- I find the title "Neural Fourier Transform" a bit misleading, as the Fourier transform is an extremely general signal processing tool, where in this work it is used as an example of finding linear representations of a group.
- It would have been nice to have some results on a task that is a bit more "in the wild".

### Questions
- How did you combine the autoencoder framework with the downstream (e.g. classification) objective? Did you have to weight the two objectives? How did you find the hyperparameters?
- Do you have an idea of how to get the tuples of nonlinear group actions in the wild?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
