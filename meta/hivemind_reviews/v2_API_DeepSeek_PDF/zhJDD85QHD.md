## Summary
# Final Review Report

## Summary

This paper proposes CEIR (Concept-based Explainable Image Representation), an unsupervised representation learning method that combines a Concept Bottleneck Model (CBM) with a Variational Autoencoder (VAE) to produce both semantically meaningful and interpretable image representations. The pipeline has two phases: (1) using CLIP and GPT-4-generated concept candidates, a linear projection layer maps image backbone outputs to a concept vector space where each dimension corresponds to a human-comprehensible concept; (2) a VAE compresses these high-dimensional concept vectors into a compact latent representation. CEIR is evaluated on clustering (CIFAR10, CIFAR100, STL10, ImageNet) and linear probing, and demonstrates qualitative concept attribution on benchmark and open-world images.

**Core strengths:** The paper tackles a relevant problem—interpretability of unsupervised representations—and proposes a clean pipeline that integrates CBMs into representation learning without labels. Clustering results are strong, especially with large ViT backbones (e.g., CIFAR10 ACC 95.70%, STL10 ACC 99.19% with ViT-L/14). The concept attribution visualizations are intuitive and demonstrate the potential of concept-based representation analysis.

**Critical weaknesses:** (1) The VAE loss and KL notation are underspecified, affecting reproducibility. (2) The training protocol merges test data into VAE training and uses the test set for early stopping, creating a significant information leakage concern (ablation shows a 4-6 point drop when test set is removed). (3) The Discussion introduces unsupported claims about domain generalization and causal concept discrimination. (4) The concept attribution evaluation is purely qualitative with no quantitative validation. (5) The performance drop from raw CLIP features to CEIR representations in linear probing is non-trivial and not adequately analyzed. Novelty assessment is deferred (external literature unavailable in this run).

**Overall assessment:** The paper presents an interesting direction with promising empirical results, but the evaluation protocol concerns and missing methodological details reduce confidence in the reported gains. Major revision is required before acceptance.

## Strengths
1. **Relevant and timely problem.** Interpretability of unsupervised representations is an important open problem. The paper's goal of producing representations that are both high-performing and human-interpretable addresses a genuine need in representation learning.

2. **Clean pipeline design.** CEIR's two-phase design (concept bottleneck + VAE compression) is conceptually simple and modular. Using CLIP's shared embedding space as weak supervision to align concept vectors is a practical and well-motivated choice.

3. **Strong clustering performance.** With ViT-L/14 backbone, CEIR achieves state-of-the-art or near-SOTA clustering results on CIFAR10 (ACC 95.70%, NMI 90.08%), STL10 (ACC 99.19%, NMI 97.87%), and competitive performance on CIFAR100-20 and CIFAR100. These results demonstrate that concept-compressed representations retain strong semantic structure.

4. **Interpretable concept attribution.** The alluvial map visualizations (Figure 3) provide intuitive, human-readable explanations of what semantic information each representation encodes. The ability to highlight shared vs. distinctive concepts across similar categories (e.g., "vehicle" shared by golf cart and sports car; "orange and black patterns" specific to leopard) is a genuine qualitative strength.

5. **Open-world demonstration.** The concept mining demo on 24 unsourced Kamakura images (Section 4.4) illustrates the potential for zero-shot concept extraction, which is a useful capability for automated label generation and data exploration.

6. **Ablation coverage.** The ablation experiments in Appendix A.2.3 systematically examine the contribution of each component (class-related concepts, test set in VAE training, VAE itself) and the impact of latent size, providing useful insights into the method's behavior.

7. **Computational efficiency.** The method trains quickly on small benchmarks (<30 minutes on CIFAR/STL10) with a lightweight VAE (two-layer MLP), making it accessible for practitioners.

## Weaknesses
1. **Potential information leakage from merging test data (Major).** The VAE training merges training and testing sets, and the concept projection layer uses the testing set for early stopping. The ablation (Table 7) shows a 4-6.4 point drop in NMI/ACC/ARI when the test set is removed from VAE training. This means the main reported results are achieved with a non-standard, test-informed protocol, making them difficult to compare fairly with baselines that do not use test data.

