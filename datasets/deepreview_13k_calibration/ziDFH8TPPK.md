# Long-Term Typhoon Trajectory Prediction: A Physics-Conditioned Approach Without Reanalysis Data

- Decision: Accept
- Avg Score: 6.25
- Scores: 3, 6, 8, 8

## Abstract
In the face of escalating climate changes, typhoon intensities and their ensuing damage have surged.
Accurate trajectory prediction is crucial for effective damage control.
Traditional physics-based models, while comprehensive, are computationally intensive and rely heavily on the expertise of forecasters.
Contemporary data-driven methods often rely on reanalysis data, which can be considered to be the closest to the true representation of weather conditions.
However, reanalysis data is not produced in real-time and requires time for adjustment because prediction models are calibrated with observational data.
This reanalysis data, such as ERA5, falls short in challenging real-world situations. Optimal preparedness necessitates predictions at least 72 hours in advance, beyond the capabilities of standard physics models.
In response to these constraints, we present an approach that harnesses real-time Unified Model (UM) data, sidestepping the limitations of reanalysis data.
Our model provides predictions at 6-hour intervals for up to 72 hours in advance and outperforms both state-of-the-art data-driven methods and numerical weather prediction models.
In line with our efforts to mitigate adversities inflicted by \rthree{typhoons}, we release our preprocessed \textit{PHYSICS TRACK} dataset, which includes ERA5 reanalysis data, typhoon best-track, and UM forecast data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a framework for data-driven typhoon prediction based on cross-attention between encoded representations of the past trajectory points as well as global weather data (geopotential and wind directions). The paper shows good results in forecasting the typhoon trajectories, especially compared to physics-based baselines.

### Strengths
Overall I believe that the paper has great potential for presenting an interesting case study with strong empirical results on this important problem, but in its current form the lack of clarity and details for better understanding the study are severe issues.

- The results seem strong and quite significant gains over physics-based baselines (coming from various meteorological institutions) are reported. I am not familiar with the typhoon track forecasting literature though.
- Open-sourcing the data will be valuable. When doing so, the authors should put care into making it easily accessible and well-documented
- Training on NWP data such as UM instead of ERA5 is a good study to make but has limited originality.

### Weaknesses
 - Clarity can be improved significantly. Firstly, there are a lot of grammar mistakes worth fixing with a grammar checker. Secondly, many implementation details are conveyed very unclearly or details are missing. This inhibits understanding the significance of the paper and would hurt reproducibility. For example:
    - The method seems to have been tested using a GAN, a CVAE, and a diffusion model, but implementation details are largely lacking. It's unclear what architectures were used for each, what the loss functions were, how the latent spaces were structured, and what specific training procedures were adopted.
    - Unclear meaning and implementation details of *"so it is matched through the latitude and longitude mapping and the interpolation method"*. It is not clear what this matching process entails, what interpolation method is used (e.g., bilinear, nearest neighbor), and how the different resolutions are handled during the matching process.
    - Unclear what exactly the *"ensemble method"* refers to and how exactly it is performed in practice for all the models. Is this a simple averaging of predictions, or is there a more complex weighting or combination scheme? The lack of detail makes it impossible to assess the validity of this approach.
    - Please include more ablations, e.g. with UM and joint training and bias-correction but without pre-training. The whole ablation study section is a bit hard to understand and should be expanded (in the appendix if needed). It's not clear what the different ablation settings are and what the purpose of each setting is. For example, what is the effect of removing the bias correction step, or what is the effect of using only UM data without pre-training?
- Are the baselines in the first set of rows of Table 2 (e.g SocialGAN) all off-the-shelf pre-trained human trajectory prediction models? If so, it is not surprising at all that they perform so badly, and it would be good to retrain them on your data. Additionally, why is Ruttgers et al. not included in the benchmarking?

