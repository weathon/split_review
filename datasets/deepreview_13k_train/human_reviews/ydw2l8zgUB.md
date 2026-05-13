# EEGTrans: Transformer-Driven Generative Models for EEG Synthesis

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Recent advancements in Large Language Models (LLMs) have been significant, largely due to improvements in network architecture, particularly the transformer model. With access to large training datasets, LLMs can train in an unsupervised manner and still achieve impressive results in generating coherent output. This study introduces a transformer-based generative model, EEGTrans, designed for sequentially generating synthetic electroencephalogram (EEG) signals. Given the inherent noise in EEG data, we employ a quantized autoencoder that compresses these signals into discrete codes, effectively capturing their temporal features and enabling generalization across diverse datasets. The encoder of EEGTrans processes EEG signals as input, while its decoder autoregressively generates discrete codes. We evaluate our method in a motor imagery Brain-Computer Interface (BCI) application, where merging data across datasets is particularly challenging due to experimental differences. Our results demonstrate that the synthetic EEG data effectively captures temporal patterns while maintaining the complexity and power spectrum of the original signals. Moreover, classification results show that incorporating synthetic data improves performance and even surpasses that of models based on Generative Adversarial Networks. These findings highlight the potential of transformer-based generative models to generalize effectively across multiple datasets and produce high-quality synthetic EEG signals.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This manuscript describes a vector-quantization-based autoregressive transformer as a generative model for EEG. They use their generative model to generate synthetic data for EEG classification tasks. Results show that using the real data and the synthetic data with an auxiliary loss slightly outperforms using only the real data on motor imagery decoding tasks.

### Strengths
* applies commonly used, yet fairly recentnovel deep learning methods from other fields to EEG, where they have not been used as much
* supplies code
* overall approach probably makes sense (even though have not fully understood it)

### Weaknesses
I found the way how actually the synthetic data is generated hard to understand and may still not have fully understood it. This should be more clearly described early on I am still confused about it.

Some of the writing I found vague and therefore hard to read, e.g. first sentences "Large language models (LLMs) have been extensively utilized across various scenarios due to their powerful model characteristic: the generative models. These models are not restricted to producing specific forms of output; instead, they can generate output in any form" I found these sentences mostly confusing.

It is unclear to me how the authors split the data into training and test, I think they did not follow official train/test splits of the datasets? Did not see this information, maybe I missed it.

Also, there are of course a lot of existing works on those data that should be compared to, and for this it is also necessary to check and align the train/test split with those works and to also mention their performances.

Average power spectra (e.g., for all trials fo one subject) for synthetic and generated data should be shown to assess quality of generated EEG.

### Questions
As written, still do not understand how data is exactly generated for the classification tasks. Can you try to explain it very concisely?

Also, what train/test splits did you use? In the different training stages (generative model training, classifier training etc.)

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors proposed EEGTrans (Encoder - Decoder) based architecture for generating synthetic EEG datasets. It is useful, as collecting EEG data is a human subject-dependent and time-consuming process. Authors evaluated on multiple motor-imagery datasets after downsampling them to 128 Hz.

### Strengths
The paper used Transformer architecture to generate synthetic EEG. The idea is not novel as there have been previous attempts on this, however the problem is not well studied. Thus utilising transformers seems a reasonable attempt at testing the capability. 
They Validated on multiple datasets.

### Weaknesses
There have been other methods where authors used GPT-based architecture to claim a foundation Model: "Neuro-GPT: Towards A Foundation Model for EEG". There is another paper "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers" for time series data -  The authors should have evaluated that.

There should be more details on architecture, and optimisation. The authors explained for EEGTrans but for CycleGAN approach, I couldn't find the information on layers/number of parameters/etc. There is some information in the appendix but still not complete.
I would encourage authors to include maybe clear architecture diagram for both in the main text, so it is easier to compare and understand the implementation.

Additionally, There is an extreme weakness in the paper related to evaluating synthetic data. The authors didn't perform standard evaluations like PSD, STFT, activation in alpha and beta bands, or source analysis. Averaging all the subjects doesn't distinguish activations.

