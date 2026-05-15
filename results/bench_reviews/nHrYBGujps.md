Now let me read one more anchor paper for balance — the InteractComp one (3.50) to compare with a rejected interactive benchmark paper:

Already read. Let me now compile my review. I have sufficient information from all the anchors I've read.

Let me now carefully verify each harsh critic claim against the paper text and construct my final review.

**Verification of Harsh Critic Claims:**

**Claim 1: "The benchmark's interactive realism is artificially narrow"**
- Section 3.3: The function-driven simulator does indeed map to three actions: AMB(), LOC(), UNA(). AMB() handles pre-annotated ambiguities with SQL snippets. LOC() uses AST-based retrieval. UNA() rejects inappropriate requests.
- The paper argues this is a deliberate design to prevent leakage (shown in USERSIM-GUARD: 67.4% → 2.7% leakage reduction).
- The paper acknowledges the trade-off; Section 8 mentions future work on "post-trained, human-aligned local user simulator."
- The human correlation (0.84) provides some validation that the simulator approximates real behavior.
- This is a valid criticism about scope limitation, but not "fatal" — it's an inherent design trade-off that the paper explicitly acknowledges and justifies. MAJOR, not fatal.

**Claim 2: "Construct validity not demonstrated for model rankings"**
- Section 6 reports Pearson 0.84 on task-level success rates between simulator and humans on 100 tasks.
- The paper does NOT claim to validate model rankings — it validates task-level success rate alignment.
- This is a valid limitation but the paper doesn't overclaim here. The correlation study shows the simulator produces success patterns similar to humans at the task level. MINOR.

**Claim 3: "Memory-grafting experiment doesn't support communication bottleneck claim"**
- Section 5.2, Figure 5: GPT-5 improves from 13.8% to 18.8-20.5% with other models' interaction histories.
- The paper claims "a more effective communication schema is required."
- The critic is correct that the experiment doesn't fully isolate communication quality from information content. MINOR — the experiment is still informative even if the interpretation is somewhat overclaimed.

**Now let me check if any criticism should be REMOVED per hard rules:**

All criticisms appear to be about the paper's actual content, not about:
- Existence/release of models/tools/benchmarks → None of the criticisms do this
- Factual errors → I verified these are plausible interpretations, not factual errors
- Unfair comparison favoring baselines → Not applicable
- Missing related works → The harsh critic mentions this but I'll remove per rule
- Formatting/typo nits → Not present in the criticism
- Reproducibility nits about undisclosed hyperparameters → The harsh critic mentions confidence intervals but I'll handle this

Wait, the harsh critic mentions "omits recent clarification-focused works" - per hard rules, I should REMOVE criticisms about missing related works. Let me check: "The coverage of multi-turn text-to-SQL is concise but omits recent clarification-focused works that also attempt dynamic interaction, such as later extensions of LEARN-TO-CLARIFY with user simulators." This is about missing related works. I should REMOVE this.

Also, the harsh critic's "Section-by-Section Notes" mentions:
- "The choice of λ_pat=3 as default (and base budget 6) is arbitrary" - This is a nitpick about hyperparameter choices. Per hard rules about removing "trivial implementation details," I should weaken or remove this. But it's a reasonable point about the budget design. Let me keep it as minor.
- "For a-Interact, the action space includes costly Retrieve Knowledge and Retrieve Column Meaning actions, but these are not differentiated from simply asking the user" - This seems like a misunderstanding. The paper defines 9 discrete actions. Let me check. Actually, this might be valid.
- "The ITS 'law' is introduced but not operationalized" - This is valid. The paper defines an "ITS Law" but Figure 4 doesn't show any model actually matching or surpassing the idealized single-turn line. The term "law" is indeed misleading.

OK, let me now write the final review.

About the strength finder: I need to filter out generic/nonspecific strengths. Let me check each:

1. "Dynamic, realistic interaction environment" - Specific, backed by citations. KEEP.
2. "Challenging task suite that exposes model limitations" - Specific, backed by Table 2. KEEP.
3. "Dual evaluation paradigms reveal complementary insights" - Specific, backed by results. KEEP.
4. "Rigorous ambiguity injection and follow-up construction" - Specific, backed by annotation methodology. KEEP.
5. "Validated importance of communication and interaction scaling" - Partially valid but with caveats about memory grafting. KEEP but note the limitation.

Supporting strengths:
1. CRUD coverage - This is specific and backed by Table 2 with BI/DM split. KEEP.
2. Budget-constrained evaluation - Specific. KEEP.
3. Detailed analysis of model behavior - Specific, backed by action distributions. KEEP.

None seem to be generic/nonsense that should be removed. 

