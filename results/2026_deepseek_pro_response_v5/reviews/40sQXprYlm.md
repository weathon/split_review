Now let me produce the final consolidated review.

---

## Summary
This paper introduces Distributed Neural Architectures (DNA), where tokens or patches are dynamically routed through a pool of computational modules rather than following a fixed feed-forward sequence. The authors train DNA models on ImageNet (vision) and FineWeb-Edu (language), demonstrating competitive performance against dense baselines while analyzing emergent routing structures, path specialization, and compute allocation. The work is explicitly exploratory — aiming to show feasibility rather than beat state-of-the-art.

## Strengths
- **Competitive performance against dense baselines across two domains**: Vision top-1 DNA achieves 79.1% ImageNet accuracy vs. ViT-small's 79.8% (Table 1), a 0.7% gap. Language top-2 DNA outperforms GPT-2 medium on 6 of 8 benchmarks (Table 3) including validation loss (2.674 vs 2.720), BoolQ (61.0 vs 60.5), and HellaSwag (41.8 vs 40.5). This provides substantive evidence that distributed architectures are trainable and viable.
- **Clean conceptual unification**: DNA subsumes feed-forward networks, Mixture-of-Experts, Mixture-of-Depths, weight sharing, and early exit as special cases (Section 2.1), and the paper demonstrates that a mixture of these behaviors emerges from end-to-end training.
- **Emergent parameter reuse without explicit incentives**: 15–25% of parameters are reused at inference time (Section 3.3) despite no load-balancing or weight-sharing loss. Cross-model correlation in vision confirms this reuse is not random for that domain.
- **Sparse, dynamic attention as a novel form of data-dependent sparsity**: Patches routed through different modules do not attend to each other (Fig. 1e), producing naturally sparse attention patterns that emerge from the architecture rather than being hand-crafted.
- **Honest presentation of limitations and controls**: The paper includes a random-model baseline for path distributions (Fig. 1c,d), acknowledges that module reuse in language is "most likely random" (Section 4.3), and explicitly states the work is "not focused on beating SOTA" (footnote 3).

## Weaknesses

### Fatal
None.

### Major
- **Interpretability evidence is qualitative and anecdotal**: Claims about path specialization and routing interpretability rest on hand-picked examples — four paths from thousands (Fig. 3), three reconstructed images (Fig. 4), two example paragraphs for router grouping (Section 4.2). There is no quantitative metric for specialization, no statistical test of whether observed groupings differ from chance, and no systematic comparison to dense model representations. The paper's own random-model footnote (footnote 5) admits that random DNAs also cluster images, which further weakens the interpretability narrative without stronger quantitative evidence.
- **Parameter count mismatch complicates competitiveness claims**: DNA models carry more total parameters than dense baselines in most configurations (e.g., 583M vs 406M for language top-1, 34M vs 22M for vision top-1). The "active parameters" framing is helpful but does not replace total-parameter-matched comparisons. The top-2 DNA with 30% skip actually underperforms the 30% shallower GPT-2 baseline (2.784 vs 2.772 loss, Table 3), suggesting compute efficiency gains are not yet clearly demonstrated at matched compute budgets.

### Minor
- **The power-law path distribution is partially an architectural artifact**: The paper itself reports that randomly initialized DNA models also produce power-law path distributions with exponent −1 (Fig. 1c,d caption). The trained exponent shift (−1.0 to −1.2 for language) is the only difference attributed to training, and no significance test or analysis of what drives this shift is provided. This weakens the claim that path distributions are evidence of learned structure.
- **"Any order" claim overstates implementation**: The abstract claims tokens can traverse modules "in any order," but the implementation uses a fixed sequence of routers (one per step) with a cap s_max, plus N_b hard-coded backbone layers. The paper acknowledges this constraint ("this is not the most general way" in Section 2.2), but the abstract's framing is stronger than what is implemented.
- **The bias-based skip controller complicates "emergent" framing**: The identity module bias update rule (Eq. 3) is an explicit, hand-designed controller pushing the model toward a target skip ratio r. This is a reasonable engineering choice, but the paper simultaneously claims compute allocation is an emergent property, which overstates the case.
- **Missing architectural hyperparameter from main text**: Key values like s_max (maximum steps per token) are not reported in the main text or tables, making it difficult to assess the actual compute budget and how routing is constrained.

### Trivial
- **"Not feed-forward" terminology is imprecise**: The abstract describes DNA as "not feed-forward," but Section 2.1 clarifies the forward pass is "fully causal" and sequential through steps. The novelty is in per-token dynamic routing, not in recurrence or feedback loops.

