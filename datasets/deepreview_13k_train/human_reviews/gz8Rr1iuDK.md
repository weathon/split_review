# Geometric and Physical Constraints Synergistically Improve Neural PDE Integration

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
Neural PDE surrogates can improve on cost-accuracy tradeoffs of classical solvers, but often generalize poorly to new initial conditions, accumulate errors over time. To close the performance gap between training and long-term inference, we constrain neural surrogates with symmetry equivariance and physical conservation laws as hard constraints, using novel input and output layers that support scalar and vector fields on the staggered grids commonly used in computational fluid dynamics. We systematically investigate how these constraints affect accuracy, individually and in combination, on two challenging tasks: shallow water equations with closed boundaries and decaying incompressible turbulence. Compared to a strong baseline, both types of constraints improve performance consistently across autoregressive prediction steps, accuracy measures, and network sizes. Symmetries are more effective but do not make physical constraints redundant. Doubly-constrained surrogates were more accurate for the same network and dataset sizes, and generalized better to initial conditions and durations beyond the range of training data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper systematically investigates how various symmetries and conservation laws affect PDE integration accuracy, individually and in combination. To impose these as hard constraints, this paper introduces novel input and output layers. Exepriments are carried on two challenging tasks: shallow water equations with closed boundaries and decaying incompressible turbulence, and it was shown that both types of constraints improve performance consistently across integration times, accuracy measures, and network sizes, and that symmetries are more effective than physical constraints and optimal performance was achieved by combining both.

### Strengths
1. Extensive experiments on two challenging tasks and state-of-the-art performance on prediction accuracy. 
2. clear conclusion that symmetries are more effective than physical constraints and optimal performance was achieved by combining both.
3. Introduction of novel input and output layers to staggered grids to impose symmetry and conservation constraints.

### Weaknesses
1. Novelty.  This paper focuses on testing the effect of symmetries and conservation laws on PDE integration accuracy to give a transparent comparison of the effectiveness of individual techniques. Enhancing neural PDE integration with symmetries has been explored in (Wang et al., 2020; Helwig et al., 2023; Smets et al., 2023; Huang & Greenberg, 2023; Ruhe et al., 2024), and improving neural PDE integration with physics constraints has been explored through additional loss terms (Read et al., 2019; Wang et al., 2020; Stachenfeld et al., 2021; Sorourifar et al., 2023), or by reparameterizing neural network outputs to respect them as hard constraints (Mohan et al., 2020; Beucler et al., 2021; Chalapathi et al., 2024; Cranmer et al., 2020; Greydanus et al., 2019). Besides novel input and output layers and a fair comparison, are there any algorithmic novelties in comparison to these works?
2. In fig.3 and fig.4, the energy is shown. Why did not show the mass directly which is the conserved quantity under consideration?
3. Generalization: the SWE equation is linear to the fluid surface elevation , can this fact explain the generalization capability on SWEs using a "L" shaped initial surface? How to explain the generalization capability on INS? Also, please give a definition or reference for wavenumber, which did not appear in equation (9).
4. In the paragraph starting from line 187, please cite appendix E that describes the phyiscs constraints. And in equation (73), what is the relationship between mass and the surface elevation? 
5. Please give the hardware used and simulation time to generate the reference solution and training data. Also, please give the hardware used and GPU-hours for training.
6. Typos: line 68, "to solutions at time via supervised learning" should be "to solutions at time t via supervised learning"? line 256, "Iinitial" should be "Initial", line 347, "perdition" should be "prediction".
7. Theory. This paper could be improved from the theoretical aspect. For example, the conserved physical quantities are related quantitatively with the solutions, so the losses corresponding to solution prediction and conservation laws are correlated, and maybe a loss bound or convergence rate can be analyzed based on this.

### Questions
see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a method for enfiorcing symmetry and PDE constraints in neural PDE "integration", together with a study on how symmetry constraints and physical constraints act together to improve the rollout stability for the investigated PDE settings.

