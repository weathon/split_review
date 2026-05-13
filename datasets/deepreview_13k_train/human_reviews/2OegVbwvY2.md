# ZIP: An Efficient Zeroth-order Prompt Tuning for Black-box Vision-Language Models

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Recent research has introduced various approaches for prompt-tuning black-box vision-language models, referred to as black-box prompt-tuning (BBPT). While BBPT has demonstrated considerable potential, it is often found that many existing methods require an excessive number of queries (i.e., function evaluations), which poses a significant challenge in real-world scenarios where the number of allowed queries is limited. To tackle this issue, we propose Zeroth-order Intrinsic-dimensional Prompt-tuning (ZIP), a novel approach that enables efficient and robust prompt optimization in a purely black-box setting. The key idea of ZIP is to reduce the problem dimensionality and the variance of zeroth-order gradient estimates, such that the training is done fast with far less queries. We achieve this by re-parameterizing prompts in low-rank representations and designing intrinsic-dimensional clipping of gradients. We evaluate ZIP on 13+ vision-language tasks in standard benchmarks and show that it achieves an average improvement of approximately 6% in few-shot accuracy and 48% in query efficiency compared to the best-performing alternative BBPT methods, establishing a new state of the art. Our ablation analysis further shows that the proposed clipping mechanism is robust and nearly optimal, without the need to manually select the clipping threshold, matching the result of expensive hyperparameter search.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces ZIP for efficient zeroth-order prompt-tuning of black-box vision-language models. ZIP addresses the challenge of excessive query requirements in existing black-box prompt-tuning methods by reducing problem dimensionality and gradient estimate variance through feature sharing and intrinsic-dimensional gradient clipping. ZIP demonstrates significant improvements in few-shot accuracy and query efficiency over other existing methods. Various experiments on image classification show the effectiveness of ZIP.

### Strengths
- ZIP is well-motivated.
- The paper is well-organized.
- Empirical analyses of the proposed method are sufficient.

### Weaknesses
I'm not familiar with this research field, i.e. black box prompt tuning. Therefore, it's hard for me to accurately judge the novelty of the proposed method compared with existing works.

From my perspective, one major weakness is that I find the competitors in the experiments are slightly old, e.g. BLACKVIP is published at CVPR'23 and BPTVLM is published at IJCAI'23. There are some more recent works like [a][b] in this field. I think the authors should better discuss the differences between ZIP and more recent works like [a][b], and provide fair experimental comparisons as well.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method to optimize black-box models without the need for computing gradients (zeroth-order). The key observation is that increasing the number of learnable parameters in soft prompts hurts the performance and training speed of zeroth-order optimization, while this trend is reversed for SGD-based prompt tuning (first-order). To overcome this, authors propose to reparameterize soft prompts in order to reduce the effective number of learnable parameters while maintaining the extrinsic embedding dimensionality. The proposed reparameterization involves projecting parameters into a diagonal matrix, feature sharing and gradient clipping. In addition, reducing the number of learnable parameters results in increased query efficiency (reduced number of forward passes through the model). The proposed method is applied to black-box prompt-tuning of a CLIP model, and evaluated on a suite of standard vision-language benchmarks, achieving improvements of 6% in few-shot accuracy and 48% in query efficiency compared to the best performing existing methods.

### Strengths
* Good motivation to reduce the number of learnable parameters in ZO optimization (section 3) and clever idea to reduce the intrinsic dimensionality while maintaining the number of tokens (and the extrinsic dimensionality, which is a requirement from the model being optimized).
* Several techniques (diagonal matrix, parameter sharing) are applied to preserve performance while reducing the number of learnable parameters.
* The proposed method not only improves few-shot performance wrt existing ZO methods but also reduces considerably the number of function evaluations required to reach a certain level of performance (section 5.3).
* All the design choices for the soft prompt reparameterization are thoroughly ablated in section 6.
* The paper is clearly written and easy to follow.

### Weaknesses
 * Authors motivate fine-tuning black-box models with the use case of improving proprietary LLMs (e.g. GPT-4, Gemini) which are only accessible through API. However, this interface only accepts text and images as input, not soft prompts or embeddings, so the proposed method would not be directly applicable to API-based models.
* To verify the method's robustness and generality, it should be evaluated on other model families such as multimodal LLMs. The current evaluation is limited to CLIP and SigLIP, which are both vision-language models, but do not represent the full spectrum of models where this method could be applied.
* Figures 2, 4, 6 and 7a should report validation accuracy since there could be overfitting. The absence of validation curves makes it difficult to assess the generalization capability of the proposed method and whether the reported improvements are not simply due to overfitting the training data.
* The performance of the proposed method (ZIP) compared to the m=0 baseline (no engineered prompt) is not always consistent. For several datasets (e.g., Flowers102, Food101, FGVCAircraft, UCF101), optimizing soft prompts with ZIP actually hurts performance compared to using no engineered prompt. This raises questions about the robustness of the method and its applicability across different datasets.
* In table 3, the average accuracies for CDT between ZIP and the second-best method seem very close. The standard deviations reported in the table suggest that the performance differences between ZIP and BlackVIP on several datasets (e.g., IN, Flowers102, Food101, ImageNetV2, ImageNet-Sketch) are not statistically significant, which weakens the claim that ZIP consistently outperforms existing methods in cross-dataset transfer.

