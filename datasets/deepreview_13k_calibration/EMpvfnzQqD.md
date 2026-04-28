# OTTC: A differentiable alignment approach to automatic speech recognition

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 6, 3

## Abstract
The Connectionist Temporal Classification (CTC) and transducer-based models are widely used for end-to-end (E2E) automatic speech recognition (ASR). These methods maximize the marginal probability over all valid alignments within the probability lattice over the vocabulary during training. However, research has shown that most alignments are highly improbable, with the model often concentrating on a limited set, undermining the purpose of considering all possible alignments. In this paper, we propose a novel differentiable alignment framework based on a one-dimensional optimal transport formulation, enabling the model to learn a single alignment and perform ASR in an E2E manner.
We define a pseudo-metric, called Sequence Optimal Transport Distance (SOTD), over the sequence space and highlight its theoretical properties.
Based on the SOTD, we propose Optimal Temporal Transport Classification (OTTC) loss for ASR and contrast its behavior with that of CTC.
Experimental results on the English Librispeech and AMI datasets demonstrate that our method achieves competitive performance compared to CTC in ASR.
We believe this work opens up a potential new direction for research in ASR, offering a foundation for the community to further explore and build upon.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This is a well-written submission describing a novel application of Optimal Transport to the fundamental alignment problem in ASR. Re-casting alignments as a matrix of coupling weights representing the "transport" of units in a source alignment to units in a target alignment the authors to use concepts from Optimal Transport to minimize the overall transport cost efficiently and flexibly, in a way that mitigates the peaky behavior typically observed in ASR alignments based on the CTC model with dynamic programming. The work presents ASR results (WERs) on well-known public domain tasks (LibriSpeech and AMI); the proposed method trails the standard CTC model, but the work offers a fresh perspective on a long-standing challenge in core ASR modeling technologies. As such I think the work is a high interest to the community.

### Strengths
Clarity of presentation, quality of the writing, and originality; very good literature survey & references.

### Weaknesses
A few concepts could be explained more clearly. One thought regarding the evaluation: since the proposed method only learns a single alignment path, it might make sense to include a comparison with CTC models trained using the single best alignment paths for any given training utterance (aka the "Viterbi algorithm") rather than the standard sum over all possible alignments. I am wondering if the gap in WER between proposed method and standard CTC comes from the use of a single path, versus multiple paths. This could be part of the evaluation.

Adding to my earlier comment, if indeed a limitation of the work is that only a single path is learned, and though this of practical/computational interest, if further investigation were to reveal that this actually hurts generalization, could one formulate SOTD so as to learn multiple transports for each utterance?

More comments, mostly nits re: writing:

L048, "requires comparatively large amount of data" --> "requires a comparatively large amount of data"

L128: re: the "d-dimensional vector sequences": the writing suggests that x_i and y_i are both d-dimensional, is that intended...?

L190: specify what is a "δ measure"?

L195, "ν[β, n]", I think this should be "ν[β, m]"?

L207, " coupling matrix γ∗ ": is there a more informative term? It suggests this is an alignment matrix, but then AIU each entry is actually an amount of mass moved from i to j.

L223, "α→γ∗ =argmin_{γ∈Γ} W(μ[α,n],ν[β,m])," give the reader a heads up, How will γ typically be found... gradient descent, or some other method? Give an intuition about the east/difficultly therein?

L241, "The computational cost of these alignment functions is low," explain why? (relating to previous comment). (The cost seems to go beyond just the bins being sorted or not, but perhaps that is in fact the key aspect it is not completely clear to me).

L252, "Sequences Optimal Transport Distance (SOTD)": motivate this extension more? I.e., make it clear what is missing from the alignment model presented so far.

L271, "there is sequences" : fix typo

L302, "When the function F is powerful, the model can collapse ": be more precise than "powerful"? What types of specific functions would lead to collapse?

L325, "Ce", define Cross-Entropy somewhere? This would make e.g. Eq. (14) clearer .

L376, "relaxation of the last term ": what does "relaxation" here and in the following mean...?

L455, "peror-mance", fix typo

L520, "envision that learning label weights with suitable constraints can bridge the performance gap", be more specific?

L845, "SOTD ARE PSEUDO METRIC" --> "SOTD IS A PSEUDO METRIC"?

### Questions
Adding to my earlier comment, if indeed a limitation of the work is that only a single path is learned, and though this of practical/computational interest, if further investigation were to reveal that this actually hurts generalization, could one formulate SOTD so as to learn multiple transports for each utterance?

