- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 5, 5, 3, 6
## Summary

This paper bridges graph autoencoders (GAEs) and graph contrastive learning (GCL) by arguing that both structure- and feature-based GAEs can be understood through a contrastive lens. It proposes a unified design space with five components (augmentations, contrastive views, encoder/decoder, contrastive loss, negative samples), enumerates eight contrastive-view configurations in a taxonomy (Table 1), identifies three previously unexplored variants (cases ⑥⑦⑧), and benchmarks them alongside existing GAEs on link prediction and node classification across seven datasets. The three new variants show competitive performance, often matching or beating state-of-the-art.

---

## Strengths

- **Systematic enumeration of the contrastive-view design space (Table 1).** The taxonomy exhaustively organizes combinations of graph views (A=B vs. A≠B), receptive fields (l=r vs. l≠r), and node pairs (v=u vs. v≠u), mapping each of the eight configurations to existing methods (GCLs, GAE, MaskGAE, GraphMAE, etc.) and cleanly identifying three unexplored cases (⑥⑦⑧). This provides a unified organizational framework that the literature was missing, and directly motivates the empirical investigation.

- **Competitive empirical performance of the proposed variants.** The three new variants (⑥⑦⑧) perform at or near state-of-the-art on both link prediction and node classification across multiple datasets (e.g., \ours⑧ achieves best accuracy on Cora (84.5%) and CS (93.1%); \ours⑦ achieves best AUC on PubMed (98.9%) and best AP on Cora (97.2%)). These results validate that the taxonomy-driven exploration yields practically effective architectures.

- **Scalability insight contrasting structure-based vs. feature-based GAEs.** The paper documents that all feature-based baselines run out of memory (OOM on 24GB GPU) on the Physics dataset, while the structure-based \ours variants scale cleanly. This is a practically useful observation that is rarely highlighted in prior benchmarks.

- **Modular discussion of negative samples.** Section "Negative samples" explicitly discusses how techniques from GCL (stop-gradient, asymmetric networks) could eliminate the need for negative samples in structure-based GAEs, and notes that feature-based GAEs already avoid them. This design-level insight goes beyond standard GAE formulations.

---

## Weaknesses

### Fatal
None.

### Major

- **Node classification evaluation protocol is not specified in the main text.** The paper reports node classification accuracy (Table 4) but never states *how* the classifier is trained on top of the self-supervised representations. Is it linear probing (e.g., logistic regression on frozen embeddings), fine-tuning the entire model, or something else? Which classifier architecture and training procedure were used? The paper only mentions data splits (line 321) and number of runs (10). This is the paper's primary evaluation task, and the protocol is a critical piece of information. The community cannot assess whether the numbers reflect meaningful differences or protocol-specific artifacts without this detail. (The code is publicly available, which mitigates but does not eliminate this concern — the paper itself should be self-contained on this point.)

### Minor

- **Theoretical novelty is explicitly limited and the framing oversells it.** The paper's Lemma (feature-based GAEs lower-bounded by an alignment loss) is acknowledged as "a direct consequence of applying [Zhang et al., 2022, Theorem 3.4]" to the graph setting. The connection for structure-based GAEs was already established by MaskGAE. Remark II honestly states that the theoretical expositions "were largely inspired by previously established theoretical insights" and that a more detailed analysis "is still beyond the scope." Given these acknowledgments, the paper's claim in the introduction — "\ours is the first work to explore contrastive learning principles and architecture design in the context of GAEs" — is overstated. The main value lies in the systematic framework and empirical taxonomy, not in novel theoretical results; the framing should reflect this.

- **Benchmark scope is narrower than claimed.** The paper claims to "set a new benchmark for GAEs across diverse graph-based learning tasks," but the experiments cover only transductive node classification and link prediction. No graph-level tasks (e.g., graph classification, graph regression) are included, even though several baselines (GraphMAE, GiGaMAE) were originally evaluated on those. No large-scale graphs (e.g., ogbn-arxiv, ogbl-ppa) are used. The seven datasets are all from two families (citation networks and Amazon co-purchase). The benchmark contribution is solid within its scope, but the claims should be calibrated to match.

