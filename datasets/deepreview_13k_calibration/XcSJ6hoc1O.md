# Predicting and analyzing memorization within fine-tuned Large Language Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Large Language Models have received significant attention due to their abilities to solve a wide range of complex tasks. However these models memorize a significant proportion of their training data, posing a serious threat when disclosed at inference time. To mitigate this unintended memorization, it is crucial to understand what elements are memorized and why. Most existing works provide \textit{a posteriori} explanations, which has a limited interest in practice. To address this gap, we propose a new approach based on sliced mutual information to detect memorized samples \textit{a priori}, in a classification setting. It is efficient from the early stages of training, and is readily adaptable to practical scenarios. Our method is supported by new theoretical results that we demonstrate, and requires a low computational budget. We obtain strong empirical results, paving the way for systematic inspection and protection of these vulnerable samples before memorization happens.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proses a measure to identify samples that are likely to be memorized using Pointwise Sliced Mutual Information (PSMI). The intuition is to use a model's snapshot from early in training when the model has learned "some" useful representations (but hasn't saturated to zero loss) to find possible outliers where PSMI between representation of an input X cannot predict its label Y. Such outliers are likely to be memorized as training proceeds, so they can be removed or dealt with as the model developers sees fit to ensure the final fully trained model doesn't suffer from pitfalls of memorization. Since the method uses a partially trained model very early on in training (typically 2-5% of training steps) and only requires forward passes through this partially model which makes it computationally much cheaper than training the full model and then removing memorized samples, after the fact. Empirical results show good FPR at a high TPR thus indicating the method could work in practice to detect a-priori the samples at risk of memorization.

### Strengths
- The method is simple and intuitive and isn't computationally very expensive
 - The paper is well written and properly compares the proposed method to baselines
 - I appreciated the section on ablations of hyperparameters

### Weaknesses
 - [Why is this approach specific to finetuning] In section 1.2 you mention that unlike Biderman et al [1] your approach is specific to finetuning. Why is this the case? Moreover, finetuning is typically much less computationally demanding than pretraining, thus I don't fully get why you put the same strict constraints on computational constraints as Biderman et al (who are focused on pretraining, thus these constraints make more sense in their setting).

- [Evaluation Metric] Why did you pick FPR at TPR = 0.75? This is a rather arbitrary number and would be rather context dependent. Why don't you just show the tradeoffs like you do in Fig 3a, or simply take the area under the curve if you must distill it into a number?

- [Sample ordering] What if the sample that is at risk of being memorized (ie low PSMI) has already been seen in the partial model? That is, the order in which you feed finetuning data will matter. Currently you are assuming any at the risk of memorization will not have been seen by the partial model you use to actually find the samples with low PSMI. But if any sensitive information has already been seen by the partial model then it seems like 

 - [Finetuning loss] What kind of finetuning are you doing? I could not find any information on this anywhere in the paper. Are you finetuning on the benchmarks like MMLU to literally to classification by attaching a classification head? Or are you doing supervised finetuning where you mask out the loss of question?

 - [Why is MIA an indication of memorization] I am confused by the choice of using MIA (LiRA) to infer ground truth memorization. Since you have full access to finetuning data why don't you use standard memorization measures like in [1,2] to infer what has or has not been memorized? MIA also has its own concerns, see [3].

 - [No improvement over logit gap or loss baselines] I appreciate that the authors compared fairly with baselines, however I do not see any claimed improvements on the FPR vs TPR tradeoff. Authors say that PSMI requires no tuning of threshold, which may be true but PSMI requires tuning, arguably more expensive hyperparams like when during finetuning should one stop (currently chosen as 95% in Algorithm 1) or which layer to use for PSMI (currently chosen as final layer in Algorithm 1). 

 - [Need more experiments to confirm broad applicability] The experiments in the paper are good, however to support the claim that this method is broadly applicable there is a need to test this on more kinds of finetuning methods. Current evals are only on LoRA finetuning which can have its own effects on memorization [4]. I would expect comparison with full finetuning as well as a few other popular parameter efficient methods like bitfit, softprompts etc.

 - [Minor concern] You say in related work that "However, this belief was challenged by Zhang et al. (2017), who proved that a model can simultaneously perfectly memorize random labels and achieve state-of-the-art generalization." -- however you can see Figure 1 in Zhang et al and this is not what they claim. They in fact show that a model can perfectly memorize random label samples but such models totally fail to generalize.

