# Jump Your Steps: Optimizing Sampling Schedule of Discrete Diffusion Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 5, 8, 8

## Abstract
Diffusion models have seen notable success in continuous domains, leading to the development of discrete diffusion models (DDMs) for discrete variables. Despite recent advances, DDMs face the challenge of slow sampling speeds. While parallel sampling methods like $\tau$-leaping accelerate this process, they introduce \textit{Compounding Decoding Error} (CDE), where discrepancies arise between the true distribution and the approximation from parallel token generation, leading to degraded sample quality. In this work, we present \textit{Jump Your Steps} (JYS), a novel approach that optimizes the allocation of discrete sampling timesteps by minimizing CDE without extra computational cost. More precisely, we derive a practical upper bound on CDE and propose an efficient algorithm for searching for the optimal sampling schedule. Extensive experiments across image, music, and text generation show that JYS significantly improves sampling quality, establishing it as a versatile framework for enhancing DDM performance for fast sampling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method, Jump Your Steps, to optimize the discretization schedule of discrete diffusion models, by minimizing the compounding decoding error (CDE). The authors provide a KL-divergence upper bound (KLUB) for different continuous-time Markov chains of discrete diffusion models and propose techniques to efficiently approximate the timesteps minimizing KLUB.

### Strengths
This paper proposes an approach to improve the sampling quality and efficiency by optimizing the sampling schedule. This paper is well-written and easy to follow. The sampling and acceleration of diffusion models is an interesting topic for the community.

### Weaknesses
- Theorem 3.1 seems to be standard entropy bounds, and Theorem 3.2 seems to directly follow from Equations 3.2 and 3.4 of Ding & Ning (2021) and Theorem 3.2 of Sabour et al. (2024). The authors should illustrate their technical contributions and the novelty of their theoretical results with a comparison to the previous literature.
- The authors only compare the JYS schedule with the uniform schedule. Additional experiments on other schedules, e.g. EDM, Linear LogSNR, and Cosine LogSNR, should be presented.
- The proposed scheduling strategy only considers $2^K$ numbers of function evaluations (NFE). How can the schedule extend to other values of NFE?
- In Figure 5, is there any intuition to explain the error increase of the $k$-Gillespie sampler with the JYS schedule when NFE=16?
- In Figure 10, the comparison between uniform and JYS is not significant for NFE=32, 128, or 256. Please consider providing additional experiments on other image datasets, e.g., toy 2D datasets in Sabour et al. (2024).
- The practical significance of JYS is not fully convincing. In Figure 19, the quality of JYS with NFE=64 is clearly worse than uniform with NFE=128, which seems to contradict the claim that JYS achieves comparable performance with half the NFE. The visual quality of the generated samples is a key factor in evaluating generative models, and the results in Figure 19 raise concerns about the practical impact of the proposed method.

### Questions
- The proposed scheduling strategy only considers $2^K$ numbers of function evaluations (NFE). How can the schedule extend to other values of NFE? 
- In Figure 5, is there any intuition to explain the error increase of the $k$-Gillespie sampler with the JYS schedule when NFE=16? 
- In Figure 10, the comparison between uniform and JYS is not significant for NFE=32, 128, or 256. Please consider providing additional experiments on other image datasets, e.g., toy 2D datasets in Sabour et al. (2024).

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
4

### Summary
This paper introduces Jump Your Steps (JYS), a novel approach that optimizes the allocation of discrete sampling timesteps. It achieves this by minimizing Compounding Decoding Error (CDE) without incurring any additional computational cost. The authors derive an upper bound on CDE and employ techniques to simplify the computation. Based on the upper bound, they propose an algorithm for searching for the optimal sampling schedule, thereby enhancing the sampling quality.

### Strengths
The algorithm presented in this submission is straightforward and simple. Experimental results have been provided to demonstrate the feasibility of the proposed algorithm.

### Weaknesses
1. The novelty of the proposed algorithm is rather limited. The authors merely transfer Align Your Steps (AYS), which is originally for image generation, to the framework of SEDD for text generation.

