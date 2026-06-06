---

## Summary

The Open Proof Corpus (OPC) is a large-scale dataset of 5,062 human-evaluated LLM-generated proofs across 1,010 competition mathematics problems (USAMO, IMO, Putnam, etc.), produced by six state-of-the-art LLMs and graded by 13 expert judges (former IMO participants). Beyond dataset construction, the paper uses the OPC to answer three concrete open questions: the performance gap between formal and informal proof generation, the relationship between final-answer accuracy and full proof correctness, and the effectiveness of best-of-n selection strategies. A fine-tuned 8B model (OPC-R1-8B) achieves 88.1% judgment accuracy at majority voting, matching Gemini-2.5-Pro.

---

## Strengths

- **Dataset scale and annotation quality**: With 5,062 proofs across 1,010 problems and 6 LLMs, this is the largest openly released, human-annotated dataset of LLM-generated proofs to date. Double-grading ~10% of proofs yields 90.4% inter-annotator agreement, and the estimated individual judge error rate of ~5% is derived rigorously (§4, solving (1−p)² + p² = 0.904).

- **Rigorous expert annotation pipeline**: Judges were former IMO participants, with a full pilot phase, dynamic problem assignment, and a custom grading interface. The introduction of LLM-generated issue summaries is validated as bias-free by an agreement-rate experiment before and after their introduction (§3.2) — a careful methodological check.

- **Concrete resolution of important open questions**:
  - Formal–informal gap: GEMINI-2.5-PRO achieves 82.7% on PutnamBench vs. <19% for the best formal model GOEDEL-PROVER-V2 (Fig. 4, §5.3), a 4× difference.
  - Final-answer vs. proof gap: o3 drops from 87.6% final-answer accuracy to 59.5% proof correctness, while GEMINI-2.5-PRO drops only from 84.9% to 77.6% (Fig. 5, §5.4) — demonstrating that final-answer benchmarks are unreliable proxies for proof capability in a model-dependent way.
  - Best-of-n: Swiss pairwise ranking improves from a 26% pass@1 baseline to ~47%, significantly outperforming discrete/continuous selection (~35%) (Fig. 6, §5.5).

- **Practical training value**: OPC-R1-8B (8B parameters fine-tuned via GRPO) achieves 88.1% maj@5 accuracy, matching GEMINI-2.5-PRO's maj@5 and outperforming its base model by 17% (Table 2, §5.2), demonstrating the dataset's usefulness for training proof judges.

- **Contamination robustness experiment** (Table 4, §5.6): Providing ground-truth solutions to judges yields no statistically significant accuracy improvement, mitigating concerns that training data contamination inflates judging results.

- **Self-evaluation bias finding** (Table 3, §5.2): All models except QWEN3 judge their own proofs worse than others' proofs — a nontrivial, empirically grounded insight with implications for self-improvement loops.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **OPC-R1-8B distribution overlap**: The paper acknowledges that "the train set for OPC-R1-8B shares the same distribution as this test set, which may inflate its performance" (§5.2). The out-of-distribution robustness is relegated to §C, and the extent of the inflation remains unclear. Since the 88.1% figure is presented prominently as a key contribution, this caveat deserves more prominent treatment in the main body.

- **Small best-of-n evaluation subset**: The primary comparison of all five selection methods is conducted on only 60 problems with full human labels (Fig. 6a). The larger subset of 134 problems excludes *Rank (Bracket)* and has wide confidence intervals. The small-n results drive most of the conclusions in §5.5.

- **Bug causing exclusions in Rank (Swiss)**: "A small bug in the Rank (Swiss) method caused incorrect selections for 18 questions. These are excluded from the analysis" (footnote 1). While 18/134 is modest, this is not discussed in the main text and raises minor concerns about the robustness of the ranking results.

### Trivial

- The caption in Fig. 3 is somewhat confusing in distinguishing "First Partition" and "Second Partition" — the explanation (second partition is harder) is clear in the caption but the visual split may initially mislead readers into thinking it is a temporal train/test split.

---

## Nice-to-Haves

