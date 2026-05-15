Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

## Summary

The paper proposes SUMMER, a framework for Multimodal Emotion Recognition in Conversations (MERC) that combines three main components: (1) a Sparse Dynamic Mixture of Experts (SDMoE) for adaptive token-level filtering, (2) a Hierarchical Cross-Modal Fusion (HCMF) module with a Global MoE for contextual modeling, and (3) a "retrograde distillation" strategy where a pre-trained unimodal (text) teacher guides a multimodal student model via interactive knowledge distillation (IKD). Experiments on IEMOCAP and MELD show consistent improvements over published baselines, with notable gains on minority and semantically similar emotion categories (e.g., +9.76% w-ACC on "happy" in IEMOCAP, +15.5% on "Fear" in MELD).

## Strengths

1. **Novel distillation framing that targets a real problem in MERC.** Using a unimodal teacher to regularize multimodal fusion is a non-obvious approach directionally opposite to standard KD, and the paper correctly identifies "fusion disorientation" (gradient conflicts from modality heterogeneity) as a genuine challenge. The IKD loss combines multiple terms (cross-entropy, KL divergence, MSE on intermediate features, label smoothing) that together provide rich supervisory signal, and ablation (Table 4) confirms IKD contributes positively.

2. **The SDMoE module provides a principled mechanism for token-level redundancy filtering.** Rather than fixed top-K selection, the dynamic routing uses a statistical threshold (μ±2σ) on gating weights with Gumbel noise for differentiability. Ablation shows replacing SDMoE with standard MoE degrades performance (Table 4), and Figure 4 demonstrates consistent gains across modalities during teacher pre-training.

3. **Comprehensive ablation studies isolating each component.** Tables 3 and 4 systematically evaluate the teacher modality choice, SDMoE substitution, HCMF replacement, and IKD removal. The paper also tests different teacher modalities (text-only vs. multimodal variants in Table 3), providing evidence for the text-teacher choice.

4. **Substantial per-class improvements on minority and confusable emotions.** Unlike many MERC papers that report only macro metrics, the paper details gains on specific categories: "frustration" (+3.32%), "sadness" (+1.86%), "excitement" on IEMOCAP, and "Fear" (+15.5% over CORECT), "Anger" (+3.5%), "Disgust" (+5.81%) on MELD (Section 4.4). These numbers support the claim about improving fine-grained emotional distinctions.

## Weaknesses

### Fatal
None.

### Major

1. **No statistical significance or variance is reported for any experimental result.** All tables report single numbers without standard deviations, confidence intervals, or statement about number of runs. IEMOCAP and MELD are small datasets (∼12 hours, ∼13K utterances) with known variance across random seeds, speaker splits, and initialization. Without multiple runs, the claimed 2–3% SOTA improvements and the smaller ablation deltas (0.4–1.2%) cannot be assessed for statistical significance. This is the most consequential weakness: it prevents the reader from determining whether the core empirical claims are reliable.

2. **The "retrograde distillation" is not compared against a conventional distillation baseline.** The paper proposes using a weaker unimodal (text) teacher to guide a stronger multimodal student — contrary to standard KD where the teacher outperforms the student. The ablation in Table 4 removes IKD entirely but never replaces the unimodal teacher with (a) a standard multimodal teacher of equal or larger capacity, (b) a self-distillation baseline (the student distilling itself), or (c) a larger-capacity unimodal teacher. Without such a control, the paper cannot substantiate that the *direction* of distillation (weaker→stronger) is what helps, rather than simply the extra loss terms. The conceptual justification in Section 3.5 ("using a single modality as a prior") is intuitive but not supported by controlled experiments.

3. **The mechanism by which the frozen unimodal teacher's classifier processes heterogeneous student features is underspecified.** Section 3.6 states: "we freeze the teacher's parameters and apply its classifiers to the student's intermediate features... ensuring that the heterogeneous modal features are mapped into a uniform distribution space." The teacher is trained on text-only features; it is not explained how its classifier (expecting text-dimension input) can process audio or visual features from the student, nor whether explicit projection layers or shared embedding spaces are used. This gap affects both reproducibility and the conceptual soundness of the IKD design.

### Minor

4. **Several key hyperparameters are not justified or explained.** The masking threshold in Eq. (6) (0.5) and the dynamic adjustment factor φ in the teacher-guided attention (Section 3.5) are introduced without tuning procedure, update rule, or sensitivity analysis. The routing statistics μ and σ in Eq. (3) are not specified as per-token, per-batch, or dataset-wide. These underspecifications hinder reproducibility.

5. **The motivational example in Figure 1(a) is not explicitly revisited.** The paper introduces a concrete dialogue where a model might confuse sadness for happiness or excitement for anger, but the experimental section does not return to this example to show SUMMER's predicted distribution vs. a baseline. Given that per-class gains are reported, this is a missed opportunity rather than a flaw in the results.

