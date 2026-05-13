# Mixture of Experts Guided by Gaussian Splatters Matters: A new Approach to Weakly-Supervised Video Anomaly Detection

- Decision: Reject
- Scores: 6, 8, 5, 5, 5, 6, 3

## Abstract
Video Anomaly Detection (VAD) has proved to be a challenging task due to the in-
herent variability of anomalous events and the scarcity of data available. Under the
common Weakly-Supervised VAD (WSVAD) paradigm, only a video-level label
is available during training, while the predictions are carried out at the frame-level.
Despite decent progress on simple anomalous events (such as explosions), more
complex real-world anomalies (such as shoplifting) remain challenging. There
are two main reasons for this: (I) current state-of-the-art models do not address
the diversity between anomalies during training and process diverse categories
of anomalies with a shared model, thereby ignoring the category-specific key at-
tributes; and (II) the lack of precise temporal information (i.e., weak-supervision)
limits the ability to learn how to capture complex abnormal attributes that can
blend with normal events, effectively allowing to use only the most abnormal snip-
pets of an anomaly. We hypothesize that these issues can be addressed by sharing
the task between multiple expert models that would increase the possibility of cor-
rectly encoding the singular characteristics of different anomalies. Furthermore,
multiple Gaussian kernels can guide the experts towards a more comprehensive
and complete representation of anomalous events, ensuring that each expert pre-
cisely distinguishes between normal and abnormal events at the frame-level. To
this end, we introduce Gaussian Splatting-guided Mixture of Experts (GS-MoE),
a novel approach that leverages a set of experts trained with a temporal Gaussian
splatting loss on specific classes of anomalous events and integrates their predic-
tions via a mixture of expert models to capture complex relationships between
different anomalous patterns. The introduction of temporal Gaussian splatting
loss allows the model to leverage temporal consistency in weakly-labeled data,
enabling more robust identification of subtle anomalies over time. The novel loss
function, designed to enhance weak supervision, further improves model perfor-
mance by guiding expert networks to focus on segments of data with a higher like-
lihood of containing anomalies. Experimental results on the UCF-Crime and XD-
Violence datasets demonstrate that our framework achieves SOTA performance,
scoring 91.58% AUC on UCF-Crime.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the Gaussian Splatting-guided Mixture of Experts (GS-MoE) for weakly-supervised video anomaly detection. This method enhances the capability of class-expert models to understand the anomalous events in videos by utilizing the temporal Gaussian splatter loss, and captures the complex relationships between different anomalous patterns through a mixture-of-expert architecture. The experimental results show that this method has achieved significant performance improvements on the UCF-Crime and XD-Violence datasets. This paper proposes a promising new method for weakly-supervised video anomaly detection, and its effectiveness is proved by their experiments.

### Strengths
Innovation: This paper proposes a new framework for weakly-supervised video anomaly detection framework that combines Gaussian splatter loss and mixture-of-expert architecture. The idea has some novelty in the field of video anomaly detection.
Performance: Experimental results show that the proposed GS-MoE achieves better performances than existing SOTA methods on both UCF Crime and XD Violence datasets with significant improvements, especially in handling complex abnormal events.
Presentation: This paper gives a detailed description for each component of GS-MoE, including the calculation of Gaussian splatter loss and the design of the mixture-of-expert architecture. This makes the proposed idea not difficult to be comprehended.
Experiments: This paper conducts extensive experiments on two widely-used datasets and compares their proposed method with other SOTA methods. Additionally, ablation studies and category performance analysis are also given to validate the effectiveness of each component.

### Weaknesses
My concern about this paper mainly focuses on the computational complexity due to the use of a mixture-of-expert architecture, where the authors assign an expert for each anomaly. It seems that the proposed approach may consume a significant amount of resources. I suggest the authors discuss on the inference speed of the proposed model (such as FPS) as well in Table 1, so that the advantages and disadvantages of the model can be better illustrated.

