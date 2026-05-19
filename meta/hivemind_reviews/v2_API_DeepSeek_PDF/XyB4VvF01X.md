## Summary
# Final Review Report

## Summary

This paper presents Graph2Tac (G2T), a graph neural network for tactic prediction in the Coq proof assistant. The core contribution is a neural definition embedding task that enables the model to compute representations for mathematical definitions not seen during training, adapting online to new Coq projects. G2T operates on a faithful graph representation of Coq terms extracted from the kernel, encoding the hierarchical dependency structure of definitions. The model is integrated with the Tactician framework and can be used on consumer hardware. Empirical evaluation on 120 Coq Opam packages shows that G2T-Anon-Update solves 26.1% of test theorems (10-minute limit), compared to 17.4% for a frozen-definition baseline and 25.8% for the strong k-NN baseline. Combined, G2T and k-NN achieve 33.2%, demonstrating complementarity. The paper also provides a broad comparison including a transformer baseline and CoqHammer.

**Core merits:** (1) The online learning setting for new definitions is practically important and relatively underexplored for Coq. (2) The graph representation faithfully encodes Coq kernel terms. (3) The definition embedding task demonstrably improves performance (+8.7 absolute percentage points over frozen baseline). (4) The threats-to-validity discussion is unusually thorough.

**Core weaknesses:** (1) Statistical significance is unknown—single-run evaluation without variance reporting. (2) The loss weighting (1000x for definition task) is unsubstantiated and may cause training instability noted by the authors. (3) Several strong claims ("first practical neural solver", "first comprehensive comparison") overreach the evidence. (4) The related work section is organized as a chronological list rather than analytical comparison. (5) The k-NN baseline equals or exceeds G2T on many metrics, raising questions about whether the GNN complexity is justified for the practical setting.

## Strengths
1. **Practical and timely problem formulation.** The online learning setting—adapting to new definitions in unseen Coq projects—is a genuine bottleneck for deploying ML proof assistants in real-world development workflows. The paper correctly identifies that most prior work evaluates on fixed benchmarks where train and test sets are drawn from the same distribution, which overestimates real-world utility.

2. **Faithful graph representation of Coq terms.** Using a graph extracted directly from the Coq kernel (rather than surface syntax or token sequences) captures the full hierarchical dependency structure of definitions. This is technically well-motivated and avoids name-resolution ambiguities that plague text-based representations.

3. **Clear demonstration of the definition task's value.** The ablation from G2T-Frozen-Def (17.4%) to G2T-Anon-Update (26.1%) provides compelling evidence that the definition embedding task materially improves performance. This is the cleanest causal evidence in the paper.

4. **Complementarity of G2T and k-NN.** The combined solver (33.2%) outperforming either individual solver, along with the Venn diagram analysis (Figure 6), convincingly shows that the two online approaches exploit different information (definitions vs. proof scripts) and are genuinely complementary.

5. **Thorough threats-to-validity discussion (Appendix A).** The paper candidly discusses single-run evaluation, training instability, incomparable baselines, data leakage risks, and the impact of inconsistent axioms. This transparency is a significant strength and should be preserved in revisions.

6. **Reproducibility commitment.** Open-source code, dataset release plans, and detailed training configurations (Appendix J) are provided. The acknowledgment that a two-day training run achieves similar results to the three-week run lowers the reproducibility barrier.

7. **Broad baseline comparison.** The paper compares G2T against k-NN, two transformer variants (CPU/GPU), CoqHammer with multiple ATP backends, and built-in Coq tactics—a wider set than most prior work in this area.

## Weaknesses
1. **Lack of statistical significance and variance reporting (Severity: High).** All results come from single training runs with no confidence intervals, error bars, or significance tests. Given the authors' own acknowledgment that "models were difficult to reliably train" and that "our results are more variable" due to package-level splitting, the numerical rankings (e.g., 26.1% G2T vs 25.8% k-NN) cannot be distinguished from noise. This fundamentally limits the strength of any comparative claim.

