# Quality Diversity Imitation Learning

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Imitation learning (IL) has shown great potential in various applications, such as robot control. However, traditional IL methods are usually designed to learn only one specific type of behavior since demonstrations typically correspond to a single expert. In this work, we introduce the first generic framework for Quality Diversity Imitation Learning (QD-IL), which enables the agent to learn a broad range of skills from limited demonstrations. Our framework integrates the principles of quality diversity with adversarial imitation learning (AIL) methods, and can potentially improve any inverse reinforcement learning (IRL) method. Empirically, our framework significantly improves the QD performance of GAIL and VAIL on the challenging continuous control tasks derived from Mujoco environments. Moreover, our method even achieves $2 \times$ expert performance in the most challenging Humanoid environment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel Quality Diversity Imitation Learning (QD-IL) framework designed to learn a diverse set of high-performing policies based on varied but limited expert demonstrations. The proposed framework, MConbo-IRL, combines elements from standard QD algorithms, such as CMA-MEGA, and adversarial imitation learning methods such as GAIL and VAIL, and introduces two key modifications: (1) adding an extra reward term that encourages exploration of policies with diverse measures (referred to as the measure bonus), and (2) adding the single-step measure of the current state as an input to the discriminator (referred to as measure conditioning). Experimental results across several continuous control tasks demonstrate that the proposed framework outperforms the baseline (PPGA trained under a single reward function learned by GAIL/VAIL) in QD metrics.

### Strengths
1. This paper is the first to explicitly integrate standard QD algorithms with imitation learning, though it is not the first to study imitation learning methods that learns a diverse set of policies.
* (There is another paper that studies imitation learning methods in a similar setting inspired by QD algorithms, although it diverges from standard QD algorithms: N. Justesen, M. González-Duque, D. Cabarcas, J. -B. Mouret and S. Risi, "Learning a Behavioral Repertoire from Demonstrations," 2020 IEEE Conference on Games (CoG), Osaka, Japan, 2020, pp. 383-390, doi: 10.1109/CoG47356.2020.9231897.)

2. The measure bonus, designed to encourage exploration of policies with diverse measures, is straightforward and intuitively sound.

3. The effectiveness of the designed MConbo-IRL is demonstrated through empirical results on several contibuous control tasks, which show that the MConbo- version of GAIL/VAIL overall outperforms PPGA + GAIL/VAIL and sometime outperforms PPGA + true reward in terms of QD metrics, including QD-Score, Coverage, Best Reward, and Average Reward.

### Weaknesses
1. The effects of measure conditioning: While the purpose of the measure bonus is straightforward, it is less clear how the measure conditioning affects the QD-IL performance. The paper states (such as in Introduction, Section 4.2.1, Appendix E) that measure conditioning (i.e., adding the single-state measure as an input to the discriminator) "enables the agent to learn broader behavior patterns". However, this claim lacks sufficient empirical support. The ablation study on measure conditioning in Appendix E shows that it impacts QD-Score and Average Reward, but the mechanism of how it impacts the policy learning remains unclear without further analysis of the algorithm's inner components.
My confusion is as follows: if adding the single-state measure input to the discriminator improves the discriminator performance, doesn't this only makes it easier for the discriminator to distinguish policy trajectories that demonstrate single-state measures absent from expert demonstrations? It seems that this could potentially discourage the policy learning to be more diverse. Could the authors clarify if this reasoning is correct, or if measure conditioning is intended to encourage diversity policy learning in a different way?

2. In Section 5.3, the observation that MConbo-GAIL achieves much higher coverage in the Humanoid environment than the PPGA expert is attributed to the "synergy between the measure bonus and CMA-MEGA". However, there are other baselines, such as PWIL and GAIL, that also achieve much higher coverage than the PPGA expert in this environment. This suggests that other factors may contribute to coverage performance in this case.

3. The expert demonstration data contains trajectories collected from multiple experts with diverse behaviors. These experts, as optimized agents from PPGA under the true reward of the environment, each optimizes their own version of the reward function. Therefore, there is no shared reward function among them. This places the PPGA + GAIL/VAIL baseline at an intrinsic disadvantage, as it is designed to learn a single reward function. It may be worthwhile to explore additional forms of baseline methods based on standard GAIL/VAIL. For example, applying PPGA + GAIL/VAIL to create a policy archive for each demonstration expert individually, then aggregating all policy archives together, could provide another baseline.

