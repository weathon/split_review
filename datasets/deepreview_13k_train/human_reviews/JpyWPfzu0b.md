# PaLI-3 Vision Language Models: Smaller, Faster, Stronger

- Decision: Reject
- Scores: 6, 3, 8

## Abstract
This paper presents \NEWNAME, a smaller, faster, and stronger vision language model (VLM) that compares favorably to similar models that are 10x larger.
As part of arriving at this strong performance, we compare Vision Transformer (ViT) models pretrained using classification objectives to contrastively (SigLIP) pretrained ones. 
We find that, while slightly underperforming on standard image classification benchmarks, SigLIP-based PaLI shows superior performance across various multimodal benchmarks, especially on localization and visually-situated text understanding.
We scale the SigLIP image encoder up to 2 billion parameters, and achieves a new state-of-the-art on multilingual cross-modal retrieval.
We hope that \NEWNAME, at only 5B parameters, rekindles research on fundamental pieces of complex VLMs, and could fuel a new generation of scaled-up models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents PaLI-3, a vision-language model with only 5B parameters but achieves state-of-the-art results across several benchmarks. The authors begin by comparing contrastively pretrained visual encoders and classification-pretrained ViT models, drawing the conclusion that the contrastively pretrained visual encoder demonstrates better performance on vision-language tasks, especially grounding tasks. Compared to previous state-of-the-art models (SOTAs), PaLI-3 can achieve competitive scores with significantly fewer overall parameters. Despite the training process being conducted without any video inputs, PaLI-3 is still capable of accomplishing video-based tasks.

### Strengths
- The conclusion that a contrastively pretrained visual encoder can outperform a classification-pretrained encoder in vision-language tasks, particularly in grounding, is valuable and beneficial to the vision-language community.
- Strong performance with much less parameters.
- Sufficient in-depth analysis on general tasks and fairness, bias and potential issues are performed to better model understanding.

### Weaknesses
 - The main weakness of PaLI-3, from my perspective, is the way the authors used to draw their conclusion. Specifically, the authors claim that because SigLIP shows better performance than the classification-pretrained visual encoder used by PaLI and PaLI-X, they conclude that a contrastively pretrained visual encoder is superior to a classification-pretrained one. However, it's worth noting that most of the accessible contrastively pretrained visual encoders for the vision and vision-language community are members of the OpenCLIP family. Have you ever attempted to utilize OpenCLIP as a vision encoder?
- The results in Section 4 are per-benchmark finetuned. What's the performance of PaLI-3 without task-specific fine-tuning (zero-shot)? Is it possible to generate target answers with few-shot demonstrations by prompting (in-context learing)?
- As mentioned in Section 3.2, during stage 0 of PaLI-3's training process, the contrastive visual encoder is pretrained with a 3B UL2 as a text encoder-decoder. Subsequently, the same 3B UL2 model is employed as the language model for PaLI-3. Is this consistency in using the same language model for both contrastive visual pre-training and generative vision-language pre-training crucial or not? Have any experiments been conducted on this?

### Questions
See weaknesses

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents the latest improvement in the so-called PALI series of VL models. The main contributions are the replacement of the Visual Encoder with a SigLIP model and the increase of resolution. The authors present many experimental results which show the effectiveness of their pipeline.

** Post rebuttal: ** The fact that contrastively pre-trained ViT with language supervision on billion scale dataset outperforms purely visually trained encoders is a well known fact in literature. All methods proposed in last couple of years (e.g. Flamingo, BLIP2) use that. Moreover, just replacing a backbone with another backbone is not of sufficient novelty for ICLR. Finally, increasing accuracy by increasing resolution is also well known. So unfortunately I will sit on my original rating.

### Strengths
The main strength of the paper is the numerous experiments the authors have carried out and the good results presented. Moreover, the paper is fairly easy to follow.

### Weaknesses
Unfortunately I don't believe that the claimed contributions (used of SigLIP and increase of resolution) are enough for ICLR. The finding that contrastively pre-trained visual backbone with language supervision works better than training for classification doesn't seem very surprising. Moreover, training follows previous PALI training pipelines so no particular novelty in this regard either. Actually incorporating these improvements could probably benefit any other model compared with the proposed one. The paper lacks a thorough analysis of the computational cost associated with the increased resolution. While the results show improved performance, the paper does not sufficiently explore the trade-offs between accuracy gains and the increased computational demands. Furthermore, the paper does not explore the limitations of the proposed approach, such as potential biases introduced by the pre-training dataset or sensitivity to specific types of visual inputs.

### Questions
No questions

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces PaLI-3, a new vision language model. One important modification is using SigLIP as the vision module encoder. The final model is small but effective. It performs comparably with many larger models on various benchmarks and also achieves better results in localization and text understanding than prior works.

### Strengths
1) Very good results in terms of cost-effectiveness trade-off.Comprehensive evaluation on various benchmarks.
2) The paper is very easy to read and understand.
3) The approach is simple and easy to implement.
4) The effectiveness of SigLIP is very insightful. It seems that such a simple modification can give a significant improvement. It shows the potential of the importance of designing a smarter training objective that aligns better with the language models.

### Weaknesses
1) I strongly encourage authors to provide more comparisons between CLIP and SigLIP under this paper's setting. The current ablation only includes the comparison between SigLIP and vanilla classification. Specifically, it would be beneficial to see a direct comparison of performance on the same downstream tasks using both CLIP and SigLIP as the vision encoder, keeping all other aspects of the model and training procedure constant. This would isolate the impact of the pretraining objective (contrastive vs. classification) on the final performance of the vision-language model.
2) I understand the paper mainly focuses on a smaller and cheaper model, as stated in the title. However, I think it is important to study the scaling results to check the effectiveness on a larger scale. Can the SigLIP still be so effective when using a larger vision encoder and language models? It would also be interesting to further scale down the model and see what would happen. It is not clear if the performance gains observed are specific to the current model size or if they generalize to larger and smaller models. Exploring this would provide a more comprehensive understanding of the proposed approach.

### Questions
1) Any plan to release the code? UL2 and SigLIP are both open-sourced. I think it would be nice to have an open-sourced version (would be better to use open-sourced data to pretrain) and will be easy to compare and use this model as a baseline. This model is small. If you can provide a fully reproducable version, I believe more folks from GPT-poor institutes would be motivated to follow.
2) I understand this paper's setting is not a huge model with a very strong zero-shot ability like GPT-4V. However, I'm highly interested in what do authors think about the potential of using SigLIP as the vision encoder for real LLMs (maybe > 100B or so).
3) Could you provide a detailed discussion about the difference between PaLI-3 and the previous versions? It would be better to have a table and show the differences directly.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
