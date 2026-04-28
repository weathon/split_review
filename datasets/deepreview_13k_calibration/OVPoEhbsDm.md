# Thermodynamics-inspired Structure Hallucination for Protein-protein Interaction Modeling

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
Modeling protein-protein interactions (PPI) represents a central challenge within the field of biology, and accurately predicting the consequences of mutations in this context is crucial for various applications, such as drug design and protein engineering. Recent advances in deep learning (DL) have shown promise in forecasting the effects of such mutations. However, the effectiveness of these models is hindered by two primary constraints. First and foremost, obtaining the structures of mutant proteins is a persistent challenge, as they are often elusive to acquire. Secondly, interactions take place dynamically, but thermodynamics is rarely integrated into the DL architecture design. To address these obstacles, we present a novel framework known as Refine-PPI, which incorporates two key enhancements. On the one hand, we introduce a structure refinement module that is trained by a mask mutation modeling (MMM) task on available wide-type structures and then is transferred to hallucinate the inaccessible mutant protein structures. Additionally, we employ a new kind of geometric networks to capture the dynamic 3D variations and encode the uncertainty associated with PPI. Through comprehensive experiments conducted on the established benchmark dataset SKEMPI, our results substantiate the superiority of the Refine-PPI framework. These findings underscore the effectiveness of our hallucination strategy to address the absence of mutant protein structure and hope to shed light on the prediction of the free energy change.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A framework, Refine-PPI, of predicting $\Delta\Delta G$ is proposed in this paper, which include 3 components: a structure encoder $h_\rho$, a structure refiner $f_\theta$, and a readout (pooling) function $g_\tau$.

New backbone coined as PDC-Net is proposed to model structures.

Experimental results show marginal improvements on $\Delta\Delta G$ prediction.

### Strengths
The general framework of Refine-PPI is interesting.

The $\Delta\Delta G$ prediction quality is seemingly equivalent / marginally improved.

### Weaknesses
1. A lot of missing details hinder the reproducibility of the paper. See Questions.

2. Overall the paper introduce a new framework and a new architecture. Although a general ablation is done, the paper very much lacks deep analysis to each components.

3. Weak benchmark performance: the elevation of performance is too marginal (especially those in the Appendix), and the time complexity is not studied. No variance is reported.

4. The usage of term "thermodynamics" and "hallucination" is hardly relevant to the proposed method and thus confusing. I would suggest the authors to use plainer descriptions.

### Questions
Q1 How are $h_\rho, f_\theta, g_\tau$ built precisely? What are the $\phi$ functions in Eq 5-7?

Q2 How are $\sigma_{x_i}$s modeled? And how are those initialized? In Eq 4 they are matrices while in Eq 7 they seem to be vectors. In my opinion 3d variance should either be a scalar or a learnable SPD matrix. Using vectors does not satisfy SE(3) invariance because an ellipsoid with standard axis is presumed, and the results are thus varied when rotations are applied to the input structure. Thus the method is not "readily apparent" to be equivalent.

Q3 There lacks a visualization of the "hallucinated" structures.

Q4 On what data, precisely, is Refine-PPI trained? The description seems to point to a 3-fold cross validation, but the concrete splits should be specified. And, since all benchmark performances are "directly copied" from a preprint, the authors must justify that their evaluation scheme is exactly the same to all benchmarks.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel deep learning architecture, Refine-PPI, for protein-protein binding mutation effect (DDG) prediction. Refine-PPI consists of two modules. The first module learns to predict the mutated structure through a masked mutation modeling task on wild-type structures. The second module learns to predict DDG of a protein-protein complex based on wild-type and mutated structures. The second module represents a protein-protein complex as a probabilistic density cloud (PDC) and encodes it using a novel PDC-GNN, where the messages are represented by its mean and variance. Refine-PPI achieves state-of-the-art performance on the standard SKEMPI benchmark.

### Strengths
* This paper models a protein as a dynamic structure, using a probabilistic density cloud representation.
* This paper develops a new message passing network architecture for probabilistic density clouds. The messages between each node consists of both mean and variance.
* The evaluation setup is comprehensive, with all the relevant baselines

### Weaknesses
 * The model only slightly outperforms previous state-of-the-art RDE-Net on a subset of metrics. It seems that overall performance of Refine-PPI and RDE-Net is similar.
* The evaluation of Refine-PPI on the first mutation structure prediction task is missing.

### Questions
* The description of probabilistic density cloud representation is a bit unclear. In particular, how are the $sigma$'s initialized? If they are initialized as zero, then they will stay zero all the time. Are they initialized by some physical calculations?
* For the first task of mutation structure prediction task, can you report the RMSD between predicted mutated structure and ground truth?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper deals with the problem of mutation stability prediction—i.e., given a mutation to a bound complex with known structure, predicting the change in binding free energy. The authors make two contributions (1) they propose _masked mutation modeling_ (MMM) a auxiliary training task where the model must generate a structure for the mutant complex, and this generated (“hallucinated”) structure is used as additional input to the free energy predictor; (2) they introduce a _probability density cloud_ (PDC) modification to EGNN which is meant to capture the uncertainty in atomic positions. The empirical results slightly improve over RDE, the previous state-of-the-art.

### Strengths
* The introduction of the MMM task is quite sensible and well-suited for data-poor tasks such as mutation stability prediction.
* The “probability density cloud” modification to EGNN is quite interesting and represents a commendable attempt to introduce physical inductive biases into point cloud networks.
* The clarity of the exposition is above average for ICLR submissions. Each contribution is well-motivated and contextualized.

