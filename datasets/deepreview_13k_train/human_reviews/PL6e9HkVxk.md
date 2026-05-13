# ROOT DEFENCE STRATEGIES: ENSURING SAFETY OF LLM AT THE DECODER LEVEL

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
Large language models (LLMs) have demonstrated immense utility across various industries. However, as LLMs advance, the risk of harmful outputs increases due to incorrect or malicious instruction prompts. While current methods effectively address jailbreak risks, they share common limitations: 
1) Judging harmful responses from the prefill-level lacks utilization of the model's decoding outputs, leading to relatively lower effectiveness and robustness. 2) Rejecting potentially harmful responses based on a single evaluation can significantly impair the model's helpfulness.
This paper examines the LLMs' capability to recognize harmful outputs, revealing and quantifying their proficiency in assessing the danger of previous tokens. Motivated by pilot experiment results, we design a robust defense mechanism at the decoding level.
Our novel decoder-oriented, step-by-step defense architecture corrects harmful queries directly rather than rejecting them outright. We introduce speculative decoding to enhance usability and facilitate deployment to boost secure decoding speed. Extensive experiments demonstrate that our approach improves model security without compromising reasoning speed. Notably, our method leverages the model's ability to discern hazardous information, maintaining its helpfulness compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a defense mechanism. They train a classifier to guide the model to exclude certain unsafe words during decoding. They also integrate speculative decoding the expedite the process.

### Strengths
The paper is easy to follow. Discussions are thorough in the paper.

### Weaknesses
1. Details regarding the training the classifier are missing in main text. However, this is the main contribution of the paper.

2. What is the advantage of training the classifier compared to simply maintaining a list of unsafe words? Are there direct evaluations on the trained classifier or case study?

3. The results in Table 1 (main results) seem not demonstrate the effectiveness of the method. RDS achieves similar results to several baselines.

### Questions
Please refer to the weakness part.

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
4

### Summary
The paper introduces a jailbreak defense strategy (“Root Defence Strategies”—RDS) that makes use of a classifier applied at each step of generation to the next top k tokens to guide the generation towards only producing safe tokens. The authors integrate their method with speculative decoding strategies to make it faster. Their evaluation results across 5 jailbreak datasets and 5 models show early promise.

### Strengths
- LLM safety is a crucial topic, where developing strong defense strategies against jailbreaks can be a potentially highly valuable contribution.

- Addressing safety during the decoding stage is a promising approach for mitigating jailbreaks.

- Using a small-scale classifier during generation might point towards efficient decoding-time defenses.

- I like the authors’ choice of presenting preliminary exploratory experiments that motivate the developed method early in the paper.

### Weaknesses
While I find certain aspects of the paper interesting/promising, I believe that currently there are some severe methodological and presentation weaknesses that limit the overall contributions of the paper:

**Writing, clarity, and accuracy**

Although, as mentioned, I appreciate the structure of the paper, I find the writing and presentation very difficult to follow and often erroneous. Certain claims, choices, or statements are also made without clear foundations.

For instance, the sentence starting on line 111 refers to “previous studies”, but does not cite them.

Or on lines 195 to 198, the authors write about their motivating experiments presented in Figure 2 that it “illustrates that the classifier cannot accurately determine whether the output is harmful based solely on the model’s overall decoding…”, but even after multiple careful readings, I do not see how this statement can be derived from the experiment that only looks at certain tokens in the decoding. Perhaps the authors can clarify this point in their next revision. Further, they then use this conclusion to extrapolate onto current defense methods that act on the whole response of the LLM to judge if the response was safe, which I find methodologically questionable, as (i) the experiment was limited to the classifier used by the authors, and (ii) the experiment only covers the case where one looks only at the tokens in certain positions in the response.

Another grieving example is the paragraph under Table 3, which is aimed at conveying a key conclusion, however it is very unclear how the results imply that word-level alignment is the key problem and token-level corrections are the answer.

Mostly in the introduction, but also later on, the paper repeatedly makes the claim that response filtering approaches do not work because they introduce a single point of failure, and doing many classifications, such as in the proposed method, is more favorable. While in general I agree with the intuition, the paper does not seem to follow up on this hypothesis in its evaluation (or at any later point) to back it up with evidence.

The paper contains small errors, both in the use of language, citation formatting (citet vs citep), and technical “typos” (e.g., equation 5 should say argmin if my understanding is correct).

**Evaluation, Technical approach and contribution**

While the overall idea of addressing safety during the decoding stage on a token representation-level is promising, it is closely related to [1] and [2]. While [1] is cited and compared to in the experiments, [2] is omitted both from technical and empirical comparisons. Crucially, the technique of [1] is highly similar to the proposed technique of RDS, which warrants a closer discussion outlining the differences and highlighting in which aspects RDS would mean an improvement over [1]. Currently, I find the novelty introduced by RDS over [1] limited.

