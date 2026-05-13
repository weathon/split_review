# IS SYNTHETIC DATA USEFUL FOR TRANSFER LEARNING? AN INVESTIGATION INTO DATA GENERATION, VOLUME, AND UTILIZATION

- Decision: Reject
- Scores: 6, 8, 6, 5

## Abstract
Synthetic image data generation represents a promising avenue for training deep learning models, particularly in the realm of transfer learning, where obtaining real images within a specific domain can be prohibitively expensive due to privacy and intellectual property considerations. 
This work delves into the generation and utilization of synthetic images derived from text-to-image generative models in facilitating transfer learning paradigms. Despite the high visual fidelity of the generated images, we observe that their naive incorporation into existing real-image datasets does not consistently enhance model performance due to the inherent distribution gap between synthetic and real images.
To address this issue, we introduce a novel two-stage framework called bridged transfer, which initially employs synthetic images for fine-tuning a pre-trained model to improve its transferability and subsequently uses real data for rapid adaptation. Alongside, We propose dataset style inversion strategy to improve the stylistic alignment between synthetic and real images. 
Our proposed methods are evaluated across 10 different datasets and 5 distinct models, demonstrating consistent improvements, with up to 30\% accuracy increase on classification tasks. Intriguingly, we note that the enhancements were not yet saturated, indicating that the benefits may further increase with an expanded volume of synthetic data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach "Bridged Transfer" to improve transfer learning in computer vision by augmenting the dataset using text-to-image generative models. The paper introduces a two stage approach for transfer learning - 1) creating a synthetic dataset for target task using text-to-image generative models 2) training the backbone network using this synthetic dataset followed by reinitializing the classifier weights in order to finally train the classifier via target real dataset. The paper shows using naive mixing of real and synthetic data fails to improve transfer learning. The paper also proposes to reduce the distribution gap between the generated dataset and real target dataset using dataset style inversion technique that stylizes and aligns the generated dataset with the real target dataset. The paper empirically shows improvement of this transfer learning algorithm for multiple target classification tasks.

### Strengths
The paper explores a transfer learning framework that augments the target datasets with generated datasets derived from text-to-image models. The proposed approach “Bridged Transfer” achieves improvement on various image classification tasks (~ 1%- 6%) along with few-shot classification tasks. The paper provides detailed ablation experiments to analyze the various components of Bridged transfer algorithm. Ablation experiments regarding the size of synthetic dataset sheds light on the benefit of utilizing this synthetic dataset (for eg higher volume of synthetic datasets leads to better performance). The paper is well-written and easy to follow. The paper provides code for reproducibility.

### Weaknesses
It would be helpful for the reader to get a better understanding of the following:

1. It would interesting to have the approach proposed in paper “IS SYNTHETIC DATA FROM GENERATIVE MODELS READY FOR IMAGE RECOGNITION?” as a baseline (let’s say this baseline as Transfer1).
Specifically, it would be interesting to see the following:
    1. Performance of Transfer1 on the same setting (i.e. having same generative text2image model, same evaluation datasets and using the proposed approaches of dataset filtering RF, RG to close the domain gap) 
    2. Performance of Bridged transfer on pre-trained CLIP models and then comparison with Transfer1 on the same proposed evaluation setting introduced by Transfer1.
    3. The idea of the above 2 suggestions is to glean out what additional information we can learn on top of the findings discovered by Transfer1 approach.
    4. Also, it might be helpful for the reader, if there was a subsection/paragraph that describes the difference between Bridged transfer and Transfer1. For example Bridged transfer uses Dataset style inversion to reduce the domain gap whereas Transfer1 leans on filtering approaches to create a higher quality dataset.
2.  It might be helpful to see some qualitative results on the benefits of data style inversion (DSI). It can visually show that the domain gap of synthetic datasets with target dataset decreases (for e.g. comparison between with and without DSI module for the same text prompt in the context of some target datasets)
3. It might improve the readability of the paper if Bridged Transfer+FC Reinit & mixup is also included in the figure 2.

### Questions
It would be helpful if the paper can answer the following questions:
1. How much training time/wall-clock time and memory resources does it take for dataset style inversion (DSI) for each dataset to optimize the S* token? For e.g. it’s mentioned that it takes 20k training iterations for Aircraft dataset.
2. Are there any qualitative reasons that for datasets like DTD and Pets, the improvement is kind of limited ? Does the synthetic dataset has higher domain gap or is this a fine grained task for which text-to-image models can’t generate enough informative samples. Also, it would be interesting to see the impact of synthetic data volume increase for these classes similar to Fig 5(a).
3. Is Bridged Transfer++ equal to “Bridged Transfer + FC Reinit & mixup” or “Bridged Transfer + FC Reinit & mixup + DSI” ? In table 3, does Single Template correspond to “Bridged Transfer + FC Reinit & mixup” ? If yes, why are the number for DTD not matching up between Table 2  (72.3 +- 0.3) and Table 3 (71.5+-0.4) while the numbers does match for rest of the dataset like Aircraft, Cars, Foods and SUN397 ?
4. In table 3, what does Single Template correspond to (which Bridged Transfer version and what’s the network architecture)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Synthetic image data is quite important for model training/fine-tuning/transfer learning under a series of practical problems such as data shortage, privacy, IP considerations, etc. This work delves into the generation and utilization of synthetic images derived from text-to-image generative models in facilitating transfer learning paradigms. This work observed that, despite the high visual fidelity of the generated images, their naive incorporation into existing real-image datasets does not consistently enhance model performance due to the inherent distribution gap between synthetic and real images. To address this issue, this paper introduced a novel two-stage framework called bridged transfer, which initially employs synthetic images for fine-tuning a pre-trained model to improve its transferability and subsequently uses real data for rapid adaptation. Alongside, they proposed a dataset style inversion strategy to improve the stylistic alignment between synthetic and real images. Empirical evaluation across 10 different datasets and 5 distinct models demonstrates their consistent improvements.

