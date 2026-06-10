## Summary

EffoVPR proposes a simple retrieval pipeline for Visual Place Recognition built on DINOv2. The global stage uses the [CLS] token with a CosFace classification loss (borrowing the training paradigm from EigenPlaces) and fine-tunes only the last 5 layers of DINOv2. The re-ranking stage extracts intermediate-layer Value features from the ViT, filters them by attention-map score, and counts mutual nearest neighbors above a similarity threshold. The method achieves state-of-the-art results on most of 20 benchmarks, with a zero-shot variant that outperforms prior zero-shot approaches by large margins, and compact 128D features competitive with 8,448D features.

## Strengths

- **State-of-the-art recall with dramatically reduced feature dimensionality.** EffoVPR achieves 94.6% R@1 on Tokyo24/7 at only 128D — matching SALAD's 94.6% which uses 8,448D (a 66× reduction) — and 97.5% at 1024D, the top result on that dataset (Table 2). This is directly evidenced in the compactness-vs-performance plots (Figure 1).

- **Zero-shot method outperforms prior zero-shot approaches by large margins on challenging scenarios.** EffoVPR-ZS achieves 90.8% on Tokyo24/7 (vs. AnyLoc's 60.6%) and 57.9% on Nordland (vs. AnyLoc's 16.1%) — gaps of +30.2 and +41.8 points respectively on the day/night and seasonal-change benchmarks (Table 1). The paper also shows this zero-shot method competing with several *trained* VPR methods (Figure 3a).

- **Two-stage method achieving SoTA on all four standard benchmarks simultaneously.** EffoVPR-R ranks first on Tokyo24/7 (98.7% R@1, +4.1% over SALAD's 94.6%), MSLS-val (92.8%), MSLS-challenge (79.0%, +4.0% over SALAD's 75.0%), and second on Pitts30k (93.9%, within 1% of leader). No competing method leads on more than one benchmark (Table 3).

