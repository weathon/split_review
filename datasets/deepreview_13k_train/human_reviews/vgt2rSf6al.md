# MindSimulator: Exploring Brain Concept Localization via Synthetic fMRI

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Concept-selective regions within the human cerebral cortex exhibit significant activation in response to specific visual stimuli associated with particular concepts. Precisely localizing these regions stands as a crucial long-term goal in neuroscience to grasp essential brain functions and mechanisms. Conventional experiment-driven approaches hinge on manually constructed visual stimulus collections and corresponding brain activity recordings, constraining the support and coverage of concept localization. Additionally, these stimuli often consist of concept objects in unnatural contexts and are potentially biased by subjective preferences, thus prompting concerns about the validity and generalizability of the identified regions. To address these limitations, we propose a data-driven exploration approach. By synthesizing extensive brain activity recordings, we statistically localize various concept-selective regions. Our proposed MindSimulator leverages advanced generative technologies to learn the probability distribution of brain activity conditioned on concept-oriented visual stimuli. This enables the creation of simulated brain recordings that reflect real neural response patterns. Using the synthetic recordings, we successfully localize several well-studied concept-selective regions and validate them against empirical findings, achieving promising prediction accuracy. The feasibility opens avenues for exploring novel concept-selective regions and provides prior hypotheses for future neuroscience research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new data-driven approach to localize concept-selective regions in the brain by using synthetic brain recordings generated via a probabilistic model, MindSimulator, conditioned on concept-oriented visual stimuli. This approach enhances coverage and reduces bias, achieving high prediction accuracy in localizing known concept regions.

### Strengths
1 - The authors employ a generative fMRI encoding model to synthesize individual fMRI signals corresponding to concept-oriented visual stimuli, addressing the inherent one-to-many correspondence issue between visual stimuli and fMRI recordings.

2 - The paper is well-structured, with a clear formulation of the problem and a thorough description of the proposed model's components and methodology.

3 - The authors provide extensive ablation studies that effectively validate the model architecture's contributions and showcase the performance impact of each component.

### Weaknesses
1 - Capturing both spatial and temporal dependencies within the autoencoder is essential for producing meaningful representations of brain activity, which is inherently dynamic. The current model appears to underutilize temporal information based on the description in Supplementary Material Section A. To address this limitation, you might consider adding recurrent layers, such as LSTMs or GRUs, or using 3D convolutions in the autoencoder to enhance temporal processing. Additionally, it would be helpful to clarify in the main text or supplementary materials if and how temporal dependencies are integrated in the current approach. This added information would improve understanding of how well the model aligns with the time-varying nature of fMRI data.

2 - It would be helpful if the authors could clarify their voxel selection and masking process, specifically how spatial relationships between neighboring voxels are preserved when creating the autoencoder input. If there is a risk of losing local spatial context, consider alternative approaches, such as using 3D convolutions or patch-based inputs, which may mitigate this issue and maintain spatial continuity within the masked regions. The current approach of flattening the masked 3D fMRI data into a 1D vector may discard crucial spatial relationships between voxels, which are known to be important for representing distributed neural activity patterns.

3 - To improve the evaluation of your results, please include comparisons with specific, relevant works. For example, you may consider applying a connectivity-based parcellation approach (ref are given below) to both the original and synthetic data to examine whether similar visual networks emerge in each case. Including these comparisons would help readers to contextualize the reported metrics and enable a clearer understanding of your model's relative performance and its contributions to the field.

4 - To aid in assessing scalability, please provide details on the computational complexity of the model, including training time, memory usage, and the hardware specifications used in your experiments. These details would offer valuable insight into the practical feasibility of implementing your approach in various research or clinical settings.

### Questions
1 - Given the brain’s dynamic complexity and somewhat chaotic behavior, generative models offer both benefits and limitations in modeling brain function. Could the authors evaluate the similarity in temporal and spatial gradients between the original and synthetic data to better assess these dynamics?

