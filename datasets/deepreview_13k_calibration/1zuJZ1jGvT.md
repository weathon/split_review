# Offline Reinforcement Learning with Closed-loop Policy Evaluation and Diffusion World-Model Adaptation

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Generative models, particularly diffusion models, have been utilized as world models in offline reinforcement learning (RL) to generate synthetic data, enhancing policy learning efficiency. Current approaches either train diffusion models once before policy learning begins or rely on online interactions for alignment. In this paper, we propose a novel offline RL algorithm, Adaptive Diffusion World Model for Policy Evaluation (ADEPT), which integrates closed-loop policy evaluation with world model adaptation. It employs an uncertainty-penalized diffusion model to iteratively interact with the target policy for evaluation. The uncertainty of the world model is estimated by comparing the output generated with different noises, which is then used to constrain out-of-distribution actions. During policy training, the diffusion model performs importance-sampled updates to progressively align with the evolving policy. We analyze the performance of the proposed method and provide an upper bound on the return gap between our method and the real environment under the target policy. The results shed light on various key factors affecting learning performance. Evaluations on the D4RL benchmark demonstrate significant improvement over state-of-the-art baselines, especially when only suboptimal demonstrations are available -- thus requiring improved alignment between the world model and offline policy evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work attempts to address the important issue of policy distribution shift in offline RL. The authors propose a novel method which uses a world model as a synthetic data generator for closed-loop policy evaluation, where the world model is adapted via importance sampling to the changing distribution of the learned policy. The proposed method is supported be theoretical bounds on the return gap and shows impressive performance on key offline tasks with suboptimal offline datasets.

\* Note that while this paper does fall squarely within my expertise, I was not able to give it the time it deserves and that is reflected in my confidence score.

### Strengths
1. The proposed method is novel, well-motivated and clearly explained.
2. Theoretical results to support claims of bounding the return gap between world model and environment.
3. Strong results.

### Weaknesses
1. While I like the method proposed by the paper, I don't see a clear dependency on diffusion. From my understanding, the method can be generalized to any world model with some form of uncertainty estimation. As such, I think the paper would be stronger if the method is generalized to any world model. However, I would also be satisfied by an ablation comparing diffusion to other world model types, and clearly showing why diffusion is necessary for the level of performance presented.

2. The paper can be made shorter and more concise to improve readability. I believe Section 3 is mostly unnecessary. You introduce the full notation and background of diffusion but barely sue it in the main text. I recommend shortening it significantly (possibly including it in Section 4) and leaving the full notation and explanation in the appendix as it is necessary for the proofs.

3. In Section 4.1, you state that "Introducing $s_{t+1}$ as an extra input significantly improves accuracy of reward prediction [...]". This is atypical in world model literature and I would recommend backing up this claim with an ablation. Specifically, an ablation study comparing the reward prediction accuracy of a model using only $s_t$ and $a_t$ as inputs versus a model using $s_t$, $a_t$, and $s_{t+1}$ would be valuable. Terminating based on high uncertainty is also new to me and a great suggestion! I would also love to see an ablation of this as this changes the distribution of your trajectories significantly. An ablation study examining the impact of different uncertainty thresholds on the overall performance would provide further insights into the robustness of this approach.

4. The main results in Table 1 are poorly presented. I would recommend replacing the table with aggregated statistics as suggested by [1]. Table 2 can also be bundled into this figure.

### Questions
1. I like the idea of using IS to adapt the world model but the reasoning is not exactly clear to me. Usually, we want to use IS to estimate some variable under an unknown distribution by reweighing it by some other known distribution. However, in this case, we can estimate both distributions very well. If my understanding is correct, can you motivate the use of IS more?
2. From my understanding, IS is a poor technique to use when the two (policy) distributions are very different and that is a completely plausible scenario in your problem setting. Can you explain how you avoid this? Furthermore, have you considered alternative techniques such as MCMC?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper operates in the setting of offline reinforcement learning. The paper proposes a new approach that uses an uncertainty-penalized diffusion model as a world model. This world model is used to update the offline policy by constraining a standard SAC's actions via uncertainty estimates. The world model is updated using importance sampling to address the distribution shift of the trained policy from the behavioral policy over time. The paper provides a theoretical analysis of error bounds as well as an experimental section highlighting the approaches performance in comparison with recent offline methods.

### Strengths
I would like to preface this review by saying that I am not an expert in offline model-based RL. However, I am very familiar with the general online RL and theoretical RL landscape.

