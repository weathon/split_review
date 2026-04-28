# One QuantLLM for ALL: Fine-tuning Quantized LLMs Once for Efficient Deployments

- Decision: Reject
- Avg Score: 4.50
- Scores: 1, 6, 6, 5

## Abstract
Large Language Models (LLMs) have advanced rapidly but face significant memory demands.  While quantization has shown promise for LLMs, current methods typically require lengthy training to alleviate the performance degradation from quantization loss. However, deploying LLMs across diverse scenarios with different resource constraints, e.g., servers and personal computers, requires repeated training per application, which amplifies the lengthy training problem. Given that, it is advantageous to train a once-for-all (OFA) supernet capable of yielding diverse optimal subnets for downstream applications through one-shot training. Nonetheless, the scale of current language models impedes efficiency and amplifies interference from weight sharing between subnets. We make an initial attempt to extend the once-for-all framework to large language models. Specifically, we decouple shared weights to eliminate the interference and incorporate Low-Rank adapters for training efficiency. Furthermore, we observe the imbalance allocation of training resources from the traditional uniform sampling. A non-parametric scheduler is introduced to adjust the sampling rate for each quantization configuration, achieving a more balanced allocation among subnets with varying demands. We validate the approach on LLaMA2 families, and downstream evaluation confirms our ability to maintain high performance while significantly reducing deployment time faced with multiple scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces LLM-QFA, a supernet-based approach that fine-tunes multiple quantized models with identical architectures but varied bit widths to cater to different deployment scenarios. The main contribution lies in integrating quantization-aware training (QAT) with LoRA, allowing different subnets to share the same LoRA component. Comparisons are drawn against GPTQ and QA-LORA, with claims of improved accuracy over GPTQ and faster fine-tuning than QA-LORA.

### Strengths
The paper is well-organized and clear in its explanations, with the exception of the details surrounding equation (8), which could be further clarified.

### Weaknesses
 **1. Practical Relevance of the Problem:**

The proposed approach addresses a problem that lacks practical application. In real-world deployments, training a large array of subnets to cover various quantization configurations is typically unnecessary. Practitioners often select a few configurations (e.g., 2-bit, 4-bit, or 8-bit quantization) rather than an exponential number, as suggested in the paper. This exponential approach not only demands excessive computational resources but also offers limited benefits. For scenarios requiring mixed-precision models, existing methods (e.g., “Hessian-Aware Quantization of Neural Networks with Mixed-Precision,” NeurIPS 2020) strategically determine which layers to quantize without needing such an extensive range of models. Thus, the paper’s proposed problem appears impractical and lacks substantial real-world applicability.

**2. Misalignment Between Proposed Approach and Evaluated Scenarios:**

The proposed approach is positioned within a Once-for-All-Training (OFA) framework, which suggests the need to train numerous models simultaneously. However, the evaluation focuses only on fine-tuning 2-bit, 3-bit, and 4-bit quantized models, with no consideration of other configurations. This discrepancy affects the validity of the reported execution time, as it excludes the cost of fine-tuning all potential bit-width combinations, thereby leading to an unfair comparison with QA-LORA. As it stands, the execution time presented does not accurately reflect the time required for the complete proposed approach, making the comparison with baselines misleading.

**3. Choice of Baselines:**

The selection of baselines lacks fairness. The proposed approach uses quantization-aware training (QAT), yet GPTQ, a post-training quantization method, is chosen as a baseline. A more appropriate baseline would employ QAT as well, providing a more equitable comparison.

**4. Low Novelty:**

The approach primarily combines existing techniques—quantization-aware training and LoRA—within an OFA context, but it does not substantively test the full implications of this setting. Without new insights or substantive contributions, the approach appears to merely integrate established methods without yielding notable theoretical or practical advancements.

**5. Ambiguity in Explanation of Equation 2:**

Equation (2) is not adequately explained, leading to potential misinterpretations. For example, the meaning of certain variables, such as “t”, remains unclear.

**6. Suspicious Results in Table 1:**

Some reported results in Table 1 raise concerns. For LLaMA2-13b, the QA-LoRA approach claims 0-shot accuracy values of 52.3%, 49.9%, and 31.8% for quantization widths 4, 3, and 2, respectively; however, their average does not match the reported 45.3%. Similarly, for another setting, it reports 5-shot accuracy values of 54.2%, 51.7%, and 32.0% for the same widths, but the average is again inconsistent with the reported 45.8%. These discrepancies suggest possible errors, raising doubts about the thoroughness of the entire experimental validation.

### Questions
1. Could the authors compare their approach with a baseline that also employs quantization-aware training?

2. Could they report the total execution time for training all bit-width combinations? (On page 3, the paper states that the number of subnets is L^3, where L is the number of layers.)

3. Can the authors provide further justification for the practical relevance of the addressed problem?

4. Could they clarify the novelty of the proposed approach in terms of unique contributions?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues that, in the context of training multi-width LLM OFA supernets,  decoupling shared weights to eliminate interference from weight sharing between subnets, using low-rank adapters for training efficiency, and dynamically adjusting the sampling strategy across training steps improves deployment time. The paper provides experimental evidence supporting this argument.

### Strengths
The paper addresses the important problem of enabling OFA training of multi-width quantized LLM supernets and allows this problem to be solved more efficiently than brute-force techniques while maintaining accuracy.

It works. It improves training time compared to QA-LoRA roughly in proportion to the number of specialized models required.

Although not extremely novel, it is a fun and interesting paper to read. The authors do a pretty good job explaining the challenges they encountered and motivating their solutions. There is one portion of the paper (on the problem with using uniform sampling) that I think could be clearer. I think conference attendees might find this interesting even if they don't need to use the specific approach the paper describes.

