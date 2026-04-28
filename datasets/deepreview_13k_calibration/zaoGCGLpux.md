# RETHINK MAXIMUM STATE ENTROPY

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 8, 3, 3

## Abstract
In the absence of specific tasks or extrinsic reward signals, a key objective for an agent is the efficient exploration of its environment. A widely adopted strategy to achieve this is maximizing state entropy, which encourages the agent to uniformly explore the entire state space. Most existing approaches for maximum state entropy (MaxEnt) are rooted in two foundational approaches, which were proposed by Hazan and Liu \& Abbeel, respectively. However, a unified perspective on these methods is lacking within the community.

In this paper, we analyze these two foundational approaches within a unified framework and demonstrate that both methods share the same reward function when employing the $k$NN density estimator. We also show that the $\eta$-based policy sampling method proposed by Hazan is unnecessary and that the primary distinction between the two lies in the frequency with which the locally stationary reward function is updated.  Building on this analysis, we introduce MaxEnt-(V)eritas, which combines the most effective components of both methods: iteratively updating the reward function as defined by Liu \& Abbeel, and training the agent until convergence before updating the reward functions, akin to the procedure used by Hazan. We prove that MaxEnt-V is an efficient $\varepsilon$-optimal algorithm for maximizing state entropy, where the tolerance $\varepsilon$ decreases as the number of iterations increases. Empirical validation in three Mujoco environments shows that MaxEnt-Veritas significantly outperforms the two MaxEnt frameworks in terms of both state coverage and state entropy maximization, with sound explanations for these results.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides a stronger proof for learning a policy that achieves maximum state-entropy, by using a simpler and more adaptive policy-sampling strategy. It further claims to unify two popular approaches to maximum-entropy RL. Empirical results suggest that this improved sampling strategy leads to more exploratory and uniform policies.

### Strengths
The authors do a good job of explaining the shortcomings of the bounds provided by Hazan. The thorough description of why small η leads to unrealistic T was very helpful for intuition. The proof result, if I understand it, is a significant improvement in that regard. I generally thought the mathematical writing in this paper was strong.

### Weaknesses
I understand this is largely a theoretical paper, but nevertheless the experimental section of this paper is not very well-described or thorough. That’s the main reason for my “weak reject” – if the authors sufficiently address these concerns, I’ll gladly raise it.

From the plots, it appears that the experiments are run with one seed – if so, this isn’t acceptable, but can be easily rectified.

I’m very confused how you are using the NGU bonus, which is history-dependent, while not using a memory-based (e.g. LSTM) policy. Can you explain? The NGU bonus as I understand it doesn’t make much sense without recurrence. I also found it a bit unfair to criticize MaxEnt-LA for using a non-stationary reward when you use one here (of almost the same form, even).

