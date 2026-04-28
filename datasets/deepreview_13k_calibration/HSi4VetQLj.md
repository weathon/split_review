# Improving Uncertainty Estimation through Semantically Diverse Language Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
Large language models (LLMs) can suffer from hallucinations when generating text. These hallucinations impede various applications in society and industry by making LLMs untrustworthy. Current LLMs generate text in an autoregressive fashion by predicting and appending text tokens. When an LLM is uncertain about the semantic meaning of the next tokens to generate, it is likely to start hallucinating. Thus, it has been suggested that predictive uncertainty is one of the main causes of hallucinations. We introduce Semantically Diverse Language
Generation (SDLG) to quantify predictive uncertainty in LLMs. SDLG steers the LLM to generate semantically diverse yet likely alternatives for an initially generated text. This approach provides a precise measure of aleatoric semantic uncertainty, detecting whether the initial text is likely to be hallucinated. Experiments on question-answering tasks demonstrate that SDLG consistently outperforms existing methods while being the most computationally efficient, setting a new standard for uncertainty estimation in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Semantically Diverse Language Generation (SDLG) to enhance uncertainty measurement by generating semantically diverse output sequences. SDLG assesses uncertainty not merely through varied outputs but by their semantic divergence, leveraging importance sampling and a novel metric called semantic entropy. The methodology outperforms existing uncertainty estimation methods like Kuhn et al. (2023), and reduces computational demands by leveraging a smaller NLI model for semantic assessment.

### Strengths
The paper proposes an innovative and effective method to quantify uncertainty in language models, addressing a significant challenge in NLG. The approach of considering semantic diversity rather than relying on traditional sampling methods for uncertainty estimation is both straightforward and sound. By integrating a smaller NLI model, the paper also makes strides in computational efficiency, making it practical for real-world applications. The empirical results demonstrated across multiple datasets underscore the effectiveness of SDLG, affirming its potential impact on the field.

### Weaknesses
 - Since the method relies heavily on the NLI model to assess semantic equivalence, any biases inherent in the NLI model could skew the uncertainty estimations. The paper lacks a discussion on how to handle or mitigate potential biases within the NLI models, which could affect the reliability of the uncertainty measurements. I recommend including a more comprehensive evaluation of how variations in NLI models might affect the uncertainty measurement.
- Also the dependency on an external NLI model that shares the same tokenizer as the language generation model could restrict the applicability of the method across different language models with varied tokenizers. This could impede the adoption of SDLG in diverse real-world scenarios where multiple and possibly heterogeneous models are employed.
- Due to space constraints, the current main paper does not include a detailed illustration of its scoring mechanism and how the specific token pairs are selected and replaced. I recommend reducing sections 2 and 7 or relocating parts of them to the appendix.

### Questions
1. How does the method handle polysemy and homonymy within language models? Given that words may have multiple meanings based on context, how does SDLG differentiate and handle these variations in semantic assessments?
2. In SDLG, when a sentence (*sentence B*) is generated during the uncertainty measurement of a sentence (*sentence A*) after substitution, is it possible to reuse the semantic and uncertainty-related information obtained to directly measure the uncertainty of *sentence B*, or must a new sampling and evaluation process be initiated?
3. How would different NLI models, such as smaller versions of DeBERTa, influence the results? Can the robustness of SDLG be maintained across different NLI models?
4. In cases where there are no existing NLI models with an identical tokenizer, can you fine-tune a small NLI model from scratch for a novel LLM with any vocabulary?
5. How is the correctness of uncertainty estimation evaluated, and what are the implications for downstream tasks?
6. Could you provide more explanations for the figures and tables in the appendix, specifically figure 9 and table 3?
7. Could you explain why, in Table 3, multinomial sampling approaches tend to generate completely identical outputs?
8. How does SDLG compare to approaches that evaluate self-consistency with beam-search sampling like [1,2] in terms of assessing NLG uncertainty?

[1] Wang, Xuezhi, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. "Self-consistency improves chain of thought reasoning in language models." arXiv preprint arXiv:2203.11171 (2022).

[2] Xie, Yuxi, Kenji Kawaguchi, Yiran Zhao, James Xu Zhao, Min-Yen Kan, Junxian He, and Michael Xie. "Self-evaluation guided beam search for reasoning." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to evaluate uncertainty in LLM generation by determining whether model samples are semantically equivalent. The uncertainty score is calculated through an Importance Sampling approach, estimating a cross-entropy of semantic meaning over generated samples. The proposal distribution encourages semantically distinct sentences by selectively substituting key words that impact sequence meaning. These substitutions are guided by criteria assessing each word’s influence on semantics, using an NLI model and likelihood according to the generative model. The method is evaluated on closed books QA tasks. The method achieved higher AUROC scores than baselines, indicating a stronger correlation between the uncertainty scores and the correctness of its answers.

