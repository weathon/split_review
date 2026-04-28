# Common Causes for Sudden Shifts: Linking Phase Transitions in Sinusoidal Networks

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 6, 6, 5, 6

## Abstract
Different phases of learning dynamics exist when training deep neural networks. These can be characterised by statistics called order parameters.  In this work we identify a shared, underlying mechanism connecting three seemingly distinct phase transitions in the training of a class of deep regression models, specificially Implicit Neural Representations (INRs) of image data. These transitions include: the emergence of wave patterns in residuals (a novel observation), the transition from fast to slow learning, and Neural Tangent Kernel (NTK) alignment.  We relate the order parameters for each phenomenon to a common set of variables derived from a local approximation of the structure of the NTK.  Furthermore, we present experimental evidence demonstrating these transitions coincide.  Our results enable new insights on the inductive biases of sinusoidal INRs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper identifies a shared, underlying mechanism connecting three seemly distinct phase transitions in the training of a class of deep regression models, in implicit neural representations of image data.  The paper then presents experimental results on the distribution of critical points and the dynamical consequences of hyperparameters.

### Strengths
The paper is easy to follow.
The paper conducts 'preliminary investigations into the dynamics of feature learning within INRs for image data' and analyzes the dynamic phase transition of SIREN models.  This shows 'NTK provides a rich theoretical tool for deriving and relating order parameters to understand training dynamics'

### Weaknesses
I am unfamiliar with this field.
As the paper is mainly theoretical, it is unclear beyond the simple raw images presented in the paper. In my opinion, such theoretical works tend to be less useful than application papers in general since they only tend to be valid in very specific circumstances.   Furthermore, there are no practical suggestions on improving machine learning performance.  However, as there are other theoretical papers that analyze NTK that are accepted to peer machine learning conferences this paper is within the remit of ICLR.

### Questions
N/A

### Soundness
3

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
3

### Summary
The authors report interesting theoretical work and computational experiments to analyze transitions in the evolution of parameters of a neural network. They use SIREN (sinusoidal representation networks) models of simple natural images (cameraman, cat) for computational experiments. They unify several order parameters, namely the evolution of loss distribution, the evolution of loss rate, and the evolution of the prediction over a local neighborhood of data points to identify the fast and slow training phases. An important feature of the work is the interpretation of the spatial order of neural tangent kernels during different phases of training.

### Strengths
* The analysis of training dynamics in SIRENs is sound. Understanding training dynamics in neural networks is important as the field works towards foundational and generalist models. The authors establish unifying links between different measures of phase transitions in a neural network's parameters. 
* The order parameter (MAG-Ma) is a valuable measure of spatial alignment in the model's predictions. The authors also introduce an order parameter that measures spatial alignment with the data's spatial structure.

### Weaknesses
 * Writing: The description is dense in critical parts of the paper and not always sequential. For example, the transition from eq. 2 to eq. 3 requires an elaboration: the time derivative of parameters ($\dot{\theta}$) is the same as the opposite of the gradient of the loss relative to the parameters. After articulating this conceptual link, eq. 3 can be derived from eq. 2. Before that, eq. 3 is too dense. The authors should explicitly state that they are using gradient descent, where the parameter update is proportional to the negative gradient of the loss function with respect to the parameters. This is a crucial step that is not clearly explained, making it difficult to follow the derivation. The lack of clear explanation makes it hard to understand the link between the parameter dynamics and loss landscape.
* No links to CNN: Given the prevalence of CNNs in discriminative and generative models of images, it is important to contrast phase transitions in CNNs vs INRs. Without the comparative analysis, it appears that MAG-Ma can be used only for INRs and not other models that depend on the edges/spatial texture for regression. The authors should discuss the applicability of their proposed order parameters to other architectures, particularly CNNs, which are widely used for image-related tasks. The current analysis is limited to SIRENs, and it is unclear if the same phase transitions and order parameters would be relevant for CNNs. This limits the broader impact of the work.
* Computational experiments are insufficient: The authors should assess the training dynamics for a substantive dataset, e.g., each image of ImageNette. The experiments are limited to only two images, which is insufficient to draw general conclusions about the training dynamics of SIRENs. The authors should evaluate their method on a larger and more diverse set of images to ensure the robustness of their findings. The lack of a comprehensive evaluation limits the generalizability of the results.
* No code seems available: Reproducing and building on top of this work requires authors to share their code. Some of these order parameters can be used to improve training efficiency, e.g., to stop training once the critical point is reached. The absence of code makes it difficult for other researchers to verify the results and build upon this work. This lack of reproducibility hinders the progress of the field.
* I'd suggest an alternative title to clarify the contribution (as I read): "Surfacing inductive biases of sinusoidal networks by linking phase transitions"

