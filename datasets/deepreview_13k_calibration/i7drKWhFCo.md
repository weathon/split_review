# Disentangling 3D Animal Pose Dynamics with Scrubbed Conditional Latent Variables

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Methods for tracking lab animal movements in unconstrained environments have become increasingly common and powerful tools for neuroscience. The prevailing hypothesis is that animal behavior in these environments comprises sequences of discrete stereotyped body movements ("motifs" or "actions"). However, the same action can occur at different speeds or heading directions, and the same action may manifest slightly differently across subjects due to, for example, variation in body size. These and other forms of nuisance variability complicate attempts to quantify animal behavior in terms of discrete action sequences and draw meaningful comparisons across individual subjects. To address this, we present a framework for motion analysis that uses conditional variational autoencoders in conjunction with adversarial learning paradigms to disentangle behavioral factors. We demonstrate the utility of this approach in downstream tasks such as clustering, decodability, and motion synthesis. Further, we apply our technique to improve disease detection in a Parkinsonian mouse model.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present a framework for motion analysis that uses conditional variational autoencoders to disentangle desired behavioral variables seen in animals and to remove nuisance confounds. They augment the C-VAE loss function to reduce dependence between the VAE latent variables and the behavioral variables of interest. They explore different methods to scrub out disentanglement including linear, quadratic, cubic, MLP, and MI based approaches. They thoroughly analyze their model in a simulated setting and apply their technique to improve disease detection in a Parkinsonian mouse model.

### Strengths
The paper is very clearly written, the results are compelling and thorough, and the model addresses a need in the neuroscience community as there are increasingly common adaptations of VAE style models to behavioral data. I appreciate the overview of C-VAEs as well as their motivation and clear explanation of their scrubbing methodology. The analysis on the two real datasets demonstrate the utility of the approach and I appreciate the clear visualizations demonstration appropriate disentanglement using the various SCVAES.

### Weaknesses
Some more discussion of the parkinsonian dataset would be appreciated. It is unclear what details are similar with this particular dataset and the previous one (e.g. are the behavioral variables scrubbed/conditioned the same way? are the model architectures and hyperparameters the same? ) This is a small point but it might be nice to point to supplemental information in this brief final results paragraph.

Why do the authors think that the linear scrubbing improved the conditioned sequence best? This is seemingly the most limited way to represent z in equation 2? In principle, shouldn't the more sophisticated approaches (like quadratic and cubic) also be able to capture the linear approach? A bit more discussion on this point might be interesting to include.

### Questions
Why do the authors think that the linear scrubbing improved the conditioned sequence best? This is seemingly the most limited way to represent z in equation 2? In principle, shouldn't the more sophisticated approaches (like quadratic and cubic) also be able to capture the linear approach? A bit more discussion on this point might be interesting to include.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose scrubbed conditional variational autoencoder (SC-VAE), a novel framework for disentangling nuisance factors by removing variable information from latent spaces by using an adversarial learning objective. They demonstrate the utility of SC-VAE using 2 mouse behavior datasets.

### Strengths
- This framework extends C-VAEs into a more interpretable realm by introducing scrubbing. The idea of scrubbing the nuisance variables out of data can allow researchers to focus on the variable of interest without the unnecessary/irrelevant information. 
- The idea of isolating the semantic information from the character of the action has the potential to be applied to many fields other than neuroscience such as speech recognition or emotion classification.
- Clear flow throughout the paper.

### Weaknesses
 - Generalizability: Since there is the need for specific assumptions and constraints to guarantee disentanglement, e.g.  picking the known factors, SC-VAE might be inflexible across datasets with unknown structures. I know that the unsupervised methods were briefly mentioned at the beginning and the most prominent weakness to them seemed to be the sensitivity to nuisance variability but this then brings the flexibility in mind once again in terms of more complex datasets with less prior knowledge on the structure. I would be interested to know how SC-VAE could be adapted to work in cases where nuisance factors are hard to determine.
- Figures: Figures can be more polished. Right now many of them look like default matplotlib figures (See minor points for improvement suggestions).

Minor points

- For each plot in Fig 2.a,b,c,d, the top and rightmost axis can be removed, and for Fig2.a.b the legend doesn't need to be repeated. Same for fig4.
- Fig3.f and fig3.i have overlapping histograms, and in general the axis labels are illegible in fig3.
- l398 there might be extra space in ‘Fig. 2e’.
- Fig4.a the second plot y axis label is too close to the title.