2. **VAE loss formulation is underspecified (Major).** Equation (2) writes `KL(f(q_i))` without specifying the encoder output distribution. Standard VAE uses a stochastic encoder outputting `(μ, log σ²)`, but the notation `KL(f(q_i))` treats the encoder output as a single vector, which is ambiguous. The reconstruction loss uses L2 without discussing output activation or normalization of concept vectors.

3. **Loss function Eq. (1) contains unexplained notation (Major).** Cubed terms `\overline{l}_k^3` and `P_{:,k}^3` appear in the cosine similarity loss without any justification. This is likely a PDF extraction error or an underspecified design choice. If intentional, the rationale for cubing must be provided.

4. **Unsupported claims in Discussion (Major).** The Discussion asserts domain-shift resilience and causal/spurious concept discrimination without any supporting experiments. These claims should be removed or explicitly labeled as speculation.

5. **Concept attribution evaluation is purely qualitative (Major).** Figure 3 provides compelling visual examples, but no quantitative metric (concept-probing accuracy, human evaluation, or comparison to baselines) is used to validate concept quality. The paper cannot substantiate claims about "fine-grained semantic concepts."

6. **Linear probing shows notable performance drop (Moderate).** CEIR representations underperform raw CLIP features by 0.9-5.3 points in linear probing (Table 3). The ResNet50 backbone shows a 5.3-point ACC drop, which contradicts the abstract's claim of preserved robustness.

7. **Contribution 3 is overstated (Moderate).** The third contribution claim ("CEIR allows interpretation incorporated with label-free attribution methods...valid concept-driven interpretation") is not quantitatively validated. The paper only provides qualitative attribution examples; there is no evaluation of attribution quality, reliability, or comparison to other methods.

8. **Introduction narrative is unfocused (Moderate).** The introduction covers motivation, linear probing critique, attribution methods, and concept-based methods in rapid succession without a clear narrative arc. Key terms ("reliability," "comprehensibility") are used without definition. The gap statement is generic.

9. **Related Work does not clearly differentiate from LF-CBM (Minor).** The paper uses the same concept generation pipeline as LF-CBM (Oikarinen et al., 2023) but does not explain the key difference (LF-CBM trains a supervised classifier on concept vectors; CEIR replaces it with an unsupervised VAE) until the Method section.

10. **Novelty assessment is incomplete (Deferred).** Due to external literature unavailability in this run, novelty claims (C1-C3) cannot be verified against the existing literature. Manual literature verification is required. The paper's main novelty—applying CBM to representation learning via VAE concept compression—appears plausible but needs external validation.

11. **No statistical significance or variance reporting (Minor).** All results in Tables 2 and 3 are reported as single runs without standard deviations or confidence intervals. Given that some improvements are marginal (e.g., CIFAR100-20 ACC: CEIR 62.53% vs. TEMI 63.20%), variance information is needed to assess reliability.

## Key Issues
### Issue 1: Test-data-informed evaluation protocol undermines fairness (Severity: Critical)
The VAE is trained on merged training+testing sets, and the concept projection layer uses the testing set for early stopping. The ablation shows a 4-6.4 point gap when test set is removed from VAE training. This means the headline numbers in Table 2 are achieved with a protocol that gives CEIR an information advantage over all baselines that do not merge test data. The † and ∗ markers in Table 2 partially disclose this, but the impact is not prominently discussed in the main text.

**Required action (Must):** Report clustering results *without* test set merging as the primary result, and present the current results (with test set) as a variant. Add a clear disclosure paragraph in Section 4.1.

### Issue 2: VAE implementation ambiguity (Severity: Major)
Equation (2) is not a valid VAE loss as written. The KL term `KL(f(q_i))` is underspecified—KL divergence requires two distributions. The paper must clarify whether a stochastic encoder is used, how reparameterization is performed, and what the exact loss function is.

**Required action (Must):** Rewrite Eq. (2) with explicit encoder output distributions, reparameterization, and β weighting. Report whether β is tuned.

### Issue 3: Loss function Eq. (1) has unexplained exponent (Severity: Major)
The cubic exponent `^3` in Eq. (1) is not explained and likely erroneous. This affects the correctness of the training objective for the concept bottleneck layer.

**Required action (Must):** Clarify whether the exponent is intentional or a typesetting error. If intentional, provide justification and gradient analysis.

