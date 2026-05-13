# Calibrate to Discriminate:Improve In-Context Learning with Label-Free Comparative Inference

- Decision: Reject
- Scores: 3, 6, 3

## Abstract
While in-context learning with large language models (LLMs) has shown impressive performance, we have discovered a unique miscalibration behavior where both correct and incorrect predictions are assigned the same level of confidence. We refer to this phenomenon as \textit{indiscriminate miscalibration}. We found that traditional calibration metrics, such as Expected Calibrated Errors (ECEs), are unable to capture this behavior effectively. To address this issue, we propose new metrics to measure the severity of indiscriminate miscalibration. 
Additionally, we develop a novel in-context comparative inference method to alleviate miscalibrations and improve classification performance. Through extensive experiments on five datasets, we demonstrate that our proposed method can achieve more accurate and calibrated predictions compared to regular zero-shot and few-shot prompting.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates a phenomenon called "indiscriminate miscalibration" in LLMs during in-context learning, where models assign similar confidence levels to both correct and incorrect predictions. The authors propose new metrics to measure this issue and introduce a label-free comparative inference method that includes unlabeled samples in prompts to improve calibration and classification performance. The authors evaluate their approach on 5 datasets using various Llama models and demonstrate improvements in both classification metrics (F1 score, accuracy) and calibration metrics.

### Strengths
1. The paper identifies an interesting and important problem regarding LLM calibration
2. The proposed label-free approach is novel and doesn't require labeled examples
3. The method appears to improve both classification performance and calibration metrics

### Weaknesses
1. The experimental design has several limitations that raise concerns about the generalizability and robustness of the results. Firstly, the evaluation is only conducted on Llama family models, which may not be representative of other language models or architectures. Secondly, the 5 datasets used are relatively standard classification tasks, and it is unclear how the method would perform on more complex or challenging datasets. Furthermore, the maximum of 500 test samples feels limited for a robust evaluation, and the lack of ablation studies examining the impact of different comparison sample selection strategies makes it difficult to disentangle the effects of different components of the method.

2. The paper lacks a rigorous theoretical analysis of why the comparative inference approach works. The assumptions made in Section 4.1.2 about bias averaging (Equation 3) are not well justified, and it is unclear what underlying principles drive the improvement in calibration and classification performance. A more thorough exploration of the theoretical foundations of this method would be necessary to fully understand its implications and limitations.


3. The comparative inference method increases the inference cost significantly due to multiple forward passes, which may be a concern for real-world applications where computational resources are limited. Moreover, the post-hoc calibration requires validation data, which may not be readily available for open-ended generation tasks, limiting the method's applicability in these scenarios.

### Questions
1. Why do you believe the bias averaging assumption in Equation 3 holds? Can you provide theoretical or empirical evidence?

2. How do you select comparison samples in practice? Is there a strategy better than random selection?

3. What is the computational overhead of your method compared to standard few-shot prompting? Please provide detailed timing analysis.

4. How sensitive is the method to the choice of comparison samples?

5. Can you comment on the method's impact on open-ended text generation and language modeling tasks?

### Soundness
2

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
5

### Summary
This paper addresses the problem of indiscriminate miscalibration in Large Language Models (LLMs). The authors introduce a new calibration metric called Discriminate KL Divergence (DKL) and propose an in-context comparative inference method -- a label-free approach termed LF -- to mitigate this issue. They validate their method on five classification tasks using five models from the LLama family, employing both traditional and their newly proposed metrics.

### Strengths
1. The idea of using comparative inference to improve confidence calibration in LLMs is novel.
2. Extensive experiments demonstrate the effectiveness of their method.
3. The paper is clearly written and easy to follow.

