# ToRL: Topology-preserving Representation Learning Of Object Deformations From Images

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Representation learning of object deformations from images has been a long-standing challenge in various image or video analysis tasks. Existing deep neural networks typically focus on visual features (e.g., intensity and texture), but they often fail to capture the underlying geometric and topological structures of objects. This limitation becomes especially critical in areas, such as medical imaging and 3D modeling, where maintaining the structural integrity of objects is essential for accuracy and generalization across diverse datasets. In this paper, we introduce ToRL, a novel *Topology-preserving Representation Learning* model that, for the first time, offers an explicit mechanism for modeling intricate object topology in the latent feature space. We develop a comprehensive learning framework that captures object deformations via learned transformation groups in the latent space. Each layer of our network's decoder is carefully designed with an integrated smooth composition module, ensuring that topological properties are preserved throughout the learning process. Moreover, in contrast to a few related works that rely on a reference image to predict object deformations during inference, our approach eliminates this impractical requirement. To validate ToRL's effectiveness, we conduct extensive multi-class classification experiments across a wide range of datasets, including synthetic 2D images, real 3D brain magnetic resonance imaging (MRI) scans, real 3D adrenal computed tomography (CT) shapes, and \textcolor{blue}{real 2D facial expression images}. Experimental results demonstrate that ToRL outperforms state-of-the-art methods, setting a new way to enforce topological consistency in representation learning. Our code is available at - https://anonymous.4open.science/r/ToRL-44BF/

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents a representation learning for image deformations by learning transformation groups in the latent space, and innovates the preservation of topology of object in the decoder by incorporating a smooth group composition module. Experiments on various databases along with the comparison with SOTA models are given.

### Strengths
The work proses a novel representation learning to preserve object topology in deformation. The whole paper is well-written.

### Weaknesses
1.	The descriptions and proofs of the given formula (2), (5), (6) are insufficient. Readers cannot fully understand the reason of the design.
2.	The qualitative experiments results are incomplete. No figures show the results on 3D Brains.

### Questions
1.	Please explain and verify the key formula proposed by this work. And explain the originality of the formula. For example, in formula (2), what is the second part? What is the relation to LDDMM?
2.	Please give more qualitative results, especially for 3D Brains database.

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
4

### Summary
This paper introduces ToRL, a novel topology-preserving representation learning model for capturing object deformations from images. Unlike existing deep neural networks that primarily focus on visual features, ToRL explicitly models object topology in the latent feature space through learned transformation groups. The model incorporates a novel decoder architecture with a smooth composition module to preserve topological properties during the learning process. Notably, ToRL eliminates the need for reference images during inference, which is a limitation in existing approaches. The authors validate their method through extensive experiments on multiple datasets, including 2D shapes and 3D medical images, demonstrating superior performance in classification tasks and better preservation of topological properties compared to state-of-the-art methods.

### Strengths
1.	The technical contribution is novel and well-formulated, with a clear mathematical foundation for the transformation groups and their properties in the latent space.
2.	The elimination of the reference image requirement during the inference addresses a practical limitation in existing methods, making the approach more applicable to real-world scenarios.
3.	The experimental validation is comprehensive.

### Weaknesses
1.	The mathematical formulation, while thorough, could benefit from more intuitive explanations or visualizations to help readers better understand the paper. Specifically, the connection between the transformation groups and the actual deformations observed in the images is not immediately clear. It would be beneficial to see a visual representation of how different group operations affect the latent space and how these transformations correspond to changes in the input images. The paper would also benefit from a more detailed explanation of how the group structure is learned and how it ensures topological preservation.
2.	The individual contributions of different components within the ToRL architecture are not analyzed. In particular, how different choices of transformation groups might affect the model's performance is not investigated. For example, the paper does not explore the impact of using different Lie groups or other types of transformation groups on the model's ability to capture various types of deformations. A more detailed ablation study is needed to understand the role of each component and the sensitivity of the model to different design choices.
3.	Although the paper claims superiority in preserving topological properties, additional metrics for assessing topological preservation are needed. While qualitative results are presented, quantitative metrics such as persistent homology or other measures of topological similarity should be included to provide a more rigorous assessment. The current evaluation lacks a direct measure of how well the model preserves topological features such as connected components, holes, and handles.
4.	The paper lacks a detailed analysis of the model's robustness to different types of input perturbations or variations in image quality, which is particularly relevant for medical imaging applications where image acquisition conditions can vary significantly. It is unclear how the model would perform with noisy images, images with varying contrast, or images with artifacts. A robustness analysis is crucial to determine the practical applicability of the proposed method.
5.	Beyond classification, are there any downstream tasks that could better showcase the capabilities to preserve the topology? The paper focuses primarily on classification tasks, which may not fully exploit the topological preservation capabilities of the model. Exploring tasks such as shape matching, image registration, or deformation analysis could provide a more compelling demonstration of the model's strengths.

