# Rethinking Semantic Few-Shot Image Classification

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
Few-shot learning aims to train models that can be generalized to novel classes
with only a few samples. Recently, a line of works has been proposed to enhance
few-shot learning with semantic information from class names. However, these
works focus on injecting semantic information into existing modules such as visual
prototypes and feature extractors of the standard few-shot learning framework,
which requires complex designs of the fusion mechanism. In this paper, we
propose a novel few-shot learning framework that uses public textual encoders
based on contrastive learning. To address the challenge of alignment between
visual features and textual embeddings obtained from public textual encoders,
we carefully design the textual branch of our framework and introduce a metric
module to generalize the cosine similarity. For better transferability, we let the
metric module adapt to different few-shot tasks and adopt MAML to train the
model via bi-level optimization. Moreover, we conduct extensive experiments on
multiple benchmarks to demonstrate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel few-shot learning framework for image classification that leverages semantic information extracted by a public textual encoder based on contrastive learning. The proposed approach addresses the challenge of alignment between visual features and textual embeddings obtained from public textual encoders and introduces a metric module to generalize the similarity measure. The metric module is designed to be adaptive to different few-shot tasks for better transferability, and MAML is adopted to train the model via bi-level optimization. The paper demonstrates the effectiveness of the proposed method through extensive experiments on multiple benchmarks with different domains. The main contributions of the paper are the proposed few-shot learning framework, the carefully designed textual branch of the framework, the metric module for generalizing the similarity measure, and the demonstration of the effectiveness of the proposed method through extensive experiments.

### Strengths
+ The paper has a clear and well-organized presentation of the proposed method, and the authors provide comprehensive experiments.

+ The proposed method aims to bridge the gap between visual and textual modalities, which is a good direction towards few-shot learning.

+ The visualization (sec. 5.4) looks good.

### Weaknesses
- The paper lacks a comprehensive comparison with other state-of-the-art few-shot learning approaches. While the authors demonstrate the effectiveness of their method, it is difficult to assess its performance relative to methods such as TRIDENT [1], BAVARDAGE [2], and PEMnE-BMS [3]. Although these methods might not directly rely on pre-trained vision-language models, their inclusion would provide a more complete picture of the current state of the field. Moreover, the authors overlook some relevant works that utilize category names for few-shot learning [4], which could offer valuable insights into the initialization of the bridge between visual and textual modalities.

- The bi-level optimization strategy, while innovative, raises questions about its specific implementation. The authors update the metric module in the inner loop and then update all parameters in the outer loop. This approach suggests that the metric module is treated differently during optimization. A more detailed explanation of the rationale behind this strategy is needed. Specifically, why is the metric module, responsible for image-text alignment, updated separately in the inner loop, while other modules, such as the feature extractor, are updated in the outer loop? What are the implications of this separation for the overall learning process?

- The paper introduces a metric module to bridge the gap between visual and textual modalities, adding learnable parameters to facilitate alignment. However, vision-language models are inherently capable of zero-shot inference, suggesting that the initialization of this "bridge" is crucial. The authors should elaborate on whether they considered leveraging category name embedding for initialization, as proposed in [4]. This approach could potentially achieve automatic alignment between the two modalities, simplifying the learning process and potentially improving performance. A discussion of the trade-offs between a learnable metric module and category name initialization would be beneficial.

### Questions
I expect to hear back from the authors regarding the below questions and concerns.

1. Comparison regarding other state-of-the-art few-shot approaches with established results on CUB or Mini-Imagenet.
2. Explanation of the motivation or insights of the training strategy, especially why only the metric module is updated in the inner loop and all parameters are updated in the outer loop.
3. Discussion about the category name initialization and possible comparison or further experiments by adding that strategy to existing approach.

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
This paper is about few shot image classification. It aims at improving it by exploiting semantic information that takes the form of textual embedding obtained using existing textual encoders. As this textual information is not directly aligned with the visual one, the authors propose to align them by metric learning and in particular contrastive learning widely used in self-supervised representation learning. This training procedure follows the metal-learning approach and in particular MAML. Experimental validation and comparison to the state-of-the-art are done on two few shot benchmarks (miniImagenet and tieredImageNet) and the CUB-200-2011 dataset for fine-grained recognition. Their approaches improve the performances on these benchmarks. An ablation study on the metric learning part is provided.