### Questions
- [Why is this approach specific to finetuning] In section 1.2 you mention that unlike Biderman et al [1] your approach is specific to finetuning. Why is this the case? Moreover, finetuning is typically much less computationally demanding than pretraining, thus I don't fully get why you put the same strict constraints on computational constraints as Biderman et al (who are focused on pretraining, thus these constraints make more sense in their setting).

- [Evaluation Metric] Why did you pick FPR at TPR = 0.75? This is a rather arbitrary number and would be rather context dependent. Why don't you just show the tradeoffs like you do in Fig 3a, or simply take the area under the curve if you must distill it into a number?

- [Sample ordering] What if the sample that is at risk of being memorized (ie low PSMI) has already been seen in the partial model? That is, the order in which you feed finetuning data will matter. Currently you are assuming any at the risk of memorization will not have been seen by the partial model you use to actually find the samples with low PSMI. But if any sensitive information has already been seen by the partial model then it seems like 

 - [Finetuning loss] What kind of finetuning are you doing? I could not find any information on this anywhere in the paper. Are you finetuning on the benchmarks like MMLU to literally to classification by attaching a classification head? Or are you doing supervised finetuning where you mask out the loss of question?

 - [Why is MIA an indication of memorization] I am confused by the choice of using MIA (LiRA) to infer ground truth memorization. Since you have full access to finetuning data why don't you use standard memorization measures like in [1,2] to infer what has or has not been memorized? MIA also has its own concerns, see [3].

 - [No improvement over logit gap or loss baselines] I appreciate that the authors compared fairly with baselines, however I do not see any claimed improvements on the FPR vs TPR tradeoff. Authors say that PSMI requires no tuning of threshold, which may be true but PSMI requires tuning, arguably more expensive hyperparams like when during finetuning should one stop (currently chosen as 95% in Algorithm 1) or which layer to use for PSMI (currently chosen as final layer in Algorithm 1). 

 - [Need more experiments to confirm broad applicability] The experiments in the paper are good, however to support the claim that this method is broadly applicable there is a need to test this on more kinds of finetuning methods. Current evals are only on LoRA finetuning which can have its own effects on memorization [4]. I would expect comparison with full finetuning as well as a few other popular parameter efficient methods like bitfit, softprompts etc.

 - [Minor concern] You say in related work that "However, this belief was challenged by Zhang et al. (2017), who proved that a model can simultaneously perfectly memorize random labels and achieve state-of-the-art generalization." -- however you can see Figure 1 in Zhang et al and this is not what they claim. They in fact show that a model can perfectly memorize random label samples but such models totally fail to generalize.


[1] Biderman et al. https://arxiv.org/pdf/2304.11158

[2] Carlini et al. https://arxiv.org/abs/2202.07646

[3] Duan et al. https://arxiv.org/pdf/2402.07841

[4] Biderman et al. https://arxiv.org/pdf/2405.09673

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies memorization when fine-tuning LLMs for classification tasks by applying a metric called pointwise sliced mutual information (PSMI) from prior work. The authors show how PSMI can be used to detect which examples are prone to memorization early during training by stopping the training loop after the loss has decreased by 95%, computing PSMI of each dataset sample, and flagging samples with negative PSMI as potentially memorized. They provide theoretical evidence for this approach and empirically demonstrate its efficacy by training Mistral 7B, LLama 2 7B and Gemma 7B models on the MMLU, ETHICS and ARC benchmarks. The results show that PSMI is competitive with previous metrics and can be run more efficiently.

### Strengths
1. The paper empirically demonstrates that the PSMI metric is a strong indicator of memorization in settings where LLMs are used for classification, performing as well or better than alternative metrics.
2. PSMI is also shown to be computationally more efficient than alternative metrics.
3. The authors theoretically show that PSMI can be used to detect memorized outliers.
4. The arguments for using false positive rate (FPR) at high true positive rate (TPR) to evaluate the effectiveness of memorization metrics are convincing.

