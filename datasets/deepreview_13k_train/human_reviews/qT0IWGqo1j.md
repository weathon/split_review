# Training on test proteins improves fitness, structure, and function prediction

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
Data scarcity and distribution shifts often hinder the ability of machine learning models to generalize when applied to proteins and other biological data. Self-supervised pre-training on large datasets is a common method to enhance generalization. However, striving to perform well on all possible proteins can limit model’s capacity to excel on any specific one, even though practitioners are often most interested in accurate predictions for the individual protein they study. To address this limitation, we propose an orthogonal approach to achieve generalization. Building on the prevalence of self-supervised pre-training, we introduce a method for self-supervised fine-tuning at test time, allowing models to adapt to the test protein of interest on the fly and without requiring any additional data. We study our test-time training~(TTT) method through the lens of perplexity minimization and show that it consistently enhances generalization across different models, their scales, and datasets. Notably, our method leads to new state-of-the-art results on the standard benchmark for protein fitness prediction, improves protein structure prediction for challenging targets, and enhances function prediction accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this study, training/fine tuning at test time (TTT) is applied to adopt the representations learned by foundation models, trained on large corpus of protein families, to a specific task defined on a test protein. The proposed technique has been extensively benchmarked to demonstrate improvements in protein fitness, structure and function prediction tasks.

### Strengths
1. Proposes a general technique that can be used with any backbone trained with masked language model head. However, the idea is not novel.

2. The paper has a nice “Related Work” section as well as clear and easy-to-follow narrative.

### Weaknesses
1. Proposes a general technique that can be used with any backbone trained with masked language model head. However, the idea is not novel.

2. As acknowledged by the authors, the TTT technique has been used in other domains, however this study applies it for the first time to the computational problems in protein domain.

3. One of the motivations of this work is to get rid of additional data collection (MSA) for a given test protein, however the experiments do not show this in a comparable setting. I may be wrong, so the author’s clarification is appreciated. Please see the questions for more detailed on this.

    **(i)** It is shown that the performance is improved by applying TTT to foundation models, e.g. ESM2. However, there is no comparable setting in which the foundation model is fine-tuned on the sequences homologous to the test protein. Therefore, it is not clear when one should choose to go with TTT instead of MSA, i.e., incorporating evolutionary features.

    **(ii)** It looks like incorporating (co)evolutionary features through fine tuning may be a better option than applying TTT to $fog$ (transformer encoder and masked language model head) for protein fitness prediction. Three out of five phenotypes in Table 1 support this claim.

### Questions
1. In Table 1, is the TTT done per protein individually or simultaneously for all proteins in the test set? Does the same applies to the other benchmarked methods as well?

2. Since TTT on one test protein is motivated by the derivation of MSAs to be time consuming, have you tested variants of ESM2 and SaProt where the models ($fog$) are finetuned by the homologous sequences derived for each protein? Do these variants outperform TTT fine tuned models? My understanding is that ESM2 and SaProt see similar proteins to the test/target protein in their training but are not further fine tuned on the MSA derived per protein.

   (i) Also, it would have been nice to see a combination of MSA and TTT, where TTT is done for all the homologous sequences to the test      protein. It is not clear to me whether it hurts or improves the performance compared to only using TTT on the single test protein.

    (ii) The point of homologous sequences can be applied to the other included benchmarks too. 

3. What is meant by TTS steps?

4. Is there any preference on what $h$ (task specific head) has been trained on? Should it be the same dataset as the one used for backbone ($f$) training, e.g., like the structure prediction task using ESMFold (Section A.2.3), or it could be any other large dataset with information on the task.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a technique for self-supervised fine-tuning during the testing phase, enabling models to dynamically adapt to the specific test protein without extra data. Their experiments show that the approach achieves new state-of-the-art results on three tasks: (1) standard benchmarking for protein fitness prediction, (2) enhanceing protein structure prediction, and (3) improving protein function predictions. They also establish a connection between their objective and perplexity minimization.

### Strengths
## Motivation

The paper is well-motivated. There is an abundance of popular, large, and expensively-trained models by major institutions on massive amounts of protein data that perform "subpar" at best on specific downstream tasks. This under-performance problem has been established time and time again in subsequent studies and paper. Any simple approach that can mitigate this problem, however modestly, can positively influence the future work in this area. This paper is addressing this problem directly.

