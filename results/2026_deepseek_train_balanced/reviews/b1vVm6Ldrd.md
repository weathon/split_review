## Summary

EgoSocialArena introduces a benchmark framework to evaluate LLMs' Theory of Mind and "socialization" (own-mental-state evolution) capabilities from a first-person perspective. It converts existing third-person ToM benchmarks (ToMI, ToMBench) to first-person via role-prompting, adds three manually-designed social scenarios (Counterfactual, New World, Blackjack), and two interactive environments (Number Guessing with rule-based opponents, Texas Hold'em with RL opponents). The framework comprises 2,195 entries across seven scenarios, evaluated on 9 LLMs with a human baseline.

## Strengths

- **Systematic first-person conversion methodology with measurable impact.** The paper proposes a concrete, replicable conversion pipeline (system message modification, pronoun replacement in stories/questions/answers) and demonstrates empirically in Table 2 that every tested LLM achieves a different score in first-person vs. third-person on the ToMI dataset (e.g., Claude-3-5-Sonnet: 71.0→80.5; GPT-4-Turbo: 55.4→69.7). This establishes that perspective shift non-trivially changes evaluation outcomes, supporting the paper's core motivation that first-person evaluation is a distinct measurement axis.

- **Creatively designed novel scenarios.** The Counterfactual (inverted Rock-Paper-Scissors rules) and New World (alternative social realities) scenarios genuinely test whether models can adapt to novel rule structures, going beyond standard reading-comprehension ToM. Results in Table 3 show dramatic variation (o1-preview: 90.0% vs. GPT-3.5: 37.0% on Counterfactual; Claude: 90.0% vs. LLaMa-3-8B-Chat: 6.7% on New World), demonstrating these scenarios capture meaningful variance beyond general reasoning ability.

- **Careful data construction with high annotation quality.** The two-round validation process achieved 97.6% average agreement (Section 4.1), and the manual evaluation for Blackjack reached 96.3% inter-evaluator consistency — solid quality control exceeding typical NLP benchmark construction standards.

- **Qualitative analysis revealing specific failure patterns.** The identification of "mid-point belief," "strange guess," and "get back on track" patterns (Section 5.4, Figure 5) provides diagnostic insight into how models reason about opponents, going beyond aggregate accuracy scores.

## Weaknesses

### Fatal

None.

### Major

- **The conversion methodology lacks a control to distinguish genuine perspective effects from task simplification.** The paper reports that all LLMs perform better on first-person ToMI than the original third-person version (Table 2). The across-the-board improvement is equally consistent with a simpler explanation: converting narrative comprehension ("What does Sally believe?") into direct role-prompting ("What do you believe?") makes the task easier regardless of perspective effects, since LLMs are heavily tuned to follow "you are X" instructions. To establish that the conversion measures something distinct about first-person reasoning, the paper would need a control transformation — e.g., converting third-person benchmarks to first-person but then asking about *another* character from that first-person frame, or varying role assignment systematically. The paper does not provide or discuss such controls, so the central claim that first-person evaluation reveals a meaningfully distinct capability is not adequately supported by the evidence presented.

### Minor

- **The ToM/socialization conceptual distinction is operationalized but not justified.** The paper defines "socialization" as own mental state evolution and maps first-order third-person ToM questions → socialization, while higher-order → ToM (Section 3.1). No argument is given for why the *order* of the original ToM question should correspond to a different underlying capability after conversion. Both cases involve the model reasoning about mental states — the target shifts between self and other, but the paper does not establish that this distinction is meaningful as measured. This weakens the two-category structure but does not invalidate the broader framework.

- **The "babysitting" problem is asserted without empirical evidence.** Section 3.3 states that weaker models "distract" stronger ones during LLM-LLM interaction, motivating the replacement with rule-based/RL opponents. No experimental data, quantitative analysis, or even illustrative examples are provided to demonstrate that this phenomenon occurs or how large its effect is. While the resulting design choice (controlled opponents) is reasonable, the lack of evidence for the claimed problem makes it hard to assess whether simpler alternatives would suffice.

- **Number Guessing scenarios have a tenuous connection to theory of mind.** Level 1 (constant 50) is a trivial pattern-recognition task — a model can succeed by guessing the midpoint without any mental-state reasoning. Level 2 (arithmetic sequence: 50, 45, 40...) can be solved by detecting linear patterns. The paper itself acknowledges this implicitly (Section 5.4: models "grasp some patterns" without ToM reasoning) but continues to frame these as ToM evaluations. Texas Hold'em (classifying RL agents as aggressive/conservative) is a behavioral classification task rather than recursive mental-state reasoning.

