Now I have sufficient calibration. Let me write the consolidated review.

**Round 1 bracket:** 3.5 – 6.0  
**Narrowing:** Compared against Tree-Planner (5.25), MAP (4.50), ReAct Critique (4.00), and the AoT+ paper (6.40). The current paper has more novelty than the ReAct Critique paper but significantly weaker experimental rigor than Tree-Planner or AoT+. The MAP paper (4.50) is the closest comparator — similar level of novelty but MAP had more thorough experiments. I place this slightly below MAP due to the uncontrolled comparison.

**Final score: 4.5**

---

## Summary

This paper proposes using the Task-Method-Knowledge (TMK) framework — a knowledge representation approach from cognitive science — as a structured prompt to improve LLM planning on the PlanBench Blocksworld benchmark. The TMK prompt replaces the natural-language domain description with a hierarchical JSON decomposition of goals (Tasks), procedures (Methods), and domain concepts (Knowledge). The central empirical finding is a "performance inversion": for the o1 reasoning model, TMK raises Random Blocksworld accuracy from 31.5% to 97.33%, while its Mystery Blocksworld gain is more modest (74.3% → 83.3%), reversing the usual pattern where models perform better on Mystery than Random.

## Strengths

- **Novel and well-motivated application of TMK to LLM planning.** Borrowing a formal knowledge representation framework from cognitive architectures and educational science is a genuinely creative move that departs from the usual CoT/ReACT playbook. The paper clearly explains the tripartite Task-Method-Knowledge decomposition and provides a complete specification for Blocksworld (Figure 1).

- **The "performance inversion" finding is genuinely interesting and non-obvious.** Under standard plain-text prompting, o1 scores 74.3% on Mystery vs. 31.5% on Random — the expected pattern where semantic obfuscation is easier to handle than opaque tokens. TMK reverses this: 83.3% vs. 97.33%. This pattern is the paper's strongest empirical signal, and it is the kind of finding that could stimulate follow-up work on how prompt structure interacts with a model's latent processing pathways.

- **Methodological care on some fronts.** The paper uses full-plan validation (every step must be correct, not just final-state matching), one-shot prompts with a random example that does not match the query, and evaluates across multiple model families (GPT-4, GPT-4o, o1-mini, o1, GPT-5). These choices address several standard criticisms of prior prompting-for-planning work.

## Weaknesses

### Major

1. **No properly controlled one-shot plain-text baseline.** The Plain Text column in Table 2 is described as "best of sampled Zero & One shot" drawn from the public leaderboard and the authors' own sample runs. The TMK column is always one-shot. The paper argues this is conservative (zero-shot > one-shot for plain text), and this argument has some merit, but it does not eliminate the confounds. The plain text and TMK conditions differ in multiple independent variables simultaneously: prompt format (natural language vs. JSON), number of shots (zero vs. one), precise prompt wording, API version/date, and extraction post-processing. Without a side-by-side comparison where the **only** variable is whether the domain description is plain-text vs. TMK-structured (same one-shot example, same model version, same temperature, same extraction function), the claimed advantage of TMK cannot be cleanly attributed to the TMK structure. The observed gains — especially the headline 31.5% → 97.33% for o1 on Random — could be influenced by the one-shot output-format template, the JSON syntax, or other factors.

