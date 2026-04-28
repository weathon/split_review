# From Child's Play to AI: Insights into Automated Causal Curriculum Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 5, 3, 3, 3

## Abstract
We study how reinforcement learning algorithms and children develop their causal curriculum to achieve a challenging goal that is not solvable at first. Adopting the Procgen environments that comprise various tasks as challenging goals, we found that 5- to 7-year-old children actively used their current level progress to determine their next step in the curriculum and made improvements to solving the goal during this process. To evaluate RL agents, we exposed them to the same demanding Procgen environments as children and employed several curriculum learning methodologies. Our results demonstrate that RL agents that emulate children by incorporating level progress as an intrinsic reward signal exhibit greater stability and are more likely to converge during training, compared to RL agents solely reliant on extrinsic reward signals for game-solving. Curriculum learning may also offer a significant reduction in the number of frames needed to solve a target environment. Taken together, our human-inspired findings suggest a potential path forward for addressing catastrophic forgetting or domain shift during curriculum learning in RL agents.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies intrinsic learning in children and how they use ‘level progress’ information to modulate their understanding of goals and make progression towards task goals. This automated curriculum selection in children isn’t random (as shown with experiments) and helps them learn. Authors use the same principle to design RL agents to solve simple game playing tasks with varying levels and design hand-crafted curriculum and conduct experiments to understand how RL agents learn in the absence of extrinsic rewards and whether they are able to recover from failures. The baseline they develop isn’t able to achieve goals as difficulty levels increase. “Although for simpler environments it may be possible to recover, as the complexity is smaller and random actions may find the goal, for harder environments with multiple lanes, this divergence is unrecoverable.” From Fig 5b, Before training divergence (which happens with increasing levels of difficulty and catastrophic forgetting), the exact relationship of reward and level progress depends on the task complexity. The easiest task (1 water lane, dark blue) has the greatest slope, since changes in level progress yield relatively greater mean training reward. However, this pattern does not transfer as the complexity increases. With inspiration from how children use the level progress as a proxy for reward signal, authors conduct experiments using the similar level progress information as intrinsic reward signal. RL agents learn much better and can recover from catastrophic forgetting when using this intrinsic progress as a reward signal after every episode. Intrinsic rewards decrease as levels progress however they do not collapse and can increase (recover) in certain circumstances. Authors suggest understanding how to integrate these intrinsic level progression into RL agents from the world states (eg. From high dimensional images) will be crucial towards the path for more general learning agents.

### Strengths
- Design the complex experiments to understand how small children learn using simple games that contain difficulty levels and drawing inferences on what signals children utilize as intrinsic signal for achieving goals is a very good contribution of this study. Many ideas in the paper seem intuitive; however, these scientific experiments and evaluation to generate various hypothesis is commendable. 
-  The paper is equally divided into a user study of children to understand how they use automated curriculum learning to solve tasks and then explore how RL agents can learn on same tasks using similar automated learning strategies. Authors show promising results and future directions of the work to highlight where the field should focus to utilize automated curriculum learning with RL agents and how to design these intrinsic rewards.

### Weaknesses
 - Although very inspirational work, there are many questions around the user study that is not clear. How reliable are children responses? How was this controlled for and simplified so children could understand and respond appropriately?
- Asking 5 year olds multiple choice questions pertaining to the true causal rules of games needs more supportive evidence.
- These are small experiments - Children’s selection of an easier level after failing a level is spread over different levels (including 1/7 choosing a more difficult level). 42.1% of failed levels led to choosing an easier level, 37.4% of failed levels led to choosing the same level. - how reliable is this and it is not clear how the authors are utilizing any of this fine-grained signals in the intrinsic reward design process for RL agents.

### Questions
(please address the points under weakness section)
- RL experiments are done with only Leaper game. Are the results similar on other games?

Minor comments:
- Table 2 missing
- Section 3, 5th line - unclear - “we heightened the difficulty by increasing the number of platforms” - what’s a platform here?
- Fig 3 references fig 9 and fig 10 in appendix (not present)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study curriculum learning in reinforcement learning by conducting human experiments on complex sequential tasks. They discover that children successfully solve the final complex tasks by taking the correct curriculum arrangement according to the task progress. Motivated by this, the authors design a reinforcement learning experiment to verify this finding by setting progress level as an intrinsic reward. The experimental results indicate that the progress level intrinsic reward improves the curriculum learning performance.

