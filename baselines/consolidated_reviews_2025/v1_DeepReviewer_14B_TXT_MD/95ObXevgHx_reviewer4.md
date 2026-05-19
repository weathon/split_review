### Summary

This paper investigates the relationship between the layer-wise representations in deep language models (DLMs) and the temporal dynamics of neural activity in the human brain during natural language processing. The authors use electrocorticography (ECoG) to record neural activity from participants listening to a 30-minute narrative while also feeding the same narrative to a high-performing DLM (GPT2-XL). They then extract contextual embeddings from the different layers of the DLM and use linear encoding models to predict neural activity. The results reveal a strong correlation between the layer depth of the DLM and the time at which the layers are most predictive of neural activity in the brain, particularly in high-order language areas such as the inferior frontal gyrus (IFG) and temporal pole (TP). The findings suggest that the layered hierarchy of DLMs may be used to model the temporal dynamics of language comprehension in the brain, with the DLM's layer-by-layer accumulation of contextual information mirroring the timing of neural activity in high-order language areas.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The use of ECoG data provides a unique perspective on the temporal dynamics of language processing in the brain, which is not possible with other non-invasive methods like fMRI.
- The results are robust and consistent across different language areas, suggesting that the findings are not specific to a particular region of the brain.
- The paper provides a novel perspective on the relationship between DLMs and the brain, which could have implications for the development of more brain-inspired language models.

### Weaknesses

#### Some Related Works


#### comment

 - The study only uses one DLM (GPT2-XL) and one dataset (a 30-minute narrative). It is unclear whether the findings would generalize to other DLMs or other types of language processing tasks.
- The paper does not provide a detailed analysis of the limitations of the study, such as the potential for overfitting or the impact of individual differences in brain structure and function.
- The paper does not provide a detailed discussion of the implications of the findings for the development of more brain-inspired language models. It is unclear how the findings could be used to improve the performance of DLMs or to develop new models that are more closely aligned with the neural mechanisms of language processing.

### Suggestions

The study's reliance on a single deep language model (DLM), GPT2-XL, and a single 30-minute narrative dataset raises concerns about the generalizability of the findings. While GPT2-XL is a high-performing model, its architecture and training regime are specific, and it is unclear if the observed layer-wise correlations with neural activity would hold for other DLMs with different architectures (e.g., transformer variants, recurrent neural networks) or training objectives. Furthermore, the use of a single narrative dataset limits the scope of the study, as different types of language processing tasks (e.g., reading, conversation, story generation) might engage different neural mechanisms and thus exhibit different patterns of correlation with DLM layers. To address this, future studies should explore a range of DLMs and datasets, including those with varying complexities and modalities, to determine the robustness of the observed layer-wise correlations. This would provide a more comprehensive understanding of the relationship between DLM representations and neural activity during language processing.

Another area that requires further attention is the potential for overfitting in the encoding models. The paper mentions using cross-validation, but it does not provide sufficient details about the specific procedure used, such as the number of folds, the size of the training and test sets, and the criteria used for model selection. Overfitting is a common problem in neural encoding models, and it is crucial to ensure that the reported correlations are not due to overfitting to the specific data. Furthermore, the paper does not discuss the impact of individual differences in brain structure and function on the results. It is well-known that there is considerable variability in brain activity across individuals, and it is important to determine whether the observed layer-wise correlations are consistent across participants or whether they are influenced by individual differences. Future studies should include a more detailed analysis of individual variability and explore methods for accounting for these differences in the encoding models.

Finally, the paper should provide a more detailed discussion of the implications of the findings for the development of more brain-inspired language models. While the paper suggests that the layered hierarchy of DLMs may be used to model the temporal dynamics of language comprehension in the brain, it does not provide concrete examples of how this could be achieved. For instance, how could the observed layer-wise correlations be used to improve the performance of DLMs or to develop new models that are more closely aligned with the neural mechanisms of language processing? The paper should explore specific avenues for future research, such as using the neural data to guide the training of DLMs or to develop new architectures that are more biologically plausible. This would help to bridge the gap between the fields of artificial intelligence and neuroscience and could lead to the development of more powerful and interpretable language models.

### Questions

- How do the findings of this study relate to other studies that have investigated the neural basis of language processing using different methods?
- How do the findings of this study relate to other studies that have investigated the neural basis of language processing using different methods?
- How do the findings of this study relate to other studies that have investigated the neural basis of language processing using different methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
