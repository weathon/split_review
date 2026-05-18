Now I have a thorough understanding of the paper and all reviewer claims. Let me write the final consolidated review.

## Summary

This paper introduces SECToR (Self-Education via Chain-of-Thought Reasoning), a self-training procedure where a language model uses chain-of-thought (CoT) reasoning to generate training data for addition problems beyond its supervised training range, then fine-tunes itself without CoT on that self-generated data. The authors frame CoT reasoning as a "policy improvement operator" analogous to MCTS in AlphaZero. They demonstrate that a 582M-parameter ByT5 model, after supervised fine-tuning only on 1–6 digit addition, can bootstrap itself to solving up to 28-digit addition with ≥98% accuracy through 22 steps of self-improvement using entirely self-generated data.

## Strengths

- **Genuine empirical demonstration of multi-step self-improvement in language models for arithmetic.** The 582M model undergoes 22 successive rounds of self-training without the rapid degeneration (error avalanching) that has limited prior self-learning efforts to a few steps at most. This is a nontrivial result that advances the state of the art in LLM self-training (Section 4, Figure 3).

- **Simplify-and-Guess decoding with commutativity checks effectively mitigates error avalanching.** The paper introduces a novel decoding method that combines CoT-based problem simplification with majority-vote self-consistency. Figure 4 shows this reduces data-generation error rates by roughly an order of magnitude compared to direct sampling or simplify-only baselines. The commutativity check further reduces errors, making sustained multi-step self-training feasible.

- **Clean framing of the self-improvement loop.** The core insight — using CoT to generate solutions the model cannot reach directly, distilling those into direct capabilities, and thereby expanding the set of problems the model can solve with CoT in the next iteration — is clearly articulated and supported by the experimental design (Figure 1, Section 2.1).

## Weaknesses

### Major

- **The paper lacks controlled experiments needed to isolate the self-training loop as the causal driver of improvement.** The most natural question a reader would ask is: how much of the observed improvement is attributable to the self-training mechanism specifically, versus to other factors such as continued training, the particular curriculum, or the CoT generalization capabilities that already exist? Concretely:
  - There is no comparison to a model that receives additional supervised training on the same 1–6 digit data (with more iterations) to see whether continued training alone, without self-generated data from larger digits, produces any length generalization.
  - There is no full-loop ablation showing what happens when the commutativity consistency check is removed — does the loop collapse, or does it merely terminate sooner? Figure 4 shows error rates for data *generation* with and without checks, but never for the *full self-training loop* without them.
  
  Without experimental isolating of these factors, attributing improvement specifically to the self-training loop remains partially speculative. The paper would be substantially strengthened by even one control experiment that directly demonstrates failure or degradation when a key component is removed.

- **The mechanism connecting self-training on direct (non-CoT) solutions to improved CoT performance on harder problems is not analyzed.** The paper's central loop works as follows: (1) the model uses CoT to solve N+1-digit problems → (2) the model is trained to solve N+1-digit problems *without* CoT → (3) the improved model can now solve N+2-digit problems *with* CoT. Step (3) is critical, but why it happens is left as speculation ("freeing up reasoning capacity," Section 2.1). No probing, representation analysis, or behavioral ablation is provided to explain how learning direct solutions for one digit length helps CoT generalization to the next. This limits the paper from being an explanation to being a proof-of-concept demonstration, reducing its value for guiding future work on other tasks.

### Minor

- **The title overstates what is demonstrated.** "Chain-of-Thought Reasoning is a Policy Improvement Operator" is a declarative claim that implies theoretical generality and formal guarantees analogous to MCTS in AlphaZero. The paper's own content is appropriately hedged ("hypothesis," "proof-of-concept"), and the evidence is limited to a single task (addition) with a single model size (582M). A title such as "Chain-of-Thought Reasoning as a Policy Improvement Operator for Self-Training Addition" or similar would better match the scope of evidence.

