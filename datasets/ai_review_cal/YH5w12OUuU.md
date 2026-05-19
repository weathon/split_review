- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

The paper proposes TEMPO, a framework that integrates STL time series decomposition (trend, seasonality, residual) with a semi-soft prompting strategy to adapt a pre-trained GPT model for zero-shot time series forecasting. The core idea is that explicitly decomposing the input into these three components and concatenating component-specific learned prompts enables better cross-domain transfer than feeding raw or patched time series into the LLM. The paper evaluates TEMPO on standard benchmark datasets (long-term zero-shot) and two multimodal datasets (short-term with textual context), reporting improvements over both LLM-based and transformer-based baselines.

## Strengths

- **Novel integration of decomposition + prompting for GPT-based time series**: TEMPO is the first to combine STL decomposition with semi-soft prompts that are specific to each component (trend, season, residual), using a hard-prompt template to initialize learnable soft prompts per component. This is clearly described in the architecture (Figure 1) and Section 3.2, and differentiates the work from prior LLM-for-time-series approaches (One Fits All, TEST) that feed raw/patched series without explicit decomposition.

- **Theoretical motivation for decomposition**: Theorem 3.1 formally states that if trend and seasonal components are non-orthogonal, no set of orthogonal bases can fully separate them. The paper then connects this to the self-attention mechanism (citing prior work that attention learns orthogonal transformations analogous to PCA) to motivate why explicit input decomposition is needed. While the theorem itself is a basic property of orthogonality, this formal framing is a useful contribution beyond purely empirical justification.

- **Strong claimed empirical performance**: The paper reports that TEMPO achieves best average MSE/MAE across all prediction horizons in the many-to-one zero-shot setting, including a 6.5% MAE improvement on Weather and 19.1% on ETTm1 over PatchTST. The textual description claims consistent gains over both LLM-based (GPT2, T5, LLaMA) and non-LLM baselines.

- **Extension to multimodal time series forecasting**: TEMPO is extended to handle time series with textual context (TETS, GDELT) by concatenating text embeddings with decomposed component embeddings. The paper reports that TEMPO outperforms all baselines in cross-domain zero-shot transfer on these datasets, going beyond most prior work that treats time series in isolation.

- **Ablation study isolating components**: The ablation (Section 5.1, table visible in text) systematically compares TEMPO against variants without decomposition, without prompts, and without the decomposition loss. The average results confirm that both the prompt design and decomposition contribute to performance.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity about baseline training/evaluation protocol in the zero-shot setting**: The paper explicitly describes the "many-to-one" zero-shot protocol for TEMPO (trained on source datasets, tested on unseen target). However, it does **not** specify how the baselines (PatchTST, FEDformer, DLinear, GPT2, T5, LLaMA, etc.) are configured in the comparison. The paper simply says "we compare TEMPO with the following baselines" (line 139) without stating whether they are (a) also trained in the same many-to-one zero-shot manner, (b) trained in a standard supervised fashion on the target dataset, or (c) used in a frozen zero-shot manner. Each interpretation leads to a fundamentally different reading of the reported results. Since the paper's central claim is state-of-the-art zero-shot forecasting, the baseline protocol must be explicitly stated. This ambiguity undermines the ability to interpret the reported improvements.

- **Missing critical reproducibility details**: The paper omits several key experimental choices needed to reproduce or evaluate the results: (i) which specific GPT model variant/size is used as the backbone (the paper only says "decoder-based generative pre-trained transformer" and references GPT-2 via radford2019language, but GPT-2 has sizes from 124M to 1.5B parameters); (ii) training hyperparameters — learning rate, batch size, number of epochs, optimizer, LoRA rank, embedding dimension; (iii) which specific source datasets are used for which target (only one example — Weather — is given). Without these details, the experiments cannot be independently verified or reproduced.

### Minor

- **Theorem 3.1 is a basic restatement with a tenuous link to the proposed method**: The theorem restates that non-orthogonal components cannot be separated by a set of orthogonal bases. The claim that "self-attention learns an orthogonal transformation" is cited from prior work (one_fits_all), not proven or analyzed here. The theorem serves as motivation for decomposition, but the paper does not provide a formal analysis showing that TEMPO's approach resolves the claimed limitation (e.g., that the STL decomposition produces components that are orthogonal, or that attention would fail without it).

