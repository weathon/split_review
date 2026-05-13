# MrT5: Dynamic Token Merging for Efficient Byte-level Language Models

- Decision: Accept
- Scores: 6, 5, 3, 3

## Abstract
Models that rely on subword tokenization have significant drawbacks, such as sensitivity to character-level noise like spelling errors and inconsistent compression rates across different languages and scripts.
While character- or byte-level models like ByT5 attempt to address these concerns, they have not gained widespread adoption---processing raw byte streams without tokenization results in significantly longer sequence lengths, making training and inference inefficient.
This work introduces \textbf{MrT5} (\textbf{M}e\textbf{r}ge\textbf{T5}), a more efficient variant of ByT5 that integrates a token deletion mechanism in its encoder to \emph{dynamically} shorten the input sequence length. After processing through a fixed number of encoder layers, a learnt \emph{delete gate} determines which tokens are to be removed and which are to be retained for subsequent layers. MrT5 effectively ``merges''  critical information from deleted tokens into a more compact sequence, leveraging contextual information from the remaining tokens.
In continued pre-training experiments, we find that MrT5 can achieve significant gains in inference runtime with minimal effect on performance. When trained on English text, MrT5 demonstrates the capability to transfer its deletion feature zero-shot across several languages, with significant additional improvements following multilingual training.
Furthermore, MrT5 shows comparable accuracy to ByT5 on downstream evaluations such as XNLI and character-level tasks while reducing sequence lengths by up to 80\%.
Our approach presents a solution to the practical limitations of existing byte-level models.png}\hspace{0

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents MrT5 (Merge-T5), a more efficient variant of ByT5 that introduces dynamic sequence shortening through a learned token delete gate after the first few encoder layers. Though it is called Merge-T5, no tokens are merged together, only deleted or preserved. 
The method is a lightweight addition to a typical transformer architecture, with fully-differentiable soft deletion used during training via attention-masking and a regularizer with a tuned weight to adjust the degree of deletion, and hard deletion at inference time. 
Performance is shown to be comparable to ByT5 (+/- 2% accuracy) while reducing sequences by up to 80% and runtime up to ~55%. 
Only 4,000 steps are necessary to adapt a ByT5 model to a MrT5 model. 

Experiments are well designed and illustrate the properties of the method in different settings.  
First, synthetic tasks (vowel deletion, token merging) are used to understand learned deletions with controlled settings and small 31M parameter models.  
Next, they introduce token deletion in continued pre-training of ByT5-small both on English and multilingually, ablating components of the mechanism and different degrees of deletion. The task is span corruption loss, which for byte-level input may affect character and word boundaries. 
MrT5 is (generally) able to delete bytes in other scripts even if they have been unseen (if the model has been pretrained on English only), but results in slightly higher losses than ByT5. Multilingual pretraining reduces but does not remove the loss difference between MrT5 and ByT5. For Chinese, though, token deletion does not occur zero-shot.  
--> It is not clear the significance of the differences in CE in Figure 2 & 3 here - it would be nice if this could be made clear.  
Finally, MrT5 is evaluated on downstream tasks, XNLI and 2 character-level tasks.  
For English, MrT5 outperforms ByT5 with a reduction in sequence length and inference time of ~50%, while averaged across all languages there is a slight performance degradation of ~2% (though a significant speedup).   
On two English character-level tasks (contextual spelling correction and word search), MrT5 again saw ~2% accuracy drop compared to ByT5 in exchange for a 30-55% runtime decrease.  
When comparing different layer placements, it seems that a middle layer (3) balances training stability and deletion level, allowing contextual representations to be learned before deleting tokens while still pruning sufficient tokens for efficiency gains. 

It would be good if it were made clearer what the possible performance cost of introducing the deletion gate is, and some sense of the variability across languages, on explicit task performance as well as the loss presented in Figure 3.

### Strengths
A straightforward and lightweight addition to ByT5 models which can provide significant efficiency improvements (up to 80%) with a small trade-off in accuracy (~2%) compared to ByT5 (and often small improvements for English).

### Weaknesses
Efficiency gains (though generally significant) can come at a slight performance cost for non-English languages, and it is not clear how much variance in this cost there may be. 

- Without continued training in non-English scripts, there can be performance drops for non-English languages with less efficiency improvements. Figure 3 suggests that for Chinese for example, there may be almost no reduction in seq length zero-shot for the span corruption task, and some languages have relatively large drops in CE compared to ByT5
- For the downstream experiments, the results are reported in aggregate for non-English languages in the main text. While the results are broken out by languages in the Appendix, a mention of the variance across languages and a comment on the relationship between these results and those in the previous section would make it clearer what the potential trade-offs are and when they arise

### Questions
Questions: 
- I'd like to see the 'all languages' split for the downstream tasks discussed in the main text to match the CE analysis -> is it the case for example that you see a performance hit and no sequence length reduction for Chinese when the deletion gate is used zero-shot on a task, following Figure 3? Essentially, it would be nice to clearly state what the possible performance cost of introducing the deletion gate is, and some sense of the variability across languages, on explicit task performance as well as the loss presented in Figure 3. 
  - There is not much difference in performance between MrT5 and ByT5 for Chinese XNLI in Appendix Table 6, and there is ~20% length reduction - why do you think there is a difference to Chinese in the top half of Figure 3 with only a ~2% length reduction? Similarly, for Swahili, there seemed to be a significant difference in CE in Figure 3 zero-shot, but a smaller gap in Table 6. Why do you think that is? I suggest addressing these inconsistencies in the main text and providing possible explanations for the differences between training and downstream task performance. 

Suggested citations:  
- [Cherry et al 2018](https://arxiv.org/abs/1808.09943) learns to delete characters for temporal compression with character-level models in MT
- [Limisiewicz et al 2024](https://arxiv.org/pdf/2403.10691) uses morphologically inspired compression for byte sequences to create MyT5, a ByT5 variant 


Presentation nits:
- L99: "the main the limitations" -> "the main limitations"
- How α was set was not super clear to me. L196: "For most of our experiments, we set α by hand, which allows the model to dynamically set the deletion ratio [based on the loss]." This paragraph says α was set by hand most of the time, but that it is easier to allow α to dynamically change. Do any of the experiments in the main text allow α to change? (It doesn't seem so?) Why not, if it is easier?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work builds on ByT5 and introduces a new token deletion mechanism that dynamically determines how to remove unnecessary tokens from the sequence without compromising performance.

The authors incorporate additional neural layers to learn the optimal token deletion process. During training, a loss function is introduced to encourage the model to progressively delete tokens (softly) or to achieve a specific ratio. During inference, the layers identify and discard unimportant tokens in a hard manner.

Controlled experiments on synthetic tasks demonstrate that the method, MrT5, can effectively learn to compress the input sequence. Further results on downstream tasks, such as XNLI, also support the authors' claims.

### Strengths
* A simple yet effective method that enables models to dynamically learn how to delete tokens from byte-level inputs.
* Controlled experiments and results on downstream tasks support the authors' claims.
* MrT5 demonstrates competitive inference speed compared to ByT5.

### Weaknesses
* If I understand correctly, during training, the byte tokens are deleted softly, meaning there are still significant burdens for byte-level language models given that standard attention has quadratic time complexity, which limits their scalability to larger sizes.
* The experiments presented utilize moderate model sizes, which may constrain the overall persuasiveness of the proposed method.

### Questions
If possible, I am interested in comparing the effectiveness of additional parameters introduced by MrT5 in learning to delete tokens.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work improves on top of ByT5 by adding a delete gate at a certain layer to remove unimportant tokens. The proposed model trains a soft deletion layer which is fully differentiable, and then uses the same layer for hard (i.e., discrete) deletion during inference. The model only requires unsupervised data for training. 

The model is evaluated on monolingual and cross-lingual pretraining tasks, showing a trade-off between cross-entropy loss and sequence length reduction. On two evaluation tasks, the model is also shown to be competitive with ByT5 while reducing sequence length.

### Strengths
• Clear and illustrative figure

• Very well-written and easy to read

• Demonstrate that the proposed method performs competitively with ByT5 on XNLI and Spelling Correction.

• The soft and hard deletion switch can be considered novel, at least for applying to this line of work.

### Weaknesses
• The baselines for MrT5 are not properly constructed (Section 5). To see how well MrT5 does, one should compare it with other orthogonal methods/models (e.g., pooling) that reduce sequence length and see how much increase in x-entropy loss they incur.

• For downstream tasks we should compare with non-byte-level models to see the gap: how far are we in terms of accuracy? What's the run-time comparison after this token deletion optimization? These questions are left unanswered in the paper.

• Just evaluating on XNLI and Spelling Correction is not enough to claim that the model is stronger than ByT5, let alone comparing comprehensively with models equipped with traditional tokenizers.

### Questions
Suggestions:

• 034-035: "... via algorithms such as byte-pair encoding (Sennrich et al., 2016) or SentencePiece (Kudo & Richardson, 2018) ..."
Consider rephrasing this sentence as BPE is part of SentencePiece.

• Consider discussing the relation between this work and GemFilter (https://arxiv.org/pdf/2409.17422) as both pertain to token deletion.

• The proposed method seems readily transferrable to decoder-only models, which is the most widely used architecture nowadays. Would like to see some experiments, or at least some discussions about this direction.

• 150-151: "(1) we want to avoid the overhead of executing the deletion algorithm multiple times;"
This motivation is better discussed from the perspective of "trade-off". If executing the algorithm multiple times can reduce the number of tokens/positions to process in later layers even more without compromising generation quality, then there is no reason to not do it.

• The regularizer loss only seems to encourage the increase of the number of deleted tokens, but does not encourage the gate output to converge to the extreme values (i.e., the min or max gate value). This could make hard deletion during inference less effective because merely setting a threshold may delete some "somewhat useful" tokens. Please refer to a very old paper on NALU to see how they do this: https://arxiv.org/pdf/1808.00508. Preferably this work can discuss the motivation of why or why not there is no such regularization term.

• It's an interesting choice to combine experimental setup and results into one section, but I still think it's better to present them separately.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces MrT5, a ByT5 variant incorporating a learned delete gate for dynamically reducing the byte sequence length during the encoding process. By removing tokens from the sequence, the model is encouraged to implicitly merge the information from the deleted tokens into those which remain. The authors find that this reduction in sequence length leads to significant gains in runtime efficiency at inference time, with minimal differences to baseline performance. They show the deletion mechanism can reduce sequence length in zero-shot scenarios with new languages and see further improvements when training with multi-lingual data.

### Strengths
**Originality**
Most previous work in this area focus on algorithms for learning “what to keep” when performing sequence compression. This paper provides an interesting alternative by framing the problem as learning “what can be removed”. The proposed deletion mechanism can be added to existing architectures, making their solution easy to integrate into existing models via fine-tuning.

**Quality**
The authors conducted several levels of experimentation including simple tasks for gaining an intuition about the mechanism of their approach, a more difficult span completion task to compare against baselines, and down-stream tasks to assess cross-lingual semantic understanding and sensitivity to character-level manipulations.

**Clarity**
The paper is well-organized and clearly written. The ideas, methodology, and findings were easy to follow and understand.

**Significance**
The paper focuses on improving tokenization-free language models, which is a very relevant topic of interest to the community. Tokenization leads to several issues in LMs, including those listed by the authors as motivation: sensitivity to character-level noise (spelling errors), number representation for mathematical reasoning, and inconsistent compression rates across languages.

### Weaknesses
**1** The results are sensitive to the $/alpha$ hyperparameter. The gate regularization loss does not directly relate $\alpha$ to the desired compression rate, leading the authors to manually tune $\alpha$ or use the proposed P-controller to optimize for a desired compression during training. Previous work such as those cited by the authors (Nawrot et al., 2023) use a binomial loss to directly incorporate the desired compression rate into the regularization term. The same approach could be used here to remove the additional complexity.

**2** The location of the gate in a specific network also needs to be tuned. The authors show that for implicit merging of contextualized tokens the gate needs to be placed later in the network, reducing the cost-savings of the approach.
The results of the synthetic experiments were not convincing. The deletion gate seemed to only target the correct characters when sequence length was significantly reduced, resulting in a steep drop in sequence-level accuracy.

**3** There were no comparisons with other token-merging models in any of the experiments. It would have been nice to see a head-to-head comparison of this approach with the unsupervised boundary predictor from the cited (Nawrot et al., 2023) paper or the faster Toucan model from (Fleshman and Van Durme, 2023). Stronger baselines are needed throughout.

 **4** The models aren’t trained to convergence (footnote 4), and the potential 15% improvement in the baseline through continued training might not translate to MrT5, increasing the performance gap.

### Questions
**Q1** When training from scratch, what prevents the model from learning to set G=-30 (minimizing gating loss) and inflating QK^T for all tokens to offset the impact? It seems this would give the model additional capacity without increased loss.

**Q2** Does the specific value of k impact results when fine-tuning existing models, or does k=-30 seem to always work well?

**Q3** If the models are trained until convergence does the performance gap between MrT5 and ByT5 increase?

**Q4** Why was softmax_1 used in the ByT5 baseline? Wouldn’t the unmodified ByT5 perform better?

**Q5** The paragraph beginning at Line 180 suggests that a sequence’s compression rate depends on the least compressed sequence in the batch. Are the rates reported in the paper based on this batch-dependent compression rate or the rate you’d get with a batch size of 1?

**Q6** Similarly, are the performance metrics reported using this explanation of batch processing, or are they reported as if sequences were fully compressed?

**Q7** In Figure 3, why is the English-only trained model doing better than English on many of the other languages?

### Soundness
2

### Presentation
3

### Contribution
2
