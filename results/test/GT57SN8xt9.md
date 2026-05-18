Now I have all the information needed. Let me compile the final consolidated review.

## Summary

This paper introduces PEL (Parameter-Efficient Long-Tailed Recognition), a framework for fine-tuning CLIP on long-tailed datasets. The key ideas are: (1) using parameter-efficient fine-tuning (PEFT) instead of full fine-tuning or classifier fine-tuning to prevent overfitting on tail classes, (2) a semantic-aware classifier initialization using CLIP text features to accelerate convergence, and (3) test-time ensembling (TTE) for improved generalization. PEL achieves state-of-the-art results on ImageNet-LT, Places-LT, and iNaturalist 2018 while requiring only 10–20 training epochs (versus 80–160 for prior methods) and no external data.

## Strengths

- **Identifies and diagnoses a real overfitting problem in fine-tuning for long-tailed recognition**: Section 3.2 and Figures 2d–2e empirically show that both full fine-tuning and classifier fine-tuning degrade tail-class accuracy relative to zero-shot CLIP, even when using a balanced loss. This diagnosis is well-motivated and provides a clear rationale for adopting PEFT in the long-tailed setting.

- **Proposes a general, unified PEFT framework that achieves state-of-the-art results with minimal computational cost**: Tables 1–3 show that PEL consistently outperforms prior methods (VL-LTR, RAC, BALLAD, LPT) on ImageNet-LT, Places-LT, and iNaturalist 2018 while tuning only 0.18M–0.62M parameters and training for ≤20 epochs. This combination of efficiency and performance is a genuine advance.

- **Semantic-aware classifier initialization is simple, novel, and effective**: Section 3.3 and Table 5 demonstrate that initializing the classifier weights with CLIP textual features from a single forward pass significantly outperforms random initialization and class-mean initialization, while adding negligible overhead. Figure 5 shows this enables rapid convergence (within 10–20 epochs), particularly for few-shot classes.

- **Demonstrates robustness across diverse PEFT methods and comprehensive ablation studies**: Table 4 evaluates seven different PEFT variants under a unified framework, showing all outperform full fine-tuning and classifier fine-tuning. Additional ablations (Figure 6 on parameter quantity, Table 5 on initialization, Figure 4 on feature separability) systematically validate the design choices.

- **Practicality**: The method is one-stage, end-to-end, requires no external data, and runs on a single GPU with 20 GB memory, making it substantially more practical than two-stage approaches like LPT (100+ epochs) or data-hungry methods like VL-LTR.

## Weaknesses

### Fatal
None.

### Major

- **CLIP variant is never specified.** The paper repeatedly refers to "CLIP" without stating which variant is used (e.g., ViT-B/32, ViT-B/16, ViT-L/14). Zero-shot performance varies substantially across variants. Without this specification, the entire set of reported results is not reproducible, and the zero-shot CLIP numbers in Figures 2a–2c are unanchored. This is a basic reproducibility requirement that must be addressed.

- **Test-time ensembling (TTE) details are underspecified.** The paper defines TTE as averaging predictions from \(M\) perturbed versions \(\alpha_i(x)\) but never specifies \(M\) or the augmentation strategy. The only clue is a brief mention of "mitigat[ing] bias introduced by image cropping" (line 107). Without these details, the TTE component cannot be reproduced, and the computational overhead claim ("minimal computational overhead") is unverifiable. Since TTE contributes measurable gains (e.g., +1.4% on Places-LT), its specification is essential.

- **No measure of result stability.** All results are reported as single numbers without standard deviations, error bars, or multiple seeds. This is especially concerning where margins are modest (e.g., PEL at 79.5% vs. VL-LTR at 78.8% on ImageNet-LT). While single-run benchmarks are common in this literature, the lack of any variance estimate undermines confidence in the reported improvements and the significance of the state-of-the-art claims.

### Minor

- **The overfitting claim is asserted but not rigorously demonstrated.** The paper attributes the tail-class accuracy drop after fine-tuning (Figures 2d–2e) to overfitting, but the evidence is circumstantial — it shows lower tail accuracy rather than directly demonstrating training/validation divergence. Providing training vs. validation accuracy curves for the baselines (full fine-tuning, classifier fine-tuning) would substantiate the diagnosis. This weakens the paper's central motivation, though the claim remains plausible.

