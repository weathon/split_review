# Compositional simulation-based inference for time series

- Decision: Accept
- Avg Score: 6.17
- Scores: 6, 5, 8, 6, 6, 6

## Abstract
Amortized simulation-based inference (SBI) methods train neural networks on simulated data to perform Bayesian inference. While this approach avoids the need for tractable likelihoods, it often requires a large number of simulations and has been challenging to scale to time-series data. Scientific simulators frequently emulate real-world dynamics through thousands of single-state transitions over time. We propose an SBI framework that can exploit such Markovian simulators by locally identifying parameters consistent with individual state transitions. We then compose these local results to obtain a posterior over parameters that align with the entire time series observation. We focus on applying this approach to neural posterior score estimation but also show how it can be applied, e.g., to neural likelihood (ratio) estimation. We demonstrate that our approach is more simulation-efficient than directly estimating the global posterior on several synthetic benchmark tasks and simulators used in ecology and epidemiology. Finally, we validate scalability and simulation efficiency of our approach by applying it to a high-dimensional Kolmogorov flow simulator with around one million dimensions in the data domain.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a simulation-based inference (SBI) method for state-space models where the transition dynamics is Markovian. The core idea is to simulate many single-state transitions and then aggregate them instead of simulating entire trajectories of time-series, so as to reduce the total number of simulator calls.

### Strengths
The paper addresses the relevant problem of computational complexity in SBI which arises when the simulator is costly to sample from. 

The experimental evaluation seems thorough, and the results are significant for FNSE.

### Weaknesses
My main concern is related to the novelty of the paper. The main technical contribution lies in deriving the factorized NSE method, which as the authors mention, is an extension of the setting of the Geffner et al. (2023) paper to the Markov setting. An in-depth analysis/discussion around selecting the proposal $\tilde{p}(\mathbf x^t)$ and providing recommendations on its choice would have strengthened the paper significantly and added to the technical contribution. The paragraph discussing the proposal is kind of confusing. The authors say that "there is lots of flexibility in the choice of the proposal...", but also that "...designing a good proposal can be challenging". I appreciate the experiments evaluating the sensitivity of the results to the choice of proposal, but it is not clear how the proposals are chosen in the first place.

The clarity of writing can be improved by providing examples, especially when it comes to motivating the setting, the core idea, and the assumptions. For instance, the authors say "...given sufficiently many single-step transitions, it should be possible to infer the global target...". A discussion around the cases in which this does (and does not) hold would help the reader understand the scope of this work. Another example is the requirement that "...the proposed state must be independent of the parameters involved in the current state transition...", where it is not clear how restrictive this requirement is, what kind of cases does it cover, etc. Similarly, some examples of expensive real-world scientific simulators in para 3 of the intro would be nice to have.

On the topic of clarity, I found Section 3.2.2 difficult to follow. In particular, it is not clear when the authors are talking about background of previous work (Geffner 2023 and Linhart 2024), and which part is their contribution. Perhaps some of the discussion regarding the implementation details can be moved elsewhere, as they are not easy to follow without reading those two works anyway.  

The paper is presented as a sample-efficient method for Markovian time-series simulators. However, the experiments measure the performance as a function of the number of transitions. To conclude that the proposed method is "simulation-efficient", I would have expected performance to be plotted as a function the number of calls to the simulator (or computational cost) for a fixed number of transitions.  

Would be nice to have a small discussion on other sample-efficient SBI methods in the related works (e.g. based on sequential sampling, Bayesian optimization, etc.).

Minor comment: Typo in line 125-126 (the word "approaches")

