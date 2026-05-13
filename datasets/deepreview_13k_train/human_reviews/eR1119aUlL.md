# Dynamical modeling for real-time inference of nonlinear latent factors in multiscale neural activity

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
Continuous real-time decoding of target variables from time-series data is needed for many applications across various domains including neuroscience. Further, these variables can be encoded across multiple time-series modalities such as discrete spiking activity and continuous field potentials that can have different timescales (i.e., sampling rates) and different probabilistic distributions, or can even be missing at some time-steps.  Existing nonlinear models of multimodal neural activity do not support real-time decoding and do not address the different timescales or missing samples across modalities. Here, we develop a learning framework that can nonlinearly aggregate information across multiple time-series modalities with such distinct characteristics, while also enabling real-time decoding. This framework consists of 1) a multiscale encoder that nonlinearly fuses information after learning within-modality dynamics to handle different timescales and missing samples,  2) a multiscale dynamical backbone that extracts multimodal temporal dynamics and enables real-time decoding, and 3) modality-specific decoders to account for different probabilistic distributions across modalities. We further introduce smoothness regularization objectives on the learned dynamics to better decode smooth target variables such as behavioral variables and employ a dropout technique to increase the robustness for missing samples. We show that our model can aggregate information across modalities to improve target variable decoding in simulations and in a real multiscale brain dataset. Further, our method outperforms prior linear and nonlinear multimodal models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents MRINE, a nonlinear dynamical modeling framework for multiscale neural activity that enables real-time information aggregation across modalities with different timescales and/or missing samples. MRINE consists of a multiscale encoder that fuses modalities after learning within-modality dynamics, a multiscale dynamical backbone for extracting multimodal temporal dynamics and enabling real-time decoding, and modality-specific decoders to account for different probabilistic distributions. The authors also introduce smoothness regularization objectives and a time-dropout technique to improve robustness to missing samples. Through simulations and application to a real multiscale brain dataset, MRINE is shown to outperform prior linear and nonlinear multimodal models in fusing information across modalities to improve decoding, even with different timescales or missing samples, making it valuable for real-time neurotechnology applications.

### Strengths
- Modeling neural dynamics across varying modalities.
- The ability to handle different timescales and missing samples.
- Enabling real-time decoding.

### Weaknesses
 - My main concern is that it’s difficult to find significant scientific insights in this work. It feels more like a combination of various features to achieve an improvement in behavioral decoding accuracy over the baselines, yet the 61% accuracy does not seem particularly high. In other words, the improvement in decoding accuracy alone doesn’t convincingly justify the introduction of different timescales and handling of missing samples, as I think baseline accuracy could potentially be enhanced through additional parameters or optimized training settings, such as changing the factor dimension in LFADS.

 - The choice of using only 20 spike and LFP channels is not well-justified. While the authors mention multimodality, limiting the input to 20 channels per modality seems arbitrary and potentially restricts the model's ability to capture the full complexity of the neural data. It is unclear if this choice was made due to computational constraints or other limitations, and it raises concerns about the generalizability of the findings to datasets with higher channel counts. The impact of this limited input dimensionality on the model's performance should be further explored and justified.



### Questions
- Why were only 20 spike and LFP channels used? This seems like a small number. Does this mean the input feature dimension of the data is 20+20=40?
- Is it possible to compare the accuracy of baselines with missing samples in Section 3.3?

### Soundness
3

### Presentation
2

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
Summary: The paper presents a model named MRINE, which is designed to infer latent factors from multi-scale neural data in real time. The contribution of this model is claimed to generalize the latent variable models to multi-timescales, multi-probabilistic distributions, and allow missing samples across modalities. The model can work on discrete Poisson spiking activity and Gaussian local field potentials (LFPs). The evaluation is worked on simulated and real-world neural datasets, which show performance gain in subject behavior decoding and latent dynamics reconstruction.

### Strengths
1. MRINE's key components include a multiscale encoder for fusing modality-specific dynamics, a multiscale dynamical system backbone, and modality-specific decoders. 
2. The writing and presentation of the paper is fairly good and easy for the readers to follow.
3. It's quite interesting for combing and aggregating the infromation from various modalites in neuroscience.

### Weaknesses
1. While I am inclined to hold the point that the quesiton/task this paper is focusing on has less scientific meaning, for model generalizaiton and for dealing with abnormal/missing data points.
2. From the modeling and ML perspective, the components in this MRINE's framework seems to be a combination of several existing techniques and empirical regularizers.

### Questions
1. What properties do the Poisson observations and Gaussian observations have in common?
2. A have no more questions, other concerns please refer to the Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose MRINE,  a dynamical modeling method that nonlinearly aggregates information across multiple modalities with different distributions and distinct timescales,  and missing samples. In addition, it can support inference in real time. The authors apply MRINE to two datasets, one synthetic (stochastic Lorenz attractor simulations) and one publicly available neuroscience dataset (NHP dataset).

### Strengths
1) Possible real world applications: Possibility of real time inference support is a great addition to many other multimodal models in neuroscience. This could possibly have positive applications to brain-computer interface research.
2) Robustness: The ability of the model to account for differing sampling rates and missing data is potentially impactful as much neuroscientific data is far from perfect, so models that take this into consideration are useful for real life applications.
3) The presentation is clear.