There are 5 datasets for evaluation: Only 1 dataset is there with 1 subject and 128 Hz sampling. Why use that dataset to bring the other 4 datasets with higher resolution and number of subjects to 128 Hz? Maybe let go of that dataset and deal with 250 Hz, as we have tried over the years to have higher sampling and temporal resolution for these datasets 

In paper, I have seen repetitive occurrences stating the same stuff, authors can reduce that, to add more information in main text. ex:
"Visual inspection indicates that EEGTrans produces higher-quality synthetic data compared to CycleGAN. It is evident from the
visual comparison that EEGTrans’s generated data is significantly superior". 

another Line [493]The BCI Competition IV Dataset 2a was collected some time ago] - "some time ago" really? We can say, 2a was collected in 2008 and HGD was in 2017. However the may statement is speculative in nature, so authors can point towards noise/interference due to room/environment. 

Line [534] : "This method produces high-quality synthetic data that enhances downstream classification tasks." - If you only intended for classification (only one downstream), just train a classification model utilizing transformers?

### Questions
This paper will need a lot of work, to perform all the experiments and evaluate the synthetic EEG Data.

Can the authors perform simple group-level beamformer source analysis for both real and synthetic data?

Additionally Time Frequency plots for beta power changes in case of motor imagery for both generated and real data?

Can we get some loss plots for the training and fine-tuning?

Line [318-320] "We focus on three channels commonly used in motor imagery experiments, and two epochs are shown to allow us to confirm the robust performance of EEGTrans across different channels and multiple epochs." - which 3 channels - c3, c4, cz?

Line [416]"As shown in Table 2, only EEGTrans closely matches the ground truth (real data) with minor differences, retaining high sample entropy and thus indicating high complexity and variation. However, it does not retain high-frequency components, which is evident in the spectral entropy. " - Can we have some statistical comparison?

Line[463]"Table 3 shows the classification accuracy achieved through various approaches: using only real data, only synthetic data, combining real and synthetic data, and incorporating real data with synthetic data along with auxiliary loss. For a comprehensive analysis, we employ five-fold cross-validation instead of the original train-test split used in the competition." - How did you do 5 fold cross- validation? What was your distribution of the test and validation set, or it was simple 80 -20? Since it's already a competition dataset, why did you choose to do cross-validation and not cross-session analysis?

Can you also do inter-subject analysis?

Is it justified to benchmark against cycle gan for non-stationary time series data?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes the transformer-based EEG generative model, namely EEGTrans, to synthesize EEG data based on multiple datasets. The model used the RVQ autoencoder to train the discretize the EEG signal and build the codebook to represent EEG tokens. Then EEGTrans can model the generative task as a next-token prediction task in an auto-regressive manner just as what a language model is doing and then the RVQ decoder can generate the EEG signal similar to the real data. Experiments confirms the similarity by comparing the spectral entropy and sample entropy. Further experiments confirms that with these synthetic data as augmentation, a model can achieve better results on the target BCI dataset.

### Strengths
1. The general idea is taken from the language model, thus the overall methodology is reasonably backed up with empirical results, and is still novel in the EEG synth task. 
2. The experiments demonstrate their superior performance compared to a classic method CycleGAN. 
3. The overall presentation is good. The authors clearly conveys their ideas.

### Weaknesses
First of all, I have to mention that the key research problem of the EEG synthesis is not "what is the best method to generate the synthetic EEG data", but "why do we need to generate the synthetic EEG data". The paper answers this question in the most common way, which is to use these data as augmented data to improve the performance on a specific downstream task (and in this paper the BCI motor imagery task). From this point of view, the scope of the contribution of this paper will be limited to getting improved synthetic EEG data for data augmentation rather than extending our understanding for this area. 