### Issue 4: Discussion contains unsupported strong claims (Severity: Major)
Domain generalization, causal concept discovery, and robustness claims are presented without experimental support. These claims misrepresent the paper's actual contributions.

**Required action (Must):** Remove or explicitly label as speculation all unsupported claims. Replace with specific, bounded limitations.

### Issue 5: Concept attribution quality is unvalidated (Severity: Major)
The paper's third contribution claims "valid concept-driven interpretation" but provides only qualitative examples. No metric, baseline comparison, or human evaluation is used.

**Required action (Must):** Add quantitative evaluation of concept attribution (e.g., concept-probing accuracy, human relevance ratings). Alternatively, downgrade contribution 3 to a qualitative demonstration.

### Issue 6: No statistical significance or variance reporting (Severity: Moderate)
All experiments report single-run results without standard deviations or confidence intervals. Given that some gains are marginal (<1 point), statistical reliability is unclear.

**Required action (Must):** Report mean ± std over at least 3 seeds for all main results (Tables 2 and 3).

### Issue 7: Incomplete related-work differentiation (Severity: Moderate)
The paper does not clearly articulate how CEIR differs from LF-CBM in the Related Work section. Since Phase 1 directly follows LF-CBM's approach, the novelty distinction (supervised classifier → unsupervised VAE) should be explicit from the introduction.

**Required action (Nice-to-have):** Add a comparison table or explicit paragraph in Related Work 2.3 contrasting CEIR with LF-CBM along supervision requirement, representation format, and applicability axes.

## Actionable Suggestions
### Suggestion 1: Fix the evaluation protocol and re-report results (Must, High Impact)
**Current issue:** VAE training uses merged train+test sets; early stopping uses test set.
**Action:** Re-run the VAE training using only the training set (and optionally a held-out validation split from the training set). Report the "no test set" variant from Table 7 as the primary result in Table 2. Keep the current (test-set-augmented) results as a secondary variant with clear disclosure.
**Expected benefit:** Fair comparison with baselines; ~4-6 point reduction in metrics but honest reporting.

### Suggestion 2: Clarify VAE loss with full mathematical specification (Must, High Impact)
**Current issue:** Eq. (2) writes `KL(f(q_i))` ambiguously.
**Action:** Replace Eq. (2) with:

$$ \mathcal{L}_{\text{VAE}}(\theta, \phi) = \sum_{i=1}^{N} \left[ \| q_i - g_\phi(z_i) \|_2^2 + \beta \cdot D_{\text{KL}}( \mathcal{N}(\mu_\theta(q_i), \text{diag}(\sigma_\theta^2(q_i))) \| \mathcal{N}(0, I) ) \right] $$

where $z_i \sim \mathcal{N}(\mu_\theta(q_i), \sigma_\theta^2(q_i))$ via reparameterization. Report the value of $\beta$ and whether it was tuned.
**Expected benefit:** Reproducibility and clarity.

### Suggestion 3: Correct or explain Eq. (1) cubic exponent (Must, High Impact)
**Current issue:** Unexplained `^3` superscript.
**Action:** Remove the `^3` superscript unless it has a specific purpose. If intentional, add one sentence: "We use cubed cosine similarity to amplify agreement between highly activated concepts while suppressing low-activation noise."
**Expected benefit:** Mathematical correctness; reviewer trust.

### Suggestion 4: Restructure Discussion as bounded limitation section (Must, High Impact)
**Current issue:** Unsupported domain generalization and causal claims.
**Action:** Replace the current Discussion with three subsections: (a) Validated findings (what has been shown), (b) Bounded limitations (concept set quality, no OOD evaluation, qualitative-only attribution), (c) Specific future work (concept quality metrics, domain-adaptation experiments).
**Expected benefit:** Scientific credibility; honest positioning.

### Suggestion 5: Add statistical significance reporting (Must, Medium Impact)
**Current issue:** All results are single-run.
**Action:** Report mean ± std over 3 random seeds for Tables 2 and 3 (clustering and linear probing). Add a note about using the same frozen CLIP backbone across seeds.
**Expected benefit:** Readers can assess reliability of reported gains.

