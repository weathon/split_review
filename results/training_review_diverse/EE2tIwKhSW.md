Now I have all the information needed. Let me compile the final review.

## Summary

This paper identifies two critical evaluation defects in prior membership inference attacks (MIAs) on diffusion models—over-training and dataset shift—and builds CopyMark, a benchmark that simultaneously removes both defects by using pre-trained models (single-epoch training) with unshifted member/non-member datasets. Experiments show that all state-of-the-art MIAs (loss-based and classifier-based) perform near-random or degrade severely under these realistic conditions, supporting the conclusion that current MIAs are unreliable for detecting unauthorized data usage in pre-trained diffusion models.

## Strengths

1. **Systematic identification and tabulation of two evaluation defects in prior MIA work.** Section 3 and Table 1 enumerate every prior evaluation setup and mark each for over-training (≥300 epochs) and dataset shift between members and non-members. This concise catalog directly supports the claim that no prior evaluation is realistic.

2. **Construction of CopyMark, the first benchmark that simultaneously removes both defects.** Three new setups—(c) SD1.5 on LAIN→LAIN, (d) CommonCanvas-XL-C on CommonCatalog→MS-COCO, (e) Kohaku-XL on HakuBooru split—use single-epoch-trained models with verified minimal/no dataset shift (CLIP-based hyper-plane classification achieves TPR≈0.5 on these setups vs. TPR>0.88 on defective ones). This directly validates the design criteria.

3. **Empirical demonstration that loss-based and classifier-based MIAs fail under realistic conditions.** On setups (c), (d), (e), loss-based methods (SecMI, PIA, PFAMI) achieve TPR@1%FPR ≤ 0.02 with well-controlled test-set FPR, confirming near-random performance. Classifier-based methods (GSA₁, GSA₂) show large validation-to-test performance drops (e.g., TPR drops from 1.000 to 0.702 on setup (c); test FPR rises to 0.27–0.43), exposing severe overfitting.

4. **Introduction of a two-stage evaluation protocol (validation + blind test) that exposes overfitting in classifier-based MIAs.** Algorithms 1–2 formalize this workflow, and the results repeatedly show that GSA methods achieve perfect validation performance but degrade significantly on the blind test set. This methodological contribution provides a concrete tool for future realistic evaluations.

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison between the blind baseline and loss-based MIAs (§5, Table 3).** The paper claims "the blind baseline beats loss-based MIAs" on realistic setups, but the comparison is not controlled for FPR. For loss-based methods, the threshold chosen on the validation set maintains FPR near the 1% bound on the test set (e.g., SecMI test FPR = 0.88% on setup (c)). For the blind baseline, the same threshold produces a far higher test FPR (e.g., 39.38% on setup (c), 15.64% on (d), 30.64% on (e)). Comparing TPR values at vastly different FPR operating points is meaningless. The blind baseline test TPR of 0.4592 at 39% FPR is not directly comparable to a loss-based TPR of 0.0108 at 0.88% FPR. The paper's text (line 386) does not qualify this mismatch. **This weakness does not affect the core finding** (that loss-based MIAs fail with controlled FPR, and that classifier-based MIAs overfit) — the loss-based results stand on their own. But the "blind baseline beats" claim as currently stated is methodologically unsupported and should be withdrawn or reformulated with proper FPR-bounded comparison (e.g., by reporting test-set AUC for all methods).

2. **Test-set AUC is not reported.** AUC is only given for the validation set. For the test set, only TPR and FPR at two fixed thresholds are reported. Without test-set AUC, it is impossible to compare methods on the test set in a threshold-independent manner. Reporting test-set AUC would also enable a fair comparison between the blind baseline and other methods without the FPR mismatch issue above. This is a straightforward addition for a benchmark paper.

### Minor

1. **Single fixed random split without confidence intervals.** The paper fixes one random seed for member/non-member assignment (2500 per class) without reporting variance across multiple splits. Given the moderate dataset size, results may be sensitive to sampling variability. Reporting results over 3–5 random splits with confidence intervals would strengthen reliability.

