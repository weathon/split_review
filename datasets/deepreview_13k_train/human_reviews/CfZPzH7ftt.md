# Improving Neural Optimal Transport via Displacement Interpolation

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Optimal Transport (OT) theory investigates the cost-minimizing transport map that moves a source distribution to a target distribution. Recently, several approaches have emerged for learning the optimal transport map for a given cost function using neural networks. We refer to these approaches as the OT Map. OT Map provides a powerful tool for diverse machine learning tasks, such as generative modeling and unpaired image-to-image translation. However, existing methods that utilize max-min optimization often experience training instability and sensitivity to hyperparameters. In this paper, we propose a novel method to improve stability and achieve a better approximation of the OT Map by exploiting displacement interpolation, dubbed Displacement Interpolation Optimal Transport Model (DIOTM). We derive the dual formulation of displacement interpolation at specific time $t$ and prove how these dual problems are related across time. This result allows us to utilize the entire trajectory of displacement interpolation in learning the OT Map. Our method improves the training stability and achieves superior results in estimating optimal transport maps. We demonstrate that DIOTM outperforms existing OT-based models on image-to-image translation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel method (DIOTM) to solve the optimal transport mapping problem for the quadratic transport cost (Wasserstein-2 OT) with neural networks. The approach is ideologically inspired by the previous works in the field which solve the dual (semi-dual) optimal transport problem by approximating an OT map and the dual potential (a.k.a. discriminator) with neural networks and optimizing them in the GAN-style adversarial manner (max-min).

The key innovative thing in the current paper lies in exploiting the properties of the W2 OT maps. They are related to the displacement interpolation linear interpolation from the input distribution to the target using the OT map). More precisely, the authors formulate the (semi-)dual problem for finding the displacement interpolation for a given time moment t in (0,1) which requires optimizing a particular t-dependent dual potential. Then they group all these problems together and obtain a dual problem when they have to optimize over one t-conditioned dual potential (and also additional t-dependent transport maps). In principle, each problem for different t can be viewed as independent, but

1) The authors note that after some reparameterization, the t-dependent dual potentials should satisfy the Hamilton-Jacobi-Bellman (HJB) condition. At this point, the authors propose to incorporate the HJB-inspired regularization into the optimization, which helps connect optimization problems for each t together.

2) The authors note that the optimal transport maps at each time moment t are connected with each other. In fact, they all can be expressed through each other and through the main transport map (from source to target). As a result, the authors use restricted parameterization where all these t-dependent maps are parameterized through a single map.

The resulting algorithm is a (simulation free) bi-directional max-min adversarial training scheme. The authors demonstrate the superiority of the proposed technique compared to previous dual form neural optimal transport solvers & their regularization techniques through a series of experiments (toy 2D data + image-to-image translation).

### Strengths
1) The idea of exploiting the displacement interpolation overall looks interesting and fresh. To my knowledge, it has not been actively studied in the field, so I believe that further developing it may be interesting and fruitful for the community of adversarial/dual-based OT methods. Overall, the contribution of this paper looks as significant for the neural OT field, as WGAN-GP improved WGAN.

2) The HJB based-regularization proposed here seems to be very natural and unbiased in the sense that it looks theoretically justified and does not bias the resulting solution. This is not the case for other GAN-based regularizing techniques which appear in related works (like R1 or other gradient penalty regularizers). However, for me it is still not clear from the main text if the authors in their method use only HJB or HJB+R1. This should be clarified.

3) The experimental comparison on unpaired Image-2-Image looks rather convincing and supports the main claim that HJB regularizer is useful for stability and works (I deduce this from the results of comparison with various dual OT methods).

4) The text is overall readable and the clarity is ok (although sometimes the amount of the bolded text is too annoying).

### Weaknesses
1) I believe that there might be a theoretical gap in the proposed DI-OTM approach which lies in the restricted parameterization of the t-dependent transport maps. Specifically, each transport map (for a particular t) should be parameterized the way that it should solve the corresponding inner conjugation (c-transform) minimization for a particular corresponding dual potential (for time t). However, when the authors tighten all the transport maps together via a single function, this may not hold and may spoil the theoretical validity of the proposed semi-dual form. This aspect should be discussed in more detail. The authors should clarify if the parameterization of the transport maps as a linear interpolation between the source and target domains is a constraint or a result of the optimization procedure. If it is a constraint, then the theoretical justification becomes questionable as it forces a specific structure on the transport maps that may not be optimal for the given dual potential at each time t. This could lead to a suboptimal solution compared to a more flexible parameterization.

