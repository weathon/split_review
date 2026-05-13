# Why not both? Combining Bellman losses in deep reinforcement learning

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Several deep reinforcement learning algorithms use a variant of fitted Q-evaluation for policy evaluation, alternating between estimating and regressing a target value function. In the linear function approximator case, Fitted Q-evaluation is related to the projected Bellman error. A known alternative to the projected Bellman error is the Bellman residual, but the latter is known to give worse results in practice for the linear case and was recently shown to perform equally poorly with neural networks. While insufficient on its own, we show in this paper that the Bellman residual can be a useful auxiliary loss for neural fitted Q-evaluation. In fact, we show that existing auxiliary losses based on modelling the environment's reward and transition function can be seen as a combination of the Bellman residual and the projected Bellman error. Experimentally, we show that adding a Bellman residual loss stabilizes policy evaluation, allowing significantly more aggressive target network update rates. When applied to Soft-Actor Critic---a strong baseline for continuous control tasks---we show that the target's faster update rates yield an improved sample efficiency on several Mujoco tasks, while without the Bellman residual auxiliary loss, fitted Q-evaluation would diverge in several such instances.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes using the Bellman Error (BE) as an auxiliary loss in combination with the Projected Bellman Error (PBE) for Fitted Q-Evaluation (FQE). When the action-value function $Q(s,a) = \Phi w$ is expressed as the product of a learnable feature vector $\Phi$ and a learnable weight $w$, we can find the parameters $w$ minimizing the PBE in closed form by following the standard LSTD solution. Meanwhile, the feature vector $\Phi$ can be minimized using the BE. The authors suggest an adaptation of FQE that iteratively minimizes these two objectives. They provide an upper bound of the BE loss when $w$ is the solution of the PBE, which depends on the reward function and the next state-action feature. For practical implementation, they propose a model-free algorithm that does not require estimating these quantities. Experimental results demonstrate that the addition of a BE auxiliary loss makes the Soft Actor-Critic algorithm more stable, especially when increasing the number of gradient steps before updating the target network, resulting in improved sample efficiency.

### Strengths
- The paper offers a comprehensive and clear presentation of the differences and relationship between the Bellman Error and the Projected Bellman Error.

- To my knowledge, the application of the BE as an auxiliary loss alongside the PBE loss is a novel approach.

- The experiments show a decrease in distance to the true Q function for the proposed method and an increase in sample efficiency, which shows that the proposed auxiliary loss can be effective in practice

### Weaknesses
- The presentation related to the theoretical results is, in general, clear, apart from equation 13: what are $m_r$ and $M_{\Phi}$?

- In the paper, it is claimed that the proposed method allows for more aggressive target network update rates. However, from the text, I could not understand what exactly that means: is it the case for DouBel(20) or DouBel(1). This generated some confusion throughout the text. I suggest to add an explanation in the text on how target networks are used and why they are important in this setting.


- The paper lacks a simple experiment (e.g., with finite state and action spaces) where the theoretical results can be shown to hold true without approximating the solution of LSTD. It would be beneficial to demonstrate how the auxiliary loss aids such settings before introducing approximations.

- From Table 1, it seems that both DouBel(20) and FQE(20) have much lower loss than DouBel(1) and FQE(1). I would expect to see for some of the datasets presented a plot showing the final distance to the true Q function as a function of the number of gradient steps before the target network is updated (e.g., from 1 to 40). Is the loss in DouBel always lower than the loss in FQE, or is there a trade-off?

- It is not clear to me how the theoretical results imply that the algorithm can have more aggressive target network update rates. I understand that the use of the auxiliary loss can decrease the error in the Q function. However, could the author clarify why this matters when having more target network updates?

### Questions
I incorporated most of the questions above. Other minor questions:

- What is the difference between Figures 6, 7, and 8? 