### Suggestion 6: Add quantitative concept attribution evaluation (Nice-to-have, Medium Impact)
**Current issue:** Concept quality is only shown qualitatively.
**Action:** Add one of: (a) concept-probing accuracy (train linear probe on concept vectors to predict human-annotated concept presence), (b) human evaluation (10-20 images, 3 raters scoring top-5 concept relevance on Likert scale), or (c) comparison to CLIP-zero-shot concept alignment.
**Expected benefit:** Validation of the core interpretability claim.

### Suggestion 7: Add clarity to narrative structure (Nice-to-have, Low Impact)
**Current issue:** Introduction mixes motivation, linear probing critique, and literature review without clear flow.
**Action:** Restructure the introduction into 4 paragraphs: (P1) Motivation with concrete stakes, (P2) Why current evaluation/attribution is insufficient, (P3) Why concept-based methods, with explicit gap, (P4) CEIR proposal and contributions.
**Expected benefit:** Reader comprehension.

### Suggestion 8: Disclose class-related concept retention transparently (Nice-to-have, Low Impact)
**Current issue:** The concept filtering step intentionally retains class-related concepts (Section 3.1, Appendix A.1.3). While ablation shows minimal performance drop without them, the potential for label leakage should be discussed.
**Action:** Add one sentence: "While retaining class-related concepts could introduce label information indirectly, the ablation study shows their removal causes only a minor performance drop (≤0.73 points for ViT-L/14), suggesting that CEIR's clustering ability does not primarily depend on label-correlated concepts."
**Expected benefit:** Transparency about a potential concern.

## Storyline Options + Writing Outlines
### Abstract Outline (Current vs. Recommended)

**Current abstract structure (5 sentences, mixed roles):**
S1: Trend of SSL → S2: Problem (interpretation difficulty) → S3: Proposed method → S4: Benefits → S5: SOTA clustering + open-world claim.

**Problems:** S2 uses "improves the difficulty" (ungrammatical). S4 and S5 make unsupported generalization claims. The method description does not signal the non-standard VAE usage.

**Recommended Abstract Outline (5 sentences):**
- **S1 (Problem):** State the concrete problem: self-supervised representations are hard to interpret because they lack labels and direct semantic grounding.
- **S2 (Gap):** Existing concept-based methods require supervision or produce explanations only in input space, not in a human-comprehensible concept vocabulary.
- **S3 (Method):** CEIR combines a CLIP-aligned concept bottleneck with a VAE that compresses concept vectors into a compact, interpretable latent representation—all without labels.
- **S4 (Key result):** CEIR achieves competitive unsupervised clustering (e.g., CIFAR10 ACC 95.7%, STL10 ACC 99.2% with ViT-L/14) while enabling concept-level attribution.
- **S5 (Bounded implication):** The approach offers a path toward interpretable unsupervised representations; concept attribution quality and domain generalization require further validation.

### Introduction Outline (Complete, Paragraph-by-Paragraph)

**P1 — Motivation with concrete stakes (NEW):**
Role: Establish why interpretable self-supervised representations matter.
Claim: Self-supervised representations are increasingly used in practice, but their opacity limits debugging, fairness auditing, and scientific discovery.
Evidence anchor: Reference common deployment contexts (medical imaging, autonomous driving) where interpretability is critical.
Transition: "However, current evaluation protocols cannot tell us what these representations actually encode."

**P2 — Why current evaluation is insufficient (rewrite of current P1):**
Role: Critique linear probing and downstream-accuracy-based evaluation.
Claim: Linear probing measures label-predictive power but does not assess semantic content or human-comprehensibility of the representation itself.
Evidence anchor: Reference known limitations of linear probing (e.g., labels can exploit spurious correlations).
Transition: "To evaluate representations directly, we need post-hoc attribution methods that explain what each representation dimension encodes."

**P3 — Limitations of existing attribution methods (rewrite of current P2-P3):**
Role: Review existing attribution approaches and explain why they fall short for unsupervised representations.
Claim: Feature-attribution methods are unstable and operate in input space, example-based methods lack granularity, and concept-based methods require labels.
Evidence anchor: Cite Kindermans et al. (instability), Crabbé & van der Schaar (label-free adaptation), Kim et al. / Koh et al. (concept methods with supervision).
Transition: "A gap remains: no existing method produces unsupervised representations that are both semantically rich and attributable to human concepts without labels."

