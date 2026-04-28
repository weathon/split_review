# On more accurate alignment modeling methods for automatic speech recognition

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
The connectionist temporal classification (CTC) training criterion
optimizes the conditional log probability of the label sequence given the input,
which involves a sum over all possible alignment label sequences including blank.
It is well known that CTC training leads to peaky behavior
where blank is predicted in most frames and the labels are focused mostly on single frames.
Thus, CTC is suboptimal to obtain accurate word boundaries.
Hidden Markov models (HMMs) can be seen as a generalization of CTC
and trained in the same way with
a generalized training criterion,
and may lead to similar problems.
Label units such as subword units and its vocabulary size or phoneme-based units
also significantly impact the alignment quality.
Here we study different methods of obtaining an alignment
with the goals
to improve alignment quality
while keeping a good performing model,
and to gain better understanding of the training dynamics.
We introduce
(1) a synthetic framework to study alignment behavior,
and compare various models, noise and training conditions,
(2) a new training variant with renormalizing the gradients to counteract the class imbalance of blank,
(3) a novel CTC model variation to use a hierarchical softmax and separating the blank label in CTC,
as another alternative to counteract class imbalance,
(4) a novel way to get alignments via the gradients
of the label log probabilities w.r.t. the input features.
This method can be used for all kinds of models,
and we evaluate it for CTC and attention-based encoder-decoder (AED) subword based models
where it performs competitive and more robustly,
although phoneme-based HMMs still provide the best alignments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper tackles the problem of CTC models for ASR and the poor quality of the word-level alignment due to the use of a "blank" token, no explicit silence label and "peaky" output labels. To help ameliorate the issue, the authors introduce an artificial task to study alignment behavior of various systems under tightly controlled conditions, ie. the amount of silence and distribution of word start and end times are set precisely to yield known distributions.

The contributions of the paper include synthesizing a task for diagnostic purposes, a renormalized gradient training regime for CTC to counteract the well known class-imbalance with the blank token, reformulating the CTC output into a hierarchical softmax, then blank/non-blank, as alternate mitigation  for blank class-imbalance, and lastly computing the alignment from gradients. The experiments demonstrate the usefulness of the mixing the transition, prior and posterior probabilities and the alignment are generaly robust to these values as long as they are not too extreme (e.g. \alpha=1.0, \beta=\gamma=0.); also the hierchical softmax "separated blank", normalized gradient and alignment via gradient were all found to be beneficial in generated better alignments with CTC models.

### Strengths
Well written and motivated with a strong set of experiment and analyses on well-controlled synthetic task and realistic test sets.
Contributions are good for a widely used class of model (CTC) and address an important aspect of the model ie alignment quaility for transcription.

### Weaknesses
The paper focuses on a narrow subject for the ICLR community, namely transcription alignment quality for CTC modeling. Its hard to make a constructive comment on how to make this work more broadly appealing to the general ICLR audience.

While the paper introduces several techniques to improve alignment, the evaluation is primarily focused on a synthetic task and a single real-world dataset. The generalizability of these findings to more diverse datasets and acoustic conditions is not fully explored. The paper also lacks a comparison with other alignment techniques beyond standard CTC decoding, making it difficult to assess the relative advantages of the proposed methods. The computational cost of the proposed gradient-based alignment method, especially when compared to simpler decoding techniques, is not thoroughly discussed, which is important for practical applications.

### Questions
In Table 1, the penultimate line where \alpha=0.5 is better than \alpha=1.0 is this because the posterior scores are too sharp? Do you have any intuition on why this scaling performs better?

In Table 2 of this paper,  the CTC models have worse TSE 89.5ms on the same dataset in https://arxiv.org/pdf/2407.11641 (Table 1, best 38ms). What are the differences in the training/modeling that explain the difference in TSE?

In Section 7.3 the paper reports on Blank Separation and no improvement in convergence rate. Another reported benefit is computational; while it may implementation dependent, do you have any results that demonstrate efficiency gained from the hierarchical softmax?

### Soundness
3

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
CTC training commonly leads to peaky behavior where the model predicts blank in most frames and the labels are focused mostly on single frames. Therefore, CTC is suboptimal in obtaining accurate word boundaries. Gaussian mixture hidden Markov models are typically used to obtain reliable and accurate segment and word boundaries. 

