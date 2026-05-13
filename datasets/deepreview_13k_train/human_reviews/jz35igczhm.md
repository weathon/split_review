# Brain-inspired $L_p$-Convolution benefits large kernels and aligns better with visual cortex

- Decision: Reject
- Scores: 5, 8, 8, 8, 5

## Abstract
Convolutional Neural Networks (CNNs) have profoundly influenced the field of computer vision, drawing significant inspiration from the visual processing mechanisms inherent in the brain. Despite sharing fundamental structural and representational similarities with the biological visual system, differences in local connectivity patterns within CNNs open up an interesting area to explore. In this work, we explore whether integrating biologically observed receptive fields (RFs) can enhance model performance and foster alignment with brain representations. We introduce a novel methodology, termed $L_p$-convolution, which employs the multivariate $p$-generalized normal distribution as an adaptable $L_p$-masks, to reconcile disparities between artificial and biological RFs. $L_p$-masks finds the optimal RFs through task-dependent adaptation of conformation such as distortion, scale, and rotation. This allows $L_p$-convolution to excel in tasks that require flexible RF shapes, including not only square-shaped regular RFs but also horizontal and vertical ones. Furthermore, we demonstrate that $L_p$-convolution with biological RFs significantly enhances the performance of large kernel CNNs possibly by introducing Gaussian-like structured sparsity in convolution. Lastly, we present that neural representations of CNNs align more closely with the visual cortex when $L_p$-convolution is close to biological RFs. This research shines a light on the potential of brain-inspired models that merge insights from neuroscience and machine learning, with the hope of bridging the gap between artificial and biological visual systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this submission, the authors propose to bridge the gap between artificial and biological visual receptive fields by introducing $L_p$ convolutions implemented modeled using the multivariate p-generalized normal distribution (MPND). The authors claim that it is possible to model a spectrum of receptive fields with increasing resemblance to biological receptive fields by tuning the $p$ and $\sigma$ parameters of MPND. On a Sudoku quiz benchmark, the authors show that L-p convolution is capable of learning diversely shaped receptive fields. On a couple of image classification benchmarks (CIFAR-100 and Tiny ImageNet), the authors show that tuning $p$ in various convolutional architectures integrated with $L_p$ convolution leads to classification performance gains. Representational similarity analysis testing the neural encoding ability of $L_p$ convolutional networks at different values of $p$ shows that networks with smaller $p$ (which are characteristic of biological RFs modeled with $L_p$ convolution) are better encoders of mouse visual representations.

### Strengths
+ This submission proposes a very interesting characterization of the disparities between artificial and biological receptive fields using multivariate p-generalized normal distributions (MPNDs).
+ The authors have worked rigorously on their model comparison experiments by testing all models with different random initializations and adequate statistical testing to highlight significant differences.
+ It is really interesting that $L_p$ convolutions with smaller $p$ values are also better encoders of mouse visual representations recorded from V1 in response to natural images.
+ Thanks to the authors for releasing code for reproducing their results.

### Weaknesses
 - The paper is quite hard to read. Especially the sections introducing $L_p$ convolution (sections 2 and 3) need to be written with much more clarity to make them more accessible. Currently, there are issues such as an abundance of notations, symbols being introduced after their first use, etc. that make it difficult to understand exactly how $L_p$ convolution works and models the spectrum from biologically resembling to artificial receptive fields.
- I don't find the similarity of $L_p$ convolution with small p with mouse visual receptive fields to be very convincing. First of all, this seems like a qualitative comparison and is not an objective way to measure similarity to biological receptive fields. It also seems from Appendix A4 (Fig 7A) that the mouse functional synapses in V1 lack any visible structure representative of selectivity to low-level visual features. This is quite concerning as it makes one wonder whether these neurons are selective to low-level features as one would expect from V1 neurons.
- There also seems to be an issue with both untrained and trained receptive fields of AlexNet's conv1 layer in the same figure. Untrained filters seem to have a peculiar checkerboard-like structure that one wouldn't expect in randomly-initialized kernels. Re. pretrained filters, in the AlexNet paper [1] the authors plot the filters in the first convolution layer of an AlexNet trained on ImageNet-1k in Figure 3 of their paper. There is a big gap in terms of how selective their filters are in comparison to the filters visualized in the current submission in Figure 7 of Appendix A4. Could the authors please explain this discrepancy?
- Overall, I believe that in the current state, there are several open issues such as the (key) ones I highlighted here in my review that need to be fixed in order to push this paper above the acceptance threshold.

