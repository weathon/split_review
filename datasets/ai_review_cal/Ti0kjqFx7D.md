- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper identifies that model editing (correcting a model's prediction on specific misclassified nodes) is uniquely challenging for Graph Neural Networks because changes propagate through message passing. The authors first demonstrate empirically that fine-tuning a single node's prediction causes up to ~50% accuracy drops in GNNs, then visualize the sharp KL divergence landscape of GNNs to explain this phenomenon. They propose EGNN, which stitches a compact trainable MLP onto a frozen GNN and only updates the MLP during editing, thereby decoupling editing from neighbor propagation. The proposed method is intuitive and well-motivated by the observed pathology.

## Strengths

- **Empirical demonstration that GNNs are fundamentally harder to edit than MLPs (Table 1).** The paper systematically shows that fine-tuning a single node with gradient descent causes accuracy drops of up to 49.31% (GraphSAGE on ogbn-arxiv), while the same procedure on an MLP causes only 7.52% drop. This spans four datasets (Cora, Flickr, Reddit, ogbn-arxiv) and two GNN architectures. This finding concretely establishes the paper's core motivating observation.

- **Loss-landscape analysis provides a principled explanation for the pathology.** Figure 1 (described in §3.2) visualizes the KL divergence between pre- and post-edit node representations, showing that GCN and GraphSAGE have sharp landscapes (small weight perturbations → large representation shifts) while MLPs are flatter. Figure 3.2 also includes EGNN's landscape, claimed to be the flattest among all compared architectures, directly linking the proposed solution back to the diagnosed cause.

- **Novel and principled method design.** EGNN's approach of freezing GNN weights and stitching a small MLP that is trained with a locality-preserving KL loss (§3.3, Algorithm 1) directly addresses the propagation issue. The design is simple, interpretable, and follows naturally from the paper's own analysis.

## Weaknesses

### Fatal
- None verifiable from the paper as written. (The paper as provided here is truncated, but this may be a parser artifact; see Major.)

### Major

- **The paper as provided to the reviewer lacks any experimental evaluation section.** The text cuts off at the end of §3 (Proposed Methods). The abstract and introduction claim "up to 90% improvement in overall accuracy" and "more than 2× savings in memory and time," but no experimental results, baselines, ablations, or comparisons appear in the material. This makes the paper's core empirical claims unverifiable. *Caveat: this may be a PDF-parser truncation issue rather than a submission flaw; if so, the authors should ignore this point.*

- **The motivation experiment (§3.1, Table 1) overclaims relative to what it actually tests.** The abstract claims "existing model editing methods significantly deteriorate prediction accuracy (up to 50% accuracy drop) in GNNs," and the introduction says "existing editors significantly harm the overall node classification accuracy." However, the experiment only tests *naive gradient descent fine-tuning on a single node* — it does not test any actual model editing method (e.g., ENN, MEND, SERAC). Naive fine-tuning causing accuracy drops is a known result even in vision/NLP. The experiment validly shows that *GNNs are harder to edit than MLPs* when using simple fine-tuning, which serves its purpose as motivation. But the language in the abstract/intro frames it as a critique of "existing methods" rather than as a discovery about GNNs' inherent sensitivity. This is an overclaim and should be corrected.

### Minor

- **The KL locality loss formulation is underspecified.** The paper writes `KL(h_v + g_Φ(x_v) || h_v)` where `h_v` is called a "node embedding at the last layer." KL divergence requires probability distributions as inputs. In knowledge distillation practice, the intended meaning is `KL(softmax(h_v + g_Φ(x_v)) || softmax(h_v))`, but this is never stated. The paper also refers to `h_v` as both an "embedding" and a "prediction" (line 240), which creates confusion about whether the GNN's classifier layer is part of the frozen GNN or subsumed by the MLP. A brief clarification would resolve this.

- **The "theoretical" claim is asserted without development.** Line 173 states "We theoretically show that when model editing corrects the model predictions on misclassified nodes, GNNs are susceptible to altering the predictions on other connected nodes." No theoretical analysis follows in the provided text (it may have been in a dropped section). If no formal theory exists, this claim should be removed; if it does, it should be included in the main paper.

### Trivial
- Line 50: "we found want to correct" — appears to contain an editing artifact ("found want to").
- Figure captions reference figures (Fig. 1) that are not visible in the text (parser issue; not the authors' fault).

## Nice-to-Haves
- The main experimental evaluation would ideally compare EGNN against existing model editing methods (ENN, MEND, SERAC) adapted to GNNs, not just against naive fine-tuning. This is standard practice and would strengthen the paper.
- An analysis showing that edits on one node generalize to similar nodes (same class, similar neighborhoods) would directly support the generalizability claim in the abstract.
- The MLP training phase (§3.3, "Before editing") uses labeled training data. The paper should clarify whether this creates an unfair comparison — i.e., whether baselines also receive this additional warm-up.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper does not mention any existing graph-specific editing work"** — The paper claims to be the first to propose model editing for graphs (line 93). If no prior work exists, this is not a weakness.
- **"GNNs trained inductively on subgraphs may artificially weaken GNNs"** — This is a known setup choice in transductive vs. inductive settings; the paper explicitly describes the choice (lines 145-146) and it is a standard evaluation protocol.
- **"The edit procedure iterates until correction with no constraint on steps"** — Many editing methods (e.g., ENN) use an iterative correction procedure without explicit step limits; this is not unusual.
- **"Scalability claims require runtime benchmarks"** — This is a reasonable experimental request but it belongs in the experiments section, which is absent; noted above as a missing-section issue.
- **"The sharp loss landscape link to neighbor propagation is not proven"** — The paper provides a plausible mechanism and supports it with the landscape visualization; formal proof is not required for an empirical motivation.
- Several formatting/style nitpicks, speculative concerns about confounders, and scoping critiques ("paper should discuss when EGNN might fail") that are not standard evaluation criteria for a new-method paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the core assessment — the paper has a clear motivating observation, a reasonable proposed solution, and the experimental evaluation is missing or insufficiently described. The harsh critic's framing of "strawman baseline" overstates the issue (the motivation experiment is valid for what it tests; the overclaim is in the abstract's wording), and several of the critic's concerns are speculative or based on missing sections that may be parser artifacts. The strength finder accurately identifies the paper's concrete contributions.

## Suggestions

1. If the experiments section exists in the original submission, the review should be re-evaluated with access to that content. If it does not, the paper must be completed with a full experimental evaluation before it can be reviewed.
2. Correct the abstract and introduction to avoid claiming that "existing model editing methods" fail when only naive fine-tuning was tested. The motivation experiment is still meaningful when framed as "GNNs are fundamentally harder to edit than MLPs."
3. Clarify the KL loss formulation: state explicitly whether softmax is applied before computing the KL divergence over the logit vectors.
4. Clarify whether the GNN's original classifier layer is frozen and used on `h_v + g_Φ(x_v)`, or if the MLP subsumes the classification head.
5. Either provide the theoretical analysis referenced in line 173 or remove the claim.
