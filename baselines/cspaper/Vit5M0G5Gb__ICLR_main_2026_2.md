---
job_id: e3a3df54-0c36-4b5b-be44-9d0214d9b11e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Vit5M0G5Gb.pdf
paper: Saddle-to-Saddle Dynamics Explains a Simplicity Bias Across Neural Network Architectures
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in scope for ICLR, it studies learning dynamics, non-convex optimization, implicit bias, and representation complexity across several neural architectures.

## Minimum Quality
Pass ✅. The paper contains the expected core components, including abstract, introduction, related-work discussion, methodology/theory, empirical validation, and discussion, and it presents a substantive theoretical contribution with supporting experiments rather than a trivial extension or an incomplete technical report.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or manipulative text in the provided paper content or figure material.

# Expected Review Outcome:
## Summary
This paper proposes a unified framework for dynamical simplicity bias in neural networks, centered on saddle-to-saddle learning dynamics. The authors show, for a broad class of architectures covered by their layer formulation in Equation (1), that fixed points of narrower networks can be embedded as fixed points of wider networks, and that corresponding invariant manifolds constrain the network to behave as if it had fewer effective units. They then analyze two concrete mechanisms for stage-like learning in two-layer models, data-induced timescale separation in linear cases and initialization-induced timescale separation in quadratic cases, and use these analyses to explain plateau-and-jump training dynamics across linear, ReLU, convolutional, quadratic, and attention-based examples.

## Strengths
1. The paper has a genuinely ambitious scope, and unlike many papers that advertise “unified” views while really giving a loose analogy, this one does provide a common structural language across multiple architectures. The combination of embedded fixed points in **Theorem 1**, invariant manifolds in **Theorem 3**, and architecture-specific timescale-separation arguments in **Section 5** gives the work a coherent backbone.

2. The fixed-point and invariant-manifold results are conceptually strong. In particular, the move from fixed-point embeddings in **Equations (4) to (7)** to dynamical constraints in **Section 4** is one of the more compelling parts of the paper. The authors are not just cataloguing stationary points; they are trying to explain why trajectories should spend time near functionally simpler subnetworks.

3. I appreciated that the paper distinguishes two mechanisms rather than forcing everything into one story. The contrast between the linear case, where the separation is across data directions via the singular structure of $\Sigma_{yz}$ in **Theorem 4**, and the quadratic case, where the separation is across units via initialization in **Proposition 5**, is a meaningful insight. That distinction also helps explain why different architectures in **Figure 1B-G** show different weight structures during plateaus.

4. **Figure 1** is effective and important, not just decorative. Panel A gives a useful cartoon of the proposed mechanism, and panels B-G make the claimed architecture-dependent manifestations concrete. In particular, the bottom-row weight visualizations are helpful for connecting the three fixed-point categories to the formal constructions in **Equations (5), (6), and (7)**. I also appreciated that the authors explicitly tie the visual structures in **Figure 1B,C**, **1D,E**, and **1F,G** to those different cases.

5. The empirical implications in **Figure 2** are reasonably well chosen. Panel A supports the claim that width has very different effects in linear networks versus quadratic-like attention models; panel B tests the role of spectral gaps; panels C and D probe initialization structure and scale. This is the kind of figure that at least tries to move beyond “here are some pretty plateaus” to “here are predictions implied by the theory.”

6. The MNIST experiment in the appendix is more informative than many theory papers’ token real-data section. In **Figure 3** and **Table 1**, the connection between plateau duration and the singular values of the data statistics is at least directionally consistent with the theory. The table is especially useful because it operationalizes the otherwise abstract discussion of what controls plateau lengths.

7. The paper is generally well organized. The narrative from general structural results to concrete dynamics to implications is easy to follow, and the authors are better than average at telling the reader which statements are rigorous, which are heuristic, and which are conjectural.

## Weaknesses
1. The main conceptual claim, that this is a broad explanatory framework for simplicity bias across architectures, is stronger than what is actually established in the paper. The formally analyzed dynamics in **Section 5** are restricted to two-layer networks where $\phi(\mathbf{x};\mathbf{u})$ is a homogeneous polynomial in the unit-specific weights, with only the linear and quadratic cases treated in detail. By contrast, some of the headline architectural breadth in the introduction includes deep networks, ReLU networks, convolutional networks, and self-attention more broadly. For several of these, the paper gives either structural results that hold for Equation (1) or empirical illustrations, but not a full dynamical theory. This matters because the central message is not merely “some architectures can have embedded saddles,” but that saddle-to-saddle dynamics explains simplicity bias generally. Right now, the strongest rigorous support is for a narrower slice than the framing suggests.

