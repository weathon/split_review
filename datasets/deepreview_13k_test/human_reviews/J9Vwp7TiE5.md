# SegGen: Supercharging Segmentation Models with Text2Mask and Mask2Img Synthesis

- Decision: Reject
- Scores: 5, 5, 8, 6

## Abstract
We present \modelname, a new data generation approach that pushes the performance boundaries of state-of-the-art image segmentation models.
One major bottleneck of previous data synthesis methods for segmentation is the design of ``segmentation labeler module'', which is used to synthesize segmentation masks for images~\cite{wu2023diffumask}. The segmentation labeler modules, which are segmentation models by themselves, bound the performance of downstream segmentation models trained on the synthetic masks. These methods encounter a  ``chicken or egg dilemma'' and thus fail to outperform existing segmentation models. 
To address this issue, we propose a novel method that \textbf{\textit{reverses}} the traditional data generation process: we first (i) generate highly diverse segmentation masks that match real-world distribution from text prompts, and then (ii) synthesize realistic images conditioned on the segmentation masks. In this way, we avoid the need for any segmentation labeler module. 
\modelname integrates two data generation strategies, namely MaskSyn and ImgSyn, to largely improve data diversity in synthetic masks and images. 
Notably, the high quality of our synthetic data enables our method to outperform the previous data synthesis method~\cite{wu2023diffumask} by +25.2 mIoU on ADE20K when trained with pure synthetic data. 
On the highly competitive ADE20K and COCO benchmarks, 
our data generation method markedly improves the performance of state-of-the-art segmentation models in semantic segmentation, panoptic segmentation, and instance segmentation.
Moreover, experiments show that training with our synthetic data makes the segmentation models more robust towards unseen data domains, including real-world and AI-generated images.
\keywords{Image Segmentation \and Image Generation \and Deep Learning}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the usage of image synthesis techniques to augment the training data for image segmentation models. More specifically, the authors proposed two techniques, one is text2mask synthesis and the other one is mask2image synthesis. The authors employed state-of-the-art open-sourced stable diffusion model for text-to-mask generation, and then ControlNet pipeline for mask-to-image generation. Afterward, two models are finetuned on COCO annotations and then used for augmenting the original COCO segmentation dataset. The experimental results demonstrate that the generated image-mask pairs are beneficial for COCO segmentation tasks under different settings. Further ablation studies shed light on how to use generated data to improve the image segmentation performance.

### Strengths
1. The authors explored a way of using generative models for data augmentation for training image segmentation models, With the increasing fidelity of image generation models, e.g., stable diffusion, it is worth to have a study on how the powerful image generation model can empower or benefit image understanding tasks.

2. This work proposed two strategies for augmenting image segmentation data to boost the performance of image segmentation models. Specifically, the authors employed stable diffusion model to generate masks from texts, and then used ControlNet-like model for mask-to-image generation. These two strategies together helps to attain a large amount of image-mask pairs with high quality.

3. Based on the proposed techniques, the authors augmented COCO training set for image segmentation and then tried two training strategies: pretraining and joint training. It turned out that the extra generated images are beneficial to the image segmentation models under different settings.

### Weaknesses
1. My main concern is about the relatively marginal improvement after adding a large amount of generated images. Though the author claimed over 2pt and 1pt gain for tiny and large models on ADE20k, I think the performance-price ratio is pretty low in that they generated over 1M images for ADE20K, which is significantly larger than the original training data size. Likewise, the authors also generated over 1M images for COCO, which is around 10 times bigger than the original training data. However, the gains for large models are less than 1pt across the board. These results make me highly doubt whether the generated images are really extrapolating the training data or just lazily interpolating the training data.

2. The ablation study using 1000 training examples is misleading. If I understand correctly, the authors still used the full COCO training set for training the image generation models. As such, the generation models are indeed able to "extrapolate" the training data beyond the 1000 examples, and the final improvements over the baseline which merely uses 1000 real examples are not surprising at all. I would suggest the authors fine-tune a generation model on the 1000 real examples and see whether the generation model can do "extrapolation", which I think is a very important factor in making the method shine.

3. There is no clear guidance on when we should use data augmentation training and when using the pretraining strategy with the generated data. The current study is somehow empirical and the audience cannot get a good amount of insights on when to use which techniques. In practice, however, having a principle is very important given that trial-and-error on the huge amount of generated data is usually with high cost. Moreover, Fig 7 implies another uncertainty on how to determine the augmentation probability on a custom dataset. The authors conducted the ablation study only on ADE20K, which is insufficient to draw any conclusion.