### Weaknesses
1. Lack of in-depth analysis on why comparative inference alleviates indiscriminate miscalibration. It remains unclear how such a comparison triggers the LLM to output discriminative confidence. The authors should explore the underlying mechanisms more thoroughly, perhaps by analyzing the attention patterns or internal representations of the model when processing comparative inputs versus single inputs. This could involve techniques like probing or representational similarity analysis to understand how the model's internal states differ. Furthermore, it would be beneficial to investigate if the effectiveness of comparative inference is consistent across different model architectures and sizes, as this could provide insights into the method's generalizability.
2. Unfair comparisons in the experiments. For instance, the 0-shot-agg LF-ICL requires ensembling 10 inferences to produce one result, resulting in 10 times the computational cost compared to the 0-shot ICL baselines. While this is not a major issue since 0-shot LF-ICL still outperforms 0-shot ICL, including a 0-shot-ensemble ICL baseline would provide a more rigorous comparison. It is crucial to control for the computational cost when comparing different methods. The authors should also consider reporting the inference time for each method to provide a more complete picture of the trade-offs involved.

### Questions
1. Regarding the experiments on post-hoc calibration, the authors claim that "comparative inference with post-hoc calibration can be combined with few-shot prompting" to further improve performance. Do the authors have experimental data to support this claim?
2. The LF-based methods do not show a robust improvement in terms of Expected Calibration Error (ECE) in the post-hoc calibration experiments. Why do the authors not present results using other metrics like the DKL they have just proposed?

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
4

### Summary
The paper studies the confidence calibration of large language models (LLMs) on classification tasks. The authors observe the indiscriminate miscalibration behavior of LLMs where accuracy is similar regardless of whether confidences are high or low and that metrics like ECE fail to capture this behavior accurately. The authors propose a KL divergence-based metric that can better capture this behavior and propose a post-hoc label-free calibration method to alleviate indiscriminate miscalibration.

### Strengths
The indiscriminate miscalibration observation, where both correct and incorrect predictions are assigned the same level of confidence, is quite interesting, as previous studies predominantly reported findings similar to Figure 1(b). Notably, the proposed method does not require labels, which is commendable. Experiments were conducted on five different LLMs of varying sizes which is also laudable.

### Weaknesses
 **Key Related Works Missing**: One of my primary concerns is that the paper does not cite several key works in the calibration literature that are highly relevant, including:

1)	Abbas, M., Zhou, Y., Ram, P., Baracaldo, N., Samulowitz, H., Salonidis, T., and Chen, T. Enhancing in-context learning via linear probe calibration. In Proceedings of The 27th International Conference on Artificial Intelligence and Statistics, pp. 307–315, 2024.

2)	Zhixiong Han, Yaru Hao, Li Dong, Yutao Sun, and Furu Wei. Prototypical calibration for few-shot learning of language models. In Proc. of International Conference on Learning Representations, 2023.

3)	Zhongtao Jiang, Yuanzhe Zhang, Cao Liu, Jun Zhao, and Kang Liu. Generative calibration for in-context learning. In Houda Bouamor, Juan Pino, and Kalika Bali (eds.), Findings of EMNLP 2023.

4)	M. Shen, S. Das, K. Greenewald, P. Sattigeri, G. Wornell, and S. Ghosh. Thermometer: Towards universal calibration for large language models. ICML 2024.

These papers focus on calibration for LLMs and could also serve as valuable baselines. While the first three aim to enhance LLM performance, particularly in the in-context learning (ICL) setting, 1) Abbas et al. (2024) and 4) Shen et al. (2024) notably also tackle the issue of Expected Calibration Error (ECE) metric. Thus, I respectfully disagree with the authors’ statement in lines 358-359 that “While such methods can decrease ECE, it does not help with improving model classification performance,” as these papers address both aspects.

**Limited baselines**: The baselines are too limited, and the papers I mentioned earlier should be included as valid baselines. Even though the authors claim that combining their method with existing post-hoc calibration methods would lead to better results, these results should be shown to validate this claim. The existing post-hoc calibration methods also compare with the raw ICL method, which makes them valid baselines.