This paper proposes modifications to the CTC training criterion and training procedure to improve alignment quality. The paper proposes normalized gradients as an alternative to training with label priors to improve CTC training. The paper also proposes to separate the blank label in CTC loss calculation to counteract class imbalance.

### Strengths
The paper is well-written and systematically builds the improvements to the CTC to reduce the peakiness in CTC alignments.

### Weaknesses
My main critique of the work is that the proposed method doesn't seem to be all that effective at improving the alignment quality. For example,

Section 7.2, "NORMALIZED GRADIENT", L460 "Unexpectedly, there does not seem to be any improvement in terms of alignment quality (TSE). Also, in terms of convergence rate, there was no difference"
Section 7.3, "BLANK SEPARATION IN CTC" while the left-right boundaries improve by separating the blank, there is still a significant gap between the CTC alignments and GMM reference alignment. There seems to be no improvement for the word center positions. There is no improvement in the convergence rate and the reduction in WER is very small (<0.2).

Overall the results seem significantly worse than GMHMM alignments.

### Questions
Does the baseline CTC (e.g. in Table 4,5 ) use frame-level priors during training? If not, why not? Why are previous works (Zeyer et al., 2021; Chen et al., 2023; Huang et al., 2024) not included in the result tables?

### Soundness
2

### Presentation
3

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
This submission focuses on the important goal of improving the alignment model for ASR, primarily for the CTC framework, but with consideration of the AED framework too. A synthetic data experimental framework is adopted as part of the investigation, in addition to evaluations performed on the well-known public domain datasets, Switchboard and LibriSpeech. New alignment modeling techniques are proposed: (1) a gradient normalization method aimed at class balancing, (2) a blank-factored CTC model, and (3) a gradient-based approach to obtaining the gradients for both CTC and AED. The results suggest that the blank-factored CTC model yields slightly more accurate time alignments, and slightly better WERs too; and that the gradient-based method for obtaining alignments improves alignment quality for larger vocabularies.

### Strengths
Improving alignment quality is a highly relevant practical topic in the field of ASR, and this work provides value in evaluating a number of reasonable variants of current modeling methods. The evaluation includes use of controllable synthetic data framework, as well as well-known public benchmarks. Some small but significant improves in alignment quality and WER are presented.

### Weaknesses
The presentation and writing seem a bit rough, and in particular, the motivation for some of the methods proposed is not expressed very clearly -- though the reader can speculate and fill in the blanks. The motivations stated in the Abstract and Introduction seem a bit vague. I don't disagree with most of the overall points made, but I think the reasoning could be made tighter and clearer. I think the 3 new model methods proposed can reasonably be expected to improve alignment quality, but it's not really detailed exactly why that is so... E.g. the notion of "imbalance". Just because e.g. the blank symbol or silence token occur very very frequently, why is that necessarily bad for a "naive", non-blank-factorized model's alignments? I can speculate, but ideally there would be a clearer argument than provided by the paper. Similarly for the proposed gradient based renormalization, the authors write: "Instead of the prior (which is e.g. estimated on the average of p(y | h)), now we use the prior estimated on the average of the soft alignment υ." Sounds reasonable, but what is the theoretical or practical advantage compared to using a standard prior normalization, as previously proposed in the literature? Same question for the gradient-based obtaining of the gradients. For AED, the advantage is clear, since there is no explicit notion of alignment for AED. But what is the theoretical or practical advantage for CTC?

Regarding the Synthetic Data setup, in Section 6.1, I think it would be helpful to summarize the essential properties of the setup before going into the details. What are the specific dimensions that the authors wish to control, that the synthetic data setup provides?

In the Abstract:

"Hidden Markov models (HMMs) can be seen as a generalization of CTC": usually we think of the CTC model as existing within the broader HMM framework, not the other way around.

"Label units such as subword units and its vocabulary size...": it is not clear what "its" refers to here.