Many details are missing for experiment configuration as well. How much training data is gathered each epoch? How much training is done per epoch? Was there a concrete measurement for the “epsilon-accurate stopping criteria” in the empirical results, or was it based on the number of training steps (it's hard for me to understand what "train to convergence" means in the high-dimensional setting)? What does an “epoch” mean for MaxEnt-LA? What’s the scale of the NGU bonus? Are the projection functions consistent across methods (the random projections for each method need to have the same parameterization for the comparison to be fair)?

How can there be a slight downwards tick for the blue line for Ant for “total unique states visited during training”?

To clarify, in the appendix when you describe projecting down the states to a 7-dimensional space, that’s only for entropy calculation, correct? And not projecting down for control as well?

I would also encourage the authors to choose a different name for their method. “MaxEnt-Veritas” seems to imply that the authors view their method as the “one final and true MaxEnt” method, while also implying that there was something false about prior work. The main difference between your method and Hazan is an improved policy-selection scheme, and so I don’t think this method is any more “truthful” than theirs, possibly just more efficient. And I’m sure someone (maybe even you) will at some point improve upon this method as well. I similarly think the title is not as informative about the methodology as it could be.

### Questions
Largely the empirical questions above, which is what my review currently hinges on. In brief:

* Can you run with more seeds?
* Can you include much more information on experimental configuration in your paper? Especially, can you describe what an "epoch" means, and if epsilon-accurate stopping is used, how that works in practice? Can you clarify whether projection is only for entropy computation or control as well? I should in theory be able to recreate your experimental protocol from your paper, but at the moment that's the not the case.
* As I understand, the NGU bonus as applied in the original paper (computed using previous states seen throughout a given trajectory) seems incorrect for a non-recurrent method. Would you share your thoughts on this? And can you comment on the non-stationarity introduced by NGU in relationship to the criticisms of MaxEnt-LA?
* Can you explain the slight downward tick in the blue line, since that doesn't seem possible given the plot's description?

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
The authors study the two algorithms by Hazan (MaxEnt-H) and by Liu \& Abbel (MaxEnt-LA), which both compute a mixture of policies to maximize the (discounted) state entropy of an agent evolving in an infinite-time MDP. A priori, the reward function they maximize is different, the weights of the mixture are different, and the number of policy updates are different before updating the intrinsic reward estimate. The authors nevertheless prove that (1) the intrinsic rewards both algorithms optimize are proportional to each other when computed using kNN, (2) the parameter $\eta$ for computing the mixture in MaxEnt-H is unnecessary, and a uniform mixture as in MaxEnt-LA is sufficient (3) it is better to completely optimize the policy before updating the estimate of the intrinsic reward function, as advocated by Hazan in MaxEnt-H. Based on these three observations, the authors introduce a new algorithm (MaxEnt-V) by combining the methods from Hazan and Liu \& Abbel. They remove the unnecessary steps from Hazan, and compute the mixture as in Liu \& Abbel, but optimize the policy as in Hazan before updating the intrinsic reward estimate. The algorithm is $\epsilon$-optimal, meaning that the agent is at most suboptimal by $\epsilon$, and under some assumptions $\epsilon$ decreases by $(B + \beta \ln T) / T$ where $T$ is the number of iterations and where $B$ and $\beta$ are constant. In practice it performs at least as well as the algorithms from Hazan and from Liu \& Abbel.

Warning: I must apologize beforehand for not having checked the demonstrations in the appendix.

### Strengths
1. The paper is well written and easy to follow.
2. The problem addressed is interesting to the community. 
3. The algorithm the authors propose is well motivated, with theoretical guarantees, and tested on several problems, where it also outperforms the alternative methods.

### Weaknesses
1. I would appreciate if the authors could clarify if their algorithm is always to be favoured compared to that of Hazan and Liu & Abbel, or if there may be configurations in which their method would fail and where the others would not. Specifically, under what conditions might the fixed replay buffer of MaxEnt-V hinder performance, and when might the more frequent reward updates of MaxEnt-LA be beneficial despite potential instability? A more detailed discussion of the trade-offs between these approaches is needed.

2. Paragraph line 313 to line 317 is pretty unclear to me. Could the authors explicitly provide the order of $\epsilon$ when $\eta \rightarrow 0$. Also, the bound of Hazan seems to be exponentially decreasing in T, wich a priori looks better than the bound of MaxEnt-V. It would be helpful to see a more detailed comparison of the theoretical convergence rates, especially concerning the dependence on the number of iterations $T$ and the parameter $\eta$, and how these relate to the practical performance observed.

3. In Figure 4, results are represented in term of epochs. To my understanding, an epoch is a step $t$ in algorithm 1. Then, as in MaxEnt-H and MaxEnt-V, and epoch fully optimizes the policy, I suppose it is also much longer in terms of wall-time, compared to MaxEnt-LA. How do the figures look like as a function of the wall-time? It is crucial to understand the computational cost of each algorithm, and presenting results in terms of wall-time would provide a more practical comparison, especially given the different update frequencies.

4. I do not agree with line 486, stating that the algorithms maximizing the action entropy lack the capability of exploring in absence of extrinsic reward. To me, without extrinsic rewards, these methods aim to explore the action space uniformly, which does not guarantee uniform state exploration. In opposition MaxEnt-H, MaxEnt-LA, and MaxEnt-V aim to explore the state space uniformly, which does not guarantee action space exploration. Both approaches have different intrinsic motivation (i.e., exploration objective), and it is possible to construct examples for which uniform action exploration outperforms uniform state exploration, and vice versa. The authors should acknowledge that the choice of exploration strategy depends on the specific problem and that neither approach is universally superior.

5. In paragraph line 508, there is an important distinction to make between parametric methods. Some are explicitly based on the entropy. The intrinsic motivation is to maximize the entropy of some distribution, which is typically approximated with a neural density estimator. Other methods are based on the uncertainty of some model. The intrinsic motivation is to take actions for which a parametric model over states and/or rewards provides different outcomes compared to the MDP realization. The distinction is particularly important in the current work as the first class of algorithms optimizes the same objective as the method the authors presented (and may have been added in the experiments). I think in particular that the related work should include [1, 2, 3], and probably other, more recent, works.

### Questions
1. I cannot see the reward functions in the three algorithms that are stationary and those that are not. In particular the sentence line 183 confuses me.
2. Line 195 to line 199, might their be a confusion between MaxEnt-V and MaxEnt-H?
3. Line 488, I suppose the entropy function is concave and not convex.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper first presents two established approaches to tackle the maximum state entropy maximization problem in reinforcement learning. Then, they first show how the two algorithmic schemes fundamentally aim to solve the same formal problem and present limitations of both schemes. Crucially, they identify that the policy sampling schedule is sub-optimal for one, while the policy update strategy is sub-optimal for the other one. Towards bridging the two schemes in a unified manner and overcoming these issues they propose a new algorithm, provide a theoretical analysis of its finite-time sub-optimality, and provide experimental comparisons with the previously mentioned existing algorithms.

### Strengths
CLARITY:
- The paper presents a clear and detailed comparison between two existing RL algorithms for state entropy maximization. 
- The intentions of the paper are clearly specified from the abstract and followed along the paper in a clear and coherent manner.

QUALITY:
- After a brief check of the proof, the deviation from the original analysis of Hazan et al. of Theorem 1 (pag. 14 of the paper) seems correct and well explained.

ORIGINALITY:
- Although maybe common in other areas, I am not aware of other works in this context leveraging the Euler-Mascheroni constant to analyze the telescoping sum as done in the proof of Theorem 1.

SIGNIFICANCE:
- The problem tackled within the paper, namely state entropy maximization, is a fundamental problem for RL as it tackles from first principles the issue of exploration in RL. As a consequence, investigation in this direction is highly relevant for RL and beyond.
- Theorem 1 closes a gap between theory and practice in the choice of policy sampling schedule.

### Weaknesses
ORIGINALITY and SIGNIFICANCE:
Unfortunately, the paper seems to suffer a quite fundamental issue in terms of originality and significance because of the following points holding together:
1) The work fundamentally aims to 'build a unified perspective' on  the maximum state entropy problem by bridging two established schemes, namely the algorithms presented by Hazan et al. (MaxEnt, here renamed MaxEnt-H) and by Liu et al. (APT, here renamed MaxEnt-LA).
2) Crucially, the work by Liu et al. cites (and seems to build on) work [1]. This work fundamentally already presents the algorithmic ideas used in Liu et al. (namely the non-parametric entropy estimate to scale to non-tabular domains) in the context of the maximum state entropy problem presented by Hazan et al. (Sec. 4 of [1]). Moreover, it proposes an algorithm, named MEPOL, that seems to be nearly analogous to the one proposed by the authors (MaxEnt-Veritas) as a subcase. In particular, by choosing a high value of $\delta$ in MEPOL, it seems that the policy update scheme corresponds to the one in MaxEnt-Veritas (as in Hazan et al.), while using the policy sampling scheme as in Liu et al.
3) The authors cite [1] both in the Introduction and Related Works section, where they claim that [1] 'focuses on maximizing trajectory-wise state entropy' which is a 'fundamentally different objective'. Although this is the case for later works of the same author that alike the mentioned work by Jain et al. optimize trajectory-wise state entropy, this does not seem to be the case in [1], where the notion of entropy in MEPOL is not trajectory-wise.

