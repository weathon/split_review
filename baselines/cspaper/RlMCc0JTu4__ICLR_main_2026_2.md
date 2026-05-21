---
job_id: 68a1f443-7ed5-4d2c-83e7-623efe1d13b6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: RlMCc0JTu4.pdf
paper: Tactile Affordance for Robot Synesthesia for Dexterous Manipulation
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly in scope for ICLR through reinforcement learning, multimodal representation learning, and robotics manipulation.

## Minimum Quality
Pass ✅ The submission has the required high-level structure, including abstract, introduction, related work, method, experiments, and conclusion. That said, there are serious quality issues, including internal inconsistency, missing referenced figures/tables, and unclear mathematical exposition, which strongly affect the review outcome but do not by themselves force a desk rejection under the stated checks.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any explicit hidden prompt, instruction to automated reviewers, or other obvious manipulation attempt in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes TARS, a visuo-tactile manipulation framework that aims to unify external visual perception and local tactile sensing using a shared point-cloud representation for dexterous manipulation across both contact and non-contact states. The method combines a visual-tactile affordance module and a teacher-student policy learning setup, and is evaluated on four simulated manipulation tasks, with claims of robustness and real-world applicability.

## Strengths
The paper targets a meaningful problem. Handling the transition between non-contact visual perception and contact-rich tactile interaction is a real difficulty in robot manipulation, and the stated goal of using a unified representation across both regimes is well motivated in the Introduction.

The high-level intuition is easy to understand. In particular, **Figure 1** does a reasonable job illustrating the intended benefit of the approach, namely that visual affordance should help before contact while tactile sensing becomes important after contact. Even though the figure is conceptual rather than quantitative, it helps convey the central idea that the method is trying to support manipulation across different contact states instead of treating vision and touch as isolated modules.

The paper evaluates the method on multiple manipulation tasks, not just one toy scenario. Lift, Pick-and-Place, Pull Drawer, and Open Door cover a somewhat broader range of interaction regimes than many narrowly scoped robotic manipulation papers.

There is at least an attempt to go beyond a single full-system comparison. The experimental section discusses baselines and variants, including RS, VA, and PN+MLP, and also claims studies on downsampling, modality ablations, and object transfer. If these experiments were fully and clearly presented, they could have been useful for understanding which part of the method matters.

The paper also tries to connect representation design to policy learning, rather than presenting perception and control as totally separate pieces. That systems perspective is valuable for the robotics/representation-learning audience.

## Weaknesses
I have substantial concerns about the paper’s internal consistency, technical presentation, and evidentiary support. The core idea is interesting, but the manuscript in its current form is not reliable enough for publication.

1. **The paper appears to contain severe internal inconsistency, including sections that do not match the claimed method.**  
   The most alarming issue is that large parts of **Section 3.2 (Visual-Tactile Affordance, Pages 4 to 6)** discuss a membrane model for a bubble sensor, including quasi-static equilibrium, FEM discretization, pressure forces, stress/strain relations, and force estimation. This is extremely difficult to reconcile with the stated TARS contribution, which is supposed to be a unified visuo-tactile affordance framework for manipulation using optical tactile sensors and point clouds. The equations from **Eq. (1) to Eq. (13)** read like a different paper on finite-element force reconstruction for a soft bubble tactile sensor. The mismatch becomes undeniable in the **Conclusion on Page 8**, which states: “We presented a finite element force estimation method for soft-bubble grippers...” That conclusion does not summarize TARS at all. This is not a minor writing issue, it directly undermines confidence that the submitted manuscript is a coherent and accurately presented scientific contribution.

2. **The mathematical presentation is badly underspecified and contains notation/equation problems that prevent verification of the method.**  
   Several equations are malformed or inconsistent:
   - In **Eq. (3), (6), (7), (10), and (11)**, the notation is garbled enough that the intended tensor/matrix shapes are unclear. For example, the expression for $\delta F_{pressure}$ in **Eq. (3)** is not written as a valid matrix expression, and the colon-like separators make the dimensions ambiguous.
   - There are two different equations labeled **(7)**, one on **Page 4** for $\vec{u}_{v,2D}=\text{project}(\vec{u}_v)$ and another on **Page 6** for $F_{ext}=...$, which is a clear numbering inconsistency.
   - **Eq. (4)** mixes indices inconsistently, using $\sigma_j$ and $\sigma_i$ where one would expect $\sigma_{jj}$ and $\sigma_{ii}$.
   - The derivation of **Eq. (11)** from **Eq. (2), (3), and (10)** is not actually shown with enough care to verify correctness.
   - Most importantly, these FEM equations appear unrelated to the policy architecture described later in **Section 3.3**. So even if the math were correct locally, the paper does not explain how this mathematical block is actually integrated into the proposed learning framework.
   
   This matters because the method is not checkable. I cannot tell what is actually optimized, what is simulated, what is learned, and which signals are used at train and test time.

