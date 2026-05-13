# Cross the Gap: Inter-modal CLIP Representations Are Superior for Intra-modal Tasks

- Decision: Accept
- Scores: 3, 6, 8, 8

## Abstract
Pre-trained multi-modal Vision Language Models like CLIP are widely used off-the-shelf for a variety of applications. Previous work has shown that, due to contrastive pre-training, there is a modality gap between the text and image feature embedding spaces. In this paper, we show that the common practice of individually exploiting the text or image encoders of these powerful multimodal models is highly suboptimal for intra-modal tasks like image-to-image retrieval. We argue that this is inherently due to the inter-modal contrastive loss commonly used to train CLIP models. To demonstrate this, we leverage two optimization-based modality inversion techniques and the inductive bias of the pre-trained encoder of the complementary modality to transform native modality inputs into inter-modal representations. We empirically show in multiple settings (image retrieval, text retrieval, and zero-shot image classification), and at the single-feature level -- i.e. each individual feature embedding is mapped to its complementary modality without any need for auxiliary data or additional trained adapters -- that approaching these tasks inter-modally significantly improves performance with respect to intra-modal baselines on more than fifteen datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper investigates the suboptimal performance of using pre-trained multi-modal Vision Language Models (VLMs) like CLIP for intra-modal tasks. It highlights the modality gap, a disparity between text and image feature spaces due to contrastive pre-training, which leads to poor performance in tasks like image-to-image retrieval when using individual text or image encoders. The authors propose a modality inversion technique to transform native modality inputs into inter-modal representations, leveraging CLIP's inter-modal alignment. Extensive experiments demonstrate significant performance improvements over intra-modal baselines in image retrieval, text retrieval, and zero-shot image classification tasks.

### Strengths
- The paper introduces a novel modality inversion method that significantly outperforms standard intra-modal approaches by exploiting inter-modal alignments of CLIP models, providing a new direction for enhancing VLMs' utility in single-modal tasks.

-  With experiments spanning multiple datasets and tasks, the paper offers robust evidence of the proposed method's efficacy, showcasing its broad applicability in the field of multi-modal learning.

### Weaknesses
- The contribution is incremental, as the OTI has already been introduced by existing methods.  
- In zero-shot classification, current methods utilize both image and text encoders concurrently. Therefore, only utilizing the image encoder compromises fairness in the experimental comparisons for this task.  
- Several relevant comparative methods are omitted. In particular, the proposed method achieves similar effects to prompt learning and adapter learning, which should be discussed and included in further comparisons.

### Questions
Please see the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper points out the problem of  intra-modal misalignment in CLIP, which limits its effectiveness for intra-modal tasks such as image-to-image retrieval. To address this issue, the paper proposes to transform intra-modal tasks to inter-modal ones via Optimization-based Textual Inversion (OTI) and Optimization-based Visual Inversion (OVI), which map representations to the complementary modality. The experiments demonstrate its effectiveness on fifteen datasets.

### Strengths
1. The paper tackles an intriguing problem, since CLIP encoders are widely used in various tasks and serves as components in other models like LVLM. Addressing the intra-modal misalignment issue could enhance CLIP's performance in image and text understanding.
2. The presentation quality is high. The paper is well-written, easy to follow, and features clear and informative figures.

### Weaknesses
1. The analysis of the intra-modal misalignment problem could benefit from more quantitative insights. In Figure 1, the authors illustrate that intra-modal similarity scores can be higher for the same class than for different ones. Providing statistics to demonstrate the significance and frequency of this issue would strengthen the argument.
2. The experiments lack comparative analysis. While the related works section mentions existing works that explore intra-modal misalignment, it would be beneficial to compare these methods in the experimental study to validate the paper's contributions.

### Questions
It is interesting to know if it is possible to have a more systematic approach for selecting the number of tokens and optimization steps used in OTI and OVI, as discussed in Figure 2.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors point out in this paper that the common practice of using intra-modal similarities from pre-trained CLIP encoders is inherently suboptimal for intra-modal tasks. To address this, they adapt optimization-based modality inversion techniques (OTI and OVI) and leverage them to transform native modality inputs into intermodal representations for similarity measures. Experiments across three settings—image-to-image retrieval, text-to-text retrieval, and zero-shot image classification—on 15 datasets and with 5 different pre-trained models validate the authors’ hypothesis, demonstrating the effectiveness of optimization-based modality inversion.

### Strengths
- The idea is good and interesting. Using inter-modal CLIP representations for intra-modal similarity measures makes sense. If this has not been done before, it is a novel idea.

- The paper is well-motivated, with comprehensive experiments, promising results, and clear writing.

- The authors validate their hypothesis and demonstrate their method's effectiveness through extensive experiments involving over 15 datasets, 3 different types of CLIP models, and 5 different pre-trained models.

### Weaknesses
- The method is quite simple. OVI is similar to OTI. There is nothing new about the inversion. But applying the inversion in this particular context can be appreciated. The authors might want to tune down the claim on the methodology contribution.

- It is a surprise to see the proposed method also helps with image classification tasks. Why? Image classification is supposed to be an inter-modal task. In the open-vocabulary setting, it is often done by comparing CLIP image features with a set of CLIP text features on the class vocabulary, which is already inter-modal. 

- Missing baseline: For the image-to-image retrieval task, the authors convert the query image to a corresponding textual feature using OTI, then calculate semantic similarity between this feature and the other image features (obtained from the CLIP image encoder) to get the final results. An important baseline is missing, i.e., converting all the images into OTI features and then measuring the similarity among OTI features. This can demonstrate your proposed inter-modal CLIP representations are better for intra-modal tasks.

### Questions
- Please answer those issues pointed out in the weakness.
- In Table 1, the use of OTI features outperforms native image features on all datasets except for the EuroSAT dataset. What distinguishes the EuroSAT dataset from the others? Why does it show a performance decrease with OTI features? 	
- The authors use the template sentence “a photo of” concatenated with the pseudo-word tokens in Section 4.1. Have you tried other templates?
- It would be better to provide more training details (e.g., training time, memory usage, and training data).

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
4

### Summary
This paper demonstrates that CLIP models, trained exclusively with inter-modal contrastive loss, perform suboptimally on intra-modal tasks like image-to-image and text-to-text retrieval. The authors attribute this limitation to a modality gap and the absence of intra-modal supervision during pre-training. To address this, they employ modality inversion techniques, transforming inputs across modalities to bridge this gap and enhance intra-modal performance. Through extensive experiments, they show that CLIP’s intra-modal performance improves by leveraging the structured nature of inter-modal cosine similarities, which are more consistent than intra-modal ones.

### Strengths
Well written, easy to follow.
Extensive experiments and analysis.

### Weaknesses
Lack. of alternative baselines, consider evaluating alternative baselines, such as using an image-captioning model to generate captions for query images, followed by image-to-image retrieval based on these captions. This could provide a comparative perspective on the effectiveness of the proposed modality inversion techniques.

Minor: Are the ticks and crosses correct in Table 2. Right. ?

### Questions
1. Does combining the native image representation with its inverted (cross-modal) image representation provide any performance benefits?

2. For text-to-text retrieval, have you tried the method on a purely textual task with less than 77 tokens context? Existing text retrieval datasets could be summarized to 77 tokens using an LLM. My assumption is that this approach would only be effective when the text can be represented visually, which might explain its success with text derived from image-captioning datasets.

3. Have you considered alternative baselines for image-to-image retrieval, such as using a captioning model?

4. Do you have any intuitions on why the image-image retrieval score for EuroSat dataset goes down with modality inversion?

### Soundness
4

### Presentation
4

### Contribution
3
