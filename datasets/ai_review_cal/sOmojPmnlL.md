- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 6, 3
Now I have all the information I need. Let me write the consolidated review.

## Summary

AnyExpress proposes a lightweight Audio-Motion Adapter that eliminates the ReferenceNet module used in prior audio-driven portrait animation methods, achieving a claimed 7× reduction in trainable parameters. The framework supports "Freeform Portrait Animation" — generating talking faces with arbitrary poses, dynamic backgrounds, and text-based control — by replacing strong ReferenceNet-based identity control with weaker IP-Adapter-Face control plus a two-stage-trained audio-motion module. Qualitative results demonstrate capabilities (animated contexts, text-conditioned animation) that prior open-source methods lack.

## Strengths

- **Novel architectural contribution — ReferenceNet-free design with practical benefits.** The paper identifies a real limitation of current ReferenceNet-based methods (excessive coupling, limited flexibility, incompatibility with personalized models) and proposes a clean solution: a self-contained audio-motion adapter that can be plugged into any T2I model. This is concretely demonstrated in Fig. 6b, where the same adapter animates both a realistic base model and an Asian-style model without retraining. No prior open-source method achieves this degree of modularity.

- **Quantitative advantage on pose diversity (Table 2).** AnyExpress achieves the best Pose Diversity Score (ΔP = 1.53) under Any Face Pose conditions while maintaining competitive lip-sync (Sync-C), video quality (DOVER), and identity consistency (FaceSim, CLIP-I) against four open-source baselines (AniPortrait, EchoMimic, V-Express, MegActor). This provides direct evidence that the ReferenceNet-free design delivers greater pose flexibility without collapsing quality on other axes.

- **Demonstrated capabilities beyond prior methods.** The paper shows portrait animation with animated backgrounds (Fig. 6a) and text-only-driven animation without a reference image (Fig. 6b). These are genuinely new capabilities for audio-driven portrait animation that no prior open-source baseline in the comparison supports. Even if the quantitative comparison were weakened, these qualitative demonstrations constitute a meaningful contribution.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation data contamination — training and evaluation overlap is unacknowledged.** The paper states that AnyExpress is "trained by HDTF" (line 116) and that "quantitative evaluation (Table 2) was performed on the HDTF, CelebV datasets" (line 116-117). No held-out test split is mentioned. The term "test set," "validation set," or any exclusion of training samples does not appear anywhere in the paper. As written, the reader cannot rule out that Table 2 includes videos seen during training, which would inflate AnyExpress's scores relative to baselines not trained on HDTF. This undermines the primary quantitative evidence for the method's superiority. CelebV evaluation partially mitigates this (since CelebV is not listed as a training source), but the HDTF column remains suspect. *Verification: lines 116-117 confirm the ambiguous wording; no test-split language exists in the paper.*

- **All ablations are purely qualitative.** Section 4.4 presents four ablation studies (Progressive Prefix Conditioning vs. Progressive Fusion, two-stage vs. single-stage training, motion block selection, identity controller choice) — every one supported only by visual comparisons in Figs. 7 and 8. No metric values (ΔP, Sync-C, FaceSim, DOVER, or any other) are reported for any ablation condition. For a methods paper whose core claims depend on precisely these design decisions, this is a serious evidential gap. Without numerical results, the reader cannot verify that the proposed designs constitute genuine improvements rather than cherry-picked examples. *Verification: lines 154-173 — all ablations describe visual outcomes only.*

- **Efficiency claim is stated without supporting evidence.** The abstract claims "reducing the number of trainable parameters by 7 times," but the paper provides zero actual numbers: no parameter counts for AnyExpress or any baseline, no training time, no inference speed (e.g., seconds per frame, FPS). This is the paper's headline efficiency advantage, and there is no way to verify it from the published text. The related work section even discusses that ReferenceNet "dramatically increases computation" (line 32), yet the paper never quantifies how much computation its own method saves. *Verification: grep for "parameter," "trainable," "inference," "speed," "FPS," "seconds" confirms no numerical efficiency data.*

### Minor

- **Entropy analysis used as evidence lacks a formal definition.** The paper describes an "entropy difference across attention heads" (line 78) and uses it to argue that weak control enables broader exploration. However, "entropy" is never defined — it is unclear whether this refers to Shannon entropy of attention weight distributions, some other measure, or how it is computed and aggregated across heads. The experiment uses only 30 identities and 50 clips (line 78), which is small for a claim meant to justify a core architectural decision. This analysis is better presented as intuition than as evidence. *Verification: lines 78-83 describe the analysis but give no definition of the entropy measure.*

