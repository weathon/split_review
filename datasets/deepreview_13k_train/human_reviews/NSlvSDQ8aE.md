# Force-Guided Bridge Matching for Full-Atom Time-Coarsened Dynamics of Peptides

- Decision: Reject
- Scores: 5, 8, 8

## Abstract
Molecular Dynamics (MD) is crucial in various fields such as materials science, chemistry, and pharmacology to name a few. Conventional MD software struggles with the balance between time cost and prediction accuracy, which restricts its wider application. Recently, data-driven approaches based on deep generative models have been devised for time-coarsened dynamics, which aim at learning dynamics of diverse molecular systems over a long timestep, enjoying both universality and efficiency. Nevertheless, most current methods are designed solely to learn from the data distribution regardless of the underlying Boltzmann distribution, and the physics priors such as energies and forces are constantly overlooked. In this work, we propose a conditional generative model called Force-guided Bridge Matching (FBM), which learns full-atom time-coarsened dynamics and targets the Boltzmann-constrained distribution. With the guidance of our delicately-designed intermediate force field, FBM leverages favourable physics priors into the generation process, giving rise to enhanced simulations. Experiments on two datasets consisting of peptides verify our superiority in terms of comprehensive metrics and demonstrate transferability to unseen systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a conditional generative model called Force-guided Bridge Matching (FBM) to improve Molecular Dynamics (MD) simulations. Traditional MD simulations, while accurate, are time-consuming due to the need for small time steps. FBM leverages a physics-informed approach to time-coarsened dynamics by incorporating an intermediate force field to guide the generation process. This allows the model to better approximate the Boltzmann distribution, essential for realistic molecular conformations, and improves simulation efficiency without sacrificing accuracy.

### Strengths
1. The paper is clearly written and easy to follow, also this task is indeed important.
2. The experiments are effectively support the conclusions.
3. The code and detailed hyperparameters are provided, making it easy for others to reproduce the results.

### Weaknesses
I believe the main weaknesses with this paper is its lack of novelty, as it appears to be a straightforward combination of [1], [2] and [3] in a slightly altered setting. It seems the author did not conduct a comprehensive literature review. My reasons are as follows:

1. Training with trajectory pairs was already introduced in [1]; the only difference here is that [1] focused on protein backbones and employed SE(3) FM. In addition, next frame prediction is also a subtask in [2]. The current work does not significantly deviate from this approach, merely applying it to a different molecular representation without introducing substantial methodological novelty. The core idea of learning dynamics from trajectory pairs remains the same, and the change in representation does not warrant a claim of significant advancement.
2. The concept of force-guided training was discussed in [3], with the main difference being that [3] uses SE(3) diffusion. While the current paper uses bridge matching, the underlying principle of incorporating force information to guide the generative process is directly derived from [3]. The shift from diffusion to bridge matching, while a technical variation, does not introduce a fundamentally new concept in terms of force-guided training. The core idea of leveraging force fields to improve the generative process is already established in [3].

In essence, this paper combines aspects of both [1] ([2]) and [3] without properly referencing [1], [2]. While it presents a solid engineering application, it lacks originality.

Additionally, I have another concerns, which I’ve outlined in the Questions section.

### Questions
1. Using bridge matching may not be ideal, as all samples along the same trajectory are expected to follow the same Boltzmann distribution. Ideally, we would achieve **a constant transformation**; however, in practice, we are performing point-to-point correspondence (from one delta distribution to another). This approach, therefore, appears theoretically unsound. What are your thoughts on this?
2. Experiments on peptides alone are too limited and should at least be performed on the smallest “protein” (backbone), Chignolin.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel model, FBM, which integrates force guidance into a bridge matching framework for time-coarsened dynamics. Traditional MD methods often struggle with achieving a balance between computational efficiency and accuracy, especially over long time scales. FBM addresses this challenge by directly targeting a Boltzmann-constrained distribution, effectively combining physical priors with generative modeling to capture full-atom time-coarsened dynamics.

### Strengths
- The integration of force-guided priors within the bridge matching framework for MD simulations is innovative. This approach goes beyond standard generative modeling by incorporating Boltzmann-distributed physical priors, improving the model's ability to simulate realistic molecular transitions over extended time scales. 
- The authors conduct a comprehensive evaluation of FBM on two peptide datasets, demonstrating that it consistently outperforms baseline models across several metrics, including distribution similarity and validity of generated molecular conformations. 
- The paper is generally well-structured, with a clear presentation of the methodology and objectives. 
- The model’s ability to generate high-quality conformations with transferability across unseen systems is particularly valuable for applications requiring generalized and scalable MD simulations.

