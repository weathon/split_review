---
job_id: 4f6864ac-ecf5-4452-8a31-65523c9f7304
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 5qd7V5TNGV.pdf
paper: CP4D: Compositional Physics-aware 4D Scene Generation
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on generative models, compositional modeling, physics-aware scene generation, and hybrid AI systems combining learned priors with simulators.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, methodology, experiments, quantitative and qualitative results, and conclusion; despite substantial weaknesses in novelty, methodological specification, and evaluation, it clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes CP4D, a compositional pipeline for text-driven 4D scene generation that decomposes the task into background generation, foreground object generation, physics-based motion simulation, and final 4D scene composition. The method combines pre-trained image, editing, segmentation, image-to-3D, monocular depth, and video diffusion models with heterogeneous physical solvers, and uses SDS-style optimization to refine physical parameters and inter-object positions. Experiments on a curated set of 17 prompts compare CP4D to video generation, physics-based simulation, and text-to-4D baselines, with qualitative examples, quantitative metrics, and ablations.

## Strengths
The paper tackles a relevant problem. Many current 4D generation methods do indeed struggle with physical plausibility, and the paper is trying to move beyond purely appearance-driven generation by explicitly injecting simulation and scene composition structure. That broad direction is meaningful for the ICLR community.

The overall decomposition is intuitive and easy to follow. In particular, **Figure 1** does a good job of communicating the three-stage pipeline, namely background/foreground 3D synthesis, physically grounded motion simulation, and automated scene composition. Even though many components are borrowed, the figure makes the system design legible and clarifies how the different expert modules are wired together.

The compositional formulation is practically appealing. Splitting a 4D scene into static background plus dynamic foreground objects is a sensible engineering choice, and the claimed editing flexibility in **Figure 6** is one of the more convincing practical aspects of the submission. The examples suggest that the pipeline can swap foregrounds or backgrounds while keeping the rest of the scene reasonably coherent, which is a useful property even if the core scientific advance is limited.

The paper identifies a real issue with simulator-render mismatch in multi-object interactions. **Figure 2** is helpful here: the visual progression from simulation artifact to rendered mismatch to optimized result illustrates the paper’s motivation for position refinement more concretely than the text alone. This is one of the few places where the need for the proposed refinement is shown in a targeted way rather than asserted abstractly.

There is at least some quantitative effort to compare against diverse baselines. **Table 1** includes not only open-source video models but also physics-based and 4D-generation baselines, and CP4D shows stronger scores on the chosen metrics. While I have significant reservations about the evaluation setup, the paper did not limit itself to a single weak comparison point.

The ablation intent is appropriate. The authors do try to isolate the effects of material optimization and position optimization, and **Figure 5** plus the associated appendix **Table 3** at least aim to connect the main design choices in Section 4.2 and 4.3 to visible differences in the outputs.

## Weaknesses
1. **The contribution is heavily a system integration of many existing components, and the paper does not do enough to establish what is actually new beyond the assembly.**  
   The pipeline in Section 4 combines an LLM for prompt decomposition, a text-to-image model, an image editor, SAM, image-to-3D models, monocular depth estimation, physical simulators, and a video diffusion model with SDS. That is not automatically a problem, but the burden then shifts to clearly isolating the new algorithmic ideas. I do not think the paper succeeds there.  
   The main “novel” pieces appear to be: (i) using SDS to optimize physical parameters $\Theta$ in **Equation 4**, (ii) using SDS to optimize object displacements $\Delta \Gamma$ in **Equation 5**, and (iii) the depth-based initialization plus refinement in **Equations 6-9**. Each of these is plausible, but they are presented at a fairly high level and feel incremental relative to the prior combination of simulator priors and diffusion guidance already discussed by the authors in Section 2.2. The paper needs a much sharper statement of what exact technical idea is new, why that idea is non-obvious, and how it differs from simply “optimize simulator parameters with a generative prior.”

