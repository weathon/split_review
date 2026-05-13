# Flexible Active Learning of PDE Trajectories

- Decision: Reject
- Scores: 8, 5, 8, 8, 5

## Abstract
Accurately solving partial differential equations (PDEs) is critical for understanding complex scientific and engineering phenomena, yet traditional numerical solvers are computationally expensive. Surrogate models offer a more efficient alternative, but their development is hindered by the cost of generating sufficient training data from numerical solvers. In this paper, we present a novel framework for active learning (AL) in PDE surrogate modeling that reduces this cost. Unlike the existing AL methods for PDEs that always acquire entire PDE trajectories, our approach strategically generates only the most important time steps with the numerical solver, while employing the surrogate model to approximate the remaining steps. This dramatically reduces the cost incurred by each trajectory and thus allows the active learning algorithm to try out a more diverse set of trajectories given the same budget. To accommodate this novel framework, we develop an acquisition function that estimates the utility of a set of time steps by approximating its resulting variance reduction. We demonstrate the effectiveness of our method on several benchmark PDEs, including the Heat equation, Korteweg–De Vries equation, Kuramoto–Sivashinsky equation, and the incompressible Navier-Stokes equation. Extensive experiments validate that our approach outperforms existing methods, offering a cost-efficient solution to surrogate modeling for PDEs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose an active learning framework for training surrogate models that can aid in solving partial differential equations. Traditional solvers for partial differential equations are computationally expensive, which motivated the development of surrogate models to efficiently solve PDEs. However, for training these surrogate models, costly numerical simulation data are required. Current active learning based strategies for training such surrogate models require entire PDE trajectories from a given starting condition, which is costly. The authors propose a flexible sampling strategy, which does not require entire PDE trajectories, and only samples upto a given budget. Experiments show that the method performs better in terms of RMSE compared to baseline.

### Strengths
The motivation of the work is presented well. The related literature is reviewed well in the introduction section and related work section.

### Weaknesses
The methodology of the paper requires a lot more elaboration. Here are a few points that are not clearly answered in the current manuscript:
How does sparse sampling works for numeric solvers? For example, given a pattern S = {T, F,F,..., T}, which is basically sampling an initial condition and final condition, how will we sample the data here without sampling all intermediate states? If we cannot do that, then how does the method reduce the cost of acquiring training data? The explanation of how the surrogate model is used to generate intermediate states is missing, making it unclear how the sparse sampling strategy actually reduces the computational cost associated with numerical solvers. The paper needs to explicitly state that the surrogate model is used to predict the intermediate states, and how this prediction is incorporated into the training process.
How much computation cost, data acquisition cost is reduced in this framework? The experimental results report the accuracy of the trained model, however since the original motivation of the work is about reducing such costs, presenting these additional statistics makes more sense than only reporting model accuracy alone. The paper needs to quantify the reduction in computational cost, not just the model accuracy. It should include metrics such as the number of numerical solver calls, the total time spent on data acquisition, and a comparison of these metrics with the baseline methods. Without these metrics, it is difficult to assess the practical impact of the proposed method.
Algorithm 1 should be described line by line, probably best to do this at the end of section 3.3. The description of the algorithm is too high level and lacks the necessary details for reproducibility. The paper needs to provide a step-by-step explanation of each line in Algorithm 1, including the specific operations performed at each step, the meaning of the variables, and the conditions for accepting or rejecting a proposed pattern. The current description is insufficient for a reader to understand and implement the algorithm.
Figure 1 needs some rethinking, currently it is difficult to see the author’s motivation, or the entire framework from this figure alone. Perhaps show how the cost increases with added data acquisition side by side with the baseline and FLEXAL strategy. The figure should clearly illustrate the difference in data acquisition costs between the proposed method and the baseline. It should show how the proposed method reduces the number of calls to the numerical solver while maintaining a comparable level of accuracy. The current figure does not effectively convey this key aspect of the work.