- Why is there an initial divergence in Figure 4 for SAC, and how does it relate to the theoretical results?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the use of projected Bellman error (PBE) or the mean squared Bellman Error/Bellman residual (BE). the authors show that although BE is not great on its own, it can be a useful auxiliary loss for neural fitted Q-evaluation. Authors provide theoretical results show that existing auxiliary losses that model reward and transition dynamics can be seen as a combination of PBE and BE, and this motivates the design of a new auxiliary loss, the Double Bellman (DouBel) loss. Empirical results are further provided to show that by using the proposed loss on SAC, it is possible to achieve better loss and performance on MuJoCo benchmark, and allow a more frequent target network update.

### Strengths
**originality**
- the paper presents a very interesting novel insight making connection between the Bellman losses and the commonly used forward dynamics and reward prediction auxiliary losses. 
- empirical results are provided to further support the theoretical results.  

**quality**
- the writing and structuring of the paper are good. 
- good covering of related works 
- the proposed method is well-motivated.
- many technique details are provided, enough seeds are run

**clarity**
- the results and arguments presented in the paper are clear and easy to follow
- figures and tables are clear

**significance**
- the theoretical insight in the paper is quite interesting. 
- the empirical results show that the proposed method can indeed achieve better performance and smaller losses. When comparing to SAC, the proposed method is less prone to divergence and can allow faster target network updates. The proposed method can be a nice way to improve algorithm stability. And I believe this applies to not just SAC but other related algorithms as well.

### Weaknesses
I think the paper is very interesting but can be nice to see a bit more empirical study and analysis. 
- To my understanding, a hyperparameter (lambda in algorithm 2) is used to balance how much auxiliary loss to use, can you provide more ablation on how the algoirthm's behavior and how the accuracy of its Q estimates change as lambda changes? 
- In some recent works it has been shown that techniques that provide more accurate Q estimates can be especially helpful when the algorithm is taking more udpates per data point collected. Will the proposed method also benefit from this setting? 
- How much computation overhead does the proposed method have? Would like to see a table comparing wall clock time between it and SAC baseline. 
- Will the proposed method also lead to better long-term performance?

### Questions
- Given the same computation budget, will the proposed method be more efficient compared to methods with other auxiliary losses or with ensemble-based bias reduction? 
- Will it be beneficial to combine the proposed method with other auxiliary losses or other bias reduction techniques, or that does not make sense?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to use residual algorithms, which have some nicer theoretic properties but have often performed worse in practice, especially with deep networks. The proposed resolution is derived as follows.

We can first decompose a deep NN $Q(s,a)$ into $\phi \cdot w$ where $\phi$ is a feature vector and $w$ are the linear weights. The w can be viewed as the final layer of an NN which is usually linear. Assume a discrete state and action space, the $\phi$ can define a $\Phi$ "feature matrix" of size $|S x A| x K$ where $K$ is the dimensionality of the feature layer. This is mostly for notation purposes and such a $\Phi$ is never instantiated in practice except for toy problems.

The projected bellman error $||Q - T^\pi Q||$ can be rearranged $||\Phi w - T^\pi Q||$. Following prior work, we can demonstrate that this error can be upper bounded by a model learning loss $L(\phi)$, where $\phi$ are the latent features of the model, and the loss is defined by how well $\phi$ can model the reward function / features of the next state assuming an optimal $w$ for said $\phi$. If I understand the argument correctly, this has not gotten to the new proposed part of this work and is summarizing prior work. The key point is that it shows adding auxiliary model-based losses to a model-free RL algorithm is theoretically justified (and that such losses would be applied to the feature space $\phi$ and ignore updating the final linear weights $w$)

The proposal of this work is to not explicitly use a model-based auxiliary loss. Instead, we should just use something like the Bellman error as an auxiliary loss. We are already using a standard TD-error as our "base" RL loss, but we can take the Bellman residual objective and use this as the aux. loss. Inspired by feature learning work, we only allow this aux. loss to affect the feature layers (every layer except the last one). This still runs into the classic double sampling bias, which we can either choose to correct for or not.

### Strengths
The paper provides a helpful primer on Q-learning literature, in particular on the notation norms for considering the $\phi$ vs $w$ decomposition. I appreciate that the plots have error bars and the empirical improvements over baseline SAC seem slightly promising.

