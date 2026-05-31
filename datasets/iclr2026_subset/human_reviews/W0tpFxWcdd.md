## Human Reviewer 1

### Summary
This paper provides a framework for allowing humans to give observations to an RL agent (human in the loop) during training to improve sample efficiency. The high level idea is to show the agent where a reasonable location to focus attention is with limited samples. They provide four options for giving their agents clues in the space of image inputs. They evaluate their method on a set of vision-based RL experiments.

### Strengths
The general idea of giving agents feedback is interesting and relevant.

The clarity of the paper is moderate. The general idea is described well.

The significance of this work is good. Improving RL-agents by adding humans in the loop is a well motivated idea and this is a good method for it.

### Weaknesses
The originality of the work seems to be reasonable but I think there are missing a section in their related work about human in the loop RL which seems to be the most relevant part of the literature (https://jair.org/index.php/jair/article/view/15348).

In the empirical results the tables (2 and 3) are confusing. I like the confidence intervals (thank you for that) but it is very difficult to tell what is going on. Specifically, it is hard to understand what each of the HINT-FCs changes and why they are different. As well why are these figures not in the empirical section where you discuss them afterward and instead at the very end? Figure 3 is tiny. I can't tell what is going on at all here at all.

There is no description of the limitations of this method. There is no conclusion or general discussion. You should have a discussion about weaknesses and a conclusion not just end randomly.

The generator implementation isn't described very well, specifically the section 3.3 seems critical but isn't very clear.

I think with added clarifications this is a good paper and I'll gladly raise my score if these are addressed.

### Questions
051 - Agents learn faster? In what sense? Time?

041 - Can just use the word "in distribution"

142 - The agent takes in hints as observations. How does it work without hints during inference? 

220 - How do we make sure the agent doesn't over rely on hints?

330 - So a problem with HIL RL is that it isn't possible for the real world to just "stop" and give hints. Is there a way to incorporate this into off policy or offline RL instead?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper addresses the challenge of data-efficient learning from pixels in continuous-control reinforcement learning. It introduces HINTS, a framework where human-designed conceptual hints (such as curvature or orientation) are grounded into numerical cues and provided to the policy through lightweight conditioning schemes. HINTS allows policies to integrate structured guidance with visual input, improving learning speed and stability. Experiments on standard benchmark tasks show that HINTS significantly outperforms vision-only baselines and often matches state-based agents under the same sample budget.

### Strengths
1. **Conceptually simple and practical.** The core idea is straightforward yet useful in practice—real-world agents can often benefit from human-provided hints or structured cues, making the approach both intuitive and implementable.
1. **Appropriate empirical design.** Results are averaged over 50 random seeds, providing good statistical confidence; I appreciate this, as many papers report results with far fewer runs.
1.** Well-structured presentation.** The paper is well signposted, with each experimental subsection beginning with a clear takeaway that makes the narrative easy to follow and the results easier to interpret.

### Weaknesses
1. **Clarify the generator and hint definitions.** The paper provides intuitive explanations for the generator and hints, but is unclear what exactly they are at the implementation level. My understanding is that the generator is a hardcoded rule that maps environment states to handcrafted features (the hints). Please clarify how G is implemented in each domain and what form the hint vectors take in practice. If the hint is just a handcrafted feature, then HINTs is simply bypassing the challenge of learning from pixels by having a human provide some useful features so the agent doesn't have to learn features on its own. 
1. **Weak Results.** Results in Tables 2 and 3 look statistically insignificant. I'm not sure what if the +/- uncertainty represents standard error, 95% confidence interval, etc., but the uncertainty intervals for HINTs are quite large and often overlap with the uncertainty intervals of other methods. 
1. **Ground-truth dependency.** The paper claims that HINTS “does not depend on the availability of ground-truth scene information,” yet all reported experiments appear to rely on privileged state access to compute the hints. It would strengthen the paper to include at least one setting where hints are inferred without using ground-truth data.

1. **Presentation and layout issues.** Many tables and figures appear far from their in-text references and are sometimes cited out of order, which disrupts the reading flow. Please reorder or reposition them closer to the discussion paragraphs. In addition, several figures contain text that is very small and difficult to read; enlarging labels or simplifying legends would improve clarity.

Two comments:

* > Similarly, our approach, introduced in Sec 2-3, gives human experts a means of conveying concepts that guide the system toward effective control strategies, freeing them from the onus of providing clean, complete training examples. 

    This idea is reminiscent of Guided Data Augmentation (GuDA) [1], which generates expert-quality augmented data by leveraging human intuition about what constitutes task progress. In GuDA, the human is not required to *generate* expert actions directly but only to *identify* whether a given trajectory exhibits expert-level behavior.

* I think it's worth explicitly mentioning that it is reasonable to expect a human to identify or design such cues in real-world tasks. Part of the LR community really dislikes priors like this, but I say it's a very reasonable expectation for the targeted problem settings.


[1] Corrado et. al. Guided Data Augmentation for Online Reinforcement Learning and Imitation Learning. RLC 2024. https://arxiv.org/abs/2310.18247

### Questions
1. Is the generator a hardcoded, task-specific rule? Is the hint just a handcrafted feature?
2. Can the authors comment on the statistical significance of the results in Tables 2 and 3?

### Soundness
3

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper proposes HINTS, a framework that integrates human-intuited conceptual cues into reinforcement-learning (RL) training for continuous-control tasks under partial observability. Instead of demonstrations or full human supervision, the approach introduces a programmatic generator that emits grounded hints (e.g., curvature, angular velocity, or goal distance) representing the kind of coaching guidance a human might give. These hints condition the policy through four possible mechanisms—latent concatenation (LC), additive (AC), feature-wise affine (FC), and masked conditioning (MC). The authors empirically evaluate HINTS on image-based Classic Control, Car Racing, and MuJoCo Locomotion domains, demonstrating high sample efficiency and strong performance.

### Strengths
Compelling idea: Human‑intuitive coaching as grounded cues, bridging between pure RL and demo‑heavy IL.

Breadth of evaluation: Classic Control, CarRacing (including Hairpin distribution shift), and MuJoCo locomotion

Informative ablations: Utility of targeted hints over full/partial state, suggesting careful hint design matters.

Consistent gains under data limits: Notably in Classic Control and Humanoid, where HINTS trails only DAGGER but beats PPO‑RGB.

### Weaknesses
In the introduction, the contribution is motivated while comparing it to behaviour cloning methods. However, there are other human feedback methods in reinforcement learning. I encourage authors to position themselves using the survey paper here and make the necessary comparisons: https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.584075/full

Opaque generator design. The paper does not detail how G computes curvature, on-track flags, etc.(key for reproducibility).

No clear selection rule for conditioning schemes. LC/AC/FC/MC are task-dependent but unexplained; a unified comparison in the main text is missing. I would pick only FC in the main text, and explain alternatives with comparison in the appendix.

Missing code release

### Questions
How does HINTS differ from frameworks in feedback RL literature?

How are hints are generated during training?

Please clarify generator's design, does it access privileged state?

Can hints learned in one domain (e.g., curvature in Car Racing) transfer to related environments without retraining the generator?

How should one pick among LC/AC/FC/MC?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
2

---

## Human Reviewer 4

### Summary
This paper investigates the use of "human coaching" to enhance the learning efficiency of reinforcement learning agents. The authors introduce a hint generator that processes conceptual human hints and a hint-conditioned policy that integrates these hints. The proposed approach is evaluated on a selection of MuJoCo and Car Racing tasks. Experimental results demonstrate that the method outperforms baselines that do not incorporate human hints.

### Strengths
1. The motivation of this paper is clearly established. The capacity for a RL agent to integrate and utilize external conceptual hints is a functionally important yet empirically underdeveloped research domain. This capability is significant because it allows the learning process to move beyond simple reward maximization based solely on raw environmental feedback. 

2. While some clarification is needed, this paper is generally well structured.

### Weaknesses
1. The reviewer has major concerns regarding the core technical contribution of this work. While the authors characterize the proposed methodology as Human-in-the-Loop Reinforcement Learning, the implemented mechanism appears to function primarily as advanced input feature engineering. The approach involves providing the agent with additional, privileged information as extended input features to the observation space, which facilitates the learning process. Critically, the reviewer notes a lack of genuine, dynamic interaction or feedback between the learning policy and the human operator, which is typically the defining characteristic of a true HiL system.

2. The proposed approach raises serious concerns regarding scalability and generalizability. A significant limitation is the reliance on manual intervention; specifically, for each new task, users are required to design and provide a distinct, tailored set of 'cues' or hints.

### Questions
The current experimental validation is confined to a restricted set of environments. To conclusively demonstrate the robustness and broader applicability of the proposed method, the experimental section requires significant expansion. Specifically, the inclusion of results from more diverse and complex environments—such as an expanded suite of Mujoco tasks, challenges from the DeepMind Control Suite (DM Control), or large-scale strategic domains like StarCraft II—would substantially strengthen the credibility of the findings.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4