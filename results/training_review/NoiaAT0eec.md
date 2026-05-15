Now I have a thorough understanding of the paper and can cross-check all claims. Let me write the final consolidated review.

## Summary

This paper proposes MI-MAE, a masked image modeling approach that applies the information bottleneck (IB) principle to understand and improve masked autoencoders. The authors derive an IB-inspired analysis of MAEs, yielding two mutual information losses: an InfoNCE-style maximization between latent features of different masked views, and a MINE/CLUB-based minimization between the latent and the input. Experiments on ImageNet-1K show that a 400-epoch MI-MAE achieves 83.9% top-1 accuracy, surpassing a 1600-epoch vanilla MAE by 0.5%.

## Strengths

- **Empirical promise**: MI-MAE (400 epochs, 4 masks/image) achieves 83.9% on ImageNet-1K, outperforming vanilla MAE at 1600 epochs (1 mask/epoch) by 0.5%. Given both see the same total number of masked views (4×400 = 1600), the comparison is apples-to-apples in terms of effective mask exposure, and the improvement suggests the MI losses provide some benefit.
- **Broad evaluation scope**: The paper evaluates on classification, object detection, and semantic segmentation, testing generalization across tasks (though detailed tables are in the now-stripped appendix).
- **Clear algorithmic specification**: Algorithm 1 and the loss formulations (Eq. 6, 9, 10) provide reproducible implementation details.

## Weaknesses

### Major

- **The theoretical derivation (Section 4) is significantly incomplete and contains gaps that undermine the paper's central claimed contribution.** The paper presents itself as providing a rigorous information-theoretic framework, but the mathematical development is too informal to serve this role:
  - *Theorem 2* (Eq. 4) presents an upper bound with a subtracted term \(-I(\hat{z}; X\cdot m|r)\), uses the quantity \(Y\) without prior definition (Y is defined only later in Assumption 3), and includes an \(O(\cdot)\) term whose derivation is unexplained. The bound's validity cannot be assessed without a proof, and the claim that it provides actionable insight is unsupported.
  - *Corollary 4* states that \(I(\hat{z}_k;z_k)\) "can be maximized **only when**" three conditions hold, but this "only when" claim does not follow from an upper-bound inequality. From an upper bound, one can infer *sufficient* conditions for maximizing the *bound*, not necessary conditions for maximizing the *actual quantity*. This is a logical gap.
  - The connection from Corollary 4's condition (3) to the proposed loss \(\mathcal{L}_{\text{min.mi}}\) is merely asserted ("we find that by optimizing Eq. 10, the third condition... is also satisfied") without any argument or derivation. Similarly, the claim that InfoNCE *directly satisfies condition (1)* is stated without formal justification (though InfoNCE is a standard MI lower-bound estimator, the specific mapping from the corollary to the loss form is not explicitly reasoned).

  Since the paper's novelty narrative is built on "our theoretical analyses reveal..." and "building upon our proofs...," these gaps are serious. They mean the method is not actually derived from the presented theory in a rigorous sense — rather, the theory provides a plausible motivation, and the losses are then introduced heuristically.

- **Missing critical ablation: MAE with multiple masks and reconstruction loss only.** The paper uses 4 masks per image. A baseline of MAE trained with the same 4 masks (only \(\mathcal{L}_{\text{rec}}\), no MI losses) at 400 epochs is absent. Without this control, the improvement of MI-MAE over vanilla MAE (1 mask) cannot be attributed to the proposed MI losses rather than to the increased diversity of training signal from seeing multiple masks per epoch. This is the most important missing experiment.

### Minor

- **Algorithmic novelty is limited.** The two loss components are standard techniques: \(\mathcal{L}_{\text{max-mi}}\) is InfoNCE (SimCLR/MoCo-style contrastive loss applied to different mask views), and \(\mathcal{L}_{\text{min.mi}}\) uses MINE with a variational posterior approximation (CLUB). The paper acknowledges prior work connecting MAEs to contrastive learning (Zhang et al., 2022; Kong & Zhang, 2023; Huang et al., 2023), but it does not clearly articulate how its use of these losses differs from or improves over these existing connections. The claimed novelty resides primarily in the theoretical framing rather than in the algorithmic components themselves.

