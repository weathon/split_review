Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes an autotuning framework for time series transformers that combines Low-Rank Adaptation (LoRA) with Limited Discrepancy Search (LDS) to efficiently fine-tune pre-trained Chronos T5 models to target domains. The approach is evaluated on 10 out-of-domain datasets from the Monash repository, showing that a small fine-tuned model (Chronos Mini, 20M parameters) can outperform both full fine-tuning on out-of-domain datasets and zero-shot inference from much larger models (up to 710M parameters), achieving an average MASE improvement of 5.21% over the zero-shot baseline.

## Strengths

- **Autotuned LoRA outperforms full fine-tuning on out-of-domain datasets**: Table 3 shows that on datasets not seen during pre-training (e.g., Exchange Rate, M5), the autotuned LoRA model achieves lower MASE (0.867 and 1.969) than full fine-tuning (1.073 and 2.174). This directly supports the claim that parameter-efficient fine-tuning with structured HPO can beat full parameter updates on genuinely novel target domains. The paper provides a plausible explanation: for domains seen during pre-training (traffic, weather, electricity), full fine-tuning wins narrowly; for truly novel domains, LoRA wins.

- **A small fine-tuned model surpasses much larger zero-shot models**: Table 4 demonstrates that the autotuned Chronos Mini (20M) beats zero-shot Chronos Large (710M) on Traffic (0.634 vs. 0.644), Weather (0.770 vs. 0.786), ERCOT Load (0.777 vs. 0.985), and Australian Electricity (0.816 vs. 1.043). This is a practically meaningful result — it shows that targeted fine-tuning of a small model can match or exceed the capability of models 35× larger, with substantial savings in inference cost.

- **Practical search budget**: The algorithm achieves consistent improvements across 10 datasets using only 10 trials per dataset, demonstrating that useful LoRA configurations can be found under realistic resource constraints.

- **Broad evaluation across diverse domains**: Experiments span energy, transport, retail, web, weather, and finance datasets from the Monash repository, all explicitly held out from Chronos pre-training, strengthening the generalizability claims.

## Weaknesses

### Fatal
None.

### Major

1. **The LDS-based search procedure is not adequately described, compromising reproducibility.**  
   Line 38–39 states "Algorithm 1 outlines the steps involved in our autotune approach" but the description cuts off mid-sentence (after "We use Limited Discrepancy Search or") with no pseudocode or algorithmic specification provided in the extracted text. Even reading the prose that is present, the paper never specifies: (a) what the *initial configuration* is from which discrepancies are measured, (b) how hyperparameters are ordered (which matters for LDS), (c) how the search space is enumerated or sampled across the 10 trials, or (d) how "discrepancy" is defined concretely for each hyperparameter (e.g., is rank=2→4 one discrepancy? what about a categorical change in target modules?). LDS is a known algorithm, but its application to this specific search space requires these details to be specified. Without them, the core algorithmic contribution is opaque and the experiments cannot be reproduced.

2. **No comparison against standard HPO baselines, undermining the LDS-specific claims.**  
   The paper motivates LDS as a way to "minimize computational overhead" compared to exhaustive search, but never compares it against basic hyperparameter optimization methods such as random search, Bayesian optimization, or simple grid search with the *same budget of 10 trials*. The novelty claim (contribution 2: "adoption of LDS for exploring the LoRA hyper-parameter search space") is unsubstantiated without evidence that LDS performs better than or comparably to these alternatives under an equal trial budget. Random search with 10 trials would take the same wall-clock time and serve as the natural minimal baseline. Absent this comparison, the reader has no basis to believe LDS contributed anything beyond the fact that HPO with 10 trials works — which is known from existing work.

3. **Critical training hyperparameters are missing, preventing reproducibility of both LoRA and full fine-tuning experiments.**  
   The paper does not report the number of training epochs, learning rate, learning rate schedule, optimizer, or batch size for either the LoRA fine-tuning trials or the full fine-tuning baseline. The full fine-tuning section simply states it was performed on "the Chronos mini model described in Ansari et al. (2024)" — this describes the *model architecture*, not the fine-tuning procedure. Without these details, the comparison between autotune and full fine-tuning is uninterpretable: full fine-tuning may simply have been undertuned. These are not trivial implementation details; they are essential for any meaningful empirical comparison.

### Minor

4. **Inconsistency in the reported number of hyperparameters.**  
   Line 117 states "the number of LoRA hyper-parameters to be tuned which in our case is equal to 8." However, Table 2 (to the extent it can be read from the extracted text) lists four hyperparameters: rank, alpha, dropout, and target modules. Whether target modules are treated as a single categorical variable or as multiple binary choices is not explained, but neither interpretation straightforwardly yields 8. This inconsistency erodes confidence in the precise definition of the search space.

5. **No error bars, standard deviations, or confidence intervals are reported.**  
   All MASE scores are reported as point estimates averaged over 5 runs (as stated in the Implementation Details). Many observed differences are small (e.g., on several datasets where autotune and full fine-tuning are close). Without uncertainty quantification, the reader cannot assess whether the improvements are robust or merely reflect random variation, especially given the stochastic sampling used to produce point forecasts (median of 20 samples). This weakens the paper's central quantitative claims.

