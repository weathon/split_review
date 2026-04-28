# LLMs Can Achieve High-quality Simultaneous Machine Translation as Efficiently as Offline

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 6, 3, 3

## Abstract
When the complete source sentence is provided, Large Language Models (LLMs) perform excellently in offline machine translation even with a simple prompt *"Translate the following sentence from [src lang] into [tgt lang]:"*. 
However, in many real scenarios, the source tokens arrive in a streaming manner and simultaneous machine translation (SiMT) is required, then the **efficiency** and **performance** of decoder-only LLMs are significantly limited by their auto-regressive nature. 
To enable LLMs to achieve high-quality SiMT as efficiently as offline translation, we propose a novel paradigm that includes constructing supervised fine-tuning (SFT) data for SiMT, along with new training and inference strategies. 
To replicate the token input/output (I/O) stream in SiMT, the source and target tokens are rearranged into an interleaved sequence, separated by special tokens according to varying latency requirements. 
This enables powerful LLMs to learn read and write operations adaptively, based on varying latency prompts, while still maintaining efficient auto-regressive decoding. 
Experimental results demonstrate that, even with limited SFT data, our approach achieves state-of-the-art performance across various simultaneous translation benchmarks and different evaluation metrics, and preserves the original capabilities of offline translation.
Moreover, EAST generalizes well to document-level SiMT without requiring specific fine-tuning, even beyond the offline translation model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Towards simultaneous machine translation, this paper mainly presents a novel dataset created for LLMs. The main contribution of the paper is the construction of the dataset for simultaneous translation. Compared to other methods, the proposed method enables LLMs to perform simultaneous translation effectively, achieving the desired performance in the experiments.

### Strengths
1. This paper provides a simultaneous translation dataset for the training of large language models (LLMs), enabling LLMs to perform simultaneous translation tasks in the form of multi-turn dialogues. This dataset is valuable for the training of similar simultaneous translation models in the future.

2. Subsequent experimental results show that the large language models fine-tuned with this dataset demonstrate the ability to perform simultaneous translation tasks.

### Weaknesses
1. Lack of Innovation. The innovation in this paper is limited. The idea of performing simultaneous translation tasks through multi-turn dialogues is relatively straightforward, and similar attempts, such as Conversational SimulMT[1], have already been made in the past. The main contribution of this paper lies in using GPT-4 to split a traditional full-sentence translation dataset into more granular dialogue-form data. While the authors also attempt to extend their method to multilingual simultaneous translation, this contribution is more of an engineering effort rather than a methodological innovation.

2. Unclear Experimental Description and Conceptual Errors. The analysis of the experiments is vague, with some fundamental misunderstandings. The paper reports the AL-CA metric in Table 2 but does not describe the speech translation dataset or provide information about the machine used for the experiments. Moreover, it is unclear how a text-based simultaneous translation model handles speech input. Therefore, regarding the AL-CA metric, which simultaneously accounts for waiting time of source input and machine processing time, the paper’s description and results are unsatisfactory.

3. Unfair Comparison. The paper compares its method to previous approaches such as Mono-KD, Agent-SiMT+HMT, and shows better results in Figure 7. However, the authors use Llama3 as the LLM for their method, while the other methods used Llama2 or smaller Transformer models. This comparison does not demonstrate the policy advantage of the proposed method, as the choice of a more powerful generation model already provides a significant advantage.

### Questions
The questions is shown in the Weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces EAST, a novel method for performing simultaneous machine translation with Large Language Models.  The authors address the limitations of LLMs in SiMT, such as the computational overhead of KV cache recomputation and the lack of adaptive read/write policies. EAST employs a two-stage supervised fine-tuning process. First, the authors resort to GPT to constructSiMT dataset  with interleaved source and target chunks marked by special read/write tokens which can be used to further finetune the model. Second, it fine-tunes the model on a multilingual SiMT dataset (SiMT-Multi-90K) and an offline MT dataset using LoRA.  The authors claim EAST achieves state-of-the-art performance on various benchmarks, maintains near-offline translation quality, and generalizes well to document-level SiMT without specific fine-tuning.

