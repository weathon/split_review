# Reinforcement Learning with Elastic Time Steps

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Traditional Reinforcement Learning (RL) policies are typically implemented
	with fixed control rates, often disregarding the impact of control rate
	selection. This can lead to inefficiencies as the optimal control rate varies
	with task requirements. We present the Multi-Objective Soft Elastic
	Actor-Critic (MOSEAC), an off-policy actor-critic algorithm that uses elastic
	time steps to dynamically adjust the control frequency. This technique
	minimizes computational resources by selecting the lowest viable frequency. We
	demonstrate that MOSEAC converges and produces stable policies at the theoretical
	level, and validate our findings in a real-time 3D racing game. MOSEAC
	significantly outperformed other variable time step approaches in terms of
	energy efficiency and task effectiveness. Additionally, MOSEAC shown
	faster and more stable training, showcasing its potential for real-world RL
	applications in robotics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends the classical RL setting, where there is no concept of the action execution time, to RL with elastic time steps. The authors propose SEAC to output the next action as well as the duration of the next time step.

### Strengths
The proposed problem is interesting. The figures are vivid, and the paper is easy to follow.

### Weaknesses
The contribution and novelty is vague. As for the traditional RL, the control frequency is only an abstract definition. I think the proposed framework can be seen as a special instance of the traditional RL framework given a reformulated action space / state space / reward function. The algorithm also seems quite like SAC with new state / actions. Also, what is the relationship between the proposed algorithm with HRL methods?

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a reactive reinforcement learning policy, which breaks the fixed time step assumption commonly adopted in RL and determines the next action and the duration of the next time step as input to the controller, thus integrating the temporal aspect into the learning process. The authors test their approach in a simulation of a simple word with Newtonian kinematics, showing its effectiveness in leading to higher efficiency in terms of speed and energy consumption.

### Strengths
The contribution is clearly stated and it is relevant to the development of real-world efficient and effective RL-based control systems. The paper structure is well organized and clear. Figures and schemes are helpful and explanatory. Limitations of the proposed approach (which components would be necessary for a real-world implementation) are clearly stated.

### Weaknesses
The contribution is relevant but it is limited compared to the existing state of the art. Since the contribution is mainly aimed to applying RL control outside of simulation, a proof of concept of the functioning of the proposed algorithm on a real-world application (rather than only in a simulation environment) would be important, in my view. 
Although the paper’s quality of presentation is generally fair, I found the comparison with the related works poor and lacking of an insightful discussion about existing time-sensitive RL tasks, which are only quickly listed at the end of section 2. Expanding such a paragraph could make the relevance and applicability of the paper’s contribution clearer. Specifically, the authors should elaborate on how their approach differs from existing methods in terms of handling temporal dependencies and action durations. A more thorough discussion of the trade-offs between the proposed method and other time-sensitive RL algorithms would also strengthen the paper.
The presentation of the results could also be improved. For instance, in Figures 5 and 6, it is unclear what the different representations on the left and right sides signify. Clarifying whether the right side is a zoomed-in view of the left side and explaining the legend for the lighter colored plots in the captions would enhance the readability. Additionally, Figure 7, while showing that SEAC dynamically changes the control rate, does not provide sufficient context to evaluate whether these changes are meaningful. Including information about the scenario and/or corresponding actions would make the concept clearer. Figure 8 could be more readable by inverting the x and y axes, placing the evaluation metric on the y-axis. Also, the mention of the overall reward in the section and figure caption is not visually represented, which could be confusing.