2. The jump from exact invariant manifolds to actual training trajectories that only evolve “near” them is underdeveloped mathematically. **Theorem 3** states exact invariance under exact equalities or proportionalities. But the observed learning behavior in **Figure 1** and the claims in **Section 5** depend on approximate low-rankness, approximate proportionality, or some units staying much smaller than others. The paper repeatedly uses phrases like “evolves near the invariant manifold” and “closely follow,” yet there is no quantitative perturbation analysis showing how close is close enough, for how long, or under what conditions a trajectory starting off the manifold will remain in its vicinity. This gap is not cosmetic. It is precisely the bridge needed to convert a nice geometric picture into a dynamical theorem rather than a plausible interpretation.

3. The mathematical treatment is uneven in rigor, especially around the dynamics claims. **Theorem 4** is a theorem about the linearized system in **Equation (10)**, not the full nonlinear gradient flow in **Equation (9)**. The paper then uses this to argue for subsequent saddle-to-saddle transitions via the projected dynamics in **Equation (12)**, but that part is explicitly heuristic and pushed to appendix discussion. Likewise, **Proposition 5** concerns the approximate quadratic system in **Equation (14)**, not the full dynamics in **Equation (44)**. In other words, the strongest claims about the full learning trajectories are not really proved, they are inferred from early-time approximations and geometric intuition. That is not illegitimate, but the paper should present the scope of what is actually established more conservatively.

4. There are places where the notation and derivations are sloppy enough to create avoidable confusion. A concrete example is in **Appendix G.2**, where the theorem is stated in the main text using $\Sigma_{yz}$, but the appendix proof introduces the block matrix in **Equation (32)** using $\Sigma_{yx}$. Similarly, in **Lemma 6** on Page 39, the fixed-point condition is written in terms of $\Sigma_{yz}\Sigma_{zz}^{-1}\Sigma_{yz}^{\top}$ and eigenvectors $\mathbf e_k$, but the exposition around how this yields the projected dynamics in **Equations (41) and (42)** is quite compressed. For a paper whose selling point is a unifying mathematical framework, these notation shifts and compressed transitions are more damaging than usual.

5. I am not fully convinced by the treatment of self-attention as fitting into the general layer form. **Equation (2)** is presented mainly as a notational rewrite, and the paper explicitly notes that this is “not a common notation.” That is fair, but the price is that the connection between the abstract $\phi(g_{\text{in}}(\mathbf{x}); \mathbf u_i)\mathbf v_i$ formulation and standard attention parameterization is harder to parse than it should be. Since attention models are a major part of the claimed breadth, the abstraction should be unpacked more carefully in the main text. As written, the attention case feels more asserted than cleanly integrated.

6. The experiments support the intuition but are still fairly limited in scientific stress-testing terms. Most demonstrations are on synthetic setups with tiny input dimension, teacher-generated data, or specially structured tasks, and the deep-network evidence is largely qualitative. **Figure 2** is nice, but it is not a substitute for a more systematic benchmark of whether the theory predicts plateau number, plateau duration, or effective-width transitions quantitatively. The paper claims predictive power regarding data distribution and initialization, yet the validation remains mostly trend-level rather than quantitatively diagnostic.

7. Related to the previous point, the notion of “effective width” is central but not really operationalized as a robust empirical diagnostic outside hand-picked visualizations. In **Figure 1**, one can visually inspect the first-layer weights and agree that one or two effective units are active. In **Figure 3**, singular values provide a clearer proxy for linear/ReLU cases. But the paper does not give a generally applicable metric for detecting effective-width transitions across all architectures it discusses. This matters because the practical usefulness of the framework depends on whether a reader can diagnose these stages in less toy-like settings without manually inspecting scatter plots of 2D weights.

8. **Table 1** is a useful addition, but it also highlights a limitation. The table reports singular values “governing” the first and second plateau for several MNIST digit pairs, and the text says these approximately match the plateau durations in **Figure 3**. However, the paper stops short of a direct quantitative comparison, for example predicted versus observed duration on a common scale, or even a correlation analysis over more tasks. Since one of the paper’s selling points is predictive power, the table reads a bit like suggestive evidence that was not pushed as far as it could have been.

