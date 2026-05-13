# Improving Inverse Folding for Peptide Design with Diversity-Regularized Direct Preference Optimization

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Inverse folding models play an important role in structure-based design by predicting amino acid sequences that fold into desired reference structures. Models like ProteinMPNN, a message-passing encoder-decoder model, are trained to reliably produce new sequences from a reference structure. However, when applied to peptides, these models are prone to generating repetitive sequences that do not fold into the reference structure.  To address this, we fine-tune ProteinMPNN to produce diverse and structurally consistent peptide sequences via Direct Preference Optimization (DPO). We derive two enhancements to DPO: online diversity regularization and domain-specific priors. Additionally, we develop a new understanding on improving diversity in decoder models. When conditioned on OpenFold generated structures, our fine-tuned models achieve state-of-the-art structural similarity scores, improving base ProteinMPNN by at least 8\%. Compared to standard DPO, our regularized method achieves up to 20\% higher sequence diversity with no loss in structural similarity score.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies an important problem in protein design, inverse folding. The authors propose to fine-tune ProteinMPNN with DPO to generate diverse and structurally consistent peptide sequences. In experiments, the fine-tuned ProteinMPNN achieves state-of-the-art structural similarity scores and diversity.

### Strengths
- The paper is well-written and easy to follow.
- The authors observe that popular inverse folding models perform poorly for peptide design.
- This paper applies DPO to improve diversity.

### Weaknesses
 - ProteinDPO [1] has applied DPO to fine-tune ESM-IF to design more stable proteins. More comparisons are desired.
- The modified DPO algorithm is mostly based on vanilla DPO and is similar to ProteinDPO.
- In Table 1, the DPO fine-tuned ProteinMPNN does not achieve better diversity than vanilla ProteinMPNN significantly. The reported diversity decrease is concerning, given the stated goal of the paper.
- In Table 2, even with fine-tuning, ProteinMPNN + DPO is worse than ESM-IF in TM-Score. Therefore, it's interesting to fine-tune ESM-IF with the same algorithm.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel approach that could help design peptide sequences. It mainly uses an advanced DPO structure to finetune ProteinMPNN. The proposed model obtained a significant improvement in various metrics. The paper is easy to follow.

### Strengths
- The introduction of DPO into inverse folding is interesting. Finetuning Graph-based models may provide some insights into designing a smaller structural encoder.
- The paper integrates structural information into training (maximizing TM-score) in the inverse folding tasks. It is a nice try but it may also include bias (seen in the next part)
- The design of the reward function and the loss function avoids the reliability of the policy term, it is an interesting approximation!

### Weaknesses
 - In line 58, the use of Tmscore appears abruptly, as the models listed in the previous paragraph are purely structure-to-sequence models, there needs to be a further explanation about the idea of Inverse Folding, which is actually a structure-sequence-structure pipeline. Although it has been addressed in the Part 2.
- The use of the TM-score in training may lead to bias since the TM-score is obtained through a static structure prediction model. Although it may not be easy to analyze the reason, I think at least the authors can mention that and do some analysis (like using multiple structure prediction tools to calculate the TM-score to average the bias). It might be a little bit time-consuming, so it doesn’t have to be done in the rebuttal phase and it would have no effect on my rating. Just a concern.
- The approach itself is a bit target-specific, it did not work well on the co-optimization purpose as the author claims. From Table 1, the diversity and recovery do not excel from others, I am not blaming the results but curious about the reason.

### Questions
- As the paper compared to GVP, ProteinMPNN, and ESMIF, why doesn’t the paper compare with some more recent approaches? Since the paper cited the ProteinInvBench, it provided a model zoom and colab demo to re-run the newer models easily if the input sequence is ready.
- Could there be an appendix for analyzing the statistical features of the dataset used in training?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel DPO method to finetune inverse folding models on peptide design task, by adding online diversity regularization objective function and incoporating scalar reward into original DPO.

### Strengths
1. The concept of employing DPO for fine-tuning peptide inverse folding models is innovative.
2. Leveraging ColabFold and the Openfold database to address the data scarcity issue in peptide entries shows great promise.
3. The online diversity formulation appears to be an improvement over the original diversity-regularized objectives, and the inclusion of differential entropy is particularly inspiring.

### Weaknesses
1. As discussed in Sections 3.1 and 3.2, incorporating diversity regularizations and scalar weighted control into DPO is not a novel technique; it has been extensively studied in prior work, which may limit the paper's novelty.
2. The experimental setup is not comprehensive, particularly in terms of baseline details and sampling settings.
3. The presentation in Section 4 is somewhat unconventional; the theoretical analysis in Section 4.4 appears confusing and out of place.
4. The baseline results are limited and may not be convincing.
  + Clarify how the baselines are used: are they pretrained or fine-tuned? Since baseline methods like GVP-GNN are not trained on the OpenFold benchmark, this comparison may not be fair. Please provide clarification.
  + In line 267, the paper claims to use 4 samples and T=0, which is an unusual hyperparameter setting. T=0 implies deterministic sampling of ProteinMPNN (T=0.1 by default), and 4 samples are too few. I encourage using more samples (e.g., 64) and the original T setting.
  + Additionally, I recommend including more baselines, particularly fixed-backbone models specific to peptide design tasks (e.g., PepFlow by Li et al. 2024).
