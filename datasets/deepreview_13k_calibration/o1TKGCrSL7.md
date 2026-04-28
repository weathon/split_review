# Cross-modality debiasing: using language to mitigate sub-population shifts in imaging

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Sub-population shift is a specific type of domain shift that highlights changes in data distribution within specific sub-groups or populations between training and testing. 
Sub-population shift accounts for a significant source of algorithmic bias and calls for distributional robustness. 
Recent studies found inherent distributional robustness in multi-modality foundation models, such as the vision-language model CLIP, yet this robustness is vulnerable through parameter fine-tuning.
In this paper, we propose leveraging the connection of robustness among different modalities and reshaping the distributional robustness of one modality with another. 
Specifically, in the context of the distributional robustness of CLIP, we propose to leverage natural language inputs to debias the image feature representations, to improve worst-case performance on sub-populations.
Our extensive empirical studies show that image representations debiased by natural language can achieve significant performance improvement and reduction of performance instability under sub-population shifts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addressed the sub-population shift problem, denoting a domain shift within specific sub-groups between training and testing, by proposing distributional robustness via language (L-DRO). To employ a CLIP model as a debiased zero-shot classifier, L-DRO incorporates an extra feature adapter for image embeddings, enhancing the entropy of their predictions on spurious attributions. In experiments, the author demonstrates that L-DRO attains the highest worst-case accuracy on the Waterbirds and CelebA dataset, surpassing $\mathcal{X}^2-$DRO, CVaR DRO, and JTT.

### Strengths
- L-DRO exhibits efficient applicability even in scenarios with multiple categories of spurious attributes. 
- Unlike other methods, the training procedure of L-DRO maintains stability across epochs, while competitors experience performance fluctuations.

### Weaknesses
 - One significant concern revolves around the limitation of entropy maximization.
  - As entropy reaches its maximum on a uniform distribution, the analytic solution of $max \ \ell_{ent}$ can be obtained through $(A_{\theta_A} \odot I(\mathbf{x}))^T (T(\hat{t}_1) - T(\hat{t}_2)) = 0$.
  - This occurs when $(A_{\theta_A} \odot I(\mathbf{x})) $ is projected onto the null-space of $(T(\hat{t}_1) - T(\hat{t}_2))$. However, reducing a single rank is insufficient to eliminate the entire spurious representation. Specifically, the method only ensures that the adapted features are orthogonal to the *difference* of the spurious attribute embeddings, which does not guarantee that the adapted features are orthogonal to each spurious attribute embedding individually. This is a critical flaw as the spurious correlation may still be present in the adapted features. The empirical evidence of this limitation can be observed in Table 5 that penalizing semantically correlated sources even increases worst-case accuracy in zero-shot classification.
- Another concern is the relatively modest performance of the proposed method compared to recently published methods. For instance, [1] achieved 92.9% and 88.3% worst-group accuracy on Waterbirds and CelebA, respectively, which is 10% and 30% higher than L-DRO. This underperformance may be attributed to the weak regularization of the entropy regularization. The method's reliance on a single feature adapter might be insufficient to fully disentangle spurious correlations, especially when compared to methods that employ more complex architectures or training strategies.
- Baseline implementation
  - The worst-group accuracy of JTT reported in [1] stands at 86.7% and 81.1% on Waterbirds and CelebA, significantly higher than the results presented in this paper. This discrepancy raises concerns about the implementation and tuning of the baseline methods, as the reported results are notably lower than those in the original paper, suggesting a potential issue with the experimental setup or the hyperparameter selection for the baselines.

### Questions
- Ablation study) Are there any experimental results for the model trained on the loss defined in Eq.(1)?
- Table 3) Could you compare this experiment with the other methods? The table does not convey how L-DRO maintains stability with varying data sizes. 
- Table 4) In some rows, the same source was utilized as the target, resulting in the highest worst-case accuracy. Could you please elaborate on the intention behind this choice and the corresponding performance gain?


- Minor corrections) 
  - Table 1) Would you consider changing one of the parentheses { } in the prompt to [ ] or ( ) so that readers can distinguish?
  - Eq. and equation are redundantly appeared.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper  proposes a method to mitigate subpopulation shifts within one modality (e.g., vision) by leveraging the robustness inherent in another modality (e.g., text). This is achieved by learning a vision feature adaptor, which is trained by minimizing equation (4) with debiasing prompts. This will encourage the inability to distinguish across sub-population while maintaining a representation space consistent with the learned space. Utilizing the debiased vision representation alongside the original task-relevant classification prompt enhances worst-case accuracy and also yields benefits for average accuracy.

