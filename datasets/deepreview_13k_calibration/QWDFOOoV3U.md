# ResidualViT for Efficient Zero-Shot Natural Language Temporal Video Grounding

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 8, 6, 6

## Abstract
The goal of this work is to efficiently compute frame-level features from videos for the Zero-Shot Natural Language Temporal Video Grounding (NLTVG) task. The contributions of this work are three-fold. First, we introduce a novel vision transformer (ViT) architecture, dubbed ResidualViT, that capitalizes on the large temporal redundancies in video. Our architecture incorporates (i) learnable residual connections that ensure temporal consistency across consecutive frames and (ii) a token reduction module for enhancing processing speed by selectively discarding temporally redundant information. Second, we describe a lightweight distillation strategy that enables learning parameters of  ResidualViT from existing frame encoders without additional manual annotation. Finally, we validate the effectiveness of our approach across three diverse datasets, demonstrating significant reductions in computational cost (up to 60%) and improvements in inference speed (up to 2.5x faster), all while observing marginal accuracy reduction with respect to the teacher model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a novel framework, named ResidualViT, to efficiently transfer a pretrained image model (i.e., ViT) to video data for zero-shot natural language temporal video grounding.
Given that the number of patches per frame directly impacts processing costs when applying an image transformer across multiple video frames, the framework addresses this by categorizing video frames into two types:
To address this challenge, the proposed method divides video frames into two types: 

1) I-frames: Processed by the original image encoder to extract comprehensive I-features using all available tokens, capturing full information; 
2) P-frames: Processed by the ResidualViT, which takes the previous I-feature along with the tokens of the current P-frame. A residual tokenizer—a simple linear layer—projects the I-feature into the ViT’s input space, while a token reduction strategy removes certain tokens from the P-frame. The reduced tokens and projected I-feature are then fed into the ViT, cutting down computational costs without compromising essential information.

The ResidualViT is trained with the feature distillation strategy, where the original ViT is a teacher network and the ResidualViT is a student network.
ResidualViT is trained using a feature distillation approach, where the original ViT acts as the teacher network and ResidualViT serves as the student network. Training is guided by cross-entropy loss based on the softmax similarity between frame and language features from a pretrained text encoder.
Extensive experiments demonstrate the efficiency of the proposed ResidualViT, showing substantial reductions in computational cost and significant improvements in inference speed.

### Strengths
**[S1]** The proposed method is a novel attempt to efficiently transfer a pretrained image model (vision-language model in practice) to video data.

**[S2]** This paper presents extensive experiments, including token reduction, input configuration, and distillation.

### Weaknesses
 **[W1] Distillation through the soft target.**
In training, the proposed method leverages a language description corresponding to the input video to obtain soft targets by computing the softmax inner product between the visual and language features.
However, directly distilling the visual feature from the teacher network to the student network's feature can also be considered, as the pretrained vision and language encoder are kept frozen.
As shown in Section E, the ablation for the distillation strategy shows that there is no significant performance gap between models trained with each strategy.
Rather, the use of language descriptions appears to reduce the training efficiency due to the requirement of the CLIP text encoder.
An explanation and discussion of the benefits of distillation via soft target is required.

**[W2] Learning objective.**
The proposed learning objective makes the visual features from the teacher and student networks contain the same information. Meanwhile, correspondence between visual and language features seems to entirely rely on the pretrained model's capacity.
As the proposed ResidualViT focuses on the video-language task, considering frame-language interaction or video-language interaction in the learning objective would be good. (Note that this is simply a suggestion and the authors do not need to respond to this review.)

**[W3] Missing references.**
There are several previous works for efficient image-to-video transfer learning (e.g. [1-6]). While they have not focused on zero-shot natural language temporal video grounding, they could be included in Section 2.

```
[1] Lin et al., "Frozen CLIP models are efficient video learners," ECCV 2022
[2] Pan et al., "St-adapter: Parameter-efficient image-to-video transfer learning for action recognition," NeurIPS 2022
[3] Ni et al., "Expanding language-image pretrained models for general video recognition," ECCV 2022
[4] Ju et al., "Prompting visual-language models for efficient video understanding," ECCV 2022
[5] Yang et al., "AIM: Adapting image models for efficient video action recognition," ICLR 2023
[6] Park et al., "Dual-path adaptation from image to video transformers," CVPR 2023
```

**[W4] Additional issues.**
- Missing training details: In Table 2, the authors highlight the proposed method is not trained on downstream task datasets. However, the training data configuration has not appeared in the paper.
- Missing inference details: There is no explanation for inference, which should be included.
- Formatting: The reference formatting makes it hard for the reviewer to read and understand the paper. You may use \citep instead of \cite.

### Questions
**[Q1] Language description.**
- The proposed method requires language descriptions corresponding to the given videos. In that, the form of language data could affect the capacity of the learned representations and the final zero-shot natural language temporal video grounding performance. The quality of language description seems to be different for each training data. Is there an analysis according to the language descriptions' quality?
- Long-form videos are typically explained by multiple language descriptions as they contain multiple events. The proposed method takes a single text feature to compute the soft target, and I wonder whether this is sufficient when training a model using long-form videos.

**[Q2] Visual features.**
Are the visual features (i.e., I-/P-features) [CLS] token of the ViT's output?

**[Q3] Application.**
The proposed framework can be applied to any video or video-language tasks, such as action recognition and video-text retrieval.
Is there a reason to focus only on zero-shot natural language temporal video grounding?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an efficient method for feature extraction from dense video frames. The key idea is to exploit temporal redundancy in video. Features are extracted using vanilla ViT intermittently from keyframes. These features are subsequently propagated to nearby frames, whose features are extracted using a modified ViT, dubbed ResidualViT, with significantly reduced computational overhead. This is achieved by subsampling the input token embeddings while also inputting the features from the preceding keyframe to fill in the missing information. ResidualViT is trained using a distillation objective, with the goal of matching both the visual and textual features from a pre-trained CLIP. The experiments demonstrate that the method achieves competitive accuracy on the downstream task of video grounding yet higher efficiency when compared to running vanilla ViT on all frames.

