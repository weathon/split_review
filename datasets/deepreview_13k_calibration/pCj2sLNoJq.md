# A Generalist Hanabi Agent

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 6, 3, 5, 5, 3, 6, 5, 6, 8, 8

## Abstract
Traditional multi-agent reinforcement learning (MARL) systems can develop cooperative strategies through repeated interactions. However, these systems are unable to perform well on any other setting than the one they have been trained on, and struggle to successfully cooperate with unfamiliar collaborators. This is particularly visible in the Hanabi benchmark, a popular 2-to-5 player cooperative card-game which requires complex reasoning and precise assistance to other agents. Current MARL agents for Hanabi can only learn one specific game-setting (e.g., 2-player games), and play with the same algorithmic agents. This is in stark contrast to humans, who can quickly adjust their strategies to work with unfamiliar partners or situations. In this paper, we introduce a generalist agent for Hanabi, designed to overcome these limitations. We reformulate the task using text, as language has been shown to improve transfer. We then propose a distributed MARL algorithm that copes with the resulting dynamic observation- and action-space. In doing so, our agent is the first that can play all game settings concurrently, and extend strategies learned from one setting to other ones. As a consequence, our agent also demonstrates the ability to collaborate with different algorithmic agents ---agents that are themselves unable to do so.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new approach to utilizing text generation to enable knowledge transfer in more than 2 agents in Hanabi tasks. The proposed method shows performance improvements with different LLMs in ZSC settings. Overall, the paper is well-written and shows some interesting inspirations.

### Strengths
- The paper is well-written
- The idea seems to be promising and novel
- The experiments are extensive

### Weaknesses
 - the text template is not clear enough. What information is included in the text template? Will the text be revealed to other agents? It seems that the template will record all "previous" information which is simply the history of the observations. Then why not use history instead of text recording?
- the author said R2D2 is a foundation of R3D2, but it does not compare to R2D2. Moreover, since R2D2 is not introduced in detail, it is hard to perceive the technical contribution of R3D2
- what's the intuition behind multiplying the state and action embeddings? Where do you integrate the text information? how do you make sure it can accommodate different numbers of agents and task settings?

### Questions
Besides the questions from the weakness. I have a few concerns about the text templates used in the paper:
- if the text is embedded and used by the Q-functions, does it mean the text is better than observation features? Is there any intuition behind this?
- is there any communication between the agents? In Hanabi tasks, the agents can utilize hint actions to communicate information implicitly. If the text is now used, would this shift to explicit communication and potentially risk leaking private information?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new method to train an agent to be able to play the game of Hanabi with the ability to generalize to all game settings and to be able to play with other agents in a zero-shot coordination capability. They do this by reformulating the task as a text task by converting current state and an action and play history into a text representation, embedding it using a language model and then feeding these embeddings into a Deep Recurrent Relevance Q-Network (DRRN) trained in a distributed way with a shared replay buffer. Their architecture called R3D2 uses R2D2 (Recurrent Replay Distributed Deep Q Network) as it’s foundation.

The biggest claim of this work is that no other work before their work has been able to generalize Hanabi agents across game settings.

### Strengths
1.	The paper is motivated well and written clearly, with a sufficient explanation of the game and the existing literature to bring the reader upto speed
2.	The evaluation and experiments are thorough, ablating and justifying all of the pieces. They start with first demonstrating that LM only is not sufficient to play the game. Then they show comparisons against 3 existing approaches.

### Weaknesses
1. The work is Hanabi-centric. It may be possible to apply this same work to other card games as it's mostly the text representation that would change
2. Even with its Hanabi focus, I am unable to see the claims being made in the results section. R3D2 scores lower on Self-play and intra-XP but higher on inter-XP. The grid in Fig 5, also does not have massive increase in scores against R3D2