2. **Unsubstantiated loss weighting (Severity: High).** The combined loss uses $L = 1000 L_{\text{def}} + L_{\text{tactic}}$ without any justification or sensitivity analysis. The factor of 1000 is extreme—if $L_{\text{def}}$ (cosine similarity, range ~0-2) is scaled by 1000, it would completely dominate $L_{\text{tactic}}$ (cross-entropy over a large vocabulary). This may explain the reported training instability and periodic checkpoint restarts.

3. **Overclaiming in contributions and positioning (Severity: Medium).** Several claims go beyond available evidence: (a) "first practical neural network-based solver for Coq on consumer-grade computer" requires comparison against ASTactic, TacTok, and ProverBot9001 on the same hardware; (b) "first comprehensive comparison" excludes the strongest prior neural solvers from direct comparison; (c) "state of the art among existing Coq solvers" (Claim 5) is based on informal, non-conclusive comparisons in Appendix B.

4. **Related work is a chronological list, not analytical (Severity: Medium).** The section surveys systems platform-by-platform (Coq, then Mizar, HOL4, HOL Light, Isabelle, Lean) without organizing by comparison axes (online/offline, graph/text/feature-based, definition-aware/tactic-aware). This makes it difficult for readers to identify the paper's specific differentiation.

5. **k-NN baseline challenges the core contribution (Severity: Medium).** The simple k-NN (25.8%) nearly matches G2T (26.1%) despite having no neural architecture, no definition understanding, and no training. Combined, they reach 33.2%, but G2T adds only ~7.4 percentage points over k-NN alone (and much less at shorter time limits). This raises the question of whether G2T's complexity is justified for the online Coq setting.

6. **Graph pruning may lose important structure (Severity: Low-Medium).** Graphs are pruned to 1024 nodes, and proof terms are omitted from theorem definitions based on proof irrelevance. While practical, these choices are not validated—e.g., would including proof terms improve the definition embeddings? No ablation study addresses this.

7. **Restricted tactic argument prediction (Severity: Low-Medium).** G2T cannot predict term arguments, only local hypotheses or global definitions. This limits the model to a subset of Coq tactics and is only mentioned in the appendix (Threats to Validity).

## Key Issues
### Issue 1 (Severity: Major): Uncertainty of numerical results due to single-run evaluation
**Location:** Page 7-8 (Experimental Setup and Results)
**Evidence:** The paper states "we only train one of each model instead of multiple instances, and our models were difficult to reliably train" (Page 15, Threats to Validity). No confidence intervals, standard deviations, or significance tests are reported for any pass rate. The gap between G2T-Anon-Update (26.1%) and k-NN (25.8%) is 0.3 percentage points—well within typical variance from different random seeds or train/test splits.
**Impact:** Without variance information, the central claim that "the definition task improves the model from 17.4% to 26.1%" cannot be interpreted reliably. The improvement could be smaller or larger in a different split. Comparative claims against k-NN are even more fragile.
**Remediation:** Run each model variant with at least 3 random seeds and report mean ± std pass rates. If computational budget is prohibitive, run at least the primary comparison (G2T-Anon-Update vs. k-NN) with 3 seeds and report individual run results.

### Issue 2 (Severity: Major): Unsubstantiated loss weighting factor
**Location:** Page 6 (Section 3.1, combined loss formulation)
**Evidence:** $L = 1000 L_{\text{def}} + L_{\text{tactic}}$. The definitions immediately preceding state $L_{\text{def}} = 1 - \cos(\text{DefTask}(g_d), \text{DefEmb}(id))$. Cosine similarity loss ranges from 0 (identical) to 2 (opposite). Cross-entropy $L_{\text{tactic}}$ for tactic sequences over a large vocabulary can be 5-20 nats per example. The 1000x multiplier would scale $L_{\text{def}}$ to dominate $L_{\text{tactic}}$ by at least 50x.
**Impact:** This imbalance likely causes the gradient signal from tactic prediction to be negligible during shared-backbone training, which may explain why "training was difficult to reliably train" (Appendix A). It also means the definition embedding quality may be achieved at the expense of tactic prediction accuracy.
**Remediation:** Provide a sensitivity analysis (lambda = 1, 10, 100, 1000) on a held-out development set. Alternatively, use uncertainty weighting or GradNorm to balance the losses automatically.

