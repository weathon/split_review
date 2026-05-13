# Label Privacy in Split Learning for Large Models with Parameter-Efficient Training

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
As deep learning models become larger and more expensive, many practitioners turn to fine-tuning APIs. 
These web services allow fine-tuning a model between two parties: the client that provides the data, and the server that hosts the model.
While convenient, these APIs raise a new concern: the data of the client is at risk of privacy breach during the training procedure.
This challenge presents an important practical case of vertical federated learning, where the two parties perform parameter-efficient fine-tuning (PEFT) of a large model.
In this study, we systematically search for a way to fine-tune models over an API *while keeping the labels private*.
We analyze the privacy of LoRA, a popular approach for parameter-efficient fine-tuning when training over an API.
Using this analysis, we propose P$^3$EFT, a multi-party  split learning algorithm that takes advantage of existing PEFT properties to maintain privacy at a lower performance overhead.
To validate our algorithm, we fine-tune DeBERTa-v2-XXLarge, Flan-T5 Large and LLaMA-2 7B using LoRA adapters on a range of NLP tasks. We find that P$^3$EFT is competitive with existing privacy-preserving methods in multi-party and  two-party setups while having higher accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a privacy-preserving approach to safeguard label privacy during the fine-tuning of large language models (LLMs) using Parameter-Efficient Fine-Tuning (PEFT) techniques. It addresses a two-party learning scenario, where users can access forward and backward APIs to update the model. Experiments are conducted to evaluate the approach across various language models.

### Strengths
The paper addresses a critical question of how to protect privacy in client-server fine-tuning settings. The author proposes a privacy-preserving approach to safeguard label privacy in vertical learning and evaluates this method across various models and NLP tasks.

### Weaknesses
The paper claims that backpropagation is conditionally linear in output gradients and attempts to decompose gradients to enhance privacy. However, based on my understanding, if decomposed gradients are backpropagated through earlier layers, how can this linearity be maintained? The core issue lies in the non-linear activation functions within the neural network; backpropagating through these functions will inherently introduce non-linearities, regardless of how the gradients are initially decomposed. The paper needs to clarify how this conditional linearity is preserved during the backpropagation process, especially when considering the chain rule and the impact of non-linear activation functions.

The proposed approach requires the user to decompose gradients into separate parts and make multiple API calls. What is the associated computation and communication overhead? The paper should provide a detailed analysis of the computational cost associated with the multiple forward and backward passes required for gradient decomposition. Furthermore, the communication overhead, particularly the size of the gradients being transmitted between the client and server, needs to be quantified. Additionally, to my knowledge, I am not aware of any LLM companies that offer APIs for forward and backward passes in this way. Could the authors provide examples of such an application if available?

If the client is involved in parameter updates and can observe the training process, how is it ensured that the client cannot access private information during training? The paper focuses on label privacy, but it's not clear how the client's ability to observe the training process and manipulate parameters might lead to other privacy breaches. For instance, could the client infer information about the model's internal representations or the training data itself through iterative parameter updates? Regarding the experimental results, I don’t see a clear definition of what "leak" represents in the tables. My assumption is that it refers to the client’s prediction accuracy. If this is correct, with prediction accuracy over 60%, it doesn’t seem that label privacy is effectively preserved.

### Questions
Can you provide some definitions to describe the metrics used to evaluate the approach?

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
2

### Summary
This paper proposes $P^3EFT$, based on PEFT for fine-tuning models in a 2-party setting common to fine-tuning APIs in practice. The focus is on guaranteeing a form of empirical label-privacy. Their approach utilises a private backpropagation approach inspired by secure-aggregation to prevent the server from inferring label information and further trains a mixture of multiple adapters to improve privacy.

### Strengths
- The paper focuses on an interesting and relevant privacy problem related to fine-tuning APIs which are increasingly popular.
- Strong empirical results which show that the proposed method can maintain both accuracy and empirical label-privacy.
- The presentation of the paper is clear and well-written.

### Weaknesses
 - More could be done to compare with existing baseline methods in the experiments section (see below).