2. **The method specification is underspecified in several places, especially the optimization objectives, which makes it hard to assess correctness and reproducibility.**  
   The SDS formulations in **Equations 4 and 5** are too abstract for the central role they play. For example:
   - What exactly is the rendering process from simulated 3D Gaussian states $\mathbf{G}_f^i$ to the video $V$?  
   - How are camera trajectories chosen during optimization? A single fixed view, multiple views, random views? This matters because the paper claims explorable 4D scenes and view-consistent dynamics.  
   - What prompt is used in the SDS loss, only $\mathbf{T}_f$, or is motion-specific text separated from object identity text?  
   - How are timesteps $\zeta$ sampled and what is the weighting $\omega(\zeta)$?  
   - What regularization prevents degenerate solutions, for example unrealistic but prompt-matching parameter values?  
   Without these details, **Equations 4 and 5** read more like placeholders than complete learning objectives. Given that these optimizations are central to the claimed gains in physical realism, this is not a cosmetic issue.

3. **The physical parameter estimation and optimization story is scientifically weakly grounded.**  
   In Section 4.2 the paper says a VLM infers material properties such as $E$, $\mu$, and $\rho$, as well as external forces $\mathbf{Q}$, then SDS optimizes them. But the paper never explains the admissible parameter ranges in the main text, the parameterization used for optimization, or how physical validity is enforced. For example, if Young’s modulus and density are optimized directly, are positivity constraints imposed, perhaps via log-parameterization? Is Poisson ratio constrained to a valid interval? Are external forces regularized to remain physically meaningful?  
   This matters because otherwise the method is not really learning “physics-aware” parameters, it is just searching over simulator knobs until a video prior is satisfied. That distinction is important: one is physically interpretable modeling, the other is perceptual fitting through a simulator. Right now the paper rhetorically leans on the former while methodologically looking much closer to the latter.

4. **The composition model in Section 4.3 relies on fragile heuristics and the geometry is not fully justified.**  
   The transformation in **Equation 6**, $\mathbf{G}_f^* = S \times \mathbf{G}_f + P$, only includes isotropic scaling and translation. No rotation is considered. That may be acceptable for some scenes, but the paper does not discuss when this assumption breaks. If the foreground object produced by the image-to-3D model has an arbitrary canonical orientation, placement into the background coordinate frame generally requires at least a rotation parameter.  
   Similarly, **Equation 7** initializes $P$ using the centroid depth of the segmented foreground in a monocular depth map from the composite image. This is a very rough heuristic, and the paper does not analyze its failure cases, sensitivity, or ambiguity. **Figure 3** illustrates the frustum-based scale initialization clearly, but it also reveals how coarse the approximation is: the scale is chosen to fit the object inside the view frustum at depth $P^z$, not to match metric scene geometry or contact constraints. This is more of a visibility heuristic than a reliable scene-composition method.  
   The subsequent optimization in **Equation 9** uses only an image-space $\ell_2$ loss to fit $\hat{\mathbf{I}}_{b,f}(P,S)$ to $\mathbf{I}_{b,f}$. That objective is weakly posed, and the paper itself admits ambiguity between $P$ and $S$. The sequential optimization is a practical patch, but not a principled resolution.

5. **The paper’s central claims about physical realism are not supported by sufficiently rigorous evaluation.**  
   The evaluation set contains only **17 examples** (Page 7), which is extremely small for the breadth of claims made in the abstract and introduction. The paper repeatedly claims “faithful adherence to complex physical dynamics” and “significantly outperforming existing methods,” but a dataset of 17 curated prompts is much too limited to support such sweeping conclusions.  
   In addition, many comparisons are hard to interpret as apples-to-apples. Some baselines are pure video generators, some are image-to-video systems, some are physics-grounded but restricted in material type, and some do not model full scenes. This does not invalidate comparisons, but the paper should be much more careful in distinguishing task mismatch from model superiority.

