# LucidPPN: Unambiguous Prototypical Parts Network for User-centric Interpretable Computer Vision

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Prototypical parts networks combine the power of deep learning with the explainability of case-based reasoning to make accurate, interpretable decisions. They follow the this looks like that reasoning, representing each prototypical part with patches from training images. However, a single image patch comprises multiple visual features, such as color, shape, and texture, making it difficult for users to identify which feature is important to the model.
To reduce this ambiguity, we introduce the Lucid Prototypical Parts Network (LucidPPN), a novel prototypical parts network that separates color prototypes from other visual features. Our method employs two reasoning branches: one for non-color visual features, processing grayscale images, and another focusing solely on color information. This separation allows us to clarify whether the model's decisions are based on color, shape, or texture. Additionally, LucidPPN identifies prototypical parts corresponding to semantic parts of classified objects, making comparisons between data classes more intuitive, e.g., when two bird species might differ primarily in belly color.
Our experiments demonstrate that the two branches are complementary and together achieve results comparable to baseline methods. More importantly, LucidPPN generates less ambiguous prototypical parts, enhancing user understanding.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Summary Of Contributions:
1.Introduction of LucidPPN: This novel architecture separates color features from other visual components during inference, enabling clearer identification of feature importance in the decision-making process.
2.Consistent Object-Part Mapping: A mechanism ensures that prototypes within each class consistently correspond to the same object parts, improving interpretability.
3.Enhanced Visualization Method: A more intuitive visualization type is introduced, optimized for fine-grained classification.
4.Comprehensive Analysis: The paper provides an in-depth examination of LucidPPN's usefulness and limitations, particularly identifying cases where color may or may not be a critical feature in fine-grained classification.

### Strengths
1.The LucidPPN in the paper consists of two branches, one for color and the other for shape/texture, which effectively decouples different features. This method can reduce the ambiguity of traditional prototype networks and enable users to better understand the reasons behind the model's decisions.

2.Compared to existing methods, LucidPPN achieves a more detailed analysis of Prototypical Parts, making it easier for users to understand the features that the model is focusing on.

3.Through user studies, it was proven that the explanations provided by LucidPPN are clearer and easier for users to understand than those of other models such as PIP-Net. This empirical result helps to enhance the persuasiveness of the method.

### Weaknesses
Weakness

1.The Section 3 has a lot of paragraphs but lacks subheadings, making it difficult to follow the logical flow of the different parts.

2.There was no noticeable advantage in accuracy. The model was compared on four datasets in total, and its accuracy was lower than that of PIP-Net on two of the datasets, especially on the CUB dataset, where its accuracy was lower than that of all three methods, and no explanation was given for this gap.

### Questions
Concerns:
1.It is recommended to add subheadings to each key step or method description to make it easier for readers to understand and locate the content.

2.Consider further improving the accuracy of LucidPPN to enhance its explainability while maintaining a minimal loss of performance.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors proposed a Lucid Prototypical Parts Network (LucidPPN), a novel prototypical parts network that separates color prototypes from other visual features. A LucidPPN has two branches: a ShapeTexNet and a ColorNet. Given an input image, the ShapeTexNet is a convolutional neural network (CNN) that takes a gray-scale version of the image as input and outputs a set of feature maps, and the ColorNet is another CNN that takes a down-sampled version of the image as input and outputs another set of feature maps. Since the last layer of both the ShapeTexNet and the ColorNet is a 1x1 convolutional layer with KM filters, we can interpret the last convolutional layer as a prototype layer with KM prototypes, where K is the number of prototypes per class and M is the number of classes, and the output of the last layer as prototype activation maps. The output feature maps (aka prototype activation maps) from the ShapeTexNet and the ColorNet are fused using element-wise products, and then max-pooled to yield a prototype similarity score for each prototype. The predicted class score is simply an average of the prototype similarity scores over all prototypes of the class. In a LucidPPN, each of the K prototypes in each of the M classes corresponds to consistent image parts (e.g., the first prototype of each class corresponds to head of a bird, etc.). This is achieved by aligning the fused output feature maps (prototype activation maps) with segmentation masks produced by a pre-trained PDiscoNet (an object part segmentation model) using a prototypical-object part correspondence loss. In addition to a loss function to improve the classification accuracy of the entire model, the authors also introduced a loss function to improve the classification accuracy of the ShapeTexNet alone and to disentangle color from other visual features. The authors evaluated their LucidPPN models on 4 commonly used fine-grained classification benchmarks (CUB-200-2011, Stanford Cars, Stanford Dogs, and Oxford Flowers), and found that their LucidPPN models achieved competitive test accuracy compared to other interpretable models. The authors also did a user study to evaluate the influence of disentangling color from other visual attributes on interpretability.

