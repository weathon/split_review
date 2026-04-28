# What do vision transformers learn? A visual exploration

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Vision transformers (ViTs) are quickly becoming the de-facto architecture for computer vision, yet we understand very little about why they work and what they learn. While existing studies visually analyze the mechanisms of convolutional neural networks, an analogous exploration of ViTs remains challenging. In this paper, we first address the obstacles to performing visualizations on ViTs. Assisted by these solutions, we observe that neurons in ViTs trained with language model supervision (e.g., CLIP) are activated by semantic concepts rather than visual features. We also explore the underlying differences between ViTs and CNNs, and we find that transformers detect image background features, just like their convolutional counterparts, but their predictions depend far less on high-frequency information. On the other hand, both architecture types behave similarly in the way features progress from abstract patterns in early layers to concrete objects in late layers. In addition, we show that ViTs maintain spatial information in all layers except the final layer. In contrast to previous works, we show that the last layer most likely discards the spatial information and behaves as a learned global pooling operation. Finally, we conduct large-scale visualizations on a wide range of ViT variants, including DeiT, CoaT, ConViT, PiT, Swin, and Twin, to validate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, authors  address  the visualizations on vision transformers. they observe build up of complex features across the hierarchy across layers, similar to CNNs. They also find that neurons in ViTs trained with language model supervision (e.g., CLIP) are activated by semantic concepts rather than visual features. They also show that transformers detect image background features, just like CNNs.

### Strengths
This work addresses an important problem in deep learning which is understanding how visual transformers work, and shed light on these black boxes. This is certainly helpful to, in particular, the vision community.

The paper is generally well organized and well written. The prior research is also adequately mentioned.

The findings, although, not all being quite novel, are interesting. In particular, I find the finding that transformers make better use of background and foreground information, compared to CNNs, interesting. "we find that transformers detect image background features, just like their convolutional counterparts, but their predictions depend far less on high-frequency information."


This works applies classic methods for visualizing CNNs to ViTs and is that sense is actually not very different from other approaches and results are somewhat expected and less surprising. The works emphasizes on similarities between CNNs and Transformers, in particular progressive specialization, rather than highlighting main differences deep inside the network, rather what information is being used.

### Weaknesses
The work still does not get into the meat of what transformers really do! For example, what key, query, and value do? and what makes them more effective. For example, it is shown that they use foreground and background more effectively, but it is not explored why that happens. Another important aspect would be how the key,query,value operations relate to convolution. Some visualization may help get insights regarding this.


Minor issues:
Page 3  Recent work ? —> missing reference

### Questions
Q: in light of your results can you tell what really explains higher performance of vision transformers compared to CNNs? I mean in the architecture? can that be visualized?

Q: how much of these also apply to the MLPmixer architecture, or its variants

Q: It seems like authors, are discarding visualization of keys, queries and values! I think visualization of these features might actually gives good insights regarding the designs of ViT. And to understand how exactly these differ from convolution operation! 

Q: In page 5, section: you are discussing the receptive field of neurons. It is true that neurons in all layers have full receptive field in the image, but what is the effective receptive field? In other words, can you show how much and where in the image a neuron in getting its input from?

Q: For long researchers believed that CNNs might be a good model of how vision should be done mainly because they parallel well with human visual system and extract features in a hierarchy. Vision transformers seem to match less with CNNs and human visual system in terms of their structure. Can we say we are diverging from coming up with a unified model of how vision should be done?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper visual the intermediate features learned by ViTs using an optimization-based approach. It then explores the differences between ViTs and CNNs on the learned features and find that ViTs tend to detect background features and depend less on texture information. Further they show that ViTs maintain spatial information in all layers except the last one. The visualization is also conducted on other variants including DeiT, CoaT, Swin and Twin etc.

### Strengths
-	Visualization features for ViTs is an important but largely neglected topic. This work presents some solid feature visualization results and may inspire the community on related research.

