# Low-Rank Interconnected Adaptation across Layers

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
Low-rank adaptation (LoRA) is a powerful parameter-efficient fine-tuning method that utilizes low-rank projectors $A$ and $B$ to learn weight updates $\Delta W$ for adaptation targets $W$. Previous research has shown that LoRA is essentially a gradient compressor, performing random projections on the gradient using a fixed projection matrix $A_0$. However, this setup restricts the overall weight update to be low-rank, which limits the adaptation performance. In this paper, we propose \underline{l}ow-rank \underline{i}nterconnected adaptation across \underline{l}a\underline{y}ers (Lily). Specifically, we employ a hierarchical framework where low-dimensional projectors (LPs) retained for downward projection at a particular level, while globally-shared high-dimensional projector (HP) experts perform upward projection across all levels of layers. Lily uniquely connects each LP to all HP experts, therefore the gradient projections are no longer dominated by fixed projection matrices, but rather by selective combinations of all the projectors, thereby breaking the low-rank constraint of LoRA. Furthermore, Lily's cross-layer connections facilitate the capture of intricate information and dependencies across different layers, thereby enhancing the model's representational capabilities. Experiments across various modalities, architectures, and model sizes underscore Lily's great performance and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a parameter-efficient fine-tuning method based on the concept of LoRA. Specifically, they introduce a technique to construct the B matrix through a weighted combination of inter-layer weights during inference. This approach allows the adapter to overcome the low-rank limitation, improving its expressiveness. The proposed method is motivated by findings that suggest LoRA functions as a gradient projector, with updates primarily influenced by the initialization of the A matrix. The authors evaluate their method on both transformer-based and Mamba-based models, comparing it with baseline methods across various NLP and image tasks. Additionally, they conduct ablation studies and qualitatively assess the learned features.

### Strengths
- Overall, this paper is well-written. The authors provide a comprehensive description of the proposed method, and the appendix is detailed.

- The authors apply the proposed method to various models across different modalities, demonstrating its effectiveness. They include both quantitative and qualitative evaluations.

- The proposed method is inspired by a thorough analysis of the existing LoRA approach.

### Weaknesses
 - Since the authors derived the forward path of the proposed method in Section 3.2, would it be possible to analyze the rank gain? A theoretical analysis of the improvement assuming a single layer could be helpful.

- It would be beneficial if the authors could further evaluate the improvement qualitatively, as the current gains are not particularly substantial. For example, in the RoBERTa-base experiments, the proposed Lily method only outperforms others on 2 out of all tasks. Additionally, AdaLoRA does not outperform standard LoRA, which is somewhat counterintuitive. Could the authors explore conducting experiments on larger BERT models? Given that different PEFT methods involve varying numbers of learnable parameters, is it fair to compare these methods directly in light of these parameter differences?

- The authors have renamed the A and B matrices in LoRA as the downward low-dimensional projector and upward high-dimensional projector, respectively.

### Questions
- The authors might want to discuss the difference of the proposed method with several related recent works. For example, in [HydraLoRA], the authors introduced a LoRA MoE method which share the same A matrices but also a mixture of B matrices. In [LoRA Asymmetry], the authors proposed freezing A matrices and only training B, backed by a another line of theoretical study. Another related works, [LoRA+], the authors analyze the gradient of LoRA matrices and propose to use a larger learning rate for B to improve the performances. 

[Tian, Chunlin, et al. "HydraLoRA: An Asymmetric LoRA Architecture for Efficient Fine-Tuning." arXiv preprint arXiv:2404.19245 (2024).]

[Zhu, Jiacheng, et al. "Asymmetry in low-rank adapters of foundation models." arXiv preprint arXiv:2402.16842 (2024).]

[Hayou, Soufiane, Nikhil Ghosh, and Bin Yu. "Lora+: Efficient low rank adaptation of large models." arXiv preprint arXiv:2402.12354 (2024).]

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a novel hierarchical adaptor for fine-tuning the Transformer. The results show a high advance of proposed method on the NLU and computer vision tasks.