L037: "The classic speech recognition models such as Gaussian mixture hidden Markov model (GM-HMM) and later the hybrid neural network (NN)-HMMs (Bourlard & Morgan, 1993) rely on frame-wise cross-entropy training on a single best alignment path": (1) GMM-HMMs do not use cross-entropy training; (2) and both GMM-HMMs and Hybrid ASR DNN/HMMs have often been trained with dynamic programming to sum over all alignment paths. Embedding dynamic programming into the optimization process has been a standard tool for HMM-based ASR for decades, see e.g. Rabiner & Juang, "Fundamentals of Speech Recognition", 1993. (I suppose we can disagree on what is the "most classic" approach, but it seems to me the statement is too strong).

L045: "HMMs can be trained with the sum over all alignments as well, and differ from CTC only by label topology." To me this is a type mismatch: CTC exist within the HMM family, so "HMMs" actually includes a multitude of topologies, including CTC. It's like saying, "Animals can live in many different environments, and differ from cats only in what they eat."

L071: "word-error-rate" --> "word error rate"

L121: "averaged of the posterior" --> "average of the posterior"

L167: "This is very related to the training criterion with a prior: Instead of the prior (which is e.g. estimated on the average of p(y | h)), now we use the prior estimated on the average of the soft alignment υ": I agree, but what is the advantage?

L203: "In this case, the classes in pA are much more balanced compared to the classes in pY , as blank is usually the most imbalanced class": blank is the more frequent class, certainly, but what does it mean for a class to be imbalanced...? "Imbalanced" is a negative value judgment, but the authors don't flesh out why e.g. a very frequent class poses a problem to alignment modeling -- though the reader might agree with the statement, it should be motivated with a specific theoretical or practical intuition.

L373: "7.1.2 PHONEME-BASED MODELS" Clarify early on that the results in this section will use Switchboard and LibriSpeech, not the synthetic data?

L399. "Here, we use less number of epochs" --> "Here, we use fewer epochs" or "Here, we use a smaller number of epochs"

Re: Switchboard and LibriSpeech in 7.1.2: though the authors provide citations for these in the Appendix, it seems the citations should appear in the section? This section is a slightly odd mix of self-contained and not self-contained, in the sense that the Switchboard results are in Table 2 of the main body, the LibriSpeech results discussed are in Table 10 of the Appendix.

L531: "framerate" --> "frame rate"

### Questions
In addition to the questions I mention above, some specific comments/questions on the text:

In the Abstract:

"Hidden Markov models (HMMs) can be seen as a generalization of CTC": usually we think of the CTC model as existing within the broader HMM framework, not the other way around.

"Label units such as subword units and its vocabulary size...": it is not clear what "its" refers to here.

L037: "The classic speech recognition models such as Gaussian mixture hidden Markov model (GM-HMM) and later the hybrid neural network (NN)-HMMs (Bourlard & Morgan, 1993) rely on frame-wise cross-entropy training on a single best alignment path": (1) GMM-HMMs do not use cross-entropy training; (2) and both GMM-HMMs and Hybrid ASR DNN/HMMs have often been trained with dynamic programming to sum over all alignment paths. Embedding dynamic programming into the optimization process has been a standard tool for HMM-based ASR for decades, see e.g. Rabiner & Juang, "Fundamentals of Speech Recognition", 1993. (I suppose we can disagree on what is the "most classic" approach, but it seems to me the statement is too strong).

L045: "HMMs can be trained with the sum over all alignments as well, and differ from CTC only by label topology." To me this is a type mismatch: CTC exist within the HMM family, so "HMMs" actually includes a multitude of topologies, including CTC. It's like saying, "Animals can live in many different environments, and differ from cats only in what they eat."

L071: "word-error-rate" --> "word error rate"

L121: "averaged of the posterior" --> "average of the posterior"

L167: "This is very related to the training criterion with a prior: Instead of the prior (which is e.g. estimated on the average of p(y | h)), now we use the prior estimated on the average of the soft alignment υ": I agree, but what is the advantage?

L203: "In this case, the classes in pA are much more balanced compared to the classes in pY , as blank is usually the most imbalanced class": blank is the more frequent class, certainly, but what does it mean for a class to be imbalanced...? "Imbalanced" is a negative value judgment, but the authors don't flesh out why e.g. a very frequent class poses a problem to alignment modeling -- though the reader might agree with the statement, it should be motivated with a specific theoretical or practical intuition.