- **Ablation inconsistencies**: On ECL horizon 720, the full TEMPO model (0.279/0.355) is outperformed by w/o Dec (0.271/0.351) on both MSE and MAE and by w/o Pro (0.269/0.359) on MSE. While TEMPO wins on average across all horizons, this particular case suggests the contributions are not as clean or consistent as the paper's language implies.

- **Decomposition loss (L_Dec) is not precisely defined**: Line 95-96 defines it as `f_T(X, θ_T) -  X̂^g_T` but does not clarify what "global STL decomposition" means in practice — the window or data span over which the global decomposition is computed, how the global reference is obtained, or how this interacts with the "local decomposition within each instance" mentioned earlier.

- **Prompt term V^i in Eq. 1 not fully specified**: The problem definition includes a prompt term V^i, but it is unclear whether this is learned per channel, per dataset, or per instance, and how it is obtained for a new unseen dataset during zero-shot evaluation.

- **Alternative architecture choice not ablated**: The paper acknowledges that an alternative design (separate GPT blocks for each component instead of concatenation) is possible (line 114) but does not provide an ablation or justification beyond a brief mention. This is a significant design choice with no empirical support.

- **TETS dataset lacks description**: The paper introduces the TETS dataset but provides no information about its size, number of channels, time span, collection methodology, statistics, or license. For a newly released dataset, this is insufficient.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment comparing GPT-2 fine-tuned on time series vs. GPT-2 without any time-series fine-tuning, to directly test the claim that pre-trained language model initialization helps.
- Sensitivity analysis on the STL decomposition window size, patch length, and prompt length.
- Confidence intervals or significance tests for the main results.

## Removed Points

These points from the input reviews were flagged and removed, with brief justification:

- **Harsh critic's claim that missing tables (parser issue) prevents verification of results**: The tables are absent due to PDF extraction (parser issue), not author omission. The original submission includes them.
- **Harsh critic's speculation about three possible baseline protocols (a/b/c)**: The critic hypothesizes scenarios without evidence. The real issue is that the paper does not specify the protocol — the speculation about what might be happening adds unnecessary drama. I have kept the core concern (protocol ambiguity) but removed the speculative framing.
- **Claim that "transformer-based architectures training from scratch... tend to underperform... is plausible but unsupported"**: The paper does provide experimental results (Table 3) showing this trend. The criticism is factually incorrect.
- **Strength Finder's strengths that are generic or superficial**: All listed strengths were tied to specific sections/tables, so none were dropped from that source. However, the underlying weakness about the evaluation ambiguity qualifies the "superior zero-shot forecasting" strength — I have preserved the strength as stated by the paper but it should be read with the noted caveat.
- **"Related work does not discuss LLMTime"**: Rule prohibits mentioning missing related works since I cannot verify external content.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about TEMPO's approach that the paper itself does not already state or imply.

## Suggestions

1. **Clarify the baseline protocol explicitly** — state for each baseline category whether it was trained on the target dataset (supervised), trained on the same source datasets in a many-to-one zero-shot manner, or used with no time-series training. If supervised baselines were used, frame the comparison as "zero-shot TEMPO vs. supervised baselines" and note that this is a harder setting for TEMPO.
2. **Report all missing training details** — GPT model variant/size, hyperparameters (learning rate, batch size, epochs, LoRA rank), and a table mapping each target dataset to its set of source datasets.
3. **Define the decomposition loss more precisely** — clarify what "global STL decomposition" refers to and how the global reference window is chosen.
4. **Provide a short description of the TETS dataset** — at minimum: number of instances, time series length, domains, and train/test split.
5. **Ablate the concatenation-vs-separate-GPT-blocks design choice** to justify the architectural decision.
6. **Tone down the foundational model language**: The experiments use 6 benchmark datasets and one multimodal dataset at modest scale — this is impressive for a zero-shot TS paper but does not yet constitute the "paradigm shift" claimed in the introduction.
