# Plug-And-Play Controllable Graph Generation With Diffusion Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Diffusion models for graph generation present transformative capabilities in generating graphs for various downstream applications. However, controlling the properties of the generated graphs remains a challenging task for these methods. Few approaches tackling this challenge focus on the ability to control for a soft differentiable property using conditional graph generation, leading to an uninterpretable control. However, in real-world applications like drug discovery, it is vital to have precise control over the generated outputs for specific features (e.g. the number of bonds in a molecule). Current diffusion models fail to support such hard non-differentiable constraints over the generated samples. To address this limitation, we propose PRODIGY (PROjected DIffusion for generating constrained Graphs), a novel plug-and-play approach to sample graphs from any pre-trained diffusion model such that they satisfy precise constraints. We formalize the problem of controllable graph generation and identify a class of constraints applicable to practical graph generation tasks. PRODIGY operates by controlling the samples at each diffusion timestep using a projection operator onto the specified constrained space. Through extensive experiments on generic and molecular graphs, we demonstrate that PRODIGY enhances the ability of pre-trained diffusion models to satisfy specified hard constraints, while staying close to the data distribution. For generic graphs, it improves constraint satisfaction performance by up to $100$%, and for molecular graphs, it achieves up to $60$% boost under a variety of constraints.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces PRODIGY (PROjected DIffusion for Generating constrained Graphs), a plug-and-play methodology for generating graphs that adhere to designated constraints by leveraging pre-trained diffusion models. Addressing the intricacies of controllable graph generation, the technique integrates a projection operator into the reverse diffusion process to ensure alignment with the specified constrained space. Notably, PRODIGY augments the capabilities of existing diffusion models to satisfy stringent constraints without compromising the proximity to the original data distribution.

### Strengths
The proposed method implements controllable graph generation by applying a plug-and-play approach based on the pre-trained diffusion model without fine-tuning, this is a new perspective to reduce experimental costs.

### Weaknesses
1. My biggest concern is whether such an operation, which pulls the embedding towards the designated constrained space through projection during the reverse process, is effective in more practical scenarios. The paper proposes some compromises to determine whether to pull towards the original data distribution or the constrained space during the reverse process. However, from the experimental results, I find that the performance of this approach is not entirely satisfactory. For example, in the Community-small and Ego-small datasets, the MMD metric worsens in many cases after applying the PRODIGY method. Additionally, in the QM9 molecular generation experiment, adding PRODIGY poses a significant risk of decreasing validity and novelty. The observed degradation in MMD, particularly on smaller datasets, suggests that the projection operation might be overly aggressive, disrupting the learned data manifold and leading to samples that are not representative of the original distribution. The trade-off between constraint satisfaction and data distribution fidelity needs further investigation, especially considering the potential for the projection to introduce artifacts or biases.

2. Another concern I have pertains to the potential impact of such operations on the convergence of the Langevin Dynamics process. It would be prudent to provide a proof for the convergence of the Projected Inexact Langevin Dynamic/Algorithm follows some ideas from PSLA [1]. The lack of a convergence proof raises questions about the stability and reliability of the proposed method, particularly in complex scenarios. The projection step, while intended to enforce constraints, could potentially interfere with the convergence properties of the underlying diffusion model, leading to unpredictable behavior or suboptimal results. A rigorous analysis of the convergence properties is essential to ensure the robustness and generalizability of the approach. It is not clear if the projection operation maintains the detailed balance condition required for convergence.

3. I also have some concerns regarding the practicality of the proposed method. From the projection operations summarized in the paper, the proposed method seems more suitable for controllable generation for atomic features X or structural information A related properties, such as valency, atom count, and molecular weight. However, in real-world applications, such as constrained molecular generation, we mostly expect the generated molecules to exhibit certain graph-level properties. The current implementation appears to be limited to constraints that can be directly applied to node or edge attributes, while many real-world applications require control over more complex, graph-level properties that are not easily expressed as simple projections. For instance, controlling properties like the presence of specific substructures or the overall connectivity patterns of the graph would be challenging with the current projection approach. This limits the applicability of the method to a subset of relevant constraint types.

Minor:

4. Some notations should be introduced when they are first proposed, such as $\textbf{Z}_\theta$ in Eq. (3).

### Questions
Why does the method in the paper only demonstrate its effectiveness on continuous diffusion methods and not on recently proposed discrete diffusion methods, such as DiGress+PRODIGY?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a conditional graph generation framework that can be applied in a plug-and-play manner to pretrained diffusion models. In particular, this work proposes to project the denoised samples to the constraint set at each sampling step which results in graphs that satisfy constraints, which could be applied to hard non-differentiable constraints that previous diffusion models are not applicable to.

### Strengths
- The paper is well-written and easy to follow, with sufficient background, related works, and problem setup.

- The motivation of this work, i.e., generating graphs from the data distribution that satisfies hard constraints, is clear which previous diffusion models are not directly applicable due to the non-differentiable constraints.

- This work presents various practical constraints on graph structures or properties (e.g., edge count, degree, valency, dipole moment) and the corresponding projection operators.

- The experimental results show that the proposed method is able to generate graphs that satisfy given conditions in a plug-and-play manner without re-training or fine-tuning the pre-trained diffusion models.

### Weaknesses
 - The main concern is that using the proposed approach seems to have inferior generation quality compared to the original diffusion model. For example, in Table 2, GDSS+PRODIGY results in a significantly higher clustering coefficient MMD for the Community-small dataset and Enzymes dataset. This is problematic as the generated graphs should primarily follow the data distribution, not only satisfying the constraint. The increase in MMD, particularly for the clustering coefficient, suggests that the projection step might be distorting the underlying graph structure, moving it away from the true data distribution. This is a critical issue, as the primary goal of a generative model should be to produce samples that are statistically similar to the training data, and not just satisfy constraints.

