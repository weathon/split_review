# Learning to Model the World with Language

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
\begin{hyphenrules}{nohyphenation}
\ignorespaces
\vspace{-0.5ex}
To interact with humans and act in the world, agents need to understand the range of language that people use and relate it to the visual world. While current agents can learn to execute simple language instructions, we aim to build agents that leverage diverse language---language like ``this button turns on the TV'' or ``I put the bowls away''---that conveys general knowledge, describes the state of the world, provides interactive feedback, and more. Our key idea is that \emph{agents should interpret such diverse language as a signal that helps them predict the future}: what they will observe, how the world will behave, and which situations will be rewarded. This perspective unifies language understanding with future prediction as a powerful self-supervised learning objective. We instantiate this in Dynalang, an agent that learns a multimodal world model to predict future text and image representations, and learns to act from imagined model rollouts.
While current methods that learn language-conditioned policies degrade in performance with more diverse types of language, we show that Dynalang learns to leverage environment descriptions, game rules, and instructions to excel on tasks ranging from game-playing to navigating photorealistic home scans.
Finally, we show that our method enables additional capabilities due to learning a generative model: Dynalang can be pretrained on text-only data, enabling learning from offline datasets, and generate language grounded in an environment.
\end{hyphenrules}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Dynalang, an agent that grounds language to visual experience via future prediction.

### Strengths
The writing of this paper is clear, and the descriptions and justifications of the methods are comprehensible.

### Weaknesses
1. The technical contribution is somewhat limited, primarily differing from DreamerV3 by adding text tokens to observations. A deeper exploration of Dynalang's components and their significance is needed. For example, an ablation study could help clarify the role of the language token in the world model. Specifically, it is unclear if the language token is directly influencing the learned dynamics or if it is primarily used by the policy network after the world model has generated a latent state. The paper does not sufficiently disentangle these possibilities.

2. The paper lacks a detailed ablation study that could validate the importance of each component in Dynalang. Explaining why the language token is necessary, particularly if it only serves as input for the policy network, would provide valuable insights. For instance, if the language token is simply concatenated to the latent state before the policy network, the world model itself might not be learning to incorporate language information into its predictions of future states. This would significantly weaken the claim that Dynalang is truly integrating language into its world model.

3. While the paper explores various game environments, they appear simplistic. Evaluating the method on more challenging games, such as Crafter or Minecraft, would enhance the paper's credibility. The environments, while diverse in their language requirements, do not fully capture the complexities of real-world scenarios where visual and physical interactions are more intricate. The current environments may not be sufficient to demonstrate the scalability and robustness of Dynalang.

### Questions
What are the primary challenges addressed by the article? And what are its main contributions?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the challenge of enabling RL agents to comprehend and act based on complex language input. The proposed framework, Dynalang, enhances agent performance by incorporating language signals into the prediction of future states. Notably, Dynalang builds upon DreamerV3 by introducing text tokens into observations at each step. Experimental results demonstrate its effectiveness across various games, such as Homegrid, Messenger, Habbit, and LangRoom, outperforming previous language-conditioned RL baselines.

### Strengths
1. The paper addresses a compelling problem by enabling RL agents to understand intricate human language, expanding beyond straightforward task instructions, which is an understudied but important area in RL research.

2. The paper's writing, especially in the introduction, effectively highlights the core problem and how Dynalang provides a solution.

3. The study includes experiments across multiple game environments and consistently demonstrates improvements over existing language-conditioned RL methods.

### Weaknesses
 - The title is a bit over-claimed, in the sense that the proposed model is still learning to model “one environment” at a time, particularly for the action dynamics as multimodal representation generation. At least an experiment or novel method is required to learn to model some worlds (environments) and generalize to a held-out test world – this would justify the “modeling the world” parts of the claims.
- While claimed to be flexible, in many applications, the instructions of a task will only take place at the beginning of the episode while the rest is the robots’ job to accomplish the instructed tasks, where the proposed multimodal alignment will only be performed from the beginning few frames of the episode. How does the proposed method work under such conditions? E.g., how would the method benefit from such an alignment in environments such as ALFRED [1] or TEACh [2]?
- In Section 4.4, the performance of the actual SOTA models need to be reported as well, even if the proposed method is inferior to them. There are reasons why modularization and use of certain foundation models is beneficial in these long horizon complex (at least closer to) real world tasks.
- The environments, if at all except for navigation, are all quite toy-ish, where the visual observations are of fairly low fidelity. Since the proposed method heavily relies on the future representation predictions, examining the method on more realistic embodied environments would strengthen the work more.

