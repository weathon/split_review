# Uncertainty-aware Constraint Inference in Inverse Constrained Reinforcement Learning

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Aiming for safe control, Inverse Constrained Reinforcement Learning (ICRL) considers inferring the constraints respected by expert agents from their demonstrations and learning imitation policies that adhere to these constraints. While previous ICRL works often neglected underlying uncertainties during training, we contend that modeling these uncertainties is crucial for facilitating robust constraint inference. This insight leads to the development of an Uncertainty-aware Inverse Constrained Reinforcement Learning (UAICRL) algorithm. Specifically, 1) aleatoric uncertainty arises from the inherent stochasticity of environment dynamics, leading to constraint-violating behaviors in imitation policies. To address this, UAICRL constructs risk-sensitive constraints by incorporating distributional Bellman updates into the cumulative costs model. 2) Epistemic uncertainty, resulting from the model's limited knowledge of Out-of-Distribution (OoD) samples, affects the accuracy of step-wise cost predictions. To tackle this issue, UAICRL develops an information-theoretic quantification of the epistemic uncertainty and mitigates its impact through flow-based generative data augmentation. Empirical results demonstrate that UAICRL consistently outperforms other baselines in continuous and discrete environments with stochastic dynamics. The code is available at https://github.com/Jasonxu1225/UAICRL.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents UAICRL, a novel approach for addressing Inverse Constrained Reinforcement Learning (ICRL) by considering both aleatoric and epistemic uncertainties. UAICRL leverages a distributional critic in conjunction with a risk-measure to calculate the cost, so as to handle aleatoric uncertainty. In addition, it utilizes mutual information and flow-based trajectory generation techniques to reduce epistemic uncertainty. The experimental results demonstrated improved performance and included ablation studies on the use of risk-sensitive constraint and data augmentation.

### Strengths
- Addresses both aleatoric and epistemic uncertainty, in contrast to previous methods that primarily focus on epistemic uncertainty.
- Works with both continuous and discrete spaces, unlike most previous methods limited to discrete spaces.
- Supports stochastic training environments, whereas earlier works frequently assume deterministic environments.

### Weaknesses
1. The ablation of the mutual information term in Eq. (7) results in a configuration where only the risk-sensitive constraint from Eq. (4) is utilized. This particular setup is not discussed in the paper.
2. I'm concerned about expanding the dataset by generating trajectories based on a learned flow function. It is still possible for the flow function to generate out-of-distribution data.

### Questions
1. I'm wondering if the flow functions can be substituted with other conditional generative models, or if the flow matching objective is tightly coupled with UAICRL. For example, can one use a conditional diffusion model to replace the Flow-based Trajectory Generation (FTG) algorithm?
2. While Table B.1 suggests that FTG can maintain consistent hyperparameters across various tasks, I wonder how the performance of UAICRL might be influenced by the selection of hyperparameters for the FTG network. This concern arises from the potential of FTG to either underfit or overfit, which could lead to generating out-of-distribution trajectories and potentially causing a decline in overall performance. Could you explain the process of tuning the hyperparameters for the FTG network?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers addressing the uncertainty issues in the inverse constrained RL problem. The authors propose to (1) replace cost critic by a distributional one in constrained RL to model the aleatoric uncertainty, and (2) use FTG to augment data to reduce epistemic uncertainty. The authors compare their method with previous inverse constrained RL baselines on different domains including gridworld, safety-mujoco and highway driving.

### Strengths
- This paper is well organized and easy to follow.
- The proposed method addresses two types of uncertainties in constrained RL, which are overlooked by previous research.
- The ablation studies validate the effectiveness of distributional critic when encountering aleatoric uncertainty.

