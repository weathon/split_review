# Rethinking Uncertainty Estimation in Natural Language Generation

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 5, 3, 3, 3

## Abstract
Large language models (LLMs) are increasingly employed in real-world applications, driving a need to determine when their generated text can be trusted or should be questioned. To assess the trustworthiness of the generated text, reliable uncertainty estimation is essential. Current LLMs generate text through a stochastic process that can lead to different output sequences for the same prompt. Consequently, leading uncertainty measures require generating multiple output sequences to estimate the LLM’s uncertainty. However, generating additional output sequences is computationally expensive, making these uncertainty estimates impractical at scale. In this work, we challenge the theoretical foundations of the leading measures and derive an alternative measure that eliminates the need for generating multiple output sequences. Our new measure is based solely on the negative log-likelihood of the most likely output sequence. This vastly simplifies uncertainty estimation while maintaining theoretical rigor. Empirical results demonstrate that our new measure achieves state-of-the-art performance across various models and tasks. Our work lays the foundation for reliable and efficient uncertainty estimation in LLMs, challenging the necessity of the more complicated methods currently leading the field.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach to uncertainty estimation in natural language generation (NLG) models. The authors propose using the negative log-likelihood (NLL) of the generated sequence as a surrogate for uncertainty estimation. By leveraging the theoretical framework of proper scoring rules, they demonstrate that NLL can serve as an effective uncertainty metric. This approach simplifies the estimation process because it only requires the likelihood of the generated sequence under the model, avoiding the need for multiple samples. The theoretical foundation is well-established within the framework of proper scoring rules, and the empirical results demonstrate the method's superiority over existing metrics across various models and tasks.

### Strengths
- The paper introduces a new uncertainty estimation metric based on NLL that avoids the need for multiple sequence generations, which is a common bottleneck in existing methods.
- By eliminating the need to generate multiple output sequences, the proposed method significantly reduces computational overhead, making it more practical for large-scale applications.
- The method achieves or surpasses the performance of existing state-of-the-art uncertainty estimation methods across different models and tasks.
- The approach shows strong performance across various model architectures, sizes, and training stages, demonstrating its broad applicability.

### Weaknesses
 - The proposed metric focuses on statistical uncertainty derived from model probabilities but does not explicitly account for the semantic aspects of generated text. Incorporating semantic uncertainty would provide a more holistic estimation, capturing discrepancies between the generated content and the underlying meaning or intent. While the authors briefly discuss this limitation in the conclusion, it remains a significant issue that warrants deeper exploration, possibly through additional methods or combined metrics.
- While the experiments are extensive, they focus primarily on free-form question-answering tasks. Additional experiments on other types of NLG tasks (e.g., dialogue generation, story generation) would strengthen the claims.
- The paper spans 7 pages, whereas the conference allows submissions up to 10 pages. This unused space represents an opportunity to expand on key areas such as additional experiments, detailed analyses, or discussions that could further strengthen the paper's contributions.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a MAP-based approach to estimating uncertainty in large language models (LLMs) to improve the reliability of generated text. Traditional Monte-Carlo uncertainty estimation methods rely on generating multiple output sequences, a process that is computationally intensive and inefficient at scale. This study introduces a streamlined method that estimates uncertainty using only the negative log-likelihood of the most probable output sequence, eliminating the need for multiple sequences. The proposed approach maintains theoretical rigor and outperforms or matches existing methods across a range of tasks and models.

### Strengths
- Computational Efficiency: The proposed uncertainty measure requires only a single output sequence, significantly reducing computational costs compared to methods that generate multiple sequences, making it highly scalable for real-world applications.
- Theoretical Soundness: Using MAP as the metric of uncertainty is grounded in established principles of proper scoring rules, ensuring theoretical robustness while simplifying the complexity of uncertainty estimation for natural language generation models​.

### Weaknesses
 - Questionable Efficiency: It seems to me that obtaining the MAP sequence (argmax) is non-trivial. While seemingly at the end of the day we only get one sequence, taking efforts to approximate it to be the MAP could be no computationally cheaper than sampling a lot of candidates, which is exactly what the paper is claiming to avoid. It would make the paper more compelling, if the authors can briefly study how well the argmax sequence is approximated, and if the approximation of obtaining argmax is not quite good, what is the worst-case performance of the proposed method.

### Questions
Please refer to Weaknesses).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Traditional uncertainty estimation relies on sampling-based methods, which inevitably incurs additional computation cost. This work addresses this limitation and proposes to measure the uncertainty solely based on the negative log-likelihood of the most likely sequence. Empirical results demonstrate the performance of the proposed metric in distinguishing between correct and incorrect answers.

### Strengths
1. The proposed metric alleviates the need for sampling to estimate the uncertainty in natural language generation. 

2. The derivation of the different uncertainty terms and defining aleatoric and epistemic uncertainty is helpful.

3. The presented experiments cover a few backbone models and representative tasks.

### Weaknesses
1. The only metric proposed by this work is the zero-one score, which is one minus the predictive distribution for the most likely output sequence. Therefore, I find this is actually equivalent to propose $p(y=y’|x)$ as the confidence estimation, which has been widely applied in the machine learning community, whereas uncertainty is simply derived by 1-confidence. Consequently, this metric lacks technical novelty.

