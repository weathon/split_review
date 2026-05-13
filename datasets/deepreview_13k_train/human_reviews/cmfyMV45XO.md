# Feedback Favors the Generalization of Neural ODEs

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
\textcolor{black}{The well-known generalization problem hinders the application of artificial neural networks in continuous-time prediction tasks with varying latent dynamics. In sharp contrast, biological systems can neatly adapt to evolving environments benefiting from real-time feedback mechanisms. Inspired by the feedback philosophy, we present feedback neural networks, showing that a feedback loop can flexibly correct the learned latent dynamics of neural ordinary differential equations (neural ODEs), leading to a prominent generalization improvement. The feedback neural network is a novel two-DOF neural network, which possesses robust performance in unseen scenarios with no loss of accuracy performance on previous tasks.} A linear feedback form is presented to correct the learned latent dynamics firstly, with a convergence guarantee. Then, domain randomization is utilized to learn a nonlinear neural feedback form. Finally, extensive tests including trajectory prediction of a real irregular object and model predictive control of a quadrotor with various uncertainties, are implemented, indicating significant improvements over state-of-the-art model-based and learning-based methods\footnote[3]{The project codes will be made available upon publication.}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the challenge of enhancing generalizability and adaptability in Neural ODEs for continuous time-series prediction tasks. It introduces feedback mechanisms into the Neural ODE framework, which dynamically adjust model parameters in response to errors in predictions. The study begins with a theoretical analysis, providing a convergence analysis of linear feedback, and extends to a practical implementation where a neural network learns the feedback mechanism. Experimental results highlight the improved performance of the neural feedback mechanisms over traditional ODE models.

### Strengths
1) The paper studies the critical issue of adaptability and generalizability in continuous-time prediction tasks using Neural ODEs, which is essential for real-world applications.
2) By incorporating feedback mechanisms, the approach potentially enhances the adaptability and generalizability of Neural ODEs, making it a contribution to the field.
3) By conducting several experiments, the proposed method demonstrates superior performance across various trajectory and dynamics prediction tasks.

### Weaknesses
1) **Comparison with Existing Feedback Mechanisms**: While feedback mechanisms are commonly employed in other neural network-based time-series prediction tasks, this paper does not compare its approach to these established methods. For example, studies such as [1,2] use feedback mechanisms inspired by the Kalman filter and Extended Kalman Filter (EKF) to adapt neural networks for online time-series prediction. Including a comparison with these relevant works would be beneficial. Specifically, the paper should analyze how the proposed method's performance and computational cost compare to EKF-based adaptive methods, which are known for their real-time capabilities and robustness to noise.

2) **Connection to Continual Learning**: The claims about generalization across new tasks while maintaining performance on previous tasks touch upon the principles of continual learning. A discussion of related works in continual learning, particularly focusing on online continual learning [3] and test-time adaptation [2,4], would provide a richer context. The paper should clarify whether the proposed feedback mechanism is designed to address catastrophic forgetting, a common challenge in continual learning. Furthermore, it should discuss the differences between the proposed method and existing continual learning techniques, such as regularization-based methods or replay-based methods.

3) **Evaluation of Theoretical Claims and Linear Feedback**: The paper presents a theorem on the convergence of linear feedback to a bounded error but does not empirically evaluate this claim. Designing a simple toy experiment to test this theorem and discussing the practical implications of the assumptions would enhance the credibility and thoroughness of the research. Specifically, the paper should provide empirical evidence of the convergence rate and the error bound, and discuss how the assumptions of the theorem (e.g., bounded learning residuals) affect the practical performance. In addition, reporting the results of Linear feedback on several trajectory prediction tasks in the experiment will improve the quality of the paper.

4) There are minor typos and notation errors that need correction for clarity. Line 167: $\dot{z}=[\hat{f}^T,\hat{f}^T]^\top$ -> $\dot{z}=[f^T,\hat{f}^T]^\top$ ; Line 257：  'sate'  ->  'state'.

### Questions
1) Review Related Work on Feedback Adaptation in Time-Series Prediction [1,2].  
2) Explore the Relationship with Continual Learning [2,3,4].  
3) Perform Experiments on Linear Feedback.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces *feedback neural networks*, enhancing the generalization of neural ODEs in continuous-time tasks by adapting learned dynamics through real-time feedback. Inspired by biological systems, the network employs a two-DOF structure with linear feedback (whose convergence is theoretically analyzed) and nonlinear feedback learned via domain randomization. Unlike prior methods, it achieves robust generalization without sacrificing accuracy. Experiments, including trajectory prediction and quadrotor control, demonstrate its improvements over existing methods.