### Questions
- First sentence of methods section: 1) There is no index *i* for none of the variables (e.g. it should be $c_i$, I think); 2) $t_p$ is the input sequence **length** (not the input sequence). Similarly for $t_f$; 3) $p$ is given different meanings for $C_p$ and the pressure levels $p \in P$. This is confusing, can you use different letters, please?
- Why are geopotential height and wind vectors inputs taken from the output timesteps $i=t_p+1, \dots, t_p+t_f$? Should it not be $i=1, \dots, t_p$?
- 3.1 Preliminaries (not preliminarily)
- Tone down "is too large scale to train a model from scratch". There exist models trained from scratch on ERA5...
- "$\tilde X$ is the forecasting values for ERA5 from time $t$ to $t+t_f$". Shouldn't it be $t+1$ to $t+t_f$?
- I don't completely understand how the bias correction phase works, is the UM data matched with ERA5 based on the timestamp?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the Long-Term Typhoon Trajectory Prediction (LT3P), a novel approach for real-time typhoon trajectory prediction without the need for reanalysis of data. LT3P is a data-driven model that utilizes a real-time Numerical Weather Prediction (NWP) dataset, making it unique in its field. The model is designed to predict the central coordinates of a typhoon, eliminating the need for additional forecasters and algorithms. LT3P is accessible to various institutions, even those with limited meteorological infrastructure. The paper includes extensive evaluations, demonstrating that LT3P achieves state-of-the-art performance in typhoon trajectory prediction. However, the model is currently applied only to typhoons and has not been tested on other types of tropical cyclones. The authors plan to extend its application in future work and contribute to the field of climate AI by releasing their dataset, training, test codes of LT3P, and pre-trained weights to the public.

### Strengths
- Innovative Approach: LT3P is one of the first data-driven models for real-time typhoon trajectory prediction that utilizes a real-time NWP dataset, distinguishing it from other methods in the field.

- Extensive Evaluations: The paper includes comprehensive evaluations, showcasing the model's state-of-the-art performance in typhoon trajectory prediction.

- Contribution to Climate AI: The authors plan to release their dataset, training, test codes of LT3P, and pre-trained weights to the public, contributing valuable resources to the field of climate AI.

### Weaknesses
 - Limited Application: The model has only been applied to typhoons and has not been tested on other types of tropical cyclones, limiting its current applicability.

- Dependence on Real-Time NWP Dataset: The model's performance is dependent on the availability and accuracy of the real-time NWP dataset, which could be a potential limitation.

- Need for Future Work: While the paper outlines plans for future work, including extending the application to all kinds of tropical cyclones, these aspects have not yet been addressed or tested.

### Questions
- How well does the LT3P model generalize to different regions and conditions of typhoon occurrences? Have there been any specific challenges in adapting the model to various geographical locations?

- Could you provide more insight into why LT3P outperforms other state-of-the-art models and established meteorological agencies’ predictions? What specific features or methodologies contribute to its superior performance?

- How does the dependency on real-time NWP datasets affect the model’s performance, especially in scenarios where real-time data might be sparse or inaccurate?

- How does the LT3P model handle uncertainties in typhoon trajectory prediction, and what measures are in place to ensure the reliability of its predictions?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This paper proposes a encoder-decoder type weather prediction model, focusing on the typhoon trajectory prediction. 
- A notable point is the use of two different reanalysis data. A precise but slow-to-retrieve ERA5 data is used to pretrain the encoder-decoder module. A rough but fast-to-retrieve UM data is then used to fine-tune the encoder-decoder, as well the trajectory predictor. 
- Reanalysis data is usually used only for off-line training, However, the UM data is known fir its quick release (3 hours after observations),  one can use the UM for computing the ERA5-like embedding for precise trajectory prediction. 
- Enables 72 hours ahead prediction based on a UM reanalysis data.

### Strengths
- It is novel to use re-analysis data for a prediction (inference) phase. This can change the possible applications of the reanalysis data, usually used for offline computations only. 
- An error correction scheme to utilize the quick but erroneous UM reanalysis effectively sounds interesting.

### Weaknesses
 - If I read correctly, several explanations about network architecture, losses, ... are missing. This would prevent the re-production by fellow researchers.
  * Number of layers, embedding dimensions, total amounts of learnable parameters, ..
  * L_{trajectory} not defined?