The proposed approach avoids being overly complex, and it seems plausible to generalize to downstream tasks not included in the data. The method does not require new labels, an auxillary dataset, or prior knowledge about the tasks. I belive these features make this study well-placed in the literature.

## Supporting the Claims

The main experiments section provides enough data to satisfy the three claimed tasks. The experiments prior to the main section (e.g., Figures 3 and 4) substantiate the claims made in the introduction and model description section. Since the contributions in the paper are simple enough to verify (e.g., the correlation of the perplexity measure and the TTT approach), I find the improvements related to the contribution of the approach.

## Strengths

1. The paper is quite well-written. I enjoyed reading the paper, understanding the approach and the problem, and the explanations were easy on the mind. The key contributions were stated clearly in the introduction, and the abstract and the title are fair representatives of the work.

2. The experimentation quality is reasonable and statistically significant confidence intervals were reported. That being said, the number of random seeds is a bit on the lower side (i.e., 5 is not too large).

3. The appendix contains notable valuable and complementary information to the paper; (1) many ablation studies and results for a number of hyper-parameters were included, and (2) the experimental setup is clearly detailed.

4. The improvements seem modest but consistent across the board, for instance in Table 1. Even when the proposed method does not work best, it doesn't perform terrible. It is relieving to see this approach does not induce a lot of risk.

### Weaknesses
My main concern is the proper estimation of the number of test-time training steps. Such fine-tunings have been studied frequently and are prevalant in other areas, such as few-shot learning, meta-learning, domain adaptations, etc. Most, if not always, (1) the size of the fine-tuned parameters, and (2) the number of training steps can play a significant role in the outcome.

While the paper is not devoid of studies regarding these effects, I don't feel they are complete enough. One would expect a clear degradation in performance with large-enough step sizes and model-complexity. Some intuitive indications of when and how TTT should be proposed, studied, and tested are needed. There is almost no theoretical component to the paper, which is not a deal breaker for this paper, but it may assist in the correct choice of such hyper-parameters. For instance, the paper does not explore the effect of varying the number of fine-tuned layers, or the impact of using techniques like early stopping based on validation performance on the target protein itself, which could prevent overfitting. The current approach relies on a fixed number of steps, which may not be optimal for all proteins or tasks.

A more thorrough discussion and experimental results regarding the **limitations** of the approach is also missing from the paper. Specifically, the paper lacks a detailed analysis of failure cases. It would be beneficial to see examples where TTT does not improve performance or even degrades it, and to understand the characteristics of these cases. This would help to define the boundaries of the method's applicability. Furthermore, the paper should discuss the computational cost associated with TTT, especially for large models and long protein sequences, and how this cost compares to the benefits gained.

### Questions
The improvements in structure prediction seem slightly more significant than the fitness or function prediction tasks. Would you care to comment on why this may be the case?

## Minor Comments

1. Line 54: seems unnecessarily cut off.

2. Line 477: "Evaulation" in "Evaulation setup" should be "Evaluation"​.

3. Line 508: "syntase" in "terpene syntase (TPS)" should likely be "synthase"​.

4. Inconsistent Hyphenation: Terms like "protein language model" and "test-time training" sometimes appear with inconsistent hyphenation (e.g., "test time-training")​.

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
3

### Summary
Data scarcity and distribution shifts impede generalization in machine learning models for biological data. To overcome this, this paper proposes a self-supervised fine-tuning method at test time, which adapts models to specific proteins without extra data, enhancing generalization and achieving state-of-the-art results in protein fitness prediction.

### Strengths
Good attempt at biological problems.

### Weaknesses
 **Section 2 - Model Adaptation:**
- **TTT Method Selection:** The rationale for selecting the current TTT methods is unclear. Provide a clear justification for the choice. The paper does not sufficiently compare various methods within the field, instead relying on a straightforward application as "Test-Time Training with Masked Autoencoders." A more thorough discussion of the landscape of TTT methods is needed, including a comparative analysis of the strengths and limitations of different TTT approaches, such as one-pass versus multi-pass adaptation.

**Section 3 - Training Objectives:**
- **Performance Linkage:** The objectives should be linked to improved biological performance. Add relevant goals to achieve desired outcomes.
- **Efficiency:** Reducing perplexity is insufficient for justifying large model use. Considering smaller discriminators or LLM query filtering for efficiency is the same.
- **Resource Management:** Finetuning large models is resource-intensive. Assess cost-effectiveness and seek more efficient training strategies.

