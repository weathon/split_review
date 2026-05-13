# Learning and aligning single-neuron invariance manifolds in visual cortex

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Understanding how sensory neurons exhibit selectivity to certain features and invariance to others is central to uncovering the computational principles underlying robustness and generalization in visual perception. Most existing methods for characterizing selectivity and invariance identify single or finite discrete sets of stimuli. Since these are only isolated measurements from an underlying continuous manifold, characterizing invariance properties accurately and comparing them across neurons with varying receptive field size, position, and orientation, becomes challenging. Consequently, a systematic analysis of invariance types at the population level remains under-explored. Building on recent advances in learning continuous invariance manifolds, we introduce a novel method to accurately identify and align invariance manifolds of visual sensory neurons, overcoming these challenges. Our approach first learns the continuous  invariance manifold of stimuli that maximally excite a neuron modeled by a response-predicting deep neural network. It then learns an affine transformation on the pixel coordinates such that the same manifold activates another neuron as strongly as possible, effectively aligning their invariance manifolds spatially. This alignment provides a principled way to quantify and compare neuronal invariances irrespective of receptive field differences. Using simulated neurons, we demonstrate that our method accurately learns and aligns known invariance manifolds, robustly identifying functional clusters. When applied to macaque V1 neurons, it reveals functional clusters of neurons, including simple and complex cells. Overall, our method enables systematic, quantitative exploration of the neural invariance landscape, to gain new insights into the functional properties of visual sensory neurons.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper adapts and builds on work that optimizes for an “invariance manifold” of maximally exciting inputs to neurons. The authors introduce an affine transformation that can be applied to learn a minimal similarity between one neuron’s invariance manifold and another’s. They show that this allows efficient clustering of neuron properties in simulations of macaque V1 responses and in neural predictions obtained from “digital twin” models of macaque V1 responses.

### Strengths
Overall, the idea behind the paper seems solid. It extends previous work of capturing invariances in an interesting direction of aligning the invariances between different neural populations. The paper is also fairly easy to read and understand, apart from the sections noted below.

### Weaknesses
As currently written, the paper muddles together previous work and what is new in this paper. For instance, in the abstract (lines 14, and followed up in line 21) it is noted that previous work does not model the invariances as a “continuous manifold”, and that this paper learns the continuous invariance manifold. However, I believe that the authors are directly using a method from Baroni et al 2023, which defines a continuous manifold so this isn't actually "novel" in this work. More details about weaknesses and ways to improve the paper are covered in the section section.

The paper states that it tests the method on “biological neurons from macaque V1” (line 72). This is not true. The paper tests the method on *models* (i.e. additional simulations) trained to predict the response of V1 neurons (digital twins). There is no biological neural data in the paper to validate the method, and thus the findings may just be properties of the models and not properties of biological neurons. The wording in this section and elsewhere in the paper MUST be changed, as currently it is misleading to readers.

Using the phrase “trivial” to describe known properties of receptive field attributes like position, size, and orientation does not seem appropriate. These coding properties are thought to be *fundamental* to the organization of neurons in primary visual cortex. For the second bullet point on line 56, Perhaps the authors mean something like “The method should allow for flexibility to account for known variability of neurons, and find common structure given this variability”?  Please rephrase this bullet point as you see appropriate, and also change other locations in the paper where these properties are referred to as “trivial”.

I found the explanation of INRs (Lines 136-158) and the associated figure 1 very difficult to follow. This whole section could be improved to concretely explain what was done for this paper, instead of generally explaining INRs and differences from previous work (as the reader might not be familiar with the details of Baroni et al, so the methods should be self-contained in this paper). For instance, in Figure 1, the depiction of two neural networks is confusing, as I believe that the parameters of the response-predicting model $\theta$ are fixed, but this is not noted? Additionally, what images are used to train the INRs (is there a train/test set? I could not find details of this, or how these images were chosen for the two sets of experiments, in the main text or the supplement). It is also unclear how the modifications allow direct control of the spatial frequency (line 157), and if this is critical it should be better explained. These are some examples, but I would encourage the authors to generally revise this methods section and add appropriate details to the supplement so that the setup is clear to the readers.

How are the parameters for the contrastive objective for “near” and “distant” points determined, and are different results obtained when using a different range for near and distant points? Additionally, it is stated that the formulation encourages a smooth and diverse learned manifold (218-219). It would be good if this was quantified, for instance by showing lines for real points like that in Figure 1 bottom right, to show that there are no jumps etc. when varying the latent parameters.

