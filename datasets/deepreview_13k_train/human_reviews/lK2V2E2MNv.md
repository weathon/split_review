# Bridging Vision and Language Spaces with Assignment Prediction

- Decision: Accept
- Scores: 8, 5, 6, 5, 5

## Abstract
This paper introduces \method, a novel approach that bridges pretrained vision models and large language models (LLMs) to make frozen LLMs understand the visual world.
    VLAP transforms the embedding space of pretrained vision models into the LLMs' word embedding space using a single linear layer for efficient and general-purpose visual and language understanding.
    Specifically, we harness well-established word embeddings to bridge two modality embedding spaces.
    The visual and text representations are simultaneously assigned to a set of word embeddings within pretrained LLMs by formulating the assigning procedure as an optimal transport problem.
    We predict the assignment of one modality from the representation of another modality data, enforcing consistent assignments for paired multimodal data.
    This allows vision and language representations to contain the same information, grounding the frozen LLMs' word embedding space in visual data.
    Moreover, a robust semantic taxonomy of LLMs can be preserved with visual data since the LLMs interpret and reason linguistic information from correlations between word embeddings.
    Experimental results show that \method achieves substantial improvements over the previous linear transformation-based approaches across a range of vision-language tasks, including image captioning, visual question answering, and cross-modal retrieval.
    We also demonstrate the learned visual representations hold a semantic taxonomy of LLMs, making visual semantic arithmetic possible.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to align the LLMs (encoder/decoder or just decoder) with image encoders such that the LLMs can comprehend visual input better. It further restricts the design space to freeze the original LLM and visual encoder, just relying on a cheap learned linear transformation. To adapt such a transformation, the paper presents two learning objectives -- assignment prediction and image captioning. Empirical results are presented on 3 different tasks -- image captioning, VQA and cross-modal retrieval (I2T, T2I).

### Strengths
* The problem is well motivated with wide applications.

* The paper is mostly well written and explained.

* The empirical results show a big delta which demonstrates the effectiveness of the approach. The studies are also conducted on wide range of problem settings.

### Weaknesses
 * The motivation for restricting the learned parameter space to just linear layers is unclear -- it would have been more interesting to see more analysis around different learned parameter space including non-linear layers.

### Questions
-- Can the authors show ablation studies for the L_map and L_cap objectives to develop better understanding of each component?

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
The paper proposed to bridge the vision and language modalities by predicting the assignment between LLM word embeddings and those two modalities. Specifically, the optimal transport is employed to decide the assignment between LLM word embeddings and image/caption contextualized embeddings, and then the model is required to predict the assignment of one modality from the other modality. Experiments are conducted on multiple tasks/datasets to prove the effectiveness of the proposed method.

### Strengths
1. Demanding one modality's representation to predict the assignment between the other modality and common feature space (LLM word embedding) is an interesting idea to bridge two modalities. 
2. Evaluations on different tasks show a better performance than previous work.

### Weaknesses
1. Comprehensive ablation of w/ and wo/ assignment prediction on the same vision/language backbones is missing. 
2. Comparison with other baselines that are designed for alignment is missing. For example, contrastive alignment in ALBEF, BLIP, and the first-stage alignment by BLIP2 which includes image-text matching, and image-grounded text generation.
3. In experiments, the pre-training data is CC3M which is too small in terms of scale. Whether this method can be generalized to larger scale is not validated.
4. In Tab1,2,3, when compared with previous works, the vision/language backbone is always different. I wonder if using the same backbones as previous works, will the proposed method still outperform them?

### Questions
1. Does the LLM word embedding have to be from the same LLM as used in language encoding?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces VLAP bridges vision encoders and language models through assignment prediction and the use of word embeddings to map visual representations into language space. 
An optimal transport-based training objective is proposed to enforce the consistency of word assignments for paired multimodal data. This allows frozen LLMs to ground their word embedding space in visual data and use their robust semantic taxonomy visually. 
The experiments demonstrate that VLAP outperforms the linear transformation-based approaches in a variety of vision-language tasks, such as image captioning, visual question answering, and cross-modal retrieval.
It also shows that the visual representations that have been acquired contain a semantic taxonomy of LLMs, thus making it possible to do visual semantic arithmetic.

### Strengths
The paper is well-written and easy to follow.
The work proposed a straightforward way of learning the linear projection layer for visual modality to learn multimodal representation, which accommodates the LLM generation.
The visualization shows an impressive semantic arithmetic ability to combine multimodality understanding in LLM generation.

### Weaknesses
(1) The main concern of this work is the methodology is relatively incremental without new concepts or findings.
Concept-wise and architecture-wise, it is similar to Asano et al. (2020) Selavi, which performs optimal transport across modalities with similar pipelines. Mathematics using the Sinkhorn clustering Swav as Caron et al. (2020).
(2) The main difference lies in 3 parts: word embedding as fixed center space, different distribution assumptions (polytope), and LLM application.
The first two are the most interesting part, which will be different from previous Sinkhorn-based work.
However, there is no ablation study on these two components, which leads the readers to question whether borrowing existing Selavi and Swav will also work.
(3) Also, there is no ablation on different objectives, such as existing next-word prediction on learning visual projection on LLM.

### Questions
Either additional ablation, justification, or additional baseline can elaborate the concern in the weakness (2).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In vision-language modeling, a significant challenge persists: bridging the modality gap between pretrained vision and language models. This gap arises primarily due to the models' pretraining exclusively on unimodal data, leading to inconsistencies in their embedding spaces. Motivated by this limitation and the computational costs of previous methods, this work introduces VLAP, a novel linear transformation-based approach that employs assignment prediction to connect vision encoders and large language models (LLMs). By harnessing the established word embeddings of LLMs and introducing an optimal transport-based assignment prediction objective, VLAP maps visual data representations to LLM's word embeddings, aiming for consistent modality representation. This not only results in visual data representations with the semantic richness of LLMs but also surpasses prior methods in computational and memory efficiency across various vision-language tasks.