### Weaknesses
 * The PDC module, while a very interesting idea, is on shaky ground mathematically.
    * The authors assume all atom positions to be independent, which is a very questionable assumption as the thermal fluctuations and epistemic uncertainty of neighboring atoms certainly should be dependent. This assumption drastically simplifies the uncertainty modeling but ignores the complex correlations that exist in molecular systems. For example, the movement of a residue in a protein is highly constrained by its covalent bonds and non-covalent interactions with neighboring residues, leading to correlated fluctuations. Ignoring these dependencies could lead to an inaccurate representation of the true uncertainty.
    * It is not possible to write down the self-covariance of the difference of random variables without knowing the cross-covariances. However, even assuming the positions to be independently distributed, then if their mean is updated as in Eq 6, then Eq 7 should read $${\sigma_{x_i}^{(l+1)}}^2 = \left[1 + \frac{1}{|N(i)|}\sum_{j \in N(i)} \phi_\mu(m_{j \rightarrow i})\right]^2{\sigma_{x_i}^{(l)}}^2 + \frac{1}{|N(i)|}\sum_{j \in N(i)}{\sigma_{x_j}^{(l)}}^2\phi_\mu(m_{j \rightarrow i})$$ i.e., with $\phi_\mu$ instead of a different $\phi_\sigma$, and distributing and squaring the $x_i$ terms because $x_i - x_j$ is not independent of $x_i$. The current formulation in the paper does not correctly propagate the variance through the message passing steps, and the use of a separate function $\phi_\sigma$ is not theoretically justified. The correct update should account for the change in the mean and how it affects the variance of the position.
    * With that said, I don’t think it’s a serious issue in itself if the network is not updating the co-variances properly. But my general concern is that the authors have not given sufficient treatment to these subtleties, and hence, the PDC module is not actually constrained to model the atomic uncertainties as the authors claim; rather, to the network ${\sigma_{x_i}^{(l+1)}}^2$ just looks like some other latent variable which it can use to help model the positional updates. It would be better to call the module “loosely inspired” by the modeling of uncertainty. If the authors nevertheless claim that this is a generally helpful modification to EGNN, this is a claim that requires significantly more thorough evaluation (on many different tasks ideally) than is given here.

* There are several critical missing details in the methodology and experiments (see Questions below).

* Some over- or mis-claiming throughout the paper
    * The authors claim (Eq 1) to recover the structural distribution of the masked residues, but the training objective is risk minimization (Eq 3), not any kind of distributional modeling objective.  The use of a mean squared error loss does not imply that the model is learning a distribution, and this claim is misleading.
    * The authors state that MMM “encourages graph manifold learning with the denoising objective”, but there is no further discussion or elaboration on how “graph manifold learning” is accomplished. The connection between the denoising objective and manifold learning is not clearly established, and the authors should provide more details on how the model is encouraged to learn the underlying data manifold.
    * Repeatedly misleading use of the term “thermodynamics” when the authors mean “uncertainty.” The former term should be reserved when explicitly referring to physically meaningful quantities like energy, entropy, and free energy. Using “thermodynamics” in place of “uncertainty” is not appropriate and should be corrected.
    * “The pictures show that particles in the interface have smaller variation compared to those in the edges of proteins.” This claim is not backed quantitatively, and, as discussed, there is no reason to believe that the learned $\sigma^2$ actually corresponds to uncertainty. Visual inspection is not sufficient to support this claim, and a quantitative analysis is needed.
    * “It can be found that generally, a small error of wide-type structure reconstruction leads to a more accurate $\Delta\Delta G$ prediction.” I see no such correlation in Figure 4B. The figure does not clearly support this claim, and the authors should either provide more evidence or remove this statement.


Justification for score: there is the potential for interesting technical contribution in the PDC, but the current presentation is not thorough enough for a conference paper. The MMM objective by itself is less novel, as auxiliary training or pretraining for mutational stability prediction has been done before, and the results are only a bit better than those prior approaches.

### Questions
* Methodology details and design are unclear
    * Where is the PDC module actually used? How are the $\sigma^2$s initialized?
    * “Moreover, it is readily apparent that PDC-Net maintains the equivariance property.” The authors should provide a proof here.
    * Because there are no gradients from the $\Delta\Delta G$ task to the structure refinement module $f_\theta$, the MMM task is really a pretraining task and not an auxiliary training task. Is there any reason to not train MMM across the entire PDB?
    * Is there any reason to use the same encoding module $h_\rho$ for the $\Delta\Delta G$ predictor and for the structure refinement module $f_\theta$. Why can’t $f_\theta$ carry its own encoding module?
* Experimental details
    * It is not clear how the baselines are run in order to obtain \Delta\Delta G predictions, especially. ESM-1v, B-Factor, etc. While some reasonable guesses exist, the authors should spell it out and not leave it up to guessing.
    * How many different complexes are in SKEMPI and is the average per-complex improvement statically significant?
    * In the ablation studies, why does Model 1 use the RDE-Net backbone instead of the Refine-PPI modules $h_\rho$?
* Minor issues
    * Broken link to figure 3.2 where a visualization of the PDCs is promised. 
    * The term “probability density cloud” suggests a more expressive parameterization than Gaussian uncertainty. I suggest the authors rename the module.
    * In Table 1, what is the meaning of “pretraining”? How is it possible that Refine-PPI and ESM are classified as no-pretraining, yet B-factors are classified as pretraining?
    * Inconsistent use of $\Sigma$ vs $\sigma$.
    * Typos: “Wide type”, "paradiagm", "disucssion", "intergrate", "envision" instead of "visualize"
    * The clarity could be improved with a figure illustrating the coordinate initialization.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
