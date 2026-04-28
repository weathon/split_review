# Bridging the Gap Beteween SL and TD Learning via Q-conditioned maximization

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 1, 5, 3

## Abstract
Recent research highlights the efficacy of supervised learning (SL) as a methodology within reinforcement learning (RL), yielding commendable results. Nonetheless, investigations reveal that SL-based methods lack the stitching capability typically associated with RL approaches such as TD learning, which facilitate the resolution of tasks by stitching diverse trajectory segments. This prompts the question: How can SL methods be endowed with stitching property and bridge the gap with TD learning? This paper addresses this challenge by exploring the maximization of the objective in the goal-conditioned RL. We introduce the concept of Q-conditioned maximization supervised learning, grounded in the assertion that the goal-conditioned RL objective is equivalent to the Q-function, thus embedding Q-function maximization into traditional SL-based methodologies. Building upon this premise, we propose Goal-Conditioned Reinforced Supervised Learning (GCReinSL), which enhances SL-based approaches by incorporating maximize Q-function. GCReinSL emphasizes the maximization of the Q-function during the training phase to estimate the maximum expected return within the distribution, subsequently guiding optimal action selection during the inference process. We demonstrate that GCReinSL enables SL methods to exhibit stitching property, effectively equivalent to applying goal data augmentation to SL methods. Experimental results on offline datasets designed to evaluate stitching capability show that our approach not only effectively selects appropriate goals across diverse trajectories but also outperforms previous works that applied goal data augmentation to SL methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel method named Goal-Conditioned Reinforced Supervised Learning (GCReinSL) aiming to address the limitation of outcome-conditioned behavioral cloning (OCBC) methods in reinforcement learning tasks. Current supervised learning methods in RL lack the capability of trajectory stitching which allows the algorithms to effectively combine data from suboptimal trajectories to achieve better performance. This paper leverages expectile regression for Q-function estimation and demonstrates through theoretical analysis and experiments that this augmentation enables OCBC methods to solve the stitching problem. Experimental results on offline datasets show that GCReinSL outperforms existing goal-conditioned SL methods.

### Strengths
- The paper solves the stitching problem in OCBC methods by introducing Q-conditioned maximization, which allows the algorithm to combine data from suboptimal trajectories.
- The paper provides theoretical and empirical analysis to demonstrate the effectiveness of the proposed method in enhancing OCBC methods.
- The motivation for using executive regression for Q-function estimation is well-explained and aligns with the goal of estimating the maximum expected return without out-of-distribution issues.

### Weaknesses
 - **Inconsistent and Incomplete Notations**:
The mathematical notations are poorly defined and inconsistent, for example, equations like Eq. (3), which omits necessary terms such as the expectation over the initial state distribution. The objective function $J(\pi)$ should explicitly show its dependence on the initial state $s_0$, as the return is calculated from this starting point. Furthermore, the policy $\pi$ is overloaded; in Eq. (2) it is a goal-conditioned policy $\pi(a | s, g)$, while in Eq. (3) it appears to be a trajectory-wise policy $\pi(\tau | g)$, without a clear definition of the relationship between these two. These inconsistencies make it difficult to follow the derivation and understand the core concepts.

- **Lack of Theoretical Rigor**:
Theorem 4.1 and its proof are presented in a sloppy and non-rigorous manner. Important terms are either undefined or unclear. For instance, the notation $\textbf{SG} = (s, g, a, Q)$ is introduced, but then $Q(\textbf{SG}, a)$ is used, which implies $Q(s, g, a, Q, a)$, a nonsensical expression. Additionally, $\mathbf{Q}^m$ is used as if it were a policy, and the optimization in $\pi_{\theta}^* = \arg \min \mathcal{L}^m_Q$ is not clearly defined, especially since the loss function $\mathcal{L}^m_Q$ does not seem to depend on the policy parameters $\theta$. The proof in Appendix A.2 uses inequalities between vectors without specifying whether it is element-wise, and it refers to "all Q-values from the offline dataset" without clarifying if these are true Q-values or estimated ones. The lack of precision and clarity in the theoretical development undermines the validity of the claims.

