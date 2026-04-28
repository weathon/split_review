# Gap Preserving Distillation by Building Bidirectional Mappings with A Dynamic Teacher

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Knowledge distillation aims to transfer knowledge from a large teacher model to a compact student counterpart, often coming with a significant performance gap between them. We find that a too-large performance gap can hamper the training process, which is also verified in recent studies.
To address this, we propose a \textbf{Gap Preserving Distillation (GPD)} method that trains an additional dynamic teacher model from scratch along with training the student to bridge this gap. In this way, it becomes possible to maintain a reasonable performance gap between teacher and student during the whole distillation process. 
\yong{To further strengthen distillation from the dynamic teacher to the student, we develop a hard strategy by enforcing them to share parameters and encouraging parameter inheritance. Besides hard strategy, we also build the soft bidirectional mappings between them which are built on an \emph{\textbf{Inverse Reparameterization (IR)}} method and a \emph{\textbf{Channel-Branch Reparameterization (CBR)}} strategy.}
We highlight that our IR is able to initialize a larger dynamic teacher with an arbitrary expansion ratio, while preserving exactly the same accuracy as the given student model. \yong{In this way, it guarantees that the dynamic teacher and student start from the same point and avoid a too large gap in early stage of training.}
As for our CBR, with parameter-sharing, it directly extracts an effective student model from the well-learned dynamic teacher without any post-training, making our method highly flexible for model deployment.
In the experiments, GPD significantly outperforms existing distillation methods on top of both CNNs and transformers architectures, achieving up to 1.58\% accuracy improvement. 
Interestingly, GPD also generalizes well to the scenarios without a pre-trained teacher, including training from scratch and fine-tuning, yielding a large improvement of 1.80\% and 0.89\% on ResNet18, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Gap Preserving Distillation (GPD) to address the challenge where large performance gaps between teacher and student models hinder effective knowledge transfer. GPD introduces a dynamic teacher model that trains alongside the student, maintaining an optimal performance gap to improve transfer efficiency. The performance gains from GPD are primarily due to its use of Inverse Reparameterization (IR) and Channel-Branch Reparameterization (CBR), which create flexible connections that enable parameter sharing between the dynamic teacher and student. Experimental results show that models trained with GPD outperform those using traditional fixed teacher models and perform robustly even in scenarios without a pre-trained teacher, such as training from scratch and fine-tuning.

### Strengths
1. This paper identifies the performance gap between teacher and student models as a key challenge in knowledge distillation. By introducing a dynamic adjustment mechanism, the method effectively narrows this gap, facilitating more efficient knowledge transfer.

2. The proposed GPD demonstrates adaptability across various training settings, with significant improvements across multiple models and datasets. Extensive ablation studies further validate the method’s effectiveness.

### Weaknesses
1. Needs More Theoretical Explanation
This paper could benefit from a deeper explanation of why a large performance gap between the teacher and student models makes knowledge transfer less effective. Right now, the idea that a big gap harms learning is mentioned, but it would be stronger if some theoretical reasoning or tests showed how this happens. Adding experiments that test different gap sizes could also help show how different levels of teacher-student gaps impact the student model’s final performance. Specifically, the paper lacks a clear explanation of the underlying mechanisms that cause performance degradation when the teacher model is significantly more powerful than the student. For instance, does a very strong teacher lead to over-confident predictions that are not easily generalized by the student, or does it cause the student to focus on irrelevant features? A more detailed analysis of the information flow and feature representations would be beneficial.

2. Overengineering in the Dynamic Teacher Model 
The necessity of the complex structure designed in this paper, including Inverse Reparameterization (IR) and parameter sharing, appears somewhat disconnected from the core problem. If the primary goal is to reduce the performance gap, it remains unclear whether the proposed architecture (specifically the IR and shared parameters) is required to achieve this. Making the connection between these design choices and the main goal a bit clearer could help the paper feel more cohesive. It is not immediately obvious why these specific mechanisms are crucial for bridging the performance gap, and the paper would benefit from a more detailed justification of these design choices. For example, are there simpler ways to achieve a similar effect, such as using a teacher model with a capacity that is closer to the student model, or is the dynamic adjustment truly necessary?

### Questions
1. How can we better understand and measure the impact of the performance gap on knowledge transfer? The paper mentions that keeping a reasonable performance gap between teacher and student models helps with effective knowledge transfer. However, it doesn’t fully explain why a larger gap might hurt the process. How exactly does the size of this gap affect the student model’s final performance? As mentioned in the weaknesses section, adding some theory or controlled experiments here could help clarify this point and give a clearer idea of the best range for this gap.