### Questions
Please refer to the weaknesses section in my review above.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The Authors introduce the so-called Lp-convolution that is based on the multivariate p-generalized normal distribution to address the gap between the artificial and biological receptive fields. The Authors study the properties of the Lp-convolution and provide evidence that the proposal benefits, for instance, large kernel sizes in a classification task using previous well-studied architectures (e.g., AlexNet) with the CIFAR-100 and TinyImageNet datasets.

### Strengths
The manuscript has been well-written, and the ideas behind the paper have been legibly presented with an experimental part following the requirements of the ICLR conference.

I have found the most attractive part of the paper in section 6, where The Authors evaluated the alignment between biological
and artificial models.

### Weaknesses
I do not see particular weaknesses in the manuscript.

### Questions
Could the Authors comment on how their work is related to the concept of foveation?

https://doi.org/10.1007/s11263-016-0898-1

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, large convolution kernels are masked by multiplication with a parameterizable function that can range from a 2D Gaussian to a more box-like function. The mask parameters are trained with the rest of the network. Suitable masks are learned in a network that solves Sudoku puzzles. Adding this method to several common architectures improves their image classification performance. Activity in these trained networks is compared with mouse visual cortex activity via representational similarity analysis, and it is found that more Gaussian-like masks tend to produce higher peak similarities between mouse and model representations.

### Strengths
The method is interesting, elegant, effective, and as far as I know novel. The paper is clear and well organized. The experiments make sense for demonstrating several different properties of the model, and the results seem convincing.

### Weaknesses
I don’t find much to complain about but I will do my best.

It’s interesting that the mask is more general than a Gaussian function, but the benefits of non-Gaussian versions seem less clear (e.g. Table 1). I don’t know whether I should actually use this mask rather than a simpler Gaussian one. 

The p value that sets the smoothness of the mask seems not to change much during training, judging by the visualizations in Figure 2 and the performance differences due to different initializations of p in Table 1. I wasn’t sure that it was actually being optimized effectively. If it were optimized more successfully then it seems that a method other than initialization might be needed to apply pressure on p one way or another (such as a loss term).

In the Figure 1g caption please clarify which comparisons were tested and whether there was a correction for multiple comparisons.  

Page 8 says the models were compared with data from multiple subregions of mouse V1, but the appendix shows VISal, VISam, etc. as well as VISp. Is V1 a typo on page 8? 

Please elaborate on the logic of the definition of functional synapses in the 3rd paragraph of A.2. Is it meant to relate to biological functional synapses? How? 

In Figure 7 b and c, the middle-row (untrained) receptive fields have a grid structure and the ones in the bottom rows (trained) mostly have a bright line along the bottom. Could these phenomena please be explained?

### Questions
In the Figure 1g caption please clarify which comparisons were tested and whether there was a correction for multiple comparisons.  

Page 8 says the models were compared with data from multiple subregions of mouse V1, but the appendix shows VISal, VISam, etc. as well as VISp. Is V1 a typo on page 8? 

Please elaborate on the logic of the definition of functional synapses in the 3rd paragraph of A.2. Is it meant to relate to biological functional synapses? How? 

In Figure 7 b and c, the middle-row (untrained) receptive fields have a grid structure and the ones in the bottom rows (trained) mostly have a bright line along the bottom. Could these phenomena please be explained?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose adding a gaussian mask to the square kernels of CNNs/transformers, parametrized by the L_p metric, to give ANN receptive fields a flexibility similar to Biological NNs (BNNs). They find that these including these Lp masks improve network accuracy

### Strengths
The basic idea is very compelling. 

The connection to BNNs is well supported.

The paper is very well-written.

The results table has +/- std devs.

### Weaknesses
I am left wondering if CNNs do this RF masking already, by different means.

I am unclear how the covariant matrix C is trainable. what is the update process?

Reviewer limitation: I am not well-versed in this literature, so I am assessing the paper itself with limited background.


Notes to ICLR: 

1. Please include line numbers in the template. They make reviewing much easier! 

