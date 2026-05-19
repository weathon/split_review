- Decision: Reject
- Avg Score: 2.33
- Scores: 3, 1, 3
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

The paper presents Paramanu-Ganita, a 208M-parameter decoder-only transformer pretrained from scratch on 31.5B tokens of curated mathematical text and code with a domain-specialized 17K-vocabulary BPE tokenizer, then chain-of-thought instruction fine-tuned on MetaMathQA. It achieves 39.4% on GSM8K, outperforming the math-specialized LLEMMA 7B (36.4%) and various base 7B models, using only 170 A100 GPU hours (135× less than LLEMMA 7B). The paper aims to show that small, domain-specific models pretrained from scratch can be a cost-effective alternative to continual pretraining of much larger LLMs for mathematical reasoning.

---

## Strengths

1. **Dramatic cost reduction with competitive performance against key baselines.** The paper provides concrete evidence (Section 7.1 and abstract) that Paramanu-Ganita required only 170 A100 hours versus 23,000 A100 hours for LLEMMA 7B—a 135× reduction. Despite this, it outperforms LLEMMA 7B on GSM8K (39.4% vs. 36.4%) and several other benchmarks, and outperforms base (non-instruction-tuned) 7B models (LLaMA-2, Falcon, PaLM) by large margins. This is a quantifiable and meaningful efficiency gain.

2. **Comprehensive multi-benchmark evaluation.** The model is evaluated across diverse difficulty levels: GSM8K (grade school), MATH (competition), MMLU-math (high school/college), AGIEVAL-AQuA-RAT (GRE/GMAT), AGIEVAL-SAT-Math, and LogiQA (logical reasoning). This breadth provides evidence that the model's capability extends beyond a single benchmark.

3. **Sound technical methodology.** The paper uses μ-transfer for hyperparameter tuning from a 15M proxy model (Section 7.1), a domain-specialized tokenizer (Section 5), and curriculum-informed data curation mixing AutoMathText, MathPile, AlgebraStack, and CoT-templatised Q&A (Section 4). These design choices are well-motivated and reflect genuine engineering rigor.

---

## Weaknesses

### Fatal
None.

### Major

1. **Selective reporting of comparisons misrepresents the model's standing against instruction-tuned math models.** The paper includes WizardMath 7B (54.9% GSM8K) and MetaMath 7B (66.4% GSM8K) in Table 2, but the results text (Sections 9, 10) never discusses them—it only highlights comparisons Paramanu-Ganita wins. The abstract claims the model "outperforms... math-specialised LLMs by 3–23% points," which is true for LLEMMA and Minerva but false for WizardMath and MetaMath (which outperform Paramanu-Ganita by 15–27 points). The data is in the table but the framing is misleading. This is not a fatal flaw (the data is transparently presented), but it is a significant presentation issue that undermines reader trust.

   *Quoted evidence*: Results section (lines 169–178) lists only outperformed models and omits any discussion of WizardMath or MetaMath, despite both appearing in Table 2's caption (line 150) and the table itself.

2. **No standardized evaluation protocol across comparisons.** The paper uses zero-shot greedy decoding (via lm-eval-harness) for Table 3 benchmarks (line 154). For GSM8K/MATH (Table 2), it uses a custom prompt (Section 8.1). Baseline scores are "quoted from respective author papers" (line 150), which may use different shot counts, prompting strategies, and answer extraction methods. This makes the reported performance gaps uncalibrated—it is unclear how much of the claimed improvement is due to the model vs. evaluation asymmetry. A fair comparison would evaluate all models under identical conditions.

### Minor

3. **The absolute MATH score for Paramanu-Ganita is not explicitly stated.** The paper reports only percentage-point differences against baselines (e.g., "outperformed LLaMa-1 7B by 7.44% on MATH"). The reader must infer the absolute score (~10.3%) by adding the difference to known baseline scores. This is a basic reporting omission that harms clarity.

4. **No comparison against similarly-sized models after instruction tuning.** The paper's most relevant question is whether domain-specific pretraining *from scratch* beats generic pretraining at similar model scale. The only size-matched baseline is OLMo 1B (evaluated as a base model in Table 3). No comparison is made against TinyLlama 1.1B, Pythia 410M, or OLMo 1B after instruction tuning on the same MetaMathQA data. Such a comparison would isolate the value of domain-specific pretraining from scratch vs. continued training of a generic model.