### Questions
1. Some parts of the setup were a little confusing. eg: “All baselines use R2D2 as a basis” vs “we utilized OP and OBL checkpoints from the original paper which focused exclusively on the 2-player setting”. Were the original checkpoints foundationally R2D2?
2. Is a jump of 3-5 points a big jump in the game of Hanabi, regarding Table 5?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a fundamental challenge in multi-agent reinforcement learning (RL): the difficulty of achieving robust performance across environments beyond those the agents were specifically trained on. To tackle these issues, the authors propose and evaluate their approach in a well-established environment for multi-agent RL, Hanabi, which is commonly used to test cooperation in complex multi-agent settings. The paper makes two primary contributions. First, it reformulates the task using textual representations, motivated by evidence that language can improve transferability. By representing the Hanabi game through text, the authors aim to create agents that are more adaptable and capable of generalizing beyond their training environment. Second, they introduce a novel neural network architecture that combines a language model with the Deep Recurrent Relevance Q-network (DRRN). The results presented indicate that the proposed method achieves high intra-algorithm cross-play scores when trained in a self-play setting, underscoring its capacity for adaptability and teamwork. Additionally, the method performs exceptionally well in inter-algorithm play, highlighting its capability to cooperate with agents utilizing different algorithms.

### Strengths
1. One of the primary strengths of this work is its success in achieving effective transfer learning in a zero-shot setting. The proposed method shows adaptability across varying scenarios without requiring additional retraining, which addresses a significant limitation in existing multi-agent RL models.

2. Through careful evaluation, the authors demonstrate that their approach outperforms existing methods in inter-algorithm play, achieving high scores in cross-play with agents using different algorithms.

3. By representing the Hanabi game through text, this work leverages advances in natural language processing (NLP) and large language models (LLMs), marking a novel direction in multi-agent RL. Their approach allows the potential for more seamless integration with future advancements in language models.

### Weaknesses
1. The reliance on text-based representation, while novel, may face significant challenges in more complex or non-linguistic domains. For instance, domains where numeric data dominates—such as algorithmic trading, where key data points include stock prices and volumes, or robot-taxi applications, where visual and sensory data are crucial—may not naturally fit into a textual framework. An extension or discussion on the applicability limits of textual representation in various domains would provide valuable context and guide future research on adapting the method to broader applications.

2. The self-play performance is relatively poor. Insights into possible contributing factors, such as model structure or training limitations, would be useful. Additionally, outlining potential directions for improving self-play performance, whether through modifications to the architecture, training process, or environment setup, would provide actionable guidance for future work.

3. There is insufficient discussion on the choice of neural network architecture, particularly regarding the component where the element-wise dot product is applied between the embedded observations and actions. Similar ideas have been explored in the literature, such as in https://proceedings.mlr.press/v202/ma23e/ma23e.pdf. The authors may consider incorporating insights from existing explanations in the literature to better articulate the advantages and underlying mechanisms of this architectural choice.

### Questions
1. Could the authors clarify why the focus is primarily on self-play during the training phase? While it is impressive that the proposed method achieves high cross-play scores after self-play training, it seems limiting not to explore other training strategies, especially when inter-algorithm play is a key evaluation goal.

2. Given the novel combination of language model and DRRN components, was there a reason for not experimenting with a wider variety of neural network architectures? Exploring different architectures might reveal other configurations that could improve performance, especially in self-play or more complex settings. Were alternative architectures considered during development, and if so, what were the outcomes? Additional details about architectural choices and trade-offs would be helpful.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper considers the problem of generalization and coordination in multi-agent reinforcement learning (MARL) within the game of Hanabi, focusing on enabling agents to adapt across different game settings and learn to collaborate with unfamiliar partners. To tackle this, the paper makes two primary contributions: first, it reformulates the Hanabi environment using a text-based representation, which enables use of language model to process state and action space, thereby providing a consistent observation and action space across varying player configurations; second, it extends the distributed training regimen of Recurrent Replay Distributed DQN (R2D2) by combing language model with Deep Recurrent Relevance Q-network,  creating what they call Recurrent Replay Relevance Distributed DQN (R3D2), an agent architecture that can process dynamic observation and action spaces in a multi-agent environment. Experiments assess R3D2’s ability to coordinate with both familiar and unfamiliar agents in zero-shot settings and to transfer strategies across different player configurations, evaluating performance across various player numbers and agent types. The authors propose that this approach could support further exploration of generalization in MARL for complex cooperative games.

