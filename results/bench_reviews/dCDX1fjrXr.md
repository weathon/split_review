## Summary

The paper introduces Sparse Labels Node Classification (SLNC), a node-classification setting with extremely few labels sampled over the whole graph rather than guaranteed per class. It proposes ELI, which estimates an unsupervised pseudo-label/similarity structure, uses it for selecting key labeled nodes, and incorporates the resulting graphs into LP- and SGC-style propagation through averaged Laplacians. The reported results show substantial gains over LP, SGC, DGI, GMI, and CGPN across several benchmark graphs, but the central experimental protocol is inconsistent with the claimed random-label setting.

## Strengths

- **The paper targets a concrete and under-examined sparse-label protocol.** Section 3 defines SLNC as the case where only very few labeled nodes are available and “these labeled nodes are not chosen on a per-class basis, but randomly over the entire set of nodes” (lines 55–57). This is meaningfully different from standard semi-supervised node classification protocols that assume fixed labels per class.

- **The method has a specific mechanism for using unsupervised structure without requiring pseudo-label IDs to match true class IDs.** Section 4.3 explicitly notes the permutation mismatch between the unsupervised pseudo-label matrix \(H\) and the true label matrix \(Y\), and instead uses \(H\) through a graph Laplacian \(L_{\mathcal G_H}\) to impose smoothness (lines 99–105). This is a plausible way to exploit cluster/similarity information without directly aligning cluster IDs to class IDs.

- **The framework is instantiated for both LP and SGC.** The paper derives an LP-style objective with averaged Laplacians over the original graph, pseudo-label graph, and labeled-node graph (lines 101–122), and then applies the same averaged adjacency idea to SGC (lines 140–143). The experiments compare LP-ELI and SGC-ELI to their non-ELI counterparts.

- **The empirical evaluation spans several standard attributed graph benchmarks.** The paper evaluates on citation networks, a web graph, co-purchase networks, and a coauthor graph (lines 156–159), and runs each experiment 10 times with means and standard deviations (lines 167–172).

- **The paper acknowledges at least one important assumption.** The limitation section notes that ELI requires knowing the number of classes in advance (line 243), which is indeed a substantial structural assumption for an unsupervised pseudo-labeling approach.

## Weaknesses

### Fatal

