# Glocal Hypergradient Estimation with Koopman Operator

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Gradient-based hyperparameter optimization methods update hyperparameters using hypergradients, gradients of a meta criterion with respect to hyperparameters.
Previous research used two distinct update strategies: optimizing hyperparameters using global hypergradients obtained after completing model training or local hypergradients derived after every few model updates.
While global hypergradients offer reliability, their computational cost is significant; conversely, local hypergradients provide speed but are often suboptimal.
In this paper, we propose \emph{glocal} hypergradient estimation, blending ``global'' quality with ``local'' efficiency.
To this end, we use the Koopman operator theory to linearize the dynamics of hypergradients so that the global hypergradients can be efficiently approximated only by using a trajectory of local hypergradients.
Consequently, we can optimize hyperparameters greedily using estimated global hypergradients, achieving both reliability and efficiency simultaneously.
Through numerical experiments of hyperparameter optimization, including optimization of optimizers, we demonstrate the effectiveness of the glocal hypergradient estimation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a hypergradient descent method that uses local hypergradients to estimate the global hypergradient. The method is based on Koopman operator theory which uses a finite-dimensional linearization of the nonlinear dynamics of the hypergradient. Authors characterize the estimation error and provides detailed comparisons on the computational complexities of Glocal HGD, local HGD, and global HGD. Finally, they present experiments that show the practical efficacy of the method.

### Strengths
The paper studies an important problem, since hyperparameter optimization is a common challenge in training neural nets. The paper's approach using Koopman operator theory is clever and connects hyperparameter optimization to nonlinear dynamical systems. The algorithm and the computational complexities are clearly written, and I appreciate the diagnostic plots in the experimental section.

### Weaknesses
1. Important design choices are not given: (1) how should we select the dimension of the Koopman operator $n$? Intuitively, $n$ should depend on properties of the underlying dynamical system, and it would be helpful to have some guidelines. Specifically, what are the trade-offs between choosing a small $n$ (which might lead to a poor approximation of the Koopman operator) and a large $n$ (which increases computational cost)? (2) how should we select $\textbf{g}$? Authors use Hankel DMD in the experiments, and it would be great to provide some justification. For example, why is a time-delayed embedding appropriate for this problem, and how does the choice of the delay affect the performance of the method? Are there other choices for $\textbf{g}$ that might be more appropriate for different types of hyperparameter optimization problems? 

2. Experiments: (1) the experiments are relatively small scale. Authors mention that global hypergradients are difficult to obtain for larger models, but still it would be good to compare Glocal to other baselines, for example the best tuned SGD. Without larger scale experiments, it is difficult to know how the proposed method scales with model size. It is also unclear how the performance of Glocal compares to simpler hyperparameter optimization methods like random search or grid search, especially given the computational overhead of estimating the Koopman operator. (2) it would be useful to compare Glocal with the best tuned SGD/Adam as a baseline (3) it would be great to verify empirically that Glocal can indeed estimate the global hypergradient. If I understand correctly, one can compare the estimated gradient with the true global hypergradient. What is the error between the estimated and true hypergradient, and how does this error affect the performance of the method?

3. Theoretical analysis: Theorem 3.1 assumes a Koopman operator of dimension $n$ exists. Without specifications on $n$, this result is less meaningful as $n$ can be very large. However, a large $n$ can make the Glocal method impractical. It would be helpful to provide justification and guidance on $n$. Specifically, what are the conditions under which a finite-dimensional Koopman operator exists, and how can we determine a suitable value for $n$ in practice? The theorem should also discuss the impact of approximation error when the true Koopman operator is infinite-dimensional.

4. Section 2.3 is not clear: (1) Line 172, what is the relationship between $\phi$ and $\varphi$? The decomposition of $g$ is written in $\phi$ on line 172 but in $\varphi$ in eq. (7). (2) Eq. (8) is not precise, because large $\lambda$'s will diverge, but the arrow notation usually means convergence. It would be more precise to state that the hypergradient is approximated by the leading eigenvector of the Koopman operator. (3) The notation for the set of measurement functions $\textbf{g}$ and the individual functions $g_i$ is confusing because they can be very different from the original function $g$ and yet use the same letter. It would be helpful to use different notation to distinguish between the original function $g$ and the measurement functions $g_i$.

