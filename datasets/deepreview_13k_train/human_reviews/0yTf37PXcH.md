# Improving Multi-modal Large Language Model through Boosting Vision Capabilities

- Decision: Reject
- Scores: 6, 5, 3, 8, 5

## Abstract
We focus on improving the visual understanding capability for boosting the vision-language models. We propose \textbf{Arcana}, a multiModal language model, which introduces two crucial techniques. First, we present Multimodal LoRA (MM-LoRA), a module designed to enhance the decoder. Unlike traditional language-driven decoders, MM-LoRA consists of two parallel LoRAs -- one for vision and one for language -- each with its own parameters. This disentangled parameters design allows for more specialized learning in each modality and better integration of multimodal information. Second, we introduce the Query Ladder adapter (QLadder) to improve the visual encoder. QLadder employs a learnable ``\textit{ladder}'' structure to deeply aggregates the intermediate representations from the frozen pretrained visual encoder (e.g., CLIP image encoder). This enables the model to learn new and informative visual features, as well as remaining the powerful capabilities of the pretrained visual encoder. These techniques collectively enhance Arcana's visual perception power, enabling it to leverage improved visual information for more accurate and contextually relevant outputs across various multimodal scenarios. Extensive experiments and ablation studies demonstrate the effectiveness and generalization capability of our Arcana. The code and re-annotated data are available at \url{https://arcana-project-page.io}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Arcana, a multi-modal large language model (MLLM) designed to improve visual perception capabilities. Arcana introduces two key techniques: MM-LoRA and QLadder. MM-LoRA enables separate vision and language pathways, reducing modality interference, while QLadder enhances the visual encoder's ability to capture fine-grained visual details. Extensive experimentation across benchmarks like VQAv2 and TextVQA demonstrates Arcana’s  improvement over existing MLLMs in both zero-shot and fine-tuning scenarios, highlighting its capacity for accurate visual reasoning and multi-modal alignment

### Strengths
The paper is well written and structured

### Weaknesses
The structural innovations of MM-LoRA and QLadder are not sufficiently solid, as the design does not appear to specifically address identified issues such as color recognition, object counting, small object understanding, and spatial location. The paper's motivation highlights these specific visual perception challenges, yet the proposed architectural modifications seem somewhat generic and lack a direct mechanistic link to solving these problems. For instance, while MM-LoRA aims to reduce modality interference, it's unclear how separating vision and language pathways inherently improves color perception or object counting, which often require intricate visual feature analysis. Similarly, QLadder's aggregation of intermediate visual representations, while potentially beneficial, does not explicitly target the fine-grained detail required for small object understanding or precise spatial reasoning. The improvements observed could potentially stem from increased model capacity or better optimization, rather than a targeted solution to the stated visual perception issues.

### Questions
In terms of motivation, the paper aims to resolve MLLM visual perception issues such as color recognition, object counting, small object understanding, and spatial location. However, the structural designs of QLadder and MM-LoRA do not seem specifically tailored to address these problems, leading to the impression that performance improvements may stem from data rather than a well-targeted structural design, which appears somewhat forced into explaining the results.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper seeks to improve visual understanding capability of vision language model. It introduces two components to enhance the capacity of the VLM: Multimodal (MM) -LoRA and Query Ladder. The MM-LoRA increases the capacity of the decoder by introducing low-rank adaptable matrices separately for the vision and language modalities. The QLadder increases the capacity of the encoder by incorporating learnable tokens at the input. Overall, this approach shows benefits of individual components and also competitive performance across MM/Language benchmarks.

### Strengths
- The identified problem of the lack of strong visual capabilities (e.g. detection, localization, color-comprehension etc.) in current vision language models is interesting and worth studying
- It's also interesting to see the need for modality specific adaptation 
- The paper is easy to comprehend and well supported by various block diagrams

### Weaknesses
* The summary section (line 519-520) mentions "achieving notable performance improvements even with limited data resources". However, the problem of limited data sources is not convincing, especially in the context of multimodal tasks. While domain-specific scenarios like medical imaging might present data limitations due to privacy concerns, the paper does not adequately address this. For the kind of problems mentioned in the paper (detection, localization, color-comprehension), it is unclear why data would be considered limited, given that LLM's and Visual-Encoders are typically trained with web-scale data. The authors should clarify whether they are referring to limitations in supervised fine-tuning (SFT) data specifically, and elaborate on the challenges associated with acquiring sufficient SFT data for effective multimodal alignment.

