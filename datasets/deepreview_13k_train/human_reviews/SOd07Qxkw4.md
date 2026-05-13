# Improved Convergence Rate for Diffusion Probabilistic Models

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Score-based diffusion models have achieved remarkable empirical performance in the field of machine learning and artificial intelligence for their ability to generate high-quality new data instances from complex distributions. 
Improving our understanding of diffusion models, including mainly convergence analysis for such models, has attracted a lot of interests.
Despite a lot of theoretical attempts, there still exists significant gap between theory and practice.
Towards to close this gap, we establish an iteration complexity at the order of $d^{1/3}\varepsilon^{-2/3}$, which is better than $d^{5/12}\varepsilon^{-1}$, the best known complexity achieved before our work.
This convergence analysis is based on a randomized midpoint method, which is first proposed for log-concave sampling \citep{shen2019randomized}, and then extended to diffusion models by \citet{Gupta2024Faster}. 
Our theory accommodates $\varepsilon$-accurate score estimates, and does not require log-concavity on the target distribution.
Moreover, the algorithm can also be parallelized to run in only $O(\log^2(d/\varepsilon))$ parallel rounds in a similar way to prior works.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper focuses on enhancing the theoretical convergence rate of diffusion models, which are widely used for high-quality data generation in various machine learning applications. Traditional analyses show a significant gap between theoretical complexity and the number of steps needed in practice for good performance. This work introduces a faster convergence rate of $O\left(d^{1 / 3} \epsilon^{-2 / 3}\right)$, an improvement over previous bounds, achieved by adapting a randomized midpoint method. The authors' analysis allows for smooth, $\epsilon$-accurate score estimates without assuming restrictive properties like log-concavity in the data distribution. Additionally, they propose a parallel sampling technique that minimizes the number of parallel rounds required, further increasing efficiency.

### Strengths
1. Theorem 1 introduces a new convergence rate for diffusion models, specifically $O\left(d^{1 / 3} \epsilon^{-2 / 3}\right)$, which is faster than previous results (e.g., $O\left(d^{5 / 12} \epsilon^{-1}\right)$ by Gupta et al., 2024). This improvement relies on an adaptation of the randomized midpoint method from log-concave sampling and brings theoretical guarantees closer to practical performance.
2. Theorem 2 paper presents an efficient parallel sampling method that reduces the number of parallel rounds needed while maintaining the improved convergence rate.

### Weaknesses
1. Theorem 2 describes an efficient parallel sampling method with fewer parallel rounds, but the practical implementation details are limited. like How does memory consumption scale with $d$ in parallel sampling? Are there specific cases or datasets where the parallel method might fail to produce substantial speedups due to communication overhead between processors? If so, what alternative strategies or adjustments would the authors suggest?
2. Are there specific types of data distributions (e.g., multimodal, heavy-tailed) that the authors believe may not meet the framework’s assumptions?

### Questions
See weaknesses part above.

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
4

### Summary
This paper studies the diffusion models and proposes sampling method based on randomized midpoint for probability flow ODE.  Their method has an improved sequential iteration complexity as $Ld^{1/3}/\epsilon^{-2/3}$ and similar parallel iteration complexity $\log^2(d/\epsilon)$, with measurement as total variance.

### Strengths
- The paper studies the complexity of the inference process of diffusion models, which is a problem of significane interest and practical importance in the related fields.

- the sequential itertaion complexity is improved from $L^{5/3}d^{5/12}\epsilon^{-1}$ to $Ld^{1/3}\epsilon^{-2/3}$.

### Weaknesses
 - This main drawback is the additional smoothness assumption on the score function and its estimation. This assumption, while potentially allowing for improved convergence rates in some scenarios, significantly limits the applicability of the method in practice. Many real-world score functions, especially those arising from complex data distributions, may not satisfy such strong smoothness conditions, thus restricting the practical use of this method.

- The algorithm and the proof presented in Lemma 3 are difficult to follow. It may be helpful to provide more detailed explanations or include additional diagrams for clarity. The current description lacks sufficient detail to fully grasp the nuances of the error analysis, particularly how the randomized midpoint approach specifically controls the error terms. The connection between the discretization of the ODE and the error bounds is not clearly articulated, making it hard to assess the validity of the proof.

- Your method looks like N=poly(T)-stage Runge-Kutta method with random Runger-Kutta matrix. Then $\varepsilon^{-1/N}$ iteration complexity is expected although such method needs higher order smooth for ode case [1]. Calling it the midpoint method seems somewhat misleading.

### Questions
- I am curious about the results when your method is applied to the implementation of diffusion models using SDEs

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of sampling from a diffusion model, and provides an algorithm with the best known dimension dependence of $d^{1/3}$, an improvement over $d^{5/12}$ of previous work. It also improves the dependence on the score estimation error $\epsilon$, from $1/\epsilon$ to $\epsilon^{-2/3}$. The algorithm uses the randomized midpoint method along with corrector steps, a strategy first proposed for diffusion by Gupta et. al. (2024). The authors show that a new analysis of this algorithm (with some modifications) achieves the improved iteration complexity bounds.