### Questions
* Are the data in Fig. 2, 5, and 6 that show the mean and variance of the order parameters measured over multiple training runs for the same image (cameraman or cat) or different images?  If single images, why not evaluate training dynamics over a substantive set, e.g., a set of models for 1000 different images that represent natural images and physical simulations?
* Can the order parameters be computed efficiently during training to be used as stopping criteria or to adjust the learning rate?
* An observation: the neural tangent kernel is mathematically related to the concept of spatial coherence (measured by mutual intensity) in statistical optics (see Joseph Goodman's book on statistical optics).

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
4

### Summary
This is a quite interesting paper that considers the training dynamics
of sinusoidal neural networks. It takes an approach that is in the
tradition of understanding machine learning methods through a
"statistical physics" approach, seeking to understand
disordered/ordered phenomena through phase transitions.

Specifically, this work concerns itself with examining the dynamics of
training sinusoidal networks fit to image data via the evolution of
the neural tangent kernel. That is to say, by examining how the
correlation structures of the gradients evolve, the patterns of
learning dynamics are uncovered. Multiple methods and metrics are
proposed to detect these changes, which are shown to correspond to
distinct phases and phenomena in fitting sinusoidal networks to image
data. These metrics seem to provide a nice mix of "local" and "global"
measurement.

### Strengths
This paper provides a nice way to examine the behavior of neural
networks used for representing images by examining the features of
tangent kernels. I found it quite easy to follow, and reasonable in
its claims. For the most part, the authors justified their ideas
without making overly-bold claims regarding their derivations -- in
this way, the work is modest, which is appreciated.

I also found the metrics proposed to be practical -- the quantities
studied are fairly easy to calculate, which suggests that this paper
could be of use to practitioners.

Although some of the claims aren't entirely justified (for instance,
see the discussion on "diffusion" in the weaknesses section), for the
most part the metrics proposed by the authors for detecting do not
come out of thin air -- they are justified by a mixture of approximate
calculations and empirical insights gleaned from tests on image data.

### Weaknesses
Before listing the weakness: I would like the authors to understand
that the list of weaknesses is much longer than the list of strengths
not because it is a bad paper, but because the weaknesses are
"actionable," and thus are better-served by a more detailed write-up!

It is unclear to what extent the results are specific to sinusoidal
networks. Of course, images parameterized by SIREN networks are used
to demonstrate the ideas, but I as the reader am not sure whether the
analysis carried out in the paper is really specific to anything about
natural images, apart from some references to the notion of an "edge"
in an image in Section 3.2. It would be helpful if the authors would
clarify what aspects of their work they think are specific to
images/SIREN, and what aspects should apply broadly to regression
tasks using MLPs. A simple question to ask is the following: does it
make sense for this paper to be rewritten using ReLU MLPs applied to
low-dimensional regression tasks (which I suppose would look more like
the references [23,24,25])? In this direction, a more detailed
comparison to the existing literature would be helpful -- as it is
now, your proposed metrics are not compared to anything else in the
literature.

The arguments made by the authors to characterize, say, the phenomenon
of "diffusion" (Eq. 15), are a bit handwavy, in the sense that they
make a series of approximations that end up in a nice PDE that one can
call a diffusion equation. It is plausible that this is the underlying
mechanism explaining the diffusion phase in the training dynamics, but
it is not clear if this is a coincidence or not. Some more validation
in the experiments section would have been nice, showing somehow that
the training dynamics indeed resemble a diffusion equation like the
one given in (Eq. 15). For example, if we were to run two experiments:
one where we perform gradient descent to fit an INR to an image, and
another where we use the gradients of the INR to parameterize the
diffusion equation (15), would they yield similar results? Something
along these lines would make the claim significantly more convincing.

Despite the analysis being interesting, the conclusions fell flat at
the end. I understand that this paper is more of a scientific
investigation than it is an engineering exercise, so I do not fault
this work for not providing extensive experiments, proposed methods,
and so on. However, the audience of this work will probably go beyond
those who are interested in inherent properties of INRs -- the only
section to this effect was Section 4.2, which had the single
conclusion saying that $\omega_0$ is the most important
hyperparameter, as opposed to width and depth, say. It would be nice,
either via more experiments or an expanded discussion, to see how the
proposed metrics could be used by practitioners to guide their design
and use of INRs.

Another /potential/ weakness of this paper is the small scale of the
experiments. This doesn't bother me too much, personally, but it would
be more convincing if your results were reported for a larger set of
images.

### Questions
Please see the weaknesses section for points that would be helpful to have addressed -- I think addressing those points thoroughly would strengthen this paper by quite a bit.

I also have some editorial notes:

The references in this paper are formatted in a non-standard
way. Please make sure that the paper formatting guidelines are
followed closely. I am not sure if the way the authors have formatted
their in-text references is wrong, but it is different than most ICLR
papers I have read.

