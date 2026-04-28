# Attaining Human's Desirable Outcomes in Indirect Human-AI Interaction via Multi-Agent Influence Diagrams

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
In human-AI interaction, one of the cutting-edge research questions is how AI agents can assist a human to attain their desirable outcomes. Most related work investigated the paradigm where a human is required to physically interact with AI agents, which we call direct human-AI interaction. However, this paradigm would be inapplicable when the scenarios are hazardous to humans, such as mine rescue and recovery. To alleviate this shortcoming, we consider indirect human-AI interaction in this paper. More detailed, a human would rely on some AI agents which we call AI proxies to interact with other AI agents, to attain the human's desirable outcomes. We model this interactive process as multi-agent influence diagrams (MAIDs), an augmentation of Bayesian networks to describe games, with Nash equilibrium (NE) as a solution. Nonetheless, in a MAID there may exist multiple NEs, and only one NE is associated with a human's desirable outcomes. To reach this optimal NE, we propose pre-strategy intervention which is an action to provide AI proxies with more information to make decision towards a human's desirable outcomes. Furthermore, we demonstrate that a team reward Markov game can be rendered as a MAID. This connection not only interprets the successes and failures of prevailing multi-agent reinforcement learning (MARL) paradigms, but also underpins the implementation of pre-strategy intervention in MARL. In practice, we incorporate pre-strategy intervention into MARL for the team reward Markov game to model the scenarios where all agents are required to achieve a common goal, with partial agents working as AI proxies to attain a human's desirable outcomes. During training, these AI proxies receive an additional reward encoding the human's desirable outcomes, and its feasibility is justified in theory. We evaluate the resulting algorithm ProxyAgent in benchmark MARL environments for teamwork, with additional goals as a human's desirable outcomes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on a problem scenario where humans interact with other AI agents via AI proxies. In this multi-agent environment with some specified group goal, the proxies are able to take into account human preferences via "pre-strategy intervention"

### Strengths
The motivation of intervening on multi-agent games through AI proxies is quite interesting because it allows us to see a mathematical strategy for interpolating between centralized and "independent" learning through the lens of intervening via proxies. Results are promising on a set of JaxMARL benchmarks.

### Weaknesses
The environments used for evaluation involve discrete actions. The formula to evaluate a pre-policy involves a summation over strategy profiles. How do you expect the results to scale up to more complex environments with continuous state and action spaces, including more complex observation spaces? Specifically, the summation over all strategy profiles becomes computationally intractable as the number of agents and action spaces grow. The paper does not address how the proposed method would handle the curse of dimensionality in these more complex settings. There also isn't as much comparison of the paper's results to related works in inverse RL for multi-agent cooperation in the experiments section, although the ablations are helpful for understanding the author's strategy in developing their approach. The lack of comparison to inverse RL methods is a significant gap, as these methods also aim to infer agent preferences and could provide a strong baseline for comparison. The paper also does not discuss how the pre-strategy intervention would handle situations where human preferences are not consistent or change over time, which is a common challenge in real-world human-AI interaction scenarios.

### Questions
Though cited in the main paper, I think it would be nice for the paper's presentation to put a motivating example of how MAIDs work in the main paper, rather than just the appendix. The paper could also benefit from a more extensive results discussion. I understand there is a lot of background to be laid out about causal models, etc., but I think these additions would actually help motivate and enhance readers' understanding of the work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an innovative indirect human-AI interaction paradigm where humans do not directly engage with AI agents. Within this framework, the authors propose the concept of AI proxies that interact with other AI agents to achieve alignment with human-desired outcomes. The interactive processes are modeled using multi-agent influence diagrams, and the authors propose a pre-strategy intervention approach to achieve optimal Nash equilibrium in the game-theoretic setting. The effectiveness of this pre-strategy intervention is demonstrated through its integration into Multi-Agent Reinforcement Learning (MARL) and subsequent evaluation in two established MARL environments.

### Strengths
1. This paper studies an interest paradigm, i.e., the indirect human-AI interaction, which is common in the real world, such as remote surgery and mine rescue. 
2. The paper demonstrates a well-structured and well-articulated presentation.
3. The introduction of experiment is complete and easy to follow.

### Weaknesses
1. The introduction of indirect human-AI interaction is not enough. From the Figure 1 (a)-(c), it cannot recognized which agents represent human, which represent the AI proxies, which represent the AI agents.
2. The author gives a proof about the existence of nash equilibrium in their game. However, they doesn't prove their proposed method, i.e., pre-strategy intervention based method can be ensured to converge to optimal nash equilibrium.
3. The selection of baseline in experiments are not proper. I suggest the authors choose some MARL algorithms, such as MAPPO and QMIX.