### Weaknesses
1. The applicability of the results is quite narrow, for a paper targeted at generative LLMs. The paper focuses on detecting memorization when fine-tuning LLMs for classification, i.e. to predict the label for an input sequence. However, most LLM fine-tuning settings are generative, i.e. with the goal of learning to generate a particular distribution of text. The methodology of the paper relies on categorical labels as targets, so it cannot be applied to generative settings. Therefore, it also cannot be used to mitigate regurgitation-based memorization issues where the model might e.g. regurgitate private or copyrighted information, that are primarily of concern for generative models. I think the PSMI metric proposed here would make more sense in typical classification settings, but feels out of place for generative models. The choice of fine-tuning models on datasets typically used for benchmarking (MMLU, ETHICS, ARC) also feels strange in this context.
2. The discussion in 3.1 about the dynamics of memorization and the three phases of "pattern initialization", "pattern complexification" and "pattern degeneration" seems rather speculative to me. For instance, in line 345 onwards, the authors claim that "increasingly complex patterns bring easy elements closer to the decision boundary". Is there any evidence for a dynamic like that? Further, in line 349 the authors state that the training loss further decreases during the degradation phase, but that is not really visible in Figure 2c). Finally, the text repeatedly refers to accuracy values which are not shown.
3. The paper uses LoRA to fine-tune models. LoRA limits the degree to which representations can change due to the low-rank deltas and limited contribution of the deltas (modulated by the $\alpha$ parameter) to the base model's representations. Therefore, it is possible that for non-LoRA fine-tuning, e.g. full fine-tuning, representations might change in a different way. Since the PSMI metric relies on the interplay between representations and labels, it might behave differently for other types of fine-tuning.
3. There are a number of minor language issues, e.g. "help the model to generalized to similar..." (l 37), "train one or more shadow model, which ..." (l 87), "they are likely to be difficult point ..." (l 356), "mutual information is null" -> zero (l 207), mixing past and present tense (e.g. "observe" and "observed"), somewhat non-standard lowercase notation for figure and other references, etc.

### Questions
1. What were the input samples on which memorization was detected? Were samples entire input rows from the datasets or were substrings also considered? While models might not memorize entire input sequences, they might memorize substrings, so this choice might lead to different degrees of measured memorization. Prior work on memorization in LLMs typically uses substrings [1, 2].
2. Appendix C.3 states that the evaluated model is only trained on 1% of the data, and the remaining 99% are used to train shadow models. Could the authors clarify how many samples the models are trained and evaluated over? Appendix C.3 also states that similar results are obtained when picking other data splits. How many splits do the authors evaluate? To better judge the reliability of the results, it would be very useful to annotate the plots with confidence estimates over the different runs.
3. In Figure 3, why does the Mahalanobis distance use representations from layer 13, but PSMI representations from layer 29?
4. Line 458 mentions additional results but does not mention where to find them. If those results are in the appendix it would be good to reference them there.

[1] Quantifying Memorization Across Neural Language Models, Carlini et al., https://arxiv.org/abs/2202.07646

[2] Memorization Without Overfitting: Analyzing the Training Dynamics of Large Language Models, Tirumala et al., https://arxiv.org/abs/2205.10770

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study how to detect memorization by language models early in finetuning on classification tasks. The authors argue that PSMI is a predictive measure that can be computed early in training.

### Strengths
- Grammatical errors aside, the paper is relatively well written
- The Related Work is extensive

**Edit: The authors improved the paper in many of the ways I requested. I'm increasing my score from 3 to 5. I had initially planned to go higher but the newest version of the manuscript helped me realize that this paper is about detecting memorization by classifiers. The focus on LLMs in the title, abstract, introduction, methodology and results is (in my new understanding) a smokescreen/misdirection because the paper applies generically to classifiers, as their new image classifier results make clear.**

### Weaknesses
 - This work, as best as I can tell, studies memorization in a classification setting. This limits the contribution of the work. It also oddly contrasts with the literature since, to the best of my knowledge, much work on memorization by LLMs has not studied classification and instead studies a broader notation of memorization of sequences of tokens (e.g., Social Security Numbers, credit card information)
