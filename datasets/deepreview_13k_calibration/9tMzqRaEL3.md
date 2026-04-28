# Exploring How LLMs Capture and Represent Domain-Specific Knowledge

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
We study whether Large Language Models (LLMs) inherently capture domain-specific nuances in natural language. Our experiments probe the domain sensitivity of LLMs by examining their ability to distinguish queries from different domains using hidden states generated during the prefill phase. We reveal latent domain-related trajectories that indicate the model's internal recognition of query domains.  We also study the robustness of these domain representations to variations in prompt styles and sources. Our approach leverages these representations for model selection, mapping the LLM that best matches the domain trace of the input query (i.e., the model with the highest performance on similar traces). Our findings show that LLMs can differentiate queries for related domains, and that the fine-tuned model is not always the most accurate. Unlike previous work, our interpretations apply to both closed and open-ended generative tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper makes the observation that the hidden states from autoregressive LLMs can separate data from different domains using the mean and variance of the activations. Using this property, a classifier is trained to predict the domain of the input from the hidden states and then route the example to a corresponding (domain specific) model.

### Strengths
- The observation that domains can be separated in the activation space by autoregressive LMs but not masked LMs (e.g., Deberta) is quite interesting. (However, I have an alternative explanation below that should be tested.)
- The idea of looking at the traces across layers is useful.

### Weaknesses
 - Important details are missing regarding the methods and the experiments. （See questions below)
- The main claims need further evidence:
    - Figure 2 shows that Deberta doesn’t show a separation as other autoregressvie LLMs. But it’s also a much smaller model (86M vs >2B). It’s possible that such separation only shows in larger models. It’s good to test on an autoregressive LM of similar size such as GPT2.
    - The domain separation on MMLU is clear. However, when incorporating multiple datasets in Figure 2, it appears that math and medical domains (the green and blue lines) aren’t well separated (e.g., MedMCQA and GSM8k). Also, mean separation is not shown.
    - For the example routing results, almost all variation comes from the MATH and GSM8k dataest. More analysis would be helpful. E.g., the general performance on MATH is fairly low; how large is the dataset and what’s the standard error? What domains are predicted?
    - Also, I don’t quite understand the routing result. Is the idea to route each example to a different domain classifier? But why would examples from math datasets (say GSM8k) benefit from say a medical domain model?

Typo:
133: dim -> dimension

### Questions
- Equation 1: A is undefined. If A is the output of the normalization layers, shouldn’t the mean be always zero? Also, are the LLMs tested using the same type of normalization (or architecture)?
- Which LLM does the hidden states come from in Table 2?
- 379: why finetune on emotional data?
- 388: Are the Phi-3 models the finetuned models in step 1?
- 392: In step 4, what’s the input features to the MLP layer? Is it concatenated hidden states of all layers of the last token? But then, how do you change the number of layers; maybe it’s a sum of the hidden states of all layers? 
- What is LLM sequence classifier?

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
The paper investigates how Large Language Models (LLMs) capture domain-specific nuances by analyzing hidden states during the prefill phase. The authors introduce the concept of "latent domain-related trajectories," which reveal domain sensitivity. They claim that these trajectories provide a robust signal for domain-specific tasks and model selection, leading to improved performance in cross-domain generalization tasks like legal, medical, and mathematical reasoning.

### Strengths
* Originality: Proposes a novel method to use hidden state trajectories for domain-specific model selection.
* Quality: The experiments are comprehensive, covering various architectures and tasks.
* Significance: Potential utility in improving model selection.

### Weaknesses
 * Clarity: The writing is not engaging, making the paper hard to follow.
* Justification: The rationale for why these hidden state patterns indicate domain sensitivity is weak.
* Generalizability: Limited applicability beyond the datasets studied, as acknowledged in the limitations.
* Interpretability: It’s unclear how this work significantly enhances our understanding of LLM behaviour or interpretability.r

### Questions
* Can you elaborate on why the observed hidden state patterns conclusively indicate domain-specific understanding?
* How do you envision this approach being practically used, given the need to process queries through multiple models before selection?

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
4

### Summary
This paper presents quite an intriguing investigation into how LLMs encode domain-specific knowledge. The authors have undertaken a comprehensive study examining hidden state patterns during the prefill phase, introducing what they've termed "latent domain-related trajectories." Their experimental work spans multiple architectures - Gemma-2B, Phi-3-mini-3.8B, Llama2-7B, and Mistral-7B - and demonstrates rather fascinating patterns in how these models process domain-specific queries. They've shown that hidden states can serve as reliable indicators of domain understanding, leading to a 12.3% improvement over baseline methods in model selection tasks. The work includes thorough analyses across various domains - medical, mathematical, and legal - and examines the robustness of these patterns across different prompt styles. Rather innovative, I must say, particularly in their approach to leveraging these patterns for practical applications in model selection and routing.

