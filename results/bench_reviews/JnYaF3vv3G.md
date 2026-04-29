## Summary
The paper proposes **LabelDP-Pro**, a family of central-model label-DP training algorithms that augment DP-SGD with projection-based denoisers constructed from public features and hypothetical labels. Its main practical instantiation, **ALTCONV**, projects noisy gradients onto a convex hull of per-class gradients from an independently sampled feature batch, enabling privacy amplification while empirically improving utility in high-privacy regimes on MNIST/CIFAR-style benchmarks and a Criteo user-level setting.

## Strengths
- **Concrete and well-motivated use of the label-DP setting.** The method exploits the fact that features are public but labels are private: Section 3.1 constructs per-example/per-class gradient structures using only features and hypothetical labels, and uses them to denoise DP-SGD gradients.
- **Strong empirical signal in the high-privacy regime.** In Section 5.2, the paper reports that at \(\varepsilon=0.2\), prior RR-style baselines are near random guessing while LabelDP-Pro reaches \(92.9\%\) on MNIST and \(30.8\%\) on CIFAR-10. The text also states that LabelDP-Pro improves over vanilla DP-SGD, supporting the claim that the projection step adds value beyond simply using central DP-SGD.
- **ALTCONV is carefully designed around privacy amplification.** Section 3.4 gives a plausible post-processing argument: the DP-SGD gradient is produced by a Poisson-subsampled Gaussian mechanism, and ALTCONV’s projection batch uses only public features and independent randomness, so the projection can be treated as post-processing. The paper also explicitly explains why SELFSPAN/SELFCONV do not enjoy the same amplification argument.
- **The memory-efficient projection implementation is a genuine systems contribution.** Section 3.2 identifies that naively storing \(n_2 K d\) per-class gradients is infeasible, and proposes computing \(\mathbf G u\) and \(\mathbf G^\top v\) through VJP/JVP autodiff primitives rather than materializing \(\mathbf G\).
- **The paper identifies and empirically addresses an important stability issue.** Section 3.3 observes that noisy projection coefficients can concentrate on incorrect classes and cause large cross-entropy gradients; the coefficient-smoothing trick is supported by Figure 2 and Table 2.
- **The user-level evaluation is a useful extension.** Section 6 evaluates LabelDP-Pro on Criteo with real user identifiers, per-user gradients, and varying maximum contributions \(k\in\{2,5,10\}\), showing that the approach is not limited to item-level image benchmarks.

## Weaknesses

### Fatal
None.

### Major
- **The central “projection preserves the signal and removes only noise” explanation is only clean for SELFSPAN/SELFCONV, not for the main experimental method ALTCONV.** Section 3.1 and Figure 1 explain the denoising mechanism by saying the non-private gradient already lies in the projected structure, so projection mainly removes Gaussian noise. This is correct for SELFSPAN, where the projection is built from the same batch’s per-class gradients. However, the method used “unless otherwise specified” is ALTCONV, which projects onto a convex hull from an independently sampled alternative batch \(I_t^P\) (line 71). The current-batch gradient need not lie in that hull, so ALTCONV introduces an approximation/bias term as well as noise reduction. Lemma 4 does partially acknowledge this through the \(1/n_2\) term, so this is not a fatal flaw, but the paper’s main intuition and Figure 1 overstate the mechanism for the algorithm actually used in the experiments.
- **The theory is a stylized convex analysis and does not fully justify the implemented deep-learning algorithm.** Section 4 analyzes convex ERM with \(C\)-Lipschitz losses and bounded gradients, while the experiments use deep networks and cross-entropy; Section 3.3 itself notes instability from unbounded cross-entropy gradients. The theory also does not clearly incorporate coefficient smoothing, approximate PGD projection error, or the exact interaction with DP-SGD clipping. The paper does state that the bounds hold only for convex losses (line 146), so the issue is not that the theory is wrong, but that claims such as “theoretical analyses that justify the choice of the Denoiser” are stronger than what the analysis establishes for the deployed algorithm.
- **The state-of-the-art claim should be more carefully qualified by privacy/trust model.** The paper repeatedly says LabelDP-Pro improves the state of the art for LabelDP in the high-privacy regime, but its advantage partly comes from using central approximate label DP and amplification, while many RR-style baselines provide local/pure label-DP guarantees. The paper acknowledges this distinction in the contribution list, but the abstract/conclusion-level claim is still too broad. A fairer framing is that the paper advances **central approximate label-DP training**, rather than unqualifiedly dominating all LabelDP methods under matched assumptions.
- **The clipping/projection relationship is not fully specified in the main method description.** DP-SGD relies on per-example clipping, while the projection sets in Section 3.1/3.2 are described in terms of raw gradients \(\nabla_\theta \ell(\theta,(x_i,\kappa))\). If the private signal is an average of clipped gradients, then projecting onto a convex hull of unclipped per-class gradients changes the geometry; if the projection vertices are also clipped, that should be stated and reflected in the analysis. This matters because the convex-hull denoising interpretation depends on the signal belonging, or approximately belonging, to the projected set.