3. **The core learning objective for the policy is missing or incomplete.**  
   In **Section 3.3 on Page 6**, the paper says “The loss function for the VTP module is shown as follows:” but no actual loss equation is properly provided. Instead, the text becomes fragmented prose about a Gaussian mixture density model, with symbols like $\mu_i$, $\Sigma_i$, and mixing coefficients mentioned informally, but without a complete formula. This is a serious omission. For a teacher-student imitation framework with multimodal point-cloud observations, the exact student objective is central. Without it, the proposed learning procedure is not reproducible and not really assessable.

4. **Critical figures and tables referenced in the text are missing, which makes the paper’s claims impossible to verify from the main paper.**  
   The manuscript repeatedly refers to **Fig. 3**, **Fig. 4**, **Fig. 5**, and **Tab. I, Tab. II, Tab. III**, but these are not present in the provided main paper. This is not cosmetic. The missing content includes:
   - **Fig. 3**, which is supposed to explain tactile information decomposition.
   - **Fig. 4**, which is supposed to show the entire VTP/TARS framework.
   - **Fig. 5**, which is supposed to describe the tasks.
   - **Tab. I**, the main baseline comparison.
   - **Tab. II**, the object generalization study.
   - **Tab. III**, the training-stage comparison across modalities.
   
   Because the paper’s main empirical claims in **Section 4.3** are all tied to these missing tables, the evidence is effectively absent from the main submission. For example, the authors state that “the comparison results, as shown in Tab. I, demonstrate that our method... achieves the best overall performance,” but the reader cannot inspect the actual numbers, variances, or task-by-task margins. Likewise, the object generalization and training-dynamics arguments hinge entirely on **Tab. II** and **Tab. III**, neither of which is available. This is a major problem for scientific review.

5. **The experimental evidence is described only at a narrative level, with insufficient quantitative detail even aside from the missing tables.**  
   In **Section 4**, the paper claims “extensive experiments” and robustness under various conditions, but the main text does not provide actual success rates, standard deviations, confidence intervals, number of seeds, episode budgets, or clear protocol details. Since **Tab. I–III** are missing, the reader is left with only qualitative claims like “significant improvement,” “strong generalization ability,” and “best overall performance.” At ICLR level, especially for RL and robotics, this is not enough. Quantitative evidence is not optional here, it is the basis for judging whether the claimed gains are meaningful or statistically credible.

6. **The baseline setup is not convincing enough, and fair comparison is hard to assess.**  
   The baselines in **Section 4.2** are described only briefly. RS, VA, and PN+MLP are named, but the implementation details are too vague to evaluate fairness. For instance:
   - Are all methods using the same point count, encoder capacity, and training budget?
   - Does VA have access to the same tactile information at training and deployment?
   - How exactly is the “visual-tactile classification one-hot encoding” constructed, and is it equally available to all baselines?
   - Why is the end-to-end affordance baseline omitted entirely because it “did not converge,” without any quantitative trace or training diagnostics?
   
   This matters because an integrated multimodal system can easily benefit from hidden implementation advantages. The current text does not rule that out.

7. **The paper overstates novelty relative to prior robot synesthesia work, while not clearly isolating what is genuinely new.**  
   On **Page 2**, the paper claims “we are the first to apply these concepts to a robotic system using optical tactile sensors and external cameras.” Given that the paper itself cites prior work on robot synesthesia, point-cloud-based visual-tactile coordination, and visual-tactile affordance, that claim needs much more precise qualification. As written, the distinction from prior visuo-tactile point-cloud fusion work is blurry. Is the novelty the use of affordance supervision, the handling of non-contact states, the optical tactile sensing setup, the teacher-student RL framework, or the particular feature encoding? The manuscript gestures at all of these, but never cleanly separates “what existed before” from “what this paper adds.” This makes the contribution feel more incremental than the introduction suggests.

