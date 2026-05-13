# MT-Ranker: Reference-free machine translation evaluation by inter-system ranking

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
Traditionally, Machine Translation (MT)  Evaluation has been treated as a \textit{regression problem}---producing an absolute translation-quality score. This approach has two limitations: i) the scores lack interpretability, and human annotators struggle with giving consistent scores;  ii) most scoring methods are based on (reference, translation) pairs, limiting their applicability in real-world scenarios where references are absent.
In practice, we often care about whether a new MT system is better or worse than some competitors. In addition, reference-free MT evaluation is increasingly practical and necessary. Unfortunately, these two practical considerations have yet to be jointly explored.  
In this work, we formulate the reference-free MT evaluation into a \textit{pairwise ranking problem}. Given the source sentence and a pair of translations, our system predicts which translation is better. In addition to proposing this new formulation, we further show that this new paradigm can demonstrate superior correlation with human judgments by merely using indirect supervision from natural language inference and weak supervision from our synthetic data.
In the context of reference-free evaluation, \modelname, \textit{trained without any human annotations},  achieves state-of-the-art results on the WMT Shared Metrics Task benchmarks DARR20, MQM20, and MQM21.
On a more challenging benchmark, ACES, which contains fine-grained evaluation criteria such as addition, omission, and mistranslation errors, \modelname \ marks state-of-the-art against reference-free as well as reference-based baselines

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel reference-free machine translation evaluation method which directly compares the two hypotheses from two systems by pre-trained language models, e.g., mT5.

### Strengths
The manuscript is commendably clear in its presentation, providing a lucid explanation of the method's underpinnings and its design rationale. The method itself is logically structured and appears to be grounded in a sound understanding of the underlying technical principles.

### Weaknesses
(Main) 1. **Experimental Settings**: Upon meticulous examination, I observe that the experimental setup deviates from the conventional practices of evaluating numerous systems simultaneously. The study opts to assess a custom set of 'Better-worse judgments' between pairs of system outputs. This focus narrows the scope of the evaluation and raises concerns about the validity of the correlation results. The paper's method shows a strong correlation with these judgments but fails to conclusively demonstrate the superiority of one system over another. The more critical challenge lies in integrating these pairwise comparisons into a comprehensive evaluation framework that can handle multiple systems. The current approach's limitations in addressing this challenge may undermine its utility and applicability.

2. **Scope and Generalization**: The narrow focus of the study may limit its applicability beyond its stated domain. The paper could benefit from an expanded discussion on how the proposed method might adapt or extend to other evaluation contexts, such as the assessment of large language models (LLMs). While ICLR might be receptive to specialized domain contributions, the paper's current emphasis suggests that it might find a more fitting audience at a dedicated NLP conference.


### Questions
1. How should the paper address the ranking of two MT systems? Is there a more robust method than simply tallying the number of better translations?
2. When scaling up the evaluation to multiple systems, how might one resolve apparent ranking contradictions, such as the scenario where System A outperforms System B, System B outperforms System C, but System C outperforms System A?

These questions are pivotal in addressing the practical implications of the proposed method and its capacity to function in a more complex, real-world evaluation environment. A more thorough exploration of these aspects could substantially strengthen the paper’s contribution to the field.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a method to learn pairwise reference-less evaluation of MT. This scenario corresponds to a common, real use where reference translations are mostly unavailable and the interest is mostly in comparing systems, rather than absolute scores. The pairwise ranking is a good framework since it is easier to collect synthetic data with pairwise judgments, as opposed to assigning quality scores to synthetic examples. Pairwise rankings also achieve higher inter-annotator agreement than human judgments. The method proposes a 3-stage pipeline for finetuning with various kinds of synthetic data. 

The results show that the approach can achieve state-of-the-art performance comparable or better than supervised approaches. The analysis also shows that adding supervised data can further improve performance modestly. Interpreted in another way, it also means that the synthetic data generated is sufficient to capture most of the attributes of supervised data for pairwise ranking of systems.

### Strengths
* The paper is well-written and explains the motivation for the work well. 
* The experiments are extensive and establish that reference-less evaluation is very competitive with reference-based metrics. 
* The use of synthetic data for pairwise ranking is a very clean way of using synthetic data and helps train high-quality reference-less metrics.

### Weaknesses
While pairwise evaluations of systems are useful, a more practical utility would be to rank multiple models. Score-based systems enable that easily. With pairwise ranking-based systems, multiple comparisons have to be run. Every time a new system has to be ranked, it has to be compared with multiple existing systems.

