# Enhancing Hallucination Detection with Noise Injection

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 3, 5, 5, 5

## Abstract
Large Language Models (LLMs) are observed to generate plausible yet incorrect responses, known as hallucinations. Effectively detecting such hallucination instances is crucial for the safe deployment of LLMs. Recent research has linked hallucination to model uncertainty, suggesting to detect hallucinations by measuring dispersion over answer distributions obtained from a set of samples drawn from the model.
While using the model's next token probabilities used during training is a natural way to obtain samples, in this work, we argue that for the purpose of hallucination detection, it is overly restrictive and hence sub-optimal. Motivated by this viewpoint, we perform an extensive empirical analysis showing that an alternative way to measure uncertainty - by perturbing hidden unit activations in intermediate layers of the model - is complementary to sampling, and can significantly improve detection accuracy over mere sampling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the potential of injecting noise into the intermediate layer outputs of LLMs to induce greater uncertainty when they are prone to hallucination.

### Strengths
* Good logical flow and storytelling.
* Clear presentation of experimental results and straightforward mathematical formulations.

### Weaknesses
 * Lack of theoretical justification for the noise injection approach: Although the injection method is simplistic, the authors do not clarify why they chose to sample noise from a uniform distribution with fixed mean and variance across LLMs. This choice raises concerns about the generalizability of the results. The lack of a principled method for selecting the noise distribution and its parameters, such as mean and variance, is a significant oversight. The authors should provide a more rigorous justification for their choices, potentially exploring alternative distributions or adaptive methods for parameter selection based on the specific characteristics of the LLM and the task.
* No evaluation of statistical significance: The reported performance improvements with noise injection are marginal, and the absence of confidence intervals weakens claims regarding these improvements. The use of point estimates without any measure of uncertainty makes it difficult to assess the reliability of the observed gains. It is crucial to provide confidence intervals or perform statistical tests to determine whether the improvements are statistically significant and not due to random chance. The current analysis lacks the necessary rigor to support the claims of performance enhancement.

### Questions
No specific question from me. But my concerns are majorly stated in the previous section.

### Soundness
2

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
5

### Summary
The paper addresses the challenge of detecting "hallucinations" in Large Language Models (LLMs). The study proposes a novel technique to improve hallucination detection by adding "noise injection" to intermediate layers of the model, creating an additional source of randomness during response generation.

### Strengths
- The paper touches a critical issue in current LLMs. Any progress in error detection is critical to the field.

### Weaknesses
 The paper presents some notable weaknesses in both the presentation of content and in aspects of the methodology and experimental design. Below are specific areas of concern:

- The review of related work is somewhat shallow. There is substantial literature on detecting hallucinations in models, yet this paper does not adequately differentiate its approach or clarify how it builds upon existing insights.
- All experiments are conducted on a single model, which limits the generalizability of the conclusions. Testing across multiple models would strengthen the claims.

## Intro:
- The term "hallucinations" is only briefly defined as instances where a model generates “plausible yet incorrect responses.” However, it remains unclear if this term includes all model errors or just those based on plausibility. The paper does talk about plausibility further, leaving the reader uncertain about what qualifies as a hallucination.
- You refer to figure 7  which is in the appendix. Core results should be presented in the main paper, and anything you talk about in the intro is definitely core. Note that reviewers are not required to read them but in your case it was fundamental to understand your results. This note is relevant for the rest of the paper as well.
- We empirically validate the hypothesis in Figure 7 (a) -> how exactly the figure validates your hypothesis? Readers need a step-by-step walkthrough to see how Figure 7(a) substantiates the hypothesis.

## Section 2:

- The definition of $f$ is a bit vague and as a results, the method as well. The model's output is not a function of all of its hidden states, because each hidden state $l$ is a function of the previous hidden state $l-1$. I think that maybe you could say that if you talk about the residual stream that sums all hidden states (because later you talk about mlp output), but it is very not clear at this point of reading.
- Because of that, it's not clear what happens when you replace $h_t^l$ with a noised version. Do you recompute $h_t^{l+1}$ to get a noised version or do you just noise the clean version? This needs to be clearly explained. If you add the noise to the MLP output which in turn simply goes to the residual stream, and you don't recompute the following MLPs in higher layers after adding noise, then this is just equivalent to add noise K times (where K are the number of layers you noised) to the residual stream, without significance the the specific layers that are noised, because the unembedding layer simply takes the residual stream after the final layer.