Further, certain technical choices are unclearly motivated and unconvincing. I understand that a linear model is (arguably) the fastest choice, however, it might be too weak for general use. To test this, perhaps more complex jailbreaks should have been evaluated where responses are made that may appear benign in the first few tokens (where the presented method seems to have stronger discriminative ability).

It is unclear why the linear classifier is applied on the first k principal components, and not on the whole representation. The choice of k is not tested either.

Crucially, the paper claims to introduce a faster method than competing methods, however, this solely depends on the integration with speculative decoding, as evidenced by the generation time experiment, where the presented method performs consistently as the slowest of all when speculative decoding is not applied. Here, for a fair comparison, speculative decoding should also be applied to the competing methods. Additionally, I believe that integrating the presented method with speculative decoding does not constitute a contribution, as it seems that the speculative decoding technique of choice was applied without any involved adjustment on top of the method.

I find the evaluation metric confusing and atypical. What is the rationale behind setting thresholds over the five samples and reporting only a binary score across the five samples responses? Why is the threshold set to 0.5 for refusal? Why not report just the average across the samples?

I think that evaluations on the Custom dataset should be highlighted and treated more carefully, as this is also the dataset that was used to develop the method and train the classifier.

Finally, my most important doubt over this paper lies in the promise of indiscriminate token-by-token classification. I see two key issues with this approach:

- It is slow even with a fast linear model, as shown even by the experiments of the authors themselves.

- The limitations of the classifier can severely limit the capabilities of the model during generation. This is currently also not evaluated well, as the evaluation solely focuses on jailbreak success and refusal, not evaluating the remaining utility in the models either in the content of the non-refused responses or on unrelated utility benchmarks (e.g., MMLU or TQA).

To summarize, I have certain reservations over the effectiveness of the presented technique and believe that the current evaluation does not explore scenarios that would be specifically difficult for this method to handle well enough.

### Questions
See my (implicit) questions in the weaknesses section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper finds that LLMs have the ability to identify whether their output is harmful during the decoding stage, and proposes a Root Defence Strategies (RDS) to select harmless candidate tokens based on the harmfulness score from the LLM. Speculative decoding is introduced to boost the decoding speed. The experiments show RDS achieves the best harmlessness and helpfulness trade-off, with only the "root" security (without further fine-tuning).

### Strengths
1. The paper is well written, and clearly expressed. 
2. The idea of using LLMs to discriminate the harmfulness of its own decoded tokens is novel and sounds interesting.
3. Table. 2 shows RDS do not increase the refusal rate of LLMs. It is a good merit in practical scenarios.

### Weaknesses
1. The results in Table. 1 suggest the previous methods like SafeDecoding and Self-Examination have corrected all of risks on harmfulness benchmarks, the saturation results would reduce the significance of the comparison and make it difficult to show the superiority of RDS. Can authors use more challenging benchmarks or less secure LLMs? It makes the results more distinguishable. 
2. RDS should be limited by the ability of base LLMs. If a worst LLM which has low discriminative capability of harmful content, I cannot guarantee the RDS is still better than other baselines.

### Questions
1. The performance of the classifier determines the effect of the defense strategy. But I cannot find any numerical indicators of classifier's performance. Is it comparable with LLaMA-Guard?
2. Is there any alternatives of classifier, instead of PCA?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces the Root Defense Strategy (RDS), a novel approach aimed at improving the security of Large Language Models (LLMs) at the decoding level. Instead of focusing solely on input (prefill-level defenses) or evaluating the entire response (response-level defenses), RDS assesses and corrects the generation process on a token-by-token basis. This step-by-step method adjusts harmful tokens in real-time, leveraging speculative decoding to maintain inference speed. The authors conduct experiments on five models, demonstrating that RDS effectively reduces compliance with harmful queries while preserving helpfulness and enhancing generation speed.

### Strengths
1. The paper presents a new defense mechanism at the decoder level, moving away from traditional input-based or whole-output defenses, offering a more granular and continuous risk assessment.
2. Experimental results demonstrate that RDS is a practical and efficient solution, as it enhances security without compromising speed or utility.

### Weaknesses
1. The writing could be improved, as there are inconsistencies between the figures and the content. For example, in Figure 2, the legend does not align with the text, making interpretation more difficult.
2. While the paper evaluates several LLMs, some models are outdated, and incorporating more contemporary models would offer better insights into the generalizability of RDS. Moreover, the evaluation lacks coverage of models with varying sizes, such as the Phi-3 series.
3. The paper provides insufficient detail on the implementation of the training process, particularly regarding how the model learns to detect different harmful token patterns.
4. The paper lacks a theoretical framework or deeper analysis explaining why the token-level corrections proposed by RDS are more effective than existing defense mechanisms.

### Questions
1. Could you provide some insights about why the token-level corrections proposed by RDS are more effective than existing defense mechanisms?
2. Is RDS consistent in handling different types of harmful queries? Does RDS show consistent defense capabilities across all categories of harmful queries (e.g., malicious instructions, adversarial prompts)?
3. How does RDS perform in multi-turn conversations?

### Soundness
2

### Presentation
2

### Contribution
2
