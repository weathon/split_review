Now I have a thorough calibration. Let me write the consolidated review.

## Summary

This paper introduces a novel problem formulation in machine unlearning: label domain mismatch, where the target concept to be forgotten does not align with the class label of the trained model. It defines four scenarios (all matched, target mismatch, model mismatch, data mismatch) illustrated in Figure 1, systematically reveals why existing methods fail on these scenarios through a theoretical lens of "representation gravity" (Theorem 3.2), and proposes TARF — a framework combining annealed gradient ascent on forgetting data with target-aware gradient descent on hard-to-affect remaining data. Extensive experiments across CIFAR-10/100, Tiny-ImageNet, ImageNet-1k, plus LLM and diffusion model case studies demonstrate that TARF achieves dramatically lower Gap with the retrained reference than all baselines on mismatch tasks (e.g., Gap of 0.21 vs. 8.86 for the best baseline on CIFAR-100 target mismatch).

## Strengths

1. **Novel and practically motivated problem formulation.** The paper systematically defines label domain mismatch in class-wise unlearning (Section 3.1, Figure 1), expanding the scope beyond the conventional all-matched scenario that prior work (Golatkar et al., 2020; Jia et al., 2023; Chen et al., 2023) assumed. The four scenarios (target mismatch, model mismatch, data mismatch) model realistic situations where user-reported cases and pre-training taxonomies diverge — a genuine gap in the literature.

2. **Theoretical insight connecting representation distance to forgetting dynamics.** Theorem 3.2 (Section 3.2) bounds the loss change during gradient ascent unlearning by the representation distance between data subsets. While the bound involves unobservable quantities, it provides a principled motivation for why existing methods fail in mismatch scenarios (Remarks 3.2, 3.3) and grounds the design of TARF's identification step — going beyond the purely empirical contributions common in the unlearning literature.

3. **Empirical effectiveness on mismatch tasks.** Table 3 shows that TARF achieves drastically lower Gap (aggregate deviation from the retrained reference) than all baselines on target mismatch and data mismatch scenarios. For example, on CIFAR-100 target mismatch, TARF obtains Gap=0.21 vs. GA's 8.86 (next best); on CIFAR-10 data mismatch, TARF obtains Gap=0.96 vs. GA's 5.89. No prior method performs well across all four settings, demonstrating that TARF solves a problem that earlier methods cannot.

4. **Generalization beyond controlled benchmarks.** The paper validates TARF on concept removal in stable diffusion (Figure 6) and information removal on the TOFU dataset with LLaMA (Table 5), demonstrating the framework's applicability outside image classification.

5. **Systematic ablations and analysis.** Figure 7 examines the effect of the annealing parameter \(k\), the benefit of dynamic vs. constant gradient ascent schedules, sensitivity to model architectures, and the choice of operation on selected data. These ablations provide evidence for why each component of TARF is necessary.

## Weaknesses

### Fatal

None.

### Major

None that rise to the level of undermining acceptance. The paper's core claims are well-supported by the evidence presented.

### Minor

1. **Framing tension between concept-level language and data-level evaluation.** The paper describes the target concept (e.g., "people") as the object of forgetting (Figure 1b, 1d) and discusses "false retaining data not completely forgotten" as a challenge. However, the gold standard retrained model is trained on \(\mathcal{D}_r = \mathcal{D} \setminus \mathcal{D}_f\) (data-level forgetting), which by design does NOT forget the false retaining data either. This creates a tension in the narrative: the paper sometimes sounds like it is aiming for concept-level forgetting, while the actual evaluation measures data-level approximation of retraining. The evaluation is internally consistent with the stated goal in Eq. 1, but the framing could confuse readers. The paper would benefit from explicitly clarifying that "target concept" is used to describe the *scenario*, not to redefine the unlearning target — which remains the retrained model on \(\mathcal{D} \setminus \mathcal{D}_f\).

