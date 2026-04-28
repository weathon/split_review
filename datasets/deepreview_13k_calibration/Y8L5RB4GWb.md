# Reconstruction-Guided Policy: Enhancing Decision-Making through Agent-Wise State Consistency

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
An important challenge in multi-agent reinforcement learning is partial observability, where agents cannot access the global state of the environment during execution and can only receive observations within their field of view. To address this issue, previous works typically use the dimensional-wise state, which is obtained by applying MLP or dimensional-based attention on the global state, for decision-making during training and relying on a reconstructed dimensional-wise state during execution. However, dimensional-wise states tend to divert agent attention to specific features, neglecting potential dependencies between agents, making it difficult to make optimal decisions. Moreover, the inconsistency between the states used in training and execution further increases additional errors. To resolve these issues, we propose a method called Reconstruction-Guided Policy (RGP) to reconstruct the agent-wise state, which represents the information of inter-agent relationships, as input for decision-making during both training and execution. This not only preserves the potential dependencies between agents but also ensures consistency between the states used in training and execution. We conducted extensive experiments on both discrete and continuous action environments to evaluate RGP, and the results demonstrates its superior effectiveness. Our code is public in https://anonymous.4open.science/r/RGP-9F79

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper addresses two issues with multi-agent reinforcement learning: the errors from reconstructing the global state of the environment during execution, and respecting dependencies between agents which are necessary for optimal decision making. The paper shows how the model addresses these two issues and empirically dissect it to show its better performance than current MARL solutions, as well as reasons for what causes this.

### Strengths
* The writing flows well and is well-motivated. It was easy to understand the MARL background and the problems of state reconstruction error and inter-agent coordination that this paper tackles.
* Important assumptions and details (critical to the solution method and results) were made clear often to the reader: such as the guidance network only being used during the training, and the implementation details for the experiments.
* Enumerating the research questions tremendously helped with the paper's clarity and structure. This practice should be adopted into more papers in the field!

### Weaknesses
 * Figures need a bit more clarity: What do the shaded regions in Fig 5 represent? How many runs were used for Figure 5? Depending on the number of seeds and the claim being made, this has to be specified as context to the reader. For example, tolerance intervals or bootstrapped confidence intervals are great for showing the variability in performance when there, even when there are a small number of runs. 95% confidence intervals would be appropriate if there are more runs and it's safe to assume the y-axis variable is normally distributed.
* The paper lacks a limitations section. Besides the one limitation regarding smaller fields of view, it  would be nice to see what other challenges to do with partial observability in MARL would need to be addressed next, and if there are any other shortcomings of RPG. Certain parts of the work speculated reasons about why results were seen (such as the impressive score of RGP+FACMAC in Predator-Prey). This could be summarized at the end of the conclusions section.
* [Very Minor] Line 483: typo “continuous”

### Questions
* What is the uncertainty measure in Table 1? Is it a standard error?

### Soundness
4

### Presentation
4

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
Partial observability in multi-agent reinforcement learning (MARL) limits agents to local observations, often leading to suboptimal decisions and inconsistencies between training and execution. To solve this, the paper proposes the Reconstruction-Guided Policy (RGP), which reconstructs an agent-wise state capturing inter-agent relationships, ensuring consistent input for both training and execution. Experiments across discrete and continuous action environments show RGP’s good performance.

### Strengths
- The paper studies an important problem in cooperative MARL, that is dealing with partial observability and non-stationarity
- The paper proposes a novel method, which is based on state-of-the-art techniques such diffusion models and attention mechanism.
- The paper includes strong ablation study, which examines and justifies the selection of the method's components.
- The proposed method achieves good results across different benchmarks.

