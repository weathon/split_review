# AsymDreamer: Safe Reinforcement Learning From Pixels with Privileged World Models

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Safe Reinforcement Learning from partial observations frequently struggles with rapid performance degradation and often fails to satisfy safety constraints. Upon deeper analysis, we attribute this problem to the lack of necessary information in partial observations and inadequate sample efficiency. World Models can help mitigate this issue, as they offer high sample efficiency and the capacity to memorize historical information. In this work, we introduce AsymDreamer, an approach based on the Dreamer framework that specializes in exploiting low-dimensional privileged information to build world models, thereby enhancing the prediction capability of critics. To ensure safety, we employ the Lagrangian method to incorporate safety constraints. Additionally, we formulate our approach as an Asymmetric CPOMDPs (ACPOMDPs) framework and analyze its superiority compared to the standard CPOMDP framework. Various experiments conducted on the Safety-Gymnasium benchmark demonstrate that our approach outperforms existing approaches dramatically in terms of performance and safety.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents AsymDreamer, an approach based on the Dreamer framework that specializes in exploiting low-dimensional privileged information to build world models, thereby enhancing the prediction capability of critics. AsymDreamer employs the Lagrangian method to incorporate safety constraints. This paper formulates the proposed approach as an Asymmetric CPOMDPs (ACPOMDPs) framework. Experiments on the Safety-Gymnasium benchmark demonstrate that AsymDreamer outperforms existing approaches in both performance and safety.

### Strengths
- The paper is well-motivated and novel. It successfully extends the Dreamer framework to handle asymmetric information in RL, presenting a novel ACPOMDP framework. It shows the effectiveness of using privileged Information.
- The results from Safety-Gymnasium benchmarks show that AsymDreamer outperforms baseline models in both task performance and safety metrics, especially in complex scenarios like 3D navigation. The thorough ablation studies are also conducted.
- The paper includes rigorous theoretical analysis and compares ACPOMDP to standard CPOMDP.

### Weaknesses
I am not in this field so I am unable to evaluate the signficance of the proposed method and ACPOMDP problem/analysis.

Some of my concerns include:
- Over-reliance on privileged information:  AsymDreamer’s performance relies on privileged information during training, which may not be available or hard to simualte in real-world environments. It potentially leads to bad performance or compromised safety in environments with limited or unavailable privileged information.

- Extension to real-world environments:  The experiments on Safety-Gymnasium benchmark are a bit toyish (even the most challenging 3D navigation one, although it may also be the cases for the related work). Additional testing in real-world environments would be beneficial to demonstrate the effectiveness.

### Questions
I am not familar with this field at all and I cannot evaluate the novelty of this work (especially over its predecessor / related works). It is an interesting read and I didn't identify significant issues. The paper is well motivated with solid analysis and experiments. My major concern is that this paper only evaluates on toyish environments and may not generalize well to real-world scenarios.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose AsymDreamer, a Dreamer-based safe reinforcement learning framework that utilizes low-dimensional privileged information to construct world models. The world model in AsymDreamer features two branches: the Privileged World Model, which takes a handcrafted low-dimensional vector as input, and the Observation World Model, which uses partially observed images (64x64 RGB). Additionally, the authors formulate their approach within the framework of Asymmetric CPOMDPs (ACPOMDPs) and integrate AsymDreamer with the Lagrangian method. Empirical results show that AsymDreamer outperforms existing safe reinforcement learning methods on the Safety-Gymnasium benchmark.

### Strengths
1. The theoretical analysis of ACPOMDPs in this paper is comprehensive. The authors propose the ACPOMDPs framework and provide a detailed analysis showing that asymmetric inputs reduce the number of critic updates and lead to a more optimal policy compared to the standard CPOMDPs framework.
2. The authors introduce privileged information into the RSSM world model, enhancing the model's imaging capabilities and consequently improving the performance of the safe policy.

### Weaknesses
1. The methodology in this paper is too similar to prior work[1], and lacks sufficient novelty. In my view, the only difference is the inclusion of privileged information in the modeling of the RSSM world model.
2. The authors are encouraged to include an ablation study to analyze the impact of adding privileged information to the observation input on the baseline algorithm.
3. There are some typos in the paper that need to be corrected in the next version (e.g., line 400 and figure 2).

### Questions
1. Please clarify the similarities and differences between the proposed method and SafeDreamer[1].
2. The reviewer is confused about what the global state in your privileged world model input is and where the privileged information (the low-dimensional vector from Appendix E) is used.

[1] Huang, Weidong, et al. "Safe dreamerv3: Safe reinforcement learning with world models." arXiv preprint arXiv:2307.07176 (2023).

### Soundness
2

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
4

### Summary
This paper focuses on the safe RL problem that struggles with performance degradation and often fails to satisfy safety constraints. They attribute this problem to the lack of necessary information in partial observations and inadequate sample efficiency. Specifically, they exploit low-dimensional privileged information to build world models, thereby enhancing the prediction capability of critics. The authors propose Asymmetric Constrained Partially Observable Markov Decision Processes, a relaxed variant of CPOMDPs. The key distinction is that ACPOMDPs assume the availability of the underlying states when computing the long-term expected values. To ensure safety, they employ the Lagrangian method to incorporate safety constraints. The experiments conducted on the SafetyGymnasium benchmark demonstrate that the proposed approach outperforms existing approaches dramatically in terms of performance and safety.

### Strengths
1.	The idea of using privileged information in the Dreamer structure is interesting. Separating observation modeling and task-centric prediction modeling avoids the potential trade-off between these two tasks. This also allows the observation world model to capture more detailed observation information, thus enabling the actor model to achieve better performance with richer input features.
2.	The paper is generally well-written and well-organized. Figure 1 clearly shows the training pipeline.

