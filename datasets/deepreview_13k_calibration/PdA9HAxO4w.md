# One Perturbation is Enough: On Generating Universal Adversarial Perturbations against Vision-Language Pre-training Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
Vision-Language Pre-training (VLP) models have exhibited unprecedented capability in many applications by taking full advantage of the multimodal alignment. However, previous studies have shown they are vulnerable to maliciously crafted adversarial samples. Despite recent success, these methods are generally instance-specific and require generating perturbations for each input sample. In this paper, we reveal that VLP models are also vulnerable to the instance-agnostic universal adversarial perturbation (UAP). Specifically, we design a novel Contrastive-training Perturbation Generator with Cross-modal conditions (C-PGC) to achieve the attack. In light that the pivotal multimodal alignment is achieved through the advanced contrastive learning technique, we devise to turn this powerful weapon against themselves, i.e., employ a malicious version of contrastive learning to train the C-PGC based on our carefully crafted positive and negative image-text pairs for essentially destroying the alignment relationship learned by VLP models. Besides, C-PGC fully utilizes the characteristics of Vision-and-Language (V+L) scenarios by incorporating both unimodal and cross-modal information as effective guidance. Extensive experiments show that C-PGC successfully forces adversarial samples to move away from their original area in the VLP model's feature space, thus essentially enhancing attacks across various victim models and V+L tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a method to learn universal perturbations that can transfer across different Vision-Language Pre-training (VLP) models and downstream tasks. The authors leverage contrastive loss to disrupt cross-model interactions and use a Euclidean distance-based loss to maximize the distance between adversarial data and the original data. Experimental results show that the proposed method achieves strong attack performance on various VLP models and downstream tasks.

### Strengths
1. The paper focuses on an important task of evaluating robustness of VLP models.
2. Both adversarial images and texts are learned.

### Weaknesses
Several concerns remain:
1. Motivation: 
- In the abstract, the authors claim to "fully utilize the characteristics of Vision-and-Language (V+L) scenarios by incorporating both unimodal and cross-modal information." However, the authors do not seem to fully exploit the characteristics of different V+L scenarios or tasks. The paired relationships between images and texts are a common aspect of cross-modal attacks, and it is unclear what novel insights are derived from this task. Furthermore, different cross-modal tasks, such as cross-modal retrieval and image captioning, focus on distinct contents and relationships between images and texts, each with unique characteristics. The paper does not sufficiently explore these task-specific characteristics, raising concerns that the approach may not fully leverage the diverse aspects of V+L scenarios.
- In the introduction, Figure 1 compares two methods and claims that "the generator-based approach GAP consistently achieves superior ASR compared to UAP." Since UAP uses the DeepFool method to learn perturbations, its inferior performance compared to a generator-based approach does not necessarily demonstrate the superiority of the generator-based method over other approaches, e.g., PGD. More experiments including comparisons with other strong baselines like PGD are needed, along with a more comprehensive analysis of why generator-based methods are required to support this claim. It is also unclear why generative methods achieve significantly better performance compared to PGD methods, and the underlying rationale behind this difference should be explored.
2. Algorithm: 
a: My biggest concerns are the definition of universal perturbation learning and adversarial text learning.
- The authors use generators to produce adversarial data based on cross-modal conditions. The main advantage of universal adversarial attacks is their ability to produce perturbations that are generalizable across all data without needing to generate sample-specific perturbations, thereby improving efficiency. In other words, universal perturbations should be independent of the test data and applicable to unseen data. However, relying on cross-modal conditions appears to conflict with this objective. If cross-modal conditions are required, why not generate sample-specific perturbations instead? The authors need to clarify how to maintain the universality of the perturbations without using cross-modal conditions. Additionally, the authors should report results of universal attacks for more scenarios, e.g., using perturbations generated on the Flickr30k dataset to attack models on the MSCOCO dataset.
- Learning adversarial text perturbations requires ensuring that they do not compromise the quality of original texts. However, the authors did not address this, rendering the algorithm impractical. Calculating the semantic similarity between clean and adversarial texts cannot solve this problem. Instead, the higher similarity between them shows that the proposed method does not significantly alter the original semantics in the feature spaces. Thus, it cannot achieve effective attacks. The authors should prove that adversarial texts are visually plausible. Further verifications are required, such as utilizing proposing metrics to evaluate the semantic consistency of perturbed texts or discussing potential methods to constrain the text perturbations to maintain readability and coherence.
b. In addition, the authors utilize contrastive learning to disrupt the cross-model relationships and use the Euclidean distance-based loss to enlarge the distance between adversarial data and their original counterpart. First, the authors utilize contrastive learning to enlarge the gap between multiple texts and minimize the distance with diverse target texts. However, I question whether setting different targets can truly maximize the distance between adversarial and original images. An ablation study is necessary to verify this, such as comparing the proposed approach with a baseline that doesn't use diverse target texts, or to analyze how different choices of target texts affect the effectiveness of the perturbations. Second, the authors use two distinct losses to maximize the distance between adversarial images and each modality in the original image-text pairs. It is unclear why two losses are needed, rather than using a unified loss for both modalities. Additional experiments comparing their two-loss approach with a unified loss approach, and analyze the impact on both cross-modal and intra-modal relationships should be conducted. 

