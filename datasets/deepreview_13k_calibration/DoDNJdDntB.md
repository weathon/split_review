# Flow Matching for Posterior Inference with Simulator Feedback

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 3, 3, 6, 6

## Abstract
Flow-based generative modeling is a powerful tool for solving inverse problems in physical sciences that can be used for sampling and likelihood evaluation with much lower inference times than traditional methods. 
We propose to refine flows with additional control signals based on a simulator. Control signals can include gradients and a problem-specific cost function if the simulator is differentiable, or they can be fully learned from the simulator output.
In our proposed method, we pretrain the flow network and include feedback from the simulator exclusively for finetuning, therefore requiring only a small amount of additional parameters and compute. We motivate our design choices on several benchmark problems for simulation-based inference and evaluate flow matching with simulator feedback against classical MCMC methods for modeling strong gravitational lens systems, a challenging inverse problem in astronomy. We demonstrate that including feedback from the simulator improves the accuracy by $53\%$, making it competitive with traditional techniques while being up to 67x faster for inference.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the problem of modelling the posterior $p(\theta\mid x)$ in a generative model $\theta\to x$, where $p(x\mid\theta)$ is available as a simulator, but possibly without access to exact likelihoods. When the sampling of $\theta$ given $x$ is modelled as a conditional (on $x$) neural ODE and this ODE is trained by flow matching objectives, it is proposed to place an inductive bias on the drift model: the output of simulator or its gradient, evaluated at an intermediate time point or its extrapolation to the target space, is encoded and given as an input to the drift model. Such a form of the drift model is hypothesised to improve the approximation of the target distribution by effectively guiding the drift to the modes of the posterior. Experiments are done on several low-dimensional simulation-based inference tasks, including the lens and source parameter estimation problem in strong gravitational lensing.

### Strengths
- The problem studied is highly relevant as foundation models (including diffusion and flow-based models) become available in various scientific domains. It is important to develop  inference methods for inverse problems that have low bias, good posterior coverage, and high efficiency of training and inferences -- this paper attempts to solve these problems.
- The proposed algorithm plausibly attacks these challenges (even if it is not very well demonstrated by the experiments, see below) and should give an asymptotically correct solution to the posterior sampling problem.
- Interesting analysis of algorithm variants in Section 5.2.

### Weaknesses
Throughout the text, there are many inaccurate or somewhat sloppy statements and references that confuse a specialist in flow matching models (and would likely impede understanding by non-specialists as well). A list follows.

- Abstract: I would suggest to revise it to explain the problem setting and approach at a higher level.
  - First sentences: "Flow-based generative modeling is a powerful tool for solving inverse problems in physical sciences" -- this is a bold claim. The use of flow-based models for inverse problems is not yet well-established; in fact, this is what this paper aims to do.
  - The next few sentences do not set up the problem well (it is not even explained that we are talking about continuous normalising flows).
  - The results at the end do not make sense without context: what does "improves the accuracy by 53%" mean?
- Introduction:
  - L046: "normalising flows transform a noise distribution to the posterior distribution" is true, but:
    - It is a statement with low specificity (VAEs and GANs also transform noise to data).
    - These models are first introduced in the setting of training from samples, which is not what we usually have in Bayesian inference (no ground truth samples from the posterior).
    - Two of the three citations about diffusion models are actually about ODEs / flow matching. The two are of course connected, but I think it is unfair to call flow-based models an instance of "success of diffusion models [...] specifying a corruption process". For instance, flow ODEs can be learned that are not the probability flow ODEs of diffusion processes, including Liu et al.'s rectified flow (the first iteration is indeed a diffusion ODE, the later 'straightened' ones are not) and Tong et al.'s minibatch OT-based flow matching.
      - One solution could be to explicitly state the connection between FM and diffusion in the cases where it exists (e.g., for Ornstein-Uhlenbeck noise, optimal drifts of ODE and SDE are both expressed in terms of the score, so learning one is tantamount to learning the other).
  - In the paragraph starting L052, somehow we have jumped from a general distribution-matching setting (which is not how flow-based models were introduced -- they are trained from samples!) to a conditional posterior modelling setting. Please state the setting/assumptions (e.g., that we have conditional posterior samples from a simulator).