### Issue 3 (Severity: Medium): Overclaimed positioning of contributions
**Location:** Page 2 (Contributions list), Page 2 (Introduction), Page 10 (Abstract)
**Evidence:** Seven numbered contributions include: (3) "first comprehensive comparison" — but the main benchmark excludes the strongest prior Coq neural solvers (ASTactic, TacTok, ProverBot9001) from direct comparison. (5) "state of the art among existing Coq solvers" — relies on informal Appendix B comparisons described as "non-conclusive." (7) "G2T is one of the first neural solvers conveniently available to end-users" — ambiguous and not empirically positioned.
**Impact:** Claims that overreach the evidence invite reviewer criticism and can distract from the paper's genuine contributions (definition embedding task, graph representation, complementarity analysis).
**Remediation:** Replace "first comprehensive comparison" with "a comparative evaluation across multiple solver families." Remove or qualify "state of the art" to reflect the informal nature of the CoqGym comparison. Bound claims to the actual experimental protocol.

### Issue 4 (Severity: Medium): Related work lacks analytical structure
**Location:** Page 3 (Background and related work)
**Evidence:** The section lists systems chronologically by ITP platform (Coq, Mizar, HOL4, HOL Light, Isabelle, Lean) with brief descriptions but no thematic grouping or comparison axes (online vs. offline, graph vs. text vs. feature-based, definition-aware vs. tactic-aware). The novelty claim at the end is a single sentence.
**Impact:** Readers cannot easily determine where G2T fits in the landscape or what its specific differentiation is. This weakens the paper's positioning, especially for reviewers from adjacent fields.
**Remediation:** Restructure the related work around 2-3 comparison axes (Section 3, Annotation 6 on Page 3 provides a concrete revision). Explicitly state how G2T differs from the most closely related method in each category.

## Actionable Suggestions
### Suggestion 1 (Must): Report multi-seed variance and significance
- **Target:** Section 4 (Evaluation) and Tables 4, Figures 5-7
- **Action:** Run at least 3 seeds for G2T-Anon-Update, G2T-NoDef-Frozen, k-NN, and the combined solver. Report mean ± std pass rates. If full re-training is too expensive, run 3 seeds for the primary comparison (G2T-Anon-Update vs k-NN) and note single-seed results for other variants.
- **Expected benefit:** Provides statistical grounding for the 17.4% → 26.1% improvement claim. Without this, the paper's central result is not formally established.

### Suggestion 2 (Must): Justify or re-tune the loss weighting
- **Target:** Page 6, $L = 1000 L_{\text{def}} + L_{\text{tactic}}$
- **Action:** (a) Add a sentence explaining the range and typical values of each loss term. (b) Show that $\lambda=1000$ produces balanced gradient norms, or (c) perform a sensitivity sweep of $\lambda \in \{0.1, 1, 10, 100, 1000\}$ on a small development set, or (d) adopt adaptive loss balancing (e.g., uncertainty weighting or GradNorm).
- **Expected benefit:** Addresses a likely reviewer concern about training stability and the multi-task trade-off.

### Suggestion 3 (Must): Tighten contribution claims
- **Target:** Page 2 (Contributions), Page 2 (Introduction), Abstract
- **Action:**
  - Replace "first comprehensive comparison" → "a comparative evaluation across multiple solver families including k-NN, transformer, and CoqHammer."
  - Replace "state of the art among existing Coq solvers" → "competitive with existing Coq solvers on the poltac package (see Appendix B for informal comparison)."
  - Remove or substantiate "first practical neural network-based solver for Coq on consumer-grade computer" with concrete hardware and runtime benchmarks.
