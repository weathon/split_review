# Diffusion Models are Few-shot Learners for Dense Vision Tasks

- Decision: Reject
- Scores: 6, 3, 8, 3, 6

## Abstract
The ability to adapt to new, unseen tasks with only a handful of training examples is a key factor behind the unprecedented success of language models. However, in computer vision, few-shot adaption has largely focused on adapting to new semantic categories or answering new visual questions. Adapting a model to dense vision tasks – depth estimation, surface normal estimation, semantic segmentation – has only been possible with large amounts of training data and with custom decoder heads, since the output spaces for each task varies widely. For instance, depth estimation outputs continuous values while semantic segmentation generates discrete categorical assignments. In this paper, we found that the diffusion prior can effectively adapt to various dense tasks, and based on this, we introduce an adaptation mechanism that exploits a pretrained diffusion model for 12 different dense vision tasks using only a few training examples. Moreover, adapting to different tasks requires only modifying the input, without changing the internal parameters of the model. Our key insight is to reframe all dense prediction tasks into a codebook-conditioned classification problem, even for continuous outputs.
Specifically, we learn two set of parameters: (1) concept embeddings that condition the diffusion model to encode task-specific representations in their attention masks; and (2) codebook embeddings that recombine discrete outputs to continuous ones. With this novel design, we achieve state-of-the-art results across 12 datasets for few shot learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an approach for adapting a diffusion model for dense vision tasks in a few-shot setting. To do this, the authors transform dense prediction tasks into classification tasks, with a learnable codebook that converts the classes into continuous outputs. The method is (likely) efficient to train as it only requires finetuning the additional components added to the diffusion model, and not the entire model end to end.

### Strengths
1.	The paper is generally well-written, and addresses an important task with growing interest in the field (how to use diffusion models for discriminative tasks)
2.	The figures are both easy to understand and aesthetically pleasing.
3.	The results appear to outperform the prior methods reported across all tasks in a few-shot setting.

### Weaknesses
1.	My main concern is that it’s not clear to me where the wins are coming from compared to prior work. As I understand it, the submission uses a more capable Stable Diffusion backbone compared to prior work, and the paper does not ablate the importance of this. Specifically, the improvements could be attributed to the architectural differences between Stable Diffusion v1.5 and v2.1, such as the increased number of parameters and the modified attention mechanisms, rather than the proposed method itself. Without a direct comparison using the same backbone, it's difficult to isolate the contribution of the proposed approach.
2.	My second concern is that this win appears to show up only in the few-shot setting, and VPD outperforms when there is more data. Given the size of vision datasets today, I’d be curious where this sort of few-shot adaptation is a concern – it would be great to show off the value of this method in a setting like that! I’d also be curious what the tipping point is at which VPD starts to outperform (100 images? 1,000 images? 10,000 images?) This lack of clarity regarding the practical applicability of the method in realistic scenarios with varying data availability is a significant limitation. The paper should provide a more detailed analysis of the performance trade-offs with respect to the number of training samples.



### Questions
1. My main concern: How much does SD2.1 affect results? The prior methods that use diffusion, from what I understand, used earlier or different variants of Stable Diffusion, and it’s not clear how much of the improvement can be explained by that.
2. The ablations in Fig 3 suggest that a major improvement is due to transforming the dense tasks into classification tasks, though this is only on train loss. What happens to the evals here?
3. The main ablations are:

    i) Code book size: It doesn’t seem like codebook size affects results significantly

    ii) Classification vs. not: This is very important

    iii) Self attention is slightly helpful
4. Ultimately VPD performs better with more data. What if you had a simpler baseline like VPD but with more parameters frozen? What is the threshold of data at which VPD starts outperforming? Is it easy to compare the models with a few different thresholds of data points?
5. Fig 1 caption says the method is more useful for real-world online deployment because the approach only requires optimizing the model’s input. But this should only impact training, not deployment, right? 

Nit: L451: typo: “We can see We can observe that both”

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors demonstrate that a pretrained diffusion model can be successfully used to adapt to novel dense vision tasks in scenarios when only few examples are available. To this end, the authors propose the use of learnable concept embeddings (i.e. prompts) and a combination of the model’s internal attention maps to extract category-probabilities for discrete tasks, whereas continuous outputs are recovered via a codebook-based value mapping conditioned on the input image via CLIP embeddings – allowing the approach to be used across a variety of dense vision tasks.

### Strengths
**Originality & Significance:**   
- The authors propose an elegant method to leverage the internal power of pretrained diffusion models in a parameter-efficient manner
- The codebook-based value mapping is a versatile way to map between discrete and continuous domains

**Quality:**   
- Experiments conducted across a good selection of datasets, contrasted to some recent related works

