# CLIP Exhibits Improved Compositional Generalization Through Representation Disentanglement

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Vision-language models (VLMs), such as CLIP, have shown promising Out-of-Distribution (OoD) generalization under various flavors of distribution shifts. Recent studies attempted to investigate the leading cause of this property. In this work, we target the same goal, but focus on a certain type of distribution shift, in which test images contain unseen compositions of attribute-object pairs, but with the objects and attributes being individually seen during training. The models are expected to classify those images into the composition classes, i.e. attribute-object pairs, and also into object classes by ignoring attributes. We carefully designed an authentic image test dataset consisting of attributes for objects that are unlikely encountered in the CLIP training data. We found that the compositions diversity in the training data, as measured by normalized mutual information between objects and attributes, has a significant effect on the improvement of compositional generalization in the CLIP models. We found that image/text representation disentanglement with respect to the composition constituents also plays a key role in the improved generalization of these models. We notice that larger training datasets could potentially trigger emergence of such a disentanglement, as the compositions are typically more diverse in such datasets. We validate this hypothesis through different representation disentanglement metrics, including Z-Diff, and explicitness scores for various CLIPs. Our findings reveal a correlation between better OoD performance and higher scores in these disentanglement metrics, suggesting that improved disentanglement potentially contributes to enhanced compositional OoD generalization in VLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, author examine the compositionally generalization in vision language model. By adopting different combination of disentangled attribute in training dataset of CLIP, author generate a authentic test set that is unseen by model but share the same disentangled attribute. Author also argue that the level of feature disentanglement is high correlate to model generalization by presenting various analysis.

### Strengths
1. This paper propose a high quality test set measuring compositional generalization with generative model. This benchmark provide a simply and more straightforward measurement for compositional generalization of Top1 accuracy for synthetic dataset, over prior measurement like using Visual Genome, or captions perturbation. This could be significant to the community exploring model generalization.
2. Author have conducted various analysis over the relationship between compositionally and feature disentanglement, demonstrate the potential influence of the proposed dataset at a large scale.

### Weaknesses
1. In 3.2, the statement 'We interpret these findings as strong evidence that the inclusion of language supervision, particularly during CLIP training, positively impacts the model representation quality' might be too strong of a claim. As explored in prior work("Data Determines Distributional Robustness in Contrastive Language Image Pre-training (CLIP)") , language supervision might not be the sole reason for model generalization. There're multiple variance between VLM and other modality and author should not attribute such improvement solely on language supervision. Specifically, the authors do not adequately control for other factors such as the size and diversity of the image data itself, which could also contribute to the observed improvements. The comparison between VLM and other modalities needs more rigorous controls to isolate the impact of language supervision.
2. Conclusion are less convincing due to the limited candidate in each experiment. For instance, in Table 1, it will be interesting to shows the NMI for a subset of LAION with the same number of data to other dataset. Also in table 2, there's only 4 results, please consider adding more variance of dataset and CLIP architecture . The lack of diversity in datasets and model architectures makes it difficult to generalize the findings. For example, including different CLIP architectures such as ResNet-based models would provide a more comprehensive view. The limited number of data points in Table 2 makes it difficult to draw statistically significant conclusions.
3. The narrative after section 4 is a bit too rush, it's hard to follow the method and results. For instance, what is 'dimensions' in 4.1 stands for? And more context over 'switching dimension' would be helpful. Moreover, I cannot tell how the conclusion of 'A higher level of accuracy in the image retrieval task indicates that the model embeddings are more disentangled.' can be drawn from experiment in 4.2. The explanation of 'dimensions' within the embedding space is unclear, and the 'switching dimension' concept requires more detailed explanation. The connection between image retrieval accuracy and disentanglement is not well-justified, and the experimental setup needs more clarity.
4. There's some grammar and formatting issue, for instance in section 4, spaces were missing between sentences.

### Questions
Page 3: in the imrpoved generalization -> typo
Please refer to weakness. While this work could be potential significant to the community, the clarity could be further improve, especially on drawing the connection between compositionally and feature disentanglement.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies CLIP models under a different type of distribution shift namely compositional OOD generalization, where the objects and attributes may be individually seen during training, but their composition is unseen. A new dataset, ImageNet-AO is generated using DALL-E, containing such novel compositions for ImageNet classes. It is ensured that the generated compositions are not present in the CLIP training datasets. Key observations are - i) compositional diversity of the training dataset improves the compositional generalization of the CLIP model, ii) image/text representation disentanglement of objects and attributes improves generalization, iii) larger, more diverse datasets leads to better compositional generalization, iv) better disentanglement in representations leads to better compositional generalization.

### Strengths
- The experiments are well-designed 
- Conclusions drawn are very interesting and insightful 
- The dataset ImageNet-AO can be helpful for future study as well

### Weaknesses
- "*the training dataset of the OpenAI CLIP has not been released, which makes designing a test set that has a truly different distribution from the training one challenging. We aim to address these issues in this paper, by focusing our attention on the compositional generalization
in the single object setting, and designing an authentic test dataset to assess the training data characteristics and mechanisms in the models that lead to the OoD generalization.*" -- This contradicts the following statement where the authors claim that they verify that the ImageNet-AO images are not a part of several CLIP training dataset -- "*To ensure these combinations were not present in the CLIP training set, we conducted a thorough search and removed any combinations that were found.*"
- "*By assessing the captions in the training sets, we guarantee that none of the captions in our test dataset or similar captions are included in the CLIP training data.*"
    - Is this check done for all the other datasets considered in the paper as well (LAION, YFCC15m, CC12m, and DataComp)?
    -  A similar check should be done on images as well, it is possible that such images with different captions are present in the training set. Usually, captions from web sources are not exactly descriptive of the image.
