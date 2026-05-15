Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper introduces Zero-Shot Noisy Test-Time Adaptation (ZS-NTTA), a practical setting where a VLM must adapt to a test stream containing out-of-distribution ("noisy") samples. The authors first show, through a three-pipeline analysis, that existing TTA methods suffer because unfiltered noisy samples produce gradients orders of magnitude larger than clean samples, degrading both classification and detection. Based on this, they propose AdaND, which decouples the classifier from the detector: the VLM backbone and text classifier remain frozen, while a lightweight linear noise detector is trained online using ZS-CLIP's own detection outputs as pseudo-labels. For clean streams, Gaussian noise is deliberately injected to prevent the detector from misclassifying all samples as noise. Experiments across 11 ID datasets and multiple OOD datasets show AdaND outperforming existing TTA methods, and it also transfers well to ZS-OOD detection.

## Strengths

- **Well-motivated problem formulation**: The ZS-NTTA setting fills a genuine gap between TTA (assumes all samples are in-distribution), noisy TTA (requires source prototypes), and ZS-OOD detection (offline, focuses only on detection). The evaluation using Acc_S, Acc_N, and Acc_H is appropriate for the task.

- **Insightful failure analysis of existing TTA methods**: The three-pipeline study (Table 1) cleanly demonstrates that unfiltered noisy samples degrade adaptation more than clean samples improve it. The gradient analysis (Figure 4, Observation 3.3) concretely shows noisy samples producing gradients an order of magnitude larger, with a clear three-stage degradation. These diagnostics provide strong, evidence-based motivation for keeping the classifier frozen.

- **Simple, efficient, and effective method**: AdaND trains only a single linear layer on frozen features using pseudo-labels from the same frozen model. This keeps computational cost nearly identical to ZS-CLIP (~14ms per sample on ImageNet vs ~10ms), while outperforming all compared TTA methods. The design follows directly from the analysis.

- **Comprehensive evaluation**: The paper evaluates across 11 ID datasets and multiple OOD datasets (44 ID-OOD pairs), with ablations on noise type, injection frequency, queue length, threshold window, initial training steps, backbone choice, and noise ratio. Hyperparameters are fixed across all datasets, and ablations show robustness to their choice.

- **Dual benefit (ZS-NTTA + ZS-OOD detection)**: AdaND also advances ZS-OOD detection (9.40% improvement in FPR95 over prior methods), which is a notable side benefit.

## Weaknesses

### Fatal
None.

### Major

- **No error bars or confidence intervals for main results**: Tables 2, 3, and 5 report single numbers without any variance measure. The paper does run 5-seed experiments for the varying-order simulation (CIFAR-10/100, Tables 18—19) and acknowledges the data-stream order can affect results, but the main results across all 11 ID datasets lack uncertainty estimates. Since improvements over ZS-CLIP are sometimes modest (a few percent), it is impossible to assess whether the reported gains are statistically significant or within the noise of stream-order variation. This is the most significant weakness.

### Minor

- **The headline improvement claim (8.32% Acc_H) needs clearer specification**: The paper states "a notable improvement of 8.32% in Acc_H for ZS-NTTA" compared to "existing TTA methods" / "state-of-the-art methods." The exact baseline (best single method vs. average over methods) and whether the number is absolute or relative should be explicitly stated. Since the table values appear only in images, this creates ambiguity. The authors should clarify the comparison basis in the text.

- **The Section 3 failure analysis is conducted on a single ID-OOD pair (CIFAR-10/SVHN)**: The three-pipeline study (Table 1), score distribution visualization (Figure 3), and gradient analysis (Figure 4) all use CIFAR-10 as ID and SVHN as OOD. While the phenomenon is plausible and the method's generalizability is supported by the broad results in Section 5, the core diagnostic evidence would be stronger if replicated on at least one more diverse pair (e.g., ImageNet + a near-OOD dataset).

- **Limited analysis of why Gaussian noise injection works**: The paper shows empirically (Table 6, Table 16) that injecting Gaussian noise prevents the detector from collapsing on clean streams. The explanation — "injected noise will be included in the adaptive threshold calculation, preventing the misclassification of clean samples as noisy" — is a plausible heuristic, but the paper does not analyze the mechanism more deeply (e.g., how the threshold or score distribution changes with and without injected noise). This makes the component feel like a well-tuned trick rather than a principled solution.

### Trivial

None.

## Nice-to-Haves

