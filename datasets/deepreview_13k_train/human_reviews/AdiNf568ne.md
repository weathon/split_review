# Erasing Conceptual Knowledge from Language Models

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
We propose a comprehensive evaluation framework for concept erasure in language models, addressing the need for a holistic assessment of effective unlearning. Our framework centers on three critical criteria: innocence (complete knowledge removal), seamlessness (maintaining conditional fluent generation), and specificity (preserving unrelated task performance). These evaluation metrics naturally motivate the development of Erasure of Language Memory (ELM), a new method designed to address all three dimensions. ELM employs targeted low-rank updates to alter output distributions for erased concepts while preserving overall model capabilities including fluency when prompted for an erased concept. We demonstrate ELM's efficacy on biosecurity, cybersecurity, and literary domain erasure tasks. Comparative analysis shows that ELM achieves superior performance across our proposed metrics, including near-random scores on erased topic assessments, generation fluency, maintained accuracy on unrelated benchmarks, and robustness under adversarial attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors proposed to evaluate LLM concept erasure with innocence, seamlessness and specificity, and put forward Erasure of Language Memory (ELM) as a new erasing method which claims to exile in all these three aspects by integrating losses (i.e. erasing, conditionally fluency, and retention) specifically designed for each of them. ELM was tested on WMDP dataset and evaluated with multiple choice questions, perplexity and MTBench/MMLU to exhibit innocence, seamlessness and specificity respectively. Based on the results on Zephyr 7b, ELM, compared with RepNoise and RMU, achieves marginally higher performance in terms of innocence and specificity, while processing a larger advantage in seamlessness. A similar experiment was conducted about erasing the concept of Harry Potter from Llama2 7b, the result of which, instead, indicates noticeably better innocence, with marginally better seamlessness and specificity, than RMU and WHP. There is also an ablation study to verify the impact of the losses on the three desiderata, as well as a robustness experiment by luring the LLM to comply with the request about the erased concept using GCG to show that ELM responses are less gibberish than the baselines.

### Strengths
1. The overview picture about the two individual losses are helpful for understanding the design of ELM.
2. The idea of keeping the models' response seamless post removal of a concept is interesting.

### Weaknesses
1. Inconsistent and Incomplete Experiments & Non-significant Improvement: In the main experiment, comparisons with baseline methods are only made for Zephyr 7b and missing for the Mistral and Llama 3 models, making it hard to draw a convincing conclusion about the merits of ELM. Additionally, in the experiment about removing the concept of Harry Potter, RepNoise was replaced with another baseline WHP, and the target model is switched to Llama 2 7b. The experiment settings are not consistent with each other. The results in the two experiments are also telling different stories: in both cases ELM only shows clear advantage in one of the three desiderata, and its seamlessness in the former and innocence in the latter, but there lacks discussion about this difference.
2. Questionable Claim about Seamlessness: While seamlessness is definitely a desirable feather for concept erasure, measuring it with PPL is obviously insufficient. Based on the example responses in the main body as well as in appendix, responses post ELM are only less gibberish but not actually meaningful to make it acceptable seamless.
3. Questionable Novelty: Tackling concept erasure by combining losses designed for forgetting and retaining is nothing new. The baseline RMU, for instance, also has a forget and a retain loss, with the only difference being using cross-entropy or L2 distance. The fluency objective is relatively new, but it only seems incremental to the existing framework.
4. Poor Presentation: The section about probing and activation analysis, supposedly, is going to be interesting. However, Figure 3 is using a elusive legend and captions, making it impossible to relate the the analysis with the data in the figure.

### Questions
Most question are covered in the weaknesses outlined above, e.g. Why using such a inconsistent setup across experiments? Why so little comparisons? How to interpret the different improvement in different experiments?, etc. The authors are encouraged to include more results and explanations to alter my opinion on these weaknesses.

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
3

### Summary
This paper studies how to effectively erase corresponding knowledge from LLMs. The authors first propose three metrics (Innocence, Seamlessness, Specificity) to comprehensively measure the effectiveness of a knowledge erasure method. The authors claim that current erasure methods typically fall short in one or several metrics above.  Then, the authors propose a  method called the Erasure of Language Memory (ELM) that is motivated from the classifier-free guidance diffusion work to achieve more effective erasure performance on all three metrics.

### Strengths
1. The model unlearning/knowledge erasure problem is important and practical, as there are many cases that we want the LLMs to forget some targeted concepts.

