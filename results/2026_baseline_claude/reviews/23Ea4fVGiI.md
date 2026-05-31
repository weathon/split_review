## Summary

The paper introduces Task-Method-Knowledge (TMK), a hierarchical knowledge representation framework from cognitive and educational science, as a structured prompting technique to improve LLM planning performance. The authors evaluate TMK-structured JSON prompts against plain-text prompts on the PlanBench Blocksworld benchmark (Classic, Mystery, and Random variants) using OpenAI models (GPT-4, GPT-4o, o1-mini, o1, GPT-5). The headline finding is a striking "performance inversion" in the o1 reasoning model: with standard prompting, o1 scores 74.3% on Mystery and 31.5% on Random; with TMK prompting, Random jumps to 97.33% while Mystery rises to 83.3%, reversing domain difficulty order.

---

## Strengths

- **Striking quantitative finding on a formal benchmark.** The 65.8% gain for o1 on Random Blocksworld (31.5% → 97.33%) and the "performance inversion" are evaluated on PlanBench, which uses automated PDDL plan validators (VAL, Fast Downward), providing rigorous formal correctness checking rather than approximate match. This is a much harder bar than most prompting benchmarks.
- **Serious engagement with existing critiques.** The paper explicitly addresses the most pointed critiques of CoT/ReACT work (Stechly et al., 2024; Bhambri et al., 2025)—memorized patterns, CoT contradicting answers, failure across models—and takes concrete countermeasures (providing a structurally dissimilar one-shot example, requiring full step-by-step plan correctness).
- **The performance inversion is a genuinely novel phenomenon.** The systematic flip in relative domain difficulty (Random > Mystery) under TMK, observed across the reasoning model class, is not a trivial consequence of adding tokens to a prompt and points to something interesting about how structured prompting interacts with model internals.
- **Multiple model families tested.** Results span plain LLMs (GPT-4, GPT-4o) and large reasoning models (o1-mini, o1, GPT-5), and the paper makes a credible distinction between their behaviors.

---

## Weaknesses

### Fatal
None that individually invalidate all results.

### Major

1. **Unfair zero-shot vs. one-shot comparison.** The most important methodological problem: baseline plain-text prompts are zero-shot while all TMK prompts are one-shot. The authors argue that (a) zero-shot typically outperforms one-shot for plain text in PlanBench, and (b) the one-shot TMK example is not tailored to the query. These are partial mitigations. However, the zero-shot plain-text vs. one-shot TMK comparison is not the same as controlling for shot count. A proper within-paper baseline—one-shot plain text using the same example problem—is not reported directly in the main results table. Without it, a portion of every gain attributed to TMK may be attributable to the shot-count difference.

2. **No ablation isolating TMK structure from richer domain information.** The TMK prompt encodes explicit preconditions, postconditions, and hierarchical procedural decomposition for every action—information that is structurally analogous to a PDDL domain file. A plausible and simpler explanation for the gains is that the model benefits from receiving all precondition/effect predicates in a structured format, not from the TMK formalism *per se*. No comparison against an equally detailed but non-TMK structured domain description (e.g., a structured plain-English table or a literal PDDL domain) is provided. Without this, "TMK improves planning" conflates framework-specific structure with information content.

3. **Modified evaluation code for Random Blocksworld undermines comparability.** The authors acknowledge they altered the PlanBench extraction code for Random Blocksworld to tolerate formatting artifacts ("object", "-", "_" etc. in model outputs). While they argue this is consistent with ICAPS standards, the modification changes the evaluation surface. The leaderboard scores for o1preview (37.3% Random) were obtained with the original extractor, while TMK o1 (97.33%) uses the relaxed extractor. Even though relative (plain-text vs. TMK) comparisons within the paper use the same extractor, the headline "surpasses state-of-the-art" claim depends on cross-experiment comparability that is not verified.

4. **Single domain, one model family.** Results are confined to Blocksworld with OpenAI models. The paper acknowledges this but still draws general conclusions about LLM planning and "symbolic steering mechanisms." Even the Logistics domain included in PlanBench is untested. The theoretical mechanism proposed (TMK steers toward code-execution pathways) is entirely untestable with available evidence.

### Minor

- The o1-mini Mystery regression (19.1% → 16.83%) is attributed to "capacity limitations" and "semantic overload" without evidence. The same TMK structure helps o1-mini on Random (+17.7%) but hurts on Mystery (−2.3%); no controlled experiment distinguishes these hypotheses.
- No confidence intervals or significance tests are reported; for smaller gains (GPT-4 Classic: 34.6% → 39.7%) statistical significance is unclear.
- The "symbolic steering" and "code-execution pathways" hypothesis, while interesting and plausible, is mechanistically un-grounded in the paper. The inference is circular: TMK helps most where semantic cues are absent → therefore TMK activates code pathways → therefore absence of semantic cues benefits code pathways.

### Trivial
- Inconsistent block-name counts across Table 1 and Figure 1.

---

## Nice-to-Haves

- Include a direct one-shot plain-text baseline (using the same example problem used for TMK) to properly control for shot count.
- Add an ablation: equivalent domain information provided as a structured JSON without the TMK Task/Method/Knowledge hierarchy, to isolate structural versus informational contribution.
- Test on at least one additional PlanBench domain (Logistics) to validate generalizability before making broad claims.
- Provide the modified Random Blocksworld extractor outputs alongside the original extractor's outputs for transparency, so readers can gauge the magnitude of the evaluation change.

---

## Novel Insights

The performance inversion under TMK—where a reasoning model switches from performing much better on Mystery (semantic obfuscation) than Random (opaque tokens) to the reverse—is a genuine empirical novelty. This reversal, if replicable with controlled baselines, would constitute an interesting probe of how structured prompting interacts with semantic representations in LLMs. The direction (structured prompts suppress semantic interference when tokens are non-semantic) is theoretically coherent and aligns with Chen et al. (2024)'s code-vs-text reasoning axis. The connection to cognitive scaffolding in educational science is an underexplored avenue in the prompting literature. However, the evidence for the underlying mechanism (steering toward code-like inference) remains entirely post-hoc and requires mechanistic experiments (e.g., looking at reasoning tokens in transparent models, or comparing TMK to PDDL-formatted prompts) to be more than speculation.

---

## Suggestions

- **Primary:** Run all comparisons (plain text and TMK) in the same shot regime (both one-shot) and report the full matrix; this single change would resolve the main confound.
- **Primary:** Add one ablation condition: a JSON-structured domain description with the same precondition/effect content as the TMK prompt but without the hierarchical Task/Method/Knowledge decomposition. This would disambiguate informational from structural contributions.
- **Secondary:** Apply both the original and modified Random Blocksworld extractors to the same model outputs and report both scores to bound the effect of the extraction change.
- **Secondary:** Extend experiments to at least one non-Blocksworld PlanBench domain (e.g., Logistics) to test generalization of the key claims before submission to a broader venue.

---

## Score and Decision

The paper tackles an important and timely question (can structured prompting improve formal planning?), presents striking quantitative results on a rigorous benchmark, and identifies a novel performance inversion phenomenon. However, the zero-shot vs. one-shot comparison confound, the absence of ablations disentangling TMK structure from domain content richness, and the modified extraction code collectively weaken confidence in the claimed magnitude and mechanism of gains. The findings are suggestive and worth following up with a more controlled study, but in current form the central claims are not fully supported.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>