### Weaknesses
 - The effectiveness of data augmentation is a little questionable.
    - In theory, FTG can augment the expert and nominal datasets but the last term in the objective of eq.(8) includes the OOD trajectories $\bar{\tau}$. So how do you generate $\bar{\tau}$?
    - In practical experiment (fig 3), UAICRL actually performs similarly to UAICRL-NDA, which removes the data augmentation part. 
    - Although the authors give more illustrations in fig.7 (I suppose the top is for MEICRL and bottom is for UAICRL), I think it's not very clear. For example, I believe the authors should at least explain what the generated trajectory is, and which parts are OOD.

minor issues:
- In fig 4, the baseline should be "GACL" instead of "GAIL".



### Questions
- What are the target cost limits $\epsilon$ for experiments in table 2, fig 3&5?
- Why are some experiments early stopped when they obviously have not converged? E.g., in fig.3&4.
- The authors run experiments on Mujoco tasks with different scales of stochasticity in env. But many baselines have much higher constraint violation rate with smaller noise, e.g., comparing fig.3, D3&D4. My intuition is that these methods should behave better with smaller noise as they cannot model such uncertainty. Could you explain it?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a thorough discussion on the topic of inverse safe reinforcement learning. The authors introduce the Uncertainty-Aware Constraint Inference Constrained Reinforcement Learning (UAICRL), a novel framework that takes into account both aleatoric and epistemic uncertainties to enhance uncertainty awareness in constraint inference. The authors conducted extensive experiments to demonstrate the superior performance of their method over several other ICRL methods in both continuous and discrete environments, highlighting its strong uncertainty-aware capabilities.

### Strengths
(1) Noteworthy topic: The study on Inverse Constrained Reinforcement Learning appears to address a critical issue, and the proposed method holds promising potential for real-world applications. 

(2) Extensive experimental validation: The authors' extensive experiments with a wide range of baseline methods and tasks to demonstrate the strength of their approach are commendable and impressive.

### Weaknesses
 (1) Insufficient theoretical support: It is observed that the proposed method may benefit from further strengthening its theoretical foundations, as acknowledged by the authors. 

(2) Limited discussion and explanation of experiments: While the manuscript presents extensive experimental results, a more comprehensive discussion and elaboration of these findings would enhance the paper's overall quality. Moreover, a detailed examination of performance across various scales of randomness within the primary context could provide valuable insights, as noted in my question (1-3).

### Questions
(1) Could you please explain the reason behind the divergence trend observed in the UAICRL method in section 6.2, particularly in the Blocked Walker task? Additionally, would it be possible to provide results with an extended number of epochs? Were the curves smoothed in your analysis? 

(2) What factors contribute to the challenges posed by the Blocked Swimmer task? It seems that most methods struggle to learn a safe (low-cost-violation) policy for this specific task. 

(3) Could you elaborate on the factors leading to the relatively unsatisfactory results of the baseline methods in the tasks? Specifically, what could explain the discrepancy in the performance of GACL, which performs well in the Block Ant task but not in other tasks shown in Figures D.3 and D.4? 

(4) How would you describe the generalizability of your method to multi-cost settings?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is interested in Inverse Constrained Reinforcement Learning (ICRL), that is, simultaneously learning imitation policies whilst learning and adhering to the constraints respected by the expert.
The authors propose to incorporate the uncertainties arising from stochastic environments (aleatoric uncertainty), along with
the epistemic uncertainties arising from learning from limited data.
To this end, they propose to learn the cost model with distributional Bellman updates.
They then propose a flow-based generative data augmentation scheme to mitigate issues arising from epistemic uncertainty.
That is, the augmented trajectories should remain in regions of the learned model which can be predicted confidently (low epistemic uncertainty).
The method is tested in i) a discrete-action grid world environment and ii) five MuJoCo environments with additional noise.

