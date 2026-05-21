---
job_id: 1030ab41-db94-43a0-ad95-a4309e24bc14
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Vgm77U4ojX.pdf
paper: SigmaDock: Untwisting Molecular Docking With Fragment-Based SE(3) Diffusion
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope through generative modeling, diffusion on manifolds, equivariant learning on geometric structures, and application to molecular biology/drug discovery.

## Minimum Quality
Pass ✅. The submission includes all core components expected of a research paper, namely abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion, and it provides substantial technical and empirical content without any obvious fatal flaw that would warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, reviewer-directed instructions, or other manipulative content in the paper text.

# Expected Review Outcome:
## Summary
This paper proposes SigmaDock, a molecular docking method that decomposes ligands into rigid fragments and performs generative pose prediction by diffusion over \(\mathrm{SE}(3)^m\), where each fragment is assigned an independent rigid-body transformation. The method combines a fragmentation scheme (FR3D), soft triangulation-based geometric conditioning, and an \(\mathrm{SO}(3)\)-equivariant architecture built on EquiformerV2, and is evaluated primarily on PoseBusters and Astex in rigid-receptor re-docking. The paper reports strong empirical performance, including high PB-valid Top-1 success on PoseBusters and favorable generalization to unseen proteins.

## Strengths
1. The paper tackles an important and timely problem. Molecular docking is a high-value application area for geometric generative modeling, and the authors are clearly trying to address a real weakness of prior deep docking work, namely the gap between RMSD-only success and chemically valid pose generation. That focus on PB-validity is appropriate and scientifically meaningful.

2. The central design choice, moving from torsion-space diffusion to rigid-fragment \(\mathrm{SE}(3)^m\) diffusion, is well motivated. The discussion in Section 2.2.2 is one of the stronger conceptual parts of the paper. Even if some claims are stated more strongly than the evidence fully supports, the underlying intuition is sensible: torsional perturbations induce awkward nonlocal Cartesian effects, while fragment-wise rigid motions align better with the geometry the model actually sees.

3. The method is more than just “apply existing SE(3) diffusion to docking.” The paper contributes a full package: FR3D fragmentation, dummy-atom handling, triangulation conditioning, a specific equivariant architecture, and a sampling/ranking strategy. This is a coherent system contribution rather than a thin wrapper around prior diffusion machinery.

4. The empirical results are strong and, importantly, are reported using a more demanding notion of success than plain RMSD. In **Figure 4** and **Table 1**, SigmaDock substantially improves PB-valid Top-1 over prior open-source generative baselines on the intended split, and the gap is large enough that it is difficult to dismiss as noise or implementation luck. The paper is also appropriately explicit that it uses rigid-receptor re-docking and known pockets.

5. The ablation study is useful and better than what many docking papers provide. **Table 1** gives reasonably direct evidence that triangulation conditioning, protein-ligand interaction edges, fragmentation merging, and ranking heuristics each matter. In particular, removing triangulation conditioning hurts PB-valid Top-1 from \(79.9\%\) to \(67.1\%\), which supports the claim that the geometric priors are doing real work rather than being decorative additions.

6. The paper includes several figures that genuinely help understand the method. **Figure 1** is an effective high-level illustration of the fragment-based forward and reverse process, and **Figure 3** makes the FR3D reduction idea much easier to follow than the text alone. **Figure 9** is also useful because it clarifies the somewhat complicated graph construction, especially the distinction between fragment atoms, virtual nodes, and triangulation edges.

7. The generalization analysis is a strong point. The sequence-similarity breakdown in the right panel of **Figure 4** is directly relevant to the paper’s anti-memorization narrative, and the results are materially better than what one typically sees from docking models that quietly rely on train-test similarity.

8. The paper makes a genuine effort on symmetry and geometric consistency. The orientation-invariance issue for local fragment frames is real, not cosmetic, and the use of a pseudo-force / Newton-Euler prediction head is a thoughtful way to address it. Theorem 2 is therefore targeting an important modeling subtlety.

