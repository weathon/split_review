# Scaling Optimal LR Across Token Horizons

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
State-of-the-art LLMs are powered by scaling -- scaling model size, dataset size, and cluster size. It is economically infeasible to extensively tune hyperparameters for the largest runs. Instead, approximately optimal hyperparameters must be inferred or \textit{transferred} from smaller experiments. Hyperparameter transfer across model sizes has been studied in \citet{mup}. However, hyperparameter transfer across dataset size -- or token horizon -- has not been studied yet. To remedy this we conduct a large-scale empirical study on how optimal learning rate (LR) depends on the token horizon in LLM training. We first demonstrate that the optimal LR changes significantly with token horizon -- longer training necessitates smaller LR. Secondly, we demonstrate that the optimal LR follows a scaling law and that the optimal LR for longer horizons can be accurately estimated from shorter horizons via such scaling laws. We also provide a rule-of-thumb for transferring LR across token horizons with zero overhead over current practices. Lastly, we provide evidence that LLama-1 used too high LR, and argue that hyperparameter transfer across data size is an overlooked component of LLM training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies how the optimal learning rate changes when varying the total number of tokens that are fed into GPT-3-like models (which, equivalently, means training for a longer time). Consistently, it is found that increasing the number of tokens corresponds to a decrease in the optimal learning rate. This inverse relationship is then studied more in detail by fitting a power law, and its extrapolation allows for a precise prescription of how the learning rate should scale with the number of tokens. Finally, this approach has discovered that LLAMA-1 has been potentially trained with a too-large learning rate.

### Strengths
The paper has significant strong points.

1. Experimental Scale. The authors had the capability to run large-scale experiments (billion scale). This makes the results very reliable in the specific experimental setting adopted here (i.e. architecture, model size, optimizer setting).

2.  The research question of how the learning rate should scale up is very important in practical settings and it is not covered in either theoretical or empirical research. Thus, the experimental findings are both novel and relevant.

3. The case study on LLAMA training is very interesting, for instance, by retrospectively questioning how hyperparameter tuning was performed in that setting.

### Weaknesses
 The paper has some weaknesses, mainly due to the depth of the investigation that is performed. More concretely (in order of importance):

1. It is unclear whether the observed inverse relationship between the number of tokens used for pretraining and optimal learning rate is due to the fact the model is trained progressively for a longer number of time steps, or because the network has processed more data. This is quite a fundamental experiment, and it’s unclear what the view taken by the authors is, given that the meaning of the term “token horizon” is not entirely specified. This could be tested, for instance, by fixing the amount of data and training for multiple epochs, and by increasing the batch size while fixing the number of steps (this is already partially done in the current paper). Aggregating these experiments together with the ones already performed by the authors should elucidate the aforementioned question. Specifically, it remains unclear if the observed learning rate scaling is a function of the total number of training steps, the total number of unique tokens seen, or a combination of both. The paper does not sufficiently disentangle these factors, which is crucial for understanding the underlying mechanisms driving the observed trends. For example, the authors could have explored scenarios where the same dataset is iterated over multiple times, or where the dataset size is varied while keeping the number of training steps constant.

2. The experiment of Section 4 ignores the fact that as the scale gets larger, the value of $\beta$ is very different. Thus, with the provided evidence these results are hardly predictive of the optimal learning rate in the joint scaling (model size, token horizon), and more investigation is needed. In fact, the observation that $\beta$ changes with scales (which the authors make) should already advise against the approach of independently fitting the constants for model size and token horizon. However, the authors explicitly advertise this suggestion to practitioners. On the other hand, it would have been more appropriate to see reported how $\beta$ changes with scale, especially for $\mu$P. In particular, for $\mu$P we expect the learning rate to transfer across width, so the joint scaling properties should be more feasible to test. The paper's claim that a single $\beta$ value can be used across different scales is not sufficiently supported by the evidence, especially given the observed variation of $\beta$ with model size. The authors should have provided a more detailed analysis of how $\beta$ changes with scale, and how this impacts the predictive power of their proposed scaling law. Furthermore, the practical advice to use a fixed $\beta$ value is potentially misleading, as it does not account for the observed variations.

3. The authors observe a different $\beta$ for different model size (Table 5). Fundamentally, the authors increase the model size by increasing both the width and at times the depth of the model. Thus, it is unclear whether the observed different $\beta$ at different model sizes is due to the width or the depth scaling.


Minor:

4. Another fundamental limitation of this work is that $\beta$ would potentially change as any architectural modification is made (e.g. QK norm, attention method, gating, etc..). Thus, the $\beta=0.32$ proposed to practitioners, on top of the problems stated above, is valid only in the GPT-3 setting studied. I think this should be emphasized more to not be misleading. 

