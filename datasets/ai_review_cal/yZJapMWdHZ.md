- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6
Here is my final consolidated review.

## Summary
This paper identifies a blind spot in LLM uncertainty estimation: tokens and sentences are treated equally even though they carry vastly different semantic weight. The authors propose SAR (Shifting Attention to Relevance), a two-level reweighting scheme that up-weights semantically relevant tokens and sentences when computing predictive entropy. Experiments across 5 LLM families (OPT, LLaMA, Vicuna, WizardLM, LLaMA-2-chat) and 5 QA datasets show consistent AUROC improvements over Predictive Entropy, Length-normalized PE, Lexical Similarity, and Semantic Entropy.

---

## Strengths

- **Well-motivated by quantitative evidence of generative inequalities.** Figures 2–3 in Section 3.4 demonstrate that irrelevant tokens dominate uncertainty volume despite low semantic relevance, and that irrelevant sentences commit more uncertainty than relevant ones. This directly motivates the proposed correction rather than relying on intuition alone.

- **Consistent AUROC gains across diverse LLMs and datasets.** Table 1 shows SAR outperforms Semantic Entropy by up to 3.6% AUROC (CoQA, OPT-30b); Table 2 shows SAR beats SE by 7.1% AUROC on average across instruction-tuned LLMs on TriviaQA, SciQ, and CoQA. The trend holds across pretrained (OPT, LLaMA) and instruction-tuned (Vicuna, LLaMA-2-chat, WizardLM) families.

- **Token-level and sentence-level components are independently validated and synergistic.** Section 4.3 and Table 1 show that TOKENSAR and SENTSAR each improve over baselines individually, and their combination (SAR) yields further gains (e.g., 0.748 vs. 0.723 each on OPT-30b/CoQA), supporting the claim that joint attention-shifting is effective and the two components are complementary.

- **Generation-efficiency demonstrated.** Figure 4 shows SAR achieves 0.750 AUROC with only 5 generations and continues improving with more, while baselines plateau or degrade — a practically useful property.

- **Validation extends to medical QA.** Table 3 reports SAR outperforming baselines on MedQA and MedMCQA, extending applicability to high-stakes scientific domains.

- **Sensitivity analysis of sentence similarity encoders.** Table 4 systematically compares third-party sentence encoders against the target LLM's own embeddings, showing general-purpose models are more effective — providing concrete deployment guidance.

---

## Weaknesses

### Fatal
None. The core methodological claims are supported by evidence and no fundamental flaw is present.

### Major

- **Temperature hyperparameter \(t=0.001\) is used without ablation or justification.** Equation (9) introduces a temperature \(t\) that scales the relevance term before adding it to the generative probability. The paper sets \(t=0.001\) (Section 5.1) with no sensitivity analysis. Because the generative probability \(p(s_j|x)\) is an exponential product over tokens and typically extremely small, a \(t\) this small could cause the relevance term to dominate, potentially rendering the generative probability nearly irrelevant. Without an ablation across a range of \(t\) values (e.g., \(\{10^{-4}, 10^{-3}, 10^{-2}, 0.1, 0.5, 1.0\}\)), it is unclear whether the reported gains are robust or depend on this specific setting. This is the most significant evidential gap in the paper.  
  *Evidence*: Lines 176–179 define \(t\); line 239 sets \(t=0.001\) with no further discussion or sensitivity study.

- **No error bars, confidence intervals, or replication statistics are reported.** All tables present single AUROC values. Given that several improvements over Semantic Entropy are small (e.g., OPT-6.7b/TriviaQA: 0.694 vs. 0.691, a gain of 0.003), it is impossible to assess statistical reliability. While single-run reporting is common in this area, the paper's core claim of "superior performance" would be substantially strengthened by variance estimates (e.g., 3–5 runs with different sampling seeds).  
  *Evidence*: Tables 1–4 report only point estimates; no standard deviation, confidence interval, or replication information appears anywhere in the paper.

### Minor

- **Token-level relevance computation cost is acknowledged but not quantified.** The paper's limitations statement (line 285) notes "additional latency," but does not discuss that computing Eq. (2) for a sentence of length \(N\) requires \(N\) forward passes through a Cross-Encoder RoBERTa-large model (one per removed token). No runtime, latency, or practical approximation is reported, making it difficult to assess deployability.  
  *Evidence*: Eq. (2) in lines 77–81 defines the token relevance computation; the only cost discussion is the short sentence in line 285.