### Strengths
- The paper considers the important problem of enabling agents to collaborate across different player configurations and game settings, a key challenge for advancing multi-agent reinforcement learning. This focus addresses a critical gap in MARL research, as agents must be able to generalize and coordinate flexibly in dynamic, multi-agent environments, an area relevant to both academic research and real-world applications.

- The key contribution of the paper can be seen as creating a text-based version of Hanabi game. Consequently, the exploration in Section 5 of how current language models perform in the Hanabi environment is a valuable addition, as it highlights the capabilities and limitations of large language models (LLMs) in multi-agent coordination tasks. This analysis opens pathways for further investigation into LLM limitations, potentially contributing to future improvements in language model-based reinforcement learning.

- Within the Hanabi environment, the results indicate that the proposed R3D2 approach achieves effective transfer of strategies across different game settings, demonstrating the agent’s adaptability to variable player configurations.

### Weaknesses
 - The authors make several broad claims in the introduction about multi-agent reinforcement learning (MARL) and the adaptability of agents, but these claims lack supporting evidence or citations. For example, in the following statements: “Artificial agents should do the same  for successful collaboration of artificial and hybrid systems” (line 34-35), “… players are required to infer the beliefs and intentions of their counterparts through theory of mind reasoning” (line 42-43), and “…resulting in misunderstandings and thus a drop in cooperation …” (line 48-49), the authors do not provide empirical data or references to substantiate these claims, limiting the rigor of their introductory motivation.

- The paper does not sufficiently establish why Hanabi is an appropriate testbed for studying adaptability to new settings and collaborators, nor does it explain how findings in Hanabi might translate to real-world collaborative tasks. The link between Hanabi’s in-game interactions and broader applications remains unclear, and this omission leaves open questions about the broader relevance and applicability of the research.

- While the authors cite work by Hu and Sadigh as justification for their choice of Hanabi and as a baseline for comparison, this prior research does not fully support the tasks explored here. A central focus of Hu and Sadigh’s work was on human-AI coordination, which this paper does not directly address. This gap makes the comparison less relevant, as the primary objectives differ significantly.

- The authors critique Hu and Sadigh's approach for requiring an explicit specification of the expected behavior of the learning agent. However, the proposed R3D2 method also requires specific environment settings, which could present a similar or greater burden. The need to configure a consistent environment specification might, in some ways, be less useful than specifying interaction strategies, as discussed in later sections.

- A significant oversight in this paper is the lack of reference to the extensive body of literature on unsupervised environment design in both single-agent and multi-agent settings [1,2]. This research area directly addresses the problem of adaptability and generalization in agent training, which the authors claim to investigate. For the paper’s contributions to be meaningful within the field, it is essential for the authors to engage with this related work and to include comparative empirical evaluations.

- While creating a text-based version of Hanabi contributes to the approach, it is unclear how this addresses the problem of adaptability that the authors set out to solve. Converting the environment to a text-based form, and leveraging symmetries within Hanabi, simplifies many of the original environment’s complexities. As a result, adaptability may not be fully tested here since the text-based version removes many elements that would typically require generalization, making it a fundamentally easier learning problem.
- The approach also necessitates adapting the replay buffer to handle a variable number of players, which could be a limiting factor. Although this modification works here because Hanabi caps players at five, it may not scale effectively for environments requiring more flexibility or involving larger numbers of agents.

- The empirical evaluation of collaboration with other agents is limited to two-player settings, as the other agents require training specific to each number of players. This narrow scope restricts the evaluation, as it remains unclear how these methods would perform in settings with more players. Additionally, because the baseline agents are not trained using a text-based representation, this could lead to an unfair comparison between approaches.

