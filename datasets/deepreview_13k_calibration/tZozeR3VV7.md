# Backdooring Vision-Language Models with Out-Of-Distribution Data

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 5, 8

## Abstract
The emergence of Vision-Language Models (VLMs) represents a significant advancement in integrating computer vision with Large Language Models (LLMs) to generate detailed text descriptions from visual inputs. Despite their growing importance, the security of VLMs, particularly against backdoor attacks, is under explored. Moreover, prior works often assume attackers have access to the original training data, which is often unrealistic. In this paper, we address a more practical and challenging scenario where attackers must rely solely on Out-Of-Distribution (OOD) data. We introduce VLOOD (Backdooring Vision-Language Models with Out-of-Distribution Data), a novel approach with two key contributions: (1) demonstrating backdoor attacks on VLMs in complex image-to-text tasks while minimizing degradation of the original semantics under poisoned inputs, and (2) proposing innovative techniques for backdoor injection without requiring any access to the original training data. Our evaluation on image captioning and visual question answering (VQA) tasks confirms the effectiveness of VLOOD, revealing a critical security vulnerability in VLMs and laying the foundation for future research on securing multimodal models against sophisticated threats.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies backdoor attacks on vision-language models (VLLMs) under an out-of-distribution setting, where the attacker has access only to a new, out-of-distribution dataset and lacks knowledge of the original training dataset. The primary contributions of this work are (1) two novel loss functions: clean knowledge preservation loss and conceptual consistency preservation loss, and (2) a dynamic weighting mechanism between clean and poisoned data. When fine-tuning the VLLM using a combination of the default language model (LM) loss and the proposed losses, the model achieves a high attack success rate (ASR) on poisoned data using image triggers while maintaining the original performance on clean images. Experiments are conducted on three VLLMs and evaluated across two tasks: image captioning and visual question answering. Empirical results demonstrate the method's effectiveness in both maintaining model performance and achieving a high ASR with image triggers compared to existing methods.

### Strengths
1. The experimental setting in this paper is practical and accessible. The proposed method is straightforward to implement and requires minimal modification to model fine-tuning.

2.  Compared to other methods, only the proposed approach achieves near 100% accuracy while preserving the original performance of VLLMs on image captioning and visual question answering tasks. 

3. The experiments are comprehensive, and results across three VLLMs and three datasets demonstrate the effectiveness of the proposed method.

### Weaknesses
Although the two proposed loss functions are straightforward, I am not very clear about their necessity in their current form. Specifically:

- For the CKP loss, it has the same role as $\mathcal{L}_{LM(clean)}$ in general, which is to minimize the distance between the backdoor model's output distribution and the gold distribution on clean images.  The only different is that for LM loss the gold distribution is the ground truth and for the CKP loss, the gold distribution is the distribution from the benign model. If the benign model is well trained, the two distribution should be the same ideally.

- For the CCP loss, it has the same role as $\mathcal{L}_{LM(poisoned)}$, which is to minimize the distance between the backdoor model's output distribution and the gold distribution on images with the image trigger.  Recall $a_i$ and $x_i$ represent the predicted token embeddings and corresponding ground truth text token embeddings, the LM loss computes the KL divergence between $a_i$ and $x_i$ while the CCP loss is a scaled $\ell_1$ loss. In line 282-283, the paper discusses the benefits of using $\ell_1$ loss. However, I cannot understand it very well.

In addition to demonstrating the necessity of the current forms of these two loss functions, it would be great if authors can experiment with 
- replace CKP loss with $\mathcal{L}_{LM(clean)}$ **and/or**
- replace CCP loss with $\mathcal{L}_{LM(poisoned)}$

### Questions
1. In table 1, the performance of "Default + CCP" is less interesting, while I would like to see the comparison between "Default + CKP" and  "Default + CKP + CCP". What is the difference between "Default + Dynamic" and "VLOOD (Ours)"?

2. In Table 2, the clean performance is the performance of the model fine-tuned on the OOD dataset if I understand it correctly. Why not use the performance of the model before this fine-tuning as the clean performance?

3. The attacked models (BLIP2, Mini GPT4) are some early work on VLLMs with lower performance, can the method work on SOTA VLLMs like Llama3.2 Vision and Qwen2-VL?

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
This paper explores backdoor attacks on Vision-Language Models (VLMs) for image-to-text generation using Out-of-Distribution (OOD) data, addressing a realistic scenario where attackers lack access to the original training dataset. The proposed VLOOD framework introduces new loss functions for maintaining conceptual consistency under poisoned inputs, aiming to balance model performance across clean and backdoored samples. Experimental results suggest VLOOD’s effectiveness.

### Strengths
**Pros:**

1. The use of OOD data in backdoor attacks on image-to-text generation is both novel and practical, aligning well with real-world scenarios.
2. The proposed VLOOD framework contributes to multimodal security research, offering insights into backdoor vulnerabilities in vision-language models (VLMs) and expanding the exploration of VLM backdoor threats beyond traditional approaches that require original training data.

### Weaknesses
 **Main Concerns:**