- **Only a single training run is reported without error bars or variance measures.** The paper explicitly notes this (line 251), and the evaluation uses 100 examples per digit length. While this is acceptable for a proof-of-concept, it limits the robustness of the quantitative claims. A second run would meaningfully strengthen confidence.

- **The Simplify-and-Guess parameter K=5 lacks sensitivity analysis.** The paper states K=5 "was found to be a good balance between computational speed and accuracy" but provides no ablation showing how performance or loop duration varies with K. Since this parameter directly controls the data quality / computational cost trade-off, some sensitivity analysis is needed.

- **The commutativity check is highly domain-specific.** While clever and effective for addition, this consistency mechanism does not generalize to most other tasks (multiplication, programming, reasoning). The paper acknowledges this (Section 5) but only in passing. The broader value of SECToR for non-commutative domains depends on finding analogous self-consistency checks, which is a nontrivial open problem.

- **The paper does not fully justify why the self-training phase is necessary given that CoT already generalizes to N+1 digits.** The precondition for starting self-training is that the model already generalizes nearly perfectly to N+1 digits *with* CoT. If the model can already solve N+1-digit problems via CoT, what does self-training on direct solutions add? The paper's answer is that it enables solving even larger problems (N+2) with CoT, but this claim is the very one that lacks mechanistic analysis (see Major weakness above).

### Trivial

None.

## Nice-to-Haves

- Sensitivity analysis on K (the number of Simplify-and-Guess rounds).
- An ablation running the full self-training loop without commutativity checks to directly demonstrate error avalanching in the loop (not just in data generation).
- Comparison of final model accuracy to a supervised model trained on ground-truth 1–28 digit addition, to contextualize how much is lost (or not) by self-training.
- Reporting the number of self-generated examples per iteration and the mixing ratio of old to new data, if not already in the (stripped) hyperparameter appendix.

## Removed Points

- **"The paper does not report the total number of self-generated training examples used per iteration"** — Removed because the paper references Section sec:hyperparameters for such details; the parser strips appendix content from all papers, so this information likely exists in the original submission.
- **"The paper does not establish that the self-training loop drives improvement [framed as a fatal flaw]"** — Re-framed as a Major weakness rather than a fatal one, because Figure 3 does show progressive improvement during self-training and the paper's core claim is about the *possibility* of self-teaching, not optimality. The point about missing controlled experiments is preserved in Major but the severity is calibrated to the paper's proof-of-concept class.
- Several of the Strength Finder's generic formulations were condensed or merged (e.g., multiple generic strengths about "interesting idea" or "important problem" were dropped as they lack specific evidence content).

## Novel Insights

Beyond the paper's own contributions, the most thought-provoking aspect is the observation that CoT generalization and direct-solving generalization have *different* length-extrapolation properties, and that these can be exploited asymmetrically: CoT can reach further than direct solving, and distilling CoT solutions into direct weights somehow extends the CoT frontier further still. This asymmetric bootstrapping — using a weaker-but-further-reaching capability to improve a stronger-but-limited capability, which in turn extends the weaker capability — is a potentially general principle that the paper surfaces but does not deeply investigate. The connection to "Type 1 / Type 2" reasoning (Kahneman) and process supervision is also noted but underexploited.

## Suggestions

1. Add at least one control experiment: (a) compare SECToR to a model that continues training on ground-truth 1–6 digit data for the same number of additional iterations, or (b) run the self-training loop without the commutativity consistency check to directly demonstrate its necessity for loop stability.
2. Temper the title to match the scope of evidence — the current declarative title implies theoretical guarantees that the paper does not (and does not aim to) provide.
3. Include a second training run with variance estimates to improve confidence in the quantitative results.
4. Add probing or behavioral analysis to shed light on *why* learning direct solutions for N+1 digits improves CoT ability on N+2 digits — even simple experiments (e.g., analyzing whether the model learns a digit-by-digit addition algorithm or relies on pattern matching) would substantially increase the paper's explanatory value.
5. Provide sensitivity analysis for K in Simplify-and-Guess.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>