### Questions
- In terms of pose estimation, I often hear about DeepLabCut. I know that framework doesn’t use a VAE backbone but in general how does SC-VAE compare to DeepLabCut?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a framework for modeling 3D pose dynamics which is capable of disentangling both continuous and discrete nuisance factors (such as speed and animal identity). They propose to use a conditional variational autoencoder, where the conditioning variables are the nuisance factors to disentangle. In order to properly ensure disentanglement of the nuisance factors from the VAE latents, the authors then propose a series of strategies for "scrubbing" the nuisance factors from the latents. They then demonstrate the effectiveness of these various strategies using 3D poses from a mouse behavioral experiment in a series of well-designed control studies. Finally, they apply these strategies to a larger dataset of healthy and diseased mice and demonstrate their ability to accurately discriminate between these two groups.

### Strengths
the problem is well-motivated appropriate for the ICLR audience, and the paper is generally well-written

the solution proposed by the authors is a creative synthesis of the existing literature, as well as some extensions necessary to make their solution work in practice

the validation experiments shown in figs 2a-c are strong, with appropriate baselines (I like the use of VAE Processed as a baseline in the heading direction experiments)

consistent motion synthesis (sec 4.3) is also a neat way to test disentangling

### Weaknesses
the authors test a wide range of models, but there is a lack of comparison to other established disentangling methods. while this literature is large, it would, for example, be useful to compare speed disentangling against the model in costacurta et al 2022. this model builds invariance to a specific nuisance variable (speed) and was designed for this exact type of data; if the authors could show that one of their models performs on par with the costacurta model, and can disentangle other generic variables besides, it would strengthen the argument for the scrubbing approach with pose data.

some details of the experiments are not clear. in sec 4.2, is there a separate model fit for each of the nuisance variables? if so, what happens if a single model is trained to scrub both speed and heading direction? in general, it is not clear if this approach is robust to scrubbing multiple variables at once. It would be beneficial to clarify whether the scrubbing is performed sequentially or jointly, and what the implications of each approach are for the final latent representation. Furthermore, it is not clear if the scrubbing is done in the latent space, or if it is done in the input space before encoding, which would have a large impact on the interpretation of the results.

the MMD analysis in sec 4.5 should be expanded upon, at the moment it is hard to understand. A simple decoding analysis (healthy vs diseased) would be a nice complement, and could lead to a punchier conclusion ("we could decode disease state x% of the time in the VAE, and y% of the time in the SC-VAE-QD"). I am also somewhat surprised that scrubbing leads to _improved_ discriminability between healthy and diseased conditions; I suppose this is because there are systematic differences between the two conditions that are obscured by animal identity? There are many such healthy vs diseased experiments with transgenic lines where a single subject will fall into one or the other category, but never both. In this case _not_ scrubbing subject ID would likely lead to higher discriminability (though perhaps for uninteresting reasons, such as diseased subjects are slightly smaller on average, etc.)

unsupervised clustering of pose data is becoming more ubiquitous in large-scale drug screens and disease research. the differences between two disease models, or the effects of a drug, can manifest in subtle differences in animal behavior. one of the potential drawbacks of this approach is that, by scrubbing certain information from the latent representation, these subtle differences may also be lost. while I think this work is super interesting and useful, I think a fuller discussion of its potential drawbacks (and possibly how these can be controlled) should be included in the Conclusions section.

### Questions
the sentence starting on L76 is very dense and difficult to parse: "we show that simple linear estimators perform favorably to traditional neural adversarial paradigms while introducing strategies for nonlinear estimators which bypass the need for specifying adversarial neural networks and their hyperparameters." can this be clarified?

fig 1 contains a lot of information but is difficult to see at its current size (especially 1c), can this be enlarged?

L293: "we increment or decrement the forgetting factors based on which filter provides a better fit to the minibatch statistic" - this seems to imply either/both forgetting factors can change, which contradicts the previous statement that one factor is "fixed" - please clarify

sec 4.4: the authors find that different scrubbing strategies are appropriate for heading vs speed. This is an interesting finding, but what does it mean for the practical applicability of this method?

do the authors have any intuition for what features are being removed by scrubbing subject identity? is it just subject size, or something else? if the 3D poses were normalized within each subject by, say, distance from tailbase to neck (or some other such pair of points), does the subject id scrubbing still result in disentangling?

as a control experiment, if the authors scrubbed disease state instead of animal identity in the final analysis, does the MMD drop to a chance level?

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
3

### Summary
The paper, "Disentangling 3D Pose Dynamics with Scrubbed Conditional Latent Variables," introduces the Scrubbed Conditional Variational Autoencoder (SC-VAE) as a framework for analyzing 3D pose data to extract behavior-relevant signals from nuisance factors like speed, direction, and individual traits. While the approach could offer valuable tools for behavioral research, several fundamental issues weaken the rigor, interpretability, and reproducibility of the work, limiting its potential impact.