2. Please reformat the default bibliography style to make searching the bib easier! eg numbered, last name first, initials only except for last name.



General review context: Please note that I am simply another researcher, with some overlap of expertise with the content of the paper. In some cases my comments may reflect points that I believe are incorrect or incomplete. In most cases, my comments reflect spots where an average well-intentioned reader might stumble for various reasons, reducing the potential impact of the paper. The issue may be the text, or my finite understanding, or a combination. These comments point to opportunities to clarify and smooth the text to better convey the intended story. I urge the authors to decide how or whether to address these comments. I regret that the tone can come out negative even for a paper I admire; it's a time-saving mechanism for which I apologize.

Key comments:

Note: Addressing the two issues in "Weaknesses" above would be great. The rest of the comments can be handled as the authors see fit.

Bibliography: Perhaps reformat the bibliography for easier searching, eg numbered, last name first, initials only except for last name.

Abstract "gaussian-like structured sparsity": I don't think of gaussian weightings as "sparse", since few values get sent to zero. Is this the correct technical term for what is happening?

1. paragraph 1, "LecCun and ... by introducing backprop": Backprop was not LeCun. I think more complete citations are needed here.

1. paragraph 1, "alexNet": CNNs blew up with the convergence of backprop, CNNs, big data sets, and GPUs that enabled training them.

1. Paragraph 2, list of similarities: A 4th important similarity is local RFs (as you note in the next paragraph).

Provided code :)

2. Multivariate p-general... "the reference position of the RF": Do you mean "reference position of a pixel in the RF?". If not, I am confused.

Eqn 1: Is the superscript "p" standard notation? I think I usually see L_p as ||   ||_p (subscript only).

Covariate matrix C: does this raise dimensionality issues, since C includes d^2 new parameters per filter? (doubles the number of free parameters I think).

Fig 1 e: this shows up too small on a printed page.

Fig 1 f: Did you try p < 2? It looks like the masks converge to rectangles (all weights in mask the same) at low p, so that the difference between 4 and 16 is slight. 

3. "introduce L_p convolution": clever mechanism.

Just after eqn 4 "C and p are trainable": I do not see how to do this. Is it explained in the paper?

"mask take one": I stumbled on this. Clearer might be "equal one", or "have the value one". Also, maybe note that this is the limit as p increases, and in fact is roughly attained at p = (some value).

4. Sudoku: Perhaps explain why this is a good test case for the method (since it is not usual, and the usual image examples come later).

Fig 3 b: the line colors/labels are unclear in these subplots. Perhaps make them bigger, or use dashed lines for some cases, or change to brighter colors.

Fig 4: What is the definition of "distortion"?

Fig 4 a: The different labels (alpha, theta) on the two sides of the mosaic are hard to decipher, especially on a printed page. Perhaps make the mosaic horizontal, or make labels larger, or break up the sets of 9 boxes with bolder lines, or provide clearer guidance in the caption.

Fig 4 a: what role do diagonal masks play in the Sudoku networks, given the problem's horizontal-vertical-box structure?

Fig 4 a: A crucial question for me: These RFs look a lot like what we often see in CNN papers. Is the L_p method generating something novel, or is it a new way of getting to what already happens?

Comparisons with base models:  It appears that adding an L_p mask at each filter effectively doubles the free parameter count while holding the filter size fixed. Might this account for the difference in accuracy scores?

Section 7: This looks like it should appear earlier in the paper - it is background.

### Questions
General review context: Please note that I am simply another researcher, with some overlap of expertise with the content of the paper. In some cases my comments may reflect points that I believe are incorrect or incomplete. In most cases, my comments reflect spots where an average well-intentioned reader might stumble for various reasons, reducing the potential impact of the paper. The issue may be the text, or my finite understanding, or a combination. These comments point to opportunities to clarify and smooth the text to better convey the intended story. I urge the authors to decide how or whether to address these comments. I regret that the tone can come out negative even for a paper I admire; it's a time-saving mechanism for which I apologize.

Key comments:

Note: Addressing the two issues in "Weaknesses" above would be great. The rest of the comments can be handled as the authors see fit.

Bibliography: Perhaps reformat the bibliography for easier searching, eg numbered, last name first, initials only except for last name.

Abstract "gaussian-like structured sparsity": I don't think of gaussian weightings as "sparse", since few values get sent to zero. Is this the correct technical term for what is happening?

