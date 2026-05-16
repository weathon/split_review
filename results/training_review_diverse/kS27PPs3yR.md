Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes FAPrompt, a zero-shot anomaly detection framework that learns fine-grained abnormality prompts. It introduces two modules: (1) Compound Abnormality Prompting (CAP), which decomposes abnormality prompts into shared normal tokens + learnable abnormal tokens with an orthogonal constraint for diversity; and (2) a Data-dependent Abnormality Prior (DAP) module that adapts prompts per test image by selecting top-M abnormal patches as a sample-wise prior. Evaluated on 19 industrial and medical datasets, the method achieves strong average improvements over existing ZSAD methods.

## Strengths

- **Compound Abnormality Prompting (CAP) for fine-grained anomaly representation**: CAP explicitly models diverse anomaly types via decomposed prompts with shared normal tokens (Eq. 1) and an orthogonal constraint (Eq. 2). The ablation study (Table 3) confirms CAP alone improves the base model AnomalyCLIP by 3.1/3.4 points (image-level AUC/AP) on industrial datasets and 2.9/2.5 points on medical datasets, demonstrating that fine-grained, non-redundant prompts capture anomalies that coarse-grained approaches miss.

- **Data-dependent Abnormality Prior (DAP) for cross-dataset generalization**: DAP adapts abnormality prompts per test image without requiring target dataset training. The ablation shows DAP alone improves pixel-level PRO on medical datasets by 1.9 points over the base model, and the full model (CAP+DAP) outperforms either module alone, confirming the value of per-sample adaptation.

- **Comprehensive and state-of-the-art evaluation**: The paper evaluates on 19 real-world datasets across industrial and medical domains (Tables 1, 2). The full model achieves best or second-best results on most tasks, with notable gains on challenging medical datasets (e.g., +5.2 AUROC on BrainMRI, +3.2 on Br35H over the second-best method). Average improvements over the strongest baselines reach 3–5% on several metric/dataset groupings.

- **Ablation isolates each component's contribution**: Table 3 systematically ablates CAP (with/without L_oc) and DAP (with/without L_prior), showing both modules and both loss terms contribute positively. This allows the reader to see that the prompting innovation alone (CAP) already outperforms the base model.

- **Comparison against ensemble baselines**: The paper shows FAPrompt's K=10 complementary prompts outperform an ensemble of 10 independently trained AnomalyCLIP models (Table "various_prompt"), directly supporting the claim that non-redundant fine-grained prompts capture richer semantics than a bag of coarse ones.