Furthermore, the method for peak selection in the Gaussian splatter loss, while described, lacks significant novelty. The reliance on a simple prominence threshold for peak detection seems rudimentary, especially considering the potential for complex and rapidly fluctuating anomaly scores. This raises concerns about the robustness of the method in real-world scenarios where anomaly patterns might not exhibit clear, isolated peaks. The absence of a more sophisticated peak detection strategy, such as adaptive thresholding or techniques that consider the temporal context of the anomaly scores, is a notable limitation.


### Questions
1. Considering that the Gaussian splatter extracts the Gaussian kernels from the peak values of the abnormal scores and renders it onto the curve, how are the peaks detected or selected? Please give more detailed explanation about the method of peak selection, especially when the curve fluctuates frequently?
2. Considering that misclassifications may often occur in MIL, please provide some analysis of such examples, such as incorrectly detected peaks on normal snippets.
3. Please provide experimental results on the UbNormal dataset to fully demonstrate the effectiveness of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces GS-MoE, a novel framework for weakly-supervised video anomaly detection that combines a Mixture of Experts (MoE) architecture with Temporal Gaussian Splatting (TGS). TGS uses Gaussian kernels to capture broader temporal dependencies, enhancing the model’s ability to detect subtle and complex anomalies. The MoE architecture includes specialized expert models for different anomaly types, coordinated by a gating mechanism for fine-grained detection. Experimental results on UCF-Crime and XD-Violence datasets demonstrate state-of-the-art performance.

### Strengths
1. The paper is well-written and clearly structured, making the ideas easy to follow.

2. The proposed GS-MoE framework is well-motivated, effectively addressing key limitations in weakly-supervised video anomaly detection. It introduces Temporal Gaussian Splatting (TGS) to reduce over-dependency on the most abnormal snippets, allowing the model to capture subtle temporal patterns across a broader range of anomaly cues. The Mixture of Experts (MoE) architecture further enhances performance by learning category-specific, fine-grained representations and connecting these with coarse anomaly cues, resulting in a more compact and accurate anomaly representation.

3. The approach achieves state-of-the-art results on UCF-Crime and XD-Violence, setting new benchmarks and demonstrating its effectiveness across various metrics.

### Weaknesses
1. In Table 3, there seems to be a labeling error. The column labeled "With skip connect" should likely be labeled "With task-aware features"

### Questions
See the weaknesses.

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
4

### Summary
This paper proposes a Gaussian Splatting-guided Mixture of Experts (GS-MoE), leveraging a set of experts trained with a temporal Gaussian splatting loss on specific classes of anomalous events and integrating their predictions via a mixture of expert models to capture complex 
relationships between different anomalous patterns. Temporal gaussian splatting reduces the dependencies on the most abnormal snippets.

### Strengths
Pros: 
1. Usage of Gaussian kernels extracted from the estimated abnormal scores to generate complete representation 
2. Splatting the kernels along the temporal dimension for modeling anomalous temporal dependencies 
3. Dedicated class-expert models focus on individual anomaly types 
4. Improvements on benchmarks.

