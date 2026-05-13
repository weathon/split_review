# Minifinetuning: Low-Data Generation Domain Adaptation through Corrective Self-Distillation

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
Finetuning language models for a new domain inevitably leads to the deterioration of their general performance.
This becomes more pronounced the more limited the finetuning data resource.

We introduce minifinetuning (MFT), a method for language model domain adaptation that considerably reduces the effects of overfitting-induced degeneralization in low-data settings and which does so in the absence of any pre-training data for replay.
MFT demonstrates 2-10x more favourable specialization-to-degeneralization ratios than standard finetuning across a wide range of models and domains and exhibits an intrinsic robustness to overfitting when data in the new domain is scarce and down to as little as 500 samples.

Employing corrective self-distillation that is individualized on the sample level, MFT outperforms parameter-efficient finetuning methods, demonstrates replay-like forgetting mitigation properties, and is composable with either for a combined effect.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents an algorithm for domain adaptation of large language models (LLMs), that mitigates catastrophic forgetting on the original pre-training tasks, without access to any of the pre-training data.

The method is a form of self-distillation, where pseudo-targets ("corrected" targets) are created by linearly combining the probability vector of the pre-trained model with the one-hot vector representing the new target, with a coefficient chosen so that the target token is the most probable one (by a margin), while minimizing the effect on the other tokens' predictions.

Extensive experiments on different families of models, and different sizes within a model family, show this method consistently gives a lower "degeneralization" rate (perplexity change on the original, general domain), and better generalization / degeneralization trade-off, compared to other methods that do not use data from the general domain (fine-tuning, different low-rank adapters).
Only the Replay method (which uses original training data) outperforms it.
Ablations are conducted to show that all the different mechanisms involved in this method are necessary to reach this performance.

### Strengths
Originality
--------------
1. To my knowledge, this is the first method specifically design to fine-tune off-the-shelf pretrained LLMs on a different domain, without having access to their training distribution.
2. The specific formulas derived for token-wise adaptation, including the special case of the original model's maximum prediction being already right, are not obvious.

Quality
----------
1. The various parts of the algorithm are well justified
2. Main experiments are comprehensive, across model types and sizes, and support the paper's conclusions
3. Additional experiments, like weeping over capacity of low-rank algorithms, and the margin parameter for MFT), further demonstrate the behavior of the metrics used (DG, DG/S) and algorithms compared
4. Incremental ablation showcase how the different parts of the algorithm proposed influence generalization and degeneralization.

Clarity
---------
The paper is extremely clear and well presented. Graphs give a more intuitive feeling of how the "correction" affects probabilities, and the derivation of coefficients in section 2 should be enough to re-implement the method.

Significance
----------------
A straightforward, reasonably efficient method to avoid over-fitting on a small SFT set is valuable, as LLMs adapted for different domain is an increasingly popular use case. The fact it is compatible with low-rank adapters (and can be combined with them) is also a point for its adoption.

### Weaknesses
Quality
----------
I understand why Replay had to be included as a baseline, despite its advantage, but I'm wondering if a variant of Replay using only synthetic data sampled from the pre-trained model could have made the point stronger that the actual training data is necessary, vs. Replay acting as a regularizer. Specifically, it's unclear if the benefit of Replay comes from the specific data points or simply from the regularization effect of training on a larger, more diverse dataset, even if that dataset is not perfectly representative of the original pre-training data.

Minor points
-----------------
1. l. 222: Basline -> Baseline
2. l. 527: the citation for the Gemma paper shows up as "Team et al.", which is not really informative. Maybe update the bibtex to show "Gemma Team" or something.
3. Similarly, use braces in bibtex entries so that capitals are preserved, e.g., l. 609, `{OpenELM}` would avoid it being rendered as "Openelm". Same for "rlhf", "llm", "lora", etc.

### Questions
1. I'm wondering how a baseline closer to Replay, but using synthetic data sampled from the pre-trained model, would perform. I understand that it would be major additional experiments to perform, and I'm not asking for that, but I'm wondering if it's something you've considered addressing, or if there's literature of something similar being attempted. Intuitively, it could help further mitigating the degeneralization further away from the domain-specific distribution, by providing soft labels from a broader distribution, even if the synthetic data is not as good as the actual training data.

