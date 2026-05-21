Now I have all the information needed. Let me synthesize the final review.

## Summary

CEIR proposes a novel pipeline for learning interpretable image representations by combining concept bottleneck models (derived from CLIP + GPT-4-generated concepts) with VAE compression. The key idea is: (1) project images into a human-comprehensible concept vector space via a trained bottleneck layer supervised by CLIP similarity; (2) compress the high-dimensional concept vectors with a VAE into a low-dimensional latent representation; (3) perform clustering or downstream tasks on the VAE latent space while also providing concept-level attribution via integrated gradients. The method achieves strong clustering ACC/NMI/ARI on CIFAR10, CIFAR100, and STL10, and demonstrates interpretable concept decompositions on both benchmark and open-world images.

## Strengths

- **Concept-based representation learning that combines interpretability with strong empirical performance.** The core idea — that concept vectors from CBM can be compressed via VAE into a representation that is both clusterable and interpretable — is novel and well-motivated. The paper bridges concept bottleneck models and representation learning in a clean way, and the pipeline (concept projection → VAE → attribution) is clearly defined.

- **Interpretable concept decompositions without supervision.** Figure 3 demonstrates that CEIR can decompose images into human-comprehensible plain-text concepts (e.g., "rear hatchback", "lion-like mane", "blue and white exterior") without any label supervision during the VAE stage. This capability goes beyond prior concept bottleneck models (LF-CBM, TCAV) which either require supervised labels or operate in a classification-only setting.

- **Lightweight architecture.** As noted in Section 4.1, CEIR "only integrates one trainable projection layer (MLP) and a shallow VAE consisting of a two-layer MLP," yet achieves competitive results against methods with deeper architectures (ProF, SPICE, SCAN). This efficiency is a genuine differentiator.

- **Competitive linear probing despite the interpretability trade-off.** Table 3 shows CEIR (ViT-L/14) achieves 97.19% ACC on CIFAR10 linear probing, within 0.92% of CLIP ViT-L/14 (98.11%) and surpassing DINO (96.80%), demonstrating that the concept bottleneck + VAE transformation retains substantial discriminative information.

## Weaknesses

### Fatal
None.

### Major

- **The clustering evaluation protocol uses test data in VAE training, which undermines the headline results.** Section 4.1 states: "In our VAE model training, we merge training and testing sets" and clustering is then evaluated "on h produced from the testing set." The VAE has thus seen the test-set concept vectors during its reconstruction training before K-means is run on those same test-set latents. While the VAE's reconstruction objective is unsupervised (not label-driven), this is a form of data leakage that violates standard evaluation practice. The paper marks results with † ("additional data including testing set") but this notation does not fully convey the circularity. Many baselines in Table 2 (TEMI, SimCLR, MoCoV2) do not merge test data into their training. The size of the inflation is unknown, making the reported SOTA clustering claims unreliable as-is.

- **No comparison against the most natural baselines: raw concept vectors (q_i) or LF-CBM bottleneck features.** The paper evaluates against vanilla VAEs on raw images and representation learning methods (SimCLR, MoCoV2, CLIP), but never isolates the effect of the VAE compression by reporting clustering on the concept vectors q_i directly, or on the LF-CBM bottleneck outputs before the VAE. Without this comparison, it is impossible to tell whether the VAE adds value or simply passes through (or degrades) the already-informative concept vectors. This is a critical missing ablation for a paper whose core claim is that VAE compression of concept vectors yields superior representations.

### Minor

- **The concept evaluation is entirely qualitative.** Figure 3 shows interesting concept decompositions, but there is no quantitative assessment of explanation faithfulness, completeness, or concept-removal impact. Standard evaluations from the concept-based interpretability literature (e.g., concept insertion/removal tests, alignment with human-annotated attributes on CUB, or agreement with ground-truth concept correlations) are absent. The claim that CEIR "can capture both high-level and fine-grained semantic concepts" is supported only by cherry-picked examples.

- **Loss function design choice in Equation (1) is not justified.** The cubed similarity alignment ($\bar{l}_k^3 \cdot P_{:,k}^3$) is non-standard. An ablation comparing it to standard cosine similarity or temperature-scaled softmax would strengthen the method section.

- **No comparison of VAE variants or alternatives.** The paper uses "vanilla VAE" with no ablation comparing it to PCA, a plain autoencoder, or a β-VAE on the concept vectors. The choice of VAE latent dimensionality K is not discussed or ablated.

- **Open-world mining (Section 4.4) is a demonstration without metrics.** The word cloud and qualitative examples are evocative, but there is no quantitative evaluation of label quality, alignment score, or comparison to alternative label generation methods.

### Trivial
None.

## Nice-to-Haves

- An ablation training the VAE on training-only data and comparing clustering results to the merged-set version would directly address the main concern and likely not change the conclusions given the VAE's reconstruction task.

- A comparison against using LF-CBM bottleneck outputs directly as representations for clustering would isolate the VAE's contribution.

- Quantitative concept faithfulness evaluation (e.g., measuring how well the top-k concepts predict human-annotated attributes on CUB or Broden) would substantially strengthen the interpretability claims.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The details are deferred to the appendix (missing), so reproducibility is limited"** — The appendix was stripped by the PDF parser; it exists in the original submission. Removed per policy.