* The paper lacks a thorough explanation for why components like MM-LORA and Q-Ladder should improve visual capabilities like detection, localization, and color-comprehension. While the attention visualization (line 469-482) demonstrates the effect of these components on visual-token-attention, it does not sufficiently explain why that itself should improve performance on these specific tasks. Statements like "promotes cooperation between different modalities" (line 478) and "enriches the visual information" (line 481) lack concrete evidence or intuitive explanations. The authors need to provide a more detailed mechanistic understanding of how MM-LORA's decoupled design and Q-Ladder's intermediate feature aggregation directly contribute to improvements in the targeted visual capabilities.

* The contributions of the proposed components are not clearly distinguished from prior work. For instance, the benefit of LORA for limited-data-adaptation has been well studied in the past [1]. Similarly, the importance of introducing additional visual tokens to visual encoders has also been shown [2]. The paper should more clearly delineate the novel aspects of MM-LORA and Q-Ladder. Specifically, how does the multi-modal parameter decoupling in MM-LORA differ fundamentally from existing LORA implementations? How does Q-Ladder's "ladder" structure for aggregating intermediate-layer features provide a unique advantage over simply adding visual tokens, as explored in prior work? 

* Are the benefits of Qladder/MM-LORA consistent across scales? If we increase the scale of LLM and Visual Encoder, will Qladder/MM-LORA still show benefits? This is a crucial question for assessing the generalizability and practical impact of the proposed method. The paper would be significantly strengthened by experiments demonstrating the performance of Q-Ladder and MM-LORA across different model scales. 

* Miscellaneous
    * Is the beta gamma ration study consistent across a range of LORA ranks (say 64 - 1024)? here it was set to 256
    * Why was LORA applied only to linear layers?
    * In qualitative evaluations (Fig. 5), comparisons should be made with other models to clearly show qualitative gains from using Qladder/MM-LORA

### Questions
What was the main problem that was being addressed? Was it limited data adaptation, was it visual capabilities? If it was just visual capabilities, how does LORA or a few-learnable tokens based adaptation compare against scaling up?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work aims to enhance the visual capabilities of MLLMs through two main contributions: (1) the introduction of a MM-LoRA for the LLM decoder, and (2) the development of a Query module for visual encoders.

### Strengths
It is well known that MLLMs often exhibit limitations in their visual capabilities, and this work addresses this important issue. Additionally, the paper is well-written and easy to follow.

### Weaknesses
- The proposed method leverages additional learning parameters to enhance the visual capabilities of MLLMs. Recent studies (e.g., LLaVA-Next, VILA-1.5, Qwen-VL-2) have shown that simply improving image resolution using various (*any resolution*) techniques is a straightforward and effective way to address this issue. I am skeptical that the proposed method will achieve performance comparable to these AnyRes approaches, particularly on tasks requiring high resolution. The proposed method appears limited by the visual encoder, despite the incorporation of additional LoRA modules.
- The focus of this study is on the visual capability of MLLMs. However, only one ViT is examined, and there are no ablations on different ViTs. This raises doubts about the generalizability of the proposed approach.
- The improvements from the proposed method should be evaluated based on the ablation studies, rather than relying on Table 1 and 2, as the model Arcana reported in Table 1 and 2 is trained on a combination of large datasets (comparing to LLaVA-1.5 presented in Table 1 and 2). However, it is important to note that only a limited selection of four benchmarks is presented in ablations.

### Questions
N/A

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
5

### Summary
This paper proposes a novel Multi-modal Large Language Model (MLLM) called Arcana, designed to enhance visual understanding capabilities. It introduces two key components: Multimodal LoRA (MM-LoRA) and the Query Ladder adapter (QLadder). MM-LoRA consists of two parallel LoRAs (one for vision and one for language) to disentangle the modalities and enhance their specialized capabilities. QLadder aggregates intermediate representations from the visual encoder, further boosting the visual abilities of the MLLM. Experimental results demonstrate that Arcana outperforms previous MLLM baselines (e.g., LLaVA-1.5, mPLUG-Owl2, etc.) on visual question answering and multi-modal conversation benchmarks. Notably, the ablation study shows that QLadder significantly improves MMVP performance, which requires strong vision capabilities.