**1. Insufficient Justification of Loss Function Choices:**
The paper introduces two main loss functions, CKP and CCP, to balance model performance on clean and poisoned inputs. However, it lacks a theoretical or empirical justification for why these specific losses are optimal for the backdoor scenario. While CKP employs KL divergence, the paper does not clarify why KL divergence is superior to other similarity measures in preserving model behavior. Likewise, for CCP, the choice of Manhattan (L1) distance lacks a deeper explanation regarding its suitability for embedding alignment in poisoned data scenarios.

Although the authors mention in line 283 that L1 distance is generally reliable across most dimensions, it may lead to overly sparse results in high-dimensional spaces, potentially affecting embedding alignment. L1 distance may fail to effectively capture semantic consistency in the embedding space between clean and poisoned samples. Alternative measures like L2 distance or cosine similarity, which are more sensitive to small differences in high-dimensional spaces, might better reflect conceptual consistency within the embedding layer.

**2. Dynamic Weight Adjustment Mechanism:**
The adaptive λ mechanism aims to balance the impact of clean and poisoned samples, yet the mechanism lacks a robust evaluation. The paper describes λ adjustments based on the impact on clean vs. poisoned data but does not provide clear guidance on λ initialization or its initial adjustment rate.

The initial value and adjustment rate of λ can significantly impact the convergence speed and stability in the early training stages. Although the authors outline the update strategy in Equation (5) and lines 330-332, varying distributions in OOD data (e.g., complexity or sample size) may necessitate different adjustment strategies. The absence of guidance on λ initialization could lead to inconsistencies in reproducing this mechanism across different experiments. Additionally, the paper does not discuss whether λ should adjust faster during early training for quicker adaptation or slower for stability. Empirical data on λ convergence (e.g., whether λ stabilizes within a certain number of iterations) would strengthen this mechanism’s reproducibility.

**3. Trigger Size and Position Sensitivity:**
The ablation study on trigger size highlights a limitation: although ASR remains high across various trigger sizes, the impact on Conceptual Consistency (CACC and PACC) fluctuates. This suggests that backdoor success may be sensitive to trigger configuration. As stated in line 773 of the Appendix, the trigger position is random, which lacks systematic analysis.

If the backdoor’s effectiveness varies significantly by specific regions (e.g., image edges or center), trigger position becomes an issue warranting focused analysis. A systematic study of trigger placement (e.g., corners and center) would provide a clearer understanding of how position affects ASR and conceptual consistency, beyond just random placement. Additionally, while the paper tests trigger size variations independently, it does not explore combined effects of size and position on attack effectiveness. Testing different size-position combinations would clarify these factors’ interactions on attack performance.

**4. Lack of Ablation Study for λ Mechanism:**
Without defined initialization parameters for λ across different OOD data, the impact of λ’s initialization on model performance remains unclear. Ablation studies on the λ mechanism would clarify how initial values affect ASR, CACC, and PACC, aiding in parameter optimization to enhance model balance across clean and poisoned data. Such studies would also confirm if λ maintains consistent adjustment trends under different initial values, crucial for evaluating robustness.

**Minor Issues:**

**1. Code Reproducibility:** Given some parameter settings are not fully stated, I recommend that the authors consider open-sourcing the code and experiment configurations after acceptance or revision. This would significantly enhance reproducibility within the academic community.

**2. Typographical Errors:** Minor issues include spelling errors like “wo Defense” on line 490, which should be “no Defense.”

### Questions
As mentioned in the **Weaknesses**.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces VLOOD, a novel backdoor attack targeting Vision-Language Models (VLMs) using Out-of-Distribution (OOD) data. Unlike previous approaches, VLOOD successfully injects backdoors into VLMs for complex image-to-text generation tasks, such as image captioning and Visual Question Answering (VQA), while preserving the original semantics of clean images. VLOOD is composed of three main components: Clean Knowledge Preservation (CKP), Conceptual Consistency Preservation (CCP), and dynamically adjusted weights, ensuring the model retains clean behavior under benign inputs while subtly inserting a predefined target phrase in poisoned outputs. Experiments on datasets like Flickr8k, COCO, and VQAv2 demonstrate VLOOD's high attack success rate with minimal semantic degradation. This method highlights critical security vulnerabilities in VLMs and opens avenues for defending multimodal models.

### Strengths
1. VLOOD’s use of OOD data for backdoor attacks on VLMs addresses an unexplored yet critical security concern in multimodal learning.

2. The method is well-validated across multiple datasets and VLM architectures, showcasing both its robustness and transferability.

3. The paper effectively presents the technical components of VLOOD, with visual examples and clear, structured explanations.

4. By revealing VLM vulnerabilities in realistic settings, VLOOD has substantial implications for the design and security evaluation of VLMs.

### Weaknesses
1. Further analysis on different VLM architectures could strengthen claims on VLOOD’s universality.

### Questions
How does VLOOD’s effectiveness vary with increased amounts of OOD data below 3000 samples?

Could the authors clarify potential limitations of CKP and CCP in cases where visual content significantly deviates from the original training data?

### Soundness
3

### Presentation
3

### Contribution
3
