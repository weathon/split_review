# HyperCLIP: Adapting Vision-Language models with Hypernetworks

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 6, 3

## Abstract
Self-supervised vision-language models trained with contrastive objectives form the basis of current state-of-the-art methods in AI vision tasks. The success of these models is a direct consequence of the huge web-scale datasets used to train them, but they require correspondingly large vision components to properly learn powerful and general representations from such a broad data domain. This poses a challenge for deploying large vision-language models, especially in resource-constrained environments. To address this, we propose an alternate vision-language architecture, called HyperCLIP, that uses a small image encoder along with a hypernetwork that dynamically adapts image encoder weights to each new set of text inputs.  All three components of the model (hypernetwork, image encoder, and text encoder) are pre-trained jointly end-to-end, and with a trained HyperCLIP model, we can generate new zero-shot deployment-friendly image classifiers for any task with a single forward pass through the text encoder and hypernetwork. HyperCLIP increases the zero-shot accuracy of SigLIP trained models with small image encoders by up to 3% on ImageNet and 5% on CIFAR-100 with minimal training throughput overhead.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposed a hyper-network to generate parameters for normalization layers in the vision model of CLIP. The paper is aimed at solving the efficiency problem of CLIP on edge computing scenarios. The experiment results show that the proposed method can get better zero-shot accuracy over the CLIP baseline.

### Strengths
1. As shown in Table 2, the proposed hyper-network can improve the zero-shot accuracy on ImageNet by up to 3%.

### Weaknesses
 **Unclear Motivation and Unsupported Claims by Experiment Results**

The motivation for using a hyper-network to address CLIP's efficiency challenges in edge computing applications is unclear. The introduction does not clearly explain this choice. The experiments show performance improvement over a baseline without a hyper-network but fail to address the efficiency problem. In other words, the hyper-network enhances performance only in small-scale models rather than improving CLIP's efficiency directly. The paper does not provide a clear definition of efficiency in the context of edge computing, leaving the reader to assume that parameter count is the sole metric. This is problematic as other factors like FLOPs, memory access patterns, and model quantization are crucial for real-world edge deployment.

**Poor Writing and Difficult to Follow**

* Several English expressions are incorrect, likely due to machine translation. For instance, in lines 041-044: "These methods often include first training a large model, and then applying the chosen technique in a post-hoc fashion. Additionally, many of these methods can require specialized hardware support for actual memory and latency reduction." This section is hard to understand.

* The text includes many excessively long sentences. For example, in lines 045-050: "We propose a method of pre-training vision-language models (VLMs) that allows us to derive small vision models appropriate for deployment on edge devices without requiring multi-step training procedures or any specialized hardware. We suggest a new contrastive learning architectural design based on hypernetworks that improves performance over current state-of-the-art baselines and can additionally be used in conjunction with a variety of model compression methods for further memory or latency improvements."

**Limited References and Literature Review**

* The introduction has limited references, mentioning only three prior works (Sun et al., 2023a; Dettmers et al., 2022; Frantar & Alistarh, 2023). Including more background citations would strengthen the paper’s credibility.
* The related work section is limited to a single paragraph (L488-503). A more thorough literature review, including discussions on established methods like LoRA and adaLN would enhance this section and contextualize the paper’s contributions.

### Questions
1. Why the text transformer (a width of 768, 8 heads, feed-forward dimension of 2560) is not a small model, since the proposed HyperCLIP is targeted for compute-restricted scenarios. 
2. Is the HyperCLIP trained from scratch or initialized from SigLIP?
3. Which part of the experiments are zero-shot results, and which part are linear probing results?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces HyperCLIP, a novel architecture that adapts vision-language models by using a hypernetwork to dynamically adjust the weights of a small image encoder for each new set of text inputs. 
This approach enables the creation of zero-shot deployment-friendly image classifiers with a single forward pass through the text encoder and hypernetwork. 
HyperCLIP is designed to overcome the challenges of deploying large models in constrained environments by offering a smaller, yet powerful alternative.
The model increases zero-shot accuracy on ImageNet and CIFAR-100 with minimal training throughput overhead.

### Strengths
1. The paper proposes using a hypernetwork to generate weights for a smaller image encoder within the SigLIP contrastive pre-training framework, allowing for task-specific specialization without extensive retraining.
2. HyperCLIP achieves significant improvements in zero-shot accuracy on ImageNet and CIFAR-100, with minimal overhead, making it suitable for resource-constrained environments.
3. The method is compatible with any type of contrastive pre-training, enhancing its versatility.
4. The paper demonstrates that HyperCLIP can improve the performance of small vision models on standard benchmarks by adapting only the normalization layers.
5. HyperCLIP has the potential to democratize computer vision by enabling the deployment of high-performing models on devices with limited resources.

### Weaknesses
1. By focusing on adapting only normalization parameters, the paper may not fully leverage the potential of hypernetworks to modify other model parameters.

### Questions
1. Will you plan to release the code ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes HyperCLIP, a vision-language architecture, as an alternative efficient solution for large vision-language models. The approach leverages hypernetworks to dynamically adjust a smaller image encoder based on input text embeddings. This approach allows large vision-language models to operate effectively with reduced resource requirements, making them suitable for edge devices and resource-constrained environments. Experiments in the paper show that the proposed approach improves SigLIP zero-shot accuracy by 3% on ImageNet and 5% on CIFAR-100.

### Strengths
1. The approach presents an efficient way of using smaller models to deploy vision-langauge models for resource-constrained real-world applications.
2. The adaptive approach that modifies weights at test-time for VLMs/CLIP is novel.
3. The datasets used in experiments align well with prior works.

### Weaknesses
1. The approach doesn't generalize to broader VLMs especially the larger models. CLIP models are generally the smaller models among recent VLMs. I don't think the proposed approach generalizes to the larger VLM models such as LLaVa [1] that uses very large decoder-only transformer LLM as component. The core issue is that HyperCLIP modifies the image encoder weights based on text embeddings, which is not a common approach in larger VLMs that typically use a fixed pre-trained image encoder and focus on cross-modal attention mechanisms within the LLM. This makes the proposed method less applicable to architectures beyond CLIP.
2. CLIP models have wide range of applications, among which an important one is to use the visual features produced by the image encoder as inputs to downstream models. HyperCLIP reduces CLIP applications to only image classification. The dynamic modification of the image encoder weights in HyperCLIP makes it difficult to extract consistent visual features for use in other tasks, such as object detection or segmentation, where stable feature representations are crucial. This limits the versatility of the approach.
3. The experiments are not solid. The paper claims that HyperCLIP performs well on ImageNet in zero-shot setting. However, In Appendix A.5, the paper writes 'selects samples containing text that overlaps with ImageNet class names', which shows that the ImageNet class names are used in data collection which is used in training.  - so it's not truly zero-shot.

### Questions
Can you explain why do you think your experiments are conducted in zero-shot setting? 

My biggest concern is weakness #3.

### Soundness
1

### Presentation
1

### Contribution
2