### Questions
1. Can the proposed method handle changing dynamics, given that the training dynamics change over time (initially the loss drops significantly and then less so)?
2. For experiments, how do the results change over different initial learning rates? Can Glocal HGD always converge to a good learning rate no matter what the initial learning rate is?
3. Why does Glocal outperform global HGD towards the end of training?

Also see Weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel method called glocal hypergradient estimation for hyperparameter optimization. This method combines the computational efficiency of local hypergradients with the reliability of global hypergradients. It utilizes Koopman operator theory to approximate global hypergradients from the trajectory of local hypergradients, enabling efficient and effective hyperparameter updates. Finally, the paper validates the effectiveness of the proposed method in hyperparameter optimization through experiments.

### Strengths
1. The integration of Koopman operator theory to enhance hypergradient estimation is a novel approach, offering a fresh perspective on hyperparameter optimization.

2. The method significantly reduces computational costs compared to traditional global hypergradient approaches.

3. The approach is scalable to large-scale problems, making it applicable to real-world deep learning tasks. Furthermore, the paper provides numerical experiments demonstrating the method's effectiveness in various scenarios.

### Weaknesses
1. Algorithm 1 and Theorem 3.1 rely on assumptions about the spectral radius and stability, which may not hold in all cases. Specifically, the assumption that the Koopman operator can be well-approximated by a finite-dimensional linear operator is a strong one, and the paper does not provide sufficient justification for when this assumption is valid in the context of hyperparameter optimization. The practical implications of violating this assumption, such as divergence or instability in the hyperparameter optimization process, are not discussed.

2. The theoretical foundation involving Koopman operators may be complex for practitioners unfamiliar with the concept. The paper introduces this concept without sufficient background or intuitive explanation, making it difficult for a broader audience to grasp the core ideas and potential limitations. The connection between the Koopman operator and the dynamics of hypergradients is not clearly established, and the practical relevance of this connection could be better motivated.

3. The experiments are somewhat limited. Could additional datasets be included, or could comparative experiments be conducted on other models as well? The current experiments are primarily focused on image classification tasks, and it is unclear how the proposed method would perform on other types of problems, such as natural language processing or time series analysis. Furthermore, the lack of experiments on different model architectures limits the generalizability of the findings.

4. The presentation of the experimental results is somewhat unclear. For example, all the experimental results in Section 4.2 are only summarized in Table 2, with no accompanying figures. Could Table 3 offer a more detailed explanation? The absence of visual aids makes it difficult to assess the convergence behavior and performance of the proposed method compared to the baselines. The specific metrics used in the experiments, and their relevance to the hyperparameter optimization problem, could also be better explained.

### Questions
1. In equation (9), could you provide an analysis of the computational complexity of solving the optimization problem w.r.t $A\in \mathbb{C}^{n\times n}$? Furthermore, are there any potential challenges in its implementation?

2. In equation (13), the computation of $g^\dagger$ involves solving a system of linear equations $g^\dagger g(x) = x$. How does the computation affect the overall complexity of Algorithm 1?

3. In Section 4.1, why is the Global curve missing in Figure 3? Could you discuss any implications this might have for the comparison between methods?

4. How does the proposed approach compare with specific state-of-the-art hyperparameter optimization methods, such as Bayesian optimization or evolutionary algorithms, in terms of performance metrics like accuracy or convergence speed, as well as computational overhead?

There are some typos:
1. In equation (1), the meta-level function is expressed as $\tilde{l}(\theta^*(\Phi);\tilde{D})$. However, the meta objective in line 37 is written as  $\tilde{l}(\theta,\Phi;\tilde{D})$

2. In equation (9), the expression $\sum\limits_{t=0}^{t-1}$ has a conflict because the variable $t$ is used both as the index and the limit of summation.

3. In line 266, "requires time $O(\tau p)$ and space $O(p)$ complexities" should be "requires time complexity of $O(\tau p)$ and space complexity of $O(p)$".

4. The sentence in line 325 seems to be awkwardly structured.

### Soundness
2

### Presentation
2

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
This work considers the problem of hyperparameter optimization for bilevel optimization problems. By leveraging Koopman operator theory, the authors provide a method to estimate global hypergradients (usually only available after fully solving the inner problem) with local hypergradient trajectories (partial solution trajectories of the inner prolbem).

