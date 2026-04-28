# Fast Sampling via De-randomization for Discrete Diffusion Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Diffusion models have emerged as powerful tools for high-quality data generation, such as image generation. Despite its success in continuous spaces, discrete diffusion models, which apply to domains such as texts and natural languages, remain under-studied and often suffer from slow generation speed. In this paper, we propose a novel de-randomized diffusion process, which leads to an accelerated algorithm for discrete diffusion models.  Our technique significantly reduces the number of function evaluations (i.e., calls to the score network), making the sampling process much faster. Furthermore, we introduce a continuous-time (i.e., infinite-step) sampling algorithm that can provide even better sample qualities than its discrete-time (finite-step) counterpart. Extensive experiments on natural language generation and machine translation tasks demonstrate the superior performance of our method in terms of both generation speed and sample quality over existing methods for discrete diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Very interesting work. Assuming a diffusion process to exists several transition times ---when the process will be still after that time. Using this nice property can achieve acceleration of sampling steps. The authors study both the discrete process and the continuous process. The authors first point out that for each process there is a transition time. Then they prove that transition time are independently spread and follows a certain analytic density. Following this density, the authors design algorithms to jump at each transition time to achieve acceleration of diffusion sampling. Their method demonstrates efficiency in several scenarios using small NFEs.

### Strengths
This paper is novel, in the asense it proposes to leverage the transition time in the diffusion process to accelerate the sampling. As far as I know, no one before thought of that. And this method indeed achieves nice performance.

### Weaknesses
This paper is not complete. First of all, it lacks ablation studies to demonstrate the influence of distributions of the transition time. With respect, I do not agree with that, all instances of transition times are equal in effect.

Following up on the above point, why not the author study which instantiation of the transition time is the best for sampling, in the sense of quality and speed? Stopping at the distribution stage is not a good thought, I believe.

Another thing is the visualization of transition times, the x_t at those times, and other related values. Letting me see that x_t gets still after the transition time will make me more convinced of your method and creativity.

Apart from that, the authors did not implement this work in image generation. I guess they may have a good reason for that, as diffusion is the dominating and most influential method in image generation. A method to improve diffusion sampling but not implemented on the image is strange. Are there anything barriers to the method to apply in images?

Also, I believe the authors also agree with, the proposed method does not outperform competitors in all shown cases. Sometimes the improvements are marginal.

As a theoretical work, I appreciate the idea a lot, but the theoretical analysis is not that deep so I can safely vote for acceptance with no objection from the other reviewers and the AC. Deeper theoretical analysis related to sampling NFEs, approximation error with the original process, and techniques to further improve it could be much more appreciated.

I am not an expert in the language generation domain, if I have any mistakes, do please correct me.

The major problem of this paper to me, is the lack of enough empirical analysis, and results on image domains.

### Questions
Algorithms like DPM-Solvers do not work in the language case? Please kindly tell me.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a de-randomized diffusion method that can be used to accelerate existing discrete diffusion processes while preserving the conditional distributions. From here, they propose DNDM, a discrete non-Markov diffusion model, and evaluate the approach on language generation and machine translation tasks. The technique allows for a continuous-time sampling algorithm, which is demonstrated to have superior performance than discrete-time finite-step counterparts.

### Strengths
Originality:
- The paper proposes a de-randomization procedure for discrete diffusion processes, which allows for a huge boost to sampling speed. Furthermore, the procedure allows for a continuous-time formulation of the discrete diffusion process, which the authors demonstrate outperforms the finite-time counterparts.

Quality:
- The method is well-justified, and the mathematical framework behind the de-randomization process is clearly formulated. The experimental results demonstrate a clear speedup to sampling speed, as well as non-trivial boosts to BLEU score on conditional text generation tasks.

Clarity:
- The paper is generally well-written and clear.

Significance:
- Since the proposed de-randomization procedure is orthogonal to existing discrete diffusion processes (e.g. can be applied out of the box to Multinomial Diffusion (1) and Absorbing Diffusion (2)), and leads to sampling speedups and non-trivial performance gains, this work is likely relevant to many researchers in the area of discrete diffusion.

1. Emiel Hoogeboom, Didrik Nielsen, Priyank Jaini, Patrick Forré, and Max Welling. Argmax flows and multinomial diffusion: Learning categorical distributions.
2. Jacob Austin, Daniel D Johnson, Jonathan Ho, Daniel Tarlow, and Rianne Van Den Berg. Structured denoising diffusion models in discrete state-spaces.

### Weaknesses
 - The experiments are promising, but the scope is a bit limited. For example, the claims of the paper could be strengthened with results on sequence-to-sequence generation tasks such as question generation and paraphrasing (1, 2).
