# Addressing Misspecification in Simulation-based Inference through Data-driven Calibration

- Decision: Reject
- Scores: 5, 5, 8, 6

## Abstract
Driven by steady progress in generative modeling, simulation-based inference~(SBI) has enabled inference over stochastic simulators. However, recent work has demonstrated that model misspecification can harm SBI's reliability.
This work introduces robust posterior estimation~(ROPE), a framework that overcomes model misspecification with a small real-world calibration set of ground truth parameter measurements.
We formalize the misspecification gap as the solution of an optimal transport problem between learned representations of real-world and simulated observations. 
Assuming the prior distribution over the parameters of interest is known and well-specified, our method offers a controllable balance between calibrated uncertainty and informative inference under \textit{all possible misspecifications} of the simulator. Our empirical results on four synthetic tasks and two real-world problems demonstrate that ROPE outperforms baselines and consistently returns informative and calibrated credible intervals.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a robust posterior estimation method (RoPE) for simulation-based inference (SBI) when the model is misspecified but the the underlying parameters of interest can be physically measured via (possibly expensive) experiments. RoPE uses such a calibration dataset to better quantify the posterior uncertainty under model misspecification scenarios.

### Strengths
The paper addresses a relevant practical problem in the field of SBI. The paper is largely well-written, and the experimental evaluation seems thorough. The idea of using the optimal transport coupling for learning statistics is neat (approach is similar to the work of Huang et al. (2023) who also learn statistics to be robust to model misspecification, without the calibration set of course).

### Weaknesses
I have concerns regarding the soundness of the proposed method. The main claim is that RoPE provides well-calibrated uncertainty quantification, which I am not convinced of. The self-calibration property discussed in Appendix F is under the assumption that the NPE posterior is well-calibrated, which itself is not guaranteed and is often overconfident as pointed out by [1] (and therefore making NPE well-calibrated is an active area of research in SBI [2]). Moreover, the expectation in equation 10 in the proof is estimated using $N_o$ Monte Carlo samples from the test set, which I am assuming, would be limited (unless having a large test set is one of the assumptions/requirements of RoPE, in which case it should be mentioned clearly since the other methods do not have such a requirement). Basically I do not see why RoPE solves the problem being addressed.

[1] Hermans et al. (2022). A Crisis In Simulation-Based Inference? Beware, Your Posterior Approximations Can Be Unfaithful. TMLR.
[2] Falkiewicz et al. (2023). Calibrating Neural Simulation-Based Inference with Differentiable Coverage Probability. NeurIPS.

Looking at how the authors define the model misspecification problem, it seems like the problem is of posterior calibration. Calling it "model misspecification" only makes it confusing since the definition is in terms of posteriors, and is not necessarily a property of the model (the example in Appendix A focuses on posterior bias rather than calibration). I do not see what is gained by calling this a "model misspecification problem", as a well-specified model may still produce mis-calibrated posteriors (mentioned in lines 92-93). I really think that the story becomes straightforward if the problem being addressed is of obtaining calibrated SBI posteriors (i.e. a "calibration problem"), both in cases when the model is well- or mis-specified (right?), which can be done using some additional information (in the form of calibration dataset), which is available in scenarios such as the cardiovascular system and industrial process. If the authors agree with this statement, then the more appropriate baseline for RoPE is the method of [2], instead of NPE-RS and NNPE.

The equation in line 190 is the same as equation 3 from the Ward et al. (2023) paper (NNPE method). Seems like the primary difference between the two is that RoPE uses OT to learn $p(\mathbf x_s | \mathbf x_o)$, while NNPE uses a spike and slab model. Please elaborate on the key differences between the two approaches, as it would help gauge the originality of this work. Also, it is not clear to me what is the role of the assumption in equation 3 then, as NNPE does not seem to have that assumption but still arrives at the same equation (correct me if I am wrong). I suppose lines 193-194 states why this assumption is needed, but it is not clear to me. Plus, there needs to be more discussion on how limiting is this assumption, in which cases is it satisfied and not satisfied, and the implications for when it does not hold.

The notation is unclear at times. For instance, what is the difference between $\mathbb{P}^\star$ and $p^\star(\mathbf x_o)$? Sometimes the author say $p^\star(\theta)$ is the true distribution of parameters in the real-world, but then they use $p^\star(\theta | \mathbf x_o)$ which is not introduced.

In section 2.2, it would be great if you could explain what an OT coupling is and what is the general idea (in simple words) before going into the OT details. This would help the readers not familiar with OT to get a sense of what this does without needing to understand every detail.