6. **The quantitative metrics in Tables 1 and 2 are not well aligned with the paper’s strongest claims.**  
   **Table 1** reports VBench and WorldScore metrics such as motion smoothness, consistency, imaging quality, photo consistency, and 3D consistency. These are useful generic perceptual metrics, but they are not strong evidence of physical correctness. For instance, a model can score well on consistency and imaging while still violating contact dynamics, momentum transfer, or material behavior.  
   **Table 2** relies on GPT-4o scores for “physical realism,” “photorealism,” and “semantic alignment.” This may be acceptable as a weak supplementary signal, but here it is being used as one of the main pieces of evidence for physical realism. The problem is not merely that it is an LLM judge; the problem is that the paper offers no stronger task-specific physical evaluation. If the core claim is physics-aware generation, the evaluation should include explicit measurements of collision timing, penetration, rebound behavior, deformation plausibility, trajectory error relative to simulator outputs, or human studies focused specifically on physics violations.  
   Put differently, **Table 1** mostly shows CP4D produces videos that score well on broad quality metrics, not that it genuinely advances physics-aware 4D generation.

7. **The ablation study is too shallow relative to the complexity of the pipeline.**  
   Section 5.3 and **Figure 5** only ablate two refinement components. But the full method has many consequential design choices: prompt decomposition, image editing for background-foreground harmonization, the choice of separate 3D models for background and foreground, the depth-based position initialization in **Equation 7**, the scale heuristic in **Equation 8**, the sequential optimization in **Equation 9**, and the choice of heterogeneous solvers.  
   The appendix **Table 3** adds more ablations, but even there the analysis is limited. For example, there is no ablation comparing against simpler alternatives such as using the raw simulator outputs without diffusion refinement but with better manual parameter tuning, or comparing the proposed composition to a naive but stronger geometric baseline. Given how many moving parts there are, the current ablation is not enough to identify where the gains actually come from.

8. **The qualitative evidence is selective and somewhat over-claimed.**  
   **Figure 4** shows only two examples, and those examples are carefully chosen to favor the proposed method. The figure does support the claim that CP4D can produce more stable-looking outputs than some baselines, especially in the cloth and bottle cases. However, the paper uses these examples to support broad statements about physical plausibility and identity preservation, while offering only a small number of cherry-picked cases in the main paper. With a 17-example evaluation set, stronger per-category breakdowns would be more informative than a couple of visual showcases.  
   Also, the claim that the method yields “explorable and interactive 4D scenes” is stronger than what is convincingly demonstrated in the main paper. The appendix mentions multiview rendering, but the main paper does not analyze the extent of camera freedom, view consistency degradation, or whether the backgrounds are actually geometrically complete enough for meaningful exploration.

9. **The fairness of baseline setup is not sufficiently documented.**  
   The baseline section on Page 7 lists a heterogeneous group of methods, but the paper does not clearly explain how prompts, initialization images, 3D assets, or scene context were adapted for each baseline. This matters a lot because some methods naturally operate on foreground-only objects, some require images rather than text, and some do not support backgrounds. If one baseline receives only a foreground crop while CP4D benefits from a handcrafted compositional pipeline, the comparison can be informative, but it is not a straightforward “same task” benchmark. The paper should separate such comparisons more carefully and disclose the exact protocol in the main text, not only implicitly through appendix details.

10. **The paper overstates the scientific role of the video prior refinement.**  
    The text in Section 4.2 claims the video diffusion model injects “commonsense knowledge” to correct inaccurate physical parameters and coarse collision geometry. That is plausible at an intuitive level, but it is also where the paper becomes conceptually slippery. A video prior can improve perceptual plausibility, but it can also simply push outputs toward what looks common in videos, regardless of true physical validity. This is especially concerning when the same model is used to optimize both material parameters and object positions via SDS. The paper should discuss this tension more honestly, because otherwise “physics-aware” risks meaning “simulator-based initialization plus appearance-based correction.”

11. **There are clarity and notation issues throughout the paper.**  
    A few examples:
    - In **Equation 2**, the order of assignments is unconventional and slightly confusing, with $\mathbf{G}_b,\mathbf{G}_f$ defined before $\mathbf{I}_b,\mathbf{I}_{b,f},\mathbf{I}_f,\mathbf{M}_f$ that they depend on.  
    - In Section 4.2, the notation for the solver output $\mathbf{G}_f^i$ and time $t$ is imprecise. Is $i$ a time index, object index, or deformation state index?  
    - In **Equation 7**, the notation $\mathbf{D}_{b,f}[(M_f=1)_{\text{cen}}]$ is not standard and needs a more careful definition.  
    - There are several typos or awkward phrases, for example “foareground” in the caption of **Figure 1**, “Position-Base-Dynamic” instead of Position-Based Dynamics, and inconsistent capitalization in section titles.  
    These may look minor, but they accumulate and matter because the method is already complicated and modular.

