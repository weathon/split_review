# Flex: End-to-End Text-Instructed Visual Navigation with Foundation Models

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
End-to-end learning directly maps sensory inputs to actions, creating highly integrated and efficient policies for complex robotics tasks. However, such models are tricky to efficiently train and often struggle to generalize beyond their training scenarios, limiting adaptability to new environments, tasks, and concepts. In this work, we investigate the minimal data requirements and architectural adaptations necessary to achieve robust closed-loop performance with vision-based control policies under unseen text instructions and visual distribution shifts.
To this end, we design datasets with various levels of data representation richness, refine feature extraction protocols by leveraging multi-modal foundation model encoders, and assess the suitability of different policy network heads. Our findings are synthesized in \Flex \ (\textbf{\texttt{F}}ly-\textbf{\texttt{lex}}ically), a framework that uses pre-trained Vision Language Models (VLMs) as frozen patch-wise feature extractors, generating spatially aware embeddings that integrate semantic and visual information. These rich features form the basis for training highly robust downstream policies capable of generalizing across platforms, environments, and text-specified tasks.
We demonstrate the effectiveness of this approach on quadrotor fly-to-target tasks, where agents trained via behavior cloning on a small simulated dataset successfully generalize to real-world scenes, handling diverse novel goals and command formulations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studied robust multimodal representations for drones. It combines spatial and lexical features via patch-wise descriptors from VLMs. The training pipeline for closed-loop visual navigation agents that generalize across unseen environments, using real-time natural language instructions to achieve adaptability well beyond the training scope. Extensive experiments on drone fly-to-target tasks, showcasing the ability in generalization and real-world deployment

### Strengths
1. This paper is well written and easy to read.
2. The experiment part is good with analysis in feature robustness quality. Real-world experiments are given.

### Weaknesses
1. The motivation of using mask-based patch features is unclear to me. I think it can be simply replaced by ViT style patch feature encoding and attention-based interaction. And for some downstream policy nets like MLP, the spatial feature is eliminated by average pooling. Why the spatial dimension is necessary?
2. Following above, I do not find any ablation studies on different feature designs.

### Questions
See weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces FLEX, a method for making drones understand and follow natural language commands. Instead of building everything from scratch, it cleverly uses an existing vision-language model (BLIP-2) to process both camera images and text instructions. The system was trained on simple simulated scenarios with just two colored balls, yet surprisingly, it worked well in real-world tests with various objects. The key innovation is how it breaks down camera images into patches and processes them alongside text commands, allowing the drone to understand both what it sees and what it's looking for.

### Strengths
1. Integrating visual navigation with the vision-language foundation model is an interesting direction.
2. The performance of this paper is reasonable with targeting and query on a limited set of objects.
3. The paper writing is in general good except the introduction.
4. The paper evaluates their methods in both simulation and real scenarios.

### Weaknesses
1. The paper writing is strange where the introduction section is quite similar to related work.
2. The training data seems to be rich with 1, 1M, 2, 2M, however those four datasets contain only a limited amount of target, and query, which I think is not enough for an open world navigation paper.
3. In addition the paper didn't handle how to solve image sequences for navigation work, which means that they predict action frame by frame.
4. One interesting thing is that in order to correctly navigate in the scene, actually we need to know the depth information, however, the amount of data the paper trained is not enough for that kinds of generalization.

### Questions
1. I am mostly interested on how the evaluation data is different from the training data. I am happy to fix my score, if I could understand the performance is not from scene memorization.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper conducts an empirical study on using features extracted by frozen Vision-Language Pretrained Models (VLMs) for downstream policy learning in object-guided quadrotor visual navigation. The policy is trained with synthetic data in simulation and demonstrates a real-world deployment example, providing an initial test of generalizability.

### Strengths
1. The motivation to investigate frozen VLM encoders for semantically rich and spatially aware embeddings without extensive retraining is clear and well-grounded, offering a promising approach to simplify training in complex robotic tasks.
2. The experimental setup is thorough, exploring various dataset configurations and policy architectures, which provides valuable insights into design choices for multi-modal robotic policies.

### Weaknesses
1. Limited Task Scope: While the use of VLM features for visual navigation is compelling, the experiments are restricted to quadrotor object navigation. Broader experiments across different robotic tasks or navigation scenarios could help demonstrate Flex’s general applicability, aligning with the paper’s claims of “closed-loop visual navigation agents that generalize across unseen environments.” The current evaluation does not sufficiently demonstrate the claimed generalization capabilities beyond the specific quadrotor setup. For example, the approach could be tested on manipulation tasks or navigation with different robot morphologies to better assess its versatility.

2. Feature Extractor Generalizability: Although the study aims to investigate “suitable feature extractors for text and vision-based robotics learning,” the experiments focus solely on BLIP-2 and modifications to its Q-former. Including other VLMs, such as CLIP or ImageBind, would strengthen the claim of generalizability and demonstrate the adaptability of the proposed method across diverse VLM architectures. The paper lacks a comparative analysis of different VLM feature spaces, which is crucial for understanding the robustness of the proposed approach. The choice of BLIP-2 appears somewhat arbitrary without a clear justification based on empirical evidence or theoretical considerations.

3. Task Complexity: In the current setup, the target is observable from the beginning, and language instructions are relatively simple. Visual navigation in complex settings involves learning semantic associations between language and visual cues and exploring the environment effectively to locate and reach the target. Here, the task primarily involves target identification and navigation, with limited indication of the benefits of end-to-end learning over modular approaches like GOAT. Clarifying the advantages of end-to-end learning in this setup would improve the paper’s impact. The current task setup does not fully leverage the potential of VLMs for complex reasoning and planning.

4. Language Instruction Scope: The difficulty and complexity of language instructions in the dataset are not discussed. Unlike works in Zero-Shot Object Navigation (ZSON) or Zero-Shot Vision-and-Language Navigation, which leverage the language comprehension capabilities of VLMs, the findings in this paper are limited to basic instructions. This limitation makes it challenging to support claims of Flex being “user-interactive,” as the current level of interaction falls short of handling more complex language instructions effectively. The lack of diversity in the language instructions limits the assessment of the model’s ability to understand and act upon complex commands.

### Questions
See weakness

### Soundness
2

### Presentation
1

### Contribution
2
