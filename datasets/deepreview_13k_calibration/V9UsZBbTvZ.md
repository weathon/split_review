# Masked Mamba: An Efficient Self-Supervised Framework for Pathological Image Classification

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Extracting visual representations is a crucial challenge in the domain of computational histopathology. Considering the powerful strength of deep learning algorithms and the dearth of annotated samples, self-supervised learning presents itself as a compelling strategy to extract effective visual representations from unlabeled histopathology images. Although some self-supervised learning methods have been specifically proposed for histopathology image classification, most of them have certain drawbacks that may affect the functionality or representation capacity. In this work, we propose Masked Mamba, a novel self-supervised visual representation learning method tailored for histopathology images that can adequately extract local-global features. The proposed method consists of two stages: local perception positional encoding (LPPE) and directional Mamba vision backbone (DM). In addition, we use masked autoencoder (MAE) pretraining to unleashing directional Mamba vision backbone's potential. Masked Mamba makes good use of domain-specific knowledge and requires no side information, which means good rationality and versatility. Experimental results demonstrate the effectiveness and robustness of masked Mamba on common histopathology classification tasks. Furthermore, ablation studies prove that the local perception positional encoding and directional Mamba vision backbone in masked Mamba can complement and enhance each other.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors have built an image encoder self-supervised learning training tech for histopathological patches from whole slide images.  The technique uses principles of masked image encodinf (i.e. masked autoencoder) and principle for training recurrent neural networks (i.e. mamba) to build masked mamba.  The authors also built a novel model for subpatch merging called patch ghosting that is incorporated in the the masked mamba training archetecture.  The authors benchmark their technique on several patch level classfication tasks against standard architectures including MAE with favorable performance.  The authors also show that within their architecture patched ghosting outperforms ViT and Swin transformer.

### Strengths
The concept is novel.  We are interested in any and all SSL techniques that improve upon others for feature extraction of downstream tasks. 

The model does show modest improvement on chosen benchmarks relative to MAE. 

The masked mamba approach, relative to ViT and Swin Transformer is also a novel approach that could be explored in more detail.

### Weaknesses
I believe that a some portions  of the text (not the entire paper) was written with an LLM.  It makes the paper read a little hyperbolic with unneeded adjectives and superlatives.  A sentence like "... manifested the most exemplary classification proficiency." is not likely something someone would write.  Although I cannot certain. 

Our experience is that masking strategies have yielded poor results for feature extraction for downstream tasks.  Not benchmarking with more successful techniques like DINO doesn't make sense to me. If authors can show performance relative to DINO that would greatly strengthen paper. 

Generally speaking feature extraction encoders are most useful for allowing whole slide image classification tasks.  Any experiments showing performance on a useful whole slide image task would enhance this work.

Given that the model is not segmenting cells, how can you claim "Therefore, our Patch Ghosting generates feature maps that encourage the model to capture diverse feature representations of similar cells." I don't see experiments that support such a claim.

### Questions
Given that the model is not segmenting cells, how can you claim "Therefore, our Patch Ghosting generates feature maps that encourage the model to capture diverse feature representations of similar cells." I don't see experiments that support such a claim.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors proposed a new, self-supervised framework designed to improve the classification of pathological images. The framework includes a unique Patch Ghosting module that captures local image features effectively, and a MixedMamba Block to enhance the model's understanding of global and long-range dependencies. This proposed design helps overcome issues related to limited high-quality annotated data and variability in sample staining.

### Strengths
The authors proposed a newer feature representation learning method using Mamba.

### Weaknesses
1.	The quality of the paper is poor. The equations do not aid the audience in understanding the work and lack significant details.
2.	The title claims that the method is unsupervised. However, training the classification head still requires labels, making the claim of unsupervised classification inaccurate. The Mamba-based unsupervised autoencoder only extracts feature embeddings. Therefore, the work should be described as unsupervised feature representation learning with a supervised classification method.