### Strengths
1. The proposed methodology that considers cross-layer interactions is new to me.
2. The empirical results show the method's potential in various domains.

### Weaknesses
The major flaws are about the presentation.

1. Some derivation steps could be merged and only the important steps can be given. The blanks could be reserved for discussing the intuitions and analysis.
2. The fonts in the figures are too small. Normally they should be larger than the smallest font in the main body.

### Questions
How does the proposed method affects the efficiency of the adaptation?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the limitation of weight update in LoRA the limitations of weight updates in LoRA, highlighting that it functions as a random projection on an initialized low-rank matrix. To address such limitations, the author introduces low-rank interconnected adaptation across layers (Lily), which employs model-wise shared low-rank matrices inspired by the mixture of experts (MoE) framework. Extensive experiments have been conducted to demonstrate the effectiveness and adaptability of the proposed methods.

### Strengths
1. The motivation is reasonable as learning multiple shared low-rank matrices can represent various low-rank subspaces, and their combinations have the potential to capture information across a higher-rank space.

1. Comprehensive experiments demonstrate the effcacy and adaptability of Lily, achieving state-of-the-art results across a diverse set of tasks in both language and vision domains.

### Weaknesses
1. The presentation of the methodology has significant room for improvement.

    1.  The description of the methodologies (lines 204-210) and the framework depicted in Figure 1 within the main text differ from the final implementation discussed in Appendix A.1.1 (lines 770-778). In the main text, low-dimensional projectors (LPs) are described as being tied to each layer of a module, while high-dimensional projectors (HPs) are shared across the model. However, Appendix A.1.1 indicates that Lily essentially learns a set of model-wide shared LPs and HPs that are selectively applied to specific layers. This discrepancy introduces confusion regarding the core mechanism of the proposed method, as the main text suggests a layer-specific approach while the appendix details a model-wide sharing strategy for LPs, which are then selectively applied to layers. The lack of clarity in the main text regarding the sharing of LPs across layers makes it difficult to understand the actual implementation.

    1.  The derivations from Eqn. 9-14 lack rigor in scenarios involving multiple LPs and HPs. To extend the derivation from Eqn. 5-20 in [1] to multiple LPs and HPs, several adjustments are needed:

         - **First**, Eqn. 9 should incorporate a summation over the LPs, leading to a double summation in Eqn. 11. The current formulation does not account for the possibility of multiple low-rank projectors being applied to a single layer, which is a crucial aspect of the proposed method.

         - **Second**, gradient with respect to each $B_{i}$ should be considered. The derivation does not explicitly show how the gradients are computed with respect to each of the multiple high-dimensional projectors, which is necessary for understanding the backpropagation process.

         -  **Third**, the applicability of Theorem 2.1 in [1] for multiple LPs and HPs must be proven before use. The paper assumes that the theorem can be directly applied to the multi-projector scenario without providing any justification, which is a significant oversight.

         Without proper proofs, simple substitutions may lead to inaccuracies, making the current mathematical discussion unconvincing. The lack of rigorous mathematical justification undermines the theoretical claims of the paper.

    1.  Eqn. 17 - 18 are just simple math that does not warrant separate discussion. In addition, the definition of $s$ in Eqn. 19 - 20 is missing.

    1.  In essence, it is advisable to directly present the core idea (a set of multiple LPs and HPs) if the theoretical discussion lacks sufficient proof.

