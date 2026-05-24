Now I have enough to calibrate. Let me write the final review.

**Calibration Summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Masked VAE (tt0SCefKQL) | 3.00 | R1 | Our paper is clearly stronger — has real technical contributions and empirical validation |
| MLO-MAE (oVZ9XaOSFK) | 4.40 | R1 | Our paper is stronger — method is sound, issues are framing rather than fundamental fairness |
| Bayesian Prompt Tuning (XjlZJJFyla) | 5.00 | R2 | Comparable — both have real novelty but significant issues; theirs: missing baselines/weak comparisons; ours: overclaiming/mislabeling |
| SSL Positional Features (nf4v09zw6O) | 5.25 | R1 | Our paper is slightly weaker — theirs had clean scope but limited novelty; ours has more novelty but worse framing |
| CLIP Generalization (tnBaiidobu) | 5.75 | R2 | Our paper is weaker — theirs was cleanly scoped and honest; our overclaims pull it down |
| Visual Concepts (74vnDs1R97) | 5.80 | R2 | Our paper is weaker — theirs was well-scoped analysis; ours has framing problems |
| Specialized FMs (JYTQ6ELUVO) | 6.50 | R2 | Our paper is clearly weaker — theirs rigorously demonstrated overclaims; ours commits them |
| Wi-GATr (9TClCDZXeh) | 7.00 | R1 | Our paper is clearly weaker — theirs had real-world validation, new datasets, clean framing |

**Round 1 bracket**: 4.0–6.5
**Round 2 narrowed**: 4.5–5.5 → Final score: **5.0**

---

## Summary

This paper proposes SigMap, a two-stage framework for wireless localization that combines (1) cycle-adaptive masked pre-training on CSI data to prevent periodic shortcut learning, and (2) a geographic prompt-tuning mechanism that encodes 3D map information via GNNs and prepends it as soft prompts to a frozen transformer backbone during fine-tuning. The method is evaluated on single-BS and multi-BS localization tasks using ray-tracing datasets (DeepMIMO, WAIR-D).

## Strengths

- **Cycle-adaptive masking is a genuine technical contribution.** The masking strategy dynamically adapts to detected CSI periodicity (Equation 6), and the ablation in Table 3 confirms it yields better downstream localization than fixed grid or strip masking (MAE 0.673m vs. 0.770m and 0.753m, respectively). The core insight — that periodic signals enable reconstruction shortcuts and must be disrupted for the model to learn meaningful propagation features — is well-motivated.

- **Map-conditioned prompt tuning consistently improves localization accuracy.** Adding geographic prompts reduces single-BS MAE from 2.275m to 1.564m (Table 1) and multi-BS MAE from 0.789m to 0.673m (Table 2). The prompt generation pipeline (Algorithm 1, Figure 4) is cleanly designed: Delaunay triangulation constructs a spatial graph over building vertices and BS positions, which a small GCN encodes, and the resulting vector is projected into the transformer's token space. The 2D-vs-3D ablation (Table 4) usefully shows that most of the gain comes from topological/LoS cues rather than detailed 3D geometry.

- **Parameter-efficient adaptation is demonstrated.** Table 5 shows only 85k parameters (0.7% of the pre-trained model) are updated during fine-tuning, enabling 30-minute adaptation. This is a practical strength for deployment scenarios where full fine-tuning is expensive.

- **Evaluation spans multiple settings.** The paper evaluates single-BS, multi-BS, and NLoS conditions across DeepMIMO O1, O2, and WAIR-D Scenario-2, providing coverage of different task difficulties and environments.

## Weaknesses

### Fatal

None.

### Major

- **The "foundation model" framing is not supported by the evidence.** The model is pre-trained on a single urban scenario (DeepMIMO O1_3p5, Section 4.1). Foundation models are, by definition, pre-trained on broad, diverse data to learn representations that transfer across many settings. Pre-training on one layout — essentially one city block — does not establish that the learned representations are general or "foundational." The few-shot adaptation results on O2 and WAIR-D (Section 4.5) show some transfer, but this is a much weaker claim than what "foundation model" implies. The paper should either rescope its framing or pre-train on a genuinely diverse, multi-scenario CSI corpus. This is not a fatal flaw — the underlying method remains valid — but it is a structural misalignment between the paper's claims and its evidence.

- **The abstract and contributions claim "zero-shot generalization" but the experiments are few-shot.** The abstract (line 20) and contributions (line 55) state "strong zero-shot generalization in unseen environments." However, Section 4.5 explicitly describes fine-tuning the downstream task heads and geographic prompt module using "approximately 100 instances per scenario" and calls it a "few-shot learning setup" (line 329). This is few-shot adaptation, not zero-shot. No experiment reports direct inference from the pre-trained model without target-domain labeled data. This discrepancy between the claimed capability and the experimental evidence misrepresents what the method achieves and must be corrected.

- **The main results (Tables 1 and 2) are in-domain, not cross-scenario.** Both tables evaluate on DeepMIMO O1_3p5 — the same scenario used for pre-training. While fine-tuning on the pre-training environment is a valid evaluation, it does not test the generalization that the paper's title and abstract emphasize. The generalization experiments in Section 4.5 are the crucial evidence for cross-scenario transfer, yet they are presented as a subsection rather than as the main evaluation. Additionally, the labeled data amount used in Tables 1 and 2 is never specified, making it impossible to evaluate the "limited labeled data" claim.

### Minor

- **The "interpretable fusion" claim is unsupported.** Contribution 2 (line 54) states that geographic prompts "enable interpretable fusion of environmental constraints." No interpretability analysis — visualizations, attention maps, or case studies of how the prompt influences predictions — is provided. The GNN-based prompt is a projected vector fed into the transformer; its influence on predictions is opaque. This claim should either be supported with analysis or removed.

