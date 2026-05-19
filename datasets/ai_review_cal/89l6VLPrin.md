- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6
Now I have all the verified information. Let me produce the final consolidated review.

---

## Summary

This paper presents a unified framework for node-level graph representation learning, showing that both graph drawing (2D layouts) and graph contrastive learning (high-dimensional embeddings) can be approached via neighbour embedding methods. It introduces graph t-SNE for 2D layouts (non-parametric, using the graph adjacency matrix directly as the affinity matrix for t-SNE optimization) and graph CNE for node-level contrastive learning (parametric MLP-based, using graph edges as positive pairs with InfoNCE loss). Graph t-SNE is strongly supported empirically, consistently outperforming three baselines across six datasets by large margins. Graph CNE is presented as a simpler alternative to existing GCL methods that achieves competitive results without a GCN architecture, but its evaluation has a significant comparison-fairness concern.

## Strengths

- **Graph t-SNE achieves substantially better local structure preservation than existing graph layout algorithms.** Figure 3 shows graph t-SNE winning on all six datasets on both kNN recall and kNN accuracy (12 out of 12). The paper reports average improvements of 18.2 percentage points in kNN recall and 6.7 percentage points in kNN accuracy over the best competitor. These are large, consistent gains verified from the paper's own re-runs of all baselines on the same data.

- **Conceptual and practical simplicity.** Both methods are direct applications of existing neighbour embedding frameworks (t-SNE and CNE) with minimal modification: graph t-SNE simply replaces the kNN graph with the graph adjacency matrix and uses openTSNE with default parameters; graph CNE uses the InfoNCE loss with graph edges as positive pairs, no augmentations or complex heuristics. This contrasts with prior work (tsNET, DRGraph, t-FDP) that required custom implementations and approximations.

- **Clean conceptual unification of graph drawing and GCL.** The paper explicitly ties together two normally distinct paradigms under a single neighbour-embedding framework, and introduces parametric 2D embeddings as a "missing link" between the two tasks (Section 7). This provides a coherent conceptual contribution that goes beyond the sum of the two individual methods.

- **Honest treatment of limitations.** Section 7 explicitly acknowledges that graph t-SNE may perform poorly on simple planar graphs / Swiss-roll-type manifolds, and that graph CNE's MLP architecture is a deliberate design choice rather than an oversight. The paper also transparently reports variance over five runs for its own method.

## Weaknesses

### Fatal
None.

### Major

- **The abstract overclaims graph CNE's performance.** The abstract states that graph CNE achieves "state-of-the-art linear classification accuracy." However, Table 2 (and the paper's own description on line 178) shows that graph CNE achieves the best result on only 1 out of 6 datasets (PUB), and is below the best GCN-based method on the other five. On ARX, it trails the best baseline by over 16 percentage points. The body text more accurately uses "comparable performance" (line 178, 193), but the abstract's stronger claim is not supported by the paper's own data.

- **The comparison between graph CNE and existing GCL methods in Table 2 lacks transparency about evaluation protocols, which may invalidate the comparison.** The paper's linear evaluation uses 2/3 of nodes for training (Section 4, line 130: "the same train/test split" as the 2/3-1/3 split described for kNN accuracy). The baseline numbers are taken from Zhang et al. (2022) and Guo et al. (2023) without specifying what training protocol those baselines used. The standard protocol in the GCL literature (e.g., DGI, GRACE, GCA, BGRL) uses 20–30 labeled nodes per class for linear evaluation — a dramatically smaller training set. On Cora, for instance, 2/3 training is ~1800 nodes versus ~140 for 20-per-class. If the baselines indeed used the standard small-training-set protocol, the comparison in Table 2 is invalid and graph CNE's competitiveness against GCN-based methods is unsubstantiated. The paper must clarify the baselines' protocol or re-run baselines under its own protocol to make a fair comparison.

### Minor

- **Graph t-SNE's claim of outperforming "all existing algorithms" (abstract, line 4) overstates the scope of the evaluation.** The paper tests against only three baselines (FDP, DRGraph, t-FDP). While these include two recent state-of-the-art methods, the claim should be scoped to the specific algorithms tested, particularly since well-known alternatives (ForceAtlas2, sfdp) are discussed in the Related Work but not compared.

- **Potential preprocessing mismatch for baseline comparisons.** The paper restricts all datasets to the largest connected component (LCC, line 111). It does not clarify whether the baseline numbers taken from Zhang et al. (2022) and Guo et al. (2023) also used LCC-only preprocessing. For datasets like Amazon Computers and Photo, the LCC is smaller than the full graph; if baselines used the full graph, this compounds the comparison concern for Table 2.

- **No error bars or variance reported for the baseline methods in Table 2.** The paper reports mean ± std over five runs for graph CNE but cites single numbers for baselines without variance. While common practice, this asymmetry makes it difficult to assess whether differences are meaningful.

### Trivial
None.

## Nice-to-Haves

- **Test-time node inference experiment.** The paper motivates using an MLP over GCN by arguing that GCN cannot embed a single held-out node without re-training (Section 7). An experiment demonstrating this capability (e.g., training on a subset of nodes and embedding new nodes at test time) would concretely substantiate this claimed advantage.
- **Broader graph layout baselines** (e.g., ForceAtlas2, sfdp) would strengthen the "outperforms all" claim for graph t-SNE, though the observed improvements over the tested methods are already substantial.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about missing related works.** Removed per policy — missing related works cannot be verified without external sources.
- **Criticism about implausible or unverifiable results based on assumed normalization.** Not present in the paper, not applicable.
- **Formatting/style nitpicks.** Removed per policy — parser artifacts are not author errors.
- **Strength Finder's claim that graph CNE "directly supports the claim of state-of-the-art linear accuracy."** Removed because this conflicts with the verified weakness (abstract overclaim; CNE best on only 1/6 datasets). The weakness finding takes priority.
- **Strength Finder's characterization of graph CNE as achieving "comparable" performance to GCN-based methods.** Weakened to reflect that the comparison may be invalid due to the training protocol mismatch.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface a verification gap in the GCL evaluation and confirm the strength of the graph t-SNE results, but do not offer observations that the paper itself does not already contain or imply.

## Suggestions

1. **Fix the abstract.** Replace "state-of-the-art linear classification accuracy" with a more measured claim such as "competitive linear classification accuracy, outperforming other MLP-based GCL methods" — this is what the data actually support.
2. **Clarify or fix the GCL comparison.** Either (a) re-run baselines under the paper's own 2/3 training protocol to enable a direct apples-to-apples comparison, or (b) adopt the standard 20/30-labels-per-class protocol and re-evaluate graph CNE under that setting. Without this, the central claim of graph CNE's competitiveness is not supported.
3. **Clarify the baselines' preprocessing.** State whether the cited baseline numbers from Zhang et al. (2022) and Guo et al. (2023) used LCC-only preprocessing, and if not, discuss the potential impact.
4. **Scope the graph t-SNE claim.** Replace "all existing algorithms" with "all tested algorithms" or explicitly list the comparison set.