1. paragraph 1, "LecCun and ... by introducing backprop": Backprop was not LeCun. I think more complete citations are needed here. 

1. paragraph 1, "alexNet": CNNs blew up with the convergence of backprop, CNNs, big data sets, and GPUs that enabled training them.

1. Paragraph 2, list of similarities: A 4th important similarity is local RFs (as you note in the next paragraph).

Provided code :)

2. Multivariate p-general... "the reference position of the RF": Do you mean "reference position of a pixel in the RF?". If not, I am confused.

Eqn 1: Is the superscript "p" standard notation? I think I usually see L_p as ||   ||_p (subscript only).

Covariate matrix C: does this raise dimensionality issues, since C includes d^2 new parameters per filter? (doubles the number of free parameters I think).

Fig 1 e: this shows up too small on a printed page.

Fig 1 f: Did you try p < 2? It looks like the masks converge to rectangles (all weights in mask the same) at low p, so that the difference between 4 and 16 is slight. 
 
3. "introduce L_p convolution": clever mechanism.

Just after eqn 4 "C and p are trainable": I do not see how to do this. Is it explained in the paper?

"mask take one": I stumbled on this. Clearer might be "equal one", or "have the value one". Also, maybe note that this is the limit as p increases, and in fact is roughly attained at p = (some value).

4. Sudoku: Perhaps explain why this is a good test case for the method (since it is not usual, and the usual image examples come later).

Fig 3 b: the line colors/labels are unclear in these subplots. Perhaps make them bigger, or use dashed lines for some cases, or change to brighter colors.

Fig 4: What is the definition of "distortion"?

Fig 4 a: The different labels (alpha, theta) on the two sides of the mosaic are hard to decipher, especially on a printed page. Perhaps make the mosaic horizontal, or make labels larger, or break up the sets of 9 boxes with bolder lines, or provide clearer guidance in the caption.

Fig 4 a: what role do diagonal masks play in the Sudoku networks, given the problem's horizontal-vertical-box structure?

Fig 4 a: A crucial question for me: These RFs look a lot like what we often see in CNN papers. Is the L_p method generating something novel, or is it a new way of getting to what already happens?

Comparisons with base models:  It appears that adding an L_p mask at each filter effectively doubles the free parameter count while holding the filter size fixed. Might this account for the difference in accuracy scores?

Section 7: This looks like it should appear earlier in the paper - it is background.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Inspired by the observation that the spatial distribution synaptic inputs in the early visual system of the brain is approximately Gaussian, the authors propose a masking strategy for convolution filters in convnets for image recognition. They observe that such (approximately) Gaussian masking enables convnets to learn with larger filters, leading to improved performance on the Sudoku challenge and a number of small-scale image classification tasks. They also show that networks trained with Gaussian masked filters exhibit slightly increased representational similarity to the mouse visual system.

### Strengths
+ Creative inductive bias transfer from biology to machine learning
 + Overall well-written paper
 + Well-motivated and well-executed experiments

