Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

This paper studies Dual-level Noisy Correspondence (DNC) in Multi-Modal Entity Alignment (MMEA), a problem where both intra-entity (entity-attribute) and inter-graph (entity-entity, attribute-attribute) correspondences can be noisy. The authors propose RULE, a framework that: (1) estimates correspondence reliability via uncertainty and consensus modeling, (2) divides pairs into clean/intermediate/noisy subsets for tailored robust training, and (3) optionally employs a test-time MLLM reasoning module (TTR) to uncover latent attribute connections. Experiments on five benchmarks show substantial gains over seven baselines.

## Strengths

1. **First formal treatment of dual-level noise in MMEA.** The paper provides a crisp definition of DNC (Section 2.1) distinguishing intra-entity noise (entity-attribute misassociation) from inter-graph noise (entity-entity and attribute-attribute misalignment), and empirically motivates the problem in Fig. 1(b). This is a realistic problem that prior work has not jointly addressed.

2. **Principled two-fold reliability estimation.** The paper proves (Theorem 1) that uncertainty alone is insufficient and introduces consensus as a complementary principle. Fig. 4 shows that uncertainty + consensus cleanly separate the three subsets \(S_U, S_I, S_C\), supporting the tailored loss design. This combination is well-motivated and validated.

3. **Training-time components deliver substantial gains without the MLLM.** The ablation (Table 3) shows RULE without TTR achieves H@1 = 56.5 on ICEWS-WIKI Non-name 50% DNC, versus 42.4 for the best baseline (MEAformer) — a 14.1-point margin. This cleanly demonstrates that the core DNC-handling method (uncertainty/consensus estimation + dually robust losses) is effective on its own, independent of the test-time MLLM.

4. **Extensive and well-designed evaluation.** Experiments span 5 datasets (including two challenging ICEWS benchmarks with high inherent noise) and 3 noise levels (inherent, 20%, 50%), with consistent state-of-the-art results across all settings. Tables 1-2 report H@1, H@5, and MRR.

5. **Analytical validation of internal mechanisms.** Fig. 3(b) confirms that clean pairs receive high reliability scores and noisy pairs low scores; Fig. 5 shows that the learned reliability weights correctly downweight injected intra-entity noise. These visualizations substantiate that the method behaves as intended.

## Weaknesses

### Fatal
None.

### Major

1. **The main comparison tables (Table 1, 2) present "Ours" only in the full configuration (with TTR), while baselines have no analogous MLLM module.** Although the ablation in Table 3 (on one dataset) confirms that RULE without TTR still dramatically outperforms baselines, the reader cannot verify this pattern across all five datasets from the main tables. Including a "RULE (w/o TTR)" column in Tables 1-2 would cleanly separate the contribution of the training-time DNC-handling method from the additional MLLM-based reasoning, making the comparison fully transparent. As it stands, the headline numbers conflate two distinct contributions.

2. **The value function in the consensus estimation (Section 2.2.2) is ambiguously defined.** The formulation \(v(\pi) = \max\big(\frac{1}{|\pi|}\sum_{j\in\pi} s_i^j\big)\) never explicitly states what \(s_i^j\) denotes (whether it is a scalar or a vector) or what the \(\max\) operates over. From the downstream usage in Eq. (7) / line 137 — where \(\arg\max\) applies to \(\frac{1}{|\pi^*|}\sum_{m\in\pi^*} s_i^m\) — it can be inferred that \(s_i^j\) is a similarity vector over candidate entities and \(\max\) picks the best candidate score, but this is not spelled out. Combined with Assumption 1 (marginal contribution sign indicates correctness), which is stated without any empirical validation, the consensus estimation procedure is harder to assess and reproduce than it should be. Clarifying the notation and validating Assumption 1 (or relaxing it) would strengthen the paper.

### Minor

3. **The pair-division threshold uses \(S^{TP} = \{i \mid \arg\max(s_i) = \arg\max(y_i)\}\), where \(y_i\) itself may be noisy** (Section 2.2.3). The rationale — that agreement between model prediction and annotation indicates a clean pair — is defensible, but the paper does not discuss how errors in \(y_i\) could propagate into the threshold setting or analyze the quality of \(S^{TP}\) under high noise. A brief analysis or caveat would suffice.

4. **No statistical variance or multiple-seed results are reported.** Given that the noise injection procedure is random (random replacements/perturbations), reporting results from a single run makes it difficult to assess the stability of the observed margins. This is a common practice gap in the MMEA literature, but the paper would benefit from adding variance estimates.

5. **Sensitivity of the greedy strategy's initial subset \(\pi_0\) is not analyzed.** The choice \(|\pi_0| = \lfloor M/2 + 1\rfloor\) (Eq. 7) could affect which attributes are selected, but no sensitivity study is provided. A brief analysis or justification would increase confidence in the method's robustness.

### Trivial

