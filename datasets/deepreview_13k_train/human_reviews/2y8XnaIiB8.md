# Vision-Language Dataset Distillation

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Dataset distillation methods reduce large-scale datasets to smaller sets of synthetic data, preserving sufficient information to quickly train a new model from scratch. However, prior work on dataset distillation has focused exclusively on image classification datasets, whereas modern large-scale datasets are primarily vision-language datasets. In this work, we design the first vision-language dataset distillation method, building on the idea of trajectory matching. A key challenge is that vision-language datasets do not have a set of discrete classes. To overcome this, our proposed method jointly distills image-text pairs in a contrastive formulation. Further, we leverage Low-Rank Adaptation (LoRA) matching to enable more efficient and effective trajectory matching in complex modern vision-language models. Since there are no existing baselines, we compare our distillation approach with three adapted vision-language coreset selection methods. We demonstrate significant improvements on the challenging Flickr30K and COCO retrieval benchmarks: for example, on Flickr30K, the best coreset selection method selecting 1000 image-text pairs for training achieves only 5.6\% image-to-text retrieval accuracy (i.e., recall@1); in contrast, our dataset distillation almost doubles that to 9.9\% with just 100 training pairs, an order of magnitude fewer.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method for distilling vision-language datasets that consists of image-text (caption) pairs.

The method is based training an expert model on the original datasets and a student model on the distilled dataset (initialized as samples from the original dataset) for a number of epochs. After which the samples from the distilled dataset are updated by back-propagating the loss function that measures the difference in parameter value trajectories of the student and expert models, over those selected number of epochs.

In the distilled dataset, the images are updated in the pixel space, but text captions in the text encoder’s input embedding space.

As no prior dataset distillation methods for language-vision data exist, the paper compares the proposed approach to 3 coreset selection methods and show consistent and substantial improvement over all of them.

### Strengths
- (S1) The paper contains a good set of experiments. The authors find a way to compare their method against image-only dataset distillation methods (Table 1) which somewhat isolates the impact of the specific model proposed vs. the task of image-text dataset distillation, as opposed to image-label. Additionally, the authors also experiment by distilling only one modality (either only text or only image) (Table 4), which demonstrates the relative impact of each of the modalities and the combination of them on the performance. The results contain standard deviation values.
    
- (S2) The quantitative results demonstrate that the proposed approach is consistently and substantially outperforming alternative approaches of coreset selection
    
- (S3) The paper is very well-written, and the method well-explained

### Weaknesses
 - (W1) The distilled dataset samples shown in the qualitative results (Figure 3) are, in case of images, not very different from the original images - only augmented with some noisy high-frequency patterns, and in case of text, do not consistently appear to be better than the original captions. That raises a question of how robust those distilled datasets are and indicates that maybe the source of effectiveness of distilled datasets is somewhat different from what one would expect, that is, models constructing very informative and representative samples. Instead, the impact appears to come from some artifacts, like these high-frequency patterns discussed by the authors. The lack of substantial visual change in the distilled images, beyond the addition of high-frequency noise, suggests that the distillation process might not be learning semantically meaningful transformations of the images. This raises concerns about the generalizability of the distilled dataset, as the performance gains might be tied to these specific artifacts rather than a more robust representation of the data.
    
- (W2) If I understood correctly, the evaluation of the distilled datasets (image-to-text and text-to-image retrieval) is performed on of the same architecture as the dataset distillation models. The paper does not seem to evaluate if the distilled datasets are equally effective for models of architecture different than those used for distilling the datasets. Considering the point raised above (W1), there is a risk that they are not. Images from the distilled datasets could be easily evaluated on different architectures. However, for text, the approach of operating on the input embeddings might not be adaptable in a straightforward way to other models. The reliance on input embeddings for text distillation makes it difficult to assess the generalizability of the distilled text data across different text encoders. This is a significant limitation, as the distilled text might be highly specific to the encoder used during distillation, hindering its use with other architectures.

