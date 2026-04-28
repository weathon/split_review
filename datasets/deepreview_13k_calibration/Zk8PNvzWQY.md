# Penalizing Infeasible Actions and Reward Scaling in Reinforcement Learning with Offline Data

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Reinforcement learning with offline data often suffers from Q-value extrapolation errors due to limited data, which poses significant challenges and limits overall performance. Existing methods such as layer normalization and reward relabeling have shown promise in addressing these errors and achieving empirical improvements. In this paper, we extend these approaches by introducing reward scaling with layer normalization (RS-LN) to further mitigate extrapolation errors and enhance performance. Furthermore, based on the insight that Q-values should be lower for infeasible action spaces—where neural networks might otherwise extrapolate into undesirable regions—we propose a penalization mechanism for infeasible actions (PA). By combining RS-LN and PA, we develop a new algorithm called PARS. We evaluate PARS on a range of tasks, demonstrating superior performance compared to state-of-the-art algorithms in both offline training and online fine-tuning across the D4RL benchmark, with notable success in the challenging AntMaze Ultra task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the PARS algorithm, which aims to address Q-value extrapolation errors prevalent in offline reinforcement learning (RL). The authors propose a twofold approach combining (1) Reward Scaling with Layer Normalization (RS-LN) and (2) Penalizing Infeasible Actions (PA). The former stabilizes the Q-function learning by scaling rewards while employing layer normalization to manage output variances effectively. The latter penalizes Q-values for infeasible action regions to prevent overestimation outside the feasible data coverage. The paper shows that PARS, built upon the minimalist TD3+BC algorithm, outperforms existing state-of-the-art (SOTA) methods in offline, and offline-to-online setups, particularly in the challenging AntMaze environment.

### Strengths
- The paper demonstrates the effectiveness of the proposed PARS method through comprehensive empirical results across various domains, showing that it outperforms or matches strong baselines. 
- The method’s simplicity and minimal code changes required for implementation make it attractive for practitioners looking to enhance existing RL models without significant overhead.
- The paper is well-written, with clear visualizations that effectively convey the concepts and intuitions behind the approach. This aids in understanding the methodology and its application.

### Weaknesses
 - The way infeasible regions and reward scaling are defined—through arbitrary thresholds without adaptive or data-driven characterization—limits the method's novelty.
- While the paper mentions following prior work for hyperparameter tuning, the strategy of tuning hyperparameters with online interactions contadicts offline RL, which undermines the problem’s nature. Using Off-Policy Evaluation methods for hyperparameter selection, or fixing a set of hyperparameters for each environment would be better aligned with Offline RL.
- The paper does not discuss offline RL methods that do not query out-of-distribution (OOD) actions, such as SQL [1] , XQL [2],  and IQL. and how PARS ideas can be leveraged by those.

### Questions
- Please check weaknesses.
- How do you define the feasible boundary for the action space in your method? Specifically, what do  l_i  and  u_i  represent? Are they derived as the minimum and maximum a_i within the dataset?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper incorporates reward scaling with layer normalization and infeasible action penalization into existing offline reinforcement learning algorithms, specifically TBC+BC with critic ensemble, to enhance their performance. The proposed method is evaluated on various offline and offline-to-online benchmarks and compared with several baseline methods. The results show that the proposed method outperforms the baseline methods on the chosen tasks.

### Strengths
- The presentation is clear and easy to follow.
- The proposed method is incremental but appears effective.
- The experimental evaluation is thorough and covers a wide range of tasks.

### Weaknesses
 - The presentation is clear and easy to follow.
- The proposed method is incremental but appears effective.
- The experimental evaluation is thorough and covers a wide range of tasks.

 - The motivation for penalizing infeasible actions is not clear. As shown in Figure 2(c) and (d), it seems penalizing OOD actions within the feasible region will lead to the same optimal policy (e.g., argmax Q) as RS-LN and PA. In this case, the proposed method is equivalent to RS-LN and PA, though the absolute Q values are different. The paper needs to provide a more rigorous justification for why penalizing OOD actions within the feasible region is necessary, especially given that the argmax Q policy would remain the same.

