Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper introduces the first method specifically for label unlearning in Vertical Federated Learning (VFL). The active party uses a small set of labeled samples, applies manifold mixup to augment the passive parties' forward embeddings, then runs gradient ascent on the mixed embeddings to erase the target label from both active and passive models. The paper also demonstrates that existing unlearning methods leak label information to passive parties via gradient clustering (up to 97.80% clustering accuracy). Across four datasets, two architectures, and single/two/multi-class scenarios, the method achieves near-zero accuracy on unlearned data while retaining higher utility on remaining data than six baselines, and does so with the fastest runtime (seconds).

## Strengths

- **First systematic treatment of label unlearning in VFL**: The paper correctly identifies a genuine gap — existing VFU works address passive-party removal, not label-specific unlearning. The problem is well-motivated and the threat model (semi-honest, non-colluding parties) is clearly stated.

- **Simple, efficient, and empirically effective method**: Manifold mixup + gradient ascent is lightweight (completes in seconds) and consistently outperforms six baselines on $\mathcal{D}_r$ preservation while driving $\mathcal{D}_u$ accuracy to near 0%. The ablation in Fig. 4 directly demonstrates that mixup is critical: plain gradient ascent on 40 samples gives 40.48% $\mathcal{D}_u$ accuracy, whereas the proposed method achieves 0% with the same 40 samples.

- **Generalizability across settings**: The method works with 1, 2, or 4 passive parties (Table 4) and under differential privacy or gradient compression (Figs. 5, 6), settings where baselines degrade. This robustness is valuable for practical VFL deployments.

- **Novel label leakage demonstration**: The clustering attack on gradients transmitted during existing unlearning (Section 3.2, Fig. 1) is a clear empirical demonstration of a real privacy risk, and is a useful contribution in its own right.

## Weaknesses

### Fatal

None. The paper's core claims (first VFL label unlearning method, effective few-shot unlearning) are supported by evidence. The unsubstantiated label-leakage claim is a major weakness but does not invalidate the primary contribution.

### Major