- **Per-scenario data breakdown is not reported.** The total of 2,195 entries is given, but the distribution across Daily Life, Counterfactual, New World, Blackjack, Number Guessing (×3 levels), and Texas Hold'em is not provided. Sample sizes likely vary substantially, making it hard to assess the reliability of per-scenario accuracy estimates.

- **The human baseline is limited.** Ten graduate students from the same institution is a small sample. The identical 90.2% for both third-person and first-person ToMI is unusual and should be discussed — it may indicate ceiling effects rather than insensitivity to perspective.

### Trivial

None.

## Nice-to-Haves

- **Confidence intervals or variance estimates** would strengthen the benchmark, though single-run evaluation is the norm in this area.
- **Concrete examples of the conversion** (before/after pairs of system message, story, question, and options) would improve replicability.
- **Expanded coverage of the Counterfactual and New World scenarios** — these are the paper's most distinctive contribution and could naturally serve as its core offering.

## Removed Points

These points were flagged for removal, included here for reference:

- *"LLMs do not have mental states, so the ToM/socialization framing collapses"* — This is a general philosophical objection applicable to ALL LLM ToM research (models don't have genuine beliefs either), not a paper-specific weakness. Removed.
- *"The scaling claim (line 241) is contradicted by the paper's own data"* — The paper specifically compares LLaMa-3-8B-Chat with LLaMa-3-70B-Chat and LLaMa-3-8B-Chat with LLaMa-3-8B-Instruct. The critic cited LLaMa-3.1-405B-Instruct, which is a different model generation. The claim as stated is supported by the comparisons the paper explicitly makes. Removed.
- *"Using 'socialization' is unconventional in social sciences"* — The paper defines the term clearly and uses it consistently. Terminological novelty is not a weakness. Removed.
- *"The ToM/socialization distinction is 'structural' and 'fatal'"* — The conceptual boundary is imperfectly justified, but the paper's core contributions (first-person conversion, novel scenarios, interactive environment) do not depend on this distinction being perfectly valid. Demoted from fatal to minor.

## Novel Insights

The reviews collectively surface one useful observation beyond the paper's own claims: the Number Guessing scenario's structure (constant 50, arithmetic sequences) creates a natural confound between pattern-matching and theory-of-mind reasoning. The o1-preview's 90% across all three levels likely reflects proficiency at pattern completion (including the meta-pattern of "the opponent follows a rule") rather than mental-state inference per se. This highlights a general challenge for interactive ToM evaluation: distinguishing genuine mental-state reasoning from statistical pattern recognition in rule-based environments. Future work should design scenarios that explicitly control for this confound (e.g., comparing rule-based opponents against opponents that have genuine beliefs to deceive).

## Suggestions

1. Add a control experiment for the conversion methodology: test models on first-person versions of non-social reasoning benchmarks (e.g., math word problems) to disentangle perspective effects from generic role-prompting ease.
2. Provide at least illustrative evidence for the "babysitting" phenomenon — even a small-scale quantitative comparison or a single qualitative example would substantially strengthen the motivation.
3. Report per-scenario sample sizes and discuss how the distribution affects measurement reliability.
4. Reframe the paper's contribution around what is most distinctive and well-supported: the first-person perspective as a methodological innovation and the Counterfactual/New World scenarios as novel evaluation tools.
5. Discuss the human baseline's identical 90.2% on both ToMI versions and consider whether ceiling effects limit its informativeness.

## Score and Decision

The paper makes a genuine contribution: it is the first to systematically convert ToM benchmarks to a first-person perspective, introduces creatively designed novel scenarios (Counterfactual, New World) that go beyond standard reading-comprehension ToM, and provides careful data construction with high annotation quality. However, the major weakness — lack of validation controls for the conversion methodology — means the central empirical claim (that first-person evaluation reveals a meaningfully distinct capability rather than reflecting task simplification) is not adequately supported. The ToM/socialization distinction is also under-justified, and the interactive scenarios' connection to ToM is tenuous.

Overall, the paper has real contributions but significant methodological gaps. At a top venue, this is a borderline paper that would benefit from revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Weak Accept</decision>