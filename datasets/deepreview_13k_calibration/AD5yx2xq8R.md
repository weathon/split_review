# XAIguiFormer: explainable artificial intelligence guided transformer for brain disorder identification

- Decision: Accept
- Avg Score: 5.75
- Scores: 3, 6, 8, 6

## Abstract
EEG-based connectomes offer a low-cost and portable method to identify brain disorders using deep learning. With the growing interest in model interpretability and transparency, explainable artificial intelligence (XAI) is widely applied to understand the decision of deep learning models. However, most research focuses solely on interpretability analysis based on the insights from XAI, overlooking XAI’s potential to improve model performance. To bridge this gap, we propose a dynamical-system-inspired architecture, XAI guided transformer (XAIguiFormer), where XAI not only provides explanations but also contributes to enhancing the transformer by refining the originally coarse information in self-attention mechanism to capture more relevant dependency relationships. In order not to damage the connectome’s topological structure, the connectome tokenizer treats the single-band graphs as atomic tokens to generate a sequence in the frequency domain. To address the limitations of conventional positional encoding in understanding the frequency and mitigating the individual differences, we integrate frequency and demographic information into tokens via a rotation matrix, resulting in a richly informative representation. Our experiment demonstrates that XAIguiFormer achieves superior performance over all baseline models. In addition, XAIguiFormer provides valuable interpretability through visualization of the frequency band importance. Our code will be publicly available after acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposed a dynamical-system-inspired architecture, XAI guided transformer (XAIguiFormer), where XAI not only provides explanations but also contributes to enhancing the transformer by refining the originally coarse information in the self-attention mechanism to capture more relevant dependency relationships.

### Strengths
1. This method proposed a fusion strategy to explicitly inject the frequency and demographic information into tokens, improving the model’s understanding of the frequency and mitigating the negative effects of individual differences.
2. This method proposed to use XAI to directly enhance transformer performance rather than focusing only on analyzing the visual interpretability.

### Weaknesses
1. Robustness is unclear. How about the performance after changing to other explainers in the module in addition to using DeepLift? How about the robustness?
2. How to calculate the frequency band importance? Is the result from the explainer inside the proposed model? If so, can it get the same conclusion after changing the explainer?
3. In Fig 3, why does the accuracy of warm-started XAI keep decreasing after training? The accuracy at the beginning is the best one, so how does it prove the effectiveness of the proposed method? It becomes worse after training the proposed one.

### Questions
see above. The questions are about the description of warmup start XAI guidance and the robustness of the explainer module in the proposed method.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces XAIguiFormer, a transformer model guided by explainable AI (XAI) techniques to enhance model performance. The authors integrate both frequency and demographic information into the model’s tokenization process, demonstrating that these features are essential for the observed performance improvements. XAIguiFormer achieves superior results compared to baseline models

### Strengths
1. The authors clearly define the specific issue they aim to address and effectively outline their solution approach. The introduction is clear and acknowledges the relevant literature and highlighting the limitations of current methods. The authors also provide a thorough comparison with a range of other methods and evaluate their approach on two public datasets. Another strength is that they intend to share their code upon acceptance, promoting transparency and reproducibility. The ablation studies also highlights the importance of both proposed suggestion (positional embedding and models guided by interpretability)

### Weaknesses
2. Section 5.1 provides a brief description of the datasets; however, given the importance of demographic information to the proposed method, the authors should expand on this aspect in that section. Specifically, the description lacks detail regarding the distribution of demographic features within each dataset, such as age, gender, and the specific types of brain disorders. Furthermore, it would be helpful to know if demographics were considered when creating the train/test/validation split. How was the data split? Are the different diseases balanced on both datasets? Furthermore, what is the distribution of patients with brain disorders versus healthy individuals across splits? The absence of this information makes it difficult to assess the potential for bias in the model's performance and limits the generalizability of the findings.



### Questions
3. Line 369: The authors mention that the BAC, AUC-PR are the average performance and standard deviation across five different random seeds on the TUAB and TDBRAIN dataset. I am assuming that the models were re-trained 5 times using different train/val splits while test data was kept constant, could the authors clarify if this is case? I am guessing that the reason why the models were re-trained 5 times is due to computational limitations, could the authors elaborate on the computational costs of their method compared to the other baseline methods? 
4. In the text line 335 the authors mention: “XAIguiFormer is not sensitive to \alpha as long as it is larger than 0.3”. Could the authors report those results and discuss why they believe that there is a lower threshold but not an upper threshold?
5. Figure 4 illustrates the importance of difference frequency bands, could the author further clarity how the frequency information can be extracted from XAIguiFormer?
6. Could the authors include some discussion on the limitations of the presented method?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces XAIguiFormer, a transformer model that uses explainable AI to both interpret and improve brain disorder detection from EEG data. The model features novel tokenization and encoding methods to preserve brain network patterns, achieving better performance than existing approaches while providing insights into which brain wave frequencies are most important for diagnosis.

### Strengths
The paper uses XAI to actively improve model performance rather than just for interpretation.

The connectome tokennization approach and demographic-aware frequency encoding are also novel.

There are comprehensive experiments and ablation studies.

### Weaknesses
Authors should discuss further on why they chose to model EEG as connectome rather than time series, given some state-of-the-art EEG foundation models with time series as input, such as [1], especially it focuses on frequency domain as well. Experimental comparisons with these EEG models are also missed in the paper.

It seems like only temporal frequency is considered in positional encoding, how about spatial frequency for different brain regions? Some work like [2] developed spatial connectome based positioning, which should at least be discussed in the paper.

Limited dataset scope: Only tested on two datasets (TUAB and TDBRAIN) which may not fully represent real-world clinical diversity.

Discussion of training time, computational efficiency compared to the baselines would be appreciated.

The model relies heavily on DeepLift's accuracy without exploring alternative explanation methods ot validating explanation quality.

### Questions
The proposed method assumes explanations from an imperfectly trained model can improve performance, would that propagate early training errors?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors proposed XAIguiFormer, the first framework to employ XAI for enhancing transformer performance in neuroimaging data. The explanability and accuracy are both improved as shown in experiments, while the improvement of accuracy might be not caused by the higher explanability.

### Strengths
1. Clear motivations.

2. Good paper writing.

3. Idea of explanability guiding self-attention is novel.

### Weaknesses
1. Figures are too far to the corresponding descriptive text, e.g., fig.2 in page 6 is described in page 9. I recommend moving Figure 2 closer to its description or adding a forward reference earlier in the text.

2. The attention map by the proposed XAI has lower entropy, which is called an improvement in line 463. It confused readers to an accuracy improvement according to the proposed XAI attention map. Although authors were selling the story under such motivation, the relationship between entropy and accuracy are missed. Can you provide entropy-accuracy curves or other quantitative evidence demonstrating how the lower entropy attention maps directly contribute to improved model performance? I think this the key results to support the proposal in this paper, I will raise the score if these results are fit with the expectation.

3. The proposed method leads to a new attention map that is more determined and hence easier to be explained. Even there is an qualitative assessment given neuroscience literatures, more details are needed on how the results in fig.4 were computed. Can you include a quantitative evaluation of how well the attention maps align with established neuroscience knowledge?

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
3
