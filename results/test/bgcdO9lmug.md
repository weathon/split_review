Now I have all the information I need. Let me compose the final consolidated review.

## Summary

The paper proposes REPROMPT, a method for automatically optimizing the step-by-step instructions in prompts for LLM agents by summarizing batch chat histories from interactive agent loops (e.g., ReAct, Reflexion) and using an LLM-based optimizer to iteratively refine the prompt. The core idea is to operate without a final solution correctness checker by leveraging intermediate feedback already present in agent interactions. The method is evaluated on PDDL generation (single-epoch optimization using pre-existing human annotations) and Travel Planner (multi-epoch optimization using Reflexion feedback), showing first-round success rate improvements.

## Strengths

- **Practical elimination of a dedicated solution checker is a genuine contribution.** The paper makes a principled distinction between needing a final correctness evaluator (as required by prior APE methods) and being able to use intermediate feedback that is already generated during normal agent interaction loops. Section 3.2.1 motivates this clearly—settings where final evaluation is expensive, inaccurate, or missing (e.g., GPTs, online user interactions) are common and prior methods cannot operate there.

- **Empirical breadth across two contrasting feedback regimes.** REPROMPT is tested on PDDL generation (human expert annotations—expensive, accurate) and Travel Planner (Reflexion's tool-based feedback—cheap, noisy). The method improves first-round success in both, showing it is not brittle to feedback quality. The PDDL result is especially notable: training on one domain (Tyreworld) generalizes to other related domains without introducing new errors (the error set of the new prompt is a subset of the original's).

- **The ablation study directly tests a key design trade-off.** Table 3 holds the total budget fixed (training samples × epochs = 50) and finds that intermediate sample sizes (5 or 10) outperform both very small (overfits to noise) and very large (insufficient epochs for convergence) settings—matching the intuition the paper's gradient-descent analogy would predict.

- **Honest error analysis and transparency about failure modes.** Section 5 documents practical issues (incomplete prompt templates, accidental format changes), provides LLM-based workarounds, and reports the empirical failure rate for one fix ("less than 10%"). This candor strengthens reproducibility for subsequent work.

- **Identifies a specific bottleneck addressed by the optimization.** In Travel Planner, REPROMPT specifically improves the "reasonable city route" commonsense constraint, which the original Travel Planner paper identified as a challenge where agents struggle to align reasoning with actions. This targeted diagnosis gives readers a concrete example of the type of issue the summarizer catches.

## Weaknesses

### Fatal
None.

### Major

- **The exact prompts for the summarizer and optimizer are not provided, significantly hampering reproducibility.** The method's core behavior is defined by the natural-language instructions given to two LLMs (the summarizer and the prompt optimizer). The paper describes the *role* of each (Section 3.2.1: "summarize the primary focus point" for the summarizer; follow rules 1–2 and steps 1–5 for the optimizer) but never discloses the actual prompt templates. Because LLM behavior is highly sensitive to wording and framing of instructions, and because the paper acknowledges that both failure modes (incomplete prompts, accidental format changes) and ad-hoc LLM-based fixes are needed, a reader cannot faithfully reproduce the method or assess whether results depend on specific prompt phrasings. This is not a minor appendix issue—it is central to whether the method is an algorithmic proposal or an anecdotal demonstration.

- **Evaluation is too thin to support the paper's claimed generality.** (a) Only one LLM (GPT-4-turbo-1106-preview) is used; no variance or replication across seeds is reported. Though temperature=0 reduces randomness, LLM API outputs are not truly deterministic, and no confidence intervals are given. (b) The PDDL experiment trains on a single domain (Tyreworld) with one epoch. The text refers to "other related domains" in Table 1 but does not explicitly name them in prose or describe how many there are or what baseline results look like individually. (c) The only APE baseline is PromptAgent, which the paper itself acknowledges is designed for single-round QA and performs worse. There is no comparison to any prompt optimization method adapted to multi-turn agent settings. The paper's central claim—that REPROMPT improves over prior APE—would be substantially stronger with even one adapted baseline (e.g., using an LLM-based scoring function to simulate a final checker in the agent setting). (d) The Travel Planner experiment uses only 10 training examples drawn from a validation set of 180, and the paper does not analyze how sensitive the results are to which 10 are chosen.

- **The PDDL experiment's "no checker" framing is strained.** The PDDL experiment uses pre-existing human expert annotations (correctness judgments) from Guan et al. (2023) as its training signal. These annotations are, in practice, a form of final solution checking—they assess whether each generated action's preconditions and effects are correct. While REPROMPT benefits from not requiring *new* annotations during training (the annotations already existed), the scenario demonstrated is not the one promised in the framing ("final evaluation could be expensive, inaccurate, or even missing"). The Travel Planner experiment better matches this framing.

### Minor

