# On the Influence of Shape, Texture and Color for Learning Semantic Segmentation

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
In recent years, a body of works has emerged, studying shape and texture biases of off-the-shelf pre-trained deep neural networks (DNN) for image classification. These works study how much a trained DNN relies on image cues, predominantly shape and texture. In this work, we switch the perspective, posing the following questions: What can a DNN learn from each of the image cues, i.e., shape, texture and color, respectively? How much does each cue influence the learning success? And what are the synergy effects between different cues? Studying these questions sheds light upon cue influences on learning and thus the learning capabilities of DNNs.
We study these questions on semantic segmentation which allows us to address our questions on pixel level. 
To conduct this study, we develop a generic procedure to decompose a given dataset into multiple ones, each of them only containing either a single cue or a chosen mixture. This framework is then applied to two real-world datasets, Cityscapes and PASCAL Context, and a synthetic data set based on the CARLA simulator. We learn the given semantic segmentation task from these cue datasets, creating cue experts. Early fusion of cues is performed by constructing appropriate datasets. This is complemented by a late fusion of experts which allows us to study cue influence location-dependent on pixel level. Our study on three datasets reveals that neither texture nor shape clearly dominate the learning success, however a combination of shape and color but without texture achieves surprisingly strong results. Our findings hold for convolutional and transformer backbones. In particular, qualitatively there is almost no difference in how both of the architecture types extract information from the different cues.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an analysis of the influence of shape, texture, and color on semantic segmentation performance, proposing a methodology that leverages augmented datasets to isolate these specific ‘cues’ and assess their individual contributions. To achieve this, the paper uses HSV channels to represent colors, edge detection to represent shapes, and ground-truth mask cropping to isolate textures. Through extensive combinations of these cues, the authors evaluate the performance of semantic segmentation using both real-world datasets and the CARLA simulator, applying this methodology to both convolutional and transformer-based architectures.

### Strengths
The paper is easy to read, with a significant level of detail dedicated to the experiments and results. The study is comprehensive in its scope, providing extensive combinations of cue-based datasets and evaluating them across different model architectures. 

By isolating and recombining shape, color, and texture cues, the paper sheds light on how each of these elements contributes to segmentation performance. This could be beneficial for understanding data domain gaps and predicting failure modes of segmentation models.

### Weaknesses
The study’s approach, while straightforward, lacks sufficient depth in its experimental design and interpretation. The experiments primarily provide surface-level insights without delving into a more profound analysis of underlying factors. The paper would benefit from a more rigorous exploration of the interactions between the different cues, rather than just evaluating them in isolation and simple combinations. For example, the study does not explore how the strength or quality of one cue might affect the reliance on other cues. It also does not investigate the impact of noise or perturbations on individual cues and how this affects the overall segmentation performance. A deeper analysis of these interactions would provide more meaningful insights. 

Most of the findings and corresponding discussion, for example, that shape cues correspond heavily to semantic boundaries and that textures play a significant role in broader regions—are valid but not particularly surprising and interesting to computer vision researchers. Most of the results presented in the paper fall into this category. The insights gained from this study feel somewhat limited, leaving the reader with few novel takeaways. As such, it may fall marginally below the acceptance threshold in its current form.

There are several technical and methodological concerns, please see Questions.

### Questions
Using Voronoi diagrams, assigned randomly to semantic classes, raises questions about whether the generated "texture" dataset truly reflects the original distribution of classes. How about assigning semantic classes to Voronoi diagrams by their frequency in the original dataset?

The reliance on an external edge detector for shape cues introduces external biases. For example, if the edge detectors are trained on semantic boundaries, using them will introduce additional semantic information. How about using low-level filter-based edge detectors?

When shape and color are combined (no texture), the input image becomes piecewise constant. Since the segmentation maps are also piecewise constant, this operation simplifies the mapping between input and output. The authors present this result as surprising, yet it is somewhat intuitive given the characteristics of segmentation tasks.

