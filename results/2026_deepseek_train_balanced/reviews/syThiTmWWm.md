## Summary

This paper demonstrates that "null models" — models that output a single constant string irrelevant to every input instruction — can achieve top-ranked win rates on three widely-used automatic LLM benchmarks (AlpacaEval 2.0, Arena-Hard-Auto, MT-Bench) by exploiting syntactic confusion in the auto-annotator's evaluation template. A structured response that closes the template's JSON structure and fabricates a new evaluation context achieves an 86.5% LC win rate on AlpacaEval 2.0, an 83.0 score on Arena-Hard-Auto, and a 9.55 on MT-Bench — all surpassing verified SOTA models. The attack is transferable across instructions (using a public instruction set for optimization) and generalizes across auto-annotators (GPT-4, Llama-3-8B/70B). The paper tests two anti-cheating defenses (template paraphrasing and PPL filtering) and shows both are insufficient.

## Strengths

1. **Null models with structured responses achieve top-ranked scores on three major benchmarks.** Table 1 shows the Structured+RS variant achieves an 86.5% LC win rate on AlpacaEval 2.0 (+29 points over verified SOTA), 83.0 on Arena-Hard-Auto (matching verified SOTA), and 9.55 on MT-Bench (exceeding the 8.96 SOTA). These numbers are striking and clearly demonstrate a real vulnerability.

2. **The attack is transferable across instructions without access to the benchmark's private test set.** The paper assumes the 805/500/80 benchmark instructions are private (Section 2, threat model) and optimizes the adversarial prefix using a disjoint public instruction set (UltraFeedback). Despite this restriction, the transferable prefix still drives win rates far above SOTA, making the attack realistic rather than reliant on test-set access.

3. **Systematic ablation on open-source auto-annotators shows the vulnerability extends beyond GPT-4.** Random search without test-instruction access achieves 95.4% LC win rate on Llama-3-8B and 95.1% on Llama-3-70B (Table 2). With test-instruction access, these approach ~99%, confirming the vulnerability is not GPT-4-specific.

4. **The paper tests two candidate anti-cheating defenses and demonstrates both are insufficient.** Template paraphrasing still yields a 92.1% LC win rate on the unseen official template. The PPL filter is ineffective because the structured response's perplexity falls below the reference-model threshold (Figure 7). These negative results strengthen the paper's call for more robust defenses.

5. **The threat model is appropriately stringent.** The cheater has no access to the auto-annotator's parameters, no access to test instructions, and the null model generates a constant output across all inputs (Section 2). This conservative setup means the demonstrated vulnerabilities are lower bounds on what a less restricted adversary could achieve.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The high-level framing ("null models achieve high win rates") omits the crucial qualifier that this requires a specifically crafted structured response that prompt-injects the judge's template.** The abstract and title say "even a 'null model' that always outputs a constant response can cheat automatic benchmarks" without making clear that arbitrary constant responses achieve near-0% win rates (Figure 1b shows persuasive responses at 0.0–0.6% LC). Only specifically-structured responses that break the template syntax succeed. The paper body explains the mechanism clearly (line 52: "exploiting a weakness in LLMs, which may become confused during syntactic analysis when processing the evaluation templates"), but the high-level framing could lead a reader to infer a simpler failure (e.g., that judges intrinsically prefer short/empty outputs) rather than the actual template-injection vulnerability.

2. **The paper does not quantify the contribution of the structured component vs. the RS-optimized prefix vs. the template-breaking characters for GPT-4.** The paper states qualitatively that an adversarial suffix alone is "ineffective" (line 221) and shows Structured alone (76.8%) vs. Structured+RS (86.5%). But given the 9.7 percentage-point gap, readers cannot assess whether the RS prefix is providing genuine improvement or is mostly cosmetic for GPT-4. For Llama models the structured response alone is nearly useless (2.9% and 0.4%), and RS drives everything — this asymmetry deserves explicit discussion.

3. **The threat model does not explicitly state the assumption of template access.** The cheater is assumed to have no access to auto-annotator parameters or test instructions (line 170). But the entire attack depends on knowing the exact evaluation template format (closing braces precisely match the template structure). Line 172 says "Our experiments utilize the official evaluation templates" — but this is presented as an experimental choice, not an explicit threat-model assumption. Since the templates are public for these benchmarks, this is a realistic assumption, but making it explicit would sharpen the paper's characterization of the attack surface.

