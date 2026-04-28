# The Value of Sensory Information to a Robot

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
A decision-making agent, such as a robot, must observe and react to any new task-relevant information that becomes available from its environment. We seek to study a fundamental scientific question: what value does sensory information hold to an agent at various moments in time during the execution of a task? Towards this, we empirically study agents of varying architectures, generated with varying policy synthesis approaches (imitation, RL, model-based control), on diverse robotics tasks. For each robotic agent, we characterize its regret in terms of performance degradation when state observations are withheld from it at various task states for varying lengths of time. We find that sensory information is surprisingly rarely task-critical in many commonly studied task setups. Task characteristics such as stochastic dynamics largely dictate the value of sensory information for a well-trained robot; policy architectures such as planning vs. reactive control generate more nuanced second-order effects. Further, sensing efficiency is curiously correlated with task proficiency: in particular, fully trained high-performing agents are more robust to sensor loss than novice agents early in their training. Overall, our findings characterize the tradeoffs between sensory information and task performance in practical sequential decision making tasks, and pave the way towards the design of more resource-efficient decision-making agents.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method to answer the question in the title. More specifically they approach the problem as how does the frequency of observation updates change policy performance. They perform many studies on various environments to answer this question.

### Strengths
Research Problem
Very good. In my view there are two research questions that this work attempts to answer. One is “how important is recent information to learned policies?”, the other is “what is the best way to determine how important is recent information to learned policies?”. Both questions are interesting and relevant to the field. 

Novelty
Very good. I’m not very familiar with the sensing in agent learning literature but if their related work is complete (which it seems to be), their work has significant novelty.

Significance/Contribution
Very good. This work could have a lot of significance in the field. The idea of not only discovering the importance of information to policies (and robots) but also the general idea of how to study this question could provide many other works a base to work off. My one complaint is that the introduction doesn’t give the authors perspective on their exact contribution with this work. Adding a few lines in with their contribution would be great as someone who is more broadly in the RL field but not the specific questions of sensing for RL and learning.

Algorithm Details
Good. There isn’t an algorithm in this work exactly, but their method is described well. It isn’t an extremely complex idea (using policies that can predict multiple actions in the future) but from their description I believe I could recreate their work.

Experimental Selection
Excellent. Most of this paper is made up of experiments and analysis to answer their questions. I think the questions presented are well thought out.

Presentation of Results
Good. In general, the results are clear and the figures well done.  

Clarity
Very good. In general, this paper is very well written and clear. I had no issues reading or understanding the ideas.

Future Work/Conclusion
Very good. I think the future work presented in this paper answers the ideas I had for future work. I think the authors can build upon it in interesting ways and can continue to grow our understanding of these questions presented in the paper.

### Weaknesses
The one figure I’m still confused about is Figure 9. I don’t completely understand the figure even with the description in the text.

Statistical Rigor
I would like confidence intervals on all of the figures. They are on some but figures 3, 4, 5 and 11 don’t have them. Having CIs is critical to understanding the data.

### Questions
Baseline Comparisons
There are no baseline comparisons in this work. It seems to be that there is no comparable baseline to have here from the related work. That is reasonable to me but I wonder if for the results presented in figure 11 you might be able to have a baseline comparison? The idea is for different amounts of maximum regret you have some amount of sensory interaction. Is it possible to do some comparison here for the other works that also reduce sensory interaction?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper empirically studies the value of sensory information in a variety of robotic tasks and for policies stemming from different learning approaches. This is achieved by mixing open-loop and closed-loop control. Performance degradation is analyzed and its correlations with sensing-frequency, task proficiency, task difficulty, etc. are analyzed. VoSI is proposed as a metric, as well as derived variants that are reward-free and interaction-free. Finally the paper shows a first attempt at using the VoSI profiles for control with parsimonious sensing. The paper studies 7 robotic tasks and a benchmark, which reveal insights.

### Strengths
The paper is well written and tackles an interesting and understudied problem, that has practical relevance in robotics.
The extensive experiments are well designed and executed. Having a diverse set of tasks and environments is appreciated.
The methodology for analysis is sound, the proposed metrics potentially more widely applicable, and the final proposal for using them for control interesting.
The paper is well written and easy to follow. The supplementary material is well done and provides many additional relevant details.