In section 4.1, a few more details about the model neurons should be provided in the main text so that readers understand the simulations. Additionally, another sentence in the main text describing how the manifold alignment is measured (the right bars on the plots in Figure 2E,F & Fig 3 C) would be good to help  the reader understand the difference between the measured “Activation” and “Manifold” similarity.

How does this method hold up in the case of the underlying invariance manifold not being continuous in pixel space? For instance, take the simple example of $y=\texttt{min}(x^2, 1)$. Two points at +/-1 have the same y output (which is the maximum value) but they are not connected. In this sense, there are two discrete invariance manifolds of the maximum responses. I’m not sure how a  case like this would fit into the proposed framework, and so more detail about why a continuous manifold is a reasonable assumption (or at least acknowledging limitations of it) would strengthen the paper.

In terms of invariances, the work by Feather et al. (Neurips 2019, and Nature Neuro 2023) come to mind. However, this work found that deep neural networks often have idiosyncratic invariances that are not shared across different models (and they also did not attempt to characterize the full manifold of invariances—they just draw samples from it). Do the authors add in regularization priors (such as smoothness etc) to the initial MEI generation to promote more smooth and interpretable MEIs, which could encourage them to be more shared across the different models? Or is there something about the fact that the models used are an ensemble of CNNs, rather than a single one, discouraging idiosyncrasies? It also might be worth mentioning this previous work on invariances in the related work section.

Can some of the “affine transformations” for similarity of the manifolds be cast as a different similarity metric applied to the representations? The work by Williams et al. (NeurIPS 2021) on generalized shape metrics comes to mind. https://arxiv.org/pdf/2110.14739

Typos and other minor suggestions:
* Line 53:  “and identifying” is the wrong tense (does not match “compare”) – it should be “and identify”
* As currently written, the related work section is difficult to understand. It might be worth revisiting this section to unpack some of the jargon. Alternatively, some authors put the related work towards the end near the discussion, which in this case might help the reader understand why each of these points matters for the paper (for me, I had to return to this section after reading the rest of the paper to really understand what was going on).
* In Figure 1 bottom right panel, is this real data from one of the experiments or is it just a fake-data visualization? This should be noted.
* How is noise taken into account for the neural data?  
* Lines 269-272: I believe wording in this section is too strong – the Gabor pattern of the simple cell will not always maximize the activity of a complex cell? Maybe rephrase, or more concretely explain what is meant.
* Line 429 – are there really “no invariances” in the Gabor patterns in Figure 3A? It seems a little strong to say this, as there are slight pixel changes.

### Questions
A few easy-to-address concerns would move this paper into a clear acceptance for me: 
1) The paper states that it tests the method on “biological neurons from macaque V1” (line 72). This is not true. The paper tests the method on *models* (i.e. additional simulations) trained to predict the response of V1 neurons (digital twins). There is no biological neural data in the paper to validate the method, and thus the findings may just be properties of the models and not properties of biological neurons. The wording in this section and elsewhere in the paper MUST be changed, as currently it is misleading to readers. 
2)	Using the phrase “trivial” to describe known properties of receptive field attributes like position, size, and orientation does not seem appropriate. These coding properties are thought to be *fundamental* to the organization of neurons in primary visual cortex. For the second bullet point on line 56, Perhaps the authors mean something like “The method should allow for flexibility to account for known variability of neurons, and find common structure given this variability”?  Please rephrase this bullet point as you see appropriate, and also change other locations in the paper where these properties are referred to as “trivial”. 
3)	I found the explanation of INRs (Lines 136-158) and the associated figure 1 very difficult to follow. This whole section could be improved to concretely explain what was done for this paper, instead of generally explaining INRs and differences from previous work (as the reader might not be familiar with the details of Baroni et al, so the methods should be self-contained in this paper). For instance, in Figure 1, the depiction of two neural networks is confusing, as I believe that the parameters of the response-predicting model $\theta$ are fixed, but this is not noted? Additionally, what images are used to train the INRs (is there a train/test set? I could not find details of this, or how these images were chosen for the two sets of experiments, in the main text or the supplement). It is also unclear how the modifications allow direct control of the spatial frequency (line 157), and if this is critical it should be better explained. These are some examples, but I would encourage the authors to generally revise this methods section and add appropriate details to the supplement so that the setup is clear to the readers. 
4)	How are the parameters for the contrastive objective for “near” and “distant” points determined, and are different results obtained when using a different range for near and distant points? Additionally, it is stated that the formulation encourages a smooth and diverse learned manifold (218-219). It would be good if this was quantified, for instance by showing lines for real points like that in Figure 1 bottom right, to show that there are no jumps etc. when varying the latent parameters. 
5)	In section 4.1, a few more details about the model neurons should be provided in the main text so that readers understand the simulations. Additionally, another sentence in the main text describing how the manifold alignment is measured (the right bars on the plots in Figure 2E,F & Fig 3 C) would be good to help  the reader understand the difference between the measured “Activation” and “Manifold” similarity. 