### Strengths
1. Clear and promising motivation and concise writing that trace the development of integrating Neural ODEs with feedback structures, progressing from linear to nonlinear feedback.
2. Theoretical analysis is presented for the linear feedback case, demonstrating that prediction error converges to a bounded set with an appropriately chosen feedback gain.
3. Extensive illustrations on simple cases effectively demonstrate their method’s performance compared to standard Neural ODEs.
4. In addition to toy experiments on trajectory prediction, they conduct practical quadrotor tracking experiments, incorporating learned prediction models within an MPC controller, where the proposed FNN-MPC shows superior performance over alternative approaches.

### Weaknesses
I have limited experience with Neural ODEs, so I’m not fully confident in assessing the contribution to this area. My main concerns, however, relate to the experimental section. While the current experiments effectively showcase the improvements of FNN, the experimental setup is relatively simple and lacks key baselines in learning dynamics models beyond Neural ODEs, such as [1-3]. Furthermore, it is unclear how flight trajectories were collected and how tracking performance was evaluated. Given the complexity of quadrotor dynamics and aerodynamics, these aspects significantly impact the difficulty of the task and the validity of the results. Although a preliminary overview of quadrotor dynamics is provided in the appendix, additional discussion on environmental conditions, such as wind fields and airflows [4], would help clarify the experimental setting.

### Questions
See the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces closed-loop feedback neural ODEs which offer better generalization performance compared to open-loop neural ODEs. A linear state-error feedback term is introduced to compensate for prediction inaccuracies in the closed-loop error mechanism. This feedback term is shown to improve the generalization performance which was poor in the previous open-loop neural ODE formulations.

### Strengths
I believe this paper makes a strong contribution. The paper is well-written and easy to follow. The technical development with the use of closed-loop state error feedback term is well-motivated. I found the paper an interesting read.

### Weaknesses
Despite the significant contributions, there are quite a few mathematical errors and a general lack of mathematical rigor in the paper. These errors might be minor and easy to resolve, I suggest the authors address the following issues.

1. Equation (7) appears erroneous. Combining (4) and (6) should actually give the term $L(\bar{x}(t)-\hat{x}(t))$, not $L(x(t)-\hat{x}(t))$. This error gets carried forward to Eq. (9) of the convergence analysis, thus potentially invalidating Theorem 1. As far as I can help, this issue can be avoided redefining Eq. (6) in terms of $x(t)$ instead of $\bar{x}(t)$. In that case, Eq. (8) needs to be adjusted accordingly. Alternatively, the authors can add and subtract $Lx(t)$ term in the derivation of Eq. (9), which should result in an extra $L(x-\bar{x})$ term in (9). This term will need to be bounded and that bound would need to be considered in the ensuing Lyapunov-based stability analysis to obtain the correct error bounds. Either way, the mathematical analysis needs revisions to address the error in Eq. (7).

2. The development in Eq. (4)-(8) is in a discrete-time setting but the convergence analysis in Section 3.2 is in a continuous-time setting. To be consistent, the authors are suggested to either reformulate the development in Section 3.1 using continuous-time integrals instead of discrete-time summations, or rederive the convergence analysis in Section 3.2 using discrete-time Lyapunov theorem or contraction analysis. I believe this should be easy to address.

3. Although the proof of Theorem 1 is correct, it appears the analysis is not performed in the most efficient manner. Specifically, the use of Young's inequality in Eq. (2) is not the most efficient because it results in the $\lambda_m(L)-\frac{1}{2}$ term which carries forward through the analysis. The problem with this term is that the gain condition $\lambda_m(L)>frac{1}{2}$ would need to be imposed to enure an exponential decay. Such a gain condition is missing in the paper. However, changing the analysis in Eq. (20) would remove the need for a gain condition. I suggest the authors use the following form of Young's inequality instead

$$ \tilde{x}^T \Delta f(t) = \sqrt{\lambda_m(L)}||\tilde{x}||\frac{\gamma}{\sqrt{\lambda_m(L)}}=\frac{\lambda_m(L)||\tilde{x}||^2}{2}+\frac{\gamma^2}{2\lambda_m(L)}.$$