- The authors indicate that all agents were trained using identical hyperparameters (line 374-375), despite the agents having different architectures and representations. Given these differences, it is crucial to tune hyperparameters individually for each agent to ensure a fair comparison, as uniform parameters may disadvantage some agents more than others.

- The explanation given for the relatively low performance of OP (line 410) lacks clarity, and the observed performance of OBL seems promising in comparison to R3D2. However, the current experimental setup does not provide sufficient data to substantiate why R3D2 should be chosen over OBL or how these results might generalize across settings.

- The passage on lines 422-425 presents an unclear and convoluted explanation of the comparison between methods, and the reported marginal improvements in R3D2’s performance relative to other settings are not fully justified within the results.

- The insights gained from the results presented in Figure 6 are unclear. Given that R3D2 was trained across all game environments, it is unsurprising that it performs adequately across settings. Without a clearer interpretation, the results lack novelty, as the outcomes align with the fact that R3D2 has been exposed to all environments during training.

### Questions
- Could the authors clarify their rationale for selecting Hanabi as a testbed for studying adaptability to new settings and new co-players? Specifically, in what ways does Hanabi reflect the complexities of real-world collaborative tasks, as mentioned in the introduction?

- How does the proposed approach relate to the existing literature on Unsupervised Environment Design, particularly for multi-agent reinforcement learning? Were there considerations given to this body of work in framing the method, and if so, how does the R3D2 approach build on or diverge from these methods?

- How scalable is the R3D2 approach with respect to increasing the number of players? Given that the current implementation handles a maximum of five players, are there foreseeable limitations if applied to environments with a larger number of agents?

- On line 205, it is mentioned that the text representation “includes the knowledge of the player’s own hand.” Could the authors clarify if this refers to the player’s hand as revealed by others through clues up to the current time point?

- Are the baseline algorithms (such as OP and OBL) trained on the text-based version of the Hanabi environment or on the original bitstring encoding? If not on the text-based version, could the authors address how this may impact the fairness of the comparison?

- Given the different architectures and representations used for each baseline, why were all agents trained with identical hyperparameters (as noted on line 374-375)? Could the authors discuss whether hyperparameter tuning was considered for each model to ensure the most accurate and fair evaluation of baseline performance?

- The explanation for OP’s lower performance on line 410 is somewhat vague. Could the authors provide additional insights or analysis on why OP underperformed relative to R3D2, as well as a more detailed comparison between R3D2 and OBL?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a scalability study of LLMs in the context of tackling Hanabi, an imperfect information cooperative game. The techniques of theory of mind, as well as solving a smaller game robustly then scaling to larger games is used. The work is "okay" in its current state but can be improved. See detailed comments below.

### Strengths
1: LLMs and theory of mind seem to be the right platform to address the game size of Hanabi.

2: Cooperation with unknown or novel agents seems to be a strong problem that this work addresses, and very much applies to Hanabi.

3: Using robustness to tackle (2) seems to be a reasonable path forward.

4: Using LLM's to "encode" the state space of Hanabi does seem to significantly improve the ability to solve the game.

5: Using dot product to create a fixed length embedding for state-action pairs does help in going from solving small 2-player games to 5-player games, for example.

6: The validation is sufficient for the claims that are being made in the work.

### Weaknesses
I'm not opposed to accepting this work in its current state, however I wonder whether we can make the approach more straightforward to understand.

1: The key probelm we're solving is: Hanabi is an imperfect information game where the information is held by other players. This is the unique challenge of Hanabi.

2: Whether you're looking at Information Sets or some sort of statistical model in order to turn partial information games into perfect information games, the standard approach remains the same: reduce the imperfect information game to a perfect information game in some way, then solve it using traditional approaches.

3: If you look at the historical progression of solving games, it often seems to be about scalability. See for example Deep Blue being a showcase of tree search, AlphaGo about the success of using CNNs to understand the game state, then using a combination of techniques (including MCTS) to solve it.

4: So again, it seems that the key theoretical insight here is: how to reduce an imperfect information game into a perfect information game through Theory of Mind.

