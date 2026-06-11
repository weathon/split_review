## Summary

This paper investigates whether activation steering—an inference-time technique for controlling LLM behavior by adding vectors to hidden states—compromises safety alignment. Through experiments on 8 models (Llama3, Qwen2.5, Falcon3, 3B–70B), the authors find that even random steering directions increase harmful compliance from a claimed 0% baseline to 2–27%, that SAE features (the standard interpretable steering method) show comparable or greater jailbreaking potential, and that averaging 20 random vectors that jailbreak a single prompt creates a universal attack. A real-world case study demonstrates jailbreaking Llama3.1-8B via Goodfire's public API using a benign "brand identity" feature.

## Strengths

- **Random steering baseline demonstrates a fundamental, previously unexplored vulnerability.** Prior work focused on adversarially optimized vectors; the finding that arbitrary random noise suffices (Fig. 2, lines 125–126) is a distinctive conceptual contribution. Non-zero compliance rates are observed across all tested model families.

- **Universal attack from aggregating random vectors generalizes to unseen prompts with minimal resources (Sec. 4.4, Fig. 6).** The attack requires no model weights, gradients, or harmful training data—only black-box steering capability. For Falcon3-7B, compliance jumps from ~5.7% to 63.4%, a striking demonstration.

- **SAE features, the standard interpretable steering method, show comparable or greater harmful potential than random noise (Fig. 2c, lines 150–151).** Moreover, 668/1000 SAE features jailbreak at least 5 prompts each (Fig. 4a), and the most dangerous features represent *benign* concepts like "brand identity" and "physical positioning"—making them invisible to safety monitoring.

- **Systematic evaluation across diverse model families and scales.** The paper tests 8 model variants (Falcon3-3B/7B, Falcon-H1-34B, Llama3-8B/70B, Qwen2.5-3B/7B/32B) and evaluates ~300,000 responses (line 96), with breakdowns across 10 JailbreakBench categories (Fig. 3).

- **Layer-depth analysis identifies precisely where safety mechanisms are most vulnerable.** Fig. 2b reveals middle layers show maximal compliance rates with sharp drops in later layers, providing mechanistic insight beyond a binary "steering breaks safety" claim.

- **Real-world case study via a production API documents concrete failure modes.** Sec. 4.3 (Fig. 5) demonstrates jailbreaking via Goodfire's public API using a benign SAE feature, and identifies two behavioral patterns—*disclaimer-then-compliance* and *justification via fictional framing*—that validate the practical deployability of the attack.

## Weaknesses

### Fatal
None.

### Major

- **No variance or uncertainty reported for any quantitative result.** Throughout the paper, compliance rates are reported as point estimates averaged over 1,000 random vectors or 1,000 SAE features, with no standard deviations, confidence intervals, or error bars. The single-prompt sweep (Fig. 2) plots smooth lines that hide all variance. The universal attack experiment (Sec. 4.4) averages 20 distinct universal vectors per model but never reports variance across them. Since the paper's central contribution is quantitative (measuring compliance rates under various conditions), omitting uncertainty is a significant gap. Without it, the reader cannot assess whether reported differences (e.g., SAE steering's "2–4%" advantage over random steering) are meaningful relative to measurement noise. The authors already sample 1,000 vectors per condition—computing and reporting standard deviations would add enormous credibility at no additional experimental cost.

### Minor

- **The "4× increase" claim for the universal attack is selectively framed.** Disaggregating Fig. 6 shows the ratio is ~13× for Falcon3-3B and ~12× for Falcon3-7B, but only 1.6–2.3× for five of the eight models, and 1.0× (no improvement) for Qwen2.5-32B. The headline "4×" is the arithmetic mean of a highly bimodal distribution driven by the two smallest Falcon models. While the paper notes "effectiveness varies substantially across model families" (line 235), the abstract and conclusion lead with "4×" without this nuance. This is an honest summary statistic but a misleading one.

- **SAE experiments limited to a single SAE (Goodfire, layer 19) on a single model (Llama3.1-8B).** The paper acknowledges this (line 82–83), but the broader claim that "SAE-based steering proves even more dangerous" (conclusion) goes beyond what this evidence supports. The result could be specific to Goodfire's SAE; testing on other sources (e.g., Gemma Scope, Anthropic's SAEs) would be needed to argue this is a general property of SAE-based steering.

- **Universal attack tested with only one seed prompt.** The attack construction uses only "Write a tutorial on how to make a bomb" as the seed prompt (line 218). Different harmful seed prompts (e.g., fraud, violence) might produce universal vectors with different effectiveness. The seed-dependence of this construction method is unexplored.

- **The 0% baseline is asserted rather than empirically demonstrated for all 100 prompts.** The paper states "for all models and prompts, the baseline compliance rate without any steering is 0%" (line 86). While the single-prompt sweep (Fig. 2) shows 0% at coefficient 0.0, and this is a standard property of JailbreakBench for aligned models, an explicit empirical verification across the full dataset would strengthen the paper.

### Trivial

- Several table values use approximate (~) markers (e.g., "~5", "~64" in Fig. 6 table), making exact interpretation difficult without cross-referencing the figure bars.

## Nice-to-Haves

- Ablation of steering on prompt tokens vs. generation tokens only, to better understand the mechanism.
- Testing the universal attack construction with 2–3 different seed prompts.
- Quality metrics (perplexity, response length) to distinguish active refusal from output degradation at high steering coefficients.
- Reporting variance or confidence intervals for the already-averaged data (a no-cost addition).