5. I am not entirely clear on the purpose of the $\mu$P  experiment. $\mu$P is just not designed to exhibit hp transfer across a number of samples (in this case, the number of tokens, or equivalently training time). Thus it is not entirely clear what the expectation of this experiment was in the first place. However, in the related work section, the authors state that exploring this limitation was part of the objectives of the paper, hence I do not decrease my score for this reason.

6. The $\mu$P extension to depth scaling is derived in at least two existing works [1,2]. Thus, there is a parametrization that exhibits learning rate transfer across depth as well. However, I would partially still agree with the authors that the scaling with respect to depth still has to be fitted with power laws (as it is advertised to practitioners), due to the nature of Transformers that have >1 layers within a single residual block. Despite this, I would appreciate it if a more thorough/informed explanation of these suggestions were present in the paper.

### Questions
What do these results seem to suggest about a possible “$\mu$P extension” to a simultaneous scaling limit of the multiple dimensions (token, width)?

**Update**

I thank the authors for their additional answers.

I apologize if it was not very clear, but please let me stress the fact that my point about the semantics of what token horizon means underlies deep questions about the paper's claim and the extension of their validity. In my honest opinion, this paper presents exciting results about how the optimal learning rate evolves with more training time. However, it fails to define adequate boundaries for the (empirical) claims. In this respect, the fact that no specific meaning is attributed to token horizon stems from these missing experiments that would help to disentangle the various causes of the right shift of the optimal learning rate. Therefore I would not say that the new results are *"completely consistent with our previous experiments"*: however, they are consistent with the revised notion of token horizon that does **not** equal dataset size. And I do sincerely appreciate the authors for promising to update the paper, and carefully revising the notion of token horizon across the manuscript. 

The fact that $\beta=0.32$ transfers across architectures is itself a very counterintuitive claim, and in my opinion, it would require significantly more ablations to be verified. I would at least state that it could be that more investigation is needed for architectures that are not GPT or Llama-1, and $\beta=0.32$ might not be the right scaling exponent outside the tested framework (I thank the authors for pointing out Figure 11). At a fundamental level, no explanation is provided as to what and why the shift happens. Thus, I think these limitations have to be addressed (i.e. stated). 

I am referring to the papers that extend the lr transfer to the network's depth: https://openreview.net/forum?id=17pVDnpwwl and https://arxiv.org/abs/2309.16620.

Overall, I think that with the agreed revision of the storyline around the conceptualization of token horizon, and with the additional experiments, this paper deserves a slightly higher score. Thus, I am updating it to 6.

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
4

### Summary
As LLMs are scaled up it is not possible to tune hyperparameters at the largest scale. This necessitates a way of predicting optimal hyperparameters. This paper focuses on predicting optimal LR as the training dataset size is scaled. Specifically, they fit a scaling law for optimal LR as a function of dataset size and find 1. Good fits to the scaling law and 2. The exponent is negative i.e. optimal LR decreases with increasing tokens. They also find that they can fit the loss vs log-LR curve by a quadratic (At least around the optimum value).

### Strengths
As described, the problem studied by the paper is important and the paper's findings give an important starting point for predicting optimal LR.

### Weaknesses
There are some other hyperparameters which strongly interact with learning rate such as weight decay and warmup. The paper does not explore the interaction between these factors and learning rate.

The warmup used by the authors is much smaller than that used in many recent works[1]. The authors should provide more justification for this choice, especially given the potential for instability with very short warmups.

### Questions
The warmup used by the authors is much smaller than that used in many recent works[1].


To confirm that the results are robust to values of other hyperparameters, could the authors report results on one of the setups but with 10% warmup steps and 0 weight decay? Assuming the results are robust, I would be happy to increase my score.

 
[1] SMALL-SCALE PROXIES FOR LARGE-SCALE TRANS-
FORMER TRAINING INSTABILITIES.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper conducts an empirical study to characterize scaling law of optimal step-size with respect to the token used in the training of LLMs. They make some interesting observations: 1- best step-size shrinks approximately according to D^.32 where D is the training horizon and 2- this scaling law is almost consistent for different network sizes.

### Strengths
The paper is clear and well written. It delivers what it promises.

This is an impactful research area. Efficient methods or scaling laws for finding best step-sizes helps to improve overall training efficiency and performance.

### Weaknesses
The paper provides no analysis or in-depth intuition on why optimal LR scales with exponent -.32 ~= -1/3. 

The scale of experiments are rather small for a fully empirical paper. Unless there is an analytical explanation or intuition provided for the observed patters, the trends might be unreliable for larger networks and longer horizons. In the same vein, would the scaling law remain the same for other transformers like Llama and Mistral? It would also be interesting to study how optimal LR scales with respect to training horizon in other architectures like ResNet and MLP.

In general, this is a solid paper, however in my view it falls marginally below the ICLR bar in terms of contributions. See below for some suggestions that I think would help in improving the contributions and the scores.

### Questions
Can the authors provide any theoretical analysis or intuition for why the optimal learning rate scales with an exponent of approximately -1/3?

