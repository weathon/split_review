# Light Schrödinger Bridge

- Decision: Accept
- Scores: 8, 8, 5, 5, 8

## Abstract
Despite the recent advances in the field of computational Schrödinger Bridges (SB), most existing SB solvers are still heavy-weighted and require complex optimization of several neural networks. It turns out that there is no principal solver which plays the role of simple-yet-effective baseline for SB just like, e.g., $k$-means method in clustering, logistic regression in classification or Sinkhorn algorithm in discrete optimal transport. We address this issue and propose a novel fast and simple SB solver. Our development is a smart combination of two ideas which recently appeared in the field: (a) parameterization of the Schrödinger potentials with sum-exp quadratic functions and (b) viewing the log-Schrödinger potentials as the energy functions. We show that combined together these ideas yield a lightweight, simulation-free and theoretically justified SB solver with a simple straightforward optimization objective. As a result, it allows solving SB in moderate dimensions in a matter of minutes on CPU without a painful hyperparameter selection. Our light solver resembles the Gaussian mixture model which is widely used for density estimation. Inspired by this similarity, we also prove an important theoretical result showing that our light solver is a universal approximator of SBs. Furthemore, we conduct the analysis of the generalization error of our light solver.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Summary
1) The authors propose a novel light solver for continuous SB with the Wiener prior, i.e., EOT with the quadratic transport cost. The solver has a straightforward non-minimax learning objective and uses the Gaussian mixture parameterization for the EOT/SB, which avoids the time-consuming max-min optimization, simulation of the full process trajectories, iterative learning, and MCMC techniques that are in use in existing continuous solvers.
2) The authors show that their novel light solver provably satisfies the universal approximation property for EOT/SB between the distributions supported on compact sets.
3) The authors demonstrate the performance of the light solver in a series of synthetic and real-data experiments, including the ones with the real biological data considered in related works.

### Strengths
Strengths:
- The authors provide a light solver for SB that does not rely on neural network parametrization.
- This work provides a universal approximation for the solver which seems to be rather non-trivial. But to be honest, I'm not familiar with the proof so I'm not sure of the technical depth.
- A minor thing but I really appreciate the authors giving a very clear description of the limitations of the solver.

Following the rebuttal, the authors also provided statistical guarantees for the method.

### Weaknesses
Weaknesses:
This work does not have a finite-time nor finite-sample convergence guarantee. I believe that with additional assumptions one can obtain convergence guarantees as in [1]. Furthermore, there have been multiple works on the sampling complexity of quadratic cost EOT, and given the equivalence between EOT and SB, I believe that obtaining guarantees should be feasible. Specifically, the lack of explicit bounds on the convergence rate with respect to the number of Gaussian components in the mixture model is a significant concern. While the authors demonstrate universal approximation, a practical solver needs to also address how the approximation error decreases as the number of components increases, and how this interacts with the statistical error.

I also think that the experiments are not comprehensive enough. While the results are nice, I'm wondering what is the runtime performance of the light solver against other solvers. I cannot vouch for the method if I don't know how the method would improve in terms of the quality of the result and the computational cost. The current experiments lack a detailed comparison of the computational cost, including wall-clock time, memory usage, and scaling with dimensionality. A more thorough analysis should include comparisons against state-of-the-art solvers across a range of problem sizes and complexities. The experiments should also explore the performance of the solver in more challenging scenarios, such as higher-dimensional problems or those with more complex target distributions.

The authors did mention that the work relies on Gaussian mixture parameterization and the entropic cost. It is indeed a limitation but personally, I think it is fine. Nevertheless, I will still raise this as a potential weakness.

All and all, I like the paper but it does not convince me enough to vouch for its acceptance yet.

Minor comments:
I think the literature on EOT is not sufficient. The authors should include gradient-based EOT solvers such as [2] (both of these methods achieved the optimal O(n^2/eps) complexity, which is stronger than that of APDAGD and seems to have good performance) and a gradient-based entropic UOT solver [3].

