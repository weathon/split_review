# Simple ReFlow: Improved Techniques for Fast Flow Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Diffusion and flow-matching models achieve remarkable generative performance but at the cost of many sampling steps, this slows inference and limits applicability to time-critical tasks. The ReFlow procedure can accelerate sampling by straightening generation trajectories. However, ReFlow is an iterative procedure, typically requiring training on simulated data, and results in reduced sample quality. To mitigate sample deterioration, we examine the design space of ReFlow and highlight potential pitfalls in prior heuristic practices. We then propose seven improvements for training dynamics, learning and inference, which are verified with thorough ablation studies on CIFAR10 $32 \times 32$, AFHQv2 $64 \times 64$, and FFHQ $64 \times 64$. Combining all our techniques, we achieve state-of-the-art FID scores (without / with guidance, resp.) for fast generation via neural ODEs: $2.23$ / $1.98$ on CIFAR10, $2.30$ / $1.91$ on AFHQv2, $2.84$ / $2.67$ on FFHQ, and $3.49$ / $1.74$ on ImageNet-64, all with merely $9$ neural function evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies ways of improving the ReFlow procedure for diffusion and flow matching. They break the design space into training dynamics, learning and inference, and show isolated ablations w.r.t. the choices here (weighting, time distribution, loss function, initialization, dropout, sampling, ODE solvers, [0, 1] discretization). The main experimental results ablate these on CIFAR10, AFHQv2, and FFHQ.

### Strengths
I find the paper well-presented. The design space is clearly communicated and the ablations are convincing. These dimensions show how to squeeze the performance on these standard image generation settings.

### Weaknesses
I do not find many weaknesses in the paper, as it clearly communicates the goal and setting and explores it nicely:

1. The experimental settings of CIFAR10, AFHQv2, and FFHQ are interesting, but only a small subset of all of the other potential uses and larger applications of flow matching and diffusion models. It would be interesting to see if the improvements continue holding in these.
2. The paper is niche in the sense that it relies on wanting to do generative modeling with ReFlow, and discussing the relevant dimensions here.

### Questions
None

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
This paper provides an empirical study of how to improve the FID of rectified flow based image generative models. They aggregate a number of design choices studied in the context of diffusion and reconsider them in the context of flow matching and rectification. These design choices focus on the various aspects of the loss function: the metric under which the regression is performed (e.g. MSE vs PIPs, vs generalized invertible mappings), the time weighting, and loss normalization. They then consider training choices, like how the training data is chosen based on the first deterministic coupling of the rectification (fixing a Gaussian base value for each data point, called forward pairs). Finally they run ablations over discretizations of the ODE.

### Strengths
The paper provides a number of useful empirical studies of what ultimately influences the performance of the flow matching models and when they are rectified to straighter paths. As the reviewer sees it, the paper aggregates many of the design space choices that arise from the diffusion model literature and uses them to study how these knobs affect flow matching. It is nice to have them all considered in one place. 

The inclusion of a new high pass filter metric on the loss is nice, and could be well motivated in other domains where we explicitly know these frequency regimes are important, e.g. for generative models in the sciences.

The extent of the ablations is thorough and the reviewer acknowledges the size of this experimental undertaking!

### Weaknesses
Thanks to the authors for their hard work on this project.

*Main remarks*:
- While the paper provides a number of empirical insights for training, it would be nice if there was more of an analysis of why these tricks ultimately help. The reviewer stresses this a bit because a number of the proposed innovations are directly inspired from their application in other work, e.g. the improvement of loss normalization in Karras et al (2023b), and e.g. equations (8)-(12). Specifically, the paper lacks a deeper investigation into the underlying mechanisms that cause these modifications to improve performance. For example, while loss normalization is shown to be effective, the paper does not provide a theoretical justification for why normalizing the loss with respect to both $x_t$ and $t$ is superior to other normalization strategies, or why the specific form of the time-dependent scaling is optimal.