2) I think that some of the results presented here are not completely novel and the authors miss a large set of related work. The key problem which is exploited in the current work is the displacement interpolation optimization (equation 8). In essence, this is the Wasserstein-2 barycenter problem and, to my understanding, it has already been well studied both in theory and in practice. For example, the W2 dual barycenter problem (equation 9 in theorem 3.1 in the current paper) has been derived in the founding work [1], see their derivations around proposition 2.2. The semi-dual version (which is the second part of theorem 3.1 in the current paper) seems to directly follow from the general semi-dual for barycenters which has been recently introduced in [2] (theorem 4.1). I think these relations to the barycenter literature (theoretical and computational) should be clearly clarified and the related literature should be included. The authors should explicitly acknowledge that their formulation is a specific instance of the Wasserstein barycenter problem and discuss how their approach relates to existing methods for solving barycenter problems, particularly those that also use neural networks.

3) The DIOTM approach proposed here seems to work only for the quadratic cost optimal transport (and may be for some lp-based OT as well) due to reliance on the displacement interpolation properties. It looks like it can not be generalized to more general OT formulations, e.g., formulations with non-lp transport costs. This point is more a limitation than a weakness as the authors specifically target the quadratic cost OT. Nevertheless, it should be mentioned in the paper and the background considers the general cost OT.

4) While the authors claim that they significantly improve the accuracy of solving OT, they omit detailed evaluation of this aspect in high dimensions. The experiments in 2D are good but do not convincingly support the claim, more advanced and high-dimensional evaluation should be considered [3] and some recent baselines should be included like [4]. The image-to-image translation task, while high-dimensional, does not directly measure the accuracy of the OT map itself. The authors should include experiments that explicitly evaluate the quality of the learned transport map in high dimensions, such as comparing the learned map to a known ground truth or using metrics that directly assess the transport quality, like the Sinkhorn divergence between the transported source and target distributions.

5) Some of the theoretical statements are not very mathematically rigorous. For example, the authors prove some results regarding the optimal dual potentials (like eq. 10/11), but do not explain to which functional spaces they belong. If I correctly get it from the proof, they should be continuous functions. Does the supremum among the continuous functions is achieved, i.e., are f* also continuous functions?

### Questions
I think the ideas in this paper are very interesting and should be presented to the community. My current score is based on the current condition of the paper but I may adjust it if the authors carefully reply to the weaknesses which I raised and revise the paper accordingly. Also, I have some additional questions:

1) What is the point of introducing alpha? The OT map/displacement maps should be the same for all alpha, right?

2) Could you please provide some analysis of the time sampling schemes (line 294)? In diffusion models, this is an important aspect, so I believe it may be important here as well and at least some analysis should be provided. For example, you can consider a scheme where t is mostly samples closer to 0/1 and the other scheme where t is concentrated around 0.5 and show the results.

3) It looks like the training curves (figure 5) present the losses which are generally not very representative in adversarial learning. Could you please provide FID(epoch) plots to see how stably your method converges compared to the baselines? This would be much more convincing.

4) Most comparisons are quantitative through FID which does not measure optimality but only measures matching the target. Could you please provide a side-by-side qualitative comparison with the baseline in I2I tasks? It would be nice to see how your trained generator preserves the content compared to the baselines.

5) Could you please run your method in some I2I experiment several times. Does it converge to roughly the same solutions (qualitatively), i.e., recovers (nearly) the same map (which should be optimal)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a theoretically justified method for the computation of dynamic optimal transport using the theory of Displacement Interpolation. The authors derive a dual formulation of Displacement Interpolation. They show that the optimal potential for solving the dual problem satisfies the HJB equation and incorporates the HJB equation as a regularizer for the training of the proposed method. The method is validated on synthetic datasets - G->8G, G->25G, Moon->Spiral, G->Circles - and several image-to-image translation problems - Celeba and Wild->Cat. The proposed method achieves the best FID among considered competitors CycleGAN, OTM, NOT, DSBM, and ASBM for image-to-image translation problems and outperforms closely related OTM method on most synthetic datasets in W^2 distance.

