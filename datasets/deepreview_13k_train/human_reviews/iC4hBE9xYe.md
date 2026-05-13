# Provable Convergence of Single-Timescale Neural Actor-Critic in Continuous Spaces

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Actor-critic (AC) algorithms have been the powerhouse behind many successful yet challenging applications. However, the theoretical understanding of finite-time convergence in AC's most practical form remains elusive. Existing research often oversimplifies the algorithm and only considers simple finite state and action spaces. We analyze the more practical single-timescale AC on continuous state and action spaces and use deep neural network approximations for both critic and actor. 
Our analysis reveals that the iterates of the more practical framework we consider converge towards the stationary point at rate $\widetilde{\mathcal{O}}(T^{-1/2})+\widetilde{\mathcal{O}}(m^{-1/2})$, where $T$ is the total number of iterations and $m$ is the width of the deep neural network.  To our knowledge, this is the first finite-time analysis of single-timescale AC in continuous state and action spaces, which further narrows the gap between theory and practice.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proves a novel result for average reward MDP's. Prior convergence results for actor critic for average reward were only able to prove convergence for a finite state action spaces. This paper is the first result of its kind and thus deserves acceptance in my opinion. I do however have some concerns.

### Strengths
The paper is well laid out and easily readable. The appendix has been arranged in a way that makes it easy to follow. The biggest strength of the paper is the novel contributions that it has.

### Weaknesses
1. Even though the results proved in the paper are novel, the proof seemed quite derivative of the paper Chen 2024.

### Questions
1. I have a concern about the assumption 4.5. Specifically the term ${\mu_{\theta}}{\int_{\mathcal{S}{\times}{\mathcal{A}}}}(\pi_{\theta}-1)\mathcal{P}(s^{'}|s,a)d(a{\times}s^{'})$. Since the term $(\pi_{\theta}-1)$ for all state action pairs, is this term not always negative? This would make the assumption 4.5 not true. It is likely I am misunderstanding the notations, so some clarity here would be helpful.
2.  On page 24. In the second left hand side for $Z_{T}$. I am having trouble figuring out where the $\mathcal{O}\left(\frac{1}{\sqrt{m}}\right)$ has come from.  It would be helpful if some information would be given in this regard.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors consider the convergence of single time scale actor critic algorithm in continuous state and action spaces with infinite horizon average reward as the performance metric. The state and action spaces considered are assumed to be compact and the value functions and the policies are parametrized through deep neural networks. The average reward, the relative value function and the policy are all updated on a similar time scale. Finite time convergence guarantees to a stationary point are provided under the overparametrized neural network regime. They resort to a NTK style analysis where by the virtue of overparametrization, the weights do not change much in magnitude by the end of the training period.

### Strengths
1. Most prior literature in RL (especially average reward RL) considers finite state and action spaces. Hence the setting of continuous state and action spaces is relatively understudied given its significance. 
2. Neural networks (NN) have consistently demonstrated strong capabilities as function approximators, with prior results showing that they can approximate continuous functions to any desired accuracy. However, their theoretical foundations remain relatively underexplored. This paper addresses a crucial problem, particularly given the extensive practical applications of neural networks.
3. They characterize tight bounds in terms of dependence on the number of iterations and number of parameters of the NN.

### Weaknesses
1. Since this paper is motivated by the promise of neural networks in policy optimization in the realm of RL, simulations demonstrating the same would increase the strength of the paper. As of now, the paper analyzes the standard actor critic algorithm and provides finite time bounds, but relating these to whats observed in practice would vastly help with understanding (especially in terms of determining the various step sizes required for updating different quantities of interest).
2. The paper provides convergence to a stationary point which can be a local minima. However, some of the recent works have proposed global convergence guarantees for average reward problems. See ref below. Although these are for finite state and action spaces, the optimization landscape might be the same independent of the finiteness of the problem parameters.
3. The assumptions require the nonlinear activations to be differentiable and smooth, this precludes the use of ReLU. However the authors suggest other nonlinear activations which indeed satisfy these assumptions. Once again, a simulation to demonstrate their practicality would help.
4. Regarding Assumption 4.3: Does this assumption require the original value functions to also be smooth with respect to the underlying parameter $\theta$. Since the parameters are initialized from a normal distribution, it is not clear as to how assumption 4.3 can be satisfied in practice (the uniform boundedness of the optimal parameters corresponding to the value function estimate). In case of linear function approximations, this assumption is trivial since typically $\|\phi\| \leq 1$, where $\phi$ is the feature vector. Its not clear whether this assumption can be satisfied in a straight forward manner when using neural networks. 
5. Regarding Assumption 4.4: Since this assumption holds for every state, when dealing with uncountably infinite states, it is unclear as to how $\lambda_1$ can be uniformly bounded from below across all states.

