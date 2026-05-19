Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

---

## Summary

This paper proposes MutualNeRF, a framework that uses mutual information (MI) theory to improve NeRF under limited samples. It addresses two tasks: (1) sparse view sampling, where a greedy algorithm selects informative new viewpoints by minimizing MI (operationalized as CLIP semantic distance + camera pose distance), and (2) few-shot view synthesis, where plug-and-play regularization terms maximize MI between rendered and training images (CLIP-based semantic loss + RGB color-consistency loss). The paper claims consistent improvements over baselines like ActiveNeRF, FreeNeRF, and RegNeRF on Blender, LLFF, and DTU datasets.

## Strengths

- **Consistent empirical improvements across multiple settings.** The method shows gains over several strong baselines on multiple datasets and metrics. In the sparse view sampling setting (Table 1), Ours(P→S) yields +7.3% PSNR over ActiveNeRF on Blender under Setting I, and Ours(S→P) achieves -17.6% LPIPS. In the few-shot setting (Tables 3, 4), the method shows modest but consistent gains over FreeNeRF/RegNeRF on LLFF, DTU, and Blender. These improvements, while modest in the few-shot regime, are directionally consistent across diverse experimental conditions.

- **Novel dual-perspective decomposition (macro + micro).** The paper decomposes the notion of image correlation into semantic-level (CLIP cosine distance) and pixel-level (camera position distance / RGB color distance). This dual-lens approach is shown through ablations to outperform either perspective alone. While the theoretical MI framing is problematic (see Weaknesses), the practical insight that combining semantic and geometric distance is beneficial is a useful engineering contribution.

- **Computational efficiency via constraint reduction.** The greedy algorithm reduces the optimization from O(N²) constraints to O(N) per iteration, making the selection process tractable for large candidate view sets. The sequential approach (S→P or P→S) avoids a balancing hyperparameter between the two distance metrics.

## Weaknesses

### Fatal
None. The weaknesses are significant but do not outright invalidate the paper's empirical findings; they undermine the theoretical framing and the strength of the claims.

### Major

- **Definition 4 (multi-image MI via max) is non-standard and undermines the theoretical foundation.** The paper defines $I(R_1,\ldots,R_m;\overline{R}) = \max_i I(R_i,\overline{R})$ and cites Williams & Beer (2010), which concerns *partial information decomposition* — a completely different concept. This definition implies that adding more known images never provides more information than the single most informative one, which contradicts the core motivation of the paper (using multiple known views to enrich information). Since the paper's central claim is that MI provides a "theoretically robust" and "unified" framework, this definitional choice directly weakens that claim.

- **Assumption 1 (proportionality of conditional entropy to distance) is unjustified.** The paper states: "We assume the relative information of two images $H(R|\overline{R})$ is proportional to the similarity measure and distance measure between two images" — i.e., $H(R|\overline{R}) \propto s(R,\overline{R})$ and $\propto d(R,\overline{R})$. No justification is given for why CLIP cosine distance or camera-position Euclidean distance should be proportional to conditional entropy. Mutual information is a probabilistic quantity over distributions of images, not a distance between fixed feature vectors or camera coordinates. This assumption bridges a significant conceptual gap without any defended distributional model.

- **The logical chain from Lemma 3 to the micro regularization term is flawed.** Lemma 3 states: $\|\hat{C}(\mathbf{r})-\hat{C}(\overline{\mathbf{r}})\| \le 3L\|\mathbf{o}-\overline{\mathbf{o}}\| + C$ (color difference is *upper bounded* by camera distance). The paper then claims "the difference in RGB color serves as a lower bound for the difference in camera position" and "to reduce pixel space distance, we aim to minimize the color difference" (lines 234–235). Minimizing a variable that is an *upper bound* on camera distance does not guarantee a reduction in camera distance — the inequality runs the wrong direction. This logical gap means the micro term's connection to the claimed MI objective is not established by the paper's own lemmas.

- **Lemma 2 (2-approximation for the greedy algorithm) is stated without proof or justification.** The paper asserts a 2-approximation guarantee for the greedy algorithm without establishing that the objective (minimizing max pairwise MI) is submodular or exhibits any known structure that would yield such a guarantee. Standard greedy approximation guarantees (e.g., Nemhauser et al. for submodular maximization) do not straightforwardly apply to this minimax formulation. Without proof or citation, this claim is unverifiable. (Note: the proof may be in a parser-stripped appendix, but as presented, the claim is unsupported.)

- **No error bars or confidence intervals on any reported metric.** Given that many improvements are in the range of 0.2–0.5 dB PSNR (few-shot setting) — within typical run-to-run variance for NeRF — the absence of variance estimates makes it impossible to assess statistical significance. This is particularly problematic for the few-shot results (Tables 3, 4).

### Minor

