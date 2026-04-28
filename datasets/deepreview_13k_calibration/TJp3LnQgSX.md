# FIRING-Net: A filtered feature recycling network for speech enhancement

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6

## Abstract
Current deep neural networks for speech enhancement (SE) aim to minimize the distance between the output signal and the clean target by filtering out noise features from input features. However, when noise and speech components are highly similar, SE models struggle to learn effective discrimination patterns. To address this challenge, we propose a Filter-Recycle-Interguide framework termed Filter-Recycle-INterGuide NETwork (FIRING-Net) for SE, which filters the input features to extract target features and recycles the filtered-out features as non-target features. These two feature sets then guide each other to refine the features, leading to the aggregation of speech information within the target features and noise information within the non-target features. The proposed FIRING-Net mainly consists of a Local Module (LM) and a Global Module (GM). The LM uses outputs of the speech extraction network as target features and the residual between input and output as non-target features. The GM leverages the energy distribution of self-attention map to extract target and non-target features guided by highest and lowest energy regions. Both LM and GM include interaction modules to leverage the two feature sets in an inter-guided manner for collecting speech from non-target features and filtering out noise from target features. Experiments confirm the effectiveness of the Filter-Recycle-Interguide framework, with FIRING-Net achieving a strong balance between SE performance and computational efficiency, surpassing comparable models across various SNR levels and noise environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Speech enhancement model with local and global information, where target and non-target portions interact with each other.

### Strengths
Idea appears to make sense, experimentation is done with care and results are good.

### Weaknesses
I am not completely sure that noise types used in training are not also seen in testing. What is clear is that SNR levels are same in training andf testing cases. So, it would be good to see how well the model generalizes to unseen conditions, unseen SNR level would be a fairly extreme tests case. 

I also noticed that SNR scale is pretty extreme (from -5 to 5 db). How about using more moderate noise levels? Would the differences to competing models then disappear? 

All ideas seem to be gathered from previous publications (like CV papers). It would be good to emphasize the novel technical contributions in the Introduction.

### Questions
- How do you know that in Eq. (1) convolution is going to separate target and non-target? In the Fig 3 it seems to be the case, but it is not clear to me that why that happens.
- Why in Table 6 lots of methods have same STOI value? 
- In Eq. (14) some loss hyperparameters are explained, you set those to "0.2, 0.9, 0.1, and 0.3.", did you try to optimize these values? Even more importantly if you did experiment with these values, then did you look at the Table 1 and 2 while experimenting?  What I am looking for here is that how britle are these selections for practical use cases. Can someone just use them and assume that they will work out of the box?
-  Why reverb is used in the training, when testing no such cases are seen? How about removing reverb data from the training. Also, did you use the exactly same training set for all competing models?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This article presents FIRING-Net, a speech enhancement method based on the Filter-Recycle-Interguide strategy. This approach refines the extraction of speech and noise features through local and global modules, improving speech enhancement performance in complex noise environments. Experiments show that FIRING-Net significantly enhances performance across multiple datasets. The main contributions include a novel feature optimization strategy and experimental validation under various noise conditions.

### Strengths
1. The paper introduces a novel "Filter-Recycle-Interguide" (FRI) strategy, which is capable of effectively distinguishing between speech and noise features by mutual guidance, thereby achieving better noise reduction and speech restoration.

2. Through the design of local modules (LM) and global modules (GM), the paper effectively extracts target and non-target features by utilizing the energy distribution of convolutional module outputs and self-attention maps, respectively, thereby enhancing noise resistance performance.

3. By conducting extensive experiments on various public datasets and at different signal-to-noise ratio (SNR) levels, the proposed method demonstrates significant improvements in metrics such as PESQ and SI-SNRi compared to some existing methods, validating its effectiveness.

### Weaknesses
1. The paper's starting point is that "when noise and speech components are highly similar, it is difficult for the SE model to learn effective discrimination patterns." However, this aspect of the contribution is not prominently mentioned in the subsequent methodology analysis and experiments. The paper does not adequately demonstrate how the proposed Filter-Recycle-Interguide (FRI) strategy specifically addresses this challenge of high similarity between speech and noise. The explanation of how the recycled filtered information and the output are "primarily dominated by noise and speech features, respectively" lacks sufficient detail and justification.

2. In the field of speech enhancement, there have been some related studies on refining and interacting features that were not referenced in the paper. Therefore, the selection of baseline methods for comparison in the experiments also lacks specificity. The paper does not clearly articulate how the proposed method differs from existing feature interaction techniques. The lack of a thorough literature review makes it difficult to assess the novelty of the approach. The baseline methods chosen for comparison do not seem to directly address the specific problem of highly similar speech and noise components.