9. Some claims about breadth drift into conjectural territory without strong enough guardrails. For instance, the discussion of higher-order polynomial activations in **Section 5.2** and deep networks in **Section 7** is explicitly speculative, which is fine, but these speculative extensions are placed close to stronger claims and examples. The result is that the paper sometimes feels like it is collecting a theorem, several heuristics, and several conjectures under one umbrella, without always marking the borders sharply enough.

10. There are also some presentation-level issues that should be fixed. On **Page 5**, the sentence “In panels (E,F), the fixed points are described by Equation (5)” appears inconsistent with the earlier pairing in **Figure 1**, since the three categories were introduced as **(B,C)**, **(D,E)**, and **(F,G)**. There are a few typos as well, for example “toward a fix point” in **Page 6**, “the the mechanism” in **Page 6**, and “newtorks” on **Page 10**. None of these are fatal, but in a mathematically dense paper they do not help.

## Questions
1. The paper’s key dynamical step is that trajectories starting near, but not exactly on, the manifolds from **Theorem 3** remain close enough to approach the next embedded saddle. Can the authors make this quantitative in the rebuttal, even if only for one representative architecture? For example, can they state a bound of the form “if the deviation from the manifold is $O(\delta)$ at time $T$, then the trajectory remains within $O(\delta^\alpha)$ for a time interval sufficient to reach a neighborhood of the next saddle”? Even a local statement would materially increase my confidence.

2. For the linear case, the main theorem is about the approximate early-time system in **Equation (10)**. Can the authors clarify more explicitly what is rigorously known for the full nonlinear system in **Equation (9)** beyond the first transition? In particular, what part of the multi-stage picture is theorem-level versus heuristic extrapolation from **Equations (12), (41), and (42)**?

3. For the quadratic case, **Proposition 5** requires $\Sigma_{yZ}$ to be symmetric and to have both positive and negative eigenvalues. How essential are these assumptions for the claimed unit-wise timescale separation? Are there natural attention or quadratic examples in the paper’s scope where one of these assumptions fails, and if so, what behavior should we expect there?

4. The attention abstraction in **Equation (2)** is doing a lot of work. Could the authors add a more explicit mapping between the standard attention-head parameters and the $(\mathbf u_i,\mathbf v_i)$ decomposition used throughout? Right now the claim that self-attention is naturally covered by Equation (1) is plausible, but not especially transparent.

5. Can the authors provide a more operational empirical definition of “effective width” that applies beyond the 2D toy visualizations? For instance, for ReLU, convolutional, and attention models, what statistic should one compute during training to test the theory automatically rather than by manual inspection of weight clouds as in **Figure 1** and **Figure 5**?

6. **Figure 2B** and **Table 1** both suggest that spectral gaps control plateau lengths. Could the authors provide a more quantitative test of this claim, even a simple regression or scaling plot over many synthetic tasks? That would strengthen the “predictive power” claim considerably.

7. In **Figure 2A**, increasing width has “little effect” in linear networks but clearly shortens plateaus in linear self-attention. Can the authors comment on whether this difference remains after matching parameter count or initialization statistics more carefully across architectures? This would help separate architectural mechanism from raw scaling effects.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns identified from the paper content. The work is theoretical and uses standard synthetic and MNIST-based experiments, with no apparent privacy, fairness, legal, or human-subject issues.

## Soundness Rating
3: good. The paper contains meaningful theoretical results and the central intuition is supported by analysis and experiments, but some of the strongest dynamical claims rely on approximations and heuristic extensions beyond what is fully proved in the main text.

## Presentation Rating
3: good. The paper is generally well written and well structured, with effective figures, but some notation shifts, compressed derivations, and a few inconsistencies/typos reduce clarity.

## Contribution Rating
4: excellent. The paper makes a substantial contribution by connecting embedded fixed points, invariant manifolds, and stage-like learning dynamics into a unified perspective spanning several architectures, even if some parts of the generality are more suggestive than fully nailed down.

## Overall Rating
8: Accept, good paper (poster). This is a strong theory paper with a real organizing idea, useful structural results, and good empirical support for its main intuitions. I do not think every broad claim is equally well established, and I would like a sharper separation between theorem, heuristic, and conjecture, but the contribution is still clear and valuable for the ICLR community.

## Reviewer Confidence
4: confident. I am confident in this assessment and checked the main mathematical and empirical components with care, though some architecture-specific technical details, especially for the attention formulation, could still hide nuances.