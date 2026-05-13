# How the Level Sampling Process impacts Zero-Shot Generalisation in Deep Reinforcement Learning

- Decision: Reject
- Scores: 8, 3, 6

## Abstract
A key limitation preventing the wider adoption of autonomous agents trained via deep reinforcement learning (RL) is their limited ability to generalise to new environments, even when these share similar characteristics with environments encountered during training. In this work, we investigate how a non-uniform sampling strategy of individual environment instances, or levels,  affects the zero-shot generalisation (ZSG) ability of RL agents, considering two failure modes: overfitting and over-generalisation. As a first step, we measure the mutual information ($\mut$) between the agent's internal representation and the set of training levels, which we find to be well-correlated to instance overfitting. In contrast to uniform sampling, adaptive sampling strategies prioritising levels based on their value loss are more effective at maintaining lower $\mut$, which provides a novel theoretical justification for this class of techniques. We then turn our attention to unsupervised environment design (UED) methods, which adaptively \textit{generate} new training levels and minimise $\mut$ more effectively than methods sampling from a fixed set. However, we find UED methods significantly \textit{shift} the training distribution, resulting in over-generalisation and worse ZSG performance over the distribution of interest. To prevent both instance overfitting and over-generalisation, we introduce \textit{self-supervised environment design} (SSED). SSED generates levels using a variational autoencoder, effectively reducing $\mut$ while minimising the shift with the distribution of interest, and leads to statistically significant improvements in ZSG over fixed-set level sampling strategies and UED methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
One of the fundamental problems in reinforcement learning is generalization of the learned policies to new environments. One solution approach is to use an adaptive sampling strategy over a wide range of environments. However, the level of sampling required to achieve the desired generalization remains unknown. The authors propose a new theoretical framework to answer this question using mutual information and minimization of an upper bound on the generalization error from adaptive sampling. Once this relation is established, now, the authors study the problem of creating new environments systematically and improve generalization. Specifically, the authors propose a self-supervised environment design (SSED) to minimize mutual information for zero-shot generalization. The authors provide a theoretical bound and proof for the generalization gap using mutual information with training level and reinforcement learning policy. Then, use level scores from rollout trajectories to define adaptive sampling distribution. 

SSED consists of two components: a generative phase, in which a variational autoencoder (VAE) is employed as a generative model and a replay phase, in which we use an adaptive distribution to sample levels. The algorithm alternates between the generative and replay phases, and only perform gradient updates on the agent during the replay phase, while the VAE weights remain fixed throughout training. The authors use a complex environment benchmark, ProcGen from OpenAI, and Minigrid, a gridworld navigation domain (ChevalierBoisvert et al., 2018) for empirical evaluation.

### Strengths
Originality & Significance. In some sense, it feels like a no-brainer to use variability in the new environment setup and maximize diversity (minimize mutual information) for better generalization. Similar to classical system identification methods for control systems. I believe the originality comes off from measuring the diversity in the environment to quantify generalization, instead of randomly exploring over a large set of environments. 

Quality & Clarity. The paper is well-written. And the explanations are clear. There are not many grammatical errors. 

The authors baseline their approach to other state-of-the-art approaches.

### Weaknesses
The authors originally use ProcGen to describe some of the concepts but later on all the empirical experiments are in Minigid. While Minigrid is a good toy problem to start with, it lacks the complexity of the most real-world environments where the generalization is the most important. Having to include ProcGen examples would have been a good mid-step towards addressing real-world challenges in generalization to new environments. The choice of Minigrid, while simplifying the experimental setup, raises concerns about the practical applicability of the proposed method to more complex, high-dimensional environments. The generalization capabilities demonstrated on Minigrid might not directly translate to scenarios with richer state and action spaces, and more intricate dynamics. Furthermore, the specific types of generalization challenges present in Minigrid, such as variations in grid layouts and object placements, might not fully capture the diverse range of challenges encountered in real-world applications.

### Questions
I was surprised that while the authors started out with ProcGen, then switched to Minigrid. While the Minigrid provides a good framework as a starting point to showcase the generalization issue, I believe it lacks many of the real-world complexities for generalizing the RL policies to new environments.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to connect a working technique in active domain randomization with a bound on mutual information between histories and contexts/levels. The authors also introduce a method (SSED) to sample more contexts from a similar distribution than the training set by training a VAE on the context-parameters. Both claims are evaluated on maze navigation tasks, which have been modified such that the optimal policy on the training set is not the same as on the entire parameter set. Results show that SSED improves the performance while reducing the optimality gap slightly (but significantly).

