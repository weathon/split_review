## Human Reviewer 1

### Summary
This paper studies the problem of ensuring hard constraints and avoiding out-of-distribution in safe offline reinforcement learning. The proposed method first models the latent action through a flow module, which concentrate probability mass on safe regions, and then applies a refinement stage that updates the base-space variable to improve reward and safety before decoding actions. Experimental results on several benchmarks show that the proposed method achieves fewer violations and comparable or higher return than the baselines.

### Strengths
1. The experiments are extensive, covering mainstream safe offline RL benchmarks and algorithms.
2. The writing of the paper is clear.

### Weaknesses
1. The contribution of the proposed method over existing methods is unclear.
2. The motivation of the refinement stage given the flow module is not described clearly.
3. The practice of the refinement steps is not sound enough.

### Questions
1. This paper considers a state-wise hard constraint setting. The authors claim that existing methods for handling hard constraints typically induce conservatism. What is the cause of such conservatism?
2. The authors claim that the proposed method is not "pushed by hard constraints" but "pulled by density". What does this mean? What is the benefit of being "pulled by density" over being "pushed by hard constraints"?
3. In prior density shaping, the loss function (12) involves the value functions with regard to reward. Does this mean that the flow module is also taking reward into consideration? If this is the case, it seems that both the flow module and the refiners are simultaneously considering reward and constraint. Then, what is the difference between the roles of them?
4. In the refinement stage, why are the three refiners applied in the order of safety-reward-shared? Why not averaging their incremental updates into a single update or even learning a single refiner that directly optimizes the total loss? Does the process of repeating the refinement steps finally converge?

### Soundness
1

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper addresses the problem of safe offline reinforcement learning (RL), proposing a new method termed FLRP. The key idea is to leverage a normalizing-flow-based latent action manifold together with a refiner module that operates in the latent space to balance safety and performance while remaining within the support of the offline dataset. The method is evaluated on standard safe offline RL benchmarks and demonstrates competitive results against recent baselines such as FISOR, LSPC, and CDT.

While the empirical results are promising and the paper is well-organized, the conceptual novelty appears somewhat limited given the overlap with several recent works. Addressing the following points (please refer to Weaknesses and Questions sections) could significantly strengthen the paper’s contributions.

### Strengths
1. The formulation of a zero-violation feasibility critic via HJ-style value functions is a natural and well-motivated choice for safety-critical domains. The latent-space refinement idea is also practical and nicely complements this design.
2. The framework avoids the complex minimax optimization often arising from Lagrangian formulations in constrained RL, leading to a more tractable training procedure.
3. The paper is generally well-written and clearly structured, and it includes ablation studies that help justify the design choices.

### Weaknesses
1. Conceptual novelty and prior work: The incorporation of HJ-based critics for safety has already been explored in works such as RCRL [1] and FISOR [2], while decoding from safety-dense latent embeddings is reminiscent of LSPC[3]. Although these works are cited, the specific novelty and distinction of FLRP are not sufficiently articulated. Strengthening the introduction section and related-work discussion to clearly delineate what is new (and what is adapted) would improve the paper’s contribution clarity.
2. Potential conservatism: The use of feasibility values might make the method conservative when high-reward and low-cost regions do not coincide with high-density behavior data. This could explain why the authors primarily report results under a fixed cost threshold (10) rather than varying thresholds (e.g., 10, 20, 40) as done in the original DSRL evaluation. Including results under different safety budgets would help evaluate the robustness–safety trade-off.
3. Computational complexity: Normalizing flow modeling in high-dimensional action spaces can be computationally expensive due to inverse computations and potential convergence sensitivity. While implementation details are briefly discussed, it would be interesting to know whether implicit density models (e.g., flow-matching or diffusion-based methods) could serve as lighter or more stable alternatives.
4. Presentation and algorithm clarity: Algorithm 1 is currently deferred to the very last of the paper. Given that the proposed method involves multiple components (flow model, multiple refiners, and multiple critics), including a compact pseudocode or schematic in the main text (or at least referencing the appendix early) would significantly aid readability and reproducibility.
5. Ablation on HJ-feasibility function: Although the reward-wise policy improvement scheme remains the same, the “w/o HJ” variant consistently underperforms (reward-wise) the full FLRP model. Clarifying whether the critics or refiners are retrained independently for this variant would help ensure that this comparison is fair and interpretable.
6. Figure 2 clarity: While the visualization itself is appealing and informative, the labels are not clearly defined and the figure is not thoroughly discussed in Section 5. Clearer explanations of what each axis and color corresponds to would help readers better connect the figure to the text.

[1] Yu, et al. "Reachability constrained reinforcement learning." ICML, 2022.

[2] Zheng, et al. "Safe offline reinforcement learning with feasibility-guided diffusion model." ICLR, 2024.

[3] Koirala, et al. "Latent Safety-Constrained Policy Approach for Safe Offline Reinforcement Learning." ICLR, 2025

