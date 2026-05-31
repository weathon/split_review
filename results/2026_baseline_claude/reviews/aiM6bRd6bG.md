## Summary
The paper introduces *PPI Candidate Ranking*, a novel problem formulation that, given a query protein with known interaction partners, ranks novel candidate proteins by predicted interaction likelihood to prioritize experimental validation. The authors propose an interpretability-guided retrieval mechanism that uses contact-map activations from D-SCRIPT and Topsy-Turvy to identify active residue regions, then measures cosine similarity between these activated embeddings of known partners and candidates. A multi-signal re-ranking stage further refines the top-10 candidates using interaction scores, structural plausibility (SpeedPPI/pDockQ), and semantic/LLM features. A prospective evaluation using STRING v11→v12 transitions shows dramatic improvements over direct use of model prediction probabilities.

---

## Strengths

- **Practically motivated problem formulation.** Framing PPI discovery as a *ranking* problem conditioned on known interaction partners directly addresses the experimental validation bottleneck. This is more useful than generic binary classification because it matches the real workflow of experimental biologists.

- **Rigorous prospective evaluation design.** Using the STRING v11→v12 database transition as the test set is methodologically sound and genuinely prospective: models trained on v11 are evaluated on interactions discovered only in v12, cleanly simulating the target use case. GroupKFold by protein identity for the cross-encoder fine-tuning properly avoids protein-level leakage.

- **Large and consistent empirical improvements.** The interpretability-guided approach achieves Recall@10 = 26.4% and MAP@10 = 29.5% for D-SCRIPT compared to <2% with raw prediction probability. MRR increases 4–5× across both backbone models. These are not marginal gains; the improvement is substantial and replicated across multiple metrics and cutoffs.

- **Comprehensive multi-signal analysis.** The systematic pairwise rank-shift analysis (Table 2) spans 10 re-ranking strategies across sequence, structure, and language modalities and reveals complementary roles: PubMedBERT cross-encoder is most consistent (75.5% maintain-or-improve), lightweight TF-IDF/Jaccard signals are surprisingly effective, and pDockQ is better suited for filtering than ordering.

---

## Weaknesses

### Fatal
None.

### Major

1. **Overstatement of improvement magnitude.** The paper repeatedly claims "improvements by two orders of magnitude." Checking Table 1: MAP@5 rises from 0.0103 to 0.2714 (~26×) and nDCG@5 from 0.0098 to 0.2067 (~21×). These are approximately 1.3–1.4 orders of magnitude—impressive, but not two orders of magnitude (100×). MRR increases only 5× (~0.7 orders of magnitude). The actual gains are still remarkable and do not need exaggeration to support acceptance; the overclaim undermines the paper's credibility.

2. **Absence of ablation on the core retrieval design.** The interpretability-guided step involves two non-trivial choices: (a) selecting the single contiguous residue segment of highest average activation, and (b) taking the maximum similarity over all known partners (Eq. 4). Neither choice is justified empirically through ablation. For (a), using all activated residues or top-k isolated residues might work as well or better. For (b), mean aggregation or attention-weighted aggregation might produce different rankings. Without ablations, the contribution of these specific design choices to the observed gains is unverified.

3. **Re-ranking limited to top-10 candidates without justification for LLM/semantic signals.** The paper states "due to the heavy processing of some of the techniques, we focus on the top 10 ranked candidates," which is reasonable for SpeedPPI. However, semantic methods (TF-IDF, BioBERT, PubMedBERT) are computationally lightweight and could be applied at much larger cutoffs (top-100 or top-500). Operating on only top-10 candidates means re-ranking is conditioned on the first stage not missing the true novel partner, masking scenarios where semantic re-ranking could recover missed candidates. This design choice is not discussed or validated.

### Minor

1. **The baseline comparison is not fully symmetric.** The baselines (D-SCRIPT, Topsy-Turvy, xCAPT5 raw scores) do not use the known partner set KP(p), whereas the proposed method explicitly conditions on it. This is the design point of the paper, but it should be stated more precisely and the contribution framed as: "given KP(p), the proposed approach ranks far better than naively using model probabilities which ignore KP(p)." A fairer ablation would also include a simpler KP(p)-aware baseline (e.g., mean cosine similarity over all residues, no activation masking) to isolate the benefit of interpretability guidance.

2. **No analysis conditioned on |KP(p)|.** The method relies on known partners as anchors. Proteins with very few known partners (e.g., |KP(p)| = 1) may produce noisy or unreliable anchor signals. The paper acknowledges this limitation qualitatively but provides no quantitative breakdown of performance by number of known partners, which would substantially clarify the method's scope.

3. **PubMedBERT cross-encoder potential leakage caveat.** The paper correctly notes that "it is uncertain if their gains reflect not only semantic generalization but also latent knowledge of interactions from the training data" for BioBERT/BioMedRoBERTa. The same caveat applies to the fine-tuned PubMedBERT cross-encoder, which is trained on v11 interactions and then evaluated on v12 new interactions—even with protein-level GroupKFold, the model may have learned from the general interaction landscape rather than the specific novel interactions.

### Trivial
None worth noting.

---

## Nice-to-Haves

- An ablation comparing: (a) full-sequence cosine similarity vs. activated-region cosine similarity, and (b) mean vs. max aggregation over anchors, would cleanly quantify the contribution of the interpretability guidance.
- Stratified results by |KP(p)| (e.g., 1–5, 5–20, >20 known partners) would clarify when the method is most and least reliable.
- Applying lightweight re-ranking (TF-IDF, BioBERT) beyond top-10 to assess whether semantic signals can rescue missed candidates from the retrieval stage.

---

## Novel Insights

The core novel insight is that contact-map activations, originally intended as an interpretability device for D-SCRIPT/Topsy-Turvy, serve as a natural mechanism to identify *binding region representations* of known partners that generalize to novel interactors. This repurposing of model internals for retrieval—rather than generating human-facing explanations—is elegant and produces dramatically better rankings than raw interaction probabilities. A secondary insight from the re-ranking analysis is that even simple bag-of-words overlap on curated protein annotations (localization, key terms) is highly predictive of interaction plausibility, suggesting that much of the information PPI models try to learn from sequence alone is already encoded in curated databases and should be used more systematically.

---

## Suggestions

- Add an ablation with full-sequence (no masking) cosine similarity to isolate the value of active-residue selection.
- Apply TF-IDF/BioBERT re-ranking at top-50 or top-100 to measure recovery of candidates missed at top-10.
- Qualify the "two orders of magnitude" claim to accurately reflect the observed ~20–26× improvements.
- Report performance stratified by |KP(p)| to characterize when the method degrades.
- Discuss whether an ensemble of re-ranking signals (e.g., combining IS and PubMedBERT) further improves performance.

---

## Score and Decision

The paper presents a genuinely novel problem framing with a principled approach and strong prospective evidence. The interpretability-guided retrieval idea is creative and the STRING v11→v12 evaluation is scientifically sound. The main weaknesses—an overstated magnitude claim and absence of ablations on core design choices—are significant but not fatal; the empirical improvements are robust enough across metrics to support the method's value. The limited re-ranking scope is an acknowledged limitation. On balance, the paper makes a solid contribution to PPI discovery methodology that would be of interest to the ICLR community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>