2. Though the proposed NLL metric seems to be superior to baselines, this work lacks justification and insights on why the NLL is a better metric than the variants using sampling. Specifically, the paper does not delve into the nuances of how the NLL captures different aspects of uncertainty compared to sampling-based methods, such as the variance in predictions across multiple samples. This makes it difficult to understand the underlying reasons for the observed performance differences.

3. Verbal explanations have been widely implemented in estimating the confidence level of LLMs. The author includes relevant discussion in Line 249. However, there is no empirical comparison to this type of baseline.

### Questions
1. What’s $\mathcal{D}$ in Line 115?

2. Could you provide more justifications on why NLL may be better than other sampling-based baselines?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes to quantify the uncertainty of a language model for a specific prompt using the log-likelihood of the most probable sequence. Empirical results show that this new measure is effective in quantifying the uncertainty of the model without having to generate multiple times.

### Strengths
1. The paper studies an important topic, which is crucial for many applications (e.g. improving trustworthiness of LMs).

2. The experiment results are good, which is surprising given the simplicity of the proposed method.

### Weaknesses
1. The idea to use a single generation to “approximate the most likely output sequence (line 223)” is concerning - the motivation is to avoid generating multiple sentences, and yet in order for beam search to find the most probable sentence (even in a toy setting), it requires multiple samples (Appendix A, Figure 2). Practically, I don’t know how close a greedy sampled / top-k sampled sequence is close to the most likely sequence even of the same length. The paper does not provide any analysis on the distribution of log-likelihoods of different sequences, nor does it discuss how the variance in these log-likelihoods might affect the proposed uncertainty measure. It's unclear if the greedy approach consistently finds a sequence that is even close to the mode of the distribution over possible sequences.

2. The contribution (using log-likelihood of one generation) is somewhat limited to empirical findings without any theoretical guarantees that one generation is able to find a sequence that is close to the most probable sequence. The paper lacks a theoretical justification for why the log-likelihood of a single, greedily generated sequence should correlate with the model's uncertainty. Without theoretical backing, it's difficult to generalize the findings beyond the specific experiments conducted. The paper does not address the potential for the greedy approach to get stuck in local optima, and how this might impact the reliability of the uncertainty measure.

2. The paper is not very well written, making it difficult to understand what the authors want to convey. See the questions section.

### Questions
083: What is \mathcal{V} here? You need to introduce the vocabulary. 

094: “since \mathcal{Y} scales exponentially with the sequence length T.” Here you defined \mathcal{Y} as all possible sequences, which is an infinite set so it shouldn’t be growing. If you want to make this claim, you can define \mathcal{Y}_t as the subset of all sequences with length <t. 

098-100: “We consider uncertainty for a given LMs, … a valid assumption” I am a bit confused, what is the assumption here?

111: Here if you are sampling y’ from p(\cdot |x, \cdot) it is better to write it explicitly “y’ \sim …” It can be a bit confusing here, and I am not sure how the discussion on “Proper Scoring Rules for Uncertainty Measures.” advances your main claims - if this is only about evaluation, you can defer this to later sections.

127: Again, I am not sure how “Aleatoric and Epistemic Uncertainty” relates to your proposed method. The purpose of “related works” or “preliminaries” is to make people ground your work to existing literature, if you believe that your proposed method is connected with this literature, make it more explicit.

898: “The reference answer sampled using beam search with a size of 20 is considered for assessing overall correctness, as it represents the most likely answer generated by the language model” - why is beam search of 20 = most probable answer? Do you have any guarantees that a beam size of x makes the generated sequence log-prob close (difference bounded) to the most likely sequence?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies the uncertainty quantification for LLM. The paper first defines uncertainty as the expected score (which needs to be designed) of LLM prediction with respect to all possible parameters fitting the data. It then defines the scoring function as zero-one indicator of whether the generated sequence reaches maximal likelihood. The paper claims the estimation of the final uncertainty quantity only requires max-decoding (such as beam search). The paper evaluates the proposed method against prior baselines on 3 tasks for 6 LLMs. The paper used AUROC to measure accuracy and claims the proposed method achieves the best.

### Strengths
1. The uncertainty quantification for LLM is an important topic. 
2. The derivation of aleatoric and epistemic entropy is valid. 
3. The introduction of zero-one score is valid.

### Weaknesses
1. The writing of the paper is very blurred. It is not clear which part is from prior paper, which part is the original contribution in this paper. Eq(7-8) are proposed in this paper. But Eq(1-6) are unclear. 
2. The definition of uncertainty in Eq (1) seems to suggest there is a groundtruth y generation. The definition in Eq(2) is questionable. It is unclear what is the posterior distribution of parameter w. Does it need to have a distribution of parameter? What if the parameter is fixed. 
3. The actual estimation algorithm is not described. In particular, Eq(8) needs to estimate an expectation term. It is unclear how to estimate this part. There is no description in the paper. 
4. The evaluation approach and the metric used are quite questionable. It is unclear why this particular F1 threshold-based correctness is used. But the details of estimation such correctness is also not described well. The use of LLaMA 70B as the evaluator is also quite questionable. The paper lacks justification for using a large language model as a judge, especially without fine-tuning for this specific task. The potential biases and limitations of using LLaMA 70B in this manner are not discussed.

### Questions
1. Are eq (1-6) developed by you or prior work? 
2. what is the exact step to calculate Eq(8).
3. Do you have real groundtruth measurement for generation correctness?
4. How many generations do you need to estimate uncertainty for one sequence?

### Soundness
2

### Presentation
1

### Contribution
1
