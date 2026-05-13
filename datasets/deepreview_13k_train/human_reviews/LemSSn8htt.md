# Delta-AI: Local objectives for amortized inference in sparse graphical models

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
We present a new algorithm for amortized inference in sparse probabilistic graphical models (PGMs), which we call $\Delta$-amortized inference ($\Delta$-AI). Our approach is based on the observation that when the sampling of variables in a PGM is seen as a sequence of actions taken by an agent, sparsity of the PGM enables local credit assignment in the agent's policy learning objective. This yields a local constraint that can be turned into a local loss in the style of generative flow networks (GFlowNets) that enables off-policy training but avoids the need to instantiate all the random variables for each parameter update, thus speeding up training considerably. The $\Delta$-AI objective matches the conditional distribution of a variable given its Markov blanket in a tractable learned sampler, which has the structure of a Bayesian network, with the same conditional distribution under the target PGM. As such, the trained sampler recovers marginals and conditional distributions of interest and enables inference of partial subsets of variables. We illustrate $\Delta$-AI's effectiveness for sampling from synthetic PGMs and training latent variable models with sparse factor structure. Code: https://github.com/GFNOrg/Delta-AI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents Delta-AI, an algorithm for the problem of amortized inference in PGMs. The main idea behind the paper is to leverage the sparsity of PGMs to pose a local constraint that can then be used as a novel loss function for GFlowNets. This local constraint makes GFlowNets more efficient both in terms of memory and time since only the few relevant variables can be used in each training step. The proposed inference algorithm is tested on a sytnetic data set as well as MNIST data and outperforms vanilla GFlowNets and other amortized inference algorithms.

### Strengths
1. Interesting use of local constraints in GFlowNets for amortized inference within the realm of probabilitic graphical models. 

2. The proposed DELTA-AI seems sound and performs pretty well in the shown experimental settings.

### Weaknesses
1. The experiment settings are a bit weak in my opinion. Formalizing the idea and getting a a proof of concept is fine using a synthetic data. Also if there are no real data sets available that can also be considered but just considering MNIST as the real data is a bit limiting and does not show the full power of DELTA-AI. For example why not use the DELTA-AI loss within PixelVAE and try inference on natural images?

2. The paper is based on taking advantage of local credit assignment -> local losses this part gets kind of obsfuscated as the paper goes along. (but this is a simple fix by rewriting a bit of portions in sections 3)

### Questions
1. How will the proposed inference algorithm scale to natural images?


P.S: Being an emergency reviewer I might have missed some specifics and thus am lowering my confidence. Looking forward to the rebuttal.

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
The authors propose a technique for amortized inference in sparse probabilistic models which they call \Delta-AI (\Delta-amortized inference) that takes advantage of sparse model structure (previously specified). This is done by matching the conditional distribution of a variable given its Markov blanket. The sparsity of the graphical model allows for local credit assignment in the policy learning objective. They experiment with synthetic PGMs and latent variable models with sparse factor graph structure to show the algorithms effectiveness.

### Strengths
The authors show how to take advantage of  known (or assumed) graphical model structure to allow for local credit assignment. Computationally, this lowers the memory requirement as parameter updates only requires instantiating a single variable and its Markov blanket.

### Weaknesses
The paper was hard to read - while there was a fair amount of discussion about the graphical model basics, there was not much about GFlowNets.

The core motivation of the paper, which is to leverage the structure of the graphical model for local credit assignment, is not clearly articulated. While the paper mentions that the sparsity of the graphical model allows for local credit assignment, it does not explicitly state how this is achieved in the algorithm. The connection between the Markov blanket and the local updates is not made explicit enough, leaving the reader to infer the details. The paper also lacks a clear explanation of how the proposed method compares to other amortized inference techniques, particularly in terms of computational cost and approximation quality. It is unclear why the proposed method is superior to existing methods, or when it is expected to perform better or worse.

Not having direct background / experience with GFlowNets, I found myself wondering why have two representations of the model (the 
factorized Markov network p and the inference network q) - is the assumption that $p$ is provided (not just the structure / factors (sets of nodes) but also the exact parameters - or are the parameters of both learnt?

### Questions
Not having direct background / experience with GFlowNets, I found myself wondering why have two representations of the model (the 
factorized Markov network p and the inference network q) - is the assumption that $p$ is provided (not just the structure / factors (sets of nodes) but also the exact parameters - or are the parameters of both learnt?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents Δ-amortized inference (Δ-AI), a new algorithm for efficient inference in sparse probabilistic graphical models (PGMs). Δ-AI leverages sparsity to assign credit locally in the agent's policy learning, enabling faster off-policy training without the need to instantiate all random variables. The trained sampler matches conditional distributions and recovers marginals, making it effective for inference in partial variable subsets. Experimental results demonstrate its efficiency for synthetic PGMs and latent variable models with sparse structures.

### Strengths
- The paper is well written and organized. It presents a clear and compelling motivation for the problem at hand. The discussion of prior works is thorough and well-structured, and the paper offers promising avenues for future research.
- The paper develops a novel algorithm namely, Δ-AI that offers substantially faster training when compared to regular GFlowNets and other amortized inference methods, since each training step involves only a small subset of variables, resulting in negligible sampling costs. Furthermore, the memory cost associated with Δ-AI is exceptionally low, since the algorithm leverages the sparsity of the probabilistic graphical model to compute the gradient update locally over a small set of variables. Lastly Δ-AI provides the advantage of flexible probabilistic inference by amortizing numerous potential sampling orders into a single sampler, by learning Bayesian networks with multiple Markov-equivalent structures.

### Weaknesses
As the current paper falls outside the scope of my research interests, I am unable to identify any significant weaknesses in the paper. Consequently, my confidence in assessing the paper is limited.

- The paper hinges on the assumption that the factors of the distribution $\phi_{k}$ are known. This seems like a stringent condition, and it is worth exploring how the framework and algorithm proposed in the paper can be extended to scenarios where these factors are unknown and need to be learned.

-  The paper asserts that it accomplishes simultaneous amortization over multiple DAG structures. However, it would be beneficial to provide a more detailed explanation of how this simultaneous amortization is achieved.

### Questions
- The paper hinges on the assumption that the factors of the distribution $\phi_{k}$ are known. This seems like a stringent condition, and it is worth exploring how the framework and algorithm proposed in the paper can be extended to scenarios where these factors are unknown and need to be learned.

-  The paper asserts that it accomplishes simultaneous amortization over multiple DAG structures. However, it would be beneficial to provide a more detailed explanation of how this simultaneous amortization is achieved.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