### Questions
* Is there a reason why comparison with NSE is not done? 
* Can FNSE be also made sequential in a similar manner as other simulation-efficient SBI methods such as SNPE/SNLE/SNRE? 
* Which score composition method is used in the experiments when implementing FNSE? (I might have missed if this is mentioned in the appendix)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper applies compositional score-matching, previously introduced for SBI on exchangeable models, to non-exchangeable, Markovian models. The appealing aspect of the methodology is that a score estimator can provide good posterior estimates without simulating the full process for each batch instance, but instead simulating single transitions per batch instance and learning to aggregate across time. The hope is that one can achieve the same posterior accuracy with less than $N * T$ evaluations, where $N$ is the simulation budget and $T$ is the maximum time horizon of the simulator.

### Strengths
- The paper is self-contained, easy to follow, and it attempts to address a challenging problem that is relevant to the field as a whole. 
- The method is applicable to different classes of SBI methods (e.g., likelihood approximation, likelihood ratio approximation, direct posterior estimation).
- The idea is original and can stimulate further research into efficient SBI on dynamic models, especially when simulation budgets are scarce.

### Weaknesses
 - As far as I understand it, the proposed method is a straightforward extension of FNPE with an additional input to the score estimator (Eq.6 in [1]). As such, the claim that a new “general SBI framework” is proposed requires some calibration. In contrast, the authors could highlight and extend the empirical aspects of the work.

- While the basic idea is rather appealing, I find it a bit unconvincing that FNPE can robustly approximate the correct global posteriors with sparse training (the same goes for FNLE). There is an aspect of the methodology that strikes me as magical: suppose that most information about $\theta$ in a time-varying signal is contained in later time segments (e.g., as in certain non-stationary signals) or subject to latent transitions (e.g., as in HMMs). It would be incredibly hard to get to that information if the simulation is not evolved for longer $T$, but the factorized approach is supposed to somehow get enough training signal from very sparse simulations in all relevant time windows. How is it possible for the score network to properly learn the correct composition without any assumptions on signal stationarity or smoothness? I assume the reasonable performance on the toy examples can be attributed to the rather short signal lengths and the use of simple, low-dimensional models (Fig.9 reveals striking miscalibration for longer time series on the only challenging model, confirming my fears).

- Overall, the evaluation lacks robustness and I am concerned that it is subject to randomness given the extremely limited number of test simulations used (10!). Since the work is explicitly situated in an amortized inference context and pitched as such, the evaluation could have been much more comprehensive, featuring hundreds or even thousands of test simulations and at least some practically relevant metrics with an absolute interpretation, such as calibration error or other measures used for evaluating computational faithfulness in Bayesian analysis [2]. In addition, there are no ablation studies (e.g., one such study could vary the simulation budget or use an adaptive solver for better-than-uniform sampling, another study can consider extremely long time horizons $T$), all models only have a few parameters (SIR and LV are toy models from the 60s, but presented as distinct from the toy model section), and it is hard to tell if the performance on the only non-trivial model (4.4) is acceptable given the lack of ground-truth and the poor calibration for not not even that long time horizons ($T=100$).

- It may be helpful to clarify some points in Section 2.2 regarding related work on amortized inference. It might strengthen the section to highlight that amortized Bayesian inference is explicitly introduced in [3] and extensively discussed and expanded upon in inference compilation methods [4, 5, along with additional references therein]. Including this line of research could offer a more comprehensive overview of the field. Additionally, [6, 7] don't seem to introduce, discuss, or validate amortized methods; instead, they focus on sequential likelihood-free techniques, such as SNPE [7], without suggesting or claiming to use amortization. In fact, [6] cursorily note that learning over the prior predictive is possible but ultimately dismiss it as “grossly inefficient” (p.3).

*Minor*
Some attention to typos and neologisms is needed (e.g., P2L107 -> one can sample, …, to its probability density?, P7L377, etc.).

### Questions
Why does sW seem to, counterintuitively, increase for increasing number of transitions (Figure 2)?
Will the method be robust to missing or corrupted data?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a class of methods to perform neural simulation-based inference on time-series data when the forward model has Markovian structure, i.e. when the next step only depends on the current one. This is the case in many physical systems defined by PDEs, for example. The method exploits this structure of the simulator / forward model to learn locally (in timestep) amortized estimators for global parameters of interest that describe the system in question. The paper exploits many recent advances in amortized simulation-based inference and adapts them to the Markovian time-series setting.

