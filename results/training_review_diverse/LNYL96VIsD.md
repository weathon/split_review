Now I have verified the paper content against the reviewer claims. Let me synthesize the final review.

## Summary

This paper identifies a phenomenon called "the curse of singularities"—a vicious cycle where large learning rates cause weight matrices to develop low stable rank (high parametric singularity), which concentrates Jacobian energy on dominant singular directions, further reducing stable rank until loss explosion occurs. The authors propose Parametric Singularity Smoothing (PSS), a lightweight method that detects impending instability via gradient norm spikes and smooths the singular spectra of weight matrices. Experiments on BERT and GPT-2 models across scales show PSS expands the usable learning rate range by 5–10× over gradient clipping and orthogonal regularization, with negligible computational overhead (0.21% of training time).

## Strengths

1. **Empirical identification of a concrete instability mechanism.** The paper directly shows that a sharp drop in stable rank (SR) occurs several steps before loss explosion, accompanied by token cosine similarity spiking to 0.9 in deep layers and NTK-λ_max rising sharply, while these metrics remain normal in stable training (Fig. 3, Section 2.2). This provides a clear, measurable signal that explains *when* and *why* loss explosions happen under large LRs.

2. **PSS achieves 5–10× expansion of usable learning rate.** On BERT-base, PSS expands the maximum stable LR from 1e-4 to 2e-3 (10×); on GPT-2-Medium it achieves 10×; on larger models (BERT-large, GPT-2-Large, GPT-2-XL) it achieves up to 5×. Gradient Clipping and Orthogonal Regularization achieve at most 2× and fail at higher LRs (Fig. 4(b), Table 1). These results directly support the central practical claim.

3. **PSS can rescue training even after instability has already occurred.** Figure 5(a) shows that PSS applied after loss divergence restores normal loss descent, whereas prior methods require trial-and-error from saved checkpoints. This is a strong practical benefit that distinguishes PSS from existing approaches.

4. **Negligible computational overhead.** Table 2 shows total overhead on BERT-base is only 0.21% of baseline training time; protection is triggered in fewer than 0.1% of steps even at extreme LRs (Section 4.2). This makes the method practically viable.

5. **Validation across multiple model scales and architectures.** Results span BERT-base (110M), BERT-large (340M), GPT-2-Medium (345M), GPT-2-Large (774M), and GPT-2-XL (1.2B), demonstrating generality (Section 4.1–4.2).

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are supported by the evidence presented.

### Minor

1. **Limited comparison baselines relative to the method's motivation.** The paper compares PSS only against Gradient Clipping and Orthogonal Regularization. Since PSS operates by directly modifying singular spectra, spectral normalization (Zhai et al., 2023)—which also controls singular values and is cited in the paper's related work—is a natural and expected baseline. Its absence weakens the claim that PSS outperforms "existing methods" broadly, rather than just the two tested alternatives. The paper would be substantially strengthened by including spectral normalization in Table 1 and Figure 4.

2. **SJE (Stable Jacobian Energy) is introduced as a core analytic construct but never validated in the evaluation.** SJE is defined (Definition 2) and used to explain the vicious cycle in the analysis (Fig. 2(b)), but it does not appear in the post-intervention analysis (Fig. 6 shows SR, NTK-λ_max, and token similarity—not SJE). The paper would be internally more coherent if it either (a) demonstrated that PSS reduces SJE when smoothing is triggered, or (b) acknowledged SJE as an explanatory concept rather than a metric that needs to be tracked. As it stands, the narrative asserts a causal role for SJE but provides no evidence that PSS actually affects it.

3. **Detection threshold τ = 2.5 is given without systematic sensitivity analysis.** The paper claims the choice is robust and argues that false positives do not disrupt training (Section 3). However, no experiments vary τ across different model architectures or LR regimes to demonstrate this robustness empirically. While the rescue robustness (Fig. 5(a)) partially addresses concerns about high τ values missing instabilities, a systematic sweep across τ values would turn a plausible claim into a demonstrated one.

4. **The specific smoothing function used in the main experiments (Table 1, Fig. 4) is not reported.** Section 3 lists several viable options (Logarithmic with Scaling, Softplus, Softmax, clipping) and states flexibility, but the paper does not specify which one produced the results in the central tables and figures. This is a basic reporting requirement.

