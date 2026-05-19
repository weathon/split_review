- Decision: Reject
- Avg Score: 6.25
- Scores: 5, 6, 8, 6
Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

The paper proposes VITask, a framework for adapting pre-trained Vision-Language Models (VLMs) to task-specific domains by leveraging small Task-Specific Models (TSMs) during fine-tuning. It introduces three strategies: (1) Exemplar Prompting (EP), which augments VLM features with TSM features during training; (2) Response Distribution Alignment (RDA), which distills the EP-augmented VLM's response distribution back to the unaugmented VLM so the TSM can be discarded at inference; and (3) Contrastive Response Tuning (CRT), which sharpens the VLM's ability to rank correct over incorrect image-response pairs. Experiments on 12 MedMNIST medical diagnosis datasets show VITask achieves competitive or superior performance to both vanilla instruction-tuned VLMs and the standalone TSM baseline.

## Strengths

- **Exemplar Prompting effectively bridges TSMs and VLMs.** Table 1 shows VITask with EP achieves the highest average accuracy (0.847) across 12 datasets, outperforming the TSM (0.816), LLaVA-13B (0.759), and InternVL-2B (0.742), while matching the TSM on macro F1 (0.771 vs. 0.772). This is concrete evidence that TSM features can guide VLMs without disrupting pre-trained vision-language alignment.

- **RDA enables competitive performance without a TSM at inference time, validated by careful ablation.** Table 2 (w/o EP rows) shows that when the TSM is discarded at inference, adding RDA improves F1 by 8.16% on average over the vanilla VLM, and RDA+CRT together improve by ~11.2%. This directly supports the paper's practical claim that the TSM is only needed during training.

- **CRT demonstrably sharpens the visual response ranking capability.** Figure 3 provides a clear diagnostic: the pre-trained VLM shows near-identical probability densities for correct and incorrect image-response pairs; vanilla instruction tuning leaves substantial overlap; CRT produces a clean separation. This visual evidence is compelling and directly motivates the design.

- **Diagnostic analysis (Section 3) clearly identifies why instruction-tuned VLMs underperform TSMs.** The head-to-head comparison on HAM10000 (TSM F1=0.790 vs. InternVL-2B F1=0.531) and the controlled experiments with trainable vision encoders cleanly isolate the two root causes (unspecialized image representations and indirect tuning objective), providing strong motivation for the proposed framework.

- **Thorough ablation (Table 2) transparently quantifies each component's contribution.** The table separately reports w/ EP and w/o EP conditions, making it clear where each component matters. The paper also honestly notes that RDA provides marginal gains when EP is already available at inference (Section 5.4), which the authors correctly attribute to RDA's intended use case (no-EP inference).

- **Plug-and-play adaptability is demonstrated on external datasets.** On APTOS, IDRiD, and MESSIDOR, VITask$^\text{plug}$ (swapping the TSM for a new one without retraining the VLM) achieves the best accuracy and F1 among all VLM-based methods, showing the framework's practical flexibility for new tasks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Hyperparameters α and β are introduced but their values are not reported.** The paper defines α and β as weighting terms for the RDA and CRT losses (line 244) but never specifies their values or how they were chosen. This is a reproducibility gap that should be addressed (shared across datasets or tuned per dataset?).

- **No error bars or repeated runs are reported.** The CRT component involves random negative sampling (line 222), which introduces stochasticity. Without confidence intervals or repeated trials, it is difficult to assess whether the reported margins (e.g., +1–2% F1 w/ EP or +8–11% w/o EP) are statistically significant. This is standard to request even if single-run evaluation is common practice in this field.

- **Robustness to incomplete instructions is evaluated on only one dataset (DermaMNIST) with one modification.** The paper reports a sharp drop for the vanilla VLM (0.531→0.423 F1) but only says VITask showed "a slight decrease" without giving exact numbers in the text (they appear only in a figure). Testing more datasets and instruction-degradation levels would strengthen the claim of general robustness.

