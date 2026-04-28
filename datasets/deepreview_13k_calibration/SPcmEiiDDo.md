# Episodic Control-Based Adversarial Policy Learning in Two-player Competitive Games

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
Training adversarial agents to attack neural network policies has proven to be both effective and practical. However, we observe that existing methods can be further enhanced by distinguishing between states leading to win or lose and encouraging the policy training to prioritize winning states. In this paper, we address this gap by introducing an episodic control-based approach for adversarial policy training. Our method extracts the historical evaluations for states from historical experiences with an episodic memory, and then incorporating these evaluations into the rewards to improve the adversarial policy optimization. We evaluate our approach using two-player competitive games in MuJoCo simulation environments, demonstrating that our method establishes the most promising attack performance and defense difficulty against the victims among the existing adversarial policy training techniques.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper assumed that adversarial agent’s historical experiences can be used to distinguish winning states and losing states.
The paper selected episodic control as their distinguishing model.
By distinguishing winning states and losing states and adjusting rewards, the paper designed a method to improve the effectiveness of the adversarial agent. 
For adjusting rewards, the paper used the prediction of episodic control minus the recent average reward as the new reward.
The results show that it improves on some of the Mojoco two-player environments.

### Strengths
1 Using history to predict the rewards makes sense.

2 Results seem better than the baseline.

### Weaknesses
1 Using the history in robust RL is not new. With more information, it is not surprising that the results are better.
"Robust Deep Reinforcement Learning against Adversarial Perturbations on State Observations"

2 Need more justification for the design selection. For example, why not train a reward function that takes some history features as input. Or Why not use a transformer or a CNN instead of a LSTM?

3 It is well known that the agents are not robust to adversarial attacks. It is more meaningful if it is attacking a robust agent. Or maybe at least test on more agents. For example, attacking agents that also have histories as inputs.

### Questions
see weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an episodic control-based adversarial policy training approach for two-player competitive games. The authors propose a method that enhances adversarial policy training by utilizing an episodic memory to store historical evaluations of game states and modify the corresponding rewards accordingly, helping adversarial agents prioritize states that lead to winning outcomes. The technique is tested in MuJoCo simulation environments and is claimed to show superior attack performance and difficulty in defending against trained adversarial agents when compared with baseline adversarial policy training methods.

### Strengths
The proposed method appears effective within MuJoCo games and may serve as a reward-shaping technique to enhance existing approaches.

### Weaknesses
Although the proposed method achieved some empirical success at the selected Mujoco games. I do have some concerns regarding the current method.

(1) The proposed method lacks a theoretical guarantee and relies primarily on empirical results. The approach essentially applies reward adjustments by assigning intermediate rewards to specific states, which resembles a form of reward manipulation. It would be better if the author could give some bounds analysis regarding their propose method.

(2) Clarification is needed on how patterns are selected during an episode. Are multiple patterns chosen, or is only a single pattern used per episode? Could you elaborate more on this?

(3) It is unclear whether this method would succeed in more complex environments, such as StarCraft II or other sophisticated games. In these games, identifying successful patterns would likely be more challenging than in simpler environments like MuJoCo.

### Questions
Based on the weaknesses noted, I believe the paper does not meet the quality standards required for acceptance at the ICLR conference.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on improving the efficiency of training an adversarial policy in two-player competitive games. Specifically, the paper proposes a framework which leverages historical states and their rewards from previous episodes to compute a score using a recurrent model. This score is then used to augment the rewards during the training of the adversarial policy. Experimental results on MuJoCo environments showed the improved efficiency of the proposed method over existing baselines.

### Strengths
The paper is generally well-written and easy to follow, with the exception of certain sections in the results section, which seemed a little too brief. The idea of using past experiences to augment the rewards to improve the training is not necessarily novel, however, I believe they are novel in the context of applying them to train adversarial policies in two-player games  The methodology is also well-organized and the experimental results supports the paper claims. The use of group--based episodic feedback is an interesting technique, which adds to the quality of the findings and I appreciate the additional experiments which demonstrates the generalizability of the proposed methods to other baselines in the Appendix. The findings have potential implications for improving the robustness of agents in two-player competitive games.

### Weaknesses
Some sections lack clarity, specifically the sections on the Ablation study and terms like "non-loss rate" should be defined for completeness and would help readers understand these concepts better. The related works section would also benefit from rephrasing as certain paragraphs sounds a little misrepresented to me. The idea of using past experiences to improve the efficiency is also similar to works like Prioritized Experienced Replay, Hindsight Experience Replay, etc which could be cited in the related works section to provide a more comprehensive overview. In terms of the soundness of the results, the latter parts of the result heavily depends on anecdotal evidence and including more examples of such observations would make the findings more convincing. Additionally, discussing the limitations of the proposed method in terms of additional complexity would also help the readers better weigh the pros and cons of the method. My specific concerns are listed below.