- An ablation of the choice to use Beta distribution to approximate the true transition time distribution (induced by the $\alpha_t$ schedule during training) would be clarifying. This is especially true in the case of the continuous time evaluation (Tables 1, 2), where it's slightly unclear whether the boosts to performance are due to the continuous time formulation or the choice of Beta distribution.

### Questions
Questions:
- The derivation of the de-randomization process (e.g. Thm 2.1, Thm 3.1) shows the conditional distributions $q(x_t \mid x_0)$ should be consistent with the standard Markov diffusion process. Then, what is the explanation for why DNDM generally underperforms RDM with 25 to 50 steps on conditional text generation (Tables 1, 2)?
- Similarly, why is it that DNDM consistently outperforms RDM at 1000 steps (Tables 1, 2)? Is this due to variance reduction in the sampling process with high step number, or the approximation of the true transition time distribution using the Beta distribution (or something else)?
- How well does the model compare to RDM when the Beta distribution transition times are not used?

Clarification:
- Regarding the WMT14 results, the authors mention the weaker performance relative to the other datasets could be a sign that WMT14 "violates our assumption that the pretrained score model is uniformly accurate for all time steps" -- could you clarify what this means?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an accelerated sampling method for discrete diffusion models by transforming traditional discrete diffusion forward processes to more deterministic equivalents, so that only a single transition is made in the forward process for each independent token. Sampling is then done by sampling the transition times for each token (along with the prior tokens), and iterating over each step that has any transitions occurring in it. Since for large step counts, there may be some time steps with no transitions occurring at all, the proposed method accelerates sampling by skipping over them. The paper further goes to present an infinite-step limit, where each token gets a different transition time, providing a maximum to the time required for sampling. The paper goes on to showcase that the method achieves competitive results in machine translation compared to another method for accelerating discrete diffusion sampling, and also provides clear improvements over standard discrete diffusion models in unconditional text generation on small-scale data sets.

### Strengths
+ The topic is important due to the slowness of most current discrete diffusion models. While there is quite a bit of work on accelerating continuous diffusion model sampling, less work exists on discrete diffusion model acceleration.
+ I think the idea is very sensible and presented in a very understandable manner. 
+ Does provide improvements over baseline D3PM model, as well as the previous RDM method with relatively large step counts
+ I found it especially surprising that the new sampling procedure outperformed the baseline uniform diffusion model on text8 so clearly, since seems that cutting down the sampling steps in a smart way actually improves generation quality. This is quite counterintuitive, given that usually increasing steps improves results in diffusion models.

### Weaknesses
- I think that the use of the phrase “sampling iterations” in the paper can be somewhat misleading, for instance on page 5, where it is indicated that the generation time increases sub-linearly with sampling iterations (as opposed to RDM). While technically true from the diffusion perspective, this also overlooks the fact that the relevant metrics are actually the amount of function evaluations (or the time taken for sampling). Similarly, comparisons with the same step counts to RDM in Table 1 & 2 seem suboptimal to me, and instead it should be (approximately) the same amount of function evaluations / wall clock time. 
- It would also be good to elaborate where exactly does the method provide an improvement over RDM, since they focused more on step counts <25, whereas the comparisons here are for step counts >25. In this sense, is the model even a direct competitor for RDM, or could the two methods be combined?
- I think the paper may require more work on clarifying what are the new contributions of the proposed model and designing the experiments such that they clearly showcase these contributions (see also questions on ARDM). E.g., under what conditions exactly can we expect improvements in sampling speed?
- It seems to me that there are quite a bit of (potentially subtle) similarities with the previous work [1], where the authors note a connection between absorbing diffusion models and order-agnostic autoregressive models. In particular, as pointed out in their Appendix C, the continuous-time limit of an absorbing diffusion model is effectively equivalent to to their order-agnostic ARDM, which seems to be also equivalent to the infinite-time limit for absorbing diffusion presented in this paper. Would the authors of the submission agree, or maybe are there differences that I have overlooked? I do see that in the non-infinite-time case, the models do not exactly match, and the model is formulated from a different point of view, potentially allowing more flexibility in designing the generative process. But it would be good to give more elaboration on the differences to ARDM and maybe also provide direct numerical comparisons in the paper. 
- One downside of the paper as of now is that a method to estimate the data likelihood is not included. Perhaps it would be possible to create a lower bound by not having having intermediate latents $x_t$ at all, and considering the transition times $\tau$ as latent variables? For instance, setting the inference distribution to $q(\tau^{1:D}) \prod_k^D q(x_T^k | x_0^k)$, where $\tau^k$ is distributed according to Uniform({1,…,T}), and the corresponding generative process defined such that we first sample from the priors $p(x_T)$ and $p(\tau)$, and then generate the different dimensions according to the ordering of $\tau$. If I am not mistaken, this would be similar to what was done in the ARDM paper as well, and one could form an ELBO similar to theirs.
- How is the evaluation with the BERT model done for the unconditional generation experiments, exactly?

