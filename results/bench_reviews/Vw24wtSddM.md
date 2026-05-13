## Summary
The paper proposes Tree Cross Attention (TCA), a cross-attention variant that organizes context tokens into a (k-d) tree, uses a REINFORCE-trained policy to walk root-to-leaf, and applies cross attention over the O(log N) nodes visited/passed. Built on TCA, ReTreever is presented as a token-efficient alternative to Perceiver IO. Empirically it matches Cross Attention with far fewer tokens on a Copy Task, GP regression, image completion, and Human Activity, and outperforms Perceiver IO at equal token budgets.

## Strengths
- **Logarithmic token / memory footprint of the cross-attention step is empirically demonstrated.** Figure 4 (left) shows TCA's inference memory grows logarithmically while CA grows linearly; Table 1 shows TCA matches CA accuracy on the Copy Task using ~50× fewer tokens.
- **Non-differentiable reward formulation is a real, validated design choice.** Table 5 shows accuracy-as-reward substantially stabilizes RL training over negative cross-entropy (99.6 vs 80.3 at N=1024), giving a concrete motivation for the RL framing.
- **Path-based retrieval guarantees coverage in a different sense than Treeformer.** Section 3.3's invariant that every token is either selected or has a selected ancestor distinguishes TCA from leaf-only tree attention (Treeformer's TF-A) and is a cleanly stated design property.
- **Useful loss-weighting ablations.** Figure 3 (middle/right) characterizes the roles of $\lambda_{CA}$ (early-stage stability) and $\lambda_{RL}$ (necessity for convergence), giving actionable training guidance.

## Weaknesses

### Fatal
None.

### Major
- **The "O(log N) inference" headline materially overstates what the method delivers end-to-end.** §3.5 explicitly defines ReTreever's encoder as $\mathbb{R}^{N\times D}\to\mathbb{R}^{N\times D}$ (e.g., a Transformer encoder), so the per-context cost is at best linear and typically quadratic, and the per-query retrieval traversal performs an attention-parameterized policy step at each of $\log N$ levels. The "% Tokens" metric in Tables 1–4 measures only the cross-attention buffer at the final step, not FLOPs or wall-clock. The abstract and introduction do not qualify this; only a careful read of §3.5 reveals it. This is the central marketing claim of the paper.
- **All evaluated benchmarks have queries that are spatially aligned with the k-d tree's split axis.** §3.1 builds the tree by splitting on time (Copy Task / time series), or x/y coordinates (images), and in every task the query is itself a coordinate in that same space. Tree descent then reduces largely to a positional lookup, which trivially explains the perfect Copy Task accuracy. The paper claims TCA as a general efficient cross-attention but never evaluates a setting where the query is not coordinate-aligned with the tree (e.g., content-based / associative retrieval, RAG-style key-value lookup). Without that, "learned retrieval" is conflated with "deterministic spatial indexing wrapped in attention."
- **Missing comparison to natural efficient-attention competitors.** Treeformer (TF-A) is discussed in §5 but never benchmarked; top-k cross-attention, Linformer, Nyströmformer, BigBird are absent from both discussion and experiments. The headline framing — efficiency gains over $\mathcal{O}(N)$ cross attention — needs at least one direct baseline from the efficient-attention family to be informative.

