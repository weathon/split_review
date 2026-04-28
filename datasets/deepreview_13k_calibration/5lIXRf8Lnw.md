# Automatically Interpreting Millions of  Features in Large Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 6, 3

## Abstract
While the activations of neurons in deep neural networks usually do not have a simple human-understandable interpretation, sparse autoencoders (SAEs) can be used to transform these activations into a higher-dimensional latent space which can be more easily interpretable. However, SAEs can have millions of distinct latents, making it infeasible for humans to manually interpret each one. In this work, we build an open-source automated pipeline to generate and evaluate natural language interpretations for SAE latents using LLMs. We test our framework on SAEs of varying sizes, activation functions, and losses, trained on two different open-weight LLMs. We introduce five new techniques to score the quality of interpretations that are cheaper to run than the previous state of the art. One of these techniques, intervention scoring, evaluates the interpretability of the effects of intervening on a latent, which we find explains latents that are not recalled by existing methods. We propose guidelines for generating better interpretations that remain valid for a broader set of activating contexts, and discuss pitfalls with existing scoring techniques.co/datasets/EleutherAI/auto_interp_interpretations}{here}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduced five automated scoring methods to score the explanations of SAE latents, and discussed the shortcomings of existing scoring techniques. The paper also finds that SAE trained on nearby layers are highly similar, and provided actionable insights for practitioners to train wider SAEs instead of narrower SAEs to be efficient when there’s a compute constraint.

### Strengths
- Given the large sizes of SAEs nowadays and an increasing need for model explainability, automatically generating explanations of SAE latents efficiently is an important topic.
- The paper is well written, with ablations of design choices clearly described.

### Weaknesses
 - Format: There are no line numbers, and it's showing "Under review as a conference paper at ICLR **2024**" instead of **2025** at the top.
- The low correlation between different evaluation methods in Table 1 is concerning. Since the simulation method proposed in prior work is vetted and established, the new ones proposed in this work should at least have strong rank correlation (> 0.7) with it to prove that they work. Since this the scoring methods are the primary contribution in this paper, the authors should conduct more rigorous tests to ensure their validity. I would also encourage the authors to conduct experiments with ground truth explanations (e.g., SAE latents with known explanations found in prior work, or easily constructed an embedding model responding to a known concept/explanation), to make a stronger case in terms of the reliability of these new methods.
To add on, instead of correlation of the raw scores, it might make more sense to look at the "rank" correlations of different methods.
- The authors claim that the new methods are more efficient than prior scoring methods without actually quantifying the efficiency gain to support the claim. If efficiency gain is one of the highlights of these scoring methods, the authors should consider comparing runtime of different methods to support the claim.
- The author mention “Our large-scale analysis confirms that SAE latents are indeed much more interpretable than neurons, even when neurons are sparsified using top-k postprocessing.” in the abstract as one of the main findings, but the details cannot be found in the main paper but in the appendix. The authors should consider moving it to the main paper if this is one of the main claims.
- Reproducibility: The author mentioned a plan to open-source the project, but it's hard to evaluate the quality of their code for reproducibility purpose either since it's not provided as one of the supplementary files.

### Questions
- Missing a highly relevant work, "Explaining black box text modules in natural language with language models". How does their scoring method compare to the ones proposed in this paper?
- Can the authors explain  the negative correlation between the fuzzing score and intervention score in figure 4? If they are both useful scoring methods, why would the correlation be negative?
- Unlike the claim in the paper, figure 5 is still showing statistical alignment across layers. Can the authors provide evidence for semantic similarity? (e.g., compute explanation similarity across layers instead of the matrix statistics)

*Minor issues*
- The authors say “we introduced *five* new techniques” in the abstract, and “We addressed issues with the conventional simulation-based scoring and introduced *four* new scoring techniques” in the conclusions. The readers might get confused in terms of the number of methods actually introduced in the paper, if it’s five, please be consistent throughout the paper.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper builds an open-source automated pipeline to generate and evaluate natural language explanations for sparse autoencoder features with LLMs. The framework has been evaluated on various dimensions, including SAE size, activation function, loss, and LLMs. Five new scoring techniques are proposed. The paper finds that SAEs trained on nearby layers' the residual stream are highly similar. And they are also more interpretable than neurons.

### Strengths
- The open-source framework is comprehensive and valuable for large-scale SAE analysis. The experiments are well designed to illustrate the effectiveness of the proposed method.
- The metrics proposed in this paper provides more dimensions to evaluate the generated explanations, which would be valuable for the SAE community.
- Some of the findings are meaningful to the SAE community. For example, larger latent SAE learn more dataset-specific latents. The relations between different sampling approaches and the generated explanations. And the high correlations between latents at adjacent layers.

### Weaknesses
 - The method is a bit hard to understand for readers who are not familiar with SAEs. For example, how section 3.1 is related to 3.2? Would be more illustrative if a figure of the whole pipeline is provided.
- It would be more clear to provide a simple example of explaining the latents of SAEs. And even better if an example involves the whole workflow of this framework is provided.