### Questions
See the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel model and method for image representation that aims to preserve topological information. The authors highlight two main contributions: (i) developing an explicit mechanism for maintaining topological integrity within the latent space, and (ii) integrating a smooth group composition module into the skip connections of a U-shaped network to ensure topology preservation. The performance of ToRL is compared with other methods on downstream classification tasks. However, it should be noted that only classification tasks were evaluated. The main issue with this paper is that everything is artificial: the data, the tasks, and the method are all designed based on these artificial settings.

------

### Update given the author responses:  
Thank you for the responses! While I still believe that the issues I highlighted — including those related to experiments, writing, and methodology — persist, I am willing to acknowledge that the quality of this work has improved. I have therefore raised my score (from 3 to 5) to reflect my perspective and leave the final decision to the AC.

### Strengths
1. The overall approach is somewhat inspiring and can essentially be regarded as an SVF  in the feature space.
2. The experiments demonstrate the effectiveness of the proposed representation learning method by showing improvements in downstream classification tasks

### Weaknesses
1. Lack of real-world applications: The data, tasks, and methods used are all based on artificial settings, similar to early spatial transformer models. Although diffeomorphism is introduced to address classification task with spatial distortion, there is no extensive exploration of SO(3) transformations or other variations, despite substantial literature in this area. There are no experiments involving real applications related to diffeomorphisms, such as registration. The classification experiments are overly simplistic, and there is no post-hoc analysis to determine if the model truly preserves topology. In fact, due to the discrete errors in SVF, it is not theoretically a true diffeomorphism, yet no analysis is provided. As a result, this paper is neither theoretical nor practical.

2. Poor writing structure and unclear contributions: The paper spends considerable space discussing diffeomorphisms, which are not directly related to its contributions, without clearly highlighting what has been contributed. The design of TGM, which could be a key part of the method, is barely mentioned. In contrast, irrelevant network architecture details with many similarities to existing models (e.g., UNet, UNet++) are overly emphasized.

3. Factual errors or lack of evidence: There is a significant factual error regarding AdrenalMNIST3D, which is a binary shape dataset, but the paper incorrectly refers to it as "3D Abdominal MRIs." If the author have visualized the data, no one will make mistakes on distinguish binary shape and MRI. In fact, even for the source, the shape is from CT scans, not MRI. This raises concerns about other potential factual errors that I may not find. Furthermore, the claim that "our approach can be easily applied to other parameterizations of diffeomorphisms" is unsupported. TGM is not adequately described, making it difficult for readers to understand its details, and it is questionable whether other NeuralODE-based methods can be seamlessly integrated into this approach.

4. Computational cost not reported or compared: The paper does not compare the parameter count and computational load against state-of-the-art methods, which may result in unfair comparisons. Additionally, the experiments do not provide comparisons of the model's parameter count and computational load (e.g., FLOPS) before and after incorporating the smooth group composition module. Therefore, it is unclear whether the observed performance improvements are due to the proposed module or simply an increase in parameters and computational cost.

### Questions
See weakness. Please clarify if I've misunderstood.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Existing deep learning methods focus on visual features (like intensity or texture) but fail to preserve geometric and topological structures of objects, which is crucial for applications in medical imaging and 3D modeling. The paper introduces ToRL, a new topology-preserving representation learning framework that models complex object deformations directly from images without relying on a reference image during inference.

contributions:

1. The proposed method models intricate geometric deformations in the latent space using learned transformation groups.
This latent space representation preserves structural and topological integrity during training and decoding.

2. The decoder architecture integrates skip connections with a novel smooth group composition module. This ensures that deformations remain smooth and topologically consistent across network layers.

3. Unlike other models that require a reference image for deformation prediction, ToRL removes this dependency, improving practical usability.

### Strengths
1. ToRL explicitly preserves geometric and topological consistency throughout the representation learning process, which is essential for high-stakes applications such as medical imaging and 3D modeling.

2. Unlike many previous methods, ToRL eliminates the need for reference images during inference, making it more practical and efficient for real-world applications.

3. The decoder’s design with smooth transformations ensures structural continuity and smoothness, addressing the challenges of traditional feature fusion methods like simple concatenation or addition.

4. The results look good to me as it improves the classification performance and the ablation study is comprehensive.

### Weaknesses
1. I am concerned with the complexity. The incorporation of group transformations in the latent space and smooth group composition can increase computational overhead, making the method slower for large-scale datasets or real-time applications.

2. The custom decoder design and latent transformation modules may make it more difficult to integrate with standard architectures (like ResNet or UNet) without extensive modification.

3. Although ToRL is validated on several datasets, it might benefit from additional tests on larger or more diverse real-world datasets to further demonstrate its robustness and generalizability.

4. The strong focus on topology preservation could lead to overfitting in scenarios where topological consistency is not essential, potentially reducing the model’s flexibility.

### Questions
It would be great if the authors could explain more on the computational complexity of the proposed method, and evaluate on more diverse real-world datasets.

### Soundness
3

### Presentation
3

### Contribution
3
