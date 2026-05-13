# Sinkhorn Distributional Reinforcement Learning

- Decision: Reject
- Scores: 3, 8, 5, 6, 3

## Abstract
The empirical success of distributional reinforcement learning~(RL) highly depends on the representation of return distributions and the choice of distribution divergence. In this paper, we propose \textit{Sinkhorn distributional RL~(SinkhornDRL)} algorithm that learns unrestricted statistics, i.e., deterministic samples, from each return distribution and then leverages Sinkhorn divergence to minimize the difference between current and target Bellman return distributions. Theoretically, we prove the convergence properties of SinkhornDRL in the tabular setting, which is consistent with the interpolation nature of Sinkhorn divergence between Wasserstein distance and Maximum Mean Discrepancy~(MMD). We also establish a new equivalent form of Sinkhorn divergence with a regularized MMD beyond the optimal transport literature, contributing to interpreting the superiority of SinkhornDRL over existing distributional RL methods. Empirically, we show that SinkhornDRL is consistently better or comparable to existing algorithms on the suite of 55 Atari games.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new projection method for distributional reinforcement learning, which utilizes Sinkhorn divergence to learn the target return distribution.

As two popular existing distributional RL methods, QR-DQN and MMD_DRL provide $N$ return value outputs in terms of quantile and Dirac function respectively, the proposed method SinkhornDRL uses this neural network architecture to represent the return distribution and learn the return distribution function by the proposed Sinkhorn divergence loss function.

Theoretically, this paper extends the result of MMD-DRL into proving the convergence property of the return distribution in terms of Sinkhorn divergence.

In the experiment, the authors provide the result of Atari-55 performance within 40 million steps, where the number of compared baselines is not enough to show the superiority of the proposed method.

### Strengths
The propsed sinkhorn divergence based Bellman update loss includes the regularization loss which is the mutual information of a given distribution and the target distribution.

This makes the above two distributions statistically independent, and the reguarlizaiton loss with the coefficeint $\epsilon$ helps to increase the interquantile mean performance of atari-55.

### Weaknesses
The main theoretical contribution can be seen as a simple combination of the architecture of MMD DRL and Sinkorn divergence. The additional KL divergence term (mutual information) in the proposed loss is a key factor to improve the DRL algorithms except for two corner cases $\epsilon=0,\infty$. However, the role of this proposed element is not well explained in the main text. The detailed comments are as follows. The main strength statement in this paper is that Sinkhorn divergence can be useful in the complex environments with high dimensional action space. This discussion is not rigorous, because I cannot find any explanation why the mutual information between two return distribution and the dimension of action space is related.

I also have the following minor concerns.

1. It is hard to get an insight by introducing the Sinkhorn divergence. For example, the paper of MMD DRL provides the figure that explains the propsed scheme can estimate the high order moments better than the existing methods.
2. The main ablation study (sensitivity anlysis) is provided without any detailed discussion. The authors states taht the property of loss changes as the value of $\epsilon$ changes in the main theorem, but the empricial analysis and discussion is not provided well. 
3. The experiment protocol in this paper is not standard. Previous works almost conducted in 200M iterations or the authors could have chosen the protocol of the paper, DRL at the edge of statistical precipice to validate the performance.
4. In table 2 and Figure 2, the propsed method outperforms in terms of mean score but not in median score than baselines, and the proposed method show remarkable performance in venture and sequest. This means that the proposed method is not a generally better algorithm but a specialist for Venture and Sequest. In my point of view, the authors should have stated why the propsee method is better in such envs.
5. There exists more projection method for distributional RL such as EDRL [A], but the provided baselines is not enough.

### Questions
I mentioned my main concern in the weakness part. Please refer the weakness section.

In addition, it is hard to understand that reducing the mutual information helps to build a better projection operator.
Can the authors provide detailed explanation why the mutual information between the return distribution and target distribution is important?
In my point of view, the unresticted statistics can be constructed better, because its deterministic samples can be more uncorrelated by reducing the mutual information.
If it is true, the main effect seems related to the sampling scheme, not the discrepency between two ground-truth return distribution.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Much of the success of distributional RL is dependent upon how the return distributions are represented and which distribution divergence criteria is used. The authors propose a new variant of distributional RL called Sinkhorn DRL which uses Sinkhorn divergence as the distribution divergence criteria. The authors also provide theoretical proofs of the convergence properties of Sinkhorn DRL. The authors perform experiments that show the superiority of SinkhornDRL to current state of the art DRL algorithms on 55 different Atari games.

### Strengths
The authors did a great job giving background information on sinkhorn divergence and providing theoretical analysis to strengthen their argument. They also provided the necessary details for the experiments.

### Weaknesses
The discussion section is rather short, but I understand that this is due to the page limit and the authors giving preference to the more important sections of the paper.

