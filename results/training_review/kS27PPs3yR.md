Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes FAPrompt, a framework for zero-shot anomaly detection (ZSAD) that learns multiple fine-grained abnormality prompts via a compound normal+abnormal token design (CAP module) and adapts them per test image using a data-dependent abnormality prior (DAP module). The core idea — decomposing abnormality semantics into multiple complementary prompts built on shared normal tokens — is a clean extension of prior prompt-based ZSAD methods (e.g., AnomalyCLIP). Evaluations across 19 industrial and medical datasets show consistent improvements, with average gains of 3–5% AUC/AP over strong baselines.

## Strengths

- **Novel compound prompting design (CAP) for fine-grained abnormality semantics**: The paper introduces a principled way to learn multiple decomposed abnormality prompts, each formed by shared normal tokens plus a few learnable abnormal tokens (Eq. 1). This allows the model to capture diverse defect types (e.g., stains, cuts, holes) without manual annotation, directly addressing the coarse-grained limitation of prior methods like AnomalyCLIP. The orthogonal constraint (Eq. 2) encourages diversity among prompts without requiring per-defect-type supervision.

- **Consistent improvements across a broad evaluation**: The method is evaluated on 19 datasets spanning industrial and medical domains, using both image-level (AUROC, AP) and pixel-level (AUROC, PRO) metrics. Tables 1 and 2 show coolname achieves best or second-best results on nearly every individual benchmark. The average gains over the best competing methods are meaningful: 3.7%/4.9% (industrial image), 5.2%/3.4% (medical image), 2.7%/4.4% (industrial pixel), 3.0%/3.7% (medical pixel).

- **Rigorous ablation and hyperparameter analysis**: Table 3 systematically ablates each component (CAP alone, DAP alone, with/without L_oc, with/without L_prior), confirming the contribution of each design choice. The comparison against a naive AnomalyCLIP ensemble (Table: various_prompt) convincingly shows that coolname's orthogonal regularization yields genuinely complementary prompts rather than redundant ones.

- **Principled handling of normal images in DAP via L_prior**: The abnormality prior loss (Eq. 6) suppresses noise injection from normal images by penalizing non-zero priors from normal samples. The ablation ("DAP w/o L_prior") shows this design choice is important, especially for pixel-level performance.

## Weaknesses

### Fatal
None.

### Major
- **Overstated performance claims in the abstract and contributions**: The abstract (line 10) and contributions list (line 52) claim coolname "substantially outperforms state-of-the-art methods by at least 3%-5% AUC/AP." However, per-dataset results tell a more nuanced story: on MVTecAD (the most widely used industrial benchmark), coolname's image-level AUROC (91.9) trails AnoVL (92.5) and only improves over AnomalyCLIP by 0.4%. On MVTecAD pixel-level AUROC, coolname (90.6) underperforms AnomalyCLIP (91.1). The main text (line 244) correctly qualifies these as *average* improvements ("on average... up to 3.7%"), but the abstract uses the unqualified "at least," which is materially misleading. This discrepancy between the abstract's strong claim and the actual per-dataset headroom should be corrected.

- **The claim of "fine-grained abnormality semantics" is not directly validated**: The paper asserts that each of the K abnormality prompts captures a distinct defect type (e.g., color stains vs. cuts vs. holes). However, the only evidence provided is a t-SNE visualization (Fig. 5) showing that different prompts produce different anomaly score distributions — this demonstrates diversity but not that any specific prompt maps to a semantically interpretable defect category. Without a per-prompt diagnosis (e.g., showing which prompt fires most strongly for known defect types in MVTecAD categories like "carpet stain" vs. "carpet cut"), the claim of "fine-grained semantics" at the prompt level remains unsubstantiated.

### Minor
- **Pixel-level results on MVTecAD are mixed**: On the most standard pixel-level benchmark, coolname achieves 90.6 AUROC vs. AnomalyCLIP's 91.1 — a regression of 0.5 AUROC — while improving PRO (83.3 vs. 81.4). This mixed result should be acknowledged. The paper's claim of improvement "in both image- and pixel-level ZSAD tasks" (abstract) is too sweeping given this regression on a key metric of a key dataset.

- **DAP's marginal gain on top of CAP is small for image-level performance**: Adding DAP to CAP improves image-level AUROC by only +0.1% on industrial datasets and +0.3% on medical (Table 3). While DAP alone (without CAP) gives meaningful standalone gains (+1.9%/2.5% on industrial/medical image-level), its *incremental* contribution on top of CAP is near-negligible for image-level tasks. The paper's emphasis on DAP as a co-equal contribution should be tempered. (Note: pixel-level gains from DAP on top of CAP are more substantial — +0.4/+1.1 PRO on industrial, +1.6/+2.1 on medical — so the contribution is real for pixel-level.)

- **The orthogonal constraint uses absolute-value cosine similarity without discussion**: Eq. 2 uses |cos_sim|, which penalizes both positive and negative correlations equally. The paper does not explain why sign-agnostic orthogonality is preferred over simply encouraging low absolute correlation (which is equivalent to encouraging either orthogonality or anti-correlation). While this is a minor design detail, it merits at least a brief comment.