- **Underwhelming Empirical Performance**:
The proposed method, GCReinSL, underperforms significantly compared to existing methods like IQL and CQL, particularly in the more challenging Antmaze datasets. The results fail to justify the claimed advantages of sequence modeling approaches over TD-based methods. The paper does not provide sufficient analysis to explain why GCReinSL struggles in these environments, especially given the theoretical claims about its ability to perform trajectory stitching. The empirical results do not support the core hypothesis that the proposed method effectively bridges the gap between SL and TD learning.

- I have spent a significant amount of time and effort thoroughly reviewing this paper, but the conceptual, theoretical, and empirical weaknesses, along with poor clarity, lead me to come to a conclusion that the paper is not ready for publication.

- **Lack of Clarity**:
The paper is riddled with errors and unclear explanations, making it challenging to read (see below). The poor writing quality detracts from the overall presentation and makes it difficult to follow the core ideas.




### Questions
- Can you provide more insights into the computational cost of adding the conditional variational autoencoder and how it scales with the size of the dataset?
- Can this method adapt to the return-conditioned formulation? What are the challenges and limitations of this approach?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper aims to enhance the effectiveness of supervised learning (SL) methods in reinforcement learning (RL) by introducing a framework called Goal-Conditioned Reinforced Supervised Learning (GCReinSL). The authors propose that traditional SL-based RL methods, such as outcome-conditioned behavioral cloning (OCBC), lack trajectory stitching capabilities, which are critical for integrating suboptimal trajectories into optimal paths—a feature common in temporal-difference (TD) learning. To address this, the authors introduce Q-conditioned maximization, positing that the objective in goal-conditioned RL is equivalent to the Q-function, thereby allowing SL methods to maximize expected returns.

The paper presents GCReinSL as a solution to bridge the gap between SL and TD learning by embedding Q-function maximization into SL-based methods. The proposed approach is evaluated on various goal-conditioned offline RL tasks, such as Pointmaze and Antmaze, and compared against other methods like IQL, CQL, and other sequence modeling techniques. The authors claim that GCReinSL improves stitching performance and generalization across unseen goal-state pairs in offline RL datasets.

### Strengths
- The paper tackles the relevant challenge of bridging the gap between supervised learning (SL) and temporal-difference (TD) learning, especially focusing on trajectory stitching—a key limitation of SL-based RL methods.
- The paper’s focus on goal-conditioned RL is timely and aligns with practical applications in areas like robotics and offline RL.

### Weaknesses
1. The introduction lacks sufficient emphasis on motivation, such as the advantages and necessity of SL compared to TD under the goal-conditional setting. It would be better to discuss the importance of SL-based methods, like OCBC, in detail in the introduction.  
2. Following Weakness 1, the experimental results also show a significant gap compared to TD-based algorithms (Table 1). It is still helpful to discuss this experiment phenomenon after Table 1.
3. As shown in Figure 5, the performance of GCReinSL is inferior to the advanced TGDA method in some higher-dimensional tasks. Could the author discuss this result in detail?

### Questions
See the questions above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the stitching property for SL within goal-conditioned offline RL problems. This stitching property is commonly obtained in TD-based algorithms and fails in SL. This paper proposes the GCReinSL, which enhances SL-based approaches by incorporating maximize Q-function.  Equipped with the GCReinSL framework, the previous outcome-conditioned behavioral cloning (OCBC) algorithms exhibit the switching property and achieve better performance under the goal-conditioned setting.

### Strengths
1. The difference in trajectory stitching property between SL and TD does exist and is valuable for studying to improve the generalization performance of SL.
2.  The method that incorporates maximizing Q-function is natural, and the experiments show effectiveness.

