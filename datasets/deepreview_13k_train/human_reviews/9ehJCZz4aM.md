# Learning Closed-Loop Concept-Guided Policies from Unlabeled Demonstrations

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
Training embodied agents to perform complex robotic tasks presents significant challenges due to the entangled factors of task compositionality, environmental diversity, and dynamic changes. In this work, we introduce a novel imitation learning framework to train closed-loop concept-guided policies that enhance long-horizon task performance by leveraging discovered manipulation concepts. Unlike methods that rely on predefined skills and human-annotated labels, our approach allows agents to autonomously abstract manipulation concepts from their proprioceptive states, thereby alleviating misalignment due to ambiguities in human semantics and environmental complexity. Our framework comprises two primary components: an *Automatic Concept Discovery* module that identifies meaningful and consistent manipulation concepts, and a *Concept-Aware Policy Learning* module that effectively utilizes these manipulation concepts for adaptive task execution, including a *Concept Selection Transformer* for concept-based guidance and a *Concept-Guided Policy* for action prediction with the selected concepts. Experimental results demonstrate that our approach significantly outperforms baseline methods across a range of tasks and environments, while showcasing emergent consistency in motion patterns associated with the discovered concepts. Our code and models will be public.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework for long-horizon imitation learning by combining the ‘automatic concept discovery’ module and the ‘concept-guided policy learning’ module. The former is trained without human annotations of the sub-sequences of robot trajectories. Instead, they assign the concept to the trajectories in a self-supervised manner.

### Strengths
The paper proposes a method for hierarchical imitation learning by discovering the motion ‘concept’ without human annotation and motion policy conditioned on the discovered concept. The three tricks for discovering these concepts stably from trajectories seem to be reasonable.

### Weaknesses
Some literature potentially relating to the method or problem setting of this paper is missing. For example, learning abstract action with clustering (BeT[1]) and with VQ-VAE[2]; please contrast this work with others listed above.
The proposal is tested with the Robosuite (MimicGen) benchmark, whose task is inherently highly compositional, so the concept discovery seems to be relatively easy. It is interesting to see the result with an “in-the-wild” dataset, such as dataset collected with a ‘learning from play’ manner [3].

### Questions
1)	Why is only proprioception used for the automatic concept? It seems natural to include observations in addition to proprioception to assign the abstract concept to the time step. How can we generalize it to observation? There may be a case where similar proprioception (e.g., robot pose) but a different observation (e.g., an obstacle in the environment).
2)	How do you decide the total number of concepts/codebooks of VQ-VAE (K)? How robust is the proposal in terms of the number of concepts?

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
3

### Summary
## Research Question
For imitation learning(IL), 1)data annotation requires additional human effort; 2) the inherent subjectivity in manual data collection\annotation leads to manipulation concepts that do not align well with the robot’s configuration, and such inconsistency will accumulate, and 3)  IL will face further difficulties due to the varying and unpredictable conditions encountered at each step. 


## Proposed Method
To mitigate the above challenges, the author proposed a framework that combines automatic concept discovery with closed-loop concept-guided policy learning. Such a framework will take unlabeled demonstration for training and autonomously extract and utilize manipulation concepts directly from the robot’s proprioceptive states.  Specifically, for training, the "Automatic Concept Discovery" module will first derive manipulation concepts automatically. Then, for both training and testing, the "Concept Selection Transformer (CST)" will propose and adjust manipulation concepts in real time during the robot’s interactions with the environment. Finally, the "Concept-Guided Policy (CGP)" utilizes the selected manipulation concepts to execute actions based on instantaneous visual input

### Strengths
1. The idea is a good catch for research questions

The manual annotation(sample efficiency), accumulative action inconsistency, and environmental unpredictability are classic bottlenecks for imitation learning,  and the general idea of "self-discovered sub-policy\concepts" is also not something new. However, the author directly extracts the concepts from the robot’s proprioceptive states,  such design not only mitigates the misalignment caused by ambiguities in human semantics but also adapts dynamically to unforeseen situations. 

2. Appropriate baseline and good performance

The selected baselines are new and SOTA, and reasonable to compare with the proposed method.  Major advances of the proposed method are observed according to Table 1.

### Weaknesses
1. Unclear presentation 

The figures are a little bit messy (e.g. lack the connection of each part in Fig 3, the Closed-Loop Policy part in Fig 2 is unclear  ), but it's a minor point. What matters are: 1) if the discovered concepts are consistent in all demos, i.e. if the concepts are in a unified, task-agnostic space for all demos; 2) For evaluation, it says 950 demos for each task, so does it mean: 2.1) the training data is 950 * |# of task| for single unified policy (set of concepts) and get tested all 6 type of tasks at once( in a mixed way). Or: 2.2) for each task,  it uses 950 demos to train and test only for the task.

