# Symbiotic Tuning: A Simple Approach for Enhancing Task Performance of Side-Tuning

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
The reduction of the computational and memory overhead associated with fine-tuning large language models remains a significant challenge for current research in natural language processing. Achieving an optimal balance between task performance, adaptability, and low memory requirement often presents a complex trade-off. Parameter-efficient fine-tuning (PEFT) methods, such as LoRA, have gained attention for their ability to reduce the number of trainable parameters while preserving task performance. However, they have not yet achieved a notable reduction in memory usage, which is still predominantly consumed by model weights and activations during backpropagation. In contrast, Ladder Side-Tuning (LST) has been proposed as an alternative that effectively reduces memory usage by freezing the backbone language model (BLM) and training only lightweight side networks. Nevertheless, this reduction in memory usage often results in a decline in performance, as LST typically exhibits inferior performance compared to PEFT methods on the same BLM. To address these limitations, we propose Symbiotic Tuning (SymTune), a novel approach that extracts intermediate outputs from the BLM and integrates symbiotic modules to enhance feature processing capabilities. This method avoids a direct trade-off between performance and memory efficiency, offering two key advantages: 1) robust performance across a wide range of natural language tasks, and 2) reduced memory consumption through an improved side-tuning architecture. The experimental results demonstrate that SymTune provides a scalable and memory-efficient solution for fine-tuning language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel parameter-efficient fine-tuning method, referred to as Symbiotic Tuning (ST), that follows the design principle of ladder side-tuning. The proposed ST method redesigns the plug-in network architecture of side-tuning, with the objective of reducing VRAM usage while maintaining high fine-tuning performance. Each layer’s plug-in module consists of a feature selector and a Transformer block. Specifically, the feature selector serves as a bottleneck block, projecting the hidden states from the backbone model to a lower dimension. The side Transformer block merges the hidden states with those from the backbone model through a weighted cross-attention mechanism. In addition, the attention weights of the backbone model are also incorporated into the cross-attention calculation. The ST method is applicable to both encoder-only and decoder-only language models, with feasibility demonstrated through experiments on DeBERTa and OPT. The experimental results on ordinary GLUE benchmarks and multi-class classification tasks (SemEval) demonstrate that ST outperforms ladder side-tuning and LoRA in terms of VRAM usage. Furthermore, ST achieves performance comparable to full-parameter fine-tuning, whereas ladder side-tuning does not.

### Strengths
1. The proposed ST method advances ladder side-tuning by designing a more efficient architecture for the side network, making the side-tuning paradigm competitive in fine-tuning performance without sacrificing computational efficiency.
2. The ST method is easy to integrate with mainstream language models due to its plug-and-play nature, and it provides viable solutions for both encoder-only and decoder-only models.
3. The ST method has the potential to scale to a wider range of models and could be effectively applied to generation tasks beyond just NLU tasks.

### Weaknesses
1. An important advantage of LoRA is its lower inference latency compared to other plug-in PEFT methods, such as adapters. The introduction of an additional network in ST could increase inference time. The authors should discuss this point and compare the inference efficiency of ST with that of LoRA/Full FT.
2. The ablation study could more solid by including the discussion of trainable weight $ c^{(l)}$ in Eq.4. It remains unclear how this fusion solution for hidden states operates. Specifically, how do hidden states from the backbone model and the ST module interact (i.e., learned values of these weights), and does a fixed weight setting yield better results?
3. Some experimental baselines are missing. In Tables 1 and 2, the DeBERTaV3-base includes a BitFit baseline, but BitFit is absent from the DeBERTaV3-large experiments.
4. For the decoder-only model, it would enhance the analysis to ensure that the baseline choices are consistent with those used for the encoder-only model, thereby demonstrating the effectiveness of ST method.
5. Typos:
- L068: toLST -> to LST
- L236: $f_{ca}$ -> $f_{ICA}$
- L242: $A$ -> $\mathbf{A}$
- L244: B -> $\mathbf{B}$

