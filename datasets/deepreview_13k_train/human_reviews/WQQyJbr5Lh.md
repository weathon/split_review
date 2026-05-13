# Discovering Influential Neuron Path in Vision Transformers

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Vision Transformer models exhibit immense power yet remain opaque to human understanding, posing challenges and risks for practical applications. While prior research has attempted to demystify these models through input attribution and neuron role analysis, there’s been a notable gap in considering layer-level information and the holistic path of information flow across layers. In this paper, we investigate the significance of influential neuron paths within vision Transformers, which is a path of neurons from the model input to output that impacts the model inference most significantly. We first propose a joint influence measure to assess the contribution of a set of neurons to the model outcome. And we further provide a layer-progressive neuron locating approach that efficiently selects the most influential neuron at each layer trying to discover the crucial neuron path from input to output within the target model. Our experiments demonstrate the superiority of our method finding the most influential neuron path along which the information flows, over the existing baseline solutions. Additionally, the neuron paths have illustrated that vision Transformers exhibit some specific inner working mechanism for processing the visual information within the same image category. We further analyze the key effects of these neurons on the image classification task, show- casing that the found neuron paths have already preserved the model capability on downstream tasks, which may also shed some lights on real-world applications like model pruning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study focuses on uncovering the inner workings of vision Transformer models by examining critical neurons that influence model inference. They introduce the Neuron Path approach, which uses a new joint neuron attribution measure to identify key neurons in information flow across layers. The analytical experiments highlight the significance of these neuron paths for model inference and provide insights into the internal operations of vision Transformers, enhancing the field's understanding of visual information processing.

### Strengths
This paper is relatively well-motivated as understanding vision transformer is a crucial issue. I also find the evaluations thorough. The strengths are as follows:

1,The target issues of the paper are meaningful and worth exploring.
2. The motivation is clear.
3.The paper is easy to follow.

### Weaknesses
 1. In section 4.4, neuron path method is used in model compression. It would be better if this method is compared to the the pruning method.
2. This method aims at vision transformer. Can this method be utilized in NLP tasks?

### Questions
See Weaknesses

### Soundness
3

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
This paper addresses identifying the neuron path within Vision Transformers (ViT) that comprises the most impactful neurons. Two methods are utilized to identify a neuron pathway. The proposed joint attribution score assesses the influence of the neuron pathway on the network's inference process. Another method referred to as layer-progressive neuron locating identifies the most significant neuron pathway for predicting the target image. The proposed method demonstrates its effectiveness in identifying neuron pathways. This paper presents a range of applications that leverage the proposed method.

Thank you for the authors' response. I think they answered my question adequately. Thus, I keep my score as a weak accept.

### Strengths
This paper presents innovative concepts for identifying influential neuron pathways. The proposed approach is capable of identifying the trajectory of neurons by analyzing the gradient magnitude. This method has the potential for application across diverse architectural frameworks.

This paper demonstrates the applicability of the proposed method across a range of scenarios. Initially, Figure 4 visualizes the pathways of neurons categorized by class. The visualization validates that various classes utilize unique neural pathways. Subsequently, Figure 5 demonstrates the class relationships derived from the discovered neuron pathways. This approach has the potential to facilitate the assessment of similarity between classes in forthcoming research.

### Weaknesses
This paper does not adequately present a thorough review of the existing literature regarding the proposed method. The reviewer, upon examining the current manuscript, encounters difficulty in clarifying the significance of the proposed method in relation to recent studies. The discussion should not merely enumerate related works; it should also engage in a comparative analysis of the proposed method to facilitate a clear understanding of its significance for the readers.

The manuscript requires enhancements in coherence for better clarity and flow. The abstract states, “showcasing that the found neuron paths have already preserved the model capability on downstream tasks.” However, there is a lack of research focused on downstream tasks.

The absence of crucial ablation studies for the proposed joint attribution score is a significant oversight in this paper. The proposed joint attribution score represents a sophisticated approach that necessitates multiple iterations of back-propagation. To establish its efficacy, it is essential to conduct a comparison with a more straightforward baseline method and demonstrate its superiority over that baseline. Nonetheless, Table 1 presents a simultaneous variation of search methods and scores, which complicates the identification of the specific component contributing to performance improvement. An appropriate ablation study is essential to address the increase in search complexity associated with the proposed method.

This paper does not include comparisons with the baseline method in Figures 5 and 6. The analysis studies are commendable; however, it is essential that they also incorporate quantitative metrics in relation to the baseline for a more comprehensive evaluation. The sole quantitative metric presented in this paper is presented in Table 1. The author needs to incorporate more extensive assessments to demonstrate the advantages of the proposed method.

### Questions
How can we calculate the output by leveraging the neurons present in the initial N layers? Should we share the final classifier to compute the probability p of Eq 1?

