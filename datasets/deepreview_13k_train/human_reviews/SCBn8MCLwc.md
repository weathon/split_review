# Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Training a language model to be \emph{both} helpful and harmless requires careful calibration of refusal behaviours:
Models should refuse to follow malicious instructions or give harmful advice (e.g.\ ``how do I kill someone?''), but they should \textit{not} refuse safe requests, even if they superficially resemble unsafe ones (e.g.\ ``how do I kill a Python process?'').
Avoiding such \textit{false refusal}, as prior work has shown, is challenging even for highly-capable language models.
In this paper, we propose a simple and surgical method for mitigating false refusal in language models via single vector ablation.
For a given model, we extract a false refusal vector and show that ablating this vector reduces false refusal rate without negatively impacting model safety and general model capabilities.
We also show that our approach can be used for fine-grained calibration of model safety.
Our approach is training-free and model-agnostic, making it useful for mitigating the problem of false refusal in current and future language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers the problem of false refusals in LLMs, e.g., refusing to answer "How do I kill a python process?".  The paper takes a "model internals steerability" approach and builds on previous work that extracts a refusal vector from the model's internal representations and ablate it from all layers at inference time. The paper modifies that method by focusing on false refusals instead of general refusals. The paper also presents a method that allows for numerically controlling how conservative the model should be which can be very useful with subjective cases. The paper presents results and analysis that demonstrates the effectiveness of the presented approach in comparison to existing methods.

### Strengths
1. The approach is simple and very justified

2. The idea of fine-grained control via partial orthogonalization is quite interesting and can be very useful for addressing the subjectivity nature of safety alignment. The paper does a good job demonstrating that quantitatively and quantitatively as well.

3. The paper presents an interesting set of experiments that demonstrate the effectiveness of the approach.

### Weaknesses
1. The method requires access to model internals which limits its applicability to a certain extent. 

2. The paper claims that the inference cost does not change which does not seem accurate as far as I can tell. The operation in eq. 4 is applied at all layers of the model. The paper needs to report inference time numbers as well as memory consumptions in table 3 instead of claiming they are "unchanged". 

3. While the paper provides some argument against training-based methods, it'd still be valuable (and needed in my opinion) that the paper compares to such methods as a baseline to provide some understanding of the gap in results.

### Questions
I am mostly puzzled by the claim about the unchanged inference time cost. Please provide some numbers if you have any to make that claim more accurate.

### Soundness
3

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
The paper presents a method for reducing false refusals in language models by ablating a single vector from the model's activation stream. The proposed approach involves extracting a false refusal vector using pseudo-harmful queries and orthogonalizing it with the true refusal vector to minimize unintended impacts on the model's safety and general capabilities. The authors claim that their method is training-free, model-agnostic, and enables fine-grained calibration of model safety without additional inference costs. Experimental results are provided on several datasets using different language models to demonstrate the effectiveness of the proposed method.

### Strengths
1. Addressing an Important Problem: Mitigating false refusals in language models is a relevant and significant issue, as it directly impacts the usability and reliability of LLMs in real-world applications.

2. Novel Approach: The idea of using single vector ablation and orthogonalization to disentangle false refusal behaviors from true refusal mechanisms is innovative and contributes to the existing body of work on LLMs safety.

3. Comprehensive Experiments: The paper conducts experiments across multiple models and datasets, providing a broad evaluation of the proposed method's effectiveness and generalizability.

4. Fine-Grained Control via Partial Orthogonalization: The ability to adjust the orthogonalization coefficient (λ) for fine-tuning the model's sensitivity to ambiguous queries is a valuable feature. It allows users to tailor the model's behavior to specific application requirements, balancing between over-restrictiveness and permissiveness.

### Weaknesses
1. Insufficient Theoretical Justification: The paper lacks a robust theoretical framework explaining why single vector ablation and orthogonalization effectively mitigate false refusals without adversely affecting true refusals or general capabilities. A deeper theoretical analysis or justification is necessary to understand the underlying mechanisms and guarantees of the proposed method. Specifically, the paper does not provide a clear explanation of why ablating a single vector, derived from pseudo-harmful queries, would selectively target false refusals while preserving the model's ability to identify genuine harmful content. The method's reliance on orthogonalization also lacks a theoretical basis, making it unclear why this operation would disentangle the desired behaviors. A more rigorous analysis, perhaps drawing from concepts in linear algebra or representation theory, is needed to support the claims.

2. Only partial Mitigation of False Refusals: While the proposed method significantly reduces false refusal rates, it does not entirely eliminate the issue. The paper does not explore the limitations of the method in detail, such as the types of queries that still result in false refusals. Further research is needed to fully address the underlying causes of false refusals in language models, and it is unclear if the proposed approach can be extended to handle more complex cases. The paper should also discuss the potential for adversarial attacks that could exploit the method's weaknesses, leading to new forms of false refusals or bypassing safety mechanisms.


### Questions
The paper presents a novel method for mitigating false refusals in language models. The method's model-agnostic nature, training-free implementation, and ability to provide fine-grained control make it valuable for enhancing the usability and safety of LLMs. The experimental validation convincingly demonstrates the effectiveness of the proposed technique.

Here are some questions I want to ask:

1. Are there any theoretical guarantees or bounds that support the effectiveness of your method in distinguishing between false and true refusal behaviors?

2. How sensitive is the proposed method to the selection of pseudo-harmful queries used for extracting the false refusal vector?