### Questions
1. The backbone models used in these experiments are smaller than 7B parameters. Given that current large language models are typically greater than 7B parameters, will the proposed method be effective for larger-scale models? Note: this is not a weakness of the paper, the applicability to smaller models is also important!
2. For encoder-decoder language models like T5, do you anticipate that the cross-attention mechanism of the backbone model could pose challenges in applying the proposed ST method?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the method of Symbiotic Tuning (SymTune), a novel approach that aims to reduce the VRAM consumption of language model finetuning while preserving the models' downstream performance. SymTune leverages the symbiotic modules injected into the backbone language model (BLM) to achieve the trade-off between the model performance and VRAM efficiency. By selectively filtering significant values from BLMs' hidden states while sharing the attention weights between the BLM and symbiotic modules, SynTune can achieve comparable performance on natural language understanding benchmarks to full parameter finetuning and PEFT.

### Strengths
- SymTune introduces novel symbiotic modules into language models that can finetune language models with minimal memory consumption.
- SymTune uses inverse cross attention (ICA) and attention sharing (ATS) that effectively captures the key features in BLM's hidden states with context-aware interactions.
- Experimental results show that SymTune achieves better performance than LoRA and LST, while costing less VRAM in model finetuning.

### Weaknesses
 - Even though the experimental results in Section 4 demonstrate that SymTune achieves better performance-memory tradeoff than LoRA and LST, the improvements seem minimal and insignificant. 
- SymTune is aimed at reducing the VRAM usage in large language model finetuning (as mentioned in the paper's introduction), yet the results only contain small-to-medium-sized language models (up to 2.7b).
- All benchmarks being used in this paper are natural language understanding tasks, and therefore, there is no proof to demonstrate that SymTune can be seamlessly adapted to natural language generation tasks with larger models.
- The difference in the models' performance with and without the usage of ICA/ATS shown in Table 6 is minimal.

### Questions
- There is a lack of a brief introduction to the SymTune method in the introduction section. It would be beneficial if the authors could simply describe the overall motivation and functionality of ICA and ATS here.
- Statistical significance test could be useful in the experiment section to show whether the SymTune method is indeed effective or not.
- Typo in Table 6's caption: "affect" is a verb so it should be "effect" here.

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
4

### Summary
The authors propose SymTune to reduce the vRAM in usage and try to maintain the performances of the model.
But lots of problems need to be addressed in the results.

### Strengths
The authors propose SymTune to reduce the vRAM in usage and try to maintain the performances of the model.

### Weaknesses
In Table 3-6, why not include LORA for comparison.
In Table 2, include the average performance.
From Table 1 and 2, the number of parameters of ST is only slightly lower than LoRA and ST has only slightly better performance compared with LoRA. Any reason for that, which is a great weakness of this work.

Why LoRA uses more vRAM than ST even if they utilize similar number of parameters?

### Questions
N/A

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
3

### Summary
This paper proposes a parameter-efficient fine-tuning method named Symbiotic Tuning by introducing internal attention representations into Ladder Sider-Tuning. Experimental results on classification tasks with pre-trained encoder models and decoder models show that symbiotic tuning achieves better performance than Ladder Sider-Tuning and LoRA.

### Strengths
Extensive experiments on classification tasks are conducted to show the effectiveness of Symbiotic Tuning. However, the evaluation on decoder models is mainly focused on the perplexity of language modeling tasks and in-context learning performance. It will be better to show the performance of Symbiotic Tuning on these tasks.

### Weaknesses
1. **Limited novelty**. The method proposed is an intuitive incremental work based on Ladder Sider-Tuning. The core idea of incorporating internal attention representations, while potentially beneficial, lacks a strong theoretical justification and appears to be an ad-hoc modification rather than a fundamentally new approach. The paper does not adequately explore the potential limitations or failure cases of this symbiotic interaction, especially in scenarios where the pre-trained and fine-tuned modules might have conflicting objectives or representations.

2. **Missing important details**. The details of implementing baseline method are missing. There are some concerns about the replication problems. Specifically, the paper lacks crucial information regarding the hyperparameter settings for both the baseline methods (Ladder Side-Tuning and LoRA) and the proposed Symbiotic Tuning. This includes learning rates, batch sizes, optimizer choices, and the specific configurations of the side networks in Ladder Side-Tuning. Furthermore, the paper does not specify how the internal attention representations are selected and integrated, raising concerns about the reproducibility of the results.

3. Typos: The second h0 and h1 in Figure 2 --> h1, h2

### Questions
1. Are there any in-context learning results on the pre-trained decoder language model?
2. Can you provide more experimental settings for baseline methods to replicate the results?
3. What does VRAM refer to? Is it referred to Video Random Access Memory?

### Soundness
3

### Presentation
2

### Contribution
2