### Strengths
- Originality: The paper introduced a novel idea of disentangling color from shape and texture, so that the visual attribute of each prototype is more clearly defined (compared to prior work).
- Quality: The authors did show that their LucidPPN could maintain a reasonable accuracy while providing less ambiguous prototypes.
- Clarity: The paper is clearly written.
- Significance: Interpretability is a significant area of research in machine learning.

### Weaknesses
 - Quality: There seems to be no prototype projection in this work. Without prototype projections, it is unclear if the prototypes can be faithfully visualized using training images (because the closest training images to a prototype could still be far away from the prototype in the latent space). The lack of a projection step raises concerns about the interpretability of the prototypes, as the visualized patches may not accurately represent the learned features. The reliance on finding the closest training images in the latent space without explicit projection could lead to visualizations that are not truly representative of the prototype's activation pattern.
- Clarity: Page 6, Lines 314-315. I am confused as to whether you are aligning the segmentation masks from PDiscoNet with prototype activation maps from the ShapeTexNet or the aggregated feature maps. It is not clear if the correspondence loss is applied before or after the fusion of the ShapeTexNet and ColorNet feature maps. This ambiguity makes it difficult to understand how the part alignment is achieved and whether the color information influences the part correspondence.

### Questions
- My main concern is that I did not see prototype projections in this work. Without prototype projections, how could you conclusively visualize prototypes using training images? The closest training images to a prototype could still be far away from the prototype in the latent space.
- During training, are the segmentation masks from PDiscoNet aligned with the ShapeTexNet feature maps or the aggregated feature maps? 
- I am also not clear as to why binary cross entropy is used instead of multi-class cross entropy for training?

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
5

### Summary
This paper propose to disentangle color prototypes from other visual features in ProtoPNets, by introducing a novel network architecture, named LucidPPN. The proposed method clarifies feature importance and aligns prototypical parts with object semantics, enhancing interpretability. Experiments show that LucidPPN achieves competitive accuracy while producing clearer and less ambiguous explanations for users.

### Strengths
* This paper explicitly decouple prototypes into specific semantic types, such as color and shape, whereas existing methods have overlooked this aspect of information. And I believe this paper could serve as a significant inspiration for future research.
* This paper provides sufficient cases and visualizations to validate the semantic information of the learned prototypes.
* The paper is well-written and easy to follow.
* The authors provide code for reproducibility check.

### Weaknesses
[Major]

1.  **Quantitative evaluation of the interpretability:** In previous work, Huang et al. [1] have discussed the inconsistency of traditional ProtoPNets. Does this issue exists within the proposed method? Please provide qualitative or quantitative evaluations. Specifically, how does the proposed method address the issue of prototype drift during training, which can lead to inconsistent explanations? Furthermore, how does the method ensure that the learned prototypes remain semantically meaningful and do not become entangled with irrelevant features over time? A more rigorous analysis of the temporal stability of the prototypes is needed.
2.  **Experiments:** Please supplement the missing results for baseline methods on datasets like DOGS and FLOWERS in Table 1, as adapting to these datasets, which were not covered in the original papers, seems quite straightforward. The lack of these results makes it difficult to assess the generalizability of the proposed method across different datasets and image characteristics. It is crucial to demonstrate that the method performs consistently well, not just on a limited set of datasets.
3.  **Experiments:** This paper only implement the proposed method on several CNNs. However, vision Transformers are introduced to the realm of CV for several years, and have also been implemented as the backbone of ProtoPNets [2]. Please provide additional experimental results using ViT [3-4] or even CLIP [5] as the backbone. The absence of experiments with transformer-based architectures is a significant limitation, given their widespread use and potential for capturing long-range dependencies in images. It is important to evaluate the proposed method's performance with these architectures to demonstrate its versatility and applicability to modern deep learning models.
4.  **Related Work:** In XAI, introducing human understandable semantics as evidences for prediction has been explored by concept bottleneck models (CBMs) [6]. What is the relationship between the proposed method and CBMs. Can concepts be introduced into the realm of ProtoPNet for higher interpretability? Specifically, how does the proposed method compare to CBMs in terms of the level of human interpretability and the ability to provide causal explanations? A more detailed discussion of the differences and potential synergies between these approaches is needed.