5: The key shortcoming here is I'm not really sure what Theory of Mind is, nor are many people familiar with the "inherent" properties of languages which are undisputed. 

6: Given (5), it's difficult for me to view this paper as something much more than a scalability study of LLMs.

A more alternative presentation of the work would be, communication is used to reduce imperfect information to perfect information.

### Questions
1: Can the authors modify their presentation somewhat to make their approach more clear? See above.

2: In particular can a better presentation be provided regarding the role of language and Theory of Mind for making the imperfect information portion of Hanabi into perfect information portion.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focus on Hanabi benchmark, and devises a MARL algorithm which combines deep recurrent relevance Q-network and language models to build Hanabi agent. The proposed algorithm can deal with resulting dynamic observation and action spaces based on the text-based encoding, and thus can play all game settings on Hanabi. Finally, the experiments ranging from 2-player to the 5-player are performed to validate the effectiveness of the proposed algorithm.

### Strengths
1. The idea of incorporating all game setting together during trainging is interesting, as many current MARL algorithms need to retrain the policy network when the game setting changes.
2. The writting is clearly, and the structure is well organized.

### Weaknesses
1. This paper only focuses on the Hanabi game. Whether the proposed algorithm can be scaled to other domains or environments is a critical question.
2. The claimed first contribution of "framing Hanabi as a text-based game" appears weak. Previous work [1] has already devised text-based observations and actions for the Hanabi game. Additionally, the authors need to include comparative experiments.
3. The explanation of how R3D2 can support environments with varying numbers of players is insufficient. The paper does not clearly articulate how the dynamic recurrent network handles the changing input and output dimensions associated with different player counts.
4. The open-source code will help other researchers reproduce and build upon this work.

### Questions
1. The authors state that they utilize GPT-4 and LLama-2 to develop action strategies and claim that the results "struggle with optimal planning" in Section 5. However, I could not find any related experimental results shown in the paper, including the appendices.
2. When introducing the results about fine-tuning LLama-7B, the authors only conduct experiments on different data sizes and LoRA rank settings, without comparing the results to their proposed method. Therefore, how was the conclusion that "the model performs poorly" derived?
3. The purpose of Section 5 is unclear. If the authors want to justify choosing BERT instead of other language models, they should replace the BERT structure with other LMs in their approach and show the experimental results in an ablation study, rather than listing results that only depend on LMs.
4. I do not believe the advantage of generalizing all game settings comes from the dynamic network structure. Rather, it appears to stem from language models' ability to describe different environmental information and encode it without dependence on environment-specific characteristics, correct?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method based on language model agent for the multi-agent Hanabi game. The motivation lies in transforming Hanabi to a text-based game. The key idea lies in using BERT to provide embeddings of the text information in the game, and to be jointly trained with the policy model using Q-learning. The major target of the proposed method is to obtain a policy which can generalized to various game settings with different number of players and strategies.

### Strengths
1. The paper is well-motivated for building a general multi-agent game play agent. I agree that the generalization issue is a fundamental one in reinforcement learning. 

2. The design of conducting cross-strategy and cross-setting experimental results is interesting to me.

### Weaknesses
1. Even though the proposed method is armed with language models, its performance seems not desirable. From Fig. 5 and Fig. 6, its performance does not outperform classical methods IQL and the more recent one OP. This remains in doubt about its effectiveness.

2. Even though the paper pursues a meaningful goal, the final results provide limited insights. From Fig. 5 and Fig. 6, they show that IQL and OP have better generalization ability than the proposed method. This shows that the proposed method does not provide a sound solution to the generalization problem.

3. In my view, the major promising characters for language models to perform in game playing are knowledge providers and reasoners. While in the proposed method, the language model only plays the role of modeling the text embeddings. This usage is somehow not quite novel and effective.

### Questions
- How to explain the phenomena in Point 1 and 2 mentioned in the weaknesses?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 8

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a new LLM based MARL algorithm, R3D2, capable of playing Hanabi and generalize to a changing number of players by using a text observation. R3D2 is also capable of generalizing to cooperation with unseen players, similar to previous work on Hanabi.

