# Convex Potential Mirror Langevin Algorithm for Efficient Sampling of Energy-Based Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 8, 3, 3

## Abstract
This paper introduces the Convex Potential Mirror Langevin Algorithm (CPMLA), a novel method designed to optimize sampling efficiency within Energy-Based Models (EBMs). CPMLA employs mirror Langevin dynamics in conjunction with convex potential flow as a dynamic mirror map for sampling in EBMs. By leveraging this dynamic mirror map, CPMLA enables targeted geometric exploration on the data manifold, enhancing the convergence process towards the target distribution. Theoretical analysis proves that CPMLA achieves exponential convergence with vanishing bias under relaxed log-concave conditions, supporting its efficiency and effectiveness in adapting to complex data distributions. Experimental results on established benchmarks like CIFAR-10, SVHN, and CelebA showcase CPMLA's enhanced sampling quality and inference efficiency compared to existing techniques.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies mirror Langevin descent algorithm, where the mirror map is the gradient of a convex function. Novel theoretical results are proven for the convergence of this algorithm under weaker assumptions than previously available in the paper "The Mirror Langevin Algorithm Converges with Vanishing Bias", and in a stronger metric (KL divergence). The mirror map is modelled using an input-convex neural network (Amos et al, 2017), which is formulated in a way to guarantee invertibility of the mirror map. This is called CP-Flow. By jointly optimizing the parameters of this network, and performing sampling, an efficient algorithm is obtained for generative modelling, with dramatically fewer parameters compared to other models (this is due to faster convergence because of the preconditioning of the Langevin dynamics with the mirror map).

### Strengths
The paper proposes a very interesting new algorithm for generative modelling based on a combination of input convex neural networks with mirror Langevin descent. There are some new theoretical results showing vanishing bias and bounding convergence rates under weak assumptions. The empirical performance is convincing, especially given the fact that the total number of parameters is much lower than some competing models.

### Weaknesses
The FID scores on the example are not yet competitive with the latest score-based generative models such as NCSN++. Nevertheless, there is a lot of potential in this method, and simply modifications might still significantly improve performance.

In terms of presentation, a better explanation of exactly how is the mirror map function G is found in practice would be useful. We have found section 3.2 too short and difficult to fully grasp.

Section 4.2 is also not sufficiently clearly explained, especially this cooperative learning aspect. It would be important to be precise about the implemented algorithm, if there is not sufficient space in the main paper, you could add this discussion in the appendix.

### Questions
Could you please give more details on exactly how the mirror map function G is found? Do you alternate between exploring the target distribution, and updating G in an adaptive way, or do you fix G in advance before applying mirror Langevin? You seem to mention cooperative learning on page 6, do you mean that G is updated several times after sampling?

In particular, Section 3.2 should be clarified. Section 4.2 is also not sufficiently clearly explained, especially this cooperative learning aspect.
It would be important to be precise about the implemented algorithm, if there is not sufficient space in the main paper, you could add this discussion in the appendix.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel approach for efficiently training and sampling from energy-based models, addressing key limitations such as the challenges in obtaining high-quality samples, which are essential for the training of energy-based models to converge. Additionally, the authors provide valuable theoretical justifications for the convergence of mirror Langevin algorithms within the context of deep neural networks. They demonstrate the effectiveness of their method across several established benchmarks, including CIFAR-10, SVHN, and CelebA, and carefully compare their results with existing approaches.

### Strengths
* The proposed method is well-presented, featuring convincing empirical evaluations and solid theoretical justifications.
* The paper is clearly written and effectively organized.
* The proposed algorithm enhances sampling efficiency from energy-based models without significantly increasing the number of parameters in the CP-Flow component.
* The authors include a comprehensive appendix that provides detailed information on the experimental setups and the theoretical proofs.

### Weaknesses
 * The parameterization of the CP-Flow model in the proposed algorithm appears too constrained, which may complicate the optimization process. Specifically, the requirement for strong convexity with respect to the input x, while theoretically sound, might limit the representational capacity of the CP-Flow. This constraint could hinder the model's ability to capture complex data distributions effectively. Additionally, the authors approximate the Hessian matrix during training using only its diagonal components, and I believe this estimation will become less accurate as the dimensionality increases. This diagonal approximation neglects off-diagonal elements, which capture the interactions between different dimensions of the input space. In high-dimensional spaces, these interactions can be significant, and ignoring them could lead to suboptimal convergence and less accurate gradient updates, especially when the Hessian is not diagonally dominant.


### Questions
I am curious about the efficiency of the proposed method in comparison to the approaches presented in [1] and [2], which are relatively easy to implement for both the toy problems and the image generation tasks discussed in the paper. Notably, these methods seem more relevant to the proposed algorithm than some of the literature cited.

[1] Carbone, D., Hua, M., Coste, S., & Vanden-Eijnden, E. (2023). Efficient training of energy-based models using Jarzynski equality. Advances in Neural Information Processing Systems, 36, 52583-52614.

[2] Du, Y., Li, S., Tenenbaum, J., & Mordatch, I. (2020). Improved contrastive divergence training of energy-based models. arXiv preprint arXiv:2012.01316.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper expects to enhance sampling quality and inference efficiency by introducing the convex potential flow (CP-Flow) to energy-based models (EBM). Different from standard EBM, this paper not only approximates the gradient of log density of target distribution but also considers the SDE path toward the target. The benefits of enforcing the SDE path to optimal transport in this paper lie in decreasing the mixing time of the convergence expected for the continuous version.

### Strengths
1. The motivation for introducing the SDE path requirement to EBM to enhance the sampling efficiency is interesting and reasonable from an intuition perspective.
2. This paper is well written; the intuition, implementation, and experiments are clear.