Now let me also incorporate the "Removed Points" section.

Points to remove:
- Missing related works criticism (harsh critic's related work section note)
- Any criticism about the paper not including specific comparisons with COSQL/LEARN-TO-CLARIFY (this is methodological nitpicking about what experiments to run)

Let me now write the review.Now I have a thorough understanding of both the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

BIRD-INTERACT presents a benchmark for evaluating LLMs on interactive, multi-turn text-to-SQL tasks. Its core innovations are (1) a function-driven user simulator that prevents ground-truth leakage while enabling scalable evaluation, (2) two complementary evaluation settings (protocol-guided *c*-Interact and agentic *a*-Interact), and (3) a task suite of 900 items covering the full CRUD spectrum with injected ambiguities and state-dependent follow-up sub-tasks. Even the strongest model (GPT-5) achieves only 17.00% end-to-end success, demonstrating that current LLMs lack the strategic interaction skills needed for realistic database querying.

## Strengths

- **Function-driven simulator solves a real evaluation problem.** The two-stage design (LLM-as-parser → constrained action → controlled response) reduces ground-truth leakage from up to 67.4% in baseline simulators to 2.7%, as demonstrated by the USERSIM-GUARD evaluation (Figure 6). This is a genuine methodological contribution that directly addresses a well-known weakness of LLM-based user simulators.

- **Challenging, unsaturated benchmark.** Table 2 shows GPT-5 at 17.00% end-to-end success in *a*-Interact and only 8.67% in *c*-Interact on the full set. These low success rates, combined with substantial headroom, make BIRD-INTERACT a meaningful target for the research community.

- **Dual evaluation settings produce complementary insights.** The *c*-Interact and *a*-Interact settings reveal differentiated model behaviors — e.g., GPT-5 ranks worst in *c*-Interact but best in *a*-Interact (Table 2) — validating the claim that matching interaction mode to model capability matters.

- **Rigorous construction with human validation.** The annotation methodology (three-tier ambiguity injection, five-category follow-up taxonomy, state-dependency between sub-tasks) is systematic and well-documented. Inter-annotator agreement of 93.33–93.50% (Table 1) and a human-simulator Pearson correlation of 0.84 (p=0.02, Table 3) provide credible quality assurance.

- **Substantial scale and infrastructure.** 900 tasks generating up to 11,796 dynamic interactions, with an executable Docker environment, test cases, and a hierarchical knowledge base, represent significant engineering effort that benefits reproducibility.

## Weaknesses

### Fatal

None.

### Major

- **Interaction realism is fundamentally constrained by the simulator design.** The function-driven simulator maps all model questions into three actions (AMB, LOC, UNA). AMB returns pre-annotated SQL snippets tied to known ambiguities; LOC uses AST-based retrieval that can expose query structure. While the paper convincingly argues this design is *necessary* for leakage control (and the USERSIM-GUARD results support this), the resulting interaction is closer to a structured information-retrieval game than to the open-ended, co-constructive clarification that real users engage in. The paper's language about "restoring missing realism" and capturing "production-grade" challenges overstates what this particular simulator design can deliver. This does not invalidate the benchmark — controlled evaluation has genuine value — but it limits the strength of the realism claims and means the benchmark primarily tests targeted information extraction under a known answer distribution rather than general interactive text-to-SQL capability.

### Minor

- **Memory-grafting experiment does not fully isolate communication quality from information content.** When GPT-5 is given ambiguity-resolution histories from better-performing models (Section 5.2, Figure 5), performance improves. But these histories contain the concrete clarification *answers* (the missing SQL fragments) that GPT-5 itself failed to elicit. The experiment cannot distinguish "GPT-5 asked the wrong questions" from "GPT-5 could not induce the simulator to reveal the necessary facts even with good questions." The claim that "a more effective communication schema is required" is therefore only partially supported. An additional condition grafting only the content of clarifications (not the dialogue phrasing) would disentangle these factors.

- **The "ITS Law" framing is misleading.** Section 5.2 defines an "ITS Law" stating that with enough interaction turns, model performance should match or surpass idealized single-turn performance. However, Figure 4 shows no model actually reaching the idealized single-turn line under any patience setting tested. The notion of a "law" is premature when the data demonstrate only a monotonic trend for some models. Renaming this as "ITS scaling behavior" would be more accurate.

- **Construct validity for model rankings is not directly established.** The human-alignment study (Section 6) reports a Pearson correlation of 0.84 between simulator and human success rates across 100 tasks. This validates task-level alignment but does not directly test whether the *relative ranking of models* produced by the benchmark matches what human users would experience. Most benchmark papers do not perform this level of validation either, so this is not a critical gap, but it is worth acknowledging as a limitation of the current evaluation.

### Trivial

- **Single-run evaluations without statistical dispersion.** Given the low success rates and the stochastic nature of LLM outputs, reporting only point estimates (Table 2) makes it difficult to assess whether differences between models are reliable. The authors note cost constraints, which is understandable at this scale, but the limitation should be stated explicitly.

## Nice-to-Haves

- A breakdown of failure modes (ran out of budget vs. asked wrong questions vs. generated incorrect SQL vs. misunderstood follow-up state) would make the benchmark more actionable for future method development.
- Ablation on action costs in *a*-Interact to test whether the bias toward `submit`/`ask` is structural or an artifact of the specific cost multipliers chosen.
- Free-mode *a*-Interact experiments (mentioned in future work) would complement the stress-mode results and help characterize natural interaction strategies.

## Removed Points

These points were flagged during review synthesis. Treat them with caution:

- **Missing related works (e.g., extensions of LEARN-TO-CLARIFY with user simulators).** Removed per hard rule: we do not flag missing related works, as we cannot verify their existence or relevance from external sources.

- **Demand for comparison with COSQL or LEARN-TO-CLARIFY benchmarks.** Removed: this is a methodological preference (which experiments to run), not a substantive flaw. The paper's contribution is in providing a *new* evaluation paradigm; requiring cross-benchmark comparisons is scope creep.

- **Criticism of arbitrary budget parameters (λ_pat=3, base budget=6).** Removed as a standalone weakness: these are standard hyperparameter choices in benchmark design, and the paper does provide a stress-testing rationale. The paper also explores varying patience levels (Figure 4).

## Novel Insights

The paper's most interesting finding is the interaction-mode dependency of model rankings: GPT-5 performs worst in the structured *c*-Interact setting but best in the more open-ended *a*-Interact setting (Table 2). This suggests that different interaction paradigms draw on distinct model capabilities (likely stemming from training data distributions and architectural biases), and that no single evaluation setting can fully characterize interactive text-to-SQL performance. This insight has implications beyond this benchmark — it suggests that interactive AI evaluation more broadly should employ multiple, qualitatively different interaction protocols.

## Suggestions

- Reframe the realism claims to more precisely describe what the simulator does and does not capture. The benchmark is best characterized as testing *targeted ambiguity resolution under controlled conditions* rather than *general interactive text-to-SQL capability*.
- Add a content-only grafting condition to the memory-grafting experiment to strengthen (or appropriately qualify) the communication-bottleneck claim.
- Rename "ITS Law" to "ITS scaling behavior" or similar, and explicitly note that no tested model reached the idealized single-turn ceiling.
- Report confidence intervals or bootstrap estimates for the main results table, or at minimum acknowledge the single-run limitation explicitly.

---

## Anchor Comparison

| Anchor Paper | Path | Avg Score | Comparison |
|---|---|---|---|
| LLMs Get Lost In Multi-Turn Conversation | VKGTGGcwl6.md | 8.00 | Stronger: deeper behavioral analysis, cleaner protocol, more fundamental insight. BIRD-INTERACT is a benchmark paper with different contribution type. |
| SPARTA | 8KE9qvKhM4.md | 5.00 | BIRD-INTERACT is stronger: better human validation (0.84 correlation vs. lightweight validation), more innovative evaluation design (dual settings + budget constraints vs. standard QA), and addresses a broader problem space (CRUD + interaction). |
| EHR-ChatQA | hLweUPBz7k.md | 4.00 | BIRD-INTERACT is stronger: larger scale (900 vs. unclear but smaller), better simulator validation (USERSIM-GUARD), full CRUD coverage vs. SELECT-only, and more models evaluated. |
| InteractComp | psEcdvhOJx.md | 3.50 | BIRD-INTERACT is stronger: much larger scale, better simulator design, and more comprehensive evaluation framework. |
| ConDABench | jOxfpsnDFo.md | 2.50 | BIRD-INTERACT is substantially stronger: human-annotated tasks vs. fully auto-generated with limited validation, genuine simulator innovation vs. LLM-based proxy, and stronger quality control. |
| Octopus | BdlIQGetYv.md | 2.50 | BIRD-INTERACT is substantially stronger: human annotation with high agreement vs. fully auto-generated, execution-based evaluation with test cases, and genuine novelty in interaction design. |

BIRD-INTERACT is clearly above the 4.0–5.0 tier of benchmark papers (stronger validation, larger scale, more innovative simulator) but does not reach the 8.0 tier (its insights are less fundamental and its analysis less exhaustive). The function-driven simulator is a genuine methodological contribution that distinguishes it from prior interactive benchmarks.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>