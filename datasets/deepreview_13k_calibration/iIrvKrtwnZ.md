# HuRi : Humanoid Robots Adaptive Risk-ware Distributional Reinforcement Learning for Robust Control

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
Due to the high complexity of bipedal locomotion, the locomotion control of humanoid robots requires precise adjustment of the balance system to adapt to the varying environment conditions. In the past, few studies have explicitly incorporated risk factors into robot policy training, and lacked the ability to adaptively adjust the risk sensitivity for different risky environment conditions. This deficiency impacts the agent’s exploration during training and thus fail to select the optimal action in the risky environment. We propose an adaptive risk-aware policy(HuRi) based on distributional reinforcement learning. In Dist. RL, the policy control the risk sensitivity by employing different distortion measure of the esitimated return distribution. HuRi is capable of dynamically selecting the risk sensitivity level in varying environmental conditions by utilizing the Inter Quartile Range to measure intrinsic uncertainty and Random Network Distillation for assessing the parameter uncertainty of the environment. This algorithm allows the agent to conduct safe and efficient exploration in hazardous environments during training, enhancing the mobility of humanoid robots. Simulations and real-world deployments on the Zerith-1 robot have been conducted to confirm the robustness of HuRi.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents an approach to training humanoid robots for locomotion in risky environments using deep reinforcement learning.  The key innovation is the development of an adaptive risk-aware distributional reinforcement learning algorithm, which allows adjusting risk sensitivity based on uncertainty in the environment.  This is achieved by combining intrinsic uncertainty, measured using the interquartile range, and parameter uncertainty, evaluated using random network distillation.  The proposed algorithm enables the robot to learn a robust locomotion control policy.  The method's effectiveness is demonstrated through simulations and real-world experiments on the Zerith robot, showing its ability to handle various disturbances such as sudden impacts, load variations, and uneven terrain

### Strengths
1. This paper introduce Wang function for risk-aware reinforcement learning and considers intrinsic uncertainty and parameter uncertainty for risk sensitivity adjustment.
2. The proposed method demonstrates superior performance compared to the baseline PPO and a fixed risk-sensitive method (CVaR0.5) in both simulation.
3. The proposed method is extensively evaluated in different scenarios, including simulations with different types of disturbances and real-world experiments on a physical robot.

### Weaknesses
1. Effectiveness of Wang function needs to be verified. Considering add some experiments to verify the effectiveness of Wang function as it is one of the core contribution of this paper, for example, adjusting the risk sensitivity of CvaR with intrinsic uncertainty and parameter uncertainty and compare with your method.
2. The real robot experiment is weak, authors should considering comparing your method and baselines on real robot.
3. The authors claim that "our method exhibits strong robustness in agents and bridges the gap between simulation environments and the real world", however, there is no content in the paper shows how the method benefits sim2real.
3. Considering other recent work focusing on blind humanoid locomotion, such as [1], have much better performance on locomotion, I wonder if risk-aware reinforcement learning is harmful to locomotion task.

### Questions
See weakness.

### Soundness
3

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
4

### Summary
This paper introduces HuRi, a new method for training humanoid robots to walk stably in challenging conditions by automatically adjusting their movement cautiousness based on environmental risks. The approach combines distributional reinforcement learning, which learns the full range of possible outcomes rather than just averages, with an adaptive risk adjustment system that uses uncertainty measures (IQR and RND) to assess danger levels and modify the robot's behavior accordingly. The authors demonstrate through both simulated and real-world experiments that HuRi outperforms baseline methods, achieving better stability under various disturbances including external forces, heavy loads (up to 42% of body weight), and sudden impacts.

### Strengths
- Well written paper with thorough implementation details. The empirical results demonstrates meaningful improvements over baselines for humanoid walking, particularly in handling disturbances and varied terrain
    
- Effectively demonstrates how uncertainty-aware RL can aid safe exploration in complex humanoid tasks - an important contribution that could extend beyond locomotion to manipulation and other high-dimensional control challenges in humanoid robotics

### Weaknesses
 - Statistical robustness concerns: Figure 3 appears to show results from a single training seed, as evidenced by sharp performance dips. Multiple seeds are needed to validate learning stability, and success rate curves across seeds would better demonstrate robustness claims
    
- Limited exploration of reward structure impacts: While the method shows improvements, there's no analysis of how dependent these gains are on their specific reward formulation. Recent work [1] has shown phase/clock-based rewards may not be optimal for robust locomotion. A comparison with alternate reward structures would strengthen their claims.
    
- Uncertainty measurement complexity: The combination of RND with distributional RL seems potentially involved. I did not quite understand the justification of why RND is needed on top of distributional uncertainty estimates. Did the authors try to explore whether simpler approaches could achieve similar results, for example just using RND?

### Questions
**Minor Details:**

1. For improved readability, best scores in Table 1 should be highlighted in bold or black
    
2. Section 4.2's experimental description needs clearer organization: explicitly state that the evaluation focuses on two distinct robustness tasks (handling continuous forces and sudden impacts) with corresponding training setups. Current wording creates ambiguity about whether evaluations were conducted on out-of-distribution scenarios
    