### Weaknesses
 - In my opinion the paper studies entirely the wrong setting
  - It only becomes clear rather late in the paper that all experiments (except 4-room) are done in a setting assuming perfect sensing and that everything is deterministic. That's exactly the opposite of how things work on a real robot and where the challenges lie. Sensing is going to be imperfect, and a robot has to deal with unknown perturbations, changes and variability in the environment/objects/tasks, etc. The authors mention those things as future work, but I'd argue that without considering those the paper isn't much more than an academic exercise in a setting that is simplified to a point it doesn't have any practical use for robotics and/or control. The assumption of perfect sensing and deterministic environments fundamentally limits the applicability of the findings to real-world robotic scenarios, where these conditions are rarely met. This simplification makes the analysis less relevant to the core challenges in robotics, such as dealing with sensor noise, model inaccuracies, and environmental uncertainties.
  - In a similar vain, I would not call the considered tasks 'robotic'. Some of them are more on the side of toy benchmark tasks, others are indeed robotics-inspired but still quite far from being representative for real robot tasks (see reasons above, and you already hinted at problems of Robosuit yourself [being essentially purely kinematic]). The tasks, while common in the robot learning community, lack the complexities of real-world robotic manipulation, navigation, and interaction. The reliance on purely kinematic models and the absence of dynamic effects further reduces the practical relevance of the experiments. For instance, tasks like the cup-catch, while visually appealing, do not capture the intricacies of real-world object manipulation with noisy sensors and imperfect actuators.
  - On the flip-side, the tackled problem really is only relevant for real robots. For other policy learning settings - simulated robots, or maybe entirely different domains - the usefulness seems rather limited. Also, how much of a need for parsimonious sensing there really is, is also a bit debatable - it highly depends on the robot embodiment (light-weight UAV vs. stationary robot arm vs. networked swarm).
- The paper ignores a huge body of work. Work in the control community, in particular on event-based/event-triggered control/state-estimation, has studied this kind of problems since decades$^*$ and as a consequence come to the same insights. Overall the paper feels a bit like re-inventing the wheel (also e.g. the state-disagreement metric). Work on event-based sensing / event-based cameras also goes in a similar direction.
- With the above background, this paper serves as a nice confirmation about what common knowledge in control and robotics would predict.
  - When having the 'perfect world' assumption in mind, none of the findings are surprising, let alone counter-intuitive. In a perfect world, with perfect models, sensing etc. all tasks can be solved open-loop. Feedback is required when the models no longer hold (external perturbations, stochasticity, imperfect models) which you nicely show.
  - And then we can also think about making things more robust, i.e., finding a strategy that can deal with imperfect models/sensing, usually at the cost of performance, e.g., sim2real approaches.
- At least for the RL setting, I find the approach of using a policy that was trained closed-loop problematic as you point out in l. 339. It sounds a bit like "we got lucky". When instead training the policy with the parsimonious sensing, the policy will potentially change drastically to account for that. So the analysis is at best a proxy of what could be achieved under that setting.
- Minor
  - It would have been nice to promise releasing the code
  - typo l. 313 "hase"
  - typo l. 508 "efficient efficient"


$^*$ See e.g.

Trimpe, S. and D'Andrea, R., 2011. An experimental demonstration of a distributed and event-based state estimation algorithm. IFAC Proceedings Volumes, 44(1), pp.8811-8818.

For a cool real-world demonstration

### Questions
- I'd be really curious to see how the results change when introducing stochasticity/noise. I'd assume the VoSI profiles will change quite a bit, e.g. for the upright phase in swing-up
- Another interesting aspect would be to analyze the influence of the sensing-frequency on generalization. E.g. is more frequent sensing more robust to changes in the environment, perturbation, etc.?
- To push it even further you could consider analyzing what happens if you train the base-policies with domain randomization to make them more robust.

##After rebuttal
Thanks for the detailed and constructive replies. I have increased my score (as indicated in my message below).

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates how frequently action sequences should be recomputed based on new observations with Diffusion Policy and TD-MPC2 on simulated benchmark tasks. The authors find that for many tasks, it is sufficient to recompute the action sequence at a low frequency, and for tasks from the Robosuite environment, it is even sufficient to use only the initial observations and execute entire rollouts open-loop. Furthermore, the authors identify stochasticity in the dynamics and modeling error as reasons why the action sequence needs to be updated based on new observations. They then devise a strategy for adapting the sensing and replanning frequency dynamically during the policy rollout.

### Strengths
The paper conducts an intriguing investigation of how frequent sensor input is needed during the execution of imitation / reinforcement learning policies. The paper is well-written, the experiments are clear, and the results are presented nicely. It is very interesting that the Robosuite tasks can be solved entirely with open-loop control, which suggests that this simulated benchmark might not capture the intricacies of real-world robotics applications well.

