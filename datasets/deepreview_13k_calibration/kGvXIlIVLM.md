# Toward Guidance-Free AR Visual Generation via Condition Contrastive Alignment

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 6, 8, 8

## Abstract
Classifier-Free Guidance (CFG) is a critical technique for enhancing the sample quality of visual generative models. However, in autoregressive (AR) multi-modal generation, CFG introduces design inconsistencies between language and visual content, contradicting the design philosophy of unifying different modalities for visual AR. Motivated by language model alignment methods, we propose \textit{Condition Contrastive Alignment} (CCA) to facilitate guidance-free AR visual generation with high performance and analyze its theoretical connection with guided sampling methods. Unlike guidance methods that alter the sampling process to achieve the ideal sampling distribution, CCA directly fine-tunes pretrained models to fit the \textit{same} distribution target. Experimental results show that CCA can significantly enhance the guidance-free performance of all tested models with just one epoch of fine-tuning ($\sim$1\% of pretraining epochs) on the pretraining dataset, on par with guided sampling methods. This largely removes the need for guided sampling in AR visual generation and cuts the sampling cost by half. Moreover, by adjusting training parameters, CCA can achieve trade-offs between sample diversity and fidelity similar to CFG. This experimentally confirms the strong theoretical connection between language-targeted alignment and visual-targeted guidance methods, unifying two previously independent research fields.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To bridge the gap between autoregressive language and visual generation, this work targets at removing the need of CFG in AR image generation, therefore unifying the sampling scheme and reducing the sampling cost. The authors choose to fine-tuning the pretrained AR models with the contrastive alignment loss. The intuition behind the contrastive alignment is to maximize the likelihood of positive conditions and minimize the likelihood of the negative conditions. More discussion with classifier guidance and classifier-free guidance is also illustrated, providing more insights for difference sampling schemes. Experiments are conducted on autoregressive visual generation methods like LlamaGen and VAR.

### Strengths
* The problem of sampling schemes for autoregressive models is fundamental and should be explored.

* Detailed illustrations are provided. For example, the authors review preliminaries, give formal derivation, and also the practical implementation.

* It is interesting to see that CCA provides extra gain based on CFG.

### Weaknesses
 * For the motivation, one confusion to me is why removing the CFG is necessary for unifying visual and language generation. I mean, there may no influence for sampling them with slightly different schemes? I recognize that introducing CCA can reduce the half cost. But it is achieved at the cost of sampling quality as demonstrated in Table 2.

* To my understanding, the model should be fine-tuned for each lambda and beta individually. Is that correct? If so, this will be a big limitation since other sampling schemes can adjust trade-offs during inference, which is more flexible.

### Questions
Could the authors clarify the necessity of removing CFG, except sampling cost?

Should the model be fine-tuned individually for each lambda and beta?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes CCA to replace CFG in auto-regressive models, which saves sampling costs while keeps the sampling performance on part with CFG. And this paper gives the theoretical connection

### Strengths
1. The theoretical derivation is clear and logically structured, allowing for a comprehensive understanding of the underlying concepts.
2. The authors have conducted a thorough series of experiments that effectively validate the theoretical claims made in the paper.

### Weaknesses
1. concerns mentioned in questions.
2. lack of explanation for notations when first mentioned, such as $p_{\theta}$  in line 168, $\sigma$ in line 189

### Questions
1. Your pipeline requires only 1% of the pre-trained epochs. However, could you provide insights into the corresponding GPU memory usage during training in comparison to CFG?
2. Regarding the proposed loss function in Equation 11, what is its convergence speed?
3. A more detailed inquiry: in line 372, the experiments do not utilize a common default value of s=7.5, for Classifier-Free Guidance (CFG). Could you elaborate on the reason behind this choice?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces CCA which a new alternative to CFG to finetune autoregressive image generation models so that they work like the sampling model used by CFG during inference. The key idea lies in modeling the conditional residual by learning to maximize the likelihood of an image given positive conditions, while minimizing the likelihood given negative conditions. In my opinion, it can be intuitively seen as a way to absorbing the benefits of the unconditional model (which complements the conditional model as demonstrated by CFG) right into single conditional model inference. The resulting approach is more elegant than CFG and is more efficient than CFG because it only requires 1x sampling cost. Furthermore, it can be paired with CFG for additional inference quality boost.

### Strengths
- The paper tackles an important but often overlooked problem in autoregressive image generation.

- The methodology section of the paper is mostly well written except that it lacks key information in certain areas. Overall, it provides strong motivations and reasonable derivations based on prior work that lead to the proposed CCA method. 

- The experimental results using strong AR visual generation models (LLamaGen, VAT) as baselines on ImageNet are very promising. It is impressive that without any additional inference costs (and a bit more training/finetuning costs), CCA can bring significant improvements to the FID and IS metrics. When paired with CFG, improved FIDs can be achieved.

### Weaknesses
 - Some important details are missing in the paper, such as how positive and negative data samples are chosen for CCA training. Sec 3.2 only briefly mentions that and Fig. 2 shows something about it without any verbal explanation. It is unclear if we just use the ImageNet labels as the sole criterion for constructing positives and negatives or there’s some other strategy being used. In Sec 5.4, it’s mentioned that certain unconditional data samples are used as positives but it is not clear how exactly that works. Without this key information, it may be hard for readers to understand how and why CCA works.

- Fig 2‘s caption is totally uninformative. There should be a caption describing the method in detail.

- CCA uses models pretrained with CFG training (i.e., condition dropout). For CCA to work, is there a strong requirement on this? What is the relationship of CFG pretraining and CCA finetuning?

- When CCA is combined with CFG, IS becomes worse while FID becomes better. Can the authors explain this phenomenon? 