### Strengths
The paper tackles a complicated MARL problem, where generalization is hard due to the strong reliance on collaboration to achieve high scores. The authors propose a novel algorithm that utilizes the generalization capabilities of language models to boost agent generalization. Using text input allows agents to generalize to different rules (more/less players), a notorious challenge in RL in general. The new algorithm seems on par with previous works on Hanabi when generalizing to new players.

### Weaknesses
The paper's main issue is the clarity of its claims and comparison to prior literature.

The paper is a bit unclear on the contribution of the algorithm presented, R3D2. Since prior works have already achieved Zero Shot Coordination (ZSC) between training seeds and between AI and human players, it seems like the only novelty in R3D2 is the ability to generalize to new rules, specifically changing the number of players. However, the results on generalizing to novel settings are only briefly discussed at the end of the paper in Section 6.2, and in general are presented more as a minor perk of the model. 

Reading the Conclusions section gives the impression that the R3D2 is the first algorithm to achieve a high intra- and inter-algorithmic cross-play score, which it is not.
The authors claim "R3D2’s intra-algorithmic cross-play score is on par with its self-play score, a first for Hanabi agents learning through self-play". While this may be true for self-play agents, the OBL algorithm also achieves equivalent cross- and self-play scores (that are higher than R3D2's scores).

In contrast, the abstract does a good job of clarifying what the paper's novelty is.

In general, the paper should be more clear about what R3D2 does not achieve, e.g. SOTA in inter-algorithm play, rather than give the impression that R3D2's main contribution is SOTA performance.

### Questions
Minor typo comments:
- Some citations should be in parentheses (using \citep{}), for example in section 3.2.
- Sections 6.2, 6.3 have a typo in the title (shot --> short)

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 9

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work focus on the challenging card game Hanabi and try to solve the current  bottleneck of transferring of learned policy to different settings. Language representation is selected for adapting policies among these settings. A successful zero-shot coordination architecture for MARL has been proposed and achieved sota scores on the Hanabi game, which is among the early solutions for such settings.

### Strengths
This work is a worthwhile trial to use language modelling to solve the MARL transfer ability issue, which is inspiring. In experiments it also applies to some newly proposed LLM models which shows steady improvement.

### Weaknesses
1. More up-to-date models like LLAMA 3 or GPT-4o is also encouraged to ensure the experiments are more solid.
2. Is it possible to transfer the learned policy to a different task? How about comparing the proposed approach to existing schemes like curriculum learning or multi-task MARL? Related work should also include such literature.
3. Quantitative results are given in the paper, it is better to include more qualitative demos which show how the language representation helped in transferring.

### Questions
Please refer to the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 10

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors focus on playing the game of Hanabi with multi-agent reinforcement learning. They consider the shortcomings of existing MARL systems: unable to perform well on any other setting than the one they have been trained on, and struggle to successfully cooperate with unfamiliar collaborators, which is particularly visible in the Hanabi benchmark. To solve this, they introduce a generalist agent for Hanabi. The reformulate the task using text and then propose a distributed MARL algorithm that copes with the dynamic observation- and action-space. By doing so, they train an agent that can play all game settings concurrently, and can extend strategies learned from one setting to other ones. Also, there agent demonstrates the ability to collaborate with different algorithmic agents.

### Strengths
1. The authors analyze the widespread problems of common MARL algorithms and select Hanabi, a typical scenario reflecting the common problem, for improvement and research.
2. The authors template the observation and action of the Hanabi game into natural language and use the pre-trained LM as the representation head in the RL value network. They try various pre-trained LMs and finetuning techniques to compare the performance.
3. The authors conduct extensive experiments to demonstrate the zero-shot capability of their proposed method on 2-player coordination and policy transfer over different settings.

### Weaknesses
1. The general motivation of this work, if I don't understand wrong, stands on the opinion of 'language has been shown to improve transfer'. Therefore, the authors propose to template the observation and action of the Hanabi game into natural language and process them with pre-trained LM. But why this opinion holds? It will be more convincing to provide experimental results to show this. For example, how will the performance change if substituting the natural language inputs and pre-trained LM with vector inputs and normal neural networks? Or at least, the authors should provide more sound literature to support this opinion.
2. The relationship among the three evaluation metrics, i.e. SP, Intra-XP, Inter-XP, is confusing. The authors claim in Figure 4 that R3D2 achieves significantly better inter-XP compared to the baselines while maintaining a competitive SP and intra-XP. However, the figure indicates significant drop on SP, which is even more significant that the improvement on inter-XP. How should I comprehensively understand these three metrics to determine which method performs best?
3. This paper focuses on the Hanabi game and conducts an in-depth study, but it is still unclear whether the proposed method can inspire the improvement of MARL algorithms on other different tasks.
4. The experimental details provided in this paper are limited, making it difficult for readers to directly reproduce the results. It would be great if the authors can make the code open-sourced at an appropriate time and provide more details on the experimental setups.

### Questions
1. Why is the opinion of 'language has been shown to improve transfer' is valid? Can you provide experimental results to support this claim? For example, how would the performance change if natural language inputs and pre-trained language models were replaced with vector inputs and standard neural networks? Alternatively, could you provide more solid literature to support this idea?
2. What is the relationship among the evaluation metrics SP, Intra-XP, and Inter-XP? Figure 4 shows that R3D2 achieves significantly better Inter-XP compared to the baselines, but the SP metric shows a significant drop, even larger than the improvement in Inter-XP. How should these three metrics be interpreted comprehensively to determine which method performs best?
3. This paper focuses on the Hanabi game. Could you discuss whether the proposed method can inspire improvements in MARL algorithms for other tasks?
4. Could you make the code open-source at an appropriate time and provide more detailed information on the experimental setups to help others reproduce the results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 11

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper aims to train a generalist Hanabi agent that can:
1) Play variants of Hinabi with different number of co-players 
2) Play with novel co-players