mIoU may not be a good metric to fully capture the performance across classes with different frequencies. A more robust analysis would include additional metrics such as frequency-weighted IoU and pixel accuracy.

Figures 10 and 11 are interesting and important. I suggest moving them to the main paper.

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
3

### Summary
This work studies the impact of shape and texture on training DNN. They develop a generic procedure to decompose a given dataset into multiple ones, each of them only containing either a single cue or a chosen mixture. they develop a generic procedure to decompose a given dataset into multiple ones, each of them only containing either a single cue or a chosen mixture. The study on three datasets reveals that neither texture nor shape clearly dominates the learning success, however, a combination of shape and color but without texture achieves surprisingly strong results. The findings hold for convolutional and transformer backbones. In particular, qualitatively there is almost no difference in how both of the architecture types extract information from the different cues.

### Strengths
1. This paper comprehensively analyzes the impact of shape, texture, gray and their combination on semantic segmentation tasks, and provides a method to derive a texture-only dataset. This paper compares the different effects of these image cues on CNN and Transformer.
2. The structure of the paper is relatively clear and the introduction of the methods is relatively detailed.
3. Studying the impact of different image cues on semantic segmentation is very meaningful for designing networks and contributes to the deep learning community.

### Weaknesses
1. This paper shows the effects of different visual cues on semantic segmentation, but lacks a detailed analysis of why these effects occur, and explores which modules and operations are introduced into the model to reduce these effects. Specifically, the paper does not delve into the architectural nuances that might make a network more sensitive to one cue over another. For instance, are certain types of convolutional filters or attention mechanisms more likely to capture shape information versus texture? The analysis remains at a high level, observing performance differences without dissecting the underlying causes within the network's processing.
2. In Table 3, we find that the rank change of the CARLA dataset is large relative to the Cityscapes dataset. Please provide more explanations why different performances are shown on different datasets. The paper should explore the specific characteristics of each dataset that might lead to these differences. For example, does the synthetic nature of CARLA, with its more controlled and less diverse textures, make it more susceptible to variations in cue dominance compared to the real-world complexity of Cityscapes? A more in-depth analysis of dataset properties is needed.
3. Figure 6 is not clear enough. The visualization lacks sufficient detail to understand the relationship between segment size and cue influence. It is difficult to discern the specific trends and patterns being presented, making it hard to draw meaningful conclusions from the figure.

### Questions
1. After we have studied the impact of different visual cues on the segmentation effect of the model, can we use certain deep learning operations to specifically improve the effect of the model?
2. In Table 3, we find that the ranking changes of the CARLA dataset are larger than those of the Cityscapes dataset. Why do visual cues show such differences on different datasets?

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
The paper investigates the importance of different image cues (e.g. color, shape, texture) for successful training of deep semantic segmentation models. Different from previous work, this study does not focus on the analysis of conventionally pretrained models. Instead, it is based on "expert" models trained on custom datasets containing only one or a combination of selected cues. To enable this type of analysis, the paper proposes several approaches to transform original image datasets into versions that contain only specific cues. The analysis includes two real image datasets: Pascal Context and Cityscapes, as well as a single synthetic dataset based on CARLA which provides more control over the image generation process. Additionally, the study explores considers convolutional as well as transformer based architectures.

### Strengths
Previous shape and textures bias studies rarely considered dense prediction tasks, so this looks like a valuable contribution.

The proposed study is the first that investigates the effect of individual cues (and different combinations of cues) on the training process of the semantic segmentation models.

The paper consolidates a method for extraction of different image cues from natural images. This enables transformation of the original datasets into variants that contain a single image cue or selected combination of cues.

### Weaknesses
Presentation quality could be improved. 
I suggest placing the tables and figures right after being referenced in the text. 

I found the Texture Cue Extraction paragraph confusing. The main manuscript should include more details and be more descriptive. I am not sure how the Voronoi diagrams are created and do they depend on the content of the corresponding image. Are class frequencies and distributions preserved in this texture cue dataset? 