8. **The presentation quality is poor enough to obstruct understanding of the main contribution.**  
   This is not just about grammar. There are repeated formatting issues, broken prose, and copy-editing problems that affect content:
   - Section numbering mixes styles, for example “## 6 TACTILE AFFORDANCE...” and “## 7 INTRODUCTION”.
   - **Figure 2** is effectively unusable in the provided manuscript. The embedded image appears as a placeholder rather than a meaningful FEM illustration, while the text says “Refer to Figure 2” for core geometric definitions. This weakens the already hard-to-follow derivation.
   - The phrase “visualtactile” appears multiple times without spacing.
   - Several sentences in **Section 3.3** are fragmented or missing symbols.
   
   These issues matter because the paper is already methodologically complex. When the writing and notation are this unstable, the burden on the reader becomes unreasonable.

9. **The claimed sim-to-real story is not substantiated in the main paper.**  
   The abstract and introduction mention real-world tests and deployment, and **Section 3.1** discusses using real tactile images to predict six-dimensional contact forces. However, the main paper does not provide a dedicated real-world evaluation section, concrete metrics, or visual evidence of transfer performance. If the claim is only that deployment was “successful,” that is too vague. Given that sim-to-real is presented as a central motivation, this omission significantly weakens the paper.

10. **There is a serious mismatch between the stated problem and the actual technical content.**  
   The paper advertises a unified affordance-policy framework for multimodal manipulation, but the technical depth is concentrated in a bubble/FEM force-estimation derivation that is neither well integrated nor empirically validated in the visible experiments. Conversely, the actual affordance learning and policy learning pieces, which should be the core ML contribution, are precisely the parts that are least specified. That imbalance makes it very difficult to evaluate the paper as a machine learning contribution rather than a partially assembled robotics systems draft.

## Questions
1. The biggest issue is the manuscript’s internal consistency. Can the authors clarify whether **Section 3.2 and the Conclusion** are from the intended paper version? In particular, how does the FEM-based bubble/membrane model connect to TARS’s visual-tactile affordance learning and point-cloud policy pipeline?

2. Please provide the **complete VTP training objective** in mathematical form. What is the exact loss minimized by the student, how is the Gaussian mixture density parameterized, and how is DAgger integrated with the replay buffer during training?

3. Please include the missing **Tab. I, Tab. II, Tab. III** and **Fig. 3, Fig. 4, Fig. 5** in the main paper. Without them, the empirical claims are not reviewable. For the tables specifically, I would want per-task success rates, variance across seeds, number of evaluation episodes, and ideally significance testing or at least confidence intervals.

4. For the baseline comparison in **Section 4.2**, please clarify whether all methods use the same encoder capacity, same number of input points, same training budget, same privileged information during teacher training, and same student supervision budget. This is necessary to assess fairness.

5. For the affordance module, what are the labels or targets used to train VTA? Are affordance values obtained from teacher rollouts, contact events, successful grasp points, or another procedure? The paper currently does not define the supervision signal clearly enough.

6. Can the authors provide a clean ablation isolating the effect of:
   - unified point-cloud representation,
   - tactile points themselves,
   - visual-tactile one-hot modality encoding,
   - affordance prediction,
   - teacher-student imitation,
   - GMM action head?
   
   Right now, these ingredients are bundled together.

7. The paper claims robustness to varying point-cloud scales and some degree of object transfer in the Lift task. Please clarify the exact train/test object split, whether test objects are unseen geometries, and whether the transfer results hold beyond the six “somewhat similar” objects mentioned in **Section 4.3**.

8. Since **Figure 1** frames the method around transitions between contact and non-contact states, can the authors report failure cases separately in those two regimes? For example, what happens when tactile input is absent longer than expected, or when visual occlusion persists after contact?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns identified from the content provided. The work is a robotics manipulation paper and does not present clear issues around privacy, human subjects, or sensitive deployment in the main text.

## Soundness Rating
1: poor. The main claims are not adequately supported in the visible manuscript because the method description is internally inconsistent, key equations and losses are incomplete, and the central empirical tables/figures are missing.

## Presentation Rating
1: poor. The manuscript has severe clarity and formatting issues, including mismatched conclusion content, broken notation, duplicate equation numbering, and missing referenced figures/tables.

## Contribution Rating
2: fair. The underlying problem is relevant and the intended idea of unified visuo-tactile affordance-based manipulation is potentially useful, but the paper does not present the contribution cleanly or convincingly enough in its current form.

## Overall Rating
2: Reject, not good enough. The topic is relevant and the high-level idea is interesting, but the submission in its current form has too many core issues, especially the internal mismatch between sections, missing empirical evidence in the main paper, and insufficiently specified methodology.

## Reviewer Confidence
4: confident. I am confident in this assessment because the main concerns arise directly from the paper text itself, including visible inconsistencies in equations, sections, figures, and results presentation.