# FARS: FSM-Augmentation to Make LLMs Hallucinate the Right APIs

- Decision: Reject
- Scores: 6, 6, 8

## Abstract
Large Language Models (LLMs) have shown remarkable ability to converse with humans and solve a wide range of tasks. They have also been extended to make use of external tools or services through API calls. This is commonly achieved by fine-tuning the model, or with the use of in-context learning, where instructions and descriptions of those external APIs, along with examples of how to call them, are given to the LLM via its prompt. Given the limited context available in the LLM prompt and other latency constraints, scaling up to a large number of tools is challenging and requires the help of an external shortlisting process to prepare instructions and examples from a large number of APIs to a smaller set of relevant ones. In this work, we propose a new way for an LLM to generate the right API calls without the need to shortlist instructions or examples. Rather, we do this by allowing the LLM to hallucinate meaningful output while grounding the generation to an available set of APIs using a finite state machine-based constrained decoding algorithm. We call our approach FARS (FSM-Augmentation to make LLMs hallucinate the Right APIS). FARS allows us to ground LLMs to a large set of APIs with semantically meaningful names without using an external retriever or exemplars. We also demonstrate that with FARS, LLMs can seamlessly switch between conversation and API calling during multi-turn dialogs. We show that this can be achieved without any additional fine-tuning over the standard instruction tuning typically performed to train LLMs. This allows us to pave the way to build a truly powerful AI assistant using LLMs. We demonstrate the effectiveness of FARS for API calling on two public task-oriented API datasets: SNIPS and MultiWOZ, and a very challenging in-house Smart Home Control dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel approach called FSM-Augmentation to make Language Models generate correct API calls by grounding their output in a Finite State Machine that describes valid API calls. This method, FARS, aims to address the issue of LLMs "hallucinating" plausible but incorrect API calls by using a constrained decoding algorithm based on FSM.

FARS's approach allows for the dynamic selection of API arguments and free-text values, improving upon traditional methods that rely on fixed argument orders. The FSM design enables the LLM to predict the order and subset of arguments, enhancing flexibility and accuracy.

### Strengths
1. The paper introduces a finite state machine-augmented approach, which is an improvement over traditional LLMs that often hallucinate plausible but incorrect API calls. By grounding the LLM's generation process in a finite state machine, the model is constrained to produce only valid API calls, which is a practical solution to a common problem in LLM outputs.

2. No Need for External Retrievers: Unlike other methods that rely on external retrievers or exemplars to guide the generation of API calls, FARS operates independently by incorporating the API catalog information into the FSM. This reduces the complexity and potential points of failure associated with external dependencies.

### Weaknesses
1. The effectiveness of FARS is contingent on the FSM's knowledge of the available API catalog. The paper does not detail the process of updating the FSM when new API functions are added or existing ones are modified. A comprehensive explanation of the FSM update mechanism, including its automation and potential impact on real-time performance, is crucial for assessing the practicality of FARS in dynamic environments.

2. Potential Overhead during inference. The paper briefly mentions the construction of the FSM but lacks a detailed analysis of the computational overhead introduced during inference. Specifically, how does the complexity of the FSM, determined by the number of states and transitions, affect the latency of generating API calls? A quantitative comparison of the inference speed between FARS and an unconstrained LLM baseline, across varying FSM complexities, would provide valuable insights into the trade-offs between accuracy and efficiency.

3. The scope of the paper's evaluation is limited to the Vicuna-33B model's performance on specific datasets (SNIPS and an internal smart home dataset). A broader assessment across various models, including those with different architectures and training paradigms, is needed to establish the generalizability of FARS. Furthermore, the evaluation should encompass a wider range of API complexities and domains to ascertain the robustness of the proposed approach.

### Questions
1. What is the retrieval model used in API retrieval setting?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new approach called FARS to enable Large Language Models (LLMs) to generate the right API calls without the need for shortlisting instructions or examples. The approach uses a finite state machine-based constrained decoding algorithm to ground the generation of LLMs to a set of available APIs. The paper demonstrates the effectiveness of FARS on three datasets - SNIPS, MultiWOZ, and a Smart Home Control dataset, showing significant improvements over an unconstrained LLM.

### Strengths
1) The paper introduces a novel approach to address the problem of generating the right API calls without shortlisting instructions or examples.
2) The use of a finite state machine-based constrained decoding algorithm provides a structured and grounded approach to API generation.
3) The experimental results on the three datasets demonstrate the effectiveness of FARS, showing significant improvements over an unconstrained LLM.

### Weaknesses
1) The paper could provide more details on the implementation of FARS, including the specific steps and algorithms used to integrate the finite state machine with the LLM. For instance, the paper does not specify how the states and transitions of the finite state machine are defined and represented. It would be helpful to elaborate on how the FSM is constructed from the API specifications and how it interacts with the LLM during the decoding process. What are the specific criteria used to determine valid transitions within the FSM during generation? How does the system handle potential conflicts or ambiguities when multiple valid API calls are possible? More elaboration on the mechanism for selecting the most appropriate API call in such scenarios would be useful.
2) The paper lacks a thorough discussion of the limitations and potential future directions of the proposed approach. Specifically, the paper does not address how FARS would handle APIs from unknown domains or how it could be extended to incorporate new APIs dynamically. Additionally, the paper does not analyze the model's ability to conditionally choose to engage the FSM, which could be crucial in scenarios where API calls are not always necessary.

### Questions
see weaknesses

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Generative models may hallucinate APIs when generating their responses. To this end, this paper proposes FARS to use constrained decoding to limit the token selection during API calls, making LLMs generate desired API formats. Specifically, the authors construct a finite state machine to enforce the decoding to follow the structure Begin-API-Argument-Value-End and limit the number of available tokens to the number of designed states (e.g., # APIs when generating APIs).  The implementation is based on the dynamic trie implementation to save the space cost. Experiments show the effectiveness of FARS compared with unconstrained LLMs.

### Strengths
1. FARS is a novel approach that involves an inference-time intervention to enforce LLMs to generate the correct API formats
2. The approach is sound and well-illustrated.
3. Experiment results show the improvement is quite apparent.

### Weaknesses
1. Lack of wall time analysis. I am not sure if this method will bring much extra time cost since the approach seems to involve many CPU operations. It will be good to add a wall time comparison.
2. The approach is more like eliminating "syntax" error but not "semantic" error. Will FARS eliminate "syntax" error but increase "semantic" error? For example, the function is originally semantically correct but with a wrong format, whereas FARS corrects the syntax but brings semantic errors. It will be good to see how much performance is obtained by "syntax" correction and if FARS introduces more "semantic" errors.
3. Lack of some implementation details. Please see questions for details.

### Questions
What temperature is used in the experiments? The comparison may be less convincing if the temperature is high for baseline models.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
