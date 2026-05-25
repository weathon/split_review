Now I have all the information needed. Let me compile the final review.

## Summary

This paper introduces L-TTA, a test-time adaptation framework for Vision-Language Models (VLMs) operating under long-tailed test distributions. It proposes three co-designed components: Synergistic Prototypes (SyPs) combining Deterministic and Exclusionary Prototypes to enrich tail-class representations, learnable Rebalancing Shortcuts (RSs) with a class-reallocation loss, and Balanced Entropy Minimization (BEM) with theoretical propositions. Experiments across 15 datasets with imbalance ratios up to 50 show consistent improvements over 12 VLM TTA baselines in both accuracy and macro-F1.

## Strengths

1. **First systematic treatment of long-tailed TTA for VLMs.** The paper identifies and addresses a genuinely underexplored problem — most VLM TTA methods assume balanced test streams, while real-world distributions are long-tailed. The two failure modes identified (text-induced tail erosion and modality-bias amplification) provide a meaningful conceptual framework. The paper backs up the problem motivation by showing that existing methods degrade as imbalance increases (Figure 2, Table 1).

2. **Consistent and substantial empirical gains across diverse settings.** L-TTA outperforms 12 prior VLM TTA methods on OOD (Table 1), cross-domain (Table 2), and corruption benchmarks (Table 3), with gains widening under stronger imbalance (e.g., +2.87% accuracy and +2.64% macro-F1 on the corruption benchmark). The advantage holds across four backbone families (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG) as shown in Table 5.

3. **BEM with theoretical motivation.** Propositions 1 and 2 provide a plausible analytical rationale for why standard entropy minimization biases head classes and how BEM's penalty term reduces the gradient gap between head and tail. The ablation (Table 6) confirms BEM adds a clear improvement over SyP+RS alone.

4. **Favorable efficiency-accuracy trade-off.** Table 4 shows L-TTA (1.45h, 1.89GB) is substantially more efficient than training-heavy methods (RLCF 18.3h, WATT 27.7h) while achieving the highest harmonic mean on both cross-domain and corruption benchmarks.

## Weaknesses

### Fatal
None.

### Major

1. **Exclusionary Prototype design is insufficiently justified and its claimed function does not clearly align with the update rule.** The paper states that EPs store "the most improbable features of each class" (Sec. 3.2). However, Eq. 5 updates every class's EP from every view, and for the predicted class (where φ_c = 0) the feature is incorporated with the same functional form as for all other classes — differing only in a discount factor that becomes negligible as the step counter N grows. It is not clearly explained how this mechanism produces "exclusionary" semantics distinct from a running average of all features weighted by class prediction. While the ablation (Table 6) shows that combining DPs and EPs outperforms either alone, the paper does not provide an analysis (e.g., feature similarity, nearest-neighbor visualization) demonstrating that EPs capture semantically different information from DPs. This lack of clarity undermines a core component of the method. The authors should either clarify the intended behavior with a precise justification, or provide evidence that the EPs function as claimed.

### Minor

2. **Theoretical propositions lack sufficient precision.** Propositions 1 and 2 are presented as formal claims, but the splitting rule for head/tail classes is described only as "with certain measurements" (Sec. 3.2) without specifying the partitioning criterion or the assumptions needed for the gradient inequalities. The claims are plausible heuristics, but without stated assumptions they do not rise to the level of rigorous theoretical results. The proofs (deferred to the appendix) may address this, but the main paper should at minimum specify the partitioning rule.

3. **Missing implementation details for several components.** (a) The threshold θ for DP updates is said to be updated "following the above EMA manner" but the formula is not provided. (b) The cross-attention in RSs (Eq. 6) is described only as "Attn calculates the attention score" — the specific mechanism (scaled dot-product vs. additive), dimensions, and scaling are omitted. (c) The learnable hyper-class vectors q are not described in terms of initialization or update procedure. (d) In Eq. 9, the variable \tilde{P} is used without definition. These details are necessary for reproducibility.