- **Only tested on synthetic Blender data for the active learning (sparse view sampling) setting.** The active learning pipeline is evaluated exclusively on 8 synthetic scenes from Blender. Real-world datasets (DTU, LLFF) are used only for the few-shot experiments, where the paper adds regularization terms to existing methods. This limits the generality of the claims about the view selection strategy.

- **The micro regularization term provides limited additional benefit over the macro term.** The paper's own ablation (Table 4, text) shows that when normalizing improvements to 1, $L_{\text{micro}}$ contributes 0.61 in PSNR while $L_{\text{macro}}$ contributes 0.89. The paper acknowledges "DietNeRF is a degradation of our framework" — i.e., the macro term is essentially DietNeRF's existing semantic consistency loss. The net contribution beyond prior work is thus relatively small.

- **Few-shot improvements are modest.** Gains over FreeNeRF on LLFF (+0.33 dB PSNR) and over NeRF on Blender 8-view (+0.50 dB) are within the range where error bars would be critical to establish significance.

- **Computational cost of CLIP-based evaluation in the active learning loop is not discussed.** Running CLIP on every candidate rendered view at each active learning iteration adds overhead that should be quantified and compared against baselines.

### Trivial
None beyond minor presentation issues that would be addressed in revision.

## Nice-to-Haves
- Testing the active learning pipeline on real-world datasets (DTU, LLFF) would substantially strengthen the empirical claims.
- A proper probabilistic model relating NeRF renderings to the proposed distance metrics would make the theoretical framing more credible.
- Reporting runtime comparisons with ActiveNeRF would clarify the practical trade-offs.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Notation is inconsistent: $\mathcal{R}$ as rays vs. images"** — The paper explicitly clarifies this transition (line 81: "As we need to choose training images instead of rays, we denote $\mathcal{R}$ as the set of images in this section."). This is a deliberate notation reuse with a clear statement.

2. **"Paper doesn't explain how it computes semantic distance without ground truth"** — The active learning pipeline (line 187) explicitly states: "render images from candidate views and evaluate them." This is standard for active NeRF approaches.

3. **"Code not provided"** — This is a formatting artifact (parser strips supplementary materials) and not a valid criticism for assessing the paper content.

4. **Strength: "2-approximation guarantee"** — This is claimed but unproven in the text (see Weaknesses). It cannot serve as a strength when the theoretical basis is not established.

5. **"The micro term is just a smoothness prior"** — This is a characterization, not a weakness. The paper is transparent about what the micro term does (minimizing color difference between rendered and training images).

6. **Missing baselines like SparseFusion, MipNeRF 360** — The paper acknowledges this limitation in the conclusion (line 266: "Our framework has some limitations, particularly in terms of comparisons with the diffusion-based methods."). This is a known gap the authors flag themselves.

## Novel Insights

The most interesting observation that emerges from reading the reviews against the paper is how the paper's attempted theoretical framing actually *weakens* the contribution rather than strengthening it. The practical methods (CLIP-based view selection, dual semantic+geometric regularization) are reasonable heuristics that could stand on their own. The attempt to dress them in information-theoretic notation introduces definitions (Definition 4) and assumptions (Assumption 1) that are either non-standard or unjustified, creating vulnerabilities that a straightforward presentation of the heuristics would avoid. The reviewer-identified confusion around Lemma 3 (treating an upper bound as a lower bound to motivate the micro term) is a concrete example where the MI framing introduces logical errors that would not exist if the method were presented simply as "add CLIP loss and color-consistency loss." The paper's strongest result — +7.3% PSNR in the active learning setting — is also its least dependent on the MI theory: it's essentially furthest-view sampling (geometric) filtered by CLIP semantic diversity, or vice versa.

## Suggestions

1. **Reframe the contribution honestly.** Present the method as a practical combination of CLIP semantic diversity and geometric diversity for view selection, and CLIP semantic loss + color consistency for few-shot regularization. Drop the "theoretically robust MI framework" language unless the theoretical gaps are rigorously addressed.

2. **Fix the Lemma 3 logic.** Either correct the direction of the inequality argument or remove the attempt to connect color difference to mutual information through camera distance. The micro term can be justified as a simple color-smoothness prior without invoking MI theory.

3. **Provide error bars or distributional statistics.** At a minimum, report the mean and standard deviation over 3+ runs for the few-shot experiments, where improvements are marginal.

4. **Evaluate the active learning pipeline on real-world data** (DTU, LLFF) to demonstrate that the view selection strategy generalizes beyond synthetic scenes.

5. **Quantify computational cost.** Report the additional time per active learning iteration from CLIP feature extraction, and compare total training time against ActiveNeRF.

6. **Remove or prove Lemma 2.** Either provide a rigorous proof of the 2-approximation (establish submodularity or show the problem fits a known structure) or remove the claim and present the greedy algorithm as a heuristic without theoretical guarantees.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>