2. The experiments conducted on the CIFAR-10 and Countdown datasets lack practical significance. In the realm of image generation, efficient sampling methods have been well explored. For CIFAR-10, even with 256 NFEs, the proposed approach can only achieve an FID higher than 10. In contrast, some popular sampling methods for image generation, such as DPM-Solver++ (https://arxiv.org/pdf/2211.01095) and DMD (https://arxiv.org/pdf/2311.18828), can attain an FID less than 4 using only 10 or even just 1 sampling step. Additionally, the Countdown dataset is a synthetic one. I suggest that the authors place the results for CIFAR-10 and Countdown in the appendix. Moreover, as I am not familiar with music generation, it appears to me that although JYS can lead to a significant drop in Hellinger distance, the Hellinger distance for uniform sampling timesteps is already small (less than 0.4).

3. It seems to me that the practically meaningful experimental results are mainly showcased in Figure 8 for text generation. Nevertheless, upon examining Figure 8, I cannot observe a significant improvement over the use of uniform sampling timesteps.

4. Some problems in the writing:
- The right arrows used on Line 52 seem strange. Additionally, such right arrows occur multiple times in the main content. It is suggested to use normal notations instead (and I don't think there is a need to write down the whole sequence for timesteps repeatedly).
- The term "KLUB" is first seen in Figure 2 on page 4; however, its explanation is only provided in Theorem 3.1 on page 5.
- There is no necessity to write down the Sampler in Figures 6 and 7.
- In the section on "$k$-Gillespie's Algorithm" (Line 125), '$k$' apparently means updating $k$ tokens in parallel. However, in Appendix B.1 KLUB COMPUTATION, the use of '$p(t|k)$' is presented and it is explained that this is determined by the pretrained noise schedule. As a result, I am not certain whether '$t$' signifies time. If it does, then it appears inconsistent with '$k$'. Please provide a more detailed explanation about $k$-Gillespie's Algorithm.
- The condition $\mathbb{P}_{t_0} = \mathbb{Q}_{t_0}$ in the last sentence of the proof of Theorem 3.1 should be presented as an assumption in the statement of Theorem 3.1.

### Questions
N/A

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
This paper introduces Jump Your Steps (JYS), a method for discrete diffusion models (DDMs) that enhances generation quality by finding optimal sampling schedules when using efficient parallel sampling methods. Parallel sampling methods such as τ-leaping can speed up DDM inference, but they introduce a Compounding Decoding Error (CDE) that demotes sample quality. The authors address this by deriving a practical upper bound on CDE and developing an efficient schedule optimization algorithm that minimizes this bound without additional computational overhead. They perform experiments on image, music, and text generation tasks to show that the JYS approach improves sampling quality across different transition kernels using fast sampling methods like τ-leaping or k-Gillespie.

### Strengths
The main idea of this paper is novel: the authors suggest reframing DDM sampling schedule optimization as a CDE minimization problem, introducing a Kullback-Leibler divergence upper bound (KLUB) metric to make the optimization tractable for improving sample quality in fast DDM sampling methods. The theoretical development seems sound, establishing connections between CDE minimization and path-space probability measures. This work is particularly interesting because it requires no architectural modifications or additional inference costs, unlike existing methods. As for the empirical validation, the paper includes an evaluation across diverse domains showing consistent improvements in the sample quality when using the same number of function evaluations (NFEs) as a baseline approach.

### Weaknesses
1. The empirical analysis can be improved: 
 - While improvements in the generation quality in terms of FID or perplexity scores are shown, comparisons against other quality-improvement methods (e.g., predictor-corrector approaches mentioned in Section 1), and an explicit study of their computational costs are missing. The paper should either include such comparisons or justify why they aren't necessary. Specifically, a comparison against predictor-corrector methods with varying correction steps would be valuable to understand the trade-offs with JYS. It is also unclear how JYS compares to other schedule optimization methods, such as those based on adaptive step size integrators.
 - The trade-off between schedule optimization time (or its memory requirements/end-to-end generation time) and sample quality gains isn't studied, making it difficult to assess the method's practical utility. The paper should include a detailed analysis of the optimization time for different problem sizes and how this time scales with the number of function evaluations (NFEs) used during sampling. This should include a breakdown of the time spent on KLUB estimation and schedule optimization.
- No error bars or standard deviations are provided for the quantitative metrics. This is important since generative models can have high variance in their outputs and metrics. An elaboration of the significance of the reported results would be appreciated. The lack of error bars makes it difficult to assess the statistical significance of the reported improvements. It's crucial to understand if the observed gains are consistent across multiple runs or if they are due to random fluctuations.
-- The comparison is limited to a uniform scheduling baseline. Would it be possible to compare against an adaptive step size integrator method (Runge–Kutta method modifications if they are applicable to the discrete case) or other works like a recent one [5]? It’d be great to include this or explain why such comparisons aren't applicable or necessary. A comparison against more sophisticated baselines, such as adaptive step-size methods, is needed to demonstrate the superiority of the proposed approach. The current comparison to a uniform baseline is insufficient to demonstrate the practical benefits of JYS.
2. The paper doesn't clarify how the diffusion model formulation (Eq. 1) relates to other DDM variants from [2, 3, 4]. Such discussion would be appreciated. Specifically, it is unclear how the continuous-time formulation relates to discrete-time formulations and how the method would apply to different transition kernels used in these other formulations.
3. The single-state transition assumption, while mathematically convenient, limits the method's applicability: it can lead to suboptimal schedules for fast-changing processes. It’d be great to see ideas on possible extensions to handle multiple transitions while maintaining computational tractability. The single-state transition assumption is a strong limitation, and the paper should discuss the potential impact on the quality of the optimized schedules. It would be beneficial to see a discussion of scenarios where this assumption is likely to fail and how the method could be extended to handle more complex transition dynamics.
4. Some technical details are difficult to follow or verify. For example, the authors introduce two techniques for KLUB computation in Section 3.5 but don't explain when each is preferable. It looks like both techniques are combined in Algorithm 1. No discussion of whether the hierarchical breakdown strategy converges to globally optimal schedules. The clarity of the paper could also be improved. There are suggestions on this in the Questions section.
5. No code is provided for reproducibility.

### Questions
1. As the empirical validation of the KLUB is a proxy for CDE, would it be possible to directly show that minimizing KLUB actually reduces this error?
2. Does the hierarchical breakdown strategy guarantee convergence to a globally optimal schedule?
3. The paper says “After K iterations, this hierarchical strategy yields a sampling schedule with 2^K NFEs, optimizing the schedule as the number of steps increases.” in lines 289-29. So, there is an exponential factor appearing in the number of function estimations. I wonder if it affects the overall complexity and method’s applicability, especially in resource-constrained settings.
4. I also wonder if the computational gain from this approach leads to higher memory costs. Is it this case from your observations?
5. Is there any intuition on how the method's error bounds scale with data size, or it doesn’t matter?
6. Is there any insight into the applicability of the proposed method to DDMs without fast sampling algorithms?
7. Do you think the hierarchical breakdown strategy converges to globally optimal schedules?

Small suggestions regarding the manuscript:
- There is no need to define DDMs (lines 12, 30, 94, for example) or CDE (line 156) a few times through the text if they were defined before.
- In Eq. 1 and this section, I’d suggest explicitly defining $x$ (data) and $y$ (corrupted data) variables.
- Line 133: Should it be “.” instead of “:”? 
- Maybe notations in line 148 can be combined with Section 2.1 or moved there? I’d suggest the authors go through their manuscript to make sure all notations are introduced and consistent.
NFE is not defined in line 290 or earlier. Also, it is useful to explain what it means (it is the number of calls to the score NN, right?).
- Maybe it’s worth moving Section 5 to the Intro section or a separate section at the beginning of the manuscript? Also, mentioning papers [1, 2] might be helpful.
- Adding equation numbers to Algorithm 1(line 7) would be helpful.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper describes a way to optimize sampling for discrete diffusion models. The idea is to select a good subset of optimal sample times based on an optimization criterion. Some theory and some experiments are given.

### Strengths
The direction of this research is new and interesting.

### Weaknesses
Some of the theory parts confounds heuristic and rigorous justification (by ignoring some long-time dependencies without actually emphasizing that this is a working simplification). Thus, some assumptions and/or limitations are not highlighted, which is making the paper look weaker. ----[update] this was addressed in the discussion, with reference to appendices

Also, I am not completely convinced with the interpretation of some of the experiments, but this may be just me. --- [update] the authors clarified and promised to amend some figure

1) line 189 saying "motivated by this observation" is not correct/precise I think, given that you list a bunch of factors at work and you just focus on one? the only motivating point is the dependence on sampling methods, and not the others.

2) line 202 "if we ignore the accumulated error from the previous steps": why should we ignore it? can you formulate this as an assumption somewhere?

