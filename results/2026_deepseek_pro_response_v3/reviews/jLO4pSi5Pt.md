Now I have enough information to make a final calibration. Let me compare:

- **DOTA (6.00, Reject):** TTA for VLMs with distribution estimation; reviewers noted limited novelty and missing analyses. Our paper has more novel components, a clearly underexplored problem (long-tailed TTA), and more comprehensive experiments. **Clearly stronger.**
- **MLLM Concept Drift (7.00, Accept):** Long-tailed + OOD drift in MLLMs; creates new dataset, has theoretical depth, but reviewers flagged unclear methodology and missing comparisons. Our paper has more focused evaluation and cleaner methodology, but less theoretical depth and no new dataset. **Slightly weaker or comparable.**
- **CLIP Reward TTA (6.67, Accept):** Clean single-idea TTA for VLMs. Our paper has broader scope and more comprehensive evaluation. **Slightly stronger.**

Our paper lands between DOTA (6.0) and MLLM Concept Drift (7.0), closest to **6.5**.

Now let me write the final review.

---

## Summary
This paper proposes L-TTA, the first method for test-time adaptation of vision-language models under long-tailed test distributions. L-TTA consists of three components: Synergistic Prototypes (SyPs, including Deterministic and Exclusionary Prototypes for maintaining tail-class features), Rebalancing Shortcuts (RSs, learnable cross-attention with a Class Re-Allocation loss), and Balanced Entropy Minimization (BEM, a modified entropy minimization that down-weights prior corrections for confident predictions). The method is evaluated on 15 datasets across OOD, cross-domain, and corruption benchmarks at three imbalance ratios (10, 20, 50) and five backbones, outperforming 11 baselines in both accuracy and macro-F1.

## Strengths
- **Clear empirical framing of failure modes:** The paper identifies two VLM-specific failure mechanisms (Text-induced Tail Erosion, Modality-bias Amplification) and provides diagnostic evidence via Figure 1 (rich-class analysis and SAR-on-VLM degradation), giving the method design strong motivation.
- **Comprehensive evaluation:** 15 datasets spanning OOD, Cross-Domain, and Corruption benchmarks, 3 imbalance ratios, and 5 backbones (ResNet-50, ViT-B/16, ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG). L-TTA outperforms all 11 baselines in both accuracy and macro-F1 in virtually every setting, with gains growing under corruption (2.87% accuracy, 2.64% macro-F1 average improvement, Table 3).
- **Exclusionary Prototypes as a novel mechanism:** EPs update prototypes for all classes on every sample (Eq. 5), weighted inversely by prediction confidence (φ_c), ensuring tail classes receive feature updates even when never predicted. Ablation (Table 6) confirms removing EPs from SyPs drops macro-F1 by ~3.2% on ViT-B/16.
- **BEM with theoretical grounding and empirical validation:** Proposition 2 provides a formal claim that BEM reduces the head-tail gradient gap (Eq. 10). The β analysis (Figure 4d) shows intermediate β outperforms extremes, validating the confidence-gating design.
- **Computational efficiency:** Table 4 shows 1.45h runtime vs. competitors requiring 18–28h (RLCF, WATT), while achieving the best harmonic mean of accuracy and macro-F1 (67.20 on LT-CDB).
- **Thorough component ablation:** Table 6 systematically shows progressive gains from DP alone → DP+RS → SyP+RS → SyP+RS+BEM on two backbones, with every component contributing additively.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Proposition 1 stated without explicit assumptions linking cardinality to gradient signs:** The proposition (line 132) asserts gradient sign patterns (E[∇H] < 0 for head, > 0 for tail) based solely on class cardinality ordering. However, ∇_{z_i}H = p_i(H + log p_i) depends on the model's softmax distribution, not directly on class cardinality. The main text does not state the assumptions under which class frequency translates to gradient behavior. This weakens the theoretical motivation for BEM, though BEM is independently supported by Proposition 2 and strong empirical evidence.
- **Exclusionary Prototypes rationale is somewhat underspecified:** The EP mechanism (Eq. 5) updates every class prototype with every view's features, weighted by φ_c. The paper claims this enriches tail classes with "extra inter-class knowledge," but the mechanism can also be viewed as making prototypes weighted blends of all visual features, which could homogenize rather than discriminate. The ablation (Table 6) convincingly supports EP's empirical value, but the paper would benefit from sharper justification for why accumulating features weighted by improbability aids discrimination.
- **CRA-to-class-balancing causal chain is indirect:** The Class Re-Allocation loss (Eq. 7) enforces uniform hyper-class (expert) utilization. The paper claims this "reduces dominance of head-class prototypes" (line 120), but CRA constrains routing to experts, not final predictions (Eq. 8). Head-class prototypes could still dominate while satisfying CRA. The η ablation (Fig 4b) shows empirical gains from CRA, but the rationale linking uniform expert utilization to balanced predictions is not fully argued.

