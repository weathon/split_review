## Summary
# Final Review Report

## Summary

This paper proposes **Cyclic Neural Networks (Cyclic NN)**, a neural network design paradigm that relaxes the Directed Acyclic Graph (DAG) constraint by allowing arbitrary graph structures—including cycles—between computational neurons. The authors introduce **Graph Over Multi-Layer Perceptron (GOMLP)**, an instantiation using 4 linear-layer "computational neurons" connected via various graph topologies (chain, cycle, Watts-Strogatz, Barabási-Albert, complete), trained with the Forward-Forward (FF) algorithm [Hinton, 2022] for local optimization.

The conceptual contribution—questioning the necessity of the DAG constraint and demonstrating that cyclic structures are trainable with local losses—is interesting and provocative. However, the current manuscript suffers from **significant claim-evidence misalignment**: the experiments are limited to 4-neuron networks on three small-scale classification benchmarks (MNIST, NewsGroup, IMDB), with comparisons only against tiny MLP baselines, yet the paper repeatedly uses language such as "transformative," "major shift," "superiority over current DAG networks," and "totally new way of building ANNs." The mathematical formulation has unresolved issues (goodness function using ReLU is not a probability, causing log(0) risk; complexity analysis double-counts operations), and the related work section reads as a list without the critical comparisons to RNNs and GNNs needed to establish novelty positioning.

**Core strength:** The core idea—that localized training (FF) combined with flexible graph topologies can overcome the DAG constraint—is genuinely interesting and could open a new design axis for neural architectures.

**Core weakness:** The evidence base (tiny architectures, small datasets, weak baselines, no parameter count control) is insufficient to support the sweeping claims made throughout the paper. The novelty positioning against RNNs and GNNs is buried in the appendix rather than stated clearly in the main text.

## Strengths
1. **Provocative and important research question.** The paper asks a fundamental question — "Do we really need to stack neural networks layer-by-layer?" — that has been largely overlooked in the deep learning community. Questioning the DAG constraint opens a potentially fruitful design space for neural architectures, and the paper deserves credit for raising this question in a concrete, testable way.

2. **Clean conceptual framework.** The three-component design (computational neurons, synapses, local optimization) provides a clear vocabulary for thinking about non-DAG neural networks. The biological analogy is appropriately motivated (though it could be tightened), and the distinction between local and global learning is well-articulated.

3. **Systematic graph topology comparison.** The paper tests multiple graph generators (chain, cycle, WS, BA, complete) under controlled conditions (same training algorithm FF, same number of neurons), providing a clean ablation of how connectivity density affects performance. The finding that denser graphs (WS, BA, Complete) outperform chain graphs is internally consistent and provides useful empirical guidance.

4. **Training curve stability.** The appendix shows that training curves (FF loss, classifier loss, error rate) are stable across all graph structures and datasets, demonstrating that localized optimization with cyclic graphs does not cause training collapse — a non-trivial empirical finding.

5. **Reproducibility effort.** The paper reports 20 random seeds, mean and variance, and provides an anonymous code repository. The hyperparameter tuning ranges (learning rate, weight decay, early stopping) are specified, which is commendable.

## Weaknesses
The weaknesses below are ordered by severity (highest first).

1. **Severe claim-evidence mismatch (Critical).** The paper's language ("transformative," "major shift," "totally new way," "superiority over current DAG neural networks") dramatically overstates what is supported by the experiments. The evidence comes from 4-neuron networks on three small datasets (MNIST, NewsGroup, IMDB), compared only against tiny chain-MLP baselines. There are no comparisons against modern architectures (ResNet, Transformer), no large-scale experiments, no parameter-count-controlled ablations, and no OOD/robustness tests. This mismatch undermines the paper's scientific credibility.

2. **Insufficient empirical baselines (Major).** BP-Chain* — described as "the current default way of building and training ANNs" — is a 4-neuron chain MLP. Modern deep learning uses networks with millions of parameters. The claim "first FF-trained model to outcompete BP" is therefore only valid against a toy baseline. Without comparisons to stronger BP-trained models (e.g., deeper MLPs, ResNet on MNIST, fine-tuned BERT for text), the superiority claim is unsupported.

