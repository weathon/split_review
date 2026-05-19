- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary
This paper introduces the first study of **long-distance targeted poisoning attacks** on GNNs, where injected nodes are placed entirely outside the target node's k-hop neighborhood. Two methods are proposed: **MetaLDT**, a bilevel-optimization approach inspired by meta-learning that achieves 84–96% success on small graphs but cannot scale, and **MimicLDT**, a cheaper heuristic that exploits embedding-space "collision" and achieves >55% success on graphs up to arXiv-size (hundreds of thousands of nodes). The paper evaluates against multiple robust GNN defenses and provides stealthiness metrics (degree distribution, homophily).

## Strengths
- **First demonstration of long-distance targeted poisoning**: The paper defines a genuinely new attack scenario — no prior work considered placing injected nodes entirely outside the target's k-hop neighborhood — and shows it is feasible. MetaLDT achieves 84–96% success rate on Cora against vanilla GNNs (Table 1), supporting this originality claim.
- **Scalability breakthrough via MimicLDT**: MetaLDT crashes (OOM) on graphs beyond a few thousand nodes, but MimicLDT successfully attacks arXiv (hundreds of thousands of nodes) with >55% success rate (Table 3). This directly addresses the impracticality of optimization-based attacks on large graphs.
- **Effectiveness against multiple robust GNN defenses**: MetaLDT achieves 84–96% against five defense mechanisms (ProGNN, GNNGuard, SoftMedianGDC, JaccardGCN, SVDGCN) when inner-loop training converges (Table 1). No prior long-distance attack has been evaluated against this range of defenses.
- **Principled heuristic design grounded in observation**: Figure 2 empirically shows that MetaLDT's optimization consistently reduces embedding-space distance between the target node and nodes with the target label. This observation directly motivates MimicLDT's "embedding collision" objective (Section 5), tying the heuristic to theoretically grounded behavior rather than a blind guess.
- **Stealthiness through degree distribution and homophily preservation**: The paper reports Earth Mover's Distance of 0.039±0.002 between poisoned and clean graphs for Cora (Section 6.2), and shows that the homophily constraint keeps injected node features similar to their neighbors' (Figure 4). These provide quantitative evidence of statistical stealth.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims.

### Minor
- **No direct detection experiment against explanation tools.** The paper strongly motivates long-distance attacks by arguing they evade explanation-based detection tools like GNNExplainer (Section 1: "changing nodes close to the target is undesirable because it make attack detection easy"). It validates that short-distance attacks are detectable by GNNExplainer in §E.3, and provides indirect statistical stealth evidence (degree distribution, homophily). However, it never directly tests whether MetaLDT or MimicLDT *themselves* evade GNNExplainer. The logical argument (injected nodes lie outside the k-hop neighborhood and thus affect influence scores) is reasonable, but an explicit experiment would substantially strengthen the paper's central narrative. This is an evidential gap, not a fatal flaw, since the paper's core contribution is the *feasibility* of long-distance attacks, not a claim of proven undetectability.
- **Section 6.3 (end-to-end attacks) sketches an extension without results.** The section describes extending the attack to discrete-text-feature graphs by training a decoder from continuous embeddings to text, but provides no experimental setup, results, or evaluation. This section is currently dangling — either it should be fleshed out with results or removed as out of scope.
- **MetaLDT convergence behavior is partially unexplained.** For defenses where MetaLDT's inner training loop was truncated to 50 epochs (GNNGuard, SoftMedianGDC, ProGNN) due to OOM constraints, success rates drop noticeably. The paper attributes this to early stopping but does not analyze whether MetaLDT is fundamentally incompatible with these defenses or would recover with more compute or architectural changes (e.g., gradient checkpointing). This limits interpretability of the robustness results.
- **MimicLDT experiments use the victim model's weights directly.** The paper acknowledges this (Section 6.2: "Due to time constraint, instead of training a surrogate model, our experiments directly use the weights of models under attack") and validates surrogacy on Cora. However, in a realistic poisoning scenario the attacker would not have access to the post-training weights. While the Cora validation is helpful, extending this validation to larger graphs (PubMed, arXiv) would strengthen practical credibility.