### Questions
1. Whether the introduction of AI proxies is rational? Whether AI proxies can also be regarded as AI agents? If yes, the definition of indirect interaction is not true.
2. Why the authors introduce LLM alignments in the related work. It seems that this research doesn't relevant to LLM alignment. 
3. Whether the comprison experiments can be performed when pre-strategy intervention is not introduced into the approach.

### Soundness
3

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
This paper studies a human-ai collaboration where the human interacts with other AI agents through an AI proxy. They model the indirect, interactive process among AI proxy and other agents using a multi-agent influence diagram and propose a pre-strategy intervention to select a human-desired NE. They use causal effects to optimize and measure the pre-strategy intervention in MARL. They study the MAID view of team reward in independent learning and centralized learning scenarios and evaluate proxy agents in MPE and StarCraft challenges to find (1) the proposed method converges faster than baselines and (2) human desirable outcomes that could affect the extrinsic rewards.

### Strengths
In general, it is a strong and well-written paper studying selecting the human-preferred Nash equilibrium and studying whether the algorithm works.

### Weaknesses
While the story and theory of the paper are interesting, they are less attractive in terms of method and experiments.

(1) In method/algorithm 1, I could barely get information besides the alternate training of pi_pre using intrinsic rewards and pi_agent with extrinsic rewards

(2) In experiment session, I would also demonstrate the method some games where the diverse NE(conventions) are easy to tell and has abundant prior work because nothing prevents the methods to be applied to the general-sum setting.

(3) Possibly missing literature on multi-agent diversity. I believe the diverse convention finding literature is relevant because you can find them in the first place and select among NEs. Here is a few examples [1][2][3]

### Questions
(1) This paper reminds me of [1]. Can the authors elaborate on how language conditioning and pre-strategy are related to each other?

[1] Hu H, Sadigh D. Language instructed reinforcement learning for human-ai coordination[C]//International Conference on Machine Learning. PMLR, 2023: 13584-13598.

(2) How do you get the intrinsic rewards? How do humans specify their preferences?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers an _indirect_ human AI coordination problem where the humans influence a group AI agents by setting pre-strategy for certain specific agent or agents. It formulates the problem via multi-agent influence diagrams (MAIDs) and establish connections between MAIDs and MARL.

Disclaimer: I have to admit that I am not able to fully understand the theoretical aspect of this paper, so please take my opinion with a grain of salt.

### Strengths
* The problem setting, indirect human-AI coordination, seems novel. The paper establishes connections between this setting with MAIDs and makes some theoretical contributions.
* The connections can be used to provide alternative views for some common MARL challenges, such as the non-stationary issue of independent Q learning (IQL).

### Weaknesses
The problem setting of indirect human AI coordination is insufficiently motivated. It seems that the main problem it addresses is to make sure that the learned equilibrium align well with human intention. Such problems have been studied in the literature in much more complicated settings. For example, the Cicero agent for Diplomacy[1] is trained to converge to human-like equilibrium with QRE-inspired regret matching procedure  so that it can influence other players in a human-desired way. Hu & Sadigh [2] uses natural language to construct prior for one or multiple agents, which can also be seen as some form of shaped reward, so that they behave in a human-desired way when coordinating with other agents or other humans. I am not sure if this work is fundamentally different from those “equilibrium selection” work. In the experimental results, it seems that the paper is doing similar things, such as using extra reward shaping for certain agent so that the group exhibits certain collective behavior.

I think the paper could do a better job if it can
* Make a stronger motivation for indirection human AI coordination
* Clearly contrast it with existing works and emphasize on the unique advantages that prior work cannot achieve.

The related work section on LLM alignment seems less relevant for this paper as the author makes no comparison or application into the LLM land. On the contrary, it seems to miss some of the potentially related work mentioned above. However, it could also be that I missed the main point of the paper.

### Questions
* Figure3: “Figure 3 shown that our method demonstrates general faster convergence compared with the baseline.” In Figure 3.a the GNN curve looks indistinguishable from the baseline curve, and in Figure 3.b and yellow baseline curve seems to converge faster. How do you reach the conclusion? 

* MPE experiments: “the greater the distance the larger intrinsic rewards” -> Shouldn’t this drive the red dot further from the leftmost landmark? In Figure 4.a it seems that the red dot is moving closer to the leftmost landmark?

* Instead of using the two staged approach, how would the proposed method compare to a baseline that jointly optimize all agents while the proxy agent receives the intrinsic reward?

### Soundness
2

### Presentation
2

### Contribution
2