- The paper’s narrow focus on classification is not made clear from the title nor from the schematic Figure 1. The title could perhaps be edited to make this clear, or the schematic adapted with a more explicit caption.
- While the Related Work is extensive and the authors should be commended, I couldn’t determine what other works in the memorization literature focus specifically on classification. I feel like this should be made clear to the reader to know which other memorization-detection methods are relevant in the classification setting.
- Why do the authors choose LiRA membership inference attack (an MIA-based approach) as a ground truth for memorization, rather than a memorization based metric? The most famous is probably kl-memorization, used by Biderman et al. 2023. Another might be kl-edit distance, introduced by Duan et al. 2024 (https://arxiv.org/abs/2406.14549) as a softer notion of memorization
- The authors comment that they finetune for 10 epochs (Line 284 to 285). This is a large number of epochs. Many post-training recipes prescribe < 1 epoch. This is further backed up by the author’s Figure 2c, which shows the test loss begins increasing after the first epoch. If, for instance, a practitioner uses a validation split, then they would stop at or before 1 training epoch. Consequently, I feel like the memorization this paper is studying is even more distantly connected from practice. The authors state that the validation accuracy peaks at 5 epochs (“The second [line] (epoch 5) represents the best validation accuracy” on Lines 335-336)  but I don’t see evidence of this. Figure 7 in the Appendix shows that the test loss diverges after Epoch 1 in all settings and the test accuracy plateaus after 1 epoch.
- Section 3.1 feels handwavy and unscientific. Certain sentences seem like word soup. For instance, “The superposition of all patterns learnt by the model results in the decision boundary that separates samples that are classified in each class”; what does superposition mean in this context? This feels like a vacuous statement for saying “the statistical relationship for performing classification results in a decision boundary that separates samples into their classes,” which is trite. The next sentence “The model learns simple patterns, which are efficient to perform the task approximately.” is equally perplexing. What does simple mean? What does it mean for a pattern to be efficient at approximately performing a task? This section needs to be made more quantitative and more precise.
- Section 3.1 also suggests an alternative early measure of detecting memorization: Figure 3.1c suggests that the loss per sample might be as predictive as PSMI. To explain why this might make sense, some data might be “easy” to learn and other data might be “hard” to learn. The hard to learn data are identifiable because (a)  their losses are higher and because (b) their losses exhibit non-monotonic learning curves, notably increasing before more slowly decreasing. If such hard to learn data are more likely to be memorized (as suggested by Figure 3.1a), then this test would identify the same data but be faster than extracting hidden activations of the networks and then bombarding them with vectors sampled from the hypersphere. I normally try to avoid suggesting experiments for authors because experiments can be slow and difficult, but in this case, it appears that the authors already have the loss data; the question is how well the loss performs at predicting memorization (especially compared to PSMI).
- After I finished writing the above paragraph, I made it to Section 3.2 and discovered in Figure 3a that the loss and the logit gap are as predictive of memorization (in this setting) as PSMI. I’m now very perplexed why Section 2 pays so much attention to PSMI when the logit gap and the loss are equally performant, much easier to implement and probably much more computationally efficient. The authors might argue that if we focus on FPR @ TPR = 0.75, PSMI is slightly preferable to Loss (Figure 3b), but (1) the difference is very minor and (2) if we consider a slightly different TPR (e.g. TPR = 0.8), the difference between PSMI, Loss and Logit Gap becomes ~0 and (3) the claim that PSMI is better than loss under FPR @ TPR = 0.75 appears to be refuted by Figure 4a, which shows that FPR @ TPR = 0.75 is lowest for loss on ETHICS/MISTRAL. Edit: Figure 11 in the Appendix shows that PSMI and and Loss are almost indistinguishable in all cases; I’m not sure why the logit gap is omitted.
- I find the argument in “Why PSMI is the most practical estimator” to be unpersuasive because (1) tuning hyperparameters is what we do all the time and the same theoretical justification used for PSMI can probably also be extended to be used for the loss and for the logit gap, (2) because PSMI requires testing which layer(s) can be used, but the loss and logit gap do not, (3) because loss and logit gap don’t require Step 3 of Algorithm 1, making them faster, more memory efficient and with less room for implementation error, and (4) because loss, if it can be used to detect memorization, might be extended beyond the classification setting, whereas PSMI is much hard to extend to a general setting.
- Figure 4b is uninformative. Most of the figure is whitespace.
- The choice of Early Memorization from Biderman 2023 as a baseline is questionable to me. As I understand, that paper uses a different definition of memorization (kl-memorization), is not limited to classification, and is designed for pretraining not finetuning. It’s possible that there is no appropriate baseline for classification. If so, I think it would be good to explicitly state this and say “We’re using this baseline - even though it wasn’t designed for our setting - simply because there are no other baselines.” If I’m mistaken, please correct me.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Given a fine-tuning dataset D and a language model M which is part-way through being fine-tuned on D, this work introduces an information-theoretical metric for classifying which samples in D have been memorized by M. This technique is evaluated based on its FPR at TPR=0.75, and, according to this evaluation, is shown to outperform baseline techniques for detecting memorized samples. The authors also include an analysis memorization dynamics throughout training and an ablation study.

### Strengths
1. This paper is extraordinarily well-written. The key points, relation to prior work, and implementation details were all very clearly explained.
2. I greatly appreciated the ablation study, which effectively justified the threshold for stopping training once loss has dropped by 95%. It also clarified the effect of the layer at which activations are extracted.
3. The paper is thorough in general, with comparisons against multiple baselines and many informative appendices. 
4. The authors clearly explain the problem they are trying to solve: providing a compute-efficient classifier for memorized samples which has low FPR at a fixed high TPR.

### Weaknesses
1. The PSMI metric proposed here does not improve very much over much simpler baselines. The "loss" and "logit gap" baselines are much simpler (essentially, looking at the training samples on which the model is most performant), but have only a very slightly higher FPR than PSMI at the chosen TPR=0.75. It's unclear if the added complexity of PSMI is justified given this marginal improvement.
2. Moreover, this effect appears very sensitive to the fixed choice of TPR. Typically when I've seen other authors choose a "fixed high TPR" they select something like 99%; but at TPR=0.99 it appears that the PSMI metric introduced here would perform substantially worse than the "loss" and "logit gap" baselines. At intermediate TPRs between 0.75 and 1, it doesn't seem that there's a clear best method between PSMI, loss, and logit gap. In fact, it seems that TPR=0.75 is approximately the TPR at which PSMI looks best relative to the baselines. This raises concerns about the generalizability of the reported results.
3. The Mahalanobis distance baseline uses activations from layer 13. On the other hand, the performant methods all use activations from the final layers of the model (including its output). Based on the ablation study, it seems likely that the only effect in the Mahalanobis vs. PSMI comparison is the choice of layer. I request that the authors rerun the Mahalanobis distance baseline using activations from the same layer as PSMI. This is a critical comparison that needs to be addressed to validate the claims about PSMI's superiority.
4. The authors argue that PSMI is a good choice of metric because it comes with a distinguished theoretically-justified threshold. While this is true, I am unconvinced that it is important. In practice, practitioners can choose the amount of data that they would like to filter out (e.g. perhaps they are willing to filter out 1% of their data due to privacy concerns), and they can select their threshold in order to filter out that amount of data. Between this and my point (2), I don't see practical advantages for PSMI. The theoretical justification seems less relevant than practical utility, which is not clearly demonstrated.
5. Given that the "hard" samples in section 3.1 are *defined as* being those for which PSMI is small at the training cut-off, I find the analysis based on later changes in PSMI (e.g. seeing that it increases) unconvincing. This circularity undermines the validity of the analysis in this section.

### Questions
1. It seems to me that equation (6) in Theorem 1 could be tightened to an equality rather than an inequality. Here is my argument: after swapping the orders of the expected values, the LHS of (6) is just the mutual information between X and Y conditional on $\Delta=1$. But by assumption, these variables are independent when $\Delta=1$, so the mutual information should be 0. If this is incorrect, can the authors provide a counterexample?
2. Given that PSMI is estimated by fitting Gaussians to $p(\theta^Tx_k|y)$, it should be closely related to the Mahalanobis distance between $x_k$ and $X_k|Y$. Could the authors explain this relationship? I would find it informative for getting intuition about PSMI.

### Soundness
3

### Presentation
4

### Contribution
1