5. **Novelty claims are slightly overstated relative to prior work.** The paper states it is "the first to describe the dynamic patterns of network singularities and reveal their tight associations with loss explosion" (Section 1) and "the first to study how the network's fine-grained, dynamic singularity behaviors cause loss explosions" (Section 1). However, prior work (Zhai et al., 2023; Dong et al., 2021; Noci et al., 2022) has studied rank collapse, attention entropy collapse, and their links to training instability. The paper's focus on *parametric* singularities (stable rank of weight matrices) and their dynamic interaction with Jacobian energy is genuinely novel, but the framing should more precisely delineate what *specifically* goes beyond prior rank-collapse accounts rather than claiming "first" in a space where related phenomena have been studied.

### Trivial

None.

## Nice-to-Haves

- A systematic τ sensitivity sweep across τ ∈ {1.5, 2.0, 2.5, 3.0, 5.0} on at least one architecture, reporting trigger frequency and final perplexity, would strengthen the robustness claims.
- Reporting mean and standard deviation of final perplexity across seeds (Table 1 only reports single values or instability frequencies) would help assess result stability.
- Evaluating the effect of PSS on downstream task performance (e.g., GLUE for BERT) at the expanded LRs would make the practical case more compelling, though this goes beyond the paper's stated scope on training stability.
- Showing that PSS measurably reduces SJE when triggered would improve internal consistency between the analysis and evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Formatting/typo criticisms:** The harsh critic's "Other Observations" list of typos ("singualrites," "by by 10 times," "5.10× should be 5–10×") are removed per policy — these are formatting artifacts or minor typos that do not affect scientific content.
- **"Does not discuss effect on downstream model quality (e.g., GLUE)":** Removed as scope creep — the paper focuses on training stability, not downstream task benchmarking. Moved to Nice-to-Haves.
- **"Does not report variance across seeds":** Removed from main weaknesses; the paper does report instability frequency across multiple trials. Moved to Nice-to-Haves.

## Novel Insights

The most interesting observation from the review process is that the paper's core contribution is actually two separable claims: (1) identifying the curse-of-singularities phenomenon (empirical analysis), and (2) proposing PSS as an intervention. The reviews converge on the analysis being convincing while differing on which parts of the method need more validation. The fact that all three robustness axes (rescue timing, smoothing policy, compatibility) are tested to some degree, yet the detection threshold remains unexamined, creates an asymmetry in the evaluation quality that can be fixed cleanly. The SJE critique is particularly noteworthy: it reveals that the paper's theoretical narrative and its experimental validation are partially decoupled — fixing this would improve the paper's internal coherence more than adding any single additional baseline.

## Suggestions

1. Add spectral normalization as a baseline in Table 1 and Figure 4(b). This is the most directly relevant stabilization method given that it also operates on singular spectra, and its absence is the single largest gap in the experimental comparison.
2. Either integrate SJE into the post-intervention analysis (e.g., show that PSS reduces SJE when triggered) or explicitly reframe SJE as a purely explanatory concept that does not need to be validated experimentally.
3. Report which smoothing function was used for the main results in Table 1 and Figure 4.
4. Add a brief τ sensitivity experiment (e.g., τ ∈ {1.5, 2.0, 2.5, 3.0, 5.0} on BERT-base at LR 4e-4) showing trigger counts and final perplexity.
5. Soften the "first to study" novelty claims and add a sentence in Section 2 or 5 explicitly distinguishing the paper's focus on *parametric* singularities (weight matrix stable rank) from prior work on attention entropy collapse or representational rank collapse.

## Score and Decision

**Overall assessment:** The paper makes a solid empirical contribution by identifying a concrete, measurable mechanism linking parametric singularities to training instability under large LRs, and proposes a lightweight, effective intervention. The experimental evidence is clear: PSS demonstrably expands the usable LR range by 5–10× across multiple model scales, can rescue training after instability has already occurred, and adds negligible overhead. The weaknesses are addressable — limited baselines, an under-validated theoretical construct (SJE), an unspecified smoothing function, and overeager novelty claims — but none invalidate the core contribution. With the suggested revisions, this would be a strong paper.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>