2. **No explicit limitations section.** The paper does not acknowledge its own boundaries: the benchmark covers only text-to-image latent diffusion models (3 models), all single-epoch-trained, and the number of realistic setups is small (3). Acknowledging these would improve credibility.

### Trivial

1. **Table 1's green/red checkmark format is unconventional.** The first sub-table uses ✓/✗ to indicate which methods were evaluated on which setups, while the second sub-table shows over-training and shift flags. The point is clear but the cross-referencing could be more direct.

2. **Algorithm 1 notation is slightly sloppy.** The "s.t." constraint is embedded inside the argmax (line 245–247) rather than in a separate constraint line. This does not affect correctness.

## Nice-to-Haves

- **Deeper analysis of why loss-based MIAs fail on pre-trained models** would strengthen the contribution. Section 6.1 correctly notes the single-epoch training reduces the loss gap, but explicitly measuring and visualizing the member/non-member loss distributions for one realistic setup would solidify the argument.
- **Testing classifier-based MIAs with simpler classifiers (e.g., linear probe)** could isolate whether the overfitting comes from the classifier architecture or the features themselves, deepening the insight in §6.1.
- **A brief justification of why the three selected pre-trained models suffice as representative cases** would improve motivation (though the selection is constrained by data accessibility, which the paper already notes).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's strength 5 (blind baseline outperforming on realistic setups):** The claim that "on realistic setups the blind baseline outperforms loss-based MIAs" conflicts with the verified Major weakness above (unfair FPR mismatch). The valid portion — that the blind baseline exposure on defective setups confirms dataset shift confounds — is already captured elsewhere. The problematic comparison claim is dropped.
- **Section 6.2 "conflates two issues" about copyright lawsuits:** The paper discusses both whether MIAs can detect membership and whether membership alone constitutes copyright evidence. The paper's conclusion is that MIAs are unreliable for even the first question, so the secondary legal discussion is relevant context, not a conflation. This is not a genuine weakness.
- **Model selection justification (Section 4.1):** The paper already explains the constraints (accessible training data, available non-member datasets from similar distributions) and justifies each choice. The critic's request for more justification is scope creep beyond what is needed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one subtle insight that the paper itself does not fully articulate: **the blind baseline's failure to control FPR on the test set is itself informative** — it reveals that the classifier-based approach (including the blind baseline) is overfitting to spurious features in the validation set that do not generalize. Had the paper framed the blind baseline's test-set FPR blow-up as *additional evidence of the difficulty of the task* rather than as a "beating" of loss-based methods, it would have turned this apparent weakness into a stronger finding. The blind baseline's test FPR collapse tells the same story as the GSA methods' validation-to-test gap: the features available in these realistic setups are insufficient for reliable membership separation.

## Suggestions

1. **Fix the blind baseline comparison.** Either (a) report test-set AUC for all methods (including the blind baseline) and compare on that threshold-independent metric, or (b) re-calibrate the blind baseline threshold directly on the test set to match the 1% FPR bound, then report TPR at that aligned operating point. Drop the unqualified "beats" language.
2. **Add test-set AUC to Table 3** for all methods and setups.
3. **Add confidence intervals or results over 3–5 random splits** to demonstrate statistical stability.
4. **Add a brief limitations paragraph** acknowledging the scope boundaries (LDM family only, three models, three realistic setups).

## Score and Decision

The paper's core contribution — identifying evaluation defects and constructing a realistic benchmark that shows MIAs fail — is novel, timely, and well-supported by the loss-based and classifier-based results. The blind baseline comparison issue is a real methodological flaw in a secondary claim, but it does not undermine the central findings. With the comparison fixed and test-set AUC added, this would be a solid empirical contribution to the community.

**Originality:** 4/5 — First to systematically identify evaluation defects in MIA on diffusion models.  
**Importance of question:** 5/5 — Directly relevant to copyright lawsuits and real-world deployment of MIAs.  
**Claims well-supported:** 3/5 — Core claims are supported, but the blind baseline claim is not.  
**Soundness:** 4/5 — Core experiments are sound; one flawed comparison.  
**Clarity:** 4/5 — Generally clear presentation.  
**Value to community:** 5/5 — Provides a benchmark and reality check that will influence future work.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>