3. Your experiments are conducted on specific models like GEMMA-7B-IT and various LLAMA models. How does your method scale to larger models (e.g., 175B parameters) or different architectures beyond the ones tested?

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
This paper focuses on the false refusal problem in the safety scenario of LLMs, i.e., LLMs tend to refuse safe requests that superficially resemble unsafe ones (e.g. “how do I kill a Python process?”). Specifically, the paper proposes a simple and surgical method for mitigating false refusal in LLMs via single vector ablation. For a given LLM, they extract a false refusal vector based on the activations of LLM’s layers using harmful, pseudo harmful, and harmless datasets. Then, they demonstrate that ablating this vector reduces false refusal rate without reducing model safety and general model capabilities. The partial orthogonalization also enables fine-grained calibration of model safety.

### Strengths
1.	The paper proposes a simple and surgical method for mitigating false refusal in LLMs via single vector ablation. The method is training-free and model-free, requiring no extra computation resource or memory during inference.

2.	The idea of separating refusal related features from false refusal vectors by orthogonalization is novel and interesting. Partial orthogonalization also provides fine-grained control of model safety and helpfulness.

3.	The paper conducted comprehensive experiments to demonstrate the effectiveness of the method, and enhance the understanding of different factors in the method. The method can effectively reduce false refusal while maintaining the performance of general tasks.

### Weaknesses
1.	While the method is described quite clear in the current form, adding a workflow figure to demonstrate the process of extracting (false) refusal vectors and ablating them can make it easier for understanding.

2.	In section 4, the paper uses greedy decoding for text generation, which however is not the common choice in practice. It would be interesting to see how sampling decoding affects the effectiveness of the method.

3.	In section 4, the samples of harmful, pseudo harmful, and harmless come from different sources. Will the difference of data content or domain affect the method? BTW, there are some typos of the symbols for datasets in line 182. 

4.	In section 5.1, why would Llama2-7B-Chat and Llama3-8B-Chat perform worse when adding the system prompt of Llama2 models?

### Questions
Refer to the weakness part.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an orthogonalization based vector ablation method to mitigate LLM false refusals, which ablates a false refusal vector extracted from the diff-in-means vectors obtained by prompting with pseudo-harmful and harmless queries. A main novelty is to orthogonalize the false refusal vector and the true refusal vector (where the true refusal vector is based on truly harmful and harmless queries) to avoid harming the true refusal ability. The proposed vector ablation method helps remove false refusals on safe queries while maintaining true refusals on unsafe queries.

### Strengths
Mitigating false refusals is important in enabling chat models with more satisfying responses. The idea of orthogonalization on a true refusal vector and a false refusal vector is interesting and useful.

In particular, the authors identify that the true refusal vector and false refusal vector are not independent of each other. Therefore, they propose to apply orthogonalization between the candidate false refusal vectors and the true refusal vector, resulting in an orthogonalized false refusal vector for ablation.

The proposed method achieves increased compliance rates (CR) on false refusal datasets, including ORB-H, XSTest-S(H), and OKTest. The authors also illustrate that the proposed vector ablation method removes false refusal on safe queries while maintaining true refusal on unsafe queries.

### Weaknesses
The presentation could use clearer definitions and equations, and it might be better to provide an intuitive illustration showing example queries in an example transformer network targeting at a layer and a token position. 

For example, in Section 2.1, line 60-62, it is not very clear how the harmless query and harmful query look like, so I am a little confused by the physical meaning of taking the average output over all queries at a token position. It is unclear if these queries are designed to be minimal pairs differing by a single token, or if they are more diverse. The lack of clarity on the query construction makes it difficult to interpret the resulting 'refusal vector'.

In addition, in Equation (3), I am not sure why the definition for pt is omitted (according to the context, $p_t$ is token t’s probability at the first token position in the model’s response). It is also unclear how the refusal score is thresholded, and what is the sensitivity of this thresholding process. Other possible typos: in line 116, wrong subscript in Equation (7)? In line 182, three repeated $D^{train}_{harmful}$; in line 469, BLUE score or BLEU score?

### Questions
1. I may have missed the points: 

a. Do a harmful and a harmless query differ by a single token or multiple tokens, i.e., does Equation (1) assume both queries are of the same length?

b. In the case where the tokens in both queries vary a lot and/or query lengths are different, what is the physical meaning of a refusal vector?

c. Is the [/INST] token the only token position chosen for representing a refusal vector?

d. Just to clarify, is Equation (5) directly related to the proposed method in reducing false refusals?

e. How exactly is vector ablation applied to general tasks, such as MMLU?

f. Why does general capability, as measured by acc. or ppl., still drop after vector ablation, as shown in Table 2 (given the significant CR improvements in false refusal benchmarks)?

2. Pseudo-harmful queries are essentially harmless. Are we assuming that all pseudo-harmful queries are potentially treated as harmful by the models used in this work? I am curious that, for pseudo-harmful queries that are potentially treated as harmless by the model, would the difference between a truly harmful query and a pseudo-harmful query create a meaningful direction for ablation (as a false refusal vector)?

3. Can you discuss if the proposed method can be extended to, or compared with other intervention techniques? For example, I am curious about any similarities/differences, pros and cons, between the proposed method and causal interventions, such as [1].

[1] K. Meng, D. Bau, A. Andonian, and Y. Belinkov. Locating and editing factual associations in gpt. Advances in Neural Information Processing Systems, 35:17359–17372, 2022.

### Soundness
3

### Presentation
1

### Contribution
2