- **"The concept pool generation details limit reproducibility"** — Same as above; appendix references are to content that exists in the original submission.

- **Criticisms about missing full concept pool, GPT-4 prompts, hyperparameters** — Same appendix-stripping issue.

- **"Preserving class-related concepts while using test set labels for early stopping makes this disclaimer unconvincing"** — The paper explicitly states a dedicated ablation (Appendix A.2.3) supporting this claim; the critic's suspicion about class-related concepts conflates two separate concerns (concept preservation vs. test set usage). The test-set leakage concern is already captured in the Major weakness above.

## Novel Insights

None beyond the paper's own contributions. The key observation — that concept vectors from CBM can be compressed into representations that are simultaneously interpretable via concept attribution and performant for clustering — is the paper's own contribution.

## Suggestions

1. **Fix the VAE training protocol.** Train the VAE only on training data (or hold out a validation split from the training set). Re-run the clustering experiments and report updated results alongside the current ones for comparison. This is the single highest-priority fix.

2. **Add the missing baseline: cluster directly on the concept vectors q_i.** Report NMI/ACC/ARI for K-means on q_i in Table 2. This will show whether the VAE improves or merely preserves the information in the concept vectors.

3. **Add a quantitative interpretability evaluation.** A simple experiment: on CUB (which has attribute annotations), measure whether CEIR's top-k attributed concepts correlate with ground-truth bird attributes. Alternatively, run concept removal tests (remove top concepts and measure accuracy drop).

4. **Ablate the cubed similarity in Eq. (1).** Compare against standard cosine similarity to justify or simplify this design choice.

5. **Discuss the test set leakage explicitly in the Discussion section** (Section 5), acknowledging the limitation and ideally providing preliminary evidence (or citing ongoing work) that the results would hold under a clean protocol.

## Score and Decision

**Bracketing:** Round 1 placed the paper between weak anchors (avg <3.5) and strong anchors (avg >7.5) on concept-based representation learning. Round 2 narrowed to a middle band of CBM papers (avg 4.33–5.60), including Zero-shot CBM (4.83, rejected), Editable CBM (5.60, rejected), SupCBM (5.00, rejected), and Hierarchical CBM (4.75, withdrawn).

**Round 1 bracket:** [3.5, 7.5]

**Round 2 narrowing:** The paper's contribution (novel pipeline combining concept bottleneck + VAE for representation learning) is conceptually stronger and more original than the Editable CBM and SupCBM papers, which largely apply existing techniques (influence functions, LLM-based concepts) to CBMs. However, the test set leakage issue is a substantive methodological concern that the CBM papers at the 4–5 level do not face (or face less severely). The paper's interpretability evaluation is also more limited than what a 6+ paper in this area would typically provide (no quantitative faithfulness metrics, no comparison against concept-based alternatives).

Compared to the Editable CBM anchor (avg 5.60, borderline reject with reviewers split 5-6): CEIR has a more novel contribution but also a more concerning evaluation flaw. Compared to the SupCBM anchor (avg 5.00): CEIR is stronger on novelty and empirical breadth but weaker on evaluation rigor. On balance, the paper sits slightly above the middle of the anchor cluster but is held back by the evaluation protocol issue.

**Final score:** 5.5 — a paper with a genuinely interesting contribution that is undercut by a significant (but fixable) evaluation weakness. The contribution is real but the central empirical claims cannot be accepted as-is.

**Anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| H6XYCIlZdo.md | 3.00 | R1 | Much weaker; withdrawn rejection about non-parametric clustering |
| wZiH43e5Ah.md | 3.00 | R1 | Weaker; concept extraction framework for interpretability |
| eRAXvtP0gA.md | 2.50 | R1 | Much weaker; primitive unsupervised cognition approach |
| UCOPY3FZQW.md | 3.00 | R1 | Weaker; concept factorization for clustering |
| 5Aem9XFZ0t.md | 4.83 | R1/R2 | Comparable quality but different contribution; zero-shot CBM rejected for limited novelty |
| uuvujfQXZy.md | 4.33 | R1 | Weaker; selective CBMs without predefined concepts |
| Q9Z0c1Rb5i.md | 5.00 | R1/R2 | Comparable; SupCBM rejected but had clear contribution; CEIR is more novel |
| Rv55TnDZ2W.md | 5.60 | R1 | Comparable-strength anchor; Editable CBM rejected but borderline (scores 5-6) |
| tcsZt9ZNKD.md | 8.20 | R1 | Much stronger; sparse autoencoders (oral) — different subfield |
| PBjCTeDL6o.md | 8.00 | R1 | Much stronger; unlearning-based interpretations (oral) |
| xriGRsoAza.md | 8.00 | R1 | Much stronger; inherently interpretable TSC (spotlight) |
| G32oY4Vnm8.md | 8.00 | R1 | Much stronger; prototype-based tabular representation learning (spotlight) |
| WqsYs05Ri7.md | 5.20 | R2 | Comparable; uncertainty-aware concept explanations rejected for presentation issues |
| gM8X6RbXkV.md | 4.75 | R2 | Weaker; hierarchical CBM withdrawn, limited novelty |
| eE2PXlNydB.md | 6.00 | R2 | Stronger (accepted poster); compositional zero-shot learning — different problem setting |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>