### Weaknesses
 - The comparison with the related work can be improved: The paper ignores significant works based on agent (opponent) / state modelling, world models, transformer-based methods which also aim to deal with partial observability. For instance, the authors argue that one main challenge is state inconsistency. In particular, many works (e.g. [1]) leverage state embeddings (which can be much more compressed and informative) instead of using the reconstructed state (which can be less informative for each agent's training, also due to redundant information, see [2]). Therefore, although I believe that the proposed method is interesting, the state inconsistency challenge has partially been addressed by related work, and thus the authors should better highlight their contributions in the context of related work.
- One concern is that the baselines regarding partial observability are not very established in MARL community. Some of them have not even been published at a top-tier AI/ML venue. To further improve the paper, I would suggest that the authors also include well-known methods (as baselines) based on alternative ways to deal with partial observability (e.g. [3], [4], [5]).
- The attached repo does not contain any files.
- Minor weakness: The authors do not include information about hyperparameter details of the baselines.
- Minor weakness: There are many typos and grammatical errors (e.g. lines 240-244). I suggest that the authors proofread carefully the whole manuscript.

### Questions
- How did the authors make the MPE' Navigation task (Spread) continuous ?
- What was the time horizon in SMAC tasks? Can the authors provide the plots from these experiments?

### Soundness
3

### Presentation
2

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
The paper introduces Reconstruction-Guided Policy (RGP), a method in cooperative multi-agent reinforcement learning (MARL) to address partial observability, where agents rely on limited, localized information instead of global state access. Traditional MARL approaches train with global state access but deploy with reconstructed state representations, often reducing robustness and performance. RGP is evaluated on both discrete (SMAC, SMACv2) and continuous (predator-prey, cooperative navigation) environments, demonstrating superior performance and higher retention rates compared to methods like PTDE and SIDiff during centralized training and decentralized execution. Ablation studies and retention analysis further validate RGP’s effectiveness in preserving agent dependencies and decision consistency, showcasing its versatility in various MARL scenarios with observability challenges.

### Strengths
1. Proposes an innovative approach for state consistency in MARL, which mitigates errors from training-execution state inconsistencies.

2. Effectively captures inter-agent relationships, improving collaborative performance.

3. Demonstrates versatility and strong performance in both discrete and continuous action environments through extensive experiments.

### Weaknesses
1. Limited exploration of potential biases introduced by the generative model in state reconstruction, particularly in complex environments.
2. The approach’s scalability to more agents and highly dynamic environments is not thoroughly evaluated.
3. The theoretical foundation for using diffusion models over other generative models could be further clarified, as comparable methods like VAE and MLP produced similar results.
4. Misleading use of letters/symbols, unclear annotations on some images, poor writing and reading experience

### Questions
1. The paper uses $\epsilon$ repeatedly across equations, specifically in Eq (3) and Eq (6). Could you clarify why the same $\epsilon$ notation is applied in both contexts? Given that Eq (3) refers to a noise variable for the diffusion process while Eq (6) applies to the exploration parameter, distinguishing between these variables would improve clarity and reduce confusion.
2. Figure 2 is challenging to interpret with respect to the network design for RGP. Could you provide a more detailed explanation of how each component in Figure 2 maps to the decision and guidance modules described in Sections 4.1 and 4.2? Specifically, illustrating the data flow within and between these modules and explaining how key operations like the generative model, RNN, and attention mechanisms are integrated would be very helpful.
3. Could you elaborate on the robustness of the learned policies when deployed in environments with potential state changes? How well does RGP handle discrepancies between the training and execution environments, especially if the state dynamics change unexpectedly? Additionally, have you considered incorporating techniques like domain randomization or online adaptation to improve robustness in dynamic deployment settings?
4. The large standard deviations observed in baseline methods like SIDiff (Table 2) and QPLEX (Table 1, 3s5z vs 3s6z) suggest significant variability in these baselines’ performance. Could you clarify the potential sources of this variability? Additionally, could you explain the rationale behind selecting baselines with such high variance, as they may impact the reliability of comparative assessments?
5. While the paper uses a diffusion model for reconstructing agent-wise states, the ablation study in Figure 6 suggests that alternative models (e.g., VAE, MLP) yield similar performance. Could you provide further justification for the choice of the diffusion model over simpler architectures, especially given the increased computational complexity?
6. The paper evaluates RGP in multi-agent environments with relatively small agent counts. How scalable is the proposed approach in scenarios with a significantly larger number of agents, where maintaining agent-wise state consistency could become computationally intensive?

### Soundness
3

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
3

### Summary
The authors introduce a method, Reconstruction-Guided Policy (RGP), which consists of a decision module and a guidance module. The decision module uses a diffusion model to reconstruct a per-agent agent-wise state from an agent’s partial observation of the full environment state which captures the agent’s relationship to other agents. This reconstructed agent-wise state is then used to condition a policy for agent action selection. The guidance module uses an attention-based model to guide the reconstructed agent-wise states. This ensures that the information agents condition on during acting and training remain aligned which reduces error accumulation and improves learning.

### Strengths
* The approach to guide the reconstruction of the individual agent-wise states is interesting and using a diffusion model in reinforcement learning is also interesting.
* The authors conduct detailed ablation studies to disentangle which aspects of their method have the greatest impact on algorithm performance. 
* The authors test their method in continuous and discrete action space environments.

### Weaknesses
 * The paper has multiple grammatical errors and spelling mistakes. 
* The illustrative example in Lines 71 - 80 is difficult to follow. I think the authors are trying to say that agent $x_1$ incorrectly assumes that agent $x_0$’s coverage is represented by the 2nd and 3rd elements in the state vector instead of the correct 3rd and 4th elements. Is this what the authors mean here? Since this is an example used to illustrate the necessity of the method, I think it can be explained more clearly. 
* While it is beneficial that the authors benchmark on SMACv2 instead of only on SMAC it is still quite a limitation in the work that most of the conclusions regarding the method are drawn from results on SMAC. This together with only 3 continuous action space benchmarking tasks is a rather limited evaluation set and not very extensive as the authors mention in the paper. 
* When there is improvement over a baseline it is slight and oftentimes within one measure of error of other methods. For example, in Table 1 RGP+HPN overlaps with the results of HPN-QMIX on all scenarios and RGP overlaps with QMIX, VDN or QPLEX on all scenarios. 
* In Table 3, the error is not taken into account when computing the Performance Improving Ratio of one method over another. This sketches an incomplete picture since it only uses the mean. For a more statistically sound comparison, error propagation should be incorporated into these calculations using standard error propagation techniques. Similarly, for the Performance Retention Ratio of one method over another in Table 2. 
* In Appendix C, the authors show that using an MLP to generate the per-agent state leads to similar performance as using a diffusion model. The MLP is less computationally expensive, why do the authors not use this?

### Questions
* There is no code available, the link the authors have provided seems to only have a readme containing no text except the work readme. Could the authors please fix this?
* Could the authors elaborate on how the guidance module shifts focus to agents instead of to observation features?
* Could the authors please elaborate on how the decentralised execution differs from centralised training with decentralised execution in Section 5.3? 
* The term dimensional-wise state is used but not clearly defined. What do the authors mean by this and can the authors clearly contrast this with the agent-wise state which is a key concept in the work?

### Soundness
3

### Presentation
1

### Contribution
2