- **No ablation studies visible in the main text.** The introduction and conclusion reference "detailed ablation studies," but none appear in the parsed text. While these may reside in a stripped appendix, the main text does not provide any ablation isolating the effect of individual design dimensions (e.g., holding all else fixed and varying only the contrastive view). Such ablations would directly support the paper's claim that the five design dimensions matter.

### Trivial

- **Minor writing issues** (e.g., duplicated "and" at line 34: "previous works and and closely look into").

---

## Nice-to-Haves

- Including at least one graph-level task (e.g., graph classification on TU datasets) and one large-scale dataset (e.g., ogbn-arxiv) would substantiate the "benchmark" framing.
- An ablation study isolating the effect of each of the five design dimensions (especially contrastive views) would strengthen the paper's core claims about the taxonomy.
- Reporting training time, memory usage, and hyperparameter sensitivity would make the benchmark more useful for practitioners.

---

## Removed Points

These points were flagged by the reviewers but are removed with justification:

1. **"Missing experimental details (encoder architecture, optimizer, learning rate, etc.)"** — The paper says "follow exactly the experimental settings in GAE" for link prediction (line 247) and references publicly available data splits. Implementation details (encoder layers, hidden dimensions, hyperparameters) are standard content for an appendix or experimental setup section, which the parser likely stripped. The code is publicly available. Per the instructions, criticisms about content that would reside in a stripped appendix are removed.

2. **"Missing ablation on design dimensions"** — The paper explicitly references ablation studies (lines 46, 332). These are absent from the parsed text because the parser strips appendix/supplementary sections. Per the instructions, this criticism is removed.

3. **"Reproducibility concerns / missing detailed hyperparameters"** — The code is publicly available ("The source code for \ours, including the baselines and all the code for reproducing the results, is publicly available"). Hyperparameter listings are standard appendix content. Removed per instructions.

4. **"No discussion of negative sampling schemes"** — This detail would normally appear in an experimental setup section or appendix. The code is available. Removed per instructions.

5. **"The theoretical equivalence is entirely borrowed and incoherent"** — While the theoretical novelty is limited (as discussed under Minor weaknesses above), calling it "entirely borrowed" is inaccurate. The paper explicitly acknowledges prior work (Remark II, line 136; "a direct consequence" of Zhang et al. 2022 at line 132). The taxonomy and empirical investigation are independent contributions that do not depend on novel theory. The framing oversells, but the section is not incoherent — it correctly contextualizes GAEs within contrastive learning, which is a legitimate synthesis.

6. **"Suspiciously small standard deviations"** — Standard deviations of <1–2% on standard benchmarks with fixed data splits are normal and expected, not suspicious. Many graph SSL papers report similar variance levels.

7. **"No qualitative analysis or case study"** — This is a nice-to-have, not a weakness. The paper's contribution is a framework and benchmark; qualitative analysis is beyond its scope.

---

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's framing as a "comprehensive benchmark" and the actual empirical scope. The paper's genuine strength — the systematic taxonomy (Table 1) that organizes the literature and identifies underexplored configurations — is arguably more significant than the experimental results themselves. The reviews highlight that the taxonomy itself is the core contribution, and the three new variants are useful proof-of-concept demonstrations rather than major algorithmic innovations. The paper would be stronger if it repositioned itself accordingly.

---

## Suggestions

1. **Specify the node classification evaluation protocol in the main text.** State clearly whether linear probing, fine-tuning, or another protocol is used, including the classifier architecture and training details. This is the single highest-leverage fix.

2. **Calibrate the novelty claims.** Replace phrases like "first work to explore contrastive learning principles... in the context of GAEs" with more precise language about providing a unified framework and systematic taxonomy. The paper's honest acknowledgments in Remark II should be reflected in the abstract and introduction.

3. **Either expand the benchmark or narrow the claims.** If the paper claims to be a "comprehensive benchmark," it should include at least one graph-level task and one large-scale dataset. Alternatively, reframe as a "focused benchmark on transductive node and link-level tasks."

4. **Move ablation studies to the main text** (if they currently reside only in the appendix) or add them. At minimum, an ablation varying the three contrastive-view dimensions (graph views, receptive fields, node pairs) while fixing all other components would directly validate the taxonomy.

---