This would result in 

$$\dot{V} \leq -\frac{\lambda_m(L)||\tilde{x}||^2}{2}+\frac{\gamma^2}{2\lambda_m(L)}.$$

This formulation would eliminate the need of an extra gain condition, while also obtaining a tighter bound in the $\delta$ term.

4. The purely time-dependent exponentially decaying gain schedule for the feedback gain in Eq. (11) can be problematic in terms of the performance, because the theoretical error bounds in Theorem 1 contain $\lambda_m(L)$ in the denominator. The bounds get enormous with the exponential decay, thus essentially making the neural ODE open-loop with time. There are better ways to schedule the gain using closed-loop feedback. The authors are recommended to look into recursive least squares algorithms that are popular in the adaptive control or Kalman filtering literature, where the gain decreases as the estimator gains more information instead of scheduling it to always decay with time. 

5. This is minor but the technical writing throughout the paper lacks mathematical rigor. Specifically, the mathematical entities (states, functions, constants etc.) are not formally defined. For example, the domain of x can be precisely defined, i.e., $x(t)\in\mathbb{R}^n$. The function $f$ can be defined formally as $f:\mathbb{R}^n\times\mathbb{R}^m\times\mathbb{R}\to \mathbb{R}^n$. The notations $f_{neural}(t)$ and $\hat{f}_{neural}(t)$ (which are not formally defined) are confusing because they take only time as the argument. However, they also seem to depend on x and \hat{x}. The term $L$is defined to be a constant, but it should actually be a positive-definite matrix. The concatenated state $z$ needs to be defined similarly with an appropriate domain. In the statement of Theorem 1, instead of stating "the state observation error and its derivative can converge to bounded sets exponentially, which upper bounds can be regulated by the feedback gain L", the authors should explicitly state the obtained exponentially convergent bounds.

6. Minor issue, but Figure 1 seems to indicate the error is being passed through another neural network instead of a linear feedback gain, which is not the case in this paper. The figure needs to be revised replacing this second neural network with a -L gain block.

### Questions
I do not have further questions or suggestions beyond the comments I made above. The authors are suggested to carefully examine all of my above comments. I commend the authors for this interesting work and look forward to reading their responses.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper successfully enhanced the generalization capability of Neural ODEs by introducing feedback mechanisms, demonstrating significant performance improvements across multiple practical applications. Specifically, the authors proposed a Two-Degree-of-Freedom (Two-DOF) neural network architecture that combines linear and nonlinear feedback mechanisms, effectively correcting prediction errors and exhibiting stronger adaptability and generalization capability when dealing with complex and nonlinear dynamical systems. Overall, it provides a new perspective and solution for the generalization problem of neural networks in continuous-time prediction tasks.

### Strengths
- By combining linear and nonlinear (neural feedback) forms of feedback, an innovative network architecture is proposed that enhances generalization capability in unseen scenarios while maintaining accuracy on previous tasks. This design demonstrates innovation and practical value in current research. The experimental section covers trajectory prediction and quadrotor control, validating the method's superior performance.

- The paper provides theoretical analysis, proving system stability and convergence under linear feedback conditions. This establishes a solid theoretical foundation for the method's reliability and robustness. Additionally, the paper is well-structured with rigorous logic and clear writing. The figures and tables are intuitive. Detailed algorithm descriptions enhance the method's reproducibility.

- Through domain randomization techniques, the nonlinear neural feedback component is learned independently, demonstrating an effective way to improve generalization without significantly increasing training burden. This method effectively extends the applicability of feedback mechanisms when facing unknown uncertainties.

- The feedback loops can be easily integrated into existing trained Neural ODEs without requiring retraining, reducing implementation difficulties in practical applications and enhancing the method's feasibility and scalability. Furthermore, the method shows potential for online adjustment, further increasing its practical value. 

- Generalization ability is a key challenge for neural networks in practical applications, and the paper effectively improves Neural ODE's generalization performance through feedback mechanisms, addressing the performance degradation issue of traditional methods in unseen tasks. This research has significant implications for neural network architecture design and practical engineering applications, showing broad application potential.