As a consequence, it seems to me that the authors aimed to bridge two works that were already deeply (historically and formally) connected by a misinterpreted well-established reference. Although the submitted paper brings a new theoretical result (Theorem 1) by a slight modification of the analysis in Hazan et al., this seems very limited in terms of contribution and novelty compared with what the authors claim (e.g., in the abstract), which was arguably already achieved in large part. 

CLARITY and QUALITY:
- I believe that the first 5 pages of the paper can be significantly sharpened in their presentation, which currently seems loose and slightly hard to follow at points.
- I would suggest to present Propositions 2 and 3 not as propositions as they seem simple calculations based on existing theorems and could be integrated within the text to improve the flow of the paper.

### Questions
Did I misinterpret something within points 1-3 above that renders the conclusion fundamentally wrong?

### Soundness
4

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses maximum state entropy exploration in MDPs without rewards. First, it analyzes and compare previous approaches to state entropy maximization, namely a Frank-Wolfe algorithm (like MaxEnt, Hazan et al. 2019) and a policy optimization algorithm (like APT, Liu & Abbeel, 2021). The paper shows that the two approaches share the same reward function when the entropy is estimated via kNN. Then, the paper proposes a new algorithm, called MaxEnt-V, incorporating the best of both approaches. The method is demonstrated to lead to approximately optimal policies and empirically validated in a set of Mujoco environments.

