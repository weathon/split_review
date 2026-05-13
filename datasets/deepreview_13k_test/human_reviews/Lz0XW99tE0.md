# A Periodic Bayesian Flow for Material Generation

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Generative modeling of crystal data distribution is an important yet challenging task due to the unique periodic physical symmetry of crystals. Diffusion-based methods have shown early promise in modeling crystal distribution. More recently, Bayesian Flow Networks were introduced to aggregate noisy latent variables, resulting in a variance-reduced parameter space that has been shown to be advantageous for modeling Euclidean data distributions with structural constraints (Song, et al.,2023). Inspired by this, we seek to unlock its potential for modeling variables located in non-Euclidean manifolds e.g. those within crystal structures, by overcoming challenging theoretical issues. We introduce CrysBFN, a novel crystal generation method by proposing a periodic Bayesian flow, which essentially differs from the original Gaussian-based BFN by exhibiting non-monotonic entropy dynamics. To successfully realize the concept of periodic Bayesian flow, CrysBFN integrates a new entropy conditioning mechanism and empirically demonstrates its significance compared to time-conditioning. Extensive experiments over both crystal ab initio generation and crystal structure prediction tasks demonstrate the superiority of CrysBFN, which consistently achieves new state-of-the-art on all benchmarks. Surprisingly, we found that CrysBFN enjoys a significant improvement in sampling efficiency, e.g., ~ 100x speedup (10 v.s. 2000 steps network forwards) compared with previous Diffusion-based methods on MP-20 dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new crystal generative model for materials using Bayesian Flow Networks, a diffusion-like generative model but supports more types of prior for noise distributions. To effectively enforce E(3) equivariance in generation, the fractional coordinates are generated on the hyper-torus manifold defined in Jing et al. 2022. Instead of standard Gaussian noise used for generation of torsion angles, von Mises distribution is used with derived Bayesian update. To ensure the receiver belief entropy is linearly decreasing, a numerical binary search is done for determining the schedule of the sender’s accuracy (noise) level. In experiments, this method performs better than SOTA methods such as DiffCSP, FlowMM and CDVAE. When compared with diffusion-based method DiffCSP, this method excels at sampling with fewer steps (NFEs).

### Strengths
The major strength of the method is using Bayesian Flow Networks for crystal material generation. The von Mises distribution is used and its Bayesian update is used for training the BFN model, where previous BFN models only use Gaussian distribution. And for this special distribution, the authors identified that it is important to condition the model with the entropy of the receiver’s belief instead of the time. 

The other strength is the improved sampling efficiency of BFN model as compared to diffusion-based method such as DiffCSP. But it is unclear how it compares with ODE sampling method such as flow matching or diffusion with ODE sampler.

### Weaknesses
Major weakness is on experiment evaluation.

- For baselines to compare, the latest DiffCSP++[1] (which gives better performanc) and MatterGen[2] are not included.
- For metrics, what about uniqueness, novelty, and stability? The goal of material generation is generating novel unique materials that are stable. Hence, these metrics are the most important to measure for use case of material generation.
- For comparing methods with same number of network forward evaluations, the sampling stepsizes should be adjusted, i.e. $\Delta t = 0.01$ if sampling $100$ steps. It’s not clear from the current description. Also diffusion models with stochastic samplers are known to need more steps in sampling. For better comparison, maybe consider flow matching (such as FlowMM) or diffusion model with ODE sampler, and with adjusted sampling stepsizes.

The presentation of BFN can be improved. Maybe with a small toy example to explain how it works. Also for introducing the parameters of von Mises distribution, might be good to refer to Figure 5 and illustrate how each parameter affect the distribution.

### Questions
- SE(3) or E(3) equivariance? Is reflection included when generating the fractional coordinates on the hypertorus. Only translation and rotation are mentioned to be preserved in the paper (also in Jing et al. 2022 as well), which corresponds to SE(3).
- Comparison with baselines with same number of NFEs: how are the methods evaluated, are the stepsizes $\Delta t$ adjusted by the number of sampling steps as well?
    
    Also for small NFEs, it makes more sense to compare with flow matching or diffusion model with ODE sampling, such as FlowMM? Since diffusion models use stochastic sampler which in general requires more steps as seen in the EDM paper[3]. How does FlowMM (which uses ODE sampler) perform with fewer steps?
    
- Compare with SOTA: DiffCSP++ [1] should be considered as another baseline to compare to, and also with fewer steps of sampling. Its performance seems to be better than DiffCSP. Also MatterGen-MP should be considered as a baseline for reference.
- Evaluation on metrics such as uniqueness, novelty and stability?
- Training time comparison: How does training time compare for different methods? Does the introduced von Mises distribution Bayesian update incur additional training cost per batch?

[1] Jiao, Rui, Wenbing Huang, Yu Liu, Deli Zhao, and Yang Liu. "Space group constrained crystal generation." *arXiv preprint arXiv:2402.03992* (2024).

[2] Zeni, Claudio, Robert Pinsler, Daniel Zügner, Andrew Fowler, Matthew Horton, Xiang Fu, Sasha Shysheya et al. "Mattergen: a generative model for inorganic materials design." *arXiv preprint arXiv:2312.03687* (2023).

[3] Karras, Tero, Miika Aittala, Timo Aila, and Samuli Laine. "Elucidating the design space of diffusion-based generative models." *Advances in neural information processing systems* 35 (2022): 26565-26577.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper extends BFNs to von-Mises distributions on the product of 1-spheres (flat torus) and applies this method to modeling conditional material generation (conditioned on atom type, generate positions).