### Strengths
- Novel observation: this paper firstly observed that the naive incorporation of synthesized images into existing real-image datasets does not consistently enhance model performance due to the inherent distribution gap between synthetic and real images by examining three key facets—data utilization, data volume, and data generation control—across multiple downstream datasets. This observation and all the listed key takeaways are very inspiring for the community.
- Effective framework: To address this issue, this paper then introduced a novel two-stage framework called bridged transfer, which initially employs synthetic images for fine-tuning a pre-trained model to improve its transferability and subsequently uses real data for rapid adaptation. 
- Effective strategy to further enhance performance: this paper further proposed dataset style inversion strategy to improve the stylistic alignment between synthetic and real images. 
- Extensive and solid experiments: this paper evaluated across 10 different datasets and 5 distinct models, demonstrating consistent improvements.

### Weaknesses
 - The high-quality synthetic images can always bring multi-fold benefits (cost reduction on real data collection, data shortage, privacy, IP, etc), it would be beneficial for understanding this work’s importance by clearly explaining or numerically analyze how this work can relate to these benefits.
- More discussion is expected to better understand the scope and possibility of observed phenomenon, proposed framework, and strategy. For example, beyond the transfer learning paradigms, will this observation also hold in other learning paradigms? Beyond text-to-image generative models, will the idea of bridged transfer also work?

### Questions
1. Beyond the transfer learning paradigms, will this observation also hold in other learning paradigms?
2. Beyond text-to-image generative models, will the idea of bridged transfer also work?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores the usability of a text-to-image diffusion model (Stable Diffusion) for generating synthetic images to improve transfer learning from ImageNet to different downstream datasets. Different factors of the transfer are compared, for example comparing mixing synthetic images with the downstream data compared to first fine-tuning on synthetic images followed by fine-tuning on the downstream data (bridged transfer). Experiments also show how using mixup in the fine-tuning on synthetic images improves performance, as well as reinitializing the final FC layers in the model when fine-tuning on the downstream data. For the data generation, a variant of textual inversion is explored, where the style of the entire dataset is inverted and can be used to guide the generation of the synthetic dataset. 

Experiments on 10 different downstream datasets show that synthetic data adds most value in the bridged transfer with mixup and reinit, and that style inversion is also valuable. Furthermore, different sizes of synthetic dataset is tested, showing distinct improvements with size in the tested regime of dataset sizes, and also for few-shot learning. Experiments are performed using a ResNet-18, but there are also some experiments validating the performance with ResNet-50 and ViTs.

### Strengths
+ Promising results for synthetic training data in transfer learning
+ Comprehensive experiments on multiple datasets

More details in questions/comments below.

### Weaknesses
 - Some more baseline results would be valuable
- There are no comparison of bridged transfer vs. mixing when style inversion is performed

More details in questions/comments below.

### Questions
* The main body of experiments (for example when comparing transfer learning strategies), are performed with only text prompts as conditioning for generating synthetic data. As this is expected to generate large domain gaps with the downstream datasets, it is not surprising that the mixing of real and synthetic images performs worst. How would this compare if the style inversion was included, which reduces the domain gap between synthetic and downstream data? Or using some other alignment mechanisms such as textual inversion, dreambooth [1] or diffusion inversion [2].
	[1] Ruiz, N., Li, Y., Jampani, V., Pritch, Y., Rubinstein, M., & Aberman, K. (2023). Dreambooth: Fine tuning text-to-image diffusion models for subject-driven generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 22500-22510).
	[2] Zhou, Y., Sahak, H., & Ba, J. (2023). Training on Thin Air: Improve Image Classification with Generated Data. arXiv preprint arXiv:2305.15316.

* Comparisons are made to vanilla transfer (without synthetic images) and mixing synthetic and downstream data. However, it would be of interest to also add comparisons to: 1) no transfer, training from scratch on downstream data, to show the benefit of transferring, and 2) pre-training on only synthetic data, to demonstrate if there are gains in doing the 2-stage (bridged transfer), or if it's enough to only pre-train on synthetic data.

* There should also be comparisons to vanilla transfer with FC reinit, which is not included in, e.g., Table 2 and Table 6. It seems that this makes a large difference, but it is only tested for the bridged transfer, not for the vanilla transfer.