- An analysis of pseudo-label quality: how accurate are ZS-CLIP's pseudo-labels over the course of the stream, and does the linear detector primarily correct ZS-CLIP's mistakes or simply replicate its decisions with higher confidence?
- Extension to near-OOD scenarios (e.g., samples from semantically related novel categories) rather than only far-OOD, to test the method's robustness under more challenging noise conditions.

## Removed Points

*The 8.32% inconsistency claim is flagged for removal.* The reviewer asserts the number is inconsistent with "numbers reported for ImageNet in Section 5.2," citing specific table values (70.60%, 75.92%, 70.41%). These values are from table images that cannot be verified from the extracted text. More importantly, the paper's claim is "compared to existing TTA methods" (plural) / "enhances the *average* performance" — the reviewer appears to compare against a single baseline (ZS-CLIP or SoTTA), which is not what the paper claims. I have kept a clarified version of this concern in Weaknesses (Minor) for transparency.

*The criticism that "the linear detector trained on ZS-CLIP's pseudo-labels has no clear advantage over ZS-CLIP's MCM decision" is removed.* The paper's Section 3 explicitly demonstrates why the frozen classifier should not be adapted: adaptation corrupts the detection ability (Figure 3). AdaND's detector is trained *on the test stream*, adapting to its specific score distribution — this is a fundamentally different operation from applying a fixed MCM threshold. The empirical improvements across all datasets (Tables 2, 3) confirm the detector adds value. The criticism overlooks the paper's own core argument.

*The claim that "the comprehensive experiments in the abstract refer to a single dataset" is weakened.* The analysis section (Sec 3) uses CIFAR-10/SVHN to illustrate a phenomenon, which is standard. The full experimental evaluation (Sec 5) covers 11 ID datasets. The abstract's "comprehensive experiments" encompasses both the analysis and the full benchmarking.

*The criticism of N=10 as ad hoc is removed because the paper supplies an ablation (Table 22) showing robustness to this choice.*

*The criticism that the ZS-OOD comparison is "not perfectly aligned" with CLIPN/NegLabel is partially addressed by the paper's own acknowledgment (line 178) that these methods require extra data while AdaND does not. This asymmetry favors the baseline methods, so it is a valid comparison per the rules.*

*Missing related work criticisms are excluded per instructions.*

## Novel Insights

The most interesting finding in the reviews — beyond the paper's own contributions — is the implicit tension between the analysis and the method. The Section 3 analysis convincingly shows that adaptation *corrupts the detector* even when using an adaptive threshold (Figure 3: Tent's scores for noisy samples creep up, making them indistinguishable from clean samples). Yet AdaND's detector is trained precisely by learning from the test stream — i.e., it is *also* adapted to the data. The fact that this adapted detector *improves* detection (rather than suffering the same fate as Tent) suggests a critical asymmetry: adapting a dedicated detector (trained with binary pseudo-labels on frozen features) is safe, whereas adapting a multi-class classifier's backbone (via entropy minimization or prompt tuning on potentially corrupted samples) degrades detection. This insight — that the *type* of adaptation (detector vs. classifier) determines whether the degeneration spiral occurs — is a genuinely useful nuance that the paper does not explicitly draw, and it would be valuable for future work.

## Suggestions

1. **Add error bars** to the main results (Tables 2, 3, 5) by running 3–5 random seeds with different data-stream orders, at least for a representative subset of ID datasets (e.g., CIFAR-100, ImageNet, and one fine-grained dataset). Report mean ± std in the tables.

2. **Clarify the 8.32% claim**: explicitly state (a) which methods this is the average/improvement over, (b) whether the number is absolute percentage-point difference or relative improvement, and (c) include a direct reference to the relevant table rows so readers can verify.

3. **Strengthen the analysis of Gaussian noise injection**: provide a figure showing the adaptive threshold value and score distribution with/without injected noise in a clean stream, to explain *why* injection prevents clean samples from being misclassified.

4. **Replicate the gradient analysis** (Figure 4) on at least one additional ID-OOD pair (e.g., ImageNet + iNaturalist) to confirm the three-stage pattern generalizes beyond CIFAR-10/SVHN.

5. **Add an analysis of pseudo-label quality**: report the agreement rate between the AdaND detector and ZS-CLIP's decisions, and show examples where the detector corrects ZS-CLIP's mistakes.

## Score and Decision

This paper makes a solid contribution: it identifies a well-motivated practical problem, provides useful diagnostic analysis, and proposes a simple method that is empirically effective and computationally efficient. The main weakness — lack of error bars for the main results — is important but addressable. No fundamental flaw invalidates the core claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>