- **Expected benefit:** Prevents desk-reject-level reviewer pushback on overclaiming.

### Suggestion 4 (Nice-to-have): Restructure related work around comparison axes
- **Target:** Page 3 (Background and related work)
- **Action:** Organize by: (a) online vs offline learning, (b) representation type (graph/text/feature), (c) definition-aware vs tactic-aware. Provide a summary comparison table.
- **Expected benefit:** Improves paper positioning and helps reviewers quickly identify novelty.

### Suggestion 5 (Nice-to-have): Add definition embedding visualization and analysis
- **Target:** Page 6 (definition task) or Appendix (already partially covered in Appendix N)
- **Action:** Extend the UMAP analysis (Appendix N) with a quantitative evaluation: (a) nearest-neighbor retrieval accuracy for definition embeddings, (b) correlation between embedding similarity and proof co-occurrence, (c) case studies of isomorphic definitions (true/false, andb/orb) to show symmetry breaking.
- **Expected benefit:** Provides direct evidence that the definition task learns meaningful concept representations, not just a training signal.

### Suggestion 6 (Nice-to-have): Main-text discussion of architectural limitations
- **Target:** Section 3.1 (GNN and Definition Task)
- **Action:** Move the limitation about "G2T model has no way to predict term arguments" (currently only in Appendix A/Threats to Validity) into the main method section.
- **Expected benefit:** Improves scholarly completeness and helps readers understand the model's scope.

## Storyline Options + Writing Outlines
### Current Storyline Evaluation

The current introduction follows this paragraph-level structure:
- P1: ITPs are useful (Coq examples) but theorem proving is laborious.
- P2: Prior ML approaches exist, but cannot adapt to new definitions. k-NN is simplistic. We need online models.
- P3: G2T is a GNN that adapts to new definitions, complements k-NN.
- P4: Definition embedding task details.
- P5: Contributions list.

**Alignment checks:**
- Problem alignment: The challenge (new definitions in unseen projects) matches the solution (definition embedding task). PASS.
- Variable alignment: "Definition embedding" appears in the introduction and is central to the method. "Graph representation" appears in intro and method. PASS.
- Contribution-evidence alignment: Claims (1)-(2) are directly tested; claims (3)-(7) have partial or indirect support. PARTIAL FAIL on (3) and (5).

### Proposed Storyline Alternative (Recommended)

Alternative narrative that strengthens the gap and makes the GNN choice self-evident:

**P1 (Stakes):** "Interactive theorem provers like Coq can verify complex software and mathematical proofs, but constructing formal proofs remains labor-intensive despite decades of automation efforts. Recent ML approaches have shown promise in suggesting proof tactics automatically."

**P2 (Gap):** "A critical limitation of existing neural proof assistants is that they cannot adapt to new Coq projects, each of which introduces its own definitions, lemmas, and tactics. Models must be retrained from scratch to handle new concepts, making them impractical for everyday use. While the Tactician framework introduced online k-NN models that learn from user tactic scripts, these models lack access to the global definition context—they cannot adjust their predictions when new definitions are loaded into Coq's environment."

**P3 (Solution Intuition):** "To overcome this, a model must (a) understand the hierarchical structure of definitions, where each concept depends on earlier ones, and (b) compute useful representations for new definitions at inference time without retraining. Graph neural networks are a natural fit because they can process dependency graphs and update node representations incrementally. We present Graph2Tac (G2T), a GNN that jointly learns to embed definitions and predict tactics."

**P4 (Key Technical Idea):** "G2T's definition training task is trained to align computed definition embeddings with learned embedding table entries for seen definitions. At test time, it applies this trained network to compute embeddings for unseen definitions, which are then used in the tactic prediction pipeline. This enables G2T to incorporate new mathematical concepts into its reasoning without retraining."