## Nice-to-Haves
- Report FLOPs per forward pass (average and distribution) rather than relying solely on parameter counts and active parameter ratios.
- Add quantitative evaluation of router specialization (e.g., purity of POS tags within each router's assignments across the full validation set).
- Ablation studies on core architectural hyperparameters (s_max, N_b, N_m, top-k).
- Make the random-model path distribution analysis a central, quantitative comparison rather than relegating it to footnotes and appendices.
- Add a sentence explicitly stating the gradient path through the discrete routing operation (currently implicit in Eq. 1).

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **"Gradient propagation through discrete routing is never specified (structural)"** — REMOVED because the gradient path IS specified through Eq. (1), where the softmax probabilities ρ_i multiply the module outputs. Since ρ_i is a smooth function of router logits, gradients flow through this term back to the router parameters. The equation implicitly defines the gradient mechanism; the harsh critic's claim that this is a structural gap is incorrect upon inspection of the math.
- **"The power-law path distribution is not evidence of learned structure (fatal)"** — REMOVED as fatal because the paper itself acknowledges this finding (Fig. 1 caption: "Surprisingly, the distribution of paths through the random model also follows power-law"). The paper is transparent; the criticism restates what the paper already reports. Downgraded to Minor.
- **"Bias controller means compute allocation isn't emergent (fatal)"** — REMOVED as fatal. The paper describes the mechanism explicitly (Eq. 3) and the bias is a training tool. The framing tension is real but minor. Downgraded to Minor.
- **Strength Finder: "interpretability evidence is convincing"** — Moderated significantly. The evidence is qualitative and anecdotal; calling it "convincing" overstates the case given the lack of quantitative metrics.
- **Harsh Critic: "The introduction claims DNAs are not feed-forward, which is incorrect"** — This is a terminology nitpick; the paper clarifies the forward pass structure in Section 2.1. Downgraded to Trivial.

## Novel Insights
The paper's most genuinely novel observation is that path-based routing produces interpretable computation patterns without explicit architectural priors — tokens routing through similar paths form semantically coherent groups (e.g., punctuation to one module, nouns to another in language models; edge-detecting vs. object-specific paths in vision). The finding that sparse, data-dependent attention emerges naturally from the routing structure (patches in different modules do not attend to each other) distinguishes DNA from hand-crafted sparse attention mechanisms and suggests a new axis for designing efficient architectures. The random-model baseline — showing that untrained DNAs also exhibit power-law path distributions but with different exponents and qualitatively different clustering — is an honest and informative control that raises interesting questions about what training actually contributes.

## Suggestions
- Quantify the router specialization claim for language models by measuring POS-tag or semantic-category purity within each router's assignments, compared to a random router baseline. This single quantitative result would substantially strengthen the interpretability narrative.
- Report s_max explicitly in Tables 1 and 2, along with average FLOPs per forward pass, to make compute-efficiency comparisons falsifiable.
- Include an ablation varying s_max or N_b to assess how much the "emergent" structure depends on these pre-specified architectural constraints.
- Consider total-parameter-matched baselines or explicitly discuss why active-parameter matching is the appropriate comparison given the DNA design.

## Calibration

### Round 1 — Bracketing

| Anchor | Score | Comparison |
|--------|-------|------------|
| `hbon6Jbp9Q.md` — Brain region LM fine-tuning | 2.33 | DNA much stronger: novel architecture, competitive results, two domains |
| `epFk8e470p.md` — Brain-inspired action classification | 1.67 | DNA much stronger |
| `jIAKjjEmWi.md` — A-MoD attention routing | 4.00 | DNA stronger: broader scope, two domains, more analysis, more transparent limitations |
| `Olb8JwUGZ3.md` — When/how modular networks better | 4.25 | DNA more ambitious in scope and analysis |
| `1qq1QJKM5q.md` — COMET conditional overlapping experts | 5.67 | DNA comparable novelty; COMET broader task coverage, DNA more interpretability analysis |
| `EMMnAd3apQ.md` — ToVE vision-language experts | 6.00 | DNA broader architecturally, ToVE more rigorous |
| `WQQyJbr5Lh.md` — Neuron Path in ViTs | 6.00 | DNA broader architectural contribution but weaker evidence for interpretability claims |
| `3pWSL8My6B.md` — Proving emergence of sparse interactions | 7.00 | DNA clearly weaker: less theoretical rigor, less quantitative evidence |
| `I4e82CIDxv.md` — Sparse Feature Circuits | 8.00 | DNA clearly weaker: less methodological rigor, less systematic evaluation |

**Round 1 Bracket: 4.5–6.5**

### Round 2 — Narrowing

| Anchor | Score | Comparison |
|--------|-------|------------|
| `uWvKBCYh4S.md` — Mixture of LoRA Experts | 5.00 | DNA more novel architecture; LoRA paper more rigorous evaluation |
| `thqPibDg6A.md` — Cluster-oriented MoE pre-training | 4.40 | DNA stronger: broader contribution, more analysis |
| `PPjpGTPG5K.md` — PERFT MoE fine-tuning | 5.33 | DNA comparable scope; PERFT more application-focused |
| `RVPZJpmyGU.md` — VQMoE discrete routing | 4.60 | DNA comparable but broader scope |
| `1qq1QJKM5q.md` — COMET (re-appeared) | 5.67 | DNA comparable: similar novelty, COMET broader task coverage |
| `WQQyJbr5Lh.md` — Neuron Path (re-appeared) | 6.00 | DNA broader architecturally but weaker evidence rigor |
| `fpoAYV6Wsk.md` — Circuit Component Reuse | 6.50 | DNA weaker: less rigorous methodology, less quantitative evidence |
| `41HlN8XYM5.md` — Automated Circuit Discovery | 6.33 | DNA weaker: less rigorous methodology |

DNA sits between COMET (5.67) and the 6.0+ interpretability papers. The qualitative nature of its central interpretability evidence and the parameter mismatch in competitiveness comparisons pull it below the 6.0 threshold. The paper's honest framing, inclusion of controls, and genuinely novel architectural paradigm keep it above the weaker MoE-routing variants in the 4.0–4.6 range. It lands closest to COMET (5.67) but slightly below, given that COMET demonstrated broader task coverage while DNA's interpretive evidence remains more suggestive than demonstrative.

**Final Score: 5.0** — Borderline. The paper introduces a genuinely novel architectural paradigm with competitive results and honest presentation, but the central interpretive claims are supported by qualitative/anecdotal evidence rather than systematic quantitative analysis. The paper would benefit from quantitative router specialization metrics, FLOPs-based comparisons, and total-parameter-matched baselines before its claims about emergent interpretable structure are fully convincing.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>