L373: "7.1.2 PHONEME-BASED MODELS" Clarify early on that the results in this section will use Switchboard and LibriSpeech, not the synthetic data?

L399. "Here, we use less number of epochs" --> "Here, we use fewer epochs" or "Here, we use a smaller number of epochs"

Re: Switchboard and LibriSpeech in 7.1.2: though the authors provide citations for these in the Appendix, it seems the citations should appear in the section? This section is a slightly odd mix of self-contained and not self-contained, in the sense that the Switchboard results are in Table 2 of the main body, the LibriSpeech results discussed are in Table 10 of the Appendix.

L531: "framerate" --> "frame rate"

### Soundness
3

### Presentation
2

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
The paper proposed several methods to alleviate the peaky behaviour in CTC training. The methods seem to provide more accurate alignment for ASR training with the CTC objective. The authors claimed the contributions from 4 aspects. 1). providing a framework to study alignment behavior based on artificially generated data, and compare various model, noise and training conditions. 2) proposing a new training variant: normalized gradients as an alternative to training with prior. 3) using a novel CTC model variation: Separating the blank label in CTC, as another alternative to counteract class imbalance, leading to improved alignment quality. 4) proposing to us a novel way to get alignments via the gradients of the label.

The storytelling of the proposed methods is not well organized and not that coherent. From my personal understanding, I don't see an obvious gain for some methods and some contributions claimed are not that significant. See comments below for details.

### Strengths
The strengths of the paper are:

1. The proposed methods are novel and interesting. We do see more accurate alignment with the method of separating CTC blank.
2. A good connection between the CTC and HMM models.

### Weaknesses
The weaknesses of the paper are:

1.  The paper is not well organized, making it hard to follow the main contribution and the most significant part of the paper.
2.  Some of the claims in the contribution is weak as I observed from the results.



### Questions
Here are details for my comments and suggestions to improving the quality of the paper.

1. Clarity:

a. Please provide a definition of TSE. Is it an average number over words or? I expect it to be the lower, the better.

b. What is Fw CE in Table? Please clarify.

c. I don't quite understand the role of synthetic data section. It looks like the experiments with synthetic data are used to obtain insights of training with different prior, posterior and transition scales. Table 1 shows that CTC (alpha=1, beta, and gamma=0) doesn't work for the synthetic data. However, similar ablations have been conducted on Switchboard dataset in Table 1 and of course CTC would work. Another example is using prior is helpful in the synthetic data but not that obvious on Switchboard data. I doubt if Table 1 and the contribution of using synthetic data as a useful tool are really helpful here.

d. It is confusing that the authors using different reference alignments to compute the TSE score, e.g. GMM alignment in Table 2 and CTC forced-alignment in Table 3. This would make the numbers not comparable to each other.

e. The AED model is used when evaluating the effectiveness of the proposed gradient-based alignments, making the entire paper very distracted. First, ablations on different training dynamics on HMM and CTC model without talking about improving alignment quality. Second, proposing grad norm and separating blank on CTC models. Lastly, using gradient-based alignment on CTC and AED. A natural question would be how does grad norm and separating blank CTC work on the hybrid CTC/AED framework since AED model is mentioned and studied in the paper.

2. Performance

a. I am not sure if I understand the metric quality, but in table 4, it looks like blanksep would improve the alignment quality while normed grad would improve the ASR performance as a prior. Are the rows with norm grad and Blanksep separately or incrementally added on top of baseline? If separately, do you have experiments to combine the two? If incrementally, it looks like the normed grad would remove the alignment quality gain brought by blanksep. Can authors give more explanations on this?

b. It is hard to sense the alignment quality improvements. In table 4, the TSE decreases from 111ms to 98ms, which is around 1.5 frames. I am not expecting it as a significant improvement, maybe I am wrong. It would be great if the authors can showcase the reference and generated alignments so that the readers can have a better understanding of the improvements.

c. It is sad to see no big ASR performance gain with the proposed methods. The alignment quality improvement can also be significant though.

### Soundness
3

### Presentation
2

### Contribution
2