### Strengths
+ The paper tackles an important issue in few-shot learning, i.e. improving existing approaches by injecting additional information and in particular semantic textual information. Indeed, this line of work has been largely studied recently and has shown promising results. 
+ The paper is well-written with clear objectives and motivations.
+ The experimental part implies a comparison with various inductive state-of-the-art approaches and the obtained results show an improvment in terms of performance on different 5 ways x shot settings.
+ The paper also contains a small ablation study on the metric learning part.

### Weaknesses
+ A first concern is about the experimental study which is incomplete from my point of view on several aspects :
  +  First, it is usual to study the dependence on the visual backbone. Only Resnets-12  is used in the paper but other backbones such as visual transformers backbone or recent foundation models could be included. Specifically, incorporating more recent architectures like ViT or Swin Transformers would provide a more comprehensive evaluation of the method's performance across different model types and capacities. This would also help determine if the proposed method is particularly suited to certain architectures or if its benefits are consistent across the board.
  + The influence of the prompting strategy could also be experimented with in more detail. The appendix provides an analysis of the learnable prompt template but it could have been interesting to correlate this prompting strategy to a more formalized definition of the type of semantic information that should be carried. For example, how does the performance vary when using prompts that emphasize different semantic aspects, such as class relationships versus individual class attributes? This could be explored by systematically varying the prompts and analyzing the resulting changes in the learned representations and classification accuracy.
  + Some technical details are missing. In particular, it is well known that contrastive learning is highly dependent on the negative sampling strategy but also on the size of the batch. This information is missing in the paper. Providing details on the batch size used during training and how negative samples were selected or constructed would give a clearer understanding of the experimental setup and the factors contributing to the reported performance. For instance, was a fixed set of negatives used, or were they dynamically sampled during each iteration? How does the batch size affect the stability and convergence of the contrastive learning process?
 + Some benchmarks have been provided in the Few Shot community to better take into account the semantics. See for instance meta-dataset or the work presented here. What is the behavior of the approach on these benchmarks? Evaluating the proposed approach on these datasets would provide a more comprehensive understanding of its capabilities and limitations in handling diverse semantic relationships.

+ Contrastive learning has been studied in the context of multimodal data. The positioning to these works could be interesting. See for instance the paper "Multimodal Contrastive Training for Visual Representation Learning". A more detailed comparison, highlighting the similarities and differences in terms of objectives, methodologies, and results, would strengthen the paper's contribution to the field.

+ Another concern is about the novelty of the proposed approach compared to (Chen et al, 2023). Compared to this work, the authors propose to add the metric module but this latter is also not new. I would appreciate it if the authors argued more on the novelty of this part, maybe in relation to the few shot settings and the way to tackle support and query sets. Specifically, how does the proposed metric module differ from existing metric learning approaches in the context of few-shot learning? What are the specific design choices that make it particularly effective for aligning visual and textual embeddings in this setting? A more detailed discussion on these aspects would help clarify the unique contributions of the proposed method.