3. **No parameter count control (Major).** The paper keeps "4 computation neurons" constant but does not control for the total number of parameters. In FF-Complete, each neuron receives concatenated outputs from all other neurons, making its input dimension and parameter count much larger than in FF-Chain. The observed gains may be attributable to increased model capacity rather than the cyclic graph structure.

4. **Mathematical issue in goodness function (Major).** The goodness score p(h) = ReLU(sum(h^2) - θ*d(h)) produces values in [0, ∞), not in [0,1]. The loss LN then takes log(p(·)), which can be undefined (log(0)) when ReLU outputs 0. Additionally, the loss is called "binary cross-entropy" but its form (-log(p_pos) + log(p_neg)) is not standard BCE, which requires -[y log(p) + (1-y) log(1-p)]. This mathematical inconsistency needs correction.

5. **Complexity analysis double-counts (Major).** The analysis claims O(T*|E|*|V|) for training, but edge traversal O(T*|E|) already includes neuron activation. The additional O(|V|) factor per cycle appears to double-count. The claim that "asynchronous parallel update reduces to O(|E|)" lacks a formal parallel computation model (e.g., PRAM) and is misleading without specifying assumptions about processors.

6. **Related work is a flat list (Major).** Sections 5.1 and 5.2 list method families chronologically without structured comparison. Critical positioning statements — why Cyclic NN differs from RNNs (BPTT/unrolling) and GNNs (graph as input vs. graph as model) — are relegated to Appendix A.4. Without these in the main text, readers cannot assess the paper's novelty.

7. **Weak conclusion (Major).** The conclusion introduces new unsupported claims ("various datasets," "major shift," "transformative design") and does not discuss any limitations. An honest conclusion should bound the claims to the tested conditions and outline clear next steps.

8. **Label leakage risk unaddressed (Minor).** The fusion function concatenates the label into the input for positive samples, creating a potential shortcut where neurons could learn to copy label information rather than extract meaningful features. This is a known concern with the FF algorithm that should be discussed.

9. **Graph generator parameters underspecified (Minor).** For WS and BA graphs, the paper does not specify the graph construction parameters (k-neighbors, rewiring probability, m-edges per node), making the results not fully reproducible.

## Key Issues
### Issue 1 (Critical): Claim-Evidence Mismatch and Overclaiming
**Evidence Anchor:** Page 1 - Abstract (lines 53-67), Page 9 - Results Summary (lines 107-110), Page 10 - Conclusion (lines 87-92)

The paper uses language such as "transformative," "superiority over current DAG neural networks," "first to beat BP," "major shift in ANN design," and "totally new way of building ANNs." These claims are not supported by the experimental evidence, which is limited to:
- 4 computational neurons (tiny architecture)
- 3 small datasets (MNIST, NewsGroup, IMDB)
- No comparisons with modern architectures (ResNet, Transformer, BERT)
- No parameter count control across graph topologies
- No statistical significance tests

**Impact:** This overclaiming undermines the paper's scientific credibility and would be flagged by reviewers as a critical flaw. The paper has an interesting core idea, but the presentation inflates its demonstrated value.

**Fix:** Rewrite abstract, results summary, and conclusion with bounded, evidence-grounded claims. See specific rewrite suggestions in annotations and in the Actionable Suggestions section below.

### Issue 2 (Major): Goodness Function and Loss Definition Error
**Evidence Anchor:** Page 6 - Section 3.4.1 (lines 59-72)

The goodness score p(h) = ReLU(Σ h²_i - θ·d(h)) produces values in [0, ∞), not in [0,1]. Taking log(p(h)) risks log(0) when the ReLU output is 0. The loss is called "binary cross-entropy" but the formula -[log(p_pos) - log(p_neg)] is not the standard BCE form.

**Impact:** This is a mathematical error that could affect optimization dynamics and reproducibility. If the implementation uses a sigmoid instead of ReLU (as Hinton 2022 may have), the text is wrong; if it uses ReLU as stated, the training could be numerically unstable.