### Strengths
- The paper provides a clear explanation of uncertainty estimation for LLMs, introducing a method to calculate semantic similarity in a simpler manner than existing clustering-based approaches.
- The use of Importance Sampling for generating semantically diverse outputs is a strong methodological choice and, in my view, the paper’s most significant contribution.

### Weaknesses
 - **Experimental Clarity**: The experimental section lacks clarity, particularly in explaining how ROUGE and BLEURT metrics were applied. The reference in L.409 (“in general...”) requires citation if it’s a general principle, and L.411-414 discussing AUROC are somewhat confusing, particularly the sentence “AUROC is used as a metric for classifying.” Specifically, the role of ROUGE and BLEURT in evaluating the *correctness* of the initial output sequence is not sufficiently separated from the method's *uncertainty* estimation. The explanation of how these metrics are used to classify outputs as correct or incorrect, and how this classification then relates to the AUROC calculation, remains unclear. The connection between the thresholding of ROUGE/BLEURT scores and the subsequent AUROC analysis needs further clarification. The sentence “AUROC is used as a metric for classifying” is particularly confusing, as AUROC is a measure of classification performance, not a classification method itself. The overall flow of the evaluation protocol is difficult to follow, hindering a clear understanding of how the uncertainty scores are validated.
- **Baselines and Related Work**: It is unclear why some relevant works, such as [1], are not included as baselines. Additionally, a recent paper [2] appears to be highly relevant (and also provides a clearer explanation of the evaluation setup). While the authors position their sampling method as complementary, the core contribution of the paper is uncertainty quantification, which is also the focus of the cited works. The absence of direct comparisons with these methods weakens the paper's positioning within the field. The argument that the sampling method is complementary does not justify the lack of comparison, as the final uncertainty score calculation differs significantly, including the use of semantic clusters, which is not a feature of the other methods.
- **Model Choice**: Restricting the analysis to a single model family (which is not among the most recent) slightly impacts the work’s soundness. Expanding the analysis outside OPT's scope would strengthen the findings and make them more generalizable.

### Questions
- See weaknesses.
- L.441: I found the paragraph about semantic cluster unclear. What does this mean? "Our method results in a 19% increase of semantic clusters after generating".

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a method to measure uncertainty in large language models (LLMs), Semantically Diverse Language
Generation (SDLG). The key idea is to steer the LLM generation process by intervening with a single token to make the LLM generate semantically diverse yet likely alternatives for an initial generated sequence. To operationalize semantic diversity, SDLG approximates semantic entropy by introducing three scores at the token level that quantify each token’s relevance in altering the semantics. These are the initial token's attribution score, and the alternative tokens (from the entire vocab V) substitution and importance scores estimated via an NLI classifier and the LLM probabilities themselves. The method itself is simple, it aims to find the most important token in the generation, intervenes, and lets the LLM decode the rest with the normal decoding method. 

The experimental on three QA datasets (TruthfulQA, CoQA, TriviaQA) show that SDLG outperforms prior methods including  multinomial sampling (SEM SE) (Kuhn et al., 2023) and diverse beam search (SE DBS ) (Vijayakumar et al., 2018).

### Strengths
Positive points include the following:

