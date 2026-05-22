Now I have all the information I need. Let me write the consolidated final review.

## Summary

This paper introduces Distributed Neural Architectures (DNAs), a new paradigm where tokens follow learned, data-dependent paths through a collection of modules (MLP, attention, transformer blocks, identity) and routers. DNAs generalize MoE, MoD, weight sharing, and early exit under a unified framework. The paper demonstrates that DNAs are trainable and competitive with dense baselines (ViT-Small, GPT-2 Medium) in both vision (ImageNet) and language (FineWeb-Edu) domains. It further shows that compute allocation and parameter sharing emerge from training in an interpretable way, and analyzes the power-law path distribution and emergent path specialization.

## Strengths

- **Novel and conceptually interesting architecture paradigm.** DNAs remove the notion of fixed depth/width, allowing tokens to follow arbitrary learned paths through modules. This is a genuinely new way of thinking about neural architecture that unifies several existing conditional-computation methods (MoE, MoD, layer-skip, weight sharing) under a single framework.

- **Feasibility demonstrated in two domains with competitive performance.** The vision DNA (top-1) achieves 79.1% on ImageNet vs. 79.8% for ViT-Small (within ~1%). The language top-2 DNA (433M active params) achieves lower validation loss (2.674 vs. 2.720) and outperforms GPT-2 Medium on 6/7 zero-shot benchmarks (Table 3). These results show that DNAs can be trained to perform comparably to standard architectures, which is non-trivial given the complexity of learned routing.

- **Interpretable compute allocation and path specialization.** Figure 5 shows that the top-2 DNA model allocates compute based on image complexity (boundary-rich images get more compute). Figure 3 demonstrates that different paths specialize: low-rank paths capture edges and flat colors, while high-rank paths capture specific concepts (brass instruments, puzzle pieces). The "deep-dream" reconstructions in Figure 4 show interpretable feature development across steps.

- **Honest reporting of limitations.** The paper transparently reports that (a) random models also show power-law path distributions, (b) language parameter sharing appears random/unstructured (Section 4.3), and (c) the work is explicitly framed as a feasibility study, not a SOTA pursuit. This candor strengthens the paper.

## Weaknesses

### Major