5. In Section 4.4, the paper introduces a new method using entropy instead of pairwise distance as a regularization term. However, this setting is not presented in the main results.

### Questions
1. The author should provide more comparisons to prior works, highlighting the differences, such as online optimization or ad-hoc scalar weighting. If possible, please include the original diversity regularization DPO and scalar weighting DPO in your baselines to study the improvements over these methods.
2. The baseline results are limited and may not be convincing.
+ Clarify how the baselines are used: are they pretrained or fine-tuned? Since baseline methods like GVP-GNN are not trained on the OpenFold benchmark, this comparison may not be fair. Please provide clarification.
+ In line 267, the paper claims to use 4 samples and T=0, which is an unusual hyperparameter setting. T=0 implies deterministic sampling of ProteinMPNN (T=0.1 by default), and 4 samples are too few. I encourage using more samples (e.g., 64) and the original T setting.
+ Additionally, I recommend including more baselines, particularly fixed-backbone models specific to peptide design tasks (e.g., PepFlow by Li et al. 2024).
3. In Section 4.4, the paper introduces a new method using entropy instead of pairwise distance as a regularization term. However, this setting is not presented in the main results. Please include this in the main results.

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
5

### Summary
This paper claims two main problems: 

The first one is current inverse folding methods cannot generate samples that can be folded to accurate structures sharing high similarity with the input ones (RMSD and TM-Score). The second one is current human verified peptide (<50 AA) structures is limited, leading to poorer performance in the inverse folding models. 

The authors propose a novel optimization method to address this problem via DPO while promoting sampling diversity, and obtain State-Of-The-Art performance on peptide deisgn tasks, with the evaluation metrics inculding TM-Score, Diversity, and Recovery.

### Strengths
1. The proposed challenges are attractive in this field. The inverse folding samples often suffers low TM-Scores, and diversity. Specially, towards peptide sequenes, the recovery rates are often lower than the samples with other lengths. 

2. The motivation behind the method is clear and reasonable. DPO-related methods on auto-regressive-based models work on the field of NLP. Furthermore, the diversity improvement is also impressive. 

3. The experiment is comprehensive w.r.t. analysis metrics.

### Weaknesses
1. The verfication of the proposed method is limited. There's so many popular approaches on protein inverse folding, such as PiFold, ESM-IF, LM-Design, VFN, and InstructPLM [1-5]. Regarding recovery and self-consistency TM-Score, there are approaches performing better than or competitive than ProteinMPNN. Thus, a robust method with board application should include more experiments to verify the effectiveness of the proposed methods. Specifically, the paper lacks a comparison to methods that explicitly optimize for sequence recovery or self-consistency, making it difficult to assess the true advantage of the proposed DPO approach. A more thorough comparison should include methods that use different architectures and training paradigms, not just variations of ProteinMPNN.

2. The proposed metric is not comprehensive enough, the self-consistency RMSD is also required to verifying the quality of sequence samples. The absence of RMSD as a metric makes it difficult to fully evaluate the structural similarity between the generated and target structures. TM-Score alone does not capture all aspects of structural similarity, and RMSD provides a complementary measure, particularly for local structural deviations.

3. The method is simple but the experiement results are not impressive enough to prove the effectiveness of DPO-based improvement. In Table1, the relative improvement over all metrics is smaller than or equal to 1% except TM-Score with 6%. The ablation results cannot indicate the power of proposed method enhancement. The reported improvements, especially in diversity and recovery, are marginal and do not convincingly demonstrate the superiority of the proposed method. The ablation study should have included more variations of the DPO method to isolate the effect of each component.

4. The length scale of main experiments are somehow not consistent, which makes the paper unclear to the readers. In Table1&2, the author states that they have had experiments on CATH4.3 (n=173) and Openfold (n=50), but 1) the filtering process is not clear in Openfold benchmark; 2) the filtering criteria of two benchmarks are inconsistent. The lack of clarity in the filtering process for the OpenFold dataset raises concerns about the validity of the comparison. Using inconsistent filtering criteria across different datasets makes it difficult to draw meaningful conclusions about the generalizability of the proposed method.

### Questions
1. Why you choose different filtering process of two benchmark datasets?
2. Why the diversity of ESM-IF on both datasets is zero?
3. Once the DPO-based method is effective to inverse folding methods, why the experiments are only conducted to the general protein. It is because I believe that the challenges you stated also exist in the general proteins. 
4. In the paragraph "Explaining diversity with differential entropy", can you please try to explain the interpretability via a mathematical proof to clearly state the connections between log-probabilities and diversity?

### Soundness
3

### Presentation
3

### Contribution
2