### Weaknesses
 - The experiments to evaluate the model’s performance are conducted mainly on datasets consisting of small peptides. It would provide a more comprehensive understanding of the model's performance to extend the evaluation to include larger peptides or more complex molecular structures. Specifically, the current evaluation lacks a demonstration of how the model scales with increasing system size, which is critical for practical applications in molecular dynamics.
- While the FBM model demonstrates promising results, a more extensive comparison with traditional MD simulations across additional cases would strengthen its credibility. It would be helpful to provide more detailed time comparisons between FBM and MD simulations. The current comparison lacks a rigorous analysis of computational cost, including wall-clock time and resource utilization, which is essential for assessing the practical advantages of FBM over conventional methods.
- The TIC plots in Figure 4 are not entirely clear in demonstrating the advantages of FBM. It might be more interpretable for readers to adjust the color scheme, explore alternative visualizations, or include additional quantifiable metrics. The current visualization does not effectively highlight the differences in sampling efficiency or accuracy between FBM and baseline models, making it difficult to assess the model's performance based on these plots alone.

### Questions
The TIC plots in Figure 4 are not entirely clear in demonstrating the advantages of FBM. It might be more interpretable for readers to adjust the color scheme, explore alternative visualizations, or include additional quantifiable metrics.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper the authors propose a model to produce relevant MD  trajectories from an initial structure, using bridge diffusion with a possibility to ensure that the recovered conformation statistic obeys a  Boltzmann distribution rather than blindly following the learned data distribution. They accomplish their goal by constraining the form of the conformation distribution to be the learned data distribution with each conformation being weighted by a learnable Boltzmann factor. So the constraints appeared from the beginning and are present in the trained model from the get-go: no need at prediction time to go through expensive re-weighting procedure, as it is part of the model. Hence their model relies on first learning the reverse and forward process that would generate the initial and final experimental conformations (conditional to those), then use this newly learned score function and use it within a dedicated network to calculate the associated Boltzmann weight (i.e. the conformation energy). At prediction time one can either just perform the simple diffusion, or decide to add the correction term to the simple diffusion-associated force field, which turns out to “simply” be the gradient of the energy term in the learned Boltzmann re-weighting coefficient: hence the name.

### Strengths
The paper offers a rather intuitive and straightforward way to add some physics-derived constraints to the trajectory produced at prediction time. Moreover, their model is state of the art when taking into account a rather diverse set of evaluation metrics: from comparing model output collective variables at the distribution level, in terms of validity through checking bond clashes and breaking, or finally in term structure flexibility compared to ground truth. The simplicity of adding or not the correction term in a tunable way through a guidance strength hyperparameter allows for a direct ablation study which shows the usefulness of the correction (guidance) term.
The care brought into splitting the dataset (clustering and splitting by  cluster), indeed allows them to claim generalizability, even though I  didn’t really understood why AD seems to be treated a bit separately  from the peptide in the test set.
Last but not least, it also proposes a robustness/explanatory study by adding the results of their hyperparameter tunning and some effects of those hyperparameters.

### Weaknesses
The paper is pretty strong and its only rather minor weakness has to do with easiness to have a direct interpretation/overall view of the metrics for the samples presented. Right now the metrics show their claims (their model is better) which is great, but they, I  believe, are hard to link to the model's performance and usefulness. 
For example, I think Figure 6 is nice because it shows a direct comparison with ground truth in a more obvious way than other figures. Hence the few following questions and propositions of improvement described in the next section will be about that.

### Questions
Overall all those figures and metrics are complementary and I believe for a few samples to have all of those would help a lot. Indeed we have the different JS values for the full test set but having them also for the samples presented, as well as having directly the distribution comparison to the ground truth as in Figure 6 would be super helpful. I  believe it can be hard to understand what a JS value means except that it is bigger for the output of one model compared to the other. 
It could be also nice to have more of those figures for your best-picked trajectories but also for those that didn’t work as well: again just to have a feel about what could be driving those numbers.
Moreover the study of hyperparameters effect (table 6) is a great add to show the robustness of the results. I believe it could be used to show the effect of force guidance on the trajectories generated and their metrics:  mainly following for a single or a few peptides how their trajectory change when the strength of guidance increases. This is touched upon in section f1 where it is pointed out that validity and contact metrics indeed nicely follow the guidance strength, but I feel like this is less true/obvious for the other metrics.
Finally, it would also be nice to see how easily this is applicable in more real case scenarios, with some scaling laws with peptide size, etc…

Overall I would say that all of my remarks are minors, but I still encourage  the authors to follow them as much as possible as I believe it will ease the overall understanding of the model ability. I would also like to state that even though I was able to follow all the proofs and didn’t see anything that I would deem to be problematic, I don’t believe I  have the level of expertise truly required to judge the math present in this paper with certainty.

### Soundness
3

### Presentation
3

### Contribution
3
