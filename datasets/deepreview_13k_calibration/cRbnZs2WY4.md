# SelfClean: A Self-Supervised Data Cleaning Strategy

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 6, 1, 6

## Abstract
Most benchmark datasets for computer vision contain irrelevant images, near duplicates, and label errors.
Consequently, model performance on these benchmarks may not be an accurate estimate of generalization capabilities.
This is a particularly acute concern in computer vision for medicine where datasets are typically small, stakes are high, and annotation processes are expensive and error-prone. 
In this paper we propose SelfClean, a general procedure to clean up image datasets exploiting a latent space learned with self-supervision.
By relying on self-supervised learning, our approach focuses on intrinsic properties of the data and avoids annotation biases.
We formulate dataset cleaning as either a set of ranking problems, which significantly reduce human annotation effort, or a set of scoring problems, which enable fully automated decisions based on score distributions.
We demonstrate that SelfClean achieves state-of-the-art performance in detecting irrelevant images, near duplicates, and label errors within popular computer vision benchmarks,
retrieving both injected synthetic noise and natural contamination.
In addition, we apply our method to multiple image datasets and confirm an improvement in evaluation reliability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a method to curate datasets by finding near duplicates, bad labeled and out of distribution images.
To do so, they first train a self-supervised DINO model on the dataset to filter and then use distance and clustering based methods for each kind of anomaly detection.
They compare their method against multiple baseline both on synthetic and real anomaly detection benchmarks.

### Strengths
- Clear explanation of the method
- Simple method that use the properties of SSL models to capture all factor of variations, which means that they don't require labels
- Lot of ablation studies
- The method seems robust to hyperparameter changes
- Good evaluation setup of a ill posed problem

### Weaknesses
All the methods are based on the notion that distance between images represents meaningful factors of variation. The closer the images are in the latent space, the more similar they should be, both in term of appearance but also semantically.
However, while SSL probably captures most factor of variations (and usually more than with supervised learning), it is still not possible to control the hierarchy in term of distance in the latent space between the factors. Meaning that if an image is a sketch of a dog, it is hard to tell if it will match more a real picture of a dog or a sketch of a cat using self-supervised features.
This means that images from under represented groups or from rare classes will be removed or wrongly flagged as anomaly which is a big issue in medical imaging.

### Questions
1) Could you ablate the weakness I'm talking about, for exemple by looking at the proportion of images removed from the clean version of the dataset wrt. the frequency of their labels, or grouped by multiple metadata such as demographics, device etc. (CheXpert demographics: https://github.com/biomedia-mira/chexploration https://stanfordaimi.azurewebsites.net/datasets/192ada7c-4d43-466e-b8bb-b81992bb80cf)

Optional: 
2) We can see on Table 2 that the gains are higher with kNN than with linear evaluation with a clean train set. This seems to be because kNN eval is directly based on distance, such as your filtering method. Given that zero shot evaluation of CLIP is based on the distance between the text and image encoder, it is possible that your method can enhance zero-shot evals of CLIP model.
Could you test it in a zero-shot setup such as CLIP image/text cosine similarity matching ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of this work introduce a new dataset cleaning strategy. They utilize in-domain self-supervised learning to address challenges associated with human biases/errors, task biases, and issues present in other methods that use supervised learning e.g. semantic collapse. Their primary focus is on eliminating irrelevant examples, near duplicates, and correcting labeling errors. They benchmark their approach on an array of datasets and tasks, showing that their method outperforms previous works, by a large margin in some cases while they also provide valuable insights.

### Strengths
The authors of this paper set out to tackle the prominent, and always relevant, problem of dataset cleaning. I find myself in agreement with the authors' narrative and intuition about the use of self-supervised features, which I believe address several issues encountered by past methods.  The authors benchmark their approach primarily on medical datasets but they also provide valuable insights on the application of their method to mainstream natural datasets. In general, the paper is well written and easy to go through.

### Weaknesses
My primary reservation concerns the novelty of the cleaning approach. The main contribution is the use of SSL-based models for feature extraction. Beyond this, I struggle to identify other novel aspects. While the authors propose using dataset-specific SSL, the core idea of using self-supervised features for data cleaning is not entirely new. The specific choice of DINO as a baseline, while effective, doesn't introduce a fundamentally novel approach to feature extraction for this task.

While the experiments are detailed, they appear somewhat limited in scope. The authors mainly concentrate on dermatology datasets and their experiments to natural images or other domains seems rather limited. Based on the novelty of the paper I would expect a stronger experimental section. The inclusion of ImageNet, Food-101N, and CelebA is a good start, but the analysis on these datasets lacks the depth seen in the dermatology experiments. A more thorough investigation across diverse datasets would be beneficial.