3. There is a lack of qualitative analysis of the method and experiments, which results in a lack of interpretability and fails to distinguish the proposed method from existing research and the baseline methods used in the comparative experiments. The paper does not provide sufficient qualitative examples or visualizations to demonstrate the effectiveness of the proposed method. The absence of detailed analysis makes it difficult to understand the specific mechanisms by which the proposed method achieves its performance gains.

### Questions
1. Perform qualitative and interpretable analysis of the model method.
2. Explain how the subsequent experiments and the selection of baseline models for comparison reflect the challenges addressed by the paper’s starting point, which is “when noise and speech components are highly similar, it is difficult for the SE model to learn effective discrimination patterns.”

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a novel approach to speech enhancement (SE) using a method called FIRING-Net, which incorporates a Filter-Recycle-Interguide (FRI) strategy. This strategy divides input features into target (speech) and non-target (noise) components, allowing for mutual refinement between these features.

### Strengths
1. The paper introduces a novel Filter-Recycle-Interguide (FRI) strategy for speech enhancement, which is a creative approach to refining speech and noise components. This method effectively separates and processes target and non-target features, offering a fresh perspective on enhancing speech quality.
2. The study conducted experiments on WSJ0-SI 84 + NOISEX-92 and AVSpeech + AudioSet. The results show substantial improvements in PESQ and SI-SNRi metrics compared to existing models. The paper also includes a comprehensive ablation study that validates the effectiveness of each component and the overall framework.

### Weaknesses
1. There are similar methods to this approach that also use cascaded strategies to enhance the model's ability to extract target speech, such as TaylorSENet [1]. However, these methods were not compared in the paper.

2. For the experimental section, the model trained on the DNS Challenge training set should naturally be tested on the public DNS Challenge test set. However, the authors chose two other datasets, which is quite odd. I believe the authors should test the model on the DNS Challenge test set to better demonstrate the model's performance.

3. In the appendix, the experimental results of VoiceBank-DEMAND show a significant discrepancy in the results of MP-SENet compared to the original paper. The authors mentioned that these results were not in the original paper, but they are detailed in the official repository: https://github.com/yxlu-0102/MP-SENet/blob/main/Figures/table.png. For detailed results, see: https://github.com/yxlu-0102/MP-SENet.

4. In the ablation study section, Table 3 is not referenced for the LM ablation study and should be added.

5. In the appendix, please specify whether the PESQ is narrowband or wideband, as these will yield different results.

6. The visualization results should include experiments with better-performing methods, such as MP-SENet, to see if similar issues persist.

7. For the experiments with IM-E Modification 2 and IM-D Modification 2, would incorporating both modules simultaneously yield better results? According to Tables 8 and 9, both modules perform second best but with fewer parameters, which is advantageous for speech enhancement. Is it possible to include both modules to reduce the parameter count and improve model performance?

8. Some dimension symbols in the paper, such as $L$, are not explained.

9. Word misuse: convolution operation -> convolutional operation

### Questions
Consistent with the weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new deep network architecture for speech enhancement (SE) called FIRING-Net (FIlter-Recycle-INterGuide NETwork). To deal with the more challenging scenarios where the interference/noise characteristics are highly similar to the target speech signal, e.g., in the case of babble noise, the authors propose to recycle filtered-out features for extracting more discriminative patterns between speech and noise through refinement. This is achieved by re-defining the filtered-out features as non-target features, which are used to guide the learning of target features in an interactive manner. More specifically, the FIRING-Net features two key components: Local Module (LM) and Global Module (GM), to perform the recycle-and-refine idea in a local and global manner. The LMs utilizes Interaction Modules (IMs) that have different designs for the encoder and decoder sides. The GM exploits energy distributions of the attention maps to guide extration of the speech and noise features. Experiments on several datasets demonstrate the effectiveness of FIRING-Net over various signal-to-noise ration (SNR) settings and across several noise types, including the challenging case of babble noise.

### Strengths
- The proposed system (FIRING-Net) based on the idea of recycling intermediate speech and noise features to further improve the separation of target and non-target components seems novel.

- Good performance of the FIRING-Net across various SNR and noise types (E.g., Tables 1, 2).

- Relatively small model size with low latency (Eg., Tables 3, 4), which is important for many SE applications.

- Extensive ablation studies showing the effect and contribution of each key component, i.e. LM, GM and IMs, on the overall SE performance.

### Weaknesses
 - The main weakness is there seems lacking a clear explanation as why the proposed architecture, especially the Local Modules (LMs), can promote target speech and non-target noise features extraction in the way as claimed in the paper. To be more specific, for the proposed LM-E (and LM-D) in Figure 2, what is the actual mechanism or reason that leads to the model assigning speech to the $f_t$ branch and noise to the $f_n$ branch? Please provide more detailed explanations on how such network design promotes speech and noise separation  to carry out the proposed feature recycling scheme. The paper currently lacks a detailed explanation of how the subtraction operation in the LM modules contributes to feature separation, especially given that the feature values are not inherently constrained before this operation. The explanation should clarify why this specific operation, rather than a simple addition, is crucial for the proposed feature recycling mechanism. Furthermore, the paper needs to better explain how the normalization layers interact with the subtraction to achieve feature separation, and why this combination is superior to using addition or no normalization.

