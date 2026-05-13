# Reinforcement Learning for Control of Non-Markovian Cellular Population Dynamics

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Many organisms and cell types, from bacteria to cancer cells, exhibit a remarkable ability to adapt to fluctuating environments. Additionally, cells can leverage memory of past environments to better survive previously-encountered stressors. From a control perspective, this adaptability poses significant challenges in driving cell populations toward extinction, and is thus an open question with great clinical significance. In this work, we focus on drug dosing in cell populations exhibiting phenotypic plasticity. For specific dynamical models switching between resistant and susceptible states, exact solutions are known. However, when the underlying system parameters are unknown, and for complex memory-based systems, obtaining the optimal solution is currently intractable. To address this challenge, we apply reinforcement learning (RL) to identify informed dosing strategies to control cell populations evolving under novel non-Markovian dynamics. We find that model-free deep RL is able to recover exact solutions and control cell populations even in the presence of long-range temporal dynamics.  To further test our approach in more realistic settings, we demonstrate performant RL-based control strategies in environments with dynamic memory strength.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers the problem of controlling cell-population by adjusting drug dosage. In line with medical research, the authors propose a dynamics model with memory (non-Markov) for this setting, based on ODEs, and derive the theoretical optimal controller for drug administration, that is found to be a "bang bang" controller. Using this insight, the authors formulate this problem as an RL problem, then use RL with reduced action-space to solve it. The method is evaluated against a few naive baselines on a simulated environment, showing both superiority over the baselines, robustness to noise and changes of the memory of the system.

### Strengths
### Presentation:
The paper is well written, and for me, it was easy to understand, in addition, it cites many relevant papers across all fields (RL, control theory, medicine).

### Methodology:
I think this paper bridges some of the gap between real-life problems to RL; while it is more applicative in terms of RL, it suggests how to do it right and efficient. The analysis in Sec. 2 enables RL to solve the problem (still need to show it). The experiments are extensive and show results for a few settings, and how it affects the model results.

### Weaknesses
### Presentation:
In the current form, the paper is written as two papers: One that formulates the problem and another that utilizes RL to solve the problem. For my opinion, it should have a more solid story, which would require some rephrasing. Considering the title, I suggest noting the difficulties of using RL for the raw problem, and then present your analysis for the optimal control which provides a solution which implies a much simpler problem for RL.

### Experiments:
I think that the naive baselines are not enough here, maybe add an RL variant that operates over the continuous action-space, showing the importance of your optimal control analysis?
Also, there are missing details for the experiments -- for how long the RL agent is trained? what

### Contribution:
My concern here, is that the method is motivated by real world, but eventually tested in simulation. Which shakes the ground of this paper, as it all revolves around the suggested dynamics model. I think another step towards bridging RL and real-life should be added. Since it is less likely to perform experiments that involve real-life environment and control, I would suggest showing empirically that the proposed dynamics model could indeed predict cell population -- using real-life data.

### Questions
1. How many random seeds/trajectories did you use in each experiment? What is the faded area in Fig. 4?

2. Have you tested how robust is the resulted policy to parameter noise of the model?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes to model the non-markovian process of adaptive cellular growth dynamics in bacterial and cancerous populations to learn optimal drug dosing using reinforcement learning. It shows successful training of an improved policy for memory-based systems compared to optimal control, which is robustness to observation noise and memory strength perturbations.

### Strengths
The paper is well-motivated and regards a relevant real-world application. It is generally well-written, explained, and easy to follow. It provides a formally sound theoretical connection of the problem at hand to optimal control theory, extended to the application of reinforcement learning (including realistically obtainable observations) to tackle current shortcomings. Convincing empirical results show improved adaptability and generalization to varying memory levels of the underlying model.

### Weaknesses
While, in general, the problem is well-explained and elaborated, an example or illustration might have been useful. Also, the figure placement and referencing should be improved to further ease readability. The overall objective of reducing the population by minimizing growth to negative growth could be stated more clearly in the former sections (e.g., 2.1). In Fig. 2 (right), a comparison to the memory-less or optimal control approaches used as a baseline later on could have been insightful. 

Minor comments: 

- p.2 l.89 no middle part in Fig. 2 (referencing the wrong figure?)
- p.6 l.308 RL uses gradient ascent on the reward, not SGD.

### Questions
Do the authors have any intuition on how RL would perform in a continuous drug control scenario? 

If the constructed model might not fully describe the underlying biological dynamics (cf. p.4 l 214f.), causing OC to be inaccurate, how does RL solve this issue? 

How are the objectives of maximizing net death and maintaining the stability of the subpopulations connected? 

