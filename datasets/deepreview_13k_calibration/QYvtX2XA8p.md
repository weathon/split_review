# CtrlA: Adaptive Retrieval-Augmented Generation via Inherent Control

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Retrieval-augmented generation (RAG) has emerged as a promising solution for mitigating hallucinations of large language models (LLMs) with retrieved external knowledge. Adaptive RAG enhances this approach by enabling dynamic retrieval during generation, activating retrieval only when the query exceeds LLM's internal knowledge. Existing methods primarily focus on detecting LLM's confidence via statistical uncertainty. Instead, we present the first attempts to solve adaptive RAG from a representation perspective and develop an inherent control-based framework, termed \name. Specifically, we extract the features that represent the honesty and confidence directions of LLM and adopt them to control LLM behavior and guide retrieval timing decisions. We also design a simple yet effective query formulation strategy to support adaptive retrieval. Experiments show that \name is superior to existing adaptive RAG methods on a diverse set of tasks, the honesty steering can effectively make LLMs more honest and confidence monitoring is a promising indicator of retrieval trigger

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an adaptive RAG framework, CTRLA, which focuses on dynamically activating retrieval to supplement LLMs only when needed. Instead of relying solely on statistical confidence measurements, the paper introduces a representation-based approach to extract "honesty" and "confidence" features that guide the retrieval process. This framework targets issues of hallucination and efficiency in RAG models by enabling more accurate timing of retrievals. The experiments demonstrate that CTRLA outperforms other adaptive RAG methods, showcasing its effectiveness in retrieval timing and content accuracy.

### Strengths
1. CTRLA introduces a method for adaptive retrieval, focusing on honesty and confidence features within the LLM's representation space, a departure from conventional uncertainty-based approaches.
2. The experiments reveal CTRLA’s effectiveness in generating accurate and relevant responses, with enhanced performance in both short-form and long-form QA tasks.
3. The approach optimizes retrieval timing, resulting in fewer unnecessary retrievals.
4. The CTRLA framework is lightweight and does not heavily depend on external fine-tuning, potentially making it applicable across various LLMs and use cases.
5. The figures in the paper are very exquisite.

### Weaknesses
1. The experiments cover several QA tasks, and additional datasets that may not be memorized by the LLM could have further validated the framework's robustness, especially across rapidly changing topic datasets.
2. There are many similar works described as "knowledge conflicts", but the author seems to miss them both for introducing and as baselines, such as 2.1 Xie, Jian, et al. "Adaptive chameleon or stubborn sloth: Revealing the behavior of large language models in knowledge conflicts." arXiv preprint arXiv:2305.13300 (2023). 2.2 Jin, Zhuoran, et al. "Tug-of-war between knowledge: Exploring and resolving knowledge conflicts in retrieval-augmented language models." arXiv preprint arXiv:2402.14409 (2024).
3. Does this multi-step pipeline approach increase the computational burden? What is the overall complexity?
4. Since CTRLA relies on inherent LLM honesty and confidence features, the effectiveness of the framework may vary significantly depending on the LLM's underlying architecture. Specifically, the reliance on the model's internal representations for honesty and confidence could lead to inconsistent performance across different model architectures, which may have varying degrees of representational capacity and biases.
5. This paper is based on a strong assumption that "honesty" and "confidence" features can be linearly separated within the LLM's latent space. Does the independence between the two still hold in complex contexts? It is unclear how the method would perform if these features are entangled or non-linearly separable, which is a possibility given the complexity of LLM representations.
6. The extraction of "honesty" and "confidence" is based on the parameterized knowledge of the model itself. How to ensure the fairness of this process? Because this is the basis for the following work. The method's reliance on the model's own internal knowledge for feature extraction raises concerns about potential biases or unfairness that may be present in the model's training data, which could disproportionately affect certain groups or topics.

### Questions
See above

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes CtrlA, an adaptive RAG framework to extract honesty and confidence features and use them to steer the generation. CtrlA uses contrastive prompts to instruct the LLM with corresponding behaviors (honest/dishonest/confident/unconfident), and then extracts the hidden representations of the whole statement to form the honesty/confidence vectors with PCA. It uses a linear combination to guide the generation towards the honest/confident direction. Experimental results and analyses demonstrate that CtrlA performs well in reasoning tasks.

### Strengths
- The proposed method is interesting and effective.

- The paper is well-written and easy to follow.

### Weaknesses
 - The method requires accessing the internal structure of LLMs, which may not be available for some competitive commercial LLMs such as o1 and limits its applicability. 

- The approach relies heavily on PCA and detailed layer-wise feature extraction, potentially leading to high computational costs and processing time, especially with larger models. The principle component selection process is also not discussed since the first principle component might not represent the required direction.

- The method involves intricate processes such as feature extraction, honesty steering, and confidence monitoring, which require substantial computational resources and expertise to implement. No token expenses are reported.

- The query formulation strategies lack clarity in handling ambiguous or noisy outputs. The methods for masking unconfident tokens and refining search queries are insufficiently detailed, making it challenging to understand how they ensure the retrieval of relevant documents. Additionally, there's a potential risk of losing important context when masking tokens, which could affect retrieval accuracy.