### Strengths
1. The method has a derivation of the dual problem for displacement interpolation, which opens the possibility of numerical optimal transport computation from the perspective of the Benamou-Brenier dynamic transport formulation.
2. Experiments on toy examples and image-to-image translation problems show that the proposed method achieves good numerical results over competing methods for optimal transport computation and is scalable to image problems. 
3. The paper proves numerically that the HJB regularizer improves the training procedure and is better than the OTM and R1 regularizers. This regularizer seems to be novel in the literature of numerical optimal transport computation.

### Weaknesses
1. The method doesn't compare to closely related flow-based optimal transport methods, such as Rectified Flow (Flow straight and fast: Learning to generate and transfer data with rectified flow, ICLR-2023) and Flow Matching (Flow Matching for Generative Modeling, ICLR-2023). While the authors focus on exact OT map learning, the absence of comparison with these methods, which also address transport through velocity fields, is a notable gap. These methods, despite not directly computing the optimal transport map, offer alternative perspectives on learning transport and should be included for a comprehensive evaluation.
2. The paper lacks a visual comparison for image-to-image translation problems between different methods and a discussion of why competing methods perform worse. It is not sufficient to only report FID scores; visual examples are crucial for understanding the qualitative differences in the transformations. The paper should provide a detailed analysis of the failure modes of competing methods, explaining why the proposed method achieves better numerical results despite similar visual results.
3. It is not clear how well the method computes optimal transport in high dimensions. The evaluation on 128x128 images, while substantial, doesn't fully address the scalability of the method to very high-dimensional spaces. The authors should evaluate their method on the Wasserstein-2 benchmark (Do neural optimal transport solvers work? A continuous Wasserstein-2 benchmark, NeurIPS-2021) or similar high-dimensional benchmarks to rigorously assess its performance in such scenarios.

### Questions
Questions:
1. It looks like in Eq. 6 the integration should be over $x$ instead of $d\rho_ {t}$, and $\rho_ {t}(x)$ should be under the integral. Can you comment on this?  
2. Can you clarify how long it took you to train your methods for image-to-image translation problems compared to competing methods? 
3. What is the number of parameters used by all the methods for image-to-image translation problems? Are they comparable?
4. Have you experienced failures of your method, and if so, can you provide them?
5. Can you provide an evaluation of your method on the Wasserstein-2 benchmark to show that the method is capable of solving optimal transport in high dimensions?
Typing errors:
1. Line 49 - double "the"; one should be deleted.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper builds on displacement interpolation in Optimal Transport (OT) and introduces a time-derivative HJB regularizer, enhancing training stability. The training of the model is based on min-max optimization similar to GAN. It achieves state-of-the-art results on both synthetic data and image-to-image translation tasks w.r.t $W_2$, $L_2$ and FID score.

### Strengths
1. The paper presents comprehensive and detailed theoretical derivations, with notable innovations within the OT framework. It leverages the dual formulation of displacement interpolation to derive a new min-max optimization function.

2. In terms of experimental performance, the proposed HJB regularizer is effectively insensitive to the hyperparameter $\lambda$, performing better than other regularizers such as R1 and OTM. And DIOTM outperforms other benchmarks and exhibits more stable training.

### Weaknesses
1. The motivation behind the theoretical innovation is unclear. There is no analysis explaining why decomposing the optimization of $T_\theta$ in OTM into optimizations for forward $\overrightarrow{T_\theta}$ and backward $\overleftarrow{T_\theta}$ improves training stability.

2. The experimental results in Table 2 appear unusual. I couldn't find related experimental setups for the benchmarks, and some references don’t report similar experiments or use different resolution datasets. Since the FID scores for these benchmarks couldn’t be directly cited, how were these results obtained? Were all models trained for the same number of steps? It would be beneficial to add an ablation study of FID vs. training steps.

3. The paper argues that DIOTM is more stable than OTM, but Fig. 5 shows that OTM remains stable for the first 40K steps before experiencing a sudden spike in loss. What caused this increase? If the loss curve does not decrease further, why train for 60K steps rather than 40K?

4. The paper only provides visualizations for DIOTM, making it hard to compare visually with baselines. The DSBM paper’s wild-to-cat results at 512x512 resolution look much better than those in Fig. 2, yet its FID score in Table 2 is much higher. Could the authors clarify this discrepancy?

