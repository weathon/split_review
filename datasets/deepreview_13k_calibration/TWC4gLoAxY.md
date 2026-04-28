# Enhancing Human-AI Collaboration Through Logic-Guided Reasoning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
We present a systematic framework designed to enhance human-robot perception and collaboration through the integration of logical rules and Theory of Mind (ToM). Logical rules provide interpretable predictions and generalize well across diverse tasks, making them valuable for learning and decision-making. Leveraging the ToM for understanding others' mental states, our approach facilitates effective collaboration. In this paper, we employ logic rules derived from observational data to infer human goals and guide human-like agents. These rules are treated as latent variables, and a rule encoder is trained alongside a multi-agent system in the robot's mind. We assess the posterior distribution of latent rules using learned embeddings, representing entities and relations. Confidence scores for each rule indicate their consistency with observed data. Then, we employ a hierarchical reinforcement learning model with ToM to plan robot actions for assisting humans. Extensive experiments validate each component of our framework, and results on multiple benchmarks demonstrate that our model outperforms the majority of existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel framework aimed at improving human-AI collaboration by integrating logic-guided reasoning and theory of mind. The key contributions include a method for generating and evaluating logic rules from observational data to infer human intentions and actions, a hierarchical reinforcement learning model incorporating theory of mind for planning robot actions to assist humans, and comprehensive experiments on two datasets demonstrating the effectiveness and generalizability of the proposed model.

### Strengths
1. This paper proposes a novel method that utilizes logical reasoning to generate a broad understanding of the agent’s objectives in a new environment and thus strengthen social perception and collaboration between humans and AI.
2. The detailed experiment analysis shows the effectiveness of the proposed method.

### Weaknesses
1. The experimental tasks seem somewhat weak, as even Seq2Seq (Sutskever et al., 2014) can achieve reasonably good results (Table 1). The tasks, involving simple navigation and object manipulation, do not fully capture the complexities of real-world human-AI collaboration. Specifically, the limited action space and the deterministic nature of the environment may not adequately test the proposed model's ability to handle the uncertainty and variability inherent in human behavior. For instance, the tasks lack the dynamic, multi-agent interactions and the need for complex communication that are often present in collaborative scenarios. Additionally, the evaluation is primarily based on quantitative metrics such as success rate and average number of moves, which may not fully reflect the quality of the human-AI interaction. It would be beneficial to see more complex tasks that require the AI to adapt to human preferences, intentions, and unexpected actions. Additionally, as a human-AI collaboration method, it would be more convincing if a human study could be included if possible.
2. The authors should provide the related work in the main text rather than in the appendix. The related work can help readers who are not familiar with this field quickly gain background information about this work and its positioning. Furthermore, I recommend adding a section in the related work that focuses on human-AI collaboration, as it is highly relevant to the topic of this paper. This section should not just list relevant papers but also synthesize them, highlighting the existing gaps and how the proposed method addresses those gaps. This would help readers better understand the novelty and significance of the contribution.
3. Presentation: (a) I suggest that the authors highlight the best results in Table 1 and clarify in the caption whether each metric is better when higher (success rate) or lower (average number of moves). (b) Watch-and-help is cited twice in references. (c) Citation format like WAH Puig et al. (2020) should be WAH (Puig et al., 2020). Use `\citep` command in latex.

### Questions
Although the author has demonstrated in the experiments that the method in the paper is indeed effective, one point still puzzles me: I understand how theory of mind can assist in improving the effectiveness of human-AI collaboration, but why does logical reasoning help enhance human-AI collaboration? Is it merely because logical reasoning is effective in all similar tasks (i.e. reasoning) rather than just theory of mind or human-AI collaboration? If it is effective in both, why not use this framework for accomplishing more reasoning tasks? I hope the author can provide some analysis or experimental data to elucidate the relationship between logical reasoning and human-AI collaboration.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on exploiting logic rules to guide human-like agents. They design a rule generator and rule evaluator to obtain useful rules given entities and relations, and apply hierarchical reinforcement learning with ToM to plan actions. The results show that the model achieves SOTA performance.

### Strengths
- The method to construct and utilize knowledge graphs to plan action is novel and interesting.
- The experiments show that the proposed method significantly outperforms baselines in various metrics. With the provided standard deviation, the table is more convincible.

I am not familiar with reinforcement learning and am unable to assess this part.

### Weaknesses
 - The definitions of entity, relation, and logic rule are inconsistent with the widely agreed definition in the knowledge graph academia. It seems that the users redefine them in the context of their task, while re-using these terminologies of knowledge graph. This makes the paper a little confusing, especially for audiences with a knowledge graph background.