- Related work:
  - "Inverse problems with diffusion models": This seems to be better named "solving inverse problems under a diffusion model prior". Although the works that do this with Monte Carlo (e.g., Cardoso et al, Dou et al,) are mentioned (you could also consider [Song et al.](https://proceedings.mlr.press/v202/song23k.html)), there is also stochastic optimisation (e.g., [Mardani et al.](https://arxiv.org/abs/2305.04391), [Graikos et al.](https://arxiv.org/abs/2206.09012)), or amortisation by RL methods (e.g., [Black et al.](https://arxiv.org/abs/2305.13301), [Fan et al.](https://arxiv.org/abs/2305.16381), [Venkatraman et al.](https://arxiv.org/abs/2405.20971)).
  - "Flow matching": It is strange to see "optimal transport paths (Lipman et al.)" contrasted with "independent couplings or rectified flows (Liu et al., Tong et al.)". In fact, it is Rectified Flow and OT-CFM (Liu et al., Tong et al.) who consider **non-independent couplings** through rectification steps or OT couplings (thus actually approximating the dynamic OT), respectively, while Lipman et al.'s flow matching is equivalent to one using independent couplings and is OT only on the level of the conditional probability paths used for training.
- FM theory:
  - Equation (1): $\theta$ in subscript should be $\phi$.
  - L156: Because smoothness conditions are stated, they should be precise: Do you assume Bochner integrability? Continuous differentiability (how many times?) in both $\theta$ and $t$? It should also be stated that $p_t(x)=p(t,x)$ and $p$ is a function $[0,1]\times\mathbb{R}^d\to\mathbb{R}$.
  - L182 is hard to understand: what is meant by "$q(z)=p_1(\theta)$? It should be said that the conditioning variable $z$ is identified with the endpoint $\theta_1$, etc.
- Controls for improved accuracy:
  - LL201-203 do not make sense to me. The paragraph begins with conditioning of ODEs -- how is an old trick in diffusion "for example" w.r.t. such conditioning?
  - NB. Equation (7) will be the *exact* $t=1$ endpoint of integration ($\theta_1=\hat{\theta}_1$) if we have a perfectly fit OT or any model with straight integral curves (such as the converged ODE after many iterations of rectified flow)!
  - LL225-227 and later at LL352-355: Once again, I am surprised by the repeated discussion of Liu et al. and Tong et al. yet the *omission of the actual algorithms they propose* (rectification and MBOT coupling), which both produce **straighter** paths than a vanilla FM (and hence inference in fewer steps).

Experiment results are not convincing:
- Results are not consistently showing improvement (cf. Table 1) and error bars are not reported, making it impossible to assess significance.
- In Section 5, can you comment on computational efficiency in terms of wall time?
- Lensing:
  - The evaluations do not seem to guarantee coverage ($\chi^2$ is obviously not sufficient for this, and the SBC tests use projection only on a single parameter). Have you considered coverage tests such as those used in Legin et al., Section 3? Currently it is not demonstrated that the proposed method achieves more accurate posterior sampling.

### Questions
Please see above.

Simpler than the encoder architecture, did you consider physics-inspired ways of providing the simulator information to the drift model? For example, simply expressing the drift as (learned vector field NN) + (learned scalar or diagonal NN) x (simulator gradient), as often done in work on diffusion models for sampling of Boltzmann distributions.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces flow matching with simulator feedback for simulation-based inference which extends offline flow matching for neural posterior estimation with an online phase that uses online simulations to improve the accuracy of the estimated posterior distribution. Indeed, the authors observe that learning perfectly the score function corresponding to the true posterior distribution is challenging and propose to access the simulator online and correct these imperfections at evaluation time. The method is supposedly much more efficient than alternative online method such as MCMC while having the potential to provide as accurate results. The paper introduces two types of control signals, a gradient-based and a learning-based control signal, which are made for differentiable (and deterministic) and non-differentiable (and potentially stochastic) simulators respectively. The method is empirically tested on 4 common SBI benchmarking tasks and a "strong gravitational lensing" problem. Results highlight that simulator feedback help improving the accuracy of the posterior distributions.

### Strengths
- *Novelty*: To the best of my knowledge, the idea of including simulator feedback in flow matching for posterior estimation is novel
- *Soundness*: The idea of using simulator feedback to correct for the imprecision of score matching may indeed be helpful in certain applications. 
- *Presentation*: I found the tables and figure easy to read and informative, while being also visually appealing.

### Weaknesses
While I must acknowledge certain positive aspects of the paper, I have also several concerns that motivate my negative recommendation, which I am listing below.
1. While I find the figures and tables quite enlightening, I find the presentation being a weakness. There are multiple hand-wavy explanations and claims that I find a bit confusing. See below for concrete examples.
2. Empirical validation: I was surprised by the numbers from figure 3 and 4 which seems worse than existing alternatives. In particular, the paper only compares to offline methods while it is clear from [1] that SNLE or SNPE which are sequential alternatives to NPE/NLE and perform much better than the proposed method. It is also arguable whether these benchmarks are the most relevant ones as there are quite low dimensional in term of observation dimensionality and are not fully representative of applications where SBI can shine. For instance, gravitational waveforms and spiking neurons are interesting benchmark used in many SBI papers. I also find the results of Flow matching + posterior quite bad compared to MCMC methods in figure 14 and 15 where we can clearly see an issue with bias and also variance of the predicted posteriors.
Overall, the empirical validation seems insufficient to me and do not clearly demonstrate that the method proposed is of any real use.
3. Relevance: Sequential SBI methods, which call the simulator online, are often complicated to motivate as they require to access the simulator while also arguing doing inference on this simulator without SBI is hard because evaluating the simulator is computationally demanding. While I agree this is not the case for all applications, I would expect the paper to clearly highlight and benchmark the method on use cases where simulating more samples offline to get a good amortised posterior is not enough and calling the simulator online does not take too much time.  

I am not confident these concerns can be addressed in the scope of the discussion (especially regarding results and presentation) but I am open to discussing with authors.

Hand-wavy explanations examples:
- l33-36: Seems an intricated way of explaining likelihood and posterior distributions which are very standard mathematical objects most reader should already know about.
- l37-43: The presentation of SBI is again a bit weird in my opinion. It does not clearly say when and why SBI may be necessary and what it solves. It may be interpreted as if SBI was only about Bayesian inference for the uninformed reader where frequentist methods exist as well.
- l48: what do you mean by "it became clear ... be specified a priori"?
- l49-50: this a vague and pretty strong statement that I would expect to be clarified and supported by reference.
- l52-54: I do not understand what you mean by saying there is "no feedback loop".
- l74-78: you mix the high level description of the method with specific implementation decisions which makes it hard to understand on what aspects the reader should focus on.
- Section 3 was presented in a way that I did not find easy to digest.
- l205: "a fundamental problem..." why is it a fundamental problem is unclear to me.
- l254-255: What shall we conclude from that sentence?
- l277-282: It seems like a hacky solution
 - l283: While I understand you are trying to emphasise that the algorithm still learn the "true" posterior distribution, this is stated in a hand-wavy way in my opinion. 
- l345-351: This is quite confusing again. Why is there a dropout layer? It is quite complicated to grasp the details of all variants.
- 5.4: This is again a very hand-wavy claim without actually being theoretical or empirical support.

### Questions
I would be happy if authors could provide arguments against my concerns.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper considers the problem of solving inverse problems mostly in physical sciences. In particular, we are interested in posterior inference. This paper propose to use the flow matching perspective refined with additional control signals coming from a simulator. Moreover, the authors consider various scenarios depending on the differentiability of the simulator. Finally, they show the empirical results on a few simulator-based inference problems and the gravitational lensing inverse problem.

### Strengths
The paper has some strengths overall, which I will outline below. 


**Strengths:**
1. Introduction of the flow matching perspective for these set of problems making a faster inference procedure.
2. Providing the solutions on using either differentiable or non-differentiable simulators.

### Weaknesses
Despite its strengths, the paper has a few major and minor weaknesses.

**Major weaknesses:**

1. I’m really concerned about the presentation of the results and the abilities of this method, because of the lack of enough comparisons and metrics. The paper needs to demonstrate more comprehensively the advantages of the proposed method over existing techniques. The current comparisons are insufficient to make a strong claim about the method's superiority. Specifically, the evaluation should include a broader range of metrics that are standard in the field of simulation-based inference, such as calibration metrics and metrics that assess the quality of the posterior samples beyond simple reconstruction accuracy.
2. Regarding the gravitational lensing problem (presented as the main real-world task being tackled), they are operating in a relatively small space, making the problem easy and solvable. However, they didn’t include any coverage test (e.g., TARP [1], or any other), so it’s hard to say if the posteriors are good. Moreover, as far as I understand, the evaluation test is only on their own simulations, the one that the model were being trained on. In particular, we don’t know if the model is robust to any OOD examples. Finally, the presented residuals (e.g., in Fig. 6) are looking bad. The limited parameter space and the lack of out-of-distribution testing severely limit the conclusions that can be drawn from the gravitational lensing experiments. The residuals presented in Figure 6 are indeed concerning, suggesting that the model might not be capturing the underlying physics accurately, and this needs to be addressed with more detailed analysis and potentially a more robust model architecture.
3. Regarding the part: „(…) however, previous methods are usually restricted to point estimates, use simple variational distributions or Bayesian Neural Networks (Schuldt et al., 2021; Legin et al., 2021; 2023; Poh et al., 2022) that are not well suited to represent more complicated high-dimensional data distributions.” - Legin et al. 2021; 2023 use a likelihood-free inference (or simulation-based inference) framework to get posteriors from simple feed-forward nn (not Bayesian). The statement about previous methods being restricted to point estimates or simple variational distributions is not accurate, particularly concerning the work of Legin et al. [2], which uses a likelihood-free inference framework to obtain posteriors using feed-forward neural networks. This mischaracterization of existing methods needs to be corrected to accurately position the contribution of this work.
4. The authors proposed the intensive tests only on LV, which is relatively simple problem and for sure not enough for fair comparison. Moreover, the results in Tab. 1 don’t show any superiority of the proposed method - in particular, NSF is getting similar or better results. The exclusive focus on the LV problem, which is relatively simple, is insufficient to demonstrate the method's effectiveness in more complex scenarios. The fact that NSF achieves comparable or better results in Table 1 further raises concerns about the practical advantages of the proposed approach. The paper needs to include more challenging benchmark problems to validate the method's capabilities.


**Minor weaknesses:**

1. The authors should include comparisons with other novel posterior sampling baseline methods than DPS, e.g., LGD−MC [2]. The comparison with DPS is not enough, and the authors should consider more recent and relevant baselines in posterior sampling.
2. In line 319, should be „spline”

### Questions
I would like to see especially the experiments and responses to the issues mentioned as weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a method to improve flow-based generative models for simulation-based inference by incorporating simulator feedback through control signals. The key idea is to refine a pretrained flow network with additional control signals based on simulator outputs, which can include gradients and problem-specific cost functions for differentiable simulators or learned signals from non-differentiable simulators. The authors demonstrate their method on several benchmark problems and show substantial improvements in accuracy (53%) while maintaining fast inference times (up to 67x faster than MCMC) on a challenging strong gravitational lensing application.

### Strengths
* The paper tackles an interesting problem of incorporating simulator feedback into generative models trained with flow matching. With the recent interest in the flow matching for learning generative models, the problem of incorporating downstream rewards, e.g. simulator feedback, is a critical one. This paper presents one of the first efforts in that direction (based on my knowledge). 
* The application to the lensing problem is quite interesting. Generative models are well suited to such scientific inverse problems, and this method could be a useful addition to the toolbox for such problems. 
* The method supports feedback from black-box simulators as well as differentiable simulators where gradient feedback is available. 
* The method also provides considerable speed-ups in the simulation over other approaches. 
* The paper is also quite clearly written and easy to follow.

### Weaknesses
 * The empirical evaluation seems quite a bit limited. Specifically, the paper only considers a single applicaiton on strong gravitational lensing. The other synthetic tasks are quite small and it is unclear how general the method is. Moreover, the results on the gravitational lensing experiment, the results are not convicing. The residuals indicate the samples are not capturing the posterior. Finally, the authors consider a relatively simple variant of the problem (23D). In this setting FM + simulator feedback just acts as a faster approximation to MCMC. Where FM + Simulator feedback might have an advantage is high dimensional unstructured data (e.g. images in the case of lensing)  
* Another shortcoming of the empirical evaluation is the relatively limited baselines. There are several approaches for unbiased inference with diffusion priors (like DPS) [1-4], so it would be good to add comparisons to some of these baselines.
* There is some missing discussion about related work about the guidance of flow matching models [5-6]. 
* The code to reproduce experiments is not provided though there are sufficient details in the paper.

### Questions
In addition to the weaknesses above: 
* What are the challenges to scaling the approach to high-dimensional spaces?
* How sensitive is the method to the quality of the simulator? What happens when the simulator contains significant approximations or errors?
* Have you explored using multiple different types of control signals simultaneously? Could this provide complementary benefits?
* Could the method be extended to handle multiple observations simultaneously in a more efficient way?

### Soundness
2

### Presentation
2

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
The paper presents a method for including simulator guidance in a flow matching-based simulation-based inference setup. The basic idea as far as I understand is to model the posterior using generative flow matching, and during training (possibly only at a fine-tuning stage), draw samples from the simulator by interpolating parameter samples from the velocity trajectory, and include an additional signal ensuring consistency between those samples and the training datapoint. The overall motivation is to increase simulation efficiency when a stochastic simulator is used for simulation inference (as is usually the case).

### Strengths
- Timely paper on an important problem in the field -- using information from the simulator to speed up simulation-based inference, in order to make it more sample-efficiency and well-calibrated.
- Discussion of several control mechanisms, which could be applicable depending on the specific simulator and domain.
- Good discussion of underlying theory, both the flow matching aspect as well as simulation-based inference. Sound comparison to surrounding context literature, e.g. relevance to classifier-free guidance.
- Application to an important and challenging problem in cosmology -- strong lens modeling, and comparison with a baseline HMC approach.

### Weaknesses
 - In the strong lensing section, while a comparison with HMC is done, a comparison with "traditional" neural simulation-based inference approaches like NPE is lacking. This comparison would significantly strengthen the outcomes of this experiment. Specifically, the paper should include a comparison with at least one established NPE method, such as a conditional density estimator trained with a neural network, to properly contextualize the performance gains (or losses) of the proposed method. The absence of this comparison makes it difficult to assess whether the method's performance is truly state-of-the-art, or whether similar performance could be achieved with a more standard approach.
- The pretraining/finetuning tradeoff is not comprehensively explored -- as far as I understand, a big advantage of the method is that one could just finetune using a smaller number of simulation calls. While this is mentioned briefly and tested for specific cases, a more comprehensive study of how fraction of finetuning for a fixed simulator budget affects the outcome would make the results quite a bit stronger. The paper should include a more systematic study of the impact of the pretraining and finetuning split on the final performance. This should include varying the fraction of the total simulation budget used for pretraining versus finetuning, and evaluating the performance of the method across these different splits. This would allow for a better understanding of the optimal use of the method for different simulation budgets.
- The high-level presentation could be made slightly clearer -- e.g., in Fig. 1, marking that the it is the posterior $p(\theta\mid x)$ that is being modeled/targeted, to immediately situate the reader to the problem setting. Furthermore, the description of the simulator control mechanism could be made more explicit. For example, a more detailed explanation of how the simulator is used to provide feedback to the flow matching process, and how this feedback is incorporated into the training objective would be beneficial.

### Questions
- Is there something particular about the flow matching setup (e.g. linear trajectories) that make simulator control applicable here, in contrast to a more traditional method like NPE? Does the method rely on assuming optimal transport coupling paths (eqs. 5-6), or is it more generally applicable?
- If I understand correctly, the goal of simulator control is to produce flow matching trajectories that better model the joint $(\theta, x_0)$ space by giving an additional signal that the interpolated parameter-generated samples should produce simulations consistent with the original $x_0$. This reduces the effect of simulator stochasticity. Could this partly be recreated by generating multiple samples from the same parameter point partway through training? Similarly, could producing a batch of samples for comparison to the $x_0$ further improve the flow matching control signal?
- In the strong lensing section, why was the comparison primarily made to HMC, rather than e.g. NPE?
- How critical was the $t > 0.8$ empirical threshold choice for controls, and do the authors expect this to be problem-dependent or fairly universal?

### Soundness
3

### Presentation
3

### Contribution
3