- Extending the OPC to research-level mathematics (graduate or open-problem level) would substantially increase the contribution's reach; the authors acknowledge this as a limitation and outline directions in §F.
- A more detailed breakdown of judge agreement by competition type or problem difficulty level would help users understand where the annotation noise is concentrated.
- The effect of the LLM issue-summary feature on individual judge behavior (beyond the aggregate agreement rate) would be an interesting analysis to include or reference.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

**All criticisms from the Harsh Critic are removed in their entirety.** The Harsh Critic reviewed a completely different paper — "Clip2Protect: Protecting the Makeup Style Privacy in Person Re-identification" — which is not the paper under review. The paper at the provided path is about the Open Proof Corpus (OPC) for LLM-generated mathematical proofs. Specific removed Harsh Critic points include:
- Incoherence of adversarial threat model for makeup Re-ID (applies to Clip2Protect, not OPC)
- N-ASR metric self-contradiction (applies to Clip2Protect, not OPC)
- Absence of numerical results from the paper body (the OPC paper contains abundant numerical results in Tables 1–4 and Figures 2–6)
- Staged baseline comparison via metric design (applies to Clip2Protect, not OPC)
- Unsound CLIP/StyleGAN localization mechanism (applies to Clip2Protect, not OPC)
- DukeMTMC-reID ethical concern (applies to Clip2Protect, not OPC)
- All other Harsh Critic content is similarly inapplicable to the OPC paper

**Dropped Strength Finder strengths**: None dropped — all major claims were directly verifiable against the paper's tables, figures, and quantitative claims.

---

## Novel Insights

The most genuinely novel observation that emerges from the paper — not just a restatement of its contributions — is the model-dependent nature of the final-answer/proof gap. While the community treats this gap as a uniform phenomenon, the OPC data shows it is highly model-specific: o3 suffers a ~28-percentage-point drop while GEMINI-2.5-PRO loses only ~7 points at similar final-answer accuracy levels. This asymmetry suggests that final-answer accuracy and proof capability are relatively decoupled in o3 but tightly coupled in GEMINI-2.5-PRO, which has implications for how these models should be interpreted as reasoning engines. Combined with o3's nearly exclusive behavior of acknowledging uncertainty (114 abstentions, 109 from o3), this paints a picture of qualitatively different internal proof-generation behaviors across models that deserves further mechanistic investigation.

---

## Suggestions

- Provide main-text confidence intervals (or at least explicit qualifications) for the OPC-R1-8B 88.1% result, with an honest comparison on an out-of-distribution split, so readers can assess whether the distribution overlap materially inflates the headline figure.
- The best-of-n section would benefit from combining the small (60-problem) and large (134-problem) subsets into a single coherent analysis — the current two-panel presentation obscures what the actual best estimate of Rank (Swiss)'s benefit is.
- Clearly discuss in the main body whether "correct final answer only" filtering in the MathArena subset (§3.1) affects the proof correctness rates reported in §5.4, since it selects against cases where the model gets a correct answer by luck — that conditional design is relevant to the interpretation of Fig. 5.

---

## Evaluation on Key Axes

**Originality**: High. First large-scale, open, human-annotated dataset of LLM proofs for competition mathematics, with a rigorous annotation methodology and multiple new empirical findings.

**Importance of research question**: Very high. Mathematical proof generation and evaluation are central bottlenecks for LLM progress in formal reasoning, and the paper directly addresses key gaps in understanding.

**Claims well-supported**: Very strong. Every main claim is backed by specific numbers in tables and figures, with confidence intervals and contamination robustness checks.

**Soundness of experiments**: Strong with minor caveats. The annotation methodology is well-controlled. The OPC-R1-8B distribution concern and the small best-of-n subset are the primary limitations.

**Clarity of writing**: High. The paper is well-organized, clearly motivated, and moves logically from dataset construction to open-question resolution.

**Value to the research community**: Very high. The open-sourced dataset, annotation guidelines, custom grading interface, and fine-tuned model together constitute a comprehensive community resource.

---

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>5</importance>
<claims_supported>5</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>5</community_value>
</subscores>