### Strengths
1.	The authors conduct an interesting and informative human experiment.

2.	The paper is well-organized.

### Weaknesses
1.  I’m sorry that I’m not very familiar with the human experiments in cog-science. But I worry that the number of children (only 22 children) in this study is too small. How do you guarantee that the results obtained from such a small group of children is unbiased and trustable? Maybe please point us to some related works that also conducted human experiments and claimed that such a small experimental population would be enough.

2.  Another concern is about novelty. I admire the motivation from human experiments. However, utilizing task progress is not a novel idea in reinforcement learning [1], so I worry that the proposed method is more like a trick.

3.  There are many previous works taking advantage of various heuristics to design curriculars. I think it is necessary to compare your method with them. Would you please show us some comparison results with existing techniques?

### Questions
1.	I’m sorry that I’m not very familiar with the human experiments in cog-science. But I worry that the number of children (only 22 children) in this study is too small. How do you guarantee that the results obtained from such a small group of children is unbiased and trustable? Maybe please point us to some related works that also conducted human experiments and claimed that such a small experimental population would be enough.

2.	Another concern is about novelty. I admire the motivation from human experiments. However, utilizing task progress is not a novel idea in reinforcement learning [1], so I worry that the proposed method is more like a trick.

3.	There are many previous works taking advantage of various heuristics to design curriculars. I think it is necessary to compare your method with them. Would you please show us some comparison results with existing techniques?

[1] Bruce J, Anand A, Mazoure B, et al. Learning about progress from experts

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Based on the observation that children use their current level progress to determine the next level in their curriculum, this study proposes a curriculum approach for reinforcement learning agents. Using level progress as an intrinsic reward signal, similar to the way children do, the study argues for improved data efficiency and convergence in reinforcement learning agents.

### Strengths
- This study draws inspiration from observing real 5-7-year-old children, making it interesting as a human-inspired finding.
- The intrinsic reward method proposed in this study reduces catastrophic forgetting and improves convergence.

### Weaknesses
 - The analysis of the behavior of 5-7-year-old children is intriguing, but the transition to rl-agent experiments is somewhat lacking. The study claims to use an intrinsic reward, but it seems to be primarily based on "how far the agent is into the task." This raises questions about whether this intrinsic reward function has more significant implications than the distinction between "sparse reward" and "dense reward" typically used in the general RL community. Specifically, the formulation of the intrinsic reward as (2* lambda / 100) lacks a clear connection to established reward shaping techniques or intrinsic motivation frameworks in the literature. A more rigorous definition and theoretical grounding of this reward would strengthen the paper's contribution.
- The explanation of the experimental results is somewhat vague. For instance, the paper states that the proposed method reduces catastrophic forgetting and improves convergence, but it does not provide a detailed analysis of why this occurs. Further, the experimental environment appears to be limited. The study only evaluates the proposed approach on a single environment, which raises concerns about the generalizability of the findings.
- If the way 5-7-year-old children change their levels does not apply to RL agents, it suggests that the study has not fully integrated the observations from children's behavior into RL agents. The paper mentions that children use level progress as an intrinsic reward signal, but it is unclear how this translates to the agent's level transitions in experiments 5.3 and 5.4. The agent seems to simply move to the next level when the average extrinsic reward exceeds 9, which does not necessarily reflect the nuanced level-changing behavior observed in children.
- There is no comparison with baselines or prior work. This makes it difficult to assess the significance of the proposed approach relative to existing methods for curriculum learning or intrinsic motivation in reinforcement learning.

### Questions
- In both Experiment 5.3 and 5.4, does the agent move to the next level when it achieve an average reward of 9 means (as explained in section 5.2)?
- Did the proposed method in 5.4 incorporate the way 5-7-year-old children change their levels?
- While it's mentioned that 5-7-year-old children use level progress as an intrinsic reward signal to decide which level to play to solve the most challenging level, does the proposed method in section 5.4 actually use this intrinsic reward function (2* lambda / 100) for transitioning between levels? (i.e. do they use it when they determine whether they change their level or not?, or just determine the level transition based on if(mean episode reward>9)? )
- How many seeds were used to obtain the experimental results?

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper first exams the learning strategies of children in tackling challenging tasks. The study used Procgen environments with various difficulty levels to investigate how 5 to 7 years old children adapt to these challenges. The findings reveal that children use their progress through the levels as an intrinsic reward, motivating them to excel at easier levels before tackling harder ones. 

