# Towards Reliable Offline Reinforcement Learning via Lyapunov Uncertainty Control

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
Learning trustworthy and reliable offline policies presents significant challenges due to the inherent uncertainty in pre-collected datasets. In this paper, we propose a novel offline reinforcement learning method to tackle this issue. Inspired by the concepts of Lyapunov stability and control-invariant sets from control theory, the central idea is to introduce a restricted state space for the agent to operate within. This approach allows the learned models to exhibit reduced Bellman uncertainty and make reliable decisions. To achieve this, we regulate the expected Bellman uncertainty associated with the new policy, ensuring that its growth trend in subsequent states remains within acceptable limits. The resulting method, termed Lyapunov Uncertainty Control (LUC), is shown to guarantee that the agent remains within a low-uncertainty state enclosure throughout its entire trajectory. 
Furthermore, we perform extensive theoretical and experimental analysis to showcase the effectiveness and feasibility of the proposed LUC.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to bring the concept of Lyapunov control into offline reinforcement learning. In particular, they aim to tackle the problem of partial data coverage which is very well studied, both theoretically and empirically, in the literature of offline reinforcement learning. The problem of partial data coverage is subsumed under *distributional shift* problem which is a general problem that can be encountered in any learning problem with a fixed dataset, e.g., regression problem, classification problem.

The authors propose a Lyapunov-inspired pessimistic value which also draws inspiration from the work [1]. Some theoretical analysis is provided. In addition, the proposed method is tested empirically on classical MuJoCo tasks.

[1]Ying Jin, Zhuoran Yang, and Zhaoran Wang. Is pessimism provably efficient for offline rl? In
Marina Meila and Tong Zhang (eds.), Proceedings of the 38th International Conference on Machine Learning, ICML 2021, 18-24 July 2021, Virtual Event, volume 139 of Proceedings of Machine Learning Research, pp. 5084–5096. PMLR, 2021

### Strengths
1. The structure of the paper is clear.

### Weaknesses
1. The contribution is very limited. This is mainly due to the fact the problem formulation in this paper is very partial compared to the current landscape of the offline reinforcement learning.
2. The theoretical results presented in the paper are hard to interpret and compare. The connection between the theoretical results and the practical algorithm is not clearly established. The assumptions made in the theoretical analysis are not well-motivated, and their implications for the practical performance of the algorithm are not discussed.
3. The empirical results are not adequate. There are many important benchmarks are left out. The choice of baselines is also questionable, as several relevant and state-of-the-art offline RL algorithms are not included for comparison. Furthermore, the experimental settings and the evaluation metrics are not sufficiently detailed, making it difficult to reproduce the results or compare them with other studies.

### Questions
1. Are authors aware of distributionally robust reinforcement learning (DRRL)? There is a large body of works in this track to tackle distributional shift issue in reinforcement learning, both offline and online. **Fundamentals of DRRL**: [1,2] ;**Offline DRRL**: [3,4] ; **Online DRRL**: [5,6]. This is a very much non-extensive list of works but many of these works shows robustness even when there is complete distribution shift, meaning that the test environment (model) is completely different from the training environment. [3,5] both have extensive simulations on MuJoCo tasks. There is another line of work which specifically tackles state adversarial attack. A notable paper will be [7].

My question is, since you include RORL in your benchmarks, why do you ignore a whole line of robust reinforcement learning works.

2. If you are using pessimism to solve *partial data coverage* issue, you also omitted a seminal work [8]. Could you comment on this paper and compare it with your approach?

3. Is your theoretical guarantees comparable to the ones presented in many other offline RL papers?

