# Patch-Prompt Aligned Bayesian Prompt Tuning for Vision-Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
For downstream applications of vision-language pre-trained models, there has been significant interest in constructing effective prompts. Existing works on prompt engineering, which either require laborious manual designs or optimize the prompt tuning as a point estimation problem, may fail to describe diverse characteristics of categories and limit their applications. We introduce a Bayesian probabilistic resolution to prompt tuning, where the label-specific stochastic prompts are generated hierarchically by first sampling a latent vector from an underlying distribution and then employing a lightweight generative model. Importantly, we semantically regularize the tuning process by minimizing the statistical distance between the visual patches and linguistic prompts, which pushes the stochastic label representations to faithfully capture diverse visual concepts, instead of overfitting the training categories. We evaluate the effectiveness of our approach on four tasks: few-shot image recognition, base-to-new generalization, dataset transfer learning, and domain shifts. Extensive results over 15 datasets show promising transferability and generalization performance of our proposed model, both quantitatively and qualitatively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes to hierarchically generate the label-specific stochastic prompts using generative modules from sampled noisy latent vector. Then, a conditional transport framework is employed to establish a relationship between visual patches and textual prompts. Several experimens are performed in few-shot, transfer learning, domain generalization, and base-2-new manners using ViT-B/16 and RN50 as the backbones.

### Strengths
1. The idea of using the noisy latent vector combined with deterministic mapping to generate diverse prompts for alleviating the overfitting issue in vision language prompt learning is meaningful.
2. The paper is well-organized and easy to follow.