### Trivial
- The paper states the constraint that injected nodes have at most one edge to the original graph (Section 4.1, point c). The justification (avoiding the optimization focusing on a single node) is given, but the rule reads as somewhat ad-hoc; a brief ablation or discussion of alternative constraints would clarify its necessity.

## Nice-to-Haves
- **Report runtime and memory for MimicLDT on PubMed and arXiv.** Table 2 shows data for Cora and Citeseer; explicitly reporting the same for the larger datasets would make the scalability claim more concrete (though the fact that MimicLDT produces results on arXiv in Table 3 already demonstrates feasibility).
- **Add a short-distance injection baseline.** Comparing against a variant of the attack that places nodes inside the k-hop neighborhood (same perturbation type, no distance constraint) would isolate the cost of the long-distance constraint and make the comparison more informative.

## Removed Points
- **Scalability claim is "unsubstantiated."** Removed because the paper does provide success rate results on arXiv (Table 3), which demonstrates that MimicLDT can run on this graph. The critic demanded exact runtime numbers for PubMed/arXiv, but the core scalability claim ("can scale to much larger graphs") is supported by existence of results on arXiv. Missing runtime figures are a Nice-to-Have, not a weakness.
- **"Comparison with short-distance attacks is unfair/uninformative."** Removed because no short-distance injection attack exists to compare against; the paper compares against available modification-based short-distance attacks (Nettack, FGA, IG-FGSM) and is transparent about the success-rate gap. The comparison does not pretend to isolate the distance variable — it contextualizes the results against existing methods.
- **"Injected node constraint (one-edge limit) not justified."** Removed because the paper explicitly states on line 117–118: "a constraint we add to avoid cases where the optimization spends all of its time optimizing a single injected node." The critic's claim that this is "stated without justification" is factually incorrect.
- **"Figure 2 shows a single run; consistency unclear."** Removed because Figure 2 demonstrates a specific empirical observation that motivates MimicLDT's design. The claim is not that this holds universally across all settings, but that this observed behavior inspired the heuristic. The paper's main evaluation of MimicLDT is independent of this figure.
- **Strength Finder strengths about "importance" or generic praise.** Removed per filtering instructions. All remaining strengths above are specific, concrete, and supported by evidence.

## Novel Insights
None beyond the paper's own contributions. The reviews largely converge on the paper's strengths and flag gaps that the authors themselves partially acknowledge (e.g., the surrogate validation limitation). The key insight from synthesizing the reviews is that the paper's most impactful missing piece — a direct detection-evasion experiment — is conceptually straightforward (run GNNExplainer on poisoned graphs and compare influence scores for injected vs. benign nodes) and would substantially elevate the paper's completeness without requiring new methodology.

## Suggestions
- **Run a direct detection-evasion experiment.** Feed graphs poisoned by MetaLDT/MimicLDT through GNNExplainer and measure whether injected nodes receive anomalously high influence scores. This directly tests the paper's central motivating claim.
- **Either flesh out Section 6.3 (end-to-end attacks) with actual results, or remove it.** A sketched extension with no evaluation weakens the paper's finish; commit to it or drop it.
- **Provide a brief analysis of MetaLDT's convergence failures.** For defenses where inner-loop training was truncated, add even a small-scale experiment (e.g., check if gradient checkpointing or a smaller T allows convergence) to distinguish fundamental incompatibility from compute limitations.
- **Report MimicLDT runtime and memory on PubMed and arXiv** explicitly in Table 2 to substantiate the scalability advantage.
- **Add variance/confidence intervals** for success rates on arXiv (if feasible) to match the standard set by the Cora experiments.