To this end the authors contributions are:
1) A text based version of hinabi environment - which makes learning across multuple variants easier
2) A novel-ish algorithm R3D2, which is a recurrent network with a value function generated from a text embedding.

### Strengths
The problem is original - multi-task / multi-agent problems have not been tried since the XL land paper or Maestro (both citations which are missing in this work). Although this does truly feel like the limit of how much as a community we can care about hinabi. 

I’m a massive fan of the evaluation protocol in this paper - its really nice to see cooperative marl analysis on cross-play and the introduction of intra-xp and inter-xp is a huge improvement. 

The paper is well written and to a high quality.

### Weaknesses
The choice of baselines is really confusing to me, and makes it hard to understand the authors contribution. All baselines presented are trained and evaluated in the existing hinabi environment (the non-text based encoding). This makes it hard to disentangle the importance of the R2D2 style training, the RRN modification or the language based component underneath.  To my understanding, the method isn’t really novel - this is just R2D2 but they used the text embedding for both goals and actions - which is just a trick from the Continuous Control Literature and augmented the Recurrent network to be a recurrent relevant network. Also using a text based version of Hinabi is obvious in 2024, so i don’t see this as a significant contribution. Ablations would be appreciated to understand where the juice is actually coming from. I’d also like to just know if OBL agents in the language based environment generalize better.

The results lack qualitative analysis and as such, its really hard to understand whats happening here or the significance of the work, Is the hope that the method has learnt via a larger set of environments / tasks to have more robust policies.  If so what do these policies look like? Do they share underlying similar structures or methods. Could we also evaluate methods on OOD tasks (e.g 7 players hinabi or something not in the train?).
Its hard to interpret the results in Figure 6 - yes it seems R3D2 is robust to co-players changing but because i don’t have an equivalent evaluation with a team of IQL agents or OBL agents its very hard to evaluate if this is comparatively better.