More comments, mostly nits re: writing:

L048, "requires comparatively large amount of data" --> "requires a comparatively large amount of data"

L128: re: the "d-dimensional vector sequences": the writing suggests that x_i and y_i are both d-dimensional, is that intended...?

L190: specify what is a "δ measure"?

L195, "ν[β, n]", I think this should be "ν[β, m]"?

L207, " coupling matrix γ∗ ": is there a more informative term? It suggests this is an alignment matrix, but then AIU each entry is actually an amount of mass moved from i to j.

L223, "α→γ∗ =argmin_{γ∈Γ} W(μ[α,n],ν[β,m])," give the reader a heads up, How will γ typically be found... gradient descent, or some other method? Give an intuition about the east/difficultly therein?

L241, "The computational cost of these alignment functions is low," explain why? (relating to previous comment). (The cost seems to go beyond just the bins being sorted or not, but perhaps that is in fact the key aspect it is not completely clear to me).

L252, "Sequences Optimal Transport Distance (SOTD)": motivate this extension more? I.e., make it clear what is missing from the alignment model presented so far.

L271, "there is sequences" : fix typo

L302, "When the function F is powerful, the model can collapse ": be more precise than "powerful"? What types of specific functions would lead to collapse?

L325, "Ce", define Cross-Entropy somewhere? This would make e.g. Eq. (14) clearer .

L376, "relaxation of the last term ": what does "relaxation" here and in the following mean...?

L455, "peror-mance", fix typo

L520, "envision that learning label weights with suitable constraints can bridge the performance gap", be more specific?

L845, "SOTD ARE PSEUDO METRIC" --> "SOTD IS A PSEUDO METRIC"?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a noval end-to-end loss for automatic speech recognition (ASR), called Optimal Temporal Transport Classification (OTTC), jointly learning temporal alignment and audio frame classification. This loss is derived from the introduced Sequence Optimal Transport Distance (SOTD) framework, which constructs pseudo-metrics over the sequence space. Central to this framework is a parameterized and differentiable alignment model based on one-dimensional optimal transport, offering linear complexity in both time and space. Experimental results on Librispeech and AMI datasets demonstrate that the proposed method achieves promising performance.

### Strengths
- The idea of this work is novel and non-incremental, supported by detailed mathematical theoretical proofs. Meanwhile, the writing style is excellent and impressive. 
- In theory, the proposed method achieves linear complexity both in time and space. Experimental results demonstrate that it mitigates the peaky behavior observed in the Connectionist Temporal Classification (CTC) models.

### Weaknesses
 - The performance of the proposed method is noticeably inferior to that of CTC, which significantly restricts its applicability in real-world scenarios, especially considering that CTC already lags behind transducer and hybrid systems combining CTC and attention-decoder. 
- The authors don't provide ablation experiments for the proposed OTTC model. I would suggest at least testing removing the OT weight prediction head and using fixed and uniform OT weights instead.

### Questions
- While OTTC theoretically offers linear complexity both in time and space, how about the practical training cost in terms of the GPU memory usage and training time compared to CTC? 
- In line 520-521, the authors state, "Furthermore, our framework effectively addresses the peaky behavior commonly seen in CTC models, resulting in improved alignments". To validate the claim of improved alignments, I would suggest computing quantitative metrics by comparing the decoding timestamps and the pre-computed ground-truth token-time alignments. 
- I noticed several possible typos: 
  - In line 156-157, "alignement" should be corrected to "alignment". 
  - In line 253-254, "[" should be corrected to "]".  
  - In Equation 3, should "$\gamma 1_n=\alpha$ and $\gamma^T 1_m=\beta$" be "$\gamma 1_m=\alpha$ and $\gamma^T 1_n=\beta$"? 
  - In Equation 11, should "A" be corrected to "W"? 
  - In Equation 12, should "$\log p_{l_j} (x_i)$" be corrected to "$\log p_{l_{y_j}} (x_i)$"?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to learn sequence to sequence prediction and alignment simultaneously. To achieve this, the authors define a pseud-metric called the Sequence Optimal Transport Distance (SOTD) over sequences based on one-dimensional optimal transport. SOTD enables the joint optimization of target sequence prediction and alignment.  They then derive the Optimal Temporal Transport Classification (OTTC) loss for automatic speech recognition (ASR). Experiments on the LibriSpeech and AMI datasets show that the proposed method achieves encouraging recognition accuracy, although it’s still worse than the popular sequence to sequence ASR modeling method Connectionist Temporal Classification (CTC). Besides, the alignment output from OTTC model does not have the peaky behavior observed in CTC-based models.

