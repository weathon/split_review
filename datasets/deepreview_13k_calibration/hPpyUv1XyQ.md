# Uncertainty-Aware Decoding with Minimum Bayes' Risk

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
Despite their outstanding performance in the majority of scenarios, contemporary
language models still occasionally produce undesirable outputs, for example, hallucinated text. While such behaviors have previously been linked to uncertainty,
there is a notable lack of methods that actively consider uncertainty during text
generation. In this work, we show how Minimum Bayes’ Risk (MBR) decoding, a
method that was originally designed to account for the imperfect nature of probabilistic language models, can be generalized into a principled uncertainty-aware
decoding method. In short, we account for model uncertainty during decoding
by incorporating a posterior over model parameters into MBR’s computation of
expected risk. We show that this modified expected risk is useful for both choosing
outputs and deciding when to abstain from generation. We benchmark different
methods for learning posteriors and show that performance correlates with the
diversity of the combined set of models’ predictions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper examines Minimum Bayes Risk decoding for generated text while also ensembling together multiple models (or parameter settings).

### Strengths
- The paper has a fairly extensive number of experiments.

### Weaknesses
 - I'm quite familiar with MBR, ensembling, and other related methods, and to be honest the papers seemed like it was made overly complex/mathy while still omitting details about important parts. For instance, explaining the fact that you're sampling from multiple models and doing MBR over the resulting samples (equation 10) is not a difficult concept to explain, but it was couched in lots and lots of verbose equations. On the other hand, important parts that are non-trivial, such as the IVON method introduced in section 4.1, were not explained sufficiently. I feel like the paper could benefit significantly by trying to explain things in simpler/more straightforward terms.
- There is no discussion of time or memory complexity of the methods. I expect that these methods require significant computation, so it would have been better if that could be discussed.
- It's not very clear whether the methods proposed here significantly moved forward the state-of-the-art. As far as I know, the BLEU scores on WMT14 are quite low compared to the state-of-the-art for single models, which is 35 or so.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes minimum Bayes' risk (MBR) decoding considering the uncertainty of model parameters. The MBR is a decision rule for decoding which maximizes the expected utility, not a maximum a posteriori estimate, to avoid the model errors. This work takes into account the uncertainty in model parameters so that the decision rule can reflect the uncertainty in the model parameter estimation. This work also proposes a token-level sampling but approximated by Monte Carlo in order to avoid complex computation by taking average in each step. Experiments are carried out on several natural language tasks, e.g., machine translation and summarization, and show that the proposed method achieves gains when compared with a conventional MBR method.

### Strengths
- This work demonstrate the use of MBR considering the uncertainty in model parameters. The idea is straightforward and the proposed approach of two decision rules is a sound method in performing either summation across samples drawn from different parameters (Eq. 9) and summing within samples from the same parameters (Eq. 10).

- The proposed approach and the experimental design is coupled with IVON optimization which take into account the variance of parameters in training. Since the variance is also estimated during training, it seems to be easy to draw samples from sampled parameters.

### Weaknesses
The detail of the experimental design is unclear.

- The number of samples is unclear. The line 352 stats that is is using ensemble and samples for 4, but it probably implies the number of samples from a single model parameter, and this work has no report on how many samples were drawn for model parameters, that is the size of $\mathcal{M}$. Does it mean that 1 sample was drawn for the proposed method for each parameter sample set drawn from IVON so that the proposed approach is comparable to the baseline MBR with 4 samples?

- The relation of Deep Ensemble and the proposed method is unclear. The lines 311-319 state that Deep Ensemble is performed for each training run, so that multiple IVON parameters are learned. In this case, only a single parameter set is drawn for each learned IVON model, and performed MBR decoding using the proposed method, but is it correct? Note that Deep Ensemble is performing ensemble of decoding from multiple model parameters, and thus, it is basically the same as the token-level inference in Eq. 11. When mentioning Deep Ensemble, is it performing the token-level average for each step? Or, does this work leverage Deep Ensemble to learn several parameters to compare with IVON, which employs only a single training run?

### Questions
Please check my comments regarding weaknesses.

