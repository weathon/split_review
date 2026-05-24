Now I have a thorough understanding of the paper and the calibration landscape. Let me write my final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes RTA (Regression-based Test-Time Adaptation), a method that learns a regression mapping from CLIP logits to pseudo cross-entropy loss using a LightGBM decision tree trained once on diverse pseudo-labeled data. At test time, this regression model predicts view quality (lower predicted loss = more reliable) for each augmented view of a test instance, enabling confident view ensemble without per-instance tuning. Experiments on single-label, cross-domain, and multi-label benchmarks show consistent improvements over entropy-based TTA methods.

## Strengths

**S1. Well-motivated from a striking empirical finding.** The paper first demonstrates (Tables 1–2) that oracle view selection by ground-truth cross-entropy loss (LCE) dramatically outperforms entropy-based selection — e.g., on ImageNet-A with ViT-B/16, LCE achieves 90.2% vs. entropy's 64.3% at 64 views. This establishes a clear ceiling that motivates the regression approach.

**S2. Consistent empirical gains across diverse benchmarks.** RTA outperforms existing TTA methods (Zero, BCA, TDA, ML-TTA, etc.) on nearly all datasets across single-label (Table 3), cross-domain (Table 4), and multi-label (Tables 5–6) settings. For example, on ImageNet-A (ViT-B/16), RTA reaches 65.65% vs. Zero's 64.03%; on MSCOCO (RN50), 53.25% mAP vs. ML-TTA's 51.58%. The breadth of evaluation (20+ datasets) is a clear strength.

**S3. Lightweight "train once, deploy anywhere" paradigm.** The regression model is a shallow decision tree (LightGBM, max depth 5, 16 leaves) trained on only 1,000 samples from ImageVal-12k. It requires no per-instance backpropagation, no prompt tuning, and no memory buffer at test time — only a single tree prediction per augmented view. This is substantially simpler than methods like TPT or DiffTPT that require per-instance optimization.

**S4. Diagnostic evidence for the regression hypothesis.** t-SNE visualization (Figure 2) shows structured clustering of logits by loss values across datasets, and Spearman correlation analysis (Figure 3) confirms monotonic relationships between logit features and cross-entropy loss. These provide grounding for why a regression model can predict view quality from logits.

## Weaknesses

### Fatal
None.

### Major

**W1. Duplicate baseline row in Table 4 undermines result confidence.** The ViT-B/16 section of Table 4 (line 437–438) lists "TDA [CVPR 2024]" twice with different numerical values (e.g., EuroSAT: 58.00 vs. 45.36; Average: 67.53 vs. 65.58). One of these rows is clearly mislabeled — likely from a different method (possibly MTA [CVPR 2024], which appears in Table 3 but is absent from Table 4). This error, in the paper's central cross-domain benchmark table, damages confidence in the reported numbers and must be corrected for the results to be verifiable.

**W2. Method description for multi-label adaptation is incomplete.** The regression model is trained on 1,000-class ImageNet logits (1000-dimensional feature vectors). Multi-label datasets (MSCOCO: 80 classes, VOC2007: 20 classes, NUSWIDE: 81 classes) have entirely different label spaces. The paper never specifies how the 1000-feature regression tree is applied to these tasks — whether (a) CLIP's 1000-class logits are used as a fixed feature space and only a subset of classes is evaluated, (b) a separate regression model is trained per label space, or (c) some other mechanism is employed. The method description (Section 4, Algorithms 1–2) is written entirely for single-label classification with a fixed L, and no adaptation is discussed. This is a reproducibility gap that prevents proper interpretation of Tables 5–6.

**W3. No direct comparison with a simple max-softmax (highest-confidence) view selection baseline.** The paper compares exclusively against entropy-based methods. The most natural baseline for isolating the regression model's contribution is selecting views with the highest maximum softmax probability (i.e., top-1 logit confidence). Many previous TTA works treat max-softmax and entropy as related but non-identical metrics. Without this baseline, it is unclear whether RTA's gains come from learning a refined confidence function that max-softmax already approximates, or from something fundamentally different about the learned mapping.

### Minor

**W4. Gains over strong baselines are often modest.** While RTA consistently outperforms prior methods, the improvements on several datasets are 0.5–1.5 percentage points (e.g., Table 3 ViT-B/16 on ImageNet-1k: 71.13% RTA vs. 70.89% Zero; on ImageNet-R: 81.05% vs. 80.82% BCA). The paper's tone ("significantly outperforms") overstates the margin on these cases. On some cross-domain datasets (EuroSAT, Flowers, DTD), RTA is not the best method.

**W5. The regression model is trained on pseudo-labels from CLIP's own predictions, creating a circularity that is not analyzed.** The regression model learns to predict "how well a view matches CLIP's own high-confidence predictions" rather than being validated against true loss. The paper provides no direct analysis (e.g., on a held-out set with ground-truth labels) showing that the predicted loss correlates with true LCE or that the selected views have lower true loss than entropy-selected views. While the empirical results demonstrate the method works, the mechanism is less transparent than claimed.

### Trivial

None of significance (parser artifacts and formatting issues should not be reported).

