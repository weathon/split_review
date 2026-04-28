# On-Device Collaborative Language Modeling via a Mixture of Generalists and Specialists

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
On-device LLMs have gained increasing attention for their ability to enhance privacy and provide a personalized user experience. 
To facilitate learning with private and scarce local data, federated learning has become a standard approach, though it introduces challenges related to system and data heterogeneity among end users. As a solution, we propose a novel \textbf{Co}llaborative learning approach with a \textbf{Mi}xture of \textbf{G}eneralists and \textbf{S}pecialists (CoMiGS), being the first to effectively address both. Our approach distinguishes generalists and specialists by aggregating certain experts across end users while keeping others localized to specialize in user-specific datasets. A key innovation of our method is the bi-level optimization formulation of the Mixture-of-Experts learning objective, where the router is updated using a separate validation set that represents the target distribution. CoMiGS effectively balances collaboration and personalization, as demonstrated by its superior performance in scenarios with high data heterogeneity across multiple datasets. By design, our approach accommodates users' varying computational resources through different numbers of specialists. By decoupling resource abundance from data quantity, CoMiGS remains robust against overfitting—due to the generalists' regularizing effect—while adapting to local data through specialist expertise.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces an approach for collaborative, on-device language modeling based on Federated Learning. It addresses the challenges of system and data heterogeneity, common in federated learning configurations. The focus is on language modeling tasks, specifically MoE-based LLMs using LoRA. The novelty lies in a bi-level optimization formulation for the MoE learning objective, which effectively balances collaboration and personalization. This approach is particularly advantageous in scenarios with high data heterogeneity across multiple datasets and use cases.

### Strengths
- Well-written paper. Nicely structured, well motivated, and easy to follow. Overall, excellent presentation.
- I appreciate the effort to publish the code, together with the submission, while preserving their anonymity. This is not always the case. In addition, the code is of high quality.
- While the approach that the authors have followed is simple, it is highly practical and demonstrates an effective balance when addressing data and system heterogeneity.
- Carefully chosen baselines to compare the performance.

### Weaknesses
 - My biggest concern is regarding the significance of its contribution, especially considering the heavy overlap with the listed related work "pFedMoE: Data-Level Personalization with Mixture of Experts for Model-Heterogeneous Personalized Federated Learning". I understand that the authors have clearly and fairly mentioned the differences. However, I can't deny that the other work is stealing some of its contributions.
- I would have expected a theoretical analysis section in such a paper. Instead, all results and discussions are derived from simulations. The lack of theoretical backing makes it difficult to ascertain the convergence properties of the proposed bi-level optimization, especially given the alternating update scheme for theta and fi. This is a significant limitation, as it leaves the reader unsure about the conditions under which the algorithm is guaranteed to converge to a meaningful solution.
- While I said the manuscript is very well written, I do think it is missing some background work that would make it easier to follow. For instance, a few sentences about what MoE is, what the router is, and its role, what is LoRA, etc. I am aware of the space limit, but I felt that this was missing from the paper. The absence of these definitions makes the paper less accessible to readers who are not already familiar with these concepts.
- Similar to the previous comment, it is missing some (more generic) relevant related works on the topic of addressing system and data heterogeneity during FL configurations. I understand that this work is focused on language modeling tasks; however, I believe the authors should mention (at least briefly in 1-2 lines) a few examples in more classical DNN (non-LLM) scenarios. Some examples:
  * Fjord: Fair and accurate federated learning under heterogeneous targets with ordered dropout (Horvath et al.)
  * Revisiting Sparsity Hunting in Federated Learning: Why does Sparsity Consensus Matter? (Babakniya et al.)