### Questions
Questions:
How is this method compared to Langevin dynamics/Langevin Monte Carlo methods in terms of runtime and empirical results?

### Soundness
3 good

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
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
Current SB solvers often have complex neural parameterization and time-consuming training procedures due to minimax. This work proposed a novel parameterization technique and a non-minimax training method to bypass the issues above, with the aim at offering a lightweight and easy-to-use SB baseline.

### Strengths
Strong motivation: the complex neural parameterization and time-consuming training procedures do hinder the application of current SB methods.

Clear presentation: the background knowledge and preliminaries are clearly presented. The connections with important references, such as (Tong et al., 2023), are highlighted and summarized in Table 1. The narrative is highly structural, with words and paragraphs to offer overviews of important sections.

Soundness: the work seems highly self-contained: learning objectives, training/inference strategies, and theoretical properties. Limitations are also well discussed in appendix, some of which are examined through experiments.

### Weaknesses
1. Equation (5) seems incomplete or not well-defined. The equation is a crucial part of the methodology, and its clarity is essential for both understanding the method and replicating the results. Specifically, while the equation states the intention to minimize the KL divergence between the learned policy and the optimal policy, it does not explicitly define how the set of distributions \(\pi_\theta\) is parameterized, making it unclear how this minimization is actually performed. The connection to the subsequent equations (7 and 9) is not immediately obvious, and the lack of a clear definition of the parameter space for \(\theta\) hinders understanding of the practical implementation. Furthermore, the equation lacks context regarding the state and action spaces, which are crucial for understanding the nature of the policies being compared. Without a precise definition of how \(\pi_\theta\) is constructed, the equation remains abstract and difficult to interpret.

2. It is pointed regarding other SB solvers that `they expectedly require time-consuming training/inference procedures.`. The authors state that their method avoids `time-consuming max-min optimization, simulation of the full process trajectories, iterative learning, and MCMC techniques,` which are commonly employed in existing solvers. While this claim holds conceptual interest, empirical evidence to substantiate this would significantly strengthen the paper. The absence of quantitative comparisons, particularly regarding training time and computational cost, against existing state-of-the-art SB solvers makes it difficult to objectively assess the practical advantages of the proposed method. The claim of being lightweight and easy-to-use needs to be supported by concrete data demonstrating a clear reduction in computational overhead compared to existing methods. Without such evidence, the claim remains unsubstantiated.

### Questions
See the weaknesses above.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a fast Schrodinger Bridge (SB) solver based on the parameterization of Schrodinger potentials. SB is a dynamic version of the Entropic Optimal Transport (EOT), and there exists plenty of solvers for these problems, they requires complex parameterization by the form of neural networks / or is sensitive with the entropy regularization parameters, and thus are costly in terms of evaluation on larger scale datasets. The authors of this work propose a solution to this problem by consider a settings where the continuous SB is associated with a Wiener prior (as a reference measure). The key idea is to consider the parameterization of the Schrodinger potential as a mixture of Gaussian, and rewrite the SB optimization objective following this, with easy to compute mean and (scalar diagonal) covariance matrix. The authors provide some theoretical analysis of their algorithm, along with empirical demonstrations on synthetic dataset and realistic dataset (single cell data population dynamic and image-to-image translation).

### Strengths
- Algorithms based on well-studied theory of SB and EOT.
- The paper is well-written with clear structure.
- Well-motivated problem: lightweight solver is much needed for problem that usually requires heavy computational power.

### Weaknesses
 * **Novelty of the paper:** it seems like the paper is just a combination of the two previous works [1, 2]. Admittedly, the authors have clearly elaborated in their paper of such cases, but I do not see the clear novelty in the methodology part. Even on the proof of the universal theorem of the Gaussian mixture model, one can see that half of it is straightforward calculation from the two aforementioned paper.  