### Questions
1. How does the paper ensure that the agent can effectively follow language corrections in the Homegrid environment? Are auxiliary reward signals used to guide agent learning?

2. Could you provide more details on the training process? Is the network trained from scratch, or is the world model pre-trained?

3. Have you considered using an LLM as the core of the world model, given its strong language modeling capabilities?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a conditional generative model that aligns both image frames and textual instruction tokens (one at a time) to produce multimodal future representations that can encompass visual frames, textual tokens, as well as motor actions, for controlling an agent in an environment.
The proposed method is claimed to align the visual-linguistic representations better, while encouraging the models to understand the world-dynamics in a generative modeling manner.
The method is tested on four simulated embodied environments where the agents follow certain language instructions, where performance gains are reported against two off-policy RL baselines.

### Strengths
- The observed multimodal alignment mechanism is interesting and with experimental justification.
- The overall proposed method is neat, where the generative mechanism is a sound and interesting idea to model the visual-linguistic dynamics of the work.
- Consuming all modalities in one model as conditional generative models is neat.
- The paper is well written and easy to follow.

### Weaknesses
Although the motivation is promising, the method and experiments do not support the claim.
1. It is confusing that the authors use a multimodal model including both text and images to demonstrate the idea of using language to model the world. Images also convey general knowledge and describe the state of the world, then why can't we also model the world with images / videos? The authors should provide more evidence to demonstrate the unique importance of language to support their claim.
2. The method proposed in this paper is quite like the Dreamer V3 model [1] with additional text input. In Dreamer V3 paper, they have already demonstrated the effectiveness of their method, and the authors seem to simply apply it on environments that include text. Then, how to clarify that the improvements come from the the model architecture itself or the text part? There are no experiments to demonstrate this. Notice that the author even don't compare with other model-based methods that are more similar to their proposed method, although they claim they compared with them in the introduction.

### Questions
- The proposed method shares some similarities with generative video-guided planning (at least at their high-levels), such as [3]. Could you elaborate more on why this is not an incremental concept on top of these works? (Also these works use supposedly much stronger generative models that can tackle more real-world visual observations.)
- What if the language instruction has a much shorter token span and the visual frames are much longer? How do they pad to each other or what would be the token used when language is exhausted out?
- Typos in “Future Prediction” of Section 3.1 – “whih” should be “which”.

[3] Dai, Yilun, et al. "Learning universal policies via text-guided video generation." NeurIPS 2023

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors argue that an RL agent should use language to predict the next state of the world, which will empower them with the ability to understand the world and thus generate a better policy, instead of directly learn to map language into actions. They propose to build a world model that can predict future language, video and rewards, and demonstrate that training an agent with the world model achieves better performance over other baselines.

### Strengths
1. The motivation is interesting and convincing. The large language models learn rich knowledge about the world by only predicting the next word, so it is reasonable to hypothesize that utilizing language for future prediction is a better way to help agent understand the world.
2. Experimental results show that the proposed method outperforms the baselines.

### Weaknesses
Although the motivation is promising, the method and experiments do not support the claim.
1. It is confusing that the authors use a multimodal model including both text and images to demonstrate the idea of using language to model the world. Images also convey general knowledge and describe the state of the world, then why can't we also model the world with images / videos? The authors should provide more evidence to demonstrate the unique importance of language to support their claim.
2. The method proposed in this paper is quite like the Dreamer V3 model [1] with additional text input. In Dreamer V3 paper, they have already demonstrated the effectiveness of their method, and the authors seem to simply apply it on environments that include text. Then, how to clarify that the improvements come from the the model architecture itself or the text part? There are no experiments to demonstrate this. Notice that the author even don't compare with other model-based methods that are more similar to their proposed method, although they claim they compared with them in the introduction.

[1] Hafner et al. Mastering Diverse Domains through World Models. arXiv 2023.

### Questions
The paper mentioned that at one time step only one text token will be included in the observations and the model output. I don't quite understand the setting here. If this is the case, then the setting is quite limited and it also conflicts with the example "I put the bowl away" you use in the introduction?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