* It would be of interest to demonstrate examples of the dataset style inversion, to show how this is better aligned with the downstream dataset. Perhaps also some quantification of the distributional difference compared to real data, e.g. by means of FID or such.

* The circle plots in Fig. 2 and Fig. 8 are not very intuitive to interpret. How are these produced? There is a normalization with vanilla transfer, but how are the axes shifted? For example, in Fig. 2 it seems that axes are also scaled to show mixed transfer on the inner ring, except for the Cars dataset. It would be easier to interpret the results on, e.g., bar plots or similar.

* It is a bit unclear what strategy has been used in figures. For example, in Fig. 2 the performance degrades with bridged transfer on DTD and Dogs, so I assume this is not with the bridged transfer++? However, in Fig. 3 and Fig. 9 bridged transfer performs equal or better on all datasets. So, here the method has been changed to the bridged transfer++? Please clarify around this.

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
The paper proposes using a large-scale pretrained generative image model to improve transfer learning. To do so, the method proposes querying for images based on the label to retrieve similar images to those in downstream tasks. Then 1) first fine-tunes a pretrained image model (on Imagenet) and then 2) further fine-tunes it using real images from the downstream task. The paper shows that this technique, called Bridge transfer learning, improves over directly fine-tuning on Imagenet (vanilla transfer) and fine-tuning with a mix of synthetic and real images (mixed transfer). The paper also proposes fine-tuning the diffusion model to make it generate images in the style of a given dataset, which improves performance and does not require per-class finetuning.

### Strengths
- The method is simple and may have practical value when a data source is only accessible through a pretrained generative model.

- The method is tested using fine-grained classification tasks, which may be hard for generally pretrained models to perform well.

- The study in 4.3 about inverting the dataset style is interesting and has practical utility, as it is more efficient than fine-tuning the diffusion model for every class.

### Weaknesses
 - The main issue with the paper is that it is comparing: 

1) **Baseline**: a training procedure that only takes *Imagenet-1k* data (1.3M images) + downstream data
2) **Method Proposed**: a training procedure that takes *Imagenet-1k* + *LAION-5B* (StableDiffusion).

The proposed technique uses Imagenet-1k + LAION-5B (distilled into StableDiffusion), so it should only be compared against methods that use the same or similar amounts of *data* and *compute*. For example, how does a model pretrained on LAION-2/5B (like OpenCLIP, readily available online in [1]) perform when finetuned or even zero-shot? It is unsurprising that a machine learning method that has access to 5B images (with fine-grained labels) performs better than one that only has access to 1.3M images (with 1k discrete annotations).

Because of the above, the paper fails to answer the question of whether it is better to use large-scale image data to first train for *classification* (i.e. OpenCLIP) and then finetune on small data, or use large-scale image data to first train a *generative* image model, which can generate synthetic data to augment the small-data (as proposed). This is an important (and easy to test) question, that the paper does not resolve because of the choice of using a pretrained model on Imagenet-1k and not on the full LAION.

Furthermore, the baseline also uses less overall compute than the method proposed, as training on Imagenet-1k takes an order of magnitude less than training StableDiffusion.

- Section 4.3 (effect of guidance scale) is of moderate interest, since it may depend on the generative model. There are simple studies that are more general and would give more insights into whether it is worth doing transfer learning with generative models. For example, is it better to train with all "Aircraft" images from LAION-X (possibly without fine-grained labels) and then finetune, or to get fine-grained images from StableDiffusion (different types of aircraft models, which may be hard to query for on LAION-X) and then finetune?

- What are the statistics of the data trained on StableDiffusion with respect to the downstream tasks? For example, for the class Aircraft-Boeing 787 or for a specific car model, it may be the case that LAION-X has more than 3k examples. If one cannot generate more than 3k examples (as in Figure 5, because of computational constraints?), why not use the data directly available? Looking at this and pointing out clear examples where one can generate much more quantity/diversity data than that present in LAION-X would be a good insight. For example, is there a specific type of Aircraft model that is hardly present in LAION-X, but one can generate an infinite amount of realistic images for it?

- There may be dataset contamination, which is not discussed, i.e., the test samples of the downstream tasks may be part of LAION-X, while this is not the case for the baseline. Does the model improve performance when prompted with "generate a * with the style of LSUN" without dataset adaptation?

- Visual examples would make the paper stronger. For example, when sampling the different "aircraft", how different are the images from the downstream task? How do these images change when doing dataset Style Inversion?

- Additionally, evaluating on tasks that are speciallized (like medical, satellite imaging...) that may not be as prevalent on LAION-X as "natural" images (vehicles, animals...) would make for a stronger paper and ameliorate some of the concerns expressed in the points above.

### Questions
- What is the percentage of images from synthetic and real on the Mixed transfer experiment?
- In LEEP analysis in Table 1, isn't it expected that a model that has lower train/test accuracy (as seen in Figure1 for imagenet pretrained vs bridged pertaining) performs worse on this metric too? Is the difference in transferability (when tested with this metric) also present when two models compared have the same training loss?
- See weaknesses

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
