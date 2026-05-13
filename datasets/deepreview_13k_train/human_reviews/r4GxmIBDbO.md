# Diffusion Pretraining for Gait Recognition in the Wild

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
Recently, diffusion models have garnered much attention for their remarkable generative capabilities. Yet, their application for representation learning remains largely unexplored. In this paper, we explore the possibility of using the diffusion process to pretrain the backbone of a deep learning model for a specific application—gait recognition in the wild. To do so, we condition a latent diffusion model on the output of a gait recognition model backbone. Our pretraining experiments on the Gait3D and GREW datasets reveal an interesting phenomenon: diffusion pretraining causes the gait recognition backbone to separate gait sequences belonging to different subjects further apart than those belonging to the same subjects, which translates to a steady improvement in gait recognition performance. Subsequently, our transfer learning experiments on Gait3D and GREW show that the pretrained backbone can serve as an effective initialization for the downstream gait recognition task, allowing the gait recognition model to achieve better performance within much fewer supervised training iterations. We validated the applicability of our approach across multiple existing gait recognition methods and conducted extensive ablation studies to investigate the impact of different pretraining hyperparameters on the final gait recognition performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces an approach to gait recognition that leverages both local and global difference learning within video silhouettes to enhance feature extraction. The method uses Local Difference Modules (LDM) and Global Difference Modules (GDM) to capture intricate motion details across both short and long temporal spans, with a Temporal Alignment Module ensuring consistency across the extracted features. The framework significantly outperforms existing methods on multiple benchmarks, demonstrating its robustness and effectiveness in gait recognition across diverse conditions.

### Strengths
+ Demonstrates clear improvements in model performance with respect to accuracy and training efficiency on challenging datasets.

+ Comprehensive experiments and ablation studies provide a robust validation of the proposed method across different configurations and baseline comparisons.

### Weaknesses
1. While the application of diffusion models in gait recognition represents a novel approach within this specific field, the broader concept of leveraging diffusion models for enhancing feature extraction in image and sequence analysis is not entirely new. This raises a question about the depth of innovation when such a technique is applied strictly to one domain without exploring its potential across related areas.

2. The process involves multiple stages, including the conditioning of diffusion models, which may not only prolong the training time but also require substantial computational power, particularly GPU resources. This could pose challenges for scalability, especially when deploying the model in resource-constrained environments or scaling up to larger datasets.

3. The model's reliance on well-segmented and aligned input data for effective pretraining may reduce its robustness in truly uncontrolled environments where such quality cannot be guaranteed. This dependency could undermine the practical utility of the model in real-world applications where ideal data conditions are not met. A deeper investigation into the model's performance with lower quality or adversarially perturbed inputs would be valuable.

### Questions
1. What are the computational costs associated with the diffusion pretraining, and what strategies might be considered to reduce them?

2. Could the authors elaborate on the potential applications of this method beyond gait recognition, perhaps in other areas of facial or emotion recognition?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel pre-training strategy  for gait recognition that utilizes conditional diffusion models. The authors pretrain several gait recognition model architectures from the Open-Gait Library, employing an encoder, denoiser, and pooling layer. The pretraining process leverages diffusion L2 loss in the predicted noise space, after which the pretrained model is fine-tuned for a specific gait recognition task.

### Strengths
(1) Pioneering Work: This study is the first to investigate diffusion-based pre-training specifically for gait recognition.

(2) Optimized Pretraining: The authors introduce a modified Min-SNR weighting strategy that enhances the efficiency of the pretraining process.

(3) Clarity and Readability: The paper is well-written and presents its ideas in an accessible manner.

### Weaknesses
 (1) Unclear Motivation and Justification: While the paper claims that the gait feature extractor provides conditions for the denoiser, it also mentions that this extractor is trained from scratch. Given that only diffusion L2 loss is employed during pre-training, it remains unclear how discriminative gait features are learned without a dedicated loss function guiding the feature learning process. Specifically, the diffusion loss operates in the pixel space, and it is not evident how this translates to meaningful feature separation in the embedding space used for gait recognition. The paper lacks a clear explanation of the mechanism by which the diffusion process implicitly encourages the learning of discriminative features.

(2) Assumption of Transfer Learning: The approach assumes that the downstream task serves as transfer learning for another dataset; however, this appears to resemble domain adaptation more closely. The fine-tuning process is performed on the same dataset used for pre-training, which does not align with the typical transfer learning paradigm where a model is trained on one dataset and then applied to a different dataset. This mischaracterization of the learning process undermines the validity of the claims made regarding transfer learning.