### Questions
Why were only 3 seeds used during training? Was this due to more of a time/resource constraint?

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a theoretical and empirical study of
distributional reinforcement learning algorithms where return
distributions are trained to minimize a Sinkhorn divergence, a
divergence measure closely related to the entropically-regularized optimal
transport cost. The authors establish that the distributional Bellman operator is a
contraction under the Sinkhorn divergence, which justifies use of
a Sinkhorn divergence loss for distributional policy
evaluation. Moreover, the authors demonstrate that their
implementation of "Sinkhorn Distributional RL" performs well in the
Atari suite, matching or outperforming competing algorithms in many games.

### Strengths
Sinkhorn divergence/entropically-regularized OT are an important class
of divergence measures on the space of probability distributions,
particularly with regard to computational efficiency and numerical
stability. This paper is the first, to my knowledge, to formally study
these for the purpose of distributional RL. The empirical analysis is
rigorous and interesting.

### Weaknesses
The main issues I have with the paper, which I will expand upon
further below, are the following,

1. The writing/organization can definitely use some work -- some parts
   of the text are awkward to read / not easy to follow.
2. I have some concerns about the proof of Theorem 1. Ultimately, I
   believe the claims are correct, but there are some parts that are
   less clear that should be clarified.
3. Overall, the math tends to be quite sloppy. There is lots of abuse
   of notation, some terms are not clearly defined, and that makes
   some of the steps very difficult to follow (maybe this alone can
   clarify my concerns about Theorem 1).
4. Some of the empirical results seem potentially misleading.

Some more explicit details follow.

The paragraph labeled by "Advantages over Quantile-based / Wasserstein
Distance Distributional RL" is highly unpleasant to read. The "inline
bulletpoint" style is not very easy to follow. Some concepts here are
not defined, which limits the utility of this paragraph for motivating
SinkhornDRL.

Regarding the contraction factor $\Delta(a,\alpha)$, it would be nice
if there was an explicit upper bound given (perhaps in terms of the
range of returns). The fact that this term is strictly less than 1
relies on some discrepancy between Wasserstein and entropy-regularized
Wasserstein, and it is not intuitive to me how large that discrepancy
is. Should we expect $\Delta(\gamma,\alpha)$ to be larger or smaller
than, say, $\gamma$ or $\sqrt{\gamma}$?

Regarding the empirical results, it is slightly unsettling that Table
2 reports only the statistics of the "Best" scores. In fact, it is not
actually clear to me what that means.

Moreover, the "ratio improvement" figures only show results for games
where SinkhornDRL outperforms its competitors (and the selection of
games varies per competitor). The corresponding plots in the Appendix
(where the human normalized score is shown for each game) shows that
SinkhornDRL really only outperforms its competitors on roughly half
(maybe slightly less than half) of the games.

## Proof of Theorem 1
I don't understand the proof of part 1, and the math is fairly
imprecise. For instance, the definition of convergence that is
leveraged between $\mathcal{W}^{c, \epsilon}$
and $\mathcal{W}^\alpha$
is sloppy -- it is being written like as if these are scalar
functions, but they are not. Is the convergence uniform? Also,
equation (14) does not establish the contraction any better than the
claim that $\mathcal{W}^{c,\epsilon}\to\mathcal{W}_\alpha$ does, in my
opinion. You still haven't shown a contraction here. That said, I
believe the claim is true. Same comments for the proof of part 2.

The correctness of the proof of part 3 relies on a hypothesis that the
optimal coupling for $W_\alpha$ and $W^{c,\epsilon}$ cannot be the
same (otherwise, step (b) of equation (21) can be an equality). Is it
known that this hypothesis is true? If so, I think this should be
cited.

## Minor Issues
In the last sentence of the "Quantile Regression (Wasserstein
Distance) Distributional RL" paragraph (page 3), "while naturally
circumstances the non-crossing issue" should probably say "while
naturally circumventing the non-crossing issue".

In the output of Algorithm 1, I believe the second argument to
$\overline{\mathcal{W}}^{c,\epsilon}$ should be $\{\mathcal{T}Z_j\}_{j=1}^N$.

Above equation (4), "supreme form of Sinkhorn divergence" should be
"supremal form of Sinkhorn divergence".

### Questions
What is the non-crossing issue?

Why is a sample/particle representation "more flexible" than modeling
quantiles?

Why does the RKHS nature of MMD imply failure to capture geometry?
RKHS are Hilbert spaces after all.

### Soundness
2 fair

### Presentation
1 poor

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
This paper focuses on solving online reinforcement learning using a distributional reinforcement learning formulation. It proposes a new algorithm called Sinkhorn distributional RL (SinkhornDRL) which: from the theory side, it enjoys the contraction property of the corresponding distributional Bellman operator; and empirically outperforms existing distributional RL baselines.