- **Baseline training protocols are not described.** The paper does not specify how LWLM and SWiT were pre-trained or fine-tuned — were they pre-trained on the same CSI data with comparable resources, and fine-tuned under the same labeled data regime? Without this information, the large performance gaps (e.g., SIGMAP w/o map vs. LWLM in Table 1) cannot be confidently attributed to methodological superiority rather than differences in training budgets or hyperparameter tuning.

- **Undefined metrics in Figure 5.** The radar chart uses "Overall" and "oss_scenario" as metric axes, but neither is defined anywhere in the paper. This makes the visualization uninterpretable.

### Trivial

- The paper states in Section 4.5 that SIGMAP reaches "1.580 m on WAIR-D Scenario-2" (line 352), while Table 4.5 reports 1.880m for SIGMAP (w/ map). These numbers should be reconciled.

## Nice-to-Haves

- An ablation isolating the effect of pre-training versus training the map-prompt-enhanced model from scratch on the same labeled data would clarify whether the pre-trained backbone provides a useful initialization beyond what the prompt alone adds.
- A deeper analysis of *why* cycle-adaptive masking helps — e.g., measuring whether fixed masking indeed allows periodic interpolation — would make the mechanism's contribution more concrete.
- Evaluation on real-world measured channel data (beyond ray-tracing simulators) would significantly increase practical significance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh critic: "The paper's suggestion that replacing the 2-D polygon with a street-level photograph... is speculative and not supported by any analysis."* → **Removed.** This is in the paper's own discussion section as a future direction suggestion, not a claim. Criticizing speculation in a future-work discussion is scope creep.
- *Harsh critic: "The description of how the frozen backbone processes this extended sequence in the multi-base station case is confusing."* → **Removed.** The paper describes the multi-BS fusion clearly in Section 3.5 with Equations 9–10; this is a reviewer comprehension issue, not a paper flaw.
- *Harsh critic: "The gap description implicitly treats 'exploiting periodic shortcuts' as a known failure mode... but the paper does not provide a demonstration that existing methods actually suffer from this."* → **Removed.** The paper argues theoretically that periodic patterns can be exploited as shortcuts, which is reasonable motivation without requiring empirical demonstration on specific baselines.
- *Harsh critic: "Parameter efficiency... does not by itself demonstrate practical advantage over full fine-tuning unless the method also preserves pre-trained knowledge better—a point that is not shown."* → **Demoted to Nice-to-Have.** The parameter efficiency is fairly reported; the missing comparison is a nice addition, not a flaw.
- *Strength Finder: "Strong zero-shot generalization across unseen environments... 1.880m MAE... outperforming the best baseline (LWLM) by 44.3%."* → **Removed.** The paper itself describes this as few-shot (~100 labeled samples), not zero-shot. The strength finder repeats the paper's overclaim.
- *Strength Finder: "Comprehensive evaluation spanning multiple scenarios and tasks."* → **Kept but tempered.** The evaluation is broad but the main tables are in-domain, which limits how much "comprehensive cross-scenario" credit it deserves.

## Novel Insights

The paper's combination of cycle-adaptive masking and geographic prompt tuning is a genuinely novel approach for wireless localization. The insight that CSI periodicity creates reconstruction shortcuts — and that dynamic, shift-aware masking can force learning of more meaningful propagation features — is specific to the wireless domain and not obvious from masked autoencoding work in vision or NLP. Similarly, encoding map geometry as a learnable soft prompt rather than as an explicit input feature is a clean design choice that decouples pre-training from environment-specific information. These insights, while modest in theoretical depth, are practically useful for the growing intersection of deep learning and wireless sensing.

## Suggestions

- **Rescope the paper honestly.** Replace "foundation model" with "self-supervised pre-training method" or similar. Replace "zero-shot generalization" with "few-shot cross-scenario adaptation." These are accurate descriptions of what was actually done and do not diminish the technical contributions.
- **Move cross-scenario results to the main evaluation.** The generalization experiments on O2 and WAIR-D (currently Section 4.5) are the paper's strongest evidence. Make them central, and clearly label Tables 1–2 as in-domain evaluation on the pre-training environment.
- **Report labeled data quantities** for all experiments, not just the generalization section.
- **Either provide interpretability evidence or remove the claim.** If attention maps or prompt influence visualizations exist, include them. Otherwise, drop "interpretable" from the contributions.
- **Describe baseline training protocols** (pre-training data, epochs, fine-tuning regime) so readers can assess comparison fairness.

## Score and Decision

This paper has genuine technical merit: the cycle-adaptive masking strategy and geographic prompt tuning framework are novel and the empirical results show consistent improvements over baselines. However, the paper is significantly weakened by a mismatch between its ambitious framing and its experimental evidence. The "foundation model" label is not supported by single-scenario pre-training, the "zero-shot" claim contradicts the few-shot evaluation actually performed, and the main results are largely in-domain. These are framing and presentation issues rather than fundamental methodological flaws — the underlying method works and the few-shot transfer results are meaningful. But they are serious enough that the paper, as written, overclaims what it demonstrates.

Compared to calibration anchors: stronger than MLO-MAE (4.40, rejected for fundamental experimental fairness issues), comparable to Bayesian Prompt Tuning (5.00, rejected for missing baselines and marginal novelty), but weaker than the CLIP generalization analysis (5.75, accepted for clean, honest scoping). The paper could be significantly strengthened through honest rescoping and modest additional experiments, but in its current form the overclaims prevent acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>