### Questions
Refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new method to estimate the optimal transport map between two distributions - a source and a target. The proposed method, called Displacement Interpolation Optimal Transport (DIOTM), leverages displacement interpolation which is the optimal solution of a particular dynamic formulation of OT with quadratic cost. The core component of the training algorithm for DIOTM involves a min-max loss objective, similar to GAN framework. This min-max objective is derived from the dual problem of the original minimization problem of displacement interplant. The expression involves a supremum over two potential value functions which can be combined into a single potential value function. These potential functions play a role similar to discriminators in GANs and the transport maps are similar to generators. In addition, the regularization term of the loss objective is derived from Hamilton-Jacobi-Bellman (HJB) optimality condition of the value function. The training algorithm involves alternately updating the potential value function and  the two transport maps. The paper shows applications of the proposed approach on image-to-image translation on datasets such as Male $\rightarrow$ Female (64$\times$64, 128$\times$128), Wild $\rightarrow$ Cat (64$\times$64), etc.

### Strengths
**Writing**: The paper is well-written. It provides sufficient background on major concepts involved in DIOTM such as displacement interpolation. The core algorithm has been explained well and the underlying theoretically motivation has been explained well.  

**Quality and significance**: Improving stability of Optimal transport is an important problem and this paper proposes a method to addresses it. 
- The experimental results on simple 2D toy datasets seem to indicate improved performance compared to prior methods as indicated in Table 1.  
- DIOTM seems to outperform other optimal transport based models on image-to-image translation task in terms of metrics such as FID (Table 2).
- The proposed HJB regularizer seems to help with improved training dynamics (Figure 5). Further, HJB regularizer seems to be less sensitivity to the choice of regularization hyperparameter  (Table 3) which is a desirable property.

### Weaknesses
1. This method trains two optimal transport maps from source to target distribution and vice versa which is a bit inefficient. Further, there are no experiments which demonstrate that the two independently trained transport maps are invertible, which they should be theoretically. How does source -> target -> source reconstruction perform on various datasets in the paper? Similarly, target -> source -> target reconstruction on images should be reported with a metric such as l2 error/reconstruction error.
2. Qualitative Results: The paper should Include qualitative comparison with other methods on Image-to-Image translation baseline. FID doesn’t necessarily capture lot of semantic and perceptual information of images. A better comparison would be side-by-side comparison of images obtained from DIOTM and previous OT benchmarks.
3. Quantitative results: Table 2 compares DIOTM with existing neural optimal transport models. For the sake of completeness, the paper should include another table that includes other state-of-the-art methods (e.g. GANs[1], flows as well as diffusion-based methods (e.g. Wang et al. [2]) for image-to-image translation task so that reader gets an overall picture of the landscape and the gap of DIOTM from SOTA method. I would like to reiterate that it is completely alright if DIOTM is not SOTA overall, compared to other methods for I2I task, but such a table should be included, as it is a standard practice.
4. Implementation details: The paper is missing some of the implementation details, specifically architecture details of networks for image-to-image  translation task. Further, the number of images used to calculate FID is unclear.
5. The largest image resolution considered in this work is 128X128 which is not very large. In order to reliably evaluate scalability, larger resolutions such as 256X256 or 512X512 should be considered. See Isola et al. [1] for a list of potential datasets for image-to-image translation tasks on larger resolution.

### Questions
1. Training stability: Can we have multiple curves to understand how frequently the training diverges for OTM? Also, how sensitive is training of OTM to various hyperparameters?
2. What are some practical constraints on the source and target distributions when trying to learn an OT map with DIOTM? Can it learn OT map in the cases where the distance between the source and target distribution might be large? For instance, prior works in this space consider more complex datasets/tasks for image-to-image translation such as mask-to-image synthesis (COCO / ADE-20K), sketch-to-image synthesis, day-to-night, summer-to-winter, colorization etc. 
3. The results of Figure 11 seem much more suboptimal than other cases (with multiple faces) etc. What could be the reason for more failures for this  pair of distribution?
Minor:
- Line 243: typo - parametrization
- Line 253, 256, 258: Consider using different parameter notation e.g. $\overrightarrow{T}_\theta$ and $\overleftarrow{T}_\tilde{\theta}$ for the two transport maps, as these are parametrized with two different networks with different parameters. This would make it clear that these two networks are trained separately, as opposed to using a shared network. 
- Repeated citation for Diffusion Schrodinger bridge matching paper.

### Soundness
3

### Presentation
3

### Contribution
3