- "*We also found that the CLIPs that show higher OoD generalization typically exhibit strong disentangled text representations. Furthermore, such CLIPs also enjoy a more disentangled image representation with respect to the attributes and objects as well.*" -- the experiments in the paper do hint at the above statement. But this does not necessarily imply the following: "*Specifically, a dataset with diverse compositions of attribute-objects facilitates a more disentangled text representation, which in turn induces a disentangled image representation through contrastive learning.*" It could be possible that diverse images lead to disentangled image representations as well. 
- "*To evaluate the degree of disentanglement in the training captions utilized by the CLIP, we conducted an analysis by measuring the normalized mutual information (NMI) between the object class and attribute tokens, whose domains are defined based on the captions in our generated dataset.*" -- Could the authors explain how the domains are defined based on the captions in the generated dataset? More details on how the NMI is measured would be helpful.
- Fig.4 - It is not clear how the disentanglement metrics are computed for the image encoder. 
- "*We aimed for a diverse set of class names to enhance the complexity of the generated images.*" -- It is not clear if all 1000 classes were used or only a subset. If a subset was used, how was this chosen?
- "*This dataset was produced by creating compositional images via a text-to-image model, using an Attribute+Object template.*" -- could the authors give more details/ a citation for the Attribute+Object template?
- Could the authors provide details on where the 30 adjectives were chosen from?
- "*Lastly, human evaluation was used to validate the generated images, with images not closely aligning with their prompts removed. After this process, around 12000 combinations remained, for which we successfully generated near 50000 accurate, high-quality images.*" - The order of the two statements may have to be swapped? Could the authors provide details on how this human evaluation was done?
- "*For the test sets, all 1000 classes of ImageNet were used as the in-distribution set and expanded the number of classes to approximately 12000 for the OoD set.*" -- could the authors share how the captions were created for the OOD set? Sharing some examples would be helpful. I believe the 80 captions are used only for the ID set, and single relevant captions are used for the OOD set?
- In Fig.1, for a more fair comparison, the image-only models such as DINO-v2 and BEiT-v2 should also be trained on the datasets that were used for training CLIP (by using only the images, and ignoring the captions). Without matching at least the image datasets, there is not enough evidence to support the following statement - "*We interpret these findings as strong evidence that the inclusion of language supervision, particularly during CLIP training, positively impacts the model representation quality, hence making it possible to generalize to unseen compositions, despite the absence of such compositions in their training data.*"

Nitpicks -

- citation format seems non-standard - (x) vs. [x]
- inline citations should use the format xyz et al., rather than [x] 
- A citation for the work that defines "compositional OOD generalization" would be helpful

### Questions
- Although the experiments and conclusions in the paper are interesting and useful, several aspects of the paper need more clarity. These are mentioned in the weaknesses section. I will be happy to update my score based on clarifications provided by the authors. 
- Codes, models, and datasets must be open-sourced for the benefit of future research. Could the authors comment on this? Would these be released upon acceptance?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new dataset to benchmark the compositional capabilities of several CLIP models (OpenAI and OpenCLIP). This dataset is generated using DALLE, and covers the 1000 class names from the ImageNet dataset combined with 30 adjectives. Manual annotators validated the combinations, resulting in ~12k plausible compositions, from which they generated 50k images. The authors also propose to measure the compositional generalization via the normalized mutual information between objects and attributes, and use Z-Diff Score, DCI-Informativeness, Explicitness score, and DCIMIG metrics to evaluate the disentanglement in the embeddings from the models.

### Strengths
+ This paper proposes an interesting approach to measure the compositional capabilities of large-scale VL models, by leveraging a text-to-
image model to generate new images with specific attributes.

+ The authors provide a large set of experimental results in the supplementary materials, showing that CLIP models struggle with their proposed dataset

+ This paper is well-structured, easy to read and follow.

### Weaknesses
 + There is no description or motivation for the attribute selection, are those attributes randomly selected or generated? How do the authors guarantee that those attributes are not present or co-occur less in the training data?

+ The human validation seems crucial in generating the proposed benchmark; however, there is no detailed description of how this was performed. 

+ In section 1, the authors claim: "By assessing the captions in the training sets, we guarantee that none of the captions in our test dataset or similar captions are included in the CLIP training data." -- however, I couldn't find any empirical or theoretical evidence, nor existing reference for this claim.

+ The human validation only asses for the plausibility of the noun-adjective composition, but are the images generated by DALLE following those compositions? Prior work has shown that Diffusion models "struggle to understand the composition of certain concepts, such as confusing the attributes of different objects or relations between objects"[1]. It is unclear if the generated dataset follows the attribute-noun composition, or falls into this category. See also [2].

+ Most of the conclusions are prevalent in the literature (e.g., the diversity of training captions promotes compositionality [3]), and the mutual information analysis does not seem to provide additional insights [4, 5].

### Questions
Is there any particular reason why DINO-v2 and BEiT-v2 are mentioned briefly in the introduction, but no further analysis is done in the following sections?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