1. Clarity  
a) The language in the paper is largely clear and the text has a clear red line that the reader can follow.  
b) The visualizations in Figure 1 and 2 are helpful to understand the approach.

2. Related work  
a) From what I can tell, the work cites the most prominent approaches in offline (model-based) RL and provides a reasonable amount of related work to differentiate its contribution from prior art.

3. Novelty  
a) Based on my (incomplete) knowledge the idea to constrain a model based on the distribution shift of the policy based on offline data only seems novel enough to warrant publication. However, other reviewers may have more insight into this than I do.

4. Experiments  
a) The experiments are conducted with a sizable number of baselines to demonstrate the capabilities. I do think the experiments demonstrate that there might be benefits of the method in lower quality data regimes. However, I have several things that need to be addressed before I can make a certain statement about this. I will come to them later.

### Weaknesses
1. Mathematical rigor and theory
  a) It is a well-known fact in the learning theory literature that approximate models are sufficient to obtain high return. Analysis on this goes as far back as [1] which can easily be adjusted to fixed distributions. Given that the paper states that this analysis is based on prior work, it is unclear to me what is being claimed to be novel here. There might be subtleties I am missing due to unclarity of notation which I will outline next. The claim of novelty should be made more precise and clearly distinguished from prior results.
  b) In equation 5, and all following similar expectations, it is not clear what $s_t$ is sampled from. This is quite important given that we are talking about distribution shifts and without this notation being precise it is difficult to determine the correctness. It appears that the expectation is taken with respect to the trajectory induced by running policy $\pi$ in the true environment. However, this should be explicitly stated. It is also not clear to me what an expectation over $\mathcal{M}$ means which seems to be a set. This notation should be clarified. 
  c) In equation 6, the TV distance is ill defined since $R(s_t, a_t)$ is not a distribution and there seem to be no assumptions on this function anywhere else. The authors should clarify what distributions are being compared in this equation. It seems that they might intend to compare the joint distribution of states and actions under different policies, but this needs to be made explicit.
  d) It is unclear to me, why assumption 4.3 is reasonable. The assumption states an upper bound on the total variation distance between the true and model-predicted state distributions in terms of the expected distance between states. This seems to disregard the presence of aleatoric uncertainty. The model could be perfectly accurate in its predictions, but if the environment has inherent stochasticity, the distance between two valid next states could still be arbitrarily large. It appears that this assumption might only be valid for deterministic MDPs or those with Lipschitz continuous transitions. This limitation should be addressed.
  e) Theorem statements should generally be concise, but they should also be self-contained. In order to understand Theorem 4.5, one would have to read large parts of the paper just to understand the notation. I recommend adjusting this as needed for readability. The provided proof is also not a proof, but it looks more like a sketch. I recommend stating it as a sketch and referring to the full proof.

2. Experiments
  a) Experiments over 5 seeds in reinforcement learning can often be misleading given the high variance. It would be beneficial to increase the number of seeds to at least 10 to ensure the statistical significance of the results.
  b) Tables 1 and 2 have the maximum average bolded. This can be misleading as the reader might think these methods are superior as it is not uncommon to bold statistically significant results rather than max averages. I recommend the manuscript is switched to the latter to avoid confusion.
  c) To address the previous point, it is necessary to report variance measures for all baselines and not the presented algorithm. That should in general always be the case. In Table 1, all favorable results on the med-exp dataset are within variance of another approach, at least one of the favorable results of med-rep is within variance of another approach and it is unclear how many of the other results are significant. In Table 2, at least 5/6 results seem to be within variance. Thus, the claim that the provided algorithm outperforms existing SOTA algorithms is not well supported. Statistical significance tests should be performed and reported to support any claims of superiority.
  d) The paper does not provide any additional analysis besides best returns on D4RL and as a result, it is not clear when I should use this method as the results on lower quality datasets are not completely consistent. This makes things tricky because many of the other results may not be significant. One way to remedy the fact that the results are not necessarily much stronger in many cases would be to provide analysis as to *when* this method helps. This could include an experiment that validates the claims about lower distribution shift error or an ablation on the properties of the datasets on which the approach works well. For instance, an analysis of out-of-distribution Q-values could shed light on whether the method effectively mitigates overestimation.