2. I'm also wondering what is the signification and importance of having $\tau$ in probability space, rather than in log-probability space. Is there a theoretical reason to have that margin expressed that way, or preliminary experiments showing it would be worse in log-prob?

3. Why start with further fine-tuning the pre-trained model on OpenWebText (l. 229)? What's the reason and implications of doing that, rather than take the off-the-shelf models directly?

4. l. 176 and below, is $p^T_{\textrm{argmax}\ p^T}$ just $\textrm{max}\ p^T$?

5. 2. In fig. 3, top right, it's weird to have the 1M line at 0 shortly before step 400, when it seems to have collapsed (Specialization hitting 0) in the top-left subfigure. I'd expect the DG/S ratio to be undefined, or arbitrarily high, rather than 0 at that point. Did I miss something?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper develops a novel technique for intelligent fine-tuning while minimizing forgetting of model representations learned on the pre-training dataset. The main proposed technique titled minifinetuning (MFT) employs a teacher, student based training paradigm where the (frozen) teacher model represents the pre-trained model while the (learnable) student model is initialized with the teacher weights but updated intelligently with the proposed technique to learn representations of the fine-tuning data. The crux of the finetuning technique is based on the idea of "moving" density mass uniformly from the prediction distribution P^T of a teacher model to the required target word as described by the ground truth (one-hot encoded) label on the fine-tuning dataset. The student model is updated via. crossentropy loss to mimic this corrected version of P^T to better align with the fine-tuning dataset. Instead of directly fine-tuning fully the student model via. cross-entropy loss on one-hot encoded labels, the intuition of this approach is that the degree to which P^T is modified can be controlled by user-specified parameters thereby striking a better balance between forgetting representations from the pre-training dataset and generalizing well to the fine-tuning dataset. Although the method is interesting, some crucial comparisons with existing methods that minimize catastrophic forgetting are missing as are evaluation with existing evaluation metrics popularly used in the fine-tuning, continual learning literature. Further, the related work needs to be more comprehensive and the visualization quality needs to be improved.

### Strengths
1. The paper introduces interesting results with a new, simple methodology for fine-tuning with minimal perturbation of the existing distribution learned by language models. The proposed method is intuitive and results (albeit incomplete) seem to indicate promising balance between retaining pre-trained representations while learning appropriate representations on the fine-tuning data.

2. The core idea of the soft KD by uniformly moving density mass to a specific location of interest to better match the target probability distribution is an interesting formulation and could lead to more sophisticated improvements using optimal transport based techniques in the future.

### Weaknesses
1. The coverage of techniques that alleviate catastrophic forgetting needs to be more extensive and the paper largely ignores a large set of techniques based on alleviating catastrophic forgetting and also metrics to measure forgetting (e.g., see Sec. 2.3 in `[2]`) and the stability-plasticity tradeoff (sec. 3.1 in `[2]`). 

2. The paper has a weak baseline comparison and misses comparing with state-of-the-art papers in regularization based continual learning to mitigate catastrophic forgetting (e.g., `[1]`). Such continual learning style papers are applicable as the authors make it a point many times in the paper (e.g., last row of Table 1) to highlight that the major advantage of their proposed MFT method relative to `Replay-based` methods is that MFT doesn't rely on access to training data thereby making the fine-tuning scenario similar to a continual learning style adaptation. In such a context, specific, approaches (e.g., `[1]`) exist that only retain metrics of weight-level `importance' on the pre-training dataset. This importance score is employed to intelligently fine-tune the model to minimize forgetting.

3. Paper presentation and specifically visualizations should be significantly improved. Multiple qualitative comparisons are drawn between plots where the y-axis has values on different scales (e.g., Fig. 1b,c; Fig. 3 FT:Ratio, MFT:Ratio; FT:Degeneralization, MFT:Degeneralization etc.). Either the scales should be unified (e.g., via. log scaling the axis) or such figures can be re-designed as tables for easier comparison.