The above statement is actually not the weakness of this paper. I like paper that won't overclaim but focus more on concrete things. However, starting from it, there will be the following concerns about the paper. 
1. It's unclear to me whether the label needs to be generated together with the EEG data. If so, the usage of the synthetic dataset seems to be limited to highly related tasks and the claimed cross-dataset advantage will be weakened.
2. If the synthetic data is used to boost the performance of downstream tasks, then how does it perform compared to more common but simple data augmentation methods like cropping and concatenating EEG fragments, jittering, etc.? It lacks such justification. 
3. If the synthetic data is claimed to integrate information from different datasets, then how should we compare this paradigm to a more common paradigm where model such as LaBraM will integrate information in the hidden representation space? This alternative paradigm can boost the performance of downstream tasks with unsupervised training on unlabeled EEG data, which can integrate information from more diverse dataset. 

There are also some comments on the methodology: 
1. EEGTrans doesn't take the relationship among channels into consideration, and doesn't evaluate the cross-channel reconstruction quality.
2. The role that the next-token prediction plays in the proposed method is unclear and unverified. See the questions for more details.

### Questions
1. Does the next-token prediction converge well? I'm curious about how well the next-token prediction would work. Do you have a test set to verify the next-token prediction process? If there is the test set, how well can the model correctly predict the next token? Maybe reporting metrics like perplexity will help. 
2. Following Question 1., it's possible that the model is simply yielding EEG data from the trained dataset (with some kind of bias on frequency as described in 4.5). If so, the model will be downgraded to merely replicate an existing dataset and use it to other datasets.
3. While the model is called EEGTrans, taken the name from transformer, I feel the RVQ plays the most important role for synthesizing realistic EEG data. So what if we use the discretization method such as RVQ, but do not use the auto-regressive manner to train a transformer model? For example, one can actually combine VQ with CycleGAN to also generate good-quality EEG data.
4. I'm not sure whether it is my problem, but when I'm trying to visit the link to the code in the abstract, it tells me that "The repository is not found."

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposed a transformer-based generative model, EEGTrans to autoregressively generate EEG data based on the input sequence. The proposed model was evaluated against CycleGAN and achieved more accurate 'prediction' or generation of future segments.

### Strengths
1. the structure of the paper is good and clear
2. the method section was clearly described and the figure 2 is informative.
3. the source codes are provided to facilitate reproduction

### Weaknesses
1. The model was trained for next code prediction which means the proposed method is more of a EEG signal 'forecasting' or 'prediction' rather than generation for data augmentation purpose. Therefore, the introduction and problem setup is miss aligned.
2. For synthetic data generation to facilitate training in a new dataset, both the reality and the diversity of generated signals are important. In a typical GAN or Diffusion setting, new signals can be generated or sampled from a random vector sampled from the normal distribution during inference to achieve diversity and variety. However, in the proposed method, it seems like there is no sampling process for diverse signal generation, so how can the proposed method augment the target dataset?
3. There are GAN-based method for EEG that can directly generate the raw signal which should be added into comparison. For example, EEG-GAN.
4.The language used in section 4.7 is very vague, for example, 'Dataset 2a was collected some time ago', 'the synthetic data likely does not retain subject-specific information', 'the classifier should yield very similar output'. These claims need to be justified better for example, providing a tSNE plot to show the generated data vs the real data, and the target classes vs the subject to demonstrate there is no subject-specific information. 
5. Why not use MSE as a performance metric since the method is 'predicting' the future segment?
6. The use of GAN to replace the Transformer module as baseline for next coder prediction task should be justified better.

### Questions
1. The EEG signals have high variations between subjects and between datasets, how are these addressed in this work? Is the generation subject-dependent?

2. The generation quality of the proposed will also be largely dependent on the RVQ AE, which added additional complexity to train and tune, any comment on this?

3. What are the real-world applications for the proposed method? It seems like in-order to generate synthetic data for a new target dataset, you still need to use real data as input. It is very rare that we only collect 'the first half of a trial' in BCI experiments.

4. For auto-regressive generation, how does the 'prediction' performance decline with respect of length?

### Soundness
2

### Presentation
3

### Contribution
2