### Questions
Q1: Can you elaborate on assumption 4.3 and why this is a reasonable assumption to make?  
Q2: Can you elaborate on what parts of section 4.3 are claimed to be novel in this work and which parts are taken from previous work?  
Q3: Can you elaborate on what part of the theory is specific to your algorithm and which parts you believe are generally true for all approximate models?  
Q4: Can you elaborate on why you chose standard deviation as a measure of dispersion?

### Soundness
2

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
4

### Summary
This paper proposes a model-based offline RL algorithm leveraging diffusion models. Unlike past works that use pre-trained, frozen diffusion models for generating synthetic rollouts, this work proposes to iteratively align the model's predictions with the evolving policy during training. A theoretical analysis is provided that provides an upper bound on the return gap between an optimal policy trained inside the diffusion model versus the real environment, and experiments are performed on D4RL that show an improvement over canonical offline RL methods.

### Strengths
- The experimental results are strong. Most of the required baselines (see weaknesses) are implemented and the proposed method outperforms them in aggregate.
- The theoretical analysis is additive, and as far as I can tell, sound.
- The paper is generally well-written and well-motivated.
- The appendix provides some interesting additional results that support the main body.

### Weaknesses
Though the results are impressive, my primary concern is that the method appears to be very similar to that proposed in [1,2]. It seems the key difference from prior works is the proposed mechanism for realigning the diffusion model's predictions with the changing policy during training. However, when this mechanism is ablated in Figure 3, it appears to only significantly improve performance in one of the four datasets on halfcheetah (medium-replay). The reader would be able to better understand the performance gains expected from this method w.r.t. the methods from [1,2] if they were implemented as baselines, but unfortunately they are not. A more thorough comparison of the authors proposed method with those from [1,2] would improve the paper, and leave the reader more confident that their proposals are a concrete step forward from these works.

**Minor feedback**

- Lines 120-121: Ha & Schmidhuber's paper introduced world models for online RL, not offline RL
- Section 3 title should be "Preliminaries"
- Line 151: "Agent [that] acts..."
- Line 153: transits -> transitions
- Line 161: "real dynamics $P$”?
- Line 272: collects -> collected
- Section 5 title should be "Experiments"
- Line 490 there should be text following _i.e._
- Missing closed brackets in Equations 7 and 8
- Missing brackets in Equation 12
- Line 398: "practically"

### Questions
**Important questions**

