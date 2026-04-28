# Measuring LLM Confidence through Stable Explanations

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
In many high-risk machine learning applications it is essential for a model to indicate when it is uncertain about a prediction. While large language models (LLMs) can reach and even surpass human-level accuracy on a variety of benchmarks, their overconfidence in incorrect responses is still a well-documented failure mode. Traditional methods for ML uncertainty quantification can be difficult to directly adapt to LLMs due to the computational cost of implementation and closed-source nature of many models. A variety of black-box methods have recently been proposed, but these often rely on heuristics such as self-verbalized confidence. We instead propose a framework for measuring an LLM's uncertainty with respect to the distribution of generated explanations for an answer. While utilizing explanations is not a new idea in and of itself, by interpreting each possible model+explanation pair as a test-time classifier we can calculate a posterior answer distribution over the most likely of these classifiers. We demonstrate how a specific instance of this framework using explanation entailment as our classifier likelihood improves confidence score metrics (in particular AURC and AUROC) over baselines across five different datasets. We believe these results indicate that our framework is both a well-principled and effective way of quantifying uncertainty in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new method for measuring the confidence of LLM answers. The key idea of the method is to estimate the distribution of LLM answers by marginalizing over the distribution of explanations given for each answer. And instead of using the empirical explanation distribution, the authors reweight sampled explanations by the probability that they are entailed by the question. The authors evaluate their method on five question answering datasets and two LLMs (both GPT models) and find that it outperforms baselines in terms of selective uncertainty, but not calibration.

### Strengths
1. **Interesting and novel approach to LLM uncertainty estimation.** I think the idea of accounting for the accuracy/plausibility of the explanation when computing uncertainty estimates is interesting and intuitive. However, I think in the current version of the paper, this key idea gets lost in a lot of jargon/details (e.g., the Bayesian framing). I think the paper would be improved if this idea was centered more.
2. **Strong results on the task of selective uncertainty.** The proposed method clearly outperforms baselines on this important task.
3. **Figure 1 is a nice, intuitive illustration of the benefits of the method.** I thought this was a great way to make the point that accounting explanation plausibility provides useful information about the probability that the resulting answer is correct.