### Strengths
1. The use of an interleaved sequence with special read/write tokens for SFT is a novel approach that simplifies the training process and allows for efficient KV cache reuse during inference.
2. EAST learns an adaptive read/write policy without relying on traditional wait-k strategies, potentially leading to more nuanced translation decisions.

### Weaknesses
1. While the specific techniques are novel, the overall approach of fine-tuning LLMs for SiMT is not entirely new. The incremental contribution over existing LLM-based SiMT methods by prompting a LLM to construct a SiMT dataset to teach its format is not substantial enough to warrant acceptance.

2. The evaluation primarily focuses on BLEU, COMET, and BLEURT. More comprehensive evaluation metrics specifically designed for SiMT, such as latency-aware metrics and human evaluation, are necessary to validate the claims of high quality and efficiency. The "interpolation effect" claim lacks sufficient evidence and analysis

### Questions
1. The paper mentions an "interpolation effect" for latency.  Can you elaborate on this and provide more empirical evidence to support it?
2. How robust is EAST to noisy or non-fluent input, which is common in real-world streaming scenarios?
3. Do you consider converting the format learning for LLM into a RL approach?

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
5

### Summary
The paper presents EAST, an Efficient and Adaptive Simultaneous Machine Translation method using Large Language Models (LLMs) to improve real-time translation quality while achieving efficiency comparable to offline neural machine translation (NMT). EAST addresses challenges in existing SiMT systems by generating structured training data with explicit read-write signals and employing a dynamic read-write policy during inference that allows efficient reuse of the key-value (KV) cache. Experimental results indicate that EAST achieves high-quality translations across eight language pairs and near-offline decoding speeds, thereby enhancing the overall performance of simultaneous machine translation.

### Strengths
- Simultaneous machine translation is an interesting and promising research direction. The article is well written and easy to follow.
- EAST leverages the instruction-following capability of LLMs to create structured training datasets with explicit read-write signals, enabling effective learning of simultaneous translation strategies.
- Experimental results demonstrate that EAST achieves high-quality translations across eight language pairs while maintaining near-offline decoding speeds.

### Weaknesses
 - The SiMT datasets used for training, SiMT-De-En-660K comes from WMT15 De-En. As far as I know, WMT15 De-En has about 4.5M parallel data. Why the author only rewrites 660K of the data, the motivation needs to be explained. The filtering process that led to the reduced dataset size is unclear. Specifically, what criteria were used to determine which sentences were suitable for simultaneous translation training, and how might these criteria bias the resulting model? A more detailed explanation of the filtering process is needed to assess the representativeness of the training data.
- I look forward to an experiment on the performance trend with the amount of training data, which will help guide us to retrain LLM to perform SiMT with the minimum amount of data. It is important to understand the data efficiency of the proposed approach. An analysis of how performance scales with training data size is crucial. This would involve training models with varying amounts of SiMT data and plotting the performance against the dataset size. Such an experiment would provide practical guidance on the amount of data needed to achieve a desired level of performance, and help assess the robustness of the model.
- In the main experimental results in Figure 3, it is suggested that some previous LLM-based SiMT methods can be added to demonstrate the effectiveness of EAST. The current evaluation lacks a direct comparison with other LLM-based simultaneous machine translation methods. Without such comparisons, it is difficult to assess the relative performance of EAST. Including results from relevant baselines would provide a more comprehensive evaluation of the proposed method.

### Questions
Refer to weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a unique dataset specifically designed for simultaneous machine translation, enabling large language models to perform this task. The paper primarily focuses on the methodology for constructing the simultaneous translation dataset. Experimental results demonstrate that the proposed dataset equips large language models with simultaneous translation capabilities and achieves expected performance in the experiments.

### Strengths
1. This paper proposes a dataset specifically designed for fine-tuning large language models for simultaneous machine translation.

2. Experimental results prove that the proposed dataset enables large language models to acquire a certain level of simultaneous translation capability.