1. In the related works section, the authors wrote: "However, the above attacks are argued to be unrealistic since the real-world environment can not be manipulated". While the authors referred to this statement by referencing other works, I believe this statement is slightly misrepresented. In reality, adversarial attacks on the environment via perturbing the observation/action channels are definitely realistic. Furthermore, the proposed approach of two player games is also a form of indirect environmental manipulation, which ultimately affects the observation space. Hence, this statement seems rather contradictory to me given the topic of the paper.

2. As mentioned above, the idea using good trajectories from the past to augment the training process to improve efficiency is not new. I would suggest the authors cite more related papers to create a more comprehensive overview. For example, how does the idea proposed in this paper differ from those of hindsight experience replay, prioritized experience reply, etc?

3. "The reward R′α obtained by the adversarial agent only includes the evaluations from a single game and does not contain evaluations from the historical experiences.". Does this imply that existing works on adversarial policy thus far are all on-policy?

4. In Equation 3, explaining what the "otherwise" scenario entails would make the paper clearer.

5. In Section 3.2.2, the authors used a moving average of recent rewards to compute the feedback. What happens the training destabilizes (which is common for on-policy) and the moving average decreases? Would the feedback still be helpful and is the formulation designed to handle such scenarios or is the assumption that the moving average rewards always increases needed?

6. "(In practical, we use sliding window)" --> Grammatical mistake

7. From what I understand, computing and updating the episodic memory every episode increases the computational complexity considerably of this method. Given this increased in complexity, a comparison of the wall-clock running time would be helpful, and would this method work if the memory updates are performed less frequently?

8. The conclusion that the agent is able to learn multiple winning strategies and learn adversarial and non-adversarial strategies are all based on a single anecdotal observation. The conclusions would be more convincing if the authors could provide more anecdotal examples

9. Terms like "non-loss rate" should be explained briefly for better clarity and completeness

10. In general, I find sections 4.3.1 and 4.3.2 a bit too brief to truly understand what the authors are comparing. For example, in 4.3.1, what is the difference between using the historical scores vs 3-step patterns? Could the authors elaborate more?

### Questions
1. In the related works section, the authors wrote: "However, the above attacks are argued to be unrealistic since the real-world environment can not be manipulated". While the authors referred to this statement by referencing other works, I believe this statement is slightly misrepresented. In reality, adversarial attacks on the environment via perturbing the observation/action channels are definitely realistic. Furthermore, the proposed approach of two player games is also a form of indirect environmental manipulation, which ultimately affects the observation space. Hence, this statement seems rather contradictory to me given the topic of the paper.

2. As mentioned above, the idea using good trajectories from the past to augment the training process to improve efficiency is not new. I would suggest the authors cite more related papers to create a more comprehensive overview. For example, how does the idea proposed in this paper differ from those of hindsight experience replay, prioritized experience reply, etc?

3. "The reward R′α obtained by the adversarial agent only includes the evaluations from a single game and does not contain evaluations from the historical experiences.". Does this imply that existing works on adversarial policy thus far are all on-policy? 

4. In Equation 3, explaining what the "otherwise" scenario entails would make the paper clearer. 

5. In Section 3.2.2, the authors used a moving average of recent rewards to compute the feedback. What happens the training destabilizes (which is common for on-policy) and the moving average decreases? Would the feedback still be helpful and is the formulation designed to handle such scenarios or is the assumption that the moving average rewards always increases needed?

6. "(In practical, we use sliding window)" --> Grammatical mistake

7. From what I understand, computing and updating the episodic memory every episode increases the computational complexity considerably of this method. Given this increased in complexity, a comparison of the wall-clock running time would be helpful, and would this method work if the memory updates are performed less frequently?

8. The conclusion that the agent is able to learn multiple winning strategies and learn adversarial and non-adversarial strategies are all based on a single anecdotal observation. The conclusions would be more convincing if the authors could provide more anecdotal examples

9. Terms like "non-loss rate" should be explained briefly for better clarity and completeness

10. In general, I find sections 4.3.1 and 4.3.2 a bit too brief to truly understand what the authors are comparing. For example, in 4.3.1, what is the difference between using the historical scores vs 3-step patterns? Could the authors elaborate more?

### Soundness
3

### Presentation
3

### Contribution
2
