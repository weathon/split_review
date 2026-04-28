# On Large Language Model Continual Unlearning

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
While large language models have demonstrated impressive performance across various domains and tasks, their security issues have become increasingly severe. Machine unlearning has emerged as a representative approach for model safety and security, removing the influence of undesired data on the target model. However, these methods do not sufficiently consider that unlearning requests in real-world scenarios are continuously emerging, especially in the context of LLMs, which may lead to accumulated model utility loss that eventually becomes unacceptable. Moreover, existing LLM unlearning methods often ignore previous data access limitations due to privacy concerns and copyright protection. Without previous data, the utility preservation during unlearning is much harder. To overcome these challenges, we propose the O3 framework that includes an \underline{\textit{O}}rthogonal low-rank adapter (LoRA) for continually unlearning requested data and an \underline{\textit{O}}ut-\underline{\textit{O}}f-Distribution (OOD) detector to measure the similarity between input and unlearning data. The orthogonal LoRA achieves parameter disentanglement among continual unlearning requests. The OOD detector is trained with a novel contrastive entropy loss and utilizes a glocal-aware scoring mechanism. During inference, our O3 framework can decide whether and to what extent to load the unlearning LoRA based on the OOD detector's predicted similarity between the input and the unlearned knowledge. Notably, O3's effectiveness does not rely on any retained data. We conducted extensive experiments on O3 and state-of-the-art LLM unlearning methods across three tasks and seven datasets. The results indicate that O3 consistently achieves the best unlearning effectiveness and utility preservation, especially when facing continuous unlearning requests. The source codes can be found at \url{https://anonymous.4open.science/r/O3-A02B}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a solution to the Continual Unlearning problem, in which the model provider attempts to continuously erase the influence of requested data. The authors motivate their problem formulation because existing model unlearning methods fail to account for the scenario where the unlearning requests emerge continuously, and the model provider lacks access to previous data. To this end, the authors propose a continual unlearning framework that includes LoRA adapters with orthogonal components to minimize the interference among different unlearning requests, along with an OoD detector that measures the similarity between input and unlearning data to decide on how unlearning LoRAs should be loaded.

### Strengths
1. This paper is well-written and motivated by real-world scenarios that require unlearning.
2. The design choices for the proposed unlearning pipeline are justified through ablation studies.

### Weaknesses
The authors partially motivate machine unlearning as “ a representative approach for model safety and security by removing the influence of undesired data on the target model.” I very much agree with the assertion. However, the evaluations of the proposed methods mainly focus on unlearning knowledge instead of unsafe behaviors. The usefulness of the proposed method could benefit from additional evaluations against safety-oriented unlearning benchmarks such as WMDP [1].

### Questions
How robust is the proposed method against ”targeted relearning attacks”? For example, in a safety-critical scenario, can the supposedly unlearned knowledge be solicited again after finetuning the model on related public datasets? [2]

[2] Hu, S., Fu, Y., Wu, Z.S. and Smith, V., 2024. Jogging the Memory of Unlearned Model Through Targeted Relearning Attack. arXiv preprint arXiv:2406.13356.

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
The authors address significant practical challenges in developing machine unlearning techniques for large language models (LLMs), where current state-of-the-art approaches fall short due to their dependency on retained data and inability to manage continual unlearning requests effectively. To overcome these limitations, they propose the O^3 framework, which introduces an orthogonal low-rank adapter to enable continuous unlearning of requested data and an out-of-distribution detector to assess the similarity between incoming inputs and unlearning data. Comprehensive experiments show that O^3 achieves notably higher unlearning effectiveness and utility preservation than existing methods, all without relying on retained data, even under continuous unlearning conditions.

### Strengths
1. The authors solve the critical challenge of LLM unlearning by getting rid of the access to the retained data. The design of orthogonal LoRA demonstrates significant improvement in evaluation.

2. The authors conduct extensive experiments to evaluate the effectiveness of the proposed O^3 method.

### Weaknesses
1. During the inference, each testing instance x will be fed into all OOD detector backbones. This might limit the method's scalability when the unlearning requests increase due to the higher computational cost. 

2. The experiments focus on the QA datasets, where each query only contains a single knowledge entity to be unlearned. The authors might need to evaluate the framework under more challenging and realistic settings, wherein for each query, there might be multiple knowledge entities to be unlearned. I am concerned about this because the OOD detectors are trained on single unlearning requests.

3. The authors should improve the scale of unlearning requests (more than just 4 requests) to validate the claimed contribution that the O^3 framework can handle continual unlearning settings.

### Questions
See weakness.

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
4

### Summary
This paper presents the O3 framework, designed to address continual unlearning requests in LLMs without relying on retained data, a common limitation in existing methods. The O3 framework integrates an orthogonal low-rank adapter (LoRA) for unlearning requests and an Out-Of-Distribution (OOD) detector for measuring input similarity with unlearned data. The orthogonal LoRA prevents interference across multiple unlearning requests, while the OOD detector leverages a novel contrastive entropy loss and a layer-aggregated scoring mechanism to manage unlearning effectiveness dynamically. Extensive experiments demonstrate O3’s superior balance between unlearning effectiveness and utility preservation, particularly in continuous unlearning scenarios. Compared to state-of-the-art methods, O3 shows promising results in reducing computational costs and maintaining model utility across various tasks, such as question answering and intent classification.

### Strengths
This paper addresses the LLM unlearning from the continual unlearning perspective.
This unlearning process does not need the retained data.

### Weaknesses
The proposed LLM unlearn methods LORA and OOD detector does not exactly unlearn the knowledge from the LLMs. They are just like two modules externally mounted outside the LLM and block the input and output of the LLMs related to the unlearn targets. This approach raises concerns about whether the model truly forgets the information or merely prevents access to it. The reliance on an external OOD detector, while practical, might not address the core issue of knowledge removal from the model's parameters. The orthogonal LoRA, while mitigating interference, still operates as an add-on, potentially leaving the original model's knowledge intact. This raises questions about the long-term effectiveness and robustness of this approach, especially if the external modules are bypassed or fail.

### Questions
1. With fine-tuning unlearning methods, why is retained data not acceptable? This directly reflects the paper's motivation.
2. this work's novelty seems insufficient, with LORA and OOD blocking the input/output of the LLM.
3. If the model did not really forget the data distribution in the proposed method, is this method vulnerable to attack methods?

### Soundness
2

### Presentation
2

### Contribution
2
