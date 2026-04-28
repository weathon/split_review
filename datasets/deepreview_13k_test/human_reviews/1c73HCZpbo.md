# REVEAL-IT: REinforcement learning with Visibility of Evolving Agent poLicy for InTerpretability

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Understanding the agent's learning process, particularly the factors that contribute to its success or failure post-training, is crucial for comprehending the rationale behind the agent's decision-making process. Prior methods clarify the learning process by creating a structural causal model (SCM) or visually representing the distribution of value functions. Nevertheless, these approaches have constraints as they exclusively function in 2D-environments or with uncomplex transition dynamics. Understanding the agent's learning process in complex environments or tasks is more challenging. In this paper, we propose REVEAL-IT, a novel framework for explaining the learning process of an agent in complex environments. Initially, we visualize the policy structure and the agent's learning process for various training tasks. By visualizing these findings, we can understand how much a particular training task or stage affects the agent's performance in the test. Then, a GNN-based explainer learns to highlight the most important section of the policy, providing a more clear and robust explanation of the agent's learning process. The experiments demonstrate that explanations derived from this framework can effectively help optimize the training tasks, resulting in improved learning efficiency and final performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an interpretability framework to understand an agent’s learning process in complex tasks (e.g., ALFWorld) through a GNN-based explainer. This method examines policy updates across predefined subtasks and highlights critical sections of the policy network.

### Strengths
the framework provides a structured approach for interpreting the learning progress of agents in long-horizon tasks using a GNN-based model.

### Weaknesses
- the paper's clarity could be improved. Certain terms are referenced repeatedly early in the text (e.g., introduction) but are defined too late or not at all—examples include "node-link diagram," "policy structure," "structure training tasks," and "problem" (line 91).
- the three claimed benefits of "understanding the agent’s performance post-training from the learning process of the policy and the sequences of training tasks" are difficult to grasp. Benefit 1 is too abstract, and lacks contextual detail. In contrast, Benefit 3 includes broad statements unsupported by references (e.g., "which can not deal with the big and complex problems that can not be seen in the real world").
- several key concepts lack references, including SCM and counterfactual methods (lines 95-96), MDP (line 167), and the node-link diagram representation (line 162).
- the paper motivates the question "why an agent can succeed or fail in a task" but lacks examples or case studies that would provide a unique takeaway on RL agents' interpretability.
- section 3’s "Structural visualization of the policy" is hard to understand. Goals are listed, but it is unclear how they are grounded or justified. For instance, it is mentioned that the policy visualization should use a node-link diagram to depict network architecture, but the rationale behind this choice is not explained. Additionally, it is unclear how this visualization allows users to judge the network’s robustness to translational and rotational variances or ambiguous inputs. The "gap" between visualization requirements and actual results remains unaddressed.
- in Figure 1, the authors introduce the GNN-explainer as part of the proposed framework, but Section 4.2 later introduces a GNN-predictor (also in Algorithm 1) without clarifying where it fits within Figure 1, creating confusion.

- the related work in explainable reinforcement learning (XRL) is not up-to-date, lacking recent advances in XRL.
- given that this work offers neuron-level visualization, it would benefit from referencing related literature in mechanistic interpretability (which is for understanding the inner workings of neural networks).
- the claim that prior explanation algorithms cannot model complex behaviours (lines 44-47) lacks evidence. Although (Puiutta & Veith, 2020) is cited to support this claim, it is a survey paper, which weakens the argument.

- how do the authors ensure there is any semantical interpretation w.r.t. part of the policy weights (so that humans can understand) when using GNN-explainer to visualise the policy (section 4.2)? in other words, how could users understand the visualised section of the policy? how could users link the "part of the edges (updated weights)" to the success of the RL agent?

- the GNN-based explainer is suggested to provide an understanding of each subtask’s value in training, yet this explanation seems limited to high-level progress indicators rather than deep rationales behind actions. This contradicts some of the authors’ statements like "a proficient explanation enhances understanding of the agent’s actions and helps improve performance" (lines 60-62). Moreover, the reliance on predefined subtasks limits the framework's applicability in real-world scenarios.

- step 1 in Section 4.2 is difficult to follow, particularly the authors' claim that variability does not affect GNN training. Additionally, the connection between "nodes linked to significant updates" and "activated nodes during the test" remains unclear. The assertion that "REVEAL-IT is distinguished from other explainable RL methods by its independence from external data and structure" is also debatable, as saliency maps do not impose environment or algorithm-specific constraints either.

- in Algorithm 1, it is unclear how the GNN optimizes the training task sequence; the sequence sampling appears to be based only on $P$ (see line 7 in Algorithm 1).

- a brief comparison of REVEAL-IT with baselines is missing, which is important for understanding the reasons behind its performance advantages—whether due to improved planning steps or better-learned low-level behaviours.

- figure 4, relevant to the discussion in Section 5.2, is placed in the appendix. Moving it (or parts of it) to the main text would improve readability and flow.

