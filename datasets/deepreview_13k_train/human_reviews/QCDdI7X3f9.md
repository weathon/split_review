# Model Equality Testing: Which Model is this API Serving?

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Users often interact with large language models through black-box inference APIs, both for closed- and open-weight models 
(\eg \llama models are popularly accessed via Amazon Bedrock and Azure AI Studios).
In order to cut costs or add functionality, API providers may quantize, watermark, or finetune the underlying model, changing the output distribution --- often without notifying users. 
We formalize detecting such distortions as Model Equality Testing, a two-sample testing problem, 
where the user collects samples from the API and a reference distribution, and conducts a statistical test to see if the two distributions are the same. 
We find that tests based on the Maximum Mean Discrepancy between distributions are powerful for this task:
a test built on a simple string kernel achieves a median of 77.4\% power against a range of distortions, using an average of just 10 samples per prompt.
We then apply this test to commercial inference APIs for four \llama models,
finding that 11 out of 31 endpoints serve different distributions than reference weights released by Meta.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Model Equality Testing to understand the differences between models served by APIs. The proposed method is a two-sample test that uses various prompts along with multiple generations of a given prompt and tries to infer if two instances of generations come from the same distributions using the Maximum Mean Discrepancy kernel. The proposed method is studied empirically to understand its power in identifying the differences for models served by many APIs.

### Strengths
The paper is overall well written, organized and easy to follow. The application of two sample testing using the Maximum Mean Discrepancy kernel is novel for studying distributions coming from different models.

### Weaknesses
 - I’m not convinced of the significance of this problem. Can this problem be solved through policy if the users ask from providers to disclose such changes? The API provides can be even motivated to charge users differently based on the optimizations done to models.
- Evaluations can be stronger:
    - The authors claim that the proposed method works using an average of 10 samples per prompt across 20-25 prompts. Since the paper relies on empirical analysis, I would love to see more analysis backing this claim/more guidelines around these requirements. For instance, do I still need to provide 10 samples per prompt if I generate the samples using 0 temperature? What about if my prompts are all from a niche topic versus if I’m testing across various different unrelated topics? Does one still obtain high power using 20-25 prompts?
    - The evaluations are done using samples from English, German, Spanish, French, and Russian Wikipedia. I’d love to see more diversity in the evaluation tasks. For instance, consider showing the results for coding tasks, which can help with the broader applicability of the proposed method.

- Regarding the kernel:
    - For the choice of the kernel, you are basically trading off bias and variance. I think this might be good to call out in the manuscript. My understanding is that as L goes to infinity, the hamming kernel approaches the universal one-hot kernel. Similarly as L goes to 0, one biases towards the first tokens. I’d love to understand the implications of this bias-variance tradeoff on tasks that require more creativity like writing.
    - Also L is set to 50 and the sensitivity to L is studied until L=50. I think 50 tokens for generations is typically on the lower end when it comes to LLM-based applications. I’d recommend studying it at least until 10 folds.
    - I’d think L is affected by the vocabulary size of the tokenizer. Did the authors study the effect of L under different tokenizers? 
    - The kernel checks for token equivalence but an important piece to capture might be around semantic equivalence. Have the authors considered other kernels that can capture semantic equivalence?
- Evaluations:
    - Figure 3 lower left. The power of detecting Llama3.1 8B from Llama3.1 8B (int8) and (watermark) are 0.07 and 0.32, respectively, which are very low. I’d love to hear the author's thoughts on this as one of the premises of the method is to be able to detect such changes in the model. 
    - Consider adding an analysis that shows that the method does not detect any changes if the two samples come from the same model. It would be great to show the detection power using samples obtained at different temperatures.
    - Can you extend the analysis in Figure 3 lower left to other models? One thing I’m interested to understand is that the method is able to detect different model sizes and looking at Figure 3 on the right hand side, the models from the same family look very close in terms of distance.
- Nit: Mention that L is the number of tokens in the manuscript.