- How does the performance of ADEPT compare to past works that utilise diffusion models as world models for policy training on D4RL (namely DWM (Ding et al., 2024) or PGD (Jackson et al., 2024)?
- Are the importance-sample updates more important to final performance in environments other than halfcheetah?

**Less important questions**

- Where are the uncertainty intervals for the baselines in Tables 1 and 2?
- You set $H$ to 5, how does performance change with different values of $H$? 

If the authors answer the important questions I'm more than happy to update my score.

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
This paper deals with synthetic data generation in offline RL using diffusion models. Their principal contribution revolves around two methodological changes; introducing a penalty in the reward calculation for uncertain states, and employing importance sampling to account for policy distribution shift. They motivate their design decisions theoretically, and demonstrate strong performance in D4RL, a standard offline RL benchmark.

### Strengths
In general, I find the work reports good results and, while in places is hard to parse, has writing of a reasonable standard. I raise a number of strengths for this paper below.

- I find the related work has generally good coverage over crucial areas, besides what I would class as a significant error in description for [1] (below) and an omission.
- I like the approach of penalising overestimation by relying on the uncertainty of the world model itself. This is quite elegant.
- Using importance sampling to account for distribution shift is also intuitive (though based on the ablation has a relatively minimal impact on performance). I guess it just makes things theoretically sounder.
- I am grateful to see an ablation study, which I think is very inforamtive. However, I think making claims about the significance of important sampling is hard, given that reported values are often in confidence. The ablation study does clearly suggest that the uncertainty penalty in ADEPT contributes to performance improvement.

### Weaknesses
I have a number of strong concerns about this paper.

- I found figure 1 quite confusing, and personally think that if a figure needs such a long caption the figure is probably quite unclear. For instance, I don't follow what (b3) demonstrates. It seems like finding a way to show this without showing all the data points etc., for visual purposes, might make things clearer. The current visualization makes it difficult to understand the temporal relationships between the different components of the algorithm, especially how the world model, policy, and importance sampling interact over time. A clearer depiction of the iterative process, perhaps using a more abstract diagram, would be beneficial.
- In related work, stating that [1] doesn't 'provide explicit mechanisms to solve the distributional shift issue' is **fundamentally false** - that is the entire and explicit basis of the method. Besides this, I found the related work relatively thorough; one other relevant work would be [2]. The claim that [1] does not address distributional shift is inaccurate, as the core of the method involves guiding the diffusion process to generate samples that are more aligned with the target policy, which directly tackles the distributional shift. This mischaracterization undermines the credibility of the related work section.
- I found the description of the architecture hard to interpret. I would clarify that the MLP predicts the reward when the architecture is first interpreted. Similarly, the way the inputs are introduced ('we replace $\mathbf{x}_0$ with ...') was a bit confusing and could be worded better. The description of how the MLP integrates with the diffusion model is not clear, particularly how the reward is predicted using the output of the diffusion model. The explanation of input replacement is also vague and needs to be more precise to understand the data flow.
- Despite spending a long time with it, and attempting to verify the appendix proofs, I found I had a tough time with this maths and didn't find it intuitive to follow. It is also not made clear to me how the derivations in the paper lead to the reward gap guarantee at the top. Note I am not coming from a theoretical background, but imagine that others might also find this difficult. The theoretical derivations are not presented in a way that is easily accessible, and the connection between the intermediate steps and the final reward gap guarantee is not clearly explained. The lack of intuitive explanations makes it difficult to assess the validity of the theoretical claims.
- It feels this should be compared to other existing methods for compensating for overestimation bias. The key baselines here should be comparing the same policy optimisation algorithm with different approaches for reducing overcompensation bias. This is not what is shown in this paper. The evaluation lacks a direct comparison with other methods that specifically address overestimation bias, which is a critical aspect of offline RL. The paper should include baselines that use the same policy optimization algorithm (e.g., SAC) but with different techniques for mitigating overestimation, such as adding pessimism to the value function.
- There are no error bars for any of the results besides ADEPT's, meaning it hard to see overlapping of confidence intervals. The absence of error bars for the baseline methods makes it difficult to assess the statistical significance of the reported improvements. This omission prevents a proper comparison of the performance of ADEPT with other methods.
- It is unclear whether the error bars report standard devision or standard derror. In table 2, the caption reads 'we show the standard deviation of the performance... Note that the standard *error* is usually large...'
- I feel it is important to raise the significant issue of referencing in this paper as a weakness as well as in my ethics review. Buried in the appendix (line 903) there are 12 cited papers, many with common authorship and none with relevance to this paper or explanation. Either these papers are relevant to this work, and should be raised as related work with explanation, or they are not and thus should not be included. I assume these papers should not be included in this paper, but if they should be describing **why** is important.


There are also a small number of minor points and typos to highlight:
- In line 37, stating that offline datasets typically consist of limited transitions is tautological; the offline dataset can't be infinite by nature.
- In line 44, the world model does not interact with the policy! The policy interacts with teh world model.
- The acronym of the algorithm (ADEPT) does not fit its name at all really.
- Defining in line 181 that $\hat{P}$ is the transition distribution defined by the world model would be worthwhile.
- Line 190 'is a certain various schedule' doesn't make sense and I am not sure what it is meant to say.
- Line 190 'the diffusion model define another' - firstly, this should be 'defines another'. Secondly, the diffusion model is composed of a forward and backward process, rather than this being defined by the diffusion model itself.
- Line 199 does not make sense.
- The first sentence of the methodology does not make sense.
- Line 346: I don't really know what this means - what is the discrepancy?
- Line 357: 'of between $\pi$' should not have 'of'
- Line 381: 'there existing $\delta$' should read 'there exists $\delta$
- Line 398: 'piratically' is not the correct word I asume.
- Line 411: I don't know what $H$ is and it is not defined I don't think.
- In table 2, all bolded values are with a standard error of each so bolding, which implies significant improvement, is misleading.

### Questions
- It seems a bit counterintuitive/non-obvious to compute your done flag as when uncertainty reaches a limit. Does this effectively just lead to truncated rollouts? What kind of bias does this have on bias?
- I don't quite understand the assumption of line 340, that you can omit one of the inputs in the proof. To my understanding the reward model comes after the denoising model, and as such would not intrinsically be able to ignore $\hat{s}_{t+1}$. Is this not correct?
- How were hyperparameters for the underlying learning method tuned? It says they were consistent for different methods - were they tuned for ADEPT or for one of the base algorithms, or are they taking default values.
- How does this method compare to other approaches which compensate for overestimation bias? For example, how does it compare against policy guided diffusion ([1] above)?

### Soundness
2

### Presentation
1

### Contribution
2
