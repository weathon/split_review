# Low-Budget Simulation-Based Inference with Bayesian Neural Networks

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Simulation-based inference methods have been shown to be inaccurate in the data-poor regime, when training simulations are limited or expensive.
Under these circumstances, the inference network is particularly prone to overfitting, and using it without accounting for the computational uncertainty arising from the lack of identifiability of the network weights can lead to unreliable results.
To address this issue, we propose using Bayesian neural networks in low-budget simulation-based inference, thereby explicitly accounting for the computational uncertainty of the posterior approximation.
We design a family of Bayesian neural network priors that are tailored for inference and show that they lead to well-calibrated posteriors on tested benchmarks, even when as few as $O(10)$ simulations are available.
This opens up the possibility of performing reliable simulation-based inference using very expensive simulators, as we demonstrate on a problem from the field of cosmology where single simulations are computationally expensive. We show that Bayesian neural networks produce informative and well-calibrated posterior estimates with only a few hundred simulations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper intodruces a new method for simulation-based inference (SBI) that uses
Bayesian neural networks (BNN) to better account for uncertainty in posterior estimates
due to limited training data. The authors demonstrate that previous attempts of
combining BNN with SBI showed limited success due to the choice of prior on the BNN
weights and they propose an alternative prior more suitable for the SBI setting. To
evaluate the proposed method, the authors show on four benchmarking tasks and on a SBI
use-case from cosmology that the resulting SBI posterior estimates are well-calibrated
even in the low-data regime.

### Strengths
### Originality

The idea of using BNN for SBI is not new (as discussed in the paper). However, showing
why previous approaches did not work so well and the proposal of a new type of BNN prior
more suitable for the SBI setting is a valuable contribution. Most of the previous work
on better uncertainty quantification in SBI is discussed adequately in the introduction.
The only paper with a related approach that seems to be missing in the discussion is [Lueckmann et al.
2017, section
2.2](https://proceedings.neurips.cc/paper/2017/hash/addfa9b7e234254d26e9c7f2af1005cb-Abstract.html),
who propose performing SVI on the neural network weights for continual learning across
SNPE rounds. Also, it seems a bit odd to me that the benchmark used are not cited
(except for the spatial SIR by Hermans et al.). The SLCP benchmark was introduced by
Papamakarios et al. (SNLE paper), two moons by Greenberg et al.; and the overall set of
SBI benchmarking tasks was introduced in Lueckmann et al. 2021.

### Quality

The technical contributions of the paper appear as sound and the selected methods for
applying BNN to SBI are appropriate. The experimental results tend to support the
initial claim of obtaining well-calibrated posteriors in low-data regime. However, the
number of performed experiments is quite low (three) and the results appear quite noisy.

In general, it should be made clearer how strong the trade-off is between posterior
calibration and posterior accuracy. At the moment it seems that the BNN approach tends
to be quite underconfident in some scenarios (e.g., BNN-NRE on all benchmarks). I
therefore suggest that more experiments should be run and results should be reported
with error bars (e.g., 5-10 runs with error bars showing the standard error of the mean
performance). Additionally, I think it would be good to also check the posterior
predictive distribution for the cases where the BNN has low nominal log posterior values
even in high-data regimes.

### Clarity

Overall, the paper is well-written and clearly-structured. I have a couple of remarks
that should be addressed to improve the clarity.

- In section 3, especially in section 3.2, it should be explained more clearly why and
  how the prior has to be tuned to be used for the BNN approach. In the classical SBI
  setting, the prior is usually set a priori using expert knowledge. This step usually
  does not involve using simulated data for an optimization procedure. In the BNN
  approach, it seems that the prior has to be tuned with actual simulations (e.g., lines
  254-261). Do these simulations have to be run in addition to the training data? Are
  they accounted for the in the budgets in the benchmarks?
- Figure 1 needs a couple of clarifications. The caption says it's a visualization of
  the tuned prior. Then, the next sentence says the left panels show posterior functions
  sampled from the *tuned prior prior over the neural network's weights*. How are these
  samples obtained and what are thet supposed to show? Are they obtained before or after
  SBI training? Similarly question for the last panel: is the calibration calculated
  after the full SBI training or only after the prior tuning?

In general, it seems that a better explanation of the steps involved in setting up and
training the BNN-NPE (NRE) approach. I suggest adding more details in the next and
adding an algorithm scheme in the text or appendix.

### Significance

Uncertainty quantification in neural SBI methods on the posterior approximation itself
is an important and timely problem. Especially in low-data regimes, common neural SBI
methods like NPE struggle. The proposed BNN approach with a Gaussian process prior
as proposed here appears as an important contribution for addressing this issue.

### Weaknesses
I outlined several concerns and questions above. To summarize to most important points:

- the experimental results are difficult to interpret because they show the media of
  only three repetitions. More repetitions and error bars would be better here.
- the high underconfidence of the BNN approach in how-data regimes is concerning.
  Additional evaluation of the posterior predictive distributions would be appropriate.
- the choice and construction of the prior from simulated should be explained more
  clearly. A better explanation ideally will resolve the questions on the general
  procedure and on Figure 1 above.

### Questions
1) Do these simulations for prior tuning have to be run in addition to the training data?
2) Are they accounted for the in the budgets in the benchmarks?
3) NPE / NRE ensembles seems to perform similarly well compared to the BNN approach. How
  does it perform on the cosmology example? How does it compare to the BNN approach in
  terms of computational budget? Do you think ensembles could be a good alternative when
  computational budgets are limited? What are the disadvantages of ensembles compared to
  BNN for SBI?