### Questions
- Regarding the kernel:
    - For the choice of the kernel, you are basically trading off bias and variance. I think this might be good to call out in the manuscript. My understanding is that as L goes to infinity, the hamming kernel approaches the universal one-hot kernel. Similarly as L goes to 0, one biases towards the first tokens. I’d love to understand the implications of this bias-variance tradeoff on tasks that require more creativity like writing.
    - Also L is set to 50 and the sensitivity to L is studied until L=50. I think 50 tokens for generations is typically on the lower end when it comes to LLM-based applications. I’d recommend studying it at least until 10 folds.
    - I’d think L is affected by the vocabulary size of the tokenizer. Did the authors study the effect of L under different tokenizers? 
    - The kernel checks for token equivalence but an important piece to capture might be around semantic equivalence. Have the authors considered other kernels that can capture semantic equivalence?
- Evaluations:
    - Figure 3 lower left. The power of detecting Llama3.1 8B from Llama3.1 8B (int8) and (watermark) are 0.07 and 0.32, respectively, which are very low. I’d love to hear the author's thoughts on this as one of the premises of the method is to be able to detect such changes in the model. 
    - Consider adding an analysis that shows that the method does not detect any changes if the two samples come from the same model. It would be great to show the detection power using samples obtained at different temperatures.
    - Can you extend the analysis in Figure 3 lower left to other models? One thing I’m interested to understand is that the method is able to detect different model sizes and looking at Figure 3 on the right hand side, the models from the same family look very close in terms of distance.
- Nit: Mention that L is the number of tokens in the manuscript.

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
4

### Summary
In this paper, the authors study the equivalence problem of LLMs in an API service environment. They formulate it as a two-sample test to assess the consistency of output distributions from different APIs. Ultimately, they use Maximum Mean Discrepancy (MMD) and achieve effective differentiation.

### Strengths
1. This paper is well-organized and written, making it easy to understand.
  
2. The problem addressed is valuable, as APIs have indeed become one of the mainstream forms of LLM applications.

3. The method design is reasonable and concise, and the experiments appear to be effective.

### Weaknesses
1. The study primarily focuses on the LLaMA series models. Although this aligns with the paper’s emphasis, I recommend that the authors verify the generalizability of MMD across more models. Specifically, the paper should investigate models with different architectures and training methodologies, as the effectiveness of MMD might be influenced by the underlying model characteristics. For example, models trained with different loss functions or on different datasets could exhibit varying sensitivity to the MMD metric.

2. The computation cost of MMD appears to be somewhat high. While the paper mentions the use of the Hamming kernel, it would be beneficial to provide a more detailed analysis of the computational complexity, especially when dealing with large-scale API testing scenarios. The paper should also discuss potential optimizations or approximations that could be used to reduce the computational burden of MMD, such as using dimensionality reduction techniques or sampling methods.

### Questions
1. MMD performance declines with small sample sizes, which is likely the case in real-world scenarios. Although the paper discusses sample efficiency, additional experiments with smaller sample sizes could provide further insights into this limitation.

2. In practice, API services may not use the same model but rather similar models(like MOE). I suggest the authors provide some discussion on this point.

3. How does MMD perform in terms of efficiency in large-scale testing scenarios?

### Soundness
3

### Presentation
3

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
The authors propose a method for determining whether a model black-box (i.e. an LM served through an API) differs from a reference model; usually a canonical model version or simply an earlier version of the API.
The proposed method relies on sampling texts from different models / APIs or the same one at different times and estimating their relation against a distance metric under some kernel. The authors propose a Hamming distance kernel as an empirically reliable approach for this estimation. They provide analysis of different foundation models and APIs over time gleaning insight into how inference service providers may affect inference reliability.

### Typos
- Line 081: extra article 'a' inserted before 'an API'

### Strengths
- The overall idea of providing more analytic tools for black-box models / APIs seems important and interesting. I think many people reliant on these black-box APIs are left at their mercy and have little means of understanding how different service providers could affect their system performance.
- The public release of generated samples offers valuable data for community use and future API change tracking.
- Providing a framework for analyzing APIs on non-classification based (i.e. difficult to evaluate) tasks seems fairly novel and is a good contribution.

