Now I have strong calibration. Let me synthesize the final review.

**Calibration summary:**
- "Planning in Strawberry Fields" (3.00, Reject): Pure benchmarking, no novel method — clearly weaker than our paper
- "SWAP" (5.50, Reject): Multi-domain reasoning framework, novelty concerns — comparable but our paper has a more striking finding
- "Robotouille" (5.67, Accept): Single-domain benchmark, limited baselines — comparable limitations, accepted
- "LLMs Can Plan Only If We Tell Them" (6.40, Accept): Multi-domain prompting method with ablations — stronger than our paper

The paper under review sits around 5.5: a genuine contribution with a striking performance inversion finding, but limited by single-domain scope, no format ablation, and no statistical reporting. Borderline accept.

---

## Summary
This paper investigates whether structuring prompts using the Task-Method-Knowledge (TMK) framework — a knowledge representation formalism from cognitive architectures — improves LLM planning performance on PlanBench's Blocksworld domain and its Mystery and Random obfuscated variants. The authors replace the plain-text domain description in PlanBench prompts with a JSON-structured TMK representation and evaluate across OpenAI flagship models (GPT-4, GPT-4o, o1, o1-mini, GPT-5). The headline result is a 65.8 percentage-point improvement for o1 on Random Blocksworld (31.5% → 97.33%), accompanied by a "performance inversion" where TMK makes the symbolically opaque Random variant easier than the semantically cued Mystery variant, reversing the plain-text baseline pattern.

## Strengths
- **Performance inversion on o1 is empirically striking and causally informative**: Under plain text, o1 scores 74.3% on Mystery vs. 31.5% on Random (a 42.8-point gap favoring semantic cues). Under TMK, the gap reverses: Random reaches 97.33% while Mystery reaches 83.3%. This inversion is the strongest evidence that TMK does more than add context — it shifts how the model processes the task (Section 4.2, Table 2).
- **Conservative baseline comparison with explicit justification**: The paper compares TMK one-shot against plain-text zero-shot (the stronger plain-text baseline, since zero-shot outperforms one-shot for plain text on PlanBench). They provide three explicit reasons for this choice (Section 3.2), and the comparison is conservative — any shot-count confound works against TMK, not for it.
- **Consistent improvement pattern across model families and variants**: Table 2 shows TMK improves accuracy in 13 of 15 model×domain pairs, spanning both standard LLMs (GPT-4, GPT-4o) and large reasoning models (o1, GPT-5). This breadth across models with very different baseline capabilities lends robustness to the claim that TMK-structured prompting systematically aids planning.
- **Methodological controls against known confounds in LLM planning evaluation**: The paper uses a one-shot example that does not match the query problem in length or block description (ruling out instance-level pattern matching), evaluates full plan correctness including every intermediate step (not just final-state match), and demonstrates that the one-shot example in plain text does not improve performance (Section 5.1).

## Weaknesses

### Fatal
None.

### Major
- **No format ablation to isolate TMK-specific properties from generic structured formatting**: The paper's central claim is that the TMK framework — with its teleological T-M-K hierarchy — improves planning. But the experiments only compare TMK-structured JSON against unstructured plain text. Without at least one ablation (e.g., JSON domain description without T-M-K hierarchy, bullet-point structured operators, a PDDL-formatted prompt), the paper cannot distinguish whether TMK's specific framework matters or whether any well-organized, JSON-formatted domain knowledge would produce similar gains. The Discussion (Section 5.2.1) itself attributes gains partly to JSON/code-format activation, which would apply to any JSON-structured domain description. This is the single most important missing experiment.
- **No statistical testing, variance reporting, or disclosure of problem counts**: Table 2 reports single-point accuracy percentages without confidence intervals, statistical tests, or the number of test problems. While the o1 Random gain (31.5% → 97.33%) is large enough that significance is not in doubt, many smaller gains (e.g., GPT-4 Classic: 34.6% → 39.7%, o1-mini Classic: 56.7% → 57.0%) are small enough that they could reflect sampling noise. The reader cannot assess the reliability of these claims.

### Minor
- **Overclaimed mechanistic language in abstract and conclusion**: The abstract states that TMK "functions... as a mechanism that steers reasoning models away from their default linguistic modes to engage formal, code-execution pathways" and the conclusion states "This confirms that TMK acts as a symbolic scaffold." The body text more carefully frames these as hypotheses (Section 5.2.1: "The authors of this paper have a hypothesis"), but the abstract and conclusion present mechanistic claims as established findings when only correlational outcome evidence is provided.
- **TMK implementation is structurally shallow for this domain**: In the Blocksworld TMK (Figure 1), the Task layer's Given/Makes fields and the Method layer's Requires/Provides fields are near-duplicates — the three-layer hierarchy largely collapses to two for this simple domain where each goal maps 1:1 to a single action. This is partly a domain limitation (the paper acknowledges the decomposition is kept to three layers for simplicity), but it weakens the paper's framing of TMK as capturing distinctive teleological structure.

### Trivial
- The Discussion's cognitive scaffolding argument (Section 5.2.2, invoking Bloom's taxonomy and the worked-example effect) is post-hoc and speculative, though appropriately hedged as a hypothesis.

