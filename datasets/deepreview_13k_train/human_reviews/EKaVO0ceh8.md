# Projection Optimal Transport on Tree-Ordered Lines

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
Many variants of Optimal Transport (OT) have been developed to address its heavy computation. Among them, notably, Sliced Wasserstein (SW) is widely used for application domains by projecting the OT problem onto one-dimensional lines, and leveraging the closed-form expression of the univariate OT to reduce the computational burden. However, projecting measures onto low-dimensional spaces can lead to a loss of topological information. To mitigate this issue, in this work, we propose to replace one-dimensional lines with a more intricate structure, called \emph{tree systems}. This structure is metrizable by a tree metric, which yields a closed-form expression for OT problems on tree systems. We provide an extensive theoretical analysis to formally define tree systems with their topological properties, introduce the concept of splitting maps, which operate as the projection mechanism onto these structures, then finally propose a novel variant of Radon transform for tree systems and verify its injectivity. This framework leads to an efficient metric between measures, termed Tree-Sliced Wasserstein distance on Systems of Lines (TSW-SL). By conducting a variety of experiments on gradient flows, image style transfer, and generative models, we illustrate that our proposed approach performs favorably compared to SW and its variants.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed a computation of the Sliced Wasserstein (SW) distance using a novel projections on systems of lines and achieved improvements compared to the original SW approach.

### Strengths
Clarity:
The paper is well-written and logically structured, making it easy to follow.

Originality:
The approach of efficiently solving sliced optimal transport using tree-based priors presents a novel and intriguing perspective.

Significance:
This research represents a crucial advancement in the development of more efficient closed-form tools for computing Wasserstein distances, which is an important area of study.

### Weaknesses
Quality:
The poor evaluation is the main weakness of the paper. The authors provided several experiments, but only Tables 1 and 2 offer an expressive justification of the proposed method.



### Questions
What should I observe in Figure 5? The images appear identical to me. More expressive examples of the color transfer are necessary.
Why did you consider your distance as the regularization for the GAN model? In my understanding, gradient flow methods from section 6.1 in higher dimensions would provide better evidence.
The paper demonstrates how the proposed distance can help decrease the distance to the target datasets. However, there is no evaluation showing that the computed distance is actually closer to the real Wasserstein distance provided. I think it is crucial to demonstrate this across a range of datasets.
Table 4 does not demonstrate that the proposed method actually provides better results in FID.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors advance the concept of Sliced Wasserstein (SW) distance, which involves projecting data onto one-dimensional lines and leveraging closed-form expressions for one dimensional optimal transport to reduce computational costs. The authors propose an alternative projection onto tree systems, asserting that this approach preserves topological information. Additionally, they rigorously demonstrate that their framework yields an efficient metric for comparing measures. They also present extensive experimental results showcasing the superior performance of their method compared to existing methods based on SW-type distances.

### Strengths
The derivation is clear and well-structured, providing a thoroughly developed framework. The authors demonstrate improved performance relative to previous related methods while maintaining lightweight computation. The code is provided.

### Weaknesses
Although the authors present a well-founded theoretical framework and demonstrate practical improvements on several setups, the proposed method essentially introduces (yet) another distance metric akin to the Sliced Wasserstein distance. The overall paper seems to be a rather straightforward and incremental extension of the prior related works in the field. That is, I am rather skeptical about the significance and impact of the construction proposed here on the field of ML.

It seems to me that the main purpose of the proposed TSW-SL seems to be to compare the probability distributions, a feature which is primary needed for GAN training nowadays (the other experiments in the paper with gradient flows, etc. are toy, so I do not consider them as particularly demonstrative and serious). Here I have a general concern regarding the usefulness of the proposed TSW-SL in GANs. The experiments with GANs indeed show some practical improvement in the task of image generation. However, according to the famous work [1] tuning GANs is more about tuning various hyperparameters rather than changing the particular loss functions. This is also confirmed by the fact that most more practically-related papers (from CVPR, ECCV, etc.) still rely on vanilla/NS/WGAN loss with additional regularizations rather than other more complex losses (like SW-based) proposed by the community later. This suggests that (in 2024) the contribution of the current paper (TSW-SL as a GAN loss) may be relatively minor, so I am more on the negative side about the paper.