### Questions
1. Why have state-of-the-art (non-replay based) approaches to alleviate catastrophic forgetting not been considered for comparison? For example, an approach well aligned with not having access to pre-training data is the Fisher-score based elastic-weight forgetting (EWC) technique [1] where the Fisher matrix is pre-computed and stored along with the pre-trained model weights.


2. How are $\tau$, $\alpha$, $\beta$ to be set / calibrated for fine-tuning? How are they tuned in the current setup?

## References:

1. James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A Rusu, Kieran Milan, John
Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, et al. Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences, 114(13):3521–3526, 2017

2. Wang, Liyuan, Xingxing Zhang, Hang Su, and Jun Zhu. "A comprehensive survey of continual learning: theory, method and application." IEEE Transactions on Pattern Analysis and Machine Intelligence (2024).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes MINI-FINETUNING, a fine-tuning technique that could balance specification and generalization without relying on pre-training data. The proposed technique uses the output probability of un-finetuned model as a teacher distribution to regularize the fine-tuning objective.

### Strengths
1. This presentation is clear.
2. The method is straightforward and intuitive.

### Weaknesses
 1. Although most parts of the method can be justified, I find that one particular design is a bit heuristic and unexplained. In particular, the method essentially involves a weighted combination of the one-hot distribution (for fine-tuning) and the original model's output distribution (for avoiding degeneralization). However, instead of a constant $\alpha$, the authors adopted a variable $\alpha$, such that the correct answer for the fine-tuning always dominates the original model's best answer by a fixed margin, $\tau$ (when the two answers are different). The motivation behind this is not well-explained. To me, this may induce undesirable behaviors. Consider two cases where the original model's answer differs from the fine-tuning label. In the first case, the original model's prediction is very certain, thus the distribution is very sharp; in the second case, the original model's prediction is very uncertain, thus the distribution is very flat. My intuition is that we would want to preserve the original model's knowledge more in the first case, because the knowledge is clear and very concentrated; and we would want to adapt to the fine-tuning objective more in the second case, because the original model doesn't hold a strong belief. However, the proposed method would do the opposite -- it would down-weight the original model's prediction more for the first case, because it needs to suppress the sharp distribution more to achieve a sufficient margin. This may lead to the model forgetting the key, definitive knowledge in the original model, and only retaining the superficial, ambiguous knowledge. This design is also at odds with the Replay method, to which the authors make an analogy to justify the proposed method. The Replay method can be regarded as having a fixed weight for all tokens. Could the authors better explain why it is necessary to deviate from Replay's intuition and have a variable weight, or at least provide some empirical evidence that the proposed weighting is better?

2. The authors seemed to experiment primarily with parameter-efficient LLMs. However, the specification-generalization trade-off is at greater stake and more challenging for regular state-of-the-art LLMs, such as Llama 3, 3.1 or 3.2, Mistral, Mixtral, etc. The authors did experiment with larger models in the appendix, but oddly with Llama 2 7B only, which is already outdated. Is there a reason not to test on more recent, state-of-the-art open-sourced models?

3. The authors seem to miss the rich body of works on catastrophic forgetting, which studies how to learn new knowledge without forgetting the old one, such as [1]. It would be very helpful if the authors could discuss those works in the related work section, and discuss the contribution of the proposed method in the context of catastrophic forgetting. Otherwise, adding self-distillation to prevent catastrophic forgetting does not constitute a very novel contribution.

4. (Minor) Table 1 is neither referenced nor explained in the paper. What do the stars mean? How were they rated?

### Questions
Please see the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new method, minifinetuning, that supports autoregressively finetuning LLMs on specialized domains while attempting to mitigate the amount of catastrophic forgetting of the pretraining corpus.

Minifinetuning makes use of a teacher-student setup, where the student is fine-tuned on a "corrected" token distribution, which is a hybrid of the new domain's token distribution the token probabilities output by the teacher. In this way, each token's distribution remains close to the original pretraining distribution (according to the teacher), with a minimal modification to boost the probability of the actual target token in the specialized domain.

