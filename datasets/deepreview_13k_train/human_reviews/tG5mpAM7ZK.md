# Extending to New Domains without Visual and Textual Oracles

- Decision: Reject
- Scores: 8, 5, 3

## Abstract
To avoid the high cost of collecting visual data from all test domains in domain adaption task, recent work takes advantage of the pre-trained large-scale vision language models and augment training data with only text descriptions (e.g.,“a photo/painting/sketch...”) of each test domain. However, in many real-world ap- plications, such text information of test domains is not always available in ad- vance. Moreover, even if we can verbalize all test domains, it is laborious for existing work (Dunlap et al., 2023) to train a different augmentation network for each possible unseen domain. To overcome these challenges, we benefit from the multimodal embedding space of a pre-trained vision-language model and propose to acquire training-free and domain-invariant augmentations with text descrip- tions of arbitrary crafted unseen domains, which not necessarily match test do- mains. Beyond achieving state-of-the-art results, compared with existing works that require trainable augmentation networks, our approach is also notably more time-efficient, and exhibits a more solid theoretical support.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel approach for domain adaptation with the idea of the augment of data with only text descriptions. It utilizes a pre-trained vision-language model to acquire domain-invariant augmentations using text descriptions of arbitrary, unseen domains, even if they don't match the test domains. This method outperforms existing approaches, offering greater efficiency and stronger theoretical support while eliminating the need for predefined text descriptions of all test domains.

### Strengths
Good Quality:
The submission is technically sound, in my opinion, and the advantages and limitations of this work are carefully and honestly discussed.

Good Clarity:
The submission is written with clear definitions and formulas. The organization is well-designed.

Good Motivation:
The method is well-motivated, given the recent conclusions from Liang et al. and Zhang et al.

Solid Solution:
By observing the beneficial properties of the multimodal embedding space, the authors successfully extend the findings in Liang et al. and Zhang et al.  to address the domain generalization problem, providing a new method from a novel perspective.

### Weaknesses
1.	The authors might consider evaluating their proposed method on a larger dataset, such as WILDS, which provides extensive and diverse real-world data from various domains. The current evaluation, while thorough on the datasets used, would benefit from demonstrating robustness on more complex and varied domain shifts found in real-world scenarios. Specifically, the limited number of datasets used might not fully reveal the limitations of the proposed approach when faced with more intricate domain variations, such as those involving significant changes in background, lighting conditions, or object viewpoints.

2.	Could you please explain the meaning of "1x" for Time in several tables? The notation is unclear and it would be beneficial to have a more explicit definition of what this represents, as it is not immediately obvious what the baseline for this relative time measurement is. Furthermore, it would be helpful to understand if this time refers to wall-clock time or computational time, as this distinction can impact the practical implications of the method.

3.	While the authors have successfully developed a method based on the findings of Liang et al. and Zhang et al., the paper itself lacks a sufficient explanation of the embedding space in the context of domain generalization. Although this might not be a critical flaw in the paper, providing theoretical or empirical analyses in this regard could enhance its overall impact and inspiration. Specifically, a deeper dive into the properties of the CLIP embedding space that enable this domain generalization would be valuable. For example, discussing the geometry of the embedding space, the distribution of embeddings across different domains, and how the proposed method leverages these characteristics would strengthen the theoretical foundation of the paper.

### Questions
As the authors mentioned in Figure 2 (right), there might be cases where equation 4 is not satisfied. I am curious if the CLIP features always meet the conditions of equation 4. Could the authors conduct empirical analysis to offer an intuitive understanding of when it fails?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the domain generalization without using the image nor text description of the target domain. The authors propose to use the property of modality gap of CLIP model. Specifically, they augment the embeddings of images in the source domain to the domain-invariant embedding without training. After augmentation, they train the linear probe on the mixture of domain-invariant embedding and original embedding. In inference, they apply the trained linear probe to the embedding of the target image. In the experiment, the authors test their proposed method with and without the text description of the target domain.

