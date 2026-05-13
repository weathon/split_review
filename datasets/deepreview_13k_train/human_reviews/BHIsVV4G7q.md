# Phantom: General Trigger Attacks on Retrieval Augmented Language Generation

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Retrieval Augmented Generation (RAG) expands the capabilities of modern large language models (LLMs), by anchoring, adapting, and personalizing their responses to the most relevant knowledge sources. It is particularly useful in chatbot applications, allowing developers to customize LLM output without expensive retraining.
Despite their significant utility in various applications, RAG systems present new security risks. In this work, we propose new attack vectors that allow an adversary to inject a single malicious document into a RAG system's knowledge base, and mount a backdoor poisoning attack.
We design \atkname, a general two-stage optimization framework against RAG systems, that crafts a malicious poisoned document leading to an integrity violation in the model's output.
First, the document is constructed  to be retrieved only when a specific trigger sequence of tokens appears in the victim's queries. 
Second, the document is further optimized with crafted adversarial text that induces various adversarial objectives on the LLM output, including refusal to answer, reputation damage, privacy violations, and harmful behaviors.
We demonstrate our attacks on multiple LLM architectures, including Gemma, Vicuna, and Llama, and show that they transfer to GPT-3.5 Turbo and GPT-4. Finally, we successfully conducted a Phantom attack on NVIDIA's black-box production RAG system, "Chat with RTX".

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Phantom, a framework that proposes a novel attack on Retrieval-Augmented Generation (RAG) systems by injecting malicious documents into their knowledge bases, which are then retrieved by specific trigger sequences to manipulate outputs. The attack utilizes a two-stage optimization process: firstly, crafting a document that aligns with the RAG's retrieval mechanics when triggered, and secondly, generating text to induce specific adversarial outcomes like misinformation or refusal to answer. Extensive experiments demonstrate the effectiveness of Phantom across various large language models and datasets, revealing vulnerabilities in both proprietary and open-source RAG implementations. The paper also discusses potential mitigations, stressing the challenge of balancing system security with the utility of RAG systems in real-world applications.

### Strengths
- The experiments of this paper are extensive.
- The security of the RAG system is an important topic.

### Weaknesses
1. The threat model lacks clarity, particularly regarding the attacker's capabilities. Line 153 suggests the attacker does not need knowledge of other documents to initiate the attack. However, the Multi-Coordinate Gradient (MCG) technique described on lines 274-275 requires access to the top-k passages retrieved in response to m user queries. These passages, presumably from the RAG databases, are crucial for optimization. Appendix A.3.5 explores transferability between different datasets, implying the use of a consistent dataset (MS MARCO) for both optimization and attack phases. This suggests that the attacker must have knowledge of the RAG database to effectively deploy the MCG technique.

2. The paper lacks a comprehensive comparison with prior works. Generating malicious passages retrievable exclusively by queries with specific triggers has been explored by [1], and inducing target outputs in LLMs using suffix generation has been studied by [2]. This paper does not compare its methods against [1] concerning Retrieval Failure Rate, nor does it compare attack success rates with [2]. Additionally, the authors should consider citing [2], which introduces a bi-level optimization for generation and retrieval conditions and employs gradient-based optimization to concatenate strings for retrieval and generation.

3. The novelty of the second method (MCG) appears limited. It is primarily a variant of the GCG with modifications only detailed in lines 7-8. Although MCG reportedly outperforms GCG, the reasons for this improvement and the rationale behind this incremental change are not well-explained.

4. The loss modeling for MCG is problematic. Equation 2 assumes that only one passage is retrieved and used as input for the generator. However, typical RAG applications retrieve multiple passages for context. Notably, Appendix A.2.26's Table 9 shows that the position of $S_{gen}$ significantly affects its efficacy, with prefixes performing better than suffixes. In scenarios where multiple passages are retrieved, there's no guarantee the malicious passage will be at the top-1 position, undermining the experiment's validity if $S_{gen}$ is not the prefix of the entire context. Why the string $S_{gen}$ optimized on a single passage could be effective in multiple passage settings is not clear to me

5. There is a noticeable absence of experiments involving other retrievers such as DPR, BGE, REALM, or ORQA. While the paper discusses the retrieval failure rate on DPR in the appendix, it does not present end-to-end attack success rates for these retrievers in RAG systems. The high retrieval failure rates on other retrievers besides Contriever suggest limited practicality and effectiveness of the attacks.