9. The authors provide enough implementation detail in the main paper that the work does not read like a black-box benchmark submission. The training/inference sections, equations for the diffusion process, and architectural choices are concrete enough to make the submission assessable.

## Weaknesses
1. The paper’s theoretical positioning is somewhat overconfident relative to what is actually established in the main paper. The strongest example is **Theorem 1** in Section 2.2.2, which is used rhetorically to support the claim that torsional models are inherently entangled whereas fragment models enjoy a factorized product structure. In the appendix, this argument is basically a Jacobian / Gram-matrix observation for a chosen parameterization. That does support geometric coupling, but it does not by itself show that learning in torsion space is intrinsically worse in the optimization or statistical sense claimed in the main text, such as “ill-conditioned learning problem” or “stiff sampling dynamics.” Those are stronger consequences than what is formally shown. This matters because a large part of the paper’s novelty story is framed as a principled rebuttal to torsional methods. I would strongly encourage the authors to tone down the “fundamental caveat” language and distinguish clearly between proved statements about induced measures and more empirical hypotheses about trainability.

2. Relatedly, the comparison between torsional and fragment parameterizations is not entirely apples-to-apples from a degrees-of-freedom perspective. Section 2.2.3 argues that FR3D plus triangulation narrows the effective DoF gap versus torsional models, but in the main paper this remains somewhat slippery. The text alternates between raw parameter count, hard-constraint manifold dimension, and soft-conditioning intuition. In particular, the statement around Page 6 that the effective DoFs “concentrate between \(k+6\) and \(6m\)” depends on assumptions about triangulation rank and tree-like fragment graphs that are not developed in the main paper. This matters because the paper repeatedly frames FR3D as reducing the mismatch introduced by naive fragmentation. As written, the exact source of the practical gain is still ambiguous: fewer fragments, better priors, easier denoising, or simply more favorable architecture inputs.

3. There are places where the mathematics or notation is underspecified enough to obstruct careful verification. A concrete example is **Equation (3)**, the score-matching loss. The paper writes
\[
\mathcal{L}(\theta)=\mathbb{E}\left[\left\| s_\theta(\mathbf{Z}^{(t)},t,\mathcal{G}_{\text{dock}})-\nabla_z \log p_{t|0}(\mathbf{Z}^{(t)}|\mathbf{Z}^{(0)}) \right\|^2_{\mathrm{SE}(3)^m}\right],
\]
but the main text does not specify the weighting between translation and rotation losses, even though Appendix C later introduces separate scaling factors \(\lambda_t^p\) and \(\lambda_t^R\). Since balancing Euclidean and rotational score terms is a key implementation issue in SE(3) diffusion, this is not a minor omission. Similarly, **Equation (1)** uses a simplified SDE with unit noise scales, but the actual implementation uses time-dependent \(\beta(t)\) and \(g(t)\) in Appendix C. That is acceptable for exposition, but the main paper leans rather heavily on “careful and rigorous design,” so the distinction between pedagogical and actual objective should be more explicit.

4. The translation prediction head in Appendix G.4 appears inconsistent with the standard VP score form as written. The paper defines
\[
\mathbf{s}_\theta^p=\frac{1}{\sqrt{1-\alpha_t}}\cdot \frac{1}{|\mathcal{G}_F|}\mathbf{F}_F,
\]
whereas for a VP kernel with variance \(1-\alpha_t^2\), the usual \(\epsilon\)-prediction-to-score conversion scales with \(1/\sqrt{1-\alpha_t^2}\), not \(1/\sqrt{1-\alpha_t}\). This may be a notation issue, an omitted square, or a deliberate reparameterization, but as written it is suspicious and should be clarified. Because the method’s core object is a score field on \(\mathrm{SE}(3)^m\), ambiguities in score parameterization are more serious than ordinary presentation glitches.