2. As mentioned in the weaknesses, is the complex design of the dynamic teacher model really necessary? To tackle the performance gap, the paper introduces a dynamic teacher model with intricate structures like Inverse Parameterization (IR) and parameter sharing. But has the author considered more straightforward options to close the gap? If this complex setup is essential, could they explain more about how it directly addresses the problem?

### Soundness
3

### Presentation
3

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
The paper proposes Gap Preserving Distillation (GPD), a framework designed to address the capacity gap between teacher and student networks. GPD achieves this by training an additional dynamic teacher alongside the student. To further improve performance and efficiency, GPD enforces parameter sharing between the dynamic teacher and the student using Inverse Reparameterization and Channel-Branch Reparameterization techniques. Experiments on ImageNet-1K classification primarily compare GPD with baselines using static teachers, showing preliminary effectiveness.

### Strengths
1. The problem is well-motivated, particularly in lines 54-61, highlighting the importance of adaptively managing the performance gap.
2. The proposed approach is novel. It co-trains a dynamic teacher to alleviate the teacher-student capacity gap and applies inverse reparameterization and channel-branch reparameterization for efficient parameter sharing.
3. The paper is well-organized and easy to follow, with clear descriptions, intuitive figures, and rigorously detailed algorithms.

### Weaknesses
1. **Lack of comparisons with Knowledge Distillation (KD) methods using teacher assistants**. These methods are closely related to the proposed GPD. Without these comparisons, the effectiveness of GPD is unclear or less convincing. Suggested comparisons include, but are not limited to:
   - Mirzadeh, Seyed Iman, et al. "Improved knowledge distillation via teacher assistant." *AAAI 2020*
   - Son, Wonchul, et al. "Densely guided knowledge distillation using multiple teacher assistants." *CVPR 2021*
   - Ganta, Durga Prasad, Himel Das Gupta, and Victor S. Sheng. "Knowledge distillation via weighted ensemble of teaching assistants." *ICBK 2021*
   - Zhou, Yuhang, and Wei Ai. "Teaching-Assistant-in-the-Loop: Improving Knowledge Distillation from Imperfect Teacher Models in Low-Budget Scenarios." *arXiv:2406.05322* (2024)

2. **Inappropriate and unfair baselines in Section 4.2**. The paper compares GPD without a static teacher against networks trained without any KD techniques. Since GPD involves an additional dynamic teacher, it would be more appropriate to compare it with self-distillation methods.

3. **Practicality and efficiency concerns**. The size of the additional dynamic teacher must still be tuned by adjusting the branch and channel expansion ratios, making GPD less practical and efficient. Furthermore, the method's reliance on reparameterization techniques, while novel, introduces additional computational overhead during training, which is not thoroughly addressed in the paper. The paper does not provide a detailed analysis of the computational cost associated with the dynamic teacher and the reparameterization process, making it difficult to assess the true efficiency of the proposed method. This is particularly concerning given the stated goal of addressing capacity gaps efficiently.

### Questions
1. The paper claims that the dynamic teacher shares exactly the same accuracy as the student with the reparameterization techniques. However, Figure 1 shows that the weights of the dynamic teacher are modified with added noise, which seems to contradict this claim.
2. The claim in lines 68-69, “Since DT is a larger model and often converges faster than the student,” appears counterintuitive. Is there any evidence to support this?
3. The network pairs in Table 6 do not convincingly demonstrate the effect of the teacher-student capacity gap. For instance, Table 6 shows that ViT-L performs worse than ResNet101 when distilling to a ResNet18. This may be due not to the larger capacity gap between ViT-L and ResNet18, but rather to differences in architecture. It would be more consistent to use CNN or ViT architectures for both teacher and student.

### Soundness
3

### Presentation
3

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
This paper aims to improve the effectiveness of knowledge distillation (KD) when using a teacher model with a large performance gap relative to the student model. The authors propose a method called Gap Preserving Distillation (GPD). By adopting a dynamic teacher model created through a re-parameterization operation on the student model as a proxy teacher, the performance gap is narrowed. Experimental results demonstrate the effectiveness of this approach.

### Strengths
- The problem of effectively performing KD with an extremely large teacher model is important and well-motivated.
- The paper is well-organized and easy to follow.

### Weaknesses
1. The abstract is too lengthy, as it seems to emphasize every aspect in detail. I suggest revising the abstract to improve clarity and conciseness.

2. The KD process involves training a dynamic teacher model alongside the student, which requires frequent re-parameterization. I am curious about the training cost compared to baseline methods.

3. In Table 6, it appears that the larger ViT-L teacher model leads to worse student performance than the smaller ResNet-101 teacher model (as with DKD). This suggests that the proposed method may still struggle with extremely large teacher models, despite it aims to overcome this issue.

4. The method's description primarily focuses on convolutional models. Although experimental results are provided for transformer models, it would be helpful to explain how re-parameterization is achieved for these models.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