### Strengths
Studies an important and well-studied problem and develops new techniques that allow the authors to show the best known iteration complexity. Perhaps surprisingly, as of this work, we have faster algorithms for sampling from diffusion models than for log-concave sampling.

### Weaknesses
While I appreciate the brevity of the paper, I feel that the core intuition could be explained better for easier digestion. The paper would also benefit from a more detailed discussion of the limitations of the proposed approach. Specifically, the analysis relies on a smoothness condition on the score function, and it is unclear how the results would extend to more general settings. The current discussion of the non-Lipschitz setting is insufficient, and the paper should elaborate on the specific challenges in this case. For instance, what are the key bottlenecks in the analysis that prevent a direct extension, and what alternative techniques might be considered? Furthermore, the paper should provide more insight into the practical implications of the improved bounds. While the theoretical improvement is significant, it would be helpful to understand how this translates to real-world performance, particularly in high-dimensional settings. Finally, the connection to log-concave sampling could be made more precise. While the authors mention that their results apply to the log-concave case, it is not clear whether the techniques can be used to improve bounds for standard Langevin dynamics in total variation, which is a related but distinct problem.

### Questions
- Is it possible to translate these techniques to obtain improved bounds for log-concave sampling in TV? Please update the paper to discuss any challenges in doing so.

- Can you condense the core intuition and explain it in a proof overview? Please add a proof overview to the paper that explains the key insight relative to prior work in a condensed form.

- Does this work have any implications for the setting where the score is not assumed to be Lipschitz? Please add a discussion of the challenges in translating these techniques to the non-Lipschitz setting, or what bound you could hope to get.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper considers the well-studied question of sampling from a smooth distribution $p$ given approximate access to its score functions $\nabla \ln p_t$, where $p_t$ is $p$ convolved with some level of noise.

Recent work has shown that this can be done for essentially arbitrary smooth distributions, with iteration complexity $L^a d^b/\epsilon^{c}$ for progressively smaller constants $a,b,c$. Here $L$ is the Lipschitz constant for the score functions and score estimates. Recent works of Chen et al. and Gupta et al. culminated in bounds of $(a,b,c) = (2/3, 5/12, 1)$. The present work gives a clever analysis that pushes this down to $(1, 1/3, 2/3)$.

While not explicitly written as such, the sampler the algorithms propose can be thought of as a predictor-corrector scheme: it alternates between reverse diffusion steps (implemented via a slight variant of the randomized midpoint method) and steps in which additional noise is added to the trajectory. The corrector steps allow one to essentially convert Wasserstein closeness between the algorithm and the true (continuous) reverse diffusion into KL closeness, so that the KL between the algorithm and the true distribution is small by chain rule for KL.

### Strengths
This result was quite surprising to me. It is a big open question to achieve $d^{1/3}$ dependence for log-concave sampling in KL, and I had expected that the result in the present paper would not be achieved until that milestone had been reached. 

The key insight, which is somewhat buried in the notation, is the following. The prior works of Chen et al. and Gupta et al. similarly adopted a predictor-correct approach, but their corrector was based on running underdamped Langevin dynamics to keep the sampler stationary at a fixed noise level. But this required a discretization analysis for underdamped Langevin in KL; while it is conjectured that one can achieve $d^{1/3}$ dependence for this (and indeed, this is the best known rate one can achieve for Wasserstein), the best known analyses are currently stuck at $d^{1/2}$. 

The authors of the present work sidestep this with an ingenious idea: instead of running underdamped Langevin at a fixed noise level, they simply add Gaussian noise in the corrector step and rescale. It is much more straightforward to see that this converts Wasserstein closeness to KL closeness. Instead of preserving the noise level however, this has the effect of increasing the noise slightly. But if the rescaling is chosen appropriately, it still remains on the trajectory of the reverse diffusion! By balancing appropriately between the progress the predictor step makes in reducing the noise level and the progress the corrector step undoes by raising the noise level, the authors are able to circumvent the issues from prior work and achieve the desired $d^{1/3}$ scaling. This idea of using a corrector step which raises the noise level while staying on the trajectory of the true reverse diffusion is simple and very nice.

### Weaknesses
My main complaint is that the writing is very dense and it was very hard from a quick glance to extract the key idea outlined above. If this work is to be accepted, the authors should make sure to include a technical overview section where they explain the intuition for how they are able to go beyond the prior works of Chen et al. and Gupta et al.

There might be some complaints about the fact that they need to assume Lipschitzness of the score and the score estimate, but note that no sublinear-in-$d$ bounds are known for diffusions under less stringent assumptions, so I wouldn't count this as a real downside.

I'm not sure I followed why one needs to modify randomized midpoint for the "predictor" part of the sampler, i.e. in the computation of the $Y_{k,n}$'s. Why couldn't one just run the predictor analysis in Gupta et al. off the shelf to get an analogue of Lemma 3?

### Questions
I'm not sure I followed why one needs to modify randomized midpoint for the "predictor" part of the sampler, i.e. in the computation of the $Y_{k,n}$'s. Why couldn't one just run the predictor analysis in Gupta et al. off the shelf to get an analogue of Lemma 3?

### Soundness
4

### Presentation
2

### Contribution
4