*[1] Marum, Bart Jaap van et al. “Revisiting Reward Design and Evaluation for Robust Humanoid Standing and Walking.” *ArXiv* abs/2404.19173 (2024): n. pag.*

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
## Humanoid Robotcs Adaptive Risk-aware Distributional RL for Robust Control
This paper presents a risk-aware framework for training humanoid robot policies. The main contribution of the paper is the usage of distributional RL as a method for controlling the risk that a humanoid's policy incurs during exploration and execution. The motivation of the risk-awareness in humanoid systems comes from the delicate and robust control that the actuators must execute on the robot in order to maintain stability. Finding these stable controllers is difficult and dangerous, so risk-awareness in the policy is necessary. The authors provide experiments on a simulated humanoid robot and real-world experiments.

### Strengths
This paper is well-motivated and attempts to solve a real-world problem in humanoid robotics. The demonstration of their method on real robots is commendable and a good contribution to the paper.

### Weaknesses
There are a series of minor typo errors as well as incorrect latex formatting. While most of these issues don't hinder understanding, they make it harder to read the paper. For example:
1. Title says "Risk-ware" instead of "risk-aware"
2. Line 106 is missing a citation
3. Most citations seem to not use \citep{} or \citet{}. They all are joined with the previous word.

Major issues:
1. Presentation of method is unclear: throughout section 3, the authors introduce various components of their method. Because each component is described mainly in text, the structure of dependancies and framework is difficult to understand. Figure 2 is helpful, but not fully informative. I would suggest including an Algorithm Block that goes through each component step-by-step. Further, it would be helpful to include labels for all the equations/expressions that are splitting up the paragraphs throughout the method section
2. Usage of $SR(\lambda)$: This term is introduced around line 229 but never really described in great detail. In general, this paragraph from 226 to 240 is confusing and would benefit from being described through an algorithm block
3. The quantile loss in line 241 does not include the distribution over which the expectations are being taken. 
4. MSE loss in line 247 has incorrect notation that make its meaning ambiguous (mismatched paranthesis)
5. $g_\beta^\text{Wang}$ in line 254 is introduced without any additional supporting information. In the following paragraph, the authors describe the nuances of $\beta$ but not where the function $g$ is ever used. Please clarify its position in the method.
6. *Poor reward comparison experiment*: The results in Figure 3 do not include any error bars or indicate any notion of statistical significance. It is necessary for the authors to run these experiments over multiple seeds and report aggregated performance. Also, is reward the right metric of performance? I would imagine that violation of safety constraints is a more important feature to report on. 
7. Robot specific simulated experiments: While the results reported in the remainder of the simulated experiment section are important, they seem more like results that would be found in a pure robotics paper.
8. Real world experiments lack statistical or more analytical significance. Please include some information on how the experiments show that the risk-awareness is important and that your instantiation of the risk-aware framework out performs other real-world methods. To do this, you might report success rates and safety violations that the varying methods exhibit.

### Questions
No additional questions. Please address the issues/questions I mention in the Weakness section

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript presents a novel method for risk-aware distributional reinforcement learning called HuRi. The main innovation compared to previous works is a novel adaptation scheme for choosing the risk-awareness sensitivity of the policy based on the current state (i.e. if the policy will be cautious, exploratory/aggressive or neutral). The authors propose to use a combination of distortion functions (already present in the literature) and the usage of a Random Network Distillation (RND) process. Overall, the new approach is evaluated in humanoid locomotion tasks and showcases superior performance compared to baselines and ablations.

### Strengths
1) Adapting risk-awareness depending on the current state is an interesting concept and has not been extensively explored. Especially in humanoid robots.

2) The usage of the RND process for risk adaptation is quite interesting and quite novel (as far as I am aware of the literature).

3) The real-world evaluation on a humanoid robot is highly appreciated.

4) The authors provide most details needed to replicate their approach.

### Weaknesses
1) The paper presentation needs a lot of work. There are numerous small things and typos that add up and make the paper difficult to understand. First, the citations are not well formatted and this makes reading the manuscript difficult. Secondly, the notation is not consistent: sometimes $\boldsymbol{x}$ is used for the state, and some other times $\boldsymbol{s}$ is used for the state. Another example is that the paper is about humanoid robots and then in the theorem the authors state "We describe the locomotion problem of quadruped robots". Overall, the presentation and writing of the paper requires quite some work.

2) As far as I can tell (given the difficulty of understanding the manuscript described above), the authors claim that the novelty lies in a) the usage of an adaptive mechanism for adapting the β parameter of the distortion function, and b) the training of the RND network for β adaptation. Although I can see value in the adaptation mechanism, the motivation of using the RND network is rather weak. Similarly, the evaluation and discussion on why it works better is again rather weak. I would have expected a more thorough discussion and analysis since RND seems to be the critical factor in the performance gains.

3) The experimental section requires more work. For example, in Fig. 3 (and the describing text) we do not know if the authors ran just one training and smoothed out rewards or they ran multiple seeds and take some statistics. Similarly, for the experiments shown in Fig. 4, the authors do not mention how many seeds they used. They do mention the number of seeds for the experiments shown in Tab. 1. Overall, this goes back to presentation; the manuscript requires substantial work to make it understandable.

4) In the current form, we cannot really evaluate the real-world experiments. Figures 6,7 and 8 do not showcase anything that is written in the text. We cannot validate what's happening here. The video showcases a lot of nice behaviors, but we need a more rigorous evaluation here. It is very difficult to evaluate the performance of the policy at the moment.

5) I do not get how the proposed approach is specifically suited for humanoids (which the author attempt to motivate, but fail imho).

### Questions
See weaknesses.

### Soundness
3

### Presentation
1

### Contribution
3