### Weaknesses
1. **Bayesian framing of your method is confusing/misleading.** You frame the method as the computation of a posterior distribution, as is done in Bayesian statistics. While your proposed method certainly resembles this, I don’t think this description is fully accurate. In Bayesian analysis, the computation of a posterior distribution involves updating your prior beliefs about a distribution (i.e., the prior) based on new evidence (i.e., the likelihood). To do this, you apply Baye’s rule, multiplying the prior by the likelihood and dividing by the evidence. However, your analysis does not involve the inclusion of a prior. Because your approach is not exactly Bayesian, I found this framing (as well as your use of the term “posterior”) confusing. I think it is a bit misleading and makes it more difficult to understand your method. While I still think it could be useful to describe the connection between your method and Bayesian analysis (e.g., you can say that your approach is similar to computing a posterior predictive distribution), I don’t think this should be used as the main way of describing your method. Instead, your computation of the answer distribution by marginalizing over the explanation distribution can be seen as an application of the law of total probability.
2. **Point about generalization to out-of-distribution test data is not fully supported.** You claim that one of the main weaknesses of existing uncertainty quantification methods is that they assume that the training and test data come from the same distribution. And you suggest that your method can overcome this weakness through its consideration of the explanation distribution. This is an interesting point that I believe is worth investigating, but it seems mainly speculative – the paper doesn’t provide any clear evidence to support this. In particular, it’s not fully clear to me that just because including an explanation as an intermediate step results in a new answer distribution, this new answer distribution will be better calibrated for the test data. And you don’t provide any sort of theoretical analysis to back this point. Further, your experiments are all on common benchmarks that could have been included in the GPT training data. Finally, it appears to me that the existing methods for uncertainty quantification based on CoT-consistency share the same benefit as your method with respect to this issue – they also consider explanations and therefore, “adapt” to the test data. However, you make it sound all existing methods make the ID assumption and therefore are harmed by differences between training and test data. Can you clarify this?
3. **Calibration performance is limited, and it’s not fully clear why we should discount this task compared to selective uncertainty.** The proposed method slightly underperforms some of the other methods on the ECE metric. I think this okay, given the improved performance in the selective uncertainty metrics. However, I am not fully convinced by the authors’ argument that this metric should be discounted. In the discussion section, the authors say that the ECE metric relies on the “hypothesis that the training, test, and calibration data are all drawn from the same distribution.” It is not clear to me why this is the case. I get that calibration methods rely on this assumption, but I don’t get why the *evaluation* of ECE relies on this assumption. Further, to account for the limitations around the effect of binning size, it seems like the authors could present results for multiple bin sizes or also present results for an alternative calibration metrics such as proposed in [1].
4. **Use of the term ‘stable’ is not clear.** You say that prompting a model to produce explanations, such as with CoT, “serves to ‘stabilize’ the sampled answers around an isolated minimum.” It is not totally clear to me what you mean by this, and at least in my reading of Wei et al., 2022, I don’t see this claim made. What exactly do you mean by this? Do you mean that prompting via CoT results in a lower entropy answer distribution? And do you have evidence to support this? I am mainly picking on this point because you term your method “stable” explanations, so I think it’s important that a reader can understand what you mean by “stable.”
5. **Writing lacks clarity.** This is a little bit redundant with the points made above, but in many places, I found that this paper was not fully clear, e.g.:
* To describe your method in the intro, you say that it can be thought of as “computing the posterior predictive distribution by transductive marginalization over test-time classifiers.” This uses a lot of jargon, most of which you have not yet defined at this point (and some of which you never define, such as “transductive”). Also, as I said earlier, while what you do resembles computing a posterior predictive distribution, it isn’t the same in a strict sense. I think there are much simpler ways of describing your method, which would make the paper clearer.
* As described above, it is not clear what makes an explanation “stable.”
* In the methods section, you describe a step of your method that involves grouping explanations into equivalence classes by clustering them according to their resulting next token distributions. This step is unclear to me. Exactly how do you form these clusters? And then how do you use the equivalence classes in your computation of uncertainty?
* In your description of your method, I think it would be helpful to distinguish between the probability that an LLM outputs an answer (or explanation) from the probability that an answer (or explanation) is correct. Your current writing seems to conflate these two, which I think makes the text a bit harder to parse.
6. **Analysis is limited to GPT models.** It would strengthen the paper to see how the method works on other LLMs that are not GPT/OpenAI models (e.g., Llama, Claude, etc.).

### Questions
All my questions are in the weaknesses section.

### Soundness
2

### Presentation
2

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
This paper addresses the task of confidence calibration in multi-choice QA setting, i.e., exploring how to quantify the likelihood that the answers provided by LLMs are correct. 

The authors propose an ensemble-based method involving the following steps:
1. Explanation Sampling: Multiple explanations are sampled from the LLM using prompts (set with a temperature of 0.7) to generate diverse logical justifications for these different answers.
2. Explanation Probability Calculation: The probability associated with each explanation is calculated using the entailment prompt, i.e., prompting LLM to self-evaluate whether the explanation is correct given the question. 
3. Marginal Probability Calculation: The overall answer confidence is calculated by computing the marginal probability of the answer token logits conditioned on each possible explanation. 

The main contribution of this work is introducing a new ensemble-based mechanism that leverages explanations generated by the LLM itself. Experimental results show that this method achieves slight improvements over baseline approaches, particularly in complex reasoning tasks. However, its scope is primarily limited to multi-choice problems and includes only a few benchmark datasets​.

### Strengths
Originality: The paper proposes using explanations as latent variables to observe the model's uncertainty for each question and introduces a new ensemble method. This method evaluates the correctness of each generated explanation and then estimates answer confidence based on them. Compared to other methods such as consistency, it computes the final posterior probability of each answer based on all possible explanations. While the idea of using explanations may not be very new, the specific implementation and application of explanations in LLM's calibration setting has not been explored before.

Clarity: The paper is generally well-written and easy to follow. 