### Minor
- **The self-supervised/PATE-FM comparison is informative but not a clean head-to-head.** Table 6 compares LabelDP-Pro with PATE-FM numbers from prior work, and the paper notes that PATE-FM uses a stronger semi-supervised pipeline with higher non-private accuracy. This caveat is useful, but the result should be framed as an external reference rather than definitive evidence of superiority under matched representations, architectures, and tuning.
- **The user-level baseline is somewhat limited.** Section 6 compares against RR using group privacy, which is valid but can be pessimistic as \(k\) grows. Since the paper claims improvement for user-level label privacy, a stronger user-level label-DP baseline or a more explicit discussion of the conservativeness of group-privacy RR would strengthen the claim.
- **The user resampling procedure in Criteo deserves more discussion.** Section 6 says that users with fewer than \(k\) examples are augmented by random resampling. Duplicating examples changes the empirical training distribution and may affect gradient behavior and utility; this is not necessarily wrong, but it should be better justified.
- **The paper should make the label-DP adjacency/trust model maximally explicit throughout.** Section 2 recalls standard DP adjacency, and the text motivates label privacy, but the reader would benefit from a prominent formal statement that adjacent datasets share public features and differ only in one label, and from consistently distinguishing item-level versus user-level label adjacency.

### Trivial
None.

## Nice-to-Haves
- Add a direct ablation on harder datasets separating the effects of projection geometry and privacy amplification, e.g. NOOP, SELFSPAN, SELFCONV, and ALTCONV under matched noise multipliers and then under valid privacy accounting.
- Report sensitivity to \(n_2\), projection solver iterations, and smoothing \(\lambda\), especially because Section 7 notes that the projection currently requires about 200 iterations.
- Measure projection-induced bias versus noise reduction during training, e.g. \(\|\tilde g-g\|\), \(\|\mathrm{Proj}(\tilde g)-g\|\), and angle to the true gradient.
- Provide a deeper empirical account of when projection hurts at larger \(\varepsilon\), since Section 5.2 observes a threshold \(\varepsilon^*\) where RR can outperform LabelDP-Pro.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Main-text hyperparameter/reproducibility complaints.** The harsh review criticized missing clipping norms, batch sizes, noise multipliers, projection batch sizes, solver iterations, coefficient smoothing values, tuning protocol, and model-selection details. These may be useful for the authors to include, but per review instructions this should not be treated as a substantive evaluation weakness when such details may be in the appendix or implementation materials.
- **Pure formatting/parser artifacts.** Any garbled equations, odd symbols, broken line breaks, or missing punctuation in the extracted text are parser issues and should not be counted against the paper.
- **Generic “important problem” praise.** The problem is indeed practically relevant, but generic claims that the topic is important are not retained as strengths unless tied to a concrete contribution.
- **Requests for missing related work.** These are removed because external related-work gaps cannot be verified from the paper alone under the review instructions.
- **Demanding fully matched external PATE-FM reproduction as a requirement for acceptance.** A matched pipeline would improve the evidence, but Table 6 already explicitly notes the pipeline mismatch and uses PATE-FM as a comparison point. This is best treated as a limitation/nice-to-have rather than a core invalidation.
- **Treating the absence of a complete deep nonconvex theory as fatal.** The mismatch between theory and practice is real, but Section 4 explicitly presents the analysis as convex-theory motivation and states its limitations. The issue is overclaiming, not invalidity.

## Novel Insights
The most important synthesis is that LabelDP-Pro’s real contribution is not simply “project DP-SGD noise away,” but rather a more nuanced bias-variance tradeoff made possible by public features under central approximate label DP. SELFSPAN provides the clean geometric intuition, while ALTCONV is the practical privacy-accountable variant that trades exact signal preservation for amplification and computational feasibility. The paper would be stronger if it presented ALTCONV as an approximate denoiser whose success depends on alternative-batch convex-hull coverage, rather than letting the SELFSPAN intuition dominate the narrative.

## Suggestions
- Reframe the main claim as: **LabelDP-Pro improves utility for central approximate label-DP training in high-privacy regimes**, rather than broadly claiming SOTA over all LabelDP mechanisms.
- Revise Figure 1 and the Section 3.1 explanation to distinguish exact signal preservation for SELFSPAN/SELFCONV from approximate projection for ALTCONV.
- State explicitly whether projection vertices are raw gradients, clipped gradients, or clipped-and-normalized per-class gradients, and align the theory and implementation description accordingly.
- Present Section 4 as stylized theory explaining the bias-variance tradeoff, not as a full justification for deep-network training with cross-entropy, clipping, smoothing, and approximate PGD projection.
- Add a compact table of key training/projection/privacy-accounting parameters in the main text if space permits.
- Strengthen the user-level section with either a better baseline or a clear explanation that group-privacy RR is a conservative but valid comparator.