- Some experimental results are unclear (see below).
- It is implied that training multiple adapters is a way to prevent label-leakage, yet in the experiments only n=2 adapters are used. Did you run any experiments varying the number of adapters and what effect did this have on utility and privacy? Further to this, how small are the adapters that are used? It would be useful to include some information about the overhead that is required for clients.
- I think some of the Appendix results with the PSLF method could be added into the main paper tables to show there is a clear utility loss when utilising a label DP approach and that there are advantages to using a more empirical method like $P^3EFT$.
- What does it mean in Table 6 to train with an $\varepsilon = 0$ with PSLF?
- How many times are the experiments repeated over? There is often a large amount of variance in the privacy leakage e.g., on QNLI in Table 1 and Table 3 which can make DC and $P^3EFT$ seem quite comparable.
- It could help to move Algorithm 2 (or a more concise version of it) into the main text from the Appendix to help make the final $P^3EFT$ method clear.
- The abstract mentions that $P^3EFT$ is competitive to methods in both a multi-party and 2-party setting. As far as I can tell, the experiments in Section 4 are focused only on a 2-party setting? How does this process change or scale to a multi-party setting?
- Minor: Typo L485 algorothm → algorithm

### Questions
1. It is implied that training multiple adapters is a way to prevent label-leakage, yet in the experiments only n=2 adapters are used. Did you run any experiments varying the number of adapters and what effect did this have on utility and privacy? Further to this, how small are the adapters that are used? It would be useful to include some information about the overhead that is required for clients.
2. I think some of the Appendix results with the PSLF method could be added into the main paper tables to show there is a clear utility loss when utilising a label DP approach and that there are advantages to using a more empirical method like $P^3EFT$. 
3. What does it mean in Table 6 to train with an $\varepsilon = 0$ with PSLF?
4. How many times are the experiments repeated over? There is often a large amount of variance in the privacy leakage e.g., on QNLI in Table 1 and Table 3 which can make DC and $P^3EFT$ seem quite comparable.
5. It could help to move Algorithm 2 (or a more concise version of it) into the main text from the Appendix to help make the final $P^3EFT$ method clear.
6. The abstract mentions that $P^3EFT$ is competitive to methods in both a multi-party and 2-party setting. As far as I can tell, the experiments in Section 4 are focused only on a 2-party setting? How does this process change or scale to a multi-party setting?
7. Minor: Typo L485 algorothm → algorithm

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
This paper addresses the problem of parameter-efficient fine-tuning (PEFT) over an API, focusing on preserving the privacy of training labels. It starts by analyzing the label privacy implications of API fine-tuning with LoRA, a commonly used PEFT algorithm. Empirical results demonstrate that in a split learning setup, LoRA may leak the client’s training labels. Specifically, the unprotected transmission of gradients, model parameters, and activations in split learning can expose training labels to privacy attacks. To address this vulnerability, the paper introduces the $\text{P}^3\text{EFT}$ (privacy-preserving parameter-efficient fine-tuning) framework. $\text{P}^3\text{EFT}$ employs private backpropagation and obfuscates learned activations to protect label privacy by securing activations and gradients during communication between client and server. In their PEFT experiments, the paper shows that $\text{P}^3\text{EFT}$ achieves better label privacy with a small reduction in utility compared to previous split learning methods. Privacy leakage is measured using metrics such as Spectral attack AUC, Norm attack AUC, and k-means accuracy.

### Strengths
1) Although $\text{P}^3\text{EFT}$ is based on the analysis of LoRA, its approach can be applied to any PEFT method aiming to address label privacy in split learning during PEFT over an API.

2) The concept of private backpropagation leverages the conditional linearity of the backpropagation operator, which, while conceptually similar to the secure aggregation protocol used in horizontal federated learning, is well-suited for the vertical FL setting of this problem. This approach can also extend to other vertical FL or split learning scenarios requiring gradient propagation through an untrusted party and is adaptable for future algorithms.

3) $\text{P}^3\text{EFT}$ performs significantly better than existing PEFT methods in preserving label privacy, with only a minor drop in accuracy. Moreover, compared to the distance correlation defense (DC), another privacy-aware algorithm, $\text{P}^3\text{EFT}$ achieves superior label privacy, making it a strong choice for API-based PEFT scenarios.

