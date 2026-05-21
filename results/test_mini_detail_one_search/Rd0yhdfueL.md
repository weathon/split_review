## Summary

This paper introduces Bhav-Net, a dual-space architecture with graph transformer processing for distinguishing antonyms from synonyms across eight languages. The method uses language-specific BERT encoders followed by separate projection heads for synonym and antonym spaces, graph transformer processing over word-pair batches, and a margin-based contrastive loss. The main evidence is strong English benchmark performance (0.91 F1, Table 2) and multilingual results compared against BERT baselines (Table 3).

## Strengths

- **State-of-the-art English benchmark results:** Table 2 reports Bhav-Net achieving 0.91 average F1 across adjectives, verbs, and nouns, outperforming SimCSE-based (0.89), Distiller (0.87), ICE-NET (0.84), and AntSynNET (0.82). These are concrete, measurable gains on a well-established English benchmark (Nguyen et al., 2017a), providing evidence that the overall architecture advances the state of the art.

- **Novel dual-space architectural design:** Section 3.2 defines separate projection functions \(f_{\text{syn}}\) and \(f_{\text{ant}}\) (Eqs. 3–6) that map BERT representations into distinct synonym and antonym spaces, with the margin loss (Eqs. 16a–16c) enforcing that synonym pairs have high similarity in the synonym space while antonym pairs have low similarity in the antonym space. This inductive bias is a principled departure from prior single-space approaches.

- **Multilingual dataset construction and analysis:** Table 1 provides balanced antonym/synonym pairs for eight languages derived from WordNet and ConceptNet, and Table 3 shows a clear correlation between BERT encoder quality and downstream F1 (English 0.89 BERT → 0.91 Bhav-Net; French 0.71 → 0.74), supporting the paper's claim that embedding quality is the primary performance bottleneck across languages.

## Weaknesses

### Major

- **Missing ablation results for the three listed variants.** Section 4.2 explicitly names three ablation variants (Single-Space, No Graph, No Contrastive), but their results never appear in any table or figure. The paper claims in Section 5.2 that "the graph transformer adds 2–4% absolute F1 via higher-order relational reasoning" — a specific quantitative claim that cannot be verified without showing the No Graph variant's performance. Without the ablation study, the reader cannot isolate whether the dual-space projection, the graph transformer, or the contrastive loss actually contributes to the reported gains. This is a standard methodological requirement for any architecture paper making component-level claims.

- **Unsubstantiated cross-lingual transfer claim.** Section 5.1 states: "Cross-lingual transfer experiments demonstrate that models trained on high-resource languages can provide meaningful initialization for low-resource languages, improving performance by 3-7% F1-score compared to language-specific training from scratch." No experiment, table, or figure in the paper supports this claim — there is no zero-shot transfer, fine-tuning from multilingual model, or any cross-lingual initialization experiment presented anywhere. The paper's first research question (RQ1) asks "How can semantic relationship understanding be effectively transferred..." yet provides no experimental answer. A central claim of the paper is presented as fact without evidence.

- **"BERT F1-Score" baseline is critically underspecified.** Table 3 compares Bhav-Net against "BERT F1-Score" for each of eight languages, but the paper never explains how this baseline is produced — is it a fine-tuned BERT classifier? A linear probe on frozen BERT embeddings? Zero-shot? The baseline methods section (Section 4.2) lists AntSynNET, ICE-NET, Distiller, and SimCSE-based but does not include "BERT fine-tuning" as a described baseline. Without knowing what the BERT baseline actually is, the comparison in Table 3 is difficult to interpret.

### Minor

- **Contradiction between the dual-space motivation text and the margin loss.** Line 121 states "antonyms require a complementary space where oppositional relationships become apparent through high similarity." Yet Eq. 16b forces antonym similarity in the antonym space to be below \(m_{\text{ant}} = 0.2\), i.e., low similarity. The loss description on line 241 correctly says "for antonym pairs, similarity in antonym space should be below \(m_{\text{ant}}\)," so the equations are internally consistent — the issue is that the architectural motivation (line 121) claims the opposite of what the loss implements. This is confusing but fixable; it does not invalidate the method.

- **Graph construction is under-specified for reproducibility.** Section 3.3 describes edges based on word overlap, semantic similarity above threshold \(\tau\), and transitivity constraints, but \(\tau\) is never given, the batch-structuring logic is not detailed, and how the graph varies across different batch compositions is not discussed. This makes the graph transformer component difficult to reproduce independently.