The first and second contamination strategies, while intuitive and useful, don't seem to address real-world noise. In the context of medical images, irrelevant examples often include images that are out-of-focus, images with doctor’s annotations, or images with parts from an apparatus. They do not contain random ImageNet examples, PowerPoint slides or data from a different medical modality. Similarly for the duplicates, a simple rotation, resizing etc. is a rather a simplification of real-world duplicates. The chosen synthetic noise strategies do not fully capture the complexity of real-world data quality issues.

The impact of dataset cleaning appears to be less significant than anticipated. While there are instances where cleaning the evaluation set boosts performance, there are equally instances where has a negative impact on the results.  Most importantly, when the training set gets cleaned, the performance decreases in 3 out of 5 cases. In the remaining 2 out of 5 cases, the gains in performance are rather small. This is important especially considering real-world applications – dataset cleaning is not only for benchmarking. Only the training set is accessible. The test set remains unknown and probably contains corrupted data.

When k-NN evaluation is used, cleaning the training set seems to help consistently (although marginally in most cases). However, this is rather expected given the nature of k-NN evaluation.  However, in reality we care about the performance of linear classifiers and not k-NN. Most importantly, a fine-tuning step, which is a standard expectation in real-world scenarios, seems to be missing from this analysis.

### Questions
A significant challenge in medical diagnosis is that of intra-observer variability, which complicate thing further when comes to labeling errors. How does one address this complexity when it is nearly impossible to define a ground truth?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes an data label noise detection and removal technique based on self-supervised trained embeddings and three basic heuristics to identify potential outliers, near duplicates with conflicting labels and other labeling errors using agglomerative clustering, pairwise distance comparisons (thresholding) and "intra/extra" class distance ratios. The method is evaluated on 10 different datasets including popular computer vision benchmarks (such as ImageNet, Food101, CelebA) and seven other medical image datasets, mainly through synthetic experiments. The results are compared to some other known methods such as pHash, SSIM, FastDup.

### Strengths
- Investigates label noise detection and removal on ten different images datasets including from both computer vision and medical imaging domains.

### Weaknesses
 - Lack of novelty. The described methods of clustering, distance thresholding and intra/extra class distance ratios in the embedding space trained on the target dataset have been widely known and applied in the space. Combining these approaches is not sufficient for justifying novelty. The core idea of using self-supervised learning (SSL) embeddings for data cleaning, while practically useful, does not represent a significant theoretical advancement. The paper fails to demonstrate a novel algorithmic contribution beyond the application of standard techniques to a new problem.
- Lack of proper evaluation setup. The experiments are primarily performed using the synthetic label noise which is also devised by the paper. The reliance on synthetic noise makes it difficult to assess the method's performance in real-world scenarios where noise characteristics are often complex and unpredictable. The paper does not adequately address the potential biases introduced by the synthetic noise generation process. The evaluation lacks sufficient analysis of the method's robustness to different types of real-world noise.
- Lack of proper baselines. The paper does not compare against a sufficient range of state-of-the-art methods for label noise detection and removal. The chosen baselines do not adequately represent the current landscape of techniques, particularly those that leverage similar embedding-based approaches. Furthermore, the paper does not provide a clear rationale for the selection of the specific baselines used, and why other relevant methods were excluded.
- The paper is hard to follow. The presentation of the proposed method is dense and lacks clarity, making it difficult to understand the individual steps and their interdependencies. The paper would benefit from a more structured and accessible explanation of the methodology, including clear definitions of the key concepts and parameters.

### Questions
- Dataset size and data distribution would largely impact the hyper-parameters (alpha, q etc) used for identifying near duplicates, outliers etc. It is not clear how well the proposed heuristics would generalize for other datasets or other applied settings. 
- Page 9: "Recommended use" section. The paper's proposal is to use SelfClean to identify the errors and fix them using human in the loop. However, the process would still introduce sampling bias originating from SelfClean. This should be noted. 
- What was the rationale for choosing the current baselines? Below is the suggested baseline which uses pre-trained embeddings and vector similarity to identify label noise using Markov Random Fields (most similar to the proposed approach) 
Sharma et al, "NoiseRank: Unsupervised Label Noise Reduction with Dependence Models", ECCV, 2020
-  The paper is way too dense and hard to follow. Proposed novelties also needs to be clearly noted in the abstract.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of cleaning up large datasets used for training and evaluation. The paper considers three kinds of imperfections: (1) samples which are irrelevant, (2) samples which are near duplicates of other samples, and (3) samples with incorrect labels. The proposed approach is to use self-supervised learning methods to learn an embedding of the data and then compute scores for each of the imperfection categories above based on these embeddings. Then, samples are deemed to be flawed based on either a threshold-based criterion or human review. The method is evaluated using datasets with artificially injected flaws, as well as "in the wild" datasets (in which metadata and human review are used as ground truth). 