**P4 — CEIR proposal and contributions (rewrite of current P4):**
Role: Introduce CEIR and list contributions with bounded claims.
Claim: CEIR is the first approach to combine a concept bottleneck with unsupervised representation learning via VAE concept compression.
Evidence preview: SOTA clustering on several benchmarks; qualitative concept attribution.
Contributions: (1) Concept bottleneck for representation learning, (2) Strong clustering results, (3) Label-free concept attribution (qualitative demonstration).
Transition: "We now describe the method in detail."

### Alternative Storyline Candidates

**Candidate A (Current narrative — Problem-focused):** Starts with "interpretability is needed" → discusses attribution challenges → reviews concept-based methods → proposes CEIR. **Weakness:** The connection between linear probing critique and concept-based attribution is not clearly motivated; the reader may lose track of the core problem.

**Candidate B (Method-focused — Recommended):** Starts with a concrete use case (e.g., "a practitioner wants to know what a representation encodes") → identifies the gap (no unsupervised + concept-attributable method exists) → proposes CEIR as a solution → evaluates. **Strength:** Clear problem-solution narrative; easier for readers to follow.

**Candidate C (Gap-first):** Starts by stating the missing capability (unsupervised representations with concept-level attribution) → explains why existing methods (linear probing, feature attribution, TCAV, CBM) cannot provide this → introduces CEIR as filling this precise gap. **Strength:** Direct and honest positioning; avoids narrative detours.

## Priority Revision Plan
### P0 — Must-fix before any resubmission (acceptance-critical)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0.1 | Test data contamination | Re-run VAE without test set merging; report both variants with clear labeling | Removes information-leakage concern; honest comparison |
| P0.2 | VAE loss Eq. (2) underspecified | Rewrite with explicit encoder distributions and reparameterization | Enables reproducibility |
| P0.3 | Eq. (1) cubic exponent unexplained | Remove or justify `^3` notation | Mathematical correctness |
| P0.4 | Unsupported claims in Discussion | Remove domain generalization and causal claims; replace with bounded limitations | Scientific credibility |

### P1 — Strongly recommended (quality improvement)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1.1 | No variance reporting | Add mean±std over ≥3 seeds to Tables 2 and 3 | Statistical reliability |
| P1.2 | Abstract overclaiming | Bound "state-of-the-art" to specific backbones/datasets; remove unsupported robustness claim | Honest positioning |
| P1.3 | Concept attribution unvalidated | Add quantitative evaluation (concept-probing accuracy or human evaluation) | Validates core contribution |
| P1.4 | Introduction narrative unfocused | Restructure into 4 clean paragraphs (see Storyline Options) | Reader comprehension |

### P2 — Nice-to-have (polish and completeness)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2.1 | Related Work differentiation | Add explicit CEIR vs. LF-CBM comparison paragraph | Clearer novelty positioning |
| P2.2 | Class-related concept disclosure | Add transparency sentence about potential label leakage | Reviewer trust |
| P2.3 | Open-world demo rigor | Expand demo with more diverse images and quantitative evaluation | Strengthens application claim |

### Revision Workflow (Recommended Order)