(3) Lack of Novelty:
(i) Reliance on Existing Techniques: The framework primarily amalgamates established techniques without offering substantial innovations. The use of diffusion models and the specific architecture components are not novel in themselves. The paper does not demonstrate a novel way of combining these components.
(ii) Absence of Unique Contributions: The proposed method does not demonstrate a clear theoretical or practical advantage over existing approaches. The performance gains are marginal and do not justify the complexity of the proposed pre-training method.
(iii) Need for Differentiation: The authors should emphasize the unique aspects of their methodology and clarify how it addresses the shortcomings of prior work. The paper fails to adequately position itself within the existing literature and does not clearly articulate its unique contribution.

(4) Unfair Comparison: The gait extractor is trained for 120,000 iterations. When fine-tuning, the proposed system's training duration (denoted as x iterations) results in a cumulative training time of 120,000 + x iterations. This creates an imbalance in comparison with the baseline system trained for x iterations, which raises concerns about the fairness of the comparison. The additional pre-training iterations give an unfair advantage to the proposed method, making it difficult to isolate the true impact of the diffusion-based pre-training.

(5) Outdated Models: The paper primarily utilizes older models, with the most recent being Gaitbase (2023). It does not incorporate the latest state-of-the-art models, such as DYGait, SkeletonGait, CLASH, and QAGait, which have demonstrated significant advancements on in-the-wild datasets like GREW and Gait3D. The lack of evaluation on recent state-of-the-art models limits the impact and relevance of the proposed method.

(6) Performance Relative to State-of-the-Art: Despite reporting some improvements through pretraining, the accuracies achieved post-pretraining remain lower than those of existing state-of-the-art models. The reported performance gains are not substantial enough to justify the additional complexity of the proposed method. The paper does not demonstrate a clear advantage over existing approaches.

(7) Lack of Novelty in Section 3: This section is well-articulated but does not introduce any novel components to the framework.

### Questions
Please read weaknesses for elaboration.
 
(1) How can discriminative gait features be learned without a dedicated loss function guiding the feature learning process?

(2) Does the assumption that the downstream task serves as transfer learning for another dataset not resemble domain adaptation more closely?

(3) The proposal lacks novelty, particularly in its reliance on existing techniques and the absence of unique contributions? Could the authors clarify the unique aspects of their methodology and how it addresses the limitations of prior work, especially since Section 3 does not present any novel components?

(4) Could the authors elaborate on the fairness of their comparisons as noted in the weaknesses section?

(5) Why are the latest state-of-the-art models, such as DYGait, SkeletonGait, CLASH, and QAGait, not considered in this study? 

(6) How do the reported performance metrics compare to those of state-of-the-art models, and why is the performance considered inferior?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a diffusion-based approach to pretrain the backbone of a gait recognition model, using its output as a conditioning input for a latent diffusion model. The pretrained backbone is then used to initialize the gait recognition model, which is subsequently fine-tuned with the original supervision of the gait recognition task. Experiments on GREW and Gait3D demonstrate that this pretraining enhances gait recognition performance after fine-tuning, surpassing results from training from scratch across multiple gait recognition backbones.

### Strengths
+ Using diffusion models to pretrain a gait recognition model is an interesting idea, and has not been explored in the literature.
+ Experimental results show that the performance of the gait recognition models can be improved through the proposed pre-training and fine-tuning.

### Weaknesses
 - The biggest concern is that the rationale for using features from the gait extractor as conditioning to help the designed diffusion pretraining improve gait recognition performance is not explained, as no constraints on person identity are considered during pretraining. It is understandable that if the diffusion reconstruction works well, the identity in the same gait sequence can be maintained and learned to some extent. However, it remains unclear why the discrimination capability can be improved for different gait sequences of the same person (e.g., sequences from different views), given that no generative task or supervision is applied between these sequences, which actually need to be recognized in a gait recognition task. The core issue is that the pretraining lacks a mechanism to explicitly learn inter-sequence discriminative features, which are crucial for gait recognition where the goal is to distinguish between different instances of the same person's gait.