4. The paper is not very clearly written, as it sometimes references terms (often from QD algorithms) without defining them or pointing to exact external references, making the paper less self-contained.
* For instance, the format of the policy archive and the exact procedure of archive updates, are not detailed in the paper or the pseudo-code.
* Similarly, there are other parts of the pseudo-code that are not completely defined, making it difficult to understand the exact procedure.
* What is the term $p$ in Equation 2? If $p$ is a fixed constant, can it then be ignored? If that is the case, how does the definition of measure bonus in Equation 2 differ from an indicator function (in the sense that an indicator function scaled by a value $q$ is still binary)? Are $p$ and the scaling factor hyperparameter $q$ being adjusted adaptively during the training process?

### Questions
1. Is the concept of a measure bonus constrained to QD-IL? Is there anything that would prevent adding it to QD-RL algorithms, such as PPGA, for QD-RL problems as well?
* Currently, MConbo-GAIL can outperform the PPGA expert in the Humanoid environment, even though it is trained using demonstration trajectories from experts selected from PPGA expert's archive - which is somewhat surprising. If the measure bonus were added to the PPGA expert, could this drastically improve its performance? In that case, could MConbo-GAIL still outperform it?

### Soundness
3

### Presentation
2

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
The submission combines imitation learning and quality diversity optimization to learn an archive/set of policies that all try and maximize the unknown oracle reward function of an environment. Only expert demonstrations are provided. A modified version of Proximal Policy Gradient Arborescence (PPGA) is used as the QD-RL method to get more diverse behaviors to then generate expert demonstrations and a reference archive of expert behaviors. Measure bonus and conditioning are the two main contributions to enhance existing off the shelf inverse RL algorithms to achieve better balance of exploration and exploitation and address the challenge of localized rewards.

### Strengths
- The proposed modified version of GAIL, MConbo-GAIL, addresses shortcomings of GAIL such as overfitting to demonstration specific behaviors and the inability of the discriminator to generalize to new states. The changes made are sound and help encourage the discriminator to focus on high-level more generalizable features.
- The improvements shown in table 1 and figure 6 show the impact of MConbo variations of GAIL and VAIL inverse RL methods.

### Weaknesses
- I think an ablation on the demonstrations used to verify the robustness of the proposed method could be important. It seems that a fixed set of 4 demos per environment tested are used.
- Overall I believe this paper lacks experiments investigating the method at a deeper level. There is just one ablation and then main results, however, I think it is important to understand more about several aspects including the demonstrations and perhaps how the learned behaviors might correlate with those demonstrations. E.g. a question could be "How much of the new archive is generalization beyond demonstrations?"

### Questions
- Are there any training / wall clock time numbers of the proposed method? given that a gpu sim like brax is used I think wall time may be somewhat relevant to be aware of as the purpose of GPU sim is to improve training wall time.
- How well might this method fair with sub-optimal demonstrations? Or would some form of offline RL approach now be needed?

Happy to raise score to the accept range if there is more discussion on other aspects of the proposed algorithm. I primarily feel that there are a number of aspects that should be investigated to better understand the new approach with e.g., respect to its demonstration data which often influences resulting behaviors significantly. Especially given that only 4 demonstrations are used which can be more susceptible to high variance in results.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Quality Diversity Imitation Learning (QD-IL), a method that allows policies to acquire a diverse range of skills using limited demonstrations. Quality Diversity (QD) is leveraged to explore multiple solutions to optimization problems, ensuring each solution maximizes its fitness value. The authors propose a general imitation learning framework that incorporates QD within adversarial imitation learning methods, including GAIL and VAIL. The effectiveness of QD-IL is demonstrated across three simulation tasks, showcasing its potential for learning diverse behaviors.

### Strengths
- The paper proposes the first generic QD-IL framework that integrates QD algorithms into imitation learning.
- Introducing measure bonus into GAIL and VAIL improves policy diversity while maintaining the policy’s performance. This is demonstrated using 4 QD metrics across 3 tasks.
- The paper provides ablation studies on the measure bonus which indicate the measure bonus directly encourages the exploration of new behaviors.
- The paper is well-written with the contributions explained clearly.

### Weaknesses
- The measure bonus calculation requires high-level task features design, which could be challenging for long-term and complex tasks. I would assume it always needs task-specific design.
- I can’t find the details about how the authors define the behavior spaces for the 3 tasks. Maybe I missed something, but I would appreciate it if the authors could explain more about how to implement the behavior measures in the experiments.
- The experiments do not contain tasks with manipulation. It would be great to show how the QD-IL scales to other robot manipulation tasks.
- Equation 3 lacks the explanation of $\tau^{E}$.