I liked this paper because of the problem it considers and the ambition and thoroughness of its approach. However, there are some technical issues and some issues with framing. If tweaked to be a bit more thoughtful along a few axes, it could be a great contribution to ICLR. 

I will flag the fact that I don't know the related work well enough to know whether all key baselines are included. On this, I will defer to more knowledgeable reviewers. 

# References (used later)

@article{xiao2020should,
  title={What should not be contrastive in contrastive learning},
  author={Xiao, Tete and Wang, Xiaolong and Efros, Alexei A and Darrell, Trevor},
  journal={arXiv preprint arXiv:2008.05659},
  year={2020}
}

@inproceedings{cole2022does,
  title={When does contrastive visual representation learning work?},
  author={Cole, Elijah and Yang, Xuan and Wilber, Kimberly and Mac Aodha, Oisin and Belongie, Serge},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={14755--14764},
  year={2022}
}

### Strengths
* The paper is generally well written and interesting to read. 
* Very polished - I didn't spot one typo!
* The task under consideration - cleaning up datasets for training and evaluation - is a timely and important topic. 
* The proposed methodology seems reasonable enough - see below for some caveats. 
* The experiments are thorough and thoughtful. 
* The paper includes a limitations section, which is always helpful for the reader. 
* Ample supporting details and examples can be found in the appendix.

### Weaknesses
I have a few technical concerns:
* The paper is built on augmentation-driven SSL methods. The representations learned by these methods are driven by the augmentations they use, which generally need to be chosen in a domain-specific way [xiao2020should]. These seems like a liability for the proposed method, and should be addressed. In practice, how is someone supposed to pick? Furthermore, the paper does not explore the impact of different augmentation strategies on the quality of the learned representations and, consequently, on the performance of the data cleaning task. This is a significant omission, as the choice of augmentations can drastically affect the learned invariances and the resulting embeddings.
* The SSL encoders which are the foundation of this paper are all trained with default or near-default parameters. Given that those parameters were tuned for ImageNet in the original papers, why shouldn't we worry that the encoders in this work are trained to varying levels of quality, confounding the results? The paper lacks a systematic analysis of how the quality of the SSL encoders, measured by their performance on a downstream task or by some other metric, affects the performance of the proposed data cleaning method. This makes it difficult to assess the robustness of the approach.

The paper's goals can seem a bit detached from real use cases, despite being framed in a very practical way. For instance:
* One of the three types of data fault considered in the paper is *near duplicates*. Given that the paper considers many medical use cases, this seems potentially problematic. What about adjacent B-scans in an OCT volume? Or adjacent tissue sections in an H&E block? Or longitudinal X-rays from a patient? All of these should be near-duplicates, but may be quite important. The paper does not provide a clear definition of what constitutes a 'near duplicate' in the context of medical imaging, and it does not discuss how the proposed method can be adapted to handle such cases where near duplicates are expected and informative.
* One of the three types of data fault considered in this paper is *irrelevance*. This seems like a loaded and insufficiently defined term. Isn't relevance in the eye of the beholder? When does it make sense to have a sample that is correctly labeled but "irrelevant" to the classification task at hand? Wouldn't it be obvious from the label that such a sample is irrelevant? The paper needs to provide a more precise definition of 'irrelevance' and justify its inclusion as a type of data fault. The examples provided are not convincing, and it is unclear how the proposed method can distinguish between truly irrelevant samples and those that are simply difficult to classify.
* Adding X-ray images to a dataset of images from a different domain seems like a contrived task of low difficulty. (One could probably tell an X-ray image from a photograph of a skin lesion using classical image processing methods.) It seems like the "real" use case would be more like adding X-ray images of one disease to a dataset consisting of X-ray images from a very different disease. More broadly, it seems like concept granularity is an important missing piece in this work - see e.g. the granularity-depending usefulness of SimCLR features described in [cole2022does]. The paper needs to consider more realistic scenarios for evaluating the proposed method, and it needs to address the issue of concept granularity, as the performance of the method may vary significantly depending on the semantic similarity between the irrelevant samples and the target domain.



### Questions
0. See "weaknesses" section. 
1. Why should we not be concerned about the choice of augmentations underlying the self-supervised learning used in this paper? 
2. Does the synthetic case of adding X-ray images to a dataset of images from a different domain model a realistic use case? 
3. The paper notes that "the batch size cannot be large" for SimCLR - why is this? 
4. Table 1 shows that sometimes SimCLR and DINO lead to very different performance and sometimes they do not. Is there any insight to be had into why this is? 
5. Why shouldn't we worry about the proposed method removing difficult but important images or groups of images, especially in a medical context?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good