### Strengths
The optimal Temporal Transport Classification (OTTC) loss proposed in this paper has two parts, one is alignment related, based on Sequences Optimal Transport which is proved to be differentiable. Another is classification (or prediction) related, which is based on the cross-entropy loss. The advantage of this new loss is it enables the model to lean both the alignment and classification jointly. The authors explain and prove every mathematical theory behind this loss definition in detail. The authors also conduct proof-of-concept experiments on the ASR task and compare the results with CTC-based model. The results show the proposed method achieve reasonable speech recognition accuracy and alignment. Especially the alignment is not peaky as observed in CTC based ASR model.

### Weaknesses
The main weakness of the paper is that the experimental results didn’t show the better ASR accuracy of the proposed method when compared with CTC loss. It’s claimed that the alignment from the OTTC model is better than that from CTC model because it’s not peaky. But the author didn’t compare the alignment with the ground truth alignment to measure the alignment accuracy with convincing numbers. Below are some detailed comments: 
•	Figure 4 and figure 5 show the alignment of OTTC model, but none of them show the “ground truth” alignment. And the paper didn’t present measurements of the alignment accuracy from OTTC model in other way. So, it doesn't seem credible to claim that OTTC could get better alignment since it’s not compared with the ground truth alignment. The claim of improved alignment is based solely on the visual smoothness of the alignment matrices, which is not a sufficient metric for evaluation. The lack of quantitative comparison with ground truth alignments, or even with alignments produced by other methods using established metrics, makes it difficult to assess the actual quality of the alignments produced by the OTTC model. The authors should provide metrics such as precision, recall, or F1-score calculated against reference alignments to support their claims.
•	The target of OT part of the loss is to find out optimal “alpha”(or alignment), it would be better if the author do some analyze of the value “alpha” of the trained model to show what’s the optimal value and does it have any physical meaning.  Without an analysis of the learned alpha values, it's difficult to understand what the model has actually learned and whether the learned alignment has any meaningful interpretation. The authors should investigate the distribution of alpha values, their relationship with the input audio and the target text, and whether they exhibit any patterns that could provide insights into the alignment process. This analysis could involve visualizing the alpha values, calculating their statistics, and relating them to the speech signal and the corresponding text.
•	In this paper, the authors only show the results of uniform distribution of value “beta” and said learning the optimal beta is difficult. It would be better to show how the model will perform with other choice of beta (e.g. proportional to the letter duration) to show how “beta” will affect the results with different value? If the method is sensitive to the choice of “beta’. Then more work needs to be done to make this method applicable for real machine learning tasks. The lack of experiments with different beta distributions raises concerns about the robustness of the method. If the performance is highly sensitive to the choice of beta, it would limit the applicability of the method in real-world scenarios. The authors should explore different beta distributions, such as those based on letter duration or other relevant factors, and analyze their impact on the ASR performance. This would help to understand the sensitivity of the method to the choice of beta and identify the optimal beta distribution for different tasks. 
Besides, there are some typos (or errors) in the paper. like:
•	In equation (3). If the dimension of gamma is n*m, and the dimensions of 1n is n*1. Then the multiplication of these two matrices is not valid. Similarly, the transpose of gamma has dimension m*n, it couldn’t be multiplied with the matrix with dimension m*1. 
•	In equation (11). “A” in the left side of equal sign should be “W”, also “AW” in the right side of equal sign should be "W”.

### Questions
•	For OTTC model, the OT related parameters are frozen for the last 10 epochs in the experiment?  Why is number 10 used here and whether other values have been explored? Or how much will this parameter affect the results?
•	In section 6, it’s said that in the 960h-LibriSpeech training setup, it got 4.77% WER at epoch 30 and no meaningful improvement in WER at 40 epochs without freezing the OT weights. Does it mean the final WER is also around 4.77%? It’s also said the alignments remain relatively stable as training progresses. If so, freezing alignment vs. no freezing alignment shouldn’t have big difference, but based on table 1, freezing OT weights in the last 10 epoch could get 4.24% WER. Could the author explain more about this?

### Soundness
2

### Presentation
2

### Contribution
2
