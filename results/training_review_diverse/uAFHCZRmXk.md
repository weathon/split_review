Now I have a thorough understanding of the paper. Let me compile my final review.

## Summary

This analysis paper investigates two phenomena in contrastive VLMs — the modality gap and object bias — and proposes that both share a common cause: **information imbalance** between images (information-rich) and captions (information-sparse). The paper introduces two new metrics (RMG for the modality gap, MOAD for object bias), runs controlled synthetic experiments on a custom MAD dataset, and validates on real data (CC12M). The central finding is that reducing information imbalance simultaneously decreases both the modality gap and object bias while improving performance, and that the modality gap may serve as a mechanism for controlling logit entropy.

## Strengths

- **Causal identification of information imbalance as the common trigger via controlled synthetic experiments**: The paper's strongest contribution. On the MAD dataset (Morpho-MNIST based), the authors systematically vary the number of attributes in captions while keeping images identical. Results (Figure 6) show that as information imbalance decreases, the modality gap shrinks, object bias reduces, and accuracy improves — a clean causal demonstration. This goes well beyond prior correlational studies.

- **Introduction of MOAD as a formal, quantitative metric for object bias**: Previous work only inferred object bias from poorer attribute performance. MOAD (Section 5) directly measures the bias toward objects versus attributes by comparing within-class vs. between-class similarities. The metric is validated by showing that per-sample caption presence bias (Figure 5b) — not global word frequency (Figure 5a) — causes object bias.

- **Reveals that only few embedding dimensions drive the modality gap**: Analysis of mean differences (Figure 3a) shows most dimensions have similar means across modalities while a few have stark differences. The ablation experiment (Figure 3c) confirms that removing these few dimensions closes the gap, providing geometric insight not previously documented.

- **Shows dissimilar local neighborhoods between modalities**: Using normalized Kendall-τ distance (Table 1), the paper demonstrates that image and text embeddings have substantially different neighbor orderings (~0.5 for ImageNet-100), directly explaining why post-hoc translation approaches fail to improve performance despite closing the gap.

- **Disentangles confounders in the modality gap–performance relationship**: Section 4.1 shows across 98 VLMs that the apparent positive correlation between gap size and performance is driven by confounders like model size. The correlation table (Table 1) reveals that model/embedding/dataset size correlate more strongly with performance than the modality gap does.

- **Validates findings across diverse experimental scales**: The paper uses fully-controlled synthetic data, real-data experiments on CC12M, and a large-scale analysis of 98 pre-trained VLMs (CLIP, SigLIP, etc.), strengthening generalizability.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claim — that information imbalance triggers both the modality gap and object bias — is well-supported by the controlled synthetic experiments. The remaining issues are addressable in a revision.

### Minor

- **The real-data manipulation of information imbalance (Section 6) has a methodological confound**: Dropping contiguous halves or three-quarters of captions likely changes not only the amount of information but also syntactic structure, token positions, and the distribution of objects vs. attributes. The observed increase in modality gap could partly reflect these confounds rather than purely information imbalance. The synthetic experiments cleanly establish causality, so this does not undermine the core claim, but the real-data validation — important for generalizability — is weakened. A more controlled manipulation (e.g., randomly dropping tokens proportionally) or replication on multiple real datasets would strengthen this link.

- **The entropy–temperature experiment (Section 6.1) lacks statistical rigor**: The key comparison (fine-tuning with frozen vs. learnable temperature on "quarter" captions) is presented as a single experiment — one model, one dataset, one split — with no reported variance, no replication, and no statistical test. The paper includes a footnote disclaiming causality ("we do not claim a causal relationship"), which partially mitigates this concern. However, given that the takeaway ("the modality gap can be interpreted as a feature") is a novel and emphasized claim, additional runs with different seeds or a more direct causal manipulation would substantially strengthen confidence.

- **The controlled analysis of gap vs. performance after accounting for confounders is deferred to the appendix**: Finding (1) states that "controlling for confounders suggests a lower modality gap correlates with better performance," but the controlled analysis (partial correlations or regression) is only referenced via `\cref{sub:fixed_dataset}` in the appendix (stripped by the parser). While the main text convincingly shows that confounders exist (Table 1), the actual controlled results are not visible to the reader without consulting the appendix. Moving a summary of this analysis (e.g., a partial correlation table) to the main text would significantly strengthen the paper's first major claim.

