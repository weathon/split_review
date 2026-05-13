# Neural Fluid Simulation on Geometric Surfaces

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 10, 1

## Abstract
Incompressible fluid on the surface is an interesting research area in the fluid simulation, which is the fundamental building block in visual effects, design of liquid crystal films, scientific analyses of atmospheric and oceanic phenomena, etc. The task brings two key challenges: the extension of the physical laws on 3D surfaces and the preservation of the energy and volume. Traditional methods rely on grids or meshes for spatial discretization, which leads to high memory consumption and a lack of robustness and adaptivity for various mesh qualities and representations. Many implicit representations based simulators like INSR are proposed for the storage efficiency and continuity, but they face challenges in the surface simulation and the energy dissipation. We propose a neural physical simulation framework on the surface with the implicit neural representation. Our method constructs a parameterized vector field with the exterior calculus and Closest Point Method on the surfaces, which guarantees the divergence-free property and enables the simulation on different surface representations (e.g. implicit neural represented surfaces). We further adopt a corresponding covariant derivative based advection process for surface flow dynamics and energy preservation. Our method shows higher accuracy, flexibility and memory-efficiency in the simulations of various surfaces with low energy dissipation. Numerical studies also highlight the potential of our framework across different practical applications such as vorticity shape generation and vector field Helmholtz decomposition.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel framework for simulating incompressible Eulerian fluid flow on 3D surfaces using neural implicit representations. This method leverages the Closest Point Method (CPM) and exterior calculus to parameterize the fluid’s velocity and vorticity fields directly on the surface without relying on discretization, which reduces memory costs and bypasses the need for conventional spatial discretization. The framework introduces a covariant-derivative-based advection process, which integrates surface flow dynamics while minimizing energy dissipation. Notably, this work is among the first to simulate incompressible fluid dynamics on neural surfaces, achieving enhanced accuracy and energy preservation across various geometric representations.

### Strengths
### CPM Formulation
The math formulation is clean and concise. It is quite apparent that the authors are coming from a graphics background and I love this clean DDG writing style.
- The Closest Point Method (CPM) is relatively new in visual computing, yet its integration with neural fields here aligns with my belief in CPM’s potential for solving PDEs on surfaces. Compared to surface sampling techniques (as seen in Geometry Processing with Neural Fields [Yang et al., 2021] and similar studies), CPM offers a structured way to define differential operators in volumetric data by rigorously establishing value transfer in the ambient space embedding the surface.
- A persistent challenge in neural implicit representations is that, while data is represented volumetrically (e.g., through neural SDFs), the actual solutions are constrained to the 0-level isosurface. Sampling on this isosurface can be inefficient, but CPM provides an effective alternative by leveraging the ambient space, enhancing both efficiency and rigor.

Overall, I would love to see this line of work being continued and the math formulation should be shared and seen within the ML community.

---
Some misc comments:
- The related works section is thoughtfully composed, with necessary references cited and no excess, reflecting high-quality citation practices.
- The choice of ground truth in this paper is well-justified and suitable for the presented comparisons.

### Weaknesses
I have two concerns, regarding the claimed first and third contributions.

---

### Performance vs. Storage vs. Accuracy
The storage and accuracy benefits presented as a core contribution appear somewhat overstated since these gains stem from the inherent compact representation of neural fields, as noted in prior works like INSR-PDE (Chen et al., 2023). The neural network, here largely a standard MLP, serves as a model reduction tool or compressed parameter space. However, the substantial cost is slower simulation speeds, particularly noticeable in evolving the PDE on a neural representation, and this tradeoff is well-documented in the field, tracing back to foundational work like *Geometry Processing with Neural Fields* (Yang et al., 2021). Additionally, working with surface PDEs inherently mitigates spatial complexity compared to volumetric Eulerian approaches, further diluting the impact of memory savings in this context. Unless optimized network designs or implementation techniques were used, this contribution may feel more like a tradeoff typical of neural fields than a novel improvement.

**TL;DR:** Without unique implementation optimizations, this tradeoff doesn’t stand out as an independent contribution, as neural networks naturally offer compact representations at the expense of computational speed.

