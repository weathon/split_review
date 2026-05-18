Now I have all the information needed to verify each claim against the paper. Let me produce the consolidated review.

## Summary

This paper introduces SysCaps (system captions) — text descriptions of simulation system attributes — as language interfaces for multimodal surrogate models of complex energy systems (buildings and wind farms). The authors propose a pipeline that uses LLMs to generate synthetic natural-language captions from simulation metadata, then feeds them through a lightweight BERT-based text encoder concatenated with timeseries inputs into a bidirectional sequence encoder (LSTM or SSM). Experiments on building (EnergyPlus) and wind farm (FLORIS) simulators show that SysCaps-augmented surrogates outperform one-hot encoding baselines in held-out accuracy, exhibit robustness to attribute synonyms, and benefit from prompt augmentation (multiple paraphrased captions) in small-data settings.

## Strengths

1. **SysCaps encoding substantially improves surrogate accuracy over standard one-hot and tree-based baselines.** The SSM with key-value SysCaps achieves lower NRMSE than one-hot SSM and tuned LightGBM on held-out building stock systems (Table 2, lines 217–226), demonstrating that language-based attribute encoding is an effective alternative to traditional feature engineering for this task.

2. **LLM-generated synthetic captions preserve sufficient attribute information for downstream regression while providing language flexibility.** The paper introduces a systematic pipeline (Figure 1) and a classifier-based quality metric showing ~9–12% attribute omission/error rate across caption lengths (Table 1, line 198), and the resulting natural-language SysCaps models still outperform one-hot baselines (Table 2), enabling language interfaces without expensive human annotation (lines 123–126).

3. **Language interfaces unlock generalization capabilities not possible with traditional encodings, such as robustness to attribute synonyms.** For 11/14 building-type synonyms, the NRMSE increase is less than 13%, while baselines (attribute removal, random attribute) cause 54% and 90% average increases respectively (Table 4, line 241). This demonstrates that text embeddings capture semantic similarity — a key advantage over one-hot or label encodings.

4. **Prompt augmentation with multiple caption styles regularizes small-data surrogate training.** For the wind farm dataset (only 300 training systems), using four different prompt styles reduces NRMSE from 7.23 (one-hot) to 4.57 (augmented SysCaps-nl), while one-hot models severely overfit (Table 5, lines 276–279).

5. **The architecture is computationally efficient.** LLMs are used only for offline caption generation; at inference time the surrogate uses a lightweight BERT/DistilBERT text encoder and an SSM/LSTM sequence encoder, keeping computational costs low (lines 125, 157–158).

## Weaknesses

### Fatal
None.

### Major

1. **The "accessibility" claim is not directly evaluated.** The paper motivates language interfaces by arguing they make surrogates "more accessible for both experts and non-experts" (lines 5–6, 115) and concludes that language is a "viable interface" (line 289). Yet all experiments evaluate model accuracy metrics (NRMSE), not human interaction. There is no user study, no human evaluation of ease-of-use, and no measure of "accessibility" or "intuitiveness." The design space exploration demonstration (Section 6.4) uses a fixed template caption rather than free-form natural language interaction. The paper itself acknowledges that human studies are future work (line 304), but the current framing oversells the accessibility claim relative to what is actually measured. **Impact:** The core technical contribution (text encodings improve surrogate accuracy) remains valid, but the paper should either (a) reframe the contribution around text encodings of system attributes and drop the unsupported accessibility motivation, or (b) include at least a minimal human evaluation.

2. **Natural-language captions do not outperform simpler key-value templates in the main accuracy comparison.** In Table 2 (line 220), key-value templates (SysCaps-kv) yield better accuracy than LLM-generated natural-language captions (SysCaps-nl) for both LSTM and SSM models. The paper attributes this to caption quality (line 224), but this gap undermines the special role claimed for *natural language*. The benefit appears to come from using pretrained text embeddings (BERT) to encode system attributes, not from the linguistic properties of natural language. The synonym robustness (Section 6.3) is a consequence of BERT's contextual embeddings, which would also apply to key-value templates with varied attribute names. **Impact:** The paper's defining feature (natural language) does not provide a measured advantage over structured text. The contribution effectively reduces to "pretrained text embeddings of system attributes improve surrogate accuracy," which is a valid but narrower result than advertised.

### Minor

1. **The paper does not compare against learned tabular embeddings.** The only non-text baseline is one-hot encoding (plus LightGBM). A learned embedding layer per categorical attribute (trained from scratch on the surrogate task) would help isolate whether SysCaps' advantage comes from the textual representation itself or simply from having a distributed, learned embedding rather than a sparse one-hot vector. This gap weakens the paper's central quantitative claim.