### Questions
1. Both methods FISOR and FLRP use an HJ-based feasibility critic, yet FLRP appears *generally* less conservative (achieving higher reward at a cost of higher cost). Could the authors clarify what aspect of FLRP’s design makes it less conservative than FISOR?
2. LSPC derives policy-gap and performance bounds similar to those in Corollary 1 of this paper. This is not discussed in the paper. How do the theoretical guarantees of FLRP differ or improve upon those results?
3. How sensitive is FLRP’s performance to the order of refiners? Would reversing or randomizing the order affect stability or outcomes?
4. Figure 2 interpretation: 
* The authors claim a zero-violation scheme. If the full action space were visualized, would some regions correspond to zero Q_h values? If only the cost refiner were used, would it drive the samples toward that region?
* It also seems that maximizing the decoder log-density alone already steers actions toward safer regions. Is this effect specific to the CarRun environment or more general across tasks?
5.  Equation (14): Could the authors elaborate on the safety-expert AWR objective? The form looks unusual, and I could not find a directly similar objective in the cited references.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes FLRP (Flow-guided Latent Refiner Policies), a safe offline RL framework that addresses hard safety constraints and out-of-distribution (OOD) action issues. The method has three main components: (1) **Feasibility-based value functions** using Hamilton-Jacobi (HJ) reachability to identify safe states/actions from offline data, (2) **Conditional normalizing flows** that model the latent action manifold and concentrate probability mass on empirically safe, high-density regions, and (3) **Expert refiners** (safety, reward, shared) that perform small residual updates in the base Gaussian latent space to jointly optimize reward and safety. The framework operates entirely offline and provides theoretical guarantees that refinement in base space controls distributional shift. Experiments across 26 tasks from Safety-Gymnasium, Bullet-Safety-Gym, and Safe MetaDrive show violation rates of 0.18 vs. 0.40 (second-best baseline) while maintaining competitive returns.

### Strengths
- Creative combination of normalizing flows with latent-space refinement and HJ-based feasibility signals provides a principled approach to safe offline RL
- Lemmas 2-3 and Corollary 1 provide formal guarantees that controlling base-space KL bounds downstream distributional shift in Wasserstein and TV metrics
- Avoids brittle Lagrangian penalty tuning by shaping density via flows and performing feasibility-aware refinement

### Weaknesses
- HJ operator with sparse cost signals can undervalue genuinely safe but rare samples, introducing bias (acknowledged in Section 7)
- Requires tuning expert loss weights (λr, λh, λsh), temperatures (Tv, Tq), prior shaping coefficients, and expectile τ—though authors use single config across tasks

### Questions
1.  Table 3 shows flow prior helps, but what is the computational cost? Could a simpler multimodal prior (e.g., mixture of Gaussians) achieve similar benefits?

2.  Can you quantify the gap between HJ-based feasibility estimates and true safe regions? How often do safe actions get incorrectly labeled as infeasible?

3. Freezing the decoder constrains optimization to the learned manifold. How much performance is lost vs. fine-tuning the decoder? Could you alternate freezing/unfreezing?

4.  Both use feasibility guidance with diffusion/flow models. What are the key differences? When would FISOR be preferred over FLRP?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper integrates several established techniques—flow-based density modeling conditioned on state, latent-space refinement, and feasibility value estimation via a reversed expectile objective—to form a constraint-free offline safe reinforcement learning framework.

### Strengths
The paper is carefully executed and technically sound, and there is systematic integration of well-established components. It demonstrates a deep and precise understanding of existing literature: every methodological decision (e.g., shaping the tail of the density, re-centering distributions, introducing diffusion-based regularization) is well-motivated and mathematically coherent. Each modification clearly reflects an awareness of what has worked in prior studies and why it should succeed here.

### Weaknesses
This strength in technical maturity also highlights the main limitation: the work feels more like a thorough engineering synthesis than a piece of  innovation. Each component—while justified and effective—has appeared in prior forms, and the novelty stems mainly from their particular arrangement and empirical tuning. The result is a reliable and well-executed method, but one that does not significantly advance our theoretical or methodological understanding of safe offline reinforcement learning.

### Questions
1. Given the lack of a clean and standardized benchmark for flow-based models, and given the paper's  strong technical background, could this work have instead been directed towards something more like a systematic evaluation framework? This would be similar in spirit to, e.g., Clean Diffusion (NeurIPS 2023).

2. The paper integrates several known ideas—latent action manifold learning, flow-based density modeling, and lightweight latent refinement—into a new safe offline RL framework. While the individual components are not novel per se, their combination can still represent a meaningful contribution if the paper clearly articulates what new properties or advantages this combination introduces, such as PLAS (Zhou et al., 2021), Let Offline RL Flow (Akimov et al., 2022), and later latent-space safe RL methods. These studies should be explicitly acknowledged, as they form the conceptual foundation upon which this paper is built. Then, can the authors make any distinguishing features more clear (other than what I have acknowledged above in terms of strengths)?

3. The paper adopts a hard-constraint view of safety, similar to FISOR, where violations are strictly avoided. However, another common line of work treats cost as a budgeted resource—aiming to use the safety budget efficiently rather than minimizing it to zero. e.g. Safe Offline Reinforcement Learning with Real‑Time Budget Constraints (Lin et al., 2023). Acknowledging this alternative perspective would clarify that different methods reflect different design philosophies rather than differences in capability.

4. The density term (Eq. 2) plays an important role in constraining the policy within data-supported regions, but it is relatively under-explained and/or not clearly explained in the main text. I suggest adding a brief derivation or clarification in the appendix (e.g., how the flow-based likelihood or Jacobian term is computed and used, or a direct line between the bijective nature of the conditional probability and the resulting change-of-variables). This would improve clarity, especially for readers not familiar with conditional flow density modeling, and would make the paper more self-contained..

5. The GitHub repository lacks clear installation and setup instructions, which limits reproducibility. Please include dependency and compilation details (e.g., for the BulletSafetyGem component). Also, as part of the implementation appears inspired by FISOR, it would be helpful to note this explicitly in the documentation.

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
4

### Confidence
5