### Weaknesses
1. The novelty of this paper is not enough; controlling the path of generation with additional models beyond EBM is not novel and is highly similar to the baseline Coopflow. This paper only replaces the normalizing flow (in Coopflow) with mirror Langevin Dynamics.
2. The analysis of this paper does not match their claim:
    1. Theorem 5.5 is only established when the approximation error of EBM and CP-Flow are both 0. That means this analysis does not consider how the approximation error affects the final inference efficiency. Since this paper considers a generative model rather than a sampling algorithm, I think the approximation error is necessary to be considered, just as shown in [Chen2022].
    2. The analysis of Theorem 5.5 does not include any novel technique, which just utilizes the framework proposed in [Vempala2019]  to analyze a sampling algorithm. Moreover, the Fokker-Planck equation is actually given by [Jiang 2021]
    3. Line. 37—Line. 38, authors argue that MCMC tends to get trapped in local modes and has a slow convergence. Actually, the analysis of this paper shows that CPMLA achieves KL convergence with the same gradient complexity as that in unadjusted Langevin Algorithm [Vempala2019] w.r.t. the dimension $d$ and error tolerance $\epsilon$ dependence. Besides, it is worse than underdamped Langevin Dynamics [Zhang2023].
3. The experiment does not show a significant advantage compared with Coopflow. I suggest that the authors provide an FID curve when T is larger than 20. Since the decrease in the tendency of Coopflow is sharper than that of CPMLA, in Table 2, I suggest that the authors also show the performance of CPMLA when T=30.

### Questions
Please check the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors consider the specific sampling problem where the potential is given by some learned energy. This work proposes learning a convex mirror potential alongside the energy-based model for generation, motivated by the optimal mappings given by Brenier's theorem. The authors make two key approximations to computing the convex conjugate of an input-convex neural network, and in computing the Hessian of the optimal mapping. The sampling algorithm boils down to constructing a dual mapping, performing mirror Langevin sampling in the dual space from dual noise, and mirroring back to the primal space.

### Strengths
* The idea of jointly training an energy model along with another convex model to guide training seems new. There seems to be a hidden adversarial learning perspective, where the convex guide model is learned to have large deviation between clean and generated samples, which allows for an intuitive interpretation as "larger gradient steps towards ground truth samples".

### Weaknesses
* (Critical) The algorithm and corresponding theory in its current form are dubious. There is no mention as to how the inverse map $\nabla G^*$ is computed in practice. The theory claims to show convergence of the CPMLA algorithm *during training*, but does not consider the learnable parameters (there is no mention of $\theta$ or $\vartheta$ anywhere), and appears to be a clone of Prop. 3 in Jiang (2021). I suspect it might be possible using techniques from De Bortoli et al. (2021), but this is not considered in this work.

* (Critical) Algorithmically, there seems to be a critical typo in Algorithm 1 on line 284, on the "gradient descent part", where $\nabla f$ is evaluated on an element of the dual space. This appears also in Equation 8 in the starred equality: it should be $\nabla G(\nabla G^* y_t)$ inside the sqrt. This raises some suspicion about how the authors performed the experiments.
* There is a lack of explanation of how the convex conjugate of the network is actually computed. This is explicitly given in the references but is not found in the main text or appendix.
* For the additional amount of computation that is supposedly needed to perform the mirroring, does the CPMLA method outperform standard Langevin methods during test-time, i.e. with a fixed energy model? This should be addressed to accurately consider the practicality of this method.
* Could the authors clarify the motivation behind Eq. 8 and the surrounding exposition as ``practical application'', if the version of MLA used in Algorithm 1 comes from discretizing Eq. 7? Same with the seemingly contradictory paragraph above Algorithm 1. I believe it has to do with the noise distribution $\xi \sim \mathcal{N}(0, \nabla^2 G)$ but I am not sure.
* While theoretically motivated, the practical approximations are hidden away in the text. For example, diagonal Hessian approximation (l.263) is only mentioned once, but is critical to maintaining computational feasibility. The paper could use a paragraph explaining all the approximations made, perhaps somewhere next to Algorithm 1.  
* There is no comparison towards classical MCMC methods when performing sampling from EBMs. However I am unfamiliar with the energy-based-model sampling literature, so perhaps this is not critical.
* Figure 2 appears to have an iteration cut-off at an arbitrarily chosen $T=21$, where it seems that CoopFlow may overtake CPMLA. In the following table, CPMLA is beaten by CoopFlow at $T=30$. While I appreciate that CoopFlow has significantly more parameters which may cause memory concerns, the iteration count is not enough to discern whether the proposed CPMLA is a practical method. There is no comparison towards methods with similar parameter count either.

### Questions
* (Critical) Clarify that the convergence result in Section 5 does not apply to the training, but rather to sampling for a fixed $G$.
* The assumptions required for Section 5 are not complete: $G$ needs to be $\mathcal{C}^3$.
* Please define relaxed log-concavity.
* Please add a motivation as to where $\log \det$ comes from when training CP-Flow, see Huang et al. (2020).
* (Eq 2) The stated ``Langevin Monte Carlo'' is more commonly called the unadjusted Langevin algorithm (ULA). I suggest using ULA and citing the required references. 
* How is $\nabla G^*$ computed? The authors initially claim that you can compute the conjugate using convex optimization, but this does not give you the gradient.
* (l.242) ``conugate''
* Please weaken the claim at the start of Section 5 about convergence of DNNs. This is a special case of general theory.
* (Appendix F) "our work introduces" -> "our work considers", mirror log-Sobolev has already been introduced in Jiang 2021.

### Soundness
1

### Presentation
2

### Contribution
2