- **No variance or confidence intervals in Table 2.** The quantitative comparison reports single-point estimates for each metric. For a table that is central to the paper's claims, reporting standard deviations or confidence intervals (over multiple runs or test samples) is standard practice and would significantly strengthen the comparison.

- **Baseline training setup is not specified.** The paper does not state whether the four baselines (AniPortrait, EchoMimic, V-Express, MegActor) were used with their default checkpoints or fine-tuned on the same 300-hour training data. Since AnyExpress uses substantially more training data than what the baselines may have been trained on, any performance difference could partially reflect data scale rather than architectural advantage. *Verification: lines 124 only describe selection criteria ("public availability and support for audio and face control signals"), not training setup.*

### Trivial
None.

## Nice-to-Haves
- A user study would strengthen the qualitative claims about animated contexts and text-based control, which are currently demonstrated only via example videos.
- A discussion of failure cases (e.g., extreme poses, very long videos, identity drift under text control) would improve completeness.
- Reporting FID/FVD for completeness, despite the paper's stated reason for omitting them, would help readers compare against the broader literature.
- Including a brief definition of ΔP (Pose Diversity Score) in the main text (rather than only in the appendix) would improve self-containedness.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Proposition 3.2 is unusual / adds no rigor"** (Harsh Critic): This is a stylistic observation about nomenclature, not a substantive weakness. The label "Proposition" is unconventional but does not affect the paper's validity.
- **"Motion module training description is confusing"** (Harsh Critic): The paper's description (line 99-100) is actually clear: Stage I fine-tunes both audio and motion modules; Stage II resets motion to pretrained weights and applies shorter fine-tuning with Stage I audio weights. The critic misread the passage.
- **"First-to-introduce claim is too strong"** (Harsh Critic): The claim is qualified with "to the best of our knowledge" (line 23). Whether prior work (VASA-1, Emo) constitutes the same "task" is debatable; this is a framing preference, not an error.
- **"Missing ΔP definition in main text"** (Harsh Critic): The paper provides a brief description ("measures head motion intensity") and cites prior work. This is standard practice; full metric detail in the appendix is acceptable.
- **Strength Finder: "7× reduction in trainable parameters"** as a strength with evidence: The paper claims this but provides no actual parameter counts. This is an asserted strength without verifiable evidence in the paper, so it cannot serve as a strength that supports the paper's claims.
- **Strength Finder: "Entropy analysis"** as a supporting strength: Given the lack of formal definition and the small sample size (30 identities, 50 clips), this analysis is too weakly specified to count as strong evidence. It is better categorized as an intuition.

## Novel Insights

Beyond the paper's own contributions, the review surfaces a noteworthy tension: the paper's core argument is that strong control (ReferenceNet) *limits* generation flexibility, yet the ablations show that too *weak* control (training only one motion block, using only audio modules) also fails — producing non-smooth transitions or identity overfitting. This suggests the design space between "too strong" and "too weak" is narrow and method-specific, and the paper's claim that "less is more" is better characterized as "just enough is more." The two-stage training procedure and the choice of which motion blocks to fine-tune effectively navigate this trade-off, but without quantitative ablations, the boundary conditions of this sweet spot remain unclear.

## Suggestions

1. **Clarify the evaluation split.** Explicitly state whether a held-out test split of HDTF was used, and if so, describe how it was constructed (e.g., number of videos/clips excluded from training). Report results on CelebV as a fully unseen dataset to provide a clean validation of generalization.
2. **Add a quantitative ablation table.** Report the same metrics from Table 2 (ΔP, Sync-C/D, DOVER, FaceSim, CLIP-I) for each ablation condition. This is the single highest-impact improvement the authors can make to their paper.
3. **Provide concrete efficiency numbers.** Report the total and trainable parameter counts for AnyExpress versus each baseline, along with training time (GPU-hours) and inference speed (seconds per frame or FPS).
4. **Define the entropy measure.** Formalize what "entropy difference across attention heads" means — specify the entropy type (e.g., Shannon entropy of attention probability distributions), how it is aggregated, and why it is a valid proxy for generation flexibility.
5. **Add variance information to Table 2.** Report standard deviations to establish the reliability of the single-point comparisons.