### Questions
- It seems to me that there are quite a bit of (potentially subtle) similarities with the previous work [1], where the authors note a connection between absorbing diffusion models and order-agnostic autoregressive models. In particular, as pointed out in their Appendix C, the continuous-time limit of an absorbing diffusion model is effectively equivalent to to their order-agnostic ARDM, which seems to be also equivalent to the infinite-time limit for absorbing diffusion presented in this paper. Would the authors of the submission agree, or maybe are there differences that I have overlooked? I do see that in the non-infinite-time case, the models do not exactly match, and the model is formulated from a different point of view, potentially allowing more flexibility in designing the generative process. But it would be good to give more elaboration on the differences to ARDM and maybe also provide direct numerical comparisons in the paper. 
- One downside of the paper as of now is that a method to estimate the data likelihood is not included. Perhaps it would be possible to create a lower bound by not having having intermediate latents $x_t$ at all, and considering the transition times $\tau$ as latent variables? For instance, setting the inference distribution to $q(\tau^{1:D}) \prod_k^D q(x_T^k | x_0^k)$, where $\tau^k$ is distributed according to Uniform({1,…,T}), and the corresponding generative process defined such that we first sample from the priors $p(x_T)$ and $p(\tau)$, and then generate the different dimensions according to the ordering of $\tau$. If I am not mistaken, this would be similar to what was done in the ARDM paper as well, and one could form an ELBO similar to theirs.
- How is the evaluation with the BERT model done for the unconditional generation experiments, exactly?

Overall, I think the idea is good, but if I am not mistaken on the points regarding novelty compared to ARDM, the paper requires more work on finding and clearly presenting the unique angle in which the new discrete diffusion formulation contributes to the community. Thus, I think that the paper is not ready for publication yet. 

