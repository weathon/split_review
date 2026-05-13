# Parameter-Efficient Long-Tailed Recognition

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
The "pre-training and fine-tuning" paradigm in addressing long-tailed recognition tasks has sparked significant interest since the emergence of large vision-language models like the contrastive language-image pre-training (CLIP). While previous studies have shown promise in adapting pre-trained models for these tasks, they often undesirably require extensive training epochs or additional training data to maintain good performance. In this paper, we propose PEL, a fine-tuning method that can effectively adapt pre-trained models to long-tailed recognition tasks in fewer than 20 epochs without the need for extra data. We first empirically find that commonly used fine-tuning methods, such as full fine-tuning and classifier fine-tuning, suffer from overfitting, resulting in performance deterioration on tail classes. To mitigate this issue, PEL introduces a small number of task-specific parameters by adopting the design of any existing parameter-efficient fine-tuning method. Additionally, to expedite convergence, PEL presents a novel semantic-aware classifier initialization technique derived from the CLIP textual encoder without adding any computational overhead. Our experimental results on four long-tailed datasets demonstrate that PEL consistently outperforms previous state-of-the-art approaches. The source code is available in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a fine-tuning method PEL that efficiently adapts CLIP to long-tailed recognition tasks, within typically 20 epochs. One main motivation is that both full and classifier fine-tuning suffer from overfitting, with decreased performance on tail classes. To address overfitting, class imbalance and large cost during finetuning, PEF features 4 components: 1) parameter-efficient fine-tuning (PEFT) to mitigate overfitting through optimizing only a small amount of parameters on top of a frozen backbone, 2) logit-adjusted (LA) loss for training a cosine classifier to address class imbalance, 3) semantic-aware initialization to speedup convergence, 4) test-time ensembling to further improve generalization. SOTA performance is obtained on four long-tailed datasets while the compute cost remains low.

### Strengths
- Table 8 provides nice benchmarking of the overfitting issue of popular finetuning methods, which acts as a strong motivation of using PEFT to mitigate overfitting.
- The four components of the proposed PEL method (listed above) make sense, and their combination does lead to a good perf-cost tradeoff, as shown in the many experiments.

### Weaknesses
- None of the 4 components in PEL is new, and the big featuring of existing techniques seems a bit ad-hoc, which raises novelty concerns.
- Each of the 4 components is ablated separately --- Tables 1-3 validate the need of test time ensembling, while Figs 9-10 show that both PEFT and semantic-aware initialization are helpful. Tables 9-10 respectively show that the adopted classifier and loss function are the right choice. However, there's no clue about which of the 4 existing techniques play a key role, and which is more like icing on the cake. To tell which components are more important, a systematic ablation is required but is missing in the current paper, e.g., baseline vs baseline+component 1 vs baseline+components 1&2 ... vs baseline+components 1&2&3&4.

### Questions
- Semantic-aware initialization is claimed to accelerate convergence by initializing the classifier weights with text prompt features. What if the class is OOD/unseen for CLIP? Will such class prompt features still be a good initialization?
- In Table 10, it seems that different loss functions are all about the tradeoff between tail and head class performance. For example, the adopted LA loss, despite achieving the best performance on Median/Few splits, is suboptimal on the Many splits. Any comments?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors a simple yet effective long-tail learning framework namely PEL. Based on pretrained CLIP-ViT-B, PEL first introduces AdaptFormer and an individual cosine classifier to conduct parameter-efficient tuning on long-tailed data. To reduce the training difficulty, the authors also propose semantic-aware initialization, which leverages text embeddings from "a photo of [classname]" to initialize weights in the classifier. The proposed PEL achieves state-of-the-art performance on multiple long-tailed classification benchmarks.

### Strengths
1. The proposed efficient tunning method is effective, and the proposed semantic-aware initialization is intuitive and also effective. 

2. The experimental results are promising, and the ablation studies are extensive. 

3. This paper is well-written and easy to follow.