For 1), I suppose the concepts are consistent in all demos according to the formula (1), but it's better to be clear at the beginning.  For 2), I'm not sure if it's 2.1) or not, if it's 2.2), the performance will be questionable as it's very close to overfitting. 

2. Less practical problem setting

There was a trend to label the raw robot demonstration automatically, but a more practical problem is the raw demo collection is much more expensive than demo annotation, and therefore, some researchers turn to human-play data to get more data to use. And it's the same story for this paper, the expensive robot demo collection reduces the significance of this work 

3. Concern about generalizability and scalability 

Though the paper claims better performance (compared with baselines) in a more diversified initial environment,  here the diversity is only expressed by object positions and placement angles. Some concerns are: 1)What if there is concept inconsistency in the demos,  e.g. to do the same manipulation, in a different way; 2)With the growth of the demo amount, will the # number of concepts converge or grow fast;

### Questions
Dear author:

Generally, the paper is a decent work, but it needs several extra explanations and explorations.

And I will raise my rating if the following concerns are solved:
1. The concerns in the "Weakness" part.
2. A minor point is to add an IL SOTA baseline specific to the problem, which is not limited to a Diffusion Policy basis.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method for discovering robot actions and manipulation policies from unlabeled demonstration data. It presents techniques for discovering generic action/manipulation concepts and their goals, evaluating progress towards those goals, and generating policies to achieve the goals. This is done using various modern machine learning techniques and problem/loss function formulations. For concept discovery, A VQ-VAE is used to discover concepts and put them into a finite codebook. A transformer model is used for goal state detection. A hypernetwork and another transformer are used for goal state evaluation, and a final transformer is used for goal consolidation. All of these networks are jointly trained using a large combined loss function. Then, concept selection and policy generation are learned using a combination of a transformer and a diffusion policy. Finally, the approach is validated by training on a set of 950 robot demonstrations in 6 different tasks, then evaluated with randomized starting positions (all in simulation). The success rate of different tasks learned via the proposed method is higher than for competing metrics, even/especially in the presence of perturbing noise.

### Strengths
* The paper compares the proposed approach to a set of highly relevant prior work in a fairly direct head-to-head comparison and the proposed approach nearly universally outperforms the prior work by a good margin.

* The approach is a novel combination of several modern techniques to solve a complex open problem in robotics. It expands upon work such as InfoCon by adding policy learning directly into the framework of manipulation concepts.

* The paper is written clearly and the construction of the experiments is well-explained (training, structure of network, etc.), including the re-implementation of baselines.

### Weaknesses
 * The primary weakness of this study is that it only contains a brief evaluation of the quality of the learned skills (i.e., are they generalized, are they more generalized than prior approaches), and a single visual example. Characterizing XSkill "concepts" via K-means clustering is perhaps not the most charitable interpretation of their concepts, as K-means clustering will naturally tend to collect noise in its clusters (noise is one of the stated drawbacks of the xskill results). Ideally there would be some sort of mean similarity score or some other comparison method - even something like a 2D embedding visualization of the different skills and concepts, if possible to generate, would give better faith in the stated quality of the learned concepts. This is a conference about learning representations, so I would love to see more focus on the quality of the representation of "concept". That being said, other papers, including InfoCon, also use final task success as the main comparison metric, so I don't consider this a big enough weakness to reject the paper.


* It is not clear why such a large variety of approaches were used in this paper. Many different transformer sizes were used, in addition to the diffusion policy and the VQ-VAE. Specifically, the use of hypernetworks also seems like an unnecessary addition to what is already a diverse and expressive set of architecture choices.

**Style notes**

* perhaps this is a notational convention I am unaware of, but the parentheses in epsilon^(n) seem like unnecessary clutter.

* Should eq 11 be negative to account for the fact that the log term will always be negative?

* In eq 10, is the selected action from pi_D conditioned on the k selected by p_CST? If so, this could be made clearer, perhaps by splitting into two equations.

### Questions
* At some point, the number of different networks + their parameters runs a risk of over-parameterization and overfitting. This is especially true since it seems that the set of demonstrations were collected over the same set of tasks as used in policy generation and success measurement. Combined with the lack of qualitative cross-task concept comparison or similarity analysis, I do have overfitting worries here. I have no evidence to directly support this flaw other than my own experience training large robotics models, but would still like to know the authors' thoughts on how overfitting is avoided in the proposed approach.

* Why was a hypernetwork used for a single piece of the approach?

* How were the 950 demonstrations in the experiment generated, and were they over all 6 tasks, or a different set/subset of tasks? I was not able to find this anywhere in the paper.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel imitation learning framework for training closed-loop concept-guided policies for robotic tasks, focusing on long-horizon tasks. The framework leverages self-supervised learning to autonomously discover manipulation concepts directly from robotic demonstrations, without the need for predefined skills or human-labeled data. The two main components of the system are:
- Automatic Concept Discovery, which identifies manipulation concepts by analyzing proprioceptive states and assigning discrete embeddings to different task segments.
- Concept-Guided Policy Learning, which utilizes these discovered concepts for policy learning. A Concept Selection Transformer (CST) selects relevant manipulation concepts in real time, while a Concept-Guided Policy (CGP) generates actions based on the selected concepts, using a diffusion policy to handle high-dimensional actions.