2. **Theoretical bound has limited practical utility.** Theorem 3.2 involves the largest eigenvalue of the Jacobian \(\lambda_{\max}(J_\theta)\) and the Lipschitz constant \(C_\ell\), both of which are unobservable in practice. The bound serves as directional motivation rather than a design principle. The key algorithmic choices (threshold \(\beta\), annealing schedule, gradient operations on selected data) are justified empirically rather than derived from theory. This is acceptable for an empirical systems paper, but the contribution statement in Section 1 ("we systematically reveal the challenges...") overclaims slightly relative to what the theory delivers.

3. **Some hyperparameters are heuristically set.** The identification threshold \(\beta\) is set via "top-10% accuracy drop" (Section 3.3), and the transition times \(t_0, t_1\) are not given principled selection criteria. While the ablation on \(k\) (Figure 7, left) is informative, a sensitivity analysis for \(\beta\) and \(t_0, t_1\) across multiple scenarios would strengthen the paper's claims of robustness.

4. **TOFU table shows suspicious identical values.** In Table 5, TARF(GA) and TARF(NPO) produce identical QA probability values across several settings (e.g., 0.0762/0.0824 for All-matched, 0.0095/0.0094 for Target Mismatch). If this is a formatting artifact (which the PDF extraction may have introduced), it should be clarified. If the values are genuinely identical, an explanation is needed since the base methods (GA vs. NPO) differ.

### Trivial

- Table 3 shows TARF slightly exceeding the Retrained reference on UA for Model Mismatch CIFAR-10 (91.11 vs. 87.76). This is expected behavior due to superclass-level evaluation and is clarified by the fine-grained Table 2, but a brief note in the caption would help.
- The three-phase narrative (Section 3.3, Remark 3.3) over-complicates what is fundamentally a single dynamic loss with two terms and a time-varying schedule. The paper acknowledges this is a "unified framework," but the phase framing may mislead casual readers into thinking there are separate training stages.

## Nice-to-Haves

- A concept-level gold standard (retrained on \(\mathcal{D} \setminus \mathcal{D}_t\), i.e., excluding all data belonging to the target concept) would provide an informative additional reference point for target/data mismatch scenarios, even if the paper's primary goal remains data-level forgetting.
- Compute cost breakdown for the identification phase (Phase I) — the time overhead appears modest from Table 3, but explicit reporting would strengthen reproducibility.
- Statistical significance indicators (\(\pm\) std) in the main tables, which the paper states are deferred to Appendix F.7.

## Removed Points

- **"Evaluation framework is inconsistent with problem formulation" (harsh critic, first major section).** This criticism is removed because it misunderstands the paper's evaluation. The paper's stated goal (Eq. 1) is to approximate the retrained model on \(\mathcal{D}_r = \mathcal{D} \setminus \mathcal{D}_f\). The evaluation (UA on \(\mathcal{D}_f\), RA on \(\mathcal{D}_r\), Gap vs. Retrained) is fully consistent with this goal. The concept-level language in Figure 1 describes the *scenario*, not the forgetting target. The "false retaining data" discussion explains *why existing methods fail* to approximate retraining in these scenarios — it does not redefine the goal to concept-level forgetting. Retained as Minor Weakness #1 above (framing tension) instead of the stronger version the critic asserted.

- **"The three-phase framing is misleading" as a structural weakness.** The paper explicitly states in Remark 3.3: "Note that the three-phase are interpreted from a unified framework rather than an ad-hoc pipeline." The critic's point is acknowledged but downgraded to a minor presentation note.

- **"Missing retrained reference cost" and "statistical significance" and "computation cost of identification."** These are either addressed by the paper (std values in Appendix F.7) or are standard for page-limited conference papers. Removed per the hard rules about appendix content and formatting.

- **Strengths from Strength Finder that are generic ("novel problem formulation" as stated is fine, but the framing is kept).** The Strength Finder's "empirical effectiveness in the new mismatch settings" is kept as it's specific and evidence-backed. The "demonstration on real-world applications" and "systematic ablation analysis" are also kept as they are concrete.

## Novel Insights

