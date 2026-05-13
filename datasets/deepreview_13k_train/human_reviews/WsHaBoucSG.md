# Emergent Language based Dialog for Collaborative Multi-agent Navigation

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
This paper aims to provide an empirical study on how to build agents that can collaborate effectively with multi-turn emergent dialogues. Recent research on emergent language for multi-agent communications mainly focuses on single-turn dialogue and simple settings where observations are static during communications. Here, we propose a multi-agent navigation task, a representative task with multi-turn communications and dynamic environment observations: the Tourist (the embodied agent) who can observe its local visual surroundings, and the Guide who has a holistic view of the environment but no foreknowledge of the Tourist's location. The objective of the task is to guide the Tourist to reach the target place via multi-turn dialogues emerging from scratch. To this end, we propose a collaborative multi-agent reinforcement learning method that enables both agents to generate and understand emergent language, and develop optimal dialogue decisions with a long-term goal of solving the task. We also design a real-world navigation scene with the matterport3D simulator. The result shows that our proposed method highly aligns emergent messages with both surroundings and dialogue goals, hinting that even though without human annotation or initial meaning, the agents can learn to converse and collaborate under task-oriented goals.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how to build agents that can collaborate effectively with multi-turn emergent dialogues, it proposes a multi-agent navigation task, to guide the Tourist (the agent) to reach the target place via multi-turn dialogues. It proposes a collaborative multi-agent reinforcement learning method that enables both agents to generate and understand language, and make decisions with a long-term goal of solving the task. Empirical experiments on R2R and CVDN tasks show promising results.

### Strengths
1. It introduces a multi-turn dialog for goal oriented navigation tasks. 
2. It proposes a multi-agent RL algorithm for the task, and shows promising results on two tasks (R2R and CVDN).

### Weaknesses
Based on the motivation of this work, CVDN is a natural task for this method. It is better to show the performance on the test splits (unseen) comparing with SoTA methods, rather than only showing the val split. The current evaluation on the validation set is insufficient to demonstrate the generalization capability of the proposed method, particularly in the context of emergent communication where the agent's ability to adapt to novel scenarios is crucial. The lack of test set results makes it difficult to assess the true potential of the approach in more realistic settings. Furthermore, the paper does not provide a clear comparison with existing state-of-the-art methods on the standard test splits, which is essential for establishing the significance of the proposed approach.

### Questions
1. Is it possible to show the results for Test Unseen on R2R? besides the results on val seen and unseen. Similarly for CVDN dataset.

Minor suggestions:
1. Figure 2 & 3, the font is too small to read.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study introduces a multi-agent navigation task in which one agent, the Tourist, perceives its immediate surroundings, while the other agent, the Guide, has an overarching view of the environment but lacks knowledge of the Tourist's location. The primary objective is for the Guide to direct the Tourist to a specific destination using evolving multi-turn dialogues. The paper details an empirical study centered on developing agents that can collaborate effectively through multi-turn emergent dialogues. To exemplify this, the authors introduce a collaborative multi-agent reinforcement learning technique that enables both agents to generate and understand emergent language. This method is tested with the Matterport3D simulator.

### Strengths
1. The paper introduces a novel framework for emergent communication based on a vision-language navigation task.
1. An empirical study is provided as an example. That will be used as a baseline in future studies.
1. The reviewer believes that the task design will contribute significantly to expanding the study of emergent communication.

### Weaknesses
1. The paper does not sufficiently assess the quality and characteristics of the emergent language, such as its compositionality and its relation to the plan set out by the Guide. Specifically, there is no analysis of how the emergent language encodes spatial relationships, object references, or action sequences. This makes it difficult to understand the complexity and expressiveness of the learned communication protocol. For example, does the language use compositional structures to describe complex routes, or does it rely on holistic, less generalizable encodings?
1. The figures contain very small text, making them hard to understand. This lack of clarity hinders the reader's ability to grasp the experimental setup and results, especially when detailed information is presented in the figures.
1. While the main contribution seems to be the proposal of the task, a large portion of the description is dedicated to the network architecture (Section 3). The authors should provide a more intuitive explanation of the general task framework. Adding pseudocode could help potential readers grasp the proposal more effectively. The current description focuses too heavily on the implementation details, obscuring the core conceptual contribution. A higher-level explanation of the interaction protocol and information flow would be beneficial.
1, The characteristics and details of the compared baseline methods in the experiments are not clear. It would be beneficial to include these descriptions in the Appendix. The paper lacks sufficient detail on the specific algorithms and parameters used in the baseline methods, making it difficult to assess the validity of the comparisons and reproduce the results. For example, what specific reinforcement learning algorithms were used, and how were their hyperparameters tuned?

