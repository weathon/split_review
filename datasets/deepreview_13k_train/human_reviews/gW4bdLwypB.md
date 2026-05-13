# Objective Soups: Multilingual Multi-Task Acoustic Modeling for Automatic Speech Recognition

- Decision: Reject
- Scores: 6, 5, 10, 5

## Abstract
The need for training multilingual multi-task automatic speech recognition (ASR) models is increasingly evident. However, a significant challenge arises from the conflicts among multiple objectives when using a single model. Multi-objective optimization (MOO) can address this challenge by facilitating the optimization of multiple conflicting objectives, aligning the gradient updates in a common descent direction. While MOO helps avoid conflicting gradient update directions, a critical issue is that when there are many objectives such as those in multilingual multi-task ASR, it is often impossible to find such common descent directions. Therefore, an interesting question is: would it be more effective to separate highly conflicting objectives into different optimization levels or keep them in one level? To address this question, this paper investigates three multi-objective ASR training frameworks, which we refer to as objective soup recipes. These frameworks use MOO at different optimization levels to mitigate potential conflicts among all objectives. We conduct an extensive investigation using the LibriSpeech and AISHELL v1 datasets for ASR, along with the CoVoST v2 dataset for both ASR and speech-to-text translation tasks, to determine the highly conflicting objectives and the optimal training recipes among these three MOO training algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores whether separating highly conflicting objectives into different optimization levels or keeping them unified is more effective for multilingual, multi-task learning in automatic speech recognition (ASR) and speech-to-text translation (S2TT). It introduces three Multi-Objective Optimization (MOO) methods—VS-ASR, VC-ASR, and VM-ASR—designed to resolve conflicts between objectives at various optimization stages. These approaches are compared against baseline methods like pre-training and fine-tuning (PT+FT) without MOO. Through experiments on LibriSpeech, AISHELL v1, and CoVoST v2 datasets, the study demonstrates that applying MOO across multiple optimization levels yields consistent improvements in both self-supervised and supervised tasks. A key insight is that segregating highly conflicting objectives enhances performance for ASR and S2TT, and the order of optimization significantly affects ASR accuracy. The study also emphasizes the importance of penalty parameters in Multi-Level Optimization (MLO) training, showing robustness across different model sizes. These findings offer valuable insights for optimizing conflicting objectives in multilingual and multi-task speech systems, with broader implications for the development of more efficient ASR and S2TT models.

### Strengths
1. Effective Handling of Conflicting Objectives: This paper directly addresses the issue of conflicting objectives by utilizing conflict-avoidant update directions, overcoming the limitations of traditional methods like static weighting and constrained optimization.
2. Comprehensive Exploration of MOO Techniques: Unlike related work (e.g., "reward soups" by Rame et al., 2024), which focuses on linear scalarization for Pareto-optimality, this paper explores a broader range of Multi-Objective Optimization (MOO) techniques to effectively manage conflicts in multilingual, multi-task learning.
3. Transparency and Reproducibility: The authors provide accessible code, ensuring reproducibility, and clearly outline their experimental setup, facilitating verification.
4. Thorough Evaluation: Experiments are conducted in both task-based and language-based MLO settings using consistent hyperparameters, and considerations such as memory consumption and training time are discussed, adding depth to the evaluation.

### Weaknesses
1. Code Quality: The provided code requires cleaning and refinement for better readability and maintainability.
2. Organization and Flow:
a. Important conclusions and interesting findings are relegated to the appendix, disrupting the reading flow.
b. Key sections (e.g., Section 5.2) should be integrated into the main text for coherence.
3. Abbreviation Clarity:
a. Certain abbreviations (e.g., FT, VC-ASR in the introduction) are used without proper introduction or explanation.
b. A clear glossary or introductory explanations would enhance readability.
4. Limited Evaluation:
a. Only two models (Conformer 58M and 100M) are evaluated.
b. Broader evaluation across diverse architectures and sizes is necessary to convincingly demonstrate the method's effectiveness.
5. Theoretical Analysis: Further theoretical analysis is needed (Notes as Future Work in Conclusion)  to comprehensively understand the capabilities and limitations of the proposed method.

### Questions
1. Clarification on Conflict Reduction: Could you provide more details on how segregating highly conflicting tasks (ASR and S2TT) into different optimization levels reduces overall conflict among gradients, leading to improved WER scores?
2. Efficiency of MOO Model: Section 5: Can you elaborate on how a single MOO model reduces resource demands during deployment, making it a more efficient solution overall? Are there specific metrics or comparisons that support this claim?
3. WER Score Discrepancy: It's surprising that en, fr, and de have higher WER despite having more data hours in CoVoST2. Can you offer insights into this discrepancy?
4. Pareto Front Explanation: Could you clarify the statement "In such scenarios, the Pareto front tends to be large and spread out"? How do these scenarios arise, and what implications does this have for the trade-offs between objectives?