12. **The paper’s positioning relative to prior compositional and physics-aware 4D generation is not sufficiently sharp.**  
    The related work cites many relevant papers, but the actual differentiation is thin. For instance, the paper should more explicitly articulate how CP4D differs from prior compositional 4D generation pipelines and from prior works that combine physical simulation with diffusion priors. Right now the introduction and related work mostly say prior methods either lack explicit physics or support only limited materials/interactions, but the method section does not crystallize the conceptual leap beyond “use multiple existing tools in a more modular way.” This weakens the case for contribution.

## Questions
1. **Can the authors specify the exact optimization procedure for Equations 4 and 5 in the main paper?**  
   Please clarify what variables are optimized, how they are parameterized and constrained, what views are rendered during optimization, how prompts are formed, how many SDS steps are used, and what regularizers are applied. A concrete pseudocode block would increase confidence substantially.

2. **How are physical validity constraints enforced during optimization of $\Theta=\{\rho,E,\mu\}$ and external forces $\mathbf{Q}$?**  
   If there are explicit bounds, reparameterizations, or projection steps, please provide them. If there are none, please discuss whether optimized parameters remain physically interpretable.

3. **How fair are the baseline comparisons in Tables 1 and 2?**  
   Please provide a clearer protocol summary in the rebuttal: for each baseline, what input modality was used, whether the same text/image setup was provided, whether background context was available, and whether any baseline-specific tuning was performed.

4. **Can the authors provide stronger evaluation focused on physical correctness rather than generic video quality?**  
   Even a small but targeted analysis, for example penetration rate, collision timing error, rebound statistics, object identity preservation under collision, or a human study specifically labeling physics violations, would help justify the central claims.

5. **How robust is the scene composition stage to failures in monocular depth estimation and foreground segmentation?**  
   Since Equation 7 depends directly on $\mathbf{M}_f$ and $\mathbf{D}_{b,f}$, a sensitivity analysis or at least representative failure cases would be useful.

6. **Why is rotation omitted from Equation 6?**  
   Is this because the foreground 3D model is already aligned by construction, or is it an approximation? Please clarify the assumptions and discuss cases where this breaks.

7. **Can the authors report a more systematic category-wise breakdown over the 17 prompts?**  
   Since the dataset includes rigid, elastic, deformable, and fluid cases, per-category results would be more informative than only aggregate scores.

8. **What is the actual degree of 4D explorability achieved by the composed scenes?**  
   The paper claims explorable scenes, but the main text does not quantify or analyze camera range, view consistency, or completeness of the generated background geometry. More evidence here could change my assessment of significance.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work is a generative vision/graphics system and does not involve human subjects or obviously sensitive data in the presented experiments.

## Soundness Rating
2: fair. The high-level approach is plausible and some empirical evidence is provided, but the core optimization details are underspecified and the evaluation does not adequately substantiate the strongest claims about physical realism.

## Presentation Rating
3: good. The paper is generally readable and the pipeline is easy to follow, with helpful figures such as Figures 1 to 4, but there are still notable notation gaps, several unclear equations, and some over-claiming.

## Contribution Rating
2: fair. The paper addresses an interesting problem and assembles a usable pipeline, but the scientific contribution appears limited by heavy reliance on existing components, weak differentiation from prior work, and insufficient evidence that the method advances physics-aware 4D generation in a principled way.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
My main issue is not that the system is useless, it is that the paper currently reads more like an ambitious engineering stack than a clearly isolated research advance. The problem is interesting, some visuals are promising, and the pipeline is sensible, but the technical novelty and evidence do not yet match the paper’s claims. A stronger version with tighter method specification, more physically grounded evaluation, and clearer positioning could become competitive.

## Reviewer Confidence
4: confident. I am confident in the assessment, though not absolutely certain. The paper is in an area I know well, and I checked the main equations, figures, and experimental evidence carefully, but some implementation specifics are omitted from the main paper.