## Nice-to-Haves
- A format ablation comparing TMK against a non-TMK JSON encoding of the same domain knowledge would directly test whether the T-M-K hierarchy matters.
- Per-problem counts, binomial confidence intervals, or basic statistical tests would strengthen the smaller-magnitude claims.
- Analysis of reasoning traces (for models where accessible) could provide direct evidence for the code-execution steering hypothesis.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "Experimental design conflates format, shot count, and TMK structure — making it impossible to attribute gains to TMK"** — REMOVED because the paper explicitly addresses this in Section 3.2. The comparison is TMK one-shot vs. plain-text zero-shot, where zero-shot plain text is the stronger baseline (one-shot plain text performs worse, as the paper demonstrates). The comparison is conservative — any confound works against TMK, not for it. The paper provides three explicit justifications. The critic's claim that attribution is "impossible" is incorrect given the direction of the confound.
- **Harsh Critic: "Extraction function may have been applied asymmetrically"** — REMOVED as speculative strawman. The paper describes adding extraction code for random Blocksworld; the natural reading is that this was applied uniformly across conditions. No evidence supports asymmetry.
- **Harsh Critic: "Should implement CoT/CoS/ReACT as baselines"** — REMOVED as scope creep. The paper's comparison is TMK vs. plain text on the PlanBench benchmark. The Related Work critique of existing methods establishes motivation; implementing them all as baselines is beyond reasonable scope for a paper introducing a new prompting framework.
- **Strength Finder: "Cross-disciplinary grounding in cognitive science provides a coherent theoretical frame"** — REMOVED. While interesting, the cognitive science discussion (Section 5.2.2) is speculative and metaphorical — applying Bloom's taxonomy to LLMs without operationalization. It does not constitute a concrete, evidence-backed strength.

## Novel Insights
The performance inversion — where TMK prompting makes a model perform better on symbolically opaque tasks than on semantically cued ones, reversing the natural difficulty ordering — is a genuinely striking empirical phenomenon that goes beyond "structured prompting helps." It suggests that the right prompt format can qualitatively shift an LLM's reasoning strategy rather than merely providing better context. If this inversion effect replicates across other domains, it would have implications beyond planning for how we think about prompt design and model reasoning modes.

## Suggestions
- The single highest-impact addition would be one format ablation: compare TMK against the same domain knowledge encoded as flat JSON (same fields, no T-M-K hierarchy) or as a structured bullet-point list. This would let the paper claim whether TMK's specific framework matters or whether structured domain knowledge in any form suffices.
- Report the number of test problems per Blocksworld variant and add binomial confidence intervals to Table 2 — this is straightforward and would substantially strengthen the credibility of the smaller-magnitude results.
- Tone down the mechanistic certainty in the abstract and conclusion to match the more careful "hypothesis" framing used in the body text.

---

**Calibration anchor comparison:**

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| Planning in Strawberry Fields (jOuHjFw71C) | 3.00 | R1 | Pure benchmarking of o1 on PlanBench, no novel method. Our paper has a novel prompting method and a striking empirical finding — clearly stronger. |
| GRAIL (oyXoGJQlUf) | 3.00 | R1 | Action-rule induction with LLMs for robotics. Different domain, lower contribution. Our paper is stronger. |
| Exploring Planning Capabilities (koza5fePTs) | 2.00 | R1 | Benchmark construction + many-shot ICL. Limited novelty. Our paper is stronger. |
| Thinking Forward and Backward (cWrqs2lwCJ) | 3.00 | R1 | Backward planning with LLMs. Interesting direction but limited execution. Our paper has more striking empirical results. |
| ActionReasoningBench (NUD03NBDOE) | 6.75 | R1 | Comprehensive benchmark across 8 domains, 6 RAC dimensions. More thorough evaluation than our paper. Our paper is weaker on evaluation breadth. |
| PuzzlePlex (GT4gMdvVFp) | 5.50 | R1 | Puzzle benchmark for LLM reasoning. Single contribution type, accepted. Comparable to our paper. |
| Assessing Knowledge-intensive Reasoning (iSTMsye6SD) | 5.25 | R2 | Benchmark generation pipeline. Rejected. Our paper has a more compelling empirical finding. |
| ChinaTravel (9dfRC2dq0R) | 5.00 | R2 | Travel planning benchmark. Rejected. Our paper is stronger. |
| Robotouille (OhUoTMxFIH) | 5.67 | R2 | Async planning benchmark. Accepted with similar limitation profile (single domain, limited baselines). Comparable to our paper. |
| SWAP (BaMkS6E2Du) | 5.50 | R2 | Multi-step reasoning framework. Rejected due to novelty concerns, unclear notation. Our paper is cleaner but more limited in scope. Comparable. |
| LLMs Can Plan Only If We Tell Them (K3KrOsR6y9) | 6.40 | R2 | AoT+ prompting for planning on Blocksworld+Logistics. More comprehensive evaluation (multiple domains, ablations, attention analysis). Our paper is clearly weaker on evaluation thoroughness. |
| LEPA (KmmNb7631I) | 6.25 | R2 | Self-training for LLM planning with abstract plans. Stronger contribution with learning component. Our paper is weaker. |

**Round 1 bracket:** 5.0–6.0 (between weak anchors at 2-3 and strong at 6.75-8.0)

**Round 2 narrowing:** Within the bracket, the paper is most comparable to Robotouille (5.67, Accept) and SWAP (5.50, Reject). It is clearly below LLMs Can Plan Only If We Tell Them (6.40). I place it at **5.5** — a borderline paper with a genuine striking finding but significant methodological gaps (no format ablation, no statistical reporting, single domain).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>