**Clarity:**  
- The paper is mostly easy to read
- The authors provide a very clear visualization of their approach in Figure 1, which nicely accompanies their explanations

### Weaknesses
 _TL;DR: While I appreciate the work the authors have put into the paper and their experiments, the manuscript in its current form would significantly benefit from several improvements and additions (esp. to remove inconsistencies) -- and does (for me) in its current form not pass the bar for ICLR._

- Inconsistencies in analysis descriptions/interpretation, see questions.
- Very few 'few-shot' evaluations/insights for a few-shot specific work 
- Writing quality could be significantly improved, as this unfortunately negatively affects the interpretation of results / findings.
- Missing references – the idea of discretising a continuous prediction problem in vision (e.g. depth estimation) is NOT new
- Concern: copy-paste sentence (out of context) from a different (uncited) ECCV paper – needs to be explained
- The preciseness of statements could be improved: E.g. instead of ‘conduct […] experiment multiple times’ (l276f), state number explicitly


- Minor: Some criticism the authors place on other works during motivation similarity applies to their own – see questions/additional comments

### Questions
**Main concerns, questions & potential improvements:**    
- The authors’ approach of discretising a continuous space to solve the prediction problem in vision, especially depth estimation, is NOT new to the field. I’d highly suggest the authors to include references to prior work to attribute these efforts accordingly.

- For a work centered around few-shot learning, I would expect more few-shot specific evaluations: For example, how does the method behave for different tasks (continuous and discrete) when a growing number of samples become available? How does it fare for 1shot, 5shot, etc? Is it more robust than other methods? Why/why not, and on which tasks?   
-> Note that currently, the authors provide one fixed setting only which provides very little insight regarding the few-shot character of the method.

- L161f: The sentence ‘preserves the overall motion and semantics of the original video …’ is entirely out of place, and – more importantly – is a direct copy-paste from a recent ECCV paper by Fan et al. (2024)   
-> I’d like the authors to explain if this simply slipped in there, or whether there are other reasons (and potentially other copied sentences)? Note that this can significantly compromise a reader’s trust in your work. 

- During the analysis in Table 3, the authors denote in the caption that the results are “compared to only using self attention mask”, i.e. NO cross-attention – however, the table then shows “w/o Msa” and “w/ Msa”, which contradict the earlier statement;    
Independent of which of the two is correct, it would be beneficial to show all three as ablation – i.e. Msa only, Ca only, Msa&Ca; 

- The influence of Msa and Ca is only partially demonstrated for continuous tasks – I would be interested whether their influence is different in discrete settings, where they are pretty-much used directly (w/o codebook); I’d suggest the authors extend their Table 3 and present some discrete results as well;

- Figure 3 & corresponding results: The authors state they calculate the ‘regression loss’ on the validation set, which drops faster when using regression+classification loss than it does with regression-only;    
-> However, this raises the question whether the two have been using the same hyperparameters or have been independently ‘optimised’;   
-> Note: When adding the ‘additional’ classification loss, the loss will generally likely be larger, and hence gradients will likely be larger as well;  This might by itself cause a faster convergence, which is mainly caused by the magnitude and not necessarily the nature of the losses;    
I’d suggest the authors take a look at their gradient and loss magnitudes, and check fi the same holds when the learning rate is adjusted accordingly (or losses are scaled accordingly)

- I’d further like the authors to provide some more insights they have gained, as well as potential limitations they can see for their method. The manuscript in its current form mainly reports how things are done, but I am missing some deeper insights into the underlying motivations and potential corner cases / things that would need to be considered in follow-up work!    

- I’d suggest the authors read through their manuscript again and make an effort to correct typos and grammatical mistakes (e.g. l59 demonstrate, l155 missing period, l160 ‘that’ must be removed, … and many more.)   
While I am aware that this might be due to language barrier, there are many tools available to support these efforts, and it would significantly improve the quality of the manuscript.


Additional comments:
- The authors criticize other works for using ‘custom decoder heads, since the output space for each task varies widely’, mainly due to some tasks requiring continuous vs. discrete outputs;     
-> However, their own method equally uses a different methodology for continuous (codebook-based value mapping) vs. discrete tasks – and hence, the criticism could similarly be applied to their own work; Some reformulating or discussion why this would be different might be helpful for the reader.
- The ease of interpretation of the results in the table could be significantly improved by added the metrics as well as an arrow (up/down) to indicate the desired direction (e.g. minimal or maximal)