I also had a few more general questions about the work: 

6) How does this method hold up in the case of the underlying invariance manifold not being continuous in pixel space? For instance, take the simple example of $y=\texttt{min}(x^2, 1)$. Two points at +/-1 have the same y output (which is the maximum value) but they are not connected. In this sense, there are two discrete invariance manifolds of the maximum responses. I’m not sure how a  case like this would fit into the proposed framework, and so more detail about why a continuous manifold is a reasonable assumption (or at least acknowledging limitations of it) would strengthen the paper.  
7) In terms of invariances, the work by Feather et al. (Neurips 2019, and Nature Neuro 2023) come to mind. However, this work found that deep neural networks often have idiosyncratic invariances that are not shared across different models (and they also did not attempt to characterize the full manifold of invariances—they just draw samples from it). Do the authors add in regularization priors (such as smoothness etc) to the initial MEI generation to promote more smooth and interpretable MEIs, which could encourage them to be more shared across the different models? Or is there something about the fact that the models used are an ensemble of CNNs, rather than a single one, discouraging idiosyncrasies? It also might be worth mentioning this previous work on invariances in the related work section. 
8) Can some of the “affine transformations” for similarity of the manifolds be cast as a different similarity metric applied to the representations? The work by Williams et al. (NeurIPS 2021) on generalized shape metrics comes to mind. https://arxiv.org/pdf/2110.14739 

Typos and other minor suggestions: 
* Line 53:  “and identifying” is the wrong tense (does not match “compare”) – it should be “and identify” 
* As currently written, the related work section is difficult to understand. It might be worth revisiting this section to unpack some of the jargon. Alternatively, some authors put the related work towards the end near the discussion, which in this case might help the reader understand why each of these points matters for the paper (for me, I had to return to this section after reading the rest of the paper to really understand what was going on).  
* In Figure 1 bottom right panel, is this real data from one of the experiments or is it just a fake-data visualization? This should be noted. 
* How is noise taken into account for the neural data?  
* Lines 269-272: I believe wording in this section is too strong – the Gabor pattern of the simple cell will not always maximize the activity of a complex cell? Maybe rephrase, or more concretely explain what is meant. 
* Line 429 – are there really “no invariances” in the Gabor patterns in Figure 3A? It seems a little strong to say this, as there are slight pixel changes.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors developed a method to learn the invariant manifold of a visual neuron / encoding model of a visual neuron. Specifically, they used implicit neural representation to parametrize images and uses a circular variable to condition the image parametrization, creating a 1d circular submanifold. Then they optimized the image parametrization via activation maximization and contrastive loss to find the invariance manifold for a given neuron. Additional template matching step through fitting affine transforms allowed the method to account for difference in receptive field size location / rotation allowing for comparison on the population level. They validated the method on synthetic neuronal data and applied it to real neuronal data from monkey V1, finding clustering across neurons.

### Strengths
- The problem of characterizing neuronal invariances systematically in a modern way is important and under-explored.
- The method is well presented and principled, and innovative in combining INR, contrastive learning, affine fitting in an elegant way. Similar ideas can potentially impact many other fields.
- Overall, the presentation of the results are stunning and visually pleasing. Kudos on your efforts for making these.
- The method is very thoroughly evaluated on synthetic and real neural data, including consistency across noise seed, robustness across encoding models etc.

### Weaknesses
 - Intuitively and empirically, the closer to the MEI / peak, the “smaller” the invariant manifold [1]. One weakness is the proposed objective is that it didn’t explicitly allow setting a “target level” of $\alpha_i/\alpha_{MEI}$ but seek to optimize the activation value (→ 1). This could result in the invariant manifold being too close to the MEI and not having enough variability, which seems to me be the case from Fig. 2. 