### Weaknesses
1. Effect sizes are quite small
 1. A number of details on the experiments remain unclear even after screening the appendix

 a) In the Sudoku challenge, the main argument seems to be about the imbalance between row/column and block accuracy, but the difference in accuracy is <10% in all cases, which doesn't strike me as a particularly worrisome imbalance. In particular, the difference between p=2 and 7x7 (Large) is <1% (although I'm not sure what the latter model exactly is; see below). Could this be a matter of presentation and the differences would be much clearer if you looked at error rates instead of accuracy? Could you explain why you think these results are important given such small effect size?

 b) In the image classification experiments, there is a clearly significant improvement due to Lp-Conv, but not on all architectures and again the improvement is small (a few percent). Given that architectural modifications alone can now push accuracy on CIFAR-100 >90% (https://arxiv.org/abs/2304.05350v2), the 2–3% improvements in the 60–70% range feel a bit insignificant. Can you explain why you think your approach is still worthwhile? Would we expect similar gains if we included the Gaussian masking inductive bias into more modern architectures?

 c) In the representational similarity experiments the improvements due to p=2 are in the range of 0.5–2%. Again, why are such small differences relevant from a scientific point of view if the differences between, e.g., AlexNet and ConvNeXt-T are of the same order of magnitude?


 1. Experimental details

 a) Are the masks applied after training to the trained weights or during training? If the latter, does it change anything about what the network learns? It could just learn larger weights W where the mask is small, leading to the exact same network as without masking. Why is this not happening?

 b) It is not clear to me what the different networks in Fig. 3 are. It's clear that 3x3 and 7x7 refer to the kernel size. But what does "Large" refer to and what is the Lp^{\dagger} model?

 c) As far as I understand Fig. 3, p=2 refers to p being initialized as 2 but then optimized as a trainable parameter, correct? If so, what was p at the end of training for the three models with p={2, 16, 256}? This question actually applies to all experiments.

 d) Table 1: ResNet has larger kernels than 3x3 in the first layer. Are they kept the same in all variants and only the 3x3 kernels in the later layers are modified?

 e) Fig. 5: I did not fully grasp what "Max. SSM" exactly refers to. In panel a) five brain areas are colored; in panel b) five network architectures. Presumably you compared all architectures against all brain areas. What exactly is being reported here? Why is there not one such plot as in b) per brain area?


 1. Other questions

 a) Why is the spatial distribution of synapses the right thing to compare to weights in a CNN? The presynaptic neurons also have spatially extended receptive fields (RFs), which means the V1 neuron's RF envelope in pixel space is not the same as the retinotopically mapped synaptic locations.

### Questions
I am somewhat torn on the paper. While I appreciate the clear motivation and hypothesis, I am somewhat underwhelmed by the results and/or how they are (over?)sold in the paper. If the authors can provide convincing answers to the following questions, I am willing to adjust my score.

### 1. Effect size

While I very much appreciate the three main experiments presented in Fig. 3, Table 1 and Fig. 5, I am somewhat underwhelmed by the effect sizes.

 a) In the Sudoku challenge, the main argument seems to be about the imbalance between row/column and block accuracy, but the difference in accuracy is <10% in all cases, which doesn't strike me as a particularly worrisome imbalance. In particular, the difference between p=2 and 7x7 (Large) is <1% (although I'm not sure what the latter model exactly is; see below). Could this be a matter of presentation and the differences would be much clearer if you looked at error rates instead of accuracy? Could you explain why you think these results are important given such small effect size?

 b) In the image classification experiments, there is a clearly significant improvement due to Lp-Conv, but not on all architectures and again the improvement is small (a few percent). Given that architectural modifications alone can now push accuracy on CIFAR-100 >90% (https://arxiv.org/abs/2304.05350v2), the 2–3% improvements in the 60–70% range feel a bit insignificant. Can you explain why you think your approach is still worthwhile? Would we expect similar gains if we included the Gaussian masking inductive bias into more modern architectures?

 c) In the representational similarity experiments the improvements due to p=2 are in the range of 0.5–2%. Again, why are such small differences relevant from a scientific point of view if the differences between, e.g., AlexNet and ConvNeXt-T are of the same order of magnitude?


### Experimental details

 a) Are the masks applied after training to the trained weights or during training? If the latter, does it change anything about what the network learns? It could just learn larger weights W where the mask is small, leading to the exact same network as without masking. Why is this not happening?

 b) It is not clear to me what the different networks in Fig. 3 are. It's clear that 3x3 and 7x7 refer to the kernel size. But what does "Large" refer to and what is the Lp^{\dagger} model?

 c) As far as I understand Fig. 3, p=2 refers to p being initialized as 2 but then optimized as a trainable parameter, correct? If so, what was p at the end of training for the three models with p={2, 16, 256}? This question actually applies to all experiments.

 d) Table 1: ResNet has larger kernels than 3x3 in the first layer. Are they kept the same in all variants and only the 3x3 kernels in the later layers are modified?

 e) Fig. 5: I did not fully grasp what "Max. SSM" exactly refers to. In panel a) five brain areas are colored; in panel b) five network architectures. Presumably you compared all architectures against all brain areas. What exactly is being reported here? Why is there not one such plot as in b) per brain area?


### Other questions

 a) Why is the spatial distribution of synapses the right thing to compare to weights in a CNN? The presynaptic neurons also have spatially extended receptive fields (RFs), which means the V1 neuron's RF envelope in pixel space is not the same as the retinotopically mapped synaptic locations.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
