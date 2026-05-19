## Summary
This paper proposes Federated Dual Prompt Tuning (Fed-DPT), a parameter-efficient federated learning method designed to address severe domain shift across clients. By leveraging a pre-trained CLIP model, Fed-DPT introduces domain-specific textual prompts and couples them with visual prompts via self-attention to dynamically weight cross-modal representations. The method employs a novel aggregation strategy: concatenating domain-specific text prompts and averaging visual prompts, stabilized by momentum updates. Extensive experiments on DomainNet, OfficeHome, and PACS demonstrate that Fed-DPT outperforms conventional FL methods (FedAvg, FedProx) and domain-agnostic CLIP-based baselines (PromptFL, FedCLIP), achieving 68.4% average accuracy on DomainNet with lower cross-domain variance. The work presents a compelling direction for domain-aware foundation model adaptation in federated settings, though it requires tighter claim bounding, fairness clarifications in baselines, and stronger privacy justification.

## Strengths
- **Novel Domain-Aware Aggregation Strategy:** The proposal to concatenate domain-specific text prompts rather than averaging them is a conceptually sound intervention. It directly addresses the representation collapse problem in standard FL when clients operate under distinct visual distributions, preserving domain-specific semantic shifts.
- **Effective Visual-Textual Coupling Mechanism:** Using visual prompt attention weights to dynamically route textual contexts is an elegant, parameter-efficient solution. It enables the model to adapt to input-specific domain characteristics without requiring explicit domain labels or additional classification heads.
- **Comprehensive Empirical Validation:** The paper evaluates Fed-DPT across three standard domain adaptation benchmarks (DomainNet, OfficeHome, PACS) and includes thorough ablation studies on prompt length, communication frequency, and component contributions. The consistent outperformance over domain-agnostic baselines (PromptFL, FedCLIP) and lower cross-domain variance strongly support the method's robustness.
- **Parameter Efficiency and Communication Frugality:** By freezing the CLIP encoders and optimizing only lightweight prompt tokens, Fed-DPT significantly reduces communication overhead and training instability, making it highly suitable for cross-silo federated settings with large foundation models.

## Weaknesses
- **Overstated Privacy Guarantees:** The claim that shared prompts have the "same level of privacy-preserving capabilities to FedAvg" is insufficient. Prompt inversion and memorization attacks are documented risks in prompt tuning literature. The paper lacks formal privacy analysis or empirical attack simulation, relying solely on nearest-neighbor vocabulary decoding, which does not prove data safety.
- **Optimizer Mismatch in Baseline Comparison:** Fed-DPT uses AdamW, while conventional baselines (FedAvg/FedProx) use SGD. This confounds the "robustness to big models" claim, as AdamW naturally optimizes ViT backbones more effectively. The comparison lacks a controlled setting where all methods use identical optimizers, weakening the causal attribution of gains to the prompt mechanism.
- **Under-Justified Visual Prompt Role:** Ablation results show visual prompts alone contribute minimally (+0.6%), yet the narrative positions them as core domain detectors. The mechanism by which attention weights learn domain routing without explicit supervision is under-explained, and the choice of extracting keys from the last self-attention block lacks architectural justification.
- **Lack of Statistical Rigor and Variance Reporting:** Main results report average accuracy but omit standard deviations or confidence intervals in tables. Claims of "significant effectiveness" and "superior performance" rely on point estimates, making it difficult to assess statistical reliability, especially for small margins against strong baselines like PromptFL.
- **Generic Problem Formulation and Narrative Flow:** The introduction and problem formulation lack mathematical rigor regarding domain shift assumptions. The transition from non-i.i.d. label critique to domain-level heterogeneity is abrupt, and the contribution paragraph buries the core novelty (domain-specific routing) behind generic parameter-efficiency claims.

