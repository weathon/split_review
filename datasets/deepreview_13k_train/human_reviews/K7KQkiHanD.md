# One-for-All: Generalized LoRA for Parameter-Efficient Fine-tuning

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
We present Generalized LoRA (GLoRA), an advanced approach for universal parameter-efficient fine-tuning tasks. Enhancing Low-Rank Adaptation (LoRA), GLoRA employs a generalized prompt module to optimize pre-trained model weights and adjust intermediate activations, providing more flexibility and capability across diverse tasks and datasets. Moreover, GLoRA facilitates efficient parameter adaptation by employing a scalable, modular, layer-wise structure search that learns individual adapter of each layer. Originating from a unified mathematical formulation, GLoRA exhibits strong transfer learning, few-shot learning and domain generalization abilities, as it adapts to new tasks through not only weights but also additional dimensions like activations. Comprehensive experiments demonstrate that GLoRA outperforms all previous methods in natural, specialized, and structured vision benchmarks, achieving superior accuracy with fewer parameters and computations. The proposed method on LLaMA-1 and LLaMA-2 also show considerable enhancements compared to the original LoRA in the language domain. Furthermore, our structural re-parameterization design ensures that GLoRA incurs no extra inference cost, rendering it a practical solution for resource-limited applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses an enhancement to Low-Rank Adaptation (LoRA), which is call GLoR and can be a flexible approach to optimize model inference results. Experiments on llama and vit shows that GLoRA can improve over original LoRA consistently.

### Strengths
This paper is clearly presented and well organized. The authors also provide a detailed discussion of related works and variants.

GLoRA referneces the inspirations from RepVGG, which introduces fusable parameters during training to improve model capacity. This can generally bring improvements without extra inference cost as shown in the experiments. 

GLoRA offers a unifed framework that includes multiple fine-tuning paradigms and provides a more generalized prompt mdule design per layer. The final scheme is searched via evolutional algorithms, providng better capacity and flexibility.

### Weaknesses
The authors claim that GLoRA can be "seamlessly integrate into the base network", but it seems such design is for linear layer only. But there are many other type of operators like conv / normalization layers. How can GLoRA be combined with those layers?

The evolutional search (Sec 2.4) is crucial for GLoRA as it decides which layer and scheme to use during fine-tuning. However, the details of the search and final chosen paradigms are not clearly discussed in the main paper.

As the abstract emphasiss the llama experiments. The table 2 is not solid neough to support the authors' claim. For example, the mean and variance is not included; the number of learnable paramters is missing; the lora baseline for llama-v2 is not reported. Seems like the experiments are rushed and may not be solid.

### Questions
No extra inference cost is the novelty from RepVGG or LoRA, which should be claimed as the contribution of GLoRA

The main experiments are based on ViT but abstract emphasis for llama. Please make the claim conssitent.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new PEFT module named Generalized LoRA (GLoRA), which can be applied to different tasks. The authors claim that GLoRA is more general than existing PEFT modules since it can facilitate efficient parameter adaptation by employing a more scalable structure search. Moreover, the authors conduct multiple experiments including few-shot learning and domain generalization tasks to demonstrate the effectiveness of GLoRA.

### Strengths
1. GLoRA has a re-parameterization design. It is more similar to LORA than Adapter. It makes GLoRA more flexible since it does not need to change the structure of the original backbone. And it incurs no extra inference cost.
2. GLoRA integrates multiple methods and can perform similar effects as most of the existing PEFT modules.
3. The authors conduct multiple experiments to demonstrate the generality and effectiveness of GLoRA.

### Weaknesses
1. It seems that GLoRA is not general, since it has an evolutionary search procedure to obtain the suitable components. The idea is similar to Neural Prompt Search [1]. GLoRA is not a fixed design as existing modules, which might limit its practicality. The method's reliance on a search process introduces a dependency on the search algorithm's performance, potentially leading to suboptimal solutions if the search does not converge effectively or explores the space inefficiently. Furthermore, the need for a search procedure for each new task or dataset adds an overhead that fixed-design PEFT modules avoid.
2. GLoRA has a large search space, which might yield huge time costs. However, the authors have not mentioned the actual training time and memory cost of GLoRA, which is very important for PEFT modules. The lack of explicit details on the computational resources required to perform the search is a significant oversight, as it directly impacts the practicality and accessibility of the proposed method. Without this information, it's difficult to assess whether the performance gains justify the additional computational burden.
3. The authors introduce multiple PEFT modules including AdaptFormer, LoRA, etc. So could GLoRA simulate all of these modules? As far as I know, these modules are applied on different layers (LoRA in multi-head self-attention layers, while AdaptFormer in MLP layers). And which layer is GLoRA applied in practice?

