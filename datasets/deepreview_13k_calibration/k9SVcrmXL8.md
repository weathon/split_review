# BECLR: Batch Enhanced Contrastive Few-Shot Learning

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
\vspace{-0.2cm}
Learning quickly from very few labeled samples is a fundamental attribute that separates machines and humans in the era of deep representation learning. Unsupervised few-shot learning (U-FSL) aspires to bridge this gap by discarding the reliance on annotations at training time. Intrigued by the success of contrastive learning approaches in the realm of U-FSL, we structurally approach their shortcomings in both pretraining and downstream inference stages. We propose a novel \texttt{Dy}namic \texttt{C}lustered m\texttt{E}mory (\ourmodule{}) module to promote a highly separable latent representation space for \emph{enhancing positive sampling} at the pretraining phase and infusing implicit class-level insights into unsupervised contrastive learning. We then tackle the, somehow overlooked yet critical, issue of \emph{sample bias} at the few-shot inference stage. We propose an iterative \texttt{Op}timal \texttt{T}ransport-based distribution \texttt{A}lignment (\ourft{}) strategy and demonstrate that it efficiently addresses the problem, especially in low-shot scenarios where FSL approaches suffer the most from sample bias. We later on discuss that \ourmodule{} and \ourft{} are two intertwined pieces of a novel end-to-end approach (we coin as \ourmethod{}), constructively magnifying each other's impact.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed an Unsupervised few-shot learning method (BECLR). The key idea is to extend the memory queue concept to dynamically updated memory clusters (DyCE). The second key idea is to address sample bias issue (distribution shift between the unlabeled Query set and the labeled support set) by introducing OpTA at inference time. BECLR is the name of the overall method.

### Strengths
The paper tried to address several issues within a single framework. It benefits from contrastive pre-training, tries to address and distribution shift and address some of the issues around the memory queue concept. 
It seems that empirical results are strong.

### Weaknesses
-SAMPTransfer (Shirekar et al 2023) is also based on membership but its performance is reported only on the miniImageNet-->CDFSL task (Table 3). It is missing from other experiments. 
-Prior FSL works that are related to the distribution shift (sample bias) issue are not discussed. 
-Table 1: For ResNet-50 and Wide ResNet backbones, some of the comparison methods are missing. Again, in Table 3 some of the comparison methods are missing. It seems that the subset of methods used in each experiment is an arbitrary subset of the available pool of the previous methods.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In the presented paper, the authors identify two primary limitations in the existing Unsupervised Few-Shot Learning (U-FSL) methods and introduce an integrated solution named BECLR. BECLR incorporates two novel components: a dynamic clustered memory module named DyCE, designed to improve positive sampling in contrastive learning, and an efficient distribution alignment strategy termed OpTA, devised to counteract sample bias in U-FSL. While BECLR is tailored for U-FSL, the authors highlight DyCE's potential broader applications in general self-supervised learning, noting its superior performance even without OpTA, and advocate for the inclusion of OpTA in all U-FSL methods, particularly in low-shot scenarios.

### Strengths
**Originality**: The paper showcases a distinct approach by addressing recognized limitations in U-FSL and introducing the BECLR solution, merging existing concepts innovatively and presenting fresh modules like DyCE and OpTA. 

**Quality**: The research is robust, with DyCE and OpTA being methodically developed and their effectiveness demonstrated through comparisons with established methods like SwaV, SimSiam, and NNCLR.

**Clarity**: The authors articulate their findings and methodologies clearly, ensuring that readers can grasp the intricacies of BECLR, DyCE, and OpTA without ambiguity. 

**Significance**: With its potential to redefine self-supervised learning and its implications for U-FSL, especially in few-shot scenarios, the paper holds substantial importance in advancing the field and offers a direction for future research.

### Weaknesses
1. The overarching idea and structure of BECLR bear a striking resemblance to PsCo, particularly when observing Figure 2. It appears that the primary distinction is the concatenation of different views of 'X' from PsCo and the addition of a dynamic clustered memory. To differentiate their work more effectively, the authors should provide a comprehensive comparison with PsCo in both the introduction and related work sections, highlighting the unique aspects of their approach.

2. The notation used in the algorithmic section needs elucidation. Clearly defining each symbol would make it more accessible and allow readers to follow the content with greater ease.

3. The experimental section could benefit from an additional test: an evaluation of performance without merging 'X'. It would also be insightful to see results when PsCo is merged and when masking is applied, offering a more comprehensive understanding of the method's robustness and versatility.

### Questions
1. **Model Parameter Updates during Testing:** During the testing phase, are there any updates required for the model's parameters? If yes, how many times is the model updated?

2. **Comparison with PsCo in Terms of Model Size and Inference Time:** How does BECLR compare to PsCo regarding the number of parameters in the model and the inference time? A direct comparison would provide clarity on the efficiency and scalability of BECLR.

3. **Data Utilized for MiniImagenet Pretraining:** When pretraining with miniImagenet, which specific datasets were employed? Was the entire miniImagenet dataset utilized for this purpose?

Suggestions:

- **Enhanced Clarity on Parameter Update Mechanism:** A deeper dive into the model's updating mechanism during testing would be valuable. This would provide insights into the adaptability and robustness of the model, especially in real-world scenarios where data dynamics may vary.

- **Detailed Comparative Analysis with PsCo:** Given the similarities noted between BECLR and PsCo, a side-by-side comparison in terms of model parameters and inference time would offer readers a clearer perspective on the advantages and potential trade-offs of adopting BECLR.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a framework that comprises several part to better extract representations from images under the assumption that one single image in a batch corresponds to just one unique class. And also to address the issue of sample bias when few examples are playing crucial role even in cases where the sample is way higher. 
\
The main contributions are: \

a) the end-to-end framework terms BECLR that incorporates the modules that address sample bias and expands single image instance discrimination \

b) Very good results in a number of benchmarks.

### Strengths
The paper is detailed and relatively easy to follow. The underlying method is well explained and motivated and is substantiated by several experiments and ablations. \

The results are promising and impressive and the method is well grounded.

### Weaknesses
The evaluation should have considered the various components in separation and with respect to other methods.
E.g. is OPTA that improves performance or perhaps adding another base line method might have had a similar performance. 
I think in such multi-component frameworks this is an issue usually. 



### Questions
a) are the results presented throughout the paper are primarily based on the end-to-end process that involves all components, including OPTA? \
b) To be fair we need to see how other baselines work when replacing OPTA, e.g. other methods and/or linear evaluation principles for FSL. OPTA seems to have a considerable effect but is that down to the method itself or other baseline methods added to this framework could have a similar effect? \
c) Is there a reason why you did not consider running on the entire imagenet?

Typos: \
there are several typos throughout the paper - e.g. abstract "Critical" not "Clinical", "downstream" not "downstrea" and others.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