4. With all the above being said, I think the authors failed to study a very critical problem -- how to improve the diversity and quality of the generated images so that we can use much less generated samples to improve the performance of image segmentation models? Given what is presented in this paper, it is really hard to capture any idea about what we should do to improve the data-efficiency of the method, and what knowledge the generated images can bring to the image segmentation models.I would highly encourage the authors think about this and make the work more solid.

### Questions
Please see above comments.

### Soundness
3 good

### Presentation
4 excellent

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
This paper presents a data generation method with a diffusion-based model for sementic segmentation. The authors created SegGen, a method that makes image segmenting better. It uses two ways to create training data: MaskSyn and ImgSyn. MaskSyn makes new image pairs to help train the model, while ImgSyn makes new images from existing ones. This makes their models perform even better on popular tests like ADE20K and COCO. For example, they achieved improvements in MIoU of ADE20K from 47.2 to 49.9.

### Strengths
This papers confirmed that SegGen could boost the performance of semantic segmentation by augmenting training datasets with images and masks generated by the fine-tuned SDXL regarding both ADE20K, COCO panatopic and COCO instance segmentation.

The paper is easy to follow and detailed. The expriments are quite comprehensive. Many example images help readers understand.

### Weaknesses
Unfortunately the novelty of the proposed idea is very low. Some works on generating training images for segmantic segmentation with generative models is proposed before. The idea of SegGen is not novel. Regarding MaskSyn and ImgSyn, SDXL-based was fine-tuned with ControlNet. All the components adopted in this paper are existing ones. In this sense, although the reviewer agrees with the effectiveness of the SegGen method, its novelty is not enough for the ICLR paper. The reviewer guesses that large parts of the performancs improvement comes from high-quality diffusion-based image generation model, SDXL. Since SDXL can generate realistic images which are hard to discriminate as fake images, the peformance must be much improved.

### Questions
What if the older SD model like V1 or other less-quality image generation models was used ? The reviewer would like to know the extent to which developments in image generation models have contributed to the success of this method.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an interesting approach to generating segmentation datasets via Text2Mask and Mask2Image.
The main contribution is the introduction and the design of Text2Mask. It's novel and effective in improving the conventional segmentation model's performance. I think this data-centric viewpoint is valuable in this era of large models.

### Strengths
+ Text2Mask is effective. It gives us a critical insight into the diversity of mask annotation. It brings good knowledge improvement.
+ Color2SegmentationMask is simple yet effective. Before I read it, I was thinking about how to convert a continuous color map to a discrete segmentation mask. Nearest matching is a good way to solve it.

### Weaknesses
- SegGen is trained on paired segmentation datasets based diffusion model. This means diffusion prior is used in the model w/ SegGen. For a fair comparison, other models considered diffusion prior should be compared. For example, the UNet of the diffusion model, as a segmentation model with the same training setting, can be used for comparison. It's better to see this result.
- The related works of data generation in other domains are absent. For example, Scalable Multi-Temporal Remote Sensing Change Data Generation via Simulating Stochastic Change Process (ICCV'23) is highly related to the topic of data generation. Authors can discuss it in the related work for more broader impacts.

Minors:
A2. the second should be  Projection from Color Maps to Segmentation Masks.

### Questions
N/A

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This proposes SegGen, a highly-effective training data generation method for image segmentation, including two data generation strategies: MaskSyn and ImgSyn. Experiments show the synthetic data can be used for improving segmentation performance.

### Strengths
- The proposed method is resonable and easy to understand.
- The paper writing is good.
- The proposed method has improvements on multiple datasets.

### Weaknesses
- Two different training strategies, including synthetic pre-training and synthetic augmentation, seems not giving consistent improvement on different tasks. Synthetic augmentation seems giving performance drop on COCO dataset (i.e., 51.3 vs 52.0). It is not clear why sythetic augmentation is not good for training.
- It is better to compare synethic augmentation with the original data augmentation strategies.
- It is better to give the details of real data and synthetic data used in the proposed methods, which can help readers to understand the details.
- It is better to give the impact of different number of synthetic data in two different modules MaskSyn and ImgSyn.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