### Weaknesses
1. In Fig.3, the reported PLOT using ViT-B/16 is run by this submission. However, this result is much different from the one reported by PLOT on github (https://github.com/CHENGY12/PLOT/tree/main/plot-pp). According to these results, PLOT achieves better few-shot performance when using the ViT-B/16 as the visual backbone. 
2. The PLOT base to new experiment using ViT-B/16 reproduced in this paper also lacks credibility, considering that the performance of the proposed method and PLOT are comparable when similar experiments using RN50 as the visual backbone are performed.
3. In my view, the primary reference for this paper is PLOT, and therefore it needs to be compared to PLOT as exhaustively as possible. However, this paper lacks some important comparisons. For example, PLOT mainly employs RN50 as the visual backbone, although this paper has added experiments in few-shot and base-2-new manners using RN50 as the backbones, the domain generalization experiments using RN50 are missing. 
4. I appreciate the proposed Stochastic Prompts Generation, however, the conditional transport seems not meaningful. In the main text, the author only claims that OT needs two stages. However, the first stage of OT is not time-costly in the CoOp-related experiments. So, what is the main contribution of using CT instead of OT?
5. The paper lacks an ablation study on the proposed conditional transport and optimal transport (OT). We need to compare experiments using SPG and CT with experiments using SPG and OT to determine whether the proposed CT is meaningful.
6. In PLOT, the number of prompts is set to 4. However, this paper only uses C for the number in Eq. (4) without stating the exact value in the experimental details, which may result in unfair comparisons. I also find that the Moter Carlo sampling number is set to 20 as the default setting.  Does this Moter Carlo sampling number correspond to the number of PLOT prompts? If yes, this is unfair, please conduct fair experiments and explain the reason. 
7. The learnable parameters shown in Table C.9 indicate that the proposed approach uses much more parmas compared with CoCoOp and PLOT. I would like to know the composition of these parameters and whether the additional parameters rather than the suggested method are the reason for the performance improvement.
8. Multi-modal approaches such as CoPrompt[1], MaPLE[2], and VioLET[3] can achieve much better base-to-new performacne using ViT-B/16 as the visual backbone. I understand that the proposed approach only tunes the language branch, however, I wonder whether the proposed approach can further improve the multi-modal approaches.
9. From the ablation studies in Table.1, P-Prompt shows better performance compared to B-Prompt, while in Figure.7(a), B-Prompt exhibits better few-shot performance. These results indicate that the proposed CT is useful for generalization while SPG accounts for better supervised performance. This may not be intuitive, as the proposed Bayesian approach is more capable of introducing uncertainty thereby enhancing generalization performance and reducing overfitting (also mentioned in Sec. 2.2).

### Questions
The proposed method claims to be generalizable and can solve the overfitting problem well. Then I am curious, when we increase the number of training epochs to 50 or even 200 in base-to-new experiments, does it affect the generalization performance?

### Soundness
2 fair

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
This paper presents a Bayesian probabilistic approach to prompt tuning. In this method, label-specific stochastic prompts are generated hierarchically. This involves sampling a latent vector from an underlying distribution and utilizing a lightweight generative model. Additionally, a regularization technique is introduced to minimize the statistical distance between visual patches and linguistic prompts.

### Strengths
[$\textbf{Good Presentation}$] The paper is well-written and easy to follow.

[$\textbf{Effectiveness}$] Experiments have shown that the proposed method outperforms baseline methods.

### Weaknesses
[$\textbf{Lack of Novelty}$] The concept of incorporating Bayesian neural networks for prompt learning was previously presented in "Improving Zero-Shot Generalization for CLIP with Synthesized Prompts, ICCV23." This diminishes the novelty of Bayesian prompt tuning. It would be nice to differ these two works. Also, the regularization seems to be a simple utilization of conditional transport.

[$\textbf{Missed Baselines and Weak Performance}$] Some SOTA methods are missed in experiments, e.g., “Improving Zero-Shot Generalization for CLIP with Synthesized Prompts, ICCV23.”, “Self-regulating Prompts: Foundational Model Adaptation without Forgetting, ICCV23” and “MaPLe: Multi-modal Prompt Learning, CVPR23”. It is not adequate to simply compare an old baseline CoCoOp only. More importantly, comparing with these SOTA methods, the performance of the proposed methods is much worse.

[$\textbf{Some Suggestions}$] The ablation study should be conducted on ImageNet as it would nice to see the effectiveness of the proposed on the most challenging dataset.

### Questions
Please refer to the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method to improve the prompt engineering problem. They generate stochastic prompts via a random sampled inputs and a learnable sef-attention generator. Then aligns the text embeddings with the image embeddings using bidirectional distance. The model in being trained by optimizing the ELBO. The experimental results and ablation studies showing the effectiveness of the proposed method.

### Strengths
- The paper is well-written and easy to understand
- The idea of generating label-specific stochastic prompts is novel
- Results on multiple tasks validates the effectiveness of the proposed method

### Weaknesses
 - I'm thinking about the motivations of generating stochastic prompts. On one hand, there are different ways to describe a given class (e.g. "a dog that chews bones", "puppies are good friends of people"). On the other hand, we can always combine multiple prompts into one single, long prompt. Is it possible that "stochastic" method works just because it provides more input variance in the training, therefore reduces the overfitting? (Especially finetuning data is limited)

 - In figure 7 (b), I see not all randomly generated prompt correlates to the class label well (e.g. visualizations of the dog image). Are they any randomness in inference? How about the variances?

### Questions
- In figure 7 (b), I see not all randomly generated prompt correlates to the class label well (e.g. visualizations of the dog image). Are they any randomness in inference? How about the variances?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
he paper presents a novel approach to prompt tuning in Vision and Language Models (VLM), where a distribution over prompts is learned in a per-class fashion. For a target class, the prompt embeddings are drawn from a latent distribution parameterized by a small learnable MLP, similar to (Derakhshani et al., 2022). However, contrary to (Derakhshani et al., 2022), the prompts are learned for each image class, and they are computed from patch embeddings rather than from the holistic image. In addition to the extended distribution over the prompts, the paper proposes an optimal-transport loss to align the image and text features. A broad set of experiments are conducted to showcase the benefits of the proposed approach w.r.t. CoOp and CoCoOp.

### Strengths
The paper is technically sound and motivated. On the one side, extending the pool of prompts is appealing to improve generalization to new classes. On the other hand, the idea of using optimal transport to align the image and text probabilities sounds novel to me, which brings a new optimization technique to the domain of vision and language pre-training with good results.

The experiments follow the standard protocols providing superior performance to CoOp and CoCoOp, showcasing the importance of having a proper set of prompts from which one can sample in task-specific manner.

The paper is well documented, and while the writing can be improved (see below), the narrative is easy to follow and understand. The authors provide code with their submission that hopefully will be made publicly available for reproducibility.

### Weaknesses
While acknowledging the novelty of extending the sampling pool of prompts to be patch-specific and class-specific, I wonder to which extend such novelty is just marginal w.r.t. the framework proposed by Derakshani et al. In my opinion, this extension is rather marginal and while the authors have the merit to be the first to apply such extension, the technical contribution in this sense is small to me.

The use of the optimal transport is in general well motivated, but I am not sure if the results shown in Table 1 and Figure 7 (a) are a bit worrying in the sense that adding such optimization loss results in many cases detrimental. While novel, it is worth questioning whether its contribution is significant.

I wonder why the comparisons against state of the art works dismiss ProDA (Lu et al 2022) and Derakshhani et al. 2022).

The writing needs to be improved, while the narrative is well threaded, I believe the paper can benefit from proof-reading.

I might have missed this point but a question I have is to which extend having per-class prompts is beneficial and how this is applied to the new classes. A proper description of such scenario for inference would be desirable.

### Questions
All my concerns are addressed above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