2. **The caption quality evaluation lacks human validation.** Section 6.1 uses a multiclass classifier trained on the same type of LLM-generated data it evaluates. No human-annotated test set is used to validate the classifier, and the evaluation only checks for *presence* of attributes, not *hallucinated* attributes. The reported 9–12% error rate is a reasonable sanity check but is not rigorous enough to support quantitative claims about caption fidelity.

3. **No measures of uncertainty are reported.** Results are averaged across 3 random seeds (line 214) without standard deviations or confidence intervals. For several comparisons, the differences between models may not be statistically significant.

4. **The architecture novelty is modest.** The multimodal fusion approach — broadcasting a BERT embedding and concatenating with timeseries features, then feeding into a bidirectional sequence encoder — is a straightforward design. The paper's claim that this is "insightful for future multimodal text and timeseries studies" (line 41) is somewhat oversold.

### Trivial
None.

## Nice-to-Haves

- Add learned tabular embedding baselines (e.g., embedding layer per categorical attribute) to isolate whether the benefit comes from pretrained text embeddings or from distributed representations generally.
- Validate caption quality with a small set of human-annotated captions, and report both missing and hallucinated attributes.
- Include standard deviations or confidence intervals for the main accuracy results.
- Compare against alternative fusion strategies (e.g., cross-attention between text and timeseries) to justify the broadcast+concatenate design.
- Discuss mitigations for BERT tokenizer's numerical limitations (e.g., number-specific tokenizers), which the paper identifies as a limitation but does not address.

## Removed Points

- **"Wind farm experiment does not motivate why sequence model is inappropriate"** (Harsh Critic, Other Observations). Removed: The paper explicitly states "The simulation is run assuming steady-state conditions (i.e., time-independent), so we tune hyperparameters for and train the non-sequential ResNet models" (line 276). The motivation is clearly provided.
- **"Missing hyperparameters for text encoder fine-tuning"** (Harsh Critic, Missing Parts). Removed: The paper specifies the fine-tuning strategy (all BERT layers fine-tuned, only last DistilBERT layer fine-tuned, line 159). Specific optimizer/hyperparameter values are standard for BERT fine-tuning and fall under the reproducibility-nitpick removal rule.
- **Various formatting/style criticisms and missing-appendix complaints.** Removed per hard rules: the PDF parser strips these; they are not author errors.

## Novel Insights

The reviews collectively surface an important tension that the paper itself does not fully resolve: the gap between the *framing* (natural language interfaces make surrogates more accessible) and the *evidence* (structured key-value text embeddings actually work better than natural language). This suggests the paper's genuine contribution is about **text-encoded attribute representations for surrogate modeling** — a useful engineering finding — rather than about natural language interfaces per se. The most technically interesting result is the prompt augmentation finding (multiple paraphrased captions acting as a regularizer), which is underemphasized relative to the accessibility framing. The paper would be stronger if it leaned into this finding and repositioned the natural-language aspect as an enabler of automatic data augmentation rather than as an interface improvement.

## Suggestions

1. **Reframe the contribution.** Replace the "accessibility for non-experts" claim with a more precise framing: "text encodings of system attributes, whether key-value or natural language, improve surrogate accuracy over one-hot encodings and enable semantic generalization (synonym robustness)." This aligns the claims with what is actually measured.
2. **Add learned tabular embedding baselines** to distinguish whether the benefit comes from pretrained text embeddings or from distributed representations generally.
3. **Emphasize the prompt augmentation finding** (Section 6.5), which is the paper's most novel practical contribution — the ability to generate diverse training captions from an LLM as a regularizer in low-data regimes.
4. **Either add a minimal human evaluation** (e.g., comparing time/accuracy for non-experts describing systems in text vs. tabular form) or explicitly scope out the accessibility claim.

## Score and Decision

**Originality:** The application of text-encoded attributes to simulation surrogates is novel, though the architecture itself is straightforward. The prompt augmentation finding is the most original element.

**Importance:** The problem of making simulation surrogates more flexible is practically important for energy systems and related domains. The results are relevant.

**Claims support:** The core claim (SysCaps improve accuracy over one-hot) is well-supported. The accessibility claim is not supported. The NL advantage claim is contradicted by the evidence.

**Soundness:** Experiments are reasonable but missing important baselines (learned tabular embeddings) and uncertainty measures.

**Clarity:** The paper is well-written and clearly structured.

**Value:** Moderate. The paper demonstrates a useful technique (text-encoded attributes for surrogates) but oversells its implications.

The paper has a genuine technical contribution (text encodings improve surrogate accuracy, enable synonym robustness, and prompt augmentation regularizes small-data training). However, the framing mismatch between the accessibility motivation and the quantitative experiments is significant, and the natural-language component does not outperform simpler key-value templates. The missing baselines weaken the quantitative comparison. These issues are addressable with revisions but are substantial in their current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>