While I find this setting thematically intriguing and while I do see merit in the proposed method, I find the manuscript lacking on multiple fronts. My main issue is misleading messaging, as the title suggests a much broader work and a systematic treatment that would go beyond 2 examples and a single architecture. Moreover, the explanation of the method is quite lacking in my view and I would have wished for either more figures and/or a better explanation of the method in the text. 

**Conclusion**
While I think that this is promising work, I wish that the treatment was better explained and more systematic. Enforcing constraints can be done in many ways and this is just a single one with a single baseline. The title suggests a much broader study and I think the literature would benefit from a systematic study that studies the importance of physical and symmetry constraints.

As such, I do find the manuscript to be incomplete. In a normal Journal article I would suggest a major revision, but as this is a Conference venue, I suggest tthe authors rework the article and resubmit to the next conference.

### Strengths
The authors suggest an interesting method for constraining neural PDE surrogate models and show how it improves the rollout stability for their baselines. They present 2 non--trivial examples on a staggered grid, which is a departure from standard regular grids in PDE surrogates.

### Weaknesses
 **Major**

- **Misleading messaging**: I have an issue with the term "PDE integration" and as a consequence, the title, abstract and large parts of the introductory text are misleading. Unless the PDE operator is integrated numerically, by discretizing it, we cannot really call this PDE integration. We are rather learning neural surrogates, which in some regime may approximate the integral solution operator. But we are not integrating, in contrast to neural ODEs for examples, which I initially thought were related. I find the title of the paper is highly misleading in this regard and it over-sells what is actually found in the paper. I would strongly recommend the authors revise title, abstract and introduction and adapt their messaging
- **Lacking explanation of the proposed method**: The method is not explained in detail and from the text alone and Figure 1 it is hard to understand how symmetries and/or physical constraints are exactly enforced. While I do see that the text refers to Appendix C, the formulas in the appendix do not help to convey the core idea of these layers. As such, I would propoise the authors to rework the explanation of the method in the main text and augment it with figures
- **Weak baselines**: The method is only compared to a "vanilla" U-Net, which is not very well suited to autoregressivey approximate solution operators of PDEs. It would be great to have other baselines e.g. FNO and it's physics-constrained counterpart: PINO which also enforces physicality during training.

**Minor**

- I find Figures 2,3,4 quite overloaded and hard to read. Distributing these figures into separate Figures would make the paper much easier to parse and also drastically reduce the amounto f explanation these Figures require
- Why is Section 4.2 called Decaying turbulence? I do not see any mention of turbulence in this section. Is this simply due to the chosen example? Is the fact that it is decaying somehow important

### Questions
I would be curious how exactly physical constraints are enforced in the output layer. From the text and figures alone, this is unclear to me. Moreover I am curious why not more PDEs were tested such as non-hyperbolic ones? Wouldn't this method be applicable there as well? Also what about PDEs on manifolds with more complex symmetries, such as SO(3)-equivariance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
I thank the authors for an interesting submission. I found the central idea clear. 

It concerns itself with building in the inductive bias of symmetry constraints and conserved quantity preservation directly into the structure of neural PDE surrogates. They explore the p4m group of discrete translations, reflections, and right-angle rotations. Most importantly, they build these symmetries into a model that maps between staggers Arakawa C-Grids, the dominant modality for modeling fluids on regular domains. The experiments are an ablation of this idea on decaying turbulence and shallow water equations, which are common datasets/systems of consideration in this field. As expected, the authors find that increasing amounts of constraint, lead to better models. This is because in this field the constraints on preserved quantities and symmetries are exact.

### Strengths
Novelty and significance
- As far as I am aware there this is novel work. I do not know of examples of equivariant layers in the neural PDE literature that concern themselves with staggered grids as used for CFD. The Arakawa C-grid is the most commonly used in CFD applications and so this work is also aiming for impact in areas of practical significance.