6. **Baseline comparisons are taken from published papers without re-implementation.** This is common practice in MERC but still a limitation: differences in feature extractors, data splits, and preprocessing (the paper's input dimensions differ from standard practice in some prior work, e.g., using 768-dim text for MELD vs. 100-dim GloVe in some baselines) can influence relative rankings. The paper does not verify that its preprocessing pipeline matches that of the cited baselines.

### Trivial
None.

## Nice-to-Haves

- **Per-class F1 analysis with explicit discussion of the Figure 1(a) failure modes.** The paper already reports per-class numbers; a dedicated case study tracing the exact dialogue from Figure 1(a) through SUMMER vs. a strong baseline (e.g., SDT) would strengthen the qualitative claims.
- **Hyperparameter sensitivity sweeps** for the masking threshold (0.5), temperature τ, and the φ factor would improve reproducibility confidence.
- **Training/inference time and parameter counts** for SDMoE vs. standard MoE vs. no MoE, to assess whether the dynamic routing incurs meaningful overhead.
- **Gradient conflict analysis** (e.g., cosine similarity of gradients from different modalities/loss terms) to directly support the claim that IKD reduces "fusion disorientation."

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper reports only overall metrics in the text"** — Factually incorrect. Section 4.4 reports specific per-class gains (happy +9.76%, sadness +1.86%, frustration +3.32%, Fear +15.5%, Anger +3.5%, Disgust +5.81%). Removed as factually wrong.
- **"t-SNE visualizations do not include a baseline method for comparison"** — The paper shows "Original features" vs. "Features learned by our method," which is a valid before/after comparison. The critic's stricter request (comparison to another model) is a nice-to-have, not a missing baseline. Weakened and moved.
- **"The paper claims novelty in KD but doesn't support it with a literature survey"** — The hard rule prohibits requiring specific missing related works unless externally verifiable. The paper's claim about "little attention" to unimodal teachers is qualitative but not falsely stated. Removed per hard rules.
- **"Missing appendix details"** — The parser strips appendix sections (A.1, A.2 referenced in text). Per hard rules, criticisms about content absent due to parsing are removed.
- **"Figure 5 shows only one curve"** — The figure compares HCMF with and without residual connections (relevant to the ablation claim about training smoothness). The critic's demand for a different fusion method comparison conflates the purpose of the figure. This point is moved here as over-reaching.
- **Various formatting/typo nitpicks** — Removed per hard rules about parser artifacts.

## Novel Insights

The most interesting observation that emerges across the reviews is the fundamental tension between the paper's core novelty — using a weaker unimodal teacher for "retrograde distillation" — and the lack of a controlled experiment validating that the *direction* of the distillation is what drives improvement, as opposed to the extra auxiliary losses (KL divergence, MSE, label smoothing) that any teacher, including a self-distillation setup, could provide. This is a generic concern for any paper proposing an unconventional distillation paradigm: without ablating the teacher's capacity or directionality, the novelty claim remains correlational rather than causal. The paper's empirical contributions (SDMoE, HCMF architecture, consistent SOTA results) stand somewhat independently of this claim, which is both a strength and a weakness — it means the framework works, but the most distinctive selling point is the least validated.

On the positive side, the strong per-class gains on minority emotions (Fear +15.5%, Happy +9.76%) are genuine and practically meaningful. If the variance concern is resolved, these results alone would make the paper a solid systems contribution regardless of the distillation theory.

## Suggestions

1. **Add variance reporting.** Run all experiments 5+ times with different random seeds and report mean ± std in every table. Without this, the core empirical claims are unverifiable.
2. **Add a controlled distillation baseline.** Replace the unimodal teacher with (a) a multimodal teacher of similar capacity trained from scratch, (b) self-distillation from the student itself, and/or (c) a larger-capacity unimodal teacher. If the "retrograde" direction is the innovation, show that it outperforms standard KD directions.
3. **Clarify the teacher classifier mechanism.** Explain how the frozen text-trained classifier processes audio/visual student features — are there projection layers, a shared hidden dimension, or is the interaction modality-specific?
4. **Specify the computation scope of routing statistics** (μ, σ in Eq. 3) — per-batch, per-dataset, or running statistics — and the φ update rule.
5. **Run a sensitivity analysis** on the masking threshold (0.5) and temperature τ to demonstrate they are not cherry-picked.

## Score and Decision

The paper has genuine contributions (SDMoE, HCMF, consistent SOTA with per-class gains on minority emotions) and tackles a meaningful problem. However, the absence of variance reporting is a critical evidential gap that makes the central empirical claims unverifiable, and the paper's most novel claim (retrograde distillation) lacks a controlled comparison against standard distillation paradigms. These issues are major but addressable with additional experiments. In its current form, the evidence falls short of the standards needed to support the paper's strongest claims.

**Score**: 5.0

**Decision**: Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>