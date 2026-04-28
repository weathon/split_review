# Learning dynamic representations of the functional connectome in neurobiological networks

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
The static synaptic connectivity of neuronal circuits stands in direct contrast to the dynamics of their function. As in changing community interactions, different neurons can participate actively in various combinations to effect behaviors at different times. We introduce an unsupervised approach to learn the dynamic affinities between neurons in live, behaving animals, and to reveal which communities form among neurons at different times. 
The inference occurs in two major steps.} First, pairwise non-linear affinities between  neuronal traces from brain-wide calcium activity are organized by non-negative tensor factorization (NTF). Each factor specifies which groups of neurons are most likely interacting for an inferred interval in time, and for which animals. Finally, a generative model that allows for weighted community detection is applied to the functional motifs produced by NTF to reveal a dynamic functional connectome. Since time codes the different experimental variables (e.g., application of chemical stimuli), this provides an atlas of neural motifs active during separate stages of an experiment (e.g., stimulus application or spontaneous behaviors). Results from our analysis are experimentally validated, confirming that our method is able to robustly predict causal interactions between neurons to generate behavior.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a novel analysis method to infer time-varying functional connectomes from neuronal data in general and calcium imaging data in C. elegans in particular. The method is based on a three-step procedure. First, time-varying affinities between pairs of neurons are computed based on concurrent changes of the neuronal signal. Second, a non-negative tensor decomposition is employed to identify neuronal-temporal motifs of affinity across animals. Thirdly, community structure is inferred from the motifs using a stochastic block model. Taken together, these steps enable an interesting visualization of dynamical functional connectomes. The authors apply their method to experimental data recorded in C. elegans during a stimulus avoidance / attraction paradigm and identify a neuron previously not implicated in salt sensing. They then experimentally test its role by exposing worms with / without the neuron silenced to a salt stimulus and find that indeed the worms respond behaviorally as predicted.

### Strengths
The authors identify and address a highly relevant problem, i.e., the issue that relationships between neurons are highly dynamic yet few algorithms are able to infer dynamical functional connectomes. Their new methods enables a new visualization of this complex, high-dimensional data and can be used to derive experimentally testable predictions on the time-dependent involvement of neurons in behaviorally relevant neuronal ensembles. The authors further test and validate one specific hypothesis experimentally in a behavioral experiment. Another strength is that the manuscript is very well written and easy to read.

### Weaknesses
Some of the algorithmic choices appear rather ad-hoc without a rigorous theoretical or neurophysiological justification. In particular, it is unclear to me why the problems in constructing a time-varying similarity measure, that the authors discuss in the second paragraph of Section 2.1, does not also apply to the derivatives of the calcium traces? Since the derivatives represent the influx/outflux of calcium, and are thus likely a better representation of the neurons' firing rates, I would think that similar problems persist? Also, it is not clear to me why the local differential affinities should be non-negative? One could argue that two neurons also form a network if one inhibits the other, which in my understanding would lead to a negative affinity?

A further (and significant) weakness is that no link to code is provided in the manuscript. I believe that making all code publicly available is absolutely essential for reproducibility.

Since the affinity matrices are symmetric, vectorizing these (and using Euclidean norms) does not seem to be the right choice here? Have you looked into proper distance metrics for symmetric matrices [1]?


### Questions
My most relevant question is regarding code availability -- why has the code not been made available, and how do the authors intend to remedy that situation?

Further questions are minor ones:

* Since the affinity matrices are symmetric, vectorizing these (and using Euclidean norms) does not seem to be the right choice here? Have you looked into proper distance metrics for symmetric matrices [1]?
* What does "CP" stand for on page 4? That abbreviation is not introduced?
* Why was the set of neurons restricted to sensory and inter-neurons? Did the results change when using all neurons?
* Would the method also work on other neuronal data modalities, e.g., spiking data?

1. Vemulapalli, Raviteja, and David W. Jacobs. "Riemannian metric learning for symmetric positive definite matrices." arXiv preprint arXiv:1501.02393 (2015).

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study presents an unsupervised method to identify the dynamic interactions between neurons. The approach has two main steps: first, based on calcium activity, the neural traces are organized to identify groups of neurons likely interacting over specific time intervals. Then, a generative model is applied to detect weighted communities in the functional patterns.

### Strengths
The paper is well-written and easy to follow. It is well-organized with illustrative figures. Also, the proposed method is simple, yet potentially effective for different tasks and domains. Moreover, compared to existing studies that use step-by-step statistical methods, this paper designs a method that allows considering the full system of similarities and animals across time. Also, presenting extensive experimental results supports the claim and the potential of the approach.

### Weaknesses
1. The main weakness of this paper is the lack of novelty in the model design. In fact, the proposed approach is a simple combination of existing methods and I cannot see a novel insight or a novel contribution from the machine learning side.

2. It would be better to include more related baselines. In the literature, there are several learning methods that learn the structure of the brain networks. Based on the current set of baselines, the proposed method shows superior performance, but existing baselines are general graph learning methods and do not use special properties of the brain. Therefore, I suggest adding additional brain network-based graph learning approaches as baselines.

3. There is a lack of discussion and experimental results about the scalability of the method and its efficiency. It would be great if the authors could provide more information about the efficiency of the method.

### Questions
Please see the Weaknesses.

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
The goal of this work is to infer community structure in neural networks (specifically that of _C. elegans_) based on functional data. To do this, the authors 1) define a pairwise affinity score computable from single-neuron time series; 2) use tensor factorization to group these pairs into dynamical motifs; 3) feed tensor components from these motifs into a community detection algorithm. When applied to data recorded from individually identified _C. elegans_ neurons, this produces networks that are tested in validation experiments, which find that perturbation of key nodes does affect network structure and behavior related to, e.g., salt avoidance.

### Strengths
- The problem of organizing functional data from neurons into more interpretable submodules that can be investigated in causal experiments is an important one.
- The approach is reasonable and makes use of established techniques (tensor factorization, community detection).
- Use of real neural data for both algorithm validation and suggesting perturbative experiments is a huge plus.

### Weaknesses
 - I found the affinity score a bit _ad hoc_. I can understand the intuition, but it seems like there should be a more principled way to get at this information. Related, but along the opposite direction: why not include strong _anticorrelations_ in the affinity score? Shouldn't two neurons whose activity moves opposite to one another at most times be considered related/coupled?
- The tensor factorization will tend to treat affinities independently of one another, though the $N(N-1)/2$ affinities result from only $N$ neuronal time series. That is, the tensor factorization does not respect the underlying geometry of the problem. It's unclear to me how big an issue this is in practice, but it might lead to issues with the method.
- While the experimental data are a definite plus, it's always unclear how strongly they should be taken as validation of a particular data analysis method. In a strongly coupled network, ablating any one neuron is likely to have an effect, and it's not shown that that the method proposed here would necessarily outperform others for selecting which perturbations to apply.

### Questions
- How sensitive are the results presented to the particular choice of affinity score? Would, e.g., a Spearman correlation between the two time series yield qualitatively similar results?
- I might have missed this, but how did the authors decide how many tensor components to retain?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