### Strengths
The paper introduces a, to the best knowledge of this reviewer, novel concept of over-generalization to the space of all possible parameters. The proposed method SSED is not terribly novel, but makes sense and shows the effect nicely. The open sourced maze environment is another good contribution of the paper.

### Weaknesses
 **TLDR:** the paper is interesting, but in a bad state. On the one hand, it is very confusingly written, overpromises and does not do all it claims. The first contribution is also dubious: the derivation is incomplete (many terms just appear without definition), seem to rely too much on intuition, and the results do not show the effect. On the other hand, the second contribution (SSED) is simple but interesting, and the results demonstrate that it works. Nonetheless, the reviewer cannot recommend to accept the paper in its current form.

1. The paper overpromises many things, for example from the abstract:
	- "As a first step, we measure the mutual information (MI) between the agent’s internal representation and the set of training levels, which we find to be well-correlated to instance overfitting": there is no empirical measurement of MI or its correlation with overfitting in the paper. All evidence is circumstantial and the interpretation of Figure 2, in this reviewer's opinion, wrong.
	- "adaptive sampling strategies prioritising levels based on their value loss are more effective at maintaining lower MI", "We then turn our attention to unsupervised environment design (UED) methods, which [..] minimise MI more effectively than methods sampling from a fixed set.", "SSED generates levels using a variational autoencoder, effectively reducing MI": again, MI is never measured and the claim that the evaluated methods minimize MI is pure conjecture.

2. The paper is confusingly written and introduces many terms without defining them. For example, $\text{MI}(i,\pi)$ is never defined in the main paper. $S^V_i$ is defined with $\hat V_t$ and $V_t$, which have never been defined. On Page 5 the authors state $V_i^\pi(s) = V^\pi(s) + v_i^\pi(s)$, but $V^\pi(s)$ has never been defined (only for a general POMDP, the CMDP only knows context-specific values called $V_{i_x}^\pi$). Sometimes the used PPO baseline uses non-recurrent intermediate representations (p.5), another time the same implementation uses an LSTM-based architecture (which is recurrent, p.7). The reviewer has the impression that many of these details could be understand upon reading the cited papers, but as is, the paper does a poor job explaining them.

3. The connection between generalization, MI and scoring the value loss ($S^V$) is indirect, and not rigorous enough. The connection between MI and generalization is not very clear: in Figure 1 both following the black and the green cells leads to the goal in (a) and (b), but only one of the two generalizes to (c). Both have thus the same MI, but different generalization. While the statement "An agent learning level-specific policies implies high MI between its internal representation and the level identities" (p.1-2) makes generally sense, the conclusion that agents with high MI "will not transfer zero-shot to new levels" is less clear. Moreover, it is not apparent why the negation *agents with low MI generalize well*, which seem to be the basis for this paper, should be true. So the only clear connection seems to be the bound in (eq.2). The reviewer also missed a connection why "Sampling levels associated with highly negative classifier cross-entropies therefore results in less mutual information" (p.5). Finally, the idea that $V_i^\pi(s) = V^\pi(s) + v_i^\pi(s)$ separates into two errors and the second is somehow connected to MI (without any clarification how exactly) is flawed, as the errors of $V^\pi$ and $v_i^\pi$ could also cancel each other out, yielding low error, but high MI.

4. The connection of MI to generalization and to the value-error scoring is not supported by the presented data in Figure 2. Here the first two rows are not significantly different, which would lead to the conclusion that using $S_2=S^{MI}$ does *not* change the algorithm's behavior much. How does this justify the statement "$S = S^V$ therefore appears to strike a good balance between sample efficiency and mutual information minimisation", if MI is not necessary for performance. The third row shows $S^{MI}$ having a smaller generalization gap, but the performance is also much smaller, and these two metrics are highly correlated! The results can therefore also be interpreted as "using MI reduces the performance, and *as a consequence* has a smaller generalization gap". For the same reason the second plot to the right is useless without knowing the algorithms' performances. 

5. The entire Section 4 should be either removed or replaced by an experiment that actually links generalization (not just the generalization gap) to MI, demonstrates or proves that sampling levels with high MI *reduces* the overall MI, and shows a correlation between MI and the value-error score.