### Questions
-	Fig 1: I don’t find Fig 1 completely effective, based on the description within the Introduction. Since one of the contributions of the Elastic Time Step RL is that of enabling the policy to output the time step duration, together with the action, this could be somehow explicitly indicated in the Figure. Also, even though I understand the intention of splitting the “learning” and “execution” part of a RL implementation, I find the brain-like icon confusing when used to indicate the “execution” rather than the “learning” component of the system.
-	I would be curious to know from which specific practical application (robotics, autonomous driving?) comes the authors’ inspiration for the paper.
-	Page 4, sentence preceding Definition 1: “The aggregate reward for task completion is represented by r”. Did you mean “R” (capital letter)? 
-	The paragraph after Definition 1 (“We validate our reward strategy…”) could be rephrased to highlight SEAC differences compared to SAC.
-	What do you mean when you say “…giving a high probability that the agent can discover the optimal solution to complete the task”?  Maybe this sentence can be rephrased to make the exploration strategy clearer.
-	In general, from the sentence starting “we assume the agent…” to the sentence ending with “…Bellman equation”, I find the flow of the text, which can be read while referring to the scheme on Fig 3, a little hard to follow, in the sense that it jumps from one block to another one (of the Fig.3) without a precise order. Incorporating more references to the visual scheme and aligning the text with the functional flow of the figure 3 (rather than simply listing the meaning of the symbols) could help the readability. 
-	You mention that one major contribution of the SEAC is to include the execution time of each action to the output, but this term is not explicitly indicated on Fig.3, together with the At.
-	The meaning of the double arrows in Fig.3 is not very clear to me. Maybe an explanation could be included either on the caption or on the main text.
-	The impact value of the execution is defined, based on the chosen environment, as the target movement distance. Do you have in mind some examples of different implementations for different problems?
-	In the end of paragraph 3.1, when you say “the controller will compute a range of control-related parameters”, is this represented by Mt?
-	In the end of paragraph 3.1, when you say “our objective is for the agent to learn the optimal execution time”, is the execution time equivalent to the action time, and therefore represented by Tt?
-	Typo: “but but” in the sentence starting with “it is worth noting…” in paragraph 3.2
-	What is the meaning of “p” in eq. (2)?
-	Since the SAEC loss functions are (if I understand well) equal to those of SAC, rather than simply reporting the definitions, I would suggest to reorganize Section 4 to better explain how your formulation of the reward function is included in the update steps of the RL algorithm.
-	Section 5: When you refer to the “three RL algorithms”, do you mean SEAC, SAC and PPO? In this case, you should first say that you are comparing SEAC results with SAC and PPO in the text, otherwise it is not clear to the reader.
-	What are you representing differently on the left and right side of Fig. 5 and 6? Is it the right side simply a y-axis zoom-in of the left side? You should specify it on the figures' captions. What is the legend for the lighter colored plots?
-	I think that Fig. 7, as it is, is not very informative. It shows that SEAC dynamically changes the control rate, but it doesn’t allow to evaluate whether it does it in a meaningful way. Showing the scenario and/or information about the corresponding actions would make the concept clearer.
-	I feel Fig.8 would be more readable by inverting x and y axes (evaluation metric on the y-axis). Furthermore, you mention the overall reward both in the section and in the figure caption, but is the overall reward shown somewhere?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents relaxes the fixed frequency assumption of MDP typically studied in RL and proposes RL with elastic time steps.  Also a Soft Elastic Actor-Critic algorithm is derived with theoretical and practical benefits.

### Strengths
1. The work is concisely summarized.
2. The use of elastic time is important in the tasks such as robotics etc.

### Weaknesses
1. There are many existing studies with varying time (e.g. option framework, action repetitions…)
Authors introduce some notions of options and semi-MDP in appendix, but without clear definitions of each notation, which makes it harder to see the clear connections to the main work and the option framework.  (It was not clear how the authors validated Bellman-like equations for elastic time case)  Assuming the algorithm is properly derived from the option framework, it is necessary to compare to the existing work based on the framework.  (Or at least it should show significant practical results compared to the existing work; it seems the experiments are not for sufficiently complex tasks.)
2. Existing environments such as OpenAI Gym can be easily adjusted to include time as information for states; I am not sure what the authors mean by “...additional input and output information that is not available within existing RL environments…”
(Note that simulators anyway need to run with small time interval to maintain accuracy, and action durations can be just a repetition of that.)
4.  Figure 5 is a bit hard to parse: why time in seconds are negative?  I could guess this but it is better to make them crystal clear.
5.  It would be better to show baseline with 100Hz (fixed) case, not 5.0 Hz since the elastic one uses 1 to 100 Hz.
6.  Figure 7 is also hard to interpret; why are there only 2 time steps…?  2 steps are enough to complete tasks…?
7.  Finally, it was not clear why the authors specifically used the reward defined in Definition 1.

### Questions
1.  Figure 4 right seems too sparse; what does it try to imply?
2.  What is the action space A?  Is it the Cartesian product of “action” and “time”?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The main contribution of this paper is the idea that, in RL, a policy can be made to specify both a control action to apply *and* the length of time an actuator should apply that action. The paper integrates this idea within an existing, popular algorithm for model-free RL (the SAC algorithm), and presents comparative results in a small example problem.

### Strengths
As far as I know this precise idea is novel, and it is certainly intuitive. Results and other details aside, I think the community should investigate this direction more deeply and this paper provides a nice starting point for that effort.