----   
----   
## Post-Rebuttal Update:   
Some concerns have been addressed with some still remaining, including the validity of the interpretation of Fig3 and quality of the manuscript;     
Despite some clarifications, I still think the manuscript unfortunately doesn't quite pass the bar for ICLR.   
There are further serious concerns around the background section of latent diffusion models in this paper that come very close to plagiarism (w.r.t. the previously mentioned work by Fan et al.)!

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Diffusion model uses U-Net model with 2 types of attention-layers: self-attention (pixels x pixels), cross-attention (text x pixels). 

In the authors' approach they use (N-categories x pixels) instead of (text x pixels) for cross-attention. Then they extract both attention outputs: self-attention (pixels x pixels) and cross-attention (N-categories x pixels) and apply matrix-multiplication to get new feature-map (N-categories x pixels). 

Authors extracts attention outputs from the 8th to the 12th layers, and the last three layers, upsample and average all of them across layers and normalize across N-categories. They represent the label-to-value mapping as a learnable random variable. But f.e. since the values need to be smaller when representing depth for indoor scenes but larger for outdoor images, they model this random variable as a learnable codebook C that contains K sets of mappings from label to value. Codebook size is KxNxD.

During training they use 2 loss functions Classification and Regression, and train only:
1. Linear layer 
2. N Concept Embeddings
3. K Codebook Embeddings
while keep frozen both models: Diffusion and ViT-L Clip.

### Strengths
Advantages of your approach:
1. The accuracy of your approach is higher than other few-shot dense prediction methods
2. You get a single model that works well for all 10 tasks, unlike VTM which requires training 5 different models, each for 2 of the 10 tasks
3. Your approach adapts faster to a new task, because you are not training a diffusion model, unlike VPD
4. You provide experimental results showing the need to transform the regression problem into a classification problem to improve accuracy in your case, Figure 3

### Weaknesses
Disadvantage and Limitation:
Based on Table 5, if you have more training data for each sub-stream task, VPD has higher accuracy for most tasks than your approach. But this does not mean that VPD is better than your approach even in this case, since the accuracy is measured In-domain, but not Out-of-domain / Zero-shot.

The limitation of experiments is, do you measure Out-of-domain accuracy, so for the few-shot you use indoor images, while for evaluation you use outdoor images, or indoor images but at least from completely another dataset?

Do you compare number of parameters, and Flops or Latency between your model and VTM, VPD, or ViT-backbones Clip and Dinov2 in your experiments, to be sure that higher accuracy isn't achieved by using larger model?




### Questions
A few questions and notes to make some sentences in the text less ambiguous:

> our method only requires optimizing the input during few-shot adaptation, avoiding changes to the backbone parameters... by only optimizing these input tensors...
> For an input image I and task T , we load its corresponding concept embeddings as inputs to M.

It should be better explained, what is the input in this case, since the input is usually considered to be the "input image". 
While in your case your train:
1. Linear layer 
2. N Concept Embeddings
3. K Codebook Embeddings


> To our knowledge, VTM is the only work that addresses few-shot learning for universal dense prediction. But because they utilize meta-learning to achieve this, they require a significant amount of dense annotations for different tasks.


If VTM only uses 10 samples per task for fine-tuning, then why do you claim it requires a significant amount of dense annotations?

> First, we split the possible range of continuous values in the original D-dimensional output space into B buckets.

What is the difference between your approach and AdaBins[1]?


> As shown in Table. 1, the CLIP and DINOv2 backbones perform worse than the diffusion backbone under the few-shot dense prediction setting. We conjecture that this is partly because the pre-trained diffusion model, being generatively pre-trained, retains more detailed information compared to contrastive loss-based pre-training, making it more suitable for few-shot adaptation.

In some [2] paper Dinov2 pre-trained weights leads to much faster training of models: DiT (diffusion) and SiT. Quote from their paper:
> However, these representations are significantly inferior to those produced by DINOv2.


In another DepthPro[3] paper they use ViT-L Dinov2 pre-trained model and achieve much higher zero-shot accuracy and many times higher speed than diffusion-based Marigold [4] model for depth estimation task.

Are there any assumptions or conclusions why in your case the priors from the diffusion model are better than those from Dinov2, could it be due to the higher computational complexity of your model? Have you compared the sizes and latencies of your approach (Diffusion-model + ViT-Clip) vs Dinov2?


> So, we model this random variable as a learnable codebook C that contains K sets of mappings from label to value, so C ∈ R (K×N×D).

What are K, N and D in this case?


> We include the results of full training set in Table. 5. Although VPD’s performance in the few-shot setting is not strong, with more training data, we can see that its performance improves significantly because it fine-tunes more parameters.

But this does not mean that VPD is better than your approach even in this case (full training set), since the accuracy is measured In-domain, but not Out-of-domain / Zero-shot.
So if you train on Taskonomy and NYUv2, but test on completely different datasets or real-world problems, then it is possible that your approach may be more accurate, while maintaining all the other advantages.


