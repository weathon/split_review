# Tighter Performance Theory of FedExProx

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
We revisit \algname{FedExProx} -- a recently proposed distributed optimization method designed to enhance convergence properties of parallel proximal algorithms via extrapolation. In the process, we uncover a surprising flaw: its known theoretical guarantees on quadratic optimization tasks are no better than those offered by the vanilla Gradient Descent (\algname{GD}) method. Motivated by this observation, we develop a novel analysis framework, establishing a tighter linear convergence rate for non-strongly convex quadratic problems. By incorporating both computation and communication costs, we demonstrate that \algname{FedExProx} can indeed provably outperform \algname{GD}, in stark contrast to the original analysis. Furthermore, we consider partial participation scenarios and analyze two adaptive extrapolation strategies -- based on gradient diversity and Polyak stepsizes --- again significantly outperforming previous results. Moving beyond quadratics, we extend the applicability of our analysis to general functions satisfying the Polyak-Łojasiewicz condition, outperforming the previous strongly convex analysis while operating under weaker assumptions. Backed by empirical results, our findings point to a new and stronger potential of \algname{FedExProx}, paving the way for further exploration of the benefits of extrapolation in federated learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work revisited FedExProx, a recently proposed algorithm for FL, and furthered the convergence analysis. They first found the existing analysis of FedExProx is not as good as vanilla GD on quadratic problems. Then they provided a refined analysis for FedExProx on non-strongly convex quadratic problems regarding the time complexity, which beats GD. They also provided the analysis in partial participation, adaptive extrapolation strategy, and PL condition, and complete the story with numerical experiments.

### Strengths
1. Provided a refined analysis for FedExProx in some cases
2. Extend the analysis to more cases like partial participation and PL condition.
3. The paper is clearly written.

### Weaknesses
1. The scope of research is restricted to quadratic problems only, which may limit the significance of the work without enough motivation.
2. The claimed outperformance compared to GD (Theorem 4.3) is achieved with additional information on the communication protocol parameter $\mu$, computation protocol parameter $\tau$. I am skeptical that such setting are a bit coarse, I am not sure whether the communication parameter $\mu$ is easy to detect in the system, also $\tau$ corresponds to uniform computation cost for all devices, which may disregard the heterogeneity in computation among devices. Regarding authors claimed to study an empirically promising algorithm, I think authors should add more discussion on it for clarification, and to further improve the significance.
3. The stepsize choice in Theorem 6.1 depends on the exact value of the Moreau envelope or its lower bound, which is impractical in my opinion. 
4. I suggest adding vanilla GD into your experiments to verify that your outperformance theory works in practice.

### Questions
1. In your quadratic problems, I think the proximal operator attains a closed-form expression (as Eq(22) in Appendix C), why do you still use GD as the subroutine, rather than directly use the closed-form solution in Section 4.1?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper proposes a new analysis for FedExProx algorithm.

### Strengths
The analysis of the algorithm seems to be solid. It seems to improve over previous results. The authors also extended the results to partial participation scenarios.

### Weaknesses
The experiments only involves synthetic data.

### Questions
Have the authors considered running experiments on more realistic datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors re-examine a new approach to federated learning called FedExProx. 
They analyze it in the case of convex quadratic objectives all while taking lags in computation and communication under consideration, 
and show that it benefits standard approaches. This improves over previous analysis of the method.

### Strengths
1) The authors make a good job by taking into consideration also practical considerations like lags in communication and computation and reflecting them in the overall performance of the method

2) The authors illustrate a specific diagonal case where the improvement of what they suggest is obtained

### Weaknesses
1) The paper does not take the noise due to the samples into account: this is missing both in the convergence rates as well as not taken into account in
the cost of computing the prox operation

2) Focusing on quadratic functions is very limiting and does not properly reflect the more general case. Indeed, in the quadratic case, the gradients are linear in the weights which is a unique property that does not generalize

3) For quadratic functions, the authors should compare their approach to the FedAvg algorithm. 
Noticelbly, the work of (Woodworth et al): (Is Local SGD Better than Minibatch SGD?) shows that for quadratic functions then FedAvg obtains the best possible convergence guarantees. So it is not clear what is the benefit of FedExProx on FedAvg in this case?

4) The extension to the case where the Moreu envelope is PL is nice, but it is not clear if it applies in any interesting case?

### Questions
) Please compare to FedAvg in the quadratic case, what do you get?

2) The parameter $L_{S,\gamma}$ is confusing to me, shouldn't it increase with $S$, similarly to randomized coordinate descent?

### Soundness
3

### Presentation
3

### Contribution
2