**P5 (Evidence Preview + Contributions):** "On a benchmark of 120 Coq Opam packages with a strict package-level train/test split, G2T solves 26.1% of test theorems—an 8.7% absolute improvement over a version without the definition task. G2T is complementary to the k-NN model, together reaching 33.2%. G2T is integrated with the Tactician framework and runs on consumer hardware."

### Abstract Outline (Complete)

**S1 (Problem):** Formal theorem proving in Coq remains labor-intensive, and existing ML proof assistants cannot adapt to new mathematical definitions introduced in unseen projects.

**S2 (Gap):** Previous approaches either operate offline (requiring retraining for new projects) or use simple feature-based methods that lack access to the global definition hierarchy.

**S3 (Method):** We present Graph2Tac (G2T), a graph neural network that operates on a kernel-level graph representation of Coq terms and learns hierarchical definition embeddings that generalize to unseen definitions.

**S4 (Key Result):** On a package-level train/test split of 120 Coq Opam packages, G2T's definition embedding task improves the pass rate from 17.4% to 26.1%, competitive with the strong k-NN baseline (25.8%).

**S5 (Significance):** G2T and k-NN are complementary online solvers, together proving 33.2% of test theorems, and G2T is made available through the Tactician framework for practical use.

## Priority Revision Plan
### P0 Items (Must-do before resubmission)

| Priority | Item | Location | Effort | Expected Impact |
|----------|------|----------|--------|-----------------|
| P0.1 | Run multi-seed evaluation (≥3 seeds) for G2T-Anon-Update and k-NN; report mean±std | Section 4, Tables 4, Figs 5-7 | High (3-5 GPU-days) | Provides statistical validity for core claim |
| P0.2 | Justify loss weighting λ=1000 with sensitivity analysis or adaptive balancing | Section 3.1 (loss formulation) | Low-Medium (2-3 CPU-hours) | Addresses training instability and reviewer concern |
| P0.3 | Tighten all overclaims: replace "first comprehensive comparison," "state-of-the-art," "first practical neural solver" with bounded wording | Abstract, Page 2 (Contributions), Page 2 (Introduction) | Low (editing) | Prevents reviewer rejection based on claim-evidence mismatch |

### P1 Items (Should-do for strong revision)

| Priority | Item | Location | Effort | Expected Impact |
|----------|------|----------|--------|-----------------|
| P1.1 | Restructure related work by comparison axes (online/offline, graph/text/feature, definition-aware/tactic-aware) | Page 3 (Background) | Low-Medium (rewriting) | Improves positioning and novelty communication |
| P1.2 | Add definition embedding evaluation: nearest-neighbor retrieval accuracy, case study of isomorphic definitions | Section 3.1 or Appendix | Medium (2-3 days analysis) | Directly validates the core technical contribution |
| P1.3 | Move tactic limitation (no term arguments) from appendix to main method text | Section 3.1 | Low (editing) | Scholarly completeness |

### P2 Items (Nice-to-have for quality improvement)

| Priority | Item | Location | Effort | Expected Impact |
|----------|------|----------|--------|-----------------|
| P2.1 | Add graph-pruning ablation: compare 1024-node vs full-graph vs 512-node | Appendix | Medium (2-3 GPU-days) | Validates design choice |
| P2.2 | Add loss weight sensitivity table (λ = 0.1, 1, 10, 100, 1000) | Appendix | Low (2-3 CPU-hours) | Supports P0.2 |
| P2.3 | Add per-package solved theorem lists to public benchmark results | Section 6 (Reproducibility) or dataset release | Medium (engineering) | Enables future comparisons |

### Revision Strategy Roadmap

```text
[Current manuscript]
    │
    ├── P0.1: Multi-seed evaluation ──────────► Statistical grounding for core claim
    ├── P0.2: Loss weighting justification ────► Training reproducibility
    ├── P0.3: Tighten claims ─────────────────► Defensible positioning
    │
    ├── P1.1: Restructure related work ───────► Clearer novelty signal
    ├── P1.2: Definition embedding eval ──────► Validates core mechanism
    ├── P1.3: Expose tactic limitation ───────► Scholarly completeness
    │
    └── P2.1-3: Ablations + data release ─────► Stronger revision (optional)
```