[1] Shariq Farooq Bhat, Ibraheem Alhashim, and PeterWonka. Adabins: Depth estimation using adaptive bins. In CVPR, 2021

[2] Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think Sihyun Yu, Sangkyung Kwak, Huiwon Jang, Jongheon Jeong, Jonathan Huang, Jinwoo Shin, Saining Xie

[3] Depth Pro: Sharp Monocular Metric Depth in Less Than a Second, Aleksei Bochkovskii, Amaël Delaunoy, Hugo Germain, Marcel Santos, Yichao Zhou, Stephan R. Richter, and Vladlen Koltun.

[4] Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, and Konrad Schindler. Repurposing diffusion-based image generators for monocular depth estimation. In CVPR, 2024

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents an innovative approach to adapt pretrained diffusion models for few-shot learning in dense vision tasks, such as depth estimation and semantic segmentation. By reframing dense prediction tasks as codebook-conditioned classification problems, the authors enable the model to handle various tasks without altering internal parameters. They introduce concept and codebook embeddings to enhance task-specific adaptation, achieving notable performance on 12 vision tasks, especially in low-data scenarios.

### Strengths
1. The use of pretrained diffusion models for few-shot dense tasks is sound, leveraging generative models for discriminative tasks without modifying model parameters.
2. The model shows state-of-the-art results across multiple benchmarks, outperforming other few-shot learning methods like VTM and VPD.
3. The approach reduces training data requirements, which could lead to lower computational costs and broader accessibility.

### Weaknesses
1. The use of pretrained diffusion models for few-shot dense tasks is sound, leveraging generative models for discriminative tasks without modifying model parameters.
2. The model shows state-of-the-art results across multiple benchmarks, outperforming other few-shot learning methods like VTM and VPD.
3. The approach reduces training data requirements, which could lead to lower computational costs and broader accessibility.

1. The overall presentation of this paper is poor, making it hard to understand. Specifically, the notations are not clearly defined and some of them may cause confusion, for example, n, N, K.

2. The operations and the rationale behind it are not clearly illustrated. The authors merely describe the the operations step by step using notations. I suggest adding more figures to vividly show how each operation is done.

3. Adapting diffusion models without altering its original structure by prompting is not something new and I believe that the novelty of this paper is limited. More clarifications are required.

4. In Problem Formulation under Method section, the text contains incomplete sentences and unclear phrasing, making it difficult to understand. For instance, " that If T is a depth estimation task, the output is a continuous tensor J ∈ R H×W . preserves the overall motion and semantics of the original video V, while propagating the changes made to the first frame I."

5. Grammar issues are commonly seen in this article, including but not limited to, "a attention mask" in L216

### Questions
Overall, I believe presentation is the most critical issue that needs to be improved. Until then, reviewers can better understand the motivation of the approach and provide constructive feedback.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a general strategy to adapt pre-trained large diffusion models to dense image tasks (both classification and regression) in a few-shot fashion. The tackle this by framing all dense problems as pixel-wise classification and learning a a set of conditioning encodings for the cross attention, that are responsible for the classification. To address the regression tasks, the authors introduce a codebook that serves as a basis to construct the real value output, and pick from that codebook in an image-adaptive fashion.
The results show SoTA performance on Taskonomy and NYUv2 datasets.

### Strengths
- The proposed technique is simple and allows to effectively bring out the knowledge out of a large diffusion model for the classification task.
- SoTA on two standard benchmark datasets.
- The ablation experiments clearly demonstrate the importance of every component.

### Weaknesses
 - It's not clear what the rows in Figure 2 mean.
- Why do you perform inference of a diffusion U-Net with noise at t=200? I would expect the noise to degrade the performance for dense prediction tasks. Why not use a lower level of noise, e.g., t=1? Also during training time t is randomly sampled in [5, 200] range, why not make it consistent with the inference?
- It seems like 10 or 20 examples for training the codebook, the queries and the linear projection layer for clip is a little small. Have you observed overfitting? If so how have you tried addressing it?
- Does figure 3 show training loss? If so, it would be great to look at the validation loss instead.

### Questions
- Why do you perform inference of a diffusion U-Net with noise at t=200? I would expect the noise to degrade the performance for dense prediction tasks. Why not use a lower level of noise, e.g., t=1? Also during training time t is randomly sampled in [5, 200] range, why not make it consistent with the inference?
- It seems like 10 or 20 examples for training the codebook, the queries and the linear projection layer for clip is a little small. Have you observed overfitting? If so how have you tried addressing it?
- Does figure 3 show training loss? If so, it would be great to look at the validation loss instead.

### Soundness
3

### Presentation
3

### Contribution
3
