# Layerwise Recurrent Router for  Mixture-of-Experts

- Decision: Accept
- Scores: 6, 3, 6, 8

## Abstract
The scaling of large language models (LLMs) has revolutionized their capabilities in various tasks, yet this growth must be matched with efficient computational strategies. 
The Mixture-of-Experts (MoE) architecture stands out for its ability to scale model size without significantly increasing training costs. 
Despite their advantages, current MoE models often display parameter inefficiency. 
For instance, a pre-trained MoE-based LLM with 52 billion parameters might perform comparably to a standard model with 6.7 billion parameters~\citep{rajbhandari2022deepspeedmoe}. 
Being a crucial part of MoE, 
current routers in different layers independently assign tokens without leveraging historical routing information, potentially leading to suboptimal token-expert combinations and the parameter inefficiency problem.
To alleviate this issue, we introduce the Layerwise Recurrent Router for Mixture-of-Experts (RMoE). 
RMoE leverages a Gated Recurrent Unit (GRU) to establish dependencies between routing decisions across consecutive layers.
Such layerwise recurrence can be efficiently parallelly computed for input tokens and introduces negotiable costs.
Our extensive empirical evaluations demonstrate that RMoE-based language models consistently outperform a spectrum of baseline models. 
Furthermore, RMoE integrates a novel computation stage orthogonal to existing methods, allowing seamless compatibility with other MoE architectures. 
Our analyses attribute RMoE's gains to its effective cross-layer information sharing, which also improves expert selection and diversity

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the Layerwise Recurrent Router for Mixture-of-Experts, a novel approach to enhance efficiency in MoE architectures within LLM. The authors highlight limitations in traditional MoE routers that operate independently across layers, potentially resulting in suboptimal parameter utilization. To address this, Recurrent-Router MoE introduces a GRU-based mechanism that enables dependencies between routing decisions across layers, which improves the diversity and effectiveness of expert utilization. The proposed method integrates seamlessly with other MoE architectures and demonstrates substantial improvements in performance on various language modeling tasks. Through comprehensive experiments, the authors show that RR-MoE achieves superior performance over several baseline router designs with only marginal computational overhead.

### Strengths
The paper offers a simple but new enhancement to MoE architectures by introducing a layerwise recurrent mechanism, distinguishing it from other MoE router designs that operate independently across layers. The methodology is sound, with a well-motivated design backed by extensive experimental validation and ablation studies. The work is valuable to the research community, as it not only provides a means to improve existing MoE designs but also contributes insights into the impact of cross-layer recurrence on expert diversity and selection.

### Weaknesses
The authors mention that their model is under-trained and does not yet perform well on challenging tasks like MMLU and GSM8K. A more complete evaluation on these benchmarks, perhaps by including more training tokens or longer training duration, would provide a fuller picture of the model's real-world applicability.

Also the paper presents extensive performance metrics and ablation studies, a more direct analysis of gradient propagation through the recurrent router could strengthen the argument for the importance of recurrent gradients in optimizing routing decisions. Also, do we need truncated backpropagation similar to BPTT?

The paper could benefit from a deeper comparative analysis with recent MoE models that also use recurrence or other advanced routing strategies (such as XMoE, HyperMoE etc). This would help clarify how RRMoE’s benefits compare to similar innovations in this rapidly evolving field.

### Questions
The paper emphasizes the importance of gradient flow through the GRU-based recurrence in RMoE but does not mention whether Truncated Backpropagation Through Time (BPTT) or any specific method was used to manage gradients across layers. Did the authors consider using truncated BPTT for controlling gradient flow through the recurrent router? Including details on gradient management would help clarify if additional methods, like truncation, could further optimize training.

 Would it be possible to conduct a more direct analysis, such as by visualizing or measuring gradient norms through layers, to further validate the specific impact of recurrent gradients? 

 Could the authors provide insights or quantitative analysis on how the recurrence depth impacts the RMoE’s routing decisions?