### Questions
The framework proposed in this paper is a valuable tool for the SAE community. It provides an automated pipeline to generate and evaluate natural language explanations for sparse autoencoder features. However, the authors better consider to write a more accessible version for readers who are not familiar with SAEs, especially for section 3. It is a bit difficult to follow it.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates sparse autoencoders (SAEs), which project activation representations into a sparse high-dimensional latent space for interpretability. To automatically explain the large number of latent features, this paper proposes an LLM-based framework, explaining millions of latents across multiple models, layers, and SAE architectures. Four evaluation methods are proposed, including detection, fuzzing, surprisal, embedding, measuring the extent to which an explanation enables a scorer to discriminate between activating and non-activating contexts. Additionally, an intervention scoring is proposed to interpret a feature’s counterfactual impact on model output.

### Strengths
-	This paper focuses on an important research problem of SAEs producing a large number of latent features that require automatic explanations and evaluations.
-	Several evaluation metrics have been proposed to assess the generated explanations, comparing them across different explainer models, SAEs, and layers.
-	Some findings are interesting. For instance, sampling examples that are shown to the explainer model may increase the scores of features, highlighting a problem with current auto-interpretability evaluations. Experimental results suggest a priority for training wider SAEs on a smaller subset of residual stream layers. These may provide valuable insights for future research.

### Weaknesses
-	The writing and clarity of the paper could be improved. The current version is somewhat difficult to follow and understand. For instance, the rationale behind the choice of specific parameters, such as the context length for activation collection and the size of activating examples, is not adequately justified. These choices seem to contradict each other, especially given the potential impact on the identification of complex latent patterns.
-	Many observations are presented without in-depth analysis or further exploration. For example, in Section 3.1, the impact of context length and latent space size on activation data is mentioned, but a clear connection to the choice of 256 tokens for context length is missing. Similarly, in Section 3.2, the claim that “showing such short contexts to the explainer model hinders the correct identification of latents with complex activation patterns” seems to contradict the use of short activating examples with only 32 tokens. This raises concerns about the effectiveness of the proposed method in capturing the full complexity of latent features. In Section 3.3, while qualitative results for different sampling strategies are provided, the lack of a clear methodology for optimizing the sampling process leaves a gap in understanding how to best generate explanations. Furthermore, in Section 4.1, the statement “The imperfect correlations hint at either shortcomings of the scoring metrics or the fact that these metrics can measure different qualities of explanations” lacks clarity. A more detailed explanation of what specific qualities of explanations are measured by these automatic metrics and how they might differ is crucial.
-	The generated explanations largely rely on the prompts and explainer models. The paper does not sufficiently address the potential biases introduced by specific prompts and the limitations of the chosen explainer models. For example, how sensitive are the generated explanations to variations in prompt design? Are there inherent limitations in the chosen explainer models that might affect the quality or type of explanations generated? Without a thorough investigation of these aspects, it is difficult to assess the generalizability and reliability of the proposed framework.
-	While several automatic evaluations are compared, their effectiveness in accurately reflecting the quality of explanations remains unclear. The paper would greatly benefit from a human evaluation, even on a small scale, to validate the automatic metrics. This would provide a more reliable benchmark for assessing the quality of the generated explanations and understanding the strengths and weaknesses of each automatic evaluation method.

### Questions
-	Why is the context length of 256 chosen for activation collection? Is this value based on empirical selection?
-	Why is the activating example limited to only 32 tokens, given that short contexts may hinder the correct identification of latents with complex activation patterns?
-	What accounts for the differences in explanations between “randomly sampling” and “uniformly sampling”?
-	In Section 5, the statement that “if the explanation for latent α at layer j is very different from the explanation for the same latent at layer j + 1, this would suggest that our pipeline is inconsistent and noisy” raises a hypothesis. Can you elaborate on it?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents an open-source automated pipeline that uses large language models to generate natural language explanations for millions of features in Sparse Autoencoders (SAEs), addressing the challenge of manual interpretation. It introduces five efficient scoring techniques, including intervention scoring, and demonstrates that SAEs are more interpretable than neurons, offering insights into semantic similarity across model layers.

### Strengths
- The scale gets improved from previous sota.
- This work lies in an interesting direction.

### Weaknesses
 - This work did not compare the new evaluation metric with the previous evaluation metric (https://openai.com/index/language-models-can-explain-neurons-in-language-models/) in a solid form. Having similar conclusions as previous approach should not serve as a solid evidence that the new metric is as good as the previous evaluation metric.
- Comparing SAEs in adjacent layers (1) lacks support of motivation and (2) is not well supported. See Questions for details.
- The presentation is poor: readers can not capture the main contribution of this paper with a normal reading flow. The contribution of this work seems to be concentrated on a new evaluation metric, but Section 5 cuts in to discuss about behaviors of the behaviors of SAEs. I would strongly recommend to reorganize the paper to one single claim, with evidence from both sides supporting it.

### Questions
1. How is the correlation of the proposed evaluation metric with the original metric?
2. How is the efficiency of the proposed evaluation metric compared to the original metric?
3. Previous work (https://transformer-circuits.pub/2023/monosemantic-features) has already shown SAEs have more interepretable features than neurons. What's the purpose of validating this result?
4. Why comparing SAEs in adjacent layers? (Why is it interesing?)
5. How is comparing SAEs in adjacent layers related to your evaluation metric?
6. Are there any prior work that supports your method in evaluating the SAEs in adjacent layers?

### Soundness
2

### Presentation
1

### Contribution
2