- Section 3 criticizes that using a critic ensemble significantly increases the training complexity. However, the proposed method also uses a critic ensemble (4 for AntMaze, 10 for MuJoCo and Adroit), which undermines the advantage of the proposed method and makes its motivation less convincing. A comprehensive comparison of the proposed method without a critic ensemble against other baseline methods would be helpful to clarify the contribution of the proposed method. It is crucial to isolate the effect of the proposed method from the critic ensemble to understand its true contribution.

- Some of the results are not consistent with the claims in the paper. Please see the questions section for details.

### Questions
- Figure 3 shows results from a single seed on the toy example. Is this conclusion consistent when using different seeds? Will the shape worsen or converge to a pattern when the reward scaling factor is larger?
- Line 231 states, 'This regulated reduction in Srank prevents overfitting by minimizing the learning of irrelevant noise'. How can this conclusion be drawn from the results?
- Figure 7 shows that a larger reward scaling factor leads to better performance. Is this a general conclusion for other tasks? Is there any limitations about the reward scaling factor?
- Line 270 states, 'the performance does not heavily depend on the values of U when these values are set as 100 to 1000 times the boundary of the feasible region'. However, the results in Figure 7 show that performance decreases when U is large on 3 out of 4 tasks. Can you clarify this inconsistency?
- See Weaknesses.

I am willing to increase my score if all my concerns are addressed.

### Soundness
2

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
4

### Summary
This paper uses reward scaling and penalizing techniques for offline RL. The proposed method is not novel but effective. Experiments show the advantages of the proposed method.

### Strengths
The writing of the paper is very clear and easy to follow.

The idea of the paper makes sense and is intuitive. The idea of imposing penalizing infeasible actions is simple but effective. It does not need additional efforts to train a model to classify the OOD and ID.

The experiments of the paper are sufficient and valid.

### Weaknesses
The proposed method is very simple (which can also be regarded as an advantage). It is unclear to me why the layer normalization and reward scaling can mitigate OOD overestimation. The paper could elaborate more insight on this. Specifically, while the didactic example in Section 4.1 is helpful, it does not provide a mechanistic explanation of how the combination of reward scaling and layer normalization leads to the observed reduction in OOD Q-values. The paper lacks a theoretical justification for why this approach is effective, relying primarily on empirical observations. More analysis and discussion would be beneficial to understand the underlying principles.

Missing Ablation studies:

- The paper can also compare with method that use a behavior model to classify the ID and OOD. Could the PA also show benefits over that?


Minor comments:

- Line 019: lower than what?
- Line $s_t,a_t$ should be defined before using them,.
- Line 089: the returns should be expected returns.p

### Questions
Regarding the Didactic example in Sec 4.1:

- The examples are all positive. What happens if the values are negative? By the way, what is the sign of the reward in the practical environments used in the paper?
- It seems from both Figure 3 and the experimental results, with LN, larger $c_{\text{reward}}$ always leads to better results. Could you elaborate on the reason? And is it correct that we can choose a larger $c$?

Would the method and the main result also work and hold for a discrete action space?

The proposed method shows large improvements on AntMaze? Could the author elaborate more on these results?

I don't really understand why $L_I = U_I$ in Line 501. Why are they equal?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors present a concise yet effective algorithm called PARS, which introduces Reward Scaling combined with Layer Normalization (RS-LN) to mitigate extrapolation errors and enhance the offline and offline-to-online performance. The **experimental results** are particularly **impressive**.

However, I have some questions: 1) How does PARS differ from other related algorithms? Such as [1] 2) Could the authors clarify how the algorithm's design specifically contributes to its performance advantage? (see question section)

If you can given clarification, I think this paper will be much more comprehensive.

### Strengths
The advantages of PARS are primarily reflected in two key aspects:

- PARS is a straightforward approach that integrates Layer Normalization and reward scaling with TD3+BC, making it easy to implement.

- PARS demonstrates strong performance across both offline and offline-to-online tasks from a variety of domains, including Androids, Mujoco, and Antmaze, making it highly scalable and showcasing competitive experimental results.

### Weaknesses
The experimental performance of PARS is impressive. However, the authors do not thoroughly discuss the relationship between the performance improvements and the algorithm's design. Additionally, it is necessary to provide clearer distinctions between PARS and similar algorithms, such as [1], as mentioned in the questions section. Specifically, please see the **question section**.

Specifically, the paper lacks a detailed analysis of how the combination of reward scaling and layer normalization (RS-LN) contributes to the observed performance gains, particularly in the context of offline-to-online transfer. While the results are strong, the underlying mechanisms that lead to these improvements are not sufficiently explored. The paper would benefit from a more in-depth discussion of why the proposed method is effective, beyond simply stating that it works well. The connection between the mode-seeking and mode-covering properties of TD3+BC and the proposed solution is also not clearly established, making it difficult to understand the synergistic effects of these components.

Furthermore, the paper does not sufficiently address the potential limitations of the proposed method. For example, while the authors demonstrate the effectiveness of RS-LN in conjunction with TD3+BC, they do not fully explore its applicability to other offline RL algorithms, especially those that do not rely on policy constraints. The analysis of RS-LN's theoretical properties, particularly in the context of in-sample learning-based approaches, is also missing, which limits the understanding of its generalizability and scalability. The paper also needs to clarify the specific advantages of the proposed layer normalization compared to that in [1], and demonstrate its advantages over other offline-to-online algorithms, such as [1], Cal-QL, RLPD, and PEX.

### Questions
**Q.1** Please clarify the advantages of your research's LN compared to that in [1] ? And could you demonstrate your methods' advantage over other offline-to-online algorithms? Such as [1], Cal-QL, RLPD, PEX.

**Q.2** Subsequently, please clarify why your algorithm performs better in online fine-tuning. 

Cal-QL [2] suggests that value misalignment in both offline and online settings may be a reason for poor performance during online fine-tuning. If you chose to utilize layer-normalization, it implies that your algorithm may learn more conservative Q-values, potentially leading to a more conservative performance during online fine-tuning. However, the algorithm in [1] improves upon soft-actor-critic (SAC) during online fine-tuning, where maximizing entropy encourages the agent to explore more diverse samples, thus alleviating the conservatism inherited from the offline stages. 

Meanwhile, I can give you some related studies for reference. Recent research has shown that appropriately incorporating BC terms during the online process may enhance online performance [3]. Could you please give much more analytical explanation such as [3], at the very least about the potential reasons, thank you.

**Q.3** Please clarify the innovations of your algorithm compared to [1]. Specifically, is the improvement in your algorithm mainly due to the combined use of reward re-scaling and layer normalization (LN), or is it due to the combined use of TD3-BC, and the reward scaling algorithm? Thank you.

*If TD3+BC is not the majority reason for PARS' high efficiency, please answer **Q.4***, otherwise, you shouldn't have to answer **Q.4**

**Q.4** Could you please conduct additional experiments to verify the extensibility of PARS. For instance, you could replace TD3+BC with other methods, especially algorithms beyond policy constraints, such as CQL/IQL etc.

# Reference

[1]Philip J. Ball, Laura Smith, Ilya Kostrikov, Sergey Levine, Efficient Online Reinforcement Learning with Offline Data.

[2] Mitsuhiko Nakamoto, Yuexiang Zhai, Anikait Singh, Max Sobol Mark, Yi Ma, Chelsea Finn, Aviral Kumar, Sergey Levine, Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning

[3] Seohong Park, Kevin Frans, Sergey Levine, Aviral Kumar. Is Value Learning Really the Main Bottleneck in Offline RL?

### Soundness
3

### Presentation
3

### Contribution
2