A potential simple improvement will be to allow a target level to be set like having $|\alpha_i/\alpha_{MEI}-\lambda|$ in the objective. c.f. Eq.2 in [1].

[1]: Wang, Ponce, On the Level Sets and Invariance of Neural Tuning Landscapes, 2022, PMLR, https://arxiv.org/pdf/2212.13285

 - One related line of work in this domain the authors seem to miss to compare / discuss is [1, 2]. There the authors used deep generative models $G:z→I$ to parametrize natural images. After finding the activation maximizing latent $z^*$, they sampled images from a 2d submanifold around $z^*$ from the latent space of $z$, and directly find the 1d invariance / iso-response manifold (S1) from this 2d slice. They also measured this invariance manifold on various target levels, where the authors seem to miss. 
So it seems like a comparable method to find invariance transformations for image computable neuron model, that is also highly activating. 
Though targeting slightly different questions, their work seems related and worth mentioning.

[2]: Wang, Ponce, Tuning landscapes of the ventral stream, 2022, Cell Rep.

- Intuitively, the contrastive loss seems a little redundant, do we really need the numerator positive pair part? e.g. it feels like purely by the smoothness of image parametrization, the near by latent should give rise to the similar images. We just need to make distant latent to give distant images. 
( Is it there for numerical stability purpose? )
- Necessity of “Invariance alignment matrix”
For Fig 2CD and 3B, alignment of invariant manifolds, how much of it comes from the similarity of the MEI themselves (applying the fitted affine transformed), how much comes from the invariance manifold? 
It seems the images from invariant manifold are all “variation on a theme”, i.e. all pretty close to the MEI, so I think MEI will give rise to similar plots as Fig2C,Fig3B. Can you compare the matrix for MEI and the matrix for invariance manifold? 
Given so what’s the additional information in the “alignment of invariance manifold”?
- The method is amazing, but what else can the proposed method contribute to visual neuroscience beyond defining cell type clusters?
- In the end, the proposed method can only find 1 dim invariance manifold. Though we know the neurons can be invariant to much higher dim inv manifold (could be as high as d-1 dim, where d is stimuli dim). 
Can this method be used to figure out the true dimensionality of that manifold?

### Questions
- One related line of work in this domain the authors seem to miss to compare / discuss is [1, 2]. There the authors used deep generative models $G:z→I$ to parametrize natural images. After finding the activation maximizing latent $z^*$, they sampled images from a 2d submanifold around $z^*$ from the latent space of $z$, and directly find the 1d invariance / iso-response manifold (S1) from this 2d slice. They also measured this invariance manifold on various target levels, where the authors seem to miss. 
So it seems like a comparable method to find invariance transformations for image computable neuron model, that is also highly activating. 
Though targeting slightly different questions, their work seems related and worth mentioning.

[2]: Wang, Ponce, Tuning landscapes of the ventral stream, 2022, Cell Rep.

- Intuitively, the contrastive loss seems a little redundant, do we really need the numerator positive pair part? e.g. it feels like purely by the smoothness of image parametrization, the near by latent should give rise to the similar images. We just need to make distant latent to give distant images. 
( Is it there for numerical stability purpose? )
- Necessity of “Invariance alignment matrix”
For Fig 2CD and 3B, alignment of invariant manifolds, how much of it comes from the similarity of the MEI themselves (applying the fitted affine transformed), how much comes from the invariance manifold? 
It seems the images from invariant manifold are all “variation on a theme”, i.e. all pretty close to the MEI, so I think MEI will give rise to similar plots as Fig2C,Fig3B. Can you compare the matrix for MEI and the matrix for invariance manifold? 
Given so what’s the additional information in the “alignment of invariance manifold”?
- The method is amazing, but what else can the proposed method contribute to visual neuroscience beyond defining cell type clusters?
- In the end, the proposed method can only find 1 dim invariance manifold. Though we know the neurons can be invariant to much higher dim inv manifold (could be as high as d-1 dim, where d is stimuli dim). 
Can this method be used to figure out the true dimensionality of that manifold?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a method for categorizing the receptive fields of visual neurons into classes that are invariant to affine transformations. For a given neuron (referred to as the template neuron), they first employ a previously developed method (Baroni et al. 2023) to identify a one-dimensional manifold of images that maximize the response of the neuron (referred to as the template manifold). Then, given another neuron (referred to as target neuron), they identify an affine transformation of the template manifold that maximizes the response of the target neuron. If the transformed template manifold produces strong responses in the target neuron (and the converse holds), then the template neuron and target neuron are identified as belonging to the same "class". They apply their method to synthetic neurons and biological neurons to identify classes of neurons with receptive fields that are "equivalent" up to affine transformation.