4. **No confidence intervals for AlpacaEval 2.0 and MT-Bench results.** Table 1 reports Arena-Hard-Auto with a 95% CI but only point estimates for the other two benchmarks. While temperature=0 makes results deterministic for a fixed model, the RS optimization itself involves randomness, so some indication of stability (e.g., multiple RS runs) would strengthen the quantitative claims.

### Trivial

- None beyond those already addressed above.

## Nice-to-Haves

- Testing a defense that addresses the root cause (e.g., sanitizing outputs to prevent template-breaking syntax, or using programmatic/structured evaluation that does not interpolate raw outputs into a prompt) would strengthen the paper's call for better defenses. The current defense experiments show that two naive approaches fail, but do not explore what might actually work.
- An ablation quantifying how much of the win rate comes from each component (closing braces, fabricated context, RS prefix) would make the mechanism clearer.
- Reporting the cost of the RS optimization (number of API calls, cost in dollars) would help assess the practical threat level.

## Removed Points

These points were raised by reviewers but are removed with justification:

- **"SOTA comparison is rhetorically misleading"** (Harsh Critic point 2): The paper is unambiguously about cheating benchmarks. Comparing the null model's benchmark scores to SOTA models' scores is a natural way to quantify severity. No reasonable reader would interpret "our null model outperforms SOTA on this benchmark" as claiming the null model is a better LLM. Removed: does not reflect a real weakness.

- **"MT-Bench result is insufficiently explained"** (Harsh Critic point 4): The paper explicitly references appendix figures (Figures~\ref{fig:arena_template} and~\ref{fig:mtbench_template}) showing the full templates and structured responses for these benchmarks. These were stripped by the PDF parser, not omitted by the authors. Removed per rules (missing appendix content).

- **"RS algorithm is underspecified"**: The paper references Algorithm~\ref{alg:urs} in the appendix, which was stripped by the parser. The high-level description (sampling modifications, minimizing aggregated loss) is provided. Removed per rules (missing appendix content).

- **"Not testing defenses that address the root cause"**: Moved to Nice-to-Haves. This is a reasonable suggestion for strengthening the paper but is not a weakness — the paper's goal is to demonstrate the vulnerability, not to solve it.

- **"Persuasive responses also successful"** — misreading of the paper; persuasive responses achieve 0.0–0.6% win rates.

## Novel Insights

The most insightful observation that emerges from combining the two reviews — one that neither review states individually — is that the paper's significance lies not in the novelty of the attack mechanism (prompt injection through unsanitized output fields is a known vulnerability class) but in its empirical demonstration that this vulnerability completely subverts three widely-used benchmarks that the community trusts for model comparisons. The paper's real contribution is serving as a stress test showing these benchmarks have essentially no security boundary between "model output" and "evaluation instruction." The fact that a constant string with no task-relevant content can achieve top ranking (SOTA-overpassing) is what makes the paper impactful, not the injection technique itself. This reframing explains both the paper's genuine importance and why its own "null model" framing (which implies a deeper LLM-judge failure) slightly overstates the mechanism's depth.

## Suggestions

1. In the abstract and introduction, add a sentence clarifying the mechanism: "These constant responses achieve high win rates not because the judge prefers empty output, but because the response is structured to break the judge's prompt template and inject a fabricated evaluation context — a template-injection vulnerability."

2. Add an ablation row to Table 1 showing the RS-only result (structured component stripped) for GPT-4 to quantify the structured component's contribution.

3. Explicitly state in the threat model (Section 2) that the attacker has access to the public evaluation template, and discuss whether this assumption holds for each targeted benchmark.

4. Add confidence intervals for AlpacaEval 2.0 results or a brief note on the stability of RS optimization across seeds.

## Score and Decision

The paper's core empirical finding is sound, important, and well-supported by experiments across multiple benchmarks and auto-annotators. The weaknesses are primarily about framing precision and presentation, not about validity of results. The paper makes a clear contribution to the community's understanding of benchmark vulnerabilities.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>