- **Framing tension between "gap as problem" and "gap as feature" is not fully reconciled**: The paper initially frames the modality gap as an undesirable effect worth fighting (Finding 1: closing the gap improves performance), but later reinterprets it as a beneficial feature for entropy control (Section 6.1). While both positions can be consistent (the gap is a by-product that has both costs and benefits), the paper does not explicitly reconcile them or discuss when practitioners should try to close the gap vs. leave it intact.

- **The claim that "object bias is not caused by word frequency" relies on a single analysis on LAION-2B** (Figure 5a). The synthetic experiments (Figure 5b) independently support the per-sample caption presence explanation, but the direct real-data evidence for this negative claim would benefit from replication on additional datasets.

### Trivial
- The narrative around Table 1 describes "no to weak positive correlations" between gap and performance, but for medium-scale models on ImageNet the correlations are actually slightly negative (L2M: −0.008, RMG: −0.109). Neither is statistically significant, so the narrative is not wrong, but it slightly over-smooths the data.

## Nice-to-Haves
- Including error bars or multiple-run statistics for the key fine-grained experiments (information imbalance on real data, entropy–temperature comparison) would improve the paper without changing its conclusions.
- A brief discussion of limitations: the synthetic data (Morpho-MNIST) uses simple digit images with few predefined attributes, and the extent to which results transfer to complex natural images with thousands of attributes is worth acknowledging explicitly.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **Critical Issue 1 from harsh critic** ("the central claim is not supported by evidence in the main text"): This criticism complains about the controlled analysis being deferred to the appendix (`\cref{sub:fixed_dataset}`). Per the hard rule — "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references" — the appendix exists in the original submission and was stripped by the parser. The criticism is removed as a major issue but downgraded to minor (above) since the main text would benefit from including a summary of the controlled analysis.
- **Section 4.2 criticism** ("the conclusion that few dimensions drive the gap remains correlational"): The ablation experiment (Figure 3c) is a causal manipulation — removing high-difference dimensions closes the gap — not merely correlational. This criticism misreads the evidence.
- **Generic formatting/style nitpicks**: Removed per hard rules.
- **Missing related works mentions**: Removed per hard rule about external verification.

## Novel Insights
Beyond the paper's own contributions, the reviews surface a useful synthesis: the paper's strongest evidence is the synthetic MAD experiment (Figure 6), which cleanly establishes information imbalance as causally upstream of both phenomena. The entropy link (Finding 6) is the most novel but also the least supported claim. The tension between "gap is bad" (Finding 1) and "gap is a feature" (Finding 6) is a genuine conceptual loose end that the authors should address explicitly in revision — perhaps by framing the gap as a *symptom* of the model's entropy-regulation strategy that becomes problematic primarily when information imbalance is large. The real-data confound (contiguous caption dropping) is a legitimate concern but does not threaten the paper's main thesis because the synthetic experiments carry the causal weight.

## Suggestions
1. Add a summary of the controlled (confounder-adjusted) gap–performance analysis to the main text — even a single table of partial correlations would make Finding 1 self-contained.
2. Run the entropy–temperature experiment with at least 3 different seeds, report means and ranges, and optionally include a more direct causal manipulation (e.g., artificially increasing the gap post-hoc and measuring entropy change).
3. Use a more controlled caption manipulation for the real-data information imbalance experiment (e.g., randomly dropping tokens proportionally rather than dropping contiguous chunks) or replicate on a second dataset (e.g., RedCaps).
4. Explicitly reconcile the "gap as problem" vs. "gap as feature" framing in the discussion or conclusion.

## Score and Decision
The paper makes a genuine contribution by identifying information imbalance as the common cause of both the modality gap and object bias in contrastive VLMs. The synthetic experiments provide clean causal evidence, the metrics (RMG, MOAD) are well-designed, and the large-scale analysis across 98 models adds breadth. The weaknesses — primarily around statistical rigor in the confirmatory experiments and the deferred controlled analysis — are addressable and do not undermine the core claims. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>