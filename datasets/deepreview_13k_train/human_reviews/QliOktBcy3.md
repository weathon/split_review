# MPCache: MPC-Friendly KV Cache Eviction for Efficient Private LLM Inference

- Decision: Reject
- Scores: 6, 3, 8, 3

## Abstract
Private LLM inference based on multi-party computation (MPC) offers cryptographically-secure protection for both user prompt and proprietary model weights. However, it suffers from large latency overhead for long input sequences. While key-value (KV) cache eviction algorithms have been proposed to reduce the computation and memory cost for plaintext inference, they are not designed for MPC and may even introduce more overhead. In this paper, we propose an accurate and MPC-friendly KV cache eviction framework, dubbed MPCache. MPCache is built on the observation that historical tokens in a long sequence may have different effects on the downstream decoding. Hence, MPCache combines a look-once static eviction algorithm to discard unimportant tokens and a query-aware dynamic selection algorithm to further choose a small subset of tokens for attention computation. As existing dynamic selection algorithms incur too much latency, we propose a series of optimizations to drastically reduce the KV cache selection overhead, including MPC-friendly similarity approximation, hierarchical KV cache clustering, and layer-wise index sharing strategy. With extensive experiments, we demonstrate that MPCache consistently outperforms prior-art KV cache eviction baselines across different LLM generation tasks and achieves 1.8 ∼ 2.01× and 3.39 ∼ 8.37× decoding latency and communication reduction on different sequence lengths, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a framework that makes KV-caching more "MPC-friendly", for use in the context of privacy-preserving LLM inference. Concretely, KV caching is a commonly used technique to reduce the amount of work when dealing with long input sentences in LLMs. In the MPC context, both the model and input sentence are private, and inference is carried out by an interactive protocol among the parties. Unfortunately, existing KV caching techniques still require several operations that, although cheap to execute "in the clear" (that is, when both the model and the input query are known locally), it is much harder to compute distributedly using an MPC protocol, since it uses operations that are difficult to carry out in MPC. The contribution of this paper is to design several methods that enable KV caching in MPC (that is, when both model and input query are secret). Concretely, the authors propose a mix of "static eviction", which eliminates some of the operations in a data-independent manner, followed by a more data-dependent (i.e. dynamic) eviction method, which compared to usual KV caching is carried out over less data and hence it's cheaper.

The authors present experiments that validate the effect of their techniques. They show that this leads to concrete gains in MPC while not affecting accuracy dramatically.

### Strengths
The problem is well motivated. This is part of the general umbrella of enabling private inference on LLMs using cryptographic techniques, and it is widely acknowledged that in general several modifications to the underlying ML algorithms would be required. This paper introduces a series of techniques that enable KV caching in MPC in a efficient manner. The results show improvement w.r.t. using standard KV caching techniques (which are not MPC-friendly). Detailed experiments are presented and implementation is included for reproducibility.

To the best of my knowledge, no explicit work in the direction of privacy-preserving LLM inference has studied explicitly (or even acknowledged) the use of KV caching for improving efficiency. I find the ideas presented in the paper to be interesting and novel, and the experiments to be sound.

### Weaknesses
I am doubtful of the ability of these techniques to generalize to other models. The proposed method involves dropping a huge percentage of the intermediate values, since the authors find out experimentally that they contribute little to the attention heads. However, this study, which is explored deeply in the paper, is highly tailored to a specific model and datasets. This is of course acceptable and it's the usual way to study the viability of new ML techniques. However, in this specific setting the situation is more critical since an actual deployment in a real scenario would likely involve a model that is intended to be private. I don't see a clear way to deploy the techniques involved presented here without performing extensive experimentation that would require knowledge of the model (or at least leaking information about it beyond the architecture).

Overall, to summarize my concerns: I feel the techniques presented here work very well for the model evaluated, but I have no particular reason to believe this would be useful in more realistic settings where both the model and the data are private. Perhaps a scenario where a single party knows the model and also has the data to identify the best "hyper-parameters" for static-eviction would work, but this is not the most general scenario and this is not explored in the paper.

