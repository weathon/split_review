Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

This paper proposes SigMap, a wireless localization foundation model with two innovations: (1) cycle-adaptive masking that dynamically generates mask patterns based on detected CSI periodicities to prevent shortcut learning, and (2) a map-as-prompt framework that encodes 3D geographic geometry via a GNN into a soft prompt prepended to frozen CSI tokens. The method achieves strong results on DeepMIMO (1.564m MAE single-BS, 0.673m MAE multi-BS), outperforming the best baseline LWLM by 34.4% and 18.7% respectively, and demonstrates few-shot cross-scenario transfer to two unseen environments while updating only a fraction of parameters.

## Strengths

- **Cycle-adaptive masking is well-motivated and effective.** The masking strategy dynamically detects periodicity via cross-correlation and generates shift-aware mask patterns to prevent shortcut learning. Table 3 shows it reduces multi-BS MAE to 0.673m vs. 0.770m (grid) and 0.753m (strip), with CDF@1m rising to 84.5%. The design is a reasonable response to a real problem (CSI periodicity enabling trivial reconstruction).

- **Map-conditioned prompt tuning provides substantial gains.** The GNN-based geographic prompt encoding 3D building geometry as a learnable soft token improves single-BS NLoS MAE from 2.275m (no map) to 1.564m (with 3D map), more than doubling CDF@1m (Table 4). The 2D bird's-eye-view ablation shows only 8% degradation (1.692m), confirming the prompt mechanism captures essential topological cues robustly.

- **Strong cross-scenario transfer results.** On DeepMIMO O2 and WAIR-D Scenario-2 (100 cities), SigMap with map prompts achieves 1.026m and 1.880m MAE respectively, outperforming LWLM by 53.2% and 44.3% while only fine-tuning task heads with ~100 labeled samples per scenario (Section 4.5). The backbone remains frozen, demonstrating representational quality.

- **Well-designed ablation structure.** The paper isolates contributions via SigMap (w/o map) vs. baselines (architecture contribution), SigMap (w/ map) vs. w/o map (map contribution), masking strategy comparison (Table 3), and map modality comparison (Table 4). This allows readers to attribute gains to specific components.

- **Practical parameter efficiency.** Fine-tuning activates only 0.085M parameters (Table 5), with inference at 0.83ms/sample, making the approach feasible for deployment.

## Weaknesses

### Fatal

None.

### Major

- **NLoS-aware attention mechanism is introduced only in experimental results and is absent from the methodology.** Section 4.2 introduces an "NLoS-aware attention mechanism" with a learnable weight matrix W_NLoS (Eq. 11) that "allows the model to differentiate between direct and reflected paths, significantly reducing positioning ambiguity." The text attributes the key single-BS advantage to this mechanism. However, this component is never described in Section 3 (Methodology), leaving critical questions unanswered: where does the model obtain path-type information (explicit LoS/NLoS labels? learned implicitly?), how is this attention integrated into the forward pass, and is it part of pre-training or fine-tuning? The omission makes the single-BS NLoS results impossible to fully assess and reproduce, and it undermines confidence that the reported gains come from the claimed innovations (masking, map prompt) rather than from this undisclosed component.

- **"Zero-shot generalization" claim is misleading — the evaluation uses few-shot adaptation.** The abstract and introduction repeatedly claim "zero-shot generalization in unseen environments," but Section 4.5 explicitly states that approximately 100 labeled target samples per scenario are used to fine-tune downstream task heads. This is few-shot adaptation, not zero-shot generalization. The distinction is fundamental: zero-shot requires no target-domain labels whatsoever, while here labeled data is used to update model parameters. The few-shot results themselves are strong and worth reporting, but the inflated terminology damages the paper's credibility and should be corrected throughout.

### Minor

- **Data representation is inconsistent between main text and appendix.** The main text (Eq. 5, Section 3.2) describes CSI preprocessing as real/imaginary decomposition: X = [ℜ(H), ℑ(H)]. The appendix (Eq. 12, B.2) describes it as magnitude/phase decomposition: H_s = [|H_s|, ∠H_s]. These are not equivalent transformations (different information content and mathematical properties), and the paper should clarify which is actually used. The appendix hyperparameters table further lists "C: Channel dimensions (2 for real/imaginary components)" (line 833), compounding the confusion.

