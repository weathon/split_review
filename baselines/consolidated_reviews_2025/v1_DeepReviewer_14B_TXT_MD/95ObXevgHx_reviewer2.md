### Summary

This paper investigates the similarities between the layerwise representations in a deep language model (GPT2-XL) and the temporal dynamics of neural activity in the human language network as measured using electrocorticography (ECoG). The authors found that: 1) intermediate layers of the DLM best predict neural activity across language areas; 2) the layerwise predictive power of the DLM unfolds over time, such that earlier layers are more predictive of neural activity earlier, and later layers are more predictive of neural activity later; and 3) the temporal unfolding of the layerwise predictive power is most pronounced in higher-order language areas (anterior STG, TP), relative to lower-level areas (mSTG).

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and the results are interesting. The finding that the layerwise representations in DLMs map onto the temporal dynamics of neural activity in the language network is novel and provides further evidence for how the internal representations of DLMs may be relevant to understanding neural language processing.

### Weaknesses

#### Some Related Works


#### comment

The authors do not provide a strong justification for why ECoG is needed to answer the research question, rather than fMRI. The authors state that the ECoG recordings provide superior spatiotemporal resolution, but it is not clear to me that the temporal resolution is needed to address the research question. It would be useful if the authors could provide a more detailed justification for why ECoG is needed to address the research question, relative to fMRI.

The authors state that "we averaged over lags to get an average encoding performance per layer" (Line 268). This does not seem like a valid approach to calculating the average encoding performance, since it would conflate the signal attributable to the neural response to the current word with the signal attributable to the neural response to the previous word. It would be useful if the authors could clarify how they calculated the average encoding performance per layer.

The authors state that "we averaged over lags to get an average encoding performance per layer" (Line 268). This does not seem like a valid approach to calculating the average encoding performance, since it would conflate the signal attributable to the neural response to the current word with the signal attributable to the neural response to the previous word. It would be useful if the authors could clarify how they calculated the average encoding performance per layer.

The authors state that "we averaged over lags to get an average encoding performance per layer" (Line 268). This does not seem like a valid approach to calculating the average encoding performance, since it would conflate the signal attributable to the neural response to the current word with the signal attributable to the neural response to the previous word. It would be useful if the authors could clarify how they calculated the average encoding performance per layer.

The authors state that "we averaged over lags to get an average encoding performance per layer" (Line 268). This does not seem like a valid approach to calculating the average encoding performance, since it would conflate the signal attributable to the neural response to the current word with the signal attributable to the neural response to the previous word. It would be useful if the authors could clarify how they calculated the average encoding performance per layer.

The authors state that "we averaged over lags to get an average encoding performance per layer" (Line 268). This does not seem like a valid approach to calculating the average encoding performance, since it would conflate the signal attributable to the neural response to the current word with the signal attributable to the neural response to the previous word. It would be useful if the authors could clarify how they calculated the average encoding performance per layer.

### Suggestions

The authors should provide a more detailed justification for using ECoG over fMRI, specifically addressing why the temporal resolution is crucial for their research question. While ECoG offers superior temporal resolution, it is not clear that the research question necessitates this level of detail. The authors should elaborate on the specific hypotheses that require millisecond-level temporal resolution and explain why fMRI, with its slower hemodynamic response, would be insufficient. For example, if the hypothesis involves tracking the propagation of information through different layers of the language network on a timescale of tens of milliseconds, then this would be a valid justification. However, if the hypothesis is about the overall hierarchical organization of the network, then fMRI might be sufficient and more broadly applicable. The authors should also discuss the limitations of fMRI in this context, such as its inability to capture fast neural dynamics, and explain why these limitations are critical for their study. Furthermore, the authors should consider whether the same research question could be addressed with fMRI data, and if so, why ECoG is essential.

The authors need to clarify how they calculated the average encoding performance per layer. Averaging over lags, as described, is problematic because it mixes the neural response to the current word with the response to the previous word, making it difficult to interpret the results. The authors should explain how they handled the lag variable when calculating the average encoding performance. For example, did they average the encoding performance at each lag separately for each layer, and then average across lags, or did they use a different approach? It would be helpful if the authors could provide a more detailed description of the averaging process, including the specific formula used. Additionally, the authors should consider whether it would be more informative to analyze the encoding performance at specific lags of interest, rather than averaging across all lags. This would allow for a more fine-grained analysis of the temporal dynamics of the neural response and its relationship to the DLM representations. The authors should also clarify whether the lag variable was treated as a continuous or discrete variable in their analysis.

The authors should also clarify the relationship between the lag at which the encoding performance peaks and the layer number. While the authors found a significant correlation between these two variables, it is not clear what this correlation means in terms of the underlying neural processes. The authors should provide a more detailed interpretation of this correlation, explaining how it relates to the hierarchical organization of the language network. For example, do the earlier layers of the DLM correspond to lower-level sensory areas, while the later layers correspond to higher-level semantic areas? And how does the temporal unfolding of the layerwise predictive power relate to the flow of information through the network? The authors should also consider whether the correlation between lag and layer number is specific to the DLM used in this study, or whether it is a more general property of language processing. Finally, the authors should discuss the limitations of their approach, such as the fact that they are using a single DLM and a single dataset, and suggest directions for future research.

### Questions

The authors state that "we averaged over lags to get an average encoding performance per layer" (Line 268). This does not seem like a valid approach to calculating the average encoding performance, since it would conflate the signal attributable to the neural response to the current word with the signal attributable to the neural response to the previous word. It would be useful if the authors could clarify how they calculated the average encoding performance per layer.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