- **The external validation results are nuanced and the "no-TSM inference" framing could be more precise.** On APTOS, VITask w/o EP achieves lower accuracy (0.456) than vanilla VLM (0.523) but higher F1 (0.336 vs. 0.291). The paper attributes the accuracy gap to class imbalance, which is reasonable, but the best external result (VITask$^\text{plug}$) requires training a new TSM per domain. The paper frames this as flexibility (which is fair), but the claim that the VLM "can perform inference without needing the TSM" (line 253) should more explicitly acknowledge that generalization to truly new tasks still benefits from a per-task TSM.

- **ChestMNIST TSM F1 of 0.095 is suspiciously low and goes unremarked.** For a binary classification task, an F1 of 0.095 is near-meaningless, suggesting either extreme class imbalance, a training issue, or a metric calculation quirk. The paper does not discuss this, even though it sets the TSM baseline on that dataset. This does not invalidate VITask's improvements (VITask achieves F1=0.129 on the same dataset), but the unexplained baseline warrants comment.

### Trivial

- **The connection between the margin distribution loss (Eq. 10–11) and existing contrastive/InfoNCE objectives could be noted** to help readers situate the contribution.

## Nice-to-Haves

- A comparison (even small-scale) against VLM+TSM integration methods such as LLaVA-Plus or LISA would further contextualize the contribution, though the paper's setting (fine-tuning a pre-trained VLM vs. building a new VLM with tool-using capabilities) differs substantially from those works.
- A sensitivity analysis for α and β would improve reproducibility and practical usefulness.
- Reporting exact VITask F1 numbers in the robustness experiment text (not just in the figure) would be helpful.

## Removed Points

**"The TSM baseline is too weak for the claims"** — This criticism is factually incorrect. The TSM (ViT-Base on ImageNet-21k) achieves best or second-best F1 on 11 of 12 MedMNIST datasets and best or second-best accuracy on 10 of 12 (e.g., 0.965 F1 on PneumoniaMNIST, 0.990 on BloodMNIST, 0.950 on OrganAMNIST). It is a strong baseline, not a deliberately weak one. The paper also demonstrably outperforms it on average accuracy (0.847 vs. 0.816), making the comparison valid.

**"RDA and CRT contribute little when EP is used"** — The paper already transparently addresses this: Section 5.4 states "When EP is used during inference, RDA does not yield notable gains. This is expected, as RDA is primarily designed to enhance performance in the absence of exemplars during inference." The ablation study (Table 2) reports both conditions separately, and the main use case for RDA/CRT is the w/o EP scenario where they provide substantial gains (+8–11% F1). This is not a weakness, it is a properly documented design choice.

**"Missing comparisons to other VLM+TSM integration methods (LLaVA-Plus, LISA, MedAgent)"** — These works build *new* VLMs that incorporate TSMs as tools/components, which is architecturally different from VITask's goal of fine-tuning a *pre-trained* VLM. The paper scopes this out in Section 2 (line 70–72). Comparing against them would test a different research question and require significant re-implementation. This is scope creep.

**"The margin distribution loss is essentially InfoNCE"** (from Section-by-Section notes) — The observation that the loss has a contrastive structure is correct but it's a connection the paper could optionally note; it is not a weakness of the method itself.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective that the paper itself does not already provide or address.

## Suggestions

- Report the values of α and β used in experiments, and include a brief sensitivity analysis.
- Add error bars (or at minimum, report results over multiple seeds) for the main experiments, especially for the ablation involving random negative sampling.
- In the robustness experiment, state VITask's exact F1 numbers alongside the vanilla VLM's drop (0.531→0.423) in the text, and consider testing on a second dataset.
- Acknowledge the anomalous ChestMNIST TSM F1 of 0.095 and briefly explain the dataset's class distribution or training dynamics.
- In the discussion of external validation, clarify more explicitly that the "no-TSM inference" advantage applies when the target task distribution matches the fine-tuning distribution, while VITask$^\text{plug}$ addresses out-of-distribution generalization.