2. **Extraction function asymmetry for Random Blocksworld.** Section 3.2 describes an "enhanced extraction function" added for Random Blocksworld that relaxes the matching criteria (e.g., tolerating extra symbols, alternate wordings like "object" instead of the opaque token). The paper does not confirm that the plain-text baseline numbers from the leaderboard (or from the authors' own runs) were evaluated with the same lenient extraction. If the leaderboard used stricter criteria, the reported TMK scores for Random Blocksworld are inflated relative to the plain-text numbers, making the comparison invalid for this domain — which is where the most dramatic gains appear.

3. **No variance or stability information.** Table 2 reports point estimates with no indication of how many trials were run, what temperature was used, or whether results are from a single run or averaged over multiple seeds. For stochastic models, this makes it impossible to assess the reliability of the reported percentages or the significance of the differences between plain text and TMK.

### Minor

4. **No ablation isolating the effect of the TMK hierarchy vs. structured encoding.** The paper does not include a baseline where the same domain information is presented as a flat JSON listing of actions, preconditions, and effects (without the TMK decomposition). Such a baseline would distinguish whether the gains come from TMK's specific hierarchical decomposition or merely from presenting information in any structured format. The paper acknowledges this indirectly (mentioning BDI/HTN as future work) but provides no experiment to address it.

5. **No comparison to other prompting methods like CoT or CoS.** While the paper is not required to beat every existing method, including a standard CoT baseline would contextualize the magnitude of improvement and support the claim that TMK is particularly effective for planning. The related work section critiques CoT and CoS but never directly compares against them.

### Trivial

- The o1-preview row in Table 2 has "NA" for TMK with no explanation beyond the footnote about deprecation. Clarifying why TMK was not tested on this model would be helpful.

## Nice-to-Haves

- Running plain-text one-shot for every tested model under the same decoding parameters (same API version, temperature=0) would directly test whether the one-shot output-format template alone explains the gains.
- Re-evaluating leaderboard plain-text baselines with the enhanced Random Blocksworld extraction would resolve the extraction asymmetry concern.
- Reporting per-instance results or a distribution of plan lengths/error types would add useful granularity.

## Removed Points

- **Criticism about "the one-shot TMK prompt includes an example that, even if random, supplies a template for the output format"** — The paper explicitly addresses this in Section 3.2 (point 3) and notes that in PlanBench, zero-shot plain text often outperforms one-shot plain text, making the one-shot template explanation less likely. This is a reasonable rebuttal that the critic's framing ignores.
- **"Inconsistent provenance of plain-text numbers"** — Subsumed under the controlled-baseline issue (Weakness #1). The provenance is described in the paper; the real problem is the lack of a single controlled run.
- **"GPT-5 API version not stated"** — This is a minor reproducibility detail typical of any rapidly-evolving API and not a meaningful weakness.
- **Missing related works** — Per review policy, I cannot verify whether any specific work was missing.

## Novel Insights

The most interesting insight from this paper is the *direction* of the performance inversion under TMK. In standard prompting, the Mystery variant (semantic obfuscation) is easier than Random (opaque tokens) because the model can leverage approximate semantic knowledge. TMK reverses this: the model does better on the fully symbolic variant than on the one with misleading semantic cues. This is consistent with the paper's hypothesis that TMK steers the model toward code-like symbolic processing — if true, it predicts that TMK would be *least* helpful precisely where plain-text semantics already work well (Mystery) and *most* helpful where semantics are absent (Random). The o1 results fit this pattern strikingly well. Even accounting for the experimental confounds, this pattern is worth investigating further.

## Suggestions

1. **Run a clean controlled experiment** as the centerpiece revision: for each model, compare plain-text one-shot vs. TMK one-shot on the same problem instances, same API version, same decoding parameters, same extraction function. This is the single highest-leverage improvement.
2. **Add a flat-JSON ablation** where the same domain information is presented in a structured but non-hierarchical format (e.g., a JSON object listing each action with its preconditions and effects) to isolate whether TMK's hierarchy provides additional benefit beyond structured input.
3. **Report variance** by running each condition multiple times (at minimum 3–5 runs with different seeds) and reporting mean ± std, or per-instance breakdowns.
4. **Include a CoT baseline** (one-shot) on the same model set to contextualize the reported gains.

## Score and Decision

**Round 1 bracket:** 3.5 – 6.0 (based on calibration anchors for similar topics)

**Round 2 narrowing anchors:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| LLMs Can Plan Only If We Tell Them (AoT+) | 6.40 | R1/R2 | Stronger — proper controlled experiments, ablations, broader evaluation |
| Tree-Planner | 5.25 | R2 | Stronger — clean experimental design, though similar single-domain limitation |
| Modular Agentic Planner (MAP) | 4.50 | R2 | Comparable — both have interesting architecture/idea but experimental gaps; MAP more thorough |
| Query-Efficient Planning | 4.75 | R2 | Slightly stronger — more extensive experiments across domains |
| Do Think Tags Really Help LLMs Plan? | 4.00 | R1/R2 | Comparable — different contribution type (critique vs. proposal); similar level of rigor issues |
| Planning in Strawberry Fields | 3.00 | R1 | Weaker — no novel methodology, purely evaluative |

The paper's genuinely novel idea and interesting performance-inversion observation lift it above purely evaluative work (~3.0), but the uncontrolled comparison, extraction asymmetry, and lack of variance reporting prevent it from reaching the level of papers with clean experimental methodology (~5.0–6.4). Against the MAP anchor (4.50) — which also has an interesting architecture but experimental gaps — the current paper has a more novel intellectual contribution (TMK from cognitive science) but weaker execution. I score this slightly below MAP due to the severity of the baseline confound.

**Final score: 4.5**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>