```text
Stage 1 (Week 1): Fix critical methodology issues
  ├── Fix VAE loss specification (Eq. 2)
  ├── Fix/explain cubic exponent (Eq. 1)
  ├── Re-run experiments without test set merging
  └── Update Discussion with bounded limitations

Stage 2 (Week 2): Improve empirical rigor
  ├── Add 3-seed variance reporting
  ├── Add concept-probing evaluation
  └── Run failure-case analysis for concept attribution

Stage 3 (Week 3): Polish narrative and claims
  ├── Restructure introduction per storyline outline
  ├── Tighten abstract claims
  ├── Add CEIR vs LF-CBM comparison
  └── Final proofread for grammar and clarity
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Unsupervised clustering (Table 2) | CIFAR10, CIFAR100-20, CIFAR100, STL10, ImageNet; K-means on VAE latent h; backbones: RN50, ViT-B/16, ViT-L/14 | NMI, ACC, ARI | CEIR (ViT-L/14) achieves best on CIFAR10, STL10; competitive on others | C2 (SOTA clustering) | Test set merged into VAE training; no variance reported; early stopping on test set |
| E2 | Linear probing (Table 3) | Linear layer on latent h; same datasets as E1 | NMI, ACC, ARI | CEIR underperforms CLIP backbone; 0.9-5.3pt drop | C1 (representation quality) | No analysis of why drop occurs; only 3 datasets |
| E3 | Concept attribution (Figure 3) | 4 ImageNet image pairs + real-world images; ResNet50 backbone | Qualitative (alluvial maps) | Concepts capture shared/discriminative semantics | C3 (interpretability) | No quantitative metric; no failure cases; no baseline comparison |
| E4 | Open-world concept mining (Figure 4) | 24 unsourced "Kamakura" images; ResNet50 trained on ImageNet | Qualitative (word cloud) | Relevant concepts identified | C3 (open-world generalization) | Tiny sample (24 images); single query; no diversity analysis; no quantitative validation |
| E5 | Ablation: class-related concepts (Table 7) | CIFAR10, CIFAR100-20, STL10; remove class concepts | NMI, ACC, ARI | Minimal drop (≤0.73pt for ViT-L/14) | Supports claim that label leakage is minimal | Only tested on 3 datasets |
| E6 | Ablation: test set in VAE (Table 7) | Same as E5; remove test set from VAE training | NMI, ACC, ARI | 4-6pt drop across metrics | Highlights information leakage concern | This should be the primary result |
| E7 | Ablation: VAE vs. CLIP only (Table 7) | Same as E5; remove VAE, use raw CLIP backbone | NMI, ACC, ARI | VAE improves over CLIP baseline (e.g., +6.4pt NMI for CIFAR10 ViT-L/14) | C1 (VAE helps) | CLIP baseline already strong; marginal gain varies |
| E8 | Ablation: latent size (Table 8) | Vary h size: 128 vs 256 | NMI, ACC, ARI | 128 better for small datasets; 256 better for ImageNet | Supports design choice | Limited to 2 sizes; no principled selection criterion |
| E9 | Unlabeled data effect (Table 9) | STL10 with/without 100K unlabeled images | NMI, ACC, ARI | Unlabeled data helps all backbones (e.g., +6.7pt NMI for RN50) | Supports scalability claim | Only tested on STL10 |

### Research-Theme Gap Diagnosis

| Research Value Dimension | Current Support | Gap | Required Evidence |
|-------------------------|----------------|-----|------------------|
| **New knowledge** (concept bottleneck for unsupervised representation learning) | Moderate | The core idea (CBM + VAE) is novel in combination, but Phase 1 closely follows LF-CBM. Need external literature verification. | Manual literature review (deferred) |
| **Reproducibility** | Low | VAE loss underspecified; concept filtering thresholds dataset-specific; GPT-4 prompts not fully reproducible due to API nondeterminism | Full VAE spec; release concept lists; fix random seeds |
| **Impact on practice** (usable interpretable representations) | Moderate | Clustering results are strong, but concept attribution is unvalidated; open-world demo is too small to demonstrate practical utility | Quantitative attribution eval; larger open-world study |

### Proposed Research Experiments

**P0 Experiment: Re-run with clean evaluation protocol**
- **Target Claim:** Clustering performance
- **Hypothesis:** Results without test set merging are still competitive
- **Minimal Design:** Re-run VAE training on training set only for all datasets; report Table 2 results
- **Controls/Baselines:** Same baselines as Table 2
- **Metrics:** NMI, ACC, ARI
- **Success Criterion:** Results remain within 3 points of current Table 2 for ViT-L/14
- **Estimated Cost:** 2-4 GPU hours
- **Expected Paper-Quality Gain:** Removes #1 reviewer concern about information leakage

**P1 Experiment: Concept-probing evaluation**
- **Target Claim:** C3 (interpretability)
- **Hypothesis:** Top-ranked concepts per image correlate with human-annotated image attributes
- **Minimal Design:** Use 200 images from CIFAR10/STL10; for each image, ask 3 annotators whether each of the top-5 activated concepts is "present," "somewhat present," or "absent"; compute precision@5 and mean average precision
- **Controls/Baselines:** Compare to CLIP-zero-shot concept alignment (cosine similarity between CLIP text embeddings and image)
- **Metrics:** Precision@5, MAP, inter-annotator agreement (Fleiss' κ)
- **Success Criterion:** Precision@5 > 0.7, MAP > 0.6
- **Estimated Cost:** 1-2 hours human annotation + 1 GPU hour
- **Expected Paper-Quality Gain:** Validates the core interpretability claim with evidence

**P1 Experiment: Variance reporting**
- **Target Claim:** All claims in C2
- **Hypothesis:** Gains are statistically significant
- **Minimal Design:** Run CEIR (ViT-B/16 and ViT-L/14) on CIFAR10, CIFAR100-20, STL10 with 3 random seeds
- **Controls/Baselines:** Report mean±std for all baselines (re-run with 3 seeds where feasible)
- **Metrics:** NMI, ACC, ARI with std
- **Success Criterion:** Standard deviations ≤ 1.0 for all metrics
- **Estimated Cost:** 3-6 GPU hours
- **Expected Paper-Quality Gain:** Statistical rigor; confidence in gains

**P2 Experiment: Domain-shift sensitivity test**
- **Target Claim:** C1 (robustness — currently speculative)
- **Hypothesis:** CEIR concept-based representations are more stable under common corruptions than raw CLIP features
- **Minimal Design:** Evaluate on CIFAR10-C (15 corruptions, 5 severity levels); compare clustering NMI drop vs. CLIP baseline
- **Controls/Baselines:** Raw CLIP features, SimCLR, MoCo
- **Metrics:** NMI drop % (corruption vs. clean), mean corruption error (mCE)
- **Success Criterion:** CEIR shows smaller NMI drop than baselines under ≥10 corruption types
- **Estimated Cost:** 2-4 GPU hours
- **Expected Paper-Quality Gain:** Replaces the unsupported domain generalization claim with actual evidence

```text
ASCII Diagram — Experiment Upgrade Plan