### Weaknesses
1. **Oversimplified Convergence Analysis (Section 3.2)**:
    - The convergence analysis is solely based on bounded learning residual error (Assumption 1), assuming an upper bound γ. However, in practical applications, system dynamics can be highly complex, making residual errors difficult to strictly bound and potentially time-varying or having more complex characteristics (such as unbounded growth or sudden disturbances). This idealized assumption limits the applicability of theoretical analysis in real scenarios. Specifically, the analysis does not account for scenarios where the residual error might exhibit non-stationary behavior or have a distribution with heavy tails, which could significantly impact the convergence properties of the proposed method. The assumption of a fixed upper bound also neglects the possibility of error accumulation over time, a critical factor in long-term predictions.

2. **Manual Tuning of Feedback Gain Matrix \(L\)**:
    - The selection of feedback gain matrix \(L\) relies mainly on manual tuning, based on theoretical analysis and experimental results. This approach is both time-consuming and difficult to precise in complex systems, especially in high-dimensional systems or real-time changing environments where manual selection may not meet dynamic adjustment needs. The lack of a systematic approach for determining the optimal gain matrix makes the method less practical for real-world applications where manual tuning is often infeasible. Furthermore, the paper does not provide clear guidelines on how to adjust the gain matrix for different types of systems or disturbances, making it difficult to generalize the method.

3. **Training Strategy Issues in Neural Network Feedback Section**:
    - The authors adopt a two-stage training method: first training the Neural ODE, then fixing parameters to train the feedback part. This approach may not be optimal as parameters of both networks might be coupled, preventing the overall model from achieving optimal performance under joint optimization. Could different training approaches be discussed? The sequential training approach neglects the potential for synergistic learning between the feedforward and feedback components. This could lead to suboptimal performance, as the feedback network is not trained to compensate for the specific errors produced by the feedforward network during its training phase. A joint training approach could potentially lead to better overall performance.

4. **Insufficient Ablation Studies**:
    - Although the paper includes some ablation studies, they lack comprehensiveness and depth. For instance, there's insufficient in-depth analysis of individual components' impacts (like neural feedback network, linear and nonlinear feedback), and detailed sensitivity analysis of feedback gain matrix \(L\) and domain randomization parameters. Additionally, the limited variety of baseline models fails to cover more different types or improved Neural ODE variants, affecting the comprehensive demonstration of the method's advantages. The ablation studies should include a more granular analysis of the impact of each component, including the neural feedback network, linear feedback, and nonlinear feedback, on the overall performance. Furthermore, a sensitivity analysis of the feedback gain matrix L and domain randomization parameters is needed to understand the robustness of the method.

5. **Lack of Detailed Discussion on Computational Cost and Training Time**:
    - The paper's discussion of computational cost and training time is insufficient, failing to comprehensively address the proposed method's performance in terms of computational resources and training time compared to traditional methods. The paper needs to provide a more detailed analysis of the computational complexity of the proposed method, including the time and memory requirements for training and inference. This is crucial for evaluating the practical feasibility of the method, especially for real-time applications.

### Questions
1. **Automated Design of Feedback Gain and Decay Rate**:
    - Could an adaptive mechanism be developed to dynamically adjust the feedback gain matrix \(L\) and decay rate \(\beta\) based on real-time prediction errors or system states? This would reduce the need for manual parameter tuning and enhance the method's flexibility and adaptability. Alternatively, provide more detailed documentation on the specific effects of feedback gain matrix \(L\) and decay rate \(\beta\).

2. **Comprehensive Ablation Studies and Sensitivity Analysis**:
    - Suggest adding ablation experiments on the independent effects of each component (such as neural feedback network, linear and nonlinear feedback), along with detailed sensitivity analysis of the feedback gain matrix \(L\) and domain randomization parameters. This would help better understand each part's contribution to overall performance.

3. **Compare with More Baseline Models**:
    - To more comprehensively demonstrate the advantages of the proposed method, it is recommended to compare with a wider range of baseline models, including other improved Neural ODE variants or feedback-based models, to validate its effectiveness across diverse scenarios.

4. **Detailed Description of Computational Cost and Training Time**:
    - Suggest adding a dedicated section in the paper to thoroughly discuss the performance of the proposed method in terms of computational resources and training time, including comparisons with traditional methods. This would help readers better evaluate its practical feasibility and efficiency.

### Soundness
2

### Presentation
4

### Contribution
3
