# Context-aware Dynamic Pruning for Speech Foundation Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Foundation models, such as large language models, have achieved remarkable success in natural language processing and are evolving into models capable of handling multiple modalities.
Listening ability, in particular, is crucial for many applications, leading to research on building speech foundation models. However, the high computational cost of these large models presents a significant challenge for real-world applications. Although substantial efforts have been made to reduce computational costs, such as through pruning techniques, the majority of these approaches are applied primarily during the training phase for specific downstream tasks. In this study, we hypothesize that optimal pruned networks may vary based on contextual factors such as speaker characteristics, languages, and tasks. To address this, we propose a dynamic pruning technique that adapts to these contexts during inference without altering the underlying model. We demonstrated that we could successfully reduce inference time by approximately 30\% while maintaining accuracy in multilingual/multi-task scenarios. We also found that the obtained pruned structure offers meaningful interpretations based on the context, e.g., task-related information emerging as the dominant factor for efficient pruning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This research paper introduces a context-aware dynamic pruning technique for speech foundation models, enabling the models to adjust their structure based on contextual factors like language and task during inference. The authors showcase the effectiveness of their approach in a multilingual, multi-task setting, achieving approximately 30% reductions in inference time while maintaining BLEU score, ST task, and little degradation on the WER, ASR task. Additionally, they analyze the pruned model structure, offering insights into the varying importance of specific modules for different tasks and highlighting potential optimizations for speech processing architectures.

### Strengths
The paper's main strength lies in its analysis of the importance of different modules for various speech processing tasks. The findings indicate that, within the encoder-decoder framework, pruning the decoder is more effective for speech translation (ST) and automatic speech recognition (ASR) tasks. The paper is well-written and easy to understand with minor typos and incomplete sentences.

### Weaknesses
The size of dataset (20 hours) used is too small to make general claims.

The authors do not compare their results with any other pruning methods. Like the effect of simply removing the layers, instead of different modules within, on the performance on the given the size of the dataset used in the study.

While the paper focuses on reducing inference time, it doesn't address the computational overhead introduced by the dynamic pruning process itself and searching the best sparsity number during finetuning.

Lack major novelty.

### Questions
Typo ? [line 130] if out validation data >> if validation data

I think [at line 285] the sentence is incomplete. 

At line 285, the authors make a statement "This supports our initial question regarding the need for a large-scale decoder in ASR systems". This is different form the results in the paper, pruning the decoder a lot does not effect ASR performance much compared to encoder as shown in Figure 2. 

In Figure 1, it is not clear how mean pooling can be applied to the input of the transformer decoder given its autoregressive nature. 

Not able to understand after reading the paper, if the time reduction is from using the joint finetuned model or individual task finetuned model. I think it is for individual task finetuned models. 

[Please correct me if I am wrong]. The paper simply extends the work of Peng et al. (2023b) by utilizing the model structure of a speech foundation model to address multilingual and multi-task scenarios and therefore lacks major novelty. Please provide more detailed comparison of their approach to previous work and their novel contributions beyond Peng et al. (2023b).

Not suited for joint pruning? As per the results, it is better to prune decoder in multitask setting. But authors report for the ASR and ST tasks SRC-ATT and SELF-ATT are individually important in the decoder. Therefore, the motivation to prune the modules in the joint finetuning is diluted.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work proposes a dynamic pruning method to make large speech models more efficient during inference. Instead of using a fixed pruning structure, the authors adaptively prune parts of the model based on the specific context—such as the language, task, and speaker characteristics—while keeping the model’s core structure intact. This approach aims to reduce inference computational costs without losing accuracy, especially in multilingual and multi-task scenarios. Experimental results show that the proposed method achieves up to 35% faster inference with minimal impact on accuracy for tasks like automatic speech recognition (ASR) and speech translation (ST). Key contributions include the development of a context-aware pruning mechanism and a detailed analysis of how different tasks and languages benefit from tailored pruning strategies.

### Strengths
1) The approach is novel, introducing a dynamic pruning method with learned masking that adapts based on language and task contexts. The use of language tags to inform mask generation is particularly innovative, with strong potential for real-world impact.

2) The method is technically well-executed, with careful design of the module-level pruning strategy and gate predictor. Experiments cover multiple tasks (ASR and ST), languages, and configurations (encoder-only, decoder-only, and joint pruning), demonstrating the method’s generalizability across varied settings. The authors include detailed subtask-specific performance analyses, which reassures method does not introduce potential bias. Also authors show particular attention to avoiding data contamination—a notable strength given the field’s reproducibility challenges.