### Weaknesses
- Line 081: extra article 'a' inserted before 'an API'

- One immediate problem I see is that acquiring the reference distribution on a user-defined task requires setting up the reference LM anyways, which was something that is acknowledged to be inconvenient or infeasible in many cases. That would make this method impossible in certain scenarios.

- The hamming kernel's effectiveness across different tasks raises concerns, particularly for open-ended tasks like creative generation where diverse outputs may be desirable. The significance tests may struggle with high-variance outputs, potentially missing quality differences. Further analysis is needed on how task semantics and natural distribution affect the method's applicability. Additionally, using Wikipedia-based language modeling as the primary test task may underestimate output diversity due to the highly factual nature of the content and potential data contamination. This is partially addressed by the inclusion of HumanEval, but additional comparisons and/or analysis could strengthen the results.

- I didn't see any mention of two model customizations that I suspect may be popular: system prompt customization and generation-time safety interventions. It's not clear to me how the proposed method would behave under these customizations.

### Questions
- In Figure 4, you compare absolute task accuracy difference with MMD, but this is slightly less informative than showing non-absolute task difference. You imply on lines 415-418 that task accuracy difference are usually lower for the non-reference models, but this isn't necessarily obvious that a provider's interventions are always harmful to accuracy / quality. Could you provide some information about MMD and absolute accuracy?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors formulate the problem of testing whether two versions of a language models (either fully accessible, or accessible via API) are the same given two sets of samples from one model and another. They propose a simple but effective statistical test to distinguish between two sets of samples based on the Maximum Mean Discrepancy (MMD) string kernel method with the Hamming distance. They compare the chosen Hamming distance to other simple string distances and find that Hamming distance is well-suitable kernel to compare the samples from prompted language models. To evaluate the proposed MMD test, they verify that it shows high power for distinguishing different version of the same model or different models with a reasonably small number of samples, and degrades less w.r.t. the sequence length. Finally, they use the test to audit the API endpoints and find that a large portion of LLaMa 3 API providers give access to a different version of the model.

### Strengths
This paper touches upon a very timely problem of verifying the integrity of the black-box APIs and model versioning in the cases when full detailed for a particular API are not open. Namely, the important question this paper formulates and proposes a test for is whether two different versions of the same model are the same. This is an important test given that sometimes models are changed, compressed for efficiency or safety reasons, and it is important for practitioners to understand what to expect from a given API.

Overall, the paper is easy to follow, and methodology is sound. Experimental setup is sound enough to support the claims. Proposed method is simple and intuitive and builds upon the older works on string kernel based tests. I expect this paper will have a high impact within the language modelling community.

### Weaknesses
There are no critical weaknesses, in my opinion, only minor ones.

The choice of baselines is limited to different choices of string kernels.
I was a bit surprised to see Hamming distance to perform the best, and in general felt that discussion and intuition why it works well is not present.

### Questions
Q1. My intuition is that Hamming distance would be too sensitive to positions of tokens in the sentence by its construction, e.g. they don't capture the similarity between two shifted chunks of text. I would have started with Levenshtein distance, have you maybe tried it in your experiments?

Q2. How do you compute the kernels if a language model generates a shorter sentence compared to the maximal length?

Other questions:
- eq.4, should there z and z' be different?
- 162: what does accurate completion means?
- 210: is the only difference in the weights of the models, can generation algorithms also be different?
- Figure 2: a not well-readable sentence: "Curves first median power ..."
- 312: you write 1.1M unicode characters, but as far as I can check in Unicode 16.0 there are 155,063 unique characters, how it was computed?
- 326: "significantly different training data": do you use word significantly in statistical meaning here?
- 337: semantic caching, quantization: is it possible to put citations here?
- Figure 4 (right): what are the colours here?

### Soundness
4

### Presentation
3

### Contribution
3
