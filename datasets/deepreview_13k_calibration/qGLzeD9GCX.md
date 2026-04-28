# EditMark: Training-free and Harmless Watermark for Large Language Models

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities, but their training requires extensive data and computational resources, rendering them valuable digital assets. Therefore, it is essential to watermark LLMs to protect their copyright and trace unauthorized use or resale. Existing methods for watermarking LLMs are mainly based on backdoors or knowledge injection, which require burdensome training or degrade the generation quality. To address these issues, we propose EditMark, a training-free and harmless watermarking method for LLMs based on model editing. 
We observe LLM has diversity and can generate multiple logical and semantic correct answers to some open-ended questions. Therefore, we can use a watermark to generate a harmless mapping to control the LLM's answer to an open-ended question.
Inspired by this insight, EditMark involves generating a harmless mapping based on the watermark, selecting a secret key to generate watermarked inputs, and editing the outputs of LLM to align with the harmless mapping. 
Extensive experiments show that EditMark can embed 8-bit watermarks into LLMs within 2 minutes, with a watermark extraction success rate close to 100%. External experiments further demonstrate that EditMark has fidelity and is robust to model fine-tuning and editing attacks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper tackles the issues of watermarking LLMs, such that a LLM provider can track the usage of its models by third parties. Backdoors or knowledge injections have drawbacks. Instead, EditMark propose to align with a harmless watermark mapping to open-ended questions, such as controling the number of digits when generating a float.

### Strengths
The topic is important, and adequately using knowledge injection to watermark LLMs is interesting. Doing so with open-ended questions, particularly with math questions, seem relevant and adequate.

### Weaknesses
 - The paper has a lot of flows. A lot of paragraphs really look LLM written and hard to digest
- The fact that the method is simple is a good thing. However, the explanation of the watermark extraction and experimental set-up appears very light. It would help to add in the appendix more details on the experiments, examples, related work. Overall I am not convinced by the literature review, and the choice of methods that the authors compare to. It is not clear wheter the novelty comes from the choice of watermarking or the choice of doing model editing instead of full finetuning. 

Overall, the method is interesting but the paper is too drafty. 



Minor:
- The LLMs that are considered are a few years old, I don't understand why.
- The authors could use \citep insstead of cite/citet when adequate.
- "Kirchenbauer et al. proposed the first watermarking methods Kirchenbauer
et al. (2023) for LLM." What about aaranson et al ?

### Questions
When reading this (which has flaws):

"To address this issue, Li et al. proposed a watermarking method Li et al. (2024) via knowledge injection, which embeds the watermark into the knowledge and injects the watermarked knowledge into LLM. In addition, the watermarked text is logically correct, which makes it harmless for LLM. However, this method also requires training the LLMs to embed watermarks, which is a huge cost for large-size LLMs.""


- I understand that there are already some work to insert watermarked harmless knowledge into a LLM. But it needs full fine-tuning so the authors don't compare to them. On the other hand the proposed method uses model editing. But couldn't that be applied to the previous harmless knowledge injection approached?

- Does the novelty come from the proposed method of watermarking the ouputs of math questions, or from the model editing part?

- Could the authors clarify how detection is done?

- What is the field "begin" in the table?

- Could the authors detail how they generated the question-answer pairs? how many of them are used for training? how many are used for detection? Are they the same questions as the training ones?

- In figure 3, why is Llama not as good as the other models?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces EditMark, a novel approach for watermarking open-source large language models (LLMs) that is both training-free and harmless. Unlike existing methods that rely on backdoors or knowledge injection, EditMark leverages model editing to embed watermarks without significant alterations to the model’s output quality.

### Strengths
1. The EditMark method introduces a unique, training-free watermarking solution leveraging model editing, avoiding the significant computational costs and potential risks associated with backdoor and knowledge injection methods. This innovation provides a practical means to protect open-source LLMs.

2. The proposed method can embed an 8-bit watermark within approximately two minutes, as demonstrated across multiple LLMs. This rapid embedding process, combined with a high extraction success rate (ESR) close to 100%, highlights the method's effectiveness and time-efficiency compared to existing techniques.

3. Experiments conducted using the BLiMP and MMLU benchmarks show that EditMark has a negligible impact on the model’s overall performance. The watermarking process preserves the logical and semantic integrity of the LLM’s output, ensuring that model functionality is maintained.

4. EditMark demonstrates notable resilience to common model attacks, including fine-tuning and editing. The watermark extraction success rate remains high even after such modifications, indicating that EditMark's approach offers robust protection without significantly compromising model usability.

### Weaknesses
 1. The paper mentions the trade-off between watermark capacity, ESR, and embedding time. Although embedding an 8-bit watermark is efficient and robust, scalability to higher capacities could present challenges, potentially limiting its utility in scenarios requiring more extensive watermarking. Specifically, the method's reliance on editing a limited number of knowledge instances within the LLM may become a bottleneck when attempting to embed larger watermarks. The paper does not explore the practical limits of this approach, such as the maximum watermark size achievable before the ESR degrades significantly or the embedding time becomes impractical.

 2. The robustness of EditMark against an informed attacker (i.e., one who knows the specific model editing layers used) shows some vulnerabilities. As depicted in experiments with targeted attacks, the watermark's resilience could be compromised, suggesting that further enhancement in adaptability is needed. The paper lacks a detailed analysis of how the choice of specific knowledge instances for editing affects the watermark's vulnerability. It is unclear whether certain types of knowledge are more susceptible to targeted attacks than others, and how this could be mitigated.

 3. The reliance on the Memit model editing technique limits the flexibility of the approach. While Memit is efficient for editing multiple knowledge instances, the method’s compatibility with other editing frameworks is not addressed, which could be a limitation for broader application. The paper does not discuss the potential impact of using different model editing techniques on the watermark's robustness and embedding efficiency. This lack of exploration raises questions about the generalizability of the proposed method.

 4. The paper's citation formatting is problematic. The authors may use "(authors et al.)" to highlight the citation part rather than directly show "authors et al."