2 - Additionally, it would be valuable if the authors could quantify the similarity in functional connectivity maps between the original and synthetic data at each timepoint as well.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This is a paper with interesting results. However, I am uncertain whether the technique presented represents a major advancement. A key gap in the literature appears to be the investigation of cognitive processes, including the concepts discussed by the authors, not only in a spatial context but also in terms of activation trajectories over time. The authors have already addressed this point in their discussion with another reviewer. While I agree that NSD does not necessarily contribute additional insights in this context, there are datasets on movie viewing with corresponding ratings that could have been beneficial for this study.

### Strengths
-

### Weaknesses
A key gap in the literature appears to be the investigation of cognitive processes, including the concepts discussed by the authors, not only in a spatial context but also in terms of activation trajectories over time. I am not sure if the current paper provides a systematic solution.

### Questions
Nothing anymore. the authors have done a great job.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new way to implement concept-localization in the brain using a learned generative model which synthesizes fMRI responses. This is derived from the observation that fMRI responses to the same stimuli can be noisy and are better captured by sampling from a random variable instead of a learned (discriminative/static) model. A latent representation is jointly learned via CLIP in which an image embedding is paired with a voxel embedding and then trained according to the SoftCLIP loss.

The authors show reconstruction is possible via their proposed method to use synthetic fMRI, but the authors fail to show that the brain data could just as easily be ignored. Image encodings are passed into the sampler and decoders are highly able to create very realistic images but it's not clear that the modelling of the resting state inputs and learned fMRI is actually doing anything useful in a clear way as the authors make it seem (with huge swaths of cortex claimed for very restrictive conceptual categories). There are arguments for how discrete these are but once you expand the classes beyond the very limited amount presented, then quantified overlap, it would be clear that many patches are not conceptually distinct. That's my assumption. 

The idea is an interesting one, but the lack of good experimental testing against strong baselines (particularly, testing with shuffled/random fMRI data). The bulk of the promise shown here might actually be just by going between image embeddings (via the voxel encoder as it was jointly trained on image representations and not fMRI data alone).

### Strengths
The paper has a pretty good grasp on the recent literature and various approaches that have been experimented on in this area, showing a wide depth of knowledge. The analyses seem detailed and it's clear a lot of work went into some parts of the experimental analysis. There will be a pretty detailed Weaknesses section, but it's easier to point out identified weaknesses than identify lists of things done correctly. I do have a fair few issues with the way the analysis was done, but I think with some tweaks and additional analyses that are robust against better controls, better description, this paper does have potential.

### Weaknesses
 * Captions to figures are mostly vacuous and non-descriptive and need to be expanded to better describe the associated figures
* Some points are argued but are presented without evidence and for the kind of statements they are, definitely require a solid backing (see Questions section)
- Citation format is not consistent. Many citations should be in parentheticals but are not (needs to be fixed for camera-ready version)
- The language is overly flowery in a way that makes the claims nonsensical (e.g. “Fortunately, we effectively explore novel concept-selective regions, capably providing explicit hypothesis constraints…”) 
- Language needs to be checked by a person intimately familiar with the conventions of academic written English to correct some unusual and unclear phrasing (in the methods section especially)

There have been numerous recent works that have highlighted how these types of models can effectively perform the same function when replacing brain data with random noise or brain responses that aren't paired correctly with the same responses.

