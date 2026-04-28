# Spurious Feature Diversification Improves Out-of-distribution Generalization

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8

## Abstract
Generalization to out-of-distribution (OOD) data is a critical challenge in machine learning. Ensemble-based methods, like weight space ensembles that interpolate model parameters, have been shown to achieve superior OOD performance. However, the underlying mechanism for their effectiveness remains unclear. 

In this study, we closely examine WiSE-FT, a popular weight space ensemble method that interpolates between a pre-trained and a fine-tuned model. We observe an unexpected ``FalseFalseTrue" phenomenon, in which WiSE-FT successfully corrects many cases where each individual model makes incorrect predictions, which contributes significantly to its OOD effectiveness. To gain further insights, we conduct theoretical analysis in a multi-class setting with a large number of spurious features. Our analysis predicts the above phenomenon and it further shows that ensemble-based models reduce prediction errors in the OOD settings by utilizing a more diverse set of spurious features. Contrary to the conventional wisdom that focuses on learning invariant features for better OOD performance, our findings suggest that incorporating a large number of diverse spurious features weakens their individual contributions, leading to improved overall OOD generalization performance. Additionally, our findings provide the first explanation for the mysterious phenomenon of weight space ensembles outperforming output space ensembles in OOD. Empirically we demonstrate the effectiveness of utilizing diverse spurious features on a MultiColorMNIST dataset, and our experimental results are consistent with the theoretical analysis. 

Building upon the new theoretical insights into the efficacy of ensemble methods, we further identify an issue of WiSE-FT caused by the overconfidence of fine-tuned models in OOD situations. This overconfidence magnifies the fine-tuned model's incorrect prediction, leading to deteriorated OOD ensemble performance. To remedy this problem, we propose a novel method called BAlaNced averaGing (BANG) to mitigate the overconfidence problem, which significantly enhances the OOD performance of WiSE-FT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper analyses ensembling to improve OOD robustness. They find that the individually incorrect models can average out to be correct when, loosely the models do depend on the invariant feature sufficiently in both models. They setup a linear data generating process and provide some evidence of when linear