### Questions
* Equation 11 should be y=0?
* 3 languages from the WMT-20 Metrics tasks have not been included in the evaluation. It would be good to include those results as well for getting a complete view of the WMT-20 Metrics task.

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
This paper proposes a comparative MT evaluation metric: instead of comparing machine translations to references, it compares multiple machine translations. The model is built on a bidirectional LLM, that encodes pairs of translations, and a pooling and logistic regression layer on top. It is trained with data from crosslingual NLI, pairs of human and machine translations, and synthetically rated or corrupted pairs of translations. Evaluation is done on a set on the WMT20 metrics task, several MQM datasets and ACES, a challenge dataset. The proposed model is compared to previous state-of-the-art reference-free metrics and largely outperforms them across languages, as well as supervised baselines.

### Strengths
- Idea and method are simple and well explained. Given that it requires much less costly data than the competing methods, it poses an attractive solution for MT evaluation.
- The reported results are strong, given that they do not require references or direct supervision. The proposed model outperforms both supervised and unsupervised baselines.
- The ablations give an insight into the importance of the different stages and generalization to unseen languages, which allows one to get a more thorough understanding of the method and its benefits.

### Weaknesses
The novelty seems limited / overemphasized. In Quality Estimation (QE) reference-free ranking approaches have been used for MT quality estimates before it was re-invented in the context of MT metrics competitions. For example, in the very first QE task in 2012 (https://www.statmt.org/wmt12/quality-estimation-task.html) ranking based evaluations (without references) were already designed, and as a result, ranking based methods have been developed as well (e.g. Avramidis, Eleftherios. "Sentence-level ranking with quality estimation." Machine translation 27.3-4 (2013): 239-256.; Eleftherios Avramidis. 2012. Comparative Quality Estimation: Automatic Sentence-Level Ranking of Multiple Machine Translation Outputs. In Proceedings of COLING 2012, pages 115–132, Mumbai, India.)

### Questions
- Can you explain what the sentence “relative ranking annotation from direct assessment with a large enough threshold has been used with as few as one annotation” (Intro) means? Where does the threshold come into play and what does it mean to have one annotation only (I assume one per input, but not only one input)?
- Figure 1 is not adding much, its content is clear from the text. The space could be used to elaborate the connections to QE (see above) and report more empirical results on newer datasets.
- Is there any train/test overlap of the training data of mT5 and the benchmarks’ test data? 
- What if references were removed from the fine-tuning sets in Stages 2 and 3? This would be a useful ablation to make the models truly free from references.
- Which of the evaluation differences are significant? 
- What if Stages 1&2 are dropped and only Stage 3 is performed? This would further illustrate the importance of that stage and make it clear for future use where most time investment should go.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes Comparator, a reference-free MT evaluator that treats the evaluation as a inter-system comparison problem. The model consists of a pre-trained encoder that accepts the concatenation of the source sequence and a pair of translations to compare and a comparator head that pools the output embeddings and produces a binary decision on which translation is better. The model is trained in three stages: XNLI pre-training (preferring entailment over non-entailment), human/machine translation discriminating (preferring human translation over machine translations) and weakly-supervised tuning (pairs of translations judged by BertScore and synthetic data by perturbation). The proposed model is evaluated on various MT eval datasets and the results show its effectiveness and benefits even over supervised baselines.

### Strengths
- The proposed method is straight-forward and shows good performance over a range of datasets.
- Some of the indirect and weakly supervised training method is interesting and might be inspiring for future study of MT evaluation.

### Weaknesses
 - I’m wondering if the comparison is fare for other systems since the proposed model is trained with multiple external resources such as XNLI and especially some data with parallel sentences, and is based on large base pre-trained encoders. I think it would be more convincing if there can be ways to directly compare different evaluation systems (ref-free vs ref-included, score-based vs comparison-based) with the same training resources and base models. (But surely, it would be indeed a benefit if the proposed system can better utilize extra resources.)
- There should be more analysis on the proposed methods (such as those in Section 5). For example, more ablation studies on the training stages and especially the usage of different resources, and more detailed analysis on the metric and perturbation methods in Stage 3. Some of the result and setting sections may be shorten or moved to the appendix.
# --
- (Updates): Most of these concerns are addressed by the authors' responses, and the authors should provide those details in later versions.

### Questions
- What pre-trained model did the baseline systems use? Did they use up to XXL models? (Same or similar base models should be utilized for fair comparisons.)
- Are there any ways to convert the relative comparisons to absolute scores? Sometimes, we might still need the scores (for example as rewards for RL).
- In Stage 2 and the first part of Stage 3, references are required for the training purpose. If those two parts are ablated, how would it influence the results?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