### Weaknesses
1. The approach presented in this article is based on existing methods (i.e., Conversational simulmt) with some improvements, but its innovation is limited.
2. In the main experiment of Figure 3, EAST-Only-Stage-II outperforms EAST-Stage-I in the De-En direction, which is unexpected. This is because EAST-Only-Stage-II fine-tunes the LLMs using a multilingual dataset, while EAST-Stage-I fine-tuned the LLMs on a larger-scale De-En dataset. Can the author provide an explanation for this outcome?
3. In Line 298-300, this paper mention, "the EAST-Stage-I model exhibits superior performance over the Llama3-MNMT w/ wait-k method for De->En. This demonstrates the effectiveness of the SiMT-De-En-660K dataset tailored for learning the novel task". However, the comparison presented here does not sufficiently support the authors' claim. To better highlight the benefits of the constructed De-En SiMT dataset, the authors should fine-tune LLMs using an offline dataset, apply the wait-k strategy, and compare it with EAST-Stage-I.
4. In Section 4.4, the paper report the AL-CA metric, which is a latency metric for speech-to-text simultaneous translation. However, the paper does not specify which speech dataset was used for the experiment, nor does it explain how this metric was calculated.
5. In Figure 7, the authors compare their method with previous ones and claim significant improvement. However, their approach utilizes Llama3, while the previous methods use smaller Transformer models or Llama2. This comparison is not entirely fair and cannot showcase the effectiveness of the proposed method.
6. The focus of this paper is on using interleaved sequences to enable LLMs to generate next tokens based on the interleaved sequence in different languages. While this is a good starting point, we would like to see more analysis and comparison of the quality of the translation policies acquired by the fine-tuned LLMs, which is not presented in the paper.

### Questions
Pleased refer to the aboved weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a method for finetuning a large language model for simultaneous translation. They generate interleaved source-target data pairs by distilling a powerful LLM (i.e., GPT-4), which are then used to finetune a pretrained LLM. Experiments conducted on Llama-3-8B-Instruct demonstrate impressive numerical performance.

### Strengths
1. Experiments are conducted using state-of-the-art foundational LLM, Llama-3-8B-Instruct, demonstrating impressive numerical results.
2. Multilingual datasets and document-level datasets have been evaluated, which are often ignored in previous works.

### Weaknesses
1. Contribution is limited. The concept of using interleaved source-target text pairs for fine-tuning a large language model for simultaneous translation is not novel and has been discussed in prior work [1]. The paper's main contribution appears to be using a powerful LLM (i.e., GPT-4) to generate and rephrase this kind of data.
2. The use of LoRA to adapt a SiMT model for multilingual SiMT appears to be incremental and may not be highly relevant to the core focus of this work.
3. Unconvincing experiments. There is almost no comparison with recent LLM-based SiMT models (except Agent-SiMT) or state-of-the-art traditional SiMT. The comparison with Agent-SiMT is also not rigorous. **Since different foundation models are used, the advantages shown in your paper may stem from the foundational models or data distilled from GPT-4 (as the target text is modified!) rather than the simultaneous generation strategies.** A clear indication of this is that when AL is very large (i.e., close to offline translation), the translation performance gap between models widens, suggesting that streaming generation performance cannot be directly compared.

### Questions
1. Clarify your contribution compared to paper [1]. **So far, the primary difference between the two works is that [1] employs an alignment-based method to create the interleaved dataset, while this work utilizes GPT-4 to generate and rephrase the data.**

2. Conduct rigorous comparative experiments! When comparing your methods with other LLM-SiMT models, at least ensure that the foundational models are consistent. If comparing with traditional SiMT models, you should maintain consistency in training data. According to the appendix (Figure 11), **using GPT-4 to create segmented texts in your method also involves *rephrasing* the target text. This can be seen as a form of distillation from GPT-4, which will definitely boost the performance for both your model and traditional SiMT models.**

### Soundness
1

### Presentation
3

### Contribution
2
