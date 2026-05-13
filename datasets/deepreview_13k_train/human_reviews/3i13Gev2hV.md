# Compositional Entailment Learning for Hyperbolic Vision-Language Models

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Image-text representation learning forms a cornerstone in vision-language models, where pairs of images and textual descriptions are contrastively aligned in a shared embedding space. Since visual and textual concepts are naturally hierarchical, recent work has shown that hyperbolic space can serve as a high-potential manifold to learn vision-language representation with strong downstream performance. In this work, for the first time we show how to fully leverage the innate hierarchical nature of hyperbolic embeddings by looking beyond individual image-text pairs. We propose Compositional Entailment Learning for hyperbolic vision-language models. The idea is that an image is not only described by a sentence but is itself a composition of multiple object boxes, each with their own textual description. Such information can be obtained freely by extracting nouns from sentences and using openly available localized grounding models. We show how to hierarchically organize images, image boxes, and their textual descriptions through contrastive and entailment-based objectives. Empirical evaluation on a hyperbolic vision-language model trained with millions of image-text pairs shows that the proposed compositional learning approach outperforms conventional Euclidean CLIP learning, as well as recent hyperbolic alternatives, with better zero-shot and retrieval generalization and clearly stronger hierarchical performance. \textit{Code to be released.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes a novel learning method for training vision-language models. Specifically, the method involves pretraining such models with 2 losses --- hierarchical compositional contrastive and entailment losses. The hierarchical concepts correspond to image boxes and the corresponding text boxes. The experiments are conducted on large scale dataset (GRIT) consisting of 20.5M image-text pairs. In Appendix A, the authors describe an automatic procedure to obtain the text boxes (noun entities in this case) and their corresponding bounding boxes in the images. The paper details empirical results on a variety of tasks including zero-shot image classification, retrieval, object detection and scene understanding.

### Strengths
* The proposed method is simple and elegant and can be easily applied to large scale pretraining of vision-language models. The procedure to automatically generate paired image and text boxes is also relatively straightforward.
* The empirical results show improvement across several tasks which demonstrates the improved representation learning - classification, retrieval, detection and understanding.
* Table 1 results show that CLIP trained on additional image-text boxes doesn't improve the performance. However, training on the same data but with the proposed hierarchical compositional learning losses shows significant improvement in performance. This further demonstrates the effectiveness of the proposed technique.

### Weaknesses
When training CLIP on additional image-text boxes shows no improvement (Table 1), it could be because there is limited new information in such examples (as original image-text pairs are already present in the training data). For a better understanding of this, an experiment such as this might help: split the GRIT dataset into 2 random subsets of 10M each. Then compare the results on the following settings:

[1] CLIP trained on 10M image-text pairs

[2] CLIP trained on 10M image-text pairs + additional image-text boxes

[3] HyCoCLIP trained on 10M image-text pairs + additional image-text boxes

[4] CLIP trained on 20M image-text pairs

The paper presents the comparison of [1] vs [2] vs [3] (but on all 20M image-text pairs) in Table 1 but comparing [3] vs [4] will help answer the above question. It is worth noting that even if the comparison shows similar results, [3] might still be slightly favored since it can be applied on top of any existing large dataset.

### Questions
Can the authors share the results of HyCoCLIP on RedCaps dataset?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a novel approach named HyCoCLIP to vision-language modeling that leverages the hierarchical nature of hyperbolic space to better align visual and textual data. It organizes image and text data as hierarchical compositions, where objects within an image and their corresponding text descriptions are represented at different levels of abstraction in hyperbolic space.The experiments demonstrate that HyCoCLIP achieves significant performance improvements across multiple tasks.

### Strengths
1. This paper is well-organized. The motivation is easy to follow, and the method is easy-to-understand.
2. The proposed HyCoCLIP is novel and effective. It organizes data at multiple abstraction levels, providing an inspiring approach to multi-modal learning.
3. The authors performs exhaustive experiments to show that the effectiveness of HyCoCLIP. It outperforms baselines on general and fine-grained image classification tasks.

### Weaknesses
1. While the paper compare with CLIP and MERU, it should also compare some recently proposed VLMs.
2. The paper should explore how sensitive the model is to the choice of hyperbolic space parameters.

### Questions
Could you please provide more details on the choice of hyperbolic space parameters?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors proposed to incorporate hierarchical pretraining for hyperbolic vision language models and the resulting model Hyperbolic Compositional CLIP (HyCoCLIP). The core idea is to construct object regions (image boxes) and corresponding text phrases (text boxes) to build a multi-layered, compositional hierarchy within the shared hyperbolic embedding space. The HyCoCLIP shows competitive performance in zero-shot classification and retrievals. The author also conducted experiments to show how HyCOCLIP can outperform CLIP and the hyperbolic contrastive model MERU in zero-shot hierarchical classification and scene understanding tasks.

### Strengths
I think this paper is very well written and I find it easy to follow. Overall the idea behind HyCoCLIp is well motivated and I believe the authors have conducted sufficient experiments to empirically demonstrate the proposed method and model’s efficacy. The empirical performance of HyCoCLIP is very strong and to the best of my knowledge, the proposed HyCoCLIP achieved the state-of-results on many of the reported zero-shot tasks from a contrastive-pretrained model.

### Weaknesses
One major concern is the incremental nature of this work. Hyperbolic embeddings for representing hierarchical relationships have been explored in previous models, and this paper primarily builds upon these established ideas. However, the specific contributions of HyCoCLIP, particularly in enhancing hierarchical and scene understanding tasks, offer sufficient merit to make this work valuable to the broader community. The paper could benefit from a more thorough discussion of the novelty of the proposed loss functions in the context of existing hyperbolic contrastive learning methods. While the authors claim to enforce hierarchy through their loss functions, a more detailed analysis of how these losses differ from standard contrastive losses in hyperbolic space, and how they specifically encourage hierarchical structure, would be beneficial. Furthermore, the paper lacks a detailed comparison with other hyperbolic models that also aim to capture hierarchical relationships, making it difficult to assess the true advancement of HyCoCLIP.

### Questions
In Table 1/2, the authors bold the best performance overall across different model backbones. Wouldn’t it be more informative and fair to bold the best performance within each backbone group (e.g., ViT-S/16, ViT-B/16) to allow for a clearer comparison of HyCoCLIP’s performance relative to baselines on similar architectures?

Regarding the choice of batch size, the authors used a batch size of 768 due to memory limitations. Did the authors consider implementing techniques like gradient accumulation to effectively simulate a larger batch size? This could provide further insights into how batch size impacts model performance, especially since batch size has been shown to affect contrastive learning tasks significantly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the novel Compositional Entailment Learning framework to train VLMs, by using as supervision the hierarchical relations between images, captions, and constituent nouns and their bounding boxes. Their results show that this outperforms standard CLIP and the hyperbolic CLIP variant MERU on both standard multimodal and hierarchical benchmarks. This is supported by qualitative results illustrating the learned hierarchical semantics of the learned space.

### Strengths
The central idea is clever and novel – utilizing the hierarchical nature of nouns mentioned in image captions as supervision for a hyperbolic model. The exposition is clear and concepts are well-illustrated. The quantitative experiments are extensive and overall convincing.

### Weaknesses
Qualitative results (Sec 4, Supp 8) are fairly limited. In particular, it is missing a qualitative comparison to existing models (CLIP, MERU) to illustrate whether HyCoCLIP’s embedding space represents hierarchies in a more qualitatively satisfying way.

While a comparison to CLIP trained from scratch is provided, recent work has found pretrained foundation VLMs to represent hierarchies in Euclidean space [1]. It would be useful to compare to such results to understand whether HyCoCLIP trained from scratch is competitive with such models.

Could the use of objects as supervision bias the model towards nouns and concrete concepts, possibly at the expense of attributes, dynamic actions (verbs), etc.?

### Questions
Could the use of objects as supervision bias the model towards nouns and concrete concepts, possibly at the expense of attributes, dynamic actions (verbs), etc.?

Some details that are unclear from Supp. A: How were abstract nouns filtered? Are the nouns that can be grounded open-vocabulary (not limited to a fixed list)? How accurate is the GLIP-based grounding procedure?

### Soundness
3

### Presentation
4

### Contribution
3