### Strengths
1. The limitations from SOA mentioned in the paper exist, and the motivation is valid.
2. Resolving the modality gap problem with the cross-modal assignment prediction using word embeddings of LLMs is a better solution than previous methods.

### Weaknesses
1.  A better alignment (reducing the gap) in multi-modality is the essential contribution of this work. However, it lacks studies or results, apart from the overall performance, to validate that the gap reduction is achieved by the current predicted assignments rather than the linear layers from previous works. Specifically, the paper does not provide a direct quantitative measure of the modality gap, such as the distance between the means of the visual and text embeddings, before and after the proposed alignment. Furthermore, it's unclear whether the improved performance is due to the assignment prediction objective itself, or simply the addition of parameters through the linear transformation. A comparison against a baseline using only linear layers without the optimal transport assignment would be crucial to isolate the contribution of the proposed method.
2. The authors mentioned, ``Mapping visual data to LLM’s word embeddings results in learned visual representations that hold a semantic taxonomy of LLMs.'' However, there's a lack of quantitative/qualitative results to validate that this allows visual representations to inherit a semantic taxonomy of LLMs. For instance, the paper does not demonstrate that the learned visual embeddings exhibit similar semantic relationships as the LLM's word embeddings. Experiments showing that visual analogies can be solved using vector arithmetic on the learned visual embeddings would be a strong validation of this claim. Without such experiments, the claim remains unsubstantiated.
3. The final objectives are influenced by the assignment prediction loss and captioning loss. However, there's a lack of study on these hyperparameters. Also, which part contributes more to the learning remains a question. The paper does not include an ablation study to determine the sensitivity of the model's performance to the weights assigned to the captioning and assignment prediction losses. It is also unclear how the choice of these weights affects the modality gap reduction, which is the main contribution of this work. Furthermore, the paper does not explore the impact of different assignment prediction loss functions or hyperparameter settings, which could significantly affect the performance.
4. For the probability that the corresponding modality data belongs to each word, $P_{nk}$, what does $P_{nk}^{v}$ in the visual modality signify? Does this ``word'' refer to the single word token in the class label of that visual region? The paper lacks clarity on the exact meaning of $P_{nk}^{v}$. It is not clear whether the 'word' refers to a single word token in the class label of a visual region, or if it represents something else entirely. A formal definition and explanation of how this probability is calculated and interpreted are necessary.
5. There's a lack of formal definitions for the terms/operations appearing in equations, i.e., $Tr(\cdot)$, $[prefix]$. The paper uses mathematical notations without proper definitions. For example, the trace operator $Tr(\cdot)$ is used without a clear definition, and the meaning of the prefix notation $[prefix]$ is not explained. This lack of clarity makes it difficult to understand the equations and replicate the method.

### Questions
Please also refer to the previous section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method to align the visual representations of pretrained visual encoders into the input space of pretrained language models, using a linear projection layer. The linear layer is the only trainable part in the system, which is supervised by two losses: (a) assignment consistency - the visual features and text features are assigned to the word, and a similarity loss between the assignment results is applied (b) an image captioning objective. Using this method, experiments are done on 3 tasks, including image captioning, VQA, image-text retrieval to show that the method outperforms existing methods. Different variations of visual and text models are studied in the experiments. Additionally, some qualitative visual semantic arithmetic results are provided.

### Strengths
1. The method is simple and clear - train a linear layer with two losses including the newly proposed assignment prediction loss. 
2. Intensive experiments are provided on 3 tasks using different visual backbones (CLIP, BeiT) and text backbones (OPT-1.3B and T5-base), where results consistently outperforms existing methods.
3. The paper is well-written and easy to follow.

### Weaknesses
My major concern is (a) the lack of ablations and feature space visualizations to show the effectiveness of the proposed loss and (b) the contribution over existing works like MAGMA is not enough.
1. The paper is an extension of MAGMA (Merullo et. al. Linearly mapping from image to text space. In ICLR, 2023.). While MAGMA is discussed in the paper, the difference is that this paper with MAGMA is the proposed assignment prediction loss. However, the effectiveness of the proposed loss is not shown clearly in the paper.
2. No ablation results are provided to show the effectiveness of the proposed loss - this is related to weakness-1. Since the major contribution lies in this loss, an ablation to show the contribution of this loss in the final results is very critical.
3. The finding that a linear layer can transform visual representations into language models is not surprising, given existing works LLaVA (“Visual Instruction Tuning”, as in its first training stage), which is not discussed in this paper, and MAGMA as discussed. Therefore, the contribution of this work is weakened.
4. The authors motivate the work by criticizing the “distance-preserving nature of the linear layer”. However, the proposed method is still a linear layer, which doesn’t solve this problem. While Fig-4 provides several examples to show the visual semantic arithmetic, a visualization of feature space would be preferred to show the effects of the assignment loss
5. The paper would be easier to read if the method names (abbreviations) in the results tables come with citations next to them, or are described in texts to show which is which.

### Questions
1. Could abalations with and without the assignment loss be provided to show its effectiveness?
2. Could visualizations (e.g. t-SNE) over the feature space with and without the assignment loss be provided, to show its effects in aligning the features?
3. The difference/contribution over LLaVA or MAGMA can be more clearly discussed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
