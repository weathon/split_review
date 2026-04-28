# Disentangled representations of microscopy images

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 3, 1, 3

## Abstract
Microscopy image analysis is fundamental for different applications, from diagnosis to synthetic engineering and environmental monitoring. In the last few years, the number of available images has been constantly growing, thanks to technological advancements, pushing toward the development of automatic image analysis methods based on deep learning. Although deep neural networks have demonstrated great performance in this field, interpretability — an essential requirement for microscopy image analysis — remains an open challenge.     
This work proposes a Disentangled Representation Learning (DRL) methodology to enhance model interpretability for microscopy image classification. 
Exploiting benchmark datasets coming from three different microscopic image domains, including plankton, yeast vacuoles, and human cells, we show how a DRL framework, based on transfer learning from synthetic features, can provide a good trade-off between accuracy and interpretability in this domain.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a study of disentangled representation learning on three microscopy image datasets. The representation learning strategy starts by training an Ada-GVAE model using a Textures-dSprites dataset introduced in this work. The dataset is supposed to reflect simple textures that could help interpret information in microscopy images. After training this model in a weakly supervised way, it is used to encode images of another domain, with optional unsupervised finetuning using a beta-VAE. The resulting features are low dimensional, and interpretable, and are used to train classifiers.

The ideas and the study are generally interesting, but the paper lacks technical novelty, is limited to a small-scale empirical evaluation only, and the experiments are incomplete to fully understand the value of the proposed strategy.

### Strengths
* The paper evaluates the recent ideas of disentangled representation learning using weak supervision in a more realistic application.
* The paper also presents an alternative to learning the disentangled representation from RGB images based on models pretrained at large scale.
* The paper proposes a new sprites dataset to facilitate the interpretation of microscopy images.

### Weaknesses
 * The technical contribution is limited. Beyond the sprites dataset and the use of pretrained features, many of the ideas have been presented in previous works.
* The experimental evaluation is limited to quantifying the impact of classifier types (GBT vs MLP) and input type (RGB vs DINO features). Many questions remain open regarding how much classification accuracy could be obtained without the proposed disentanglement procedure. Can the authors compare results of training a classifier directly with RGB images and another classifier with DINO features without any modifications? These results would help understand how difficult the tasks are and what is the trade-off between using disentanglement vs not using it.
* It is possible that DINO features are already disentangled and all what the proposed strategy is doing is assigning names to some of the factors of variation that DINO can detect. Therefore, the disentanglement is not really happening in the VAEs but rather obtained from a model pretrained at large scale. What type of experiment can the authors design to test this hypothesis?
* If the hypothesis above is not rejected, the value of proposed methods is limited to only annotating factors of variation rather than identifying them in a weakly supervised manner to then being transferred.

### Questions
Can the authors clarify the questions above? Specifically, the extent to which DINO already offers certain degree of disentanglement and how the factors of variation of interest could be identified directly from these representations.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the interpretability challenge in microscopy image analysis using deep learning approaches. The authors propose a novel methodology based on Disentangled Representation Learning (DRL) to enhance model interpretability while maintaining classification performance. The approach leverages transfer learning from synthetic features and is validated across three diverse microscopy domains: plankton, yeast vacuoles, and human cells. The growing volume of microscopy images due to technological advances has necessitated automated analysis methods, yet interpretability remains crucial for practical applications in fields such as diagnosis and environmental monitoring. The authors demonstrate that their DRL framework successfully balances the trade-off between model accuracy and interpretability in microscopy image classification tasks.

### Strengths
1. The manuscript is well-written and easy to follow, with clear organization and logical flow.
2. The application of weakly-supervised DRL to real-world image analysis represents a promising and valuable research direction.

### Weaknesses
1.The scope of this work appears too narrow, focusing solely on microscopy images.  The proposed approach might be more convincing if demonstrated on natural images as well.
2.The authors fail to adequately justify why DRL should be specifically applied to microscopy image analysis.  Furthermore, they do not clearly articulate whether this specific application domain poses new challenges or requirements for DRL that could lead to innovative solutions.  The authors' insights into these aspects are not well presented.
3.Given the lack of compelling insights, this work appears to be primarily an application of existing DRL methods without significant methodological or theoretical innovation. This level of contribution may not align with ICLR's focus on novel methodological and theoretical advances in machine learning.
4.The paper appears to lack comparative experiments. While the disentanglement scores might be novel evaluation metrics, the absence of comparisons for classification performance is particularly concerning and unreasonable.

### Questions
Referring to the weaknesses noted above, I find the claimed contributions of this paper not sufficiently convincing.  Could the authors provide a more compelling explanation of their main contributions, particularly addressing:
1. Why DRL is specifically suited for microscopy image analysis.
2. What novel challenges or requirements this domain brings to DRL.
3. How their approach advances the theoretical or methodological aspects of DRL beyond simple application.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes a Disentangled Representation Learning (DRL) approach to improve interpretability in microscopy image classification. By pre-training on synthetic data (Texture-dSprite) to capture factors of variation, the authors apply these learned representations to real-world microscopy datasets (Plankton Lensless, Plankton WHOI15, Budding Yeast Vacuoles, and Sipakmed Human Cells). Their method aims to support model interpretability while achieving high classification performance with gradient-boosted trees and MLPs for downstream analysis.