### Weaknesses
The main concern is also comes from semantic-aware initialization. Intuitively, only vision-language pretrained models (e.g., CLIP-pretrained models) support this kind of initialization. However, vision-only pretrained models cannot benefit from this initialization method. Though as shown in the code, using mean features in training set is alternative, the quality of tail classes is still not reliable like that of head classes. The authors could further discuss different initialization methods for different pretrained models (scenarios).

### Questions
See weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the study, the authors introduce PEFT (Parameter Efficient Fine-Tuning), a method designed for efficient adaptation of pre-trained models for long-tailed recognition challenges, achieving this adaptation in a reduced number of epochs and without additional data requirements. In this paper, PEL is also proposed to introduce a small number of task-specific parameters and present a novel semantic-aware classifier initialization strategy. Experimental results demonstrate the enhanced performance of the algorithm.

### Strengths
- The topic of PEFT (Parameter Efficient Fine-Tuning) is important, enabling a low-cost adaptation for downstream applications.
- This paper conducts empirical comparisons with different paradigms on long-tailed benchmark, such as training from scratch, finetune pretrained model and finetune with additional data.
- The proposed method is effective without introducing many computational cost and extra data.
- Generally, the paper is well structured and easy to follow.

### Weaknesses
- The related work seems insufficient. The authors should include references to existing studies concerning parameter-efficient fine-tuning approaches. Although some PEFT methods are presented in Section 3.3, these methods are listed without detailed explanations. 
- The technical contribution of this paper is not clear. The choice of AdaptFormer, based primarily on its state-of-the-art results, appears unrelated to long-tailed learning and should not be considered a contribution to the field. Besides, the initialization from CLIP text embeddings can not be regarded as significant technical contribution. Logit-adjusted (LA) loss and test-time ensembling also has been proposed.
- In Table 4, the authors seem only conduct experiments with existing PEL methods, the performance of the proposed method is missing.
- The authors should compare the computational cost with PEL methods in Table 4, instead of only comparing with non-PEL methods.
- The paper should broaden its scope by comparing various long-tailed learning strategies, rather than focusing on results from Logit adjustment or cosine classifer. The current benchmark could undermine the generalizability and confidence of the results.

### Questions
- The paper lacks intuitive explanations. The authors claim that their method can prevent overfitting and decrease training epochs without extra data, but how is PEFT helping? More empirical or theoretical explanations are suggested.
- Why are the training epochs chosen as 10/20? How would the results differ if the training period were extended?
- In Table 3, PEL incurs larger(4x) computation cost than LPT. Besides, LPT is not compared in Table 1. Will PEL degenerate on more real-world long-tailed datasets? It is suggested to add more datasets to enhance the confidence of the results.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces PEL, a parameter-efficient finetuning method for long-tailed recognition. It firstly analyzes the overfitting issue caused by full finetuning or classifier finetuning. Then it adopts several techniques to mitigate the problem, including:

- using existing Parameter-Efficient Fine-Tuning (PEFT) methods (e.g. AdaptFormer) instead;
    
- initializing the classifier weights with classwise textual features generated by CLIP;
    
- ensembling logits from different cropping methods of the same image during test time.
    

Based on these, this paper achieves SoTA results on several common long-tailed benchmarks with fewer training epochs and parameters.

### Strengths
- The paper is well-written and easy to follow.
    
- The experiments results are strong, and the ablations are clear and detailed.
    
- Different PEFT methods are explored for the long-tailed recognition (LTR) task.

### Weaknesses
- The technical novelty is a little incremental. All these PEFT methods already exist, and the authors adopt them for LTR tasks directly without any tailored modification. The initialization and ensembling are more like some kind of tricks without much insights for the community.
    
- Many previous works adopt ResNet as backbone. However, no experment in this paper adopts ResNet as well, which may raise questions about its generalisability.

### Questions
1. Why only use image cropping for test-time ensembling? Have you tried other data augmentation methods?
    
2. What kind of textual prompts are used for semantic-aware initialization?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