## Score and Decision
**Assessment by axes.**  
- **Originality:** High. The projection-based use of public features for label-DP gradient denoising, especially with ALTCONV and memory-efficient VJP/JVP projection, is a distinctive contribution.  
- **Importance:** High within private learning / label-DP, especially for high-privacy regimes where RR-style methods degrade sharply.  
- **Support for claims:** Good but somewhat overclaimed. The empirical results are promising, but the broad SOTA framing and mechanistic explanation need qualification.  
- **Soundness:** Generally sound, with notable caveats around the theory/implementation mismatch and clipping/projection details.  
- **Experimental quality:** Substantial and directionally convincing, though some comparisons are not fully matched and the user-level baseline is limited.  
- **Clarity:** Mostly clear, but the paper should more sharply distinguish SELFSPAN intuition from ALTCONV behavior and central approximate DP from local/pure label-DP.  
- **Value to community:** High; the method and implementation ideas are likely useful for future work on label-DP training.

### Calibration Anchors Considered
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/IwPXYk6BV9.md` — Avg 7.50, Accept. Direct label-DP anchor with clean empirical improvements and simpler mechanism; the current paper is more ambitious but has more overclaim/theory-practice mismatch, so it scores below this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E60SIDItyT.md` — Avg 6.00, Accept. Privacy-motivated learning from aggregate labels with strong theory but narrower setting; current paper is more practically impactful but less theoretically matched.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KYipmCMmSO.md` — Avg 6.33, Reject. DP deep-learning paper with theory that only partially matches practice; current paper has a similar weakness but stronger task-specific empirical contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lLkgj7FEtZ.md` — Avg 6.50, Accept. Private learning/alignment work with useful empirical contribution; broadly comparable quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3d0OmYTNui.md` — Avg 6.67, Accept. DP framework for private alignment; comparable in being useful despite modeling/practical caveats.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ihr4X2qK62.md` — Avg 4.50, Reject. Public-gradient-subspace projection for private ML; current paper is stronger because the public information is intrinsic to label-DP and the empirical case is clearer.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sWwK0lJ8dK.md` — Avg 5.50, Reject. Privacy paper with favorable empirical claims but overclaiming and unclear guarantees; current paper has overclaiming too, but its formal DP basis is more solid.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1YYp1rPRlm.md` — Avg 5.75, Reject. Strong empirical/theoretical DP work with mismatch between theory and experimental regime; similar weakness pattern, but current paper’s central mechanism is more directly aligned with the privacy setting.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/97tbbvSJ4A.md` — Avg 3.50, Reject. DP deep-learning method with questionable credibility relative to baselines; current paper’s results and privacy accounting are substantially more credible.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/txV4dNeusx.md` — Avg 6.25, Accept. DP method with SOTA/privacy-accounting scrutiny; current paper is similar in quality, with stronger novelty but more framing issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vuvG5rNBra.md` — Avg 5.25, Reject. Empirical privacy paper needing stronger evidence; current paper is stronger because it has a formal DP mechanism and clearer empirical gains.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nM2kuesKpC.md` — Avg 3.00, Reject. DP-SGD/projection paper with weaker quality; current paper is much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/F52tAK5Gbg.md` — Avg 4.00, Accept. DP-SGD variant with serious theoretical/experimental concerns; current paper is more convincing and better positioned.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vgV4y086FY.md` — Avg 6.75, Reject. Central DP optimization paper with theory/empirics; current paper is in a similar upper-borderline range.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NFWt2PavSW.md` — Avg 5.75, Reject. DP-SGD optimization paper with useful but limited contribution; current paper has stronger novelty.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DRKkO2Tejc.md` — Avg 4.75, Reject. Label-privacy split-learning paper with unclear baselines/setting; current paper is cleaner and more formal.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/E4OcXAx5Dc.md` — Avg 5.00, Reject. Private online learning under local DP; current paper has stronger empirical relevance.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/reBq1gmlhS.md` — Avg 4.50, Reject. DP reward-learning paper with weaker validation; current paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3uITarEQ7p.md` — Avg 5.50, Reject. DP compression/fine-tuning with moderate contribution; current paper is above this due to clearer algorithmic novelty.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qazJfAmgOt.md` — Avg 6.00, Reject. Label leakage/unlearning work; current paper is comparable but has stronger formal DP framing.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nATTIkte9f.md` — Avg 4.75, Reject. DP fine-tuning under strong privacy with weaker support; current paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jMJ9IRWmH9.md` — Avg 3.50, Reject. Label-privacy API fine-tuning with confusing method and weak guarantees; current paper is much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uvq4Nh8eZB.md` — Avg 4.00, Reject. Privacy-preserving federated co-training; current paper has clearer contribution and evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MxuFXJtVTt.md` — Avg 3.50, Reject. PATE-style private aggregation with weaker evaluation; current paper is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NqkSUwMc0K.md` — Avg 3.60, Reject. Distributed DP learning with significant weaknesses; current paper is much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FNCFiXKYoq.md` — Avg 3.00, Reject. DP/fair classification with low assessed quality; current paper is far above this.

Relative to these anchors, this paper is clearly above the low-scoring DP/privacy papers with unclear guarantees or weak empirical evidence, and above the 5-ish papers where the contribution is mostly incremental or poorly supported. It is below the clean high-scoring label-DP anchor because its main narrative overstates ALTCONV’s mechanism and its theory is less well aligned with the practical algorithm. Overall, I would place it in the **borderline-to-weak-accept** range.

**Score: 6.5 / 10**  
**Decision: Accept**

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>