### Strengths
1. The paper proposes an effective framework for debiasing subgroup information using aligned representations from Vision Transformers (ViT), which improves the subgroup robustness. This work could inspire future research in this domain.
2. The evaluation is comprehensive and systematic, showcasing effectiveness across multiple datasets and metrics, and providing a comparison with several state-of-the-art baselines. The Table 4 analysis of (dis)alignment within subgroups between the source and target is both innovative and inspiring.
3. The paper is well-organized and clearly presented.

### Weaknesses
1. I’m concerned about the innovation w.r.t. proposing a new strategy for subgroup robustness. The concept of gaining robustness from language modality to enhance another is not novel, and the idea of learning debiased representations—where domain predictability is removed and task predictability is emphasized—is fairly common. Specifically, the method appears to be a fairly straightforward application of existing techniques, adapting a vision feature extractor using a contrastive loss with text prompts to encourage alignment with task-relevant features while suppressing subgroup-specific information. The core idea of using an auxiliary modality to guide debiasing is not new, and the paper does not sufficiently highlight what makes their specific approach substantially different or more effective than existing methods.
2.  While the method is motivated by the general notion that aligned representations from multimodal models can share robustness, the algorithm is restrictive — It primarily facilitates the use of text prompts to learn the debiased representation adapter for improved classification. The reliance on text prompts for debiasing limits the applicability of the method to scenarios where such prompts are readily available or easily designed. Extending the algorithm to incorporate other combinations of modalities may be challenging, particularly for modalities where designing debiasing prompts (e.g., in vision or audio) might be difficult, or where the concept of a 'debiasing prompt' is not well-defined. The paper does not adequately address how the method could be generalized to other modalities or how the debiasing process would work in the absence of easily accessible text prompts.

### Questions
1. Can L-DRO be adapted for combinations of modalities other than vision and language, or does the methodology intrinsically require assistance from the language modality?
2. Table 4 offers interesting insights. In the rows where the source and target are misaligned, the average accuracy is comparable to that of a zero-shot scenario, however, there is a significant divergence in worst-case accuracy. Does this suggest other subgroups are either adversely affected or disproportionately benefited (so that the average scores can remain similar)? Does this imply that the algorithm still works with other influential attributes even if they are not directly related to the target domain?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed to utilize the language description of opposite semantics to mitigate the sub-population shifts via CLIP model. This method doesn't require instance-wise label information but instead encourages CLIP's inability to distinguish across sub-populations using the learned features by maximizing the cross-entropy of classifying images into sub-population semantics.  Experimental result demonstrates performance improvement with the proposed method.

### Strengths
1. Proposed L-DRO doesn't require instance-level labels. It maximizes the cross-entropy loss to discourage image features too close to any biased descriptions. IMO, it's an effective and novel method. 
2. The experiments are very detailed. It studies whether L-DRO can help original CLIP zero-shot inference, how L-DRO is compared with other methods, and whether the L-DRO can help other methods, etc. And the performance of L-DRO is impressive.

### Weaknesses
1. I think the consistency loss might be a bit contradictory to the debiasing loss since the consistency loss encourages the adapter's output to be similar to original image features while the debiasing loss wants the adapter's output to be different from original image features. How do the authors think of / solve the problem? Is there any ablation on the coefficient of the consistency loss?

2. It's interesting that L-DRO can also improve average loss in Tab 1. Can authors further explain on this phenomenon?

### Questions
1. Shouldn't the `y_p` in `{y_p, y_n} := {blond, not blond}` in the second paragraph of Sec4 be `y_b` to be coherent with the notation in the next paragraph?

================\
After reading other reviews and the authors' responses, I'd like to lower my rating a bit to 5.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
*Note that this manuscript was previously submitted to NeurIPS 2023, where it was withdrawn following scores that would have likely led to rejection. I was assigned a reviewer for this paper at the time as well, and from what I can tell the paper remains entirely unchanged. Hence, I am going to take the liberty of resubmitting my previous review entirely unchanged as well.*