**Fix:** Use sigmoid(Σ h²_i - θ·d(h)) to produce a (0,1)-bounded score, then use standard BCE, or keep ReLU but add a small epsilon and rename the loss to "contrastive log-loss."

### Issue 3 (Major): Complexity Analysis Errors
**Evidence Anchor:** Page 7 - Section 3.5 (lines 67-85)

The analysis double-counts operations (O(T·|E|) already covers neuron updates via edge traversal; adding O(|V|) per cycle is redundant). The parallel speedup claim lacks a formal model.

**Impact:** Inflated complexity claims could mislead readers about the method's efficiency. The actual complexity for a complete graph with |V| neurons is O(T·|V|²·d²), which is significantly higher than the O(|V|·d²) of a standard MLP.

**Fix:** Provide a corrected complexity analysis with clear assumptions about sequential vs. parallel execution.

### Issue 4 (Major): Insufficient Baselines and Lack of Parameter Control
**Evidence Anchor:** Page 8 - Table 1, Section 4.1-4.2 (lines 60-89)

The experiments compare against toy MLP baselines only. BP-Chain* is called "the current default way" but has only 4 neurons. No modern architecture comparisons are included. The number of parameters differs across graph topologies because denser graphs create larger input dimensions.

**Impact:** The paper's central claim — that cyclic topologies outperform DAG structures — cannot be separated from the confound of increased parameter count. The FF-trained complete graph has more parameters than the FF chain, and may simply benefit from higher capacity.

**Fix:** (a) Add parameter-count-controlled baselines (match total parameters across topologies by adjusting hidden dimensions). (b) Add comparisons to standard deeper networks (e.g., 3-layer MLP with 128-256 hidden units) trained with both BP and FF. (c) Report significance tests.

## Actionable Suggestions
### S1 (Must): Rewrite Abstract with Bounded Claims
**Evidence Anchor:** Page 1 - Abstract (lines 53-67)

Current abstract claims "superiority over current layer-by-layer DAG neural networks" and "transformative ANN design paradigm." Neither is supported by the evidence.

**Action:** Replace with a measured abstract that states: (a) the research question, (b) the proposed Cyclic NN + GOMLP framework, (c) the limited empirical scope (4 neurons, 3 small benchmarks), and (d) the main finding (graph-structured topologies outperform chain-structured ones under FF training on these benchmarks). A concrete rewrite is provided in the Page 1 Abstract annotation.

### S2 (Must): Fix Goodness Function and Loss
**Evidence Anchor:** Page 6 - Section 3.4.1 (lines 59-72)

Replace ReLU with sigmoid in the goodness score to produce a proper probability, then use standard BCE loss. Alternatively, keep ReLU with epsilon clipping and rename the loss to "contrastive log-loss."

**Action:**
- Option A: p(h) = sigmoid(Σ h²_i - θ·d(h)), then L_N = -1/|D| Σ [y·log(p) + (1-y)·log(1-p)]
- Option B: p(h) = ReLU(Σ h²_i - θ·d(h)) + ε (ε=1e-7), rename to "contrastive log-loss"
- Update Eq. (6) and surrounding text accordingly.

### S3 (Must): Add Parameter-Controlled Baselines
**Evidence Anchor:** Page 8 - Table 1

The current comparison does not control for parameter count across graph topologies. The FF-Complete graph has more parameters per neuron than FF-Chain because each neuron's input dimension is larger (d^N_in = d_h + Σ d_out_pre).

**Action:** Add a new experimental condition where the total parameter count is matched across all graph topologies (e.g., by reducing d_out for denser graphs). If the performance advantage persists, the claim about graph structure is strengthened. If not, the paper must acknowledge that the gain comes from increased capacity.

### S4 (Must): Correct Complexity Analysis
**Evidence Anchor:** Page 7 - Section 3.5 (lines 67-85)

The analysis should clearly separate sequential complexity from parallel complexity, and should not double-count.