- **Hyperparameter sensitivity analysis**: The paper systematically examines sensitivity to K, M, and token lengths (E, E'), providing practical guidance for deployment.

## Weaknesses

### Fatal

None.

### Major

- **"At least 3%-5%" claim is overstated**. The abstract and contribution list state that FAPrompt "substantially outperforms state-of-the-art methods by at least 3%-5% AUC/AP" in both image- and pixel-level tasks. However, on **MVTecAD** (image-level AUROC: FAPrompt 91.9 vs. AnoVL 92.5) and **AITEX** (image-level AUROC: FAPrompt 71.9 vs. WinCLIP 73.0 and AnoVL 72.5; pixel-level AUROC: FAPrompt 82.0 vs. AnomalyCLIP 83.0), the method is either second-best or behind multiple baselines. The body text appropriately uses "up to" (lines 244, 279) when reporting per-group averages, but the abstract and contributions use the stronger "at least" phrasing, which is factually incorrect for several datasets. This should be corrected to accurately describe the average gains and acknowledge datasets where the method is not the best.

### Minor

- **The DAP module's computational cost is not discussed**. DAP requires per-test-image processing: top-M patch selection, a forward pass through the abnormality prior network ψ, and crucially a separate text-encoder forward pass with the modified prompts (Eq. 4-6). Methods with fixed prompts can pre-compute text embeddings once; FAPrompt cannot. The paper does not report inference time or compare runtime against baselines, which is relevant for practical deployment.

- **Missing per-dataset ablation results**. Table 3 reports ablation results averaged across 18 datasets for CAP and DAP variants. Per-dataset results would reveal whether the improvements are consistent across datasets or driven by a few, and would allow readers to identify datasets where individual components hurt performance.

- **No discussion of failure cases**. On AITEX and MVTecAD (image-level), the full model underperforms relative to baselines. The paper does not analyze why — e.g., whether these datasets require different granularity, or whether the training set (MVTecAD) transfers poorly to certain domains. Such analysis would strengthen credibility.

- **t-SNE visualization shown for only one dataset** (BTAD 01, Fig. 1). While the figure is a nice qualitative validation, showing it on additional datasets would strengthen the claim of prompt complementarity across domains.

- **The "zero-shot" terminology would benefit from clarification**. DAP uses information from each test image at inference time to modify prompts (which the paper transparently describes). While this is standard ZSAD (no training on the target dataset) and the paper already compares against CoCoOp and AnoVL which also use instance/test-time information, explicitly stating why this is still considered zero-shot (auxiliary dataset training only, no target-dataset fine-tuning) would preempt confusion.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment augmenting AnomalyCLIP with a simple test-time adaptation mechanism (e.g., using its own predictions to select patches and add a learned prior) would further isolate the benefit of the CAP prompting design from the DAP adaptation mechanism. However, the existing ablation (Table 3) already shows CAP alone outperforms AnomalyCLIP, so this is not essential.

- Adding a brief comparison to TPT (Test-Time Prompt Tuning) in the related work would help position DAP's relationship to other prompt adaptation methods.

## Removed Points

- **Criticism about DAP making comparisons "unfair" to fixed-prompt baselines**: Most of the harsh critic's argument about test-time adaptation conflates DAP's per-image processing with online fine-tuning. DAP is a learned, fixed module applied at inference — this is standard in ZSAD. Moreover, the paper already compares against AnoVL (which uses test-time adaptation, acknowledged on line 64) and CoCoOp (which uses instance-conditional prompts). The ablation (CAP-only vs. base) already isolates the prompting innovation. This criticism mischaracterizes the fairness of comparison.

- **Criticism that "the paper should also acknowledge AnomalyCLIP's object-agnostic prompts already generalize across datasets"**: The paper already does this on line 246: "AnomalyCLIP significantly improves performance by learning object-agnostic textual prompts for AD, demonstrating strong generalization capabilities across diverse datasets."

- **Criticism about missing limitations section**: Generic formatting preference that does not affect the paper's substantive value.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — dropped as they lack specific citation or concrete content.

## Novel Insights

The harsh critic makes a noteworthy observation that the paper's core comparison conflates two factors (prompt design and per-image adaptation) but fails to recognize that (a) the ablation study already addresses this separation by reporting CAP-only results, and (b) the paper compares against AnoVL and CoCoOp which also use test-time or instance-conditional information. The more interesting insight is that the "at least" language in the abstract is genuinely misleading — the method is not universally best — and that the paper could be strengthened by acknowledging this nuance rather than overclaiming.

## Suggestions

1. Correct the abstract and contribution list: replace "by at least 3%-5%" with the actual average improvements reported in the body ("up to 3.7%/4.9% on industrial, 5.2%/3.4% on medical") and explicitly note that on some datasets (e.g., MVTecAD, AITEX) the method does not achieve the best result.

2. Add a table or appendix with per-dataset ablation results so readers can see the consistency of CAP/DAP contributions across individual datasets.

3. Report inference-time comparison against key baselines (AnomalyCLIP, CoCoOp) to contextualize DAP's computational overhead.

4. Add a brief discussion of failure cases, particularly on AITEX and MVTecAD where the method underperforms, to strengthen the paper's credibility.

5. Clarify in the methodology or the "zero-shot" framing that while DAP uses test-image information at inference, it requires no target-dataset training or fine-tuning, and therefore is consistent with the ZSAD setting.

## Score and Decision

The paper presents a genuinely novel and well-motivated approach to fine-grained abnormality prompting, supported by extensive experiments across 19 datasets and careful ablations. The core contributions are solid. The main weakness is an overstated claim in the abstract ("at least 3%-5%") that does not hold on every individual dataset, and several minor omissions (computational cost, per-dataset ablation). None of these issues are fatal or undermine the core contribution. With revisions to the overclaim and the minor additions suggested above, the paper would be a clean accept.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>