### Questions
see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a method to perform test-time adaption of protein masked language models (MLM) for improved supervised prediction of protein properties. The method partially minimizes the standard MLM loss on a single test example before a property prediction is made from the supervised head. The authors explain that the success of this method may be due to the fact that it reduces the perplexity of masked token predictions for the target protein and lower perplexity has been shown to correlate with improved property prediction. The authors test their method on three tasks: (i) comprehensive zero-shot prediction benchmarking in ProteinGym, (ii) structure prediction with ESMFold and (iii) two supervised classification tasks (substrate prediction for a particular class of enzymes and protein localization prediction).

### Strengths
* The paper is clearly written and organized. 
* The method is described clearly and is well-motivated by existing literature. 
* The figures are nicely designed and clearly convey the intended information. 
* The evaluations covers a broad range of tasks in fitness prediction.

### Weaknesses
1. The method is motivated by models with "Y-shaped" architectures in which there is both an MLM head and a fitness prediction head. However, the authors evaluate on the zero-shot task in ProteinGym, where models use masked token probabilities as proxies for fitness predictions and therefore do not use a Y-shaped architecture. This is confusing, since ProteinGym also contains fine-tuning tasks that require the Y-shaped architectures that motivate their method. The paper would be improved by evaluating on the fine-tuning tasks in ProteinGym or by more clearly explaining why the zero-shot task is more appropriate.
2. In "Background and Related Work", the authors cite a number of papers that performed model adaptation on either protein MSAs or otherwise related proteins to the target protein. These methods are then dismissed because "constructing MSAs is time-consuming, and similar proteins may not be available for many targets." These arguments are situational and are not strong enough reasons to avoid direct comparisons with the cited methods. For example, one may be making predictions for many closely related target proteins, in which case constructing a single MSA and using that to adapt the model for all target proteins (as in TranceptEVE) may be faster than applying TTT to each target. The paper would be strengthened by including a more in-depth discussion about the distinction between existing methods and the authors' proposed method, a discussion about the situations in which each type of method is relevant, and a quantitative experiment demonstrating improved performance in a task between the proposed method and the existing methods.
    * A reasonable comparison is to compare the difference in performance between TranceptEVE and Tranception to the difference in performance between methods w/o TTT to those using TTT (e..g SaProt (650M) and SaProt (650M)+TTT). On avg spearman, the difference between TranceptEVE and Tranception is about 0.02, while the difference between methods with and without TTT is usually about an order magnitude smaller (0.0014 for SAProt (650M) and SAProt (650M)+TTT). This is not a perfect comparison, but it does suggest that the MSA-based adaption of TranceptEVE can have advantages over TTT, which warrants further investigation about the distinction and relative advantages of the methods.
3. The result on improving structure prediction in ESM3 and ESMFold is interesting, but of limited practical relevance since AlphaFold2/3 are far superior structure predictors. The paper would be strengthened by either demonstrating an application of TTT to AlpahFold or an explanation of why this is not possible.
4. Less important: the authors claim in section 3.3 to offer an explanation for the effectiveness of test time adaptation by appealing to the correlation between perplexity minimization and model performance. This is somewhat circular, since the proposed method directly lowers the perplexity of the target protein. Therefore, the positive results provide mre evidence that perplexity minimization is important, but don't provide an explanation for why the method works. I recommend framing this as a justification for the method rather than an explanation for why it works.

**Minor**:
* Line 113-114: " For example, in AlphaFold2, most of the loss function weight is put onto masked modeling of multiple sequence alignment". I believe the authors are referring to the fact that the MSA loss has a weight of 2 while the FAPE loss has a weight of 0.5. This may represent a difference in scales in the different losses rather the relative importance of the losses to training. This line should be removed.
* Line 189 typo: $h \circ g$ should be $h \circ f$
* Line 375 typo: both instances of "TraceptEVE" should say "TranceptEVE"

### Questions
* Why did the authors choose to evaluate on the zero-shot tasks in ProteinGym, rather than the fine-tuning tasks? Is there literature precedent for using test time adaption to improve zero-shot prediction?
* What is the rough time scaling of TTT? How does it compare to the scaling of MSA generation? 
* Can the authors demonstrate a scenario in which TTT clearly outperforms the MSA-based adaptation of TranceptEVE?
* Is it possible to apply TTT to AlphaFold or OpenFold?

### Soundness
2

### Presentation
2

### Contribution
2