### Questions
+ Recent works have shown the prevalence of transductive few-shot learning in image classification with this transductive setting that outperforms inductive approaches. How is the proposed approach compared to transductive sota approaches? How adapting the proposed approach to this scheme?
+ It is possible to better formalize the notion of semantic information? What kind of information should be added? 
+ The meta-learning paradigm has been discussed a lot in the few-shot community. See for instance [this paper](https://arxiv.org/abs/2003.11539). A discussion on this point should be added in the paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses few-shot image classification which is tasked to learn a classifier on new classes with only a few samples. This paper proposes to leverage class-level text-embeddings and introduces a metric module to align text and image embeddings. The text-embeddings in the experiments include language models, word embedding and CLIP text embeddings. The method follows the training and optimization framework of MAML, a popular meta-learning method. The experiments are conducted on the widely used few-shot learning benchmarks including miniImageNet, tieredImageNet and CUB. The results show better results than the baselines.

### Strengths
-The paper is written well and easy to understand.

-The proposed method is simple. It is intuitively a good idea to leverage the semantic information for few-shot image classification.

### Weaknesses
 -Overclaim the technical novelty. The framework of learning image and text alignment with a bilinear function has been extensively studied in zero-shot learning.  Some zero-shot learning methods (e.g., Xu et al.) even show that the framework generalizes well to few-shot learning setting. Although this paper adopts a different few-shot learning setting with episodic evaluation protocol, in principle, the core method is rather similar. In my view, this work seems to be a trivial combination of MAML and previous zero-shot learning methods, which can not be counted as a significant technical contribution. This paper seems to ignore this point and fails to discuss how it improves the zero-shot learning methods.

[A] Xu et al., Attribute Prototype Network for Any-Shot Learning. IJCV 2022. 

-Lack of insights. Although the proposed method achieves SOTA on some dataset, it mainly relies on the CLIP text embeddings, which is somewhat expected because it is known that CLIP embeddings can achieve impressive image classification results. The results using word embeddings and language embeddings are actually worse than some baseline methods. There are not much insights except the comparison between three different text embeddings.



### Questions
In Sec. 4.1, it says "Besides, we make the prompt templates learnable to avoid time-consuming prompt engineering following." But I did not find any technical detail about this part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work tackles the problem of few-shot learning and proposes a method to adapt a model employing the MAML framework. Specifically, the model is updated to perform on a specific task inferred from the alignment loss between text and image embeddings. The metric module is introduced to extend the cosine similarity between two modalities. The experiments show that the proposed method can outperform SOTAs in few-shot learning on several benchmarks.

### Strengths
- This paper proves the efficacy of the proposed method by beating SOTAs on several benchmarks e.g., mini-Imagenet and CUB datasets. 
- Ablation study is provided to understand the importance of the metric module.

### Weaknesses
 - The novelty of this work is limited as the off-the-shelf text encoder has been proposed previously using a similar contrastive loss for few-shot learning. The idea has overlapping to the idea proposed in VS-alignment (Afham et al., 2022) with a marginal extension in the meta-learning technique with MAML.  Some discussion (head-to-head) on the proposed method and Afham et al. would be beneficial for the readers to spot the difference and novelty of the work.
- The citation to Meta learning paradigm in Page 3 is not precise. Vinyals et al., 2016  do not discuss about meta-learning but the work is more related to learn in a few data regime. MAML paper would be a more relevant citation in this part.
- The manuscript is not well written. Equation (3?) in Page 6 is not precisely correct as the gradient descent should be performed w.r.t. I, T, and M. Please check the expression after $\nabla$. Also, the equation in Page 6 has no number. Please fix this in the revised version.
- Regarding this sentence in Page 2: “Secondly, in contrast to vision-language pre-trained models where both visual and textual encoders are learnable to align embeddings, we utilize frozen public textual encoders. This leads to totally different structures of textual embedding spaces and thus makes the alignment between visual and textual features difficult,” One concern is that why we cannot use the image encoder from a pretrained image encoder (e.g., CLIP image encoder)? Are there any settings that do not allow this condition? If this was feasible, would this work still consider MAML with several gradient steps to obtain optimal performance?
- This work must consider one important work [1] in this direction.  This work is the pioneer in using the off-the-shelf pretrained language model for few-shot learning but there is no discussion and citation to this work.
- The experiments are quite limited as most of the comparisons only involve image data without text information. It would be better to provide some other datasets e.g., COCO. Some other experiments as in [1] might be considered to show the efficacy of the proposed method and comparison with [1] on different modes (e.g., frozen and not frozen).

### Questions
Please see the weaknesses, especially the question about the image encoder.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