- The comparison experiments should also consider other pretraining methods. Just comparing with training from scratch seems unfair, as the gait recognition network in the proposed framework was trained twice (pretraining + fine-tuning) using tuned parameters. The absence of comparisons with other pretraining techniques makes it difficult to ascertain the true advantage of the proposed method over existing approaches, especially considering the additional computational cost of the diffusion pretraining stage.
- The proposed method includes several hyperparameters (e.g., $r$, $l_g/l_D$ ) that require careful tuning or selection based on the results. These hyperparameters vary across different datasets and backbones, which limits the generalizability of the proposed pretraining. For instance, the improvements of the SOTA in this paper (i.e., GaitBase, although even newer SOTA backbones are now available) on GREW using the pretraining method seem incremental. The need for per-dataset and per-backbone hyperparameter tuning makes the method less practical for widespread adoption.
- The proposed method is mainly a pretraining strategy designed for downstream gait recognition applications, and most components are based on existing modules or backbones. The main distinction lies in conditioning the gait extractor for diffusion generation, which requires further consideration of its rationale. So, the theoretical novelty of this method appears somewhat limited. The core idea of conditioning a diffusion model on gait features, while interesting, lacks a strong theoretical underpinning that explains why it should improve inter-sequence discrimination.
- Since diffusion-based representation learning has been applied to other tasks, such as image classification, as the authors mentioned, it would be better to compare the proposed method against these approaches to demonstrate its superiority. The lack of comparison with other diffusion-based representation learning methods makes it difficult to assess the novelty and effectiveness of the proposed approach.
- Based on the design of the proposed method, it does not seem to be limited only to gait data in the wild. It is recommended to conduct experiments also on CASIA-B and OUMVLP, which include significant view variations, to validate whether the pretraining also enhances performance in typical cross-view gait recognition tasks. The absence of experiments on standard cross-view gait datasets limits the assessment of the method's generalizability.

### Questions
-	In line 279, it is mentioned the ``remaining parts’’ are replicated in transfer learning. For a gait recognition model, it is important to clarify which parts are pretrained and which parts remain untrained during the pretraining process.
-	In Section 3.1.5, $s_\epsilon$ is defined as N frames sampled consecutively from the sequence, and $s_g$ is N frames sampled following the original backbone. In Fig. 5, $s_\epsilon \neq s_g$ is shown to be better than $s_\epsilon = s_g$. However, for backbones such as GaitPart and GaitGL, N consecutive frames are necessary for learning temporal information. How can $s_\epsilon \neq s_g$ be maintained in this case?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors try to make use of the superiority of the diffusion model in gait recognition, serving as a pretraining method. Based on the experiments, the proposed pre-training method have the ability to recognize the people alone. When it is trainable in the downstream task, the performance is higher than the models without pertaining, demonstrating the effectiveness of the proposed method.

### Strengths
1. The work is a good attempt to use the diffusion model in gait recognition serving as a pre-training model.
2.  The authors did extensive experiments to demonstrate the details and effectiveness of the model.
3. The present is clear and it is easy to understand.

### Weaknesses
1. The motivation is not that clear. What feature of the diffusion model is potentially helpful for gait recognition
2.  What does 'focus on gait information rather than video information' mean in sec 3.1.5. What is the video information defined here?
3. The sampling method is not clear. Sequential gait recognitions, such as GaitGL, still use consecutive 30-frames. So what is the difference between these two inputs?
4. The whole paper tells what the authors did but with little analysis, such as why the diffusion model could be helpful and why the structure is like this.

### Questions
The figure could be improved. If the different frames are selected, the figure should have this kind of information rather than the same silhouettes.
The experiments section only demonstrates the tables' content but lacks analysis, such as why there is improvement and why some works do not work well.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This research makes a good attempt to use diffusion-based representation learning on gait recognition by using gait models’ output as a condition for a latent diffusion model.

### Strengths
1. Good Novelty. The paper explores diffusion methods on gait recognition task, and reveals an interesting and useful phenomenon.

2. Good Improvement. Abundant experiments show that diffusion pertaining considerable improves the existing gait methods.

### Weaknesses
1. Question on Pre-training. The pre-training process seems a knowledge distillation between diffusion models and gait models. The experimental improvement shows diffusion models are good at identifying human in some case. Therefore, the authors are expected to directly fine-tune the TAESD (your diffusion encoder) on the downstream gait recognition task. If we can get higher performance by fine-tuning diffusion itself, why we need to pre-train other gait methods by diffusion models?

2. The reduction of supervised training iterations seems weak, since you have to pretrain other gait models at first. Tab.1 also shows that the number of original training iteration is  almost equal to that of pertaining + transfer learning.

3. The authors are suggested to try some stronger gait models (like deepgaitv2) as the backbone. It is crucial to benchmark against state-of-the-art methods to demonstrate the true value of the proposed approach. The current choice of backbones might not fully reflect the potential of the diffusion-based pre-training.

### Questions
If the authors can address my concerns, I would like to improve the final rating.

### Soundness
2

### Presentation
3

### Contribution
3