### Strengths
I'm on the fence on this submission -- the method is well-motivated and the derivation is for the most part clear, but I felt that the experimental results are somewhat of a let down.

* The paper is overall well-written, with a few minor typos. The authors do an admirable job of making their theory tractable and easy to read.
* Meta optimization is an important problem and the research setting is well-motivated.
* The authors provide a thorough runtime comparison and associated discussion, which shows that their approach is as computationally efficient as using local hypergradient.

### Weaknesses
1. I'm somewhat suspicious of the handwaving around non-unit eigenvalues. Specifically, consider the section from line 246 - 252, where basically all eigenvalues besides those which are equal to one are discarded. Is there any theoretically grounded explanation from doing so? If the koopman operator says that the global hypergradients should oscillate, when intervene and artificially eliminate those modes? The justification that the hypergradient is stable after long training is not sufficient, as the Koopman operator is supposed to capture the dynamics of the system, and discarding modes arbitrarily seems like a significant deviation from the theory. Similarly, when solving the DMD for $K$ as in (9), I don't see why you would get modes with an eigenvalue exactly equal to one as there is random noise in the collected hypergradient data. The authors should provide a more rigorous justification for this truncation, perhaps by analyzing the effect of the discarded modes on the approximation error.
2. The experiment settings are minimal, and only involve relatively simple image classification tasks. The lack of diversity in the experimental setup makes it difficult to assess the general applicability of the proposed method. It would be beneficial to see results on more complex and diverse datasets, as well as different types of bilevel optimization problems beyond image classification. For example, experiments on hyperparameter optimization for reinforcement learning or meta-learning tasks would be more convincing.
3. The experimental results somewhat conflict with the aims of the paper. Namely, the performance of the global hyperparameter estimation degrades severely in the bottom-left panel of Figure 2. In Figures C.2 and C.3 in the appendix are even worse. The appendix briefly mentions "loss explosion," but a further discussion is warranted, since my impression is that the whole point of this paper is to provide a fast way of approximating the "gold-standard" global hypergradients! The authors need to provide a more thorough analysis of why the global hypergradient estimation fails in these cases, and what are the limitations of their approach. The claim that the method avoids issues with long-horizon training is not sufficiently supported by the presented results.
4. Additional baselines of estimating the global hypergradient should be considered. At least: simply using the hypergradient at iteration $\tau$ as a substitute for $h_T$ (just once, not continuing to train as in local hypergradient estimation). This would provide a more direct comparison to the proposed method and help to isolate the benefits of using the Koopman operator.

### Questions
Comments & questions
1. I suggest mentioning, at least in passing, the initialization of $\theta_0$ beneath equation (4).
2. Minor notational note: in your problem formulation, you are adopting the convention of outer-level symbol carrying an additional tilde. The parameters are the exception ($\theta$ vs $\phi$); however, for the optimization algorithm, you are using capital $\Theta$ and $\tilde \Theta$. I like having separate symbols for the parameters, so for consistency I would recommend using a capital $\Phi$ instead of $\tilde \Theta$ for the outer-level gradient step. Or find a non-theta symbol to use to denote an optimization step. Just a suggestion, I'll leave it up to the authors.
3. In equation (8), why do terms which diverge ($|\lambda_j| > 1$) no longer appear in the expression? I would think that they would dominate all other modes.
4. For what trajectory $x_t$ is (9) being solved? Wouldn't it make sense to look at many trajectories from different initial conditions?
5. I'm confused about the implications of the bound in Theorem 3.1. The bound aggregates terms corresponding to non-unit eigenvalues, presumably becasue these were discarded previously (see Weakness 1). Wouldn't your theorem suggest that including these terms would result in less estimation error?
6. I don't understand the measurement defined in line 345. How can the measurement function depend on future hypergradients, some of which potentially haven't been computed yet? For example, how would you compute $g(h_{t^*})$ where $t^*$ is the biggest index in $\mathcal{I}_s$?

Minor notes:
* Line 123: "global hypergardient"
* Line 167: the inputs and outputs of $g$ should be clarified; I presume $g: R^m \to R$
* Line 172: mixing up $\phi$ and $\varphi$
* Line 234: "as in Section 2.3"
* Line 334: "outer steps"
* Figure 4: periods after left/middle/right

### Soundness
3

### Presentation
3

### Contribution
2