## Section 3:

- Table 2 lacks information on statistical significance, including standard deviations and the number of seeds used for experiments. Additionally, there is no indication of the dataset size.
- he statement, “This supports our intuition that incorrect answers are less robust to noise injection…” appears without prior context. While there is mention of hallucinations having higher entropy, there is no discussion that wrong answers may appear less after noise injections. Why does this happens?
- It was not clear to me why you need a separate section for GSM8K as experiments are later conducted across multiple datasets, making this section feel repetitive.

## Section 4:

The paper lacks a clear presentation of noise boundaries and statistical significance tests, which raises concerns about the reliability of findings. The difference between the proposed methods and baselines is small, and it is unclear how significant these differences are. Only Figure 4 provides such comparisons for GSM8K, while other datasets are not covered.

Some other typos etc.:
- Links to figures/equations are broken.
- Line 118: "**an** uncertainty metric"
- Line 122 sentence is not grammatically correct
- Line 289 ".,"
- Figure 7 caption: "Rest of setup up follows Figure 7 (b)" -> typo?

### Questions
- How do you extract the final answers from the long answer? How do you make sure it is always in the end? Do you do some sort of prompt engineering or few shot for this
- What is the acc of the model in greedy decoding?
- Why are the results on GSM8K are different in table 2 and 3? What is the difference in the setting? 
- "For each dataset, we select the temperature within T = {0.2, 0.5, 0.8, 1.0} which optimizes the model accuracy on this dataset" - on the validation dataset?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes enhancing the performance of hallucination detection by perturbing hidden unit activations in intermediate layers for sampling-based methods. Unlike existing approaches that measure uncertainty through prediction layer sampling, this work introduces noise to intermediate layer representations and combines this noise injection with prediction layer sampling to improve hallucination detection. Extensive experiments demonstrate the effectiveness of this method across various datasets, uncertainty metrics, and model architectures.

### Strengths
1. The motivation for introducing randomness in the hidden layer is intuitive and makes a lot of sense. The paper is well-written and easy to implement.
2.  The concept of perturbing intermediate representations to enhance the separability between hallucinated and non-hallucinated generation is overall innovative.
3. Extensive experiments are provided to demonstrate the effectiveness of noise injection in enhancinghallucination detection across various datasets and uncertainty metrics.

### Weaknesses
1. The performance improvement from noise injection is insignificant in most cases. As illustrated in Table 3, there is an insignificant increase in Predictive Entropy and Normalized Entropy, with the most notable improvement occurring only in the answer entropy of the GSM8K dataset. The reported increases are marginal, raising questions about the practical utility of the proposed method beyond specific scenarios.
2. The author argues that the effects of noise injection and prediction layer sampling are complementary. However, this claim is not strongly substantiated by the results shown in Figure 3. A Pearson correlation of 0.67 does not clearly indicate a complementary relationship between these two sources of randomness. Even without introducing noise, drawing entropy with temperatures T=0.5 and T=1.0 will show similar positive correlations. The correlation alone does not demonstrate that the two methods are leveraging distinct aspects of the model's uncertainty.
3. The author introduced additional hyperparameters $\alpha$, $\ell_1$ and $\ell_2$ to adjust the randomness of sampling. However, this comparison may be unfair, as performance could also be enhanced by optimizing parameters such as temperature T, top_P, and top_K. The introduction of new hyperparameters without a clear methodology for their optimization makes it difficult to assess the true benefit of the proposed approach compared to simply tuning existing sampling parameters.
4. Theoretical insight is limited in explaining why perturbations at the hidden layer are more effective than output layer sampling for self-consistency based hallucination detection methods. In my opinion, using a larger temperature is essentially the same as modifying the feature space to increase randomness. The paper lacks a theoretical framework to explain the mechanism by which hidden layer perturbations improve hallucination detection, and the comparison to temperature scaling is a valid concern that needs to be addressed.

