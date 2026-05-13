# Online-to-Offline RL for Agent Alignment

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Reinforcement learning (RL) has shown remarkable success in training agents to achieve high-performing policies, particularly in domains like Game AI where simulation environments enable efficient interactions. However, despite their success in maximizing these returns, such online-trained policies often fail to align with human preferences concerning actions, styles, and values. The challenge lies in efficiently adapting these online-trained policies to align with human preferences, given the scarcity and high cost of collecting human behavior data. In this work, we formalize the problem as *online-to-offline* RL and propose ALIGNment of Game AI to Preferences (ALIGN-GAP), an innovative approach for alignment of well-trained game agents to human preferences. Our method features a carefully designed reward model that encodes human preferences from limited offline data and incorporates curriculum-based preference learning to align RL agents with targeted human values. Experiments across diverse environments and preference types demonstrate the performance of ALIGN-GAP, achieving effective alignment with human preferences.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an online-to-offline reinforcement learning (RL) framework, ALIGN-GAP, aimed at aligning RL agents’ behavior with human preferences, specifically within Game AI environments. This framework incorporates a transformer-based reward model to encode human preferences from limited offline data and a calibrated preference curriculum that incrementally transitions the agent's learning objectives from maximizing environmental rewards to prioritizing human-aligned behaviors. The experimental results across various game environments highlight ALIGN-GAP’s effectiveness in reducing the alignment gap between agents and humans.

### Strengths
- The approach of fine-tuning a well-trained agent to match human preferences is novel and previously unexplored. The paper presents various challenges for this process and achieves strong performance through well-designed reward calibration and curriculum learning.

- Provides a theoretical justification for the reward calibration method, lending a solid foundation to the alignment strategy.

- Through comprehensive testing, ALIGN-GAP shows consistent improvement in agent-human alignment, proving its practicality and effectiveness in real-world scenarios like gaming.

### Weaknesses
 - I'm curious if fine-tuning a well-trained agent is necessary for aligning it with human preferences. Could training an agent offline, like AlignDiff [1], using the rollout and replay buffer data from the well-trained agent, be more advantageous?
Here’s my perspective in more detail:

  - Fine-tuning a well-trained agent to align with human preferences is challenging, particularly due to unlearning risks. While techniques the authors proposed like reward calibration and curriculum learning help, they may not fully solve the problem. Research (e.g., RLPD [2]) suggests that training a new agent using pre-collected data is often more stable and effective than fine-tuning.
  - Thus, instead of direct fine-tuning, using the well-trained agent’s replay buffer and rollout data to train a new, preference-aligned policy—either offline or online with offline data settings like RLPD—could be more effective. Specifically, it is unclear why the authors chose to fine-tune the agent using a reward model trained on a mixture of agent and human data, rather than directly training a new agent from scratch using the same combined dataset with a method like AlignDiff. This approach could potentially avoid the instabilities associated with fine-tuning and allow for a more direct alignment with human preferences. Furthermore, if offline human trajectories are available, it's not clear why AlignDiff could not be trained directly on this data.
  - The paper criticizes AlignDiff for needing manually designed attributes, but this seems inconsistent. For example, the MuJoCo experiments also rely on manually crafted attributes (such as health, movement, and cost), similar to AlignDiff. In Atari tasks, the paper relies on UMAP for unsupervised clustering of important attributes, but I think manually designing attributes might be simpler and more intuitive compared to relying on additional UMAP training. It is unclear why the authors consider the manual design of attributes in AlignDiff to be a significant drawback when their approach also requires a similar level of domain knowledge, either through reward oracles or UMAP clustering, to define relevant features for alignment.

  Therefore, it would be helpful if the authors could explain the specific benefits of the proposed method compared to using AlignDiff’s offline training (or an RLPD-like setting), supported by experimental results.

- Although the introduction of this paper suggests a focus on game AI settings, the experiments were primarily conducted on MuJoCo locomotion tasks and two Atari games. Expanding the range of experiments to include more varied game environments could help build a more cohesive argument.

### Questions
- In Section 5.4, $\lambda$ in the expression for $\alpha(t)$ appears to be an important hyperparameter, but I couldn't find any information in the paper on how to tune $\lambda$. Could you explain how you tuned $\lambda$ for the experiments with the Linear / Exponential \$\alpha(t)$? 
- In equation (5), it seems that $R_{\text{calibrated}}$ might need to be scaled differently depending on the environment. Does it empirically perform well with just simple subtraction, without considering such adjustments?