## Nice-to-Haves
- A comparison with the most related prior work (Kim et al. 2020's loss predictor for TTA) in an adapted unlabeled setting would better contextualize the contribution.
- Reporting inference latency overhead of the decision tree vs. the CLIP forward pass would strengthen the practical claims.
- Statistics on pseudo-label accuracy for the regression training set and its impact on the learned mapping.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. *"The core claim of a universal regression mapping is unsubstantiated"* — The paper explicitly tests on 20+ diverse datasets ranging from textures (DTD) to satellite (EuroSAT) to fine-grained (Aircraft, Cars). The critic's demand for medical imaging or completely disjunct taxonomies is scope creep beyond CLIP's zero-shot capabilities. The claim is sufficiently supported for the paper's scope.

2. *"EuroSAT result suggests the method is not uniformly superior"* — This is acknowledged in the paper (Table 4 shows RTA is not best on every dataset). This is a normal characteristic of any method, not a weakness. Removed as trivial.

3. *"Treatment of Kim et al. 2020 — no experimental comparison"* — The critic acknowledges direct comparison is impossible because Kim et al. requires labeled target-domain training data. Suggesting a pseudo-label adaptation is reasonable but speculative. This is a nice-to-have, not a weakness.

4. *"Regression model trained on pseudo-labels creates circularity"* — The paper explicitly states it uses pseudo-labels with confidence threshold ≥ 0.8 to avoid accessing ground-truth labels. The empirical validation across 20+ datasets demonstrates the method works despite this. The concern about mechanism is interesting but does not invalidate the results.

5. *"Strength about 'addressing an important problem'"* and similar generic strengths from the Strength Finder — removed as insufficiently specific.

6. *"Missing related works"* — By rule, I cannot flag missing related works without access to external knowledge.

7. *"Missing appendix content"* — By rule, the appendix is stripped during PDF parsing; these are not author errors.

## Novel Insights
None beyond the paper's own contributions. The reviews surface useful criticisms (the multi-label gap and table error are real) but do not identify a missed opportunity or reframe the paper's significance in a way that the authors missed.

## Suggestions

1. **Correct the duplicate TDA row in Table 4** and verify all table entries against original method papers.
2. **Clearly specify the multi-label adaptation mechanism** — state whether the same 1000-class regression tree is used with dataset-specific class prompts, whether separate models are trained, or another approach is used. If separate models are needed, adjust the framing from "one model for all" to "one model per classifier label space."
3. **Add a max-softmax view selection baseline** to all main tables. This directly isolates the benefit of the learned regression mapping.
4. **Tone down "significantly outperforms"** language where margins are small (<1 pp), or report statistical significance.
5. **Add a validation experiment** showing correlation between predicted loss and true LCE on a held-out labeled subset (e.g., a held-out portion of ImageNet-val with true labels). This would directly answer questions about mechanism.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**
- Weak anchors (avg < 3.5): /home/wg25r/review_agent/human_reviews_2026/HeGMugkCOH.md (3.00, C-TTA, Withdrawn), /home/wg25r/review_agent/human_reviews_2026/CFAYmfjd4v.md (3.20, VLBO, Withdrawn), /home/wg25r/review_agent/human_reviews_2026/snbY9Uj0Gx.md (2.67, RA-TTA, Withdrawn), /home/wg25r/review_agent/human_reviews_2026/KBtySUdWuH.md (3.00, BETA, Reject). These papers have fundamental flaws (e.g., flawed assumptions, missing baselines) and score below 3.5. RTA is clearly stronger.
- Middle anchors (3.5 < avg < 7.5): /home/wg25r/review_agent/human_reviews_2026/CLUvRxQXtf.md (4.67, CLIP-DR, Reject — incremental), /home/wg25r/review_agent/human_reviews_2026/7W4Gusa9rY.md (4.50, VLOD-TTA, Reject — limited scope), /home/wg25r/review_agent/human_reviews_2026/S90g7NE88b.md (5.00, FGA, Accept Poster — solid but some theory gaps), /home/wg25r/review_agent/human_reviews_2026/iQLZChxwDu.md (4.00, not TTA). RTA is stronger than CLIP-DR (more novel) and comparable to FGA.
- Strong anchors (avg > 7.5): All from different domains (3D reconstruction, multimodal reasoning, navigation). Not directly comparable.

**Round 1 bracket:** [5.0, 6.5]

**Round 2 — Narrowing:**
- /home/wg25r/review_agent/human_reviews_2026/7kLNGaAHaw.md (5.50, PEA, Accept Poster) — backprop-free TTA with clean analysis. RTA has broader evaluation but the table error makes it slightly weaker overall.
- /home/wg25r/review_agent/human_reviews_2026/eZO38vANPM.md (5.50, IMSE, Accept Poster) — spectral experts TTA with solid empirical results and some missing ablations. Comparable quality to RTA.
- /home/wg25r/review_agent/human_reviews_2026/4dMlAKBwrA.md (5.33, Multimodality as Supervision, Accept Poster) — different problem setting, not directly comparable.
- /home/wg25r/review_agent/human_reviews_2026/aMs6FtNaY5.md (6.00, TTT3R, Accept Poster) — different domain (3D reconstruction).

**Final score:** 5.5. Relative to the round-2 anchors, RTA is comparable to PEA (5.50) and IMSE (5.50) — a solid conference-paper contribution with a novel idea and broad experiments, but held back by the duplicate table error and the missing multi-label specification. It is clearly above the Reject-range papers (CLIP-DR at 4.67) and below the 6+ tier that would require cleaner presentation and no errors in central results.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>