### Expected Outcome After P0 Fixes

If P0 items are addressed, the paper's core scientific claim ("definition embedding task improves theorem proving in Coq") would be supported by variance-aware evidence and free from overclaim-related vulnerabilities. P1 items would further strengthen the paper by providing a clearer novelty story and validating the mechanism. With P0+P1, the paper becomes a solid acceptance candidate at a top venue.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | G2T-Anon-Update overall pass rate | 2000 test theorems, 10min limit, 1 CPU | Pass rate (fraction proved) | 26.1% | C1 (definition task improves performance) | Single run; no variance |
| E2 | G2T-NoDef-Frozen baseline (no definition task) | Same as E1 | Pass rate | 17.4% | C1 (ablation control) | Single run |
| E3 | k-NN baseline | Same as E1 | Pass rate | 25.8% | C4 (k-NN is strong baseline) | Feature-based, no definition awareness |
| E4 | Transformer (CPU and GPU) | Same as E1 | Pass rate | CPU 10.5%, GPU 14.8% | C3 (comparison across families) | Small model, no pretraining |
| E5 | CoqHammer (combined ATP backends) | Same as E1 | Pass rate | 17.4% | C3 (comparison) | Single-threaded; not optimal |
| E6 | G2T-Named-Update (with name embeddings) | Same as E1 | Pass rate | 24.1% | C1 (ablation: names vs anonymous) | Single run |
| E7 | G2T-Anon-Update + k-NN (combined) | Time-scaled aggregation on 1 CPU | Pass rate | 33.2% | C6 (complementarity) | Simulated parallel; not true ensemble |
| E8 | Package-specific pass rates (Fig 7) | Up to 500 theorems/pkg, 5min limit | Pass rate per package | Highly variable | C1, C4 | Small per-package sample sizes |
| E9 | Impact of new dependencies (Fig 14-15) | Theorems grouped by #new definition dependencies | Pass rate vs dep count | Online models improve with more deps | C1 (online usefulness) | Correlated with package identity |
| E10 | poltac comparison (CoqGym benchmark, Table 2) | 309 theorems, 5-10min | Pass rate | G2T 86.4%, k-NN 73.5% | C5 (SOTA among Coq solvers) | Informal comparison; different training sets |
| E11 | Inconsistent axiom detection (Appendix K) | Post-hoc analysis of test packages | Axiom usage counts | G2T-Anon found 192 tlc theorems via skip_axiom | Validity monitoring | Detection methodology not systematic |

### Research-Theme Gap Diagnosis

1. **New knowledge (residual novelty):** The core claim—that a definition embedding task improves online theorem proving—is supported by the 17.4% → 26.1% improvement. However, the mechanism is not directly validated. It remains unclear whether the improvement comes from better definition embeddings, better training regularization, or better initialization for the shared GNN backbone.

2. **Reproducibility:** Code and dataset will be released, and training configurations are documented. However, the unsubstantiated loss weighting (1000x) and reported training instability mean that reproducing the exact results may be challenging.

