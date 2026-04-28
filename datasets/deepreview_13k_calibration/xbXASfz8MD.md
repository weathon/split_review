# Latent Space Symmetry Discovery

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 3, 6

## Abstract
Equivariant neural networks require explicit knowledge of the symmetry group. Automatic symmetry discovery methods aim to relax this constraint and learn invariance and equivariance from data. However, existing symmetry discovery methods are limited to simple linear symmetries and cannot handle the complexity of real-world data. 
We propose a novel generative model, Latent LieGAN (\ours{}), which can discover symmetries of nonlinear group actions.  It learns a mapping from the data space to a latent space where the symmetries become linear and simultaneously discovers symmetries in the latent space. Theoretically, we show that our model can express nonlinear symmetries under some conditions about the group action. Experimentally, 
we demonstrate that our method can accurately discover the intrinsic symmetry in high-dimensional dynamical systems. \ours{} also results in a well-structured latent space that is useful for downstream tasks including equation discovery and long-term forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper considers the problem of symmetry estimation for the sake of better representation learning. The authors introduce Latent Lie GAN (LaLiGan) for learning non-linear symmetries in the input data. The paper highlights the fact that the problem has high importance for the field of representation learning. The authors demonstrate that there were many approaches for solving similar problems; however, the main focus was on linear symmetries, i.e., group representations. In contrast, the presented paper demonstrates that it is possible to learn non-linear symmetries in an adversarial manner.

### Strengths
- The paper is well-written. The flow is smooth and coherent. The paper presents good illustrations to help the reader understand the presented idea.
- The mathematical language is easy to follow, correct, and detailed when needed.
- The authors highlight the main contributions of the paper clearly.
- The presented method is clearly a next-step solution compared to approaches like LieGG or LieGAN.
- The experiments demonstrate that the proposed method can be applied in a wide range of tasks.

### Weaknesses
These are not significant weknesses. I would like to highlight the fact, that from the paper it seems like there are no natural limitations to the proposed method, which is however, not true. A straighforward explanation of situations when the method fails or can lead to an incorrect outcome will help



### Questions
I would like the authors to answer the following questions to make it easier to understand certain aspects of the method
- In Eq. 2 you learn transformations as $\sum_i\text{exp}[w_i L_i]$. How to choose the number of matrices L to be used in the method? I suppose the number of Lie algebra elements you parametrize will significantly affect the flexibility of the method in the latent space
- If I understood correctly, the proposed method works for compact groups only. The experiments demonstrate that the method can learn trajectories that are isomorphic to circles. How will the method behave on the data which has translation symmetry only? Will it fail? If so, the set of admissible symmetries seems more limited and should be highlighted
- in Proposition 4.1 you mention that $\psi$ and $\phi$ are inverse of each other. It is not correct, these functions are inverse to each other only on the input dataset. It raises the following question, how robust is the inverse property when you move away from the training dataset? How robust is the detected symmetry, when you move away from the training dataset? It reminds me of the following paper *Moskalev A. et al. On genuine invariance learning without weight-tying. Topological, Algebraic and Geometric Learning Workshops 2023. – PMLR, 2023*

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of automatically discovering Lie group symmetries. To do so the paper focuses on non-linear group actions and attempts to discover linear representations in a latent space of an autoencoder. The overall method is termed Latent LieGAN and comes with a theory that attempts to show that the learned symmetry group is actually valid. In practical tests, LaLiGAN was able to recognize the inherent symmetry in high-dimensional data, creating a structured space that can be used for other tasks. The paper also showcases how LaLiGAN can be used to enhance equation discovery and make long-term predictions for different dynamic systems.

### Strengths
This paper studies an interesting problem, which started originally from the seminal work of Higgins et. al 2018. Since then, there has been a large body of work studying automatic symmetry discovery with various results. This paper adds to this body of work by using an adversarial approach which is easy to follow in this context. Unfortunately, I have a negative view of the originality and significance of this work as I outline in the next section but I will say the paper is generally well presented and shows a high degree of polish. The experimental results are quite toy and concocted but they make for good visuals and suggest there is merit in this approach to low dimensional problems.

### Weaknesses
I have several concerns regarding this paper to the point I am confused and question the validity of the entire endeavor. These might be my misunderstanding so I hope they can be clarified in the rebuttal. But as it stands I cannot endorse this paper for the following reasons.

