# Misspecified  $Q$-Learning with Sparse Linear Function Approximation: Tight Bounds on Approximation Error

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The recent work by \cite{dong2023does} showed for misspecified sparse linear bandits, one can obtain an $O\left(\epsilon\right)$-optimal policy using a polynomial number of samples when the sparsity is a constant, where $\epsilon$ is the misspecification error. 
    This result is in sharp contrast to misspecified linear bandits without sparsity, which require an exponential number of samples to get the same guarantee.
    In order to study whether the analog result is possible in the reinforcement learning setting, we consider the following problem: assuming the optimal $Q$-function is a $d$-dimensional linear function with sparsity $k$ and misspecification error $\epsilon$, whether we can obtain an $O\left(\epsilon\right)$-optimal policy using number of samples polynomially in the feature dimension $d$.
    We first demonstrate why the standard approach based on Bellman backup or the existing optimistic value function elimination approach such as OLIVE~\citep{jiang2017contextual} achieves suboptimal guarantees for this problem.
    We then design a novel elimination-based algorithm to show one can obtain an $O\left(H\epsilon\right)$-optimal policy with sample complexity polynomially in the feature dimension $d$ and planning horizon $H$. 
    Lastly, we complement our upper bound with an $\widetilde{\Omega}\left(H\epsilon\right)$ suboptimality lower bound, giving a complete picture of this problem.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors found a misspecified sparse linear bandit algorithm based on elimination. They first proved that the traditional approaches such as OLIVE work suboptimally in this environment, and also a naive extension from the previous bandit work [Dong & Yang, 2023] fails. After that, the authors propose a lower bound from the MDP without sample to RL with sample, using the INDQ problem as a mediator. This lower bound matches with the upper bound of their algorithm, showing that their algorithm has a near-optimal rate.

### Strengths
1) Clarity & Soundness: Their writing was clear on these points. 
- They clearly stated their novelty and significant difference from the misspecified bandit algorithm proposed by Dong & Yang.
- They tried to demonstrate how they set the lower bound instance by high-level, but an explicit explanation throughout Section 3, with a nice figure. (and also the main difference from Du et al. 2020)
- The algorithm itself is also quite simple - it follows a traditional method of elimination algorithms, and thanks to the detailed explanation, I could easily get a sketch about how the proof goes on. The technique is also using some simple Hoeffding's inequality. 

2) Significance & Novelty: Even though their results are clearly written and easy to understand, many of their results are quite fresh and counter-intuitive. One cannot extend bandit algorithms in this case was quite interesting indeed.

### Weaknesses
1) Computationally intractable. If I understood correctly, they use an $\epsilon$-net on the candidates for $\theta_h$ - $P_h^0$ starts from all possible $k$-sparse vectors. After that, for each iteration, this algorithm is searching for argmax over all candidates. This implies a search over a potentially very large space, especially as the dimension $d$ increases, even if $k$ is small. The use of an $\epsilon$-net, while theoretically sound, often leads to algorithms that are impractical for real-world applications due to the exponential dependence on the dimensionality or sparsity parameter. Also, eventually they proposed an algorithm that provides $\epsilon$-optimal.

2) Even though they tried to show their process transparently, there are some parts that I cannot understand. Please check the 'Questions' below.

### Questions
1) I don't understand the word 'MDP without sample.' Without any trajectory, how could a learning agent learn something? You mean, 'without learning' the error is bounded by $\Omega(H\epsilon)$?

2) Also, it is interesting that this algorithm eliminates the 'most promising candidate' first. In bandits, the elimination eliminates all the suboptimal candidates that show less upper bound than the largest lower bound (eliminate an arm i which is max_j LCB_t(j) > UCB_t (i)). Why does this difference happen?

3) So what is the optimal size of the parameters, $\epsilon_{net}$ and $\epsilon_{stat}$? I guess they also should be in the scale of $\epsilon$. 

3-1) Also just to clarify, what is $\epsilon$-optimal in here, does this mean $V^* - V(\pi) \leq \epsilon$? If so, according to your final result (Lemma 4.4), for the error $\epsilon'$, one should set $\epsilon/H$. This means now $m$ is proportional to $H^2$ too and the overall sample complexity also should include $H^2$, I believe. 

3-2) In that sense, the line 438 is very confusing. Why it is $H^2 \cdot m$, including the $\epsilon_{stat}^2$ in the denominator? You repeat $m$ samplings for $H$ iterations. Shouldn't it be $H\cdot m$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers the problem of online reinforcement learning with linear function approximation. It is well known if that in the presence of epsilon-misspecification (in the sense that Q* is eps-approximately linear), the best one can hope for is a an error guarantee that scales with \sqrt{d}*eps, where $d$ is the feature dimension, even in the bandit setting where $H=1$. The main result in this paper is to show that if we additionally assume that the optimal parameter is $k$ sparse, it is possible to improve upon this guarantee. In particular:

* 1) The author show that it is possible to achieve an error guarantee that scales as H*eps (with no dependence on dimension), albeit with sample complexity and runtime scaling as roughly (d/eps)^{k}.

* 2) The authors show that the error guarantee above cannot be improved further, in the sense that achieving H/T*eps for any T requires exp(T) sample complexity.

### Strengths
This paper makes a reasonable contribution to the theory of reinforcement learning. Guarantees in the linearly (approximately) realizable setting the authors consider are non-trivial and often somewhat surprising, so I think this paper makes an interesting contribution by filling in another piece of the landscape.

### Weaknesses
The main drawbacks preventing me from giving a higher score are as follows:

* On the upper bound side, the significance of the algorithmic techniques is somewhat narrow. Concretely, the authors consider a setting where we have a separate parameter $\theta*_h$ for each step $h\in[H]$. If we instead assume that there is a shared parameter $\theta*$ for all steps $h$, then I believe that simply enumerating over an epsilon-net for the parameter space and trying each policy one-by-one would be sufficient to achieve the approximation and sample complexity guarantees the authors get. So, the only reason why a non-trivial algorithm is required at all is because there is no parameter sharing across the steps $h$. Indeed, without parameter sharing, an epsilon-net would have size at least 2^H and lead to 2^H sample complexity, so the authors' contribution can be viewed as removing this exponential dependence on $H$ for this setting.

* The problem setting in the paper is fairly niche, and will probably only be interesting/compelling to research working on core RL theory. Broader impact is unclear.

### Questions
Overall, I do think the results are interesting and not necessarily obvious a-priori---they certainly piqued my curiosity. Some questions I was inspired to think about based on the results are as follows:

* Can we get similar guarantees beyond linear function approximation? My thought would be that if we assume that Q*_h is eps-approximately realizable by a class \mathcal{F}_h, then perhaps we can get H*eps error while paying for roughly max_h{Covering-Number(\cF_h, eps)} in the sample complexity using a generalization of the algorithm. If so, this would suggest that the linear structure is actually not that important.

* Have the authors thought about whether there exists an algorithm that achieves the H/T*eps error vs exp(T) sample complexity tradeoff in the lower bound?

* Is there any hope of achieving just d^{k} sample complexity instead of (d/eps)^k sample complexity?

### Soundness
4

### Presentation
4

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
In this work, the authors study RL where Q-function is sparse codable up to $\epsilon$ error.
Their main contributions are
i) showing the existence of a hard instance where achieving suboptimality less than $H \epsilon / C$ requires sample complexity exponential to C,
ii) establishing a theoretical method achieving suboptimality of $2H \epsilon + o(1)$ with polynomial sample.

### Strengths
- An interesting work on the RL learnability under limited knowledge of environment.
- The theoretical results are strong in the sense that almost-matching upper and lower bounds are presented.

### Weaknesses
 - The sample complexity grows exponentially to the sparseness $k$, which is unavoidable with the present set of assumptions but undesirable in practice.
- The construction of the hard instance depends on exponentially large state space. This is not uncommon in the theoretical analysis, but worth discussing if similar results hold with smaller state space.

Some mathematical definitions are confusing: 
- Def of $\Delta(\cdot)$ lacking?
- Why parameters restricted on sphere? (I suspect the authors are confusing sphere and ball)
- How s_0 is sampled? Is it fixed?

### Questions
Does the proposed method exploit the sparseness except through the cardinality of the epsilon net?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
$\textbf{Background}$ In Q-learning with function approximation, it is assumed that the optimal Q-value function can be written as a linear function of the feature of each state, action pair, i.e., $Q^*(s, a) = <  \theta^*,  \psi(s, a)>$.
In the misspecified setting, the assumption is relaxed to be such that the optimal Q-value function is $\epsilon$-close to some linear function of the features, i.e., $| Q^* - <  \theta^*,  \psi(s, a)> | < \epsilon $.
Unfortunately, it has been shown that exponentially many samples are required in the misspecified setting even when the MDP only has $H=1$ step, which simplifies to the linear bandit setting.
Yet, a prior work shows that the hardness result can be circumvented in the linear bandit setting provided that the optimal secrete vector $\theta^*$ is further assumed to be $k$-sparse for some constant $k$. In such cases, the sample complexity for linear bandit has been improved to $O( (d/\epsilon)^k )$.

$\textbf{Contribution of this work}$ In this work, it has been shown results with a similar favor hold for general multi-step Q-learning as well. In particular, they give an algorithm that uses polynomially many samples and returns an $O(H \epsilon)$-optimal policy, where $H$ is the number of steps of the MDP.  Interestingly, the error $H \epsilon$ has been shown to be optimal up to polylogarithmic factors.

The main novelty of the proposed algorithm, compared to the prior work, is in how it chooses the policy to execute. In particular, the policy is chosen to maximize the so-called “empirical roll-in distribution” at all levels. After that, similar to prior work, the algorithm proceeds to compute average bellman error, and eliminate parameters that lead to large Bellman error (though the algorithm is a bit more conservative in the sense that it always eliminates at most one candidate parameter per level in every iteration).

### Strengths
The error guarantee of the algorithm proposed is shown to be optimal though it has a surprising linear scale with the number of steps $H$. The lower bound argument is quite interesting. They first demonstrate a suboptimality gap assuming that the RL algorithm is given no samples using hard instances based on binary trees. They further show that the instance can be modified so that the reward-signal is exponentially sparse. Hence, the algorithm must search the space in a brute-force manner to extract useful information.

### Weaknesses
The algorithm is structurally similar to the algorithm from Jiang et al., 2017. Since the algorithm eliminates one parameter per level every iteration, it is almost doing a brute-force search over the entire parameter space. As a result, the sample complexity and runtime of the algorithm both scales exponentially with the sparsity parameter $k$ of the problem. The fact that the algorithm eliminates only one parameter per level in each iteration, while being more conservative, also raises concerns about the practical efficiency of the algorithm, especially in high-dimensional settings. This approach might lead to a very slow convergence, as it explores the parameter space sequentially, which can be problematic when the number of relevant parameters is large, even if the problem is $k$-sparse. Furthermore, while the error guarantee scales linearly with $H$, the number of steps, this linear dependence might still be a significant limitation in long-horizon tasks, where $H$ can be quite large, potentially negating the benefits of the improved sample complexity with respect to the approximation error $\epsilon$.

### Questions
Do the authors have a guess whether the exponential dependency on $k$ in the sample complexity is necessary?

### Soundness
3

### Presentation
3

### Contribution
2