### Questions
1. Is there any explanation why the performance is more significant only when combined with Answer Entropy?
2. I like the results shown in Table 4, but I would appreciate it if the author can proivde more experiments in other datasets, such as CSQA or TriviaQA.
3. I would like to see more perturbation based methods. For example, what will happen if we perturb the input query for those samping based methods?

### Soundness
2

### Presentation
3

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
The paper proposes to inject noise in the intermediate representations to enhance hallucination detection. The method is mainly tested on Llama2 on 4 different datasets.

### Strengths
- The paper flows well with detailed explanations.
- Ablation experiments are thorough and extensive.
- The problem of Hallucination detection is crucial in recent LLM studies.

### Weaknesses
 - My main concern is the soundness of the experimental results. Although the authors have shown the std of experiments in Figure 4, this is only shown for the dataset, GSM8K, which had the greatest improvement. However, considering that the gain in the other three datasets is relatively smaller, I would like to see the std values for other datasets too. Also, please conduct a t-test on the improvements.
- The authors tested their method mainly on Llama2-13B-chat. Although the experiment on Mistral has been provided in Table 6, this is only done on GSM8K. I would like to see a full table of experiments on other datasets.
- The message of Figure 2 (b) is somewhat unclear to me. I don't think the figures demonstrate better separability between non-hallucination and hallucination. Maybe a more fine-grained histogram would show a better picture?
- (minor) There are some grammatical issues in writing. I suggest using Grammarly or ChatGPT to refine the manuscript.
- (minor) There is no Figure 7 while the manuscript keeps referring to it. I'm assuming it should have been Figure 2, but please correct this.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work builds upon the idea that the variability of LLM answers to a question is most pronounced when the LLM does not know the correct answer. By perturbing the intermediate LLM layers, they show this gap in variability tends to increase, facilitating the detection of hallucinations.

The work is largely empirical. Most of the results are shown for the GSM8K dataset, where the method appears to work best. On three other datasets, results are still positive but much more contained. Table 3 would benefit from reporting standard deviations over the multiple runs. Right now it is not clear if the difference in entropy over CSQA, TriviaQA and ProntoQA is significant.

I appreciate the insight this work brings in terms of showing that the epistemic uncertainty induced by perturbing intermediate layers can provide complementary effects to the aleatoric uncertainty induced by last layer for the purpose of detecting hallucinations. However, considering the complications introduced - the method needs access to the intermediate layers of the model, it may be sensitive to the noise magnitude (the Appendix in this direction is not particularly extensive) and to which layers are perturbed - I wonder if the improvements are in fact worth the effort. 

I'd suggest the authors to provide a comprehensive evaluation across many datasets, including standard deviation of the results, to show that the method works robustly in multiple instances.

### Strengths
- Perturbing intermediate layers seems to increase the uncertainty gap between instances where the model is correct and where it is not.
- The authors make an effort in ablating their results, in particular to distinguish the noise effect induced by intermediate vs last layer.

### Weaknesses
 - Results seem significant on GSM8K, less so on the other datasets. Standard deviations are missing.
- It may be worth extending the analysis on the sensitivity to the noise magnitude to better gauge the robustness of the algorithm. In the main paper, the authors only use either no noise or noise magnitudes 0.01 and 0.05, and only for one dataset. In the Appendix, results for another dataset are presented, but at different noise magnitudes. It would be good to provide results for a sufficient amount of noise magnitudes and all datasets.
- The authors refer to Figure 7 multiple times throughout the text. I believe this is a type, as there is no Figure 7. Should this be Figure 2 instead?

### Questions
- The authors refer to Figure 7 multiple times throughout the text. I believe this is a type, as there is no Figure 7. Should this be Figure 2 instead?

### Soundness
2

### Presentation
3

### Contribution
2