### Questions
1. Equation 1, what does the measure $d(a\times s')$ represent?
2. Theorem 4.9 $\alpha = \frac{c}{\sqrt{T}}$, what are the typical values of $c$ in this learning rate?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors analyze single time scale actor critic algorithms for continuous state and action space control problems. The results show that the convergence to a stable point at a rate that depends on the number of iterates and the width of the controlling network.

### Strengths
Strong results for an important problem. 

Considering Markovian sampling makes the result even stronger. 

The assumptions are explained very clearly. This is commendable as there are many assumptions ....

### Weaknesses
It is not clear how $c$ is chosen for THM 4.9 to hold. This seems to be something the algorithm would have to know a-priori. But how can that be? The constant seems to be a complex function of the problem parameters, making it difficult to determine in advance. This raises concerns about the practical applicability of the theorem. 

I don't understand why one would not take $m \to \infty$: in that case the second term is 0, but wouldn't neural network convergence issues emerge? The bound provided in the paper does not seem to account for potential issues arising from the neural network approximation error as $m$ increases. Specifically, the relationship between the approximation error, denoted as $\epsilon_{app}$, and the width of the network, $m$, is not clearly defined. While increasing $m$ might reduce the second term in the bound, it could simultaneously increase $\epsilon_{app}$, leading to an overall worse convergence. This trade-off is a critical aspect that needs further clarification.

I would appreciate to see a proof outline. Especially, pointing out to the novel elements of the analysis is crucial. Since the paper is really an exposition to the appendix where the proofs are, it is rather hard to follow where the real novelty is. 

Finally, if there is any empirical evidence for the (low) dependence on $m$ empirically for large $m$, this would go a long way to convincing me in the utility of the paper. The current theoretical results suggest a certain relationship between the convergence rate and $m$, but the practical implications of this relationship are not fully explored. A more comprehensive empirical evaluation across various $m$ values, especially for larger networks, is needed to validate the theoretical findings and demonstrate the practical utility of the proposed algorithm.

### Questions
Please see weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides a theoretical analysis of an actor critic-type algorithm in continuous spaces, and contributions are theoretical in nature.

### Strengths
- The paper is written well. 
- The mathematical analysis is easy to read.

### Weaknesses
There are some weaknesses in the proposed approaches, as listed below:

1. Continuous spaces are important and challenging, but the analysis seems to make significant assumptions that are not realistic in practice. Assumption 4.7 seems particularly concerning. While the authors motivate the study of continuous spaces for practical reasons, the specific constraints imposed by this assumption, especially condition (c), appear to limit the applicability to a narrow range of functions. For instance, it is not clear if commonly used parameterizations like a standard Gaussian policy would satisfy this condition. It would be helpful to see concrete examples of practically relevant continuous policies that provably meet Assumption 4.7, beyond the mentioned uniform distribution. The authors need to elaborate on the implications of this assumption for real-world applications.

2. Given the existing analysis in the literature, because the authors are operating in parametrized settings, extending the analysis to continuous settings seems incremental and novelty is limited. The authors should explicitly address the specific challenges that arise when moving from tabular settings to continuous, parameterized settings. For example, how does the use of function approximation impact the convergence guarantees compared to the tabular case? What new complexities are introduced by the need to estimate gradients in a continuous space? The proof appears to follow a similar structure to that in the paper by Chen and Zhao [1], with some generalizations of the assumptions. However, the authors need to clearly articulate what novel theoretical contributions are made beyond these generalizations.

3. Assumption 4.6 also requires further discussion. The authors cite several papers, but most of them focus on tabular settings. It is not immediately obvious that geometric mixing, a property often assumed in the tabular case, will hold under the same conditions in continuous spaces with function approximation. The authors should provide a more rigorous justification for why this assumption is reasonable in their setting, or at least discuss the potential limitations if it does not hold.

4. The connection between Assumption 4.5 and exploration is not well-established. While the authors claim that this assumption relates to exploration, the explanation is not entirely convincing. It would be beneficial to provide a more intuitive and perhaps visual explanation of how this assumption guarantees sufficient exploration. Are there any specific scenarios, perhaps with simple examples of continuous state spaces, where one could demonstrate how a violation of Assumption 4.5 would correspond to insufficient exploration?

5. Discussing all these assumptions is important because the paper's motivation is to study the analysis in the most practical settings; if the assumptions are not realistic, that would defeat the purpose. The authors need to carefully consider the trade-off between the generality of their theoretical framework and its practical relevance. It is crucial to strike a balance between making simplifying assumptions for analytical tractability and ensuring that the results are meaningful for real-world applications of actor-critic methods in continuous spaces.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2
