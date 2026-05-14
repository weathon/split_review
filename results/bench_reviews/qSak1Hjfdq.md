Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper formalizes the All-Day Multi-Scenes Lifelong VLN (AML-VLN) problem, where an embodied agent must continually adapt to a sequence of navigation scenarios spanning multiple scenes and illumination conditions (normal, low-light, overexposure, scattering) without catastrophic forgetting. The core contribution is Tucker Adaptation (TuKA), which lifts parameter-efficient adaptation from 2D matrix space into a high-order tensor and uses Tucker decomposition to decouple shared navigation knowledge from scene-specific and environment-specific expert knowledge. A Decoupled Knowledge Incremental Learning (DKIL) strategy consolidates shared subspaces via EWC while constraining experts through consistency and orthogonality losses. The resulting agent, AlldayWalker, is evaluated on a custom 24-task benchmark built on an extended Habitat simulator.

## Strengths

- **Genuinely novel architectural contribution**: The use of Tucker decomposition to factorize multi-hierarchical navigation knowledge (shared core × scene experts × environment experts) within a high-order tensor, and the tensor-to-matrix alignment in Eq. 3, is a creative and technically sound extension beyond the LoRA / MoE-LoRA family. The ABC-LoRA ablation (Appendix I, Table 15) is particularly convincing: a hierarchical matrix baseline using the same DKIL losses achieves only 55% SR vs. TuKA's 65% SR, isolating the tensor representation as the differentiating factor.

- **Strong empirical results with large margins**: On the 24-task AML-VLN benchmark, AlldayWalker achieves 65% average SR vs. 56% for the best baseline (SD-LoRA) and reduces forgetting (F-SR) from 18% to 11% (Tables 1–2). These margins are substantial and consistent across all six reported metrics (SR, SPL, OSR and their forgetting rates). The method also generalizes to unseen scene-environment combinations (Table 5: 55% SR vs. 39–40% for baselines).

- **Thorough ablation design**: The paper includes meaningful ablations that test core claims: third-order vs. fourth-order tensor (SR 54% vs. 65%), shared component removal (Table 3), rank scaling (Appendix G), and scalability to 30 tasks (Table 4). The ABC-LoRA comparison (Appendix I) directly tests whether the tensor decomposition provides gains beyond a matrix-based hierarchy, which is the strongest evidence for the paper's central claim.

- **Well-constructed benchmark with physically grounded degradation**: The Allday-Habitat platform extends Habitat with three imaging degradation models (atmospheric scattering, low-light with noise, overexposure with saturation) based on realistic physical models (§4, Appendix E). This provides a principled testbed for all-day navigation that goes beyond simple brightness adjustments.

## Weaknesses

### Fatal

None.

### Major

None that threaten the core claims.

### Minor

- **Single task-ordering run without statistical characterization**: The entire evaluation uses one randomized task order with no repetition across different random seeds. While this is common practice in lifelong VLN benchmarks (the comparable Uni-Walker paper accepted at ICLR with avg score 6.0 also uses single-run evaluation), and while the large performance margins (9 percentage points SR, 7 points F-SR) reduce the likelihood that the result is an artifact of ordering, reporting variance across at least 3 random task orders would strengthen confidence in the results. Given the computational cost of 24-task runs on 7B-parameter models, this is a minor limitation rather than a fatal flaw.

- **Slight overstatement of real-world validation**: The abstract claims "additional real-world deployments also validate the superiority of our AlldayWalker." The main paper does include quantitative results on real-world scenes (T21–T24 in Table 1), but these are captured real scenes rendered within Habitat, not physical robot deployments. The appendix describes a robotic platform (Figure 9) but provides no quantitative physical-world navigation results. The claim in the abstract should be softened to match what was actually evaluated, or the physical robot results should be included.

### Trivial

- The expert retrieval mechanism (§3.4) selects scene and environment experts independently via CLIP feature matching. While the generalization results in Table 5 show this works well empirically, a brief analysis of retrieval accuracy (e.g., what fraction of episodes selects the correct expert) would be informative but is not essential to validating the core contribution.

## Nice-to-Haves

- Sensitivity analysis of the DKIL loss weights (λ₁, λ₂, λ₃) to clarify whether all three terms are necessary and whether they interact in conflicting ways.
- Trajectory visualizations comparing AlldayWalker with SD-LoRA on the same episodes to qualitatively illustrate where knowledge retention makes a difference.
- Analysis of retrieval accuracy for scene/environment expert matching during inference.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No statistical significance or multiple runs are reported" as a fatal issue**: While the paper does use a single task order, this is standard practice in lifelong VLN research. The comparable accepted paper Uni-Walker (avg 6.0) was not criticized for this. The large performance margins and the fact that all baselines share the same ordering further mitigate this concern. Kept as a minor weakness rather than a fatal one.