### Weaknesses
I may be a bit out of the loop on the MuJoCo test suite, but I thought the typical number of environment steps needed per run was on the order of 10^6 steps or higher. But the methods appear to only be benchmarked up to half of that number? This makes me a little suspicious of the results.

From a style standpoint, I'm not sure the theoretical discussion in Section 3 is that helpful and the presentation seems a bit poor. This could be down to me not understanding the paper, but it felt like this:

Figure 1 - a diagram of projection error that has little to do with the proposal to use Bellman residual as an auxiliary loss.

Section 2.1 - A discussion on true bellman error vs projected error, which also has little to do with the bellman residual proposal.

Section 3 - A discussion on feature space learning, where we spend multiple paragraphs and lines of equations deriving losses that show learning good features can improve RL, before saying "but this should be worse than using the Bellman error, let's do something else", which felt a little like it was wasting my time.

The practical implementation of Bellman residual is only brought up around Section 4 and does not seem that related to the sections that come before it.

In terms of experiments, separate from the "seems like too few steps" question, it feels like the paper's argument would be stronger if it included more alternatives for feature learning in the practical section. In Table 1, the BC baseine is good, because it is using a different auxiliary loss than DouBel, and it gives an argument for why DouBel's bellman residual aux. loss is better than a next-state-feature + reward approximation loss. But this table is only for policy evaluation, and then there are no aux. feature methods in Table 2 (episode return) aside from DouBel! So I don't see evidence that DouBel is better than othr auxiliary losses when maximizing episode return, I only see evidence it is better than no aux loss at all.

I think the experiments do support better policy evaluation, but they don't support better policy learning strongly enough. This combined with some of my complaints on presentation make me a bit lukewarm about the work, even if there are some good parts within it.

### Questions
I may have missed this - in the feature function gradient, how is $\lambda$ defined? Is this a hyperparameter fixed during learning, or is it something implicitly defined by $||w||$ to match Eqn 13?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Some reinforcement learning algorithms usually use a variant of fitted Q-evaluation for policy evaluation, alternating between estimating and regressing a target value function. Based on the prior work, it seems that the Bellman residual can incur poor performance in the linear case or with the neural networks. This paper uncovers that the Bellman residual can be utilized as a useful auxiliary loss for neural fitted Q-evaluation. The authors experimentally show that adding a Bellman residual loss stabilizes policy evaluation. The authors combine the Bellman residual loss with the SAC algorithm, and observe an improved sample efficiency on some tasks while FQE can diverge without the Bellman residual loss.

### Strengths
# Strengths

- this paper is highly related to the RL community, especially focusing on the fitted Q evaluation problem

- this paper is generally well-written and well-motivated

- this paper unpacks an interesting conclusion, that the Bellman residual loss can serve as a quite good auxiliary loss for the benefit of improving the sample efficiency. The authors show that utilizing the combination of the projected Bellman error and the Bellman residual can be a better choice.

-  codes are included

### Weaknesses
# Weaknesses

- The authors ought to present the theoretical analysis more formally and organize them into theorems like many FQE papers do

- The authors ought to list a detailed hyperparameter setup table in the appendix for clarity

- The hyperparameter $\lambda$ seems to be important and the most critical part of the proposed method. While I do not see enough discussions on this hyperparameter. The authors use different $\lambda$ for different tasks or when combined with different algorithms. It is important to give practical guidance on how to determine this parameter

- Are there any way of tuning this parameter (i.e., $\lambda$) automatically? How does this hyperparameter affect the performance? How sensitive is the method to this parameter? Have you try some other datasets other than MuJoCo? Can your conclusion still hold?

- The authors only combine their method with SAC, then can your method benefit more advanced algorithms like TQC [1], REDQ [2]?

[1] Controlling overestimation bias with truncated mixture of continuous distributional quantile critics. ICML.

[2] Randomized ensembled double q-learning: Learning fast without a model. ICLR.

- Can your method still work when there are already some regularizations on the critic, e.g. DARC [3]? What trade-off we may need to balance the introduced residual loss part and the existing regularization part? I expect some further discussions on this.

[3] Efficient continuous control with double actors and regularized critics. AAAI.

### Questions
Please refer to the weaknesses part

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