**Action:** Use the corrected analysis provided in the Page 7 annotation. Specify assumptions about parallelization model (e.g., PRAM with |V| processors) and compare fairly against standard MLP complexity O(L·d²) where L is number of layers.

### S5 (Must): Restructure Related Work
**Evidence Anchor:** Page 10 - Sections 5.1-5.2, Page 15 - Appendix A.4

The critical comparisons to RNNs (BPTT unrolling) and GNNs (graph as input vs. model) are relegated to the appendix.

**Action:** Move Appendix A.4 into the main Related Work section as a dedicated paragraph or Section 5.3. See the concrete rewrite in the Page 10 Related Work annotation.

### S6 (Must): Rewrite Results Summary and Conclusion
**Evidence Anchor:** Page 9 - lines 107-110, Page 10 - lines 87-92

These sections use hype language and unsupported claims.

**Action:** Replace with bounded, evidence-grounded versions provided in the Page 9 and Page 10 annotations.

### S7 (Nice-to-have): Discuss Label Leakage
**Evidence Anchor:** Page 4 - Section 3.1 (lines 84-96)

The label concatenation for positive samples creates a potential shortcut.

**Action:** Add 2-3 sentences in Section 3.1 discussing this limitation and potential mitigation (e.g., learned fusion, label-free alternatives).

### S8 (Nice-to-have): Specify Graph Generator Parameters
**Evidence Anchor:** Page 5 - Section 3.2 (lines 50-60)

WS and BA graph parameters are not specified.

**Action:** Add the parameter values used (e.g., k=2, p=0.5 for WS; m=1 for BA) in the section.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: AI is important → ANNs are stacked layer-by-layer → Question: do we need to stack?
- P2: Biological neurons form complex graphs (C. elegans, drosophila, mouse, human) → BI uses localized learning → BP requires DAG → FF enables cycles → Three claimed advantages
- P3: Contribution bullet list

**Problem with current storyline:** Paragraph 1 opens too broadly ("AI has reshaped our daily lives") and does not establish the technical problem's stakes before asking the central question. Paragraph 2 packs too many ideas (BI connectome evidence, learning rule comparison, FF algorithm introduction, three claimed advantages) into a dense block. The transition from the BI motivation to the method is not clearly signaled.

### Recommended Storyline (Option A — Best for ICLR)

**Narrative arc:** Technical constraint → Why it matters → Prior attempts limited → Our approach → Key evidence → Scoped claims

**Paragraph Map:**

**P1 (Introduce the DAG constraint):** "Every modern neural network — from MLPs to CNNs to Transformers — is constructed as a Directed Acyclic Graph (DAG). Data flows unidirectionally from input to output through stacked layers. This design is not accidental: training with backpropagation requires gradients to flow backward through all layers, which demands a DAG structure. The DAG constraint has been accepted as a design axiom in deep learning."

**P2 (Identify the limitation):** "However, the DAG constraint imposes two restrictions on neural architecture design. First, information flows only forward, preventing later layers from modulating earlier representations during a single forward pass. Second, all layers must be arranged sequentially, excluding more complex connectivity patterns such as cycles. These restrictions are not present in biological neural systems, where neurons form intricate, cyclic graphs and learning is localized [cite connectome works]."

**P3 (Prior attempts and gap):** "Several lines of work have attempted to move beyond strict layer-by-layer computation. Recurrent neural networks introduce cycles within a single cell but require BPTT unrolling [cite Elman, Schmidhuber]. Localized learning methods [cite Hinton 2022, Nøkland 2019] remove the need for end-to-end backpropagation but have not been used to enable non-DAG topologies beyond chain structures. The combination of localized training with arbitrary graph-structured computation remains unexplored."

**P4 (Our approach):** "We propose Cyclic Neural Networks (Cyclic NN), which pair localized Forward-Forward training with graph-structured neuron topologies. Each neuron is a parameterized computation unit optimized by its own local goodness function. Neurons can be connected in any graph — including cycles — because no gradient flows between them during training. We instantiate this paradigm as Graph Over Multi-Layer Perceptron (GOMLP), testing chain, cycle, Watts-Strogatz, Barabási-Albert, and complete graph topologies."