Then this paper shows that RL agents that follow a similar approach, incorporating level progress as an intrinsic reward, show better stability and convergence during training than agents relying solely on extrinsic rewards. Curriculum designed in this way also boost the sample efficiency.

### Strengths
(1) The analysis on children playing Procgen games are enlightening and thorough.  
(2) The idea of adopting the behavioral findings from human studies to solve ProcGen is inspiring.

### Weaknesses
(1) The paper fails to provide a rigorous definition of "level progress." This ambiguity undermines the subsequent discussions and analyses that rely on this concept. Without a clear, quantifiable definition, it is difficult to assess the validity and reproducibility of the proposed method. For instance, the paper mentions that level progress is used as an intrinsic reward, but how is this reward calculated? Is it a linear function of progress, or does it involve more complex calculations? Does it vary across different environments, and if so, how is it normalized? These questions are crucial for understanding the core mechanism of the proposed approach. The lack of clarity raises concerns about the generalizability and applicability of the method to other environments or tasks. 
(2) The claim that level progress is inaccessible and not generalizable is a significant concern. The paper suggests that level progress is a measure of how far the agent has gone in a level. However, it does not specify how this information can be accessed or represented in a way that is consistent across different environments. If level progress is environment-specific, as implied, then the proposed method lacks generality and cannot be readily applied to new tasks or domains. Furthermore, if level progress is simply a denser supervision signal, as the reviewer suspects, then the novelty of the approach is questionable. It essentially reduces to providing more frequent rewards, which is a well-established technique in reinforcement learning. The paper needs to address these issues and demonstrate that level progress offers a unique and valuable contribution beyond existing methods. 
(3) The experimental evaluation is insufficient to support the claims of the paper. Presenting only single runs without multiple random seeds raises concerns about the statistical significance of the results. It is possible that the observed performance is due to chance rather than the effectiveness of the proposed method. To establish the robustness of the findings, the authors should conduct experiments with multiple random seeds and report the mean and standard deviation of the performance metrics. This will provide a more reliable estimate of the true performance and allow for a more meaningful comparison with baseline methods. Additionally, the paper should investigate the sensitivity of the proposed method to different hyperparameters and network architectures. This will help to determine whether the observed catastrophic forgetting is inherent to the method or simply a result of suboptimal parameter settings.

### Questions
Questions are related to the weaknesses section.   
(1) What is the formal definition of level progress?  
(2) How do you plan to access the level progress you defined?  
(3) Could you do a parameter search and change the network structure with multiple random seeds to see if it's poor training causing the catastrophic forgetting? In another word, is it really because the sparse reward signals?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies human and RL curriculum learning in a set of procedurally generated games.

### Strengths
Parallel studies of human and machine learning is a very exciting line of work that will help make progress in both disciplines. I think the paper is well motivated and clearly written.

### Weaknesses
Level progress is a confusing term for curriculum learning researchers. “Learning progress” or “competence progress” is a standard proposition of intrinsic motivation to guide curricula, it refers to the derivative of the competence measure with respect to time: how much the competence increases or decreases. Here you use the term “progress” but it refers to what people call “competence,” a measure of success, a score. For instance, if you play the same level 10 times and reach the same score each time, there is no progress at all across-episodes, the progress is only intra-episode. I know that level progress describes what you expect it to describe in the language of video games, but it’s confusing for researchers in this field: I thought you meant learning progress for the first 4-5 pages. Could you consider using another term? Competence is the standard term I think, score or performance could be good as well.

The hypothesis supported here is not very clearly stated. I can see several alternative hypotheses that could explain the data:
* Children have some form of heuristic curriculum strategy that would look a bit like this: if i’m very good, i switch to a harder task, if i intermediate I stay there, if i’m bad i either stay or try something easier. 
* Children have a causal understanding of the world and maximize their causal learning
* Children have an intermediate difficulty bias (~Florensa’s paper): they keep doing the task for which they have intermediate competence / performance. 
* Children have a bias towards learning progress: they can estimate expected learning progress in a model-based way and select the task that maximizes it. When a game is solved there is no further learning progress so they switch up, when they perform poorly they might expect more progress soon and stay, or not expect progress and recalibrate their estimations, which leads them to switch down.

I feel like the paper is arguing for the second interpretation, although it’s not stated clearly. I don’t see anything in the paper that would allow us to argue for one more than the others?

