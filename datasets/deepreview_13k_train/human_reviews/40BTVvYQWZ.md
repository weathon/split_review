# Learning and Steering Game Dynamics Towards Desirable Outcomes

- Decision: Reject
- Scores: 3, 6, 6, 5, 3

## Abstract
Game dynamics, which describe how agents' strategies evolve over time based on past interactions, can exhibit a variety of 
undesirable behaviours including
convergence to suboptimal equilibria, cycling, and chaos.~While central planners can employ incentives to mitigate such behaviors and steer game dynamics towards desirable outcomes, the effectiveness of such interventions critically relies on accurately predicting agents' responses to these incentives---a task made particularly challenging when the underlying dynamics are unknown and observations are limited. To address this challenge, this work introduces the Side Information Assisted Regression with Model Predictive Control (SIAR-MPC) framework. We extend the recently introduced SIAR method to incorporate the effect of control, enabling it to
utilize side-information constraints inherent to game-theoretic applications to model agents' responses to incentives from scarce data.~MPC then leverages this model to implement dynamic incentive adjustments.
Our experiments demonstrate the effectiveness of SIAR-MPC in guiding systems towards socially optimal equilibria, stabilizing chaotic and cycling behaviors. Notably, it achieves these results in data-scarce settings of few learning samples, where well-known system identification methods paired with MPC show less effective results.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This work studies how to steer game dynamics towards desirable outcomes. To do so, the authors introduce a framework that combines side information assisted regression and model predictive control. The framework first tries to perform a system identification step to approximate the control dynamics and subsequently utilizes MPC to steer the system. The authors also give several empirical studies on games, demonstrating the effectiveness of the proposed framework.

### Strengths
The problem is well motivated and the paper is overall easy to follow.

### Weaknesses
The originality and significance of the contributions seem limited. The framework primarily extends existing techniques, coupled with well-studied MPC approaches. It is not clear how the contributions could be translated into broader insights for the community. Also, is it possible to provide some theoretical justification?

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper propose Side Information Assisted Regression with Model Predictive Control (SIAR-MPC), a framework to learn the dynamics of game and steer game dynamics towards desirable outcomes when data is scarce. This framework has two components, which includes system identification part and MPC part. In system identification step, the algorithm approximated the controlled dynamics using only a limited number of samples. Second, in MPC step, based on the learned dynamics, MPC is applied to steer the system towards a desirable outcome. This framework is evaluated in data-scarce settings and show this framework have superior performance compared to other baselines.

### Strengths
- Most of this paper is well-structured and well-written.

### Weaknesses
 - The font in the plots could be larger, it is relatively hard to read. The introduction of RFI could be more detailed in section 4.1.
- The effectiveness of the algorithm in data-scarce setting could be emphasized more in the experiments, it is interesting to see how the performance is affected when the avalibility of the data varies.


### Questions
- what if there is error in the dynamics modelling step, what will happen in the MPC phase? Can MPC accomodate the error?

### Soundness
3

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
The submission investigates the problem of steering game unknown game dynamics. The submission's approach involves first identifying these dynamics by extending SIAR to control settings. Then, it uses MPC to adjust steer these dynamics. The submission gives examples of its approach for stag hunt, matching pennies and epsilon-rock-paper-scissors.

### Strengths
The problem of identifying and steering game dynamics is both difficult and seems to be understudied, though I am not a domain expert. The approach described in the submission seems sensible and technically interesting.

---

Overall, I am not sure how useful the submission is, but I found its object of study and ideas interesting. I consider the latter to be enough to merit acceptance. On the other hand, I am not an expert in this domain, so both my perception of the submission's strengths and weaknesses should be treated with a non-zero amount of skepticism. I left my confidence low so as to leave room for reviewer's who may feel more confident in their expertise on the subject matter.

### Weaknesses
1. The submission doesn't do a very good job communicating how the reader ought to be interpreting these incentives.
2. The submissions touts the "diverse range of games" on which it performs experiments. In fact, it performs experiments on 2 2x2 matrix games and 1 3x3 matrix game. I would hesitate to call this diverse.
3. The submission notes the "larger dimensionality" of rock-paper-scissors. This strikes me as somewhat concerning. If the dimensionality of rock-paper-scissors is already noteworthy in the context of the method, is there much hope of applying it to more interesting settings?
4. I think the first paragraph of section 5.2 could be clearer. In the first part of the paragraph, the submission explains that replicator dynamics and learning algorithms with non-vanishing regret possess undesirable behavior. Thereafter, it states "In that regard, ... we demonstrate the performance SIAR-MPC in steering [learning dynamics of non-vanishing regret]." If I am reading between the lines correctly, the submission is meaning to communicate something positive---that it successfully steers learning dynamics with undesirable properties. But the writing doesn't effectively get that point across, in part because there is no previously mentioned "regard" that makes the sentence read correctly.

### Questions
How should the reader be interpreting these incentives in the context of the games studied?

How scalable are these approaches to larger settings? Are there fundamental barriers to scaling here or is there hope of overcoming dimensionality-related limitations?

### Soundness
3

### Presentation
3

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
This paper investigates the problem of steering agent behaviors in normal-form games.There is a central planner being able to influence the game's utility function. The agents change their policy according to the current state of the game. The paper proposes the SIRC-MPC framework. In this framework the planner first learn the agent's behavior by fitting the dynamics with polynomial regressors. To facilitate the learning, RFI and PC are incorporated as regularizations. Then it steers the behavior via a MPC. Finally it conducts experiments to illustrate the effectiveness of this framework.

