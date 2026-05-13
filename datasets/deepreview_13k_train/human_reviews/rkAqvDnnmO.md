# A Simple Efficiency Incremental Learning Framework via Vision-Language Model with Multi-Adapters

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Incremental Learning (IL) aims to learn new tasks while preserving previous knowledge. Integration of the zero-shot learning capabilities of pre-trained vision-language models into IL methods has been a significant advancement. However, these methods face three primary challenges: 1) the need for improved training efficiency; 2) the need for a memory bank to store previous data; and 3) the need for a strong backbone to augment the model’s capabilities. In this paper, we propose the $\textbf{SimE}$ that is a $\textbf{Sim}$ple $\textbf{E}$fficiency framework which is the vision-language model with an adapter designed for solving the IL task. We report a remarkable phenomenon that there is not always a direct positive correlation between the number of adaptive adapter connections and the model's incremental learning (IL) capabilities. While increasing the number of adapter connections between transformer blocks positively impacts model performance, within transformer blocks, adding more adaptive connections in smaller incremental stages does not enhance, and may even degrade the model's IL ability. Such improvement only occurs at advanced incremental stages. Extensive experimental results show SimE surpasses traditional methods by 9.6\% on TinyImageNet and outperforms other CLIP-based methods by 5.3\% on CIFAR-100. Notably, the SimE, with only thousands of parameters and a 0-size memory bank, exceeds the ZSCL with 140 million parameters and also beats the CoOP with a 1000-size memory bank. Besides, we also conduct a systematic study to enhance the utilization of the zero-shot capabilities of CLIP. We suggest that the backbone of the encoder in SimE use the image encoder from CLIP that is pre-trained on large datasets, like LAION-2B, and larger model sizes, such as ViT-L/14, for IL tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduce a simple and efficient IL framework, SimE, which combines a vision-language model with an adapter designed for efficient IL tasks. SimE is distinguished by its efficiency in three key areas: GPU usage, the number of trainable parameters, and memory size.

### Strengths
1. This paper is easy to follow.
2. The proposed method is simple and efficient.
3. The performance of the proposed method surpasses existing methods.

### Weaknesses
1. Scientific contribution: as far as I know, the application of adapters in incremental learning is not a new thing, and the method proposed in this article is just a slightly more complex application of adapter.
2. Experimental setup：testing on Cifar 100 may not be meaningful as the data used for pre-training contains a large amount of data similar to Cifar 100.

### Questions
See weakness.

### Soundness
3

### Presentation
2

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
The paper presents SimE, a framework for Incremental Learning (IL) that integrates a Vision-Language model (VLM) with a novel Multi-Adapter setup. Here, SimE employs a pre-trained CLIP encoder in different configurations, with adapters that fine-tune only a reduced amount of parameters. The approach claims to be GPU and memory efficient while maintaining performance on CIFAR-100 and TinyImageNet. It also highlights the discovery that, within transformer blocks, adding more adapters does not always benefit IL performance. This paper asserts that SimE outperforms existing CLIP-based models and offers insights into optimizing CLIP zero-shot capabilities by exploring various backbones and adapter configurations.

### Strengths
The paper has some strengths, presented here:
- The introduction of Multi-Adapters in an IL context is an underexplored perspective, with good insights about the adapters role and capabilities in retaining old information while keeping learning.
- SimE framework needs a reduced amount of trainable parameters and memory and GPU resources while performing better than all the CL methods compared.
- Experimental results are very complete, with comparisons across multiple datasets and configurations to validare claims.

### Weaknesses
The paper has some weaknesses or flaws that could be addressed to improve the overall result:
- Although the SimE framework claims to use Vision-Language models, the reality is that only variants of CLIP’s image encoders are used. Testing other models with the same zero-shot capabilities (e.g., SigLIP) would be helpful to understand if this framework can be general across Vision-Language models or if it is just specific for CLIP. The current experiments do not sufficiently demonstrate the framework's applicability beyond the CLIP architecture, limiting the impact of the findings.
- Although the paper presents a comparison against some CL methods, it lacks the comparison with other well-known parameter efficient CL methods (e.g., prompt methods such as DualPrompt or Learning to Prompt, among others). This omission makes it difficult to assess the true novelty and effectiveness of SimE compared to other state-of-the-art parameter-efficient continual learning techniques.
- Testing the SimE framework with other adapters (e.g., IA3) could strengthen generalizability claims regarding the performance gain relative to adapters in terms of number and position within the backbone. The current focus on a single type of adapter limits the understanding of how the framework interacts with different adapter designs and their impact on performance.

### Questions
- Given the variability results across backbone architectures, are there plans to test this framework on a wider set of VLM backbones beyond CLIP?
- Can the authors elaborate on why additional connections in smaller incremental stages do not enhance IL performance? A theoretical or intuitive explanation would be helpful.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel method for class-incremental learning on vision-language models (VLMs). The primary objective is to address the issues of efficiency in current Incremental Learning(IL) models. The paper introduce SimE, a novel method that can utilizes an adapter with less parameters and achieves superior accuracy than other IL methods. The paper also provide some analysis of adapter connections and different backbones The paper also provides an analysis of the impact of adapter connections and different backbones on the zero-shot capabilities of CLIP.

### Strengths
The paper is easy to follow, the issues are clearly presented.

This paper identifies an important issue with existing IL models and provides a novel method, SimE, which can outperform current IL models in three key areas. The extensive experiments provide solid evidence.

This paper explores the relationship between the number of adapter connections and the model’s IL capabilities. The ablation studies are conducted very comprehensively.

### Weaknesses
The writing quality needs improvement; there are some writing mistakes in Figure 4, and the lack of labels and explanations in Figure 4 confuses me.