### Weaknesses
Cons: 
1. Some inappropriate expressisons and lack in sufficient literature review 
2. Each expert is trained only on refined features belonging to its assigned class and to the 
normal class. Why different classes are pre-defined like this, what if different classes are 
coupled? Anomalies are unexpected, it is difficult to define classes. The mixture of experts 
assumes that different anomaly types can be isolated effectively. However, in real-world 
applications, anomalies might not always fit neatly into predefined classes or could be ambiguous. 
This assumption may restrict generalization to unseen or blended anomaly types, particularly in 
more dynamic or less structured environments. The core issue is that the model's reliance on pre-defined anomaly classes during training limits its ability to detect novel or composite anomalies at test time. If an anomaly exhibits characteristics not present in the training classes, the model's performance will likely degrade significantly, as it lacks the specialized expert to handle such cases. This is a fundamental limitation of the approach.
3. The model relies heavily on the quality of extracted features from pre-trained I3D models. 
If the feature extraction model underperforms or isn’t well-suited to certain video types, the 
overall anomaly detection may suffer. The reliance on a fixed feature extractor may limit 
adaptability across datasets with different visual characteristics. The performance is therefore tightly coupled with the I3D model's ability to capture relevant features for the specific anomaly detection task. If the pre-trained I3D model was trained on a dataset that does not sufficiently represent the types of anomalies present in the target dataset, the extracted features may not be discriminative enough, leading to suboptimal performance. This dependence on a fixed feature extractor limits the model's robustness and generalizability across diverse datasets.
4. The combination of Gaussian splatting with a mixture of experts might make it difficult to 
interpret the model’s decision-making process. Although the framework shows strong quantitative 
results, it may be challenging to explain how or why certain frames are classified as anomalous, 
which could be important for fields requiring clear explanations of detection results.

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
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel framework named Gaussian Splatting-guided Mixture of Experts (GS-MoE) for weakly-supervised video anomaly detection (WSVAD). The approach addresses the challenges of detecting complex, real-world anomalies in videos by leveraging a set of expert models trained with a temporal Gaussian splatting loss on specific classes of anomalous events. These experts' predictions are integrated via a mixture of expert models to capture complex relationships between different anomalous patterns. The framework is designed to leverage temporal consistency in weakly-labeled data, enabling more robust identification of subtle anomalies over time. Additionally, this paper achieves state-of-the-art performance on the UCF-Crime and XDViolence datasets.


I have read the response of the authors and the comments of other reviewers. I would keep my original score.

### Strengths
1. The paper proposes a novel approach to WSVAD by combining Gaussian Splatting with a Mixture of Experts (MoE) architecture, which is a creative solution to address the limitations of current models in handling complex anomalies.
2. The framework demonstrates significant improvements over previous state-of-the-art methods on benchmark datasets, which is a strong indicator of the effectiveness of the proposed method.
3. The paper provides an extensive set of experiments and ablation studies that validate the effectiveness of the proposed contributions and provide insights into the impact of each component of the framework.

### Weaknesses
1. The paper would benefit from a more detailed analysis of the specific contributions of each architectural choice, such as the Mixture-of-Experts (MoE) design and the Temporal Gaussian Splatting (TGS) mechanism, to the overall performance. While the results are impressive, a deeper exploration of how these components enhance the model's capabilities would strengthen the paper's technical depth and provide readers with a better understanding of the innovations' impact. For instance, the paper lacks a detailed explanation of how the MoE architecture is specifically designed to handle the diverse nature of anomalies, and how the TGS mechanism improves the temporal modeling compared to other temporal aggregation techniques. A more granular analysis, perhaps by isolating the contributions of each component through ablation studies with more specific metrics, would be beneficial.
2. The paper does not sufficiently address how the GS-MoE architecture scales with increasing model size or its adaptability to different image resolutions and datasets. Providing insights into the model's scalability and flexibility would be crucial for establishing its practical applicability and robustness across various settings and data. The current discussion does not explore the computational overhead associated with adding more experts to the MoE, nor does it analyze the impact of varying input resolutions on the model's performance. Furthermore, the paper should discuss the limitations of the method when applied to datasets with significantly different characteristics than those used in the evaluation.
3. The paper could benefit from a more detailed comparison with other MoE architectures to highlight the unique aspects of the proposed approach. Such a comparison would help position the GS-MoE framework within the broader landscape of anomaly detection methods and underscore its innovative features. The paper should discuss how the proposed MoE differs from existing approaches in terms of expert selection, training strategy, and integration of expert outputs. A comparative analysis with other MoE architectures, including a discussion of their strengths and weaknesses, would provide a more comprehensive understanding of the proposed method's novelty and advantages.
4. Although the paper presents numerous visualization generation results, it lacks a discussion on failure cases. Including examples where the model underperforms or fails to detect anomalies would offer a more balanced view of the framework's limitations and areas for future improvement. The paper should include a qualitative analysis of the types of anomalies that the model struggles to detect, and discuss the potential reasons for these failures. This would provide a more complete understanding of the model's capabilities and limitations.