4) More generally, what is the computational complexity of the BNN approach compared to
  NPE (ensembles)?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a novel approach for simulation-based inference for low-budget problems using Bayesian neural networks. They additionally propose to use tailored priors for the neural network weights which generally leads to more conservative posterior estimates. They evaluate their method on several experimental models against multiple baselines demonstrating promising results for SBI when the computational budget is limited.

### Strengths
- The paper proposes a novel contribution for simulation-based inference. The method is in my opinion very relevant to the community and interesting as a low-budget solution for inferential problems.
- The motivation and derivation of the tailored prior is in my opinion particularly well done and convincing.
- Empirically, the method seems to achieve the motivated goal: having calibrated posteriors for low simulation budgets.
- The paper is well written and easy to follow.

### Weaknesses
The evaluations and presentations of the results could in my opinion be improved.

- The authors evaluate their method with the expected coverage (EC). In Figure 2, it is in my opinion very difficult to draw conclusions which methods works best. This is likely due to the fact that only 3 runs have been evaluated. Given the complexity of SBI and the high variance of the inferential results, I think they should do at least 10 evaluations and report these. The lack of statistical power makes it difficult to assess the true performance differences between the proposed method and the baselines. The reported coverage AUC values are sensitive to the specific random seeds used for training, and with only three runs, it's hard to determine if the observed trends are consistent or due to random chance. For example, a method might appear to perform well in one run but poorly in another, and averaging over only three runs might not capture this variability.
- The authors use as a second evaluation metric the expected posterior log density (EPLD). It is not clear what a good value should look like here or even if a high log density should be desired. When the goal is to have a conservative posterior, is a extremely high EPLD a good measure? The authors should, despite possible drawbacks, have used some divergence to the true posterior, such as MMD, in addition to the other two and report this. While EPLD can indicate how well the approximate posterior fits the training data, it doesn't directly measure the calibration or conservativeness of the posterior, which is the main goal of the paper. A high EPLD could simply mean that the model is overfitting the training data and not necessarily that it is producing a well-calibrated posterior. A divergence measure like MMD, on the other hand, would directly compare the approximate posterior to the true posterior, providing a more direct assessment of the quality of the approximation.
- It is not clear how crucial hyperparameters such as the temperature $T$ or the covariance functions of the reference GP are chosen in practice. The paper lacks a detailed discussion on how these hyperparameters affect the performance of the method, and how one should choose them in practice. The temperature $T$ controls the sharpness of the posterior, and the choice of covariance function and its parameters (e.g., lengthscale and variance) for the reference GP can significantly impact the shape and uncertainty of the prior. Without a clear explanation of how these parameters should be selected, it is difficult to reproduce the results or apply the method to new problems.
- The authors propose to use cold posteriors, e.g., using a temperature of $T=0.01$. The motivation of this is not clear, given that the entire idea is to use a prior that enforces calibration. Why would it be desirable to in fact reduce the impact of the prior?

#### Minor
- Figures 2 should show the standard errors.
- Figure 3 should show the reference posterior and not only the true parameter value.

### Questions
- The results in Figure 3 seem to indicate that NPE is indeed outperforming BNN-NPE here. Would the authors argue that BNN-NPE is preferable over NPE for this task?
- What do the numbers in the legend in Figure 3 mean?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors aim to produce well-calibrated posterior in simulation-based inference, in particular in cases where the simulator is very expensive and, therefore, few simulations can be used as training data. To achieve this, the authors propose to use Bayesian neural networks. They develop a novel prior which leads to a-priori well-calibrated posteriors. They apply their method to several toy simulators and to a physics simulator.

### Strengths
The idea to generate neural network weight priors which lead to a-priori well-calibrated posteriors is novel, interesting, and potentially impactful. The methodology which the authors employ to achieve this is novel, elegant, and rigorous. I thoroughly enjoyed reading these parts of the paper. In addition, the authors demonstrate that the method can be applied across methods (NPE & NRE) and they evaluate the method on a series of useful tasks.

### Weaknesses
 (1) The paper overstates its claims.