**P5 (Contributions, scoped):** "Our contributions are: (1) We show that the DAG constraint can be relaxed by combining localized learning with cyclic graph topologies. (2) We propose GOMLP as a concrete instantiation using FF-trained linear neurons. (3) On three classification benchmarks (MNIST, NewsGroup, IMDB), we demonstrate that denser graph topologies consistently outperform chain-structured baselines under the FF regime, and that FF-trained cyclic networks can match or exceed BP-trained chain networks in small-scale settings. (4) We provide the first demonstration that a FF-trained model can outperform BP-trained baselines under specific architectural conditions."

### Alternative Storyline (Option B — Biology-first)

**Narrative arc:** Biological inspiration → Gap between BI and AI → Principle extracted → Implementation → Evidence

This would start with the C. elegans connectome as the hook (move BI content to P1), then argue that the DAG constraint is a design artifact of BP, then introduce Cyclic NN as the biologically motivated alternative. This is riskier because it may be seen as metaphorical rather than technical.

### Abstract Outline

**S1 (Problem):** "Current artificial neural networks are universally designed as Directed Acyclic Graphs (DAGs) due to the constraints of backpropagation-based training."

**S2 (Gap):** "This DAG constraint limits architectural flexibility and contrasts with the cyclic, graph-structured organization of biological neural systems."

**S3 (Method):** "We introduce Cyclic Neural Networks (Cyclic NN), which combine localized Forward-Forward training with arbitrary graph-structured neuron topologies, including cycles."

**S4 (Model):** "As a concrete instantiation, we propose Graph Over Multi-Layer Perceptron (GOMLP), where each neuron is a linear layer optimized by a local goodness function."

**S5 (Result, bounded):** "On three small-scale benchmarks (MNIST, NewsGroup, IMDB), graph-structured GOMLP topologies outperform chain-structured counterparts under FF training. The complete-graph variant achieves the lowest error rates and, for the first time, allows a FF-trained model to match or exceed BP-trained baselines in this limited setting. These findings suggest that relaxing the DAG constraint is a viable direction for further investigation."

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

P0 (Must fix, paper-altering)
├── Issue 1: Claim-evidence mismatch (Abstract/Intro/Conclusion/Results)
│   └── Fix: Replace all hype language with bounded claims
│   └── Expected gain: Scientific credibility restored
├── Issue 2: Goodness function mathematical error (Section 3.4.1)
│   └── Fix: Replace ReLU with sigmoid + standard BCE
│   └── Expected gain: Mathematical correctness
├── Issue 3: Complexity analysis errors (Section 3.5)
│   └── Fix: Corrected O(T·|E|·d²) sequential, O(T·d²·max_in_degree) parallel
│   └── Expected gain: Accurate efficiency characterization
└── Issue 4: Missing parameter-controlled baselines (Section 4)
    └── Fix: Add matched-parameter baselines + significance tests
    └── Expected gain: Valid causal inference about graph structure

P1 (Must fix, positioning-altering)
├── Issue 5: Related Work is flat list (Section 5)
│   └── Fix: Restructure with RNN/GNN differentiation (move App. A.4)
├── Issue 6: Results Summary overclaims (Section 4.2 end)
│   └── Fix: Replace with bounded version
└── Issue 7: Conclusion overclaims (Section 6)
    └── Fix: Replace with validated-findings + limitations version