The authors evaluate multiple models (GPT-Neo, Phi, Gemma, and Llama 2) on three specialized subdomains (medical, legal, and math), comparing against both vanilla finetuning and parameter-efficient finetuning baselines. Replaying samples from the pretraining data tends to outperform all methods considered, but the authors argue that access to pretraining samples amounts to an "unfair advantage." Their results suggest that minifinetuning allows for appropriate specialization to the new domain, while mitigating (to a certain extent) performance degradations on the pretraining data. This is particularly the case when the pretraining with limited data.

### Strengths
- Minifinetuning tackles the important problem of catastrophic forgetting of the pretraining data, though the authors could more clearly motivate why one wants to preserve the finetuning distribution after specialized finetuning.
- The proposed approach is simple, and the benchmarks and baselines considered are sufficiently comprehensive to evaluate its performance.
- The authors provide a helpful ablation study which shows the effect of adjusting only those token distributions that result in the incorrect token on the specialized domain, providing support for the author's implemention of minifinetuning (where all distributions are modified, whether resulting in the correct or incorrect token on the specialized domain).

### Weaknesses
 - There is insufficient detail on how hyperparameters were selected for both minifinetuning and for the baselines. Why was Tau set to 0.25? How would the authors suggest setting this in practice; based on the specialization, degeneralization, ratio, or something else? The authors present tau as a design choice, but it clearly acts as a hyperparameter, influencing the trade-off between specialization and degeneralization, as shown in Figure 2. The lack of a clear methodology for setting tau undermines the reproducibility and practical applicability of the method.
- Similarly, for the LoRA and DoRA baselines, how did the authors decide to fix the rank at 8? To make robust comparisons between minifinetuning and e.g. LoRA, it is important to understand whether this is a best-vs-best comparison. If Tau was tuned, but rank was not, then this isn't a fair comparison. The authors need to clarify whether the rank was chosen arbitrarily or based on a principled approach. Without this, it's difficult to assess the relative performance of MFT against these baselines.
- As mentioned in Strengths, the paper should more clearly motivate why a practitioner might want to conduct specialization without degrading pretraining performance. The paper needs to articulate the practical scenarios where preserving pretraining performance is crucial, rather than just stating it as a desirable outcome. This could include examples of downstream tasks where general knowledge is still important.
- The paper needs some significant attention to improve its clarity, and there are numerous errors scattered throughout. For example, the phrase "construction of a per-token individualized corrected distribution" is very hard to parse, as are the italicized subheadings under section 4, e.g., "distillation and corrective distillation on incorrect tokens". I had to read several sections multiple times. The writing needs to be more precise and less ambiguous to ensure the reader can easily follow the methodology and results.
- **Minor**: Is "degeneralization" a new term coined by the authors? Perhaps "performance decrease" or "catastrophic forgetting" might more clearly convey the underlying idea and tie in with prior work. The use of a non-standard term makes it harder to relate the work to existing literature on catastrophic forgetting in neural networks. Using established terminology would improve the paper's accessibility.
- **Minor**: Subfigures often have axes on different scales. It would be helpful to use a shared scale to facilitate easy visual comparison, or to explicitly call out a 10x decrease in y axis range (e.g. fig. 1). The inconsistent axis scales make it difficult to compare the performance across different models and settings. Standardizing the axes would improve the visual clarity of the results.
- **Minor**: The tables are rather large, and it is difficult to draw clear conclusions, particularly given the presence of Replay (e.g. Table 2). Perhaps the authors could add a short takeaway message to the caption of each table, highlighting what one should be looking for.

### Questions
1. The underlying idea significantly resembles how RLHF-based post-training is conducted with PPO, wherein a KL divergence term controls distribution shift between the preference-tuned model and the original base model. Did the authors consider interpolating between the full teacher distribution and the full student distribution, rather than just w.r.t. the target token?
2. Do the authors have any intuition as to why MFT appears to improve specialization, rather than just attenunate degeneralization (e.g. fig 3, left top and bottom, 1M and 2M tokens)?

### Soundness
2

### Presentation
2

### Contribution
3