### Strengths
- The paper is exceptionally well-written. Secs. 2 and 3 set up the problem well, and describe the contributions in the context of existing literature. I feel like I learned a lot about the surrounding field beyond the specific contributions of the paper by reading these sections. Limitations are discussed upfront, and some extension settings explored in an initial way.
- The experiments in the paper are well-motivated. The paper looks at toy models, standard benchmarks, as well as more challenging simulators that highlight some of the specific advantages of the method (e.g., generalization beyond the number of steps used during training).
- The paper explores a timely question of broad scientific as well practical real-world interest. The generalization capabilities of the method beyond the number of timesteps trained for seem especially practical (and maybe should be highlighted more) -- many applications are bottlenecked by the inability to practically train on the longer-horizon timescales needed during deployment.

### Weaknesses
While the core methods are described nicely, some practical aspects receive less thorough treatment. Specifically, the proposal distribution seems like a critical design choice (especially for complex problems like Kolmogorov flow), and the score composition rules prove surprisingly robust even when their assumptions are violated (e.g. GAUSS in non-Gaussian setting). There is limited discussion of why, and limited principled guidance on these implementation choices that practitioners might need to apply the method to new domains. A more thorough discussion here could significantly strengthen the paper in particular for practitioners across domains. The paper lacks a detailed analysis of how the choice of proposal distribution impacts the performance, especially in high-dimensional and complex systems like the Kolmogorov flow. The robustness of the score composition rules, particularly the Gaussian approximation, is not sufficiently justified theoretically, and the paper does not explore the limitations of this approximation when the underlying distributions deviate significantly from Gaussianity. Furthermore, the paper does not provide clear guidelines on how to select appropriate proposal distributions and score composition rules for different types of simulators, which is crucial for the practical application of the method.

### Questions
- How sensitive is the more complex Kolmogorov flow example to the choice of proposal distribution?
- Beyond the empirical results demonstrated, do the authors have a deeper understanding of the robustness of score composition rules?
- The generalization beyond the number of timesteps seen is one of the most useful properties of the method -- how do the generalization capabilities depend on the number of timesteps used during training (e.g., max 10 vs 100 timesteps during training, then 1000 during evaluations)?

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
The authors introduce a novel approach for simulation-based inference (SBI) for time series models of which the joint probability density is Markovian. The work builds on the recently introduced framework of score-based generative models for SBI which aims to approximate the score of the posterior distribution when multiple data points (in this case time points) are conditioned on. They show that their approach is beneficial over a state-of-the-art method in time series benchmarks.

### Strengths
- The paper proposes an intuitive approach for SBI for (very) high-dimensional time series.
- The topic (SBI for high-dimensional time series data) is very timely and relevant given the (seemingly) increased interested of applied researchers.
- The paper is well written and easy to follow.

### Weaknesses
 - Despite the intuitive idea, the proposed method is very incremental. As far as I can see, instead of modelling the score $s(\theta_a|x^t)$ the paper proposes to model $s(\theta_a|x^t, x^{t-1})$, i.e., adding one variable to the score network input, in order to make the method amendable for time series?
- The evaluations are in my opinion not fully convincing.
    - The authors chose to compare their approach to exactly one other baseline which I find a bit insufficient given the wealth of SBI methods and the fact that the authors propose approaches for local FNLE, FNRE and FNSE.
    -  The baseline NPE uses an RNN as an embedding network. Given the authors assume Markovianity, they could have, e.g., just computed summary statistics and used this as conditioning variables, instead of running a costly RNN (which also needs to be trained in addition to the flow layers). Alternatively approaches that reduce the dimensionality more efficiently like neural sufficient statistics could have been benchmarked for a more thorough evaluation [1,3].
  - Relatedly, there is work on high-dimensional SBI that the authors could potentially have included in their evaluations: [1-4]