2. The motivation in Eq. (3)-(5) is interesting and clear, which makes the method easy to follow.

3. The proposed metrics are comprehensive and practical.

4. The ablation studies in Section 5.3 are thorough.

### Weaknesses
I have some questions for the authors:

1. Regarding the Erasing Objective in Line 233-247, I think the form of probability function is somehow similar to the form of emulated fine-tuning/decoding-time alignment [1,2], which also manipulate the predicted probability distribution by multiplying a re-scale factor (though this factor is different in their works). Maybe the authors could add more discussion or comparison on these works to  make the contribution more clearer. Specifically, the re-scaling of the probability distribution in the erasing objective, while different in its specific formulation, bears a resemblance to how these methods adjust the logits. A more detailed analysis of the differences in the underlying mechanisms and the impact on the model's output would be beneficial. For example, how does the proposed method's manipulation of the probability distribution compare to the logit scaling used in [1,2] in terms of the resulting changes in the model's internal representations and its generalization capabilities?

2. Regarding the Conditional Fluency Objective, I am concerned about its necessity. As the Erasing Objective  is already included, why do we need this Conditional Fluency Objective? I would assume based on the Erasing Objective , the model can learn to generate fluent response by attempting to respond to the alternative concept $c_{+}$ even though the prompt is $c_{-}$. It is not clear why the model cannot learn to generate fluent text solely from the erasing objective. The authors should provide a more detailed explanation of why the erasing objective alone is insufficient for maintaining fluency, and what specific aspects of the conditional fluency objective address this gap. For instance, is it related to the autoregressive nature of the model, or is there a specific interaction between the erasing objective and the model's generation process that necessitates this additional objective?

3. In Table 1, why do you not perform experiments with RMU and RepNoice on other three LLMs? Also, the advantage of ELM compared with RMU seems to be limited. The lack of comprehensive experiments across all models for RMU and RepNoice makes it difficult to assess the generalizability of the proposed method. Furthermore, the relatively small performance difference between ELM and RMU raises questions about the practical significance of the proposed method. The authors should provide a more thorough analysis of the performance differences, including statistical significance tests and a discussion of the potential reasons for the limited improvement.

4. The authors should include a Ethics Statement section after the main text before references, as knowledge erasure is related to some ethical concerns.

### Questions
See the weakness part.

Typos and presentation errors:

(1) Line 51, "fine tune" -> "fine-tune"

(2) Line 243 and 244 ''..'' -> ``....''

(3) Line 288, \citet -> \citep

(4) Line 294, Llama3-7B -> Llama3-8B

(5) Table 3, the R-PPL of WHP should also be highlighted.

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
5

### Summary
This paper introduces a framework for erasing conceptual knowledge from language models, aiming to ensure that the erased knowledge is irretrievable while maintaining the model's general functionality and fluency. The authors propose the "Erasure of Language Memory" (ELM) method, which is designed to meet three criteria: innocence, seamlessness, and specificity.

### Strengths
The presentation is well-written and easy to follow. The proposed three criteria—innocence, seamlessness, and specificity—are particularly insightful.

### Weaknesses
1. The paper lacks a robust justification for using low-rank adapters. It claims that full fine-tuning may lead to overfitting, but it fails to provide comparative experiments to substantiate this claim. Demonstrating overfitting through empirical results would strengthen the argument.

2. The benchmarking is limited. While the paper focuses on multiple-choice tasks, it does not explore how the method performs on open-ended generation tasks, which could provide a more comprehensive evaluation of the model's capabilities.

3. In Table 1, the implementation of baselines such as RMU for models like Mistral-7B and Llama3-8B is missing. Why?

4. I appreciate the ablation study conducted in Section 5.3; however, the approach could be more rigorous. Rather than simply removing one component of the loss function as per Equation 12, it would be more insightful to vary the hyperparameters $\lambda_1, \lambda_2, \lambda_3$ to understand their individual and combined effects on the results. The author should also develop a framework to control those hyperparameters to achieve good tradeoffs/performance.

5. The accuracy of RMU outperforms ELM in the virology benchmarks in Figure 2. Why? Are there any specific explanations?

6. The range of attacks tested in Section 5.5 is limited. To demonstrate the robustness of their defense methods universally, it would be better to include a wider variety of adversarial attack methods. This would help validate the general applicability of the defense strategies against a broader spectrum of potential threats.

### Questions
See the Weakness

### Soundness
2

### Presentation
3

### Contribution
3