### Weaknesses
I think this is incremental work. Not very novel but useful and has some novelty. It applies concepts developed in other contexts in a new related context. The observations on the implications of uniform subnet sampling during training are interesting, but not well explained.

There are some grammatical errors, e.g., "the training major the cost of deployments".

There has been some recent work claiming that interference mitigation in OFA training isn't very helpful. The authors of the paper under review claim that this problem is important and describe a potential solution. Contrasting with prior work that makes a contrasting argument would improve the paper. I have an example paper in mind, but I do not want to push you into citing a particular paper. However, I think you might find some interesting and apparently contradictory work if you do a quick survey, and contrasting with it would improve your paper.

The paper finds that that layer-wise uniform sampling of subnets is biased toward subnets with mean widths near the mean bit width. This, if I understand correctly, is a straight-forward implication of the Central Limit Theorem. However, it is important to consider what specific thing ought to be uniformly sampled: subnets or subnet mean widths. If I understand correctly, there should be more subnets with mean widths near the global mean, so one must sample them more frequently to distribute training evenly across subnets. The paper, rather implicitly and with little discussion, implies that uniform sampling over subnet mean widths is a more desirable goal. You can make samples uniform over subnets or subnet mean widths, not both. Prior work chose "subnets". You choose "subnet mean widths". Why? Your evaluation shows that it works a little bit better. Is that sampling noise or a genuine improvement? If it's genuine, do you have (ideally testable) ideas on why your notion of uniform works better in practice?

### Questions
The last paragraph in the Weaknesses section of my review is in effect also a question. We can discuss that one here. I think it's more likely an opportunity to revise for clarity instead of a fundamental flaw.

### Soundness
3

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
3

### Summary
This paper presents LLM-QFA, a framework enabling once-for-all quantization-aware training of Large Language Models for efficient deployment across different hardware scenarios. The key contributions are weight decoupling to eliminate interference between quantization configurations and a resource-balanced sampling strategy for fair training across bit-widths. Evaluated on LLaMA2 and Mistral models, the framework achieves comparable performance to QA-LoRA and GPTQ baselines while requiring only one-time training instead of repeated fine-tuning for each quantization setting.

### Strengths
* The paper propose novel attempt to apply once-for-all training paradigm to LLM quantization, addressing weight sharing interference issues.
* The paper provides strong empirical results showing competitive or better performance vs baselines (QA-LoRA, GPTQ) while requiring only one-time training.
* The paper includes clear technical writing and comprehensive ablation studies validating each component.

### Weaknesses
 * The main motivation around reducing training time overhead seems weakly justified, as quantization-aware training is typically a one-time procedure and not a time-critical task.
* The author only did limited experimental validation across model architectures (only tested on LLama2 and Mistral). What about models like Llama3 series?

### Questions
* Have the authors considered evaluating on other popular LLM architectures like Llama3 to demonstrate broader applicability? Also are there any results on larger models like Llama3-70B?
* Given that quantization-aware training is typically a one-time procedure per model, could the authors better justify why reducing training time is a critical problem?

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
This work tackles a challenge in deploying large language models (LLMs) across multiple platforms with different computing resources without the need for repeated fine-tuning. Specifically, when targeting different deployment environments (e.g., from cloud to edge devices), varying quantization settings (such as different bit-widths) may be required, and each configuration usually demands separate fine-tuning to maintain accuracy. This process is computationally expensive. To address this challenge, the paper introduces LLM-QFA, a framework designed to streamline the deployment of LLMs across diverse hardware by performing quantization-aware fine-tuning only once, rather than retraining for each scenario.

### Strengths
Given the high number of potential layer-by-layer quantization configurations, an exhaustive search is impractical. To this end, the proposed method consists of a set of techniques, including: 
1. Identify layers that are most sensitive to quantization, focusing the search on configurations likely to yield better performance.
2. Adjust sampling probabilities dynamically to ensure all configurations receive balanced training, reducing biases toward certain bit-widths.
3. Perform one-shot fine-tuning across configurations, then use a validation-driven search to select the best configurations without retraining.
4. Use varied bit-widths across layers, focusing higher precision where it matters most, to achieve efficient, high-performing subnets.

Overall, the proposed method demonstrates competitive or better accuracy compared to GPTQ and QA-LoRA, with less computational cost. In addition, LLM-QFA’s resource-balanced sampling strategy outperforms random and uniform sampling.

### Weaknesses
One concern that the reviewer has is that quantization alone may not be the most challenging problem for cloud-to-edge cross platform deployments, instead, the key challenge is the required orders-of-magnitude variance in terms of the total numbers of model parameters. Moving from cloud-level hardware to highly constrained edge devices typically requires a significant decrease in the number of model parameters, often through methods such as pruning or model distillation, and LLM-QFA does not inherently address the orders-of-magnitude compression needed to bridge the cloud-to-edge gap. Furthermore, while the paper focuses on bit-width quantization, it does not address other critical aspects of model compression for edge deployment, such as reducing the model's hidden dimension size or the number of layers. These architectural changes are often necessary to meet the stringent memory and computational constraints of edge devices. The current approach may be insufficient for scenarios where the model needs to fit within very limited memory footprints, even with aggressive quantization.

### Questions
Given the high number of potential layer-by-layer quantization configurations, an exhaustive search is impractical. However, it would be valuable if the authors could analyze the potential performance gap between LLM-QFA and a hypothetical exhaustive search. Such an analysis could help quantify how close LLM-QFA comes to true optimal configurations.

### Soundness
3

### Presentation
3

### Contribution
3