Written quality
- The written quality of the submission is high. The style is clear, the objective is clear, the exposé of ideas and execution is clear. 

Experiments
- The experiments on the shallow water equations (Fig 3) show that adding the symmetry constraints improves decorrelation time compared to baselines without.
The experiments on decaying turbulence (Fig 4) show that the adding symmetry constraints improves energy spectrum in the far term (chaotic field)
- I like the ablation where the authors try an out-of-distribution test in Figure 4. It highlights the importance of inductive biases for out-of-distribution reasoning

### Weaknesses
Significance and scope
- The work is restricted to considering finite symmetry groups of discrete grids (the p4m group of translations, reflections, and $90^\circ$ rotations, and subgroups thereof). While the symmetry groups under consideration are exact (and probably a lot simpler to implement than groups of continuous actions), they are indeed rather limited in scope. It would have been nice to see explorations in other groups. PDEs have quite interesting Lie point symmetry groups e.g. Brandstetter et al. (2022) and Wang et al. (2021) and it would have been nice to show that equivariance to these groups can be achieves on the grid.
- The authors focus on a limited set of discrete symmetries, specifically the p4m group, which while relevant for structured grids, does not capture the full range of symmetries present in many PDEs. For instance, many PDEs exhibit continuous symmetries, such as scaling invariance or rotational symmetry in arbitrary angles, which are not addressed by this work. Exploring these continuous symmetry groups, as done in Brandstetter et al. (2022) and Wang et al. (2021), would significantly broaden the applicability and impact of the proposed method. The current approach, while technically sound, is confined to a rather narrow class of problems.

Experiments
- The greatest weakness of an otherwise solid paper is a lack of comparisons with contemporary works in the field that either:
- a) explore the imposition of symmetries on to neural PDE surrogates for instance _“Incorporating Symmetry into Deep Dynamics Models for Improved Generalization”_ (Wang et al., 2021) or in the very least use data augmentations as in _“Lie Point Symmetry Data Augmentation for Neural PDE Solvers”_ (Brandstetter et al., 2022) or 
- b) explore other kinds of stabilization techniques, such as noise injection _“Learned Coarse Models for Efficient Turbulence Simulation”_ (Stachenfeld et al., 2021), pushforward technique _“Message Passing Neural PDE Solvers”_ (Brandstetter et al., 2022), alternative stabilizing losses such as _DySLIM_ (Schiff et al., 2024) or denoising architectures such as _PDE-Refiner_ (Lippe et al., 2023).

I do think the paper is well-motivated, written well, and within the (limited) experimental scope convincingly performant, but the lack of experimental baselines from elsewhere in the field is of concern when it comes to rigor. I believe cannot encourage the authors to run more experiments at this point, but I do want to highlight that this is the main reason why I can only support this paper as a marginal accept at most.

### Questions
- Equation 73: You enforce mass conservation by removing a global mean. This is somewhat different to the way that FVM works, where one first computes fluxes through cell faces and then applies continuity within a cell to compute the change of mass in each cell. 1) Did you try the former FVM-like update rule and 2) would the FVM-like rule not exemplify the use of the staggered grid more, after all the output layer computes quantities of the faces of the grid?
- How does this work tie into classical methods such as equivariant moving frame theory in _“Symmetry Preserving Numerical Schemes for Partial Differential Equations and their Numerical Tests”_ by Rebelo & Valiquette (2011). That paper shows how to construct finite difference schemes based of the Lie Points Symmetry group.
- Nit: some of the references are not placed in brackets; for example, line 93 or 105 or 115. I would advise the authors to check for these (I think the missing LaTeX command is \citep{})
- Nit: Tables 1 and 2. I found it confusing that m denotes reflection in p4m and also mass. Maybe try a different symbol?
Nit: line 347: perdition -> prediction

### Soundness
3

### Presentation
3

### Contribution
3