### Weaknesses
Weaknesses:
- The literature review is quite thin, and as a circumspect reader I do wonder how novel this idea really is, given how little literature is referenced. For example, a quick google scholar search reveals the following papers that seem to be very closely related: [1, 2]. I would also add that variable rate decision making is widely studied in the control theory literature. A key phrase to find this literature is “adaptive time step.”
- The paragraph immediately above section 3.1 indicates that there are a lot of loose ends that are not being discussed in detail, and which may strongly affect results. The imprecision of this discussion (e.g., what is a “partial MPC” and what role does the PID serve if you already use MPC?) suggests that the work may be somewhat immature. The use of a PID controller in conjunction with MPC is particularly concerning, as MPC typically subsumes the role of PID control. The lack of clarity on how these two control methods interact raises questions about the overall system design and its potential for instability or suboptimal performance.
- The reward structure discussed section 3.1 is *not* what one would properly call a “multi-objective optimization problem.” A distinguishing trait of such problems is the concept of “Pareto optimality” which encodes all of the tradeoffs among optimal performance with respect to each separate objective. By assuming a fixed weighting, this paper effectively reduces the problem to a standard optimization problem (and picks a single point on the Pareto frontier). I recommend consulting [3] for further details. The scalarization of the reward function through fixed weighting obscures the underlying trade-offs between different objectives, which is a key aspect of multi-objective optimization.
- Relatedly, the construction in Definition 1 is not as clear as it could be. For instance: are the R terms intended to be functions of state (and action)? If so, why does it make sense to only accrue reward at the times when actions are changed? Doesn’t that lead to some obvious opportunities for reward hacking? For example, could an agent decide to plow straight through some region of low reward for a bunch of (unactuated) time steps? Also, can R_t and R_\epsilon be evaluated at every time, or only at the end of an episode? Evidently, at every time t, but then I am lost as to why the agent is incentivized to minimize n, the length (in steps) of an elastic time step. I am lost. The definition of the reward function needs to be more precise, particularly regarding the timing of reward accrual and its dependence on state and action. The incentive for minimizing the length of the elastic time step is also unclear and requires further explanation.
- The details of the method are really not very clearly explained. For example, throughout the discussion of section 3 it appears that the there is some notion of an agent physically moving and the policy gets to access a measure of distance somewhere. This is unclear: everything up until this point (and in general) is framed around general MDPs, which have nothing to do with physical embodiment. How general-purpose is the proposed approach? The lack of clarity regarding the physical embodiment of the agent and its interaction with the environment raises concerns about the generalizability of the proposed approach to other MDPs.
- Relatedly, the test environment is not very clearly explained, or at the very least, suggests a very basic question: wouldn’t it make more sense for the policy to output a force, rather than a target position? This would remove the need for lower-level tracking control (MPC, PID) and also mitigate the “measure of distance” question above, I believe. The choice of outputting a target position instead of a force introduces unnecessary complexity and obscures the direct control of the agent's motion. This design decision also raises questions about the role and necessity of the lower-level tracking control.
- I do not follow the “six dimensions of the state in the environment” - in fact, I count 9: 2 each for agent/obstacle/goal position, 2 for agent velocity, and 1 for duration. What am I missing? In the same paragraph, the discussion of semi-Markov processes and recurrence is rather opaque. Use of words like “might” and “could” lead me to wonder how clearly this point is understood. I suggest clarifying the language here. The discrepancy in the stated and actual state dimensions, along with the vague discussion of semi-Markov processes, indicates a lack of precision in the description of the environment and its dynamics. The use of tentative language further suggests a lack of clarity in the understanding of these concepts.
- There are no discernible error bards in the plots, and the shaded areas appear to be traces of other plotted data - this needs to be explained precisely, and plots should show some measure of error in order to be interpreted statistically. The absence of error bars in the plots makes it difficult to assess the statistical significance of the results and raises concerns about the reliability of the conclusions drawn from the data. The nature of the shaded areas also needs to be clarified.
- More importantly, even: there is little to no interpretation of the behavior of the proposed policies. Results here indicate some differences in aggregate behavior (although the interpretation to that effect should really require some error bars as above), but it would really help to understand what is going on if the authors expanded upon Fig. 7 to illustrate what was going on in the environments in these situations and why it made sense to change the control rate as shown.

Other nitpicks:
- It seems like the main motivation here is one of saving computational resources. Obviously, most control systems are pretty lightweight and so I imagine these savings really come in from the perception side, e.g., if you no longer have to process big images at high frame rate. Experimental results to illustrate these savings more directly than the abstraction of “number of repeated actions” would be highly motivating.
- There are quite a few typos and other small syntax issues.
- The vertical axis labels are wrong in Fig. 5.
- Figures 5 and 6 could be more clear about indicating that the right hand sides are insets of the left. Also, why were the methods run for so long - it seems they all converged quite a bit earlier and then for some reason PPO destabilized. Something seems off here.
- Why does Fig. 7 say “epochs” instead of “configurations?”

### Questions
Please see my comments above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