c. Perturbation learning methods, including set-level augmentation, maximizing both intra- and inter-model differences, and leveraging contrastive learning, have already been explored by current approaches [1,2]. The specific contribution of this method remains unclear, aside from generating universal perturbations instead of sample-specific ones. Furthermore, the distinction between the generation of universal and sample-specific perturbations remains unclear.

5. Experiments:
- Previous works on universal adversarial attacks for VLP models should be discussed and compared, such as [3]. Additional comparison with relevant methods should be provided.
- The authors apply data augmentation to improve the method's effectiveness, but additional comparisons with other augmentation techniques should be conducted to better demonstrate the proposed method's superiority. Examples include ScMix [3] and Admix [4].

### Questions
Please refer to Weaknesses.

### Soundness
1

### Presentation
2

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
This paper addresses the vulnerability of Vision-Language Pre-training (VLP) models to universal adversarial perturbations, which are instance-agnostic and do not require individual perturbations for each input. The authors introduce a novel attack method, the Contrastive-training Perturbation Generator with Cross-modal conditions (C-PGC), which leverages contrastive learning to disrupt the multimodal alignment in VLP models. Experiments are conducted across multiple VLP models and tasks.

### Strengths
1. The proposed UAP framework addresses the inefficiencies of instance-specific attacks by incorporating cross-modal and unimodal guidance within a contrastive training setup, representing an advancement in universal adversarial attack methods.

2. The paper thoroughly evaluates C-PGC's effectiveness across multiple VLP models and downstream tasks, and additionally analyzes various defense strategies to mitigate the potential risks posed by C-PGC.

### Weaknesses
The proposed method leverages image and text attacks alongside cross-modal contrastive learning to generate universal adversarial perturbations. While this approach shows promise, the novelty may not be fully evident. I recommend that the authors consider further highlighting and reorganizing the unique contributions of the paper to enhance its clarity and impact.