### Strengths
1. The paper is clearly written and easy to follow.
2. This framework is very general. Only reasonable constraints are placed to enhance the sample efficiency of the learning.

### Weaknesses
1. The technical novelties of this paper is a bit unclear to me. See questions below.
2. The motivation of this paper is a bit unclear to me.

### questions:
 1. Can the authors clarify on the technical novelties of this paper? For example, one contribution of this paper is its superiority in data-scarce settings. However using PINN enhances performance in this setting is straightforward to me. Is there some technical difficulty I am missing here?
2. For the central planner, steering is not free. Larger $\omega$ is clearly more costly in real-world application. Should we compare the algorithms under the fixed budget?
3. This paper places no constraint on how we choose $\omega$ in the first phase. On the one hand, we cannot intervene a real-world game arbitrarily at our wishes, so this seems to be a strong constraint. On the other hand, if we allow online learning, i.e. adaptively picking $\omega$ so that the data is more informative, the sample complexity should be even lower. Is online learning a more natural setting?

### Questions
1. Can the authors clarify on the technical novelties of this paper? For example, one contribution of this paper is its superiority in data-scarce settings. However using PINN enhances performance in this setting is straightforward to me. Is there some technical difficulty I am missing here?
2. For the central planner, steering is not free. Larger $\omega$ is clearly more costly in real-world application. Should we compare the algorithms under the fixed budget?
3. This paper places no constraint on how we choose $\omega$ in the first phase. On the one hand, we cannot intervene a real-world game arbitrarily at our wishes, so this seems to be a strong constraint. On the other hand, if we allow online learning, i.e. adaptively picking $\omega$ so that the data is more informative, the sample complexity should be even lower. Is online learning a more natural setting?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new framework, SIAR-MPC, to address undesirable behaviors in game dynamics. The framework consists of two steps: first, it identifies controlled system dynamics using a polynomial regressor, incorporating side information as additional constraints to improve the accuracy of the learned dynamics. Second, Model Predictive Control (MPC) is adapted to predict the desired control actions.

### Strengths
1.	The paper presents an interesting setting with a clear motivation, making it easy to follow and understand. The approach of first identifying system dynamics and then planning to control the system is particularly intriguing.

2.	The use of polynomial regression with side-information constraints (RFI and PC) and the application of sum-of-squares (SOS) optimization shows a solid foundation in mathematical. The framework also leverages MPC effectively to solve constrained optimization problems dynamically.

### Weaknesses
1.	Some key concepts in the text lack clear definitions or explanations, which may confuse readers; further clarification is recommended. For example, the concept of "side-information constraints"(First shown at Page 2 Lines 56) is central to the paper, yet it lacks a clear definition and explanation. It’s not evident what constitutes side information and how it contributes to enhancing the accuracy of the learned controlled dynamics. The term "Strategic Nature" (Page 5, Line 230) is mentioned to justify the validity of the second side-information constraint. However, what actually plays a crucial role in supporting this constraint is the concept of Positive Correlation (PC). It's unclear why the authors introduced the notion of "Strategic Nature" in this context.

2.	Lack of theoretical justification. The paper does not provide evidence that a polynomial regressor is sufficient to accurately capture system dynamics, especially given the limited number of samples (K=5). The two side-information constraints are proposed to aid in learning an accurate model of the controlled system dynamics with limited data. However, there is no theoretical justification provided on how these constraints contribute to this goal. This is particularly concerning given that the second step involves MPC, which requires a high-fidelity model. Additionally, the use of SOS optimization introduces further uncertainty in achieving a precise model. Specifically, the paper lacks a discussion on the approximation capabilities of polynomial regression for the types of dynamics considered, and how the chosen degree of the polynomial impacts the accuracy of the learned model. Furthermore, the convergence properties of the SOS optimization are not discussed, leaving the reader unsure about the quality of the solution obtained.

3.	Experimental issues: In the first paragraph of Experiments (Page 6, lines 294), the neural network consisting of two hidden layers of size 5 is trained with only 5 samples, which arose the problem of underfitting. The maximum number of samples used in the training phase is 11, for such a scare data, the comparison between any neural network-based method with the proposed method is unfair. Additionally, the baselines (PINNs from 2019 and SINDYc from 2018) are relatively outdated. More recent methods, such as Phycrnet, are mentioned in the related work. Besides, in data-scarce settings, traditional linear programming methods like pseudospectral method, optimal control(based on the Pontryagin maximum principle) should be considered. The experimental section also lacks a thorough sensitivity analysis of the hyperparameters used in the proposed method, such as the degree of the polynomial regressor and the parameters of the SOS optimization. This makes it difficult to assess the robustness of the method and its applicability to different problem settings.

### Questions
1.	Why did the authors choose these two specific side-information constraints among all possible options as listed in the reference?

2.	In every experiment, there is only one initial reward matrix. Can the proposed method achieve similar performance with different reward values?

3.	How critical is MPC in this approach? How does the prediction horizon impact performance? It would be helpful if the authors could provide additional experiments to explore this.

### Soundness
2

### Presentation
3

### Contribution
2
