# AutoGenDA: Automated Generative Data Augmentation for Imbalanced Classifications

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Data augmentation is an approach to increasing the training dataset size for deep learning using synthetic data. Recent advancements in image generative models have unleashed the potential of synthesizing high-quality images in data augmentation. However, real-life datasets commonly follow an imbalanced class distribution, where some classes have fewer samples than others. Image generation models may, therefore, struggle to synthesize diverse images for less common classes that lack richness and diversity. To address this, we introduce an automated generative data augmentation method, AutoGenDA, to extract and transfer label-invariant changes across data classes through image captions and text-guided generative models. We also propose an automated search strategy to optimize the data augmentation process for each data class, leading to better generalization. Our experiments demonstrate the effectiveness of AutoGenDA in various object classification datasets. We improve the standard data augmentation baselines by up to 4.9\% on Pascal VOC, Caltech101, MS-COCO, and LVIS under multiple imbalanced classification settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method to augment class-imbalanced datasets with pre-trained generative models, where image captions are leveraged to capture the class-specific and class-agnostic variances. A novel search strategy is developed to optimize the data augmentation process for each class. Competitive results are shown on multiple datasets.

### Strengths
1. The proposed method uses image captions with the format `a photo of <y> that` to capture the class-specific and class-agnostic variance. Such captions are easy to obtain and straightforward to transfer between different classes.

2. The automated search mechanism can adaptively choose between identity, local-caption, and transfer-caption strategies based on the data distribution of different classes.

3. Results on four datasets show improvement in most settings.

### Weaknesses
1. The proposed class-filtering seems limited and lacks ablation studies regarding the parameter $m$ for closest neighbors. 
A caption suits classes A and B => A and B must be similar. However, the converse may not hold. As in the last subplot of Figure 5, `sitting on top of the books` may not fit well with the elephant (even though the elephant is a neighbor class of the teddy bear). The reliance on nearest neighbor captions for transfer augmentation introduces a risk of semantic mismatch, where captions, while syntactically correct, may not align with the visual characteristics of the target class. This is particularly concerning when the visual similarity between classes does not guarantee semantic compatibility of their associated captions. The method should explore more robust ways to ensure that transferred captions are semantically relevant to the target class, rather than relying solely on visual proximity.

2. The search-free baseline is weak in ablation studies. As shown in Fig 4, the optimal strategy from the proposed search method generally assigns a lower probability for augmented samples when the number of samples per class increases. Uniform sampling between the three augmentation types will be suboptimal, even for a fixed strategy. It would also be interesting if the authors could explore the trends of the learned probability w.r.t. N shots. The ablation study lacks a strong baseline that dynamically adjusts augmentation probabilities based on class sample size. Comparing against a fixed uniform sampling strategy is insufficient to demonstrate the effectiveness of the proposed search mechanism. A more compelling baseline would involve a strategy that adapts augmentation probabilities based on the number of available samples per class, providing a more challenging comparison for the proposed method.

3. The authors only leverage captions from the dataset itself, which may limit the diversity of class-agnostic features. One can use LLM to generate plausible captions for a class label and augment the images with them. The reliance on dataset-specific captions limits the potential for generating diverse and novel augmentations. The method should explore leveraging external knowledge sources, such as large language models, to generate a wider range of captions, which could introduce more varied class-agnostic features and improve the robustness of the augmented data.

### Questions
1. What dataset is used for the ablation study in Table 2? The numbers shown do not align with those in Table 1.

2. It might be helpful if the authors consider using an LLM to determine whether the caption suits the class. Using the search strategy to assign a lower probability for unsuitable samples such that they affect the classifier less is dodging the issue without addressing it inherently.

3. What are the trends of learned optimal probability when the number of shots increases? Can you provide a possible explanation for the trend?

4. What are the overheads of running the proposed automated search?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a novel generative data augmentation algorithm that captures the class-specific and class-agnostic variances through image captions and integrates these differences into text-guided generation processes by using the captions as text prompts. In order to determine the optimal mixture of real and synthesized images to be included for each class when fine-tuning a classifier on a dataset, the authors additionally propose a novel automated search framework that relies on the Gumble Softmax trick to make the discrete augmentation selection process differentiable and learnable. The experimental evaluation demonstrates the superiority of AutoGenDA  on four object classification datasets under multiple imbalanced and low-shot settings when compared against a few other standard and generative data augmentation baselines.

### Strengths
- The paper is well-written and is easy to follow.
- The proposed method outperforms other baselines on four object classification datasets under multiple imbalanced and low-shot settings.
- The experimental section of the paper is elaborate and the ablation study covers several different aspects of AutoGenDA such as the computationally cheaper search-free version, the non class-agnostic and the non class-specific augmentation versions, in Table 2.

### Weaknesses
 - In Section 1, line 044, the authors mention the ineffectiveness of generative models in learning diverse variations of data-deficient classes in a dataset. However, Section 4.1 - Training mentions that all experiments utilize a pre-trained StableDiffusion 1.4. Since SD1.4 is already pre-trained on a large dataset (LAION-5B [Ref. 1]) spanning several thousands of classes and samples per class, it is fair to assume that the generative model can generalize and capture data diversity even for under-represented classes in the downstream dataset. 