### Questions
See weakness section above

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a new approach of data acquisition for active learning. They suggest considering a subset of the time steps from a standard numerical solver along a trajectory, and use a fitted surrogate model to approximate the remaining of data. Given the proposed strategy does not provide a significant improvement compared to alternative methods consistently, I believe the current version of manuscript should not be accepted.

### Strengths
The paper makes a nice comparison between their suggested method of active learning and the other available methods in the literature.

### Weaknesses
I think the presented idea lacks novelty, and the shown numerical results are not suggesting any significant improvement compared to other methods.

**Major:**

- The proposed method does not seem to have a significant improvement compared to the other compared methods. For example in Fig3, RMSE of proposed strategy is slightly (around 10%) better than SBAL, random, or QbC, for KdV, KS, and NS. I wonder why the method performs so much better in case of heat equation. It definitely needs further investigation.

**Minor:**

- P2 line95, What is the space of $\mathbb{X}$? Please define the space.
- P2 line 99, I highly doubt uniqueness of the operator G_{t0}. Given solution at $t=0$ and $t=Delta t$, there may exist infinite PDEs that satisfy both initial and final condition. 
- P3 eq. 2, Wouldn't PINN loss help here, if the PDE is known?
- Algorithm 1, line 7: please clarify notation.

### Questions
**Major:**

- The proposed method does not seem to have a significant improvement compared to the other compared methods. For example in Fig3, RMSE of proposed strategy is slightly (around 10%) better than SBAL, random, or QbC, for KdV, KS, and NS. I wonder why the method performs so much better in case of heat equation. It definitely needs further investigation.

**Minor:**

- P2 line95, What is the space of $\mathbb{X}$? Please define the space.
- P2 line 99, I highly doubt uniqueness of the operator G_{t0}. Given solution at $t=0$ and $t=Delta t$, there may exist infinite PDEs that satisfy both initial and final condition. 
- P3 eq. 2, Wouldn't PINN loss help here, if the PDE is known?
- Algorithm 1, line 7: please clarify notation.

### Soundness
3

### Presentation
3

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
For a partial differential equation (PDE) $\partial_t u = F(u, \partial_x u)$, fixed time-interval $\Delta t$, and a solution/evolution operator $G$, which satisfies $G u(t, \cdot) \approx u(t+\Delta t, \cdot)$, the context for the submission is to approximate $G$ with a surrogate through active learning.
The submission proposes an alternative to computing full trajectories of the PDE solution and appending those to the dataset. Namely, the suggestion is to choose a sampling pattern S ~ (True, False, True, True, ...), simulate the PDE using a mix of surrogate and numerical solver (depending on True/False at each step), append all indices corresponding to the numerical solver to the dataset (skip the surrogate steps), retrain, and repeat.
The sampling pattern is chosen by optimising an acquisition function based on variance reduction, respectively, a batch version of it.


Now, the driving question for assessing this method is how much this "sparse" sampling pattern improves over full-trajectory (or initial-step) active learning (e.g., Musekamp et al., 2024). The manuscript investigates an answer to this question on typical PDE benchmark problems.

### Strengths
The proposed algorithm is a clear generalisation of existing PDE active-learning methods: Instead of acquiring full trajectories or initial conditions, any combination of time points can now be used.
The manuscript is generally easy to follow (I point out specific questions below, but these are really minor). The experiments are comprehensive, and the paper is in good shape overall.

### Weaknesses
The proposed algorithm generalises existing schemes through corresponding choices of sampling patterns. 
However, optimising the sampling pattern is, simply put, a lot of work (concretely, $O(2^L)$ if one doesn't use the greedy selection algorithm, where $L$ is the sequence's length; Section 3.3 discusses this thoroughly). And while this additional work seems to improve the quality of the reconstructions (Tables 1, 2, & 3; Figures 3 & 4), the proposed FlexAL takes significantly longer to run (Table 4).
Whether or not this increased runtime is problematic likely depends on the PDE. 
However, the increased runtime is a weakness of the proposed method compared to existing techniques nonetheless. 