The current evaluation omits challenging benchmarks like MMLU and GSM8K, mentioning that the models are still under-trained. Can the authors comment on whether they plan to scale the training or incorporate task-specific fine-tuning to gauge RMoE’s performance on these harder tasks? Additional results on these benchmarks could help better gauge RMoE’s robustness and adaptability in real-world scenarios.

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
Paper introduces a gated recurrent connection for routing decisions in MoEs such that routing decision in a layer depend on shared GRU so that routing decisions between layers are no longer independent. The intuition expressed by authors is that this should help improve model because routing decisions in current layer should be able to leverage routing info from previous layers.

### Strengths
Paper clearly expresses main idea, that routing decisions in MoE should have some dependency on previous routing decisions, and how they achieve this and test the results.

### Weaknesses
The results are relatively minor improvements (1-2% relative), the models are very small (on the order of 36M parameters for an MoE model) and the benchmarks are small (enwiki8 & wikitext).

### Questions
Suggestions for improvement are to show results on a larger MoE model. Not all models need to be 100s of billions of parameters, but a 36M parameter MoE model is quite small these days, and it is hard to be convinced that small gains on this model would translate to a more realistic sized model.

### Soundness
2

### Presentation
2

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
The paper presents the Layerwise Recurrent Router for Mixture-of-Experts (RMoE), designed to address inefficiencies where routers at each layer operate independently, leading to suboptimal token-expert assignments. RMoE integrates a GRU to enable cross-layer communication, establishing dependencies between routing decisions across layers. The authors validate RMoE through experiments across various model sizes and tasks, demonstrating consistent improvements over baseline MoE models. Analysis shows that RMoE’s gains are primarily due to effective cross-layer information sharing, resulting in better expert utilization and diversity.

### Strengths
- The use of a GRU to incorporate layerwise information into MoE is a novel and well-motivated approach to address parameter inefficiencies in SMoE.
- Extensive ablation studies demonstrate the importance of recurrent gradient flow, validating the primary contributor to RMoE’s improvements.
- Interesting analysis on the increase in cross-layer mutual information and gating score entropy with RMoE, providing insights into how cross-layer information sharing improves expert selection and model robustness.

### Weaknesses
 - Current performance improvement appears marginal; val and test losses alone do not demonstrate statistically significant gains over baselines. Benchmarking on standard language modeling tasks would provide more practical context for the model's effectiveness.
- Analysis of gradient flow could be more rigorous; while recurrent gradient flow is highlighted as crucial in Section 5, more sophisticated gradient tracking techniques would strengthen this claim.
- The additional computation stage introduced by the GRU increases complexity, yet the impact on training efficiency is not thoroughly analyzed across different model sizes.

### Questions
- Clarify the architecture of the layer-specific projectors used in Eq. 4; are there structural variations across layers, or have alternative projector architectures been tested for potential performance improvements?
- In Table 1, improvement over baselines is minor, yet gains are more noticeable in Table 2 (billion-level settings). Could the authors explain the differing results, specifically regarding training sizes and conditions?
- Column names in Table 8 appear inconsistent with descriptions in the text; could these be corrected or clarified?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes to use RNN to replace the linear projection layer to route the tokens in MoE models. The proposed model achieves better results than vanilla router across scales (after revision).

### Strengths
1) Elegant design. Using previous routing representation to improve the routing decision is a smart idea.
2) Some experimental results in Section 6 (Observation) are interesting, such as Layer-wise recurrence encourages expert diversity.
3) Comprehensive ablation studies in Section, which shows the effectiveness of RNN router under this scale.
4) Unshare part of trainable parameters in RNN also makes sense. I suggest to cite this work (https://arxiv.org/abs/2107.11817), which unshare the layernorm when sharing MoE Transformer blocks.

### Weaknesses
I have only one important concern, i.e. the scale of the experiments. I agree the paper is promising in many aspects, but the experiments are too toy for a model architecture paper in 2024. We need at least 3B/7B activated parameters and 1T tokens to justify the scalability of the proposed method.

However, I understand it might be difficult to acquire enough computation resources for some reasons, so I decided to give a positive rating to this paper.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
3