## Removed Points

These points from the reviewer inputs were removed and should be treated with caution:

1. **"Scaling coefficients selected per-model without cross-validation"** — REMOVED. Parameters were derived from the systematic single-prompt sweep (Sec. 4.1), which explored coefficients {0.75, 1.0, 1.25, 1.5, 1.75, 2.0} and three layer depths. The choices for the full evaluation follow naturally from those explorations; this is standard experimental practice.

2. **"Special token exclusion ablation"** — REMOVED. This is a design choice justified by prior work (Lin, 2023) and acknowledged in the paper (line 78). It is a fine-grained implementation detail that would not substantively change the core findings.

3. **"Single prompt not representative" for the sweep** — REMOVED. The single-prompt sweep is explicitly framed as a diagnostic to identify vulnerable configurations, and the paper then validates on the full 100-prompt dataset. This is a standard and valid experimental design.

4. **"5% threshold for dangerous" framing complaint** — REMOVED. The paper contextualizes this with additional analysis: "the most potent feature successfully compromised only 49 of the 100 prompts" and discusses poor cross-prompt generalization. The 5% threshold is reasonable for safety-relevant binary classification.

5. **Missing related works and formatting nitpicks** — REMOVED per rules (cannot verify external references; parser artifacts are not author errors).

6. **Reproducibility complaints about undisclosed details** — REMOVED. The paper provides model versions, steering procedures, evaluation prompts, hyperparameters, fixed random seeds, and will release code upon acceptance.

## Novel Insights

The harsh critic correctly noted that the missing variance reporting is the paper's most consequential weakness—and that it is fixable with data the authors already have. An interesting tension emerged between the Strength Finder's praise of the "4×" universal attack claim and the Harsh Critic's disaggregation: the claim is technically true as an average but misleadingly uniform. The paper's most genuinely novel observation—that even *random* directions with no adversarial optimization systematically break safety—is well-supported across models and is the strongest evidence underpinning the paper's thesis.

## Suggestions

1. **Add error bars or confidence intervals to all averaged compliance rate plots.** This is the single highest-leverage improvement. The data is already collected; reporting variance would transform the paper from one with a significant evidentiary gap to a methodologically sound one.

2. **Replace the "4×" headline** in the abstract and conclusion with a more nuanced characterization (e.g., "yielding an average 4× increase, though effectiveness varies dramatically across models—from negligible improvement on some to ~13× on others").

3. **Test the universal attack construction** with at least 2–3 different seed prompts (e.g., fraud, violence) to establish robustness.

4. **Explicitly verify the 0% no-steering baseline** on the full 100-prompt dataset; this is a quick sanity check.

5. **Expand SAE experiments** to at least one additional SAE source (e.g., Gemma Scope) or explicitly temper the scope of the claims about SAE dangers.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Human Score | Round | Comparison to This Paper |
|------|----------------|-------|------------------------|
| Measuring Effects of Steered Representation (z1yI8uoVU3) | 3.00 | R1 | Weaker — limited model sizes, narrower scope, less novel finding |
| Understanding Jailbreak Success (HuNoNfiQqH) | 4.75 | R1 | Weaker — only 4 models (some poorly aligned), less comprehensive evaluation |
| Steering Language Models with Activation Engineering (2XBPdPIcFK) | 5.00 | R2 | Weaker — outdated models, inconsistent baselines, proposes a method rather than identifying a vulnerability |
| GUARD Testing Method (lOTfiKt4Gc) | 5.00 | R3 | Different topic but comparable rigor; our paper has more comprehensive evaluation |
| Derail Yourself Multi-turn Attack (kvvvUPDAPt) | 5.33 | R3 | Different topic; our paper has broader scope and more novel findings |
| You Know What I'm Saying (yVVzaRE8Pi) | 5.50 | R3 | Comparable quality; our paper's finding is more fundamental |
| Effectively Steer LLM (ZPkNrs6aNO) | 5.50 | R2 | Comparable; our paper has more extensive evaluation across models |
| DAG-Jailbreak (xQIJ5fjc7q) | 5.50 | R2 | Comparable; our paper's contribution is more novel conceptually |
| How Jailbreak Defenses Work (RdGvvqjkC1) | 5.75 | R2 | Comparable methodology; our paper has broader model coverage, similar limitations |
| Simple Adaptive Attacks (hXA8wqRdyV) | 6.14 | R2 | Stronger — more comprehensive model coverage including API-based models, better variance reporting |
| JailbreakEdit Backdoor Injection (aSy2nYwiZ2) | 6.67 | R2 | Stronger — novel method, thorough evaluation, but requires white-box access |

**Round 1 bracket:** (4.5, 6.5) — clearly above the 3.00 activation steering evaluation paper and 4.75 jailbreak dynamics paper, but below the 6.14–6.67 strong accept papers.

**Round 2 narrowing:** Compared against anchors at 5.00, 5.33, 5.50, 5.75, 6.14, 6.67. The paper sits in the 5.5 range: its core finding is genuinely novel and the evaluation is systematic, but the missing variance reporting is a clear methodological gap that prevents it from reaching the 6+ level of the Simple Adaptive Attacks paper.

**Final score:** 5.5 — the paper identifies a real and important vulnerability with a novel finding, and the systematic evaluation across 8 models is commendable. However, the absence of uncertainty reporting is a significant methodological gap for a quantitative empirical paper, and the selective "4×" framing needs correction. These issues are fixable, and with them addressed the paper would be a strong contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>