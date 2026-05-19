## Summary
The paper studies cross-prompt transferability of adversarial examples in Vision Language Models (VLMs). It observes that multi-prompt optimization for generating adversarial images suffers from non-stationarity (fluctuating attack success rates), which it attributes to overfitting. To address this, it proposes GrCPA (Gradient Regularized-based Cross-Prompt Attack), which clips the *k* largest and smallest gradient values in the Attention and MLP components of the LLM's last *λN* Transformer blocks during backpropagation. Results on Flamingo show GrCPA outperforms Single-P, Multi-P, and CroPA baselines across four task types, with improvements in both attack success rate and output stability.

## Strengths
- **Consistent improvement over strong baselines on Flamingo (Table 1):** GrCPA outperforms Single-P, Multi-P, and CroPA across all four task types (e.g., VQA_specific ASR of 1.00 vs. 0.87 for CroPA) and across multiple target answers. The gains are consistent rather than cherry-picked.

- **Demonstrated stability improvement (Table 2):** The paper quantitatively shows that GrCPA reduces output fluctuation across iterations (consistency 0.87–1.00 vs. as low as 0.61 for Multi-P/CroPA). This directly addresses the non-stationarity problem the paper identifies, and the 5-time-point consistency metric, though coarse, provides a reproducible measure.

- **Ablation justifies dual-modality regularization (Table 5):** Regularizing only visual or only text gradients reduces ASR compared to joint regularization (0.36/0.38 vs. 0.41), supporting the paper's claim that attacking VLMs benefits from considering both modalities.

- **Prompt-number scaling analysis on a second model (Table 3, BLIP-2):** GrCPA consistently outperforms the Multi-P baseline across 1, 5, 10, 50, and 100 prompts on BLIP-2, demonstrating the method is not Flamingo-specific. The observation of diminishing returns beyond 10 prompts is practically useful.

- **Convergence analysis (Figure 3):** GrCPA achieves higher ASR at every iteration checkpoint (200–1000) compared to Multi-P and CroPA, showing better computational efficiency.

## Weaknesses
### Fatal
None.

### Major

- **Experimental breadth does not match claimed scope:** The abstract and introduction state "Extensive experiments on models such as Flamingo, BLIP-2, LLaVA and InstructBLIP." In practice, the full comparison (GrCPA vs. Single-P, Multi-P, CroPA) is conducted **only on Flamingo** (Table 1). BLIP-2 gets a prompt-count comparison (Table 3) but does **not** include CroPA or other baselines. LLaVA-1.5 is dismissed in a single sentence ("find weak transferability") with **zero quantitative results**. InstructBLIP is listed in Section 4.1 but has **no results at all**. This gap undermines the paper's claim that GrCPA is a broadly validated method. The core claim — that GrCPA is "effective" — is supported on one model; generalization to other architectures is asserted but not demonstrated with comparable evidence.

- **No ablation of the key parameter *k*:** The number of clipped extrema is set to *k*=1 in all experiments and is never varied. Since this is the central hyperparameter of the method (it determines how many gradient components are zeroed), the lack of any sensitivity analysis (e.g., *k* = 1, 5, 10, 50) is a significant omission. Without it, the reader cannot assess whether the method is robust to this choice or whether *k*=1 was selected because it happens to work best on Flamingo.

### Minor

- **Overclaimed novelty of the "non-stationarity" observation.** The paper states "To the best of our knowledge, we first identify the non-stationary phenomenon in adversarial attacks against vision language models." Oscillation during iterative adversarial optimization is a well-documented phenomenon (PGD, adversarial training literature). The paper provides a qualitative illustration (Figure 1) but no quantitative characterization (e.g., oscillation amplitude, frequency, comparison with known oscillation in single-model settings). The claim would be better framed as a demonstration that this known issue is particularly salient in the VLM multi-prompt setting, rather than a "first identification."

- **Missing statistical rigor.** No error bars, confidence intervals, or multiple independent runs are reported. Given the known variance in iterative attack optimization (especially with different random seeds and initialization), this limits confidence in the precise numbers reported.

- **CroPA comparison lacks detail on hyperparameter choices.** The paper sets the CroPA text perturbation update frequency *T* = 1 (i.e., text perturbation updated every iteration), which is an extreme setting. No justification or sensitivity analysis for this choice is provided. Since CroPA's performance is sensitive to *T*, the comparison would be more informative with an ablation or a statement that the original authors' recommended setting was used.

- **Prompt set not fully specified.** The paper uses "up to 100 prompts" for each sample but does not list the exact prompts or describe how they were generated beyond stating they cover classification, captioning, and VQA. This affects reproducibility.

- **No analysis of perturbation perceptibility.** With a perturbation bound of ε=16/255 (the upper end of what is typically considered "imperceptible"), showing example adversarial images or quantifying perceptual distance (e.g., LPIPS, SSIM) would strengthen the practical relevance of the results.

### Trivial

- Several citation markers appear as bare numbers (e.g., ".7" after "security vulnerabilities") and some sentences seem truncated (e.g., "but find weak transferability.."), suggesting minor copy-editing issues.
- The text describing Figure 3 notes the figure is included but the parsed version is image-only; the discussion in Section 4.4 is clear enough on its own.

## Suggestions
1. **Conduct the full experimental suite on at least BLIP-2** (comparison against Single-P, Multi-P, and CroPA across task types, matching Table 1's protocol). For LLaVA and InstructBLIP, even a single-task comparison with numbers would substantially strengthen the generality claim.
2. **Ablate *k*** over at least a range of *k* = 1, 5, 10, 50 (or as a fraction of embedding dimension *d*). This is critical since it is the method's only free hyperparameter.
3. **Report error bars** or results over multiple random seeds/inits for the main experiments.
4. **Tone down the "first identification" claim** regarding non-stationarity to avoid overclaiming, and provide a quantitative characterization (e.g., oscillation amplitude, variance across iterations).
5. **Provide the exact prompt templates** used, either in the paper or in a publicly hosted appendix, to improve reproducibility.
6. **Show example adversarial images** or report a perceptual similarity metric to verify imperceptibility at ε=16/255.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