Minor comments:
* In equation 6, I think there should be $\varphi$ in the left-hand side instead of $\phi$, right?
* typo in line 817: "i.d.d." instead of "i.i.d".

### Questions
In section 3.1, the authors say that "it is reasonable to learn a sufficient statistic $\mathbf h_o$ by fine-tuning $\mathbf h_{\omega^\star}$". How do we know that such a fine-tuning will produce sufficient statistics? Are there any guarantees?

In most of the experiments, the performance of RoPE does not var as the calibration set size increases. Is there a reason why the performance of RoPE saturates in those cases even with $N_c = 10$? Are these very simple problems?

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
4

### Summary
This work contributes another contender to the family of “robust” methods for neural SBI, which is known to be unreliable for out-of-distribution (OOD) data. The basic idea is to use a “calibration set” of observables and ground-truth measurements as an additional training signal to inform the neural network responsible for embedding the observables into a lower-dimensional representation about distribution shifts and reduce its susceptibility to OOD observables. During inference, an optimal transport (OT) cost matrix is used to derive weights for approximating the posterior over observables as a weighted average over an ensemble of posteriors obtained from the training simulations.

### Strengths
- The paper contributes an interesting approach to a hard problem in SBI and scientific modeling in general.
- The OT formulation and ensemble-based correction are well motivated and the assumptions are clearly stated.
- The evaluation in the setting of low-dimensional models is comprehensive and features good comparisons. The results are encouraging even with a very small calibration set.

### Weaknesses
 - The basic premise of the work is that “ground truth” parameters or latent quantities are available during training. In other words, it assumes that the simulator is parameterized in the same way as reality. This severely limits the applicability of the proposed method beyond certain domains of physics physics, as “true” latent quantities are not available or not even sought-for in a majority of applications of Bayesian inference outside of physics. Nevertheless, the authors openly acknowledge this limitation and I don’t think that it is an unsurmountable dealbreaker. On a related note, this limitation extends to the formal definition of misspecification assuming there is a “true prior”, and correspondingly, a “true posterior” that represents the updated prior which is hardly actionable - the marginal likelihood $p(x_0)$ is a model-implied quantity and de Finetti’s representation theorem about the existence of a factorization apples only to infinitely exchangeable sequences without any guarantees that $dim(\theta)$ is finite. 
- The authors are quite selective in their choice of cited related work. For instance, the authors can find extensive discussions on model misspecification in likelihood-free inference in [1, 2, 3, 4, see also references therein]; [5] also discuss an alternative definition of model misspecification through the scope of the marginal likelihood, which is also explicitly discussed in [6]. [7] propose to view misspecification as latent-space distortion and correct it during inference using the reverse KL. This goes on to show that the proposed paper can profit from a slightly more in-depth discussion on conceptual and empirical approaches to dealing with model misspecification and perhaps offer a categorization of methods designed to *detect* vs. methods designed to *fix* potential errors. Additionally, reference [8] regarding universal density approximation is misleading; see [9 and references therein] for a comprehensive treatment of the university of coupling-based normalizing flows.
- I have two concerns regarding the scalability of the method. First, it seems that the transport matrix can grow very large for settings with millions of observations and millions of simulations. This, coupled with the need to optimize the optimize the $\gamma$ trade-off parameter makes the method attractive only for small-data, small-simulation-budget settings. Second, the empirical evaluation only considers models with extremely low parameter dimensionality $\theta$ (i.e., the largest parameter space has 4 parameters), which is a serious limitation and leaves the question of generalizability to more complex models completely open. As such, I believe the claims of the paper to be a bit over the top. I do appreciate that the evaluations were performed on fairly large tests sets of 2000 simulations and that recent contenders and good ablations were considered.
- The presentation of the results is rather hard to follow. I believe some of the model details (e.g., example data sets) could have been delegated to the appendix and sushi plots summarized more succinctly. I am a bit concerned by the lack of sensitivity regarding the size of the calibration set (apart from task E).

### Questions
Can the authors explain the insensitivity of performance to the size of the calibration set?
Can the method be extended to incorporate a less-than-perfect calibration set (e.g., as coming from a well-calibrated posterior estimator from another data set)?

### Soundness
3

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
The paper introduces a method for addressing model misspecification in simulation-based
inference (SBI)  settings. Common SBI algorithms usually assume that the simulator (the
model) is well-specified, i.e., that it can simulate data close to the observed data.
However, if this is not the case, the resulting approximated posterior distributions can
be substantially biased. This paper proposes a procedure to mitigate this problem for
scenarios where multiple observed data points are available.