### Strengths
The authors have demonstrated remarkable creativity in their approach. The idea of examining hidden states for domain understanding is quite novel, and their experimental methodology shows careful consideration. I particularly appreciate their comprehensive evaluation across multiple architectures and domains. The practical implications for model selection could be quite significant, if properly developed.

### Weaknesses
1) In Section 2 and 3, the theoretical foundation appears inadequate. Authors discussed prior work but fail to establish a clear theoretical connection between hidden states and domain representation. The mathematical formulations lacks rigorous justification for why these specific activation patterns should correlate with domain knowledge. The "latent domain-related trajectories" introduced in L 68 need stronger mathematical grounding beyond empirical observations. Furthermore, the variance computation described in equations (1) and (2) requires proper statistical analysis of its significance in domain representation. Specifically, the authors do not address whether the observed variance is statistically significant or simply due to random fluctuations in the model's activations. A more rigorous approach would involve hypothesis testing to validate the claim that the variance is indeed indicative of domain-specific processing.

2) The experimental setup described in Section 4 reveals several critical issues. The model selection appears arbitrary, particularly regarding the choice of only testing models up to 7B parameters. The domain categorization described in lacks systematic justification for the grouping criteria. In Section 5.2, the prompt consistency analysis (L 327-337) needs more rigorous testing across a broader range of prompt variations. The performance improvements reported in Table 2 lack error bars and statistical significance testing, making it difficult to assess the reliability of the 12.3% improvement claim. The authors should have included confidence intervals and p-values to demonstrate the statistical significance of the reported improvements. Furthermore, the choice of datasets within each domain needs more justification, as the datasets may not be fully representative of the domain.

3) The implementation details in Section 5.3 require further clarification. The MLP classifier architecture described around lines 385-390 lacks proper justification for its design choices. The hyperparameter selection process mentioned in L 395-401 needs more detailed documentation. Most critically, the computational complexity analysis is entirely missing from Section 5.4, where the authors discuss layer reduction without properly quantifying the performance-computation tradeoffs. The authors should provide a detailed analysis of the computational cost associated with extracting hidden states from different layers and the impact of layer reduction on the overall performance of the model selection task. This analysis should include metrics such as FLOPs and latency.

### Questions
1) Can you provide mathematical proofs for why these trajectories should exist?
2) For Table 2: What is the statistical significance of the reported improvements?
3) How sensitive are your results to different prompt formulations?
4) Section 5.4: Can you quantify the computational savings from layer reduction?

### Soundness
4

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
3

### Summary
This study examines whether Large Language Models (LLMs) can recognize domain-specific nuances in natural language queries by analyzing its states, revealing that LLMs can distinguish queries from different domains. The findings suggest that LLMs can differentiate related domains and that the best-performing model isn't always the fine-tuned one, with applications to both closed and open-ended generative tasks. This study includes 4 LLM models ranging 2B-7B parameters and a subset of MMLU dataset

### Strengths
The paper addresses a very interesting topic in unfolding how LLMs works and can be utilized and selected for various tasks.
The chosen dataset is appropriate and also the four chosen models. 
The work is very interesting, in this new era of LLMs and a focus on transparency and trust of such models. The quality of the work is good, given the approach, experiments, and baselines considered, but can be improved.
The paper presentation can also be improved, as it is highlighted below.

### Weaknesses
 - i would have liked a more comprehensive discussion on the dataset, the decision to use 30 / 57 domains and also a characterization of the various subdomains, instead of mentioning just the 4 ones the paper decided to focus on.
- Next steps / research directions are unclear
- it would have been appropriate a discussion on computational runtime in these studies
- Some appendix material should be added to the core paper: in particular the discussion in A.3, A.4, A.5

Some other notes:
- the a/b/c/d labels should be clear by domain/sample
- a diagram showing the models (in/out and internals) and approach would have been good for a clearer presentation
- Figure 4: "Performance" label is unclear

### Questions
- Could you explain the rationale behind selecting 30 out of 57 domains? Additionally, can you provide a brief characterization of the various dataset subdomains, perhaps in an appendix?
- can you please clarify what other practical applications do you envision for this method? for what purpose / practical application? Routing Strategies is one mentioned, but a more detailed discussion is warranted on concrete examples of how it might be implemented in real-world scenarios.
- what are the runtime execution of such experiments? and what would be for a much bigger model?
- line 223: the baseline method are carefully explained, but not the rationale behind these choice. can you please clarify how you chose such parameters?
- Could you provide details on the computational resources used and the runtime for your experiments? How might these scale with larger models or datasets?
- What future research directions do you envision based on these findings? Are there particular applications or extensions of this work that you think would be most promising to explore next?

### Soundness
3

### Presentation
2

### Contribution
3