- **Active parameter mismatch undermines language "competitive" claim.** The top-1 DNA (matched at 406M active params, same as GPT-2) is *worse* on 6/7 benchmarks (loss 2.754 vs. 2.720, lower ARC-E, HellaS, LAMBADA, PIQA, RACE, and higher Wiki perplexity). Only the top-2 DNA (433M active params, +6.7% more than GPT-2's 406M) shows an advantage. The paper's blanket claim that "DNAs are competitive with dense baselines" conflates these two cases. The claim is defensible for the top-2 model with its modest parameter advantage, but the matched-parameter comparison tells a different story. The paper should explicitly discuss this discrepancy and calibrate its claims per-model.

- **Emergent specialization claims lack quantitative rigor.** The visual evidence for path specialization (Figures 3, 4, 8) is compelling but entirely qualitative — cherry-picked example patches/tokens shown without statistical measures (e.g., clustering purity, mutual information between path assignments and semantic categories, statistical tests for whether the observed grouping differs from random routing). The paper notes that random models also cluster images (albeit differently), but does not systematically quantify what training *adds* beyond the random baseline. For language, the paper's own analysis in Section 4.3 finds that module reuse is "most likely random." This honest admission weakens the broader specialization narrative, which would benefit from crisper claims and quantified evidence.

### Minor

- **Compute efficiency claims use a proxy metric without FLOPs validation.** The "normalized compute" metric (fraction of modules visited) is a reasonable proxy but does not account for non-trivial interactions with sparse attention patterns or the overhead of identity-module routing. Actual FLOPs or wall-clock time would substantiate the efficiency claim more strongly. This is a modest gap for a feasibility study but worth addressing.

- **No comparison to MoE or MoD baselines.** The paper frames DNAs as a "natural generalization" of these methods but compares only to dense baselines. While the explicit scope (feasibility, not SOTA) and the dense-only comparison soften this omission, the paper would be significantly stronger by including at least one MoE or MoD baseline of comparable size to contextualize whether the additional complexity of full token-level routing over diverse module types is worthwhile.

### Trivial

- None of note; the paper is clearly written and well-organized.

## Nice-to-Haves

- **FLOPs measurement** to substantiate the compute-efficiency analysis.
- **A single MoE baseline** to contextualize DNA performance against existing conditional-computation methods.
- **Quantitative metrics for path specialization** (e.g., cluster purity, mutual information) to supplement the qualitative examples.
- **Multiple seeds** for main results, given the stochasticity of routing decisions.

## Removed Points

- **Criticism about power-law distribution being a structural artifact, not emergent:** The paper explicitly notes this finding ("surprisingly, the distribution of paths through the random model also follows power-law with exponent -1") and frames the power-law observation as an empirical fact about the architecture, not a claim of emergent learning. The paper's actual claims about specialization are about *what* paths cluster (specific semantic categories), not the *distribution shape*. This criticism misreads the claim and is removed.

- **Criticism about the interpretability analysis being purely anecdotal:** This is partially valid and kept as a minor weakness (lack of quantitative metrics). But the claim of "cherry-picked" is too strong — the paper shows representative examples from multiple rank levels and the analysis of random-baseline clustering provides a meaningful comparison. The criticism is toned down accordingly.

- **Criticism about the backbone not being ablated:** Requesting a full ablation of the backbone is a reasonable suggestion but falls under nice-to-have for a feasibility paper. The backbone is a pragmatic design choice to aid training convergence, not a core claim. Moved to Removed Points.

- **Criticism about statistical significance / single runs:** While valid in principle, single-run evaluation is standard practice for large-scale vision (300 epoch ImageNet training) and language (21B token) experiments at this scale. Demanding multiple seeds for all experiments is outside typical community norms for papers of this scope. Removed.

- **Criticism about missing training compute reporting:** The paper focuses on inference efficiency; training cost is a secondary concern for a feasibility study. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no perspective that the paper's own analysis does not already acknowledge or address.

## Suggestions

1. **Clarify the language-model claim per-model.** Distinguish the top-1 (matched params, underperforms) from the top-2 (more params, outperforms) when claiming "competitive with dense baselines."

2. **Add quantitative metrics for path specialization.** For the vision analysis, report metrics like path-cluster purity with respect to ImageNet classes or visual attributes, and compare against a random-routing baseline with a statistical test (e.g., permutation test).

3. **Include at least one MoE or MoD baseline** at comparable scale to contextualize the benefits of DNAs over these simpler conditional-computation frameworks.

4. **Report FLOPs per forward pass** for both DNA models and dense baselines to substantiate the compute-efficiency claims with a hardware-agnostic but standard metric.

5. **Address the backbone choice** briefly — note whether removing it is feasible and what impact it has on routing diversity.

## Score and Decision

**Calibration Summary**

*Round 1 (Bracketing):* Queried for papers on similar topics (conditional computation, distributed architectures, routing). Weak band (<3.5): papers scoring 2.33–3.40, e.g., "Collective Model Intelligence Requires Compatible Specialization" (3.40). Middle band (3.5–7.5): papers scoring 4.75–6.00, e.g., "Gradient Routing" (5.25), "COMET" (5.67), "SMEAR" (6.00). Strong band (>7.5): papers scoring 8.00–9.00. **Bracket: 4.5–6.5.**

*Round 2 (Narrowing):* Searched within (4.0, 6.5) for conditional computation and emergent specialization papers. Anchors examined: Gradient Routing (5.25, rejected — cleaner experiments but less novel than DNAs), COMET (5.67, accepted — fixed-routing MoE with similar ambition), SMEAR (6.0, rejected — soft-routing MoE with clean baselines), Breaking Scaling Laws with Modularity (6.0, accepted — strong theory but limited scope), ToVE (6.0, accepted — vision-language MoE with strong results). The DNA paper is more novel and ambitious than all of these, but its experiments are less clean (parameter mismatch, missing MoE baseline, qualitative specialization analysis). It sits slightly below SMEAR and COMET due to these evidential gaps, and above Gradient Routing due to its broader scope and cross-domain demonstration. **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>