Significance/Quality: Overall, the paper introduces a new ensemble mechanism and demonstrates, through experiments, that it shows marginal improvements over baseline methods. However, its impact is limited by the focus on the multi-choice setting and a small set of benchmarks, making the broader applicability and superiority of the method less evident. Future work could extend this approach to more diverse problem settings to further establish its value.

### Weaknesses
Clarity: One area for improvement is the articulation of the motivation behind using explanations for the ensemble method. Providing more depth on why explanations are suited for this purpose would enhance the reader’s understanding, especially why using explanation in this manner can mitigate overconfidence. Specifically, the paper does not clearly explain why the probability of an explanation conditioned on a question is more informative than the probability of an answer conditioned on a question. The current explanation lacks a clear justification for why this approach would lead to better calibration.

Experiment setting: I view this method as an ensemble-based calibration method, so I feel like it should be compared with more ensemble-based methods besides CoT-consistency. The paper should consider comparing against other ensemble techniques that do not rely on chain-of-thought, such as methods that use multiple independently generated answers and average their probabilities. This would help isolate the specific contribution of using explanations versus simply ensembling.

Expense: The existing method's compuational complexity is O(n^2), while the CoT-consistency only requires O(n). I feel like the time complexity cost should be considered. The quadratic complexity, if accurate, could be a significant barrier to practical application, especially for large-scale datasets or real-time systems. The paper needs to provide a more detailed analysis of the computational cost and explore potential optimizations.

Overall significance: In general, this paper's impact is limited by the focus on the multi-choice setting and a small set of benchmarks, making the broader applicability and superiority of the method less evident. Future work could extend this approach to more diverse problem settings.

### Questions
1. Why did the authors choose to compute entailment probability and marginal probability for obtaining the final results, rather than performing semantic clustering on the explanations? The introduction in line 217 is too brief and somewhat difficult to understand. I feel like it would also be beneficial to try the semantic clustering approach during the experiment section or include a case study.
2. Why does utilizing explanations in this manner help mitigate overconfidence compared to directly using answers? The motivation for using explanation seems unclear to me, and I am a little bit struggled to understand why explanation can bring much more benefit than using multiple output answers directly. 
3. In Figure 1a, why is there a need to condition on correct and incorrect answers instead of simply generating explanations based on the question?
4. The hyperlink in line 319 is invalid.
5. Why is the term "stable explanation" used?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
* The paper proposes a novel framework for measuring LLM uncertainty by analyzing the distribution of generated explanations. The key insight is combining explanation sampling with a reweighting mechanism based on logical consistency, measured through entailment probability.
* The method is evaluated comprehensively across 5 datasets using both GPT-4 and GPT-3.5. Performance is primarily assessed using AURC and AUROC metrics, with several competitive baselines for comparison.

### Strengths
* Strong empirical results with thorough experimental validation.
* Well-grounded theoretical framework.
* Practical implementation requiring only black-box access to LLMs
* Comprehensive ablation studies that validate the contribution of each component

### Weaknesses
 * The paper could benefit from more figures, particularly a good figure 1 to help explain the method. Possibly some ROC figures in the main paper since AUROC is the main metric used.

 * The same model seems to be used to both generating the explanations and evaluating their entailment probability. Doesn’t this introduce circularity? A model that has learned an incorrect fact could use that fact in an invalid explanation and then give a high entailment probability for that explanation.

### Questions
* Could this method be used for open-ended generation tasks or is it only suitable for multiple choice questions?  
* The same model seems to be used to both generating the explanations and evaluating their entailment probability. Doesn’t this introduce circularity? A model that has learned an incorrect fact could use that fact in an invalid explanation and then give a high entailment probability for that explanation.

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
4

### Summary
The authors propose to estimate the uncertainty of LLM answers in single-token QA tasks by not directly recording an answer (probability) after giving a question, but asking for an explanation in-between. This is resampled multiple times per question and reweighted by how much the explanation fits to the question, judged by an NLI algorithm. First results show that this might improve the correctness AUROC on some datasets and models.