### Questions
- Is there any reason why NPE performs so badly in the C2ST statistic in Figs 3c and 3d? Previously literature, e.g., [1-2], seems to report different results.
- Could you kindly explain the exact experimental setup in Fig2a and Fig2c? Does, e.g., $100$ transitions mean that NPE received $100$ data samples of length $100$ while for $10$ transitions it received $1000$ samples?

#### References
- [1] Flow Matching for Scalable Simulation-Based Inference, Figure 4, https://arxiv.org/pdf/2305.17161
- [2] Benchmarking Simulation-Based Inference, Figure 2, https://arxiv.org/abs/2101.04653

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a set of Simulation-Based Inference (SBI) methods to perform approxiamte Bayesian (parameter) inference given an
observation that takes the from of a specific class of timeseries (finite-length homogenous Markov chains).
These methods are adaptations of existing score, likelihood, and ratio-based estimation methods, whose original formulation
assume i.i.d observations, and not observations arising from a Markov Chain.

The methods do so by estimating ratio/likelihood/scores "locally", e.g. to the individual factors of the Markov chain.
They then produce a "global" posterior estimate (e.g. an estimate of the posterior of the parameters given the entire Markov chain sample)
by relying on the factorization structure of the Markov chain probability. The composition is straightforward in the case of ratio and likelihood methods,
while when using scores, additional approximations are necessary due to the non-Markovian structure of the blurred posteriors estimated in the previous step.

These approximations are direct adaptations of the one already used in prior work:
- one performs iterative Langevin-based sampling of an annealing path of distributions bridging from a standard Gaussian distribution to the true posterior, and whose intermediate distributions are precisely the SDE solutions whose scores were estimated.
- one produces an approximation of the scores of the SDE initialized at the posterior of the parameter given the entire Markov trajectory, which can then be used to simulate trajectories from the time-reversed SDE, whose final iterate is marginally distributed according to the true posterior.

The performance of the method is investigated on a set of experiments, which include standard benchmark models and a Kolmogorov flow model with high dimensional observations. The simulators are adapted (using noise injection) to fit the formalism of stochastic inference methods.

### Strengths
The paper proposes a conceptually simple, attractive adaptation of SBI methods to Markov chains. For a total simulation budget, the shift towards learning the transition factor allows to increase the number of available observations. Moreover, learning the transition probabilities may be a simpler problem than learning the parameter-to-whole-timeseries relationship, as the observation is lower dimensional in the former case.

### Weaknesses
 **Regarding Presentation**

The presentation of the method needs some improvements. 

First, regarding the the sampling part, the presentation of FNPE and Gauss do not define precisely key details of the approximations.
- In FNPE, where is $q_a$ used for instance?
- In GAUSS/JAC, What is $\Sigma_{a,t, t+1}$?

I had to look at each of the separate papers that introduced such approximations in the iid case to understand what was going on.
The paper should be updated to define all terms properly -- most of will constitute background. Even though the adaptations made by the method are almost independent from the these terms, the paper should remain self contained as far as the core method is concerned. To save space, the FNPE approximation method could be placed in the appendix, as it is not used in the experiments.

Second, the local score estimation section could also be made clearer: for instance, this section
starts by breaking down the true (unblurred) posterior (Equation (3)), highlighting how knowing the score of each
factor is enough to get the score of the resulting posterior. However, what is actually needed for sampling is the blurred posterior,
which cannot be factorized as Equation (3). Equation (3) thus ends up not being very relevant to the method.


**Regarding experiments**: the presentation of the Kolmogorov flow experiments is missing details: for instance, it does not include any mention of stochasticity, which is confusing given that the method is about estimating probability distributions.


**Regarding performance**
- The main weakness of the method right now is that the number of timesteps investigated in the paper remains smaller (up to 100)
compared to the regime of some application of interest, like neuroscience.
- In the Kolmogorov flow experiments, the MAE of the posterior predictive significantly increases for when using 100 instead of 10. It would be nice if the authors commented on this point in the paper.