* **Unclear benefit the of LightSB solver in realistic setting:** for the single cell dataset using W1 distance as a metric, LightSB's performance leaves some gaps with the two best methods, however I do not see author's comment about this. The other benchmark on unpaired image-to-image translation is very hard to judge, as for this task there is no quantitative metric to compare with other solvers. I do not know why the authors omit unconditional image generation tasks, as this is an important and popular benchmark that has FID as a standard metric. Morevoer, there have already exist results on some of the neural EOT solvers or the diffusion SB solver (using iterative proportional fitting)/diffusion SB matching (using iterative Markovian fitting), or flow matching/rectified flow in this task, so it is easy to compared with the baseline. 
*  **Questionable theoretical result:** in the proof the universality of the Gaussian mixture parameterization for SB (theorem 3.4), in the paragraph below equation (29), I fail to understand why the authors wrote 

> "Besides, it also has scalar covariances of its components because multiplier $exp(− |x_1|^2 /2\epsilon )$’s covariance is scalar itself" 

, but what I understood in the paper's settings is that $x_1 \sim \pi_1$ is an unknown distribution, without assumptions on its parametric form. This is a key argument, as without it the factorization failed to be what the authors claimed in the statement of the theorem, I hope the authors could clarify this to me, otherwise it would be a hole in the proof of an important analysis of the paper.    

### Questions
See weaknesses section.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel method to approximate the Schrödinger Bridge problem. Following the connections of the Schrödinger Bridge problem to entropic optimal transport, the authors want to learn the true entropic OT plan. They parametrize the optimal entropic OT plan as the product of two probabilities, the source measure $p_0$ and a conditional plan $\pi(x_1|x_0)$ (up to a normalization constant). Following this novel parametrization, they show that they can optimize the parametrized plan without the knowledge of the true entropic OT plan. To deal with the normalization constant, they use a mixture of Gaussian representations to get a tractable form of each of the components. They then explain the inference and training procedure. Finally, they perform several experiments to show the practicability of the proposed method (2D synthetic data, an EOT benchmark, single-cell dynamics and unpaired image-to-image experiment).

### Strengths
i) The parametrization of the entropic OT plan is novel (to the best of my knowledge) and interesting.

ii) The derived loss is very interesting as learning the parametrized model does not require knowing the true entropic OT map.

iii) The discussion on the normalization constant and the proposed parametrization (with a mixture of Gaussians) to overcome this issue is appealing (even if the computation of the normalization constant is based on existing works).

iv) The method has been tested in different experiments.

v) The paper is clear and easy to read.

### Weaknesses
1. In the single-cell experiments, the competitor results are taken from another paper [Tong et al., 2023]. As the evaluation is performed on a leave-one-domain out and training on the others, it is questionable that the training procedure was the same. I believe that some of these competitors should be reproduced by the authors to ensure that the training setting is similar, especially as the unpaired image-to-image experiment is a quantitative experiment without competitors.

2. The experiments were performed in a relatively small dimensional setting: the unpaired image-to-image experiments used a pre-trained feature extractor of dimension 512, the single-cell data experiment used the representation of the 5 whitened principal components (ie dimension of 5), and the EOT benchmark data were (at most) of dimension 128. Therefore, the question of the performance of the proposed method in high-dimensional data is legitimate, especially as the authors use a mixture of Gaussian representation.

3. Little is said about the statistical estimation (with respect to the data dimension and sample size) of the proposed parametrization to the true entropic OT plan $\pi^\star$. It is known that it also suffers from the curse of dimension [2,3]. Specifically, the paper lacks a discussion on how the number of Gaussian components in the mixture model impacts the approximation quality and the statistical error of the estimator. The trade-off between the number of components, the data dimension, and the sample size is not addressed, which is crucial for understanding the practical applicability of the method.

4. Some related work is missing and should be discussed and mentioned [1,2,3,4]

