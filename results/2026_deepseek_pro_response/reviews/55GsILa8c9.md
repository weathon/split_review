Now I have enough comparison data. Let me finalize the review.

**Round 1 bracket:** Based on initial retrieval, CausalNovo clearly sits above weak-band papers (2.33–3.00) and the lower middle-band (4.25–5.67). The strong-band papers (8.00) have genuine theoretical contributions (identifiability proofs, rigorous SCM-derived results) that CausalNovo does not match. The initial bracket is **5.5–7.5**.

**Round 2 narrowing:** 
- RankNovo (5.50, Reject) — same domain, de novo peptide sequencing. CausalNovo is clearly stronger: principled approach vs. ensemble reranking, consistent improvements across architectures vs. modest gains tied to base model quality, better ablations.
- MADGEN (6.00, Accept) — mass spectrometry domain. CausalNovo has more thorough evaluation, better empirical results, and clearer contribution separation.
- 22ywev7zMt (5.67, Reject) — causal SCM + SSL, had significant theoretical gaps. CausalNovo is cleaner and better executed.
- 3n4RY25UWP (6.25, Accept) — disentanglement method with information criterion. Comparable empirical depth.
- q4SiDyYQbo (6.33, Accept) — contrastive learning investigation, strong theoretical contribution.
- OGtnhKQJms (7.00, Accept) — multi-view causal representation learning with identifiability proofs. Stronger theory than CausalNovo.

CausalNovo sits above the 5.5–6.0 tier but below the 7.0+ tier. My final score: **6.5**.

---

## Summary
CausalNovo introduces a model-agnostic framework for de novo peptide sequencing that aims to disentangle causal (signal ion) representations from non-causal (noise) representations. It formalizes the problem using a Structural Causal Model, derives independence and sufficiency principles, and operationalizes them through a Causality Extraction Module (CEM) that uses contrastive learning and cross-entropy objectives. The framework is integrated into three distinct baseline architectures and evaluated across three datasets, showing consistent improvements in amino acid, peptide, and PTM-level metrics.

## Strengths
- **Strong empirical motivation**: Figure 1 demonstrates that three well-trained baseline models all degrade substantially when noise peaks are perturbed, with tighter m/z tolerance thresholds amplifying the decline. This directly validates the paper's central premise that existing models rely on spurious correlations with noise.
- **Model-agnostic gains across diverse architectures**: CausalNovo delivers consistent improvements when integrated into three architecturally distinct baselines — CasaNovo (Transformer encoder-decoder), AdaNovo (conditional mutual information training), and π-HelixNovo (spectrum augmentation) — across three datasets and multiple metrics (Tables 1–2). Gains are substantial, e.g., +12.0% peptide precision on Seven-species for CasaNovo and +14.2% amino acid precision on HC-PT for AdaNovo.
- **Mechanistic validation via attention analysis**: Table 7 shows that CausalNovo shifts model attention toward causal peaks: predictions attending to all three causal peaks rise from 19.26% to 32.87%, while predictions ignoring causal peaks entirely drop from 12.73% to 10.76%. This provides evidence that the framework changes how predictions are made, not just the output.
- **Robust cross-NSR performance**: Figure 4 demonstrates that CausalNovo maintains and often widens its advantage over baselines as Noise Signal Ratio increases across all three baselines on HC-PT, with average improvements of +10.2% to +12.0%.
- **Cross-species generalization**: Table 3 shows CausalNovo improves over CasaNovo on all 8 held-out species individually with no regressions, supporting generalizability.
- **Systematic ablations**: Tables 4 and 5 provide component-level decomposition of both the learning objectives (independence, purification, symmetric training) and the intervention strategy (replace, enhance, drop), with the drop operation serving as an informative negative control.
- **Peak distinguish strategy robustness**: Table 6 evaluates CausalNovo (without retraining) using a comprehensive 18-ion-type set for noise identification, showing continued robustness (28.5% relative improvement at threshold=1), which partially addresses concerns about evaluation-training coupling.
- **Honest limitations**: The paper explicitly quantifies the 2.3× training time overhead and notes that evaluation follows NovoBench rather than the more realistic large-scale external corpus protocol.