1.) There is a strong emphasis on the non-linear group action aspect in this paper, but I believe this is a bit misguided. This is because the hallmark result of representation theory of Lie groups is that the Lie algebra connects the group to the vector space. Moreover, this can be described by matrices---hence linear representation---and you do not generally need non-linear representations. In practice, however, you can codify non-linear actions (e.g. rotations of 3D objects in a 2D image) and this is where you might want to learn a non-linear action. But I find the emphasis on the non-linear action exaggerated because LaLieGan learns a linear rep in the latent space anyways. I would suggest toning down these claims.

2.) Prop 4.1 seems to not apply to the setup that the authors consider. This is because the encoder and decoder map to a latent space of an autoencoder. This means that the latent dimension can be **lower** than the observation dimension. As a result, $\phi$ and $\psi$ cannot ever be inverses---i.e. bijective---because the information is lost. Thus, I have strong doubts about the value of the proposition. Moreover, many symmetry discovery methods already assume an autoencoder setup. The main difference is that they do not take an adversarial approach so this limits the novelty of the method. Finally, the paper learns approximate inverses anyways so there is no reason to guarantee that the learned representation is an exact Lie group.

3.) One of my biggest concerns is that the approach and results in this paper go against a relatively known result in Linear Symmetry Based Disentanglement by (Caselles-Dupré et. al 2019) who prove that symmetry discovery is impossible without interaction with the environment. This result is a symmetry-based analog to the result by Locatello et. al 2019. Thus I fear that the results in this paper are generally not true, and going beyond the toy datasets considered here might be impossible.

4.) I am confused as to why the authors do not compare with more standard baselines for symmetry discovery. Granted these works often assume knowledge of the group apriori but why this is not the correct test bed? For example $SO(N)$ is done in Fig 2 and 4 of Quessard et al 2020 (you even cite this paper) as well as the main experiment of Caselles-Dupré et. al 2019. Moreover, there has been a lot of development in Deep Delay auto-encoders that extend SINDy. In particular Deep Delay Autoencoders Bakkarji et. al 2023 is an appropriate baseline for the non-linear dynamical system discovery experiments. I encourage the authors to include this baseline as well.

### Questions
See my questions in the weaknesses section.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends LieGAN, which learns linear symmetries within data, to learn non-linear symmetries by integrating an autoencoder. The discovered symmetries/group transformations operate in the learned latent space (instead of in the input space as LieGAN) so that to be nonlinear.

Concretely, It decomposes the nonlinear group transformation into first encoding into the latent space, then linear transform, and lastly decoding back to the original space. It trains an autoencoder to ensure that the encoders and decoders are inverse of each other. It enforces the transformed data still to be in-distribution as the training dataset using a GAN loss.  

The method is shown to learn rotation symmetric latent space for several dynamic systems. The learned latent space is shown helpful for equation discovery in one domain. The discovered equation is simpler and achieves better long-term prediction accuracy.

### Strengths
This paper discusses an important problem: discovering symmetries given the dataset. It is generally well-written and easy to read. 

The method is intuitive, extending LieGAN with the latent space learned by autoencoders. 

The experimental results show promising results in several dynamic systems, including one with a high-dimensional observation space.

### Weaknesses
I am mainly concerned with the practical applicability of this method:
* As discussed in the paper, the nonlinear-symmetric-discovery problem itself is ill-posed, and there are many meaningless "optimal" solutions to it due to the representation power of neural networks. This paper incorporates several patches to alleviate this issue, such as an orthogonal weight matrix in the final layer, and zero-mean of the latent features within an empirical batch. These regularization terms seem strong and hard-coded, and there is no theoretical understanding/analysis of them.
  - Are there metrics distinguishing the qualities of learned symmetries other than human interpretation?
  - Can the model, after applying all these regularization terms, learn all desired symmetries? 
  - Are these regularization terms enough to rule out all meaningless solutions?  
* Similarly, all learned/discovered symmetries in the experiments are rotation-based. Why is that? Is it related to the choice of the regularization? Can the model learn other symmetries in practice? For example, can it learn a nonlinear version of E(n)?
  - If the model can only learn rotation-based symmetries or rotation-based symmetries are enough with powerful neural encoders/decoders, why would we learn the symmetries in the latent space then? 

Some other weakness includes
* The learned nonlinear symmetries are not that interpretable due to the neural encoder;
* It would be great to show an application area of the learned symmetries more than just the learned latent space.

### Questions
* How difficult is it to learn a meaningful nonlinear symmetry using this method in practice? Are there results showing this method learned symmetries other than those rotation-based? Are there results in domains other than the synthetic dynamic systems? 
* Are there more ways to interpret/use the learned symmetries?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