### Questions
-

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explore a new problem: VL dataset distillation, which is not explored before, and the paper follows the existed dataset distillation approach to evaluate the performance. The results show that the distilled dataset can outperform the coreset algorithms significantly.

### Strengths
1. This the first paper to perform dataset distillation on the vision-language dataset.
2. Comprehensive experiments are conducted in the paper.

### Weaknesses
1. The underlying distillation process is the same to MTT, even though the expert model is trained with bi-direction contrastive loss

2. In the bottom on page 1, the authors mention it is hard for text data but in the paper, the authors still distill in the continuous space and then simply find the closet embeddings.



### Questions
1. In the problem formulation, is there any restriction on K? Or fewer pairs is the only goal?

2. The symbol notation is not clear, e.g. in eq. 2, what is * and hat of theta?, in eq. 3, what is the summation over y'? what is the set? all of y except itself?

3. In Table 1, as the authors use BERT-pretrained models, how much contributes come from the text-pretrained model when comparing to conventional dataset distillation.

4. As the pretrained models are used, what is dependency on the pretrained dataset (not the model), e.g. if the image and text encoders are pretrained with trained with the particular datasets, what is the performance of the model pretrained on other datasets training on the distilled dataset?
5. I wonder do authors know why the distilled images still look like the original real image? In MTT paper, the distilled images are very different from the real image (at least visually). 

6. Regarding the distilled text showing in Fig. 3, it seems that the distilled text could provide vague description, e.g. the bottom right image, it changes "two" men to "four" football players, if this algorithm is applied to VQA, won't it provide wrong counting?

### Soundness
3 good

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a multimodal dataset distillation method. Visual-language dataset distillation involves, first, training multiple models on the full dataset using bidirectional contrastive loss to obtain expert trajectories at various training epochs. Then, a set of student models is trained on a distilled dataset using the same bidirectional contrastive loss, and the dataset is updated based on a bi-trajectory matching loss that measures the alignment of student model parameter trajectories with the expert trajectories. The authors evaluate their method against the closest related work and show a significant improvement

### Strengths
- The paper is very well written and easy to understand. Authors clearly explain their method and provide an intuition behind their method selection

 - Results are significantly better than related methods with fewer examples. Ablation studies show that the multimodal distillation outperforms distillation with a single modality.

### Weaknesses
 - Storing and training with the trajectory data seems like an expensive process. The addition of multimodal data requires even more resources, such as modality-specific encoders.  While I believe that these factors represent significant limitations to the work, I also recognize the substantial contribution it makes to advancing this field.

### Questions
- I believe that the sentences generated for the qualitative results are nearest neighbors for real sentences in the dataset. However, is it possible to get the nearest neighbor token from the distilled text dataset? If so, do these tokens actually form sentences that make sense?

### Soundness
4 excellent

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
This might be the first work to condense images and text together. Based on the MTT from the domain of image condensation, this paper uses some engineering methods to build the basic framework. The experiments are extensively conducted on COCO and Flickr30K.

### Strengths
1. Writing is clear and easy to understand.
2. The problem is new to me.
3. The experiments are extensive.

### Weaknesses
1. The baselines of three coreset methods are too weak. There are too many empirical studies without any theoretical analysis of why these coreset methods are good for this task. 
2. Why use Cosine similarity to evaluate the pairs? Any theoretical analysis?
3. Why not freeze the image encoder backbone and just freeze the text encoder backbone?
4. Why choose the retrieval task? A straightforward task that hit my mind is to use a subset of CLIP [a] training set to train the CLIP model with similar performance. Can the proposed method do this?
5. Why use the NormalizerFree ResNet (NFNet) (Brock et al., 2021b; Wightman, 2019) as the image backbone? It looks like not the best backbone as shown in Table 9.
6. What is the result if the ratio equals 50% in Table 2? If the proposed method can reach or close to the upper bound in Table 3, I would raise my score.

### Questions
See weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