- **The paper claims to mitigate label leakage but never verifies this for its own method.** Section 3.2 shows that a passive party can cluster gradients from existing unlearning methods to infer labels (clustering accuracy up to 97.80%). The proposed method also transmits gradients $\nabla_{H_k'}\ell$ to passive parties during unlearning (Algorithm 1, line 250; Eq. 4b). The paper claims this "mitigates the risk of label privacy leakage" (abstract, contribution 3) because mixup obscures the signal. However, **no experiment runs the same clustering attack (Eq. 3) on the proposed method's own gradients** to verify that mixup actually defeats the attack. The threat model (semi-honest passive party faithfully executing the protocol) is exactly the setting where this should be tested. Without this experiment, the paper's privacy claim is unsubstantiated. This is the single most important missing piece — the method may still be a contribution for its unlearning properties alone, but the paper should either add this experiment or temper its privacy claims.

- **Baseline implementation in the VFL setting is underspecified.** The paper says "we stimulate a VFL scenario by splitting a neural network into two bottom models and a top model" (Section 5.1), but does not explain how centralized baselines (Fisher Forgetting, Boundary Unlearning, UNSIR) are adapted to VFL constraints. For example, Fisher Forgetting requires the Fisher Information Matrix (requires joint label+feature access); Boundary Unlearning generates adversarial examples from $\mathcal{D}_u$ (requires labels that passive parties do not have). Without knowing what information the baselines are given, it is impossible to assess whether the comparisons are fair. This undermines the baseline comparisons.

### Minor

- **MIA evaluation lacks calibration.** The paper reports Attack Success Rates (ASR) in figures and claims "consistent ASR performance" for the proposed method, but does not state what ASR value corresponds to perfect unlearning (for a balanced MIA, 50% = random guessing). It also does not explicitly tabulate Retrain's ASR alongside the proposed method's ASR in the main tables, making it hard to gauge how close the method is to the gold standard. (The MIA figures likely include Retrain — since it is listed as a baseline — but the paper should state this clearly and report quantitative ASR values.)

- **Non-zero $\mathcal{D}_u$ accuracy in several settings is not adequately discussed.** The method achieves 2.00% on ModelNet single-class, 4.83% (ResNet18) and 6.00% (Vgg16) on CIFAR100 multi-class. For CIFAR100 (100 classes, random ≈ 1%), 4.83–6.00% indicates residual information. The paper says "Our solution demonstrates strong effectiveness across all models, datasets, and scenarios" without acknowledging these failures or analyzing why they occur.

- **Several hyperparameters are unspecified.** The paper does not state: (a) the exact few-shot sample count $n_p$ used in each experiment (only the ablation shows 40 vs. 5000 for CIFAR10 ResNet18); (b) how $\lambda$ is sampled (standard mixup uses $\lambda \sim \text{Beta}(\alpha,\alpha)$, but neither distribution nor $\alpha$ is given — the paper merely says "λ ranges from 0 to 1"); (c) the unlearning epoch count $N$ and learning rate $\eta$ used in the proposed method. While these are addressable, their absence makes reproduction harder.

- **The gap to Retrain on $\mathcal{D}_r$ is sometimes large (e.g., ModelNet: 83.32% vs. 93.90%).** The paper does not discuss whether such degradation is acceptable in practice.

- **Interpretation of mixup's role is missing.** The ablation shows that 40 samples without mixup fail but 40 samples with mixup succeed. The paper offers no intuition for why mixing embeddings has this dramatic effect — is it due to increased effective sample size, regularization of gradient ascent, or something else? A brief analysis (e.g., gradient norms, embedding diversity) would strengthen the paper.

### Trivial

- Algorithm 1 inputs $\mathcal{D}_u$ (line 234) but the text describes using $\mathcal{D}_p$ (few-shot private data) — this naming inconsistency could confuse readers.
- The paper says "we stimulate a VFL scenario" — likely should be "simulate."

## Nice-to-Haves

- Systematic sweep of the few-shot sample count $n_p$ (10, 20, 40, 80, 160) across datasets to establish the minimum viable number.
- Sensitivity analysis of the mixup coefficient $\lambda$ (vary $\alpha$ in Beta distribution).
- t-SNE visualization of the passive party's embedding space before/after unlearning to show the unlearned class no longer separates.
- Comparison against a centralized few-shot unlearning method (Yoon et al. 2023) adapted to VFL, as a directly relevant baseline the paper omits.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about "redundant citations and commented-out paragraphs"**: These are PDF-parser artifacts (the commented sections are from the paper's draft history and do not appear in the original rendered submission). Removed per formatting-artifact rule.
- **Criticism that time efficiency comparison is unfair because the method uses 40 samples vs. full datasets**: The paper already provides the relevant comparison in Figure 4 (GA with 40 samples vs. GA with 5000 samples vs. proposed), which directly addresses this concern. The time figure (Fig. 3) is presented alongside this ablation, so the reader can contextualize it. The critic's claim that "the dramatic speed advantage is partly artificial" overlooks that using few-shot data is an intentional design feature, not a bug.
- **Criticism that MIA does not include Retrain**: The paper lists Retrain as a baseline and the MIA figures compare "different unlearning methods" (which would include Retrain). The figures are images, but the text describes comparing methods, implying Retrain is included. The actual weakness (lack of explicit ASR tabulation alongside calibration) is retained in Minor.
- **Criticism about "does not verify whether the same clustering attack would work on the gradients transmitted in the proposed method" appearing twice**: This is the same point as the first Major weakness; the duplicate is removed.

## Novel Insights

None beyond the paper's own contributions. The paper's own demonstration that gradients from existing unlearning methods in VFL can be clustered to recover labels (Fig. 1) is the most novel insight — it clearly shows why naive application of centralized unlearning to VFL is dangerous. The finding that manifold mixup with as few as 40 samples can substitute for the full unlearning dataset is empirically striking, though the mechanism is not explained.

## Suggestions

1. **Run the clustering attack (Eq. 3) on the proposed method's own gradients.** Report clustering accuracy alongside the existing results in Fig. 1. If mixup resists clustering, this directly validates the privacy claim. If it does not, either add a defense or reframe the paper's claims.
2. **Specify baseline adaptations** — for each baseline, state clearly: (a) what information does the active party provide to passive parties? (b) do baselines have access to features they would not have in a real VFL deployment?
3. **Report a "retrain baseline" MIA ASR in the main tables** (not just figures) so readers can directly compare the proposed method's ASR to the gold standard. Discuss what ASR values are expected for perfect unlearning.
4. **Disclose all hyperparameters**: $n_p$ per experiment, $\lambda$ distribution (and $\alpha$), unlearning epochs $N$, learning rate $\eta$.
5. **Discuss the cases where $\mathcal{D}_u$ accuracy is non-zero** (ModelNet 2.00%, CIFAR100 multi-class 4.83–6.00%) and explain whether this indicates practical concern.
6. **Add an intuition section** explaining why mixup amplifies effectiveness from 40 samples — e.g., analyze gradient norms or embedding diversity of mixed vs. unmixed gradients.

## Score and Decision

The paper addresses a timely and genuinely underexplored problem (label unlearning in VFL) with a clean, simple method that is empirically effective across diverse settings. The core contribution — a few-shot unlearning technique that works in VFL — is demonstrated with solid evidence. However, the paper overclaims on privacy without verifying it, underspecifies baseline implementations, and leaves several experimental gaps. These issues are addressable with additional experiments and clearer writing, but in the current form the privacy claim is unsubstantiated and the experimental comparisons are not fully reproducible.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>