### Questions
* It is not until the background section that I understood what zeroth-order intrinsic-dimensional prompt-tuning means. I suggest to improve the introduction to make it clearer from early on.
* In figure 2, it would be good to add a baseline of accuracy when no soft prompts are optimized (i.e. m=0).
* Where are the learned soft prompts injected? Are they concatenated to text embeddings and fed to CLIP's text encoder?
* In table 3, the average accuracies for CDT between ZIP and the second-best method seem very close. Did authors run a significance test?

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
The paper introduces ZIP, a zeroth-order prompt tuning method designed for efficient prompt optimization in black-box vision-language models, particularly under limited query budgets. ZIP achieves high efficiency by using low-rank representations and intrinsic-dimensional gradient clipping, which reduces query usage while maintaining robust performance. Evaluations on multiple benchmarks show that ZIP not only outperforms state-of-the-art methods in accuracy but also greatly enhances query efficiency.

### Strengths
(1) The paper is well-organized and accessible, with clear visuals and structured explanations that effectively communicate the method's strengths.

(2) ZIP innovatively enhances zeroth-order prompt tuning through intrinsic-dimensional gradient clipping and low-rank parameterization, making it highly efficient.

(3) Comprehensive evaluations demonstrate ZIP's superior accuracy and query efficiency across 13+ tasks, proving its practical value under query constraints.

### Weaknesses
(1) While ZIP outperforms existing BBPT methods, comparisons with additional baseline methods in zeroth-order optimization, such as SPSA-GC, could strengthen claims of superiority. Specifically, a comparison with other clipped zeroth-order optimization algorithms would provide a more comprehensive understanding of ZIP's performance advantages.

(2) While ZIP shows strong performance on various tasks, its results on ImageNet in Table 1 are comparatively modest, suggesting limitations in scalability to complex datasets. An in-depth analysis of ZIP's performance on larger, diverse datasets, beyond standard benchmarks, would clarify its robustness and potential for broader application. For instance, evaluating on datasets with higher resolution images or more fine-grained categories could reveal potential limitations.

### Questions
(1) In Section 4.2, the paper introduces feature sharing to enhance expressiveness. Could the authors clarify whether this feature sharing technique affects the generalization ability on unseen datasets, and if so, how?

(2) ZIP has demonstrated strong results across vision-language tasks, but could the authors provide more insights into its potential for domain generalization? Specifically, how well does ZIP adapt to unseen domains or datasets outside the evaluated benchmarks, and would any adjustments be necessary to improve its robustness in such scenarios? Such as CoOp and CoCoOp.  

(3)  Could the authors elaborate on the sensitivity of ZIP to the choice of intrinsic dimensionality and low-rank approximation parameters? How do these choices impact both performance and query efficiency?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces ZIP, a zeroth-order intrinsic-dimensional prompt-tuning method designed to efficiently optimize black-box vision-language models. By leveraging low-rank approximation, feature sharing, and intrinsic-dimensional gradient clipping, ZIP achieves faster training speeds and superior generalization performance while significantly reducing query requirements. Extensive experiments on diverse tasks demonstrate ZIP's robustness and query efficiency, outperforming existing BBPT methods and establishing it as a practical approach for resource-constrained scenarios.

### Strengths
1.The paper presents a novel black-box prompt-tuning method, effectively addressing the issue in zeroth-order methods where an increase in trainable parameters adversely impacts accuracy. By reducing the number of parameters and query requirements, the proposed approach is well-suited for practical applications with limited query budgets.

2.The paper demonstrates strong performance across three extensive and diverse experimental settings, which effectively validate the method’s efficacy. The ablation studies further support the approach, particularly highlighting that the feature-sharing technique helps preserve the model’s expressive capacity.           

3.The intrinsic-dimensional clipping mechanism in ZIP requires no manual hyperparameter tuning, making it highly practical and user-friendly.    

4.The paper is well-written, with clear explanations and logical organization that make the proposed method and its contributions easy to understand.

### Weaknesses
1.Although the paper performs ablation studies on individual modules such as  low-rank approximation with a diagonal matrix and feature sharing, it lacks ablation experiments on different combinations of these modules.   Without evaluating different combinations, it is challenging to fully understand the synergistic effects and the relative contributions of each module to the overall performance.      


2.The paper lacks an ablation study to isolate the effect of low-rank approximation alone, making it unclear if improvements are mainly due to the diagonal matrix. This analysis would clarify the diagonal matrix's contribution.

### Questions
Suggestions: 

The caption for Figure 1 should include citations for the baseline methods (BAR, BlackVIP, BPT-VLM) to provide appropriate references and context for these comparisons. This would enhance clarity for readers unfamiliar with these specific methods.

### Soundness
3

### Presentation
3

### Contribution
3