The overall method is simple, and the novelty of the paper is limited. Using prototypes for incremental learning is common, and achieving efficiency has been discussed in previous work. Designing different adaptation structures has also been explored, so the Multi-Adapter is not particularly impressive. The specific placement and number of adapters, while explored, does not seem to provide a substantial leap in performance or insight beyond what is already known about adapter-based fine-tuning. The paper does not delve deeply into the theoretical underpinnings of why the observed adapter placement effects occur, which weakens the contribution.

### Questions
The paper conducts a systematic study and finds that larger datasets, pretrained models, and larger backbones have stronger zero-shot capabilities for incremental learning. However, the experiments only use the ViT backbone; it would be better to test on different backbones, such as ResNet and Swin Transformer. Additionally, I am concerned about another situation: if the pretrained dataset has a significant gap with the downstream dataset, does this phenomenon also exist?

### Soundness
3

### Presentation
2

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
The paper proposes SimE, an incremental learning method that uses parallel adapters in conjunction with the features of the frozen backbone. The proposed method does not need a memory buffer. It explores the effect of different CLIP backbones on performance on Split CIFAR100 and TinyImageNet. The paper sugests to use CLIP L/14 pretrained on LAION2B for incremental learning. It analyzes the effect of increasing the number of adapters and concludes that increasing the number of adapters does not lead to monotonic improvement but can also hurt performance.

### Strengths
The proposed method does not need a replay buffer, which could be advantageous in situations where data must be deleted (for e.g. privacy or legal reasons).

### Weaknesses
1. **Choice of baselines**
- The comparison with UCIR, PASS, DyTox, DER is not fully accurate, as they start from a randomly initialized model and SimE starts with a powerful CLIP backbone (as noted in Table 1). When starting with a strong pretrained backbone like CLIP, which is mostly frozen throughout training, it's expected that SimE will perform well as it also uses the frozen features. Similarly, a comparison of SimE with CLIP ViT-L/14 CLIP with other methods that use a weaker backbone are is also not fair. The performance gains observed might be primarily attributed to the strong pre-trained features of CLIP rather than the proposed method itself. A more rigorous comparison would involve using the same backbone for all methods or comparing against methods that also leverage strong pre-trained models.
- A number of prior works leverage pretrained models for incremental learning. [1-5] show strong incremental learning abilities without the use of a memory buffer at a very small parameter budget. These methods would present a better baseline for comparison. Specifically, methods like L2P, DualPrompt, and CODA-Prompt, which use prompt-based learning with pre-trained models, should be included as baselines to provide a more comprehensive evaluation of SimE's performance.

2. **Scope of evaluation benchmarks**
- The evaluation in the paper is limited to Split-CIFAR100 and TinyImageNet. Considering the method uses a pretrained CLIP model, which shows a strong zero-shot performance on most standard benchmarks, the proposed method should be evaluated on larger scale benchmarks, e.g., full Split-ImageNet1000 using the standard ImageNet resolution or DomainNet. The current benchmarks do not sufficiently demonstrate the scalability and robustness of the proposed method. Evaluating on more diverse and challenging datasets is necessary to validate the general applicability of SimE.

3. **Limited contributions**
- It is unclear what the primary contribution of the paper is. The core idea of using adapters with a frozen backbone is not novel, and the specific configuration of adapters within the transformer architecture needs more justification. The paper should clearly articulate the novel aspects of SimE beyond the incremental update over AdapterFormer.
- The proposed method SimE appears to be an incremental update over AdapterFormer. However, without comparisons with proper baselines (as mentioned in Point 2 above), and the statement on line 147 that "SimE utilizes an adapter with only thousands of parameters, yet achieves superior accuracy compared to other baseline IL models with millions of parameters" may not be fully accurate. This claim needs to be supported by comparisons against methods that also use pre-trained models and parameter-efficient fine-tuning techniques.
- The authors suggest the use of CLIP ViT-L/14 pretrained on LAION2B for CIFAR100 and TinyImageNet and compare the performance of SimE with various pretraining datasets (Table 3) and backbones sizes (Table 4). However, it is expected that using a stronger frozen backbone will lead to better performance, especially when the downstream tasks being studied already show very strong zero shot performance. Prior works in parameter efficient fine-tuning literature have shown that finetuning bigger and better models leads to better performance on downstream tasks [6]. The observation that pretraining dataset is important for good performance has also been studied before in [7]. It's unclear what this paper's contribution in this regard. The paper needs to demonstrate a clear advantage of SimE beyond what is already known about the benefits of larger pre-trained models and datasets.

4. **Increased cost of computation during inference**
- As stated in Appendix A, the frozen backbone is used during inference along with the finetuned backbone with Adapters. This increases the cost of computation during inference. The paper should address this limitation and discuss potential strategies for reducing the inference cost, such as knowledge distillation or pruning techniques.

### Questions
**Possible typos**:
- In Figure 2, the LayerNorms have been shown after the attention and MLP blocks, but in most architectures after the original transformer paper, LayerNorms are use before the attention and MLP blocks, including the CLIP ViTs used in this work.
- Equation 3 sugests that the attention block is applied after the MLP block, but in standard transformer architectures, attention precedes the MLP block. This might be a typo since equation 1 defines the structure correctly.
- In Figure 2 (A), the representation for adaptformer is inaccurate: AdaptFormer uses a residual MLP in addition to the standard residual connection, but this is not reflected in the figure. Regarding SimE, can the authors clarify if the standard residual connections removed, as shown in Figure 2 B,C,D?

### Soundness
2

### Presentation
2

### Contribution
2