### Soundness
2

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
The paper is well-written and clearly presents ALIGN-GAP, a simple method for aligning reinforcement learning (RL) agents with human preferences through an online2offline framework. ALIGN-GAP leverages a Transformer-based reward model to extract human preferences from limited offline data and utilizes a curriculum-based preference learning strategy to gradually shift the agent’s objectives from maximizing environmental rewards to aligning with human values. Extensive experiments across D4RL locomotion tasks and Atari games demonstrate that ALIGN-GAP effectively aligns agent behaviors with human preferences, outperforming several baseline methods. The thorough evaluations, including ablation studies, highlight the robustness and generalizability of the approach. However, the method lacks of theoretical foundations and also suffers from a limited range of experiments. While it performs well in the selected D4RL and Atari game environments, the scope of tasks is relatively narrow.

### Strengths
The strengths of the paper include its clear and well-organized writing, which makes the proposed approach easy to follow. Additionally, the method itself is intuitive and relatively simple, combining straightforward components like a reward model and curriculum learning for preference alignment. This simplicity makes the approach accessible and potentially easier to implement, enhancing its appeal for practical applications.

### Weaknesses
The method lacks of theoretical foundations and also suffers from a limited range of experiments. While it performs well in the selected D4RL and Atari game environments, the scope of tasks is relatively narrow.

### Questions
1. **Data Requirements**: The method relies on high-quality offline human data to build a preference model. How sensitive is ALIGN-GAP to the quality and quantity of this data? Would noisy or sparse data significantly impact the model’s performance?
2. **Theoretical Guarantees**: The paper lacks a rigorous theoretical analysis. Are there any formal guarantees on the stability or convergence of the agent's alignment process, especially when switching between environmental and human-aligned rewards?
3. **Computational Cost and Efficiency**: Given the multi-component nature of ALIGN-GAP (e.g., reward calibration, curriculum learning), what is the computational cost of this method compared to simpler baselines? Could this limit its feasibility for resource-constrained applications?
4. **Evaluation Metrics**: The paper evaluates alignment through performance similarity to human proxies. However, this measure is somewhat subjective. Are there more objective or standardized metrics that could improve the evaluation of alignment quality?

### Soundness
2

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
3

### Summary
The paper  introduces ALIGN-GAP, an innovative framework that enables alignment of high-performing RL agents trained online with specific human preferences. This framework consists of two main components: a reward model trained on limited offline human data to capture preferences and a calibrated curriculum-based learning approach to gradually adjust the agent's goals from maximizing environmental rewards to human-aligned behaviors.
Through experiments in diverse game environments, the ALIGN-GAP approach demonstrates effective alignment across various human styles, achieving behavior that closely resembles human preferences.

### Strengths
1) **Significance of the Problem**: The paper addresses a crucial and emerging issue in reinforcement learning — aligning agent behavior with human preferences, especially in cases where human data is limited and offline. By tackling the alignment problem in online-to-offline RL contexts, this work directly addresses gaps in current RL applications and sets a foundation for broader, practical deployment of RL agents in human-interactive settings.

2) **Well-structured and Methodologically Clear**: The paper is logically structured, with each section building effectively on the last. The clear delineation between problem formulation, related work, methodology, and experimental results enhances readability and comprehension, making it easy to follow the progression from theoretical motivation to practical implementation.

3) **Robust Experimental Results**: The experimental results demonstrate the effectiveness of ALIGN-GAP across a variety of environments and human preference types, showcasing the method’s versatility. The use of both qualitative and quantitative evaluations provides a compelling case for the approach, with detailed analysis that underscores the alignment improvements made by ALIGN-GAP over baselines.

4) **Rationale Behind the Proposed Method**: The approach is intuitively sensible, leveraging a transformer-based reward model and calibrated curriculum learning in a way that aligns well with recent advancements in human-preference modeling. The stepwise, calibrated shift from performance-based to human-aligned behaviors ensures that the agent maintains learned skills while adapting effectively, reinforcing the practical value and feasibility of the proposed solution.

### Weaknesses
1) **Preference Learning Paradigm Clarity**: In Section 4.1, the method constructs a preference learning framework where human trajectories are set as the “winner” samples and agent trajectories as the “loser” samples. This choice is somewhat unclear because agent trajectories may still exhibit successful behavior, albeit not fully aligned with human preferences. This setup raises concerns about whether such binary labeling could unintentionally degrade or "unlearn" the agent's effective skills. It would be beneficial if the authors could further clarify how the method differentiates between genuinely preferred human behavior and successful agent behavior to avoid compromising the agent's performance. Specifically, the reward model training process needs more clarity on how it handles the nuances of successful but non-preferred agent actions. The current binary labeling approach may oversimplify the complex relationship between successful and preferred behaviors, potentially leading to suboptimal reward model training. A more nuanced approach, perhaps incorporating a continuous preference scale or a more sophisticated loss function, may be necessary to address this issue.