The submission acknowledges this shortcoming and discusses a fix that cuts the number of training epochs for FlexAL. Still, this discussion leaves some questions to be answered. For example, the training epochs could also be reduced for existing methods with corresponding runtime gains, and it needs to be clarified how this affects the results (unless I've missed something; I checked Appendix 5.8 and couldn't find such a discussion).

Now, to convince me that this weakness isn't one, it would suffice to find an example where the additional computation for batch selection (compared to full-trajectory QbC, for instance) can be negligibly small. Alternatively, it would be interesting to see what happens to the reconstruction results in Table 1 or 2 if all columns do not receive the same number of iterations but are limited to roughly the same wall time.

However, I understand that these changes are likely outside the scope of a revision, and I am in favour of accepting this paper without them. That said, if I get convinced that the assessed weakness isn't one, my score would be slightly higher.

### Questions
I group my questions into more important and less important ones.
I don't expect a reply to the less important ones, but I would appreciate some clarification on the more important ones.
The answers do not affect my rating. However, I believe the manuscript would improve if the paper included them.

More important:

- Section 3.2: _Why_ choose the acquisition function based on variance reduction? Are there other candidates, and if so, why are they less suitable?
- Table 1: log-RMSEs of $\approx 0.1$ imply RMSEs of $\approx 1.0$, which seems to be large. Is it fair to assume that the solvers learn anything reasonable? For example, what happens if one plots the solutions and compares the surrogate's solution to the solver's? Suppose the reconstruction is good despite these large errors. Could the table be made clearer (in the sense of "success" meaning "RMSE far below 1") by choosing (for example) relative RMSE over absolute RMSE? 
Table 4: It would be great to include the context of how much runtime a numerical solver needs to simulate Navier-Stokes. Whichever outcome (in terms of "who's faster") is fine, but the context would help assess the efficiency of the active-learning methods. If the solver is slow, the context would underline the statement in line 034 that states how costly numerical solvers can be.


Less important:

- Line 053, "we argue that querying all the states (...) is not cost-efficient": does this sentence perhaps require more nuances? While sparse subsets of trajectories decrease the complexity (on paper), the suggested procedure for finding them is sufficiently expensive that the proposed algorithm is more costly than full-batch versions (Section 3.3, Table 4). 
- Line 095: Perhaps Brandstetter et al. (2022b) are not the best reference for spatiotemporal PDEs. Personally, I don't think this sentence needs any reference, but if one should be used, perhaps something like Evans' "Partial Differential Equations" book would be more appropriate.
- Line 100: This statement about existence would benefit from a reference.
- Line 112: What does "primary focus" mean here? It seems to be the _only_ focus. Have I missed something?
- Line 128: Why does this sentence introduce a distribution of initial conditions, but the rest of the manuscript (for example, Algorithm 1) operates on a pool of initial conditions? I understand that the pool is sampled from the condition, but it might be more reader-friendly to use a pool of conditions throughout.
- Line 262: How do the results depend on this choice of $T$ and $\epsilon$?
- Line 298: The abbreviation "QbC" is used early in the paper (for instance, in line 117 or 204). Maybe it would be good to introduce it before line 298.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Design-of-experiments for training surrogate models of time series. If simulated "experiments" are expensive, then it might be cheaper to train the surrogates sparsely. More specifically, a committee of surrogates is trained to estimate the uncertainty, and then value of new samples, which are then actually sampled and used to train the model.

### Strengths
The idea seems natural; In a sense a lot of machine learning is simply working out which data points need to be observed to train the correct model. In operator learning in particular we suspect much of the effort in training neural operators is wasted. 

This paper is nearly simple, which is IMO great.