4. **Failure modes are introduced without direct quantitative evidence.** The two failure modes (Text-induced Tail Erosion and Modality-bias Amplification) are presented in Figure 1 as conceptual illustrations, but the paper does not include controlled experiments that empirically confirm these specific mechanisms (e.g., comparing unimodal vs. bimodal adaptation on VLMs, or isolating the effect of text-pretraining bias). The overall degradation of existing methods under long-tailed test sets is well-documented, but the specific causal pathways asserted in the motivation remain unvalidated.

5. **Ablation studies and hyperparameter sensitivity are concentrated on a single dataset.** While Figure 4(c) and (d) include Food101 alongside ImageNet for two hyperparameters, the ablations for λ₁, λ₂ (Fig. 4a) and η (Fig. 4b) are conducted only on ImageNet. The paper does not assess whether the chosen hyperparameters generalize well to other datasets.

6. **Standard deviations are not reported.** The paper states "5 runs for each experiment" but no tables include standard deviations or confidence intervals. When improvements over baselines are modest in some settings (1–2%), variance information is important for assessing reliability.

### Trivial

7. The EMA update for DPs (Eq. 4) uses a non-standard cumulative-normalization form rather than a conventional momentum parameter. This is not inherently problematic but should be briefly justified to avoid confusion.

## Nice-to-Haves

- An analysis of how prototypes (DPs and EPs) evolve over the test stream, with visualizations or statistics for head vs. tail classes, would strengthen the claim that SyPs enrich tail representations.
- A controlled experiment that directly tests the two claimed failure modes (e.g., comparing unimodal SAR on a VLM vs. a pure visual backbone to quantify modality-bias amplification) would connect the motivation more tightly to the method.
- The CRA loss (Eq. 7) adds complexity; an ablation that replaces RSs with a simpler learned linear transformation of prototypes would clarify whether the MoE-inspired design is necessary or whether simpler rebalancing suffices.
- A study of BEM's sensitivity to prior estimation quality (e.g., comparing performance with true priors, estimated priors, and fixed uniform priors) would be informative.

## Removed Points

These points were flagged by reviewers but are removed here for the stated reasons:

- **"EP ablation not compared to DP alone"** — Factually incorrect; Table 6 explicitly reports both DP-alone and EP-alone results. Removed as factually wrong.
- **"Missing non-i.i.d. TTA baselines (SAR, DELTA, LAME, DA-TTA)"** — The paper focuses on VLM TTA and compares against 12 VLM-specific methods. The non-i.i.d. methods mentioned are not designed for the VLM prompt-tuning setting; the paper explains this distinction in Related Work. Removed as a scope misunderstanding.
- **"Proofs in inaccessible appendix"** — The parser strips all appendix content; the appendix exists in the original submission. Removed per hard rules.
- **"Corruption Benchmark uses only Gaussian noise"** — This is a presentation choice; the paper explicitly notes that 16 other corruption types are evaluated in the appendix. Removed as a format/presentation nitpick.
- **"The ablation of EP alone (excluding DP) is not compared to DP alone to isolate the contribution of the exclusionary design"** — As noted, Table 6 already provides this comparison (DP: 68.68/63.40, EP: 67.54/62.20 on ViT-B/16). Removed as factually wrong.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Clarify the EP mechanism.** Provide a clear, self-contained explanation of how the update rule (Eq. 5) yields exclusionary semantics. Include an analysis (e.g., feature similarity, t-SNE visualization) comparing DP and EP representations to demonstrate that they capture distinct information.
- **Add standard deviations** to all main experimental tables to enable assessment of result reliability.
- **Specify the head/tail partitioning rule** used in Propositions 1 and 2, and state the assumptions under which the gradient inequalities are derived.
- **Provide the missing implementation details** listed in Minor weakness #3.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>