### Strengths
- The paper provides a unifying perspective on the literature of maximum state entropy;
- The paper proposes an interesting implementation change for maximum state entropy algorithms, which prescribes to freeze the intrinsic reward for multiple policy optimization steps (like in a Frank-Wolfe routine);
- The paper makes an effort to provide theoretical ground to the proposed method.

### Weaknesses
EVALUATION

This paper provides some fresh ideas, mostly that the previous approaches for maximum state entropy can be connected into a "unifying" algorithm and that the entropy intrinsic reward shall be frozen for multiple policy optimization steps, which bears some resemblance to the target network trick for deep Q-learning. Unfortunately, in my opinion the paper fails to provide convincing evidence that the frozen reward trick gives empirical benefit to justify widespread adoption. More broadly, I think the paper falls short of the technical quality required to be accepted at ICLR. I provide below a summary of what I believe are the main weaknesses of the paper and further comments.

MAJOR WEAKNESSES

1) Misunderstandings of the literature
   1. The paper presents MaxEnt-H and MaxEnt-LA as two competing approaches for maximum state entropy. Whereas different design choices can be extracted on an abstract level, the authors seem to misunderstand the purpose of the two papers. Hazan et al. were the first to introduce the problem of maximum state entropy in MDPs. They show the latter problem is not hopeless, despite being non-convex in the policy parameters, by providing a provably efficient algorithm. While an implementation and experiments are provided, the algorithm is mostly a theoretical and analytical tool. Instead, Liu & Abbeel's paper falls into a stream of practical methods for maximum state entropy, where the main advancements were given by the use of kNN entropy estimators in place of state densities (this technique has been introduced by Mutti et al., 2021 not by Liu & Abbeel as stated in the manuscript) and learning representations.
   2. The paper suggests that MaxEnt-LA trains a mixture with uniform parameters. I am not sure this is the case. From my understanding, it does sample uniformly from a replay buffer, which may include transitions coming from previous policies, but it does that only to perform updates on the *last* policy. Indeed, the output is the last policy network, which is then fine-tuned with external reward, and not a mixture. There seems to be an important gap here.
   3. The paper says that another stream of work (Mutti et al 2021, Jain et al 2024) optimize the trajectory-wise entropy. Perhaps this distinction shall be clarified. From my understanding, the objective of Mutti et al 2021 is the same of Eq. 2, although the entropy reward is not decomposed in state terms as in Liu & Abbeel 2021. The core difference lies in the fact that Mutti et al. (2021) use a trajectory-centric approach, where the k-NN distances are computed within the context of a trajectory, while Liu & Abbeel (2021) focus on state-based rewards, computing k-NN distances across all states in the replay buffer.