## Key Issues
1. **Privacy Claim Validity (Major):** The assertion that prompt sharing is equivalent to FedAvg in privacy preservation is scientifically unsupported. Learnable prompts can memorize and leak domain-specific features. Without formal bounds or attack simulations, this claim risks misleading readers about deployment safety.
2. **Baseline Fairness and Causal Attribution (Major):** The optimizer mismatch (AdamW vs. SGD) and lack of variance reporting undermine the robustness claims. Gains attributed to domain-aware routing may partially stem from better optimization dynamics. Controlled comparisons are necessary to isolate the mechanism's contribution.
3. **Mechanism Justification Gap (Major):** The visual-textual coupling mechanism relies on implicit supervision via L2 loss, but the paper does not explain how attention weights converge to meaningful domain correlations. The ablation showing minimal standalone visual prompt contribution further weakens the narrative without a clear synergy explanation.
4. **Statistical Reliability (Minor):** Main results tables lack standard deviations. In federated learning with heterogeneous data, point estimates are insufficient to validate stability claims across communication rounds and random seeds.

## Actionable Suggestions
- **Downgrade and Bound Privacy Claims:** Replace the equivalence claim with a bounded discussion. Acknowledge that while prompts are less interpretable than gradients, they may still leak stylistic features. Cite recent prompt-privacy literature and suggest adding a membership inference attack baseline in future work.
- **Control Optimizer and Report Variance:** Re-run conventional baselines (FedAvg/FedProx) using AdamW to match Fed-DPT's optimization dynamics. Add standard deviations (mean ± std over ≥3 seeds) to all main result tables. Explicitly state that gains persist under matched optimizers.
- **Clarify Visual-Textual Synergy:** Revise the ablation discussion to acknowledge textual primacy. Explain that visual prompts act as stabilizers that reduce cross-domain variance and prevent catastrophic interference during aggregation, rather than standalone domain detectors. Add a brief analysis of attention weight distributions to visualize routing behavior.
- **Tighten Problem Formulation:** Introduce formal distributional assumptions ($P_i(x) \neq P_j(x)$) in Section 4.1. Explicitly connect domain shift to the failure of standard parameter averaging, grounding the method design in mathematical intuition.
- **Improve Narrative Flow:** Restructure the introduction to foreground the domain-specific routing mechanism immediately. Remove hype language ("Remarkably", "significant effectiveness") and replace with precise deltas and consistency metrics.

## Storyline Options + Writing Outlines
**Abstract Outline (4-5 sentences):**
- S1 (Problem): Federated learning struggles with severe domain shift across clients, as standard aggregation averages out distinct visual styles.
- S2 (Gap): Existing CLIP-based FL methods rely on domain-agnostic prompts, failing to adapt to heterogeneous feature distributions.
- S3 (Method): We propose Fed-DPT, which introduces domain-specific textual prompts dynamically weighted by visual prompt attention, enabling adaptive cross-modal alignment.
- S4 (Result): Fed-DPT achieves 68.4% accuracy on DomainNet, outperforming domain-agnostic baselines by 5.2% with lower cross-domain variance.
- S5 (Implication): The method demonstrates that decoupled, domain-aware prompt aggregation stabilizes foundation model adaptation in cross-silo FL.

**Introduction Outline (Paragraph-by-Paragraph):**
- P1 (Hook & Stakes): FL enables privacy-preserving training but faces bottlenecks when deploying large VLMs across heterogeneous clients. Domain shift breaks standard aggregation, causing representation collapse.
- P2 (Critique of Prior Setup): Simulating heterogeneity via non-i.i.d. label splits overlooks feature-level distribution shifts. Domain shift fundamentally alters input marginals, requiring adaptation beyond classifier heads.
- P3 (Proposed Solution): Fed-DPT addresses this by maintaining domain-specific textual prompts and coupling them with visual prompts via self-attention. This allows dynamic routing based on input visual style without explicit domain labels.
- P4 (Aggregation & Stability): We design a novel aggregation protocol: concatenating text prompts to preserve domain semantics, while averaging visual prompts stabilized by momentum updates to prevent sudden parameter shifts.
- P5 (Evidence & Contributions): Experiments on DomainNet, OfficeHome, and PACS show consistent gains over PromptFL and FedCLIP. Contributions: (1) domain-aware prompt formulation, (2) visual-textual routing mechanism, (3) robust aggregation strategy with empirical validation.