- The reviewer is confused by the reference to OT solutions throughout, e.g. in Section 3.3.1, which suggests a potential misconception about the rectified flow procedure. In particular, as the reviewer understands it, one iteration does not give OT, but instead gives a monge map, in the sense that the coupling $P(x_0, x_1)  = P_0(x_0) \delta(x - T(x_0))$, where $T$ is the transport endowed from learning the velocity field first with $x_0, x_1$ independently drawn in the loss. This is certainly not OT (brenier polar factorization theorem), but is a deterministic coupling. Can the authors address this? 

- The argument of proposition 2 is confusing, perhaps due to a typo. Is the first line supposed to specify the DM loss and not the GFM loss? Currently they are both statements about GFM. The lack of clarity makes it difficult to assess the validity of the proposition and its implications for the overall method.

- These analyses are mostly limited to the image domain, and it's hard to understand how any of these apply to other domains. The paper does not discuss the potential limitations of the proposed techniques when applied to data with different characteristics, such as time-series data or point clouds. The lack of discussion on the generalizability of the approach is a significant limitation.

- Can the authors address how large the bias is in rectification under the different procedures somehow? By this, the reviewer means that each iterate of rectification introduces a bias unless the flow was initially learned perfectly. The reviewer understands this to be difficult to measure, but it would be nice to understand how these ablations affect or relate to the extent of this bias. This might sit better in the questions section.


*Small remarks*:
-  the fundamental idea of of FM and rectified flow are equivalent to the method of stochastic interpolants, and should probably be cited accordingly. 
- There is in a sense a competing small set of remarks about the benefits of rectification vs distillation in the appendix section C, saying that there are benefits of rectification over distillation because rectification maintains an ODE-like structure. But this ignores the fact that the learning problem after a rectification is a distillation problem...and it too is now fitting to an imperfect teacher model. I'm not sure this remark really contributes much to the discussion.

*Very small remarks*: A few typos to watch out for. 
- "we  we" top of page 5

### Questions
The reviewer is trying to understand the language of the following claim in 3.3.1:

"Our improvement. We observe that learning the OT ODE is a harder task than learning the diffusion
probability flow ODE. For instance, at t = 1, the optimal DM denoiser only needs to predict the data mean $\mathbb E_{x_0 \sim P_0} [ x_0] $ for any input $x_1 ∼ P_1$, but an optimal ReFlow denoiser has to directly map noise to image along the bijective OT map."

