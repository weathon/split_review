# AlphaFold Distillation for Protein Design

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 5, 3

## Abstract
Inverse protein folding, the process of designing sequences that fold into a specific 3D structure, is crucial in bio-engineering and drug discovery. Traditional methods rely on experimentally resolved structures, but these cover only a small fraction of protein sequences. Forward folding models like AlphaFold offer a potential solution by accurately predicting structures from sequences. However, these models are too slow for integration into the optimization loop of inverse folding models during training.
To address this, we propose using knowledge distillation on folding model confidence metrics, such as pTM or pLDDT scores, to create a faster and end-to-end differentiable distilled model. This model can then be used as a structure consistency regularizer in training the inverse folding model. Our technique is versatile and can be applied to other design tasks, such as sequence-based protein infilling.
Experimental results show that our method outperforms non-regularized baselines, yielding up to 3\% improvement in sequence recovery and up to 45\% improvement in protein diversity while maintaining structural consistency in generated sequences.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes AFDistill, a novel model that distills knowledge from AlphaFold to predict protein structural consistency (SC) scores pTM and pLDDT for a given sequence. AFDistill is used to regularize the training of inverse folding models by adding an SC loss term, which results in improved performance on benchmarks, boosting sequence recovery and diversity while maintaining structural integrity. Experiments demonstrate that SC regularization enhances inverse folding and infilling models, enabling accurate and diverse protein sequence generation. The fast, differentiable SC scores from AFDistill can also replace slower AlphaFold evaluations to cheaply assess structural properties of proteins.

### Strengths
- Utilize distillation method for transferring AlphaFold's knowledge into fast, differentiable SC scores.
- Implement AFDistill for cost-effective integration of AlphaFold expertise into design models.
- Conduct comprehensive experiments.

### Weaknesses
 - I am unclear about the motivation behind this paper, particularly regarding the decision to utilize (distilled) AlphaFold instead of directly using AFDB. For instance, the paper states, "Despite this success, large-scale training is computationally expensive. A more efficient method could be to use a pre-trained forward folding model to guide the training of the inverse folding model." However, I fail to see the efficiency benefits of this approach, as utilizing the AF model (or distilled AF models) would entail additional on-the-fly inference costs compared to employing the AFDB.
- It is not clear whether the proposed method can outperform the model trained with AFDB or not. 
- The overall performance improvement appears not much, and it is not clear where the gain comes from.

### Questions
- Is there a comparison between using AFDB and using AF-Distill?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors present AFDistill, a distilled model of AlphaFold2 that is used for protein inverse folding. AFDistill is based on ProtBERT and trained to predict the TM/LDDT and pTM/PLDDT of protein structures. The model is then used as a differential oracle for structure-consistency loss in training protein inverse folding model (e.g., GVP, ProteinMPNN, PiFold). The experiments show that the proposed model improves the diversity of predicted amino acid sequences and keep comparable performance in other metrics (recovery and perplexity).

### Strengths
1. The insight to distill AlphaFold2 for efficient inference in protein-related tasks is well-motivated. 
2. Integration of structure consistency in inverse protein folding is important and should intuitively lead to better performance.

### Weaknesses
1. One major concern is the lack of technical novelty. AFDistill is based on existing ProtBERT without major modification of the model. The core idea of using a pre-trained language model to predict structural quality metrics is not entirely novel, and the paper does not sufficiently articulate the specific innovations in their approach beyond the application to this particular task. The modifications to ProtBERT, if any, are not clearly detailed, making it difficult to assess the technical contribution.
2. Though experimental results show significant gain in diversity of predicted amino acid sequences, the improvements on other metrics (e.g., recovery and perplexity) are trivial. The paper needs to provide a more thorough analysis of why the gains in diversity do not translate to more substantial improvements in recovery and perplexity. It is also not clear if the increase in diversity comes at the cost of other important properties of the generated sequences, such as stability or functionality.

### Questions
Other questions besides Weakness:

1. In Fig. 1, there are lines (CE loss <-> AlphaFold) that cross with each other, which can make it confusing. 
2. Why AFDistill uses discretized output (50 bins) instead of directly implementing regression tasks?
3. what is the value of $\alpha$ in Eq. 1 and how is it determined?
4. How does integration of AFDistill affect the training resources for protein inverse folding models? 
5. The authors separate the experimental results of different models into different tables. It may be better to collect main results of different models (GVP, ProteinMPNN, PiFold, etc.) in one table for better illustration. 
6. Different balanced datasets are introduced to train AFDistill. What is the main take-away of choosing which dataset for inverse folding?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method for inverse protein folding, which is the process of designing amino acid sequences that fold into a desired 3D structure. The key steps are:

- Knowledge distillation from AlphaFold to create a fast and differentiable model called AFDistill that predicts structural confidence scores (pTM, pLDDT) for a given sequence.

- Using AFDistill's predicted scores as a "structure consistency" (SC) regularization term when training inverse folding models like GVP, ProteinMPNN, etc.

### Strengths
S1. Novel idea of distilling AlphaFold into a fast and differentiable model (AFDistill) for structural consistency prediction.

S2. Elevation in recovery rate is observed though marginal.

### Weaknesses
W0. Given the marginal improvements, it is unconvincing that using plDDTs as loss (L_sc) for sequence design is really useful or not.

W1. The extra compute resources costs are significant in this plan, including both the distillation and the extra cost in evaluating / backpropagating L_sc. No justification of these extra computational costs is presented.

W2. A generated sequence with high plDDT generally means that it is *conservative* (easy to be predicted), but this is not an indicator that it corresponds to the target structure. Therefore, using plDDTs intuitively encourage "sequence stability" instead of "structural consistency". Two concepts are confused in this paper.

W3. Paper needs proofreading.

W4. In the evaluation part, the authors confused pTMs from AFD as TM. This metric lacks commonsense and is misleading, because it is totally irrelevant with the target structure. Under such evaluation, the elevation in so-called self consistency is trivial. The real TM between a structure prediction and the target structure should be reported.

### Questions
Q1. In AF2 the plDDT depends on the quality of MSAs and templates. How is the plDDT/pTM obtained? Especially for the augmented datasets where the authors run AF by themselves?

Q2. How would the authors justify that the smallest distillation set leads to largest improvements?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