An interesting experiment could be to include levels from games different from the target game level. If children optimize for learning progress only, then we should see children select easy levels of the non-target games as well. Instead, we would probably see children almost never select the irrelevant game, which argues for a combination of intrinsic (LP-like) and extrinsic (going for the target level) curriculum. 

RL experiments:
* The switch threshold appears to be an important hyperparameter, it would be interesting to see how it affects the results: .9 seems high given that children seem to switch up around 75%.
* I’m not 100% sure I understand the manual curriculum: 
* why is there 16 parallel tasks?
* what does it mean to increment the difficulty by 1/16? I thought the difficulty was the number of lanes (1–5)? if the agent passes 0.9 in the current level (eg 1 lane), I expect the 16 tasks to become 2-lane tasks and the agent to be trained on these? Here it sounds like one of the 16 tasks becomes a lane-2 task, but then how is compute the score metric now? It it computed as the average level progress over the 16 taks (15 1-lane and 1 2-lane)?
* You use an on-policy algorithm that does not leverage a replay buffer. This means that old data from easier levels are thrown away. Using an off-policy algorithm (eg DDPG) would reuse past data, which may mitigate the catastrophic forgetting problem?

Catastrophic forgetting for curriculum learning is a known problem, which is why all curriculum approaches perform stochastic selection: they do not switch from one level to the other but sample all levels with varying probabilities that are a function of the intrinsic motivation. Eg selecting the current best level with probability .7 and the rest with .3 / n_other_levels may fix the issue, see Jiang’s paper and Colas 2019 for examples.

Studies of curriculum algorithms always include the presentation of the random baseline selecting level uniformly. This baseline does not suffer from distribution shifts. 

I’m not sure how the intrinsic reward is used here. As far as I understand, it seems that the curriculum (level selection) is the same as before but that PPO now uses what the so-called intrinsic reward in addition, right?
If so, this is a problem. Intrinsic motivations must be agnostic of the goal (this is what intrinsic means). They can be either state-based: assigning an intrinsic reward to states; or goal-based: assigning an intrinsic reward to goals / tasks.
What you propose is to assign a reward to a state, but this reward is extrinsic, it measures performance in the task. Practically, you’ve just replaced a sparse reward with a dense reward, no intrinsic motivation here.
What curriculum people do in that situation usually is to use that competence measure to guide the level-selection (goal-based reward): the level selected could be the one where there is the most progress (score now vs score before, not the level progress), or the one where the competence (level progress) is intermediate. These rewards are extrinsic because they are not tied to particular levels: the level-selector only cares about learning progress or intermediate difficulty, not about any level in particular. This would involve using a bandit algorithm to explore levels and maximize that score. 

The idea of a causal curriculum is interesting, but the papers cited when discussing this topic do not engage with any form of causality: eg Florensa 2018, Sukhbaatar 2017, Bengio 2009.

A good way of discussing curriculum approaches is by making explicit the distal objective of the curriculum (maximizing performance on a set of target tasks), describing the proximal objective optimized by the approach (which usually includes forms of intrinsic motivation), and discussing what is the control parameter (the part of the MDP that is varied to maximize the proximal objective), see framework from Portelas et al 2020. Proximal objectives include: novelty, intermediate difficulty, learning progress, things that can be varied include: state space, transition space, goals, rewards, etc. The current review is not very clearly structured and omits large chunks of the field (eg learning progress maximizing methods). These are probably the closest to the one proposed in this paper so they should be mentioned. In particular, this paper proposes a curriculum over tasks (variation of state space, and transition function) where the proximal objective is an intermediate difficulty (intermediate level progress). 

What I would need to update my score:
* Further details and explanations for the points raised above
* Better account of existing curriculum approaches
* Explicit statement about the hypothesis proposed here + discussion about how the result support that hypothesis, and may or may not bring sufficient evidence to separate the different hypotheses i listed above
* I may have understood it wrong, but it seems that the authors completely missed the mark on the curriculum RL implementations: missing random baseline, deterministic level sampling instead of stochastic ones that's common in the field and, more importantly, the reward used is extrinsic and not intrinsic. It should be a goal-based reward and not a state-based reward. Again I may have understood it wrong so i'm open to discussions. 

I believe that this setup is interesting and the scientific goal is good. I'm looking forward to future improved versions of this paper. 


Minor comments: 
* Vygotsky’s citation is broken (missing y, no year).

### Questions
see above

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
