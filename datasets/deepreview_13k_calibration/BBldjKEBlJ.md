# QuantFormer: Learning to quantize for neural activity forecasting in mouse visual cortex

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Understanding complex animal behaviors hinges on deciphering the neural activity patterns within brain circuits, making the ability to forecast neural activity crucial for developing predictive models of brain dynamics. This capability holds immense value for neuroscience, particularly in applications such as real-time optogenetic interventions. While traditional encoding and decoding methods have been used to map external variables to neural activity and vice versa, they focus on interpreting past data. In contrast, neural forecasting aims to predict future neural activity, presenting a unique and challenging task due to the spatiotemporal sparsity and complex dependencies of neural signals.
Existing transformer-based forecasting methods, while effective in many domains, struggle to capture the distinctiveness of neural signals characterized by spatiotemporal sparsity and intricate dependencies.
To address this challenge, we here introduce \emph{QuantFormer}, a transformer-based model specifically designed for forecasting neural activity from two-photon calcium imaging data. Unlike conventional regression-based approaches, \ours reframes the forecasting task as a classification problem via dynamic signal quantization, enabling more effective learning of sparse neural activation patterns. Additionally, \ours tackles the challenge of analyzing multivariate signals from an arbitrary number of neurons by incorporating neuron-specific tokens, allowing scalability across diverse neuronal populations.\\
Trained with unsupervised quantization on the Allen dataset, \ours sets a new benchmark in forecasting mouse visual cortex activity. It demonstrates robust performance and generalization across various stimuli and individuals, paving the way for a foundational model in neural signal prediction.\\
Source code available \href{https://anonymous.4open.science/r/quantformer2024-FE31}{online}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a large-scale model pretrained on the Allen corpus, which includes calcium imaging spiking activity from the mouse visual cortex under various stimulus conditions. It presents a transformer that uses vector quantization to create a set of neural codebooks for forecasting spiking activity. This quantization approach was shown to be effective in neural activity prediction, outperforming other baseline time series forecasting models. Additionally, the paper demonstrates positive scaling results across different stimuli and individual subjects.

### Strengths
This paper attempts to tackle an important problem of building "foundation models" for neuroscience that can predict spiking activity and classify responses to stimuli.

### Weaknesses
1. While vector quantization has not previously been used to build neuroscience foundation models, the author did not provide sufficient justification for choosing this specific model architecture. The explanation in Section 3.3 does not adequately address why vector quantization is superior to other methods for this task, particularly given the availability of other time-series models. The paper needs a more thorough discussion of the theoretical and empirical reasons for selecting this approach over alternatives.
2. The paper proposes only two types of downstream tasks for evaluating the foundation model. A more comprehensive evaluation is needed to assess the model's generalizability across diverse downstream tasks. The current evaluation is insufficient to demonstrate the model's versatility and applicability to a wide range of neuroscience problems. The tasks should include more complex scenarios, such as decoding behavior or predicting neural responses to novel stimuli.
3. The paper lacks a scaling analysis to evaluate how effective the proposed backbone is for developing a foundation model. It is unclear how the model's performance scales with increasing data size or model complexity. A proper scaling analysis is crucial for demonstrating the potential of the model as a foundation model for neuroscience.
4. The foundation model backbone could benefit from more rigorous benchmarking against existing methods on self-supervised prediction of spiking activity. The current comparison to other time series models is not sufficient. The paper should include comparisons to methods specifically designed for neural data, such as NDT1 [1] and MtM [2], to establish the model's performance relative to the state-of-the-art.

### Questions
**Major:**
1. In the introduction and related work section, the author cites many other time series models but doesn’t clearly motivate the choice of vector quantization for this work. Is this because this architecture has not been applied to neuroscience before? Although the author attempts to motivate the model choice in Section 3.3, it would be good to clarify the motivation earlier in the paper. **Could the author elaborate on why vector quantization was used or provide interpretable analysis, similar to what is found in the Appendix regarding the neural codebook?** I’m looking for a deeper discussion of how ML tools can help us answer unaddressed neuroscience questions, rather than just presenting another ML method that hasn’t been applied in the field.
2. Instead of comparing this model to other time series transformers, this method could be better benchmarked against existing work on self-supervised prediction of neural activity, such as NDT1 [1] and MtM [2]. Both methods can be repurposed for causal prediction of calcium imaging spiking activity and use masked modeling. **Could the author include experiments that compare their model to at least one of these approaches?**
3. Regarding model architecture, why not directly predict activity using a linear layer after the transformer encoder, as done in BERT? What is the rationale for using quantization and additional parameters in the transformer decoder? **An ablation study could help show the advantages of using quantization.** While Table 3 includes an ablation comparing quantization to an autoencoder, it would be more informative to compare it to a transformer baseline without quantization.
4. In Figure 3, I’m curious why the other baselines performed so poorly in predicting the target. It seems that **the evaluation could be conducted more carefully and fairly against other methods**. **For qualitative analysis, could the authors provide single-neuron peri-stimulus time histograms (PSTH) and single-trial activity after subtracting the PSTHs?** This would help clarify whether the model is only capturing the average pattern in the data.

**Minor:**
1. The author includes a stimulus token for neural activity forecasting, but incorporating stimulus information can also be considered a form of neural encoding. What would happen if stimulus information were excluded?
2. In Equation (2), why is the loss computed on both masked and unmasked portions? What is the rationale for balancing these two components, and what advantages does this provide?
3. I find Section 3.4.1 confusing. The author states that “feeding neuron and stimulus identifiers to the encoder is a key aspect of the approach.” Could this be clarified? Why not use per-neuron tokens as in POYO [3]? Additionally, what is the dimension of $t_1, ..., t_P$?
4. In the experiment section, the author mentions allocating two sub-sessions for training and testing, with each sub-session separated by 10-15 minutes. This interval seems quite long, and I wonder how the author addressed non-stationarity and potential distribution shifts in the neural data. Has the distribution of the training and test data been visualized?
5. In lines 392-394, the author claims that “brain signals can be encoded with 32 indices.” It would be cool for the author to further interpret this finding. However, I only found ablation studies on the number of quantization indices and a visualization of the learned neural notebook in the appendix. Does the author have a hypothesis as to why 32 indices are optimal?

[1] Ye, J., & Pandarinath, C. (2021). Representation learning for neural population activity with Neural Data Transformers. 

[2] Zhang, Y., Wang, Y., Jimenez-Beneto, D., Wang, Z., Azabou, M., Richards, B., ... & Hurwitz, C. (2024). Towards a" universal translator" for neural dynamics at single-cell, single-spike resolution. 

[3] Azabou, M., Arora, V., Ganesh, V., Mao, X., Nachimuthu, S., Mendelson, M., ... & Dyer, E. (2024). A unified, scalable framework for neural population decoding.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a transformer-based architecture for single-neuron response forecasting. In a first step, the authors use autoencoding to pre-train an encoder or neuronal response sequences. In a second step, they fine-tune the encoder on an activity classification and a response forecasting task. They evaluate their model using visually evoked responses in the visual cortex of mice. Compared to a few forecasting models they achieve improved activity classification and response forecasting metrics.

### Strengths
- Novel architecture and interesting idea in principle
- Paper is well written and easy to follow
- Shows some ablation experiments to tease apart which components are important

### Weaknesses
 - Doing response forecasting on visually evoked responses seems like an odd choice
- Unclear how strong the baselines are 
- Simple baselines like PSTH or linear encoding models are missing



### Questions
While I like the overall modeling approach and thinks it’s sane in general, I am somewhat confused by the authors’ choice of evaluation using visually evoked responses, which leaves me with lots of question marks whether the model works and how well. In my opinion, it is simply impossible to deduce anything about the performance of this model from the evaluation presented by the authors, because it does not properly deal with the visual stimulus. Although I doubt it, it is possible that I’m missing something. I would therefore like the authors to answer the following:

 1. When response forecasting is the goal, why do you use visually evoked responses, where the response is primarily determined by the stimulus rather than by past or pre-stimulus activity? There is some discussion around using the model online in experiments for optogenentic manipulation, but this motivation is not clear to me. In an experiment you control the visual stimulus that is shown, so you could easily incorporate it.
 1. If you choose to evaluate on visually evoked responses, the null model that you would have to beat is to simply take the PSTH of the neuron in response to the stimulus. I understand that your hypothesis may be that neurons do more than just responding to the stimulus and your goal is to explain this additional “noise” — but to drive home this point you first need a convincing stimulus-response baseline, onto which you can add the forecasting component. 
 1. It appears to me that your model is trying to squeeze the stimulus-driven response patterns into a combination of neuron id token and stimulus token. Can you provide evidence against my hypothesis? Have you quantified for what fraction of the neurons’ response variance (during x_f) the PSTH accounts? Does your forecasting model exceed this value? I doubt it, given the correlation of 0.33 in Table 2.
 1. If you do not want to model the stimulus-driven response via an encoding model (or the PSTH), you should evaluate on datasets that do not have such strong external drive.
 1. Can you comment on whether your model beats any of your baselines on the datasets on which they have been tested and reported by the original authors? Did you train them yourself on the Allen dataset?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces QuantFormer, a novel transformer-based model designed to forecast neural activity in mouse visual cortex using two-photon calcium imaging data. The authors reframe neural forecasting as a classification problem through vector quantization, and employ neuron-specific tokens to identify single neurons. The approach uses a two-stage training process combining pre-training through masked auto-encoding with downstream training for neural activity classification and forecasting. The network is trained on raw fluorescence traces from the Allen dataset traces rather than spike data or deconvoled fluorescence data.

### Strengths
- Very paper is well written. Previous literature and related work is mostly addressed, although a few citations might be missing.
- The main novelty seems to be the quantization stage that can predict the activity of neurons as a function of 32 codebook vectors.

### Weaknesses
 - A closer examination of QuantFormer's architecture raises important questions about its broader applicability and evaluation methodology. The encoder-quantizer-decoder architecture, while novel, relies on a relatively small codebook of 32 entries to represent all possible neuronal activity patterns. Since the codebook and decoder remain frozen after pre-training (as far as I understand), this potentially limits the model's ability to represent novel activity patterns not seen during pre-training. This yields a model that is strictly not image computable and has therefore less abilities than a simple CNN model based on images (which could be trained to forecast as well). This is a major limitation of the model that is not properly discussed.
- As a direct result from using a finite set of stimuli, also the training and test protocol raises questions. As far as I understand, the pre-training phase includes data from the same neurons and images that appear in the test set, which may allow the model to learn specific response patterns before the actual testing phase. Because the Allen datasets includes repetitions of stimuli, this could be a major confounder for the results as the model can simply learn the mean responses given the the stimulus. The authors describe that they do not use neuron identities for pretraining. However, I (a) find this a questionable choice because this should severely limit the prediction capabilities of the model (what’s common to all neurons in cortex?) and (b) I am still not convinced that this would avoid the problem that the model learns mean responses of neurons.
- Because of that, I find the contributions overstated:
    - Forecasting for optogenetic manipulations is mentioned I could not find any experiment on that.
    - Forecasting has been addressed by other transformer architecture, for instance the “universal translator” by Zhang et al (see below), which is not cited or compared to as far as I can see.
    - Reframing forecasting of time series as a classification problem is per-se not a contribution if it doesn’t solve problems. As argued above, it seems to create problems.
    - Handling arbitrary neuronal populations is not new as other works (such as the POYO model) already use neuron ID tokens.
    - Finally, I would hardly call a model that is trained to forecast neurons from a finite set of stimuli a “foundation model for visual cortex”. In particular, I would expect a foundation model to be image/video computable.
- I find the choice of dataset not well motivated. The authors argue with real-time applicability. But then they don’t test it in those conditions. So in that sense they could apply it to a bigger dataset such as SENSORIUM 2022 (if they still want to exclude videos). My guess is that the method will not work well as it contains many unique stimuli in the training set. In particular, the choice of dataset is at odds with the motivation for the codebook (sparsity). I would expect fluorescence data to be less sparse than deconvolved data (such as Sensorium). It that sense SENSORIUM or spiking data should be even better data. Finally, I do not understand how they can get baseline activity for neurons in the Allen data. As far as I remember about the dataset, images are presented back to back. This means that neuronal firing does not return to baseline between images. I do not see how this is addressed in the paper.
- I find the choice of models to compare to a bit weak. I would recommend to include at least an oracle estimator that uses the mean responses of the neuron to that stimulus in the training set. Additionally, my guess is that a model pretrained properly on SENSORIUM and then trained to forecast a fixed number of steps in the future, should be competitive.
- Why is neuronal identity and the stimulus ignored during pretraining? I do not understand the rationale for it. Why is it not trained on forecasting with neuronal activities since this seems to generate problems (as discussed in 3.4.2)
- I find motivation for the classification into active and non-active not clear. It somehow assigns a special role of 10% more activity, which seems arbitrary. It also raises a question how the baseline is computed if the images are shown back to back (see above).
- I do not find the evaluation metrics very clear. How are correlations computed (across what and are correlations averaged over).
- In the appendix, the authors show a table with forecasting of unnormalized responses. The scores there are much lower. I do not find the explanations of the authors very clear here. I think this raises a question whether the normalization scheme somehow favors some models. Maybe a visual comparison of of normalized vs. non-normalized responses would help. Or a more detailed motivation for why normalization by the accumulated gradient helps. Also, I do not find this very clear (What gradient? Accumulated over what? Isn’t an accumulated gradient equal to the original signal up to a constant?).

### Questions
- Can you motivate a clear benefit of your choice of your architecture?
- Can you cleaner motivate the choice of the Allen dataset and how you avoid data leakage between training and test? Could you conduct an experiment with completely separate neurons and images in training and test?
- Related: Can you run your model on the SENSORIUM 2022 data to show that it can deal better with unique image IDs?
- Can you provide a better explanation for your normalization scheme and why it improves model performance?
- Can you define how baseline activity is measured given the back-to-back image presentation in the Allen dataset.
- Can you address the potential mismatch between the sparsity motivation and the use of fluorescence data rather than deconvolved or spiking data?
- Can you provide a more detailed explanation of your normalization method, including a clear definition of the "accumulated gradient" and how it is calculated?
Can you conduct an analysis of how the normalization scheme affects different models' performance, to ensure it's not unfairly advantaging certain approaches?
Can you provide a clearer justification why this particular normalization method was chosen?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper suggests to use a transformer to forecast neuronal activity with a focus on mice 2 photon imaged neurons. To tackle the sparse responses, the authors suggest to add quantization and classification loss derived from the quantization. They also try to tackle generalization issue and interpret their learnt neuron tokens.

### Strengths
Relatively original but not very clear paper, with interesting results.
I specifically liked
* A novel technical approach and an interesting idea with quantization, which seems to improve the results.
* The qualitative analysis of cross-former in comparison with Quant-Former (A6-A7)
* The authors made the first steps towards model interpretability, mainly in appendix, which is important for biological research.
* I appreciate attaching the code, this is a huge plus for reproducability

### Weaknesses
 * Incomplete literature review and missing baselines
   * The Zhang et al 2024 work is not mentioned (https://arxiv.org/pdf/2407.14668 ) This work does neuron based forecasting but on neuropixels data.
   * The older works for neuronal forecasting, such as Zhu et al 2022 (https://www.nature.com/articles/s41593-022-01189-0) or Ye & Pandarinath 2021(https://arxiv.org/abs/2108.01210)  are not mentioned and also not used for baselines (Zhu et al 2022 is for calcium data).

While this models do not have stimuli tokens, one of them could still be a competitive baseline. I would also be interested to see the ablation showing the importance of the stimuli tokens for QuantFormer (is it about specific stimuli or stimuli type? )

* Incorrect statement about other works and incorrect citations 
   * line 185  `SENSORIUM (Wang et al., 2023))`. Wang et al., 2023 does not use data from either Sensorium 2022 or 2023 competitions. It also barely discuss the competition
   * moreover, both SENSORIUM 2022 and 2023 provide spike traces data
   * For example, lines 176-177 *all the encoding and decoding methods discussed above rely on spiking data*, while in the mentioned works, Wang et al., 2023 (cited incorrectly though), Sinz et al 2019, Antoniades et al 2023, Turishcheva et al 2024 a/b all use calcium traces. 
   * Same for lines 90-91, both Turishcheva et al 2024 a, and Microns (https://www.microns-explorer.org/cortical-mm3) provide open access to extensive datasets with calcium traces, not spikes.
   * Lines 144-147 *Approaches such as Turishcheva et al. (2024a;b); Li et al. (2023); Xu et al. (2023a); Sinz et al. predict neural responses based on stimuli, but often rely on trial-averaged data and are not designed to forecast future neural activity on a single-trial basis without the use of synchronous behaviour variables, which are not accessible in online settings.* While, indeed these approaches do not do neuronal forecasting, at least three out of four mentioned papers do not rely on either repeats or behaviour for responses prediction, only on the visual stimuli. Adding behaviour indeed improves performance, while repeats are used only during evaluations. 
   * Mentioned  Antoniades et al 2023 work could be used for neuronal forecasting as well 

* The biological validity of the paper is not clear
    * For table 2 it is not clear what are the upper/lower bounds for the metrics, which makes it hard to interpret how good all of the models generally are, as the correlation upper bound could not be one due to significant noise in the biological data. I would inspire the authors to use repeated stimuli within the session and follow Wang et al., 2023 to estimate at least the correlation upper bound.
    * It is also not clear, if the model is actually able to reproduce linear-nonlinear phenomenas, which the neurons should be able to do (like here https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009028 )

* The writing clarity could be improved. 
   * For example,  in section `4.1 DATASET` it would be nice to explicitly write the amount of unique neurons. If the neurons across sessions for the same mice did not repeated, then its 11*3*250 $\approx$ 8500. If I understood the appendix correctly, there were 250 neurons per session on average. If these were exactly same neurons across sessions, it's 11*250 $\approx$ 3000. This makes very different impression compared to the 230 000 traces, which might be understood on neurons.
   * Generalization experiment is not explained (see questions)

### Questions
* How exactly do you perform the generalization experiment? You trained on 10 mice and evaluated on the other one?
But how the neuron-specific tokens were trained then for the test mouse? Also, were this neurons involved during pretraining? If yes, that might compromise the generalizatibility measure, as the model has see this data. What are the generalization ability of other models, like cross-former? Also, how are these numbers averaged? I am also not sure if it is really a good idea to measure generalization training on moving gratings and predicting the static ones as for the neurons ignoring motion this would be very close stimuli.

* Figure 1 states that neuronal forecasting models should take stimuli as input bit based on Figure 2- the model does not take visual stimuli as input but rather the stimulus-specific learnable tokens. Are this token per stimuli or per stimuli category (aka natural images, gratings, etc)?

Minor - 
* In lines 518-519 *2D t-SNE on neuron embeddings (Fig. A-10) revealed that the [NEURON] token encodes neuron-specific statistics like activation probability* - the t-sne plot actually does not separate low and high-activated neurons, especially on the first plot. I would inspire authors to revise this statement
* Lines 369-370 *However, we excluded natural movies, as isolating individual neuron responses is challenging, and spontaneous activity, as it is not stimulus-related.* But how do you isolate spontaneuos activity for other stimuli categories?

### Soundness
2

### Presentation
1

### Contribution
2
