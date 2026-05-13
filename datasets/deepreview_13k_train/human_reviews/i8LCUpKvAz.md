# Minimax Optimal Reinforcement Learning with Quasi-Optimism

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
In our quest for a reinforcement learning (RL) algorithm that is both practical and provably optimal, we introduce EQO (Exploration via Quasi-Optimism). Unlike existing minimax optimal approaches, EQO avoids reliance on empirical variances and employs a simple bonus term proportional to the inverse of the state-action visit count. Central to EQO is the concept of *quasi-optimism*, where estimated values need not be fully optimistic, allowing for a simpler yet effective exploration strategy. The algorithm achieves the sharpest known regret bound for tabular RL under the mildest assumptions, proving that fast convergence can be attained with a practical and computationally efficient approach. Empirical evaluations demonstrate that EQO consistently outperforms existing algorithms in both regret performance and computational efficiency, providing the best of both theoretical soundness and practical effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies reinforcement learning in tabular finite-horizon MDPs. The authors introduce EQO (Exploration via Quasi-Optimism), a novel algorithm which is basically a variant of UCBVI with much simpler bonuses of the form b_k(s,a) = c / N_k(s,a) (ie not requiring any variance term and decaying at 1/k rate instead of 1/sqrt(k)). EQO is shown to be minimax optimal for both regret minimization and PAC identification of an epsilon-optimal policy. The main novelty in the analysis is a notion of "quasi optimism", which allows EQO to achieve strong theoretical guarantees despite not being exactly optimistic at every episode. On a simple numerical experiment, EQO outperforms existing baselines in terms of cumulative regret.

### Strengths
1. Making provably-efficient RL algorithms, even for the simplest setting of tabular MDPs, more practical is a relevant problem, and the paper makes a good contribution in this direction
2. EQO achieves strong results despite its simplicity, which I think is a big plus
3. I found the idea of "quasi optimism" novel and interesting. Most existing works do need "strong" optimism (ie Q functions are optimistic at any s,a,h,k) to derive theoretical guarantees, and it is good to see that this can be relaxed
4. The paper is overall well written: the context is well motivated from the very beginning, sufficient intuition is given behind all results, and proofs/notation are clear (though I have to say that I only skimmed through the proofs quickly)
5. Relaxing existing assumptions on reward/return/value distributions (Assumption 1 and 2) is also a relevant contribution (though I have never found them as limiting factors for existing approaches, but rather just tricks to simplify proofs/notation)

### Weaknesses
My main concern is about the way these novel bonuses are built: it seems that the price to pay for having b^k(s,a) decay as 1/N_k(s,a) is an inflation of the multiplicative constant (c_k) by a factor sqrt(K) or sqrt(k), whereas existing bonuses only have logarithmic dependences in this quantity. This may have a some important negative implications:
1. If I am not mistaken, this will prevent deriving any sort of logarithmic (in K) / gap-dependent bound for the same algorithm, since a factor sqrt(K) in the regret may be unavoidable if forced into the confidence bonuses. If this is true, I think it is a quite big limitation, as one of the main directions to make these approaches "practical" is to show that they can adapt to the complexity of the specific MDP instance they face (mostly though logarithmic / gap-dependent bounds), instead of paying the cost of the hardest instance (which may not even be of practical relevance). The core issue is that the 1/N_k(s,a) bonus decay, while simple, appears to necessitate a larger scaling constant to ensure optimism, which directly impacts the regret bound's dependence on the number of episodes.
2. There is a long line of works on instance-dependent results for regret minimization [1] and PAC RL [2,3,4,5] mostly studying algorithms that are quite similar to the baselines considered here. My concern is that the current algorithm cannot achieve results comparable to them, which means that comparing to existing baselines only in terms of worst-case results may not give a complete view of EQO's pros and cons. Also, in light of this, I feel that discussing literature on instance-dependent results is quite important, but at the moment all these papers are missing from the related literature. The absence of a discussion on instance-dependent bounds is a significant oversight, as it limits the understanding of EQO's performance compared to algorithms that can adapt to the specific structure of the MDP.
3. This also break a bit the story about existing algorithms focusing only on minimax optimality. Eg the introduction states that "Although provably efficient RL algorithms offer regret bounds that are nearly optimal (up to logarithmic or constant factors), they are often designed to handle worst-case scenarios. This focus on worst-case outcomes leads to overly conservative behavior". But it is known that these algorithms can get guarantees which go beyond the minimax one, while (again, if the conjecture above is true) EQO may not. This would make EQO even more "minimax-focused" than existing literature. The claim that existing algorithms are solely minimax-focused is inaccurate, as many have demonstrated instance-dependent performance, which EQO may not be able to match due to its bonus structure.
4. I was surprised to see EQO outperforming all existing baselines despite the sqrt(K) term in the confidence bounds. I wonder if the experiments focus too much on the "low-K regime", i.e., where the algorithms are still far from converging to a (near-) optimal policy and have to pay a sqrt(K) regret. I wonder what happens in the "large-K regime", where existing algorithms should essentially transition to logarithmic regret while the EQO should (probably) still suffer sqrt(K). Also, existing papers on instance-dependent RL show examples of MDPs where good adaptive algorithms would achieve sample-complexity/regret much smaller than minimax (eg when you have a very large sub-optimality gap in some state that allows the agent to quickly "eliminate" an entire branch of the MDP, see eg Figure 1 in [1]). I wonder how EQO compares to existing baselines on such "favorable" instances. The experimental results should be more thoroughly analyzed, particularly in the large-K regime and on MDPs with favorable structures for adaptive algorithms, to fully understand the practical implications of the sqrt(K) dependence.