- **Large-margin improvements on the most challenging scenarios.** EffoVPR-R achieves 61.6% on SF-XL Night (vs. SALAD's 46.6%, +15.0 points), 59.2% on SF-XL Occlusion (vs. SALAD's 51.3%, +7.9 points), and 95.0% on Nordland (vs. CricaVPR's 90.7%, +4.3 points). These are precisely the settings where prior aggregation techniques break down (Table 8).

- **Rigorous ablation identifying that intermediate-layer Value features substantially outperform both the last layer and Query/Key features for re-ranking.** Table 4b shows that the last layer (n) *degrades* global performance (88.2% on MSLS-val vs. 90.9% global-only), while layer n-1 boosts it to 92.8%. Table 4c further shows Value features (98.7% on Tokyo24/7) clearly outperform Query (96.5%) and Key (96.8%).

- **Demonstration that fine-tuning only the last 5 layers is optimal, with full fine-tuning harming performance.** Table 6 shows 90.9% R@1 (MSLS-val) / 97.5% (Tokyo24/7) with 5 trainable layers vs. 86.1%/94.0% with all layers fine-tuned — a practical finding for fine-tuning large ViTs on limited VPR data.

- **SoTA achieved without external pooling layers or adapter modules.** Unlike SelaVPR (trainable adapters inside DINOv2), CricaVPR (feature pyramid + adapters), and SALAD (optimal transport pooling, 8,448D features), the proposed method uses only the [CLS] token with CosFace loss and no specialized pooling (GeM, NetVLAD, etc.), as stated in Contributions 2 and 3 (lines 47–48).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **SF-XL test subsets are drawn from the same geographic area as the training data, and this confound is not discussed.** EffoVPR is trained on SF-XL (line 134) and then evaluated on SF-XL Occlusion and SF-XL Night (Table 8) — subsets from the same city. Several baselines in that table (SelaVPR trained on Pitts30k+MSLS, CricaVPR and SALAD trained on GSV-Cities) were *not* trained on San Francisco imagery, making the large gaps on SF-Night (+15% vs. SALAD) and SF-Occlusion (+7.9% vs. SALAD) partially attributable to geographic familiarity rather than methodological superiority alone. The paper notes training sources (Section 4.2, lines 197) but does not connect this observation to the SF-derived test results. EigenPlaces (also SF-XL trained) is included as a baseline and does much worse, which mitigates this concern somewhat, but the confound merits explicit discussion.

2. **The DINOv2 model variant (ViT-S/14, ViT-B/14, ViT-L/14, ViT-g/14) is never specified.** This matters for reproducibility: the total number of layers differs across variants (12 vs. 24 vs. 40), so "last 5 layers" and "layer n-1" are ambiguous without this information. The embedding dimension d and number of patches p also vary by variant, affecting the re-ranking's computational profile. This information likely resides in the appendix (which was stripped by the parser), but it is a notable gap in the main paper.

### Trivial

1. **Notation error in the self-attention equation (Equation 1, line 86).** The paper writes `Attention(Q_l,K_l,V_l) = Softmax(K_l^T Q_l / sqrt(d)) V_l`. With Q_l, K_l ∈ R^{p×d}, the product K_l^T Q_l yields a (d×d) matrix rather than the expected (p×p) attention map. This should be `Q_l K_l^T` (or the equivalent transpose). The surrounding text correctly describes the standard mechanism, so this is clearly a notational slip, but it should be corrected.

## Nice-to-Haves

- An experiment applying the proposed re-ranking on top of *other* methods' global features (e.g., EigenPlaces or SALAD global features) would strengthen the claim that the Value-based MNN re-ranking is a transferable contribution independent of the global stage.
- The actual numerical values of T₁ and T₂, while likely reported in the appendix, should appear in the main paper since the paper emphasizes they are fixed across all 20 datasets — making them a central design parameter.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's claim that "global feature extraction is largely a reapplication of EigenPlaces with a DINOv2 backbone."** The paper transparently states "we adopt a similar strategy" (line 70). The training paradigm is acknowledged as borrowed; the paper's novelty lies in (a) applying it to DINOv2 with partial fine-tuning, (b) the finding that partial fine-tuning (5 layers) is optimal, and (c) the re-ranking mechanism using internal Value features. This is a framing observation about lineage, not a weakness.

- **Harsh Critic's claim about "zero-shot comparison is structurally asymmetric."** The DINOv2 baseline row in Table 1 (62.2% on Tokyo24/7) IS the global stage of EffoVPR-ZS. The paper explicitly states: "For the first stage ranking we use the [CLS] token from vanilla-DINOv2" (line 126). The gain from the pipeline is therefore directly measurable. The critic acknowledges this internally ("It appears EffoVPR-ZS does exactly this") and then treats it as a weakness — this is contradictory.

- **Harsh Critic's suggestion to "disentangle the zero-shot results" by reporting what the global stage achieves before re-ranking.** Already reported via the DINOv2 row in Table 1.

- **Strength Finder strength about "achieving SoTA without external pooling layers" — KEPT.** This is a genuine, verifiable strength.

- **Harsh Critic's comments about missing related works, hyperparameter disclosure, or format/style issues.** Removed per hard rules.

## Novel Insights

The recurring insight across the reviews is that the re-ranking mechanism — extracting Value features from intermediate layers, filtering by attention-map response to the [CLS] token, and counting MNN pairs above a threshold — is the paper's genuinely novel contribution, while the global stage is a well-executed adaptation of an existing paradigm. The finding that the *last* ViT layer hurts re-ranking while the penultimate layer helps is non-obvious and practically useful. The zero-shot results also reveal something interesting about DINOv2: its internal Value features encode instance- or region-level correspondence that can be surfaced through the attention map without any training, which AnyLoc's VLAD-based aggregation fails to capture under appearance change.

## Suggestions

- Specify the DINOv2 variant (model size, number of layers, embedding dimension, patch size) in the main paper.
- Add a brief discussion of the training/test geography overlap for SF-XL subsets in the experimental section.
- Correct the attention equation notation in Equation 1.
- Optionally: report the T₁ and T₂ numerical threshold values in the main text and consider adding an experiment that applies the proposed re-ranking on top of a different method's global features.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>