### Questions
What's the exact distributed protocol used for performing the dynamic eviction? My understanding is that this is performed by the parties obliviously, and I understood the description of the algorithm. However, this involves sorting and other complex cryptographic operations. I am unsure the authors describe the exact protocols used for this part.

Can you comment on your thoughts regarding how reasonably your method generalizes, and how it can be used in oblivious settings where the only known aspect of a model is its architecture? (and in particular, it is not possible to benchmark the accuracy of the method).

Suggestion:

* Some citations are inaccurate or missing, particularly when it comes to MPC. The 3PC protocol from Section B.3 is from Furukawa et al (CCS'17). I don't understand why Bumblebee claimed to be the SOTA for 2PC, especially when there are PCGs for non-interactive preprocessing that avoid computational assumptions in the online phase. There is also the Sigma work (SIGMA: Secure GPT Inference with Function Secret Sharing) that does 3PC as well (2PC + preprocessing), and it is not mentioned. In general the work seems to have a bias towards some specific prior works.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors introduce an MPC-friendly KV cache eviction framework, which accelerates the private LLM inference with secure KV cache eviction. The authors first incorporate the look-once static eviction algorithm and the query-aware dynamic selection algorithm to reduce the number of tokens needed for inference. To improve the efficiency of the dynamic selection algorithm, the authors propose several strategies such as MPC-friendly similarity approximation, hierarchical KV cache clustering, and layer-wise index sharing. The experiments show that the proposed methods can improve the latency by 2.01 times and communication by 8.37 times.

### Strengths
1. Protecting user privacy during LLM inference is important. Integrating static and dynamic KV cache eviction methods is a promising direction for improving the efficiency of private LLM inference.
2. The authors present comprehensive experimental results to support their motivation and to show the effectiveness of the proposed methods.
3. Although some technical details can benefit from clearer explanation, the manuscript is overall well-structured and easy to follow.

### Weaknesses
1. Key technical issue. The secure token gathering protocol is the core of MPCache, as MPCache focuses on identifying and removing less important tokens during private LLM inference. However, the proposed token gathering protocol is problematic. While the top-k indices can be turned into a one-hot vector via the secure comparison protocol, directly multiplying the cache tokens with the one-hot vector cannot remove tokens. Instead, parties will learn a token sequence of the same length after running the proposed token gathering protocol. Additionally, no party will know which token should be removed since all tokens are secretly shared. The proposed token gathering protocol is not sound and fails to implement the expected functionality shown in Fig. 14. Since the token gathering protocol is needed for almost all experiments, I am concerned about the soundness of this paper.
2. There is neither a detailed MPC protocol describing the whole secure inference process in MPCache, nor an implementation of the MPC backend in the provided code. Additionally, while the authors argue that MPCache is built upon existing cryptographic primitives, more information is revealed to the parties (e.g., how many tokens in the cache are used). A security analysis or proof is still needed.
3. There are multiple unclear citations. For example, in line 52, the author cited Autorep (ICCV'23) for "replacing non-linear activation functions with more MPC-friendly operators" to "reduce the cost of private LLM inference". Yet, Autorep is not about private LLM inference. In line 592, the author cited Lazyllm, but it does not appear in the main text. While I am aware that these papers are related, clearer citations can enhance the overall presentation.
4. As shown in Fig. 9, MPCache presents better performance than most KV cache eviction methods in the plaintext (both static and dynamic ones). Such results seem to make MPCache a competitive work in plaintext. However, the gains in secure computation do not mainly come from the proposed optimizations. As shown in Fig. 11, the improvement in latency can be largely attributed to the top-k parallel (line 412) and the communication due to the static eviction. The main techniques in Section 4.3 and 4.4 contribute to the end-to-end performance much more marginally when compared with top-k parallel and static eviction.

### Questions
1. The proposed MPCache involves multiple hyperparameters such as $\alpha$ (line 340), $\gamma$ (line 287), the number of adjacent layers affected, and the eviction ratio. How should these parameters be determined in practice? Should they be determined by the client?
2. MPCache mainly focuses on the eviction of the key cache. How does the eviction of the value cache influence the overall performance?
3. How does the parallel top-k protocol differ from that in existing works such as CipherGPT?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a new design for the KV cache in large language models (LLMs) aimed at enhancing compatibility with MPC (multi-party computation) frameworks. It highlights that the existing KV cache design incurs significant latency and communication overhead, making it inefficient for MPC applications.

To address these inefficiencies, the authors propose three main optimizations:
1. Attention-based KV cache eviction: This approach prioritizes efficiency by evicting cache entries based on attention scores.
2. Dynamic KV cache selection algorithm: Optimized to remove operations unsuitable for MPC, this algorithm improves MPC compatibility.
3. Layer-wise index sharing strategy: By sharing indices across layers, this strategy reduces the number of tokens stored, further minimizing overhead.

### Strengths
The paper presents the underlying questions and motivations, offering a clear explanation of the challenges addressed. It includes ample experimental results that demonstrate how the proposed optimizations improve overhead and latency. The structure of the paper makes it easy to follow.

Additionally, the attached appendix provides extensive information and additional experimental results, enriching the reader’s understanding of the work and its impact.

### Weaknesses
I didn’t identify any major weaknesses in this paper. It is well-structured, with sufficient explanations and experimental results to support its findings. Although the main content may be concise, likely due to page limitations, this doesn’t detract from the paper, as the appendix compensates by providing additional, valuable information.

### Questions
Thanks for this contribution. I have 2 questions:

Question 1: In Section 4.3, Hierarchical KV Cache Clustering, could you specify the number of levels (n) selected for clustering in your experiments? Additionally, Figure 6 would benefit from further explanation—could you expand on the section?

Question 2: In Figure 8, I noticed a lower commonality score between layers 6 and 12. Could you explain what might cause this dip? Also, is there any observed performance degradation when applying the sharing strategy in these layers? Any insights into this effect would be helpful.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a solution to accelerate the Key Value cache eviction algorithms for the multi-party-based machine learning inference, so as to secure the inference of LLMs. The proposed method is built on the observation of unique features of long input sequences and dynamic KV cache selection.

### Strengths
This paper does statistical observation over the inference process of LLM models, especially their limits in advancing the inference overhead of a MPC-based LLM.

### Weaknesses
Threat Model: Applying privacy-preserving techniques to large language models (LLMs) is a valuable practice to enhance security and privacy. However, the practical setup is unclear, specifically regarding how secret-sharing is implemented across parties in two-party computation (2PC) or three-party computation (3PC) settings. For instance, could you clarify how the proposed method applies to 2PC, especially in the context of results shown in Figure 13?

Practicality: Current commercial LLMs are known for their substantial model sizes, raising questions about the feasibility of splitting them into different secret-shared components. The reviewer is uncertain whether multi-party computation (MPC) is a practical solution for LLMs under these conditions. Could you provide details on the setup that enables this approach?

Research Motivation: This work aims to integrate privacy-preserving machine learning as a service (MLaaS) with key-value (KV) usage to improve ML inference. However, the reviewer notes that the primary bottleneck in existing privacy-preserving ML research is typically focused on improving efficiency, particularly the low performance associated with non-linear operators. Could you clarify how the Key-Value (KV) approach addresses this performance issue, which is crucial to the MLaaS context? The reviewer believes prioritizing efficiency improvements in MLaaS performance would be more impactful than integrating additional components that excel in their own specialized areas.

Experimental Results: The experimental setup and results provide useful insights into the performance of the proposed solutions. However, the reviewer suggests that these results should be compared to existing work within privacy-preserving MLaaS, rather than solely with other KV cache eviction approaches. The use of KV in this context is intended to enhance MLaaS inference efficiency in 2PC and 3PC settings, where numerous state-of-the-art (SOTA) solutions exist. Therefore, comparing MPCache's performance to other non-KV-based solutions would offer a clearer benchmark, as they represent the current SOTA in this domain.

### Questions
My questions are embedded in the weakness section, please refer to them.

### Soundness
2

### Presentation
3

### Contribution
1