- Thank you for the clarification, and I feel this work has an interesting contribution in the field.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Minimum Bayes Risk Decoding (MBR) has a long history in machine translation and speech recognition research. As a variation of the Maximum A Posteriori decoding, it introduces a risk at the sentence level. The goal is to improve the output sentence globally. In this paper, The risk becomes utility and the goal is to find the hypothesis that maximizes the expected utility.  This paper proposes to extend this framework to include uncertainty on the parameters of the model. Therefore it requires a "double" expectation (or an expectation wrt the joint distribution of the sequence and the parameters).  Experiments are carried out on different tasks of conditional text generation: machine translation, summarization and data-to-text.

### Strengths
The motivation of Bayes inference is to marginalize what is uncertain. This paper proposes to take into account the uncertainty on the parameters on the top of MBR. This idea is very interesting and can be applied to both large pre-trained models, and smaller models trained from scratch only for one task.

### Weaknesses
The clarity is clearly the main issue with this paper; It is true that Bayesian methods are always difficult to describe, but in this paper it is sometime difficult to follow. One reason maybe that some important information are scattered in the paper.

For instance, the capital theta is not clearly defined. We can deduce it from the context but it does not help to understand. More importantly, there are many equations in the paper (this is not an issue of course) and we can get lost among their variants: the theoretical description vs  the approximated version, ... 
Maybe it could help to first describe the theoretical part of the method, with the probability distributions, and then in a following part how it is proposed to approximate the intractable summations.

It could help to better describe how the q distribution on large pre-trained model is estimated.
- It looks like uncertainty improves over MBR, but can you clearly state in the table what are  the baseline systems (w/o MBR) and what are your improved ones ? 
- The empirical results and the associated discussion could be improved. When you say "We find that weight uncertainty improves performance across all benchmarks, even with matched
compute budgets.", it could help to ground this claim in your tables.  
- The paragraph on the complexity is a bit short. MBR decoding is costly. Maybe you solution does not increase the complexity but could you provide inference time ? 
- Do you think the improvement in performance is worth the  overall computational cost ? This question stands for MBR and you method. 
- When you say "Connected to this, since predictive uncertainty has been shown to correlate with hallucinations (Xiao & Wang, 2021), ...", this not the same uncertainty ! In this work they use the entropy of the word distributions not on parameters. Could you comment on that ?

### Questions
- It could help to better describe how the q distribution on large pre-trained model is estimated.
- It looks like uncertainty improves over MBR, but can you clearly state in the table what are  the baseline systems (w/o MBR) and what are your improved ones ? 
- The empirical results and the associated discussion could be improved. When you say "We find that weight uncertainty improves performance across all benchmarks, even with matched
compute budgets.", it could help to ground this claim in your tables.  
- The paragraph on the complexity is a bit short. MBR decoding is costly. Maybe you solution does not increase the complexity but could you provide inference time ? 
- Do you think the improvement in performance is worth the  overall computational cost ? This question stands for MBR and you method. 
- When you say "Connected to this, since predictive uncertainty has been shown to correlate with hallucinations (Xiao & Wang, 2021), ...", this not the same uncertainty ! In this work they use the entropy of the word distributions not on parameters. Could you comment on that ?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper extends Minimum Bayes Risk (MBR) decoding to incorporate model uncertainty. During the computation of expected risk, standard MBR decoding assumes a model with fixed parameters that approximates the target distribution. This paper argues that the uncertainty in model parameters should also be considered, and proposes to compute the expected risk based on predictive posterior distribution. Specifically, the paper introduces two types of posterior distributions for uncertainty-aware MBR decoding: sequence-level and token-level posteriors. Empirical evaluation across various text generation tasks, including machine translation and text summarization, shows that the proposed method achieves consistent and strong improvements over unimodal MBR decoding.

### Strengths
1. This paper is well written, clearly motivated, and theoretically grounded.
2. The proposed method shows consistent and strong improvements to unimodal MBR decoding.

### Weaknesses
1. MBR is not a very efficient decoding algorithm. I am afraid that efforts on MBR decoding may have little chance to have practical applications.
2. The concept of token-level posterior is not well-established from a theoretical perspective. As these models represent sequence-level probability distributions, their ensemble, the predictive posterior should only be an expectation over sequence probabilities.
3. The baseline of standard MBR decoding is missing. Although there is a baseline of MBR@mean, it is not equivalent to the standard MBR decoding, where the model should be trained without weight uncertainty.

### Questions
Could you elaborate the difference between the two estimators in Eq.(9) and Eq.(10), and why Eq. (10) has lower complexity?

### Soundness
3

### Presentation
3

### Contribution
3