### Weaknesses
-	The novelty of the visualization method is limited. It mainly borrows the method of Olah et al. 2017 and adapt it on ViTs with some engineering tweaks.
-	Some observations of this work are not new. For example, the authors find that ViTs maintain spatial information in all layers except the last one, and the last layer produces very similar patch tokens. This behavior has been pointed out by some existing papers. Check “DeepViT: Towards Deeper Vision Transformer 2021.” It has shown that patch tokens of the last layer are almost the same, producing very similar output patch tokens. So it is not surprising that you can just use any of the patch tokens in the last layer to predict the result and achieve decent accuracy.
-	In table2, multiple ViT models and CNN models are compared to show that the ViTs are better at using background information to predict correct classes. The issue here is that the used ViTs are more powerful than the CNNs with more parameters and more computations. ViTs have consistently better classification accuracies. The comparison is not fair and thus the conclusion of “ViTs better at using background information” is not convincing.

### Questions
There are some missing citations.  Sec. 2.1: Recent work ? has studied. Sec. 3: and augmentation ensembling (?).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper compares the learning abilities of Vision Transformer vs CNN, explores if the learning abilities changes with the language guided vision transformers such as CLIP. The authors look into optimization based Vision Transformer visualization techniques for their analysis, using gradient steps to maximize feature activations, starting from random noise. The authors experiment to identify the most activating images for each feature and then forward these images to the network. The goal is to understand the presence of spatial information in different layers of the transformer. The authors claim that most of the spatial information in individual channels is lost in the last layer. They also find that ViTs consistently outperform CNNs when information, either foreground or background, is missing

### Strengths
1. Finding that ViTs learn to preserve spatial information despite lacking the inductive bias of CNN
2. Finding that the ViTs spatial information is lost in the last layer
3. Authors look into text guided ViTs such as CLIP in a different way than existing work which I think is an important contribution that I see will be useful for the community in understanding future vision language models

### Weaknesses
1. Section 2.1 last paragraph reference missing 'Related work ?'
2. Section 3, line 4 reference missing 'augmentation ensembling ?'
3. The authors claim that ViTs learn to preserve spatial information despite lacking the inductive bias of CNN but this property disappears  from the last layer. The author seems to be not sure why (section 4, page 5). This is a key finding of the paper that needs more theory and/or experiment based proof

### Questions
1. Will you be able to show any experimentation and/or theoretical justification on why the last layer of ViTs loses the spatial information?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a framework for visualizing the features learned by vision transformers to gain insight into their internal mechanisms. It offers several key findings and conclusions, including the suitability of the linear projections in the feed-forward layers for visualization, the preservation of spatial information by ViTs, their enhanced utilization of background information compared to CNNs, and the observation that ViTs trained using CLIP learn visual concept features rather than object-specific features. The study conducts extensive experiments and visualizations to demonstrate the effectiveness of the proposed framework and to validate these findings.

### Strengths
- This paper is among the first few works that visualize the feature learned in vision transformers.
- A substantial number of experiments have been conducted to offer a comprehensive visual analysis.
- Some findings such as “ViTs  make better use of background information” is interesting.

### Weaknesses
 - The visualization method employed in this study lacks novelty.
- Section 2.2 and Section 3 suffer from incomplete or missing references, and there is room for improvement in the overall writing quality.
- The results presented in Table 1 and Section 4 fail to yield significant or novel insights. A noticeable performance disparity exists between "Natural Accuracy" and "Isolating CLS." It would be expected that fine-tuning solely the linear classification head could close this performance gap, reinforcing the notion that the CLS token primarily aggregates information in later layers. It's worth mentioning that prior research has also indicated the viability of placing the CLS token in later layers (Touvron et al. 2021), and using global averages for ViTs (Liu et al. 2021). Therefore, these findings lack substantial significance.
- While the findings in Section 5 and Table 2 are interesting, they are limited to evaluating only the basic ViT architecture.
- Currently, the presented findings appear somewhat isolated. To enhance the paper's quality, it is advisable to provide a more in-depth analysis and insight into the interrelationship between these findings.

### Questions
- What does the term “Normalized Top-5 ImageNet Accuracy” mean?
- The choice of the fifth layer in Section 6 is not well-justified and requires further explanation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