The authors propose to first follow a standard SBI approach of learning a neural-network
based embedding on the simulated data, followed by neural posterior estimation (NPE) on
the embedded data. Their key contributions consists of three additional steps. First,
they fine-tune the neural embedding using the set of observed data points. Second, they
then solve the optimal transport problem between the embedding simulated data and the
embedded observed data. Finally, at inference time, they use the optimal transport
solution between the embeddings to obtain the posterior given the observed data as a
weighted sum of the posteriors given simulated data.

The proposed method is evaluated on six benchmarking tasks for misspecification, two
existing tasks and four new tasks. It is compared to baselines and competing algorithms
and performs well in most settings. Additionally, the authors show results for ablations
and the method's behaviour for different hyperparameter settings.

### Strengths
The paper is well-written and well-structured. The first two sections
give a good introduction to the topic, accurately cite previous work and clearly state
the contributions and the specific SBI setting the method is designed to solve. The
paper uses two existing benchmarks and introduces four new model misspecification
benchmarks, which is a valuable contribution for the community. The performance of the
proposed method is promising and the ablation and hyperparameter sensitivity studies
help understanding the method and tend to make it easier for practitioners to choose
parameter in practice.

### Weaknesses
The new definition of model misspecification in SBI is a bit unclear
(see questions below) and should be clarified. Some of the benchmarking results of the
proposed method are unclear and concerning and need clarification. In general, the
figures in the experiments sections are difficult to read and make the overall results
unclear (see suggestions below).

The definition of misspecification, particularly the notion that a model can be well-specified but not well-calibrated, is confusing. It's not clear how this relates to the standard understanding of calibration, which focuses on the agreement between predicted probabilities and observed frequencies. The provided example in Appendix B, while showing a biased posterior, doesn't explicitly demonstrate a lack of calibration in the traditional sense. The distinction between the proposed definition and existing definitions, such as the one in https://arxiv.org/abs/1904.04551, needs to be more clearly articulated, especially regarding the specific conditions under which the proposed definition considers a simulator misspecified, while the synthetic likelihood approach might not. The use of $\pi$ as both a joint and conditional distribution is also confusing and requires clarification.

The practical aspects of the method also raise concerns. The choice of $\tau$ in RoPE$^*$ is not well-defined, and the explanation of how it should be chosen in practice is lacking. The claim that RoPE significantly reduces uncertainty compared to the prior needs to be substantiated with a more direct measure than LPP, as LPP is a measure of predictive performance, not directly of uncertainty reduction. The connection between ACAUC and standard posterior calibration metrics like SBC or expected coverage is not clearly explained, and the statement that it is zero for a perfectly specified prior is misleading, as it should refer to the calibration of the posterior. The definition of the **SBI** baseline is unclear, and it's not obvious how it can serve as an upper bound for misspecified simulators, especially when it performs worse than the prior in some cases. The surprisingly good performance of the MLP baseline, which assumes a Gaussian posterior, raises questions about the complexity of the benchmark posteriors. The sensitivity of the method to the hyperparameter $\gamma$ and the lack of guidance on how to tune it in real-world applications are also significant weaknesses. Finally, the figures are indeed difficult to read, with barely visible dotted lines and inconsistent markers, making it hard to discern the results. The performance of RoPE on the SIR example is concerning, and the general underconfidence in terms of ACAUC, which does not improve with calibration set size, needs further investigation, including a comparison of posterior predictive distributions.

### Questions
1) Definition of misspecification in SBI: There are several parts in the definition that
I find challenging to follow. In line 090 it says

> our simulator models the relationship between the real observations xo and the
> parameters of interest as they appear in the calibration set

and for that sentence it is followed, that the current definition is insufficient
because a model may be well-specified by not well-calibrated. I cannot follow this line
of argument. Are you defining mispecification based on posterior calibration here? Can
you please clarify? (I have seen the example in Appendix B, but it shown only that the
posterior is biased, not badly calibrated).

2) Related to my first question, I am wondering how your definition differs from the one
   given in https://arxiv.org/abs/1904.04551, who introduced a synthetic likelihood
   approach for misspecified simulators. 

3) In line 201, $\pi$ is introduced as a joint distribution. However, below in equation
   (4) it is then used as conditional distribution. Can you clarify this change please? 

4) In line 257, RoPE$^*$ is defined with $\tau < 1$, but how much smaller than 1 does it
   have to be? Further below, it is set to $\tau=0.9$. How is chosen in practice? 

5) In line 409, it is claimed that RoPE significantly reduces the uncertainty compared
   to the prior. How is this measured? Is LPP your proxy for this? If so, please clarify
   in the text. 