Additionally, the experiments with GANs lack details and sufficient explanations. For example, it is not clear why the problem in lines (Appendix) 1501-1505 is a valid GAN optimization problem. In the DDGAN experiment, how exactly the DDGAN loss is used in TSW is also not explained in detail, while it should: the DD-GAN loss is a non-trivial model due to various conditioning (discriminator is conditioned on the point, on the time moment). How this conditioning fits to the the proposed TSW-SL framework remains explained (line 1618 is not enough).

### Questions
I would like to see more experimental results and discussion regarding the GAN training.
- Could you explain how does your training time (time per iteration, per epoch, overall time to convergence) compares with the one from DDGAN and the other basedlines considered in the experiments.
- Could you please provide the convergence plots (FID as a function of epoch, e.g., once per several epochs) for your model vs. DDGAN vs. some other SW baseline? I would like to understand how stable is the overall training of your model compared with the baselines.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a variant of the Sliced-Wasserstein distance that, rather than projecting distributions onto lines, projects them onto tree systems. This approach leverages the closed-form solution of optimal transport (OT) for trees to develop a fast algorithm based on the Radon transform applied to tree structures. It uses splitting maps to define how distributions are projected onto these structures. This tree-sliced Wasserstein distance on a System of Lines (TSW-SL) is shown to be a metric. Experiments compare the original SW with TSW-SL, demonstrating that TSW-SL provides slightly better performance than SW, with comparable computation times.

### Strengths
Paper introduces a new variant of sliced-Wasserstein: relying on a tree metric is original and allows benefiting from closed-form solution that exists, allowing preserving computational efficiency. The paper is clear, well illustrated, experimental section validates the approach in different contexts.

### Weaknesses
 **Note:** I have reviewed an extension of TSW-SL for the same venue.

As noted in the conclusion, the paper *"introduces a straightforward alternative to SW by replacing one-dimensional lines with tree systems,"* aiming to provide a more geometrically meaningful space. This objective aligns with several SW variants (as mentioned in the related work section of the introduction) that have achieved performance improvements in learning tasks involving SW and/or offer alternative schemes with distinct properties (e.g., statistical characteristics, behavior in high-dimensional spaces, the ability to provide a transport plan). However, given that TSW-SL achieves similar (or slightly better) performance to SW while retaining the same limitations (e.g., difficulties in sampling meaningful lines in high dimensions, as noted in Table 2), it remains unclear why and under what circumstances TSW-SL should be preferred over SW or its many variants. The paper does not sufficiently articulate the specific scenarios where TSW-SL offers a clear advantage, particularly given its increased complexity due to the tree structure and splitting maps.

There is also no discussion regarding the impact of the number of lines per tree, which seems to be a critical aspect of the method—especially as using only one line per tree recovers the standard SW. The paper lacks a thorough analysis of how varying the number of lines affects the performance and computational cost. Additionally, the influence of the splitting maps is not addressed, despite being central to the new Radon transform. The choice of splitting map and its impact on the resulting distance metric are not explored, leaving a significant gap in the understanding of the method's behavior.

**Other Comments:**

- In the gradient flow experiment, differences in ground cost (e.g., $L_2$, tree metric) between methods make it challenging to compare results at a fixed number of iterations. The use of different ground metrics makes it difficult to isolate the effect of the proposed TSW-SL distance, as the optimization landscapes are not directly comparable.
- Table 1: By *Wasserstein distance,* do you mean $W_2$? Additionally, could you clarify the timings reported in Table 2? The description of the timing results is not clear enough to understand the computational efficiency of the method.
- Line 467: The loss should not be denoted as $\mathcal{L}$ since this letter represents a line.
- Section 6.2: It is difficult to visually confirm that *TSW-SL produces images that most closely resemble the target.* The qualitative results are not sufficiently compelling to support the claims made about the method's performance.
- Appendix p.17, line 870: $\overline{L}$ should be $\overline{\mathcal{L}}$.
- Example A.14 is unclear: $n_i $ should have length 6 (i.e.,$i = 0$ to 5). What do the arrows signify? Additionally, an arrow seems to be missing on line 1035. The progression through step $i$ is confusing. The example is not clearly explained, making it difficult to understand the tree representation.
- Page 25: Please provide more detail about the transition from eq. (46) to eq. (47). The jump between the equations is not sufficiently justified.

### Questions
- What are the main arguments in favor of TSW-SL wrt other many variants of SW? Could you highlight the unique advantages of TSW-SL?