[Minor]

1.  **Experiments:** What is the computational cost of inference and training? Please provide a comparison with baseline methods, including metrics such as training time, FLOPs, and memory usage.

### Questions
My questions are listed in "Weaknesses" section.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript presents the Lucid Prototypical Parts Network (LucidPPN), designed to identify key visual features—specifically color, shape, and texture—based on the prototypical parts networks. The proposed LucidPPN utilizes a non-color branch to process grayscale images alongside a color branch that focuses on color information, thereby clarifying the model's decisions based on these visual attributes. Experimental results demonstrate that the proposed method exhibits advantages over baseline approaches and generates more interpretable prototype parts.

### Strengths
(1)	The methodology is well-structured, with intuitive design in the separation of color and non-color network branches, making it accessible and easy to understand.

(2)	The experiments are comprehensive, with a substantial number of visualization results provided in the appendix, enhancing the manuscript's depth.

### Weaknesses
(1)	While analyzing "color," "shape," and "texture" offers a valuable perspective, these features have been extensively studied in the field of visual perception. Given that the shallow layers of deep networks are capable of extracting low-level features, the necessity for additional processing and analysis from prototypical parts raises concerns on the novelty and contribution of this work. Specifically, the shallow layers of convolutional neural networks are known to learn features that closely resemble Gabor filters and color opponency, which already capture shape, texture, and color information respectively. The added complexity of a prototypical parts network, therefore, needs more justification beyond simply disentangling these features, as this disentanglement is already implicitly present in the early layers of standard architectures.

(2)	The improvements demonstrated by the proposed method appear to be limited because its performance on some instances is lower than that of the compared methods. For example, in Table 1, the proposed method underperforms other prototypical parts networks on some datasets. While color, shape, and texture are indeed significant visual features in interpretability, they may not be sufficiently critical in this context. The performance drop suggests that the proposed method might be losing crucial information by processing color separately, and the late fusion of these features may not be as effective as early fusion in capturing the complex interplay between color, shape, and texture necessary for optimal classification performance. This raises questions about the trade-off between interpretability and accuracy.

(3)	The organization of the experimental section appears somewhat unbalanced. While the results and visualizations presented are commendable, an excessive amount of content is relegated to the appendix, which may hinder the reader’s ability to grasp key insights and maintain a coherent narrative. The main body of the paper lacks a comprehensive analysis of the results, making it difficult to assess the true effectiveness of the proposed method without referring to the appendix. This makes the paper feel incomplete and less impactful.

### Questions
(1)	The manuscript focuses on interpretability through the lenses of color, shape, and texture. However, other low-level features such as edges, contrast, and spatial frequency are also relevant. Have alternative low-level features also been considered in the analysis?

(2)	The datasets utilized in the experiments are relatively small in size. How will the proposed method perform on larger datasets, such as ImageNet? Some insights into performance scalability would be beneficial.

(3)	The manuscript primarily presents visualization results for the prototypical parts identified by the proposed method. How do these results compare with other prototypical parts-based models? A comparative analysis would enhance the understanding of the method's effectiveness.

(4)	In global feature visualizations, such as Figure 14, the manuscript illustrates the ability of the proposed method to detect shape and color. How does this compare with traditional edge detection operators (e.g., Sobel) for shape extraction and color feature extraction methods (e.g., color histogram)? Additionally, how does it compare with the direct visualizations of shallow layer attention to texture and color using techniques like Grad-CAM?

### Soundness
3

### Presentation
3

### Contribution
3
