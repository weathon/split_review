# CodeCipher: Learning To Obfuscate Source Code Against LLMs

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
While code large language models have made significant strides in AI-assisted coding tasks, there are growing concerns about privacy challenges. The user code is transparent to the cloud LLM service provider, inducing risks of unauthorized training, reading, and execution of sensitive code. Such fear of data leaking prevents developers from submitting their code to LLMs. 
In this paper, we propose \ourmethod, a novel method that perturbs privacy from code while preserving the original response from LLMs. \ourmethod transforms the LLM's embedding matrix so that each row corresponds to a different word in the original matrix, forming a token-to-token confusion mapping for obfuscating source code. The new embedding matrix is optimized through minimizing the task-specific loss function. To tackle the challenge from the discrete and sparse nature of word vector spaces, \ourmethod adopts a discrete optimization strategy that aligns the updated vector to the nearest valid token in the vocabulary before each gradient update. 
We demonstrate the effectiveness of our approach on three AI-assisted coding tasks including code completion, summarization, and translation. Results show that our model successfully confuses the source code while preserving the original LLM's performance.\footnote{Code and data available at \url{https://anonymous.4open.science/r/CodeCipher_final-9D7E/}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces CodeCipher, a new learning-based code obfuscation technique tailored for LLMs. 

CodeCipher safeguards code from unauthorized training, reading, compiling, and execution, without sacrificing LLM service quality. 

The main idea behind CodeCipher is to transform the LLM’s embedding matrix so that each row corresponds to a different word in the original matrix. This process creates a token-to-token confusion mapping, which the system uses to obfuscate tokens when encountering new code snippets.

### Strengths
The idea of using a token-to-token confusion mapping is interesting.

The efficacy of the proposed approach was assessed across three AI-assisted coding tasks: code completion, code summarization, and code translation.

Results revealed that the proposed method surpassed a range of conventional obfuscation methods in terms of both the level of confusion and the preservation of performance for downstream tasks.

### Weaknesses
Only rule-based baselines are compared.

More related techniques need to be mentioned and compared, such as:

Cryptography-based Approaches (e.g., Homomorphic Encryption, Multi-Party Computation, Functional Secret Sharing, Differential Privacy in Inference):

W.-j. Lu, Z. Huang, Z. Gu, J. Li, J. Liu, K. Ren, C. Hong, T. Wei, and W. Chen, “Bumblebee: Secure two-party inference framework for large transformers,” Cryptology ePrint Archive, 2023.

I. Zimerman, M. Baruch, N. Drucker, G. Ezov, O. Soceanu, and L. Wolf, “Converting transformers to polynomial form for secure inference over homomorphic encryption,” arXiv preprint arXiv:2311.08610, 2023.

X. Liu and Z. Liu, “Llms can understand encrypted prompt: Towards privacy-computing friendly transformers,” arXiv preprint arXiv:2305.18396, 2023.

Detection-based Approaches (e.g., Direct Detection, Contextual Inference Detection):

S. Kim, S. Yun, H. Lee, M. Gubri, S. Yoon, and S. J. Oh, “Propile: Probing privacy leakage in large language models,” 2023.
N. Mireshghallah, H. Kim, X. Zhou, Y. Tsvetkov, M. Sap, R. Shokri, and Y. Choi, “Can llms keep a secret? testing privacy implications of language models via contextual integrity theory,” 2023.

Hardware-based Approaches (e.g., Data Locality, Confidential Computing with Trusted Execution Environment (TEE)):

Y. Wang, Y. Lin, X. Zeng, and G. Zhang, “Privatelora for efficient privacy preserving llm,” arXiv preprint arXiv:2311.14030, 2023.

T. South, G. Zuskind, R. Mahari, and T. Hardjono, “Secure community transformers: Private pooled data for llms.” 2023.

W. Huang, Y. Wang, A. Cheng, A. Zhou, C. Yu, and L. Wang, “A fast, performant, secure distributed training framework for large language model,” arXiv preprint arXiv:2401.09796, 2024.

### Questions
Can the proposed idea be applicable and scalable for state-of-the-art code generation models? How does the proposed idea work on state-of-the-art code generation models?

Jingxuan He, Martin Vechev. Large Language Models for Code: Security Hardening and Adversarial Testing. 2023. In CCS. https://arxiv.org/abs/2302.05319.

Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2023. CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis. In ICLR. https://arxiv.org/
abs/2203.13474

Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2023. InCoder: A Generative Model for Code Infilling and Synthesis. In ICLR. https://arxiv.org/
abs/2204.05999

Loubna Ben Allal, Raymond Li, Denis Kocetkov, Chenghao Mou, Christopher Akiki, Carlos Muñoz Ferrandis, Niklas Muennighoff, Mayank Mishra, Alex Gu, Manan Dey, et al. 2023. SantaCoder: Don’t Reach for the Stars! CoRR
abs/2301.03988 (2023). https://arxiv.org/abs/2301.03988