It would be better to provide the meaning of Eq 2. Currently, there is no description for Eq 2. Also, the reviewer wonders about the rationale behind employing the sum of gradients as the proposed significant score.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Neuron Path as a novel method for understanding Vision Transformers (ViT), focusing on the flow of information through the Feed-Forward Network (FFN) within the transformer encoder. Unlike methods that highlight input regions, Neuron Path examines influential neurons within the FFN across layers to reveal how information is processed. The authors propose the Joint Attribution Score (JAS), a gradient-based metric that measures the collective influence of neuron groups on the model’s output, along with a layer-by-layer selection method to identify impactful neurons, forming a path that traces critical information flow from input to output. Experiments show that Neuron Path effectively identifies neurons crucial for accurate predictions, with class-level analysis indicating that similar neurons activate for related classes, suggesting an internal organization of semantic information. Additionally, the authors find Neuron Path valuable for model compression, as retaining only essential neuron paths allows for nearly the same performance, revealing redundancy in Vision Transformers that could be leveraged for pruning and optimization.

### Strengths
1. The paper introduces the innovative concept of "Neuron Path," which identifies influential neuron paths specifically within the Feed-Forward Network (FFN) of vision transformers (ViTs). It also presents the Joint Attribution Score (JAS), a gradient-based metric that quantifies the collective influence of neuron groups across layers. Additionally, the Layer-Progressive Neuron Locating Algorithm is proposed to trace influential neuron paths efficiently.

2. The research methodology is robust, with comparisons against established baselines such as "Activation" and "Influence Pattern." The study includes comprehensive experiments, such as neuron intervention and model pruning, which provide strong empirical support for the effectiveness of the Neuron Path method.

3. The paper is well-structured and clearly explains its concepts, with well-defined terms, illustrative figures, and organized sections that enhance readability and understanding.

4. The study advances the interpretability of vision transformers by revealing insights into model behavior, potential for model compression, and implications for real-world applications. It fosters the development of more transparent and efficient vision models by uncovering redundancy that can be leveraged for pruning.

### Weaknesses
1. The current analysis is limited to neurons within the Feed-Forward Network (FFN) component of the Vision Transformer (ViT) encoder. Although FFNs are shown to play a critical role in encoding semantic concepts, excluding the self-attention mechanism from the Neuron Path analysis may lead to an incomplete understanding of information flow within the model, as it overlooks potential interactions between self-attention and FFN modules.

2. The study is focused solely on image classification, a discriminative task, leaving the applicability of Neuron Path to other vision tasks unexplored.

3. The paper does not explore theoretical connections between JAS and established interpretability frameworks, such as information theory or causal inference. Relating JAS to concepts like information bottlenecks or causal pathways could provide a stronger theoretical foundation, enhancing the rigor and interpretability of the findings.

4. While the paper suggests a potential link between neuron paths and semantic information, it does not examine this relationship in depth. Conducting a detailed analysis of how neuron paths correlate with human-interpretable concepts could significantly enhance the model’s interpretability.

5. The paper primarily focuses on identifying neuron paths and their impact on model performance but does not delve into the properties of these paths. Investigating the stability of neuron paths across varying inputs or their evolution during training could provide valuable insights into the model's robustness and behavior. However, due to the computational expense mentioned by the authors, such analyses may be challenging to conduct.

### Questions
1. The proposed method focuses specifically on ViTs and is limited to FFNs. Could this approach be generalized to other model architectures or extended to vision tasks beyond image classification?

2. The authors assert that JAS computation is computationally expensive. Are there possible optimizations or approximations that could be investigated to reduce the computational load and enhance the scalability of the Neuron Path method for larger vision transformer models? Furthermore, why not use zero-order derivatives as a substitute for partial derivatives in calculating JAS, as I believe they could achieve a comparable effect?

3. The paper introduces JAS to measure joint neuron influence, yet a deeper theoretical understanding is needed. Could the authors clarify how maximizing JAS identifies crucial information pathways? Additionally, could they link JAS to information theory concepts like mutual information or information bottleneck to justify its use in measuring influential pathways?

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
4

### Summary
The paper introduces a method to uncover influential neurons across layers in Vision Transformer (ViT) models. It identifies paths of significant neurons from input to output, aiming to enhance understanding of how these models process information internally. The method, called "Neuron Path," employs a layer-progressive approach combined with a novel joint attribution score (JAS), designed to measure the collective influence of selected neurons on model predictions.
The paper proposes the Neuron Path method, which identifies key neuron paths that significantly contribute to the model’s decision-making process. This approach provides insights into information flow within the ViT model by tracing the most impactful neurons through each layer.