### Strengths
1. The algorithms show competitive results compared to existing distributional RL algorithms in the widely used benchmark 57 Atari games
2. It theoretically shows the contraction property of the distributional Bellman operator and the corresponding theoretical convergence of SinkhornDRL
3. The empirical analysis is sufficient regarding sensitivity analysis of the hyperparameters, computation cost, and etc.

### Weaknesses
1. The presentation needs to be polished since a lot of notations have not been introduced and may not be reading-friendly for people who are not familiar with distributional RL literature, as listed later.
2. The introduction of the algorithms seems not sufficient, for instance, what is the next step after getting the Sinkhorn distance in algorithm 1, such as gradient descent or other to minimize this distance?
3. Section 4.2 has a sequence of theoretical results, while more intuition will be helpful, such as the term $\overline{\Delta}(\gamma, \alpha)$ in Theorem 1(3) is represented in a very complicated way. So what do these terms mean and how large are they will be more helpful for the readers? So as the relationships to Gaussian or general kernels.

### Questions
1. As Sinkhorn is a well-known approach in optimal transport literature, it is curious what is the technical contribution of this paper, is it just an RL application inspired by Sinkhorn?

Other small issues:
1. Section 2.1, using $\overset{D}{:=}$ without defining the notation of D.
2. $Z_{\theta^\star}$ has not been introduced

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces the Sinkhorn distributional RL algorithm, which uses sinkhorn divergence to minimize differences between the current and target return distributions. Theoretical proofs show some properties of sinkhorn divergence and confirm its convergence properties. Empirical tests on Atari games show that the algorithm outperforms or matches existing distributional RL methods.

### Strengths
The paper is well-written and easy to follow, and the use of sinkhorn divergence is novel and interesting. It is complete and has both the theoretical part and the experimental part.

### Weaknesses
 - I am not quite convinced by the experimental results. Specifically, Figure 5 and the subsequent remark indicate that "sinkhornDRL achieves better performance across almost half of the considered game". However, it might be possible that both QRDQN and MMD each excel in roughly 50% of the games over the other. Consequently, sinkhorn should, on average, surpass either of the two in 50% of the games, as Sinkhorn essentially interpolates between these two algorithms. Observing Table 3 seems to draw the same conclusion: when Sinkhorn outperforms QRDQN, it often falls to MMD; conversely when it outperforms MMD, it tends to underperform relative to QRDQN. However, I admit that this is not absolute, as there are indeed some games where Sinkhorn surpasses both. But my concern is whether "better performance across half of the games" is enough.

- The kernel assumed in the theoretical part (e.g., theorem 1) is different from that used in the experiments (the Gaussian kernel). So I am not sure how are the theory and the experiments connected.

- There seem to be some related works that are missed. I'm not sure if all of them are relevant, but the author can check if they are related. Some remarks are attached to each of them.

  - Li, Luchen, and A. Aldo Faisal. "Bayesian distributional policy gradients." : this paper proposes the policy gradient for distributional RL, and they use Wasserstein distance as well.

  - Wu, Runzhe, Masatoshi Uehara, and Wen Sun. "Distributional Offline Policy Evaluation with Predictive Error Guarantees." : this paper considers the total variation distance, which seems to be stronger than both Wasserstein distance and MMD. Hence I am wondering if it is also stronger than the sinkhorn divergence.

  - Ma, Yecheng, Dinesh Jayaraman, and Osbert Bastani. "Conservative offline distributional reinforcement learning." : this paper learns conservative return distributions, which seems necessary in the offline setting. Their theoretical guarantees are also under the Wasserstein distance.

  - Rowland, Mark, et al. "An analysis of quantile temporal-difference learning." : this paper studies the convergence of the quantile TD algorithm, and thus you may want to compare your analysis with theirs. They also established the fixed point error guarantee, and I am not sure if the same thing holds under sinkhorn divergence.

### Questions
- I really appreciate that the author established some nice properties of sinkhorn divergence (e.g., theorem 1, proposition 1). However, it is still unclear to me why the authors proposed to use sinkhorn divergence. They claimed that it is an interpolation between Wasserstein distance and MMD, and thus, I am wondering why it is expected to be better.  It would be great if the authors could provide a more either rigorous or intuitive explanation.

- The author proposed to generate finite samples to approximate the distribution (algorithm 1). Hence, I think a question is how large the statistical error will be, i.e., what is the error incurred when learning from finite samples, as compared to learning from the true distribution? Furthermore, how do these errors accumulate within an MDP? This may be a bit beyond the scope of this paper, but it will be interesting to see how statistically robust sinkhorn divergence is to finite samples intuitively.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