### Weaknesses
1) While label privacy in $\text{P}^3\text{EFT}$ is evaluated using metrics such as Spectral attack AUC, Norm attack AUC, and k-means accuracy, demonstrating strong performance on these measures, it lacks a formal theoretical guarantee (e.g., differential privacy). Although differential privacy is mentioned as providing loose upper bounds on potential privacy leakage, establishing a theoretical privacy guarantee for $\text{P}^3\text{EFT}$ would enhance understanding of privacy leakage and offer a more solid theoretical basis for fair comparisons with other label privacy-focused algorithms.

2) This paper addresses label privacy in PEFT over an API within an "honest but curious" attacker model, making it a unique but somewhat limited scenario in terms of generality. Analyzing cases where the server is not "honest" would provide a broader perspective, especially given the emphasis on worst-case privacy scenarios in the paper. Additionally, extending the framework to protect both input and label privacy would be a natural generalization, though it appears challenging to adapt $\text{P}^3\text{EFT}$ for this purpose.

3) Some references in the paper would benefit from clarification. For instance, line 52 refers to private multi-party fine-tuning methods that support a narrow class of fine-tuning algorithms but does not specify which algorithms fall within this scope and which do not. Similarly, line 132 states that differential privacy upper bounds are loose and do not align with practical observations on real models, but it lacks a reference or supporting argument, leaving some statements unclear.

4) There are a few minor writing issues, including a formulation error, which I have included in the question section for reference.

### Questions
1) In line 237, it is stated that leaving gradients, activations, or parameters unprotected would compromise label privacy. While $\text{P}^3\text{EFT}$ obfuscates gradients and activations, it is unclear why parameters do not require similar privacy measures in the context of this paper.

2) In line 266, it appears that the expression $\text{backprop}(x, \theta, g_h)$ should be written as $\frac{1}{2} \Bigl( \text{backprop}(x, \theta, g_h + z) + \text{backprop}(x, \theta, g_h - z) \Bigr)$ instead of $\Bigl( \text{backprop}(x, \theta, g_h + z) + \text{backprop}(x, \theta, g_h - z) \Bigr)$. Could you confirm if this is correct?

3) Regarding Algorithm 1, did you study the effects of different noise levels in the private backpropagation algorithm? Does this imply that $\text{P}^3\text{EFT}$ would yield the same utility across various noise levels?

4) In line 479, it is mentioned that $\text{P}^3\text{EFT}$ achieves the same accuracy at a given privacy level. However, it is unclear what “same level of privacy” specifically means, given that the privacy metrics in Tables 1 and 2 differ for DC and $\text{P}^3\text{EFT}$.

5) Finally, in line 503, how is the privacy-accuracy trade-off precisely defined? It would be helpful to clarify this term—if it refers to an average measure of privacy and utility, please specify, as the term “trade-off” here is ambiguous without further explanation.

6) Here are some minor spelling errors:
line 326: it's 
line 478: $\text{P}^3\text{FT}$
line 484: both both our algorithm

### Soundness
2

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
4

### Summary
This work analyzes privacy-preserving fine-tuning of LLMs in the context of parameter-efficient fine-tuning and the two-party split learning setting. The authors show empirically that ordinary fine-tuning reveals sensitive label and successfully alleviates this privacy risk by obfuscating the back propagated gradient using forward and backward API. Experiments on 3 datasets are done.

### Strengths
This paper focuses on a very practical scenario and attempts to address an importance and realistic privacy issue. Also, I like the visualization of the of top-2 principal components of gradients and activations from different fine-tuning steps before and after the defense is applied which directly demonstrated the effectiveness of the proposed method.

### Weaknesses
1. The writing of the paper needs to be improved. For example, the last sentence in the abstract is hard to understand. "We find that P3EFT is competitive with existing privacy-preserving methods in multi-party and two-party setups while having higher accuracy." What is competitive when higher accuracy is achieved.
2. Experimental datasets are inadequate. Only classification datasets are used although generation task is also mentioned in the paper.
3. Aside from label privacy, I believe sample input privacy is also important. However, this work exposed the input samples completely to the LLM. I expect that the authors chould provide a proper real-world setting in which only label information but not input features are sensitive and should be protected.

### Questions
1. As I know, some closed-source model training API requires uploading the whole training dataset to the server. Is the proposed method able to preserve the privacy of label under this setting? If not, what might can be done to address this case?

### Soundness
3

### Presentation
2

### Contribution
2