### Questions
- The approximation in Lemma 4.1 only works if the levels are constantly sampled with $p(i)$, but your method aims to change this distribution. How does this work when your scoring selects the levels that make up the batch $B$? 
- Your goal is to produce policies that have low MI on the training set, but approximated MI is not used to change the policy, only the sampling of levels. Is there a reason why you do not simply reward actions with lower MI?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers auto-curriculum learning over the minigrid testbed and aims to train a visual policy that can generalize across various generated minigrid levels in a zero-shot manner. The paper first demonstrates the insights that the mutual information between representations and the training level. Then the paper further develops an auto-curriculum algorithm that leverages a smart sampling strategy using a pretrained VAE sampler. By combining both parts, the experiment results suggest strong zero-shot visual generalization can be achieved.

### Strengths
1. I really **appreciate the discussions in Section 4** on the connection of generalization capability and the mutual information between the representation and level identity, which is insightful. The discussion makes the proposed MI criterion natural and intuitive. Although the paper can be much stronger by presenting proof rather than simply stating it as a hypothesis. 

2. **The experiment results look strong**. I also appreciate the discussion on the importance of VAE, which should be crucial intuitively considering the testbed is minigrid. Btw, I personally guess that VAE might be unnecessary if you adopt another testbed with a goal-conditioned flavor (e.g., those environments where you create a new instance by setting a new goal).

### Weaknesses
1. **The presentation can be improved**. There are many notations that are introduced without definitions. For example, in Theorem 3.1 you didn't introduce $L$ (although I can understand its meaning after reading the whole paper). In the paragraph after equation (3), $\hat{V}_t$ is not defined either. The authors seem to have a strong intention to pack a lot of knowledge in Section 3, ranging from notation to existing theorems and algorithms. Section 3 looks a bit messy to me and hard to follow if the reader is not an expert who _masters_ all the related works. I think the section can be much better organized and self-contained. You may want to have some sub-sections with some high-level mathematical descriptions of previous works (in addition to the related work section). Specifically, the lack of explicit definitions for symbols like $L$ in Theorem 3.1 and $\hat{V}_t$ immediately following equation (3) creates a significant barrier to understanding. The rapid introduction of concepts, theorems, and algorithms without sufficient context makes the section feel dense and disorganized, requiring the reader to piece together the meaning rather than having it clearly presented. A more gradual introduction of concepts with clear definitions and motivations would greatly enhance readability. For example, before stating Theorem 3.1, defining $L$ as the set of all possible levels would provide necessary context. Similarly, explaining that $\hat{V}_t$ is an estimated value function at time $t$ would clarify its use. Furthermore, breaking Section 3 into subsections, each addressing a specific aspect (e.g., background on value functions, explanation of the VAE, details of the proposed algorithm) would greatly improve the flow and comprehension. 

2. **citation issues:** Most related works cited in this paper are within the past 3 years. I think the authors ignore a large portion of works in curriculum learning literature, such as those working on goal generation, open-ended learning, and multi-task learning. Although these works do not work on the visual minigrid test, they do share a similar high-level principle to this work and should be acknowledged. For example, the paper states "_we find that strategies de-prioritising levels with low value loss, as **first** proposed in prioritised level replay_". Well, I have to say in curriculum learning, many works have leveraged the idea of using value function as an indicator for prioritization. [Here](https://proceedings.neurips.cc/paper/2020/file/566f0ea4f6c2e947f36795c8f58ba901-Paper.pdf) is an example. I think you can do a brief survey to get more. The claim of novelty regarding de-prioritizing levels with low value loss is overstated, as this idea has been explored in various contexts within curriculum learning. The paper should acknowledge these prior works, even if they don't directly address the visual minigrid testbed. The lack of a broader literature review weakens the paper's contribution and positions it as more incremental than it might be. A more thorough survey would not only strengthen the paper but also provide a better context for understanding the specific contributions of this work. Specifically, the paper should acknowledge the use of value functions for curriculum design in prior works, even if those works do not focus on visual minigrid environments.

2. **minor issues:** Fig 2 is derived from the results of a non-recurrent policy, as stated in the paragraph below equation (7). Why not use an LSTM, as what you have done in the experiments?

### Questions
Although I personally keep a positive perspective on this paper, I would still expect the authors to update the paper for an improved presentation, which can make my judgment firm. 

It would be also great if the authors could further provide more analysis or even theoretical analysis of the hypothesis.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