5. The empirical comparison is impressive, but the baseline section is not as airtight as the bold claims would require. **Figure 4** compares against a mixture of classical methods, open-source deep learning methods, and non-open models with numbers “extracted from” prior papers. The paper also compares to AF3 in **Table 4**, but the formatting and interpretation of that table are confusing. The table appears to mix per-bucket counts and performance values from two methods into three columns, making it difficult to parse without cross-referencing the surrounding text. For a paper making strong claims like “first deep learning approach to surpass classical physics-based docking under the PB train-test split,” cleaner and more direct benchmark tables in the main paper would help a lot.

6. Some of the empirical claims overshoot what the experiments strictly validate. For example, the paper repeatedly uses language such as “theoretically-grounded \(\mathrm{SE}(3)^m\) Riemannian diffusion framework with strong generalisation” and “substantially outperform previous generative methods on the re-docking task” as evidence that the method learns more general physicochemical correlations. The re-docking setting with known holo receptor and known pocket is still a simplified regime. The authors are transparent about that, which is good, but the prose sometimes drifts toward broader conclusions about docking reliability than the evaluation setting supports. This matters because many practical failures in docking come from receptor flexibility, pocket ambiguity, or cofactor effects, and **Table 2** itself shows the method degrades substantially in cofactor-influenced settings.

7. The method relies on several choices that are likely important in practice, but the main paper leaves them underexplained. FR3D uses a stochastic search over valid merge states, then samples a cut set uniformly from the valid set. That is an interesting augmentation idea, but it raises natural questions: how large is \(\mathcal{S}\) in practice, how sensitive is performance to the randomness, and how expensive is recursion for flexible ligands? **Figure 3** illustrates two alternative reductions, which is useful, but the main text never really quantifies fragmentation variance at train and test time or whether inference-time fragmentation randomness contributes to output variance. Since fragmentation is a defining ingredient of the method, robustness to this preprocessing choice should be better characterized in the main paper.

8. The alignment-based construction of training conformers could use a more careful discussion in the main paper. Section 2.2.1 argues, based on alignment of ETKDG conformers to the bound state, that variability in bond lengths and angles can be “generally ignored.” That is plausible for many ligands, but the evidence for this claim is pushed to the appendix. In the main paper, **Figure 2b** shows one successful aligned example and **Figure 2c** gives qualitative conformer ensembles, but the actual aggregate statistics supporting the approximation are not shown there. Because this assumption underlies the whole fragment-template approach, I think the main paper should contain at least one concise summary statistic or histogram, not just a qualitative example.

9. The architecture section contains several claims that sound reasonable but are not always fully substantiated. In Section 2.4, the authors state that virtual nodes and hierarchical topology reduce over-squashing and mitigate over-smoothing, and that smooth edge decay prevents instabilities from topology changes. These are plausible design heuristics, but the main paper does not isolate them experimentally. **Figure 9** helps visualize the graph design, but there is no ablation separating virtual-node hierarchy from other architectural modifications. Given how much architectural complexity has been introduced on top of the core diffusion idea, some of the performance gain could simply come from this richer graph construction rather than from the fragment-space formulation itself.

10. Table-level presentation needs cleanup. **Table 1** includes a row “Sampling from Mh,” presumably \(\mathcal{M}_b\) or \(\mathcal{M}_c\), but the notation in the rendered table is unclear. Likewise, “\(N_{\text{web}}\)” appears where one would expect \(N_{\text{seeds}}\). These are not deep scientific flaws, but they do matter because this table is central to understanding the ablations. **Table 3** also has formatting issues in the header and metric rows. The paper is readable overall, but these details make some quantitative results look less polished than they should.

11. The comparison to AF3 is interesting but somewhat awkwardly handled. **Table 4** and Appendix J.2 emphasize lower leakage and comparable average performance, but the paper also notes that the tasks are not directly comparable and that AF3 is a co-folding model. That caveat is correct, yet the narrative still leans heavily on AF3-level performance as a selling point. I would prefer a more restrained presentation here. The method does not need that comparison to stand on its own; the PoseBusters and Astex results are already strong.