- **The connection between the theoretical analysis and the loss formulation is heuristic, not deductive.** Section 4.2 moves from "we can adopt InfoNCE" and "we use MINE" to specific loss equations, but the text does not walk through how the IB derivation uniquely leads to these particular losses as opposed to other possible MI-based objectives. The losses are *consistent with* the IB framing, but the paper overstates the extent to which they are *derived from* it.

### Trivial

- Notation is at times unclear: the overbrace/widetilde/widehat notation for the simplest effective description vs. prediction is visually similar and not clearly distinguished; \(Y\) is used before being defined in Assumption 3; the relationship between \(X_0\) and the original image in the multi-mask setup (line 103) is ambiguous.

## Nice-to-Haves

- An ablation comparing MAE+4masks (reconstruction only) vs. MI-MAE would directly isolate the effect of the MI losses.
- Reporting wall-clock time and FLOPs (including the variational approximation network overhead) would enable a more complete efficiency comparison.
- Empirical measurement of the actual mutual information values (e.g., \(I(\hat{z}_k;\hat{z}_i)\) and \(I(\hat{z}_j;X_j)\) before and after training) would demonstrate that the losses achieve their intended effect, validating the IB interpretation beyond downstream accuracy alone.

## Removed Points

The following criticisms from the reviewers were assessed against the paper and removed with justification:

1. **"Definition 1 is atypical and notation is inconsistent"** — This is a style critique of a paper-formulated definition; the definition is self-consistent as presented. Removed as a formatting/style nitpick and because the reviewer mischaracterizes the notation (the paper maintains consistent variable usage).
2. **"The proof is absent in the main text" / "appendix is stripped"** — Removed per instructions: the parser strips appendix content, which exists in the original submission.
3. **"InfoNCE connection is unsupported"** — The paper explicitly states "From the first condition... we can adopt InfoNCE" and cites Oord et al. (2018) for InfoNCE as a lower bound of MI. The connection is standard and explicitly drawn. Removed as factually incorrect claim by the reviewer.
4. **"The table of results is not provided"** — Removed per instructions: the parser strips appendix/tables; they exist in the original submission.
5. **Strength "Principled theoretical framework"** — Conflicts with the verified weakness that the theoretical derivation has significant gaps. Removed.
6. **Strength "Novel mutual information losses that operationalize the IB principle"** — The losses are standard techniques (InfoNCE, MINE/CLUB); the theory-to-loss connection is heuristic rather than deductive. Conflicts with verified weaknesses. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add the critical missing ablation: train MAE with 4 masks per image + reconstruction loss only, at 400 epochs.
2. Clarify the logical status of the theoretical development — either present it as a principled motivation rather than a formal derivation, or provide complete proofs with clear steps connecting each inequality to the loss design.
3. Remove or soften the "only when" claim in Corollary 4, which is not supported by an upper-bound inequality.
4. Explain how \(\mathcal{L}_{\text{min.mi}}\) satisfies condition (3) of Corollary 4, or remove the unsubstantiated claim.
5. Report wall-clock time and parameter count for the variational approximation network to quantify the overhead.
6. Add empirical MI estimates (computed via the trained variational network) to show that the losses actually achieve their intended effect.

## Score and Decision

The paper addresses an interesting question (theoretical understanding of MAEs) and shows promising empirical results. However, the core contribution — the IB-based theoretical framework — is presented as rigorous but contains significant gaps (undefined quantities, unjustified claims about optimality conditions, heuristic rather than deductive connection to the losses). The empirical evaluation is missing a crucial control (multiple-mask reconstruction baseline), making it impossible to attribute gains to the proposed losses. The method itself combines standard techniques (InfoNCE, MINE/CLUB) whose novelty lies primarily in the theoretical framing, which is not sufficiently rigorous to carry this weight. In its current form, the paper's contributions do not meet the bar for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>