### Questions
1. How does your method depend on the dimensionality of the data? I think that this is a legitimate question, especially with the normalization constant being approximated by a mixture of Gaussians. I recommend adding more dimensionality in some experiments (like single-cell by considering a larger number of principal components. Maybe 5, 50, 200, 500, 1000?) to study how the proposed method performs as the dimension grows. I also recommend adding this discussion to the limitation paragraph in Appendix E. 

2. On the single-cell experiment of the unpaired image-to-image experiment, could you show the training speed to reach convergence and the number of iterations it took? I checked the appendix and I did not find such plots. Maybe it would be interesting to compare to other OT solvers (sinkhorn or stochastic variants) on a simple problem to see the different behaviour. (I acknowledge that the Sinkhorn solvers are only usable in a discrete setting.) 

3. I found the limitation discussion in Appendix E interesting and it could have been in the main paper. I recommend moving it to the main paper. Maybe some discussions about related work could go in the appendix instead. 
 
I am ready to reconsider my score if the authors can reproduce some of the competitor results and consider the highest dimensional setting of single-cell data experiments (dimension of +1000). It will depend on how well the proposed algorithm will behave on medium dimensionality.


----- EDIT POST REBUTTAL -----

Thank you for your answer. I have read the rebuttal.

[Single-cell experiments] Thank you for the novel experiments on the single-cell trajectory problem. I find them interesting and encouraging, especially with the different dimensions. 

I understand the motivation for using a different metric than W_1 to compare the different approaches. However as it is not the standard metric, it is hard for me to compare your method with other standard single-cell trajectory methods. As the authors-reviewer discussion has ended (due to a late rebuttal submission), I would have appreciated seeing the Wasserstein 1 metric for the different approaches. Indeed, the novel dataset was first considered by [Tong et al., 2023] where they used the W_1 distance. As the authors did not reproduce their method with the considered metric, it is hard to compare with more standard approaches on single-cell datasets like ODE/SDE-based approaches [Tong et al., 2023]. Unfortunately, two of the considered competitive methods are not standard in the single-cell trajectory literature. Therefore, I still think that the experimental section lacks reproduced competitors especially as the metrics are different.

[Novel theoretical section] Thank you for the novel appendix H. It brings some light to the proposed methodology. I suggest the authors include Theorem H.1 in the main paper.

In my opinion, this is a borderline paper. I acknowledge that the proposed approach is new and interesting but I still think that it lacks a more rigorous experimental section to understand its practical performance with the current literature. Therefore, I will keep my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a fast, light-weighted, solver for Schrödinger bridge by using a Gaussian mixture parametrization on the energy potentials. This simplifies computation of the static EOT map that would otherwise be intractable, resulting in efficient learning process. Extensive experiments are conducted on low/mid dimensional benchmark, single-cell dataset, and unpaired image translation in latent space.

### Strengths
- The proposed method is notably simple and elegant. It effectively combines key insights from previous works and elevates them to address a significant problem within the SB community.

- The paper is well-written, and the thorough comparison to related works, especially in Table 1, is particularly valuable. Additionally, the comprehensive discussions in the appendix about limitations and broader impacts are appreciated.

### Weaknesses
 - The proposed method on image dataset requires pretrained latent space (512 dimension) that is already structurally informative.

- On the discussion of tractable / real-world SB given pairing, a few important references such as "Aligned SB" and "image-to-image SB" are missing. 

- Given that the proposed method is computationally light weighted, it'll be beneficial to have some quantitative comparison (actual runtime, memory etc) to prior works.

- All "Schrodinger" should be changed to Schrödinger.

### Questions
- Can the author provides image experiments without the latent space? I suggest smaller dataset such as AFHQ 32 or 64 for faster evaluation given the limited rebuttal period. Otherwise, can the author provide and include discussions on the scalability of the proposed method? Given Thm 3.4, it seems like the method could be applied to these scenarios.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