6. Could the authors provide explanations for the high retrieval failure rates observed with DPR and Contriever-MS? It is particularly puzzling for Contriever-MS, a version of Contriever fine-tuned on the MS MARCO dataset, to show a significant performance discrepancy compared to its base model.

7. The paper discusses an attack against the Chat RTX without detailed knowledge of its retriever. Given the poor transferability between retrievers noted in lines 1105-1107, the successful attack using Contriever on the black-box Chat RTX system is perplexing. Could the authors provide the specific success rates achieved against it?

### Questions
Please refer to the weakness part.

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
5

### Summary
Retrieval Augmented Generation (RAG) enhances the capabilities of modern large language models (LLMs), but also provides new vectors for attackers. This paper investigates mounting a backdoor poisoning attack by injecting a single malicious document into a RAG system’s knowledge base. Specifically, the paper proposes a two-stage optimization framework to optimize the injected malicious document, with the first optimization goal being to be retrieved only when a specific trigger sequence of tokens appears in the victim’s query, and the second goal being to induce various adversarial objectives on the LLM output.

### Strengths
1. The study examines multiple attack objectives against RAG systems, such as Refusal to Answer, Biased opinion, Harmful Behavior, Passage Exfiltration, and validates them through extensive experiments.
2. The paper attacks a commercial black-box RAG system, NVIDIA’s Chat-with-RTX, and demonstrates that the attack achieves various objectives.
3. This paper is well-written and well-organized.

### Weaknesses
1. The technical contribution is not substantial enough. The paper's two-stage optimization framework is based on two existing optimization algorithms, HotFlip and GCG. Even though some improvements have been made for the attack scenario, the gap in technical contribution is not significant.
2. Lacks baselines. Although the paper proposes a new threat model of backdoor poisoning in untrusted RAG knowledge bases, straightforward baselines should be set for comparison to demonstrate the superiority of the proposed method. For example, [1], although this method is not optimized for manipulating LLM generation, it can also manipulate the subsequent behavior of the LLM by pre-defining the semantics of the retrieved malicious text.

### Questions
Please see the weaknesses for details.

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
5

### Summary
This work focuses on the potential backdoor attacks on RAG. The authors propose an attacking method that inserts malicious data into the databases used in RAG, optimizes the data for retrieval and induces malicious behaviors. Experiments are conducted on various models and datasets including an application ChatRTX.

### Strengths
This work reveals an important threat that may compromise the performance of RAG. Multiple malicious behaviors are considered and evaluated. The optimization objectives are well formulated and explained. The empirical results look promising.

### Weaknesses
1. **Threat model**
* The threat model of local deployment and local file system is confusing and lacks practicality. Local files of the user's own are usually private and it is hard to imagine what kind of attacker can access and insert something into it. Though the authors mention something harmful like spam emails, they are usually taken care of before leveraging them in the system. The authors take for grant that malicious contents can be inserted into the database used in RAG, but I personally believe insertion itself is hard to either justify or conduct. The threat model should be more clearly and properly justified.
* When optimizing the tokens for retrieval, the embedding of retriever is assumed to be accessible to attackers, which can be a strong assumption. I would expect a more practical scenario that both retrievers and generation models are black-box and attackers can adopt some open-source models to craft examples. The totally black-box setting needs to be discussed either with empirical evaluations or explicitly discussing the implications and limitations of the current assumptions.

2. The design of s_ret and s_gen seems to be not imperceptible and is easy to detect. According to Section 4, s_ret and s_gen are sequences of tokens optimized by HotFlip and MCG respectively. Since there are no constraints to ensure the semantic meaningful, the optimized sequences can be full of non-meaningful strings. I can imagine that the perplexity score can also be much higher than ordinary content, which makes this attack easy to defend. This can be even more serious if the length of strings is getting longer. Moreover, the authors append many additional contents to the original query (s_ret, s_gen, s_cmd), the robustness of injected content can be very poor. Some case studies on the backdoored content should be provided.

3. The proportion of backdoored content in the database should be mentioned in the experiment part. I believe this proportion can be an important factor influencing both retrieval rate and final success rate. Ablation study on this proportion can help.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2