### Strengths
Overall I enjoyed reading this paper. It provides a systematic method for classifying neurons by their receptive fields. As the authors show, the method captures previously identified receptive fields in V1 (simple cells and complex cells) can be used to identify and characterize previously unidentified receptive fields in V1. The general procedure seems promising.

### Weaknesses
As someone who is not familiar with these types of work, it took me some time to appreciate what this paper is doing. For example, the authors state early on that they are seeking a method that "should allow for a meaningful measure of similarity between two invariance manifolds". I had no idea what this meant when I first read it. There was no mention of what this "invariance manifold" is prior to that statement (it's mentioned in the abstract, but not the introduction). I think that slowly walking through an example (maybe with a figure) with simple cells would be helpful.

A few other comments: While invariance to affine transformation seems reasonable in V1, it's not clear how one would want to define invariance in high-order visual areas, though I don't see this as an issue that needs to be addressed in this work.

This paper relies on existing methods which are only briefly explained. (I'm not familiar with these works, hence my low confidence score.)

### Questions
- How are $\mathcal{Z}_+$ and $\mathcal{Z}_-$ defined? It seems like this could have a significant effect on the learned manifold of stimuli.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a new method to map invariance manifolds of visual neurons. They combine prior methods to arrive at a new formulation that allows for continuous deformations of MEIs and clustering that marginalizes over affine spatial transformation. They validate their method on simulations and test it on Macaque V1 data.

### Strengths
The paper is well written, cites relevant prior literature and does a good job working through the logic and experiments. Figure 1 is very illustrative and of high quality. The result figures are also very clean and show convincing results. I like the focus on continuous transformations, allowed by implicit representations, rather than pointwise estimates such as Cadena et al. 2018.

The 'new cell types' on V1 data are exciting, looking forward to closed loop validation.

### Weaknesses
It would be instructive to discuss the concept of a nullspace, as being the input space that the neural response is invariant to. One can think of an MEI as a first order approximation to the response function. Thus, for such a linear function it is quite natural to think about its nullspace aka the invariance manifold. This actually leads to a question: there seems to be a way to game the objective function. One could simply keep the MEI in the RF identical while making large changes outside the RF (for instance, strongly changing backgrounds); How is this avoided?

108: The method in Klindt et al. 2017 performance functional clustering that is invariant to RF position; The method in Ustyuzhaninov et al. 2019 extends this to clustering that is also invariant to orientation; Arguably, the main difference that the affine transformations in this paper add on top of those prior methods are: scaling, shearing and reflections of MEIs

Invariance is a broader concept than just invariance around the MEI. One can have iso-response input manifolds showing different invariances at every activation level of the neuron. Please add this distinction and explain why you only study invariance at the MEI.

It would be great to add comparisons to prior methods. For instance, your method should be able to solve the functional clustering despite RF shifts like in Klindt et al. 2017; It should also be able to solve the functional clustering despite RF shifts and rotations like in Ustyuzhaninov et al. 2019. I am happy to raise my score if you can add those comparisons.

117-119: please clarify

Why do you use a periodic 1D latent variable? Please justify and explain

152: why remove batchnorm?

153: steps = typo?

155: Are the Fourier features new compared to Baroni? They are pretty standard in Sirens / implicit function modelling. Why do they allow better controlling spatial frequency etc., do you have data to support this?

Why did you choose cosine similarity as image metric? Might this have shortcomings?

253: neuron + s

Why don't you use the activation matrix directly as a similarity matrix input to agglomerative clustering, why first compute the cos.sim. between rows? [more data massaging -> more skeptical]

### Questions
117-119: please clarify

Why do you use a periodic 1D latent variable? Please justify and explain

152: why remove batchnorm?

153: steps = typo?

155: Are the Fourier features new compared to Baroni? They are pretty standard in Sirens / implicit function modelling. Why do they allow better controlling spatial frequency etc., do you have data to support this?

Why did you choose cosine similarity as image metric? Might this have shortcomings?

253: neuron + s

Why don't you use the activation matrix directly as a similarity matrix input to agglomerative clustering, why first compute the cos.sim. between rows? [more data massaging -> more skeptical]

### Soundness
4

### Presentation
4

### Contribution
3