12. There is a narrowness to the evaluation protocol that reduces the breadth of the contribution for ICLR. The paper is entirely about rigid-receptor re-docking with a provided pocket region. This is a valid and standard benchmark setup, but it is also the easiest docking regime among the practically relevant ones. The authors acknowledge this in Section 4 and Appendix J, which I appreciate. Still, it keeps the contribution from feeling fully decisive. A method can be excellent in this setup and still face serious obstacles in flexible docking, cross-docking, or blind docking.

## Questions
1. Please clarify the exact training loss used in practice. In the main text, **Equation (3)** gives a unified score-matching objective on \(\mathrm{SE}(3)^m\), but Appendix C introduces separate time-dependent scaling factors \(\lambda_t^p\) and \(\lambda_t^R\). What is the exact implemented loss, written explicitly? This would materially increase my confidence in the method’s soundness.

2. In Appendix G.4, why is the translation score scaled by \(1/\sqrt{1-\alpha_t}\) rather than \(1/\sqrt{1-\alpha_t^2}\)? If this is a notation convention, please make it explicit. If it is intentional, please explain the derivation. This point is important because it touches the correctness of the score parameterization itself.

3. Can the authors provide more quantitative evidence, in the main paper or rebuttal, on fragmentation sensitivity? For example, if FR3D samples different valid reductions for the same ligand, how much does downstream PB-valid Top-1 vary? A small robustness study here would help distinguish “good idea” from “good with lucky preprocessing.”

4. For the claim that fragment-space diffusion is better conditioned than torsional diffusion, can the authors sharpen what is theorem-backed versus what is empirical intuition? A crisper separation between formal geometric statements and optimization hypotheses would improve the scientific precision of the paper.

5. How much of the gain comes from the fragment-space representation versus the architecture and reranking heuristic? **Table 1** is useful, but I would like a stronger decomposition, especially isolating the contribution of the EquiformerV2 modifications and the sample-ranking strategy. If these are available, they would strengthen the causal story behind the improvement.

6. Please clarify the benchmark tables, especially **Table 4**. The current layout is hard to parse. A cleaner presentation of per-bucket performance for SigmaDock and AF3, with explicit column labels, would help.

7. The paper argues that aligned ETKDG conformers are close enough to the bound manifold that variations in bond lengths and angles can be neglected. Could the authors report a compact aggregate statistic directly in the main paper, for example median / 90th percentile alignment RMSD over the relevant training or validation set? This would support a central modeling assumption more convincingly.

8. Since **Table 2** shows a clear degradation in cofactor-related cases, do the authors have any evidence on whether the failure is mostly due to missing pocket geometry, missing electrostatics, or ranking failures among generated samples? That diagnosis would help assess how extensible the method is.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The work focuses on methodological advances in molecular docking using public structural datasets and does not raise an ethics issue that requires special review based on the information in the paper. Like most work in drug discovery, it could eventually be used in dual-use contexts, but the paper itself does not introduce a distinct ethics concern beyond standard scientific use.

## Soundness Rating
3: good. The method is technically substantial and the empirical evidence is strong, but there are several mathematical and experimental presentation points that need clarification, especially around the exact implemented loss, score parameterization, and the scope of theoretical claims.

## Presentation Rating
3: good. The paper is generally readable and well structured, and several figures are genuinely helpful, but some tables are confusingly formatted and a few central claims would benefit from more careful calibration and explicit definitions in the main text.

## Contribution Rating
4: excellent. Despite the caveats, this is a meaningful contribution to geometric generative modeling for docking. The fragment-based \(\mathrm{SE}(3)^m\) framing, the integration of chemical priors, and the empirical gains on a challenging benchmark make the paper valuable to the ICLR community.

## Overall Rating
8: Accept, good paper (poster). This is a strong paper with a clear empirical advance and a coherent methodological contribution. I do have reservations about how aggressively some theoretical claims are framed and about a few unresolved mathematical / presentation issues, but the strengths comfortably outweigh the weaknesses.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the technical sections with care, though some implementation-specific details remain unclear from the main paper and would benefit from author clarification.