P2 (Nice-to-have, quality improvement)
├── Issue 8: Label leakage discussion (Section 3.1)
├── Issue 9: Graph generator parameters (Section 3.2)
└── Issue 10: L2-normalization rationale (Section 3.2.1)
```

### Execution Order

| Priority | Task | Effort | Impact | Section |
|----------|------|--------|--------|---------|
| P0 | Fix goodness function + loss | 1 hour | High | 3.4.1 |
| P0 | Correct complexity analysis | 1 hour | High | 3.5 |
| P0 | Add parameter-controlled baselines | 1-2 days | Very High | 4.2 |
| P0 | Rewrite abstract with bounded claims | 30 min | Very High | Abstract |
| P1 | Restructure Related Work | 2 hours | High | 5 |
| P1 | Rewrite results summary and conclusion | 1 hour | High | 4.2, 6 |
| P2 | Discuss label leakage | 30 min | Medium | 3.1 |
| P2 | Specify graph generator parameters | 15 min | Low | 3.2 |
| P2 | Add L2-norm rationale discussion | 30 min | Medium | 3.2.1 |

### Expected Outcome After P0 Fixes

If all P0 items are addressed:
- The abstract, introduction, and conclusion will present bounded, evidence-grounded claims.
- The goodness function will be mathematically sound.
- The complexity analysis will accurately reflect the method's cost.
- The experiments will include parameter-controlled comparisons, enabling proper causal inference about graph structure vs. capacity.

After P0 + P1 fixes, the paper would be a solid "interesting proof-of-concept" contribution rather than an overclaimed "breakthrough" — which is a much more defensible and publishable position.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Compare graph topologies under FF training | MNIST, NewsGroup, IMDB; 4 neurons; Chain/Cycle/WS/BA/Complete graphs | Error rate (%) | FF-Complete best on MNIST (1.54%) and NewsGroup (38.27%) | Denser graphs improve FF performance | No parameter count control; no significance tests |
| E2 | Compare FF vs BP training | Same datasets; BP-Chain* (standard BP), FF-Chain, BP-Chain (BP+local loss) | Error rate (%) | FF-Complete > BP-Chain*; FF-Chain < BP-Chain* | FF with graphs can beat BP chain baselines | Only 4-neuron chain as BP baseline |
| E3 | Hyperparameter sensitivity (T, θ) | All 3 datasets; FF-Complete; T ∈ [1,6], θ ∈ [0,5] | Error rate (%) | Optimal T ≈ 3-4; θ ≥ 1 sufficient | Existence of threshold matters more than value | No analysis of T-θ interaction |
| E4 | Ablation (LN, LReadout) | FF-Complete on all 3 datasets | Error rate (%) | Both components contribute; -LReadout → near random | Each optimization module is necessary | Only tested on Complete graph |
| E5 | Training curve stability (Appendix A.5) | All graph structures, all datasets | FF loss, classifier loss, error rate vs epochs | Stable convergence across all settings | Localized optimization is stable | No comparison with BP training curves |

### Research-Theme Gap Diagnosis

1. **New knowledge (partially addressed):** The core new knowledge — that cyclic/arbitrary graph topologies are trainable with local losses — is demonstrated at a proof-of-concept level. However, the paper does not establish *why* denser graphs help (is it better gradient flow? more information sharing? higher capacity?), limiting the new knowledge to an empirical observation without mechanistic understanding.

2. **Reproducibility/reusability (partially addressed):** The paper provides code and seeds (20 runs), which is good. However, the method's reliance on the FF algorithm (which itself has known label leakage issues) and the underspecified graph generator parameters reduce reusability.

3. **Potential to change practice/understanding (weakly supported):** The provocative claim ("don't need DAG") is interesting, but the experiments are too small-scale to change how practitioners build neural networks. Stronger evidence is needed to support the paradigm-shift claim.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 Experiments (prerequisite for credibility, ~1 week)
├── E6: Parameter-matched baselines
│   ├── Hypothesis: Performance gap persists after matching total params
│   ├── Design: Adjust d_out per neuron so total params equal across topologies
│   ├── Control: Same optimizer, epochs, learning rate schedule
│   └── Success: Gap narrows but denser graphs still better
│
├── E7: Statistical significance tests
│   ├── Hypothesis: FF-Complete significantly better than FF-Chain at p<0.05
│   ├── Design: Paired t-test or Mann-Whitney U on 20 seed results
│   └── Success: p < 0.05 on at least 2 of 3 datasets
│
└── E8: Deeper/stronger BP baselines
    ├── Hypothesis: Cyclic NN advantage holds against deeper BP-MLPs
    ├── Design: Compare against 3-layer MLP (128-64-32), 5-layer MLP trained with BP
    ├── Control: Same input features, same evaluation protocol
    └── Success: Cyclic NN competitive (gap ≤ 2%) with deeper BP-MLPs

P1 Experiments (positioning strengthening, ~2 weeks)
├── E9: Scaling study (|V| = 6, 8, 12)
│   ├── Hypothesis: Gains from graph structure scale with more neurons
│   ├── Design: Repeat main experiment with larger neuron counts
│   └── Success: Dense graphs maintain advantage at larger sizes
│
├── E10: OOD / robustness test
│   ├── Hypothesis: Cyclic graphs improve robustness to input noise
│   ├── Design: Add Gaussian noise to MNIST, test error rate
│   └── Success: Dense graphs degrade less than chain graphs
│
└── E11: Information flow analysis
    ├── Hypothesis: Denser graphs enable richer neuron representations
    ├── Design: Compute mutual information between neuron outputs and labels
    └── Success: Dense graphs → higher MI for more neurons

P2 Experiments (nice-to-have, >2 weeks)
├── E12: Image classification on CIFAR-10 / Fashion-MNIST
├── E13: MLP-per-neuron (replace linear with 2-layer MLP)
└── E14: Comparison with BERT-finetuned baselines for NewsGroup/IMDB
```