### Questions
Is there a particular motivation behind using Sliced Wasserstein Distance for evaluation? If using it as the main criterion, it would be nice to provide an intuition as of what features of differences in distribution this distance is capturing. Otherwise, I'd suggest using the Sinkhorn Divergence instead -- with a small regularization parameter, it is essentially a direct approximation of the Wasserstein distance.

**Minor**

- The use of "time-variant" and "time invariant" should be replaced by the more standard "(time) homogenous/unhomogenous".
- "MCMC-based sampling corrections, such as unadjusted Langevin dynamics". The ULA doesn't include a correction step (it is "undajusted"). What do the authors mean by that?
- To produce symmetric quotation marks, consider using ``text'' instead of "text" in latex.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors consider performing simulation-based inference for Markovian simulators. They propose two primary methods, based on score matching, and likelihood (ratio) estimation. In both cases, they utilize the Markovian structure to increase the efficiency of inference, by performing inference using data from single-state transitions, rather than requiring whole sequence simulation. In the likelihood case, the global likelihood is the product of the transition functions $p(x^{t+1}|x^t, \theta)$ (eq. 1), which once estimated can be used with MCMC to infer the posterior. Similarly, for estimating the score, they again use the Markovian structure to factorize the score (eq. 3), and use a "local" score estimator to approximate the global score. In both cases, a proposal distribution is used, $\tilde{p}(x^t)$, from which a sample is drawn, and a single transition is performed, which is used for learning.

### Strengths
The method is to the best of my knowledge novel and provides a solution to utilizing the known dependency structure of Markovian simulators; knowledge which is often neglected in simulation-based inference.  The application area is an important area and handling sequence data in simulation based inference is known to be often challenging (in terms of performance and computational cost). The experiments are convincing and consider a set of familiar but interesting models.

### Weaknesses
My main criticism is that the paper should include a clearer description of what might constitute a "good" proposal distribution $\tilde{p}(x^t)$, especially when it is first introduced. I further feel that the requirement for choosing this proposal is a major problem for the practical utility of the introduced methods, and the authors should better address this problem. E.g. should we aim for it to resemble a prior predictive simulation for a randomly chosen $t$? Could the proposal $\tilde{p}(x^t)$ be sequentially improved as the posterior is learned? The use of hand-picked simple distributions is somewhat concerning for broader applicability.

Some smaller issues:
- The names of the contributed methods, at least FNSE, should be introduced earlier, for example, in the final paragraph of the introduction (FNSE is in Figure 1, but it's easy to miss the name).
- "except FNRE; in LV": I don't believe LV abreviation was introduced, presumably Lotka-Volterra.
- Text size in figures is often a little too small.
- There is a reasonable degree of entangling of previous work in section 3.2.2, which made it hard to read. For example, the abbreviation FNPE is introduced without definition, initially implied to refer to the method by Geffner. It is then introduced and thereafter used as an adaptation of the Geffner method. It also refers to a score-based method, so the use of NPE is confusing as it implies a neural posterior estimation method, using e.g. flows.

### Questions
Is $x^t$ in the SIR example the three states $\{S^t, I^t, R^t\}$? Correct me if I am misunderstanding, but if this is the case, the proposal is  $\tilde{p}(x^t) = \text{Unif}(0, 5)$, presumably independent for for each state S, I and R. At any given time $t$, I would expect the states to be correlated (e.g. more recovered likely implies less infected and susceptible individuals). The use of an independent uniform does not capture this. Further, I presume the method is only valid  if we observe all three states?

As mentioned above: Should we aim for $\tilde{p}(x^t)$ to resemble a prior predictive simulation for a randomly chosen $t$? Could the proposal $\tilde{p}(x^t)$ be sequentially improved as the posterior is learned?

### Soundness
3

### Presentation
3

### Contribution
2