### Strengths
1. The paper adopts the recent finding of the modality gap in the CLIP embedding space and propose a training-free augmentation which is training-efficient.
2. The paper considers a practical setting where the text description is not available for the target domain.

### Weaknesses
1. In **Training-free Augmentation with Modality Direction** (on page 5) the proof of z exists in the CLIP's normalized embedding space is trivial to get.

2. In Table 1 and Table 2, the performance of the proposed method on CUB and DomainNet does not stand out from the baselines with a significant margin. 

3. Ablation Studies are limited.

### Questions
1. Why can the linear probe trained on the domain-invariant feature and original feature be directly applied to the target feature (without any augmentation)?

2. In Stage 2, why not only train the classifier only on the augmented embeddings?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce an approach aimed at generalizing from a single domain, represented by natural object images, to previously unseen domains, including objects presented as paintings and sketches. Their method involves shifting visual embeddings using relative differences of textual embeddings from the original domain (a picture of a cat) to potential unseen test domains (a painting of a cat), thereby enabling feature-space augmentations.

The authors conduct evaluations of their proposal on datasets such as CUB and DomainNet. The results show minor improvements over the competitive LADS baseline. This work addresses an important challenge in domain adaptation by expanding the model's capabilities to novel domains, demonstrating its potential in real-world scenarios involving diverse visual data representations.


------------------------- After Rebuttal ----------------------------------------------------------------------------------------------

I thank the authors for their kind, lengthy, well written rebuttal. I carefully went through all the other reviews and post rebuttal text. However, it fails to upgrade my score upwards for three reasons:  

- The authors acknowledge the similarity to CGAP, with the apparent difference being training-based vs. training-free. This opens up a whole new set of baselines to compare against, for training-free CLIP. 
- However, I still see no update or discussion of this important paper. 
- Lack of significant improvement over LADS is still a concern to consider.

### Strengths
S1:
The paper is generally well-written and easy to follow, although there are instances where it may overly emphasize LADS rather than the paper's ultimate goal. Despite this, it remains a good read overall, providing a clear presentation of the research.

S2:
The paper takes on a highly challenging task: single-domain generalization. In the context of this demanding objective, CLIP has established itself as a robust tool, and this paper contributes to this ongoing trend.

### Weaknesses
W1 Method:

A significant concern arises regarding the similarity between this paper and CLIP the GAP (CGAP) [1], which the authors fail to acknowledge or cite. Both papers share fundamental observations: that various domains of the same object differ by constant vectors. Additionally, they both tackle the challenge of single-domain generalization. The methodological resemblance is evident: CGAP performs semantic augmentations by computing relative differences in original and target test domains of text embeddings, using these as pseudo targets to generate visual features of the target domains. The evaluation contexts differ slightly: CGAP explores weather attributes, while this paper focuses on DomainNet/CUB. Furthermore, both papers demonstrate that precise domain names are unnecessary for strong performance on unseen domains, as illustrated by CGAP's "random" augmentations in Table 7.

In light of these similarities, it appears that this paper functions as an application on CUB and DomainNet rather than a substantially novel contribution.

W2 Result:

A noteworthy concern arises from the marginal improvement over the most competitive baseline, LADS, as evidenced by Table 1 (0.78% improvement on CUB, 0.92% improvement on DomainNet). This minor improvement raises doubts about the merit and significance of the proposed method, especially considering the striking similarities to existing work, such as CGAP. The paper's originality and contribution require further clarification and validation to convincingly demonstrate its value in the domain of single-domain generalization.

Typos:

- [LADS reference]: "Using language to *extend* to unseen domains," International Conference on Learning Representations (ICLR), 2023.

- "Benefiting from the learned multimodal embedding space in pre-trained large-scale vision-language (VL) models (Radford et al., 2021; Jia et al., 2021), *we* achieve..."

### Questions
N/A

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
