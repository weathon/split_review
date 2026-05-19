## Summary
# Final Review Report

## Summary

This paper introduces a synthetic graph navigation task on directed acyclic graphs (DAGs) to study stepwise inference in transformers—the mechanism underlying chain-of-thought and scratchpad prompting. The authors train a small GPT-style transformer to navigate from a start node to a goal node in either a hierarchical or random DAG, then analyze the conditions under which stepwise (path-producing) inference outperforms direct classification, and how in-context exemplars can steer the generated path.

**Core contributions:**
- **C1 — Stepwise Inference Gap:** The paper demonstrates that stepwise inference yields higher path-connectedness accuracy than direct classification, especially in hierarchical graphs and when training paths are shorter than evaluation paths. This is attributed to a "stitching" mechanism where the model recombines sub-paths from training.
- **C2 — In-Context Steering:** Using multiple connected subgraphs ("motifs"), the paper shows that in-context exemplars can steer the model to follow specific motif chains, with compositional generalization up to the length seen in training and a bias toward the first exemplar under conflict.

**Strengths:** The synthetic framework is well-motivated, clean, and enables controlled experimentation on variables that are confounded in large-scale LLM studies. The stitching experiment (Fig. 3c) is a particularly insightful demonstration. The explicit disclaimer about limited transferability to large models shows intellectual honesty.

**Key weaknesses:** (1) The term "mechanistic understanding" in the title overclaims—the paper provides behavioral/phenomenological characterization, not circuit-level mechanism analysis. (2) The stitching claim lacks direct evidence (no path-decomposition analysis, no causal attribution). (3) The in-context steering experiments lack statistical rigor and confound controls. (4) The related-work section is a chronological list lacking structured comparison with prior synthetic frameworks. (5) The conclusion is too short and generic. (6) Novelty cannot be fully assessed without external literature verification (deferred due to Retrieval-Disabled Mode).

**Overall assessment:** A solid synthetic study with interesting insights, but the experimental evidence is thinner than the claims warrant. The paper would benefit from tighter claim-evidence alignment, additional control experiments, and a more cautious framing of what constitutes "mechanistic understanding."

## Strengths
1. **Well-motivated synthetic framework:** The DAG navigation task is clean, controllable, and maps naturally to the notion of stepwise computation. The three control knobs (graph structure, training data properties, inference parameters) are genuinely useful for isolating causal factors that are entangled in large-scale LLM studies.

2. **Stitching experiment insight:** The finding that the stepwise inference gap increases when training paths are shorter (Fig. 3c) is the paper's most compelling result. It provides a specific, testable prediction about when stepwise inference should help: when the model must recombine familiar sub-paths into novel longer paths. This insight has direct implications for understanding why chain-of-thought works in compositional reasoning tasks.

3. **Diversity-accuracy tradeoff quantification:** Measuring diversity against known ground-truth path diversity (Fig. 4) is a novel methodological contribution. The non-monotonic relationship between unique true paths and temperature suggests an optimal sampling regime, which is practically relevant.

4. **Explicit scope disclaimer:** The model-experimental systems approach paragraph (Page 3) honestly acknowledges the limitations of generalizing from a small synthetic model to large-scale LLMs. This intellectual honesty strengthens the paper's credibility, though the current phrasing is too broad (as noted in weaknesses).

5. **Reproducibility-oriented appendix:** The appendix includes DAG generation algorithms (pseudocode), hyperparameter table, model architecture diagram, and training protocol details. This makes the experiments reproducible, which is a significant strength for a synthetic study.

6. **Connections to established LLM phenomena:** The paper draws parallels between its findings and known LLM behaviors (prompt order sensitivity, lost-in-the-middle, shortcut solutions), helping ground the synthetic results in real-model phenomena even without direct validation.

## Weaknesses
Ranked by severity and impact on paper validity/value.

### W1 [Major]: Title Overclaims "Mechanistic Understanding" (Page 1)
The title promises a "mechanistic understanding" of stepwise inference, but the paper delivers behavioral/phenomenological characterization using an analogical synthetic task. No internal model representations (attention patterns, hidden states, circuit-level analysis) are examined. The term "mechanistic" sets expectations the paper does not meet, which will harm its reception among reviewers expecting causal mechanism identification.