- **"No quantitative real-world navigation results in the main paper"**: Factually incorrect. Table 1 includes tasks T21–T24 (real-world 1 and 2) with quantitative SR results. The real concern is about physical robot deployment vs. simulated real-world scenes, which is addressed in the Minor weaknesses section.

- **"Tables are hard to parse because of OCR artifacts and missing formatting"**: These are parser artifacts from PDF extraction. The original submission does not have these issues (Hard Rule).

- **"The claim that matrix-based representation is inherently limited... is stronger than the experiments can fully substantiate"**: The ABC-LoRA ablation (Appendix I, Table 15) directly tests this: a hierarchical matrix baseline with identical DKIL losses achieves 55% SR vs. TuKA's 65% SR, providing strong evidence for the tensor representation claim.

- **"Task-id agnostic claim contradicted by expert retrieval"**: The paper explicitly states that task-id is not given during testing but the agent infers scene/environment via CLIP-based retrieval (§3.4). This is a reasonable design, not a contradiction.

- **Strength Finder's generic strengths**: Removed generic claims about "addressing an important problem" that lacked specific citations or concrete evidence.

## Novel Insights

The paper's most novel insight is that Tucker decomposition can serve as a principled bridge between high-order tensor representations (which naturally capture multi-hierarchical knowledge like scene × environment interactions) and the 2D matrix backbone of LLM adapters. The tensor-matrix alignment in Eq. 3 — extracting specific expert rows and contracting with the core tensor and encoder/decoder factors to produce a standard 2D weight update — is elegant. The ABC-LoRA experiment demonstrates that this is not merely an architectural curiosity: the tensor core enables parameter sharing across joint scene–environment combinations that a hierarchical matrix factorization cannot capture, yielding a ~10 percentage point SR improvement under identical continual learning constraints.

## Suggestions

- Soften the abstract's "real-world deployments" claim to "real-world scenes" or include quantitative results from the physical robot platform described in the appendix.
- If computationally feasible, add a note about variance observed across a small number of additional runs (even 2–3 task orders for the main result) to address the single-run concern, or explicitly discuss why single-run evaluation is standard and sufficient in this setting.
- Add a brief discussion of retrieval accuracy for the scene/environment expert matching in §3.4.

---

**Calibration anchors used:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/PaYo96rjij.md` | 6.00 | Uni-Walker: most directly comparable (lifelong VLN, LoRA-based, 18 tasks). AlldayWalker is methodologically more novel (Tucker decomposition vs. DE-LoRA), has a larger benchmark (24 tasks), and more thorough ablations. Comparable or stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/pFh5ygjN3V.md` | 4.50 | M³E: continual VLN with MoE, smaller evaluation scope, less novel method. AlldayWalker is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/pZj2DhfaVD.md` | 6.00 | EWC-LoRA: revisits weight regularization for LoRA CL. Different problem (class-incremental vs. lifelong VLN). AlldayWalker has greater novelty and scope. |
| `/home/wg25r/review_agent/human_reviews_2026/Wm1SjTIjvA.md` | 3.00 | PS-LoRA: rejected for incremental contribution. AlldayWalker is substantially stronger on all dimensions. |
| `/home/wg25r/review_agent/human_reviews_2026/0za6569Jqd.md` | 2.00 | CoRe: rejected as too incremental. Not comparable — AlldayWalker is far stronger. |

The paper compares favorably to Uni-Walker (6.00), which was accepted as a poster with unanimous 6s and addresses a similar lifelong VLN problem. AlldayWalker's Tucker decomposition is more novel than Uni-Walker's DE-LoRA, its benchmark is larger, its ablations are more rigorous (especially the ABC-LoRA comparison), and its results show comparable or larger margins over baselines. The only real weakness relative to Uni-Walker is the single-run evaluation, which Uni-Walker also shares and was not criticized for.

**Originality**: High — Tucker decomposition applied to multi-hierarchical knowledge in lifelong VLN is genuinely novel.
**Importance**: High — all-day, multi-scene navigation is a practical challenge for real-world deployment.
**Claims supported**: Well supported by comprehensive experiments and ablations.
**Soundness**: Sound methodology; single-run evaluation is a minor limitation given community norms.
**Clarity**: Well-structured paper with clear motivation and method description.
**Value to community**: The benchmark and TuKA method provide a strong foundation for future work in lifelong VLN.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>