### Questions
See "Weaknesses".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents Generalized LoRA (GLoRA), an efficient framework for fine-tuning machine learning models. Building on Low-Rank Adaptation (LoRA), GLoRA introduces an advanced prompt module that not only refines pre-trained model weights but also modulates intermediate activations. Uniquely, this prompt module operates individually across each model layer, ensuring versatility across various tasks and datasets.

GLoRA employs a cohesive mathematical strategy to adapt to new tasks, modifying both weights and activations. This methodology positions it strongly for transfer learning, few-shot learning, and domain generalization.

The authors substantiate GLoRA's efficacy through experiments on diverse datasets and tasks, encompassing downstream fine-tuning, few-shot learning, domain generalization, and recent popular LLMs. The results demonstrate GLoRA's superior performance over prior techniques in these areas. Remarkably, despite its heightened capability, GLoRA demands fewer parameters and computations without incurring additional inference costs, akin to LoRA, making it an optimal choice for resource-constrained applications.

### Strengths
GLoRA effectively consolidates previous parameter-efficient fine-tuning methods within Equation 10. Importantly, all adjustable support tensors are linear, which makes structural re-parameterization readily accessible.

The paper highlights GLoRA's commendable capacity to generalize across diverse tasks, an invaluable quality in machine learning and a frequently challenging facet of model development.

### Weaknesses
Structural re-parameterization requires storing the full set of weights (including bias) for every individual downstream task. This means that as the number of these tasks increases, the storage needs can become prohibitively large. Although this approach might improve inference performance, the substantial storage overhead can be a major impediment for real-world deployment, especially when multiple tuned-models are needed to handle different downstream tasks.

The clarity of the paper is occasionally compromised by abrupt topic transitions, such as the unexpected introduction of "GLoRA with Higher Capacity" in section 2.6, without prior elucidation of terms like H_i and H_ini. A more coherent and gradual introduction of these concepts would enhance readability.

The authors touch on memory and training time costs but fail to provide concrete figures to substantiate their claims. Offering detailed, quantitative data on these costs would provide readers with a clearer picture of GLoRA's practical ramifications.

### Questions
Please refer to 'weakness' part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a general form of low-rank adaptation for vision and language large models, based on a unified formula which the authors claim to encompass serveral previous parameter efficient finetuning methods such as VPT and LoRA. As for training networks with GLoRA, the authors exploit an evolutionary strategy to search for the best subnet after training the supernet. Extensive experiments on vision and language benchmarks show the effectiveness of the propose method.

### Strengths
1. The paper rethinks serveral previous PEFT methods and unifies them with a general form, contributing a novel perspective.
2. To obtain the task-specific GLoRA network, the authors first train the supernet and then search for the best subnet.
3. Extensive experiments are conducted on both vision and language benchmarks, and also in few-shot learning and domain generalization, showing the effectiveness GLoRA.

### Weaknesses
1. The presentation of the paper could be improved, especially when comparing with previous PEFT methods. The authors could draw figures or list tables to show how existing methods can be integrated into GLoRA framework, e.g. what are the specifications of the A/B/C/D/E support tensors in Eq. (10). Specifically, it's unclear how the proposed method's parameterization relates to methods like LoRA, where a low-rank matrix is added to the weight matrix, or VPT, which introduces learnable prompt tokens. A more detailed breakdown of how the support tensors in GLoRA map to these existing approaches would significantly improve clarity. For instance, it is not immediately obvious how the vector support tensors in GLoRA can mimic the behavior of prompt tokens in VPT or the low-rank matrices in LoRA.
2. I wonder how much training time (supernet training and subnet searching) does GLoRA cost, such that to compare with existing methods more clearly from the perspective of training efficiency. The paper lacks a clear comparison of the computational cost, including both training time and memory usage, against existing PEFT methods. Without this, it's difficult to assess the practical applicability of the proposed method. A detailed analysis of the training time for both the supernet and the subnet search, along with a comparison to methods like LoRA, would be essential for a fair evaluation.

### Questions
1. There exist some typos: 1) "PETL"(maybe PEFT?) at the end of page 3 (first line of Sec. Limitations); 2) 4th line of page 4: "wieght" -> weight.
2. How about the performance if we do not add the weight/bias scaling term: W_0 x A and D x b_0 in Eq. (10) ? Or else, which of the five tensors are really necessary in terms of efficiency and efficacy ?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