- **Cycle-adaptive masking evaluation could be stronger.** The only quantitative evidence for the masking strategy is Table 3 (multi-BS localization). While the improvement over grid/strip masking is meaningful (0.673m vs 0.770m/0.753m), no statistical significance is reported, no probing experiments test whether the pre-trained representations actually capture more global features, and no analysis of reconstruction difficulty vs. random masking is provided. The central motivation — that cycle-adaptive masking forces learning of globally meaningful representations rather than exploiting periodic shortcuts — is supported only indirectly through downstream localization performance.

- **The paper overclaims what the experiments demonstrate about map integration mechanisms.** While the "w/o map" ablation correctly isolates the map contribution, the paper does not compare its prompt-based map integration against simpler map integration alternatives (e.g., concatenating a map embedding to CSI features, or using a 2D CNN on a bird's-eye-view image). Without such a comparison, the claim that the *prompting mechanism specifically* is superior to alternative map fusion methods remains untested. The comparison of 3D vs 2D map quality (Table 4) is helpful but addresses a different question (map quality, not fusion mechanism).

### Trivial

- Section 4.4 claims "near-overlapping error bars" (line 564) when comparing 3D and 2D map variants, but Table 4 contains no error bars or standard deviations. The paper states results are averaged over 5 runs (Section 4.1), but the uncertainty estimates are not shown.

- The parameter efficiency percentages differ between sections (0.7% in Section 4.6 vs. 0.4% in Section 4.5). While this likely reflects different fine-tuning scopes (full prompt tuning vs. task-head-only), the distinction is not clearly explained.

## Nice-to-Haves

- Equipping a strong baseline (e.g., LWLM) with the same 3D map information via a simpler integration mechanism (e.g., concatenation) and comparing against the prompt-based approach would more rigorously isolate the benefit of the prompt tuning design.

- Conducting zero-shot evaluation (no target-domain labeled samples at all) to properly test whether the frozen pre-trained backbone alone can generalize across environments, or retracting the "zero-shot" language entirely.

- Visualizing what the geographic prompt learns — e.g., which building structures or spatial relationships the attention weights emphasize for a given scene — would support interpretability claims.

## Removed Points

These points from the input reviews were flagged and removed after verification against the paper.

- **"Baseline comparison is unfair because baselines are not given access to map information" (Harsh Critic Point 2).** The paper includes SigMap (w/o map) as its own baseline, which already outperforms LWLM, SWiT, and CNN without any map access. This controls for architecture vs. map contribution. The remaining question about prompt mechanism vs. simpler map integration is kept as a Minor weakness above.

- **"Map ablation spin: 8% gap weakens case for 3D-specific pipeline" (from Harsh Critic Point 5).** The paper honestly presents this as "most gain comes from topological/LoS cues" and frames it as robustness to simplification (line 571), not as 3D superiority. This is a valid observation, not spin.

- **"No justification for Delaunay triangulation" (from Harsh Critic Point 5).** The paper states "To capture the inherent proximity relationships in 3D space, the edge set E is constructed using Delaunay triangulation" (line 350-351). Delaunay triangulation is a standard spatial graph construction method; extensive justification is not required for a well-known technique.

- **"The paper should have tested on real-world measurement data" (from Harsh Critic Missing Experiments).** Ray-tracing data (DeepMIMO, WAIR-D) is standard in the wireless localization literature and the paper's scope is explicitly simulation-based. This is scope creep.

- **Strength Finder's "zero-shot generalization" strength claim.** This was dropped because the zero-shot claim conflicts with the verified weakness (few-shot adaptation with ~100 labeled samples). The cross-scenario transfer results remain a strength but must be characterized correctly as few-shot.

- **Generic strength: "The problem of leveraging 3D environmental context for wireless localization is timely and practically relevant."** This is too generic — dropped.

## Novel Insights

The paper's observation that wireless CSI periodicity can be exploited as a shortcut in masked autoencoding — and that adaptive, shift-aware masking based on cross-correlation analysis can disrupt this — is a genuinely useful insight for the growing subfield of self-supervised learning on wireless signals. This is a domain-specific challenge that naive transfer of vision MAE approaches would miss. Additionally, the finding that most of the map benefit comes from 2D topology rather than full 3D geometry (Table 4) is a practical insight that could inform simpler deployment pipelines.

## Suggestions

- Either retract "zero-shot" terminology and replace with "few-shot" throughout the abstract, introduction, and conclusion, or conduct a genuine zero-shot evaluation with no target-domain labels.
- Describe the NLoS-aware attention mechanism in the methodology section (Section 3.4 or 3.5), including how path-type information is obtained, how the attention is computed, and where it fits in the forward pass. If the mechanism requires explicit LoS/NLoS labels from ray-tracing, this should be disclosed as an additional input assumption.
- Clarify which CSI preprocessing is actually used (real/imaginary vs. magnitude/phase) and make it consistent between main text and appendix.
- Report standard deviations or confidence intervals alongside all main results, since the paper already states 5-run averaging.

---

Now let me calibrate my score. Here are all the anchors returned by the search, with my assessment of how this paper compares:

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| AEMP (CSI localization SSL) | `/home/wg25r/review_agent/human_reviews_2026/3AbyfpQgR2.md` | 5.33 | Most comparable topic. AEMP has a self-supervised pre-training framework for CSI localization with masked reconstruction + autoregressive prediction. SigMap is stronger: more comprehensive experiments (cross-dataset transfer vs. single-dataset), larger margins over baselines, and the map-as-prompt is a more genuinely novel contribution than the MR+AP combination. Both have presentation issues. SigMap should score higher than AEMP. |
| SpaRTran (wireless channel SSL) | `/home/wg25r/review_agent/human_reviews_2026/fNC3aaGeIa.md` | 3.50 | SpaRTran shows weaker novelty (adapts gated SAE from LLM interpretability) and has scalability issues. SigMap has substantially more contribution and stronger results. SigMap is clearly stronger. |
| Diffusion^2 (RF from 3D) | `/home/wg25r/review_agent/human_reviews_2026/teTUSK98gA.md` | 3.50 | Diffusion^2 has modest novelty and limited evaluation. SigMap's approach is more complete and better evaluated. SigMap is stronger. |
| AGG-RL (sound source localization) | `/home/wg25r/review_agent/human_reviews_2026/bWXpJFesLS.md` | 5.33 | Different modality but similar spirit (physics-informed representation learning for localization). AGG-RL is well-executed with good generalization results. SigMap has comparable quality but with a methodological gap (NLoS attention). Comparable level. |
| WaveVerse (RF simulation) | `/home/wg25r/review_agent/human_reviews_2026/O0czoZPSZ1.md` | 5.00 | WaveVerse has a creative concept but limited evaluation. SigMap has stronger empirical evidence. SigMap is stronger. |
| Special Unitary Parameterized Estimators | `/home/wg25r/review_agent/human_reviews_2026/VaS6xcDrTb.md` | 8.50 | Completely different topic (rotation estimation), very strong theoretically. SigMap is a different kind of paper (empirical systems vs. theoretical) and not at this level of polish or theoretical depth. |
| EEG Source Localization | `/home/wg25r/review_agent/human_reviews_2026/rIIpKdKzkC.md` | 1.60 | Weak paper across the board. SigMap is clearly far stronger. |

**Score reasoning:** SigMap is stronger than the 3.5-4.0 band papers (SpaRTran, Diffusion^2, nGRF) which have modest novelty or evaluation gaps. It is comparable to or somewhat stronger than AEMP (5.33) and AGG-RL (5.33) — better experimental breadth, more novel components, but with its own issues (zero-shot overclaim, NLoS attention undisclosed). It is not at the 8+ level of theoretically deep, flawlessly executed papers.

The zero-shot overclaim and the NLoS attention omission are real substantive issues, but (a) the zero-shot issue is a wording problem — the few-shot results are still strong, and (b) the NLoS attention gap can be addressed with clarification in a rebuttal, as it's likely a component that exists but was poorly described. These pull the score down from what could otherwise be a ~7.0 paper.

I'll place this at **6.0** — a clear accept with revisions needed, above the borderline 5.33 papers but with acknowledged issues that prevent a higher score.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>