## Weaknesses

### Fatal
None.

### Major
- **Causal framing gap**: The paper builds its narrative around SCMs, Reichenbach's Common Cause Principle, and do-calculus, but the operational method reduces to label-guided data augmentation (replacing peaks far from the theoretical spectrum), contrastive learning (InfoNCE-style), and cross-entropy objectives — all standard techniques. The paper never validates that the learned z_c satisfies any causal property (e.g., that conditioning on z_c renders X and Y independent, or that C ⟂ S holds empirically). The causal language, while providing useful motivation, overstates what the method actually delivers. The contribution is more accurately described as a noise-robustness framework using domain-knowledge-guided data augmentation and contrastive regularization. This matters because the paper's claimed novelty centers on the causal framing.
- **Unclear purification mechanism**: Section 3.3 claims that maximizing I(z_s; Y) "can indirectly lead to the purification of z_c." The reasoning is opaque — if both z_c and z_s are trained to predict Y, what prevents the model from placing redundant causal information in both representations? The paper appeals to Chen et al. (2022) but does not explain the specific mechanism. The ablation shows this term helps (+0.8% precision), so the empirical contribution is real, but the theoretical justification is weak.

### Minor
- **Partial evaluation-training coupling**: Both training intervention and vulnerability evaluation (Figures 1, 3) identify noise peaks using proximity to the theoretical spectrum with b/y/a ions. While Table 6 partially addresses this by using a broader 18-ion-type set for evaluation (without retraining), and the "causality enhancement" strategy actually makes evaluation harder (x_theory is added during training but not during testing), the concern is not fully resolved. A cleaner demonstration would train with one noise-identification strategy and evaluate with a different one.
- **Retraining variance unquantified**: π-HelixNovo drops from published 0.588 to retrained 0.532 on HC-PT peptide precision (Table 1). While CausalNovo still exceeds the original published result (0.656), reporting standard deviations across multiple seeds would improve confidence, especially since retrained baselines sometimes differ substantially from published results.
- **Cumulative ablation rather than leave-one-out**: Table 4 uses additive ablation (building up from baseline), which shows components help when added but does not establish that each component is necessary when others are present. A LOO design would be more informative.
- **Missing simpler baselines**: No comparison to standard regularization techniques like input peak dropout or SpecAugment-style masking. Table 5's "Drop" row provides a partial comparison, but additional baselines would strengthen the attribution of gains to the causal design rather than to regularization in general.

### Trivial
- The attention analysis (Table 7) assumes transformer decoder cross-attention is genuinely interpretable, citing π-xNovo. A brief discussion of whether this assumption has been validated in the de novo sequencing domain would strengthen the mechanistic claims.

## Nice-to-Haves
- Validate that the learned z_c actually satisfies causal independence (e.g., test whether z_c and z_s are decorrelated, or whether conditioning on z_c reduces dependence between X and Y).
- Compare against simple data augmentation baselines (random peak replacement without CEM/contrastive objectives) to isolate the contribution of the causal disentanglement mechanism from augmentation effects.
- Report training stability metrics (mean ± std over multiple seeds) for both baselines and CausalNovo-augmented models.
- Provide a computational cost comparison table (wall-clock time, GPU memory, FLOPs) to help practitioners assess the cost-benefit tradeoff.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Hyperparameter disclosure (α, γ)**: The harsh critic noted that α (fraction of peaks replaced) and γ (tolerance threshold) are not given specific values in the main text. Removed per hard rule — these values are likely specified in the stripped appendix.
- **"Self-fulfilling evaluation is structural/fatal"**: The harsh critic claimed the evaluation is circular because training and testing use the same noise-identification criterion, and that the causality enhancement (adding x_theory) gives an unfair advantage. Removed as overstated. Table 6 addresses the criterion concern (18 ion types, no retraining, still shows robustness), and the causality enhancement actually makes evaluation harder (x_theory is added during training but NOT during testing, so CausalNovo had more signal in training than evaluation). The residual concern is retained as a Minor weakness.
- **"CausalNovo has seen precisely this kind of spectrum during training"**: The harsh critic argued the model benefits from familiarity with x_theory-augmented spectra. This is factually misleading — x_theory adds ALL theoretical peaks during training, but evaluation uses only the actual observed signal peaks, making the test distribution harder. Removed.
- **Formatting/style nitpicks**: Removed per hard rule.