### Questions
1. How does the method perform on other datasets with different types of anomalies, and have they considered any strategies to improve generalization?
2. What are the computational costs associated with training and deploying the GS-MoE framework, and how do they compare to other state-of-the-art methods?
3. How does the temporal Gaussian splatting loss impact the learning process, and can the authors provide more insights into how it improves the model's ability to detect anomalies?
4. Are there any immediate plans to incorporate interpretability or explainability features into the current model to understand the decisions made by the different experts?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a GS-MoE framework for WSVAD to address the challenges of anomaly diversity and weak supervision by using multiple expert models and a temporal Gaussian splatting loss.

### Strengths
The paper introduces a novel framework, GS-MoE, that effectively combines expert models to address the diverse nature of anomalies in WSVAD.
The approach is well-supported by comprehensive experiments, showing strong results and achieving state-of-the-art performance.

### Weaknesses
The description of the Gaussian splatting loss lacks detail, making it difficult to understand the exact mechanism by which it improves temporal consistency. Specifically, the paper does not clarify how the Gaussian kernels are parameterized, nor how the splatting operation is implemented in the temporal domain. It is unclear how the kernel size and variance are determined, and how these parameters affect the model's ability to capture different temporal scales of anomalies. Furthermore, the paper does not discuss the computational complexity of the splatting operation, which could be a significant factor in the overall efficiency of the method.

There is limited explanation regarding the selection and training of individual expert models for different anomaly types, which may affect reproducibility. The paper does not specify the criteria used to define the 'anomaly types' for each expert. It is unclear if these types are based on pre-existing categories or if they are learned from the data. The training procedure for each expert is also not fully detailed, specifically how the loss function is applied to each expert, and how the gradients are handled during backpropagation. This lack of detail makes it difficult to understand how the experts specialize in detecting different anomalies.

There is insufficient analysis on the computational cost and efficiency of the proposed mixture of experts approach, especially for real-time applications. The paper does not provide a breakdown of the computational cost for each component of the GS-MoE framework, such as the expert models, the gate model, and the Gaussian splatting operation. This makes it difficult to assess the feasibility of deploying the method in resource-constrained environments. Furthermore, the paper does not discuss the memory footprint of the model, which is an important factor for real-time applications.

### Questions
What criteria are used to assign or develop expert models for specific types of anomalies?
Are there potential limitations in using this method for scenarios where anomalies are highly similar to normal events?
Could the authors elaborate on the framework's scalability and feasibility for deployment in resource-constrained environments?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents the Gaussian Splatting-guided Mixture of Experts (GS-MoE) framework, which addresses the limitations of existing models in Video Anomaly Detection (VAD) by employing multiple expert models. Each expert is trained on specific classes of anomalies, allowing the framework to effectively encode the unique characteristics of different anomalous events. The GS-MoE framework utilizes a temporal Gaussian splatting loss, which leverages temporal consistency in weakly labeled data to enhance the identification of subtle anomalies over time. By guiding the expert networks to concentrate on segments with a higher likelihood of containing anomalies, the proposed method improves performance in the weakly supervised setting.

### Strengths
1. The formulation of the WSVAD task using Gaussian kernels allows for a more expressive and complete representation of anomalous events. 
2. The Mixture-of-Expert (MoE) architecture focuses on individual anomaly types through dedicated class-expert models. This specialization, combined with the gate model's ability to leverage similarities and diversities among different types, enhances the model's overall effectiveness and robustness in anomaly detection.