2) Some claims look subjective and lack strong support
   1. "Tuning $\eta$ is unnecessary in MaxEnt-H". Since the purpose of tuning $\eta$ comes from the analysis in Hazan et al., 2019, the paper should show that similar convergence guarantees  can be obtained with a uniform mixture to support this claim. Showing that $\eta$ is always small and tuning is unnecessary in practice is not enough. The theoretical analysis of Hazan et al. (2019) provides a specific role for $\eta$ in the convergence proof, and simply observing small values in practice does not negate the need for a theoretical justification when removing this hyperparameter.
   2. "Freezing the reward is better". Theorem 1 only provides an upper bound on the sub-optimality. It is rather weak to say that freezing the reward is better because it leads to a smaller upper bound. Maybe the upper bounds are just not tight, and the analysis would say nothing about which one (freezing the reward or changing it at any step) is better. The paper needs to demonstrate that the bound is tight or provide empirical evidence that this bound is correlated with actual performance.
   3. Theorem 1. I have some concerns on the validity of this result. First, the statement assumes that $H_{kNN}$ is smooth and bounded, which does not seem to be the case by staring at Eq. 6. The k-NN estimator, as defined in equation 6, can become unbounded when the k-NN distance is zero, which can occur if multiple identical states are present in the batch. This violates the boundedness assumption. Can the authors provide more details on when those conditions are met? Moreover, what does it mean to assume access to estimation oracle (as in lien 310)? Note that the kNN entropy estimators are biased, does that mean $\epsilon_0$ error on the biased estimate or the true entropy?

3) The empirical analysis looks very far from the standards of the community
   - Are the curves in the figures reported on a single run? Some details seem to be missing on how the experiments are conducted to meet some statistical significance (e.g., look at https://ojs.aaai.org/index.php/AAAI/article/view/11694 and https://proceedings.neurips.cc/paper_files/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html)
   - Previous papers, especially Hazan et al. 2019 and Liu & Abbeel 2021 have public implementations. To claim MaxEnt-V gives benefits over them, it would be better to compare its performance with the official implementations of MaxEnt-H and MaxEnt-LA.

OTHER COMMENTS

The literature of maximum state entropy could be presented better, especially considering that this manuscript builds over them. The first papers on this problem have been Hazan et al 2019; Lee et al 2019, Mutti & Restelli 2020), which presented algorithms requiring state density estimation, which is mostly impractical in high dimensions. To overcome this issue, Mutti et al 2021 proposed to use kNN entropy estimators (Singh et al 2003 and others) to guide policy optimization without explicit state density estimation. Mutti et al 2021 compute kNN distances on the state features, which is not suited for images. Liu & Abbeel 2021 coupled kNN estimators with contrastive representations (together with various other implementation changes, such as state-based rewards, actor-critic architecture with replay buffers). Other representations have been proposed by subsequent works, such as Seo et al 2021, Yarats et al 2021. Several other works followed on both practical methodologies and theoretical analysis of maximum state entropy. Some relevant references that does not seem to be mentioned:
- Lee et al., Efficient exploration via state marginal matching, 2019; 
- Mutti & Restelli, An intrinsically-motivated approach for learning highly exploring and fast mixing policies, 2020; 
- Guo et al., Geometric entropic exploration, 2021;
- Liu & Abbeel, Aps: Active pretraining with successor features, 2021;
- Mutti et al., Unsupervised reinforcement learning in multiple environments, 2022;
- Mutti et al., The importance of non-Markovianity in maximum state entropy exploration, 2022;
- Mutti, Unsupervised reinforcement learning via state entropy maximization, 2023; 
- Yang & Spaan, CEM: Constrained entropy maximization for task-agnostic safe exploration, 2023; 
- Zisselman et al., Explore to generalize in zero-shot rl, 2023;
- Zamboni et al., How to explore with belief: State entropy maximization in pomdps, 2024;
- Zamboni et al., The limits of pure exploration in POMDPs: When the observation entropy is enough, 2024.

Despite my concerns expressed above, I think the idea of the frozen rewards to improve maximum state entropy approaches is very interesting and worth studying. Perhaps the authors could think of restructuring the paper and their analysis to focus on the empirical benefit that this trick may provide and the (stability) issues that may arise from chasing the non-stationary reward.

MINOR
- Perhaps clarify the meaning of MaxEnt-H and MaxEnt-LA earlier in the text
- l.48 "While these importance sampling-based methods" -> what does that mean?
- Eq. 2 min -> max
- Algorithm 2, line 2: how many states are sampled?

### Questions
I mostly do not have direct questions. Some are reported in the comments above.

### Soundness
1

### Presentation
3

### Contribution
2