### Strengths
- Strong motivation. The paper targets a key challenge in video understanding, namely the high computational cost of feature extraction from dense video frames for dense labeling tasks.
- Simplicity. The method leverages pre-trained models and its training does not require large data or compute. It thus is more practical and can be more easily adapted for a wide array of video understanding tasks.
- Effectiveness. Despite its simplicity, the method demonstrates strong zero-shot video grounding results.
- Clear writing. The paper is easy to follow and clearly describes the motivation, key intuition, and key components of the method.

### Weaknesses
 - The method is highly dependent on model architecture. Token dropping and residual feature passing assume the ViT architecture, which operates on single images. It thus does not allow the modeling of temporal dependency. Further, the distillation loss requires features from both image and text encoders (CLIP). Finally, this somewhat restrictive setting is derived from the video grounding task, and does not seem to generalize on other video understanding tasks, where a text branch is not necessary. I am wondering whether applying a similar approach to ViT (image branch only) would work for tasks like temporal action localization that do not take text as input.

- Some key ablation studies are missing. Token reduction probability p is a free parameter that controls the computational cost of ResidualViT. It would be helpful to identify the optimal p that achieves the best efficiency-accuracy tradeoff. Also, it would be interesting to study whether matching text features in model distillation necessarily boosts video grounding accuracy. Finally, one may compare the N=1 (or N=2) setting with naive frame subsampling, that is, only extracting I-frame features (and skipping P-frames) for video grounding. There is no need to run ResidualViT in the latter case, resulting in higher efficiency than the proposed method.

### Questions
- According to Figure 4, the spacing N has to be kept small to avoid significant accuracy drop. I am wondering whether this can be explained by the training procedure, where training samples are features from neighboring frames. What if the spacing between the training pairs is randomly sampled from some interval?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel method for zero-shot temporal grounding, which differs from traditional approaches that typically focus on reducing model parameters. The authors utilize the inherent redundancy between frames to transfer the ViT model from the image domain to the video domain. Additionally, they design a distillation mechanism for parameter learning. The approach is validated on three datasets, demonstrating significant reductions in computational costs compared to the baseline.

### Strengths
- The authors efficiently compute video features by leveraging the inherent temporal redundancy in videos. While this is a common practice in the video domain, its application to zero-shot temporal video grounding is relatively novel.
- After pre-training, the proposed method does not require training on the target dataset. This allows for direct application across different video grounding datasets, providing good flexibility.

### Weaknesses
 - There are concerns regarding the comparison with other zero-shot methods. As a reviewer for this paper's NeurIPS 2024 submission, I noted significant differences in GFLOPs between versions. Specifically, for the Charades-STA and ActivityNet-Caption datasets, the GFLOPs were reported as 148.4 and 9.6 for the NeurIPS version, while the current submission shows values of 1370 and 370, respectively. The authors should clarify the testing process and conditions for GFLOPs to help us understand the substantial discrepancies. Since the paper emphasizes efficiency, it is crucial to compare both performance and computational metrics accurately. Additionally, could the authors provide comparisons of throughput across different methods?
- Tied to the above question, is the frame sampling rate consistent when comparing the computational costs of different methods?
- Although the proposed method does not require training on the target video grounding dataset, it is important to note that the distillation process utilizes the WebVid-2.5M dataset, which effectively uses more video-text pairs than other methods. Is this comparison sufficiently fair?

### Questions
- Please clarify the specific computation process and methodology used for calculating the computational costs.
- Although the proposed method does not require training on the target video grounding dataset, it is important to note that the distillation process utilizes the WebVid-2.5M dataset, which effectively uses more video-text pairs than other methods. Is this comparison sufficiently fair?
- Since the proposed method requires pre-training on a video-text dataset, would using more pre-training data yield better results? What is the scalability of the method?
- If the parameter 𝑁 is increased from 3 to a larger value, how would the performance be affected?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes ResidualViT architecture for efficient temporal grounding of videos applicable to foundation vision-language models such as CLIP. Experiments are conducted on Charades-STA and ActivityNet-Captions dataset to show the effectiveness of the proposed method.

### Strengths
The paper proposes to reduce the cost of encoding video features by reducing the number of tokens and using residual connections. It shows reduction in GFLOPs by 50% on average across models. Ablation studies on the choice of each module shows the contribution of the proposed method.

### Weaknesses
Experiments are only conducted on only 2 datasets for the task of NLVTG. Experiments on MSR-VTT, TaCoS are necessary to analyze its generalization ability.

Missing evaluation results for Recall@5 although it is mentioned in the evaluation metrics section L340.

For token dropping, what about other pruning methods like DiffPruning [1] or Taylor Pruning [2] or Magnitude Pruning [3]?

For ablation on the spatial resolution, the comparisons are made against ResidualVit token dropping strategy that is finetuned and so is not a fair comparison. What is the performance difference when finetuning adapters for those lower spatial resolution inputs?

Additionally, for the fully supervised baseline, the reported results differ from those presented in the CG-DETR paper (CLIP+Slowfast baseline). Could you clarify the reason for this discrepancy?

### Questions
How about the performance when applying the method to supervised or weakly supervised methods?

For the runtime analysis, is the motion-based token reduction strategy applied? Computing the motion vectors adds to the latency and so the total time should include this for fair comparisons.

Why is the interleaving factor N set to 3 during training and is different for testing?

### Soundness
3

### Presentation
3

### Contribution
2