There are also some formatting issues: e.g., at the beginning of
Section 3.1 "equation equation 5." Please look over the manuscript
carefully to check for these sorts of errors.

Figures repeatedly are missing useful features such as colorbars,
clear axis labels, and so on. Please look over your figures and work
on their clarity!

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Submission 957 investigates the dynamics of SIREN training. SIREN is an MLP (implicit neural representation) with sinusoidal activations often trained to solve tasks on low-dimensional domains such as fitting images, solving PDEs, etc.

In practice, SIRENs often struggle early in training and then suddenly fit the image, corresponding to a sharp drop in loss (a “phase transition”). Submission 957 presents an analysis using neural tangent kernel (NTK) machinery to correlate empirical phenomena at the transition to changes in the NTK.

### Strengths
- The empirical finding that the translational symmetry of (the local approximation of the) NTK is broken at the phase transition is both novel and interesting.
- The paper’s presentation is broadly accessible to practitioners (such as myself) familiar with the NTK and SIREN literature but not with more recent theoretical advancements. This is a non-trivial strength for papers in the learning theory track.

### Weaknesses
## Unclear theoretical contributions:

The paper’s main strategy is to observe empirical phenomena in SIREN training (e.g., ripples in reconstruction, the image suddenly being fit, sharp drops in loss) and try to correlate them with changes in the NTK (or a local approximation thereof). However, these analyses all appear to be speculative and do not explain _why_ these phenomena occur.

For example, Section 3.1 presents an analysis of why ripples appear during SIREN training. However, the analysis is based on fitting isotropic Gaussians to key parameters which the paper itself states (in Sec 3.2) is not appropriate and disconnected from actual empirical training. Further, the paper’s arguments for symmetry breaking appear to contradict this assumption as well. It is thus unclear what to take away from the claim that this analysis explains the ripples.

Looking holistically at Section 3, the paper shows that when training starts to work (at the “phase transition”), the NTK changes. However, please correct me if I’m wrong, but this is tautologically true – the NTK always changes when training starts to work. For example, the introduced metric $AUC(v_0, \nabla I)$ just plainly tracks when image edges start to align with the empirical NTK eigenvector so the argument comes down to “training works when the image edges start appearing” which would also correlate one-to-one with loss, PSNR, SSIM, etc. Please correct me if I’m missing something.

The actual finding relevant to SIRENs (translational symmetry breaking) in Section 3.5 is entirely empirical. Of course, this empirical insight is valuable as well, but I don’t know what to make of it as it does not explain _why_ it breaks. Further, it is unclear what aspect of the theoretical analyses is specific to sinusoidal networks/SIREN and not any other INR parameterization. As far as I could tell, it essentially comes down to fitting a Cauchy distribution to the empirical CosNTK of a SIREN. In future revisions, please disambiguate which aspects are specific to SIREN.

Importantly, all of the empirical phenomena upon which theoretical arguments are made are only drawn from 2D image fitting and the other use cases of INRs are not addressed. It is hard to see how the presented rationale would generalize to entirely different contexts, for example, inverse problems such as MRI or CT reconstruction where INRs are also widely used. 

