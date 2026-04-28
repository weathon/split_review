# Towards a  learning theory of representation alignment

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
It has recently been argued that AI models' representations are becoming aligned as their scale and performance increase. Empirical analyses have been designed to support this idea and conjecture the possible alignment of different representations toward a shared statistical model of reality. In this paper, we propose a learning-theoretic perspective to representation alignment. First, we review and connect different notions of alignment based on metric, probabilistic, and spectral ideas. Then, we focus on stitching, a particular approach to understanding the interplay between different representations in the context of a task. Our main contribution here is relating properties of stitching to the kernel alignment of the underlying representation. Our results can be seen as a first step toward casting representation alignment as a learning-theoretic problem.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this manuscript the authors first give a review of various measures of representation alignment, with a particular focus on showing how they relate. They show that many different approaches can be straightforwardly related to kernel alignment.

The authors then formalise the stitching approach to measuring task-relevant representation alignment. They demonstrate that bounds on stitching error can be derived and related to the alignment metrics that they reviewed in the first section.

### Strengths
The manuscript is clear and well-written.

Although perhaps a little dense, the first section does a good job of introducing various notions of representation alignment and elucidating their relationships. I found this precise and succinct presentation to be useful and digestible.

The formalisation of stitching methods is also clear and straightforward. While the assumption of linear stichers is quite restrictive, it does lead to some nice proofs.

### Weaknesses
I don’t think the manuscript has any significant weaknesses.

I do think that at the end of section 3 it might be helpful to give a few sentence summary of the relationships between the various measures of alignment. While the preceding material is complete, it would help readers who perhaps have not digested all of that material on a first pass to more easily comprehend the manuscript.

As mentioned above, the restriction to linear stitching functions is potentially quite limiting. It might be nice to comment more on the impact of this assumption on the analysis.

It should be noted that I am not very familiar with the field of representation alignment, so I am not in a position to comment on this work relative to the existing literature. I will have to leave that to the other reviewers. My score reflects this uncertainty, but it should be understood that this is not a comment on the manuscript, but rather my uncertainty about its impact, novelty, and relevance.

### Questions
Just a few nits:

Figure 1: it would nice to note for the reader that these symbols will be defined in section 2.

L130: I’m not familiar with the notation using the #. Perhaps add a note or reference, or a an explanatory word or two in the sentence where it is first used?

L188: I didn’t understand why H_q had codomain \mathbb{R}. This seems to be assuming something about Y_q that up until this point hasn’t been assumed. Could you clarify?

L241 & L670: McDiarmin -> McDiarmid!

L351: modals -> models?

### Soundness
4

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
2

### Summary
The authors compiled broad notions of representational alignment metrics and provide connected interpretation. Next, they mathematically formulate stitching method, which is used to evaluate similarity of representations between different models given a task by plugging representation from one model to another. They provide the generalization error bound of linearly stitched model based on kernel alignment.

### Strengths
While I am not familiar with all the references,the first section of the paper where the authors make a overview of different formulation of representation alignment and provide connected interpretation from different community seems to be a nice contribution.

The theoretical formulation of stitching method that is used frequently in practice is relevant point and the results can give valuable insights to use of stitching method in practice

In general the paper is well-written and well structured.

### Weaknesses
- I appreciate the first section of the paper, but it would be nice to have the last paragraph where authors could summarize and make a brief overview of everything in one place. 

- While it being a solid theoretical work, I think it is great that the settings in questions are still relevant for practice. Having a couple of sentences summarizing practical implication of the results in conclusion might be helpful for broader audience.

- It is little confusing about significance of 'task defined representation' and 'modality specific representation' in stitching setting. 

Minor comments on the manuscript
- little confused by term 'representation $\mathcal{H}_q$' online 4 as I thought it's entire input-output mapping
- I think there are some indexing, sqrt typos on "Spectral interpreation of KA" section; what is $\rho$?
- Typo on line 494

### Questions
- In theorem 3, why does swapping the index 1,2 require $\mathcal{G}_1 = \mathcal{G}_2$ up to linear?

- On remark 3, could you elaborate little more on the regularization of $S_{1,2}$?

- It looks like the stitching setting is quite relevant to transfer learning. Could the current result tell anything about kernel alighment and its relevance on transfer learning perspective?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a theoretical perspective on representation alignment of AI models. 
The authors state  that while there is empirical work  that supports the idea of representation alignment for bigger models, there is little theoretical perspective on the idea of representational alignment. The authors focus on the practice of (model) stitching as a device to study representational alignment. More specifically, 
they first present different ways to measure representation alignment and then focus on stitching as task to contextualise a theory for representational alignment. 
The contribution of this paper is showing that a stitching error and stitching error bound can be derived based on the kernel alignment of the underlying representations.

Overall, I think this is a good paper attempting to provide a theoretical framework to representational alignment which is usually an empirical field of research. The derived stitching error and stitching error bound seem important in order to quantify generalisation error of different models. To improve the submission I would suggest making Section 4 more coherent with Section 3, since at the moment they seem a bit disconnected to me notation wise. I would also suggest either adding a small experiment showing the usefulness of the derived theory or contextualising it within current empirical methods.

### Strengths
- The authors do a good job of introducing the different concepts of kernel alignment and independence testing needed for their theory. 
- Using Kernel Alignment to provide a generalisation error bound for stitching seems novel and useful given the rise of representation learning.
- I think the paper is generally well written making it accessible for readers that are not that familiar with a learning theoretic perspective on this problem.

### Weaknesses
- It is unclear to me from Section 4 how the stitching error and stitching error bound can be used. Since the paper makes reference to existing empirical work, I would like to see a more concrete example or a reference to where the derived theory fits in existing empirical work.
- For instance how does the proposed theory quantify the stitching error in current approaches (e.g., can different layers be compared equivalently, does normalisation, regularisation play a role?).
- I feel there is a slight disconnect between sections 3 and 4. While in section 3 a comprehensive listing of ways to measure representation alignment is presented, the introduced notation is not really used in Section 4. This makes it a bit difficult to follow what parts of Section 3 inspired Section 4. Perhaps you could write a small paragraph at the beginning of Section 4 stating how Section 3 serves as building blocks for deriving the stitching error and stitching error bound in Section 4.

### Questions
- Would it be possible to design a small experiment with, e.g., MNIST where the stitching error (bound) is used to quantify the possible generalisation error?
- Alternatively you could add a small discussion on how your theory fits in with current stitching methods or how it could be applied to learn more better representations.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work proposes a theoretical foundation for understanding representations alignment, especially the alignments for multimodal models.
The main contribution is in the idea of connecting different representations through a so-called "stitching" mechanism.

### Strengths
The paper is generally well-written. The authors gave an excellent review of measures of representation alignment, which is a nice entry point for understanding the paper. 
This paper is also supported by a thorough mathematical argument about the stitching error between models.

### Weaknesses
1. The paper provides no empirical experiment demonstrating the proposed theory's correctness.
2. Only one type of stitching, Linear Stitching, is argued. It would be helpful if the authors could briefly explain other stitching types, as this will help to familiarize the readers to this idea.

### Questions
1. The reviewer understands that the authors try to avoid complexity by only arguing about linear stitching. But how is the generality of the linear stitching? And what is its limitation? Do different types of representations require different stitching?  Please add this argument in the discussion part of the paper.

2. Please provide at least one experiment to demonstrate the correctness of the proposed theory, for example, through transfer learning.

### Soundness
2

### Presentation
3

### Contribution
2