### Questions
The most straightforward communication approach the Guide could adopt is to repeatedly send the shortest path. How does the emergent language compare with such direct communication? If this hasn't been explored, it would be worthwhile to discuss.

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce a model of communication between two agents, a Tourist and a Guide. The former must navigate an environment to reach a unknown target location following instructions provided by the latter. The Guide, without knowing the current position of the Tourist, must communicate to provide information about the path to the target position. Using two objective functions, one optimizing for Guide localization of the Tourist and one for optimizing for Tourist navigation, they report better results over previous work on two visual-language navigation datasets.

### Strengths
I think the authors investigate the interesting problem of embodies agents communicating while having different roles, a follower and a guide. The lack of any human-annotation in the training process makes it for cheap method to train embodies agents and the ablation study conducted supports the modelling choices made by the authors. Furthermore, the usage of realistic datasets shows that the method can scale to natural setups and is an important step towards deploying agents in the wild. 

Overall, I find the only weaknesses to be in the lack of an in-depth analysis of the emergent language. (more in the following section) The only analysis shown is qualitative one and is relegated to the appendix. Although, I don't see it a fundamental requirement to accept the paper, what prevented me from giving it a higher score is the lack of a deeper analysis. 

Finally, provided a minor restructuring of the manuscript is done, such as moving the analysis to the main body of the paper, I am in favor of including the paper at the conference.

### Weaknesses
As I mentioned in the previous section, I think the major weakness of the paper is in the lack of deep analysis of the emergent language. Computing metrics of emergent languages like topographic similarity (using environment encodings and agent messages) [1] could give an idea of the structure of the agents' protocols. 

A minor weakness that I found is the usage of agents without any pre-encoded linguistic knowledge. Using a LLM as navigation planner, which has shown some potential [2, 3], could solve the problem of training agents that have an opaque communication protocol. 
I am thinking that your method could be used as a fine-tuning approach over existing language-aware models, keeping in mind that the language drift problem [4] should be taken into account. I'd be happy to hear the authors' opinion on this

### Questions
- At the end of the related work section you claim: "we also empower the oracle agent to provide instructions progressively", how is it guaranteed that messages are sent progressively and not all at the beginning? While I'm not challenging your claim, I'm wondering whether it's backed by any analysis work or just by the nature of your sequential communication modules.

- In the training setup section I don't understand why you call the two objective "pre-training" tasks. Aren't they used jointly to train the agents? From the paper, I don't understand, the division, if any, between pre-training and training.

- Why do you choose a vocabulary size of 26? I first thought it was to draw a similarity with the English language, but I then realized by looking a figure 3b that it could be the result of an hyperparameter optimization following an ablation study. Could you please clarify?

- In sec 5.5, how do you compute the reduced 2D space? Could please you provide additional details? They could easily be added to the appendix for a camera-ready version


---------

misc/typos

- In section 4.1 you mention Guest position, do you mean Tourist position?

- In the related work section you mention: "[...] has a similar setting to our work but lets the Guide describe the target position’s observation in a kind of emergent language". I find "a kind of emergent language" unclear, please fix it.

- Please provide a more descriptive Figure 4 caption than the rather vague "Emergent language analysis" 

- "Language based" in the title is probably missing a "-" -> Language-based

Another related paper about navigation and emergent communication is [1]. Despite their communication modules being simpler than your, I think it makes sense to include it in your section surveying the literature.

[1] Patel et al., Interpretation of Emergent Communication in Heterogeneous Collaborative Embodied Agents, ICCV 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a collaborative multi-agent navigation via emergent dialogue, where the Tourist and the Guide learn expressions aligned with both the real-world environments and task-specific dialogue intents. The proposed method enables both agents to generate and understand emergent language, and develop optimal dialogue decisions with a long-term goal of solving the task. The paper provides a real-world navigation scene with matterport3D simulator to showcase the effectiveness of the proposed method.

### Strengths
1. The authors propose a novel multi-agent reinforcement learning (RL) framework complemented by auxiliary pre-training to effectively align emergent language with both the environment and the task.
2. Experimental results on a real-world navigation scene with matterport3D simulator to showcase the effectiveness of the proposed method.

### Weaknesses
1. The paper does not provide a detailed analysis of the underlying rules that the emergent language adheres to, which may limit the understanding of the method. Specifically, it is unclear how the learned symbols relate to the environment and task, and whether these symbols exhibit any compositional structure. Without such analysis, it's difficult to assess the robustness and generalizability of the emergent language.
2. The design of each module of the method is relatively conventional, and no particular contribution was found. The paper does not clearly articulate how the combination of these modules leads to emergent language with the desired properties, nor does it compare the performance of individual modules with existing alternatives to justify their specific design choices.

### Questions
Can you provide some text examples to compare the differences between the text learned from the best baseline and the method learned from your own method?
Can you explain again what advantages the design of each module in the method has compared to the previous method?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