References:   
[1] Iyengar, G. N. (2005). Robust dynamic programming. Mathematics of Operations Research, 30(2):257–280.  
[2] Nilim, A. and El Ghaoui, L. (2005). Robust control of Markov decision processes with uncertain transition matrices. Operations Research, 53(5):780–798.  
[3] Panaganti, K., Xu, Z., Kalathil, D., and Ghavamzadeh, M. (2022). Robust reinforcement learning using offline data. Advances in Neural Information Processing Systems (NeurIPS).   
[4] Shi, L. and Chi, Y. (2022). Distributionally robust model-based offline reinforcement learning with near-optimal sample complexity. arXiv preprint arXiv:2208.05767. 
[5] Zhou, R., Liu, T., Cheng, M., Kalathil, D., Kumar, P., and Tian, C. (2023). Natural actor-critic for robust reinforcement learning with function approximation. In Thirty-seventh Conference on Neural Information Processing Systems.    
[6] Li, Y. and Lan, G. (2023). First-order policy optimization for robust policy evaluation. arXiv preprint arXiv:2307.15890.   
[7] H. Zhang, H. Chen, C. Xiao, B. Li, M. Liu, D. Boning, and C.-J. Hsieh. Robust deep reinforcement learning against adversarial perturbations on state observations. Advances in Neural Information Processing Systems (NeurIPS), 2020.    
[8] Shi, L., Li, G., Wei, Y., Chen, Y., and Chi, Y. (2022). Pessimistic Q-learning for offline reinforcement learning: Towards optimal sample complexity. In Proceedings of the 39th International Conference on Machine Learning, volume 162, pages 19967–20025. PMLR.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Lyapunov Uncertainty Control (LUC), a novel offline RL approach that leverages Lyapunov stability and control-invariant sets to keep the agent within a “safe” state space region, reducing Bellman uncertainty and enhancing decision reliability. By controlling uncertainty growth with a Q-ensemble, LUC shows robust performance across MuJoCo tasks, particularly excelling in out-of-distribution scenarios and improving policy reliability in high-uncertainty offline RL environments.

### Strengths
​1.Innovative Approach to Stability Control: The application of Lyapunov instability control to find reliable regions introduces a unique and theoretically grounded approach to managing uncertainty in offline reinforcement learning. This paper’s transition from a density-based to a performance-based approach in utilizing Lyapunov instability is a commendable advancement. By focusing on performance rather than traditional density measures, this method offers a novel, theoretically grounded strategy for managing uncertainty in offline reinforcement learning.
​2.Strong Performance in Walker2D: Experimental results show that the proposed method achieves strong performance across various environments, with particularly outstanding results on the Walker2D task within the MuJoCo environment. This indicates the approach’s effectiveness in managing complex dynamical tasks, further showcasing its robustness.
​3.Clear Visualization of Uncertainty Resolution: The method effectively visualizes the process of resolving uncertainty in out-of-distribution (OOD) states, offering a clear depiction of its robustness. This capability emphasizes the model’s potential to manage and reduce errors in unfamiliar states, which is essential for achieving safe and reliable offline RL.

### Weaknesses
 1.Similarity to EDAC’s Regularization Approach: The proposed method’s use of a Q-ensemble for regularization has notable similarities with the Ensemble-Diversified Actor Critic (EDAC) approach, which also employs a Q-ensemble to stabilize Q-value estimation through variance reduction and normalization. Ensemble methods are indeed a common strategy in reinforcement learning to address challenges such as overestimation and uncertainty. However, given the alignment with EDAC’s approach, the novelty of the proposed method’s regularization technique may not be fully distinctive. Specifically, EDAC was designed to diversify ensemble members, thereby enhancing policy stability and improving exploration via variance-based adjustments. If the current method mirrors this approach without introducing a clearly defined improvement or novel mechanism, it may be difficult to argue that the proposed regularization is an advancement rather than a reiteration. The paper does not sufficiently articulate how the proposed method's Q-ensemble differs from EDAC's, particularly in how it contributes to Lyapunov stability and uncertainty control, beyond simply using an ensemble for regularization. A more detailed explanation of the specific mechanisms and their impact on policy stability is needed to establish the novelty of this approach.

 2.Limited Evaluation Scope: The experiments presented in this study are limited to the MuJoCo benchmark, a commonly used environment for continuous control tasks in reinforcement learning. However, focusing solely on MuJoCo may restrict the conclusions that can be drawn about the generalizability and robustness of the proposed approach. Given the objective of establishing reliable offline reinforcement learning policies under uncertainty, it would be beneficial to test the method in more complex and varied environments such as AntMaze or Android-based tasks. These environments present unique challenges, including navigation in maze-like structures and the nuanced action requirements of robotics, which are highly relevant to evaluating an RL method’s capacity to operate in uncertain or OOD conditions. Testing across such diverse benchmarks would significantly strengthen the claims of robustness and adaptability, providing evidence that the proposed method is not overfit to the dynamics and characteristics of MuJoCo tasks. The current evaluation lacks the breadth necessary to fully validate the method's effectiveness in diverse and challenging scenarios.

