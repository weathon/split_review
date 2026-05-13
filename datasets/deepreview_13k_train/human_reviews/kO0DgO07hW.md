# Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Large Language Models (LLMs) generating unsafe responses to toxic prompts is a significant issue in their applications. While various efforts aim to address this safety concern, previous approaches often demand substantial human data collection or rely on the less dependable option of using another LLM to generate corrective data. In this paper, we aim to take this problem and overcome limitations of requiring significant high-quality human data. Our method requires only a small set of unsafe responses to toxic prompts, easily obtained from the unsafe LLM itself. By employing a semantic cost combined with a negative Earth Mover Distance (EMD) loss, we guide the LLM away from generating unsafe responses. Additionally, we propose a novel lower bound for EMD loss, enabling more efficient optimization. Our results demonstrate superior performance and data efficiency compared to baselines, and we further examine the nuanced effects of over-alignment and potential degradation of language capabilities when using contrastive data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper provides a way for LLMs to respond safely to toxic prompt in the SFT stage without requiring RLHF
and also improves upon prior results by using much less safety relevant data and only require easily available unsafe responses to toxic prompts. A novel EMD based loss is introduced along with an optimizable lower bound.

### Strengths
- Very less safety-related samples are required to get safe LLMs
- safe answers are not needed which reduces human effort.
- standard evals are unaffected after training.

### Weaknesses
Multiple works question the generalization of current safety training by jailbreaking them [1, 2, 3]. In such a scenario, reducing the number of samples for safety without showing jailbreaking attempts puts a question on the practical applicability of this work. 
It would be great to understand how the proposed method generalizes and performs under jailbreaking. I would encourage the authors to explore [3] and try out simple jailbreaking attempts, if needed.

A proper study using safe examples, safe examples + unsafe examples (EMD), and unsafe examples (EMD) (with various sample sizes) to train the model and then using various jailbreak attacks on the LLM to showcase the robustness of the training is required. The overalignment issue pointed out in the paper is a good start.
Results of this experiment:
- Empirically proves the lack of need of safe examples that require costly human annotations.
- We already know that training on safe examples only does not generalize that effectively, this can provide further conclusions.
- Experiments with various sample sizes can answer questions like: lesser #unsafe examples vs more safe examples.

### Questions
<See weaknesses>

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses a critical issue in the use of Large Language Models (LLMs)—the generation of unsafe responses to toxic prompts. Traditional methods for mitigating this problem often involve extensive human annotation or the generation of corrective data from other LLMs, which are costly and less reliable. The authors propose a novel method called Toxicity Avoiding Supervised Fine Tuning (TA-SFT), which minimizes the need for large safety-related datasets by utilizing a small set of harmful responses as training data.

### Strengths
1.Data Efficiency: The method achieves high safety levels using only 0.5% of the safety-related data required by traditional methods, making it a cost-effective solution.

2. Innovative Use of EMD Loss: The use of EMD as a semantic penalty term in loss functions is novel and effectively discourages the generation of unsafe responses, as it considers semantic similarity.

3. Broad Evaluation: The paper includes extensive evaluation across several LLM architectures (e.g., Llama 7b, Llama 13b, Mistral 7b) and different safety and response quality metrics, demonstrating robustness and generalizability.

### Weaknesses
Formatting and Expression Issues:

There are several formatting and expression problems throughout the manuscript. For instance, in line 129, the first occurrence of "Negative Log-Likelihood" requires a citation. In line 120, the introduction of two subscripts needs clarification, even though I can understand it. Additionally, there are multiple instances where punctuation is missing at the end of equations. Lines 248-253 contain incorrect citation formats. Furthermore, some symbols are used without clear definitions. Overall, the manuscript has numerous formatting and expression issues that would benefit from a thorough review by the authors.


Complexity of EMD Computation:

Although EMD improves model safety, it can be computationally intensive. The paper introduces a lower bound to make it tractable, but this might limit scalability for very large datasets.


Limited Over-Alignment Solution:

While the paper identifies over-alignment, it does not fully resolve the issue. Models still show increased refusal rates for benign prompts as training progresses, suggesting room for improvement in managing over-alignment.


Dependence on Specific Safety Benchmark:

The model’s performance is largely benchmarked on safety-related datasets specific to toxic prompts. Its effectiveness in real-world applications or against evolving types of toxic input remains untested.



Contrastive Data Effect:

The inclusion of AI-generated contrastive samples caused unexpected degradation in response quality, raising concerns about the method's resilience to noise and synthetic data.

Finally, I acknowledge the innovative contributions of this work. Should the authors adequately address the identified issues, I would be inclined to reevaluate my assessment positively.

### Questions
See Weaknesses.

### Soundness
3

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
3

### Summary
This paper proposes a method to improve safety in large language models (LLMs) by utilizing a small, easily obtainable set of unsafe responses. Unlike approaches relying on extensive human feedback or corrective data from other LLMs, this method applies an Earth Mover Distance (EMD) based semantic loss to guide the LLM away from generating unsafe responses. Additionally, the paper proposes a novel lower bound for EMD to optimize efficiency. Experiments with multiple LLM models demonstrate improved safety and response quality with reduced data requirements compared to baselines. The method also addresses over-alignment issues that often arise with refusal-based safe responses.

### Strengths
- Data Efficiency: The method requires minimal safety-related data, making it cost-effective and accessible. The use of EMD loss may be a reasonable way to conduct alignment based on the token semantics, rather than only on the output.
- Semantic Loss Innovation: The application of EMD-based semantic loss introduces a novel, context-sensitive approach to penalizing unsafe responses. 
- Maintained Response Quality: The approach maintains response quality across reasoning and conversational benchmarks.

### Weaknesses
 - When calculating the EMD loss, the entire distribution of the LLM vocabulary is considered. However, there are also a lot of tokens in the harmful responses that may not be harmful if treated separately. I wonder whether maximizing the distance would result in undesirable outcomes that affect the original capability of LLM. If so, would first extract harmful keywords from the responses and only calculate the EMD loss using those tokens help?
- If the number of safety related QA pairs is limited, could the performance of SFT be improved by simply upscaling the loss for safety related QA pairs, or through oversampling?
I will consider raising the score if the authors help me with those concerns.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an EMD penalty term to prevent LLM from generating harmful information. The function of this penalty term is to make the probability distribution of tokens generated by LLM in the case of toxic prompts far away from the probability distribution of tokens in harmful responses dataset. When used for safety alignment, this penalty term allows SFT not to rely on a large number of human-collected SFT datasets while achieving a comparable or even better performance. And it will not cause the problem of over-alignment.

### Strengths
(1) This paper takes a novel approach by focusing on the perspective of distancing from harmful responses, differing from previous methods that directly align responses. 

(2) This paper takes a novel approach by focusing on distancing from harmful responses, which differs from previous methods that directly align responses. Experimental results indicate that this method achieves comparable or even superior performance using a dataset size significantly smaller than that of previous methods, demonstrating the effectiveness of the approach.

### Weaknesses
 (1) A detailed explanation is required for how the probability distribution represented by P (·|w<t−1) in line 186 of the paper is obtained. After reading the paper, I don't understand what kind of probability distribution it is.

(2)The paper discusses that good performance can be achieved with a small safety-related dataset. So, would increasing the dataset size lead to even higher performance?

### Questions
see weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