- **Comparison with LPT is confounded by different pre-training data on two out of three datasets.** The paper correctly acknowledges on ImageNet-LT (line 128) that LPT uses a ViT pre-trained on ImageNet-21K rather than CLIP. However, on Places-LT and iNaturalist 2018, the paper directly compares with LPT without noting this confound. Since PEL uses CLIP (trained on 400M image-text pairs), the performance gap could partly reflect stronger pre-training data. The core claims do not depend solely on LPT comparisons — PEL also outperforms CLIP-based methods (VL-LTR, RAC, BALLAD) — but the LPT comparisons should be transparently contextualized across all datasets.

- **Zero-shot CLIP baseline is omitted from the main comparison tables.** Figures 2a–2c show zero-shot CLIP's performance, and the text notes it "outperforms most well-designed methods" on ImageNet-LT and Places-LT. Yet Tables 1 and 2 do not list zero-shot CLIP accuracy, making it harder for readers to gauge how much improvement PEL provides over this simple baseline. Including it would add useful context.

### Trivial

- The paper states that semantic-aware initialization uses "no additional computational overhead" (line 99). While the overhead is very small (one forward pass of the text encoder), it is not literally zero. The phrasing should be tempered.
- The initialization of the PEFT modules themselves (e.g., prompt initialization in VPT, weight initialization in LoRA/Adapter) is not discussed, which is a minor reproducibility gap.
- Figures 2a–2c are informative but do not list exact accuracy values, making it difficult to compare them quantitatively with the tables.

## Nice-to-Haves

- Report TTE accuracy as a function of \(M\) (e.g., 1, 2, 5, 10, 20) to help readers understand the compute–accuracy trade-off.
- Re-implement LPT using the same CLIP backbone to enable a clean comparison, or clearly state the confound on all datasets where LPT is used.
- Include a brief discussion of failure cases or limitations (e.g., sensitivity to hyperparameters, performance on extremely fine-grained tail classes).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"CIFAR-100-LT results are mentioned only in the conclusion and not shown in the main text"**: The CIFAR-100-LT results exist in the supplementary/appendix, which the parser strips from all papers. This is a known artifact of the review format, not an author omission.
- **"Table 4 excludes full fine-tuning and classifier fine-tuning"**: The text description (line 160) explicitly states these methods are included: "In addition to commonly used full fine-tuning and classifier fine-tuning, we test PEL with other 7 types of PEFT methods in Table 4." The reviewer appears to have misread the caption.
- **"Figures 2a-2c are hard to read in grayscale"**: This is a formatting/style nitpick with no bearing on the technical contribution.
- Various phrasing issues about "not yet released" or "cannot be independently verified": The paper cites standard models and benchmarks. Per policy, all cited entities are assumed to exist.

## Novel Insights

The most interesting observation that emerges from the reviews is that the paper's strength — a clean, simple framework combining PEFT, semantic initialization, and TTE — is also the source of its main weaknesses: each component is underspecified (CLIP variant, TTE parameters, module initialization) in ways that individually seem minor but collectively hinder reproduction. The overfitting diagnosis, while plausible and well-motivated, would benefit from more direct evidence, yet the fact that PEFT consistently outperforms full/classifier fine-tuning across seven PEFT variants (Table 4) provides indirect but strong empirical support that the core intuition is correct.

## Suggestions

1. **Specify the CLIP variant** (e.g., ViT-B/16) explicitly in the experimental setup. This is the single most impactful fix for reproducibility.
2. **Document TTE details**: state \(M\) and describe the augmentation \(\alpha_i(\cdot)\) precisely (e.g., "10 random crops of size 224×224 resized from the image").
3. **Report results with variance**: run 3 random seeds and report mean ± std for all main results, especially on ImageNet-LT where margins are small.
4. **Add validation curves** for full fine-tuning and classifier fine-tuning to support the overfitting diagnosis, or soften the claim to "performance degradation" rather than "overfitting" if direct evidence is unavailable.
5. **Explicitly note the backbone confound** when comparing with LPT on Places-LT and iNaturalist 2018, or move LPT comparisons to a separate discussion.

## Score and Decision

The paper makes a genuine contribution: it identifies an overlooked problem (overfitting from conventional fine-tuning on tail classes), proposes a clean and practical solution, and demonstrates consistent improvements across multiple benchmarks with dramatically lower training cost. The weaknesses are real but fixable — no fatal flaw invalidates the core claims. The missing CLIP variant and TTE details are the most consequential issues for reproducibility and should be addressed before publication.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>