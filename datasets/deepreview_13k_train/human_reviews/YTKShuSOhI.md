# Demonstrating the capacity of a Path-Based variational inference formulation for robust hidden Markov modelling of complex and noisy binary trees

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Binary tree structures are prevalent multiple across fields such as procedural modelling, genomics, and image processing. Hidden Markov models (HMMs) provide compact and interpretable representations for these complex and fractal structures. However, current de-facto inference methods involve complex iterations over all sub-trees, implementations that are domain-specific and lack a unified open-source solution. This study explores a novel `paths-of-bifurcations' inference approach to fit hidden Markov parameters on binary trees, compatible with the use of popular modelling packages. Key contributions include: (1) demonstration of procedural modelling for creating a sandbox of synthetic trees for experimentation;  (2) comprehensive performance evaluations of our inference procedure on synthetic benchmark trees addressing various challenges: heterogeneity of branch emission distributions, low probability states, small data regimes and noisy observational data; and (3) a practical application to a medical image dataset. The latter showcases the method's ability to reveal insights into branching rules governing the human airway system, with potential implications in disease characterization, airflow analysis, and particle deposition studies. This research provides a step toward robust, scalable and user-friendly generative modelling of binary tree structures with broad interdisciplinary implications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
My sincere apologies, I posted the review of a different paper.

This paper is about HMMs on trees, and not about mutual information estimation. The authors use a variational technique to relax the problem, and introduce a parametric for states/transitions, making use of Categorical/Dirichlet and Gaussian/Inverse Gamma conjugacy.}

Updates: increased soundness score. Decreased presentation and contribution. The more I reread it the more I understand it to be simple if elegant modelling, which may not be appreciated by this community since, as a whole, ICLR is not a human biology conference.

### Strengths
-The authors address a interesting problem of expanding/branching HMMs.  
-They use a standard solution to this problem.

### Weaknesses
 * While I agree in spirit with the mathematical technique, I think section 2.3 needs work in clarifying notation (perhaps a block diagram?), and has possible errors due to its compression into a single page of 2 equations. Specifically, the relationship between the observed branching angles and the latent states is not clearly defined, and the use of a single equation to represent both the joint distribution and the objective function is confusing. The notation for the transition probabilities and emission distributions needs to be more explicit, and it's unclear how the variational parameters are introduced and optimized.
* It is not clear that air pathways actually have these complex state transitions? Could they instead be modeled using the (constant) branching process? Why are there hidden states, instead of constant branching factors or branching factors that are a function of depth? Basically, do the physical branching angles, rate of branching, etc., actually change? The justification for using a hidden Markov model over simpler models is not strong enough, and the authors need to provide more evidence that the hidden states capture meaningful variations in the branching process, rather than just adding complexity. The connection between the model and the underlying biological process is weak.
* CT has imaging resolution on the order of mm (1mm isotropic is a very high quality human CT, multi-mm thick slice or gapped slices are standard clinical CT resolution). Do we expect the actual alveolar trees to be visible? If not, would these resolutions lead to non-tree like observations? (i.e., multi-compartment mergers) The authors need to address the limitations of the imaging resolution and how it affects the validity of the tree structure assumption. It is not clear if the model is robust to the potential artifacts introduced by the imaging process, such as partial volume effects or branch mergers.

### Questions
1) I'm fairly certain the ELBO should be a lower bound. Why can we have the log inside of the integral/summand in equation (1) without an inequality? Usually the latent variables are introduced at this stage, then either the spectral gap is derived, or Jensen's inequality used.  
2) One motivating factor for this work is rule heterogeneity. However, is this actually possible using these priors? I think this is what your experiments are trying to show in 3.2; I encourage the authors to work on this. Branching processes with differing rules based on interesting conditions can be very interesting in applied fields, but Figures 4 and 5 are incredibly small and unreadable, as are table 1 and 2, but even more importantly, the authors should use the synthetic data to prove that if such a rule shift (so, a regime change between lung tissue structures) existed, it could be learned by this HMM, and wouldn't have been learned by the fixed branching process.  

Additional notes: If the authors are set on using lung tissue, I feel a medical applied conference (MICCAI, MIDL, etc.) may be better suited for this type of contribution. While the HMM is interesting, its need within the application domain will not be appreciated by this community as much as a more medically inclined community.

### Soundness
3 good

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presentes a HMM approach to modeling binary trees. Approximate inference is performed using SVI in Pyro. The method is demonstrated on a broad array of synthetic data examples as well as a real human airways dataset.

### Strengths
The proposed method is fairly simple, and builds on a well known methodology.

Studies on simulated data help to illustrate the strenghts and limitations of the approach.

Simple and effective models for tree structured data seem to be important for gaining statistical insights into important biological structures.

### Weaknesses
There is no direct comparison with other competing approaches or baselines.

The technical novelty is limited.

The method could be more clearly described in the main paper, and variables/distributions could be more clearly defined.

### Questions
"Fast and scalable inference of a generative process governing such tree-structures is key for clas-
sifying trees into categories." Are generative process modeling the prevalent approach to classification, or are there other (discriminative) approaches?

"...  and split trees into ‘independent’ paths of bifurcations ..." why is independent in quotations?

Would it be possible in the introduction to set up a more clear problem formulation so that is evident which types of data problem the paper addresses? For example, it is not clear whether the trees that are modelled have a graph-based or geometric representation, such as 3d coordinat-based or anatomical mesh representation.

If I understand correctly, emission probabilities for branching angles and roll are Gaussian. Is anything done to ensure that the first angle "is the smallest angle by definition" and that angles are within a suitable range?

Would it be possible to provide some more details (possibly in the supplement) regarding the definitions of each term in the joint distribution (Eq. 1), such as a list with clear definitions of all variables and distributions.

Which variational distributions ('guide' in Pyro terminology) are used, and how important/sensitive is the choice?

Have any other methods been used to model e.g. the human airways data? How does the proposed method perform in comparison?

What would be the primary application of the proposed method?

Minor issues: 
There are a few typos etc. Examples from abstract and introduction:
"...prevalent multiple across fields..." ?
Closing parenthesis doubled "))" in a few citations.
"... and infer states..." should be 'and infers states'
"... human airway trees segmented on CT images." unclear

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores a so-called paths-of-bifurcations approach to modelling tree structures with Hidden Markov Models (HMMs). Treating each bifurcation as a node and path from root to leaf in the tree as a sequences of nodes on path to be modelled by the HMM. The approach is evaluated in its ability to infer properties of synthetic trees generated using a procedural modelling approach developed for the purpose as well as human airway trees extracted from a public medical dataset.

### Strengths
- Generative modelling of tree structures is an important problem and is relevant.

- Novelty appear to be reasonably clearly described, and described as contributions covering the paths-of-bifurcations approach, which is an original idea as far as I know, a procedural approach to synthetic tree generation, and the practical application to human airway trees.

- Language, grammar and structure is of high quality.

- The path-of-bifurcations concept is an interesting approach to modelling tree structures with HMM sequential modelling and appears to be novel.

- Code appears to be available, which should make the results easier to reproduce.

### Weaknesses
 - I found the manuscript to be a relatively hard read. Methodological and implementation details are often not explained or reasoned about and there are many of them, moreover, figures and tables are too full of details. I would suggest this is a presentation problem, not all numbers and methodological details are equally important, and I feel like the authors could have made more of an effort in summarizing and selecting the important aspects. I believe this could make the work more interesting.

- Almost all tables and figures are not readable except in very enlarged versions. Could they perhaps be changed and/or resized to be readable at reasonable magnification/print size?

### Questions
- Could some intuition or reasoning be provided for the specific employed priors and emission distributions?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