Stage 0 (Acceptance-critical, 2-4 GPU hours)
  [Clean evaluation] -> [Re-run Table 2 w/o test set merge]
  -> [Report both variants with disclosure]

Stage 1 (High-impact, 4-8 GPU hours + annotation)
  [Concept-probing eval] -> [200 images, 3 annotators]
  -> [Precision@5, MAP, inter-annotator agreement]
  |
  [Variance reporting] -> [3 seeds, all datasets]
  -> [mean±std for Tables 2 & 3]

Stage 2 (Impact-enhancing, optional)
  [Domain-shift test] -> [CIFAR10-C, 15 corruptions]
  -> [NMI drop %, mCE comparison]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Scoring rationale (research value + novelty as primary dimensions):**

- **Research value (6/10):** The problem is relevant and the pipeline design is clean. However, the core contribution (applying CBM to representation learning via VAE) is incremental over LF-CBM. The experimental evaluation has a significant fairness concern (test-data-informed training). The concept attribution capability is demonstrated only qualitatively. These factors reduce the practical impact of the current manuscript.
- **Novelty (5/10):** The combination of CBM + VAE for unsupervised representation learning is a reasonable contribution. However, Phase 1 directly follows LF-CBM, and the VAE compression of concept vectors is a relatively straightforward extension. External literature verification was unavailable in this run, so this assessment is provisional and deferred for manual verification.
- **Validity/Soundness (5/10):** The VAE loss formulation is underspecified (Eq. 2), the training objective has an unexplained notation issue (Eq. 1), and the evaluation protocol uses test data in training. These issues reduce confidence in the reported results.
- **Reproducibility (4/10):** Insufficient detail in VAE loss, concept filtering thresholds, and GPT-4 prompt nondeterminism. The VAE implementation cannot be reproduced from the text alone.
- **Presentation/Clarity (6/10):** The concept visualizations are effective, and the overall structure is logical. However, the introduction narrative is unfocused, the Discussion introduces unsupported claims, and several sentences contain grammatical errors.

**Post-Revision Target: [6.5, 7.5] / 10**

If all P0 issues are addressed (clean evaluation protocol, corrected Eq. 1 and Eq. 2, bounded Discussion), variance reporting is added, and concept attribution is quantitatively evaluated, the paper could reach 6.5-7.5/10. The upper bound assumes external literature verification confirms sufficient novelty headroom over LF-CBM and related methods.