- The reported quantitative results In the Tables are surprisingly good. However, I have the following concerns.
  * Inconsistent trends of the scores of existing (compared) models. As I read the MGTCF paper, the authors reported that the MGTCF performs clearly better than SGAN, which is different from Tables 2, and 3.
  * The scores (Distance) of the proposed LT3P update the current SotA by order of magnitude. I checked the most recent works such as (Bi+ 2023, Lam+ 2022) but the distance scores are roughly in the same order as the existing methods. I feel the current manuscript does not sufficiently explain why this huge jump happens, although the ablation study tells that it seems the joint training with reanalysis is a key factor.

### Questions
I'm a little bit confused about how to handle the "Lead time" in evaluations in a fair way. 

The manuscript says that one needs to wait for three hours to obtain the UM reanalysis data. This means the proposed method loses the lead time of three hours. So, the score of "6-hour leadtime" should be understood as "3-hour leadtime"?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new data-based model for typhoon trajectory prediction, using current and passed typhoon locations as well as unified model (UN) pressure and wind maps.

### Strengths
The paper is interesting for both its application results compared to state-of-the-art, and also presents an interesting methodological framework. Indeed, getting rid of reanalysis data (which are not available in real time) is an important asset. The way to do so, first by learning the prediction of the physic variables maps using reanalysis data (which has more history than UN maps, and is also more precise), then to combine using a cross-attention both 'corrected' UN prediction with trajectory prediction, seems to give very good results.
I think this paper would fit at ICLR, yet I have some questions which I would like to know the answer, and also a proofreading should be performed.

### Weaknesses
1) The study is limited to one region, as it looks that the UN map has a fixed latitude and longitude values. How was it chosen, what if typhoons are in the borders, or even going outside? It also means that your model can't easily be applied on other regions? It would be important to understand the limitations of this fixed region, and if the model could be adapted to other regions without retraining from scratch. The authors should discuss the implications of this choice on the generalizability of their approach.

2) Since real-time computation is the goal, it would be important to give computation times values. The authors should provide a breakdown of the computational cost, including training and inference time, and specify the hardware used. This is crucial for assessing the practical applicability of the proposed method.

3) It is not clear how the 'probability cones' are obtained: stochasticity is mentioned only in the result part, not in the method. The method section should clearly explain how the stochasticity is introduced in the model and how the probability cones are generated. Is it through a sampling process, or a direct estimation from the model's output? This needs to be clarified.

4) I understand that the number of data is limited, but I would like to know if a validation set was used to fine-tune the hyper-parameters or if it was done using the 2019-2021 years. Please explain better. The authors should specify the exact split of the dataset into training, validation, and test sets, and explain the rationale behind this split. The hyperparameter tuning process should also be detailed.

5) Finally, it would be interesting to see one of the 'worst' cases also in Figure 3, with a comment on it. This would provide a better understanding of the model's limitations and failure modes.

6) Many typos are present, see below.

### Questions
cf. section 'weaknesses'.

Q1) in your state-of-the art comparison, which one uses UN, which uses only trajectory information?
Q2) how come the Bias-corrected is sometimes better than ERA5 only? Any insights?
Q3) Could you comment a bit more on the Figure 4? it looks like the bias-correction is actually losing the details, just fitting better to the distribution of the ERA5. Maybe there is more to see? The values (SSIM, mean) are not very convincing.
Q4) How many different typhoons are used in the training set?
Q5) Figure 1: what is the scale of the image? how many km (or give the lat/lon) in both directions?

Minor comments/grammar/typos:

- p. 2 'the UM' --> not yet defined (except Abstract)
- 'But, it is not without the drawbacks.' sentence issue
- 'while the UM data has only a 3-hour delay compared to ERA5' --> not clear: is it 3 hour less than ERA5? 
- LSTM, MLP, ... not defined acronyms
- 'on a conservation laws'
- 'hyperparameters & a architecture'
- 'The ERA5 dataset has been accumulated at 6-hour intervals from 1950 to the present, and is too large scale to train a model from scratch. It is computationally inefficient to search optimal hyperparameters & a architecture for trajectory predictions.' --> not clear.
- what do you mean by 'this architecture is computationally efficient when training with large-scale ERA5 dataset?
- (6) L_trajectory is not defined.
- 'and use it as our backbone architecture' --> we missing?
- in Evaluation Metrics, MID not defined.
- Fig 3 : we are viewing probability cones? It is not clear
- 'bais-corrected'
- ssim: not defined

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