---

### First to Simulate on Neural Implicit Surface Representation
The claim of being the first to simulate incompressible fluid flow on neural implicit surfaces is somewhat uncertain, as prior work using sampling techniques, like *Geometry Processing with Neural Fields* (Yang et al., 2021) or INSR-PDE, could also solve surface PDE like Laplace Equation by sampling on the surface. While it’s conceivable that these methods struggle with incompressibility when applied to Navier-Stokes, demonstrating their limitations would highlight the advantages of the Closest Point Method (CPM) for ensuring divergence-free constraints on neural surfaces. Including such comparative results, even as failure cases, could effectively underscore this paper’s unique approach.

### Questions
### Questions
1. **Use of DEC Language**: The paper’s use of Discrete Exterior Calculus (DEC) is rigorous and suits the formal approach taken. However, many in the ML and physics communities might be more accustomed to traditional differential or vector calculus, so DEC may require more adjustment for those readers. Adding intuitive explanations alongside the DEC formalism could enhance accessibility, although this may vary depending on the preferences of other reviewers.
2. **Handling Narrow Geometric Features in CPM**: The reliance on ambient space in CPM may lead to ambiguities when processing narrow or thin features. Clarifying whether this dependency impacts stability or accuracy for such geometries would enhance the framework’s applicability and inform potential adaptations to handle such cases.
---
### Suggestions
1. **Missing Citations**
    1. For by construction divergence-free field with neural network, maybe also cite [Deep Fluids](https://onlinelibrary.wiley.com/doi/10.1111/cgf.13619).
2. **Clarifying Performance Gains Over INSR**:Intuitive explanation of why your method is > INSR > PINN when constrained by storage size. Intuitively, INSR is superior to PINN because it doesn’t record time in the neural field, so, given the same storage budget, INSR should and must outperform PINN. However, your method doesn’t gain from saving less information in the neural field to achieve higher accuracy (i.e., it doesn’t concentrate model expressiveness on specific features to achieve this). So, what is the intuitive reason behind your method’s improved results over INSR? Is it due to the CPM formulation or the Helmholtz decomposition? An “ablation” would be helpful here.

### Soundness
4

### Presentation
4

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
This paper builds on the recently introduced Closest Point Exterior Calculus (CP-EC) to propose a novel method for preserving the divergence-free property of vector fields on surfaces. By leveraging the closest point map, this approach seamlessly extends computations from the surface to the surrounding Euclidean space. At the core of the paper, Theorem 3.1 presents a specific construction for generating a divergence-free vector field on a surface using the CP-EC framework. This framework enables the calculation of gradient, divergence, and curl in a way that respects the intrinsic geometry of the surface, ensuring that the velocity field remains divergence-free when constrained to the surface. A key advantage of this method is its flexibility, as it supports simulations on various surface representations, including analytic surfaces, explicitly defined mesh surfaces, and, notably, neural implicit surfaces. The paper introduces a complementary advection process based on covariant derivatives for fluid dynamics, designed to minimize energy dissipation. Numerical studies confirm the framework’s accuracy, energy preservation, memory efficiency, and adaptability to geometry. Results show it achieves about 15 times higher accuracy than other methods with similar storage, offers 5 times memory savings over classic methods, and effectively models fluid dynamics. Additionally, the simulator's robustness is demonstrated through an end-to-end generation task and a real-world velocity field decomposition.

### Strengths
The paper shows that the recently introduced Closest Point Exterior Calculus (CP-EC) is very well suited to simulate fluid simulation on neural implicitly defined surfaces in 3D. The CP-EC allows to automatically guarantee the divergence-free properties of the vector field. The method achieves up to 15 times higher accuracy than previously used discretization methods on the surface with the same memory requirements, which is confirmed by extensive numerical simulations of different applications.

### Weaknesses
The English in the current version of the paper needs to be improved. Numerous articles are missing and sometimes the wrong words are used (subtle instead of subleties, divergence free instead of divergence free property, etc).

Compared to the actual straigth forward application of the CP-EC to the case of flow simulation on surfaces, the paper seems cumbersomely long and is also not as clear to read as the recent papers on the topic referenced in the paper, whose presentation is clearer and more concise.  Maybe the authors can try to improve on that.

### Questions
How do you do the interpolation of the pulled forms? In the CP-EC poster the authors recommended the Cubic Lagrangian.
How does this interpolation affect the divergence-free property of the velocity field? Were there any numerical problems?
Is it possible to do an ablation study on this point?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper proposes a framework for fluid simulation on surfaces that is divergence-free by construction. This is done by using exterior calculus tools, in special the definition of the divergence based on the Hodge star operator and the exterior derivative, the property that the Hodge star is (up to a sign) its own inverse and the nilpotent property of the exterior derivative. The Closest Point Method is used to apply those tools on generalized surfaces, making a natural link with Riemannian geometry, and enabling the evaluation in the tangent space around samples in the surface. With those tools it is possible to transit between the surface and $R^3$ as needed, in special for advection which can be done considering the Riemannian metric of the manifold.

### Strengths
To be honest, I had a lot of fun reviewing this paper. Unless other reviewers flag major flaws that I could not find, I think it is ready for acceptance.

* It is a very good example of when a simple and elegant core idea based on strong guarantees enables a lot of very interesting questions and consequences. The core idea of using the nilpotent property of the external derivative and the self inverse property of the Hodge star operator to force a divergence free vector field on a surface is elegant and foment all the paper discussion.

* The loss formulation is as expected, very intuitive.

* As far as I know, It is the first method that converges in implicit surfaces.

* The method does not rely on training data.

* Evaluation is robust. The idea of starting with analytic examples where ground truth is easier to evaluate is good.

* Related work section cites every paper I could think of. The care with the citation of classic papers (even for datasets) is notable.

* Mathematical notation is very clean. It easy to see that there is a lot of effort with notation polishing.

* The paper makes use of very good references for background Math.

### Weaknesses
I will point some minor weaknesses that could be fixed to improve the paper.

(1) An image depicting equation (4) and another showing the advection process would greatly improve the friendliness of the paper since both processes are very geometric. That would make the paper be appreciated by a broader audience.

* In the image for equation (4) it is sufficient to show the neighborhood of the surface, the mapping $j$, the mapping $cp*$, the vector resulting from the gradient and the tangential vector acquired from cross product of the gradient with the normal.

* For the advection image it is sufficient to depict the push forward (pull back) function in action and the inner product using the Riemannian metric.

(2) The presentation could be more friendly by giving some intuition along the text. I will point some places I think this kind of intuition would be beneficial.

* Line 199: could say that the even though the divergence may be expressed using different k-forms, the definition of div(v) is the 0-form version resulting in a scalar function.

* Line 299 (equation 4): could say that $cp^*\sigma$ is a notation abuse because $cp^*$ expect a k-form but $\sigma$ is a 0-form. Also that the composition with $j(x)$ is to restrict the computation to the surface, the gradient is to acquire a vector field and the cross product is to acquire a tangent vector field. A reference to the proposed image would also be good here.

* Line 234 (equation 5): could say that that vorticity expression considers the rotation axis equals to the normal because it is evaluated on the surface. Then the vorticity may be represented as a scalar field.

* Line 257: could say that the expression is a neighborhood extension of the surface along the normal field.

* Line 320 (equation 13): could say that the $<. , .>_p$ notation is an inner product considering the Riemannian metric of the manifold of the tangent space at point p. A reference to the proposed image would be good here.

* Line 327 (equation 15): could say that the inner products are the first-order approximation of the push forward function.

* Line 344: that paragraph could say that the harmonic components do not contribute to the vorticity and that is the reason why the additional harmonic network is needed. Could also say that it is constant along the simulation because it is associated with the topological structure of the surface, which does not change over time.

(3) This paper deserves an acronym so it may be more easily referenced in the future by other researchers. I advise the authors to think about changing the title to include a creative acronym.

### Questions
(1) Why introducing $f$ in equation (8) instead of using $\sigma$ directly?

(2) I think a $t$ subscript is missing in equation (8) ($\Phi_t$).

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes an implicit neural representation to improve solvers that simulate flows on geometric surfaces through geometric adaptivity. The authors propose a neural physical simulation framework to construct a parameterized vector field on surfaces using exterior calculus formalism. Through a Closest Point Method, it is proposed an implicit neural network representation that is able to maintain a divergence-free property intrinsically. Divergence-free is an important property of Navier-Stokes solvers, and strictly enforcing them is a challenging task. Furthermore, the authors claim that the proposed approach is able to accurately preserve the energy of the flow as time advances.

### Strengths
Proposing alternative representations to the standard discretizations (e.g., grid/meshes) for solving PDEs is a very interesting and challenging topic of research. The authors propose a method that considers specific intricacies of the PDE solution when employing neural representations, along with desired properties that can potentially be satisfied in a continuous fashion (e.g., the divergence-free condition).

### Weaknesses
### weaknesses:
Unfortunately this paper is clearly below the ICLR quality acceptance bar. My major concerns are as follows:
- Poor exposition along with several typos which make the paper hard to understand. For example. the structure of Section 3.1 is composed of fragmented phrases forming very short paragraphs, making it hard to follow. Several typos and confusing phrasal structures (L11: “Incompressible Euler fluid on the surface”, L20: “We contribute a neural physical simulation framework on the surface with the implicit neural”, L240: “In the meanwhile" to name a few) greatly compromise the quality of the paper.
- The main idea of the paper is based on wrong assumptions. The poster “Closest Point Exterior Calculus” [7], in which the paper is heavily based, already offers a solution that is independent of the mesh quality. This invalidates one of the main motivations of this submission that previous approaches are dependent on mesh quality, and thus an implicit neural representation is required. Moreover, the assumption that storage is a limiting factor on solvers is also incorrect, since a solver usually has to store a single time-step of the represented variables for advancing the simulation state. The presented results also show very modest resolutions.
- There are missing references and/or previous methods are not thoroughly considered, leading to an outdated methodology proposition. Recent approaches such as “Covector Fluids”, “Impulse Particle In Cell”, “Fluid Simulation on Neural Flow Maps”, “Eulerian-Lagrangian Fluid Simulation on Particle Flow Maps” and “Lagrangian Covector Fluid with Free Surface” adopt structure preserving integrators by considering the deformation of the flow map during advection. This is ignored by the proposed advection method, which has a rather lengthy description in the paper. Lastly, the statement that Elcott et al. [5] suffers from instabilities is incorrect. Modern structure preserving solvers are able to accurately advect velocities without major stability issues.
- The paper partially focuses on showing mathematical proofs that are known by the exterior calculus community (divergence free vector fields on surfaces), which make the described theory not so relevant as new theoretical contributions. The authors could just reference relevant discrete exterior calculus material or move the lengthy mathematical descriptions to the Appendix.
- The paper should have been focused on more relevant aspects of the implicit neural representation, such as network structure, how to properly tackle high-frequencies of the implicit neural field, how to make the training/evaluation process efficient (e.g., check “Instant Neural Graphics Primitives with a Multiresolution Hash Encoding”) etc.
- The authors mention that pressure projection (usually the most expensive part of a fluid solver) is not required by their approach. However, they solve a non-linear optimization problem iteratively with a simple ADAM gradient descent approach. This approach is way less efficient than traditional operator splitting, as evidenced by the timings shown in Table 1 (16h for 80k vertices is a very inefficient timing for the considered resolution). Lastly, there seems to be some high-frequency “ringing” artifacts generated by the proposed method in Figure 3 which are not present in ground truth or in the HOLA-7 results.

These are some of the reasons that justify my low score for this paper. I suggest the authors to rethink their approach before resubmitting the manuscript.

### Questions
- Did the authors explore alternative network designs for representing the implicit neural fields (such as "Instant Neural Graphics Primitives with a Multiresolution Hash Encoding”) ?
- How does the method fares in simulations where regions of turbulence are highly concentrated? Is the proposed adaptivity property working as expected?

### Soundness
1

### Presentation
1

### Contribution
1