### Soundness
3

### Presentation
2

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
This work explores the paradigm of multi-objective optimization (MOO) for multitask multilingual speech processing and proposes three multi-objective training objectives to improve ASR and speech-to-text translation (S2TT) across multiple languages. These objectives are designed by separating out the supervised/unsupervised/task-specific/language-specific losses into different optimization levels. The authors demonstrate that such multi-level optimization (MLO) is effective and provides significant performance gains compared to other baselines across multiple languages for both ASR and S2TT.

### Strengths
* The authors are the first to explore the use of multi-objective optimization at different optimization levels for ASR and S2TT across multiple languages.
* The paper is structured well and was easy to read.
* The authors derive consistent gains across both tasks and multiple languages using the proposed multi-level optimization technique.

### Weaknesses
 * The reported baseline WERs and BLEU scores on CoVoST 2 appear to be significantly weaker than the state-of-the-art. The authors should clarify this further.  

* The intuition for the proposed optimization levels could be motivated further. I elaborate on this point further in my questions to the authors below.  

* The experimental section has many missing details that I elaborate in my questions below.

* The motivation for the self-supervised loss $c(x)$ in VC-ASR, particularly its flatness, is not sufficiently explained. While the authors refer to Appendix C, it lacks a discussion on the curvature of the loss landscape. The connection between the flatness of the unsupervised loss and its ability to generalize features across tasks needs further elaboration. 

* The experimental details are lacking, hindering reproducibility. Specifically, the learning rates for pre-training and fine-tuning in the Joint PT+FT baseline are not specified. Furthermore, the acoustic features used (e.g., raw audio, MFCCs, log-mel spectrograms), the token vocabulary size for each language, and whether data augmentation techniques like SpecAugment were employed are not mentioned. These details are crucial for replicating the experiments.

* In Section 5.6, the authors should point to Appendix D that provides more details about the Librispeech/AISHELL experiment:  
  * Why are numbers on test-other not reported in Table 5?  

  * As is standard, are the numbers for AISHELL CERs and not WERs?  If so, this should be fixed in the caption of Table 5.  

  * Table 5 is missing numbers with the Joint PT+FT baseline. How did this model fare?  


* From Tables 1 and 2, UAS (VM-ASR) does better for ASR and USA (VM-ASR) does better for S2TT. Can the authors hypothesize why this might be? This trend of the task right after the unsupervised objective benefiting more also appears in Table 5 (UEC benefits En ASR more and UCE benefits Zh ASR more).  


* Saif et al. 2024 is most related to this work and should be explained in more detail either in the "Related Work" section or in Section 3.2. The authors should explicitly mention how it differs from the proposed VS-ASR/VC-ASR objectives.  


* Minor typo on line 185: It should be l_s(\theta, \phi_t^n) (not \phi_t^N).