I think that the paper's theory part might have very non-sharp estimates in case this error can't be ignored, can you convince me otherwise?

3) can you comment on when is the inequality in (7) sharp? I think this has to do with question 2.

4) line 216-217 "this theorem suggests" -- I think that it'd be accurate to say "based on the case that inequality (7) is sharp, we are tempted to hypothesize" and to mention that in case accumulated error from previous steps is negligible, then this heuristic becomes stronger.

Note that in applications in which the gap in (7) is large, then theorem 3.1 gives a lax and uninformative upper bound and this heuristic has no reason for holding.

5) about Theorem 3.2, when is the inequality in (8) sharp? Upper bounds like KLUB are useful to the extent to which they are close to sharp. So this limits the range of applicability of (8), and therefore it would be good to have a description of cases in which this is sharp.

6) about the hierarchical time breakdown (described in paragraph 3.4 and summarized in Figure 3) : this is one possible time breakdown strategy. Can you comment on alternative strategies, or on how this one is better than, or equivalent to, other strategies? 

7) line 298-299 what do you mean by "computational complexities"? This is vague and easy to misinterpret for a reader. I think you mean the thing mentioned in lines 350-360? If so, I suggest moving those lines up here, so that the reader has a concrete thing in mind since the beginning.

8) about the formula/equation at lines 308-309: what does the "approximately equal" sign actually mean? and why or under what hypotheses is this approximation valid? You mention something in the preceding paragraph, but this is not giving a clear cut answer to what approximation you have in mind, and on what are the underlying assumptions behind it.

