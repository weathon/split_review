# PASRL: Stabilising Reinforcement Learning with Past Action-State Representation Learning

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Although deep reinforcement learning (DRL) deals with sequential decision making problems, temporal information representation is absent from state-of-the-art actor-critic algorithms. The reliance on a single observation vector, representing information from only one time step, combined with densely connected neural networks, causes instability and oscillations in action smoothness. Therefore many applied DRL robotics control methods employ various reward shaping, low-pass filter and traditional controller-based methods to mitigate this effect. However, the interactions of these different parts hinders the performance of the original goal for the RL algorithm. In this paper we present a reinforcement learning algorithm extended with past action-state representation learning (PASRL), which allows for the end-to-end training of RL-based control methods without the need for common heuristics. PASRL is evaluated on the MuJoCo benchmark, showing smoother actions that preserve exploration, eliminate the need for extensive hyperparameter tuning, and provide a simple and efficient solution for enhancing action smoothness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper tackles the problem of action smoothness, which is especially crucial for robotic systems that are incapable of instant changes of the motor torques.
They propose augmenting the state with the prior actions, and perform an ablation to showcase the performance differences.

### Strengths
The problem itself is important. When training for real world deployment, the constraints of the real systems need to be taken into account.

### Weaknesses
I'm not sure what the authors try to convey in terms of success/failure. Their method is better at predicting smoother actions, this is not surprising. But also not surprising is the degradation in performance. This is a result of over-regularization.

Real systems don't necessarily need the "smoothest" policy possible, but rather have some constraints as to how reactive they can be. I think this work should be extended to the constrained RL setting. Providing the required smoothness parameter as a part of the optimization process.

Then, the authors can compare with prior methods with differing hyper-parameters. In the constrained RL setting, you want to show that your work is (1) easier to tune or requires no tuning, whereas other works need delicate reward design. (2) for a given constraint, out of all methods that meet the constraints, your controller reaches the best performance on the task itself.

### Questions
-

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposed a mathod, PASRL, as an extension toTD7 which address instability and oscillations in the smoothness of concurrent actions.

### Strengths
1) PASRL introduce an approach to enhance action smoothness by incorporating past state-action representations through a RNN.
2) PASRL use pink noise  rather than standard white noise.

### Weaknesses
1) the main weakness is the optimality issue. Action plays a significant role in RL (exploration). Ideally, in order to reach optimal Q value ($Q^*(s,a)$) and optimal policy ($\pi^*$), you need to visite all state action pair (s,a) since  ($Q^{\pi^*}(s,a) \geq Q^\pi(s,a)$). During training, when you smooth the action, you will take the risk of limited exploration which affect the optimality, especially in high-dimensional environments such as humanoid. The smoothing operation, by its nature, biases the policy towards a more limited set of actions, potentially preventing the agent from discovering optimal or near-optimal solutions that require more abrupt or varied control inputs. This is particularly concerning in complex environments where the optimal policy might involve a sequence of sharp, discontinuous actions.

2) Limitation: smooth action is not always best. Consider a well-known control example, racing car, the objective is only minimizing time. In this case bang-bang control is the optimal solution however it is not smooth. The paper does not adequately address scenarios where discontinuous control is necessary for optimal performance. The focus on smoothness as a universal objective overlooks the fact that many real-world control problems require sharp, rapid changes in action to achieve the desired outcome. This limitation significantly restricts the applicability of the proposed method to a subset of control tasks where smoothness is a desirable property.

3) Simulation examples are very limited only ant and hopper. The evaluation is insufficient to demonstrate the effectiveness of the proposed method across a diverse range of control problems. The choice of only two relatively simple environments raises concerns about the generalizability of the findings. The lack of experiments in more complex and challenging environments, such as those with higher degrees of freedom or more intricate dynamics, makes it difficult to assess the true potential and limitations of the approach.

### Questions
1) Auther memtioned "The reliance on ONLY the current time step information ... causes instability and oscillations", for off-policy method such as TD3 and TD7, the data comes from reply buffer can be past time step information. Can you make the point more clear?
2) For Figure 7, how can the plot has shaded area for single seed line? when you do the experiment, I assume you change the environment seed. Do you fix the random seed, torch seed and/or numpy seed?
3) For Figure 5, the red, blue, and brown line, espicially red line has lowest reward but result in the best action smoothness. Can the auther explan why the better action smoothness will hurt the reward performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new DRL method called PASRL based on TD7 method, extended with past action-state representation learning. PASRL can achieve smoother action sequences compared to existing DRL methods through end-to-end training without heuristics design. The experiment on the Ant control task demonstrates the effectiveness of the new method.

### Strengths
1. Improving action smoothness is a meaningful research topic in DRL domains, especially in continuous control tasks such as robotics control and auto driving. 
2. The key idea of the new method PASRL is easy to follow and implement.

### Weaknesses
1. More related works need to be introduced in this paper. Improving action smoothness is the key contribution of this paper, which has been widely researched recently in DRL domain. The following are some related works:

   1. LipsNet[1]: reduce action fluctuation of DRL methods in continuous control tasks through constraining the Lipschitz constant of policy networks utilizing Multi-dimensional Gradient Normalization (MGN).
   2. TAAC[2]:  introduce a switch policy to make binary choices on whether to use the current new action or the last action at each step in continuous control tasks.
   3. PIC[3]: introduce action inertia into discrete DRL methods, where the policy tends to take the same actions at the previous step.

   Please find more related works and give a more detailed description of this research filed in the manuscript.

2. The experiment is insufficient and cannot demonstrate the effectiveness of the new method:

   1. The experiment result of PASRL in the Ant environment is not satisfactory, with unignorable reward gap compared to TD7  and other baselines (Fig. 5). Although the action smoothness of PASRL is better than other methods, the sacrifice on reward performance is unacceptable in application scenarios.
   2. The experiment is only conducted in the Ant task. It is necessary to evaluate the performance of each method in more environments, such as Hopper, HalfCheetah, Humanoid, etc.
   3. More baseline methods are necessary to demonstrate the performance of PASRL. As described above, some DRL methods have been proposed to improve action smoothness, such as LipsNet, TAAC, and some regularization methods introduced in the paper (SR^2L[4], L2C2[5], etc.). Please conduct experiments with additional baseline methods to demonstrate the superior performance of PASRL compared to these existing methods.

3. The expression of this paper needs to be revised for readiability,:

   1. Add punctuations, especially commas in some sentences. This is significant to remove ambiguity and  improve readiability.
   2. Some notations and terms are used without clear definitions. For example, in line 214 section 4.2, the readers cannot find the definition of $nh_t$. Some terms including LPF and ERE are used without claiming their full names. Please revise the manuscript accordingly.
   3. Some latex typos, such as ``representational drift'' in Line 105.

### Questions
1. As shown in Fig.5,  the action smoothness results of each method during training are given. Are these results evaluated in training mode (the agent takes actions with exploration noises) or in evaluation mode (without exploration noises)? 
   Please clarify this issue in the paper, which has a significant influence on the experiment result.

### Soundness
1

### Presentation
1

### Contribution
2