3) This work is promising for deploying large speech models in resource-limited environments, reducing inference time without sacrificing much accuracy. The context-aware pruning method offers an efficient, adaptable solution that could inspire further research into resource-saving models in NLP, computer vision, and other domains.

### Weaknesses
1) **Limited Baseline Comparisons:** The paper lacks comparisons with other dynamic pruning methods, particularly layer-wise pruning. The claim that finer-granularity pruning, like kernel or layer pruning, would disrupt model adaptability (lines 149-152) could be misleading, as studies such as [1] show that layer-wise pruning can maintain or even enhance model performance. Providing evidence for this claim, for instance by adding layer-wise pruning as a baseline, would provide valuable context for assessing the benefits of context-aware pruning, especially since there is a risk the current model is overly complex, potentially reducing its efficiency.
2) **Reproducibility:** The paper is clear enough to support basic reproduction. However, providing the code would greatly benefit the community and improve reproducibility. Additionally, a brief explanation and citation for Gumbel-Softmax [4] would enhance clarity, as this technique, though widely known, is central to the gate predictor setup.
3) **Need for more In-Depth Ablation Discussion:** While the paper analyzes different pruning configurations (encoder-only, decoder-only, joint pruning) with heatmaps for various subtasks being provided in the Appendix, it lacks discussion on how different languages or tasks are affected by these setups. Some languages may benefit more or less from the pruning process, potentially relating to their resourcefulness levels in OWSM pre-training data. Such insights could clarify the impact of context-aware pruning across subtasks.
4) **Interpretability of Pruning Choices:** The paper discusses the interpretability of context-based pruning but could offer deeper insights. For example, quantitative metrics or visualizations on why certain modules are pruned would help clarify the gate predictor’s influence on pruning decisions and whether these choices are consistent across contexts. For example, you could study the correlation between pruning decisions and specific linguistic features of the input. Additionally, analyzing the impact of pruning only specific parts of the layers (e.g., self-attention vs. FFN) could improve understanding, as prior studies [2, 3] suggest these components may have varying importance across tasks and have different weight on the computational costs. 
5) **Contribution Clarification:** Network pruning using learned masks is not particularly novel, and have been studied in various domains, including self-supervised models for language and speech. Expanding on these methods in the related work section and clarifying the novelty of this specific approach would strengthen the paper’s positioning.

### Questions
- How significant are the results? Can you provide information on the statistical significance of your results, such as confidence intervals? Reporting confidence intervals or statistical tests would strengthen the findings, especially since many works in adaptation and fine-tuning report these metrics to assess consistency and robustness.
- Have you observed any patterns in performance across different subtasks or languages, particularly with varying sparsity targets?
- Does your method require specifying the source language at inference, or can the model identify the language automatically, as Whisper does?
- Would it be possible to provide code or configuration files to facilitate reproducibility?

As a side note, I recommend adding baseline (without pruning) to the tables as this would help visualization and understanding.

### Soundness
3

### Presentation
4

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
The paper proposes a method to prune (specifically structured pruning) Whisper-like speech foundation models. The authors first show the dependency of optimal pruned networks on several auxiliary characteristics of the task, languages, etc. and finally show that their method can achieve similar performance on benchmark datasets with similar performance.

### Strengths
- The paper is well written and is easy to read.
- The paper targets an important task of efficiency in speech models. As speech models continue to grow, efficiency is important and is an important research area.
- The proposed modification to the Context-Aware Gate Predictor is novel. To handle multiple languages and tasks simultaneously, the authors created vectors representing the language and task, combined them with the speech features, and used them as input to the Gate Predictors.
- The analysis provided on sparse encoders and decoders is novel. The extension to multilingiuality and multi-task is new and promising.

### Weaknesses
 - A major weakness of the paper is the lack of baselines and comparison with prior-art. While I understand that the paper proposes a structured pruning mechanism, the ASR community has built several unstructured pruning mechanisms [1,2,3]. Unstructured pruning methods have a motivation similar to this paper and [1] also show that they achieve similar performance with high amounts of pruning. These methods have not been discussed or compared neither used as baselines. Specifically, the paper lacks a comparison to magnitude-based pruning, a common unstructured method, and fails to explore the performance trade-offs at different sparsity levels for these baselines. The absence of these comparisons makes it difficult to assess the true effectiveness and novelty of the proposed structured pruning approach.