### Strengths
The SC-VAE framework could provide useful tools in fields like neuroscience, where disentangling complex behaviors is essential. By addressing nuisance factors, SC-VAE theoretically enhances clustering and behavioral analysis. However, without stronger empirical validation, its practical contributions remain speculative.

### Weaknesses
 -Key claims lack adequate empirical or theoretical support. For example, Line 52-53 states that "the other latent variables are not necessarily, nor typically, invariant to the conditional factor" without any justification or citation. Similarly, Line 60 lacks evidence to support the assertion that nuisance factors, like speed, do not impact behavior representation. This weakens confidence in the model’s purported advantages.

-Several statements are overly vague, such as Line 222-223: "if the latent dimension D is small, one expects the C-VAE to learn a disentangled representation." Without specifying a relative scale for 𝐷, it is difficult to understand or reproduce the model setup. Clearer definitions and justifications for parameters are necessary to enhance reproducibility and interoperability. The lack of detail regarding the specific architecture of the VAE and C-VAE, including the number of layers, the type of activation functions, and the dimensionality of the latent space, further hinders reproducibility. 

-The model is evaluated against only a single baseline, despite references to multiple adversarial models. This limited comparison restricts the ability to gauge SC-VAE’s robustness and leaves the evaluation incomplete, particularly given the lack of consideration for other adversarial baselines aimed at disentangling nuisance variables. The choice of a single baseline, especially when the field offers a variety of adversarial methods, raises concerns about the thoroughness of the evaluation. The paper would benefit from comparisons with methods that explicitly optimize for disentanglement using different architectural choices.

-Line 65 refers to "weak supervision" while the model receives the full ground truth for certain variables. This contradicts conventional definitions of weak supervision, potentially misleading readers regarding the model’s true level of supervision. The use of the term 'weak supervision' is inaccurate given that the model has access to complete information about the conditional variables, which is more akin to conditional learning rather than weak supervision.

-The comparison between SC-VAE and C-VAE is not entirely fair, as SC-VAE benefits from direct optimization of latent variables, giving it an advantage. It would be fairer to include other adversarial methods in the comparison to better contextualize SC-VAE’s performance. The direct optimization of latent variables in SC-VAE introduces an inherent advantage over C-VAE, making the comparison less informative about the true capabilities of SC-VAE. A more balanced comparison would involve methods that also employ direct optimization or other forms of explicit disentanglement.

-Key implementation details, such as model architecture, hyperparameters, and balancing of loss components (particularly λ for term weighting), are missing. Without these, it is challenging to reproduce the results or determine if they arise from design choices or hyperparameter tuning. The absence of specific details regarding the loss function, including the exact form of the reconstruction loss and the KL divergence term, further complicates reproducibility. The lack of information on how the hyperparameter λ was chosen and its impact on the model's performance is also a significant concern.

-Visualizations referenced in Line 397 are cluttered and lack clear captions, making them difficult to interpret and detracting from the study’s overall clarity. Simplifying these figures and providing self-explanatory captions would improve readability and support the model’s claims more effectively. The lack of clear labels and legends makes it difficult to discern the different components of the visualizations and their relevance to the study's findings.

-The log-likelihood (LL) calculation presented in Figure 3.C is not well explained, making it hard to interpret the metric’s relevance to the conclusions. A more detailed description of the calculation process would improve transparency. The paper lacks a clear explanation of how the log-likelihood is calculated, including the specific distributions used and the parameters involved. This lack of clarity makes it difficult to assess the validity of the metric as a measure of disentanglement.

-The authors claim SC-VAE can extend to other species and behaviors, but no additional experiments support this assertion. Expanding validation to other datasets is crucial for establishing generalizability. The claim of generalizability is not supported by empirical evidence and should be tempered until the model is tested on diverse datasets.

### Questions
What evidence supports the claim that nuisance factors like speed do not affect behavior representation (Line 60)? Has this assumption been empirically tested?

Could you offer more insight into how parameter choices, especially the selection of λ for weighting loss terms, affect the model's performance?

Given that SC-VAE optimizes latent variables directly, would you consider including other adversarial methods for a more balanced comparison? How might this impact the conclusions drawn about SC-VAE’s performance?

Would you consider adding comparisons with other adversarial baselines designed to disentangle nuisance variables? This would provide a clearer assessment of SC-VAE's robustness in comparison to similar methods.

### Soundness
2

### Presentation
3

### Contribution
2