5. **No confidence intervals or variance reported.** For small test sets (e.g., AGIEVAL-AQuA-RAT has 254 questions, AGIEVAL-SAT-Math has 220), a few correct answers shift percentages by 1–2%. Without error bars, it is unclear whether small reported margins (e.g., 1–2% advantages) are statistically significant.

### Trivial
- The data mixture ratios from the various pretraining sources are not reported (Section 4 mentions sources but not proportions). This would help reproducibility.
- The tokenizer ablation (specialized vs. generic BPE) is not performed, so the claimed benefit of the custom tokenizer is untested.

---

## Nice-to-Haves
- An ablation comparing the specialized tokenizer against a generic BPE of similar vocabulary size would justify the tokenizer design effort.
- Reporting the model's perplexity on a held-out *general* text corpus would contextualize the reported perplexity of 4.349 on the domain-specific test set.
- A data contamination analysis for the MetaMathQA→GSM8K/MATH pipeline (verifying that the training and test splits are disjoint) would address a natural concern even though this is standard practice.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Data contamination concern (Harsh Critic):** "MetaMathQA is derived from GSM8K and MATH... This is circular and likely inflates results." — **Removed** because this misunderstands the setup. MetaMathQA is bootstrapped from the **training** splits of GSM8K and MATH; evaluating on the **test** splits is standard supervised fine-tuning practice, not contamination. The paper does not claim otherwise.

2. **Evaluation asymmetry "systematically favors the proposed model" (Harsh Critic):** The critic asserts that zero-shot (used by the proposed model) vs. few-shot (used by some baselines) favors the proposed model. For the GSM8K/MATH evaluation, the paper uses a specific prompt (Section 8.1) and it is unclear whether this is zero-shot or few-shot CoT. The direction of any bias is not clearly established and this claim overreaches without evidence from the paper.

3. **"Mislocation of the contribution" framing (Harsh Critic):** The critic claims the paper conflates two research questions and provides no evidence for (b). This is a framing critique about scope rather than a verifiable error. The paper's RQs (Section 1) explicitly ask about performance vs. LLMs *and* cost efficiency—both are addressed, even if imperfectly. The critique is more of a suggestion than a weakness.

4. **Strength Finder strengths about specific outperformance claims:** Some strengths from the Strength Finder about "outperforming all compared LLMs" are too broad given the WizardMath/MetaMath omission in the text. These have been subsumed into the qualified strength above.

5. **Various reviewer nitpicks about missing appendix content, formatting, and reproducibility details** — Removed per hard rules (parser artifacts, removed sections).

---

## Novel Insights

The harsh critic usefully identifies that the paper conflates two distinct research questions: (a) whether a small domain-specific model can be useful (yes, and the paper demonstrates this), and (b) whether domain-specific pretraining *from scratch* is better than generic pretraining at the same scale (the paper provides no evidence for this, as it lacks instruction-tuned similarly-sized baselines). This is a genuine structural gap that future work in this vein should address. Additionally, the observation that the paper's central claim of outperforming "math-specialised LLMs" is technically true for LLEMMA and Minerva but misleading when WizardMath and MetaMath are considered is a useful check on the paper's framing that the authors should address.

---

## Suggestions
1. **Fix the selective reporting.** In the results section, acknowledge WizardMath and MetaMath explicitly: "Our model achieves 39.4% on GSM8K, which is competitive with LLEMMA 7B (36.4%) and well above base 7B models (11–16%), though below instruction-tuned math models such as WizardMath (54.9%) and MetaMath (66.4%)." This honest framing preserves the contribution while being transparent.
2. **Add instruction-tuned baselines at similar scale.** Fine-tune OLMo 1B or Pythia 410M on MetaMathQA (or a comparable dataset) and compare. This would directly test whether domain-specific pretraining from scratch provides additive value over generic pretraining.
3. **Standardize the evaluation.** Either re-evaluate baseline models using the same lm-eval-harness configuration, or clearly document the evaluation protocol used for each baseline and discuss any systematic differences.
4. **Report the absolute MATH score** explicitly in the text or table, not just as percentage-point differences.
5. **Ablate the tokenizer** by replacing it with a generic BPE of similar vocabulary size and comparing downstream performance.

---