- The paper feels like an analysis paper. Most methods applied are borrowed from Peng et al. (2023b), who also propose module-wise structured pruning. This paper just applies it to multilingual and multi-task scenarios and explores how a large-scale speech foundation
model adapts its structure based on context. The core methodology, including the module-wise pruning and the use of Gumbel-Softmax, is not significantly different from the prior work. The extension to multilingual and multi-task scenarios, while valuable, does not introduce substantial methodological novelty. The paper would benefit from a more in-depth discussion of how the proposed method differs fundamentally from Peng et al. (2023b) beyond the application to new scenarios.
- The scope of the experimental section is rather narrow. The authors just show results on the Europarl-ST dataset and OWSM. A broader scope with more datasets and models would have been appreciated. Can Whisper be used? Can the authors expand the datasets employed for evaluation? The limited dataset scope makes it challenging to generalize the findings. The paper should include experiments on more diverse datasets, including those with varying acoustic conditions and language characteristics, to demonstrate the robustness of the proposed method. Furthermore, the lack of experiments on other speech models, such as Whisper, limits the general applicability of the findings.
- (Minor) I am not amazed by the results. It  is well known that these networks are sparse. This paper proposes a method to prune these networks. In my experience, pruning is not done extensively as it might lead the model to loose performance in other areas beyond benchmark datasets. For example, given every layer stores different kinds of information, pruning a layer based on ASR results might lead useful information for another language/task to deteriorate. I understand this is an academic paper and nevertheless the performance shown in this paper are somewhat promising.

### Questions
- Is elapsed time the correct metric for comparing model efficiency? In my experience, any torch implementation does not yet improve efficiency in terms of flops as torch is not yet designed for it. Can the authors show metrics in terms of FLOPs maybe?
- Please add wha conclusion we should draw from a figure to the caption of each figure. This makes the figures difficult to follow.

 don't have much questions. The findings presented in the paper are sound. However, I do not find anything much novel about the paper. Though novelty is not always that is required, but specifically and extension of an existing method to multilingual and multi-task scenarios is not very interesting to me. I would appreciate if the authors can point out whats novel in their "novel context-aware pruning technique" (except the gating technique) which is difficult for me to understand.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the problem of structured pruning for speech foundation models in the presence of context. The structured pruning is dynamically adjusted based on context during inference.

For each structured component in the model, a module selector estimates a mask, framed as a two-class classification problem, using Gumbel softmax. Experimental results on Speech Transcription and Speech Translation demonstrate the proposed approach’s effectiveness in improving inference efficiency without compromising performance.

The structured pruning also reveals key characteristics of several modules in the OWSM 3.1 architecture. Notably, pruning a decoder yields a significant speed-up compared to pruning an encoder.

### Strengths
- The paper underscores the effectiveness of the proposed structured pruning method with robust experimental results. 

- The ablation studies are thoughtfully designed, and each section provides detailed insights into the impact of various components in encoder, decoder, and joint pruning. 

- This work may inspire further research into new model architectures.

### Weaknesses
The original OWSM 3.1 model is a multilingual ASR model that covers a wide range of languages, each represented within the model's parameters. For high-resource languages, such as the one chosen in this study, pruning a significant portion of the network is often feasible without substantial performance degradation. However, for low-resource languages, the effects of similar pruning may lead to severe performance deterioration. Analyzing these effects could help clarify the limitations of this approach. Furthermore, the study does not explore the impact of pruning on individual modules within the encoder and decoder, which could reveal more granular insights into the model's sensitivity to sparsity. For example, it would be valuable to know if pruning attention heads or feed-forward networks within the encoder has differential effects on performance, especially across different layers. This level of analysis is crucial for understanding the architectural redundancies and potential for further optimization. Finally, the paper does not discuss the potential impact of the proposed pruning method on the model's generalization capabilities, particularly when applied to unseen data or languages. It is important to investigate whether the pruned model maintains its robustness and performance across diverse input conditions.

### Questions
1. In Table 1, the inference time for the encoder-decoder model with s_target = 0.1 exceeds the baseline (10.39 vs. 9.28). Does this indicate that model selection (pruning) is computationally expensive?

2. How critical is Gumbel-softmax for dynamic pruning? Could a simpler sigmoid-based selection function perform comparably in this setting? How are the temperatures for Gumbel-softmax adjusted?

3. Based on this study, can we reasonably infer that the E-Branchformer architecture contains additional components that could be pruned for efficiency, potentially aligning it more closely with the Conformer architecture?

### Soundness
3

### Presentation
4

### Contribution
4