- For some constraints, e.g., Degree and Molecular weight, the proposed method does not seem to achieve high validity (lower than 70%) even though the denoised samples are projected to the constrained set. In particular, GDSS+PRODIGY shows similar validity to GDSS for molecular weight constraint. Through analysis clarifying the reason for failing to satisfy the constraint is required. The fact that the projection doesn't guarantee constraint satisfaction after discretization is a significant limitation. The similar validity of GDSS and GDSS+PRODIGY for molecular weight indicates that the projection step is not effectively enforcing this constraint, which raises questions about the method's robustness and the effectiveness of the projection operator for certain types of constraints.

### Questions
- Are the MMD results of Table 2 measured between the generated graphs and the constraint-filtered test set? I presume the MMD is not measured between generated graphs and the original test set as the MMD results are different among the constraints for the same dataset.

- What is the reason for GDSS+PRODIGY showing similar validity to GDSS for molecular weight constraint?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a plug-and-play method to control the diffusion-based graph generation under certain constraints. In each step of diffusion, the generated graph is edited with the nearest feasible solution under the constraints, which can be solved with the Lagrangian method. The authors derive closed-form solutions for some well specified constraints commonly seen. Experiments show the proposed approach can effectively control the generation process to obtain results that satisfy the constraints.

### Strengths
1. Precise control with arbitrary constraints is a desired property for graph generation. The authors propose a general solution for certain classes of constraints. The authors derive closed-form solution for many commonly used constraints under the proposed projection approach. The detailed derivation may also inspire future research where new constraints may appear.
2. The empirical results are comprehensive. The authors show the proposed method can effectively control the generation direction towards graphs that satisfy the constraints, on both 2D graphs and 3D graphs. They further demonstrate the sensitivity of the approach to the interpolation value $\gamma_t$$. Analysis on the efficiency of the approach is also provided.

### Weaknesses
1. Though when the constraints cover all the graphs in the test set, the generated distribution is largely unaffected, in scenarios where the constraints do take effect, the generated distribution obviously deviates from the original distribution. And the deviation is model-sensitive. For example, in Table 2, with edge count as the constraint, the performance of GDSS downgrades by two folds on Clus. while EDP-GNN is largely unaffected. Also, on the dataset of Enzymes and Grid, both GDSS and EDP-GNN suffer a lot from the constraints. Furthermore, Figure 12 shows a lot of unrealistic molecular graphs (e.g. very large rings, disconnected graphs, very long bridging bonds) with the constraints on atom count.
2. The proposed projection paradigm main only applied to constraints with simple calculation process so that the optimization problem has a closed-form solution. When the constraints become complicated (e.g. involves non-linearity), it might be arduous or impossible to find such closed-form solution.

### Questions
1. Maybe a typo in section 4 right under equation 3: $\Pi_c(z) = \arg\min_{z\in c}||z-x||^2$，should be $\Pi_c(x) = \arg\min_{z\in c}||z-x||^2$

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes to have a constraint instead of a condition for generative modeling. The main evaluation metric is VAL_c, which measures the proportion of generated graphs that satisfy the constraint.

### Strengths
– constraint-based generation is a useful and novel avenue on graph generation

### Weaknesses
– It seems that the constrained generation settings is a completely different task from conditional generation (Hoogeboom 2022, Xu 2020) so, I think that the “constrained” keyword is more suitable?

– Since the tasks of Hoogeboom 2022, Xu 2020 are different, the comparisons with baselines are not really fair from what I read in the paper. You should compare the proposed “constrained” approach, with other constrained methods, maybe an adaptation of Bar-tal 2023 that you refer to? I am not convinced that measuring VAL_c on GDSS is fair against your model? This is why GDSS and EDP-GNN have the VAL_c metric approximately at zero, see Table 3.

– It is unclear why the authors are comparing against conditional generation models when the core contribution is about constrained generation. The evaluation against models like GDSS and EDP-GNN, which are not designed for constrained generation, using the VAL_c metric seems inappropriate. These models are not designed to satisfy hard constraints, so a near-zero VAL_c is expected, making the comparison uninformative.

– “influences the sampling process in an obscure and uninterpretable manner”: can you elaborate?

– “Such controls are not differentiable and no method exists that can control the generation for these properties without relying on curating additional labeled datasets or retaining the entire generative mode”: from what I understand conditional generation is a different setup, so does not seem fair to compare what data is required in constrained generation ?

– Condition-based Control definition: Can you write what y and c are? Or link to the part where you formalize it.

– Constraint-based Control definition: can you clarify better the difference with soft control. Or refer to where you are defining it.

– Does the plug-and-play approach require training of 2 models? Could you point to where you discuss the advantage to training the soft constrained methods?

– Figure 2: Sampling process of PRODIGY (red) versus existing methods (Jo et al., 2022). Why are you comparing them, if in the experiments you are not?

### Questions
– Can your approach be applied also into conditional generation, e.g. Hoogeboom 2022 etc?

– “influences the sampling process in an obscure and uninterpretable manner”: can you elaborate?

– “Such controls are not differentiable and no method exists that can control the generation for these properties without relying on curating additional labeled datasets or retaining the entire generative mode”: from what I understand conditional generation is a different setup, so does not seem fair to compare what data is required in constrained generation ?

– Condition-based Control definition: Can you write what y and c are? Or link to the part where you formalize it.

– Constraint-based Control definition: can you clarify better the difference with soft control. Or refer to where you are defining it.

– Does the plug-and-play approach require training of 2 models? Could you point to where you discuss the advantage to training the soft constrained methods?

– Figure 2: Sampling process of PRODIGY (red) versus existing methods (Jo et al., 2022). Why are you comparing them, if in the experiments you are not?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