### Strengths
The paper explores the application of an existing DRL framework to the specific domain of microscopy images. This idea is interesting as it shows a potential pathway for combining DRL with microscopy image analysis.

### Weaknesses
A significant weakness as it seems, is the absence of a comparison with other similar methods. The paper presents only one framework and does not discuss or evaluate alternative approaches, which weakens the case for this framework’s efficacy or advantage over existing methods.

The contributions of the paper in terms of novelty are unclear. The study applies an existing DRL approach to a new domain but does not appear to introduce any fundamentally new concepts, techniques, or substantial modifications to existing methods. The only apparent novelty - the application of DRL to microscopy imaging does not suffice. This limits the potential impact and originality of the work.

The paper’s presentation suffers from numerous issues that impede readability and clarity:
1. There are instances of informal languages, such as the use of “thanks.”
2. The text contains multiple errors at the word, sentence, and structural levels, which disrupts the reading experience. Sections like Section 2.2 (“Disentanglement Evaluation”) resemble output generated by ChatGPT and lack rigorous academic polish.
3. Figures appear low-resolution, with inadequate explanations in captions. Captions should be comprehensive and self-contained, but here, they lack essential details, e.g., explanations of metrics like OMES and balanced accuracy.
4. The use of multiple highlight types (underscoring, bold, italics) is excessive and distractive. Minimal highlighting would improve readability and make essential points more accessible.
5. Important metrics are either not explained in the text or lack adequate definitions in the captions, leaving readers uncertain of their meaning. This omission impacts the study’s reproducibility and overall clarity.

### Questions
Most of my questions are related to major weaknesses.

What specific contributions does this paper make beyond applying DRL to microscopy images? It would be helpful if the authors could clarify what is novel in their approach and how it advances the state-of-the-art in microscopy image analysis beyond existing techniques.

What are alternative approaches the authors could have used for comparison? 

Metric explanations (e.g., OMES, MIG, DCI and balanced accuracy) are mostly missing. Could the authors clarify these metrics, ideally using mathematical notation and provide justification for using them?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose to use a disentangled representation learning framework to enhence model interpretability for microscopy image classifications. The method is based on fine-tuning a model trained on synthetic images, the proposed framework is tested on some microscopy images datasets.

### Strengths
- The paper addresses a significant challenge in representation learning: disentanglement, which plays a pivotal role in improving the interpretability of classifiers, particularly in the context of biological images.

### Weaknesses
 - The proposed approach is not well explained. Indeed, the method proposed by the authors learns a disentangled model with weak-supervision using Ada-GVAE on a synthetic dataset and then fine-tune it on
 a microscopy datasets. However, it is unclear why Ada-GVAE is choosed and how is the model fine-tuned.

- The difference between the proposed method and Dapueto et al is unclear.

- The authors claim that the disentanglment learned from a synthetic images can be transferred to microscopy images, such claim should be theoretically and empirically evidenced.

- The paper is not well organized, for instance a "Related Work" section should be added. Two different sections (2.2 and 3.5) have the same title "DISENTANGLEMENT EVALUATION".

- In Fig, 1, what is exactely fine-tuned and how ?

- How is an RGB image directly fed to the classifier (GBT and MLP)?

- In line 322, the authors state "We can observe that after finetuning, it may change, nicely adapting to the specificity of the dataset, where scale and texture are more relevant.", It is unclear for me why scale and texture are more relevent then "scale and shape", as it is the case before fine-tuning.

- The proposed evaluation metrics (ex:OMES) are unclear.

- The authors do not compare their method to any other work, having a solid baseline is important.

- The used classifiers (GBT and MLP)  are very simple, more sophisticated ones should be used (CNNs based for example).

- Inputting an RGB image to the classifer is unclear as it is well-established that deep features (in this cas the features extracted by DINO) have more important patterns.
  
- To assess the quality of the representation, the authors realied on classification. While a good representation can lead to a better accuracy. A good representation does not necessary mean a disentangled one.

- Using the accuracy only to measure the quality classification performance is not enough.

- The figures are small and the captions are not clear enough.

- In Figure 6, the OMES indicates that the proposed method does not lead to better disentanglement.

### Questions
- In Fig, 1, what is exactely fine-tuned and how ?

- How is an RGB image directly fed to the classifier (GBT and MLP)?

- In line 322, the authors state "We can observe that after finetuning, it may change, nicely adapting to the specificity of the dataset, where scale and texture are more relevant.", It is unclear for me why scale and texture are more relevent then "scale and shape", as it is the case before fine-tuning.

- The proposed evaluation metrics (ex:OMES) are unclear.

- The authors do not compare their method to any other work, having a solid baseline is important.

- The used classifiers (GBT and MLP)  are very simple, more sophisticated ones should be used (CNNs based for example).

- Inputting an RGB image to the classifer is unclear as it is well-established that deep features (in this cas the features extracted by DINO) have more important patterns.
  
- To assess the quality of the representation, the authors realied on classification. While a good representation can lead to a better accuracy. A good representation does not necessary mean a disentangled one.

- Using the accuracy only to measure the quality classification performance is not enough.

- The figures are small and the captions are not clear enough.

- In Figure 6, the OMES indicates that the proposed method does not lead to better disentanglement.

### Soundness
1

### Presentation
2

### Contribution
1