This paper addresses the problem of subgroup robustness, i.e., the concern that a model shows markedly worse performance for specific subpopulations. Note that a subpopulation here is defined across both label and input space. Mathematically this translates to $\min_\theta \sup_{Q\in\mathcal{Q}}\mathbb{E}_{Z\sim Q}[\ell(\theta,Z)]$ where $\mathcal{Q}$ is a set of subpopulations and $\ell$ is the loss for a given sample, $Z$, and parameters $\theta$. That is, the goal is to maximize the worst-case performance of the classifier over all subpopulations.

The suggested approach in this paper relies on a vision-language model: The language model is used to describe the subpopulations in input space. For example, if subpopulations are defined as blond/not blond (label space) men/women (input space), then "a photo of a man/woman" ("debiasing prompt") is fed and used to generate embeddings $T(\hat{t}_i)$ (see equation 4). An adapter $A$ is then trained to "debias" the vision embeddings, which means that the embeddings lie equally far from all $T(\hat{y}_i)$ (e.g., it is no longer possible to tell the gender from the image features). At the same time, a consistency loss using the un-adapted features ensures that embeddings don't collapse.

The idea here is that if the classes are balanced (e.g., there are as many blond as not blond people in the dataset) and the vision features are debiased (e.g., there is no more information in there about gender) then the performance of the classifier must end up being equal across all of the (four) subpopulations (blond/not blond men/women).

Experiments show significant improvements in the worst-case accuracy for all models except ViT-L/14 on the CelebA dataset (subpopulations are blond/not blond men/women) and the Waterbirds dataset (subpopulations are waterfowl/landfowl in the air/on land). Experiments show that several hundred/thousand examples are needed to see improvements over the baseline (i.e., no debiasing).

A few other experiments show that the method can be used in conjunction with other methods (e.g., CVaR-DRO and $\chi^2$-DRO) and that it is possible to debias multiple attributes at the same time.

### Strengths
The proposed idea is appealing in its simplicity: A vision-language model can be used to describe which attributes should be protected/robust (e.g., male/female) and an adapter is quite directly trained to remove these features entirely from the image features.

The experimental results are encouraging. Improvements seem reliant on prompt engineering and not all improvements are equally large, but they seem consistent.

### Weaknesses
The main strength of the method also seems like a weakness: It relies on a multi-modal model to provide the zero-shot learning capability needed to identify subpopulations in the label space. This makes the method pretty specific.

A concern regarding the applicability of this method is that the experiments show that this approach requires significant prompt engineering. But the assumption in this paper seems to be that there are no labels available (e.g., no male/female labels). That means that it wouldn't be possible to compare the performance of prompts like it was done, e.g., in table 1, right?

All in all, I don't think this is a bad paper. The idea is clean and simple, and the results show that it works. However, I'm wondering if the idea is fleshed out enough, and it leaves me with several practical questions: How does one select a debiasing prompt when there is no ground truth labels? Can I use multiple debiasing prompts? How do I know if I have enough data? I am not sure if all these questions should be left to future work (I think these are more important than questions about how L-DRO interacts with other methods, for example). This is why I am recommending a weak reject.

### Questions
Some questions:

* Did the authors explore why their model fails on ViT-L/14? This seems like useful information for practitioners. For example, can they only expect this model to work on smaller models?
* My understanding is that the results in table 6 should be comparable to the 3rd and 7th rows in table 2? There zero-shot learning gets 70.6% worst-case performance. It seems that $\chi^2$-DRO is the only baseline that gets higher than this (but with huge variance)? It seems odd that all the DRO methods do worse than not doing anything at all?
* Assuming that it's not possible for a practitioner to select the best prompt based on validation results (since no ground truth labels are available for the subpopulations) it would be useful to know if the method can be extended to support multiple debiasing texts. That is, rather than having to select a single debiasing prompt and hope it is correct, the user could just give many different ones, increasing the chances of having good results (since the spread is quite large, as is evident in table 1).
* I'm surprised at the results in table 3, which seem to suggest that if the dataset isn't large enough, the proposed method actually harms the results. I would find it useful if the authors could (1) provide insight into why this is the case, and (2) provide some guidance on how a practitioner is supposed to know whether or not they have enough data available for this method to apply.

Minor things:

* It seems odd that all the prompts selected are grammatically incorrect. How does the model perform with correct phrases such as "a photo of a blond/non-blond person"/"person who is blond/not blond" and "a photo of a man/woman"/"male/female person"?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