- **No confidence intervals or variance reported.** Given the small dataset sizes for several languages (French: 702 pairs, Spanish: 1,130, Italian: 1,166), the absence of any variance estimate (standard deviation over runs, confidence intervals) raises questions about the reliability of the reported F1 scores for these languages.

### Trivial

- The reference list contains "?" as a citation (line 96 in the original PDF extraction) — a formatting artifact from the parsing.

## Nice-to-Haves

- A sensitivity analysis of the graph construction threshold \(\tau\) and the contrastive loss weight \(\lambda\) would strengthen the empirical characterization of the method.
- t-SNE or UMAP visualizations of the dual projection spaces would help illustrate the claimed separation of synonym and antonym representations.

## Removed Points

The following criticisms from the input reviews were removed with justification:

- *"No cross-lingual baselines presented"* (Harsh Critic, Critical Issue 2, first sentence): Partially incorrect. Table 3 does present BERT F1-Score as a per-language baseline. The real problem is that this baseline is underspecified, not absent. Demoted to the Major weakness about underspecification above.
- *"The method is not simple/efficient"* (Harsh Critic, Section-by-Section Notes): A scope-creep opinion about what "simple" means, not a concrete flaw in the paper's claims.
- *"Incomplete Algorithm 1"* (Harsh Critic): The algorithm covers the main training loop at a reasonable level of abstraction for a conference paper; further detail would be nice-to-have but is standard.
- *"Small multilingual datasets"* (Harsh Critic): The dataset sizes reflect resource availability in WordNet/ConceptNet, which the paper transparently reports. This is a field limitation, not a paper flaw.
- *"Missing related work"* (Harsh Critic's "?" citation note): Removed per hard rules — missing related works cannot be confirmed without external sources.
- *Strength Finder's Strength 3* ("Graph transformer yields 2-4% F1 improvement"): The claim is stated but the ablation results that would support it are not shown. Incorporated into the Major weakness about missing ablation results rather than counted as a strength.
- *Strength Finder's Strength 4* ("Cross-lingual knowledge transfer"): No experiment supports this claim. Removed as unsupported.
- *Strength Finder's generic strengths* about importance of the problem: Removed as generic/superficial per filtering rules.
- *Formatting/typo nitpicks*: Removed per hard rules (parser artifacts).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report the ablation results.** Add a table showing F1 scores for the full Bhav-Net, Single-Space, No Graph, and No Contrastive variants on English and at least 2–3 other languages (e.g., German, French). This is essential to validate the component-level claims.

2. **Conduct and report a cross-lingual transfer experiment.** The simplest design: train on English data, evaluate zero-shot on the other seven languages, and compare against language-specific training from scratch. This directly answers RQ1.

3. **Clarify the BERT baseline.** Describe whether it is a fine-tuned classifier, a linear probe, or something else. If it is a fine-tuned BERT, include it as a described baseline in Section 4.2.

4. **Resolve the motivation/loss inconsistency.** Either rephrase line 121 to say antonyms have low similarity in the antonym space (where opposition is detected through contrast with the synonym space), or correct the text to match what Eq. 16b actually does.

5. **Report confidence intervals or standard deviations** for the multilingual results, especially for the smaller datasets (French, Spanish, Italian, Russian).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|---|---|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gye2U9uNXx.md` | 7.50 | Much stronger: complete methodology, thorough evaluation, clear writing. This paper is not at this level. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4v4RcAODj9.md` | 6.50 | Much stronger: DUALFormer has extensive experiments, ablation studies, and theoretical analysis. This paper lacks all three. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BCyAlMoyx5.md` | 5.67 | Moderately stronger: cross-lingual LLM paper has mixed reviews but provides complete experimental results for its claims. This paper's missing experiments prevent comparable evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EVuANndPlX.md` | 5.60 | Moderately stronger: GNN-RAG has thorough evaluation on two benchmarks despite some reviewer concerns about novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gjRhw5S3A4.md` | 7.00 | Much stronger: GraphBridge has comprehensive experiments across 16 datasets and proper ablation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xN6z16agjE.md` | 3.00 | Comparable in execution gaps: the Arabic hypernymy paper has limited novelty but its experiments are at least complete. This paper has a stronger contribution but incomplete experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8QTpYC4smR.md` | 1.00 | Far worse: an empty survey with no contribution. This paper is meaningfully better. |

This paper presents a genuinely novel architectural idea (dual-space + graph transformer for antonym/synonym distinction) and shows strong English benchmark results. However, two major experimental gaps — the missing ablation study and the unsubstantiated cross-lingual transfer claim — prevent the paper from supporting its core architectural and transfer-learning claims. The paper needs substantial additional experiments before it can be accepted at a top venue.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>