The last paragraph in 4.1 should also describe the evaluation protocol. What kind of input each expert model considers during the evaluation? This is partly addressed at the end of the first paragraph in 4.2. However, I think it deserves a separate paragraph to clarify the edge cases, so that the reader has no uncertanties when considering the numerical results. I would also consider including the EED and HED results with processing in the corresponding table. 

I am not entirely convinced with the conclusions of the discussion about the influence of the size on the performance of texture and shape experts. The texture expert might specialize in these classes not because the size of their segments, but just because they are more frequent, or their texture is more unique and therefore easier to discriminate. I am not sure. It obviously depends on the properties of the training dataset. I think this requires further considerations.

I feel like the paper lacks some practical takeaways or ideas for future work that would use the findings of this study for improving the performance or robustness of deep models for semantic segmentation.

### Questions
Do you expect similar conclusions for panoptic segmentation as well? This might open some new questions. For example, if the same clues have equal effect on the performance in thing and stuff classes? Mask transformers [1] disentangle the panoptic inference into mask localization and classification. It would be interesting to see which clues are more important for localization, and which ones for classification. What are your thoughts about this and the future work?

In table 2, the convolutional model and the transformer achieve similar performance when considering regular images with all cues. However, the transformer consistently outperforms the convolutional model by a large margin on datasets which consider only subsets of clues. What is the reason behind that?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors try to answer an important question, which is what can DNNs learn from image cues such as shape, texture, and color. They argue that this is the opposite of what is typically done in previous literature, as previous works rather focus on understanding how much a trained neural network relies on different cues. In short, the aim of this paper is to understand what are the important cues for successful trainings.
To answer this question, the authors propose to decompose a given dataset into multiple different sub-datasets, with each one including one or more cues to learn from. They set up different experiments (cue-experts) from different combinations of cues in the context of semantic segmentation and using both CNNs and Transformers.
The outcome of these experiments is that there is no clear winner between relying on shapes rather than texture is essential for good performance, but rather a combination of shape and colors.

### Strengths
1. In my opinion, this paper addresses a very interesting problem, namely, which are the cues to learn from. A thorough analysis could be beneficial for other problems such as explainability, Domain Adaptation, and  Domain Generalization.

2. The paper is well-written and clear, and I particularly appreciate Table 1 summarising all the possible settings.

3. A good number of experiments across different datasets and architectures have been conducted.

### Weaknesses
1. My main concern about this paper is that the results are unclear. The rank change column is particularly helpful in understanding the current scenario, and all datasets clearly have different cue orders when taken individually across datasets. I understand that the authors claim that they do not drastically differ, but still, they are not consistent in drawing clear conclusions. 

2. The claimed results are not surprising, and I do not see a clear impact or the direction of this paper. For example, it is obvious to me that cues such as texture is overall better than color since texture also contains color information, as also stated by the authors. Furthermore, is not surprising that using all cues is better.

3. One final major concern is about the validity of some experiments. In particular, on how evaluation is done for the color cue expert. To my understanding, in such cases, all convolutions have been replaced with 1x1 convolution kernel. These produce very poor results, but we do not know whether this is because of a model that does not have enough capacity or the color is not a useful cue.
Furthermore, I am not sure that it is a valid method to train a model one cue and then test it on the original images. In some cases, this could make sense, but in other cases, the distribution shift between source and target images could be so high that the model is not able to perform well.

### Questions
1. When exacting the cue colors, is 1x1 convolution used for all layers or only for the first? In the former case, it is really hard to understand whether the network has enough capacity to learn a difficult task such as semantic segmentation, while the latter case would invalidate the experiment as the following layers would have a larger receptive field.

2. The second part of the sentence at L193: “As it preserves color, it extracts the cues S+V+HS, and analogously to the treatment of the C cue provides the cues S+V as well.” is not clear to me.

3. About weaknesses 3, I wonder whether it is possible to test each cue expert under the scenario it has been trained on, and not on the original images. Maybe the authors could clarify this point and motivate this choice.

### Soundness
2

### Presentation
3

### Contribution
2