### Weaknesses
1.	**Justification of using privileged information**. It seems that the motivation for using privileged information is this sentence “Since training is often conducted in simulators, there is potential to leverage privileged information during training to reduce uncertainty from partial observations”. Does the proposed method have potential applications beyond simulations, such as in real-world scenarios? The paper should discuss the sim-to-real transfer challenges and how the privileged information would be obtained in real-world settings. Furthermore, it is not clear if the performance gains are solely due to the privileged information or if the proposed architecture also contributes. It is also not clear if it is fair to compare with other methods that do not use privileged information.
2.	**Evaluation results**. The experimental evaluation is only conducted on 4 tasks, including one self-made task. The authors may need to include all the remaining tasks in the Safety Gymnasium to ensure the generalizability of the proposed method. The current selection of tasks may not be representative of the broader challenges in safe RL.
3.	**Missing baseline on the same benchmark** Although this paper proposes a model-based method, I think it is still meaningful to compare with some well-known methods on the same benchmark. This website contains some results that can be used as reference: https://fsrl.readthedocs.io/en/latest/tutorials/benchmark.html. A comparison with model-free methods would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach.
4.	There is no clear evidence to show the benefit of using privileged information. The results in Figure 5 need more investigation and explanation. Specifically, the failure of the privileged world model to train a viable cost predictor is concerning and requires further analysis. Additionally, the superior performance of DreamerV3 compared to AsymDreamer(S) in terms of reward is counterintuitive and needs a more thorough explanation. Without this, it is hard to summarize the main conclusion of the proposed method.

### Questions
1.	I think in Figure 1, the encoder, decoder, and hidden state are different for the two world models. So, it would be clearer to use different colors of notations for them to avoid confusion.
2.	Why not use SafeDreamer as a baseline?
3.	In Figure 4, why do all baselines have constant cost? Don’t they vary across training steps? What is the target cost limit?
4.	What does the red solid line mean in Figure 4 and Figure 5?
5.	There is no explanation of the baselines. What does OSRP mean? It would be better to include simple descriptions of each baselines in the appendix.
6.	The ablation study results in Figure 5 raise a lot of questions. I think the authors also feel surprised that the privileged world model fails to train a viable cost predictor when taking privileged information as input. In addition, DreamerV3 is much better than AsymDreamer(S) in terms of the reward. This is also hard to interpret. I think the authors should do more experiments to explain these results to provide insights into the model. Otherwise, there seems no clear message that can be summarized in this paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors address the challenge of exploiting asymmetric inputs under the CPOMDPs framework. They propose AsymDreamer, a new algorithm that uses privileged information to build a world model for the critic. They also introduce the ACPOMDPs framework, an extension of CPOMDPs allowing asymmetric inputs for the actor and critic. Theoretically, asymmetric inputs reduce critic updates and lead to a better policy. AsymDreamer constructs two world models, one for the actor based on historical information and another for the critic with privileged information. It is integrated with the Lagrangian method and shows competitive performance on the Safety-Gymnasium benchmark and strong adaptability to complex scenarios.

### Strengths
* The proposed method of combining DreamerV3 with two world models and Lagrangian methods, which is novel and well-motivated.
* The paper presents empirical results that compare AsymDreamer with many relevant model-based and model-free baselines in several tasks, achieving competitive performance on the Safety-Gymnasium benchmark.
* The paper is mostly well-written.

### Weaknesses
 * The work is built on top of SafeDreamer, incrementally adding another world model for critic, and differences in terms of the loss optimized are not sufficiently highlighted. Specifically, the paper does not clearly articulate how the loss functions for the actor's world model and the critic's privileged world model differ, and how these differences impact learning dynamics. The paper should explicitly detail the specific loss terms used for each model and justify the design choices.
* The DreamerV3 is basically combinations of existing methods like CPOMDPs, Augmented Lagrangian, and RSSM. While this is not a problem in itself as they are common in model-based reinforcement learning, there is very little discussion on why these particular methods were chosen and what possible alternatives from the literature exist and whether they might yield better results. For instance, the paper could discuss the potential benefits of using alternative world model architectures or different constraint optimization techniques.
* Lack of introduction to baseline algorithms. And in the PointGoal2 scenario, the performance results seem to be different from SafeDreamer reported in the paper. The paper should provide a brief overview of each baseline algorithm used for comparison, highlighting their key characteristics and differences. The discrepancy in performance results for the PointGoal2 scenario needs to be addressed with a more detailed explanation of the experimental setup and any potential differences from the original SafeDreamer implementation.
* Stability verification needs to be considered. How the hyperparameters in equation (8), (9) are selected, and certain ablation experiments need to be conducted. The paper lacks a discussion on the sensitivity of the algorithm to the hyperparameters in the Lagrangian method, specifically the penalty coefficients. Ablation studies should be performed to analyze the impact of these hyperparameters on the stability and performance of the algorithm.
* Whether modeling two world models will lead to a significant increase in learning time and the effectiveness of model learning also need to be considered. The paper should include a quantitative analysis of the computational overhead introduced by the second world model, including the increase in training time and memory requirements. Furthermore, the paper should analyze the impact of the second world model on the convergence speed and overall learning efficiency.
* Privileged information and partial observations should be considered in more environments. A single scenario in QuadrotorGoal1 cannot be trusted to determine whether privileged information enhances performance. The paper should evaluate the proposed method in a more diverse set of environments, including those with varying degrees of partial observability and different types of privileged information, to demonstrate the generalizability of the approach.

### Questions
It would be great if the authors could address the weaknesses I outlined above.

### Soundness
3

### Presentation
3

### Contribution
2