### Strengths
The Neuron Path method adopts a layer-progressive approach, which systematically identifies key neurons layer by layer. This method is a step toward understanding how information propagates through Vision Transformers (ViTs), aligning with the need for models that help illustrate the inner workings of transformers more clearly.
The joint attribution score provides a collective measure of neuron importance, enhancing typical neuron-based methods that often focus on single neurons. Although the score parallels existing joint attribution metrics, it offers a practical framework that reflects the relative importance of neurons throughout the model.

### Weaknesses
1. The paper introduces the "Neuron Path" method, which employs a layer-progressive approach to identify influential neurons across Vision Transformer (ViT) layers. However, this method significantly overlaps with established attribution techniques like [1, 2, 3]. The authors could clarify how their approach advances beyond these existing methods.

[1] HINT: Hierarchical Neuron Concept Explainer, CVPR, 2022.
[2] Neuron Shapley: Discovering the Responsible Neurons, NeurIPS, 2020.
[3] WWW: A Unified Framework for Explaining What Where and Why of Neural Networks by Interpretation of Neuron Concepts, CVPR, 2024.


2. While the paper underscores the structural complexity of ViTs as a barrier to interpretability, it narrowly investigates only one neuron type—the output of the first linear layer in each Transformer's FFN module. This limited focus raises questions about the motivation: effective explainability typically aims to enhance interpretability for either the model’s input-output relationship or its internal operations holistically. The choice to explore only specific layers restricts the scope, potentially overlooking valuable insights into other model layers or their contributions.

3. Relying solely on joint attribution scores to assess neuron influence, though innovative, lacks breadth. Incorporating additional metrics—such as concept coherence or task-specific performance indicators—could provide a more comprehensive view of the Neuron Path approach’s effectiveness. Moreover, the experimental focus on ViTs for image classification lacks exploration into generalizability. Extending this analysis to other models and tasks, like object detection, could demonstrate the broader utility of the neuron paths identified here.

4. The assumption that neurons in ViT FFNs are largely redundant warrants more rigorous testing. Studies show that FFN layers encode high-level visual features essential for robust model performance, and not all neurons in these layers may be extraneous. For example, Intriguing Properties of Vision Transformers (NeurIPS, 2021) and others illustrate that FFNs in ViTs play a significant role in preserving semantic information across layers, making them central to effective representation learning. Testing this redundancy hypothesis more thoroughly could yield valuable insights into FFN layer functionality.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To discover the most influential neuron path, this paper propose a joint influence measure to assess the contribution of a set of neurons to the model outcome and a layer-progressive neuron locating approach. In the experiments section, this paper first conducted a quantitative comparison with two baseline methods: Activation & Influence Pattern; And then perform a  class-level analysis and pruning validation.

### Strengths
1. This paper is well-written and easily understood, especially for the `Introduction` and `Related Work` sections. 

2. What's more, the authors performed clear and comprehensive experiments (such as pruning for potential application) and demonstration.

3. The method proposed in this paper is simple yet effective.

### Weaknesses
Apart from the given analysis in this paper, what interests me most is the different patterns between the supervised ViTs and self-supervised MAE, as demonstrated in `Fig.2` & `Tab.1`. At beginning, I personally attributed it to the lack of finetuning in self-supervised MAE, while the author pointed that this was also considered in `Line 218/328`. Although this almost **inverted distribution pattern** mentioned in `Sec 3.1's Preliminary Study` does not seem to have been resolved in `Tab.1`, the neuron path in MAE plays a much greater role than in supervised ViTs with lager *Accuracy Deviation*.

Perhaps this issue is beyond the scope of this paper, but this phenomenon worth a targeted analysis or discussion (maybe in future work).

The formula in `Sec.3.2`'s JAS may be a little confusing.
1. The $w_{i_l}^{l}$ used in Formula(2)&(3) could be more simplified if the two $l$ are always same.
2. A set of neuron $w_{i_l}^{l}$, original values $\bar{w}_{i_l}^{l}$, assigned value $\hat{w}_{i_l}^{l}$ could be more clearly defined before Formula(3).
3. JAS in Formula(2) is difficult to understand, pseudo code like `Algorithm 1` can be helpful.

### Questions
The formula in `Sec.3.2`'s JAS may be a little confusing.
1. The $w_{i_l}^{l}$ used in Formula(2)&(3) could be more simplified if the two $l$ are always same.
2. A set of neuron $w_{i_l}^{l}$, original values $\bar{w}\_{i_l}^{l}$, assigned value $\hat{w}_{i_l}^{l}$ could be more clearly defined before Formula(3).
3. JAS in Formula(2) is difficult to understand, pseudo code like `Algorithm 1` can be helpful.

I would be more than willing to reconsider my score based on the author's response to above `Weaknesses` & `Questions`.

### Soundness
4

### Presentation
4

### Contribution
3
