# Attention Speaks Volumes: Localizing and Mitigating Bias in Language Models

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
We explore the internal mechanisms of how bias emerges in large language models (LLMs) when provided with ambiguous comparative prompts: inputs that compare or enforce choosing between two or more entities without providing clear context for preference. Most approaches for bias mitigation focus on either post-hoc analysis or data augmentation. However, these are transient solutions, without addressing the root cause: the model itself. Numerous prior works show the influence of the attention module towards steering generations. We believe that analyzing attention is also crucial for understanding bias, as it provides insight into how the LLM distributes its focus across different entities and how this contributes to biased decisions. To this end, we first introduce a metric to quantify the LLM's preference for one entity over another. We then propose \name (Attention-based Targeted Layer Analysis and Scaling), a technique to localize bias to specific layers of the LLM by analyzing attention scores and then reduce bias by scaling attention in these biased layers. To evaluate our method, we conduct experiments across 3 datasets (BBQ, Crows-Pairs, and WinoGender) using \texttt{GPT-2 XL} (1.5B), \texttt{GPT-J} (6B), \texttt{LLaMA-2} (7B) and \texttt{LLaMA-3} (8B). Our experiments demonstrate that bias is concentrated in the later layers, typically around the last third. We also show how \name effectively mitigates bias through targeted interventions without compromising downstream performance and an average increase of only 0.82\% in perplexity when the intervention is applied. We see an average improvement of 0.28 points in the bias score across all the datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a simple and straightforward method for localizing and mitigating bias in large language models. The approach focuses on the attention scores associated with specific target words, allowing us to identify the layers where intervention is most effective. By scaling down the attention on these target words in the identified layers, the method can effectively reduce bias. Experimental results demonstrate that the proposed method significantly improves bias scores compared to baseline approaches.

### Strengths
This paper tackles the important challenge of mitigating bias and stereotypes in large language models. The proposed approach is simple, lightweight, and intuitive, yet it proves to be highly effective in the evaluated setting.

### Weaknesses
The setting explored in this paper is overly simplistic and may not reflect real-world scenarios. It is uncertain how the proposed method would generalize to more practical settings. For instance: (1) candidates may not be explicitly annotated or may even be absent in the text; (2) biased or stereotypical outputs may be more implicit than those examined; and (3) the model’s outputs can depend on candidates in more nuanced ways so suppressing attention may hurts this dependency modeling.

### Questions
1. Can the proposed method generalize to the settings where tokens corresponding to candidates are unknown or absent in the text? If not, is there any implication on the more general settings?
2. When the model's output requires the information of candidates in more nuanced ways, would the model still work?

### Soundness
3

### Presentation
3

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
This paper presents Atlas, a two-step approach to identifying and mitigating biases in LLMs when responding to ambiguous comparative prompts (i.e. asking the LLM to select one from two entities). The proposed approach first localizes the layers of transformers that contribute the most to biases, then reduces biases by scaling attention scores in these layers corresponding to tokens of entities. The paper shows that the proposed approach can effectively reduces biases while maintaining performance.

### Strengths
1. The paper studies one important problem, the findings presented might be of interest to a large number of audiences.

2. Analyzing the internal mechanisms of how biases emerges in LLMs seem novel.

3. The proposed approach seems to be effective according to the experimental results.

### Weaknesses
1. The motivation shall be stronger. Figure 1 only shows which layers obtain higher attention scores for entities instead of which entity will be biased. For example, some layers would assign more weights to "grandson" while others would assign more weights to "grandfather". It is not clear how this attention concentration directly translates to a bias towards one entity over the other. The figure needs to show a clear correlation between attention weights and the model's preference for one entity, rather than just showing where attention is focused.

2. For one entities, the paper only considers the first token of the entity for attention score computation, which might be problematic when the first token of two entities are the same (e.g., grand for grandson and grandfather). This simplification could lead to inaccurate attention score calculations, especially when the first token is not unique to the entity and the context surrounding the token is crucial for disambiguation. The method should account for the full entity representation, or at least consider multiple tokens, to ensure accurate bias localization.

3. While the intervention approach of scaling attention is straightforward, the sum of all attention weights will become less than 1. This could potentially disrupt the model's internal calibration and lead to unintended consequences, such as altering the model's confidence or introducing new biases. The paper should provide a more detailed analysis of how this scaling affects the overall attention distribution and model behavior.

4. The method needs to determine the scaling factor \lambda for each prompt, which makes it not quite usable in practice. Overall, it is hard to guarantee the LLM to generate unbiased output in general use cases. The need for prompt-specific tuning of \lambda significantly limits the practical applicability of the method. The paper should discuss how this parameter can be determined in a more automated and generalizable way, or at least provide guidelines for selecting appropriate values.

5. The experiments should include larger models such as Llama-70B.

6. The paper only considers two baselines, given that there are so many papers on mitigating llms' biases, more baselines results should be reported to better show the significance of the proposed approach. The lack of comparison with a wider range of state-of-the-art bias mitigation techniques makes it difficult to assess the true effectiveness and novelty of the proposed method.

### Questions
1. The introduction of the attention mechanism in section 2 should be polished, there are some errors that should be carefully addressed. 

2. Since this work focuses on comparative prompts, one factor that shall not be ignored is the oder of the two entities, the paper should add results when the two entities are swapped. Moreover, I think it would be more useful to report the average results of the two different orders.