### Weaknesses
1. The paper aims to provide insights for robotics tasks, yet all results are obtained only in simulation. The characteristics of simulated benchmark are clearly very different from real-world robotics tasks. Simulations tend to behave significantly more deterministically and predictably. Real-world robotics tasks typically involve significant noise e.g., from the sensors and the actuation, and there are hard to model effects like friction and contacts, which are simplified significantly in dynamics simulators. The fact that the Robosuite benchmarks can be solved by only taking the initial observation into account further indicates that these benchmarks are too simplistic and do not capture the intricacies of real robot tasks. Furthermore, it seems challenging to conduct a similar analysis on real robots since the method requires collecting multiple rollouts for each state. I would appreciate it if the authors could discuss these limitations and the expected differences if such an analysis were applied for a real task.

2. It seems to me that the reward-free and interaction-free VoSI alternatives are still not very practical since these metrics cannot deal with situations in which there exist multiple possible strategies for solving a task. TD-MPC2 learns a dynamics model of the environment. Could we use the deviation between the rollouts predicted by the model and the true rollouts as a proxy for VoSI to circumvent the problem in this case?

3. The sensing frequency adaptation scheme was only tested on a gridworld task. Due to the discrete nature of the gridworld, the tested model is either perfectly accurate or predicting some completely different state. In robotics applications (the focus of the paper), models are typically always somewhat accurate and the main issue is accumulating errors. Clearly there are certain states/actions that cause larger model error (e.g., when the robot is in contact), but still this kind of model error seems to be quite different from the gridworld setting. In a robotics setting, I assume that the optimal sensing strategy is significantly closer to the fixed-rate strategy since preventing error accumulation requires frequent corrections. Perhaps the authors could comment on whether they expect similar benefits of the adaptation strategy in a robotics scenario or on how the experiment could be made more realistic.

4. I am unsure whether sensing frequency adaptation according to the VoSI can be useful for real-world robotics applications. In the current form calculating the VoSI requires multiple rollouts, which would defeat the purpose of increasing the computational efficiency. Furthermore, I am unsure whether a strategy to adapt the replanning frequency makes sense in typical real robotics applications. Usually the actions are executed at a fixed rate on the system, so the controller might be able to produce the action faster if it does not replan according to new sensor information, but this does not mean that the execution will be faster since then the controller just needs to wait according to the control frequency anyway. I would appreciate if the authors could expand on how this strategy could potentially be extended to real systems and what the benefits in practical applications could be.

5. Line 52: "Sensing only improves the agent actions significantly at some rare moments during task execution". This statement seems to hold only for certain tasks. Row 2 in Figure 7 shows that for at least two tasks, the performance degrades continuously the lower the sensing frequency is. If the statement above were accurate, then we would see a steep increase in the VoSI at the critical timestep (as e.g., in the swingup examples). I encourage the authors to revise this statement and acknowledge that the observation only holds for certain environments.

6. Line 290/291: The statement "agents [...] exposed to more training data usually degrade less" is not really backed by the data. This is only the case in in finger-spin, while in Push-T it seems to be the other way around. The authors should either provide more data to support the claim or revise the statement to make sure that it accurately reflects the data.

7. Line 810: The way that U(s') is defined, it is a uniform distribution over all states, which would mean that the model predicts that the agent teleports randomly across the gridworld. I feel like it should rather be a uniform distribution over something like the neighboring states as this seems like a more realistic error model (a realistic model would probably get the states at least approximately correct, but might make mistakes in the details).

8. There are relatively few tasks for which there are results for both Diffusion Policy and TD-MPC2 (only swingup and Push-T). It would be good to have results for more tasks with both methods to see how consistent the results are across the learning methodologies and policy architectures.

### Questions
1. Line 54: In my opinion it is not counter-intuitive that the agent's performance is inversely correlated with the sensor dependency, particularly in the case of TD-MPC2. TD-MPC2 learns a dynamics model of the environment that it uses for planning. The longer the agent was trained, the more accurate the model is, which means that the agent needs to correct the model error less frequently with real data. Perhaps the authors could expand on why they consider this inverse correlation as counter-intuitive.

2. In the plot for Push-T in Figure 10, it seems that most of the curves are quite flat, even though the contact dynamics should be relatively hard to predict for long horizons. Do all the flat curves correspond to cases where the T is almost at the target location or are there other situations in which the dynamics behave particularly predictable?

3. Figure 11: For "fixed-rate" the sensing rate specifies the frequency at which the policy gets new sensory input and recomputes the action sequence. For the "greedy" configuration there is no fixed rate as the execution strategy adapts the h dynamically. What exactly is plotted on the x-axis for the "greedy configuration"? Is it the average sensing frequency?

4. Line 835: If I understand correctly, this maximization is supposed to choose the largest h, so that the VoSI stays above the threshold. Shouldn't that rather be formulated as
$\mathrm{max}~ h ~~ \mathrm{s.t.}~ \mathrm{VoSI}(s_t, h) \leq h \delta$?

### Soundness
2

### Presentation
3

### Contribution
2