### Trivial
- **MTA anomaly in Table 1:** MTA reports identical accuracy and macro-F1 for ImageNet-A across all three imbalance ratios (57.15/51.98 at imb=10, 20, and 50). This is either a distribution-independent property of MTA worth noting, or a copy-paste error requiring correction.
- **Dataset construction ambiguity:** The paper does not clarify whether long-tailed sampling is applied within the available classes for each OOD dataset (ImageNet-A has 200 classes, ImageNet-R has 200, ImageNet-S has 1000) or mapped to the full ImageNet label space.

## Nice-to-Haves
- A full-system baseline combining existing TTA methods (e.g., DPE) with standard long-tailed corrections (logit adjustment, balanced softmax) would directly test the paper's claim (lines 134-135) that these corrections are insufficient for TTA and that BEM is necessary.
- Per-imbalance-ratio breakdowns for the Cross-Domain Benchmark (Table 2) in the main text would better support the paper's thesis about robustness to long-tail severity.
- Comparison with existing unimodal LT-TTA methods (DELTA, LAME) — the paper mentions these in related work (line 58) and tests SAR in Figure 1b.2, but including them as baselines or explicitly explaining their inapplicability to VLM-based TTA would strengthen the evaluation.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The proof is deferred to the stripped appendix, so it cannot be examined."** Removed per hard rule: the appendix exists in the original submission and is stripped by the parser. The concern about Proposition 1 being under-specified in the main text is retained as a Minor weakness.
- **Harsh Critic: "The reference to Appendix G for further comparisons cannot be evaluated since the appendix is stripped."** Removed per hard rule. The concern about missing full-system baselines is retained as a Nice-to-Have.
- **Harsh Critic: missing unimodal LT-TTA baselines (SAR, DELTA, LAME).** The paper does test SAR in Figure 1b.2 and explicitly positions itself as distinct from unimodal TTA. Moved to Nice-to-Haves.
- **Harsh Critic: per-imb-ratio results for Table 2 should be in main text.** Moved to Nice-to-Haves.
- **Harsh Critic: efficiency metrics concern.** The paper includes Table 4 with detailed time and memory comparisons. Removed.
- **Strength Finder "CRA as creative adaptation of load-balancing":** The mechanism is creative and empirically validated, but the causal rationale is indirect (see Minor weakness).

## Novel Insights
The paper offers the insight that standard entropy minimization in TTA systematically disadvantages tail classes under long-tailed distributions, and that simply adding class-prior corrections may not fix this because EM's gradient structure differs from supervised cross-entropy — the BEM design (confidence-gating the prior correction) is a clean and effective response to this observation. Additionally, the identification that text-embedding biases create "rich classes" that amplify tail erosion independently of visual frequency is a genuinely novel diagnostic for VLM-based TTA.

## Suggestions
- Add explicit assumptions to Proposition 1 (e.g., "assuming the model's predicted class distribution sufficiently reflects empirical class frequency during adaptation") so the claim's scope is clear from the main text alone.
- Include a DPE + logit adjustment baseline to directly test the paper's claim that simpler LT corrections are insufficient.
- Clarify whether long-tailed sampling is applied within each dataset's available classes or mapped to the full ImageNet label space.
- Discuss or correct the MTA ImageNet-A anomaly in Table 1.
- Sharpen the EP rationale: explain concretely why updating prototypes with improbable features helps tail-class discrimination rather than homogenizing the prototype space.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| BLG (long-tailed CLIP) | 4.67 | R1 | Our paper is clearly stronger — TTA setting is more challenging, more comprehensive experiments, clearer motivation |
| PROGRAM (prototype TTA) | 6.20 | R1 | Our paper is somewhat stronger — broader scope (15 datasets, 5 backbones), addresses an underexplored problem |
| DOTA (distributional TTA VLMs) | 6.00 | R2 | Our paper is clearly stronger — more novel components, more comprehensive evaluation, fewer methodology gaps |
| Multi-Label TTA BEM | 6.25 | R2 | Our paper is comparable or slightly stronger — broader scope, more components |
| CLIP Reward TTA | 6.67 | R2 | Our paper is comparable — broader evaluation vs. cleaner single-idea contribution |
| MLLM Concept Drift | 7.00 | R2 | Our paper is slightly weaker — less theoretical depth, no new dataset, but more focused evaluation |
| READ (multi-modal TTA) | 8.00 | R1 | Our paper is clearly weaker — READ has deeper analysis, constructs new benchmarks, stronger reviewer consensus |

The paper sits between DOTA (6.00) and MLLM Concept Drift (7.00), with comparable scope to CLIP Reward TTA (6.67). The weaknesses are genuine but minor — they do not undermine the core empirical contribution. The evaluation is comprehensive and the method's components are well-ablated.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>