6. The notation in Eq. (7) uses \(\arg\max_{\frac{1}{|\pi^*|}\sum_{m\in\pi^*} s_i^m}\) with the expression as a subscript; this is nonstandard formatting and could be rewritten for clarity.

## Nice-to-Haves

- An analysis of the computational cost of the TTR module (inference time per entity, FLOPs) would help readers assess practical deployment trade-offs, though this is not required to validate the paper's core claims.
- Applying the same MLLM-based CoT reasoning to the best baseline's outputs as an additional controlled experiment would further isolate the effect of RULE's training-time design, though the existing ablation already addresses this concern.

## Removed Points

These points from the reviewers have been removed following the filtering guidelines. Treat them with caution — some may reflect misunderstandings or overstatements.

1. **"Unfair comparison — massive resource advantage conflates contributions"** (from Harsh Critic, Critical Issue 1). *Reason for removal:* The claim that the central claim of superiority is "not supported" is factually contradicted by the paper's own ablation data (Table 3): RULE w/o TTR (56.5) already outperforms the best baseline (42.4) by 14.1 points on ICEWS-WIKI Non-name 50% DNC. This makes clear that the training-time DNC-handling method drives the majority of gains. The issue is one of presentation transparency (covered in Major Weakness 1), not a fatal confound. The critic's stronger framing is unwarranted.

2. **"Circular dependency in pair division"** (from Harsh Critic, Section-by-Section Notes on Section 2.2.3). *Reason for removal:* The set \(S^{TP}\) uses agreement between the model's prediction (\(\arg\max(s_i)\)) and the annotation (\(\arg\max(y_i)\)). Agreement-based filtering is a standard co-training/self-training strategy, not a circular dependency. The concern is overblown; a softened version is retained as Minor Weakness 3.

3. **"Missing appendix/prompt details for TTR module"** (from Harsh Critic, Section-by-Section Notes on Section 2.5). *Reason for removal:* The parser strips appendices from all papers; the details exist in the original submission. Per the hard rules, missing appendix content is not a valid weakness.

4. **"Novelty of DNC overstated — prior work considered noisy correspondences"** (from Harsh Critic, Section-by-Section Notes on Introduction). *Reason for removal:* The paper explicitly defines DNC as *dual-level* noise (intra-entity AND inter-graph), which is distinct from prior work on uncertain correspondences (Chen et al., 2024) that focuses on inter-graph alignment uncertainty. The dual-level framing is a genuine contribution, not an overclaim.

5. **"Weakness about impracticality/cost as a 'misrepresentation'"** (from Harsh Critic, Critical Issue 3 and rephrased as misrepresentation). *Reason for removal:* Downgraded to Nice-to-Have. The paper does not claim computational efficiency as a contribution; the TTR module is presented as an optional enhancement. Discussing cost would improve the paper but omitting it is not a flaw that undermines the contribution.

6. **"DNC claim in ICLEWS exceeding 50% noise"** (from Harsh Critic indirectly). *Reason to downgrade: The paper states "over 50% in ICEWS benchmarks" and says statistics are in Appendix B. Since the appendix is stripped, this claim is unverifiable in the provided text but the weakness about it would be about missing appendix content, which should be removed per rules.*

7. **Strength Finder's point about "Code released for reproducibility".** *Reason for removal:* While this is a positive supporting detail, generic code-availability statements are dropped per the filtering guidelines since they are not a substantive strength of the scientific contribution. The paper's substantive strengths (problem definition, method design, empirical results) are retained in the main Strengths section.

## Novel Insights

The most interesting observation that emerges from these reviews — and goes beyond what the paper itself explicitly says — is that the greedy marginal-contribution strategy for consensus estimation is both the method's most novel technical move (using Shapley-value-style reasoning to infer clean attribute subsets without ground-truth correspondence labels) and its least explained component. The reviewers independently fixated on this as a weak point, which suggests the authors would benefit from significantly expanding the exposition of this part: defining the notation concretely with an example, validating Assumption 1 on a small held-out set, and showing what happens when the assumption is violated. The paper would also be strengthened by explicitly showing that the two-fold principle (uncertainty + consensus) is not just a heuristic but follows from a formal characterization of when uncertainty alone fails (Theorem 1 already begins this but the consensus definition is more ad-hoc).

## Suggestions

- Add a "RULE (w/o TTR)" column to the main comparison tables (Tables 1-2) so readers can assess the training-time contribution independently across all datasets.
- Clarify the notation in Section 2.2.2: explicitly state that \(s_i^j\) is a similarity vector over candidate entities and that \(\max\) selects the highest similarity entry. Consider adding a small illustrative example.
- Validate Assumption 1 empirically: on a held-out clean subset, compute the marginal contribution \(\Delta\) for correctly vs. incorrectly associated attributes and show that the sign pattern holds statistically.
- Add variance statistics (e.g., 3 random seeds) for the main results under synthetic noise injection.
- Discuss the computational cost of the TTR module (inference time per entity) and acknowledge its practical limitations, even if briefly.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>