- **The DAP module constitutes test-time adaptation without discussion of its implications**: DAP derives a per-image prior from the test image itself during inference (Eq. 3–5). The paper cites CoCoOp as inspiration, but does not explicitly discuss how this test-time adaptation differs from the purely zero-shot setting that competing methods (e.g., AnomalyCLIP's frozen prompts) operate in. An ablation withholding DAP during inference (i.e., using only CAP's prompts without per-image prior) would help quantify the benefit attributable to test-time adaptation vs. the learned prompts alone.

### Trivial
- The phrase "by at least 3%-5%" in the abstract uses both "at least" (implying a lower bound) and a range ("3%-5%"), which is internally inconsistent: "at least 3%" and "at least 5%" are different statements. This should be rephrased to e.g., "by 3%-5% on average."

## Nice-to-Haves
- A per-prompt defect-type analysis on a dataset like MVTecAD (which has 15 distinct categories with known defect types) showing which prompt(s) activate most strongly for each specific anomaly type.
- An ablation freezing DAP at test time (i.e., using CAP prompts without per-image prior during inference) to isolate the effect of test-time adaptation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Circular dependency in DAP (harsh critic, point under "Method (Eq. 6, DAP)")**: The critic claims that DAP has a "circular dependency" where "the prototype selects patches, then those patches update the prototype" that could lead to degenerate solutions. This is a theoretical concern not backed by any evidence; the empirical results (Table 3) consistently show DAP improves performance, and the process is a standard iterative refinement (akin to self-training or EM), not a pathological feedback loop. The paper's positive results demonstrate the design works as intended.

- **"Loss design has no methodological novelty" (harsh critic, point under "Training (Eq. 12–13)")**: The paper never claims novelty in the loss design — it adopts focal and dice losses following AnomalyCLIP. Criticizing the loss for lacking novelty is attacking a non-claim.

- **Selective reporting on DAP marginal gains (harsh critic, point under "Ablation (Table 3)")**: The critic claims DAP yields "only +0.1–0.3%" but only cites the *image-level* numbers while ignoring the more substantial *pixel-level* gains (+0.4/+1.1 industrial, +1.6/+2.1 medical). This selective framing understates DAP's actual contribution, particularly for the pixel-level task.

- **Strength Finder's claim about "consistent state-of-the-art results across 19 diverse datasets"**: This conflicts with the verified weakness about MVTecAD performance. The claim is partially true (best/second-best on *nearly all* datasets) but overreaches. The weakness wins per the rules; this strength is tempered in the main review.

- **Strength Finder's "data-dependent abnormality prior improves cross-dataset generalization"**: The ablation shows DAP helps, but the benefit on top of CAP is small for image-level. This strength is retained in spirit but qualified.

- **Strength Finder's claim about "Orthogonal constraint ensures complementary abnormality prompts"**: Supported by the ablation (CAP w/o L_oc performs worse) and t-SNE visualization. Retained in strengths but the t-SNE limitation (doesn't show specific defect types) is noted as a weakness.

## Novel Insights

Beyond the paper's own contributions, the key tension surfaced by the reviews is this: the *architectural novelty* (compound prompting with shared normal tokens) is clearly responsible for most of the performance gain, while the *instance-conditional adaptation* (DAP) adds modest incremental value. This suggests that the field's current gains in prompt-based ZSAD may be driven more by representation capacity (more prompts, better decomposition of the abnormality space) than by per-instance adaptation. The orthogonal constraint's role in enabling this without per-type supervision is a practically useful finding.

## Suggestions

1. **Correct the abstract's performance claims**: Replace "by at least 3%-5%" with a more precise statement, such as "by 3%-5% on average across 19 datasets," to accurately reflect the results in Tables 1–2.
2. **Acknowledge the MVTecAD pixel-level AUROC regression**: Add a sentence discussing why PRO improves but AUROC slightly decreases on MVTecAD pixel-level, and contextualize this against the overall positive trend.
3. **Add a per-prompt diagnostic experiment**: On a dataset with known anomaly types (e.g., MVTecAD's 15 categories), show which of the K abnormality prompts produces the highest anomaly score for each specific defect type, to substantiate the "fine-grained" claim.
4. **Add a DAP-free inference ablation**: Compare full coolname vs. a variant that uses CAP prompts without DAP adaptation during test-time inference, to separate the contribution of learned prompts from test-time adaptation.
5. **Briefly discuss the absolute-value choice in L_oc**: A sentence explaining why sign-agnostic orthogonality is preferred would address a natural reader question.

## Score and Decision

**Originality**: Good — the compound prompting design is a novel combination of ideas (shared normal tokens + multiple abnormal prompt + orthogonal constraint). Not groundbreaking but a solid incremental contribution.

**Importance of research question**: High — zero-shot anomaly detection is practically important, and the limitations of coarse-grained prompts are a real problem.

**Claims supported**: Mostly yes, but the abstract overclaims (see Major weakness #1). The central technical claim — that compound prompting improves ZSAD — is well-supported.

**Soundness of experiments**: Good — 19 datasets, two metrics per task, proper comparisons, ablation study, hyperparameter sensitivity analysis. Missing: per-prompt defect-type analysis, DAP-free inference ablation.

**Clarity of writing**: Generally clear. The method description is well-structured.

**Value to community**: Moderate-positive. The CAP module is a practically useful design, and the extensive benchmark results provide a strong reference point.

The paper has a real contribution (the CAP module) and strong experimental support across an unusually large number of datasets. The main issues are claim accuracy (fixable in revision) and one missing diagnostic (per-prompt semantics). These do not invalidate the core contribution but require attention.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>