### Questions
Overall, I think the idea is interesting, but I am concerned about how the method can be scaled to other complex tasks. I have the following questions:

- I don’t quite understand the Figure 1(a). Can you give a simple robot example for it? Like what is the policy space here? Does it mean a different observation space or action space?
- In Figure 1(b) Multiple behavior demos, traditional behavior cloning has the mode averaging problem, but some current methods such as diffusion-based imitation learning has the ability to learn multi-modality, right?
- QD-IL relies on the definition of behavior diverse measures $m$.  In Chapter 4.2.1, it says that the measure abstracts high-level task features. Does this mean you always need to design task-specific behavior patterns in advance? I would assume this is very hard for more complex and long-term tasks.
- The experiments do not contain any manipulation tasks. Could QD-IL be adapted to complex manipulation tasks? Could the authors give a simple case for that?
- In Figure 4, what is the x and y axis?

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
3

### Summary
The paper proposes a novel framework called Quality Diversity Imitation Learning (QD-IL) designed to enable agents to learn a wide range of skills from limited demonstrations. The framework combines quality diversity (QD) optimization with adversarial imitation learning (AIL). It also introduces measure-based reward bonuses and measure conditioning. Experimental results show that QD-IL significantly outperforms traditional methods in Mujoco tasks.

### Strengths
1. The writing is clear and easy to follow.
2. The problem is well-formed and the algorithm is solid. The experimental result shows clearly the superiority of the proposed QD-IL framework.

### Weaknesses
1. Missing discussion of related works: there is a large literature regarding Multi-domain Imitation Learning [1] [2] [3], skill- or option-discovery [4] [5] [6] that deal with similar problems as stated in the paper. Namely, they are all designed to "find diverse solutions" so that the policies can represent diverse behaviors. If the setting is different, I suggest the authors be clearer on that; if not, these literature should be included in the discussion, and incorporated into the baselines (other than only GAIL and VAIL). It should also be suggested the advantage of the proposed QD-IL over other related works.

   

2. Currently, the learned diverse policies can only be read by the curves (like that in Fig.1.(a)). There lacks a formal and precise theoretical interpretation of how and why it is connected to diverse behavior patterns. How strongly does a local optimal suggest a behavior pattern and how well it is guaranteed? It would be helpful to develop more theoretical analysis in this regard.



   [1] Seyed Kamyar Seyed Ghasemipour, Shixiang Shane Gu, and Richard Zemel. Smile: Scalable meta inverse reinforcement learning through context-conditional policies. *Advances in Neural Information Processing Systems*, 32, 2019.

   [2] Lantao Yu, Tianhe Yu, Chelsea Finn, and Stefano Ermon. Meta-inverse reinforcement learning with probabilistic context variables

   [3] Jiayu Chen, Dipesh Tamboli, Tian Lan, and Vaneet Aggarwal. Multi-task Hierarchical Adversarial Inverse Reinforcement Learning. In *Proceedings of the 40th International Conference on Machine Learning*, pages 4895–4920. PMLR, July 2023.

   [4] Jesse Zhang, Karl Pertsch, Jiefan Yang, and Joseph J Lim. Minimum description length skills for accelerated reinforcement learning. In *Self-Supervision for Reinforcement Learning Workshop-ICLR*, volume 2021, 2021.

   [5] Thomas Kipf, Yujia Li, Hanjun Dai, Vinicius Zambaldi, Alvaro Sanchez-Gonzalez, Edward Grefenstette, Pushmeet Kohli, and Peter Battaglia. CompILE: Compositional Imitation Learning and Execution, May 2019.

   [6] Yiding Jiang, Evan Zheran Liu, Benjamin Eysenbach, J Zico Kolter, and Chelsea Finn. Learning Options via Compression.

### Questions
1. How sensitive is QD-IL to the choice of hyperparameters? It would be helpful to have a robustness/sensitivity test.
2. Can the framework be adapted to domains with high-dimensional input data, other than the three environments stated in the paper? It is also questionable to say that the "most challenging" humanoid environment, since a pixel-based input environment like Atari is clearly more challenging. It would be helpful to make it clearer.
3. Could the author give more analysis on the learned behavior patterns? Do they really correspond to "skills" in the semantic level? E.g. moving left leg, moving right leg, etc. It should be more convincing if these diversified policies can be visualized and validated as different behavior patterns for better interpretability.

### Soundness
3

### Presentation
3

### Contribution
2
