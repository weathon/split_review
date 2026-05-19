- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 3, 6
Now I have everything I need. Let me produce the final consolidated review.

## Summary

This paper proposes the **Babel Tower Hypothesis** to describe how LLMs acquire new language capabilities during pre-training: multiple languages initially share a single knowledge system dominated by a primary language, then gradually develop language-specific systems. Using code LLMs (GPT-2 1.3B starting Python-monolingual → PHP/C#/Go/C++), the authors validate this hypothesis through working language analysis and language-transferring neuron tracking. They then derive a method (Algorithm 1) to estimate an optimal pre-training data distribution by mapping system proportions to token counts via training loss as a proxy. Experiments on 1.3B and 6.7B models pre-trained from scratch show that adjusting the corpus for two languages (PHP, C#) yields modest average improvements over the original corpus, with results competitive to existing open models.

## Strengths

1. **Clear three-stage characterization of multilingual evolution.** The paper identifies and empirically delineates Translation, Transition, and Stabilization stages for new language acquisition, supported by performance curves (Figure 2) and two complementary internal-state probes (working language proportion in Figure 3 / `fig:worklang` and language-transferring neuron counts in Figure 4 / `fig:neron`). This provides a concrete, stage-wise model that prior work on static multilingual LLMs lacked.

2. **Practical method for optimizing pre-training data distribution grounded in the hypothesis.** Algorithm 1 translates the Babel Tower Hypothesis into a usable procedure that estimates optimal token counts per language using only training loss as a proxy for system proportion. The method is validated through large-scale experiments: Optimized-1.3B achieves HumanEval average 26.61 (best among ~1B-class models in Table 1) and Optimized-6.7B achieves 41.96, outperforming both the original corpus and several open baselines.

3. **Counter-intuitive finding that dominant-language reliance can outperform own-system building.** The paper demonstrates that for PHP and C#, peak performance occurs during the Translation stage (Figure 2), and increasing language-specific data eventually degrades performance (Figure 5a). This challenges the default assumption that more data is always better and provides quantitative evidence of the trade-off (proportion of correct answers requiring Python knowledge dropping from ~60% to near 0% in Figure 2).

4. **Convergent evidence from dual internal-state probes.** The paper uses both working language identification (logit lens) and language-transferring neuron counts. These capture different aspects of internal state (token-level generation vs. neuron-level activation) and show convergent trends (WL proportion shifts from Python to the new language while LT neurons for the new language decrease), strengthening the evidence beyond what either metric alone would provide.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated, though their strength is limited by the weaknesses below.

### Major

1. **The Babel Tower Hypothesis is directly validated only in an artificial continual-pre-training setting, not tracked in realistic multilingual pre-training.** The central claim is demonstrated exclusively in a scenario where a Python-monolingual model is continually pre-trained on a *single* new language at a time (Section 3.1). The from-scratch pre-training experiments (Section 4.3, Table 1) — the only scenario that resembles real multilingual pre-training — do **not** track working languages or language-transferring neurons at any point. Readers therefore have no direct evidence that the claimed system-transition dynamics (translation → transition → stabilization) occur when multiple languages are present from the start. The hypothesis's status as a general theory of multilingual LLM evolution is thus weakened.

2. **Key assumptions underlying the corpus construction method (Algorithm 1) are weakly validated.**  
   (a) **Eq. 1** assumes training loss is a linear proxy for Python system proportion: P(ℓ) ≈ (α−ℓ)/(α−β). The paper's only justification (lines 245–246) is that loss "exhibits trends akin to those of working language metrics" — i.e., visual similarity. No empirical calibration is provided (e.g., comparing loss-derived proportion to directly measured working language proportion at corresponding checkpoints).  
   (b) **Eq. 2** assumes the token proportion in the corpus equals the final system proportion: P̄(η_i) ≈ η_i/Σ_j η_j. This is validated using only four data points for a single language (PHP at 1B, 2B, 5B, 10B tokens; Figure 3 / `fig:phptoken`). The mapping from a continual-pre-training checkpoint's system proportion to a stable from-scratch pre-training configuration is asserted without independent verification.

3. **The from-scratch pre-training experiments lack sufficient rigor to establish the method's reliability.**  
   - Only **2 of 4** languages (PHP, C#) are optimized; Go and C++ are left unchanged, with the paper stating C++ "does not depend on the Python system" (line 309) without testing this claim by adjusting C++ data.  
   - Results show **inconsistent trade-offs**: Go performance drops substantially at 1.3B scale (HumanEval: 21.43 → 16.88, Table 1) with no discussion or analysis.  
   - **No error bars, confidence intervals, or multiple random seeds** are reported for any experiment, making it impossible to assess whether the observed differences (often a few percentage points) are statistically significant.  
   - The **data source** for the from-scratch pre-training corpus is not identified, and the exact composition of the "original corpus" prior to downsampling is underspecified, hindering reproducibility.

### Minor

1. **The Python-specific subset construction conflates Python-specific knowledge with general difficulty.** The paper defines problems requiring Python knowledge as those the Python monolingual LLM solves but PHP/C# monolingual LLMs fail (lines 94–96). A problem could be hard for PHP/C# models simply because those models have less data, not because it requires Python-specific semantics. This measure conflates actual knowledge transfer with model capability differences.

2. **Working language analysis relies on only 5 built-in function pairs per language** (line 119), with GPT-4o generating 10 completion problems per identifier. This is a very coarse sampling of the language space for drawing conclusions about internal system state.

3. **The LAPE threshold for identifying language-transferring neurons is not specified.** The paper states it "follow[s] Tang et al. 2024" (line 126) but does not report the actual threshold used, making the neuron-count results difficult to reproduce or interpret.

4. **The key validation experiment (Figure 3a / `fig:phptoken_pre`) shows a non-monotonic trend** (peak at 2B tokens, drop at 5B, rise at 10B) that raises questions about noise in the measurements. The paper does not comment on this.

5. **No calibration of loss-derived proportion against directly measured internal states.** The paper uses loss as a proxy for system proportion (Eq. 1) but never compares loss-derived proportions to the working language proportions measured in the same experiments, which would have provided an empirical grounding for the linear assumption.

6. **The paper overclaims on general significance.** The claim that findings "highlight potential limitations of previous multilingual LLMs" (line 350) and "provide guidance" for multilingual pre-training broadly is not matched by the evidence, which is limited to a code LLM setting with one dominant language (Python) and four target languages, only two of which are actually optimized in the final experiment.

### Trivial
None.

## Nice-to-Haves
- **Cost analysis of the method.** Algorithm 1 requires a continual-pre-training run per target language; the paper would benefit from discussing whether simpler heuristics (e.g., always setting new languages to a fixed token budget like 2B tokens) work comparably, reducing computational overhead.
- **Analysis of why C++ and Go differ** from PHP/C# in their reliance on the Python system (e.g., syntactic similarity, shared tokens, or data characteristics). Understanding these differences would strengthen the method's applicability.
- **Tracking internal states during from-scratch pre-training** would provide direct validation of the hypothesis in a realistic setting.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **"The pre-training hyperparameters (learning rate, schedule, warmup, architecture specifics) are missing."** Removed per policy against reproducibility nitpicks about standard hyperparameters that are not central to the paper's scientific claims.
- **"The original token counts for each language before downsampling are not provided."** Factually incorrect; the paper provides these in the data statistics table (Section 3.1, wrapped table): PHP 23B, Go 11B, C# 16B, C++ 28B, Python 11B.
- **"No statistical tests are provided for trends in Figures 3–4."** The paper is presenting visual trends from a controlled experiment, not testing a statistical hypothesis; requesting significance tests on trend visualization is generic and not standard practice for this type of analysis.
- **"Baselines (StarCoder, DeepSeekCoder, CodeLlama) are not controlled comparisons."** The paper's primary comparison is Original vs. Optimized (both controlled). The baselines are provided as reference points for the community, not as controlled comparisons; this is standard practice.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface any observation that the paper itself does not make or imply.

## Suggestions
1. **Track internal states (working language proportion, language-transferring neurons) during the from-scratch pre-training experiments** to provide direct evidence that the Babel Tower dynamics hold in realistic multilingual settings.
2. **Calibrate Eq. 1 empirically** by comparing loss-derived system proportions to directly measured working language proportions at corresponding checkpoints, or provide a more principled justification for the linear mapping.
3. **Report results with at least 2–3 random seeds** (or provide error bars from the sliding window) so readers can assess the significance of the observed improvements and trade-offs.
4. **Discuss the Go performance regression** (1.3B: 21.43 → 16.88) — why it occurs and whether the method can be refined to avoid harming languages that do not benefit from the dominant-language strategy.
5. **Identify the data source** for the from-scratch pre-training corpus and specify the exact steps used to construct the "original" and "optimized" corpora.