6. **Overclaimed "distributed" execution.**  
   Contribution 1 claims "Distributed autotuning of LoRA configurations," and line 35 mentions a "distributed ray based framework." However, all experiments were run on a single MacBook Pro M3 Max with 64GB RAM, and no evidence of distributed execution across multiple workers is provided. Ray Tune can support distribution, but the paper provides no data about actual parallelization. This claim should be scaled back to what was actually demonstrated.

### Trivial
- Table 2 caption contains a typo: "LoRa Hyper-paramater Search Space" (paramater → parameter).
- The prose describes "mean absolute squared error (MASE)" but MASE stands for *Mean Absolute Scaled Error*, not squared error. The metric usage appears correct from context, but the expansion is wrong.

## Nice-to-Haves

- A wall-clock time comparison between autotune (10 LoRA trials), full fine-tuning, and zero-shot inference would strengthen the computational efficiency claims. Even approximate runtime figures would be informative.
- Evaluating on at least one additional Chronos model size (e.g., Small, 46M) would support the claim that the approach generalizes beyond the Mini model.
- An analysis of how autotune performance varies with the number of trials (e.g., does LDS converge faster than alternatives?) would strengthen the efficiency argument.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The full fine-tuning baseline was performed as described in Ansari et al. (2024)"** — The reviewer attributed this phrasing to the paper. In fact, the paper says "We also perform full fine-tuning of the Chronos mini model described in Ansari et al. (2024)" — it is the *model*, not the fine-tuning procedure, that is described in the cited work. The underlying concern (missing training details) is kept in Weaknesses (Major #3), but the specific misattributed phrasing is removed.
- **"The paper uses only the Chronos T5 Mini model for its main experiments... this limits the generalizability"** — Raised as an "Other Observation." This is a legitimate scope constraint that the paper acknowledges (line 111: "in order to utilize minimal computational resources for demonstrating the applicability of our approach"). It does not invalidate any claim, and adding more model sizes would constitute a broader paper, not a stronger version of this one. Moved from weaknesses.
- **"Figures 3–6 are described but not visible"** — This is a parser artifact, not an author error. Removed.
- **"The underlying numbers for Figure 4 should be provided in a table"** — The main quantitative results are already presented in Tables 3 and 4. The figure is a visualization. This is a presentation preference, not a weakness.

## Novel Insights

The most interesting finding from the review process is the *asymmetry* in where the autotuned LoRA model wins vs. where full fine-tuning wins. The paper itself notes that on domains the pre-trained model has seen (traffic, weather, electricity), full fine-tuning wins by a slight margin, while on truly novel domains (Exchange Rate, M5), autotuned LoRA wins decisively (20.59% improvement on Exchange Rate). This suggests that LoRA's regularization effect — freezing most weights while adapting only low-rank subspaces — may be *beneficial* when the target distribution shifts away from pre-training data, because it prevents catastrophic forgetting of general representations while still adapting to local patterns. This is a non-obvious insight worth exploring further: the right fine-tuning strategy may depend on the *distance* between pre-training and target distributions, with parameter-efficient methods having an advantage on far-domain transfer.

## Suggestions

1. **Provide a complete, precise description of the LDS-based search procedure**: specify (a) the initial configuration used, (b) the ordering of hyperparameters in the LDS tree, (c) how discrepancy is counted for each hyperparameter type (continuous vs. categorical), (d) how the 10 trials are selected across discrepancy levels. Include pseudocode or a clear algorithmic sketch.

2. **Add random search (same 10-trial budget) as a baseline**. This single addition would either validate the LDS contribution or honestly reveal its limitations. If LDS performs comparably to random search, the paper should reframe its contribution around the overall LoRA+HPO pipeline rather than LDS specifically.

3. **Report all training hyperparameters** (epochs, learning rate, optimizer, batch size, learning rate schedule) for both LoRA and full fine-tuning experiments. State the context length and prediction horizon for each dataset explicitly rather than citing prior work.

4. **Resolve the hyperparameter count inconsistency**: clarify whether the 8 hyperparameters come from treating individual target modules (query, key, value, output, feedforward?) as separate binary choices, and correct Table 2 or the text accordingly.

5. **Add error bars** (e.g., standard deviation over the 5 runs) to all reported MASE scores in Tables 3 and 4.

6. **Remove or substantiate the "distributed" claim** — given that experiments were performed on a single laptop, rephrase to "parallelized" (since Ray Tune can parallelize trials on a single machine) or provide evidence of multi-worker distribution.

## Score and Decision

**Originality**: The application of LoRA + LDS to time series transformer fine-tuning is novel in its specific combination, though both components are individually well-established. The empirical finding that a small fine-tuned model can beat much larger zero-shot models is practically interesting.

**Importance**: Efficient adaptation of pre-trained time series models is a timely and practically relevant problem as foundation models for time series emerge.

**Claims support**: The core empirical claims (LoRA+autotune beats full fine-tuning on out-of-domain data; small fine-tuned model beats larger zero-shot models) are supported by the data presented. However, the specific claim that LDS provides benefits over simpler HPO methods is unsupported.

**Soundness**: The experimental methodology has significant gaps — missing HPO baselines, no uncertainty quantification, missing training hyperparameters. These substantially weaken the paper's soundness.

**Clarity**: The algorithm description is incomplete, the hyperparameter count is inconsistent, and key experimental details are absent. Clarity needs major improvement.

**Value**: The paper demonstrates a practically useful result (small fine-tuned model beating much larger zero-shot models) that would be of interest to practitioners. However, the presentation and experimental rigor gaps prevent the paper from making a reliable contribution in its current form.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>