### Strengths
- Method seems novel and using a different model for geodesic generative modeling seems interesting.
- Results seem good and competitive.

### Weaknesses
- My main concern is I found the definitions and exposition on Bayesian Flow Networks very unclear.
- Some minor concerns about the experiments.

### Questions
About BFN extension:
  - Can the torus example in Figure 3 be explained through geodesic interpolations of $\theta_{i-1}$ and $y$?
  - I don't have sufficient background in BFN to understand the preliminaries, as it immediately uses terminology from BFNs. Can you summarize the basic BFN framework and explain why extending to periodic is not easy in 2-3 sentences in layman terms? 
  - There may be missing information about the sampling in Eq (3). How is y_1 defined? How do you sample the y_i sequence? Is that based on Phi?

Experiments:
  - Why not also report stability rate for Table 2? As I understand, this is an important metric for material generation.
  - FlowMM was also proposed for efficient sampling and has a similar (but weaker) plot of Figure 4 (Match rate vs NFE). Can you add FlowMM into Figure 4?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces a novel generative model for creating crystal structures using a Periodic Bayesian Flow. Its unique contribution is adapting Bayesian Flow Networks (BFNs) to model periodic data on non-Euclidean spaces (specifically, the hyper-torus), which is essential for the spatial symmetry of crystals. Traditional BFNs, optimized for Euclidean data, are insufficient for the periodic nature of crystals, prompting this adaptation to account for non-monotonic entropy and periodicity. The authors introduce majorly these concepts; (a) Periodic Bayesian Flow on a hyper-torus, designed for non-Euclidean spaces to improve generative modeling accuracy for crystal data. (b) Entropy Conditioning instead of time-based conditioning, which better informs the model about the generation state due to non-additive entropy dynamics. (c) Fast Sampling Algorithm and reformulations of BFN for computational efficiency, achieving approximately 100x improvement in speed over previous diffusion-based methods. Experimental results demonstrate CrysBFN's performance advantages on tasks like ab initio crystal generation and crystal structure prediction, consistently outperforming existing methods (e.g., DiffCSP and FlowMM) in accuracy, efficiency, and property statistics across datasets such as Perov-5, Carbon-24, and MP-20. The paper establishes CrysBFN as a state-of-the-art approach in generative crystal modeling, with potential applications for other data types on periodic manifolds. The approach, validated through extensive experimentation, advances both theoretical and practical methodologies for material generation tasks.

### Strengths
Overall, this work is thorough, well-written, and stands out as a valuable contribution to the literature on generative material models. The paper’s strengths lie in its originality, quality, clarity, and significance. Its originality is evident in the introduction of CrysBFN—the first periodic Bayesian Flow Network designed for modeling non-Euclidean crystal data on a hyper-torus. The following points highlight the paper’s most impressive strengths.

1. The paper introduces CrysBFN, the first Bayesian Flow Network designed for periodic, non-Euclidean crystal data.
2. Authors propose a novel entropy-based conditioning that enhances modeling accuracy for periodic structures.
3. Achieves a 100x speedup in sampling efficiency compared to previous diffusion-based methods.
5. State-of-the-Art Results, outperforms leading models in crystal generation accuracy and structural validity across multiple datasets.

### Weaknesses
1. Although not in the scope of the paper, but the paper may discuss on how CrysBFN could generalize to other non-crystal periodic or symmetrical data types. While CrysBFN shows strong results for specific crystal datasets, the paper could benefit from discussing its potential for generalization to other periodic or non-Euclidean data types beyond crystals. Including experiments or examples of how CrysBFN could extend to other symmetrical structures, such as molecular or lattice-based materials, would add depth and show broader applicability.

2. The paper introduces entropy conditioning in place of traditional time-based conditioning, which adds complexity to the model. While the necessity of entropy conditioning is discussed, providing additional comparative analysis between the two methods across varied datasets (e.g., simpler vs. more complex structures) could clarify its practical advantages and help practitioners understand when to apply entropy conditioning.

3. Though the model achieves a high sampling efficiency, the paper does not provide a detailed analysis of the overall computational cost for training and deployment. Adding a breakdown of the computational resources required, such as training time or GPU hours, would provide a clearer picture of the model’s practicality for large-scale or industrial applications.

### Questions
1. Given the scope of this work I do suggest that the section covering related work may be improved. The authors should do a good survey of the past work in cystal generations particularly in the field of crystal genration with other implicit generative models for crystal representations. Some of which I was able to find by searching for representation based genrative model in citations to CDVAE (Xie et. al.) paper are: 1. https://arxiv.org/abs/2306.04510, 2. https://arxiv.org/abs/2403.10846, 3. https://arxiv.org/abs/2408.07213 (kindly read and search for more). I request the authors to kindly include papers which are in the same field to address the concerns in this paper and how your research aligns or complements with these papers, so that this work becomes complete.

2. The authors are suggested to kindly improve section 2 of their work where they have mentioned some aspects of previous related work, it would be better to include how the work is different and morevoer how does the work takes the research forward from the previous work. If the space becomes an issue (As the authors have already breached the page limitation part, then kindly include a section in complementary section) kindly add a complementary section.

### Soundness
3

### Presentation
3

### Contribution
3