### Strengths
- The paper studies an interesting phenomenon where individually incorrect models can be made correct. The idea is related to boosting, but the different models should rely on different spurious features.

 - The experiments are direct and encouraging, although not directly connected to the theory (WiSE-FT and WSE seem to not be compatible because the methods that work for WSE cannot be applied directly to WISE-FT.

 - The theoretical setup is interesting and does confirm some of the intuition of ensembling models that are diverse in their spuriousness.

### Weaknesses
The paper's weight space ensemble is too simple, when considering overconfident models. WiSE-FT ensembles all the weights, not just the linear layer. So it is unclear how the scaling can be assumed to be a simple multiplier on the linear layer.

This is a sizeable gap because WiSE-FT is weight space ensembling of very specific models (good OOD/bad ID and good ID/bad OOD). This is not reflected in the paper except loosely when they say low overlap is good weight space ensembles. The authors acknowledge this even when they talk about their method "However, this method can not be directly applied to WiSE-FT since WiSE-FT ensemble model weights instead of the outputs."

The paper does focus a lot of output ensembling, which is not known to work as well as WiSE-FT. In that case, there is no discussion of boosting, which seems to have the same flavor (especially when forcing models to rely on different features).


It is also unclear that Mix-up and label-smoothing have singular effects on the confidence, they also regularize. So BANG is really just finetuning with MIXup/LS and then doing WiSE-FT. A more direct correction of confidence would be the right one, like doing temperature scaling for each checkpoint during finetuning and then running WiSE-FT

### Questions
See weakneses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper examines WiSE-FT to understand how ensemble based models improve OOD performance. First, a “FalseFalseTrue” phenomenon is observed, where the ensembled model predicts samples correctly even when both the pretrained and finetuned model that are ensembled predict the samples incorrectly. The paper suggests an explanation for this related to ensembled models making use of diverse sparse features, and this reducing the influence of any given sparse feature below that of invariant features. This is then shown to be the case theoretically, and on a synthetic empirical setting. Finally, the paper makes the related observation that successful ensembling requires balanced models (so that the ensembled model benefts from diverse sparse features). This motivates a recommendation to finetune models with mixup and label smoothing to decrease confidence, and the resulting ensemble model is called BANG. BANG shows empirical performance stronger than that of WiSE-FT.

### Strengths
* Weight space ensembled models have been of great interest for OOD generalization and an explanation of how these models improve OOD performance beyond both pretrained and finetuned models—which this paper seeks to provide—is valuable.
* The FalseFalseTrue phenomenon is unexpected and interesting, especially since the FalseFalseTrue ratio is comparable to the total overall improvement provided by WiSE-FT. 
* The analysis provides a partial mechanistic explanation for how EBM improves OOD performance beyond pretrained/finetuned models via diverse spurious features.
* The MultiColorMNIST experiment clearly demonstrates the value of diverse spurious features for the OOD performance of EBM.
* The observation that imbalanced models hurt EBM is actionable, and the algorithmic recommendation of BANG leads to OOD accuracy improvements over WiSE-FT.

### Weaknesses
I am not convinced that the performance gains of BANG are mainly due to better calibration as claimed in the paper and not because mixup/LS significantly improves OOD performance of finetuned models. While appendix E.6 shows that there are “oracle weights” to scale standard finetuned models when ensembling, it may not be that BANG models are bringing improvements for the same reason.

One way to demonstrate this would be analysis similar to “accuracy on the line” where there are models finetuned with mixup and LS at the same OOD accuracy as standard finetuned models. It would strengthen the claims of Section 4 if the BANG models in this setting outperform WiSE-FT even with finetuned models at the same OOD performance.

### Questions
* In tables 2 and 7, we see that on the in-distribution ImageNet test set, finetuned(Mixup+LS) models outperform standard finetuned models (by ~1.5%), but BANG does not outperform WiSE-FT. Is there intuition for what BANG is doing in the in-distribution setting that explains this?

* It would be good to see “FalseFalseTrue” analysis (like figure 2 left) of BANG models compared to WiSE-FT models. It appears from appendix E.6 that BANG models may be helpful in a “TrueFalseTrue” setting where the finetuned model was originally incorrect and overconfident. Does calibration help in the FalseFalseTrue setting?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the WiSE-FT method's ability to enhance OOD performance in machine learning and identifies a notable "FalseFalseTrue" phenomenon that shows WiSE-FT correcting both individual model errors. Motivated by this, the authors conduct theoretical analysis in a multi-class setting. The theoretical results suggest that using diverse spurious features in ensemble methods improves OOD generalization, contradicting the traditional emphasis on invariant features. This theory is validated with experiments on the MultiColorMNIST dataset. Meanwhile, the authors also identify a weakness of WiSE-FT due to its overconfidence in fine-tuned models under OOD data. Based on that, the authors proposed a new method BANG that addresses the overconfidence problem and reaches better OOD performance.

### Strengths
1. The paper is well-written with a clear structure. Motivations are well-explained on why the authors study the problem and the contributions of this study are well discussed. The illustrative examples are helpful in understanding the concepts. Overall, it is easy to follow the logic and flow of the paper.
2. Theoretical results are solid and well-organized. The authors made the theoretical settings clear: definitions are well-explained and assumptions are clear. Proofs of the theory are sound as far as I read into.
3. Empirical results support the theoretical findings. The proposed method is also shown to be effective on the ImageNet dataset.

### Weaknesses
I have the following questions regarding the empirical results
1. The paper considers the setting of ensembling two individual models (FalseFalseTrue) and show that such ensemble indeed improves over single model's OOD performance on MultiColorMNIST. Is this finding generalizable to ensembles of more than two models? If we increase the number of models in Table 1, could the ensemble's performance potentially see further improvement?
2. For datasets that specifically focus on spurious correlations (Waterbirds), there will be only one strong spurious feature (background) in the training data. In such a case, will the ensemble method still be effective? If not, could we manually adding new spurious features to the training data (color, rotation, scale, ect.) and apply ensemble methods like BANG to improve the model's performance?

### Questions
See in weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