- Different examples of rules are inconsistent. In (3), an item of a logic rule is `Walk_to(person, bedroom)`, but the examples of rule 1 in Fig.3 contain an item `Walk_to(plate)`. It is inconsistent in whether `Walk_to` needs a person as the first entity argument. I wonder which setting is actually used in the method.
- (Minor) In tables, the best results are not easy for audiences to discover. Please use bold text for the best results, and show ↑ or ↓ for each metric to indicate whether greater or less is better.
- (Minor) There are a few confusing wordings. What is the meaning of "hardness level" in the caption of Tab.1 and Tab.2? Its meaning is more like "non-softness" than "difficulty".

### Questions
In "Weaknesses".

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a framework aimed at improving human-robot perception and collaboration by integrating logical rules and Theory of Mind (ToM). Logical rules provide interpretable predictions and generalize well across diverse tasks, making them valuable for learning and decision-making. Leveraging ToM to understand the mental states of others enhances effective collaboration. 

In this approach, the authors use logical rules derived from observational data to infer human goals and guide human-like agents. These rules are treated as latent variables, and a rule generator is trained alongside a multi-agent system within the robot's cognitive framework. The process involves two stages: first, assessing the posterior distribution of latent rules using learned embeddings to represent entities and relations, with confidence scores indicating consistency with observed data. Second, a joint optimization of the rule generator and model parameters is performed, maximizing the expected log-likelihood.

### Strengths
To assist humans, a hierarchical reinforcement learning model with ToM is employed to plan robot actions.   
Multiple experiments validate each component of the framework, and the results on multiple benchmarks demonstrate that this model outperforms the majority of existing approaches.   
The combination of logical rules, Theory of Mind, and hierarchical reinforcement learning creates a comprehensive framework for enhancing human-robot collaboration and perception.

### Weaknesses
The rule generator and the reasoning evaluator are important but don't show the particular design.  
The Iterative Goal Inference seems that a process of conditional learning, so how to implement this part is not clear enough.

### Questions
Refer to the above comments.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a framework to engage human-AI collaboration by incorporating logical reasoning aiming to develop a machine to help humans work together. In the framework, trajectories of human activities are given, and logic rules that map spatial-temporal states to goals. Then, the agents are deployed to new environments where they need to work together with humans and are trained to help humans predict their goals from the sequence of actions and states. In the experiments, the proposed framework outperformed other SOTA approaches, e.g., in the success rate. Different datasets/tasks and evaluation metrics are used in the evaluation.

### Strengths
The paper addresses an important problem of integrating robots to work with humans. The idea of integrating logical reasoning for generalization in this problem setting seems novel. 
The paper provides good empirical evaluations showing the proposed framework’s advantages against baselines.
The experiments are conducted on practical datasets and environments, they give a great insight into the applications of neuro-symbolic methods, where symbolic logic and neural networks are integrated. Limitations are properly discussed.

### Weaknesses
Although I appreciate the paper’s ideas and evaluations, I found some concerns about the paper.

First, more discussions comparing the proposed approach to related studies need to be provided. Otherwise, it is not easy to understand how we can distinguish the proposed method from existing frameworks, and providing them would help readers understand the literature clearly.

Moreover, some parts of the method explanation are somewhat hard to follow. In Sec 2.3, the query is introduced as $\mathbf{v} = (\mathbf{a}$, $\mathbf{s})$, but there is no specification for these variables. I suppose this is a tuple of a sequence of actions and a sequence of states, but that should be noted explicitly. An intuitive explanation of what $\mathbf{v}$ stands for would help readers.

I list some minor comments:
- In Eq. (5). it is written as $g \in f$, but I’m not sure this is a standard notation because here $f$ is a rule, not a set.
- Typo: double periods in the caption of Fig. 3. 
-  I would kindly suggest including the literature on neuro-symbolic research (e.g. [1,2], but not necessary; it is the author’s choice), since the proposed approach is significantly related to the field, and the community would benefit from this work. The readability of the method explanation could be improved.

### Questions
What are the most related studies? How is the proposed approach compared and superior to them?

Including the time and location in the predicate (in Eq. (4)) would generate a large number of ground atoms (atoms without variables), and typically, reasoners (including probabilistic ones e.g. ProbLog and Markov Logic Networks) need to compute ground atoms to perform reasoning.
Does the proposed framework suffer from the large number of logic representations to be generated in the inference? If not, how does it avoid this problem? Are there any restrictions over the considered language/environments?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