- Another weakness of the paper is that the proposed SE model is tested on synthesized noisy speech data only. To better demonstrate the superiority of the proposed model, it will be nice if testing on real-world recorded noisy speech samples can be performed (e.g., using the realistic noisy samples from the CHiME-3 dataset: *J. Barker et al., “The third ‘CHiME’ speech separation and recognition challenge: Analysis and outcomes,” Comput. Speech Lang, 2017*). In this case, since there will be no ground-truth references to compute the objective metric scores used in the paper (i.e., PESQ, STOI, and SI-SNRi), the comparison with baselines may be done by using subjective listening testing or using automatic speech recognition (ASR) as evaluators.

### Questions
- Could the authors explicitly associate the "Network for speech extraction" in Figure 1 to the corresponding module(s) or layer(s) in Figure 2? This will help understanding where the recycling scheme actually takes place. Similarly, association of the "Network for noise extraction" in Figure 1 to the place(s) in Figure 2 will be helpful.

- In Figure 2, the LM-E (or LM-D) module has addition and subtraction operators. However, the subtraction operation may not lead to a different result from using addition if the feature value range is not constrained. For example, if the values of $f_{t,t}$ span all real-numbers, then it does not matter if you get $f_{t,n}$ by subtracting $f_{t,t}$ from $f_{t}$ as eq. (3), or by adding them as $f_{t,n}=f_{t}+f_{t,t}$ -- the Dense Block that outputs $f_{t,t}$ should be able to adjust its parameters to account for the opposite sign. Therefore, it is not clear if using the subtraction instead of addition is necessary.

- For the target and non-target feature plots in Figure 3, are they $f_t$ and $f_n$ extracted by the Conv 2D layer as eq. (1), or the refined features $\hat{f}_t$ and $\hat{f}_n$  before the IM-E (or IM-D)? Also, is it possible to compare $f_t$ to $\hat{f}_t$ and $f_n$ to $\hat{f}_n$? Knowing the difference will be helpful for understanding the contribution of the feature refinement step.

- In Figure 4 (a), the mask $M_t$ may be directly apply to extract the target features by multiplying it with the feature $\hat{f}_t$. So what is the role of the sigmoid here? (In other words, why should $|Sigmoid(\hat{f}_t)-M_t|\odot\hat{f}_t$ be considered instead of $M_t\odot\hat{f}_t$)? 

- From Figure 9, it looks like that IM-E Modification-3 (d) is just taking off one Sigmoid operation from the Original IM-E (a). Then, why does the model size become smaller (1.64M) for (d) than the original size (1.74M) for (a) as presented in Table 8? 

- On page 7, the paragraph below eq. (6): "... obtained by $f_n=f_4+f_{2,n}+f_{n,t}$" should be "$f_n=f_4+f_{2,n}+f_{3,n}$"?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper, based on the challenges in the field of speech enhancement when noise and target speech are similar, designs a Filter-Recycle-InterGuide Network (FRIGNet). It utilizes target features and non-target features for mutual refinement, and based on the mutual refinement of positive and negative features, it has designed LM and GM modules. Additionally, it employs an attention module based on energy segmentation to complement the network.

### Strengths
The paper has a novel approach. While others focus only on how to better eliminate non-target features, the authors consider both target features and non-target features to refine each characteristic. Based on this, the overall network architecture and individual modules are designed based on the logic of mutual refinement between target features and non-target features. An attention mechanism based on energy levels is also introduced. The model performs well in both comparative experiments and ablation studies.

### Weaknesses
The paper extensively discusses how the model uses operations such as generating masks, convolutions, and additions/subtractions to obtain the so-called target features and non-target features mentioned in the text. However, it lacks a theoretical explanation for why these operations result in target features or non-target features. Specifically, the use of residual calculation for extracting non-target features, while intuitively plausible, needs a more rigorous justification. The assumption that the residual primarily contains noise is not always valid, especially when the network's filtering is imperfect or when the target and non-target signals have overlapping spectral characteristics. Furthermore, the paper does not provide a clear mathematical formulation of how the normalization layers ensure energy consistency between the input and the extracted residuals, making it difficult to assess the robustness of this approach. Additionally, it is unclear whether the attention module based on energy segmentation is an original innovation or borrowed from other papers. The paper does not sufficiently detail how the energy-based segmentation is implemented within the self-attention mechanism, nor does it provide a comparative analysis with existing energy-based attention methods to highlight its unique contributions.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3