**Limited evaluation**: The dataset selection here appears quite restricted compared to related studies. For example, Batch Calibration (Zhou et al., 2023) utilizes 13 classification datasets, while Generative Calibration (Jiang et al., 2023) uses 12. Using a wider range of datasets would lead to a more thorough assessment and strengthen the study.

**Unfair comparison**: If we use two additional input samples in the prompt (as mentioned in lines 415-416), the zero-shot effectively becomes 2-shot, while three-shot becomes five-shot. I know we are not providing labels for the 2 additional samples but still the comparison of 0-shot/3-shot/10-shot LF-ICL with 0-shot/3-shot/10-shot ICL is a bit unfair since adding additional samples provides additional context/information.

**Reproducibility**: The authors did not provide the code to reproduce the results, which raises concerns about reproducibility.

**Suggestions**: 

Previous studies have shown that ICL is sensitive to the choice of demonstrations used in the few-shot setting. It would be good to report standard deviation across different choices of the test demonstrations in Table 1 and Table 2, as done by (Contextual Calibration, Zhao et al., 2021), (Linear Probe Calibration, Abbas et al., 2024), and (Prototypical calibration, Han et al., 2023) etc.

In Table 1, it would have been nice to see the results for the 3 shot-agg and 10 shot-agg as well.


**Suboptimal Writing**: The writing in the paper is quite suboptimal, containing numerous grammatical errors and typographical errors. Here are some suggestions for improvement:

Lines 027-228: Redundancy: ‘LLMs’ abbreviation defined again. It was already defined in the abstract.

Lines 094-097: Several grammatical issues in the sentence

Lines 135-136: grammar/typo: use ‘accuracies are’ or ‘accuracy is’. Moreover, "regardless whether" should be "regardless of whether". It is better to use 'LLM' abbreviation as defined earlier in the abstract. 

Line 164: grammar/typo: use 'an LLM' instead of 'a LLM'.

Lines 195-197: typo/grammar: "dataset" should be pluralized as "datasets.". typo: add space in the beginning of the sentence (i.e. between '...datasets.' and 'A smaller...').

Lines 234-236: grammar/typo: "incapable for describe" should be "incapable of describing"

Lines 268-269: grammar/typo: "it has trouble" should be "they have trouble": The subject "LLMs" is plural, so it should be followed by "they" rather than "it."

Lines 270-272: grammar/typo: "without trained on them" should be "without being trained on them". typo/grammar: "asking LM" should be "asking the LLM".

Lines 289-291: suggestion for better readability: change "Notice that even we are using words like ‘comparing’" to "Note that even though we use words like ‘comparing’". suggestion for better readability: Change "and sample 3" to "or sample 3" to improve readability.

Line 296: typo/grammar: "is because of" → "is that, due to".

Line 298: The phrase "where one would expect" is confusing in context; replacing it with "one would expect" directly makes it clearer.
Line 302: suggestion: "bias to the samples" → "bias toward samples".

Line 303-304: suggestion: "degradation of inference performance on later input samples" → "degradation in inference performance for samples appearing later in the input".

Line 341 (Figure 5): typo/grammar: "across 5 dataset." should be pluralized as "across 5 datasets."

Lines 346-347: grammar/typo: "F1 score and accuracy is also improved" should be "F1 score and accuracy are also improved."

Line 348: grammar/typo: "Though" → "Although".

Lines 367-368: typo: "referencs" → "references".

Line 485: typo/grammar: "restricts" instead of "restricted".

### Questions
**Clarification regarding Figure 1 setting**: I am not able to understand the reason behind the difference in observations between Figures 1(a) and 1(b). Why do they behave differently? What distinguishes the experimental settings in each case—is it the use of different datasets, or some other factor? These are important questions, and an apples-to-apples comparison is essential for clarity.

**With-labels version**: How would the method perform if we included labels for the 2 additional input samples? Would adding labels increase/decrease the performance? If it improves, by how much? This would perhaps be an interesting study.

### Soundness
2

### Presentation
3

### Contribution
2