### Questions
* The baseline numbers for PT+FT shown in Tables 1 and 2 fall significantly short compared to prior work that uses Conformer models. For e.g., we can refer to the official repository accompanying the CoVoST 2 dataset (https://github.com/facebookresearch/fairseq/blob/main/examples/speech_to_text/docs/covost_example.md). WER on English using a 42.9M Conformer model (https://github.com/facebookresearch/fairseq/blob/main/examples/speech_to_text/docs/covost_example.md#results) is around 23%; the authors get 29.7% with their 58M parameter model. Similarly, on S2TT, the BLEU score for Fr->En using the 58M model in the official recipe is around 27 (https://github.com/facebookresearch/fairseq/blob/main/examples/speech_to_text/docs/covost_example.md#results-1), while the authors get a BLEU score of 23.4 with their 58M model. Please clarify this discrepancy in numbers.  

* When motivating VC-ASR, the authors mention desirable properties of c(x) including the non-conflicting nature of its gradient update and that its optimization region must be sufficiently flat. We are referred to Appendix C for why the unsupervised loss possesses these properties. However, nothing is mentioned about the curvature of the loss (i.e., its flatness) in Appendix C. Please elaborate.  
  

* Many experimental details are missing and should be added to an Appendix to encourage reproducibility. Below, a few missing details are listed:
  * In the sequential optimization of PT and FT objectives in the Joint PT+FT baseline, what learning rates were used?  

  * What acoustic features were used, and what was the token vocabulary size?  

  * Was any data augmentation (SpecAug) used during training?  


* In Section 5.6, the authors should point to Appendix D that provides more details about the Librispeech/AISHELL experiment:  

  * Why are numbers on test-other not reported in Table 5?  

  * As is standard, are the numbers for AISHELL CERs and not WERs?  If so, this should be fixed in the caption of Table 5.  

  * Table 5 is missing numbers with the Joint PT+FT baseline. How did this model fare?  


* From Tables 1 and 2, UAS (VM-ASR) does better for ASR and USA (VM-ASR) does better for S2TT. Can the authors hypothesize why this might be? This trend of the task right after the unsupervised objective benefiting more also appears in Table 5 (UEC benefits En ASR more and UCE benefits Zh ASR more).  


* Saif et al. 2024 is most related to this work and should be explained in more detail either in the "Related Work" section or in Section 3.2. The authors should explicitly mention how it differs from the proposed VS-ASR/VC-ASR objectives.  


* Minor typo on line 185: It should be l_s(\theta, \phi_t^n) (not \phi_t^N).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper shows advantages of integrating unsupervised loss as constraining objectives within a multilevel multi-objective optimization. The paper experimented with LibriSpeech and AISHELL and CoVoST v2 dataset for both ASR and speech-to-text translation tasks and has shown detailed results indicating segregating highly conflicting objectives into different optimization levels.

### Strengths
Novel approach in optimizing the multi-objective for ASR, S2TT tasks yielding improved results for Speech recognition, S2TT. The experiments and approach have been well-documented 
It explained the reasoning of optimization order in MLO yielding different outcomes where UAS optimization sequence yields superior performance
It also shows that choosing right penalty parameter playing a crucial role in MLO based ASR training

### Weaknesses
The experimental results provided a stronger base for the results, however it could be helpful to have more theoretical reasoning for the same

### Questions
Can there be any further improvement done for improving training time or reducing GPU memory?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Multitask multilingual ASR consists of several objectives that may conflict with each other, and existing multiobjective optimization (MOO) methods can train models in a conflicting-objective-aware manner to resolve the conflicts to some extent. This paper provides a comprehensive comparative analysis of 3 MOO methods on 2 tasks (ASR and S2TT) and a suite of languages. The paper shows consistent improvements of MOO-based methods over non-MOO-based baselines and ablates several design choices.

### Strengths
1. The paper shows that training with an conflicting-objective-aware optimization technique (e.g. based on MOO) improves performance on ASR and S2TT across a bunch of languages, which was a nice finding.
2. The paper performs comprehensive analyses for each of their algorithm’s components e.g. the ordering of the tasks, the choice of the penalty hyperparameter, comparisons for 2 model sizes, etc.
3. The performance improvements are nice and consistent across settings.

### Weaknesses
1. The paper emphasizes multitask and multilingual learning but only considers 2 tasks (ASR and S2TT). It was unclear to me whether the findings of the paper would generalize to a true multitask setup with > 2 tasks. It does already consider several languages, which is great.
2. There are some missing baselines that I believe are needed to ensure that it is indeed conflicting objectives that cause degraded performance, and that MOO solves them. See the ‘Questions’ section for a description of these baselines.
3. Since the proposed methods are more resource-heavy than baseline, it would be fairer to report a memory-/speed-matched comparison between baselines and the proposed methods.
4. The related work section mentions that multi-task learning for joint ASR-S2TT has seen limited exploration but cites a range of papers that indeed do tackle joint ASR-S2TT; I recommend removing the ‘limited exploration’ phrase. Also, worth citing the Whisper paper (https://arxiv.org/abs/2212.04356) as an example of a model that does joint ASR and S2TT>
5. Writing: The writing can be made crisper as it was a little confusing at times. Concretely, throughout the paper you refer to ASR and S2TT tasks as ‘multitask ASR’; but S2TT is not an ASR task. I recommend calling them ‘multitask speech-to-text’ tasks for example. Also, the equations in Sections 4.1 - 4.3 consist of equations that are difficult to parse; I recommend simplifying them a little. The discussion in Section 5 can be made significantly crisper; there is no need to repeat many of the same numbers from the table again in the text.

### Questions
1. Each MOO objective (VS-ASR, VC-ASR, VM-ASR) seems to have a simpler non-MOO counterpart, which I refer to as the 'VS-ASR' baseline, 'VC-ASR' baseline and 'VM-ASR' baseline. I would like to see each of these baselines to ensure that the sophisticated MOO framework is actually what is resulting in the improved performance.
    1. 'VS-ASR' baseline: joint pretraining and finetuning (e.g. https://ieeexplore.ieee.org/abstract/document/10447834 which is cited in the paper). This baseline is already included in this paper, which is good.
    2. 'VC-ASR' baseline: pretraining followed by finetuning (by freezing the backbone, or by training the backbone with regularization on the pretraining loss), similar to KL divergence or L2 loss based continual learning regularizers.
    3. 'VM-ASR' baseline: pretraining, followed by freezing the backbone, finetuning one set of classification heads, freezing those and finetuning second set of classification heads, etc. (similar to parameter-efficient finetuning methods)
2. Could you describe the baselines (PT+FT, static weighting, and PT+FT w/o MOO) in more detail?

### Soundness
3

### Presentation
2

### Contribution
2