### W2 [Major]: Stitching Claim Lacks Direct Evidence (Page 6-7)
The central claim that the stepwise inference gap arises from "stitching together sub-paths" is supported only by aggregate accuracy curves (Fig. 3c) and a schematic (Fig. 3d). Missing controls: (a) no separation between path-length diversity and sub-path composition diversity, (b) no path-decomposition analysis verifying that generated paths actually recombine training sub-sequences, (c) results from a single graph instantiation per setting. The stitching mechanism remains a plausible hypothesis, not a demonstrated finding.

### W3 [Major]: In-Context Steering Experiments Lack Statistical Rigor (Page 8-9)
Contribution 2 (steerability) is supported by single-example demonstrations (Fig. 6e) and limited parametric sweeps. The "number of intermediate motifs" experiment (Fig. 7a) confounds chain length with token sequence length. The first-chain bias (Fig. 7b) is not tested for sensitivity to relative chain length or position. No confidence intervals, error bars, or multi-seed statistics are reported for these experiments.

### W4 [Major]: Related Work is a Chronological List (Page 3-4)
The related-work section summarizes papers one-by-one without structured comparison axes. The paper does not explicitly differentiate itself from the closest synthetic frameworks (Prystawski & Goodman 2023, Li et al. 2023, Feng et al. 2023). Readers cannot easily identify the paper's incremental contribution relative to existing synthetic studies.

### W5 [Moderate]: Overly Broad Scope Disclaimer (Page 3)
The disclaimer states findings "should not be taken as definitive conclusions directly applicable to large-scale generative models." This is so broad that it undermines the paper's contribution. Instead of a blanket disclaimer, specify concrete boundary conditions for each finding.

### W6 [Moderate]: Diversity-Accuracy Novelty Overclaim (Page 7)
The claim that the diversity-accuracy tradeoff "has not been quantitatively studied before" is contradicted by the paper's own citation (Zhang et al., 2020). The novelty lies in the synthetic ground-truth setting, not in the tradeoff itself.

### W7 [Moderate]: Conclusion is Too Short and Generic (Page 9)
The one-paragraph conclusion does not consolidate findings, bound limitations, or propose specific next steps. It reads as a placeholder rather than a synthesis.