Given that learning an RL policy in a specific real-world application would not be feasible (similar to OC), how well does the resulting policy generalize regarding the parameters underlying the assumed model (beyond the memory size)? How can overfitting to the chosen training specification be prevented?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the challenge of controlling and driving cell populations, such as cancer cells, toward extinction in environments where exhibiting adaptability and memory of past stressors. This is particularly difficult in systems with unknown parameters or those displaying non-Markovian dynamics such memory-based systems. The authors propose a new memory-based model for switching population dynamics, develop an optimal solution for the memoryless case, and apply model-free deep reinforcement learning (RL) to develop effective drug dosing strategies for cell populations with memory. The proposed approach is tested by comparing its performance against known exact solutions in controlled scenarios, demonstrating that deep RL can accurately recover these solutions. Additionally, the approach is evaluated in more complex environments where the memory strength of cell populations varies. The results demonstrate the method’s robustness in managing dynamic, memory-influenced systems.

### Strengths
- Very clear exposition, introduction to the problem and model development
- Contribution of a novel model useful for RL-based optimization of drug dosing
- Useful insights from control theory that allow simplification of the problem
- Optimal solution given for the memoryless case which serves as a sanity check for the RL-based method
- Convincing results of the RL-based solution compared to three baselines
- Clinically highly relevant problem overall

### Weaknesses
 - Limited methodological contribution: author's mainly apply existing RL methods to a newly developed simulation model (I see the model itself and the insights gained about it as main contribution)
- Not clear whether assumed time-scales are realistic

- The choice of FQF over DQN, and the use of Noisy Nets for exploration, are not sufficiently justified. The paper does not present ablation studies to demonstrate the necessity of these choices. It is unclear how much performance gain is attributable to FQF compared to a simpler DQN implementation, and whether the exploration benefits of Noisy Nets are significant over annealed epsilon-greedy. This lack of analysis makes it difficult to assess the true contribution of the methodological choices.

### Questions
- Given that mammalian cancer cells are targeted as an application scenario which generally have a cell division rate of about 24h, how realistic are the assumptions in the paper made about the delta parameter and the control frequencies applied by the pulsating policies?
- Can you give more biological motivation for the experiment with the switching memory strengths in Fig. 4 (right)?
- How important is the switch to FQF from DQN in section 5? How well would DQN do on the more challenging problems considered there? How important is the use of Noisy Nets for exploration over just using annealed epsilon-greedy? These points are not examined, which makes an assessment of the justification for the methodological choices difficult.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies how non-markovian cellular population dynamics can be chemically controlled through the lens of RL.
While prior work focused on markovian assumptions or unrealistic assumptions, this paper tries to apply deep RL (DQN-based methods) to assess how effective this would be to design drug delivery patterns that optimally control the pathogen cellular dynamics.
The results of the RL-based method are encouraging: the authors show that in the markovian case, the algorithm is capable of finding the analytical solution, and in the non-markovian case a good handling of the cellular growth rate can be achieved.

### Strengths
I've found the paper compelling and engaging. It is well written, goes through the necessary background effectively, has enough math to thoroughly back its claims and build the necessary background.

### Weaknesses
 - The paper mentions that a state encoding the memory is required, transforming the non-markovian dynamic into a Markovian dynamic. The usage of recurrent networks (or perhaps other models like transformers?) could be used to solve that problem without encoding for these states. I find this idea compelling. I wonder if using an RNN is enough material for a follow-up paper, even though it is crucially missing from this one. Hence, not having it within this publication could actually be detrimental for the publicity around this publication altogether.
- Only one family of RL algorithms is being used. Although the authors show that it is robust enough to discover the solution of the problem, it'd be nice to see how DQN compares to other techniques.

### Questions
- Why choose DQN and not another algorithm? SAC and others can also be trained in discrete action spaces. It would be nice to have a notion of how DQN compares to other algorithms (in supp. materials).

My main questions have to do with the feasibility of the proposed technique:
- How feasible is it to measure the cell growth periodically in real life settings? I guess one cannot grow cells very frequently and the amount of input data could limit the efficiency of the method proposed. Also, how feasible is it to provide drugs at the proposed rates, and would tighter constraints actually impact the policy much (could it be that a tight constraint on the frequency of the drug administration actually drives the policy to another local minimum?)
- I did not really understand if the plan here would be to train an algorithm offline on simulated data and test it in the real world (sim2real) or if the purpose of this method is to show on simulated data that RL can be used to solve the problem but this will require training the algorithm on real data. Or is the goal to get a standardized drug administration schedule that would fit all cases? 
- If the goal is sim2real, some evidence or a path forward to the applicability of this technique would be a nice add-on.
- If the goal is online training, one could maybe consider offline reinforcement learning to help solve this problem?
- How can one assess how good and representative the growth model is? Is there any evidence that sim2real would work?
- Alongside the previous points: is 300K steps for training realistic in real life?

### Soundness
4

### Presentation
4

### Contribution
4