### Weaknesses
- **Poor coverage of the literature**: Despite the discussion of the literature in the paper and comparisons to different models, I find the coverage of the literature to be at a very surface level. There was much work that was not cited in the paper that should be included to accurately show the status of the field now.  For example [2,3] are multi-modal models and [1] despite not being multimodal can handle missing data. As it is now, the paper doesn’t do justice to all the other models that can handle multi-modal data and thus draws an inaccurate/incomplete picture of multi-modal work in neuroscience. To improve this, I suggest incorporating the citations below to the ‘Multimodal Models in Neuroscience’ section in the paper as well as the introduction.
- **Comparisons**: Despite comparing the model to several different ones, I am not sure why it was not compared to some of the novel multimodal neuroscience models [2,3]. I understand there are already 5 comparisons but adding a comparison with more current models like the ones previously stated can be more refreshing, and useful,  and show how MRINE compares to more current models. 
- **Limited experiments**: The application of the model was limited, I wanted a demonstration with at least 1 more real experimental data to really make the model stand out and show its utility. Without validation on multiple real-world neuroscience datasets, it is challenging to assess whether MRINE’s claims generalize across different settings.

### Questions
1. Did you try to apply the model into more complex datasets where the behavior was not just 2d reaches? I understand this might be the standard kind of experimentation in BCI but I would be interested to learn about the behavioral decoding ability of MRINE with images or videos. In other words, how does MRINE handle high dimensional datasets?
2. How does the multiscale encoder in MRINE handle differences in noise characteristics between spike and LFP modalities + what impact does this have on the overall performance of behavior decoding?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper, "MRINE: A Novel Framework for Real-Time Decoding of Target Variables from Multiscale Neural Time-Series Data," presents a new approach aimed at addressing multimodal neural data processing challenges. While the proposed framework could contribute to advancements in real-time decoding, several critical issues and areas for improvement weaken the paper's rigor, interpretability, and reproducibility.

### Strengths
The efforts to handle missing data with techniques like smoothness regularization and time-dropout are noteworthy additions to the model.

### Weaknesses
-(Lines 64-65): The claim that no existing models address multimodal neural data is inaccurate. Recent works, including those by Rezaei et al. [1] and Coleman et al. [2], have tackled similar challenges.
- (Lines 78-80): The assertion that other models do not address different timescales and missing samples in multimodal data is also incorrect. Models like those by García et al. [3] incorporate stochasticity in dynamical systems, relevant to noise handling in neural data.

-The paper lacks citations and comparisons to relevant models, particularly dynamical VAEs, which bear strong conceptual similarities to MRINE. This oversight diminishes the theoretical foundation of the paper and obscures recent advancements in variational autoencoders (VAEs) applied to dynamical systems.

-The equations in Section 2.1 contain inaccuracies, particularly in the notation used to describe multiscale dynamics. For instance, a single time index t is used, with no discussion on how different time horizons are managed, which undermines clarity regarding multiscale capabilities.

- (Equation 8): The absence of a derivation for the loss function weakens the rigor of the methodology section. Without a clear mathematical path to this objective function, readers are left without the means to evaluate or reproduce the proposed approach accurately.

-The paper lacks a comprehensive comparison with state-of-the-art models in time-series decoding, such as Mamba and S4. The selective comparison hinders the assessment of MRINE’s capabilities relative to these established baselines.

-Figure 1 does not effectively illustrate the multiscale time dynamics central to MRINE’s approach, diminishing its ability to convey the model’s core features.

-The bar plots throughout the paper lack statistical tests and error bars, raising questions about the reliability of reported performance differences. Including these would strengthen the study’s claims and clarify the significance of observed results.

-The theoretical foundation for MRINE’s multiscale capabilities is unclear, particularly in the equations defining these aspects. Some claims made in the introduction, especially those motivating the MRINE framework, appear overstated in light of prior work by Rezaei et al. [1], Coleman et al. [2], and García et al. [3].

-While these techniques are positive additions for handling missing data, they require further explanation, particularly regarding how they compare or improve upon existing methods for handling missing samples in neural data.

### Questions
-Could you clarify the novelty of MRINE relative to existing multimodal neural data models? For instance, how does it differ from models like those presented by Rezaei et al. [1] and Coleman et al. [2] that also address multimodal data processing?

- Given that MRINE bears similarities to dynamical VAEs, could you discuss how MRINE’s approach compares to these methods, particularly regarding handling multiscale dynamics?

-To provide a fuller evaluation, would you consider adding comparisons with state-of-the-art time-series decoding models like Mamba and S4?

-The equations in Section 2.1 describe MRINE’s multiscale capabilities, but the use of a single time index t leaves the handling of distinct time horizons unclear. Could you provide additional details or adjustments to the notation to clarify how the model represents multiple time scales?

-The log-likelihood calculation in Figure 3.C is not clearly explained. Could you provide a detailed description of the calculation process and how it relates to model performance?

### Soundness
3

### Presentation
3

### Contribution
2