Could the authors use their fitted scaling law to propose a new LR schedule. For example, an LR schedule that decays with t^{-.32}. Does this outperform cosine decay? Is -.32 the best decay exponent for LR schedule? 

Could you strengthen your claims by testing the scaling law on other transformer architectures like Llama and Mistral, as well as non-transformer architectures like ResNets and MLPs? This would help demonstrate the generality of the observed scaling behaviour.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper shows that the optimal learning rate is decreasing in dataset size across scaling parameterizations, in contrast to most existing work on scaling, which studies model size (depth/width) only, and not data budget. They find that the optimal learning rate decreases approximately as a power law in the data budget, and provide a heuristic to help practitioners select an optimal learning rate scaling over data budgets. Their experiments include language model pretraining runs up to 2.7B parameters and 800B tokens, on which they fit these scaling trends.

### Strengths
I have not seen works touching on optimal LR with respect to data budget before, so this is neat. The message of the paper is clean and simple: optimal learning rate for language model pretraining decreases approximately as a power law in the data budget. In particular some strength are: 

- The message is short and simple, and the empirics are done with reasonably standard architectural decisions, and are -- most importantly -- at large scale. I imagine this was a reasonably expensive paper to write in terms of compute. 
- They check multiple parameterizations, including $\mu P$, which is important. 
- The validate their predictions and include a nice touch of showing an actionable consequence: that the LR of Llama was not tuned optimally. 
- The batch size factoring in the optimal learning rate is neat and intuitive and a good sanity check since the BS and LR are often optimized/tuned together in practice.

### Weaknesses
My gripes are mostly methodological. 

- In my mind, the main contribution is an empirical one: the dots you plot. I didn't put much weight into the actual fitted scaling laws because you fit a *separate set of constants to each curve* as you varied token horizons for a fixed model size. As I understand it, the main point of a scaling law is that you should be fitting a *fixed set of constants for all token horizons* and THAT is what you should be plotting. I suspect this is the reason for your unusually strong fit. The quote from von Neumann comes to mind: "With four parameters I can fit an elephant, and with five I can make him wiggle his trunk." Ideally, you should even be using one fitted set of constants ACROSS model sizes, but since your focus is on data and not model size scaling, I can forgive this. But one set of fitted constants per model size is a bare minimum: the current setup for how fitting is done is misleading if I am correctly understanding it. 

- It is unclear whether the main (scaling) experiments are done on the absolutely right type of architecture, ie. a modern "Transformer++," which is what they'd need to be to be most relevant to practice. Using architectural and hyperparameter choices from GPT3 is suboptimal because optimized Transformer++ architectures today use things like RMSnorm, RoPE embeddings, no linear biases, Adam $\beta$ values of $(0.9, 0.95)$, etc. Most people who work on pretraining know this, and the GPT3 architecture is certainly far from an optimized modern (2024) version by most people's standards. I see there are some preliminary experiments with the "Llama-1" architecture (though I'm not sure if it includes all the elements I outlined above). I believe the results, to be clear, and am not asking for new experiments, I just think there are some strange architectural choices even if mostly they are standard. Maybe including one ablation sweep with the architecture I described above (see perhaps the OLMo architecture for an example of a vanilla Transformer++) to check the same trends hold in the same way.  

- The functional forms you posit and fit are somewhat arbitrary. You choose a quadratic and power law, respectively, but do not explore other fits as I understand it, or even justify from any theoretical perspective why these should be the correct fits. Again, to be clear, I personally think these posited forms are fine, but they are indeed arbitrary and this requires justification.

- You definitely need to ablate LR schedule to make sure these are not an artifact of cosine LR schedule.

### Questions
- If my understanding is correct, $\mu P$ describes a particular scaling scheme for how to adjust hypers as you scale width or depth (the latter being described in more recent depth-$\mu P$ extensions, like [1]). When you say you "scale in $\mu P$" but then sweep tokens at a *fixed* model size, I don't know what this means, or how it's different from standard parameterizations? Are you just referring to using a particular initialization scale, then? Can you explicitly tell me how you are scaling in the main (standard) vs $\mu P$ experiments and how they differ if you are not varying model size in the latter, for instance in Figure 5?
- It is known why we need to decrease LR with model size, $N$, and it has to do with reasons relating to how EoS/sharpness scale in $N$, for instance see [2]. Is there a similar theoretical reason why the optimal LR should be smaller on larger data budgets? Why should we expect a priori lower LR* when training for longer (especially since LR schedules usually decrease LR over training anyway)? 

[1] Bordelon, Blake, et al. "Depthwise hyperparameter transfer in residual networks: Dynamics and scaling limit." arXiv preprint arXiv:2309.16620 (2023).

[2] Noci, Lorenzo, et al. "Why do Learning Rates Transfer? Reconciling Optimization and Scaling Limits for Deep Learning." arXiv preprint arXiv:2402.17457 (2024).

### Soundness
3

### Presentation
3

### Contribution
2