The paper would be vastly improved if consistent LLMs were used throughout the section. LLMs have quirks, different training data and different methods. It feels hard to compare results in Section 5 with any proposed in Section 6 because the underlying models are very different. I also think that the experiments in Section 5 tell us more about those models (which are rather small number of parameters) and the difficulty of supervised learning here. The conclusions drawn are overreaching.

### Questions
1) “it successfully avoids getting bombed for extended periods, “ <- is this a common term in hinabi?

2) The Appendix is missing.

3) The Inter-XP metric is calculated with which other co-player? Figure 4.

4) Could analysis be provided of the compute costs / sample efficiency and limitations of each method? Its really hard to work out why this method is working at all, is this just better domain randomisation, is there some particular underlying set of hinabi skills that generalise well over n players.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 12

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper learns a generalist agent that is able to play any-card variants of Hanabi by casting the game to a text based game and utilize model architectures from language modeling to learn such policy with Q-learning

### Strengths
1. The idea of casting Hanabi as a text game for the purpose of learning a generalist agent is interesting. Language as a common interface for variants of games, or completely different games, is interesting, especially when the game primarily requires reasoning, which is the case in Hanabi.

2. If I understand correctly, the R3D2 agent is able to learn consistent policies, i.e. achieving high intra-AXP score and small gap between intra-AXP and self-play, without any additional assumptions that prior methods use. This is a cool result and probably the benefit of using language as observation and action? Although I am not sure exactly why this model is able to do that. See my question below.

### Weaknesses
1. Although this paper does a good job showing that we can train a single generalist agent for any-player Hanabi, which is an interesting contribution, one downside is that the paper is not able to have convincing results of the benefit of having a “generalist” agent, i.e. the benefit of going from R3D2-S to R3D2-M. Apart from the fact that the generalist agent does better in Figure 6, which it should because the single-variant agents are not trained on other variants of Hanabi, I only found this single comment on the benefit of R3D2-M:
> Interestingly, R3D2-M learns decent strategies for all settings, despite receiving the same training budget as single-setting algorithms. This shows that knowledge from one setting is useful for other ones, and that the textual representation allows for effective transfer of kenowledge across settings.

However, I don’t find this to be convincing. If the generalist agent is given the same amount of data as the sum of the 4 single-variant agents, will it outperform the single agents? I think this is crucial for making such a claim and I do believe that would make this paper stronger to the general audience beyond MARL.


2. The high inter-AXP results are not super exciting because:
* IQL is known to produce strange conventions that is hard to coordinate with;
* OP has significantly higher inter-AXP score with IQL than any other methods, indicating that the reproduced OP is probably as brittle as the IQL agents, which is totally possible as some OP implementation uses tricks such as hiding the last action from the observation to regularize more;
* OBL coordinates badly with the OP agents, indicating that they are very different;

With the arguments above, a high inter-AXP score here would just translate to better coordination with  IQL/OP than OBL, which is a useful result but not necessarily an important result because eventually we want policies that coordinates better with human-like policies (OBL) rather than inhuman policies (IQL). Having a human study as in [1], a paper in a comparable conference (ICML) on Hanabi that this paper cited, would greatly address this.

### Questions
1. 
What are the agents on the x-axis of Figure 6? Are they R3D2-k agents trained for each game variant? If so, why is the diagonal not the same as R3D2-SP? The notation and explanation around this figure could be improved. For example, you are using XP to refer to cross-play everywhere else, but use CP here, which could be a bit confusing.

2. 
> In contrast, in our textual representation, symmetrical observations are the same but for a few tokens. Symmetries are thus implicitly tackled by R3D2.

Why is this the case? For example, considering two hands R1, R2, B5, B3, G4 and B1, B2, R5, R3, Y4 (R, G, B, Y for different colors), these two hands are symmetrical up to a color permutation used in OP, but they are more than a few tokens apart in the language description. The color permutation will also apply on other parts of the observations such as the firework pile so I would expect the language observation to be quite different? Am I missing something? If I did not miss something, I would be curious why the policy does not learn to use arbitrary color coding as a play strategy.

### Soundness
2

### Presentation
3

### Contribution
2