3. **Impact on practice/understanding:** The finding that k-NN (25.8%) nearly matches G2T (26.1%) is significant for practitioners—it suggests that a well-tuned feature-based approach with online learning is competitive with a sophisticated neural architecture in this setting. This deserves more discussion.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Quality Gain |
|--------|-------------|------------|----------------|---------------------|---------|------------------|-----------|----------------------|
| P0-E1 | C1 (definition task improves pass rate) | G2T-Anon-Update mean pass rate > G2T-NoDef-Frozen with p<0.05 | Train both models with 3 random seeds, same test set, 10min limit | G2T-NoDef-Frozen (same seeds) | Mean±std pass rate, paired t-test | Δ > 3% absolute with p<0.05 | 3-5 GPU-days | Statistically validated core claim |
| P0-E2 | Loss balance validity | Loss weighting affects training stability and final pass rate | Sweep λ = {1, 10, 100, 1000} on a subset of training data (10%) | λ=0 (no definition task), λ=1000 (current) | Pass rate on held-out dev set, training loss curves | λ=1000 is not dominated by a different λ | 2-3 CPU-hours | Justifies design choice; may improve results |
| P1-E1 | Definition embeddings capture semantics | Embedding similarity correlates with proof co-occurrence | For 500 held-out definitions, compute nearest-neighbor retrieval against co-occurrence in proof states | Random embeddings, G2T-NoDef embeddings | Recall@k for co-occurring definitions | G2T-Anon > G2T-NoDef by 10%+ | 1-2 GPU-days | Directly validates mechanism |
| P1-E2 | Graph representation is better than flat tokenization | G2T-Ablation (token sequence) < G2T-Graph (current) | Replace graph input with flattened token sequence + Transformer encoder | Full G2T (graph input) | Pass rate on test set | Graph version ≥ +5% absolute over token version | 3-5 GPU-days | Validates graph representation contribution |
| P2-E1 | Graph pruning threshold affects quality | 1024-node pruning is sufficient | Vary pruning threshold (512, 1024, 2048, full) on 50 test theorems | 1024-node (current) | Pass rate, inference time, memory | 1024 within 2% of full-graph performance | 1-2 GPU-days | Validates engineering design choice |

```text
ASCII Diagram — Experiment Upgrade Plan
P0 (Must-do before resubmission)
├── P0-E1: Multi-seed evaluation (3 seeds, G2T vs NoDef)
│   └── Outcome: Statistical validation of core 17.4%→26.1% claim
└── P0-E2: Loss weight sensitivity (λ sweep)
    └── Outcome: Justified/improved training procedure
    
P1 (Should-do for strong revision)
├── P1-E1: Definition embedding quality (retrieval task)
│   └── Outcome: Mechanism validation
└── P1-E2: Graph vs token ablation
    └── Outcome: Validates graph representation choice

P2 (Nice-to-have)
└── P2-E1: Pruning threshold sensitivity
    └── Outcome: Validates 1024-node design choice
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Rationale (research value + novelty as primary dimensions):**

The paper addresses a practically important problem (online adaptation to new definitions in Coq) and provides a technically sound GNN-based solution. The definition embedding task is a genuine methodological contribution, and the 17.4% → 26.1% improvement demonstrates empirical value. The broad baseline comparison, transparent threats discussion, and planned open-source release are strong points.

However, the score is constrained by: (1) no statistical significance or variance reporting for any result, making the core claim unverifiable as stated; (2) an unsubstantiated loss weighting (1000x) that may explain documented training instability; (3) overclaims in contribution positioning that outrun the evidence; (4) a simple k-NN baseline matching G2T's performance, raising questions about whether the GNN complexity is justified for the practical setting.

The paper's research value is genuine but the current evidentiary presentation does not fully support the strength of the claimed contributions. The novelty of the definition embedding task is moderate—it is an application of standard multi-task learning with a cosine-similarity objective—but its application to the online Coq setting is novel.

### Post-Revision Target: [7.5, 8.5] / 10

**Preconditions for reaching target:**
- P0.1 (multi-seed evaluation with variance) completed and core claim holds with statistical significance.
- P0.2 (loss weighting justification or adaptive balancing) completed.
- P0.3 (claim tightening) completed to match evidence scope.
- P1.1 (related work restructuring) and P1.2 (definition embedding validation) completed for stronger positioning.

If all P0 and P1 items are addressed, the paper would have: (a) a statistically grounded core claim, (b) a defensible and well-positioned narrative, (c) validated mechanism through the definition embedding retrieval analysis, and (d) a clearly differentiated contribution relative to the k-NN baseline. Under those conditions, the paper would be a strong candidate for acceptance at a top venue (ICLR/NeurIPS).