Other less important limitations:

5. About the bound for best-policy identification (Theorem 4): one important thing to note is that the algorithm has no adaptive stopping criterion, which means that in practice we have to run it until K_0 to get the guarantee on the returned policy. That can be very conservative, as an algorithm with adaptive stopping may empirically take much less than the derived worst-case bound

### Questions
1. What's the authors opinion about the impossibility of proving log(K) regret with EQO? Again, I am not 100% sure about it so I'd be happy to be proven wrong
2. Is the assumption of time-homogeneous transition kernel important for the techniques developed here or could the proofs go through even with time-inhomogeneous dynamics?

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
The authors proposed a novel algorithm for reinforcement learning in finite episodic MDPs based on the principle of Quasi-Optimism. In particular, they showed that simple exploration bonuses without any variance information can achieve the minimax optimal regret bound. Additionally, the method is easy to implement and shows good empirical performance.

### Strengths
- To my knowledge, it is the first result on a bonus-based RL algorithm that does not use variance information to achieve a minimax optimal regret bound. It is a major improvement over the prior work since, before, only posterior-sampling-based algorithms could achieve minimax optimal bound without the direct usage of the variance estimates (see, e.g., Tiapkin et al. 2022).



Tiapkin, D., Belomestny, D., Calandriello, D., Moulines, É., Munos, R., Naumov, A., ... & Ménard, P. (2022). Optimistic posterior sampling for reinforcement learning with few samples and tight guarantees. Advances in Neural Information Processing Systems, 35, 10737-10751.

### Weaknesses
 - The algorithm cannot adapt to deterministic environments. In particular, the usage of variance information allows the Bernstein bonuses to become of order almost $H/N$ in the case of deterministic environments since the variance, in this case, will be learned to be zero. In contrast, the bonuses of the presented algorithm always have order $H\sqrt{K}/N$, which is much larger than adaptive variance-dependent bonuses.
- The main technical novelty presentation should be improved. In particular, I would prefer to see the full proof of quasi-optimism in the main text since it is the most insightful part of the paper that shows why the scaling of the additional term is $\lambda_k H$ and not $\lambda_k H^2$, how it may follow from a naive analysis that uses precisely the statement of Lemma 1 for the induction. In particular, very subtle work with variance and second moments looks to be a crucial part of the paper that allows the errors not to accumulate through the horizon, and this part should be acknowledged in the paper much better. I consider raising my score if the presentation of the proof in the main text shows this critical aspect.

