# YOLO-RD: Introducing Relevant and Compact Explicit Knowledge to YOLO by Retriever-Dictionary

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Identifying and localizing objects within images is a fundamental challenge, and numerous efforts have been made to enhance model accuracy by experimenting with diverse architectures and refining training strategies. Nevertheless, a prevalent limitation in existing models is overemphasizing the current input while ignoring the information from the entire dataset. We introduce an innovative {\em \textbf{R}etriever}-{\em\textbf{D}ictionary} (RD) module to address this issue. This architecture enables YOLO-based models to efficiently retrieve features from a Dictionary that contains the insight of the dataset, which is built by the knowledge from  Visual Models (VM), Large Language Models (LLM), or Visual Language Models (VLM). The flexible RD enables the model to incorporate such explicit knowledge that enhances the ability to benefit multiple tasks, specifically, segmentation, detection, and classification, from pixel to image level. The experiments show that using the RD significantly improves model performance, achieving more than a 3\% increase in mean Average Precision for object detection with less than a 1\% increase in model parameters. Beyond 1-stage object detection models, the RD module improves the effectiveness of 2-stage models and DETR-based architectures, such as Faster R-CNN and Deformable DETR.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to improve object detection with YOLO by introducing explicit knowledge in the form of a Retriever-Dictionary (RD) module. The dictionary is created using features from LLMs, VLMs, or VMs. The additional module helps the model retrieve relevant features from a dictionary that contains distilled information about the training dataset. The paper shows that such an addition leads to improved model performance.

### Strengths
The main strength of the paper is the increase in performance that is achieved by the proposed approach. The paper shows that the proposed approach leads to more than 3% performance improvements for object detection with YOLO. This result is quite good and demonstrates that the proposed approach might be useful. The paper also shows that the proposed approach can be used with other object detection models.

### Weaknesses
The major weaknesses of the paper are related to the lack of clarity about the motivation for the proposed approach and lack of clarity about several decisions. The authors should address the following in their response:

1. It's not clear, why is the dataset dictionary needed at all. Why doesn’t batch gradient descent already incorporate dataset information during training? The paper does not make it clear why/how is the dataset information not used during standard model training.

2. In lines 262-263, the paper mentions that the dimension of the dictionary features are the same dimension as YOLO middle layer dimension. Did the authors try incorporating dataset information at multiple locations in the network? It would help to see whether adding features at multiple levels (perhaps using dictionaries of different feature dimensions) improves performance.

3. Further, why add dictionary feature information at only the middle layer? What about any other layer?  Are there any draw-backs to using another layer?

4. The objective function written in section 3.3 (no equation number), needs to be explained better. It's not clear at all what is the objective trying to achieve and how does it achieve that. Such an explanation would help in understanding the motivation/approach more readily.

### Questions
Please see the weaknesses section.

### Soundness
2

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
3

### Summary
This paper proposes the Retriever Dictionary module, which improves the model’s resource utilization by incorporating knowledge from other parts of the dataset, extending beyond the local region or individual image. The Retriever module aggregates regional features to generate a query, while the Dictionary can be an unimodal or multimodal model, such as YOLOv7, CLIP, or GPT. Experiments with multiple detectors, including YOLOv7, YOLOv9, Faster R-CNN, and Deformable DETR, demonstrate performance improvements.

### Strengths
-  The idea of leveraging external knowledge from the dataset for object detection is promising, especially with foundational large language models (LLMs) and vision-language models (VLMs) enabling this approach.

- Applying dictionary learning to enhance object detection while maintaining a minimal increase in parameters is impressive.

### Weaknesses
 - The primary weakness of this paper is the lack of computational analysis. The authors repeatedly emphasize "carefully balancing accuracy, model parameters, and latency when handling external information." However, latency is not addressed in the experiments. Although the added trainable parameters are minimal, the integration of a large foundational model significantly impacts the pipeline. It’s crucial to include runtime/latency and FLOPs metrics, particularly for YOLOv7 and YOLOv9 in Tables 1-3. This trade-off will help verify the effectiveness of the proposed approach. 

 - Employing different dictionaries demonstrates different behaviors. For instance, VLM improves YOLO models more than Faster R-CNN with LLM. This variation lacks justification, which seems essential to understand the behavior.


Minor:
- The conclusion should be separated from the Experiment section.

### Questions
- The statement, "We demonstrate that incorporating external knowledge from models such as VLMs and LLMs can significantly enhance model performance," reflects an already established idea in object detection [1, 2]. How does this paper uniquely contribute to this area?