### Questions
1. In line 161, “The 1 is transformed…,” what does '1' refer to?
2. In equation 1, what do A, B, and C represent? The authors only provided the dimensions of these matrices but did not explain their significance.
3. The proposed model's accuracy and F1 scores are exceptionally high for the LaC dataset compared to other models. The LaC dataset features are known to be extremely difficult to distinguish. Please address how the proposed method effectively learned the embedding space and extracted features that can be utilized efficiently.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a self supervised model for pathology image tasks that is based on the Mamba model and Masked auto encoder. The propsoed method modifies the convolution operation in Mamba and the patch merging procedure. Additionally it is trained with 75% masked input and learns to reconstruct the input images. The model is evaluated on 4 pathology datasets on image classification tasks and shows improved performance compared to various baselines.

### Strengths
- The paper proposes modifications to the Mamba model to make it more suitable for pathology image analysis. 
- The experimental results show improved performance compared to various baselines.
- The proposed method tries to take advantage of the feature robustness provided by Masked auto encoders to enhance the training of Mamba model.

### Weaknesses
 - Using SSM is listed as a contribution even though it is already an integral part of the Mamba model adapted in the paper.

- Also from the contributions: "By leveraging a blend of deep separable and regular convolutions as alternatives to traditional causal convolutions, our
approach reinvents the extraction and sequentialization of spatial features,". This is an over statement. A combination of separable and regular convolutions have been used in previous models, Inception to name one.

- The intuition behind the patch ghosting operation is not clear. I'm not sure where the name comes from and why it is better than other patch merging operations. Even the ablation studies don't show significant improvement in 3 out of 4 tasks.

- The model proposed even though sounds general is only evaluated and targeted towards pathology image classification tasks. No segmentation of WSI classification, and no other types of medical or natural image datasets.

- Datasets description is lacking:
	- The reference for the dataset TCGA COAD: Couture (2022) is a review paper and not a dataset paper.
	- There is no mention of the datasets tasks, their labels, and class-wise statistics.
	- It is not clear whether there is a data split that is published with the datasets or the authors split the data.
	- If the split was done by the authors, there is no mention of how the splitting performed other than the ratio and there no cross validation evaluation.
	- It is mentioned that the patches are resized to 224 by 224 but the original magnification of the datasets is not mentioned.

- The following statement needs clarification: "the resolution in pathological images is often influenced by staining and sectioning"

- The evaluation does not include more current models that have shown good performance on pathology images, such as pathology foundational models, CTransPath, PLIP,

- The improvement in performance is mostly fractional. It is not clear how signficant are the results.

- In Equation 6, the second line, it is not clear what double arrows mean.

- In line 288, SSD was not mentioned before.

- Typo: line 161: The 1 is transformed into a discrete function
- Typo: eq 11: incorrect sign (1+yn)

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Masked Mamba, an efficient model for pathological image classification. To adapt Mamba for pathological images, it introduce a patch ghosting module to capture multi-scale features and employ masked autoencoders to extract robust feature representations. Experimental results demonstrate that Masked Mamba achieves state-of-the-art performance.

### Strengths
1.	The proposed patch ghosting module effectively enhances locality with multi-scale information, making it highly practical.
2.	Extending Mamba from 1D sequence modeling to 2D image modeling is a valuable and well-motivated approach.

### Weaknesses
1.	The combination of Vision-Mamba and masked autoencoders shows limited novelty, as neither component is original to the authors.
2.	The patch ghosting module should be compared to the commonly used Local Perception Unit described in [1].
3.	Although the paper claims that Masked Mamba is efficient, it lacks a table comparing parameters or FLOPs to substantiate this claim.
4.	This paper resizes all pathological images to 224×224, which fails to convincingly demonstrate that Mamba is applicable to high-resolution pathological images.
5.	The writing and expression could be improved, as the contributions in the abstract and introduction are inconsistent.

### Questions
No question

### Soundness
3

### Presentation
2

### Contribution
2