- As stated by the authors in the limitations, the method relies on a large image captioning model such as BLIP2 and requires a textual inversion-based fine-tuning of the diffusion model. Both of these are computationally expensive steps and must be performed at inference time, thus hampering AutoGenDA’s applicability. In this light, it is important to compare the computational budgets/throughput time (time taken to generate one image) of AutoGenDA with other baselines included in Section 4. 
- It is crucial to include the vanilla text-to-image StableDiffusion 1.4 model as a baseline for comparison in Table 1 and Figure 2. This helps the readers empirically understand the impact of using the proposed methodology vs. simply augmenting the imbalanced classes with a pre-trained generative model.
- How do the authors differentiate class-specific vs. class-agnostic parts of the generated image caption in “a photo of <y> which …..”? For eg: an image-captioning model might generate a caption for an image of a cat as: “a photo of a cat which has thick whiskers and a short tail sitting on a grass field”. In this caption, “thick whiskers”, and “short tail” are class-specific whereas “a grass field” is class-agnostic. If the entire part of the prompt after “a photo of cat which” is chosen for data augmentation of another class y = “cow”, then the StableDiffusion model might end up generating unnatural images.
- The paper misses a few closely related baselines in the related work and for comparison such as [Ref. 2, 3, 4, 5, 6]. Including these in the experimental analyses helps strengthen the authors’ claims. 
- There are only 2 qualitative examples of images generated using AutoGenDA in the manuscript in Figure 5. I would encourage the authors to include more generated images of data-deficient classes with different learnt values of selection probabilities $\alpha$. This helps the reader understand the proposed approach intuitively as well as empirically strengthens the authors’ claims.
- Given that the authors specifically aim to demonstrate the efficacy of their method on class-imbalanced datasets, it would be important to include the widely-adopted ImageNet-LT [Ref. 7] dataset for experimental evaluation on long-tailed settings. This helps the reader empirically compare the performance of AutoGenDA with several other methods specifically designed for class-imbalanced datasets.
- The authors include a section (Section 4.3 - Limitations) that highlights a few limitations. However, it is important to also include the computational cost and memory requirements of using a VLM (BLIP2) and fine-tuning a diffusion model (such as StableDiffusion1.4) at inference time for few-shot learning, and even for full-dataset augmentation.

### Questions
Have the authors considered not fine-tuning the StableDiffusion model and using it out of the box for image-generation using a forward pass? This could be included as an ablation study experiment to understand the importance of fine-tuning to novel downstream classes using textual-inversion.

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
5

### Summary
This paper focuses on leveraging generative models as tools to produce data augmentations that can improve a classifier's accuracy for imbalance and low-shot classification. The authors use BLIP2 to generate captions from images and StableDiffusion to generate images from captions. The authors suggest to use the captions generated by BLIP2 using the real images that are in the majority group as augmented prompt that can be use to generate more example from the minority groups. To do so, they just replace the class label from the majority group's image caption by the class label of the minority group and use StableDiffusion to generate the corresponding image. This approach allow the authors to increase the number of examples in the minority group which improve performances on imbalance classification tasks. To avoid matching class labels with captions that could be not compatible (like "a car which is sitting in the house), the authors leverage class name embeddings to only apply "caption transfer" between class that are closed by in the embedding space.

### Strengths
- The idea is well explained and simple to understand. It make sense to try to leverage the additional diversity we have in the majority groups to augment the number of classes in the minority groups. 
- Authors show good improvements over the DAFusion baseline.
- I appreciate that the authors took the time to describe their preliminary results that did not work in the appendix.

### Weaknesses
 - Lack of relevant related works. The authors claim that they are the first to study automated data augmentation with generative models which clearly show they are not aware that there is an entire research field on this question. I added few references at the end of this comment ( 1) 2) 3) 4) )
- This lack of relevant related work induce a lack of relevant baselines. I would have expected to see comparisons between AutoGenDA and methods like Fill-Up, Diffuse-Mix or the others.
- Lack of novelty. If we look at the works I just listed, I am not convinced that the method presented by the authors is any better than the current existing methods for data augmentation using synthetic data.
- Authors did not use any of the traditional datasets use to evaluate imbalance classification (like CIFAR-10-LT, CIFAR100-LT, Places-LT ,ImageNet-LT, Inat18, NICO++).
- The ablation study does not show for now statistically significant improvement by using AutoGenDA (~0.5% d'accuracy and the authors does not present what is the variance or the dataset they are using for the ablation).


### Questions
- Since the image generation will mostly affect the background for the minority classes, do you have any insights wether the method might just improve robustness with respect to the background? There is the ImageNet-9 dataset that can be use to evaluate how much a model is robust to different background.
- For the ablation study in Table 2, do you have the mean/variance across multiple seeds? I just think that the performance of baseline 2, using only local-caption are very close to the ones of AutoGenDA. For most rows, we have a diff of around 0.5% which does not seem to be statistically significant since in Table 1, you had a variance that can be above 3%. So I would be careful about the claim that results are compromised if we do not use AutoGenDA.
- Can you do your the ablations in Table2 with your statistical test in appendix B?
- Typo line 359 on the paragraph title.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces AutoGenDA, an automated generative data augmentation method aimed at improving deep learning performance on imbalanced datasets. AutoGenDA uses image captions and text-guided generative models to extract and transfer label-invariant changes across different classes to enhance diversity in underrepresented categories. An automated search strategy is proposed to optimize the augmentation process for each class, improving model generalization. The authors claim that AutoGenDA improves baseline data augmentation methods by up to 4.9% on several object classification datasets, including Pascal VOC, Caltech101, MS-COCO, and LVIS.

### Strengths
1. The problem of learning from long-tailed data is important in practice.
2. The idea is natural.

### Weaknesses
1. The basic assumption may be not fully correct. I think the text-guided image-to-image generator should also be trained with long-tailed data.
2. Experiments are not sufficient. Results on ImageNet-LT and iNaturalist should be provided.
3. Many important baselines are not considered. The authors are suggested to compare their proposed method with the baselines considered in [*1, *2]

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