### Strengths
Although I am not well-read in Inverse Constrained Reinforcement Learning (ICRL), this paper appears to have highlighted
an important problem: imitation policies should satisfy the learned constraints subject to both the uncertainty in the environment (aleatoric uncertainty) and the uncertainty arising from learning the constraint from limited data (epistemic uncertainty).
Capturing the aleatoric uncertainty with distributional Bellman updates seems like a good idea and makes sense intuitively.
Whilst I found the flow-based trajectory generation section hard to follow, I get the general idea and this seems like a sensible way to consider the epistemic uncertainty.
I also liked that throughout the paper the authors provide intuition for the math with real-world examples. This was nice.

### Weaknesses
The paper's biggest weakness is its presentation and clarity.
I was generally happy with the paper up until Section 6 (Empirical Evaluation).
I found this section particularly hard to follow.
I'm not entirely sure what the main points are that the authors are trying to show in this section.
I would suggest the authors try to summarize the main questions and introduce them at the start of section 6.
This gives the reader an idea of what to expect in the section, which makes for an easier read.

**Experiments**
Remember, readers are stupid, you should hold their hand and walk them through your figures.
For example, what does robust and superior performance allude to in this sentence:
"When implementing both techniques, UAICRL demonstrates even more robust and superior performance compared to other methods."
This could be made a lot easier for the reader with something like:
"When implementing both techniques, UAICRL (pink) generally obtains high feasible rewards (top row Fig. 3) whilst having a low constraint violation rate (bottom row Fig. 3). This demonstrates that UAICRL is more robust and has superior performance compared to other methods."

**Illegible figures**
Most figures are illegible due to being too small and the font size being too low.
This needs to be fixed before publication.


**Conclusion is very short..**
The conclusion is very short and feels rushed. Surely the authors have more to say here??

**Bolding**
What does the bolding in the tables show? Does it show statistical significance from a statistical test or something else? This should be clarified somewhere in the text.

**Code**
There is no README file in the code supplement so it is not clear how to setup the environment or how to run the experiments.
It would be good to at least have a notebook to see how the code/method works in practice.

In my opinion, the paper highlights an important problem, has a good technical contribution and has results which support the claims.
However, I do not think the paper can be published until:
- The experiments section is made clearer
- The figures are made legible
- The conclusion is written properly

**Minor corrections**:
- The paper has many textual citations in parentheses. For example "(Liu et al., 2023; Papadimitriou et al., 2023)" in paragraph 3. You should use \citet instead of \citep to remove the parentheses.
- In Section 2, what is $\mathcal{M}^{c_{\omega}}$? It's not defined anywhere.
- Figure 1.
  - The text is way too small.
  - It's also not clear where to start reading from. I think you should start reading from $\mathcal{D}_{e}$ so perhaps this should be mentioned in the caption.
- Page 3 footnote is missing a full stop.
- Section 4.2
  - $\mathcal{T}$ is never formally introduced.
  - $F(\cdot)$ is overloaded and confusing as it is shown as $F(\tau)$, $F(s_{t})$ and $F(s,a)$. I think you should distinguish the state flow $F(s_{t})$ from the trajectory flow function.
- Algorithm 1:
  - Does "sample nominal trajectories" imply interacting with the environment? If so, I would explicitly state this.
  - Is it right that the augmented data is discarded at each iteration?
- Table 1 text is way too small
- Figure 2 needs larger text
- Figures 3/4/5/D.3/D.4/D.5/D.6
  - Larger text
  - It only needs one legend.
  - The x-axis ticks are too close
  - The plot titles don't all need to say "with noise $\mathcal{N}(0,0.1)$"
- Figure 6 is not clear.
  - Each column refers to a grid world scenario so this should be on the figure and/or mentioned in the caption.
  - The text is way too small
  - What are the constraints locations???
  - Where does the agent start/end?
- Figure 7 is not clear.
  - Each column refers to a grid world scenario so this should be on the figure and/or mentioned in the caption.
  - What does each row represent? Is the top row ICRL and the bottom row UAICRL? This needs to be made clearer.

### Questions
- What are the main questions your results section is trying to answer? Can you summarize them in a few bullet points?
- Have you made the figures legible?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