- The authors mention privacy as the motivation of using on-device LLMs (that's fair for sure), but also when applying FL. There are numerous attacks on the FL space that render such claims unrealistic, and perhaps such claims should be phrased more cautiously. The paper should acknowledge the potential for privacy breaches in FL, such as inference attacks, and clarify that FL provides a degree of privacy, but not complete protection.

### Questions
- Is there any overhead (communication, computation) compared to classical FL approaches? Especially considering the alternating update of theta and fi.
- Is there a particular reason that a theoretical analysis is missing from this paper?
- On the privacy aspect mentioned above, do you think that privacy risk changes depending on the device capabilities? E.g., more capable devices (higher capacity) will aggregate more information, and thus be more exposed?

### Soundness
3

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
3

### Summary
The article introduces CoMiGS, a collaborative learning approach designed to address the challenges of system and data heterogeneity in on-device large language models (LLMs). By combining generalists and specialists, CoMiGS facilitates knowledge sharing while also personalizing solutions for individual user datasets. A key innovation of this approach is its bi-level optimization framework for the Mixture-of-Experts (MoE) objective, which allows for flexible aggregation and adaptation to the varying computational resources of users. CoMiGS demonstrates improved performance over existing methods, such as pFedMoE, by enhancing routing mechanisms and accommodating a flexible number of experts for each user. This ultimately leads to better privacy and personalization in federated learning.

### Strengths
- The article exhibits clear writing and a well-organized structure, effectively distinguishing its contributions from existing works and facilitating reader comprehension.
- The article addresses the potential applications of CoMiGS within the realms of federated learning and large language models, highlighting the method's broad applicability and promising implications.

### Weaknesses
1. The study is based on a limited scale, involving only four clients. It would be beneficial to explore methods to further differentiate between clients, such as employing clients with the same domain data but varying quantities.

2. While the article emphasizes the relationship between large language models (LLMs) and personalized federated learning, the novelty appears insufficient. The approach seems to replace traditional personalization methods in federated learning with LoRA training for LLMs and uses the Mixture-of-Experts (MoE) framework for personalizing each LoRA module. The motivation section needs to reinforce the necessity of this approach to establish its distinct contribution.

3. The article does not adequately address how it resolves issues related to resource heterogeneity. The experimental validation in this area appears insufficient, particularly regarding the fixed nature of experts for each client, as client resources may fluctuate over time.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents CoMiGS, a collaborative learning framework for personalized fine-tuning of LLMs on edge devices, addressing data heterogeneity and privacy challenges. CoMiGS features a dual-expert structure with generalists and specialists for effective knowledge sharing while preserving local data privacy. It uses a bi-level optimization mechanism, updating router parameters based on validation loss (outer optimization) and expert parameters based on training loss (inner optimization). This approach mitigates issues seen in traditional MoE architectures. Overall, CoMiGS effectively manages system and data heterogeneity in federated LLM training, enabling efficient data sharing without compromising privacy and enhancing model robustness.

### Strengths
1. CoMiGS effectively addresses heterogeneity by integrating knowledge across diverse end users while tackling the challenges of data heterogeneity. Its bi-level optimization mechanism strategically utilizes the roles of generalists and specialists, facilitating both data sharing and personalized experiences for end users.

2. CoMiGS employs load-balancing techniques to ensure a balanced allocation among different experts, enhancing the model’s robustness and generalization capabilities by maintaining equilibrium across them.

### Weaknesses
1. CoMiGS resembles a fusion of LoRAMoE [1,2,3,4] and FL-LoRA [5,6]. However, it lacks analytical comparisons with related studies and does not provide experimental comparisons to support its claims. The method's novelty is not clearly established, particularly given the existing literature on combining LoRA with Mixture of Experts and Federated Learning techniques. A more rigorous analysis of how CoMiGS differs from and improves upon these existing methods is needed, including a detailed breakdown of the architectural and algorithmic differences.

2. CoMiGS is designed for edge deployment, but fine-tuning multiple LoRA modules (generalists vs. specialists) may incur more computational overhead. The paper does not provide a detailed analysis of the computational cost associated with training and inference using multiple LoRA modules. This is a critical concern for edge devices, where resources are limited. The paper should include a quantitative analysis of the memory footprint, FLOPs, and latency of the proposed method compared to alternative approaches, especially when varying the number of specialists and generalists.

3.  The title suggests a focus on LLMs, but evaluation is limited to GPT-2 (124M), which is too simplistic in terms of both model type and parameter count. The study omits more complex LLMs, such as Llama3-1B, Llama3-3B, and Gemma-2B, which are designed for mobile environments. With the increase in parameters, issues such as embedded knowledge may become more pronounced, potentially enhancing the robustness and adaptability for In-Distribution and Out-of-Distribution task scenarios. This prompts the question: could this technique scale effectively with future generations of LLMs? Further research is necessary to explore these possibilities. The absence of experiments on more recent and larger models limits the generalizability of the findings.

### Questions
1. To facilitate both data sharing and end-user personalization within the inherent leader-follower structure, the proposed approach seems to introduce additional computational and communication costs during training and data sharing. Could the authors clarify the impact of this optimization on computational efficiency and memory storage requirements? Additionally, how does this affect the feasibility of deploying CoMiGS on resource-constrained edge devices?

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
5

### Summary
This paper introduces a novel collaborative learning framework called CoMiGS (Collaborative learning with a Mixture of Generalists and Specialists) for on-device fine-tuning of Large Language Models (LLMs). CoMiGS addresses both system heterogeneity (differences in local computational resources) and data heterogeneity (differences in user-specific data) by differentiating between generalists, which handle shared knowledge across devices, and specialists, which adapt to user-specific data. The approach is formulated as a bi-level optimization problem, with generalists and specialists iteratively updated through a routing mechanism, which adapts based on the target distribution. Experimental results demonstrate that CoMiGS outperforms existing methods in scenarios with varied data and system settings.

### Strengths
- The token-level routing enables CoMiGS to handle data heterogeneity more efficiently than client-level methods, and the bi-level optimization approach aligns well with the personalized and collaborative goals of the framework.
- The paper provides robust experimental evaluations on three datasets, covering both in-distribution and out-of-distribution scenarios.

### Weaknesses
 - While the paper presents CoMiGS as a novel collaborative learning framework, the core idea of combining generalist and specialist models to handle heterogeneous data is not particularly new. Similar approaches have been proposed in previous federated learning and mixture-of-experts frameworks. Many existing works utilize a combination of shared global models (analogous to generalists) and personalized models (specialists) to handle data and system heterogeneity [1]. The authors do not provide a clear explanation of how CoMiGS fundamentally differs from or improves upon these prior methods, which weakens the claim of novelty.
- The bi-level optimization approach may introduce significant computational overhead, especially for on-device applications with limited resources. Each optimization level requires iterative updates, making the entire process computationally intensive. The paper lacks a detailed analysis of the computational cost associated with the bi-level optimization, including the number of gradient computations and the memory footprint of maintaining both generalist and specialist models.
- The paper does not propose alternative mechanisms for model evaluation or adaptation that avoid the use of a validation set. Other federated learning approaches often incorporate online learning or lightweight evaluation methods that do not require a dedicated validation split, which CoMiGS could consider. The reliance on a validation set limits the applicability of the method in scenarios where labeled validation data is scarce or unavailable.
- The rationale behind maintaining both generalists and specialists within the framework is not entirely convincing. If specialist models are designed to adapt to user-specific data, the role of generalists becomes ambiguous, especially in highly heterogeneous settings where each user's data diverges significantly from the global average. The coexistence of generalists and specialists adds complexity to the model without a clear demonstration of the complementary benefits of this setup. The paper would benefit from a more in-depth analysis of the conditions under which generalists contribute meaningfully to the overall performance.

### Questions
- Could the authors clarify how CoMiGS fundamentally differs from existing frameworks that use a mixture of shared (global) and personalized (local) models to handle heterogeneity in federated learning? Specifically, what are the unique contributions of CoMiGS in comparison to these prior methods?
- CoMiGS relies on a validation set for tuning and routing adjustments, which may not be feasible in real-world on-device settings due to data limitations. How would CoMiGS function without a dedicated validation set, or are there alternative mechanisms for evaluation that do not require a separate validation split?

### Soundness
2

### Presentation
2

### Contribution
1