- **Motivational analysis in Section 3.4 uses only one model (OPT-13b) and one dataset (CoQA).** While sufficient as motivation, the claim that generative inequalities are a general phenomenon would be strengthened by showing the pattern holds for at least one other model-dataset combination (e.g., an instruction-tuned model).  
  *Evidence*: Line 122: "We utilize CoQA as the dataset and OPT-13b as the model to be examined."

- **Manual entailment failure analysis is based on only 120 questions.** The claim that 36.7% of Semantic Entropy's entailment predictions are "undesirable for long generations" is used to motivate the sentence-level design, but rests on a small sample.  
  *Evidence*: Line 185: "120 questions in total."

- **Lexical Similarity baseline is minimally described.** The paper states it "considers the similarities among multiple generations" (line 218) but provides no details on how the similarity metric is computed or thresholded, making the comparison less reproducible.

- **The "LLM's own embedding" row in Table 4 is not described in text.** The paper states general-purpose models outperform "target LLMs" (line 270) but does not specify how the LLM's own embedding is extracted or used as a similarity measurement.

- **Combined token+sentence transformation in Eq. (10) receives little justification.** The paper converts TOKENSAR back to a "probability" via \(p'(s|x) = e^{-\mathrm{TOKENSAR}(s,x)}\) without explaining why this exponential transformation is natural or well-calibrated for use in the sentence-level formula.

### Trivial
- Different numbers of generations for pretrained (\(K=10\)) vs. instruction-tuned (\(K=5\)) models are used without comment on cross-comparison fairness. The paper states this explicitly (line 239), but it slightly muddies aggregate comparisons.

---

## Nice-to-Haves
- **Temperature ablation** (listed as Major, but if added, would substantially strengthen the paper).
- **Error bars / standard deviations** (listed as Major, but similarly high-impact).
- **Comparison with SelfCheckGPT or QA-consistency methods.** The paper cites Manakul et al. (2023) in related work but does not include these approaches as baselines. Adding one such comparison would broaden the competitive landscape.
- **Expanded limitations section** that explicitly discusses the \(N\)-pass computational cost of token-level relevance and possible approximations (e.g., scoring only high-variance tokens).
- **Release of code and prompts** for reproducibility, especially given the non-trivial token-removal preprocessing.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Missing code/prompt release" (Harsh Critic, Missing Parts).** Removed because reproducibility nitpicks about code release are explicitly excluded by the hard rules ("REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details, or large artifacts impractical to include").
2. **"Should expand the generative inequality analysis to instruction-tuned models" (Harsh Critic, Section-by-Section).** Not removed — kept as Minor.
3. **"SelfCheckGPT comparison missing" (Harsh Critic, Missing Parts).** Moved to Nice-to-Haves; the paper does cite Manakul et al. in related work, and requesting an additional baseline is a suggestion, not a weakness.
4. **"Equation (6) L1 vs. softmax normalization" (Harsh Critic, Section-by-Section).** The paper provides a clear two-part justification (lines 171–172: comparability across sentences and mitigating length bias). The critic's question is reasonable but the paper already addresses it.
5. **Strength Finder strength #1 ("Empirical demonstration of generative inequalities")** — kept in Strengths.
6. **Strength Finder strength #4 ("Generation-efficient")** — kept in Strengths.
7. **"Combination transformation is ad-hoc" (Harsh Critic, Section-by-Section).** Removed from weaknesses; the paper explicitly explains the transformation (line 192–193: replacing generative probabilities with exponentiated TOKENSAR values to combine both levels). The approach is principled even if brief. The concern is addressed as Minor above.

---

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an unexpected reinterpretation or cross-observation that the paper itself does not already articulate.

---

## Suggestions
1. **Add a temperature ablation** for \(t\) over at least \(\{10^{-4}, 10^{-3}, 10^{-2}, 0.1, 0.5, 1.0\}\) on one model-dataset pair (e.g., OPT-13b / CoQA) and report AUROC. This would either confirm robustness or reveal sensitivity, in which case a principled selection (e.g., cross-validation) should be adopted.
2. **Report standard deviations** by running the full pipeline 3–5 times with different random seeds for the multinomial sampling step. Given that some margins are as small as 0.003 AUROC, variance estimates are essential for interpreting the reported gains.
3. **Quantify the computational cost of token-level relevance** — report time-per-question on a representative setting and discuss possible approximations (e.g., scoring only tokens with high probability variance, using a cheaper similarity model).
4. **Expand the limitations section** to explicitly mention the \(N\)-forward-pass cost, the sensitivity of \(t\), and the fact that the method requires access to token logits (which may not be available from API-only models).
5. **Provide a one-sentence description** of how Lexical Similarity is computed and clarify how the "LLM's own embedding" similarity is derived in Table 4.

---