2) **Impact of Agent Pretraining**: Building on the previous point, it remains unclear how essential the agent pretraining phase is to the final performance. Would the method still be effective if the agent was trained exclusively with the human preference-aligned reward model, without prior environmental training? Additionally, an analysis of how different levels of pretraining influence the results would provide insight into the dependence on the agent's initial training stage and could help clarify the method’s requirements. The paper lacks a systematic investigation into the necessity of pretraining. It is unclear whether the pretraining phase is merely a convenience or a critical component for the success of the proposed method. A detailed ablation study exploring the impact of varying degrees of pretraining, or even the absence of pretraining, is needed to fully understand the method's limitations and dependencies. This analysis should include metrics that assess both the alignment performance and the agent's overall task proficiency.

3) **Potential Time and Computational Costs**: The ALIGN-GAP approach may be computationally intensive due to the need for separate alignment processes for each human player’s unique preferences. This potential cost in terms of training time, especially for applications requiring frequent preference realignments, raises questions about scalability. It would be valuable for the authors to discuss potential optimizations, such as reusing alignment data across similar preferences or developing faster adaptation techniques to make this approach more time-efficient for practical use. The paper does not adequately address the computational burden of training a separate reward model for each individual's preferences. This limitation could significantly hinder the practical application of the method in scenarios involving numerous users or frequently changing preferences. The authors should provide a more thorough analysis of the computational complexity and discuss strategies for reducing the training time, such as transfer learning or few-shot adaptation techniques.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper conceptualizes a new problem setting for reinforcement learning, namely, the online-to-offline setting, which aims to align RL agents with targeted human values in offline data after extensive online training. The proposed method aims at solving challenges in this setting, e.g., agent unlearning caused by rapid reward shifting. Experiements on Game AI verify the effectiveness of the proposed method.

### Strengths
- The paper proposes a novel problem setting, namely, online-to-offline RL. The authors clearly explain the distinction between online-to-offline and offline-to-online RL. The practical importance of the newly proposed setting is also well explained.
- The proposed method is simple and intuitive, and it well handles the issue of sharp reward shifting in the online-to-offline setting, which is demonstrated by extensive experiments.

### Weaknesses
 - The newly conceptualized setting is termed "online-to-offline", however the proposed method for this setting, namely, reward curriculum, needs access to the online environment in the offline phase, which seems inconsistent with the offline concept. Although, considering the object of this new setting, i.e., leveraging potentially insuficient offline data to align the online learned agent, it is somewhat reasonable to assume access to the online environment, this may still limit the application of the proposed method to some real-world scenarios that are truly offline in the second phase.
- The work only focuses on the Game AI context. It would be nice to see if the method works on more practical applications.
- What causes the agent's failure to learn if we don't explicitly specify "what is preferred by humans but not yet learned by the agent" by Eq. (5)? Since when the preferences of humans and the agent are aligned, $R_{\phi}(\tau)$ would be similar to $R_{\phi}(\tau')$ and so there'll be no significant reward shifting. The motivation to use RM score calibration therefore seems a bit unclear, in contrast to the use of curriculum approach.
- It would be interesting to look into why exactly the agent unlearns when the reward signal shifts rapidly. This reminds me of the recent studies of plasticity loss in the field. I think these work may help understanding this phenomenon.
- Figure 9 is not very persuasive for the purpose of showcasing the effectiveness of the aligning method, since there are only 4 pairs of static images. I think it would be nicer to accompany the paper with videos that compares the performances of different alignment methods.

### Questions
- What causes the agent's failure to learn if we don't explicitly specify "what is preferred by humans but not yet learned by the agent" by Eq. (5)? Since when the preferences of humans and the agent are aligned, $R_{\phi}(\tau)$ would be similar to $R_{\phi}(\tau')$ and so there'll be no significant reward shifting. The motivation to use RM score calibration therefore seems a bit unclear, in contrast to the use of curriculum approach.
- It would be interesting to look into why exactly the agent unlearns when the reward signal shifts rapidly. This reminds me of the recent studies of plasticity loss in the field. I think these work may help understanding this phenomenon.
- Figure 9 is not very persuasive for the purpose of showcasing the effectiveness of the aligning method, since there are only 4 pairs of static images. I think it would be nicer to accompany the paper with videos that compares the performances of different alignment methods.

### Soundness
3

### Presentation
3

### Contribution
3