6) How is ACAUC related to the more common posterior calibration metrics like SBC or
   expected coverage? In line 381, it says that it is zero for a perfectly specified
   prior. Shouldn't it refer to the calibration performance of the posterior instead? 

7) The **SBI** defined in line 387 is unclear to me. How is it obtained precisely and
   how can it be the upper bound on the performance in misspecified simulators? How can
   it below the prior baseline in the ACAUC plots for some tasks? 

8) How can the MLP baseline work so well when it assumes a Gaussian posterior? Are the
   benchmarking task posteriors all close to Gaussian? 

9) The choice of $\gamma$ can have a substantial effect on the accuracy of the
   posterior, tending towards the prior for too large values of $\gamma$. This would be
   highly undesirable in practice. How can the practitioner tune $\gamma$ for real-world
   applications, i.e., outside the benchmarking tasks where it seems clear what the upper
   and lower bound of the metric are?

10) General remark on the figures: Figure 1 is great, but figure 2-4 are packed quite
    challenging to read. The dotted lines are barely visible and quite different than
    shown in the legend. Some lines have markers, others do not. Especially in the ACAUC
    plots it is almost impossible to tell apart the different lines. Smaller line width
    would be a start, but a general improvement in the choice of color code and markers
    would be even better. 

11) Some questions on the RoPE performance: Why does it perform so badly compared to NPE
    on the SIR example? You mentioned that the misspecification in SIR is weaker. How
    does RoPE perform on well-specified simulators in general then? Could this be a
    general weakness of the method?
    Also, RoPE seems to be generally underconfident in terms of ACAUC and this does not
    improve with calibration set size. This is concerning as well. I think it would be
    important to check and compare the posterior predictive distributions as well.


**Additional feedback**

- The reference to figures from the main text is a bit off. For example, figure 1
  appears on page 2, but is referenced only on page 5. Figures 3 and 4 are referenced
  before figure 2. 
- A lot of content is moved to the appendix. It would be better to move parts of it back
  to main text, e.g., algorithm 1. Or give more context in the main text. For example,
  to me it became clear only by looking at the algoritm, that at inference time, one
  needs to run additional simulations to match the test set of observed data for
  computing the weighted posterior.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper details with the important issue of making neural posterior estimation methods more robust against model misspecification. The authors suggest to use a small set of labeled real-world data to calibrate the posterior inference in the face of a misspecified simulator. At the moment, I see some important weakness that make me cautios at recommending acceptance at this stage. But I am open and happy to change my mind during the discussion period.

After the discussion period, I have updated my score from 5 to 6.

### Strengths
- The paper investigates an important issue.
- The goals of this paper are clearly explained
- Detailed examples and ablation studies are performed.

### Weaknesses
 - The main weakness I see is the following: How do we gain access to the *labeled* real-world observations? This seems like quite a strong assumption. I would need to understand if and when this assumption is justified before I would consider recommending acceptance.
- As an expert in SBI, I struggle to understand the introduction of optimal transport in Section 2.2. Adding some more details there might help readers which are not already experts in OT to understand what is going on. Specifically, the notation used in the definition of \mathcal{B}_0 after the condition operator is unclear. As a result, the notation in EQ2 only makes sense half-way.
- The applied metrics in the experiments are reasonable but still make it hard to see in which way we actually deviate from the targeted true posterior. The authors could perhaps also show something like bias in posterior mean and SD or some other easy to understand quantities. While I understand that ground truth is not available for the real-world datasets, it should be possible to compute such metrics for the synthetic benchmarks.
- Curse of dimensionality: These scaling issues are mentioned by the authors themselves and seem to be severe in the number of model parameters(?) I would like to see the scaling laws discussed in more detail here if possible. It would also be valuable to see some empirical analysis of how the method scales with the dimensionality of the parameter space.

### Questions
- I also don’t really see in Section 3, where exactly the real-world labels (the parameters underlying the real data) are actually used. Can you explain this?
- In EQ 3, you make a central assumption. Can you explain why you think this assumption is usually justified? Asked differently, when would it not be justified?
- In equation 6: I don’t fully understand the logic of why 6 is a valid approach to learn a summary network of the real data. Can you explain this to me in more detail?
- I don’t quite understand the results in relation to the LPP and ACAUC metrics:
    - So 0 would be optimal for ACAUC, right?
    - And for LPP higher values would be better, right?
    - If so, SBI looks better than ROPE. I know this is probably not how these metrics should be read, so I am merely asking to clarify this point for me.

### Soundness
3

### Presentation
2

### Contribution
3