### Strengths
* The authors use five datasets that are challenging to current LLMs, as opposed to simple datasets like TriviaQA.
* Chain of thoughts / explanation prompting is a topic with increased current interest. 
* The limitation section is well-written, and I would love to see more experimental analyses mentioned there (such as the difference in performance on simple / hard questions)

### Weaknesses
* Many common baselines are missing, even if they are cited and discussed in the paper. I would have a higher trust in the results (and increase my soundness score) if the paper compared to P(True), Semantic Entropy, the entropy of the output distribution (eq. to Naive Entropy, because we only have one token), the number of different answers when prompted multiple times, and the Eccentricity of the NLI entailment graph between answers. To get you started quickly, I recommend the codebase of https://arxiv.org/abs/2311.07383 (I'm not author or affiliated with any authors of that paper, it's what I genuinely believe will help you the best and the fastest)
* The TTA approach has a higher ECE than the proposed method on 4 of the 5 datasets, but is hidden into Appendix B.7 because it is contemporary work. I agree that the underperformance should not be a reason for rejection because of the comtemporary nature of the work (and also because I don't believe that papers should be published if and only if SOTA) and it does not influence any of my scores (which I made before discovering it in B.7), but I strongly recommend bringing the results to the main paper for scientific integrity. 
* The authors only use 100-250 questions per dataset (Appendix B.2). This is likely to have large variance, but the variance is not reported. It could be that it is in the region of the recorded AUROC differences (~0.01 to 0.05). This lowers my soundness score. I believe a higher number of questions would be an easy way to improve the robustness of the experiments, since the experiments per Appendix B.3 currently take only 15 GPU hours (or more precisely, OpenAI-API hours). 
* Section 4.2 asks an interesting side-question, but makes an experimental choice which I believe confounds the results. That is, the (sequence) probability of explanations of wrong and correct answers is compared _after_ conditioning the generation of the explanation on the answer. Due to the autoregressive nature of Transformers, this will naturally lead to similar probabilities. Do you have data for explanations generated before giving the answer, i.e., the sequence probability of the "middle part" of a "question + explanation + answer" sequence (which is more aligned with what your method does)? This would be a highly interesting experiment, and allow to increase my soundness score. 
* The approach is limited to QA tasks with a single output token. This is a very synthetic setting compared to free-form answers, which limits the contribution score. 
* Experiments are limited to GPT-3.5 and GPT-4. These are very similar LLMs. It would be interesting to see whether the results transfer to, e.g., Llama-3.1-8b-chat (or Mistral/Falcon/Yi).
* Code and data are not released, hindering the replication of results.
* The notation is not clearly defined, hindering exact replication at the current state of the paper and being the prime reason for my presentation score (because the writing itself is good!). I.e., the (set?) $E$ is never defined. $\mathcal{A}^\tau$ is never defined. $a$ and $i$ can probably be used interchangably, since $a$ is always only a single token, bijectively identifiable by its index $i$. It's not defined whether the softmax is over the alphabet $\mathcal{A}$ or the set of possible answers $S$, and how that set $S$ is defined in the first place.
* The paper repeatedly makes the argument that the underperformance of token-likelihood based uncertainty estimates is due to a train-test distribution shift, particularly in the introduction and related works sections. However, there is no experimental data to back this claim and no data to show that the proposed method is better in this regard, such as transfer experiments or in-distribution vs out-of-train-distribution experiments. 
* The approach requires to sample multiple explanations, i.e., multiple sequences of additional tokens. This makes it expensive.

### Questions
* Do you generate the explanation before or after generating the answer? From the text, I understood that you use "Question, Explanation, Answer", but in Figures 1 (and 8 in the appendix) it looks the other way around. Is this only for the experiments in Section 4.2? 
* Why did you set the temperature to 0.7 as opposed to 1? Do you have data supporting this choice? (E.g., higher accuracy)
* Can you report the missing baseline approaches, other models, variance estimates, and potentially higher number of questions per dataset, as outlined above? 
* Can you add the updated section 4.2 experiment, as highlighted above?

### Soundness
2

### Presentation
3

### Contribution
2