### Weaknesses
1. The motivation of the proposed method is unclear. The paper does not adequately explain why a Gaussian Splatting approach is necessary or beneficial for the weakly supervised video anomaly detection (WSVAD) task. The connection between the limitations of existing methods and the proposed Gaussian kernel is not well established, leaving the reader to question the fundamental need for this specific formulation.
2. The innovation of the method is limited as the backbone is largely based on existing method and multi-expert, and gated model seems common. The core architecture relies heavily on the UR-DMU framework, and the use of a multi-expert model with a gating mechanism is not novel in itself. The paper fails to demonstrate a significant departure from existing approaches in terms of architectural design, making the contribution seem incremental rather than groundbreaking.
3. The illustrations of Figure is poor, which don't covey the central idea of the proposed method. The figures, particularly Figure 1, lack clarity and fail to effectively communicate the core concepts of the proposed method. The visual representations are not intuitive, making it difficult for the reader to grasp the key ideas and the overall workflow of the GS-MoE framework.

### Questions
Introduction:
1. The current issues of VAD in paragraph 2 of the introduction is not well illustrated and the readers may find confusing as the definition fo the issues is not clear.
2. The motivation of introducing Gaussian splatting is not well depicted in the introduction.
3. The information of Figure 1 is extremely, which doesn't convey the central idea of this paper sufficiently. It is suggested that the authors should combine Figure1, Figure2 and Figure3 and give the readers an overview of the motivation of main idea.

Methods:
1. The innovation of the proposed method is limited as the main backbone is largely based on UR-DMU.
2. Figure 4 should add illustrations of the meaning of the icons involved.
3. Algorithm 1 seems unnecessary to presented in separate section, as plain words can presented well.

Experiments:
1. Comparisons with state-of-the-art VAD methods in 2024 should be included in Table 1.
2. The performance of XD-Violence is relative low. The authors may justify why such phenomenon happens.
3. The introducing of multi-experts inevitably increasing the computational overhead, and may further lead to issue of overfitting. The authors should conduct analysis from these aspects. 

Typos:
The authors should correct their citation format using command \citet{} or \citep{}, according to the formatting instructions.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 7

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors address weakly-supervised video anomaly detection (WSVAD) by presenting a new framework termed "GS-MoE." One key aspect of their approach is mining peaks from abnormal scores and proposing "Temporal Gaussian Splatting" to generate dense pseudo-labels from these peaks for supervision. Another key point is the proposed structure of MOE, which captures the diversity of anomalies through multiple parallel Expert blocks and uses a Gate block to fuse the results of different experts. Both qualitative and quantitative results demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper is well-written and easy to understand.
2. The application of Gaussian Splatting and MOE concepts to WSVAD is very interesting.
3. Experiments were conducted on two datasets, and the performance of the proposed method significantly surpassed that of previous methods, especially on the UCF-Crime dataset.

### Weaknesses
1. The core idea of Temporal Gaussian Splatting is to use Gaussian distribution to extend and smooth sparse binary snippet-level pseudo label, which has been proposed in [1].  This greatly reduces the contribution of the author's work.
2. Since the peak detection process can significantly impact the quality of the rendered anomaly score, the final performance can be greatly affected by the initialization process, including the choice of task encoder and the hyperparameters used for peak detection. Conducting more ablation studies on these factors could demonstrate the robustness of the proposed method.
3. The author mentions that the MOE architecture learns class-specific representations. However, it is known that the differentiation between experts in MOE [2] of LLM is achieved through an additional loss function. I am curious about how different experts within the proposed framework learn to focus on different anomalies using only video-level labels.
4. The ablation experiments for some important hyperparameters, such as $\sigma_i$ in Equation (3) and the number of experts $N$, were missing from the paper.
5. There are noun consistency issues in the paper, such as the use of "TGS" in Algorithm 1 and "TSG" in other parts of the paper.

### Questions
See Weakness.

### Soundness
3

### Presentation
3

### Contribution
2
