# FOSP: Fine-tuning Offline Safe Policy through World Models

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Model-based Reinforcement Learning (RL) has shown its high training efficiency and capability of handling high-dimensional tasks. Regarding safety issues, safe model-based RL can achieve nearly zero-cost performance and effectively manage the trade-off between performance and safety. Nevertheless, prior works still pose safety challenges due to the online exploration in real-world deployment. To address this, some offline RL methods have emerged as solutions, which learn from a static dataset in a safe way by avoiding interactions with the environment. 
    In this paper, we aim to further enhance safety during the deployment stage for vision-based robotic tasks by fine-tuning an offline-trained policy. We incorporate in-sample optimization, model-based policy expansion, and reachability guidance to construct a safe offline-to-online framework. Moreover, our method proves to improve the generalization of offline policy in unseen safety-constrained scenarios. Finally, the efficiency of our method is validated on simulation benchmarks with five vision-only tasks and a real robot by solving some deployment problems using limited data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents FOSP, a novel safe reinforcement learning method. FOSP primarily addresses the issue of enhancing safety through offline training and online fine-tuning. Its main contributions include:

1. The introduction of an offline-to-online reinforcement learning framework.
2. Enhanced safety and performance balance during visual tasks through the integration of offline and online phases.
3. In real-world deployments, FOSP allows safe fine-tuning in unseen safety constraint scenarios.
4. The experiments validate the method's effectiveness in both simulated and real robotic tasks and demonstrate its safe generalization ability in new scenarios.

### Strengths
1. The FOSP method introduces the concept of safe generalization within the offline-to-online reinforcement learning framework, combining world models with offline training and online fine-tuning to enhance safety and performance. This novel strategy for applying reinforcement learning in safety-critical scenarios is insightful.
2. The design of experiments is comprehensive while covering tasks in both simulated environments and validations in real robotic settings.
3. The experiments of FOSP in real robotic tasks demonstrate real-world value and safe generalization in unseen scenarios.
4. The paper clearly articulates the optimization objectives at each stage, aiding in understanding.

### Weaknesses
1. While the experiments were validated in Safety-Gymnasium and real robotic environments, the number and complexity of tasks remain relatively limited. Specifically, the real-world robotic tasks, while valuable, are confined to relatively simple manipulation scenarios. The evaluation does not explore more complex, multi-stage tasks that would more thoroughly test the method's ability to generalize safely. For example, tasks involving dynamic obstacles or more intricate manipulation sequences are absent, limiting the assessment of FOSP's robustness in realistic settings.

2. The motivation for introducing the new offline to online setting in the paper has not been well communicated. The paper does not clearly articulate why a standard offline RL approach is insufficient for the stated goals, nor does it fully explain the specific advantages of the proposed offline-to-online transition. The reader is left to infer the necessity of this framework, rather than having it explicitly justified with concrete examples of where a purely offline approach would fail.

### Questions
1. Although this method performs better than others, it also introduces a new design for online to offline transitions. What specific problem is this design intended to address? The reviewer hopes the authors can clarify the benefits of this setting. For instance, the reviewer notes that in Table 1, the performance of SafeDreamer (offline) is actually comparable to that of FOSP.
2. How is safety ensured in this method, particularly when dealing with unseen data and new environments? Specifically, how does the online fine-tuning process avoid safety hazards? For instance, how does the constraint violation during online fine-tuning compare to the converged offline policy?
3. The reachability estimation function is a key component of this paper. How is the feasible part determined through $ S_f(\boldsymbol{s}):=\{\boldsymbol{s}|V_\varphi^c(\boldsymbol{s})=0\} $? In particular, how does this hold when $ V_{\varphi}^c(\boldsymbol{s})=0 $ may not strictly hold in the fitted value function? 
4. How do the authors view the potential of this method for safe sim2real applications? That is, training under simulated environment data while ensuring safety and improving performance during real-world deployment.
5. The safety policy expansion mechanism stabilizes performance during the initial fine-tuning phase, but does it impose limitations on long-term fine-tuning? For example, what would the comparison of results be between the FOSP(online) version and FOSP in short-term versus long-term training?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a model-based offline-to-online safe RL algorithm, FOSP. The proposed framework first uses an offline dataset to learn a world model and a pre-trained policy. The pre-trained policy is then fine-tuned through online safe RL fine-tuning. The effectiveness of FOSP is demonstrated through experiments in the Safety gym and a real-world robot experiment.

### Strengths
Extensive experiments and ablation studies were conducted, including a real-world robot experiment with high-dimensional visual observations. The proposed FOSP algorithm achieved good performance, especially in the real-world robot experiments, and outperformed baseline approaches.

### Weaknesses
While the proposed algorithm performed well in extensive experiments, I found it hard to appreciate its technical contributions due to its complex algorithm design (e.g., many moving parts, iterations between offline and online learning) and confusing presentation. It is unclear to me if all the design choices are necessary and which components are novel or come from the literature. It would be good if the authors could clearly state their technical contributions and novelty (e.g., does the novelty mainly lie in a new combination of existing components in the literature?). It would also help if the authors could provide more insights on why FOSP would outperform baseline approaches, especially SafeDreamer.

1. Where does the behavior policy $\pi_b$ in Sec. 4.2 come from? Does it refer to the offline RL policy from Sec. 4.1?
2. Does the training step in Sec. 4.2 also occur offline? Why is it necessary to divide the offline learning stage into two steps?
3. The derivation in Sec. 4.2 is very hard to follow. What is the advantage of using the reachability estimation function from RESPO? It would be helpful to introduce RESPO in the Preliminaries Section. Is $1(s\in S_f)$ equivalent to $u^\pi(s)$? How is Eqn (14) derived from Eqn (13)? Why would introducing advantage functions simplify the constraints?
4. The limitation and future work section should be moved to the main text.