- the first question in Section 5 ("learning process of an RL agent") does not appear to be fully answered. It’s unclear where this process is visualized—Figure 2 or Figure 3. How could the nodes in Figure 2 be interpretable for users, what are the verbs in Figure 3 (are they subtasks?) and which final task is Figure 3 about?

### Questions
- in Section 5, what is the precise format of the explanation the authors intend to provide? Is the optimal training task sequence itself considered the explanation, as suggested in Section 5.2 (lines 429-471)?

- what is the objective of the controller, and what purpose does the control policy serve? This remains unexplained.

- in lines 100-102, does "updating the policy" equate to "updating the agent’s learning process"? Could the authors clarify this distinction?

- could the authors elaborate on the terms “nodes linked to significant updates” and “activated nodes during the test” in Section 4.2, specifically how their correlation is analyzed?

- where is Figure 3 referenced in the main text?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors propose a framework for interpreting the training process of RL algorithms. Policy updates are visualized with node-link graphs, where the nodes are the neurons in the policy network and the edges are the weights that were updated. A GNN predictor is then trained to predict the RL algorithm’s learning progress, defined as the increase in return on a task after one policy update. A GNN explainer is trained to find which updated weights are most critical for the success of the RL agent, by finding the subset of weights that preserves the GNN predictor’s output given only that subset. The authors demonstrate that REVEAL-IT's explanations can be used to improve training efficiency and performance of various RL algorithms in ALFWorld and OpenAI gym environments.

### Strengths
REVEAL-IT addresses an important challenge in deep RL. 

The method is broadly applicable, as it is agnostic to the environment or (online) RL algorithm.

The performance appears to be quite impressive for Alfworld.

### Weaknesses
The writing is very difficult to follow due to excessive verbosity, vague language and grammar issues e.g. “you can record and correspond to the changes in the value of a specific part of the weights” (line 186) or “the understanding the critical nodes in the RL agent’s evaluation is a crucial pre-requisite for determining the significance of weights updating.” (line 220) The authors should review the paper for conciseness and grammatical accuracy

The GNN Explainer does not seem to provide much human-interpretability. Figure 2: “we will observe that the sections with more significant policy updates will undergo modifications” seems to be a trivial observation rather than something illuminating. It is not uncommon for deep RL models to have millions of weights, so the ability to highlight a subgraph of most important weight updates would still leave the user with far too many to interpret. Could the authors provide concrete examples of helpful insights gained from the GNN Explainer? 

Results tables are missing standard deviations; particularly for Table 2 it is unclear whether the improvements are significant. 

The link to view the project on line 311 is broken. 

Some figure references are broken, e.g. the distribution of training subtasks is figure 3 but referenced as figure 4 on line 430

### Questions
What is the GNN Explainer’s training objective? If it is only trained to preserve the predictor’s accuracy, then it could just output the full graph. 

What is the definition of “active nodes” in Step 1 of section 4.2? 

How exactly does the GNN explainer choose the distribution of subtasks to train on? That does not seem to be a direct byproduct of classifying the most critical weight updates. And how does it help on the OpenAI gym environments which do not involve any subtasks? 

The conclusion states that REVEAL-IT can’t adapt to multi-modal challenges. Why would it not be able to handle non-visual modalities? It seems like it can be applied wherever a neural network policy network is used, which does not seem to be constrained to image inputs. 


In Figure 2, what do the gray shaded regions correspond to? “Thicker connections indicate larger updates in weight amplitude (selected by GNN explainer)” - does this mean that thicker connections indicate weights that were both selected by GNN explainer, and had large updates in amplitude? How were the portions of the policy that are common to several sub-tasks identified? “as the training progresses toward the latter stage, there is a greater overlap between the region with a larger update amplitude and the region triggered by evaluation.” - what does “the region triggered by evaluation” refer to?

### Soundness
2

### Presentation
1

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
This paper proposes a GNN-based explainer to identify critical nodes or components for reinforcement learning (RL) tasks, with the goal of improving interpretability and enhancing the learning efficiency of RL agents. The approach involves visualizing a node graph that represents the RL training process for sub-tasks, and training the GNN-based explainer to approximate the true learning process in order to identify important components (key weights or edges) for the tasks. The GNN explainer is then used to guide policy learning. Results show improvements over standard RL models and language-based approaches (tested on ALFworld and other RL benchmarks).

Overall, the paper presents an interesting direction by learning critical components across multiple RL tasks through policy network responses. However, some technical aspects of the method are unclear and could benefit from further justification and improvement. I have outlined specific questions and concerns below and will give a borderline reject in this initial review.

### Strengths
- **[Motivation]**: The motivation is generally sound; learning from policy behavior appears to be a promising approach for developing interpretable and generalizable policies in complex environments.

- **[Empirical Evaluation]**: The empirical evaluation is relatively comprehensive, and the reported results show the potential of this approach.