### Questions
1. How scalable is the EditMark framework when embedding larger watermarks (e.g., 16-bit or 32-bit) without significantly affecting ESR and embedding time?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces EditMark, a novel method for watermarking large language models (LLMs) that is both training-free and harmless. The core idea behind EditMark is to leverage the inherent diversity in LLM responses to open-ended questions to embed watermarks without degrading the model's performance. The method involves generating a harmless mapping based on the watermark, selecting a secret key to generate watermarked inputs, and editing the outputs of the LLM to align with the harmless mapping. The authors claim that EditMark can embed 8-bit watermarks into LLMs within 2 minutes, with a watermark extraction success rate close to 100%. The method is also robust to model fine-tuning and editing attacks, maintaining high fidelity across various benchmarks.

### Strengths
1. **Training-Free**: One of the most significant strengths of EditMark is that it does not require retraining the LLMs. This makes it highly efficient and cost-effective, especially for large-scale models.
2. **Harmlessness**: The method ensures that the watermark does not affect the logical and semantic integrity of the generated text, which is crucial for maintaining the model's performance and usability.
3. **Efficiency**: The authors report that EditMark can embed watermarks quickly, within 2 minutes, making it a practical solution for real-world applications.
4. **Robustness**: The method is robust against various attacks, including model fine-tuning and editing attacks, which enhances its reliability.
5. **Fidelity**: Extensive experiments on benchmarks such as BLiMP and MMLU show that EditMark has a negligible effect on model performance, indicating high fidelity.

### Weaknesses
1. **Complexity of Implementation**: While the method is training-free, the process of generating a harmless mapping and selecting a secret key might be complex and require sophisticated algorithms. The paper could benefit from more detailed explanations and examples of these processes, specifically addressing the computational cost and memory requirements associated with generating and storing these mappings, especially for larger models and more complex watermarks. The lack of clarity around the practical implementation details makes it difficult to assess the true overhead of the method.
2. **Scalability**: The paper mentions that EditMark can embed 8-bit watermarks, but it is unclear how well the method scales to larger watermarks. Embedding more bits might introduce additional challenges and potential degradation in performance, such as increased computational time for embedding and extraction, and potential conflicts in the harmless mapping that could lead to noticeable changes in the output. The paper lacks a thorough analysis of the trade-offs between watermark capacity and model performance.
3. **Security Concerns**: Although the method is designed to be harmless, the security of the watermarking process is not thoroughly discussed. There is a need to explore potential vulnerabilities and countermeasures against advanced attackers who might attempt to reverse-engineer the watermarking mechanism. Specifically, the paper should address the possibility of attackers using statistical analysis of multiple watermarked outputs to infer the mapping or key, and how the method would defend against such attacks. The current discussion on robustness against adaptive attacks is insufficient.
4. **Generalizability**: The paper primarily focuses on open-source LLMs, but it is not clear how well EditMark would perform on proprietary models with different architectures and training methodologies. More diverse experimental settings would strengthen the paper's claims, including an analysis of how the method's performance varies across different model sizes, architectures (e.g., transformer vs. recurrent), and training datasets. The paper should also discuss potential challenges in adapting the method to models with limited access or different API structures.
5. **User Impact**: The paper does not discuss the potential impact of the watermark on user experience. For example, if the watermark alters the model's responses in subtle ways, it could affect the trust users place in the model's outputs. The paper should include a user study or qualitative analysis to assess whether the watermarked outputs are perceived as different or less trustworthy compared to non-watermarked outputs, and whether these differences are noticeable or detrimental to the user experience.

### Questions
1. **Detailed Implementation**: Could the authors provide more detailed steps and pseudocode for generating the harmless mapping and selecting the secret key? How do these steps ensure the watermark remains undetectable?
2. **Scalability**: How does the method scale to larger watermarks? Are there any limitations or trade-offs when embedding more bits?
3. **Security**: What are the potential security risks associated with the watermarking process, and how can they be mitigated? Have the authors conducted any security audits or simulations to test the robustness of the method against advanced attacks?
4. **Generalizability**: How well does EditMark perform on proprietary models with different architectures? Are there any modifications needed to adapt the method to non-open-source LLMs?
5. **User Experience**: How does the watermark affect the user experience? Are there any noticeable changes in the model's behavior that could impact user trust?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a black-box watermarking method for large language models that is both training-free and harmless. The work addresses the scenario of copyright protection for large language models by applying a model editing technique to embed the watermark.

### Strengths
+）The writing is clear and easy to understand. 

+）The authors propose a new watermarking mechanism for large language models.

### Weaknesses
 -）Although the paper applies a model editing technique, the technical contribution is limited.

-）The method used for editing the model is not properly cited. It's unclear which paper is referred to as "Memit" (lines 153-154).
Providing more examples would improve the paper.

-）The baseline selection is somewhat limited, as seen with the choice of "A watermark for large language models" [1].

-) If the attacker changes the sampling strategy (e.g., adjusts the temperature of the softmax layer), can the watermark maintain its robustness? The authors may consider extending the experiments.

### Questions
Please see weakness.

### Soundness
3

### Presentation
4

### Contribution
2