- The paper is clearly written and easy to follow.
- The simplicity of the method is appealing. 
- The evaluation setup closely follows prior work by [Kuhn et al. (2023)](https://arxiv.org/pdf/2302.09664) measuring AUROC on the same three datasets and with the same OPT models.
- The paper uses open-access LLMs (OPT family) as Kuhn et al., (2023) and replicates their results, with makes them comparable.
- Compared to Kuhn et al. (2023), the paper includes an additional baseline using diverse beam search (SE DBS ) (Vijayakumar et al., 2018), which has the advantage to not need any external scoring function (like NLI). 
- The observation that fewer samples of SDLG approximate the 10-generations well is interesting and in favor or the efficiency of the method. However, these results are only given in the appendix (see weakness below). 
- Computational cost implications are discussed in the paper (lines 446-461).

### Weaknesses
Weaknesses include the following:

- The new method relies on three scores, but their importance remains untested.
  -  The three scores are integral to the newly proposed method, but the paper lacks an ablation of the three scores (Ai, Sij , Iij ). The current evaluation uses a simple mean (line 426-428)  "we derive the final token score ranking by straightforwardly averaging the three individual token score". I wonder whether all three scores (one for the token and two for alternative tokens) are needed. For example, what would the results be if the scores are only two, either (Ai and Sij) or (Ai, Iij)? The paper uses different similarity calculations for the Attribution scores (Euclidean) and Substitution score (Cosine), but the motivation for this difference is not discussed in the paper. Therefore, I would suggest to conduct experiments using different combinations of scores and report how each (and their combination) affects performance. Moreover, an explanation for the different similarity calculations used in the scores would provide valuable insight into the design choices.

- NLI models are trained on the sentence level, the method relies on the prefix and current token to score for entailment/contradiction, but the generation so far is only partial. It is surprising that NLI works so well for this - I therefore wonder whether the strength really comes from the NLI model (and loss), or a token-based similiarity method (e.g. something as simple as word2vec distances) would be sufficient here. The paper does not empirically show that NLI is needed. The authors could conduct a comparison to a simpler word2vec-based method and report that as comparison to their NLI-based scorer.
- SE DBS is competitive with the proposed SDLG on TriviaQA (Table 1). This similar result is not sufficiently discussed in the paper. The examples in the appendix (Table 3) include only comparisons between SDLG and SE, but not DBS - To promote both baselines to the same level, adding examples for DBS and providing a detailed analysis of where and why SDLG outperforms DBS would strengthen the paper.

- Discrepancy in motivation and experimental evaluation. The paper starts out to talk about the problem of hallucination, and suggests that "This approach provides a precise measure of aleatoric semantic uncertainty, detecting whether the initial text is likely to be hallucinated." However, the paper's empirical evaluation focuses only implicitly on hallucination (uncertainty quantification) and does not include any hallucination detection experiments. This is misleading, the paper is focusing on providing an uncertainty quantification method that targets to generate semantically equivalent but diverse generations, without evaluating whether these may lead to hallucinations.  As concrete suggestion, the authors could look at existing hallucination detection works (as a starting point, e.g. [HADES dataset](https://aclanthology.org/2022.acl-long.464.pdf, code and data [available](https://github.com/microsoft/HaDes)).

- The results presented in the main text fall short and are poorly written. Results are mentioned without linking to result tables or figures. The reader has to infer  where evidence is given. For example:
  - Line 432-433: Discusses results of Table 2 in appendix, without refering to it. 
  - Line 441-442: Mentions results on semantic clusters, but I do not find where these can be found, nor how this increase is calculated. 
Moreover, there are interesting results in the appendix (like the impact on the number of generations), but these are not part of the main paper. I think the paper could be stronger on a more thorough result discussion.

- Finally, while using the same OPT models is a strong point, the paper could have included a more recent language model family (OPT is from 2022). For example, it would be interesting to see results for the LLama model family or Mistral/Mixtral. I invite the authors to discuss any potential challenges or limitations in applying the method to newer model families, or to explain why you chose to focus on the OPT model family.

### Questions
- Line 437-440 mentioned the improper semantic entropy. What is improper about the semantic entropy by Kuhn et al.? Have you described that in the paper?

- Example generations in Table 3 in the appendix: 
  - Can you elaborate on the example, why do you think do the SDLG ones lead to lower probs than MS typically? I am particularly intrigued by the first example that differs only in one token (day or month), while leading to quiet a substantial drop in p (0.793 -> 0.6x). What might explain this?
  - How different are SDLG generations from DBS sampling? Do you have examples?
  - Where do you think does the key advantage of SDLG come from, compared to DBS?

- Why is the 30b OPT model often worse in AUROC (Table 1) compared to the 13b model? Is this in line with Kuhn's findings?

Suggestions:
- Line 430-431 mention the importance of using starting subwords (not internal subwords). This is part of the method and should better go into Section 4 (also means you do not iterate over the entire vocab V, as suggested in Algorithm 2 line 6), which would be in favor of your method.
- When discussing results, link to actual result tables to provide evidence.
- Consider moving some of the interesting results from the appendix to the main text (e.g. number of generations). Why do you think fewer generations are better for your method?
- Algorithm 2 and 1 could benefit from a caption.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces Semantically Diverse Language Generation (SDLG) to generate semantically diverse yet likely output sequences, and quantify predictive uncertainty in LLMs, to alleviate hallucinations in LLMs. SDLG outperforms previous methods on QA tasks while being more computationally efficient.

### Strengths
* This paper proposes SDLR, which utilizes the NLI model not only for transforming the space of generated output sequences to semantic clusters but also for computing the contribution of every token to the final semantics.
* While not an expert in this field, the experimental results of SDLG show the effectiveness and efficiency compared with other baselines.
* Different from current methods relying on optimal sampling temperature, does not require hyper-parameter tuning as it controls the sampling.

### Weaknesses
 * The experimental evaluations are not overall enough. This paper mainly focuses on several QA tasks, but other tasks where hallucinations exist can be further explored.
* This paper uses OPT model family for experiments, while more common models like LLaMA, GPT can be investigated.
* SDLR uses an extra NLI model to compute the contribution of every token to the final semantics. Does this can be replaced by the attention score distribution?

### Questions
* Could you provide experiments on LLaMA, GPT model family?
* SDLR uses an extra NLI model to compute the contribution of every token to the final semantics. Does this can be replaced by the attention score distribution?

### Soundness
3

### Presentation
3

### Contribution
2