### Traceability

| Proposed Exp | Target Claim | Research-Value Dimension | Expected Quality Gain |
|-------------|-------------|------------------------|----------------------|
| E6 (param-matched) | Graph structure causes gains (not capacity) | Validity | Enables causal claim about topology |
| E7 (significance) | Results are statistically reliable | Reproducibility | Strengthens empirical evidence |
| E8 (stronger baselines) | Cyclic NN is viable vs. mainstream DAGs | New knowledge | Positions against real baselines |
| E9 (scaling) | Approach works beyond 4 neurons | Impact on practice | Demonstrates scalability potential |
| E10 (OOD) | Cyclic graphs improve robustness | New knowledge | Extends contribution beyond IID

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 4.5 / 10**

This score reflects the following assessment:

- **Research value + novelty (weight: primary): 5/10.** The core idea — relaxing the DAG constraint by combining localized FF training with graph-structured topologies — is genuinely interesting and addresses a fundamental design assumption. However, the novelty is partially overlapping with existing work (FF algorithm [Hinton 2022], localized learning [Nøkland 2019], and prior biologically-inspired architectures). The unique contribution is the *combination* plus the demonstration that it works, which has moderate research value. The score is restrained because without external literature verification (unavailable in this run), the precise novelty boundary is uncertain.

- **Validity/soundness: 4/10.** The mathematical formulation has a confirmed error (goodness function, loss definition) and the complexity analysis double-counts operations. The experiments lack parameter count control and significance tests. These issues materially affect confidence in the reported results.

- **Empirical evidence: 3/10.** The experiments use tiny architectures (4 neurons) on small datasets against weak baselines. The claims far exceed what the evidence supports. The paper does not demonstrate scalability, generalizability, or robustness.

- **Presentation/clarity: 4/10.** The paper overuses hype language ("transformative," "major shift") which reduces credibility. The related work section is a flat list with critical comparisons relegated to the appendix. The method description is generally clear but has reproducibility gaps (graph generator parameters unspecified).

**Post-Revision Target: [6.0, 7.5] / 10**

This target assumes the following revisions are completed:
1. (P0) Mathematical correction of goodness function and loss
2. (P0) Corrected complexity analysis
3. (P0) Addition of parameter-controlled baselines
4. (P0) Rewrite of abstract/intro/conclusion with bounded claims
5. (P1) Restructured related work with RNN/GNN differentiation in main text
6. (P1) Results summary and conclusion rewritten with validated bounds

If, in addition, the proposed scaling experiments (E9-E10) are added and confirm the approach's viability beyond 4 neurons, the target could reach the upper bound of 7.5. Without these, the paper remains a thought-provoking but empirically limited proof-of-concept, suitable for workshops or position papers rather than a top-tier conference.