3.Absence of Direct Comparison to Conservative Offline RL Approaches: Although the study emphasizes stability through Lyapunov principles, it lacks a direct and systematic comparison with conservative offline reinforcement learning techniques, notably Conservative Q-Learning (CQL). CQL has been widely studied for its conservative penalty approach to mitigating out-of-distribution (OOD) risks in offline settings by favoring actions within the distribution of the offline data. Given that the Lyapunov-based uncertainty control also aims to limit the policy’s operations to low-uncertainty (and implicitly, familiar) regions, a comparison with CQL would be invaluable in assessing whether the proposed approach offers any distinct advantage or improvement over conservative penalties in managing OOD actions. Specifically, such a comparison could clarify whether the Lyapunov-based framework introduces any measurable improvements in stability, robustness, or data efficiency compared to CQL and other conservative techniques. A comparative study would also allow for a more nuanced discussion on the benefits and trade-offs between a Lyapunov-centered approach and traditional conservative penalties, potentially uncovering limitations or situations where one may outperform the other. In the absence of this comparative analysis, it remains challenging to fully evaluate the added value and practical impact of the proposed methodology within the broader landscape of offline RL.

### Questions
​1.Difference from EDAC’s Q-Ensemble: Could you provide further clarification on how the Q-ensemble utilized in this work differs from that in EDAC, especially in terms of its impact on policy stability and uncertainty control?
​2.Generalizability Beyond MuJoCo: Have you considered extending the experiments to additional environments such as AntMaze or Android-based tasks? Results on these benchmarks could shed light on the method’s generalizability across different reinforcement learning challenges.
​3.Relation to CQL in OOD Scenarios: The proposed method appears to have parallels with conservative Q-learning (CQL) in its handling of OOD data. Could you elaborate on the specific distinctions or similarities between this approach and CQL, particularly regarding their mechanisms for addressing distributional shifts?

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
3

### Summary
This paper proposes a new approach for offline RL based on Lyapunov stability and Bellman error as a metric of uncertainty, and presents both theoretical and empirical results demonstrating the efficacy of the proposed approach.

### Strengths
Originality
- Paper uses Lyapunov stability to improve the performance of offline RL algorithms, which is a relatively novel combinations of existing tools
Quality
- Experiments are thorough, including evaluations on full D4RL suite of tasks, as well as additional experiments investigating OOD states and ablations to the algorithm
- Theoretical results show that proposed approach is conceptually sound, and highlights how errors in different components of the algorithm influence downstream performance
Clarity
- The paper could use some clarifications as discussed below.
Significance
- Experiments show that the proposed approach outperforms some existing approaches to offline RL

### Weaknesses
The paper could be further improved if it included comparisons to other standard offline RL, and if it provided a bit more discussion in text explaining each theorem and its significance.

Another paper that is related: In-Distribution Barrier Functions: Self-Supervised Policy Filters that Avoid Out-of-Distribution States

### Questions
No questions.

### Soundness
3

### Presentation
2

### Contribution
3