3. For approach 1 in line 269, would not the absolute value be adopted?

4. In table 3, you reported the change ratio of the entity with the higher prob. I believe it would be better to report the ratio of each entity that is preferred to gain better insights on to what extend the bias issue is resolved.

### Soundness
3

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
3

### Summary
The paper presents a novel approach for identifying and reducing bias in LLMs when faced with ambiguous comparative prompts. The authors argue that bias often emerges due to how the attention mechanism distributes focus among entities, particularly in the later layers of the model. By analyzing attention scores, they localize biased behavior to specific layers and apply targeted interventions to mitigate bias without significantly affecting model performance. Experiments conducted across multiple datasets demonstrate that ATLAS effectively reduces bias while maintaining fluency in the model's responses.

### Strengths
1. This paper focuses on the internal bias in LLMs, which is a significant area of research.
2. This paper identifies bias by analyzing attention weights, which is reasonable.
3. Experiments demonstrate the effectiveness of the proposed methods.

### Weaknesses
1. The paper proposes two approaches: using the difference and using the most probable candidate. While the authors select Approach 2, they do not provide a detailed analysis of why it is superior to Approach 1. Specifically, the paper lacks a comparative analysis of the two approaches in terms of bias reduction efficacy, computational overhead, and impact on overall model performance. A more rigorous comparison, including quantitative metrics for each of these aspects, is needed to justify the choice of Approach 2.
2. The paper focuses solely on comparative biases between two entities, which limits the research scope considerably. Focusing on comparative biases may overlook the complex interactions and potential biases that arise among multiple entities. For instance, many real-world scenarios involve multiple entities (such as social groups, genders, ethnicities, etc.), where the manifestations of bias can be more intricate and diverse. Simply comparing two entities may fail to capture this complexity. The method's applicability to scenarios involving more than two entities is not explored, which is a significant limitation.
3. There is a writing error: "Table 4" in line 485 should be corrected to "Table 3."

### Questions
1. Could the authors provide a more detailed analysis of their choice of Approach 2? For instance, it would be helpful to compare the two approaches in terms of bias reduction, computational efficiency, and impact on model performance.
2. I would like the authors to elaborate on whether their method has the potential for extension to other bias scenarios, such as biases involving multiple entities. If so, how could this method be adapted to address these additional scenarios?

### Soundness
3

### Presentation
3

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
The paper addresses the critical issue of bias mitigation within LLMs, particularly examining how biases can emerge internally when processing comparative prompts. The proposed method, Attention-based Targeted Layer Analysis and Scaling (ATLAS), is designed to localize and reduce bias by adjusting attention scores in specific layers. Focusing on model-internal mechanisms rather than data-centric methods, ATLAS offers a model-agnostic approach. The authors present experimental results demonstrating that ATLAS performs effectively according to the newly introduced "bias ratio" metric and maintains fluency as measured by perplexity.

### Strengths
- This paper tackles a critical issue by examining bias at the model level and introduces a new method focusing on attention layers to localize bias, providing insights into where bias might occur within the model.
- ATLAS operates model-agnostic, making it broadly applicable across different LLMs.

### Weaknesses
 - The approach relies mainly on averaged attention weights, which may miss the complex interactions across tokens and layers, contributing to bias formation. This simplification could limit the method's ability to fully capture nuanced biases embedded in the model. Specifically, averaging attention weights across all tokens within a layer may obscure critical token-specific interactions that contribute to biased outputs. For instance, if certain tokens within a layer exhibit strong positive bias while others show negative bias, averaging could neutralize these effects, leading to an inaccurate assessment of the layer's overall contribution to bias.
- The evaluation centers on a newly introduced "bias ratio" metric, which could favor the specific method over more established metrics. The absence of comparisons to state-of-the-art (SOTA) bias mitigation methods and limited ablation studies further restricts a comprehensive evaluation of ATLAS’s effectiveness. The bias ratio metric, as defined, may not capture the full spectrum of bias, particularly if it is highly sensitive to the specific prompt formats used in the study. Without comparisons to established metrics like those used in the BBQ dataset or similar benchmarks, it is difficult to assess the generalizability and robustness of the proposed method.
- The binary selection setup constrains the method's applicability to broader, real-world scenarios where decision-making may involve multiple options or more nuanced judgments. This limitation could affect the generalizability of the results to other types of bias. The method's focus on binary choices may not translate well to situations where the model must choose from a larger set of options or where the decision-making process involves more complex reasoning and contextual understanding. This limits the practical applicability of the method in real-world scenarios.
- Using perplexity to assess response quality may be less effective in this context, as the setting requires only words as an answer rather than full sentences. A different metric that better captures the quality and appropriateness of these shorter outputs could provide more relevant insights into ATLAS’s impact on fluency. Perplexity, which measures the model’s ability to predict the next token in a sequence, may not be the most appropriate metric for evaluating the quality of single-word responses. A metric that assesses the semantic appropriateness or relevance of the chosen word would be more suitable in this context.

### Questions
- In terms of top/bottom-k layers, does "k" refer to specific layers (e.g., exactly the k-th layer) or all layers within the range of 1 to k?
- If tokenization affects initial entity tokens (e.g., “grandfather” becomes "grand" + "father"), how is attention managed for variations in token splits like “grandfather” vs. “grandson”?

### Soundness
2

### Presentation
2

### Contribution
2