- Can you give some stronger argument to the claim that tree systems allow avoiding a loss of topological information? Is this claim related with the number of lines that should be sampled ? What is the impact of this parameter onto the perfomances?

- Is it possible to derive additional properties of TSW-SL? For instance, does it metrizes the weak convergence? What are its statistical properties? 

- It is stated in the conclusion that improved performances are expected by adapting recent advanced sampling schemes or techniques of SW to TSW-SL. It seems that the extension is not that straightforward: can you comment on that, and how improved performances can be expected?

- It is stated in the beginning of section 6 that "*the root is positioned near the mean of the target distribution*": what is the impact of this setting?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new tree Sliced-Wasserstein distance. This new distance is obtained by projecting on trees instead of 1d lines. The authors provide a complete theoretical analysis of the tree structures introduced, of the Radon transform used to project on them, as well as a discussion on how to sample such trees. Finally, they compare their method with the original Sliced-Wasserstein distance and some of their variants on several tasks such as gradient flows, color transfer, generative modeling with SWGAN and for diffusion models.

### Strengths
This paper provides a new tree Sliced-Wasserstein distance, which in contrast with previous works, project on trees, and is thus more flexible. 

The authors provide first a full theoretical analysis of the tree space introduced, as well as a way to sample them in practice. Defining the right Radon transform, this analysis allows defining naturally a Tree Sliced-Wasserstein distance, which generalizes the original Sliced-Wasserstein distance. They show that this is well a metric, and that it can be approximated efficiently in the same complexity as Sliced-Wasserstein (w.r.t samples). This construction is thus original, well motivated and with good properties.

Finally, they compare their distance with Sliced-Wasserstein and variants thereof, on different experiments. On these different tasks, they show consistently better performances than Sliced-Wasserstein. Moreover, their experiments are done on classical baselines such as gradient flows on 2D datasets and higher dimensional gaussians, or color transfer, but also on high dimensional data such as images with generative modeling.

### Weaknesses
Some minor weaknesses are that there are no statistical analysis for the Tree Sliced-Wasserstein distance proposed, e.g. no sample complexity, nor topological analysis. One can wonder how it relates with other distances, it TSW-SL a lower-bound of the Sliced-Wasserstein or of the Wasserstein distance?

The theoretical section on trees is very interesting, but some parts are challenging to read (for instance Section 3.2). I note however that an effort has been made on being clear, notably through Figure 1 and 2, which help to understand the constructions.

Some references are missing such as [1,2,3] when citing work which project on lower dimensional subspaces.

I think in Equation (2), there is an abuse of notation as the Radon transform of a density is a density, and not a measure.

The construction given in Algorithm 1 only samples a chain tree. Did you also test with sampling trees where nodes have different childs?

For the experiments on SW generators (Section 6.3), the number of projections (50 and 500) seems very low compared to the original paper, where I think they use something like 100K projections.

Typos:
- Line 102: "(Helgason & Helgason, 2011)" -> (Helgason, 2011)
- Line 322: "If tree systems in $\mathbb{T}$ consists only one line"

### Questions
When citing references about work which project on lower dimensional subspaces, some references are missing such as [1,2,3].

I think in Equation (2), there is an abuse of notation as the Radon transform of a density is a density, and not a measure.

The construction given in Algorithm 1 only samples a chain tree. Did you also test with sampling trees where nodes have different childs? 

For the experiments on SW generators (Section 6.3), the number of projections (50 and 500) seems very low compared to the original paper, where I think they use something like 100K projections.


Typos:
- Line 102: "(Helgason & Helgason, 2011)" -> (Helgason, 2011)
- Line 322: "If tree systems in $\mathbb{T}$ consists only one line"


[1] Lin, T., Zheng, Z., Chen, E., Cuturi, M., & Jordan, M. I. (2021, March). On projection robust optimal transport: Sample complexity and model misspecification. In International Conference on Artificial Intelligence and Statistics (pp. 262-270). PMLR.

[2] Huang, M., Ma, S., & Lai, L. (2021, July). A riemannian block coordinate descent method for computing the projection robust wasserstein distance. In International Conference on Machine Learning (pp. 4446-4455). PMLR.

[3] Muzellec, B., & Cuturi, M. (2019). Subspace detours: Building transport plans that are optimal on subspace projections. Advances in Neural Information Processing Systems, 32.

### Soundness
4

### Presentation
4

### Contribution
4