## Priority Revision Plan
**P0 (Critical - Must Fix Before Submission):**
- Downgrade privacy claims to bounded discussion; acknowledge prompt inversion risks and lack of formal guarantees.
- Re-run conventional baselines (FedAvg/FedProx) with AdamW to ensure optimizer fairness; report mean ± std over ≥3 seeds in all tables.
- Clarify visual prompt role in ablation discussion; emphasize textual primacy and visual stabilization synergy.

**P1 (Major - Strongly Recommended):**
- Add formal distributional assumptions ($P_i(x) \neq P_j(x)$) to Section 4.1 to ground the domain shift challenge.
- Include attention weight distribution analysis or visualization to empirically validate the domain routing mechanism.
- Restructure introduction to foreground domain-specific routing immediately; remove hype language and replace with precise deltas.

**P2 (Minor - Quality Improvement):**
- Add data split protocol details (e.g., 50/50 train/test) and baseline tuning budget clarification in Section 5.1.
- Improve figure captions to explicitly state main conclusions and comparison baselines.
- Proofread for typos (e.g., "realative", "DomianNet") and ensure consistent terminology across sections.

## Experiment Inventory & Research Experiment Plan
**Completed Experiment Inventory:**
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|---|---|---|---|---|---|---|
| E1 | Fed-DPT outperforms baselines under domain shift | DomainNet, OfficeHome, PACS; 6/4 clients | Accuracy (%) | +5.2% avg over PromptFL | Yes | No variance reported |
| E2 | Component ablation (visual/textual/domain-specific) | DomainNet; variants of Fed-DPT | Accuracy (%) | Full model +14.8% over zero-shot | Yes | Visual-only contribution low |
| E3 | Hyperparameter sensitivity (momentum, length, freq) | DomainNet; ablation tables | Accuracy (%) | m=16, α=0.99 optimal | Yes | Limited range tested |
| E4 | Non-i.i.d. label robustness (30 clients) | DomainNet; Dirichlet split | Accuracy (%) | -1.5% drop vs -3.6% FedAvg | Yes | Only one dataset tested |

**Research-Theme Gap Diagnosis:**
The core claim of domain-aware routing lacks empirical visualization of attention weights. Privacy guarantees are asserted but not tested. Optimizer fairness confounds robustness claims.

**Proposed Research Experiments:**
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| Domain Routing Validity | Attention weights correlate with true domain | Visualize $w_i$ distributions across domains | Randomized prompts | Entropy/Alignment | Clear domain separation | Low | High |
| Optimizer Fairness | Gains persist under matched optimizers | Re-run FedAvg/FedProx with AdamW | Same seeds/budget | Accuracy ± std | Delta maintained | Medium | High |
| Privacy Risk | Prompts leak domain features | Membership inference attack baseline | FedAvg gradients | AUC/Advantage | Lower than gradients | Medium | Medium |
| OOD Generalization | Method transfers to unseen domains | Test on VCD or new DomainNet split | Zero-shot CLIP | Accuracy drop | Smaller drop than baselines | Low | High |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a conceptually sound and empirically effective method for domain-aware federated learning using dual prompt tuning. The core idea of concatenating domain-specific text prompts and coupling them with visual attention is novel and addresses a realistic bottleneck in cross-silo FL. However, the score is moderated by overstated privacy claims, optimizer mismatch in baseline comparisons, and lack of statistical variance reporting. The mechanism justification for visual prompts also requires tightening. With targeted revisions to bound claims, ensure fairness, and add variance, the paper would be significantly stronger.

**Post-Revision Target:** [7.5, 8.5]/10

**Expected Gains:** Resolving optimizer fairness and adding variance reporting will solidify the robustness claims. Downgrading privacy assertions to bounded discussion will improve scientific credibility. Clarifying the visual-textual synergy will strengthen the methodological narrative, making the contribution more defensible and impactful.