References:
[1]: Autoregressive Diffusion Models. Emiel Hoogeboom, Alexey A. Gritsenko, Jasmijn Bastings, Ben Poole, Rianne van den Berg, Tim Salimans. ICLR 2022.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an alternative formulation of the discrete multinomial-diffusion and absorbing-state-diffusion generative models, which is "de-randomized" in the sense that each token is randomly corrupted at most once during the forward noising process. This formulation motivates an "accelerated sampling" approach, in which they skip to the transition points instead of processing timesteps without token changes (although I'm not convinced this is done correctly). This allows them to use a finite number of generation steps for the continuous limit of infinite forward process steps. They find that their approach outperforms the "reparameterized diffusion model" (RDM) of Zheng et al. (2023) in terms of BLEU score for machine translation, and outperforms vanilla multinomial diffusion in terms of perplexity for text8 and enwiki8.

### Strengths
**[S1]** The alternative formulation of the forward process for multinomial diffusion and absorbing-state diffusion is interesting. This formulation, presented in Section 2.2, takes advantage of the fact that the noising distribution of these two types of discrete diffusion models is independent of the current state, e.g. the token at time $x_{t}$ is either exactly the same as $x_{t-1}$ or it is an independent draw from a noise distribution. This means you can construct a non-Markov process with the same conditional marginal distribution $q(x_t | x_0)$ by just picking a random time at which the token is replaced with a random token $w$, and then setting $x_t$ to either $w$ or $x_0$.

**[S2]** The proposed DNDM method seems to outperform RDM and vanilla multinomial diffusion for a fixed time budget, by skipping over wasted computation in RDM for large numbers of generation steps.

**[S3]** The paper is clearly written and easy to follow.

### Weaknesses
 **[W1]** I'm not convinced that the accelerated sampling algorithm that the authors propose is actually correct from a probabilistic standpoint. The authors motivate it by proving (in Theorem 3.1) that the transition times in the forward process are independent and follow a particular distribution based on the noise schedule. However, this is only proven for the *forward process*. In order for the proposed sampling algorithm to make sense, this property would have to also be true for the *reverse process*: it must be the case that, after conditioning on the current value of $x_t$, the transition times remain independent and have a tractable distribution.

This doesn't seem obvious to me. Note that the values of the tokens get noise added independently during the forward process when you condition on $x_0$, but are NOT independent when you condition on their values in $x_t$. This is why discrete diffusion methods are typically justified using a variational ELBO argument; approximating the tokens as independent creates a bias that must be corrected for through iterative refinement. The same might be true of the transition times.

**[W2]** Overall, the proposed algorithm seems to rely on intuition and heuristics for some parts, and some important technical details about the probabilistic model are glossed over.

- (a) The paper refers to the predictive model of $p_	heta(x_{t-1} | \hat{x}_0, x_t)$ as a "score network". For continuous diffusion, the "score" refers to the gradient of the marginal density with respect to the input. I don't think this is quite correct in the discrete case. Prior work on discrete diffusion models mostly doesn't seem to use "score network" terminology, or else uses it to refer to a very specific generalization of the continuous score (e.g. [Meng et al. (2022)](https://arxiv.org/abs/2211.00802))
- (b) The assumptions being made about the "score network" are not clearly stated, although the paper later mentions "the possibility that WMT14 violates our assumption that the pre-trained score model is uniformly accurate for all time steps" in the experiments section. This seems important because the predictive model $p_	heta(x_{t-1} | \hat{x}_0, x_t)$ is never perfectly accurate. In particular, in the standard diffusion model setup $p_\theta$ makes independent predictions for all tokens, whereas those tokens may have a nontrivial joint distribution. Additionally it is only trained using a variational bound, so it seems likely to me that it would not be "uniformly accurate for all time steps".
- (c) Although the proposed DNDM model has an identical forward process, the corresponding approximate reverse process distribution isn't clearly explained; the authors instead jump straight to a sampling algorithm, and it's not obvious that optimizing the training objective will make this sampling algorithm match the forward process.
- (d) The authors note that their reverse sampler decodes predictions using "different decoding strategies including greedy decoding, top-k decoding and temperature decoding" and mentions that argmax decoding shows strong performance. I don't think this makes sense under a probabilistic view of the process; this feels just like a heuristic to improve results. *Edit: There's apparently some precent for this, since the RDM model also uses heuristic decoding methods.*

**[W3]** The authors motivate their approach based on accelerating generation speed, but I'm not convinced the gains are actually significant when compared to just using an autoregressive model. The authors seem to focus on accelerating sampling when there are more denoising steps than there are tokens (e.g. the 1000-step and $\infty$-step conditions for WMT, the 1000-step and 4000-step conditions for unconditional generation). But if you have more denoising steps than tokens, it seems like you may as well just use an ordinary autoregressive model. Indeed, in the "$\infty$-step" diffusion, the continuous-time reverse sampler requires one network evaluation per token generated, which is the same number of computation steps as an autoregressive model would use.

I expect that an autoregressive model would have a better tradeoff between generation time and quality than the method proposed here.

**[W4]** The baselines for the experiments seem fairly limited. The authors only compare against RDM and vanilla multinomial diffusion models, but seem to introduce additional heuristics into the decoding process to get better results for a fixed compute budget. It seems to me then that it would be fairer to compare to the much larger set of non-autoregressive generative models, for which similar heuristics are considered fair game and for which many ideas have already been proposed and evaluated.

As one example, I believe Mask-Predict [(Ghazvininejad et al. 2019)](https://arxiv.org/abs/1904.09324) achieves higher BLEU scores on WMT14 (relative to this work) using only 10 model evaluations, by using argmax decoding and other heuristics. Many other examples are discussed in a survey by [Xiao et al. (2023)](https://arxiv.org/abs/2204.09269).

**[W5]** Unconditional generation samples (in the appendix) remain unimpressive relative to autoregressive model generation quality. This applies to previous work as well, of course, but I don't think the improvements in Table 3 translate to a noticeable increase in overall sample quality.

**[W6]** The proposed approach only applies to discrete diffusion models that have the form in Equation (1), but this is only a subset of the discrete diffusion models that have been considered in the literature. Austin et al. (2021) discusses a few alternatives that are not of this form (e.g. discreteized Gaussian, token-embedding-distance transitions, or hybrids of absorbing and other diffusion processes as discussed in the appendix). Another recent example is Blackout Diffusion [(Santos et al. 2023)](https://arxiv.org/abs/2305.11089).

### Questions
Can the proposed approach be formalized as a probabilistically-sound variational model, and if so, how? Relatedly, does the equivalent of Theorem 3.1 hold for the reverse process in general?

Relatedly, what assumptions are you imposing on the "score function"?

For the conditional generation tasks, I think the paper could be improved by including comparisons to ordinary autoregressive generation, and also to existing non-autoregressive machine translation baselines.

For the unconditional generation tasks, why don't you compare against RDM or absorbing diffusion? Also, how does your method do with a more realistic number of sampling steps (smaller than the sequence length), and how does it compare to an autoregressive model with the same compute budget?

I'm not sure what is meant by "full de-randomization". The transition times and the sampled tokens are still random, are they not?

Section 2.2 mentions "the chain rule" but it's not obvious to me what this is referring to. The equation seems correct but I don't think the derivation involves a chain rule (?)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