Lastly and importantly, there is no theoretical analysis of the frequency aspect of INR training (as in the NTK-based [Fourier features paper](https://arxiv.org/pdf/2006.10739) ). SIREN training depends entirely on the $w_0$ parameter and initialization, but none of the analysis in Section 3 accounts for it and thus it provides an incomplete picture of SIREN dynamics. In fairness, the experiments do sweep $w_0$ and do find different behaviors, but that precisely shows that a theoretical analysis is needed. 

## Non-rigorous experiments:

As rigorous theoretical explanations are not presented for these phenomena, we turn to the experiments. However, the experiments are far too preliminary in the current submission to have clear takeaways:
- Again, there is only a single problem studied (2D image fitting), whereas previous analyses of INRs study a broad range of low-dimensional domain problems. For example, SIREN studies waveform inversion, Poisson image reconstruction, signed distance function fitting, etc. The closely related NTK-based Fourier features paper studies a variety of MRI/CT reconstruction and regression problems as well.
- Even within the context of 2D image fitting, the experiments only study five images in total (e.g. cameraman). It is hard to gain generalizable insights from five toy images on a single task.


## Presentation issues:
- The entire preamble of Section 3 (+Fig 1) should moved to the Introduction as that is where the paper is actually outlined and the main contributions are clearly defined. I would merge it with the current contributions statement. Any additional space could then be allocated to further experiments.
- Section 3 begins with “Having outlined the connection between learning in INRs and field theory, ..”. What precedes it is just definitions, most of which are not specific to INRs, and using “field theory” to refer to spatial gradients/residuals/etc. is just confusing. Please refrain from borrowing terms from physics in this context. 
- Minor presentation issues:
    - The writing in the title and abstract keeps implying multiple phase transitions, whereas there is only one. Please make this clearer.
    - typo: There’s no line numbers so control+f for “equation equation 5”
    - Page 3, section 3: Please explicitly refer to the subplots of Figure 1 in the text.

### Questions
- Do the theoretical arguments made for 2D image regression in this paper generalize to the wider set of tasks where INRs are used?
- Could the authors please clearly disambiguate the novel theoretical contributions of this work?
- What is the contribution of Section 3.1 if the rest of the paper contradicts it?
- Is there an argument for _why_ translational symmetry breaking or any of the other empirical phenomena are occurring?
- Given that SIREN training depends entirely on $w_0$, why was it excluded from analysis?
- Why are the experiments focused on regressing just five images? Also, are the experiments based on performance on test pixels or is the entire image used? If so, is there a train test gap in the theory and experiments?

Please see the weaknesses above for more.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the role of phase transitions during the training of Implicit Neural Representations. More specifically, it is revealed that phase transitions occur simultaneously. For this reason, three lenses are considered: spatial distribution of residuals, principal eigenvectors of the NTK, and training curve analysis. The first achievement is a unification of the different associated order parameters, which actually provides a theoretical reasoning for the occurrence of the phase transitions. The second major achievement is the introduction of a novel parameter termed MAG-Ma explicitly tracking violations in the translational symmetry of the NTK. In several numerical experiments, the distribution of critical points and the dynamics of hyperparameters are examined.

### Strengths
Based on my understanding, the paper offers several novel and insightful contributions, such as the identification of phase transitions in clearly defined periods and the introduction of the MAG-Ma parameter. These findings are partially rigorously justified, and the main assertions are also partly supported by numerical verification. If these findings are correct, this paper would represent a significant advancement in the theory of sinusoidal networks.
The numerical experiments impressively show the alignment of the critical points of the order parameters and the effect of depth on the critical behavior.

### Weaknesses
This paper suffers from several major drawbacks. 
First, many central statements only hold true approximately (excluding equations 10 and 11, which are numerically verified). For instance, I cannot validate the quality of the approximations in (13), (14), (28), or (29), which are crucial for major findings in the manuscript. The approximations, particularly those related to the Neural Tangent Kernel (NTK) and its spectral properties, need more rigorous justification. Specifically, the approximation of the NTK's eigenvectors and eigenvalues, which are central to the analysis of phase transitions, lack sufficient validation. The paper should provide a more detailed error analysis of these approximations, possibly by comparing the approximated quantities with their exact counterparts in simplified settings where such computations are feasible. Here, either additional numerical experiments or theoretical justifications would be highly appreciated.
Second, the presentation of the paper should be improved. Indeed, some parts of the paper can only be understood after reading the supplementary material. However, the authors do not mention the additional proofs in the supplementary material in the main manuscript, which could be tackled by forward references to the supplementary material. For example, the derivation of the MAG-Ma parameter and its connection to translational symmetry violations are not fully clear in the main text and require a deep dive into the supplementary material. This lack of clarity hinders the accessibility of the work. 
I am not sure if the numerical results in Figures 4-6 only hold true in general or only for specific situations. Additional numerical experiments would be required since these findings are crucial for the correctness of the entire approach. The current experiments do not explore a wide enough range of datasets or network architectures to convincingly demonstrate the generality of the observed phase transitions and the behavior of the MAG-Ma parameter. The paper needs to demonstrate that the observed phenomena are not specific to the chosen experimental setup. Finally, I am not sure about the simultaneity of the order parameters since according to Figure 4, the confidence regions of MAG-Ma and many other order parameters hardly overlap. In this sense, MAG-Ma can be interpreted as a time-shifted order parameter. The paper lacks a clear explanation for the observed temporal shift in the critical points of MAG-Ma compared to other order parameters. This raises concerns about the interpretation of MAG-Ma as a true indicator of the phase transition, or if it is merely a delayed consequence of the same underlying phenomenon. 

Some minor remarks:
- typo "equation equation 5" on page 3
- "Which resembles" instead of "which resembles" on page 4
- "Where we have" instead of "where we have" on page 5
- please cite the "related works" on page 6

### Questions
1) Can you please either provide rigorous mathematical justifications or additional numerical experiments for the approximations mentioned above? I would like to be sure about the correctness of all these statements.
2) From my perspective, additional numerical experiments for Figures 4-6 are required to disprove that the results are only valid for this specific configuration. Could you please perform these experiments on other datasets or in modified settings? 
3) Is MAG-Ma a time-shifted order parameter as suggested in Figure 4 or is this only true for this specific experiment? Can you please provide additional numerical experiments for this temporal evolution? Is this shift consistent across different experimental settings? Do you have any theoretical justification?
4) To improve the presentation, I would like to have more forward references to the relevant sections in the supplementary material whenever possible and reasonable.

### Soundness
3

### Presentation
2

### Contribution
4