## Novel Insights
The paper's integration of a causal disentanglement framework into de novo peptide sequencing is novel for this domain. The key insight — that noise peaks (identified via domain knowledge of theoretical spectra) can serve as the target of "causal intervention" through replacement, and that contrastive learning on the resulting representations can enforce invariance — is a creative application of causal representation learning principles to a practical problem where causal structure is partially known through domain expertise. The vulnerability analysis (Figure 1) itself is a valuable methodological contribution for evaluating noise robustness in this domain.

## Suggestions
- Either (a) strengthen the causal claims by empirically validating that z_c satisfies the proposed causal properties, or (b) reframe the contribution more modestly as a noise-robustness framework using domain-knowledge-guided data augmentation and contrastive regularization. The current middle ground overpromises.
- The purification mechanism deserves a clearer explanation — why does maximizing I(z_s; Y) purify z_c rather than creating redundancy? If the paper cannot provide a clear mechanistic account, consider reframing it as an auxiliary regularization term.
- Add a simple baseline: CausalNovo's data augmentation (replace + enhance) without the CEM and contrastive objectives. This would cleanly separate the contribution of augmentation from the contribution of disentanglement.

## Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| B6B6EhC1bW | molecular transformers paper | 2.50 | 1 | Much weaker — limited novelty, weak evaluation |
| G536mmC2HL | TorSeq molecular generation | 3.00 | 1 | Weaker — narrower contribution |
| yIRtu2FJvY | VAE variant effect prediction | 3.00 | 1 | Weaker — less thorough evaluation |
| o1efpbvR6v | retrosynthesis | 2.33 | 1 | Much weaker |
| 8GhwePP7vA | Feature Matching Intervention | 4.25 | 1 | Weaker — strong assumptions, limited experiments |
| 22ywev7zMt | OOD Generalization of SSL | 5.67 | 1 | Comparable framing issues but CausalNovo is better executed empirically |
| OGtnhKQJms | Multi-View Causal Rep Learning | 7.00 | 1 | Stronger — rigorous identifiability proofs |
| q4SiDyYQbo | Representation Harms in CL | 6.33 | 1 | Different domain, comparable empirical depth |
| 3cuJwmPxXj | Intervention Extrapolation | 8.00 | 1 | Much stronger — rigorous theory |
| hrqNOxpItr | Cross-Entropy Inverts DGP | 8.00 | 1 | Much stronger — theoretical contribution |
| 87B3zDRMjv | RankNovo (de novo sequencing) | 5.50 | 2 | CausalNovo is clearly stronger — more principled, better results, better ablations |
| 78tc3EiUrN | MADGEN (mass spec generation) | 6.00 | 2 | CausalNovo is stronger — more thorough evaluation, clearer contribution |
| bM6LUC2lec | MSA Generation | 5.67 | 2 | Different domain, CausalNovo has better empirical grounding |
| EGQBpkIEuu | Data Augmentation in DRL | 6.00 | 2 | Different domain, comparable quality |
| 3n4RY25UWP | Disentanglement of Multimodal | 6.25 | 2 | Comparable — both disentanglement methods with good empirical results |
| Lut5t3qElA | Content-Style Disentanglement | 6.40 | 2 | Comparable empirical depth |
| mutJBk3ILg | Feature Space Augmentation | 6.25 | 2 | Different domain, comparable quality |

**Round 1 bracket:** 5.5–7.5.  
**Round 2 narrowing:** CausalNovo is clearly above RankNovo (5.50) and MADGEN (6.00), comparable to or slightly above the 6.25–6.40 disentanglement/augmentation papers, but below the 7.00+ tier with genuine theoretical novelty.  
**Final score:** 6.5 — a solid applied contribution with strong empirical validation in an important domain, held back by causal claims that outrun the implementation and some minor methodological gaps.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>