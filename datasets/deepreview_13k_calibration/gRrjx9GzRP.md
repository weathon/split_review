# Leveraging Color Channel Independence for Improved Unsupervised Object Detection

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Object-centric architectures can learn to extract distinct object representations from visual scenes, enabling downstream applications on the object level. 
Similarly to autoencoder-based image models, object-centric approaches have been trained on the unsupervised reconstruction loss of images encoded by RGB color spaces. 
In our work, we challenge the common assumption that RGB images are the optimal target for unsupervised learning in computer vision.
We discuss conceptually and empirically that other color spaces, such as HSV, bear essential characteristics for object-centric representation learning, like robustness to lighting conditions. We further show that models improve when requiring them to predict additional color channels.
Specifically, we propose the RGB-S space, which extends RGB with HSV's saturation component and leads to markedly better reconstruction and disentanglement for five common evaluation datasets.
The use of composite color spaces can be implemented with basically no computational overhead, is agnostic of the models' architecture, and is universally applicable across a wide range of visual computing tasks and training types. 
The findings of our approach encourage additional investigations in computer vision tasks beyond object-centric learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores the influence of color channels on object-centric representation learning (OCRL). It first shows the strong correlation, sensitivity to lighting, and non-uniformity of the RGB space. Then a combination of RGB with other color channels is studied for OCRL. Experimental results show that RGB with the saturation channel in HSV achieves consistent improvement on all datasets used in this paper. The paper is too technical and lacks novelty as the combination of color space is often used as a trick in computer vision and image processing tasks.

### Strengths
1. Give a detailed analysis of RGB space.
2. Verify that RGB with S channel achieves consistent performance gain on different datasets.

### Weaknesses
1. The paper is not easy to read as the cross-referencing of figures and tables is disordered.
2. It claims that "We challenge the common assumption that RGB images are the optimal target for unsupervised learning in computer vision and demonstrate this for OCRL". It's better to give a reference which shows the RGB image is optimal. 
3. Table 2 is not too strong to support that RGB-S is good enough. Mostly, it's not the best on different datasets, for example, RGB-SV is better than RGB-S on Clevr, MultishapesNet-4, and MultishapesNet-24; HSV is the best for Clevrtex. 
4. The experimental analysis is not convincing, for example in Line 457, which one is most important for representation, the color space or a powerful decoder?
5. How does the model guarantee universality when it is trained on the combined color space?  I still think RGB is the most universal space even though the performance is slightly worse than others in Table 2.

### Questions
See weakness above.
The biggest concern for me is the novelty of the paper and the universality of the model trained on various numbers of color channels.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a novel perspective on output target color space for object-centric representation learning. The authors provide an in-depth discussion of various color spaces as prediction targets, including RGB, HSV, and CIE-LAB. In particular, using Slot Attention as the backbone, the authors conduct experiments with different target color spaces, encompassing both individual and composite color spaces.

### Strengths
1) As most previous works focused on the different color space input, the exploration and discussion of using different color space as the target is beneficial for the community.
2) This paper finds that predicting composite color spaces offers a slight improvement over traditional RGB targets in unsupervised object-centric representation learning (OCRL). This approach not only inspires advancements in OCRL but also provides a direction for image modeling-based unsupervised representation learning.
3) The discussion of different color spaces is also beneficial for the computer vision community.

### Weaknesses
1) Although the authors present an interesting approach to enhancing model understanding of foreground objects in a scene by predicting different color spaces, the paper primarily discusses the impact of various color spaces from a results-oriented perspective without providing a more in-depth analysis. For example, influence on model parameters and feature characteristics are lacking. I hope the authors can offer further insights into how different target color spaces influence the model.

2) Although the authors state that their work focuses on color spaces, the essence of their approach lies in enhancing the model's perceptual abilities by adjusting target objectives. Therefore, using only an RGB-RGB baseline may not be reliable. It would be more robust to include comparisons with methods that use different representations as targets, such as (Seitzer et al., 2023).

3) While the authors' idea is interesting, they do not provide a reliable analysis from a representation perspective on the inclusion of different color space targets. For instance, in Figure 2 of the main paper, there is a noticeable similarity between saturation and the mask in highlighting foreground objects; however, the mask is discrete and contains categorical information, while saturation focuses solely on object shape. There is insufficient technical analysis explaining the impact of using saturation.

### Questions
1) The authors only discuss grayscale for the single-channel approach. Considering the high correlation between RGB channels, what would the impact for OCRL be if using just one of the RGB channels as the target?

2)  Why does introducing composite color spaces improve object-centric representation? Could you provide a more detailed explanation from a feature perspective?

3) How does the model behave for different values of the number of slots? Is there an ablation showing the effect of that parameter?

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
The paper suggests that using RGB to encode input images is not the best input representation for object-centric representation learning. Instead, the paper shows that, in simple datasets, using RGB concatenated with HSV leads to better results.

### Strengths
I find very interesting the overall goal of the paper of enhancing the color representation.

### Weaknesses
Experiments are on synthetic datasets, or with simple and colorful objects. The selected datasets have few objects in front of simple backgrounds, making color information to be more useful than it would be in more challenging datasests with real images (e.g., COCO, ImageNet).

The experiments are very limited (as acknowledged in the conclusion). I praise the authors for acknowledging this, but I find that the limited experiments are insufficient to claim that building better color representations for the input would lead to improved performance in realistic image datasets beyond clever, …

I think the idea is good, but the authors should have tested the idea on more challenging datasets. It is likely that the simple approach proposed in the paper to extend color information would be insufficient when the dataset is more complex.

### Questions
1. would it be possible to test on more challenging datasets? Do you still expect a benefit there?

2. There are many color spaces that provide decorrelated channels. A simplest one is to use a linear rotation of the space spanned by the channels R,G and B by doing PCA on it.

### Soundness
2

### Presentation
3

### Contribution
2