As shown in Figure 4, the adversarial texts exhibit a clear semantic gap from the original texts. Thus, would using special characters (e.g. ##*) for the universal adversarial word be more effective?

### Questions
1. In the text modality attack, how do the authors maintain semantic similarity between original and adversarial texts? In the experiments, the authors should provide the similarity scores (e.g. bert_score) between original and adversarial texts to demonstrate that the modifications do not significantly alter the text's semantics.

2. The authors should explain how ASR is calculated in the main text.

3. As shown in Figure 4, the adversarial texts exhibit a clear semantic gap from the original texts. Thus, would using special characters (e.g. ##*) for the universal adversarial word be more effective?


4. The authors propose a contrastive training perturbation generator to produce universal adversarial perturbations for images and text. I am curious about how this generator differs from general UAP methods (e.g. Data-free Universal Adversarial Perturbation and Black-box Attack ), justifying its designation as a "generator."

I look forward to your detailed response.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a novel framework, C-PGC, designed to generate Universal Adversarial Perturbations (UAPs) targeting Vision-Language Pretraining (VLP) models. The authors introduce a cross-modal conditional perturbation generator, which leverages both single-modal and cross-modal features to disrupt the learned alignment between visual and textual representations in VLP models.

### Strengths
The writing style of the paper is commendably clear and concise, making it accessible to a broad audience within the machine learning and computer vision communities. The authors have taken care to present the technical details in a manner that is straightforward and easy to follow, even for readers who may not be deeply familiar with adversarial attacks or VLMs. The method’s components are explained in a way that balances technical rigor with simplicity. This makes the paper highly readable and ensures that a wide range of researchers and practitioners can engage with its contributions.

The experimental results demonstrate that the proposed C-PGC framework performs well across several benchmarks. The authors have conducted comprehensive experiments on multiple well-established datasets and across various VLP models. The results show consistent improvements in attack success rates (ASR) across both white-box and black-box settings.

### Weaknesses
The paper, while strong overall, has several areas for improvement:

1. **Use of Contrastive Loss**  
   The inclusion of contrastive loss (\(\mathcal{L}_{CL}\)) feels somewhat forced. Since the goal is to perform untargeted attacks, it seems unnecessary to rely on contrastive loss, which is typically used to enforce alignment between representations. While the authors have shown its utility through ablation studies, the logical foundation of using contrastive loss in an untargeted setting remains unclear. The paper could be improved by either rethinking the rationale behind using \(\mathcal{L}_{CL}\) or exploring alternative loss functions better suited for untargeted attacks. Specifically, the current approach minimizes the contrastive loss, which intuitively should bring the representations closer, not further apart, which is the goal of an untargeted attack. This discrepancy needs to be addressed with a more coherent explanation or a different loss function.

2. **Choice of Positive and Negative Samples for Contrastive Loss**  
   The current method of manually selecting the farthest sample as the positive or negative example feels arbitrary and unnecessarily complex. In the context of untargeted attacks, where the objective is not to make the adversarial sample resemble a specific class, it would make more sense to introduce a synthetic, "fictitious" sample that maximally deviates from the original, rather than relying on the farthest feature-distance sample. This approach could simplify the process and make the use of contrastive loss more coherent in the untargeted setting. The current method lacks a clear justification for why the farthest sample is the optimal choice for disrupting the model's alignment, and a more principled approach is needed.

3. **Limited Comparison with State-of-the-Art**  
   The comparison of the proposed method only with GAP, a 2018 work, limits the scope of the evaluation. Given the rapid advancements in adversarial attack methods, comparing against more recent techniques would provide a clearer picture of the method’s competitiveness. For example, comparing with more contemporary adversarial generation methods would strengthen the experimental section and make the results more relevant to current research. The absence of comparisons with recent, more sophisticated attack methods makes it difficult to assess the true novelty and effectiveness of the proposed approach.

4. **Visual Design of the Framework Diagram**  
   The framework diagram could benefit from improved design and color harmony. While this is a minor issue, it affects the overall presentation quality. The authors could refer to well-designed diagrams from recent top-tier papers to make the visualizations clearer and more appealing.

These adjustments would enhance the logical foundation of the method and improve both the clarity and relevance of the experimental comparisons.

Post-Rebuttal:

The main issue lies in the fact that the authors' response fails to address my concerns regarding the use of Contrastive Loss in the paper. The goal of the paper is to construct untargeted adversarial attacks, yet the authors manually select negative samples to construct the Contrastive Loss, which is problematic. If we follow the authors' stated motivation that "destruction is easier than construction," the approach should involve maximizing the Contrastive Loss during normal training, rather than manually selecting negative samples to minimize it. For these reasons, I am inclined to maintain my current rating.

### Questions
Please refer to the **Weaknesses** section. If the authors can address these issues, I would be willing to raise my score.

1. **Use of Contrastive Loss** 
Perhaps the authors could offer a more detailed explanation of their rationale for using contrastive loss in this context and discuss potential alternative loss functions they considered, as well as why contrastive loss was ultimately chosen despite its typical use in alignment tasks.

2.  **Choice of Positive and Negative Samples for Contrastive Loss**  
Introducing a synthetic, "fictitious" sample that maximally deviates from the original, is a more direct way. Perhaps the authors could discuss the trade-offs between their current approach and your suggested method.

3. **Limited Comparison with State-of-the-Art**  
The authors could select 2-3 recent and relevant adversarial attack methods from related work for comparison.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a universal adversarial attack method called C-PGC for VLP models. By leveraging contrastive learning mechanisms within VLP models, C-PGC generates UAP that can effectively attack across different tasks and models without requiring individual perturbations for each input. Experiments demonstrate that C-PGC disrupts image-text feature alignment efficiently in both white-box and black-box settings, outperforming existing attack methods.

### Strengths
1.	The writing is clear. The formulas are correct.
2.	The experiment is abundant and multi-dimensional.
3.	The research topic is important for VLM.

### Weaknesses
1. The generator-based UAP method is time-consuming due to its indirect optimization approach, as it does not directly update the UAP. Specifically, the reliance on a generator network introduces an additional layer of complexity and computational overhead. The generator's training process, involving iterative adjustments of its parameters to produce effective perturbations, is inherently more time-consuming compared to methods that directly optimize the perturbation itself. This indirect approach also makes it harder to analyze the convergence behavior of the UAP generation process.
2. In multimodal contrastive loss, randomly selecting texts or images may not be ideal. Instead, selecting items related to the current image-text pair in the batch could improve the performance. The current random selection strategy may lead to less effective contrastive learning because the sampled negative pairs might not be sufficiently challenging or relevant to the current image-text pair. This could result in a less discriminative feature space and thus a less effective attack.
3. The method uses the default settings of SGA in the experiment (i.e., resizing the original images into five scales {0.5, 0.75, 1, 1.25, 1.5} and applying Gaussian noise with a mean of 0 and a standard deviation of 0.5). It would be beneficial to give an explanation of the effect of such augmentation, with the experiment result being better. The lack of a detailed analysis on the impact of these specific augmentation parameters makes it difficult to assess their contribution to the overall attack performance. It is unclear whether these parameters are optimal or if other settings might yield better results. Furthermore, the rationale behind choosing these particular values should be clarified.

### Questions
Please see weakness

### Soundness
4

### Presentation
4

### Contribution
3