Huge caveat here that “**if it can be reconstructed, then the fMRI contains the information**” but you can often do reconstruction equally well from random noise, there doesn’t have to be anything real in the fMRI data. Kamitani recently showed this (https://arxiv.org/abs/2405.10078) and this paper also did (https://arxiv.org/abs/2405.06459) with EEG. 

The paper fails to take into account a number of confounds and does not seem to understand just how drastic this aspect of the analysis could be on changing the presented results. You can't present images of food and not take into account that you might be modelling shape (round plates, round food shapes) or lower-level features like colour (food is often colourful). These have been huge issues in the concept localization space using datasets like NSD but I didn't see any citations or awareness of this issue. Also, it's not likely that the concept of "surfer" or "bed" takes up anywhere near as much cortical territory as some of these plots indicate. There is high-level confounding going on here that undermines the idea of concept localization. This is why the handcrafted stimuli were carefully created in the first place, to avoid this issue. The idea of this paper seems like it goes back in the wrong direction. 

The results in Table 3 during the ablation analysis show often minimal drops when ablating important components of the paradigm, which lead me to believe that confounds and lack of good baselines are hiding shortcut learning and cheats that the model is making use of instead of it being primarily a method centred on good fMRI representations.

If you have focused on the localizers used in NSD then I think it's important you cite the (ubiquitous) paper that NSD (and many other fMRI datasets) use, namely the fact that these fLoc images come from Stigliani et al. 2015 (https://www.jneurosci.org/content/35/36/12412). 
It seems quite the oversight to not have cited this given the content of the submission, especially as you're using the images from this paper in the figures of your dataset.

### Questions
The introduction raises some claims that need supporting evidence. How do you know that the efforts to go into designing common functional localization images are insufficient and poorly generalizable? What promotes this observation? Why should a functional localiser be embedded within a naturalistic scene? Naturalistic stimuli are famously confounded across multiple dimensions and the artificial placement of a core concept in a bare background is a method to remove potential confounds. Yes, it’s undesirable because our vision is based around naturalistic scenes, but the argument for naturalistic images in functional localization is only inviting trouble. We would lose specificity and be more unlikely to be sure that we’re not detecting confounding background information and mistakenly attributing brain activity to core concepts within the images. The arguments as they’re outlined don’t naturally follow on from one another in this exposition of the paper’s contributions.

- Line 157: do you mean for the comma to be a subtraction symbol in the MSE equation?
- Why do you start the inference sampler with resting state fMRI data? What's the idea here? It's not really explained in Section 3.4.
- If an amended version is submitted, could you put the ROI boundaries on your flatmaps to better orient the distributions of voxel encodings?
- In 6.1 what's going on here? Are you using MSCOCO images or images for which there is fMRI data in NSD? It's not clear
- Also in 6.1, you mention the t-test that is done voxelwise, where are these results? What was the threshold? I don't really understand what you've done or how you have set up your test and there is also no mention of multiple comparisons correction (big red flag for me).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes "MindSimulator", a framework that synthesizes fMRI data based on visual stimuli through an fMRI autoencoder, diffusion estimator, and inference sampler. The authors first assessed the performance of the fMRI autoencoder and diffusion estimator using various metrics, demonstrating their capability to generate high-quality fMRI data. They then used the synthesized fMRI data to explore correlations between manually selected images and brain activity, offering new insights for neuroscience research.

### Strengths
1. The paper offers a novel perspective by applying well-established fMRI visual decoding models for fMRI signal synthesis, with thorough validation to demonstrate reliability.
2. This study introduces a new tool for exploring *concept-selective regions*, significantly enhancing the flexibility of investigating how specific human visual representations of concepts are spatially distributed in the brain.

### Weaknesses
1. The algorithm for localizing concept-selective regions may lack sufficient validation, as the paper only compares this approach to fLoc, without further support from neuroscience literature. Consideration of alternative methods, like Neurosynth or Text2Brain, could strengthen the results, as these methods allow a broader selection of concepts correlated with brain activity, potentially detecting concepts not covered by fLoc. 

2. In the *Evaluation Metrics* section, the method of validating generated fMRI data based on the quality of generated images may not be reliable due to its reliance on a separate trained decoding model. Given the complexity of visual decoding from fMRI, this dependence could reduce the robustness of the evaluation. Exploring alternative evaluation methods, such as comparing generated data with latent representations in the voxel encoder’s latent space, might provide more direct validation.

### Questions
1. In the *Inference Sampler* section, the mention of "resting-state brain activity fMRI" could be misleading, suggesting that the model can generate resting-state fMRI data. However, I could not find evidence of any relevant dataset being used. Could the authors clarify this point?
2. In the *Out-of-Distribution Generalization* section, CIFAR-10/100 was used, and metrics were calculated based on images decoded from synthesized fMRI data. As noted in the weaknesses, this approach may introduce bias. Why not use an image-fMRI dataset, like THING-fMRI, to compute metrics directly on fMRI data?

### Soundness
2

### Presentation
3

### Contribution
3