### Weaknesses
**[About Problem Definition, Methodology, and Experiments:]**
- 1. The authors assert that variability in learning across models will not pose an issue since the learned explainer is model- or task-specific. However, for applications in multi-task learning, pre-training, or other forms of generalization, this variability is crucial and challenging. For instance, training the same network multiple times may yield high variance in the training process data due to permutation invariance. Empirical evaluation or theoretical justification for this would be useful.

- 2. To ensure the framework is generalizable and learns universal, principled representations, it would be beneficial to further explore the alignment between the learned structural information and the actual policies or concepts, either empirically or theoretically. Approaches could include using sparse autoencoders (potentially with larger models) [1] or examining the alignment between individual components and their corresponding concepts, modularities, interactions, and causal relations [2-5].

- 3. Building on point 2, utilizing these representations could facilitate compositional and hierarchical structures in policy adaptation and generalization. Including evaluations that focus on different levels of generalization would be uesful.

- 4. The impact of network size on the results should be investigated through ablation studies. If the network size is small, do the same phenomena observed in Figure 2 still occur?

- 5. What are the primary benefits of using GNNs for contribution analysis of each node or weight? Why not directly use magnitude, partial derivatives, or conditional mutual information to assess the importance of each weight?

**[About Clarity]**

- 1. It would be helpful to list all objective functions in a separate subsection, particularly the objectives for the GNN predictor and explainers, along with an explanation of how guidance information is provided for policy updates.

- 2. In line 115, the process is mentioned as being similar to a POMDP; please formulate this for clarity.

- 3. There are some typos to address, such as in line 11 of Algorithm 1—should $\pi_0$ be $\pi_t$? Also, in line 432, figure 4 should likely be referenced as figure 3 instead.

**Others**: As a side note, many causal RL works focus on learning world models, akin to a subgroup of model-based RL with interventions, rather than behaviors or policies/reward structures, which differ from the goals of this paper. The authors mention their inability to handle complicated tasks, but a more justified statement regarding this limitation should be provided.




[1] Gao, Leo, et al. "Scaling and evaluating sparse autoencoders." arXiv preprint arXiv:2406.04093 (2024).

[2] Marks, Samuel, et al. "Sparse feature circuits: Discovering and editing interpretable causal graphs in language models." arXiv preprint arXiv:2403.19647 (2024).

[3] Gandikota, Rohit, et al. "Erasing Conceptual Knowledge from Language Models." arXiv preprint arXiv:2410.02760 (2024).

[4] Geiger, Atticus, et al. "Causal abstraction: A theoretical foundation for mechanistic interpretability." Preprint (2024).

[5] Lippe, Phillip, et al. "Biscuit: Causal representation learning from binary interactions." Uncertainty in Artificial Intelligence. PMLR, 2023.

### Questions
I listed the questions and suggestions together with weaknesses in the above section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce an interpretable RL agent, in the context of environments with sub-tasks. The algorithm uses a GNN-based approach to visualise the updates to the policy, and also uses another GNN to implement curriculum learning.

### Strengths
The authors introduce a new framework for RL interpretability which can provide better insights than other methods. The method also includes a curriculum learning component, which produces very strong results on the ALFWorld environment. The authors do also spend some time analysing the results from their interpretability framework, in order to showcase its capabilities.

### Weaknesses
The authors provide a valid criticism of more generic interpretability methods e.g. post-hoc methods like saliency maps. However, this work assumes (unless I am wrong - see below) the environment provides a set of subtasks that can be trained on, which is a large assumption. Therefore the generality of this method is somewhat limited. To what extent do subtasks need to be provided/can be inferred?

The methodology is a bit unclear, as the focus appears to be on interpretability, and then halfway through the paper the authors introduce a GNN predictor and curriculum learning. Curriculum learning is not discussed at all in the Related Works section. And yet the authors show that their method significantly outperforms other methods in ALFWorld (Table 1), so it is clear that this is not just about interpretability. If this is the case, then the authors should be mentioning this in the abstract and from the introduction.

I am also under the impression that environment subtasks are needed for REVEAL-IT, but the authors perform experiments on OpenAI Gym MuJoCo environments, which don't have them? Table 2 indicates that adding REVEAL-IT to existing methods improves their performance, but in Table 1 the authors present REVEAL-IT as its own algorithm, so once again it is unclear what is going on here. Is REVEAL-IT standalone or an addition to existing algorithms?

The paper should be checked for spelling mistakes, e.g., "Strucutral" on page 4.

### Questions
In general the authors need to be clearer about the system they have developed, and if curriculum learning is indeed part of the system, it should be discussed more thoroughly and introduced early on.

Also, very little is said about the Gym tasks, so it is difficult to understand what went on in those experiments, particularly as the standard environments do not have subtasks.

### Soundness
2

### Presentation
2

### Contribution
2