Should the reviewer interpret this as being the claim that: The velocity field solving the probability flow is generically for $\mathbb E[\dot x_t | x_t = x]$, and for a deterministic coupling $P(x_0, x_1) = P_0 (x_0) \delta (x - T(x_0)$, this conditional expectation collapses because only one $x_t$ passes through $x$? This would be true for any monge coupling, and not just the OT coupling.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes several improvements to training dynamics, learning, and inference for Rectified Flow models (e.g. initialization from the EDM model, loss reweighting, new loss function, refinements on noise-image pairs, etc.). Thorough ablation studies verify the effectiveness of the proposed improvements and the final experiment results are competitive among diffusion and flow-based models for few-steps sampling.

### Strengths
1. The paper is well-written and easy to follow, with each step of the ablation study clearly described and the results effectively presented.
2. The final experiment results after combining all improvements show lower FID and lower straightness compared with other diffusion-based and flow-based methods.

### Weaknesses
1. The projected pairs operation, which projects the coupling $Q_{01}^1$ to $\Pi(P_0, P_1)$, complicates the training pipeline (GAN training and solving Sinkhorn) while yielding only marginal performance improvements, as indicated in Table 6 (with a maximum FID improvement of 0.02, which is not even statistically significant). The computational overhead of this step, involving both a GAN training procedure and the Sinkhorn algorithm, seems disproportionate to the observed gains, especially given that the FID improvement is not statistically significant. Furthermore, the paper does not clearly discuss the sensitivity of this step to hyperparameter choices within the GAN training or the Sinkhorn algorithm, which could further impact its practical utility.

2. The authors frequently use the notation 'OT ODE' and 'OT map' throughout the paper. However, as noted in references [1] and [2], the iterative rectified flow does not generally converge to the optimal transport mapping in dimensions higher than or equal to 2. Furthermore, the algorithm presented in this paper corresponds to the 2-rectified flow. Therefore, the use of the 'OT' notation is not appropriate. The paper should be more precise in its terminology, especially when discussing theoretical concepts like optimal transport, and avoid using terms that could mislead readers about the actual properties of the method.

### Questions
I do not have other questions.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work addresses the performance degradation of ReFlow without violating its theoretical foundations. ReFlow aims to straighten the trajectories of ordinary differential equations (ODEs) by flow-matching between marginal distributions connected by a previously trained flow ODE. Theoretically, an infinite number of ReFlow updates should result in a straight trajectory that enables perfect translation between marginals with a single function evaluation. However, in practice, ReFlow suffers from a drop in sample quality, and previous attempts to mitigate this have relied on heuristic methods like perceptual losses, which deviate from the theoretical framework and may not preserve the underlying probability distributions.

The authors generalize the ReFlow training loss and categorize design choices into three key groups: training dynamics, learning, and inference. They analyze previous practices, identify potential pitfalls, and propose improved techniques within the theoretical bounds. Extensive ablation studies on datasets such as CIFAR10, FFHQ, and AFHQv2 demonstrate that their methods consistently improve sample quality and Fréchet Inception Distance (FID) scores. Ultimately, they achieve state-of-the-art results in fast neural ODE-based generation without relying on heuristic methods, offering a theoretically sound and practical approach to accelerating generative models.

### Strengths
- The paper does a very good job at ablating design choices to improve ReFlow. 
- The experimental results are state-of-the-art, by a good margin.
- The paper can be very helpful for practitioners that face similar choices when training their models.

### Weaknesses
 - Each of their contributions may be labeled as incremental, which means that the whole paper could also be labeled as incremental. Regardless, it is a very valuable paper to the community because it sheds light on several empirical choices one must make.

- The statement “This again ensures that the loss is minimized when $D_{\theta}$ outputs the posterior mean” in line 184 is false. In fact, what holds is 
$D^*(x_t,t) = \phi^{-1}(\mathbb{E}_{x_0 \sim Q(\cdot|x_t)} [\phi(x_0)])$.
When $\phi$ is far from the identity, $D^*(x_t,t)$ may be far from the desired point. This does not makes the empirical findings less valuable, but it does invalidate the theoretical claims that the authors make about the training loss based on $\phi$ adhering to FM theory.

### Questions
- As described in lines 100-111, the original ReFlow algorithm works by iteratively training $D^{n+1}$ using the coupling induced by $D^{n}$. Does Simple ReFlow proceed analogously? If so, how many iterations are used? It would be good to include this information in the paper.

- The authors propose two improvements with regards to training data: forward pairs and projected pairs. Hence, there are three ways to obtain trajectories: backward pairs, forward pairs and projected pairs. How are the three approaches combined? For example, what is the approach used to obtain the results in Table 8?

- The projected pairs approach is very interesting. The authors propose one way to solve the projection problem, which involves recasting the constraint on the marginals of $\Gamma_{01}$ as a penalty term, which forces them to use GANs. It seems that solving a Schrodinger bridge problem between P_0 and P_1 with an appropriate regularization term would also achieve the final goal of the paper, but of course one then loses the connection with ReFlow. Are there other alternatives that may be simpler? Also, it would be good to provide a more detailed explanation in Subsec. D.3, e.g., more details in how problem 42 is solved.

- What do the authors think is the improvement that is most responsible for the performance boost that is observed? As a reviewer, I think the training data improvements may be the most critical ones, but it would be nice to comment on that in the Conclusion section.

### Soundness
3

### Presentation
3

### Contribution
3