### Soundness
3

### Presentation
3

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
**Summary:**

This paper studies the way of obfuscating source code for LLMs.  The proposed approach transforms the LLM’s embedding matrix so that each row corresponds to a different word in the original matrix, forming a token-to-token confusion mapping for obfuscating source code. The paper introduce a discrete optimization strategy that aligns the updated vector to the nearest valid token in the vocabulary before each gradient update.

### Strengths
**Strengths:**

- The paper proposed a novel approach to obfuscate the code.
- The proposed approach can preserve better performance than other code obfuscation methods.

### Weaknesses
**Weaknesses:**

- Missing important metrics and SOTA baselines for privacy protection
- Missing extensive experiments on the discrete gradient search

### Questions
**Questions:**

- As the line 100 described, the application of code obfuscation are twofold. One is for privacy protection, and another one is for the robustness of code language models. Since the method is not aimed at improving the robustness of the code language model, why not use privacy protection metrics(i.e. TopK, which is a token-level metric that measures the percentage of correct words in the attacker's top k predictions)? You use the obfucation degree to measure the performance. How can you prove the effectiveness of privacy protection?
- In line 272, you compared  with an identifier renaming approach(Chakraborty et al., 2022). This approach is about naturalizing source code can enhance the performance of generation on three tasks.   Why do you use this approach which is unrelated with code obfuscation? And why it's performance decrease in your experiments? TextObfuscator is a SOTA approach for preserving inference privacy. Why don't you compare with it?

- In Figure 5(b), the obfuscated code still has tokens like "password" which is in the original code, how can you ensure the user's password "securePassword123" will not show in the obfuscated code?

**Minor comments:**

- In Table 1, the "Origin" method is not defined.
- In Figure 6, missing the references of other LLMs(i.e. deepseekcoder)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes CodeCipher, which perturbs privacy from code while preserving the original response from LLMs. CodeCipher transforms the LLM’s embedding matrix so that each row corresponds to a different word in the original matrix, forming a token-to-token confusion mapping for obfuscating source code. The new embedding matrix is optimized through minimizing the task-specific loss function. CodeCipher is evaluated on three AI-assisted coding tasks including code completion, summarization, and translation. Results show that CodeCipher successfully confuses the source code while preserving the original LLM’s performance.

### Strengths
This paper addresses the important research problem of preserving code privacy when submitting code to LLMs. It introduces an interesting approach to achieve this by transforming the LLM’s embedding matrix into a new one, creating a token-to-token confusion mapping that obfuscates the source code.

The effectiveness of the proposed approach is demonstrated through three code analysis tasks.

### Weaknesses
The feasibility of CodeCipher depends on access to the LLM's embeddings, which raises some concerns. First, if the LLM is closed-source, are the embeddings accessible? Could the authors clarify this? Second, if the LLM is open-source, I question whether the proposed approach is necessary. With access to trained LLMs for local execution, code privacy may no longer be a significant issue.

Second, adaptive attacks are not discussed in this paper. If an attacker understands how the approach works, could they potentially generate the confusion mapping themselves and deobfuscate the obfuscated code?

### Questions
1. Discuss how to obtain LLM's embeddings if LLMs are closed-source.
2. Clarify the motivation of CodeCipher when LLMs are open-source. 
3. Discuss adaptive attacks.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces CodeCipher, a method designed to transform input code sequences into an obfuscated format to mitigate the risk of data leakage when using cloud-based large language models (LLMs). Specifically, the approach modifies the embedding matrix of the LLM, ensuring that each row corresponds to a different word for the purpose of obfuscation. To optimize this transformation, a discrete gradient search algorithm is employed, leveraging the vector representation of the nearest word. Extensive experiments, including performance preservation, privacy protection, ablation studies, and transferability assessments, validate the effectiveness of the proposed technique.

### Strengths
- The research problem is interesting. With the wide use of LLMs, the security problem is essential.
- The evaluation is from different aspects, which is good.

### Weaknesses
- The performance of the obfuscated models has an evident decrease compared with the original models across three tasks in Section 5.2. 
- Some important technical details are missing, especially in the discrete gradient search algorithms. Why is single gradient computation inadequate? What is the motivation behind using the nearest valid token, and how do we get the nearest? The motivation part of the proposed algorithm can be strengthened.
- The prompt used is casual and does not have a rigorous design.
- The analysis of the transferability is weak. The ability to generalize is an interesting and important finding. However, more analysis should be discussed to explain why it works across closed models.

### Questions
- In Section 5.2, why only choose 200 samples from 2 million samples of CodeSearchNet and how to get the compilation rate using code snippets?
- Will performance be affected by the training epochs?  How to get the best hyper-parameters?

### Soundness
2

### Presentation
2

### Contribution
2