- The training strategy appears time-intensive. For example, Faster R-CNN is trained for 120 epochs, though a comparable baseline performance can typically be reached with 36 epochs (3x schedule). How do the authors justify this extended training duration?

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
4

### Summary
The paper introduces the Retriever Dictionary (RD) module, a lightweight and efficient approach to integrating explicit knowledge into existing object detectors like YOLO, Faster R-CNN and DETR. RD outperforms other knowledge integration methods by introducing only 0.2M additional parameters while achieving superior performance. The module leverages pre-stored explicit knowledge within the Dictionary to enhance input features, demonstrating improvements across various YOLO-based tasks and broader computer vision applications like segmenation. The article also discusses ablation studies and visualizations that highlight the effectiveness of the RD module in retaining important information while eliminating unimportant details.

### Strengths
* Innovation: It presents a approach to integrate explicit knowledge into YOLO-based models by "efficiently" retrieving features from a dictionary built from insights across the entire dataset.
* Efficiency & Performance: RD achieves superior performance in object detection tasks, introducing only a minimal additional computational overhead~(with 0.2M additional parameters). And the paper shows it the lightest solution among compared methods.
* Visualization: The article includes visualizations that show RD's effectiveness in retaining important information while eliminating unimportant details.

### Weaknesses
1. While the paper effectively demonstrates the RD module's potential to enhance model accuracy with minimal computational increase, the inclusion of speed metrics, specifically inference time per image or frames per second (FPS), would provide a more holistic view of the module's practicality and readiness for real-world deployment. This is crucial for assessing its suitability for time-sensitive applications. The absence of such metrics makes it difficult to evaluate the trade-off between accuracy gains and potential latency increases.
2. The knowledge integration methods compared in the article not only introduce external knowledge but also possess the capability for open-world detection, allowing them to identify objects not seen during training. In contrast, the current work is primarily tailored for specific datasets, limiting its applicability to scenarios with known object categories. Although the paper demonstrates improved accuracy within these constraints, the overall significance is diminished as a result of this lack of generalization capability.

### Questions
see Weaknesses

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
4

### Summary
The paper purposed a Retriever-Dictionary (RD) module to solve the balancing problem between current input and whole dataset information in object identification and localization. Its retriever processes region features to generate a query, and the dictionary that saves dataset information could prompt the query to select relevant atoms. The dictionary incorporates different modalities as encoder, ensuring a good overall understanding of the dataset in various modality spaces.

### Strengths
1. **Rigorousity of pipeline design.** The whole Retriever Dictionary design is theoretically robust. The authors have considered the overall operation of Retriever and designed Global Information Exchanger with Coefficient Generator. The introduction of PONO also helps to prevent Dictionary from collapsing into an identity matrix. 

2. **Innovative incorporation of multimodal external knowledge in dictionary building.** The authors purposed that the dictionary could be initialized by multiple modalities of models, ensuring a comprehensive representation of the dataset. In response to huge amount of feature vectors involved, operations including k-means and contrasive learning distillation have made the dictionary condensed and efficient.

3. **Congeneric methodology design.** The framework is extendable to RCNNs, Transformer-based detection models and other kindred models. The authors have incorporated experiments on these models. And their experiments supports their theory basically well.

### Weaknesses
1. The paper's figure lacks generalization for the whole work, i.e. Figure 1 and 2 cannot fully describe the complete functionality of the RD module. From the dictionary and module structural description, the whole pipeline is hard to follow as the authors have mentioned

2. The authors refer to RAG in their related work and mention its limitations in vision applications. RAG is a system that relies on external multi-modules and is mainly applied to Large language models.The article tries to compare its consistency with RAG in terms of knowledge base ideas, but lacks further explanations on this. e.g. How exactly does it differ from a RAG as part of the network structure?

3. Fig.5, the role of the RD module could have a richer and more well annotated picture explanation. Depending on the modality of initialisation (VM, VLM, LLM), there is also a strong need to visualize the effect of different modalities for initialization. 

4. Although the model introduces minimal parameter increase, there is limited discussion on its impact on computational speed and inference latency, especially for deployment in real-time applications.

5. The dictionary initialization process, particularly when using VLMs or LLMs, is not straightforward and may demand significant computational resources during setup. More details on optimizing or reducing this process would be beneficial. 

6. The module's efficiency in managing larger datasets or dynamic, continuously updated dictionaries remains unclear. Further analysis on handling diverse data scales could improve its adaptability.

### Questions
Have you tried incorporating multple modality initialization and alignment for the dictionary? For example, VM and VLM initialization together? For more questions, please refer to the weaknesses listed above

### Soundness
3

### Presentation
2

### Contribution
3