### Minor
- **"Full receptive field" is overstated.** §3.3 calls $\mathbb{S}$ full-receptive-field because every leaf is either in $\mathbb{S}$ or descends from a node in $\mathbb{S}$. But the descendants are represented only by a single aggregated parent vector — high-resolution access exists only along the single chosen path. This is a structural ceiling that helps explain the persistent gap to full Cross Attention in Tables 2–4 (e.g., 3.52 vs 3.88 on CelebA) and deserves explicit acknowledgement.
- **Perceiver IO comparison operating point is questionable.** Forcing $L\approx\log N$ on the Copy Task — a task where, by construction, every token can be queried — operates Perceiver IO below its design capacity. The paper does include Perceiver IO at $L=32$ in Table 2 (matching ReTreever's RBF log-likelihood at higher token cost), which is informative; but §4.1 still draws a general conclusion ("methods which distill information to a lower dimensional space are insufficient") from a task tailored to defeat compression. A more balanced framing would help.
- **No ablation isolating spatial indexing vs. learned policy.** A baseline using the same k-d tree but a fixed coordinate-routing policy (no RL) would clarify how much of TCA's gain is the structure vs. learning, and is missing.
- **Tree-construction heuristic never ablated.** §3.1 advertises tree-construction flexibility but every experiment uses k-d splits on physical coordinates; ball-tree, learned tree, and random tree are never tried.
- **REINFORCE variance is large and alternatives unexplored.** Table 5 shows σ=14.8 at N=1024 with CE reward. Standard differentiable alternatives (Gumbel-softmax / straight-through / soft tree routing) are not compared.

### Trivial
- §3.4 states the policy and CA share weights; an inference-time diagram showing this clearly would help readers.

## Nice-to-Haves
- An end-to-end FLOPs and wall-clock plot including encoder + tree construction + traversal, separating "asymptotic cross-attention cost" from "end-to-end inference cost."
- A non-spatial retrieval benchmark (associative recall with random key bindings, or document retrieval) to test the generality claim.
- A multi-path variant retrieving $k$ leaves to address the single-path resolution ceiling.
- Visualizations of selected tree paths for representative queries to show whether the policy is learning anything beyond coordinate descent.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- *Harsh critic claimed Treeformer comparison is missing.* This is real and kept as a Major concern — but the broader claim of "missing related works" in general is dropped per instructions.
- *Critic asked for confidence intervals / significance testing on Perceiver IO vs ReTreever gap.* Standard deviations across multiple seeds are already reported (e.g., $3.52\pm 0.01$ vs $3.20\pm 0.01$), so the gap is well outside reported noise; this criticism is largely addressed.
- *Strength Finder #1 (large-margin superiority over Perceiver IO).* Dropped as a top-line strength because the Copy Task margin (100% vs 15.2%) reflects a task designed to defeat fixed-latent compression, not a general superiority; Table 2's L=32 row shows the gap closes when Perceiver IO is given headroom. The narrow valid version is captured under "logarithmic memory/token footprint."

## Novel Insights
None beyond the paper's own contributions. The most genuinely interesting observation — that an RL policy parameterized as attention can directly optimize a non-differentiable reward like classification accuracy and outperform CE-as-reward — is already the paper's contribution.

## Suggestions
- Restate the complexity claim honestly: "$\mathcal{O}(\log N)$ cross-attention cost per query, with encoder cost determined separately by the chosen encoder."
- Add at least one non-spatial retrieval task and one efficient-attention baseline (top-k cross-attention, Treeformer TF-A, or Linformer) to support generality.
- Add the fixed-routing tree baseline to disentangle "tree structure" from "learned policy."
- Acknowledge the single-path resolution ceiling in §3.3 and discuss when it matters.

## Evaluation Axes
- **Originality:** Moderate. Tree-structured attention is well established; the novelty is applying it specifically to cross-attention with an RL-trained traversal and the path-based selection invariant.
- **Importance:** Reasonable. Token-efficient cross-attention is a useful goal, though the evaluated regime (N≤1024) is modest.
- **Claim support:** Weak on the headline complexity claim; reasonable on the narrower "fewer tokens at the CA step" claim.
- **Soundness of experiments:** Adequate within scope but the scope is narrow and biased toward spatial-coordinate queries; efficient-attention baselines are absent.
- **Clarity:** Good — method and ablations are easy to follow.
- **Value to community:** Moderate — the path-selection invariant and RL framing are reusable ideas, but the empirical case for generality is not yet made.

## Score and Decision

Anchors considered:
- `nkUQPOwYy0.md` (Fast Multipole Attention) — avg 5.00. Closest analog: hierarchical/multi-resolution attention, $\mathcal{O}(N\log N)$ claim, small-scale experiments, missing strong baselines and ablations. Reviewers rejected on similar grounds (missing vanilla baseline, no ablations). TCA is comparable: stronger ablations on losses and a more specific RL contribution, but suffers analogous issues with limited baselines and overstated generality.
- `jMZglnlwf7.md` (Tree Attention for decoding) — avg 5.00. Tree-structured attention efficiency paper; mixed reception. Comparable territory.
- `ESq3U7z6FD.md` (EHI: hierarchical index for dense retrieval) — avg 6.00. End-to-end learned hierarchical index; more directly tests retrieval, stronger experimental scope than TCA. TCA is weaker than this anchor.
- `xvhjRjoFCN.md` (BiXT: bi-directional cross-attention vs Perceiver) — avg 4.33. Similar Perceiver-comparison framing; received a 1 from one reviewer.
- `VjHOGqHC4I.md` (Long LoRA Perceiver variants) — avg 3.50, clearly weaker than TCA.
- `PWtx9fJqM5.md` (Linear transformations in attention) — avg 5.00, comparable methodological scope.
- `v0FzmPCd1e.md` (Selective Attention) — avg 6.75, accept. Larger-scale LM experiments, cleaner generality; TCA is weaker.
- `s1kyHkdTmi.md` (Evolved Universal Transformer Memory) — avg 7.00, accept. More extensive evaluation and stronger generality; TCA is weaker.
- `IIVYiJ1ggK.md` (Rodimus efficient attentions) — avg 6.00, accept. LM-scale evaluation; TCA does not match this scope.
- `fi9LF92Cak.md` (Trident block) — avg 4.75, comparable lower-end.
- `xThb6APBoG.md` (RL for retrieval task-specific goals) — avg 4.00, RL-for-retrieval framing, similar concerns about scope.
- `BPAZ6yW3K7.md` (LeReT, RL-enhanced retrieval) — avg 6.00, accept, broader and more convincing evaluation.
- `oqRe1KvD17.md` (Reward-RAG) — avg 3.00, weaker than TCA.
- `vnp2LtLlQg.md` (Optimizing Attention) — avg 3.00, weaker.
- `moXtEmCleY.md` (Hierarchical tree memory for LLMs) — avg 6.00, accept; broader empirical case.
- `TbTJJNjumY.md` (Linear cross-attention for VRP) — avg 6.25, accept.
- `J5s6EG6ual.md`, `q541p2YLt2.md` — avg 3.0 / 2.5, clearly weaker than TCA.

TCA most closely aligns with Fast Multipole Attention (5.00): a reasonable hierarchical-efficiency idea with solid narrow experiments but overstated complexity claims, limited baselines, and a narrow evaluation regime. It is clearly above the 3.0–4.0 cluster (real method, real ablations, clean writing) and clearly below the 6+ accept cluster (which all bring substantially more evaluation breadth or stronger generality evidence).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>