### Weaknesses
Given that sparse adaptive sampling from simulators is such a natural idea, the authors' solution "feels" surprisingly contrived. Sampling is strictly by masking over a fixed-timestep simulation pattern; to my mind it would be more satisfying to search for useful initial conditions from the traiing distribution, or to simply give up on rollouts when a given trajectory was no longer adding useful value, or to learn a predictor which could be conditioned on a rollout time, and we might imagine some scheme more elegant than this Bernoulli masking. However, this is not a blocker. Maybe this paper outlines the best progress than can be made at the moment? Maybe the best solution is not that elegant. If so, no problem.

A bigger problem for me is that I have a hard time understanding how the rollout accounts for serial dependencies in the training data. I have done my best to try to understand it, but I suspect that this might be a deficiency in the authors' explanation itself. I would be prepared to revise my recommendation if they could make this part clearer. See Questions below for a lengthier series of questions on that theme. Without clarification on that I cannot really assess the later part of the paper.

`FlexAL` is not IMO a great name; this is not particularly flexible compare to other active learning/DOE methods.

### Questions
I'm having a hard time understanding how the causal dependencies in a simulator are accounted for in this method. Can you lay it out for me? ("Explain it like I'm 5")
AFAICT each successive step in the simulator depends on the previous ones. Figure 6 seems to support this, as does text l283 "in our setting, we cannot directly acquire a time point, because there is a cost in the simulation of the trajectory.").

Reasoning this through and attempting to crosscheck with the text, I haven't been able to work it out.
So if I "mask out" timestep $t$ but I wish to train on timestep $t+1$,  don't I still need to simulate at timestep $t$? How do I save the cost of the $t$th step at full fidelity? I get that we can roll out a surrogate or a solver, and that we can choose which to use, but when we want the actual "ground truth" solver, how do we get that? Does our actual roll-out incorporate mixtures of models, e.g. in a given training run we might have some "mixed" rollout like $\hat{u}^2=G \circ \hat{G}  u^0$? (here $\circ$ is composition) OK, that seems fine, but at a later stage of my training I would get a different output from $\hat{G}$, so my training data would change and then I would need to recalculate $\hat{u}^2$, right? This should introduce an asymmetry between the acquisition functions early in the time series, and later, since the later ones are likely to be sample from some other distribution than the training distribution (e.g. they may have failed to conserve mass or momentum or whatever, when the surrogate roll-out was used).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method of active learning for PDEs. When training a neural operator for PDE, we often generate data using solvers. Solvers can be expensive, and now the question is how we can develop an active learning method to efficiently sample from a solver, in particular for temporal PDEs. 

This paper proposes to train an ensemble of models and use their disagreement as a sign to collect samples.

### Strengths
The paper tackles an important problem in practice.

### Weaknesses
There is a set of weaknesses in this work that the authors are encouraged to address.

1- The novelty. The method is very similar to prior works, with similar equitation function, ensemble approach, and philosophy.

2- One might be able to say that not much about PDE-ness is present in this approach. Similar approaches are also in the game engine, video simulation, and 3D scene settings. Nothing about PDEs is exploited here, nothing I can see it is about PDE-ness, so the approach is not dedicatedly designed for PDEs. So what is particular about this method which is related to PDE-ness of the problem?

3- Baseline active learning for simulation, video, and 3D scenes would be relevant.

4- The datasets are quite simple for this paper.

If the authors tried this approach on a challenging task, then the first 3 points, as well as the next point, could be ignored.

5- The method is quite ad-hoc and heuristic. What if all the models wrongly agree on many inputs and time steps? How can one guarantee this method doesn't collapse or capture the right "variance" and "uncertainty"? Just relying that this method, hopefully, does not collapse, is not sufficient. Again, this point could be ignored if we actually could tackle a challenging problem.

### Questions
minor, in Eq3, we often after expected value not the empirical loss.

### Soundness
3

### Presentation
3

### Contribution
2