- Modifying the representation space can inherently harm the quality of generated content, which successfully answers the question but fails to produce a plausible and fluent sentence, as illustrated in Fig 3b.

- The experimental results are not comprehensively discussed. Fig 2 and 3 show different effects of $\lambda$ on accuracy, but no further discussion is provided for such contradiction except the dataset category.

### Questions
- Why does honesty steering always improve accuracy in closed-domain QA? Generally, the result should be similar to open-domain tasks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper tackles an issue in Adaptive Retrieval-Augmented Generation by focusing on retrieval timing to reduce hallucinations, and using interpretable methods to analyze honesty and confidence. The method shows promising experimental results. However, the motivation behind some methods feels unclear, with Honesty Steering and Search Query Formulation seeming unrelated to the core goal and lacking novelty. Additionally, the experimental setup lacks clarity on segment definitions. The reliance on an outdated linear representation assumption raises concerns about applicability in modern LLMs.

### Strengths
This paper proposes to address Adaptive Retrieval-Augmented Generation by focusing on retrieval timing to reduce hallucinations. It takes an interpretable approach by analyzing internal mechanisms like honesty and confidence, providing clearer insights into model behavior. Experimental results show meaningful improvements, suggesting that the proposed method contributes effectively to retrieval-augmented generation tasks.

### Weaknesses
1.	The paper doesn’t explain why the methods are crucial for Adaptive Retrieval-Augmented Generation (ARAG). The section Confidence Monitoring as Retrieval Trigger seems directly relevant to ARAG, while the section Honesty Steering and Search Query Formulation seems to be unrelated to the main goal. The Honesty Steering part has already been introduced in similar work[1], which makes the technical contribution of the paper incremental. The methods aren’t presented in a clear, motivating way, making the paper feel disjointed.

2.	In the experiments, it’s unclear how the "segments" are defined, leaving readers without a solid understanding of the setup. Also, the ablation study misses the marks that specifically show if Confidence Monitoring is driving the improvements. Without clear evidence, it’s hard to conclude that the approach tackles the core ARAG issues.

3.	The paper builds on a linear representation assumption, referencing work from Templeton et al. (2024) which is based on early RNN-based findings[2]. Given the evolution of model architectures in the LLM era, this assumption seems to be oversimplified.

### Questions
See the above comments.

### Soundness
3

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
This paper approaches the problem of adaptive retrieval for RAG, in which “when and what to retrieve” is dynamically determined during generation. Motivated by the limitation of existing uncertainty-based approaches, this paper proposed to consider both “honesty” and “confidence” as important factors to guide adaptive retrieval. Three techniques are introduced: (1) shifting LLM representation to the honest direction, (2) projecting the representation onto a confidence feature and (3) a revised query generation technique based on the already-generated content. Experiments using several LLMs on short-form and long-form generation tasks verify the effectiveness of the proposed approach compared to existing adaptive retrieval methods.

### Strengths
* Although the adaptive retrieval framework has been introduced for several years, it is still an open problem for how to build strong adaptive retrieval strategies catered to modern LLM. The research question proposed by the paper is thus timely. 

* The empirical evaluation is thorough. A number of LLMs are evaluated with the proposed method. The authors consider several major benchmarks across different generation formats. The empirical results can serve as good reference points for future works on adaptive retrieval. 

* The proposed method is intuitive and can outperform well-known existing baselines such as FLARE and DRAGIN.

### Weaknesses
My major concern of this paper is that its proposal and contribution are not aligned with the key problem the paper is motivated by.

* This paper contains many moving parts, but most of them are (1) disconnected and (2) irrelevant to the key challenge of adaptive retrieval. The core motivation of this paper is that uncertainty-based adaptive retrieval is insufficient for determining when retrieval should be triggered. However, the proposed honesty steering and query formulation methods aim to generate higher quality RAG responses instead of solving the problem of adaptive retrieval. In addition, the proposed retrieval triggering criteria is still fundamentally an uncertainty-based method. 

* The proposed method does not seem to solve the issue in the motivating example, where adaptive retrieval fails to trigger when the model confidently says “I don’t know”. From my understanding, the proposed method will also fail in this case.

* Algorithm 1 is incomplete. Specifically, an outer loop that calls algorithm 1 is required. The input to the outer loop is the query and the document, and the output is the final generated response, instead of a single output segment. 

* More citations to the adaptive RAG literature are required in section 3. Specifically, 3.1 and 3.2.4 should cite FLARE [1], as the approaches are similar. In addition, decoding-stage feature monitoring works such as [2] and [3] should be cited in the confidence monitoring section,

### Questions
(please also see weaknesses)

* What is this paper’s definition of honesty? Can you further explain how it connects with adaptive retrieval in the proposed framework? 

* I would like to see a full ablation on the proposed techniques, where only one technique is ablated at a time and compared to the performance of all the techniques together.

* How do you determine the hyperparameters of the proposed method and the baselines (such as the retrieval threshold)? Do you always use an in-domain validation dataset to tune the parameters? Are the hyperparameters kept the same across all test sets?

### Soundness
3

### Presentation
2

### Contribution
2