2. Concerns regarding experimental results.

    1.  The reported number of trainable parameters for Lily is unclear.

        - **First**, Lily is reported to have the same parameter count as LoRA on GLUE tasks while using only 1/4 of the parameters compared to LoRA on ViT tasks. Given that vision tasks are typically more complex than GLUE tasks and generally require more parameters, this discrepancy needs clarification. The paper does not provide a clear explanation for why the parameter reduction is so different between the two types of tasks.
        
        - **Second**, based on the configurations in Tables 9 and 10, Lily only uses 2 LPs and 2 HPs shared across the entire model. Under this setup, the parameter count should be substantially lower than that of LoRA for various backbones, such as RoBERTa-base/ViT-base (12 layers), yet Lily's parameter count appears comparable to LoRA on GLUE. Further explanation is needed to resolve this inconsistency. The paper needs to provide a detailed breakdown of how the parameter count is calculated for Lily, especially when using shared LPs and HPs.

    1.  Efficiency is a critical aspect of PEFT. However, for the most computationally demanding task, commonsense reasoning, the parameter count is not provided. It would be helpful to include the parameter count and training time for this task, as shown in [2]. The absence of this information makes it difficult to assess the practical efficiency of the proposed method.

    1.  The experimental results do not include MNLI and QQP, despite these tasks being listed in the configuration table.

### Questions
See Weakness.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The Authors propose an alternative ansatz to LoRa for parameter efficient finetunig of neural networks. In particular, they propose to connect all low-rank adapters of a given network to each layer,  combined with a router. This way a weighted sum of low-rank adapters is modifying the parameters of a given layer. 
The authors demonstrate the method in an arrray of contemporary benchmarks.

### Strengths
I find the idea of using a sum of low-rank adapters interesting. 
The ansatz potentially enables a high rank adaptation using a sum of low-rank adapters. 

The method is demonstrated at an impressive number of numerical tests.

### Weaknesses
While the general idea is promising and supported by numerical evidence, I find the presentation of the method description and theoretical premisses thereof lacking in soundness and readbility. In my opinion the first part of the paper requires a major revision before being publishable.

In particular: 

- The work is based upon the premise that the B matrix is very close to 0 or equals to zero. This claim has been investigated by Hao et al. however under strong assumptions about the zero initialization of B and very small learning rates and only for the "classical" LoRa setup. 
The authors of this work just use the conclusions of Hao's analysis as the premise for their method. Two points are critical here
 1) The assumptions in the LoRa setting are not well communicated in both Introduction (Section 1) and Section 3.1. In Section 3.1 the mathematical notation is very sloppy, using equality signs between eq. 2 and 3, when this is in reality a first order approximation for small learning rates and values of B. This is missleading, especially for readers not familiar with Hao's work. The same applies for eq. 9 and 10. 

 2) The validity of the assumptions need to be shown for the newly introduced ansatz and method of this paper, instead of just taken for granted. 

- The authors claim that their ansatz (eq. 14). allows high rank updates with low-rank matrices. While it is generally true, that a sum of (even) rank 1 matrices can be high rank, it does not have to be the case. An (very simple) numerical experiment is needed to demonstrate the effectivity of this ansatz. One could think of a matrix regression problem with said ansatz. A stage 2 numerical experiment would be the anlysis of the effective ranks of each layer of an adaption of the proposed kind. 
The same ciritique is applicable for the MoE ansatz in the paper. 

- The method should be illustrated with an algorithm. 

- The effective computational efford of the method needs to be analyzed. Having strong interconnections between layers significantly increases the complexity of the gradient tape, which increases compute and memory consumption of the method, potentially defeating the purpose of PEFT. 

- Some statements are quite vague, e.g. Line 226: "shallow and deep inputs" what does that mean?

### Questions
- Does the method require that exactly L (where L is the number of layers) low-rank adapters need to be combined? I think the notation can be simplified by defining the number of adapters independently of layers, especially for the MoE ansatz.

- Have you measured the effictive compute batch training time in comparison with adalora or lora?
- Can your method be extended to be rank adaptive? 
- How does the norm of B change during training? Your method is based upon the assumption that the values of B are very small. Is this still the case after several epochs? In this regard: What are the practical thresholds for the learning rate, where the method assumptions breal?

### Soundness
2

### Presentation
2

### Contribution
3