### W8 [Minor]: Path Count Formula Oversimplification (Page 5)
The expected path count formula $(pN)^{l'-l}$ overcounts for sparse graphs (p<1). The formula is valid only in the dense limit and should be qualified.

### W9 [Minor]: Loss Function Parameter β Underspecified (Page 15, Appendix)
Equation (1) includes a temperature parameter β whose value or learning status is not specified, affecting reproducibility.

### W10 [Minor]: Shorter-Path Bias Alternative Explanations Not Explored (Page 7)
The shorter-path bias observation does not distinguish between genuine length minimization, node-frequency bias, or evaluation-distribution effects.

## Key Issues
### Issue 1: Title-label mismatch — "Mechanistic Understanding" is not delivered
**Location:** Page 1 — Title  
**Severity:** Major  
**Evidence:** The paper examines output-level behavior (accuracy, path length, diversity) in a synthetic analog; no internal model representations, attention patterns, or causal interventions are analyzed.  
**Risk:** The title sets an expectation of mechanism-level insight that the paper does not fulfill, potentially leading to rejection or major revision requests.  
**Fix:** Retitle to use "Phenomenological Characterization" or add genuine mechanistic analysis (attention probing, representational analysis, causal intervention).

### Issue 2: Stitching mechanism is a hypothesis, not a demonstrated finding
**Location:** Page 6-7 — Stitching of paths paragraph  
**Severity:** Major  
**Evidence:** The experiment varies training path length (Δ) and observes accuracy changes, but does not directly verify that generated paths recombine training sub-segments. No path-decomposition analysis, no causal control for data diversity vs. stitching.  
**Risk:** The paper's most novel claim (C1) rests on correlational evidence. If the stitching mechanism is questioned, the paper's core insight collapses.  
**Fix:** Add path-decomposition analysis (measure fraction of generated sub-sequences present in training data) and a control experiment that varies training path diversity independently of path length.

### Issue 3: Contribution 2 experiments lack statistical credibility
**Location:** Page 8-9 — Multi-graph scenarios  
**Severity:** Major  
**Evidence:** Single-example demonstrations (Fig. 6e), no confidence intervals, no multi-seed statistics, confound between chain length and token length in Fig. 7a.  
**Risk:** The second contribution (steerability) is presented as a core finding but its experimental basis is too thin to be publication-ready.  
**Fix:** Run experiments with >5 random seeds, >20 random prompt configurations per condition, report means ± std, and add a control experiment decoupling chain length from token count.

### Issue 4: Related work lacks structured positioning
**Location:** Page 3-4 — Related Work section  
**Severity:** Major  
**Evidence:** The section lists findings chronologically rather than organizing by comparison axes. No explicit differentiation from Prystawski & Goodman (2023), who also study stepwise inference in synthetic transformers.  
**Risk:** Readers and reviewers cannot readily assess the paper's novelty relative to the closest prior work.  
**Fix:** Reorganize by 3-4 thematic axes (theoretical vs empirical, synthetic vs real-task, mechanism-level vs behavior-level) with explicit "difference from this paper" statements.

## Actionable Suggestions
### S1 [Must]: Retitle to match content
Replace the current title with one that accurately reflects the paper's nature. Two candidates:
- "TOWARD A PHENOMENOLOGICAL CHARACTERIZATION OF STEPWISE INFERENCE IN TRANSFORMERS: A SYNTHETIC GRAPH NAVIGATION MODEL"
- "A SYNTHETIC GRAPH NAVIGATION FRAMEWORK FOR STUDYING STEPWISE INFERENCE IN TRANSFORMERS"

**Rationale:** The current title overclaims "mechanistic understanding." The paper provides behavioral characterization and mechanistic hypotheses, not mechanism-level evidence.

### S2 [Must]: Add direct evidence for the stitching mechanism
**Experiment:** Perform a path-decomposition analysis. For each generated test path, decompose it into all contiguous sub-segments of length k (for k=2,3,4). Measure what fraction of these sub-segments appeared in the training set. If the stitching hypothesis is correct, the fraction should be high (e.g., >70%). Include a control: compare against a random path generator.

**Expected result:** If stitching is the mechanism, >70% of length-2 and >50% of length-3 sub-segments should match training data. Report this as a table with 95% confidence intervals across 1000 test paths.

### S3 [Must]: Decouple confounds in the stitching experiment
**Experiment:** Add a control where training paths are kept short (Δ=2) but the number of unique training paths is increased to match the diversity of training with longer paths (Δ=4). If the stepwise inference gap disappears when diversity is matched, the effect is about data diversity, not stitching specifically.

### S4 [Must]: Add statistical rigor to Contribution 2 experiments
- Run all multi-graph experiments with ≥5 random seeds and ≥20 random prompt configurations per condition.
- Report means, standard deviations, and individual data points.
- For the "number of intermediate motifs" experiment (Fig. 7a), add a control condition where the total token length is held constant by padding shorter chains with filler tokens.
- For the first-chain bias experiment (Fig. 7b), test whether the bias reverses when the second chain is shorter (fewer tokens) or when it appears first in the prompt.

### S5 [Must]: Restructure Related Work by comparison axes
Reorganize the related-work section into 3-4 thematic categories:
1. **Theoretical synthetic studies** (Li et al., 2023; Feng et al., 2023; Prystawski & Goodman, 2023) — state what each shows and how your DAG framework differs.
2. **Large-scale empirical studies** (Dziri et al., 2023; Momennejad et al., 2023; Saparov & He, 2023) — state how your controlled setting complements these.
3. **Prompting phenomenology** (Turpin et al., 2023; Lu et al., 2021; Wang et al., 2022a) — state which phenomena your framework can/cannot address.
4. **Scratchpad and intermediate computation** (Nye et al., 2021; Kojima et al., 2022) — connect to your two-level computation framing.

### S6 [Nice-to-have]: Replace blanket disclaimer with specific boundary conditions
Replace "observations should not be taken as definitive conclusions directly applicable to large-scale generative models" with specific boundaries per finding. Example: "The stitching effect was demonstrated on a 2-layer, 64-dim transformer with 200-node DAGs. Whether this effect generalizes to larger models or natural-language tasks is an open question that our framework is designed to test."

### S7 [Nice-to-have]: Clarify the path count formula
Add a clarifying sentence: "The expression $(pN)^{l'-l}$ is an upper bound in the dense limit; actual expected counts are lower for p < 1 and are reported empirically in Appendix Fig. 9."

### S8 [Nice-to-have]: Specify β in the loss function
State explicitly: "We set β = 1 (standard cross-entropy without additional temperature scaling)." Or if β is learned, report its initial and final values.

### S9 [Nice-to-have]: Expand conclusion to three parts
Restructure as: (a) Validated findings with explicit evidence anchors, (b) Bounded limitations per finding, (c) Prioritized next steps for validation in larger models.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current narrative arc is:
1. LLMs show remarkable capabilities through stepwise inference (P1, Page 1)
2. We ask four questions about stepwise inference mechanisms (P1, Page 1)
3. We propose a DAG navigation framework (P2, Pages 2-3)
4. Contributions: Stepwise gap + steerability (P3, Page 3)
5. Related work (P4, Pages 3-4)
6. Data generation process (P5, Pages 4-5)
7. Results on single-graph: gap, stitching, diversity-accuracy, bias, failures (P6-7, Pages 5-7)
8. Results on multi-graph: in-context steering (P8-9, Pages 8-9)
9. Conclusion (P9)

**Strengths:** The problem-motivation-solution- results structure is standard and functional. The separation into single-graph (zero-shot) and multi-graph (few-shot) settings is logical.

**Weaknesses:** (1) The introduction lists four questions but doesn't build a compelling "missing piece" case before listing them. (2) The related work interrupts the flow between motivation and method. (3) Contributions are presented before readers have seen the technical setup. (4) The conclusion does not re-engage with the four questions.

### Selected Best Storyline (Revision Target)

**Abstract Outline (4-5 sentences):**
- S1 (Problem): "Large language models benefit from stepwise inference (chain-of-thought, scratchpad), yet the mechanisms enabling this advantage remain poorly understood."
- S2 (Gap): "A key obstacle is the lack of controllable settings where training data, task structure, and inference parameters can be independently varied to isolate causal factors."
- S3 (Solution): "We introduce a synthetic DAG navigation task where a transformer must autoregressively produce paths connecting start and goal nodes, enabling independent control of graph structure, training data properties, and sampling parameters."
- S4 (Key Results): "Using this framework, we reproduce and characterize several phenomena — including a stepwise inference gap that increases with graph hierarchy and shorter training paths, a diversity-accuracy tradeoff with optimal sampling temperature, and in-context steering of path selection — and show these arise from a sub-path stitching mechanism."
- S5 (Bounded Implication): "These findings provide testable hypotheses about stepwise inference mechanisms and establish a minimal synthetic testbed for future investigations of larger models."

**Introduction Outline (paragraph-by-paragraph):**

**P1 (Role: Problem & Gap):** "Large language models demonstrate remarkable reasoning capabilities through stepwise inference (chain-of-thought, scratchpad). Despite extensive study, the mechanisms underlying this advantage remain unclear because existing work operates at scales where training data, task structure, and model internals cannot be independently controlled." → Transition: "This lack of controllability makes it difficult to answer four fundamental questions: [list four questions from current paper]."

**P2 (Role: Solution & Framework intuition):** "To address these questions, we introduce a synthetic graph navigation task on directed acyclic graphs (DAGs). The task captures two essential components of stepwise reasoning: local step validity and global path planning. Our framework provides three control knobs: graph structure, training data composition, and inference parameters." → Briefly describe the task.

**P3 (Role: Results preview & Contribution 1):** "Using this framework, we first demonstrate a stepwise inference gap: producing intermediate steps improves path-connectedness classification, especially in hierarchical graphs and when training paths are short. We provide evidence that this gap arises from a sub-path stitching mechanism." → Briefly describe the stitching finding.

**P4 (Role: Results preview & Contribution 2):** "Extending to multi-graph settings, we show that in-context exemplars can steer the model's path selection, with capabilities and biases that mirror those observed in large-scale LLMs—including compositional generalization up to training length and a first-exemplar bias under conflict."

**P5 (Role: Contribution summary & paper roadmap):** "In summary, our contributions are: (1) a minimal synthetic framework for studying stepwise inference with controlled variables, (2) quantitative characterization of the stepwise inference gap and its dependence on graph structure and training data, (3) mechanistic evidence for the sub-path stitching hypothesis, (4) systematic analysis of in-context steering capabilities and limitations." → End with roadmap: "Section 2 discusses related work, Section 3 describes the framework, Section 4 presents single-graph results, Section 5 covers multi-graph steering, and Section 6 concludes with bounded implications."

### Alternative Storyline: Hypothesis-driven framing
Lead with the stitching hypothesis as the central claim:
- P1: Stitching is hypothesized mechanism for stepwise inference
- P2-3: Using DAG framework, derive predictions from stitching hypothesis
- P4: Test predictions experimentally
- P5: Additional findings (diversity-accuracy, bias, in-context steering)
This structure foregrounds the mechanism rather than the framework, making the paper more hypothesis-driven.

## Priority Revision Plan
Ordered by impact on paper quality and publication readiness.

### P0: Publication-Critical (Must Fix)

| Priority | Action | Effort | Impact | Section |
|----------|--------|--------|--------|---------|
| P0.1 | Retitle to match content | Low | High | Title |
| P0.2 | Add path-decomposition analysis for stitching evidence | Medium | High | Section 4 |
| P0.3 | Decouple confounds in stitching experiment (data diversity vs path length) | Medium | High | Section 4 |
| P0.4 | Add statistical rigor to Contribution 2 (≥5 seeds, error bars, confound control) | Medium | High | Section 5 |
| P0.5 | Restructure Related Work by comparison axes | Low | Medium | Section 2 |

### P1: High Priority (Should Fix)

| Priority | Action | Effort | Impact | Section |
|----------|--------|--------|--------|---------|
| P1.1 | Replace blanket disclaimer with specific boundary conditions | Low | Medium | Page 3 |
| P1.2 | Qualify the diversity-accuracy "first study" claim | Low | Medium | Section 4 |
| P1.3 | Expand conclusion to three parts (findings, limits, next steps) | Low | Medium | Section 6 |

### P2: Quality Improvement (Nice to Fix)

| Priority | Action | Effort | Impact | Section |
|----------|--------|--------|--------|---------|
| P2.1 | Clarify path count formula with bound qualification | Low | Low | Section 3.1 |
| P2.2 | Specify β parameter in loss function | Low | Low | Appendix A.2 |
| P2.3 | Add alternative explanation analysis for shorter-path bias | Medium | Low | Section 4 |

### Revision Sequencing

```text
[Stage 1 — Text revisions only (this week)]
Retitle
Restructure Related Work
Rewrite conclusion
Qualify diversity-accuracy claim
Replace blanket disclaimer
Clarify formula and β

[Stage 2 — New analyses using existing data (1-2 weeks)]
Path-decomposition analysis
Decoupled confound analysis (if data exists)
Seed-level variance reporting

[Stage 3 — New experiments (2-4 weeks)]
Deconfound chain length vs token count (Section 5)
First-chain bias sensitivity tests
Multi-graph experiments with >5 seeds

[Expected impact after P0 fixes]
Evidence gap for stitching: HIGH → MEDIUM
Contribution 2 credibility: LOW → MEDIUM
Related work positioning: LOW → HIGH
Title-claim alignment: HIGH
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|----------------------------|---------|--------------|-----------------|-------------------|
| E1 | Stepwise vs direct inference accuracy comparison | Random DAG (N=200, p=0.05), train on 20% node pairs | Path/no-path classification accuracy | Stepwise > direct; gap ~15% | C1 | Single graph instantiation; no error bars |
| E2 | Same as E1 but on hierarchical DAG | Hierarchical DAG (L=10, N_per_layer=20, p=0.05) | Same as E1 | Gap larger (~30%) vs random | C1 | Single instantiation; no error bars |
| E3 | Effect of training path length (Δ) on stepwise gap | Hierarchical DAG, vary Δ={2,3,4} | Accuracy vs training step | Smaller Δ → larger gap | C1 (stitching) | Confounds data diversity with path length |
| E4 | Diversity-accuracy tradeoff with temperature | Single (nstart, ngoal) pair, 3000 samples, sweep T∈[0,3] | Accuracy, #unique paths, #unique true paths | Non-monotonic optimal T ~0.5-1.0 | C1 (diversity) | Single node pair; diversity conflates topological vs token-level variation |
| E5 | Shorter-path bias | Random DAG, compare true vs generated path lengths | Average path length | Generated paths shorter | C1 (bias) | Doesn't isolate frequency bias vs length preference |
| E6 | Failure mode dynamics (edge vs planning accuracy) | Random DAG, measure over 100 training steps | Edge accuracy, planning accuracy | Edge accuracy saturates first | C1 (failure modes) | Correlational; 3 seeds only |
| E7 | In-context steering of motif paths | Multi-graph with ghost edges, single example path | Qualitative path following | Model follows exemplar chain | C2 | Single example; no statistics |
| E8 | Number of intermediate motifs | Vary K=1..6 intermediate motifs, measure success | Steering success probability | Success up to K=4 (training max) | C2 | Confounds chain length with token count |
| E9 | First-chain bias under conflict | Two conflicting chains provided | Fraction choosing chain 1 vs 2 | Strong bias toward first chain (70-80%) | C2 | No sensitivity analysis for relative chain length |

### Research-Theme Gap Diagnosis

- **New knowledge (partial):** The stitching hypothesis and its dependence on training path length is genuinely novel. However, it remains a hypothesis due to missing direct evidence (no path decomposition, no causal attribution).
- **Reproducibility (good):** The appendix provides DAG generation algorithms, hyperparameters, and prompt formats. The loss function has an underspecified parameter (β), and single-seed results limit reproducibility confidence.
- **Potential to change practice/understanding (partial):** If confirmed, the stitching mechanism would provide a concrete explanation for when chain-of-thought helps. However, the paper does not demonstrate that the findings transfer to real LLMs or natural-language reasoning tasks.

### Proposed Research Experiments

#### P0 Experiments (Must-do for publication)

**R1: Path-Decomposition Analysis**
- **Target Claim:** C1 — Stitching mechanism
- **Hypothesis:** Generated test paths are composed primarily of sub-segments that appeared in training data.
- **Minimal Design:** Decompose 1000 generated test paths into contiguous sub-segments of length k∈{2,3,4}. For each sub-segment, check membership in the training path database.
- **Controls:** Compare against (a) random path generator, (b) shortest-path heuristic.
- **Metrics:** Fraction of sub-segments matching training data; mean ± std over 5 graph seeds.
- **Success Criterion:** >70% of length-2 and >50% of length-3 sub-segments match training data, significantly above controls.
- **Estimated Cost:** 1-2 days (computational analysis of existing model outputs).
- **Expected Gain:** Converts "stitching hypothesis" into "stitching evidence."

**R2: Confound Control for Stitching Experiment**
- **Target Claim:** C1 — Path length effect
- **Hypothesis:** The stepwise inference gap depends on path length specifically, not on data diversity.
- **Minimal Design:** Fix Δ=2 (short training paths) but oversample to match the total unique path count of the Δ=4 condition. Test whether the gap persists.
- **Controls:** Compare standard Δ=2, Δ=4, and oversampled Δ=2 conditions.
- **Metrics:** Classification accuracy gap between stepwise and direct inference.
- **Success Criterion:** Gap in oversampled Δ=2 remains similar to standard Δ=2, confirming path-length effect.
- **Estimated Cost:** 2-3 days.
- **Expected Gain:** Strengthens causal interpretation of the central finding.

**R3: Statistical Rigor for Multi-Graph Experiments**
- **Target Claim:** C2 — Steering
- **Design:** Run all steering experiments (E7-E9) with ≥5 random seeds, ≥20 random motif configurations per condition.
- **Metrics:** Mean success rate ± std, with individual data points.
- **Success Criterion:** All effects remain significant with consistent direction.
- **Estimated Cost:** 3-5 days.
- **Expected Gain:** Transforms Contribution 2 from demonstration to quantitative evidence.

#### P1 Experiments (Highly Recommended)

**R4: Decouple Chain Length from Token Count (Fig. 7a)**
- Add a control where total token length is held constant by padding shorter chains.
- Tests whether the performance drop at K>4 is due to chain length or absolute token count.
- **Estimated Cost:** 2-3 days.

**R5: First-Chain Bias Sensitivity Analysis**
- Vary relative lengths of the two conflicting chains, and swap their order.
- Tests whether the bias is robust or depends on length/position.
- **Estimated Cost:** 1-2 days.

#### P2 Experiments (Nice-to-have)

**R6: Node Frequency Control for Shorter-Path Bias**
- Stratify path lengths by whether they use high-frequency or low-frequency nodes.
- Separates frequency bias from genuine length minimization.
- **Estimated Cost:** 1-2 days.

**R7: Causal Test of Failure Mode Dynamics**
- Artificially impair local edge accuracy via masking at inference time, observe planning accuracy.
- Tests whether planning causally depends on local edge knowledge.
- **Estimated Cost:** 2-3 days.

```text
ASCII Diagram — Experiment Upgrade Plan

                         ┌─────────────────────────────────────┐
                         │          CURRENT PAPER              │
                         │   Evidence Level: Behavioral +      │
                         │   Correlational                     │
                         └──────────┬──────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
            ┌────────────┐  ┌────────────┐  ┌────────────┐
            │  P0: Core  │  │  P1: Strengthen│  │  P2: Explore│
            │  Validity  │  │  Robustness │  │  Depth     │
            └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
                  │               │               │
    ┌─────────────┼─────────────┐ │               │
    ▼             ▼             ▼ ▼               ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│R1: Path│ │R2: De- │ │R3:     │ │R4: De- │ │R6: Freq│
│Decomp  │ │confound│ │Multi-  │ │couple  │ │Control │
│Analysis│ │ Control│ │Seed    │ │Token   │ │   +    │
│        │ │        │ │Rigor   │ │Length  │ │R7:Causal│
└────────┘ └────────┘ └────────┘ └────────┘ └────────┘
   HIGH       HIGH       HIGH      MEDIUM     MEDIUM
  IMPACT     IMPACT     IMPACT     IMPACT     IMPACT
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper presents a well-motivated synthetic framework with interesting preliminary findings, but several major weaknesses prevent a higher score. The central claim (stitching mechanism) lacks direct evidence and remains a hypothesis. The second contribution (steerability) is supported by thin experimental evidence without statistical rigor. The title overclaims relative to content. Novelty cannot be fully verified without external literature access, which is deferred. On the positive side, the framework is clean and potentially impactful, the stitching experiment (Fig. 3c) is insightful, and the appendix ensures reproducibility.

**Scoring breakdown:**
- **Research value / Contribution (primary):** 5/10 — The synthetic framework has value, but the core mechanistic claim is unsubstantiated and Contribution 2 lacks rigor.
- **Novelty (primary):** 4/10 — Deferred due to Retrieval-Disabled Mode; internal assessment suggests partial overlap with existing synthetic studies (Prystawski & Goodman 2023).
- **Validity / Soundness:** 5/10 — Results are plausible but key claims lack causal evidence and confound controls.
- **Reproducibility:** 7/10 — Good appendix details, minus the underspecified β parameter and single-seed results.
- **Writing / Presentation:** 5/10 — Title overclaims, related work is a list, conclusion is too short.

**Post-Revision Target: [6.5, 7.5] / 10**

**Conditions for achieving target:** All P0 items must be addressed: (1) retitle, (2) add path-decomposition evidence for stitching, (3) decouple confounds in stitching experiment, (4) add statistical rigor to Contribution 2 experiments, (5) restructure related work. With these fixes, the paper becomes a solid empirical study whose limitations are honestly bounded rather than undermining its contributions.