The framework is designed to dynamically adjust policies in response to environmental changes, ensuring robust performance across a variety of tasks. Experimental results show that the proposed method outperforms existing baselines in multiple robotic manipulation tasks, demonstrating improved generalization and performance in dynamic environments.

### Strengths
- The approach is highly original in combining concept discovery with closed-loop policy learning. Instead of relying on predefined, human-annotated labels or skills, the system autonomously discovers meaningful manipulation concepts directly from demonstrations. This removes the need for manual intervention and avoids misalignment between human semantics and robot operations.
The use of a self-supervised concept discovery mechanism is innovative, especially in its application to long-horizon robotic tasks. The introduction of a Concept Selection Transformer (CST) for dynamic task execution is novel and enables adaptive behavior based on feedback.
- The methodology is well-designed and robust, incorporating a clear pipeline for concept discovery and policy learning. The experimental setup is thorough, with comparisons to multiple baselines and a wide range of tasks, which demonstrates the effectiveness of the proposed framework.
The paper also includes an ablation study to assess the contributions of different components within the framework, which adds depth to the analysis and validation of the proposed method.
- The paper is clearly written, with detailed explanations of the method, supported by visualizations of the discovered concepts. The distinction between the two main components (Automatic Concept Discovery and Concept-Guided Policy Learning) is clearly articulated, and the figures help in understanding the flow of the framework.
The technical details of the system, including the loss functions and architecture choices, are well-explained.

### Weaknesses
 - Concept Interpretability: While the system autonomously discovers manipulation concepts, it would be interesting to try to explore how interpretable or human-understandable these concepts are. Specifically, a more detailed analysis of the learned embeddings and their correspondence to human-understandable actions would be beneficial. It would also be interesting to see if all the discovered concepts are utilized in downstream policy learning and, if not, what the unused ones look like. Are there any concepts that are consistently ignored by the Concept Selection Transformer (CST), and what might this imply about the concept discovery process?

- Evaluation Scope: Although the paper evaluates the framework on a variety of tasks, the focus is primarily on tabletop manipulation in simulated environments. The tasks, while diverse, still operate within a relatively constrained domain. Expanding the evaluation to more complex morphologies, such as articulated robots with more degrees of freedom, or more complex manipulation tasks, would strengthen the claim that the approach generalizes well. Furthermore, the simulated environments, while useful for development, may not fully capture the complexities of real-world scenarios.

- Lack of Real-World Validation: While the framework performs well in simulation, it has not been validated on real-world robotic platforms. The paper acknowledges this limitation but does not provide a clear roadmap for transitioning the system to physical robots, which is crucial for demonstrating its practical applicability. The challenges of transferring policies learned in simulation to real-world robots, such as dealing with sensor noise, model inaccuracies, and the sim-to-real gap, are not addressed.

### Questions
- There is some line of work using mutual information maximization to discover concepts/skills from demonstration datasets [1, 2] or self-supervised methods [3]. It may help to include some insights into those works.
- While the annotations used in the method section are very stringent and scientifically sound, it can be confusing for readers with less background knowledge or patience to fully understand the message the paper tries to deliver.
- In the automatic concept assignment stage, is the encoder trained separately from other components, or are they trained simultaneously? If the former, how did you prevent the encoder from collapsing to map to the same codebook index?
- Are all the discovered concepts meaningful and physically possible? Can I condition on an arbitrary concept index and the generated trajectories are good to use, or is the Concept Selection Transformer still necessary to act as a filter to rule out discovered but useless concepts?
- How to deal with diversity? In skill discovery works, one common issue is a diverse set of skills/concepts can be discovered, but this diversity is canceled out by a downstream skill/concept selector due to its collapse on one or two most useful skills/concepts. How can you retain all the concepts discovered and demonstrate the diversity there?

[1] Li, C., Blaes, S., Kolev, P., Vlastelica, M., Frey, J. and Martius, G., 2023, May. Versatile skill control via self-supervised adversarial imitation of unlabeled mixed motions. In 2023 IEEE international conference on robotics and automation (ICRA) (pp. 2944-2950). IEEE. 

[2] Peng, X.B., Guo, Y., Halper, L., Levine, S. and Fidler, S., 2022. Ase: Large-scale reusable adversarial skill embeddings for physically simulated characters. ACM Transactions On Graphics (TOG), 41(4), pp.1-17.

[3] Li, C., Stanger-Jones, E., Heim, S. and Kim, S., 2024. FLD: Fourier Latent Dynamics for Structured Motion Representation and Learning. arXiv preprint arXiv:2402.13820.

### Soundness
4

### Presentation
4

### Contribution
3