### Strengths
1. The presentation and writing are clear and easy to follow. Figure 1 in the introduction effectively illustrates the background, motivation, and main results of this paper.

2. Tables 1 and 2 show that Arcana achieves better performance than previous MLLM baselines (e.g., LLaVA-1.5, mPLUG-Owl2, etc.) on visual question answering and multi-modal conversation benchmarks.

3. The ablation studies in Tables 4 and 5 clearly validate the effectiveness of MM-LoRA and QLadder.

4. The ablation study demonstrates that QLadder significantly improves MMVP performance, which requires robust visual capabilities. In Table 6, adding QLadder boosts MMVP performance by 3.6%.

### Weaknesses
1. There is a lack of comparison with the latest open-source VLMs: LLaVA-OneVision, Qwen2-VL, InternVL2, etc. While these methods may use higher-quality training data and achieve stronger results, it is essential for readers to be aware of the current SoTAs. You may also explain why direct comparisons may not be feasible. It is acceptable for a research paper to fall short of SoTA results due to data quality differences, but these results should still be presented for context.

2. MMVP is crucial for demonstrating visual capability, but only QLadder is ablated on the MMVP benchmark. Why not conduct an ablation of MM-LoRA on MMVP as well? This would provide stronger support for the claims.

### Questions
1.Was the visual encoder tuning in Table 7 conducted at the pre-training or instruction fine-tuning stage?

2.Have you tried adding LoRA to the visual encoder as well?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a new MLLM named Arcana, mainly offering two improvements for boosting model comprehension on vision information. The first one is MM-LoRA, which learns two separate sets of LoRA parameters for vision and text tokens respectively, aiming to decouple the learning spaces of different modalities and better integrate the multi-modal knowledge. The other one is Q-Ladder, compared with Q-Former, it selects the vision features of different layers in ViT as the key/value vectors for different layers of Q-Ladder, instead of only using the last-layer vision token features. The experiments include the evaluation on VQA benchmarks, multi-modal benchmarks, and language benchmarks, with some ablation studies and further explorations.

### Strengths
1. The paper is quite easy to follow. People can quickly grasp the core design and the underlying motivation of the proposed two improvements. 
2. The presentation is quite ok for me.
3. The proposed method has little impact on the efficiency and the memory cost.

### Weaknesses
1. I think the proposed MM-LoRA is greatly inspired by some previous works like P-LoRA [1] in InternLM-XComposer2, visual-only modules in mPLUG-Owl2 [2] and CogVLM [3], which somehow reduces the novelty of MM-LoRA. The authors should tell the differences between MM-LoRA and these methods, along with some experiments on effectiveness and efficiency to prove the necessity of MM-LoRA. 

2. The baselines listed in Table 1, 2 are relatively old. I notice Arcana adopts ShareGPT4V data for training, but its benchmark performance seems not good as ShareGPT4V 7B model. So it is recommended to include some more advanced baseline MLLMs. 

3. It seems that the hyper-parameters introduced by MM-LoRA and Q-Ladder are not so robust and can easily affect the model performance. The authors choose the best hyper-parameters according to the ablation results. So does these hyper-parameters still work for different base LLM or architectures?

### Questions
1. Compared with Q-Former, why does the proposed Q-Ladder not require an additional stage for alignment with the vision encoder?

2. Is X_q in Q-Ladder a set of learnable tokens? Why not use instruction tokens for initialization, as done in Q-Former?

3. In the visualizations, it’s difficult to conclude that (b) demonstrates more attention on vision tokens compared to (a). But interestingly, It mainly appears that (b) has more sink tokens [1]. 

4. In Table 4, why the Q-Ladder results on 13B model are absent?


[1] Xiao et al. Efficient Streaming Language Models with Attention Sinks. ICLR, 2024.

### Soundness
3

### Presentation
4

### Contribution
3