- **The core protocol is internally inconsistent: SLNC is defined and evaluated as random sparse labels, but ELI’s method description actively selects labeled nodes.** Section 3 defines the task as labels chosen randomly over all nodes (lines 55–57), and Section 5.2 says training nodes are randomly selected as \(\#num \times c\) over the whole node set (lines 170–172). However, Section 4.2 says ELI’s second phase is “to select a label node set \(\mathcal V_L\)” and chooses \(l_H\) nodes from each pseudo-label class, using the nodes with smallest clustering-model loss (lines 81–84). This is not a minor wording issue: if ELI is allowed to choose which nodes get labeled, then it is solving an active label-acquisition/core-set selection problem, not the random-label SLNC problem as defined. If instead the labels are truly randomly fixed in the experiments, then the key-node-selection part of ELI is not actually usable/evaluated. This ambiguity directly undermines the headline claim that ELI improves learning under randomly provided sparse labels.

### Major

- **The baselines do not match the advantage ELI appears to use.** If ELI selects key nodes for labeling, then the relevant comparisons are active learning, diversity sampling, clustering-based querying, or simple “cluster then query representative nodes” baselines under the same label budget. The current baselines—LP, SGC, DGI, GMI, and CGPN—mostly test learning from a given labeled set, not whether ELI’s label-selection strategy is better than other selection strategies. Conversely, if labels are fixed randomly for all methods, then Section 4.2’s selected-label component should be removed or separately evaluated.

- **The experiments do not report class coverage in the sparse random-label regime, even though missing classes are central to the problem.** The motivation repeatedly emphasizes that random sparse labels may omit entire classes (e.g., line 16 and Section 3), but the results do not report how many classes are represented in each sampled training set, how often classes are missing at \(1c,2c,3c,4c\), or how accuracy changes conditional on class coverage. This matters because ELI’s pseudo-cluster-based selection could improve performance primarily by increasing true class coverage, rather than by improving sparse-label propagation.

- **The reported gains conflate label selection, pseudo-label graph construction, graph augmentation, and classifier choice.** ELI includes unsupervised clustering/label-distribution estimation, key-node selection, construction of \(L_{\mathcal G_H}\) and \(L_{\mathcal G_Y}\), and a KNN/SVD optimization of the pseudo-label graph. The main reported comparison is mostly “LP/SGC with ELI” versus “LP/SGC without ELI” (Section 5.6), so it is unclear whether improvements come from estimated label information, from selecting more representative labeled nodes, from adding a dense/sparse feature-similarity graph, or from the SGC classifier. This weakens the causal interpretation of the method.

- **Several core algorithmic details are underspecified or ambiguous in the main method description.** Section 4.2 says nodes are chosen by “the smallest loss used by the Label distribution estimation model,” but the clustering loss described in Section 4.1 is global, \(\|FF^\top-HH^\top\|_F^2\), not clearly a per-node score. Section 4.3 defines \(Y \in [0,1]^{n\times l}\), where \(l\) is the number of labeled nodes, while the rows are described as class-indicator vectors; the natural dimension should be tied to the number of classes. These details affect reproducibility and, more importantly, the interpretation of how missing classes are handled.

### Minor

- **The paper overclaims generality to arbitrary GNNs.** Section 4.5 says the framework can generalize to “any other GNN framework” by using the averaged adjacency (line 143), but the paper only evaluates LP-ELI and SGC-ELI. This claim is too broad, since replacing the adjacency can interact differently with attention-based, residual, heterophily-aware, or higher-order architectures.

- **The “estimated label information” interpretation is not directly validated.** The method assumes the unsupervised pseudo-label space \(H\) captures useful label-distribution structure, but the paper does not show pseudo-label purity, NMI/ARI, pseudo-cluster/true-label confusion, or any other evidence that \(H\) correlates with true labels. Since Section 4.4 later replaces \(HH^\top\) with a KNN graph built from the SVD of \(F\), it is especially important to distinguish “estimated labels” from generic feature/embedding similarity.

- **The CGPN comparison is incomplete on larger datasets.** The paper explains that CGPN was too slow and was stopped on Pubmed, CS, Computers, and Photo (line 236). Runtime is a legitimate concern, but omitting an explicitly sparse-label baseline from several datasets leaves the accuracy comparison less complete; this should be accompanied by a clearer scalability/runtime comparison and a fair statement of what can and cannot be concluded.

- **Accuracy alone is not fully diagnostic for this setting.** Since the central difficulty is sparse random labels with possible class omission, macro-F1, per-class accuracy, and performance stratified by class coverage would be more informative than only overall accuracy. This is not fatal, but it would substantially clarify the empirical story.

### Trivial

None.

## Nice-to-Haves

- Include an explicit table for each label budget reporting the number of represented true classes in the labeled set, for both random labels and ELI-selected labels if applicable.
- Add simple diagnostic baselines: random labels + ELI graph only; ELI-selected labels + original LP/SGC only; clustering/KNN query without ELI propagation; KNN graph from features without pseudo-label clustering.
- Report pseudo-label/true-label alignment metrics such as NMI, ARI, purity, or pseudo-cluster confusion matrices.
- Make the task framing unambiguous: either present ELI as a method for fixed random sparse labels, or reframe it as active label acquisition under sparse budgets.
- If the active-selection version is intended, compare against graph active learning, degree/diversity sampling, and cluster-representative querying baselines.

## Removed Points

These points are flagged to be removed or treated with caution:

- **Code release / availability concerns.** The paper states code is attached and will be released later (line 152), but criticisms about release status or independent availability should not be used in the evaluation.
- **Typos, grammar, capitalization, broken symbols, and formatting artifacts.** The provided text is extracted from PDF, so parser artifacts should not count against the paper.
- **Missing appendix-level details or missing appendix ablations/sensitivity plots.** The text references appendices for KNN construction and sensitivity studies (line 136), and the extraction may omit appendices. Therefore, I do not treat the mere absence of appendix content in the extracted file as a standalone flaw.
- **Generic “important problem” praise.** The problem is indeed meaningful, but generic importance alone is not a substantive strength unless tied to the paper’s specific SLNC definition and protocol.
- **Broad missing-related-work complaints.** I do not rely on external related-work claims beyond the protocol-relevant need for active-learning or cluster-query baselines if ELI is selecting labels.
- **Statistical-significance criticism as a major flaw.** The paper reports 10-run means and standard deviations. Additional tests would be useful, but the lack of formal significance testing is not a central weakness here.

## Novel Insights

The most important synthesis is that ELI is potentially two different papers: one about **learning from fixed random sparse labels**, and one about **choosing which nodes to label using unsupervised pseudo-clusters**. Both are legitimate research directions, but the current submission blends them in a way that makes the main empirical gains hard to interpret. If ELI’s gains come from better node selection, then the paper should be evaluated as graph active learning; if they come from better propagation under fixed random labels, then the key-node-selection component must be removed from the evaluation or isolated.

## Suggestions

- **Clarify the experimental protocol precisely.** State whether LP-ELI and SGC-ELI use the same randomly sampled labeled nodes as LP/SGC, or whether ELI selects/queries different nodes.
- **If labels are fixed randomly:** remove or disable Section 4.2 in the main experiments, and show that ELI improves LP/SGC using exactly the same labeled set as every baseline.
- **If ELI selects labels:** reframe the paper as active label acquisition and compare against active learning and cluster-representative selection baselines.
- **Report class coverage.** For each dataset and budget, show the distribution of represented true classes across the 10 runs.
- **Add component ablations.** At minimum isolate: label selection only, pseudo-label graph only, \(L_{\mathcal G_Y}\) only, KNN graph only, and full ELI.
- **Define the node-selection score mathematically.** If the score is derived from \(\|FF^\top-HH^\top\|_F^2\), specify the per-node decomposition used.
- **Correct or clarify matrix dimensions.** In particular, explain whether \(Y\) has dimension \(n\times c\), \(n\times l\), or some restricted label-index space when classes are absent.
- **Moderate generality claims.** Replace “any other GNN framework” with a narrower claim supported by the LP and SGC experiments, unless additional GNN backbones are evaluated.

## Score and Decision

**Originality:** Moderate. The SLNC framing is useful, and combining unsupervised clustering/similarity graphs with sparse-label propagation is a reasonable idea, but the components are mostly adaptations of known clustering, label propagation, and graph smoothing mechanisms.

**Importance:** High. Extremely sparse, non-class-balanced node labeling is a practically important setting.

**Support for claims:** Weak. The central claim is not well supported because the method description appears to change the label protocol from random sparse labels to selected/query labels.

**Experimental soundness:** Weak to moderate. The paper uses multiple datasets and repeated trials, but the protocol ambiguity and lack of class-coverage analysis seriously limit interpretability.

**Clarity:** Mixed. The high-level motivation is understandable, but important algorithmic details and the label-selection protocol are unclear.

**Value to the community:** Potentially useful if reframed and evaluated correctly, but the current version does not establish the claimed result.

### Calibration against retrieved human-review anchors

| Anchor | Avg score | Comparison |
|---|---:|---|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TlFDFKyEIQ.md` | 3.50 | Similar graph/label-propagation area; low score aligns with serious methodological concerns. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VyMW4YZfw7.md` | 3.00 | Similar node-classification/spectral-GNN setting; this paper is somewhat stronger empirically but has a more central protocol conflict. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nFcgay1Yo9.md` | 5.75 | Pseudo-labeling under limited annotations; stronger because its protocol appears more coherent. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hESD2NJFg8.md` | 6.50 | High-scoring sparse/label-free node-classification anchor; compared to it, this paper has weaker protocol clarity and less convincing component validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3X3LuwzZrl.md` | 6.50 | High-scoring label-propagation/message-passing paper; this paper is below it due to unsupported central claims. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wJPMe9UKow.md` | 5.50 | Borderline label-smoothing/node-classification paper with stronger empirical breadth but questions about mechanism; this paper’s core protocol issue is more severe. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/89A5c6enfc.md` | 5.75 | Related graph diffusion/noisy-label work; this paper is below it because its task definition and method do not align cleanly. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nRD5TriJ0O.md` | 4.60 | Active-learning graph paper with overclaims and baseline/protocol issues; this paper is below it because its random-vs-selected-label mismatch is more fundamental. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/t7vXubuady.md` | 5.50 | Active-learning paper with fairness concerns but less central task contradiction; this paper is lower. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GbXn0Dgf7f.md` | 3.40 | Low-scoring active-learning benchmark with weak protocols; this paper is comparable because protocol validity is the main issue. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bvjcMvMn7B.md` | 5.75 | Graph active learning with scarce labels; this paper would need to be reframed and compared similarly to approach that score range. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/om5z1n0mXA.md` | 6.00 | Fair-protocol graph benchmarking anchor; this paper falls well below because the experimental protocol is not clearly fair. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/j4VMrwgn1M.md` | 6.75 | High-scoring scarce-label node-classification anchor; this paper lacks comparable methodological and empirical rigor. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/h51mpl8Tyx.md` | 6.20 | High-scoring self-training/limited-label anchor; this paper’s pseudo-label mechanism is less isolated and less validated. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/a2ljjXeDcE.md` | 6.20 | Limited-label node-classification method with clearer experimental framing; this paper is below. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wYvuY60SdD.md` | 6.00 | Node-classification method with clearer model contribution; this paper’s contribution is less established. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VfYShlQbj7.md` | 5.00 | Borderline GNN distillation/limited-data paper; this paper is lower because the main claim is not reliably evaluated. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4UP387Adir.md` | 5.50 | Medium graph contrastive/weak-label paper; this paper is below due to protocol inconsistency. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aJl5aK9n7e.md` | 5.25 | Medium theoretical semi-supervised node-classification anchor; this paper has more empirical breadth but less sound protocol. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pL8ws91RW2.md` | 2.60 | Very low-scoring graph SSL/low-label paper with limited novelty and weak baselines; this paper is stronger in motivation and empirical scope, so I score above it. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XWb6dPuhmC.md` | 3.00 | Low-scoring node augmentation paper with weak motivation; this paper is slightly stronger but similarly undermined by evaluation concerns. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FbLuklVaX7.md` | 4.00 | Low-scoring heterophilic node-classification paper with questionable assumptions; this paper is around this level but below if the protocol mismatch is unresolved. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kZvkcc4mXi.md` | 3.50 | Low-scoring graph self-supervised/edge-construction paper; similar severity due to unclear mechanism and evaluation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PuKRVPXXpR.md` | 3.50 | Low-scoring node-classification alternative with limited contribution; comparable overall quality. |

Relative to the calibration set, this paper is stronger than the very weakest low-label graph papers because it has a concrete problem framing, multiple datasets, and a plausible mechanism. However, it is below the borderline 5–5.75 anchors because the main experimental claim may be measuring active label selection rather than random sparse-label learning. I assign **3.5**.

## Score and Decision

**Score: 3.5 / 10**  
**Decision: Reject**

MY FINAL SCORE: <pineapple>3.5</pineapple>  
MY FINAL DECISION: <orange>Reject</orange>