### Questions
- Why the time-homogeneous setting was selected? What limits the application of these techniques to a time-inhomogeneous setting?
- The experiments do not compare randomized exploration methods such as PSRL and RLSVI. Could you add these additional comparisons?
- How does the regret bound change under the sparse regret setting $R^k_h \leq 1$?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies regret minimization in tabular RL. They propose an algorithm based on the principle of “quasi-optimism” that, rather than satisfying standard optimism, satisfies a relaxed version of optimism (their estimates are not truly optimistic, but deviate from optimism by a bounded amount). They show that this relaxation of optimism allows them to obtain the tightest known bounds on regret minimization in tabular RL (in the time homogeneous setting), while also simplifying the algorithm substantially as compared to existing optimal algorithms for tabular RL. Furthermore, they show that their algorithm leads to better empirical performance than all existing algorithms for tabular RL with theoretical guarantees.

### Strengths
1. This paper introduces novel algorithmic and proof techniques for tabular RL, which allow it to obtain the tightest known bounds. As the majority of minimax optimal algorithms for tabular RL rely essentially on standard optimism, it was interesting to see these new techniques. In particular, the fact that you can achieve optimal regret without variance-dependent bonuses is surprising. I believe the insights and techniques presented here are a valuable and interesting contribution to the tabular RL literature. 

2. The simplicity of the algorithm is also very nice. The algorithms with the best known guarantees tend to be quite complex and it is not obvious that one can achieve optimality with a very simple algorithm. This paper demonstrates this is possible (and indeed, achieves bounds tighter than the previously best known bounds), which is an exciting conclusion.

### Weaknesses
1. The motivation for this paper could be cleaned up somewhat. It is motivated by saying that we want algorithms for tabular RL which are both theoretically optimal but also perform well practically, and that we don’t currently have this. To my knowledge, there are essentially no real-world applications of tabular RL, however; it is more of a theoretical exercise. I do not think this is an issue, but it would be better to not overstate the importance of having a practically useful algorithm (or better justification for why this is important should be given).

2. Furthermore, I do not think the experimental results sufficiently validate the proposed algorithm’s practicallity or superior empirical performance over existing works. The algorithm is only validated on one environment (though the size and horizon are varied). If the authors want to convincingly make the argument that their approach yields better empirical performance, I would suggest benchmarking on additional environments (for example, those from the BRIDGE dataset of [1]). I do not think this is necessary—I think the theoretical results are sufficient on their own—I would just suggest toning down the claims on empirical performance without further experiments.

3. It would also be nice to see an empirical comparison against a posterior sampling-style approach (e.g. the algorithm of [2]).

4. I found the proof sketch in Section 4.4 to be fairly mechanical—some more intuitive explanation here would help elicit the key takeaways (for example it seems like the version of Freedman’s inequality here is playing a large role and giving an improvement over more traditional Bernstein-style bounds—this could be made more explicit).

Minor typos:
- Line 252: I believe there should be brackets around $c_k$.
- Line 523: “that the our algorithm” -> “that our algorithm”.

### Questions
None.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the tabular MDP setting. They propose a new type of bonus for the UCRL algorithm, and prove that the regret of the algorithm matches the lower bound. They also show an upper bound to the PAC sample complexity, which matches to the lower bound as well.

### Strengths
1. The paper is well written. The proofs are correct.

2. The algorithms have regret which match the lower bound, and the algorithm is much simpler to those minimax optimal algorithms in previous literatures (e.g. [Azar et al,. 2017]) and do not need to estimate the variance explicitly.

### Weaknesses
1. In terms of the minimax optimality, this algorithm only matches the lower bound in the dominate terms. The low order terms does not match, while the regret of the algorithm in [1] matches the lower bound even for low order terms (the setting in [1] is time-inhomogenous, but the algorithm seems to work for time-homogenous setting as well)

2. The bonus terms added in Algorithm 1 and Algorithm 2 seem to be similar to the bonus term in Eq. (4) in [2] and Theorem 2 and 3 in [3]. There is no comparison to these related works in the paper.

3. The numerical experiments in this paper is only for the toy example. There is no experiments for real world applications.

4. While the authors claim their algorithm does not explicitly estimate the variance, the bonus term seems to implicitly address variance through a concentration inequality, which is a common technique in previous literature, such as [1]. The authors should clarify the novelty of their approach in comparison to existing variance-handling techniques.

### Questions
1. Is there any way we can tighten the low order term from $S^2A$ into $SA$ to match the lower bound?

2. Can you obtain first order regret bound (regret bound in terms of $V^*$) and second order regret bound (regret bound in terms of $\mathrm{Var}(V^*)$)?

### Soundness
3

### Presentation
3

### Contribution
2