The most interesting synthesis to emerge from the reviews is that the paper's central contribution may be best understood not as "TARF approximates retraining better" but as "TARF identifies and handles latent target concepts that were never explicitly labeled." The representation gravity insight (Theorem 3.2) suggests that gradient dynamics during unlearning can serve as a probe into the model's representational structure — revealing which data points are semantically related even when they have different labels. This reframes the paper's contribution: rather than a better optimizer for a known objective, TARF is a method for *discovering the implicit topology of the forgetting request* and adapting the objective accordingly. This perspective unifies the paper's theoretical, algorithmic, and empirical contributions more cleanly than the current "three-phase" narrative.

## Suggestions

1. Clarify the framing in Section 3.1: explicitly state that the evaluation target is \(\mathcal{D}_r = \mathcal{D} \setminus \mathcal{D}_f\) (data-level retraining) and that the concept-level language describes the scenario structure, not a different forgetting target. A one-paragraph "Clarification on the forgetting objective across scenarios" would resolve the framing tension.

2. Add a sensitivity study for the threshold \(\beta\) (e.g., varying the percentile from top-5% to top-20%) and for the transition times \(t_0, t_1\) — these are the main practical hyperparameters users need to set.

3. Investigate and explain the identical TARF(GA)/TARF(NPO) entries in Table 5, either correcting a formatting error or explaining why the base forgetting method does not affect TARF's output in those settings.

4. Consider softening the claim in Eq. 4 that \(L_{\text{TARF}} \to L_{\text{retrain}}\) to a more nuanced statement, since the convergence is by design (annealing \(k(t)\) to zero and \(\tau\) selecting a subset of \(\mathcal{D}_{\text{un}}\)) rather than by proven convergence of the learning dynamics.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
- Weak band (<3.5): hvTFoDsgCe (avg 2.50), PL0uEscEkD (avg 2.00), 62nHvQRfaw (avg 2.00), WNUDOLYlbh (avg 3.00) — Papers with withdrawn/reject decisions; clearly weaker than the reviewed paper which has extensive experiments and a novel problem formulation.
- Middle band (3.5–7.5): N8AMUF0ZeE (avg 4.00, Reject), m3FOf6nKnU (avg 4.50, Reject), pwkZFrmSS8 (avg 4.00, Reject), 4WMBSHHJEr (avg 5.50, Accept Poster) — Most relevant comparison. The Retain-Forget Entanglement paper (5.50) is the closest in topic and was accepted as a poster. Our paper has a more novel problem formulation and broader experimental scope.
- Strong band (>7.5): No directly comparable unlearning papers returned; the top results were about RL, language models, and multimodal reasoning (scores ~8.0, similarity ~0.6). This confirms the paper does not reach the oral-level tier.

**Round 1 bracket:** Between 5.0 and 7.0.

**Round 2 — Narrowing:**
- xG0mQ4Xsfm (avg 5.00, Accept Poster): REM paper about corrupted data unlearning. Our paper has stronger empirical coverage and a more principled method. Our paper is stronger.
- IPqUBL4R9x (avg 6.00, Accept Poster): Distributional unlearning with strong theory but weaker experiments. Our paper is comparable — stronger on the empirical side, weaker on the theory side.
- dHz2LBCyTh (avg 6.00, Accept Poster): Newton-based unlearning with theoretical contributions but limited empirical novelty. Our paper has more practical novelty.
- Ryc7jKP6H9 (avg 5.60, Accept Poster): Diffusion unlearning with CARE concept. Different domain but similar motivation about preserving related concepts. Our paper has broader scope.

**Final Score: 6.0** — The paper makes a solid contribution with a novel problem formulation, clean method, and extensive experiments. It is comparable to or slightly above accepted poster papers like "Machine Unlearning under Retain–Forget Entanglement" (5.5) and "Distributional Machine Unlearning" (6.0). The main weakness (framing tension) is minor and addressable. The paper does not reach the oral-level band (no unlearning papers scored 8+ with relevant similarity).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>