My main issue with this paper is that it overstates its claims and does not acknowledge the weakness of empirical results. Looking at Figure 2, and in particular for NRE: BNN-NRE _never_ reaches the log posterior of the other methods (even for 1M simulations). Yet the authors state that `the nominal log posterior density is on par with other methods for very high simulation budgets`. Where does this claim come from. Similarly, in Figure 2 (NRE), the authors do not acknowledge that the AUC is not particularly much higher for BNN-NRE as compared to NRE, even for 10 simulations. Indeed, for three of the four tasks NRE has a higher coverage AUC than BNN-NRE for 10 simulations. On top of this, for many tasks and simulation budgets, BNN-NRE does have a negative AUC, but the authors simply claim that they `show positive coverage AUC`. Finally, 

(2) The empirical results are weak.
Second, to me, the empirical results are difficult to interpret. (A) Many of the curves shown in Figure 2 are very noisy and irregular. It might be beneficial to average across more seeds to observe clear trends. (B) As a potential user, I would find it very worrisome that BNN-NRE has _significantly_ lower nominal log-posterior than standard methods. Indeed, for some tasks, it seems to require 5 orders of magnitude (for many other tasks 3 orders of magnitude) more simulations than standard methods.

### Questions
No questions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors wish to provide a method for simulation-based inference for expensive simulators that accounts for the epistemic uncertainty, which tends to be high when available data (simulations) is low. They wish to do so by using a Bayesian neural network in combination with the SBI methods NRE and NPE. They note issue with current priors for Bayesian neural networks in simulation based inference, stating they are not calibrated a priori. They note that using a Gaussian process, with the prior distribution as its mean, can be used to define a prior which is well-calibrated a priori. By optimizing the Bayesian networks prior on the weights to approximate the Gaussian process prior, the Bayesian networks prior becomes approximately well-calibrated. They perform experiments, and show this often leads to better calibrated posteriors in the low-data (low simulation budget) regime.

### Strengths
Being able to perform reliable simulation-based inference with fewer simulations would be broadly useful to the scientific community. The idea to use a prior over the weights of a BNN that is compatible with the simulators prior distribution is sensible, and using a Gaussian process to achieve this is to the best of my knowledge novel and clever. The paper is well structured overall (except for where noted below) and includes some interesting experiments, using a good choice of metrics assessing reliability of the posteriors.

### Weaknesses
Structure/Presentation:
- Lack of method summary: There's no clear summary of the method, e.g. in the contributions section, an algorithm, or the start of section 3. A brief overview of 3-4 sentences would be very beneficial for readers. It's only towards the end of section 3.2, that the overarching method begins to come together on a first read. In my opinion, the abstract also does not include enough information on the method.
- Lack of clear definitions: The concept of an "a priori-calibrated Bayesian model" should be defined more clearly when it is first introduced.  I presume that an example of a well calibrated a priori model, would be one for which the Bayesian model average at initialization is equal to the simulator parameters prior $p(\theta)$ for any $x \in \mathcal{X}$? Presumably this includes a large variety of useful and non-useful models for modelling epistemic uncertainty (as suggested in equation 8).
- Figures: The credibility figure in Figure 1 is confusing, either the standard deviations are not in order, or there is a typo one of the standard deviations. Figure 3 should have a labeled legend. Many of the font sizes are too small.

Experiments:
- Limited experimental runs: Only 3 runs are performed for each experiment, and only the median is reported. This makes it hard to assess if differences between methods are significant. Repeating with more runs would be beneficial, although I am sympathetic to limitations in computational budget.
- The BNN-NRE method appears to perform worse than NRE in terms of mass placed on true parameters, even for low simulation budgets (100-1000 in Figure 2), which is the domain where the method is proposed to be beneficial. Similarly, the results for the NPE case are not particularly convincing in terms of the mass placed on the true parameters. The coverage properties do appear to have improved, but coverage alone is not indicative of a good posterior estimate.
- The results don't align with an intuitive understanding of epistemic uncertainty. For example, in figure 3, in NPE, we can see 4000 simulations produces a reasonable posterior estimate, whereas BNN-NPE is still massively conservative, even with 65536 simulations, suggesting overestimation of epistemic uncertainty. This suggests simple alternative approaches such as training posterior estimates on subsets of the data with standard methods, such as NPE, and mixing the resulting posteriors, would likely be more effective. I understand the temperature parameter is introduced to limit this problem, but this then introduces another hard to choose hyperparameter (along with the Gaussian process parameters introduced).

### Questions
How can we be sure that any benefits are from the BNN modelling epistemic uncertainty, and not the altered initialization? For example, if we "pretrained" NPE/NRE to prior samples (and $x$ simulated from some noise distribution), such that at "initialization" the posterior estimate would be approximately equal to the prior for any $x$, it would be interesting to see if there is still be any benefit to the introduced method.

Most the benefits seem to be in the very small data regime (<100 simulations). I am not convinced that this scenario is of particular interest the scientific community, could you give an example of a practical case where this is useful?

Why is the convergence to the NPE solution so slow in terms of the number of simulations? Can the prior be altered to avoid this problem, rather than introducing a temperature parameter?

### Soundness
2

### Presentation
2

### Contribution
3