- **The error analysis does not quantify how often the optimizer produces invalid prompts.** Section 5 mentions "many times" for incomplete templates and "less than 10%" for accidental format changes, but the incomplete-prompt failure rate is not given, nor is the additional cost of the LLM-based filler quantified. Without this, readers cannot assess the reliability or overhead of the optimization process.

- **No systematic analysis of how optimized prompts change across epochs or domains.** The paper gives one illustrative example (the "reasonable city route" constraint in Travel Planner) but does not characterize what kinds of modifications the optimizer tends to make, how much the prompt drifts from the original, or whether improvements come from genuinely useful heuristics versus overfitting to the training set's quirks.

- **The method cannot update in-context examples, which the paper acknowledges but dismisses without empirical justification.** The authors state this is "extremely challenging" and that they "do not see any empirical drawback," but this is an untested assumption. For tasks where output format or reasoning pattern is primarily example-driven, this is a clear limitation that future users should weigh.

### Trivial

- The gradient-descent analogy (Contributions 1 and framing throughout) is purely presentational—the paper explicitly calls it "similar to" and "like" rather than claiming formal equivalence. It does not harm the paper but adds little analytical value.

## Nice-to-Haves

- Provide the exact prompts (summarizer and optimizer) in an appendix. Without these, the method is not reproducible by the standards of the field.
- Run at least 2–3 seeds and report variance, especially for Travel Planner where the training set is small.
- Add at least one adapted APE baseline for the agent setting (e.g., using an LLM judge as a scoring function for OPRO-like optimization).
- Quantify the frequency of each optimizer failure mode and the cost of the LLM-based template filler.
- Analyze prompt drift: show examples of the prompt at each epoch and categorize the types of modifications.
- Test on at least one additional agent task domain.

## Removed Points

These points were raised by reviewers but are excluded from the main assessment for the reasons stated:

- *Related works missing OPRO*: Per guidelines, I cannot cite missing related works. The general point about insufficient baseline comparison is kept in Major Weaknesses.
- *Table 3 "garbled to the point of being partially unreadable"*: This is a parser artifact from image extraction, not a paper flaw.
- *Gradient descent analogy "misleading" / undermines contribution*: The paper is consistently clear that this is an analogy ("like," "similar to"). The reviewer overstated this.
- *"No solution checker" claim is "misleading as stated"*: The paper carefully qualifies this—it says "final solution checker" throughout. The Travel Planner experiment cleanly supports the claim. The PDDL tension is noted in Minor Weaknesses.
- *Missing appendix, missing proofs*: These are parser-stripped sections; they exist in the original submission.
- *Formatting/typo nitpicks*: Parser artifacts.
- *Strength Finder's claim that the GD analogy "translates to a concrete optimization procedure"*: The paper's ablation study is a genuine strength, but the GD analogy is just framing. Rephrased in Strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews surface complementary perspectives—the harsh critic correctly identifies under-specification and evaluation limitations, while the strength finder correctly identifies the core contribution (eliminating the need for a final checker by leveraging intermediate signals) and the honest error analysis as distinctive features. The tension between the two is that the strength finder sees a promising algorithmic idea, while the harsh critic sees an underspecified sketch. Both are partially right: the idea is novel and practically motivated, but the paper's current execution is too thin to fully realize it.

## Suggestions

1. **Disclose the exact prompts.** This is the single highest-impact fix. Without it, the paper is an unreproducible sketch.
2. **Strengthen the PDDL evaluation**: report domain-by-domain results, test on 3–5 domains, and include at least one comparison to a cheap automated baseline.
3. **Add error bars or multiple seeds**, especially for Travel Planner where the training set is only 10 examples and results could be sensitive to selection.
4. **Quantify optimizer failure rates** (incomplete templates, format changes) so readers can assess reliability and cost.
5. **Run a simple adapted baseline** for the agent setting: e.g., a basic LLM-scored prompt search over 10–20 candidates to establish a stronger lower bound than PromptAgent.
6. **Soften the "no checker" claim** for the PDDL setting and clarify that the contribution is about using *intermediate* (cheaper/available) signals rather than requiring a purpose-built final evaluation oracle.

## Score and Decision

The paper proposes a practically motivated idea at a timely intersection of prompt engineering and LLM agents. The core concept—using batched chat history summarization to iteratively refine agent prompts without a dedicated solution checker—is novel and has genuine potential impact for settings like GPTs, online agents, and cost-sensitive deployments where final evaluation is unavailable.

However, the paper's current execution has significant gaps. The method is underspecified (exact prompts for the two LLM components that define the algorithm are not provided), the evaluation is thin (one LLM, no variance, limited baselines, one PDDL training domain), and there is a tension between the "no checker" framing and the PDDL experiment's use of expensive human annotations. These are not fatal flaws—the idea survives all of them—but they prevent the paper from being a complete, reproducible contribution in its current form.

The paper would be suitable for a workshop or a venue with a revision cycle where the prompts could be disclosed, an adapted baseline added, and minimal variance reporting included. In its current form, it is not yet ready for a top-tier conference.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>