- The proposed method resembles CLIP-like contrastive loss. I wonder if it can only work if the training batch size is large enough.

### Questions
Please refer to weaknesses

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose condition contrastive alignment (CCA), replacing classifier-free guidance (CFG). Based on CCA, they implement a guidance-free AR visual generation and unifies the alignment mechanism between language and visual models. Compared with models using CFG, generation models with CCA can reduce the sampling cost by half. To implement CCA, the authors transform CFG into a contrastive learning formulation and train the sampling model only with a fine-tuning loss. In addition, they conduct extensive experiments to validate the effectiveness of the proposed method.

### Strengths
+ This paper proposes condition contrastive alignment (CCA) for a guidance-free AR visual generation. Concretely, the authors transform CFG into a contrastive learning formulation and train the sampling model only with a fine-tuning loss. Thus, CCA is simple and easy to implement.
+ The proposed method can unifies the alignment mechanism between language and visual models.  Besides, unlike CFG, generation models with CCA can reduce the sampling cost by half, which is a practical technique.
+ The authors conduct extensive experiments to validate the proposed method. Compared with CFG, CCA achieves comparable performance in FID score under different visual models.

### Weaknesses
- Training cost. CCA needs one training epoch to get ideal performance. The training cost is negligible for ImageNet datasets. But for existing large visual generation models (like SD3), the training data is huge. The cost of training one epoch with large-scale datasets is expensive. Is there a practical solution to reduce the cost?
- Optimal $\beta$ and $\lambda$. To obtain the optimal values for $\beta$ and $\lambda$, we need to train CCA many times. The cost of this process is large. Is there a potential guideline to mitigate the substantial cost of finding optimal $\beta$ and $\lambda$?
- Negative samples in CCA. To my knowledge, negative samples have a large effect on the performance of contrastive learning. For CCA, it is based on contrastive learning framework. The selection of negative samples affects the performance of CCA largely. Is there a selection mechanisms of  negative samples?
- Implementation about integration of CCA and CFG. I do not understand the implementation completely due to lacks of details. It is necessary to clarify the implementation with more details.
- IS score. As shown in Figure 1 and Figure 6, IS score starts to degrade when model size is beyond a certain size, such as LlamaGen>775M. To my knowledge, this is an unusual phenomenon. Larger model means better IS score.

### Questions
To make the proposed method better, the authors need to provide practical solutions to some issues like training cost with large-scale datasets.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a novel method for fine-tuning auto-regressive models to enable guidance-free sampling from the same distribution that would be sampled if classifier-free guidance were used. The training objective is derived by noise contrastive estimation in which genuine pairs of condition and data are used as positive while random pairs are negative ones. The experimental results show that just one epoch fine-tuning with the proposed method greatly improves the performance of the guidance-free sampling.

### Strengths
- The motivation of this study is clear and should be important to make auto-regressive models efficiently generate high-quality visual contents. As of 2024, CFG is commonly used for auto-regressive models to achieve high-quality image generation, while it doubles the computational cost of the generation process. How to get rid of the necessity of CFG would be an important problem especially for practical applications.

- The derivation of the proposed method, particularly Eq. (10) and (11), is elegant. The theoretical connection with guidance-based sampling is clear, and the practical implementation is reasonable.

- The experimental results validate the advantage of the proposed method; it greatly boosts the performance of guidance-free sampling. Although its performance is slightly worse than that of sampling with CFG, it would be acceptable in some practical applications considering that the computational cost for the generation is halved.

- The manuscript is well-written and easy to follow.

### Weaknesses
 - I do not find any crucial weakness or major concerns on this paper. The followings are just minor points.
  - As the proposed method requires to fix a target distribution represented by beta, it cannot control the fidelity-diversity trade-off in the inference phase, which might reduce some flexibility compared with CFG.
    - It might be worth exploring whether the model could be extended to accept additional condition beta to work with various beta in the inference phase, similar to the approach in the distillation of guided diffusion models [R1]. However, it should be non-trivial how to achieve such extention in AR models.

      [R1] "On Distillation of Guided Diffusion Models," CVPR 2023.
  - It would be beneficial if the author could discuss how stable the proposed method is. As the negative pairs in Eq. (12) are random pairs of x and c, p(x|c) appeared in the loss computation could have very small values, which might cause numerical instability during the fine-tuning.

### Questions
- It is not clearly descirbed why the performance with varying lambda leads to a similar behaviour to that with varying beta. For example, why has IS score been improved by increasing the value of lambda(namely, overweighing the loss on negative pairs)?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This submission proposes an alternative way to achieve classifier-free guidance (CFG) for visual autoregressive model, by directly finetuning the model, which avoids an extra forward pass when deploying CFG. The experiment results show the proposed finetuning method introduces huge performance gain.

### Strengths
- The problem the submission addresses has very high practical value to deploying the visual autoregressive model.
- The algorithm derivation gives a clear explanation about the methods. And the derived training loss function is very concise, which is easy to train.
- The performance gain is huge, on both generation quality and diversity.
- Experimental section is thorough. Additionally, sec 5.3 is informative and appreciated, especially unlearning.

### Weaknesses
In short, this is a good work. I only have one question about the training loss function, as $\beta$ is expected to be responsible for CFG degree. But the experimental results show that $\lambda$ actually dominates the CFG controllability, any clue about it?

One open question is, will the proposed method also improve the directional autoregressive model, a.k.a., Masked Generative Models such as MaskGIT and MAGE. Or, to think even more boldly, will the method still applicable to (continuous) diffusion models, since MaskGIT could be regarded as a discrete diffusion model.

### Questions
Please check the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