9) about figure 9, I am puzzled/perplexed by the cases (a) and (c): 
In (a), why do you think that the JYS schedule has so dense subdivision in the first interval? I don't see anything in the "ground truth steps" graph that would indicate that this is optimal. 
In (c), why is the JYS deciding to just not include any timesteps in the first interval? In there, I think that the Ground Truth Steps part has a very dense time dependence, at least that's what I see in the figure.. so how do you justify this discrepancy?

To summarize, both points (a) and (c) show that JYS has high discrepancy in its "optimized" timestep choice, compared to "ground truth samples", so it would be good to understand what this means, how do we interpret this.

### Questions
1) line 189 saying "motivated by this observation" is not correct/precise I think, given that you list a bunch of factors at work and you just focus on one? the only motivating point is the dependence on sampling methods, and not the others.

2) line 202 "if we ignore the accumulated error from the previous steps": why should we ignore it? can you formulate this as an assumption somewhere?

I think that the paper's theory part might have very non-sharp estimates in case this error can't be ignored, can you convince me otherwise?

3) can you comment on when is the inequality in (7) sharp? I think this has to do with question 2.

4) line 216-217 "this theorem suggests" -- I think that it'd be accurate to say "based on the case that inequality (7) is sharp, we are tempted to hypothesize" and to mention that in case accumulated error from previous steps is negligible, then this heuristic becomes stronger.

Note that in applications in which the gap in (7) is large, then theorem 3.1 gives a lax and uninformative upper bound and this heuristic has no reason for holding.

5) about Theorem 3.2, when is the inequality in (8) sharp? Upper bounds like KLUB are useful to the extent to which they are close to sharp. So this limits the range of applicability of (8), and therefore it would be good to have a description of cases in which this is sharp.

6) about the hierarchical time breakdown (described in paragraph 3.4 and summarized in Figure 3) : this is one possible time breakdown strategy. Can you comment on alternative strategies, or on how this one is better than, or equivalent to, other strategies? 

7) line 298-299 what do you mean by "computational complexities"? This is vague and easy to misinterpret for a reader. I think you mean the thing mentioned in lines 350-360? If so, I suggest moving those lines up here, so that the reader has a concrete thing in mind since the beginning.

8) about the formula/equation at lines 308-309: what does the "approximately equal" sign actually mean? and why or under what hypotheses is this approximation valid? You mention something in the preceding paragraph, but this is not giving a clear cut answer to what approximation you have in mind, and on what are the underlying assumptions behind it.

9) about figure 9, I am puzzled/perplexed by the cases (a) and (c): 
In (a), why do you think that the JYS schedule has so dense subdivision in the first interval? I don't see anything in the "ground truth steps" graph that would indicate that this is optimal. 
In (c), why is the JYS deciding to just not include any timesteps in the first interval? In there, I think that the Ground Truth Steps part has a very dense time dependence, at least that's what I see in the figure.. so how do you justify this discrepancy?

To summarize, both points (a) and (c) show that JYS has high discrepancy in its "optimized" timestep choice, compared to "ground truth samples", so it would be good to understand what this means, how do we interpret this.

### Soundness
3

### Presentation
3

### Contribution
2