### Weaknesses
The idea is not novel, basically a combination of tricks in exsiting literature. The expriments results can not support the title. See my questions for more details.

It might be confusing to use $\pi$ to denote the probabiliy over the trajectory in $\pi(\tau|s,g)$ (3) and also to denote the policy $\pi(a|s,g)$.

In section 4.3, what is the $\pi$ in the probability distribution? at first, it was $p^{\pi}$ in line 234, then it becomes  $p^{\pi(\cdot|\cdot|g)}$ in line 245. Is it the behavior policy collecting the offline dataset?

For the Antmaze taks and the results in Table 1. The DT, EDT and Reinformer almost do not work. GCReinSL improves the performance from approximately 0 to about 10 (with large variance), there is a huge gap compared to RL method (about 50-80). Say, the improvement is about 10, and the initial gap is 50-80. Is it proper to claim 'significantly narrowing the gap with TD learning methods such as IQL'? I see this experiment as a example that SL would fail catastrophically, even with your maximum Q conditioning trick.

I have a question about the maximum Q conditioning trick. Different from the Return conditioned supervised learning methods such as Reinformer, for which they can directly access to the return in the dataset, in the goal conditioned supervised learning, the Q-function is estimated from VAE, and then the maximization is performed on the estimated Q-function. I guess the estimation error is hard to control as it may come from multiple sources: 1) how you evaluate that the VAE obtain decent estimation of the goal probability? 2) how you sure that the expectile regression gives a proper maximum in distribution Q value? Theorem 4.1 is not a accurate quantification of the return you get as it only considers the ideal case m goes to 1 and it does not consider how the maximum value is cover in the offline dataset.

### Questions
Please see the Weakness part.
1. As shown in Figure 5, the performance of GCReinSL is inferior to the advanced TGDA method in some higher-dimensional tasks. Could the author discuss this result in detail?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies reinforcement learning via surpervised learning and explores how to endow SL with trajectory stitching ability. Goal-Conditioned Reinforced Supervised Learning (GCReinSL) is proposed which emphasizes the maximization of the Q-function during the training phase to estimate the maximum expected return within the distribution, subsequently guiding optimal action selection during the inference process.

### Strengths
The paper is relatively well-written. Experiment results are solid.

### Weaknesses
The idea is not novel, basically a combination of tricks in exsiting literature. The expriments results can not support the title. See my questions for more details.

### Questions
1. It might be confusing to use $\pi$ to denote the probabiliy over the trajectory in $\pi(\tau|s,g)$ (3) and also to denote the policy $\pi(a|s,g)$.

2. In section 4.3, what is the $\pi$ in the probability distribution? at first, it was $p^{\pi}$ in line 234, then it becomes  $p^{\pi(\cdot|\cdot|g)}$ in line 245. Is it the behavior policy collecting the offline dataset?

3. For the Antmaze taks and the results in Table 1. The DT, EDT and Reinformer almost do not work. GCReinSL improves the performance from approximately 0 to about 10 (with large variance), there is a huge gap compared to RL method (about 50-80). Say, the improvement is about 10, and the initial gap is 50-80. Is it proper to claim 'significantly narrowing the gap with TD learning methods such as IQL'? I see this experiment as a example that SL would fail catastrophically, even with your maximum Q conditioning trick.

4. I have a question about the maximum Q conditioning trick. Different from the Return conditioned supervised learning methods such as Reinformer, for which they can directly access to the return in the dataset, in the goal conditioned supervised learning, the Q-function is estimated from VAE, and then the maximization is performed on the estimated Q-function. I guess the estimation error is hard to control as it may come from multiple sources: 1) how you evaluate that the VAE obtain decent estimation of the goal probability? 2) how you sure that the expectile regression gives a proper maximum in distribution Q value? Theorem 4.1 is not a accurate quantification of the return you get as it only considers the ideal case m goes to 1 and it does not consider how the maximum value is cover in the offline dataset.

### Soundness
2

### Presentation
2

### Contribution
2