### Questions
1. Where does the behavior policy $\pi_b$ in Sec. 4.2 come from? Does it refer to the offline RL policy from Sec. 4.1?
2. Does the training step in Sec. 4.2 also occur offline? Why is it necessary to divide the offline learning stage into two steps?
3. The derivation in Sec. 4.2 is very hard to follow. What is the advantage of using the reachability estimation function from RESPO? It would be helpful to introduce RESPO in the Preliminaries Section. Is $1(s\in S_f)$ equivalent to $u^\pi(s)$? How is Eqn (14) derived from Eqn (13)? Why would introducing advantage functions simplify the constraints? 
4. The limitation and future work section should be moved to the main text.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed an offline-online safe RL framework based on safedreamer, integrating the concepts from RecoverRL. When feasible, the method optimizes rewards, and when infeasible, it focuses on cost optimization. Additionally, the reachability estimation function from RESPO is utilized to introduce cost into the optimization process. To mitigate the issue of inaccurate critic estimates during offline training, in-sample actions from Implicit Q-learning are employed in the Q function learning.

### Strengths
1. The proposed safe model-based RL framework effectively addresses offline-online generalization tasks.
2. It demonstrates the capability to safely fine-tune in previously unseen safety-constrained scenarios during real-world deployment.

### Weaknesses
1. In Figure 4, the results for DreamerV3 could be omitted, as they overshadow the cost performance of all baseline methods.
2. There are too few obstacles in the real-world environment, making it difficult to assess the agent's obstacle avoidance behavior. And the website does not provide any differences between the proposed algorithm and the baseline in the video demos.
3. In Figure 4, why do the rewards for FOSP in PointGoal2 and PointGoal1 not continue to rise? Additionally, SafeDreamer does not show an increase in reward for PointButton1. Does this indicate that the fine-tuning phase was ineffective? According to the paper's description, the offline data comprises a mixture of unsafe, safe, and random policies; thus, the policy trained on offline data should not be optimal, and performance should improve during the online fine-tuning phase.



### Questions
1. I'm curious about the video demonstration of the performances of SafeDreamer and FOSP in the SafetyFadingEasy and Hard environments. Based on the experimental results you presented, FOSP seems to perform better than SafeDreamer. This environment tests the agent's memory, yet it appears that FOSP does not specifically address this aspect. What accounts for the performance improvement?
2. Why do you need to learn Q(s, a) when I recall that DreamerV3 only uses V(s)?
3. How did you adapt Recovery RL to the image-based setting, and how did you modify SafeDreamer to the offline setting?

### Soundness
3

### Presentation
2

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
This paper studies the problem of offline-to-online finetuning of learned policies with safety constraints. This is, to my knowledge, the first work to study policy safety in this setting; prior work either focus on either offline or online RL exclusively. The key contribution of this paper is an algorithm, FOSP, that builds upon model-based RL algorithm Dreamer to enable fast and safe offline-to-online finetuning on tasks with visual observations, both in simulation and on a real robot. The algorithm works by first pretraining a world model on an offline dataset (using the in-sample trick from IQL), and then finetuning the model during the online phase using safe policy expansion to minimize safety violations. Experimental results indicate that FOSP is effective at reducing constraint violations while maintaining reasonably good task performance (i.e. rewards) compared to prior methods for safe RL. Vanilla Dreamer without regards for safety achieves consistently high reward (more than any other approach) but has significant safety violation.

### Strengths
- The paper studies an interesting problem (offline-to-online safe RL) that to my knowledge has not been explored much (if at all) by prior work. I appreciate the substantial background and derivation of approach which will help readers appreciate the technical contributions more. I believe that there is adequate discussion of related work.
- The paper is generally well written and easy to follow. The paper has minor grammatical errors but they do not detract significantly from my understanding.
- The resulting algorithm appears to rather practical, and can be applied to tasks with visual observations in both simulation and on a real robot. A significant amount of prior work in safe RL does not consider visual observations nor real robot experiments.
- Baseline methods appear to be quite strong. I appreciate including vanilla Dreamer for comparison (it can be considered an ~upper bound in terms of task performance with no regard to safety), as well as SafeDreamer as a recent and highly related method.

### Weaknesses
 - The considered tasks are fairly toy. It would be useful to know how the method performs on more realistic problem settings. I believe that the real-world task is a nice step in that direction, but being simply a reaching task it does not have any of the additional complexity that usually comes with real-world tasks: object interaction, real-time control, dynamic tasks (environment might change even with an all-zero action step). Especially the latter two can have significant safety consequences.
- A substantial limitation of the method appears to be the lack of control or predictability in how safe the model really is during finetuning / at test-time when presented with OOD data, e.g. novel visual observations beyond scene re-configurations. I did not find any significant discussion of this in the paper, so it would be useful to clarify (verbally or with empirical evidence) when the proposed method can be expected to succeed / fail in a transfer setting; see my question below for more context.

### Questions
I would appreciate if the authors can address (in whichever way they deem appropriate) my comments in the "weaknesses" section above, as well the following questions:

- How would the proposed method behave in a transfer task setting where the change is more visual in nature? E.g. the target object is now green and the obstacles are now red. I suspect that such novel settings would trick the method into substantial safety violations. It would be informative to either include experimental results or a written discussion on the types of transfer settings in which the method can be expected to maintain low safety violations.
- Do the authors plan to release code that reproduces their main experimental results? I did not find any mention of that in the paper.

### Soundness
3

### Presentation
2

### Contribution
3
