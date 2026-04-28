# Atmospheric Radiation Parameterization by Neural Ordinary Differential Equations and Related Models

- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 1, 3

## Abstract
Radiation parameterization schemes are crucial components of weather and climate models, however, they are known to be computationally intensive. Alternatively, they can be emulated with machine learning (ML) regression models. Mainly vertical energy propagation motivates the usage of ML models featuring sequential data processing. We investigate these and related models for radiation parameterization using atmospheric data modeled within an Arctic region. We observe that Neural ODE performs best in predicting both the long- and short-wave heating rates. Furthermore, we substitute the architecture with its discrete form to boost its efficiency while preserving competitive performance. The practical applicability of the models is studied for different model sizes. Finally, we link the trained neural network to the operational weather forecast model and assessed its performance versus the conventional radiation parameterization.
We receive a speedup of 26.5 times of the radiation steps
without significant loss of accuracy. The proposed parameterization 
emulator dramatically reduces the computational burden and the carbon footprint of weather forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study presents the application of neural networks, particularly Neural ODEs, for surrogate radiation parameterization. It aims to reduce the runtime of radiation parameterization in numerical weather forecasting and enhance overall forecasting efficiency by leveraging the rapid inference capabilities of neural networks. To achieve this, the study approximates the heat transfer process using an ODE with an unknown right-hand side, which is estimated by a neural network. The experiments evaluated the practicality of 25 models across three types, integrating the machine learning model with the real WRF numerical model. Compared to traditional parameterization schemes, the module's runtime improved fourfold, while maintaining consistent prediction accuracy.

### Strengths
1. This work explores the application of a series of neural networks, primarily Neural ODEs, in radiation parameterization, and incorporates RNNs into the WRF model for predictive experiments, achieving practical testing of the neural network parameterization scheme.   
2. The manuscript is clearly written, adheres to formatting requirements, and contains no obvious LaTeX errors.    
3. The algorithm design follows the physical principles of radiation parameterization, successfully integrating data-driven approaches with physical information.

### Weaknesses
 1. **Method Description**: The explanation of the method selection could be more thorough. It would be beneficial for the authors to elaborate on the specific advantages of Neural ODE in its application for this radiation parameterization task compared to other ML methods. Additionally, I encourage them to clarify how the parameterization substitution task differs from standard regression and ODE fitting tasks in terms of unique challenges or requirements. It might also be worth considering why well-known and high-performing architectures like neural operators and ResNet were not included as baselines in this study. I encourage the authors to explain their rationale for selecting the baseline models they used and to clarify whether they considered including these popular architectures.

2. **Experimental Analysis**: The experimental analysis would benefit from further clarity and depth. Although the study evaluates 11 architectures across three categories and compares their accuracy, further exploration of the results is necessary for a complete understanding. I encourage the authors to provide a more detailed analysis of the performance differences between architectures, particularly for the RNN and Neural ODE models in shortwave and longwave predictions. Additionally, a discussion of potential reasons for these differences based on the characteristics of each architecture and the nature of the prediction tasks would greatly enhance the overall analysis.

3. **Significance**: In the final WRF joint experiment, the choice to use a profile-wise convolutional RNN instead of Neural ODE raises an important question about the significance of the findings. It would be helpful for the authors to clarify their reasoning for selecting the RNN model for this experiment, particularly given that Neural ODE is discussed as a key focus of the paper. If the choice of RNN, is primarily to demonstrate that profile-wise machine learning parameterization schemes (like Neural ODE and RNN) are superior, this seems less novel, as prior work[1-3] has already established similar conclusions without framing them as profile-wise methods.

### Questions
1. Would it be possible to provide a clearer theoretical justification or explanation for the viewpoint that the profile-wise convolutional RNN is a discrete substitution of the Neural ODE? What are the advantages of Neural ODEs when handling regular (discrete) time data?

2. Given that GRUs are an enhancement of RNNs, could you clarify why they are not suitable for profile-wise type experiments?    

3. In lines 221 to 222, could you provide a more detailed explanation of the "Spatial grid"? I noticed that Figure 2 only illustrates random location nodes.    

4. Regarding the selection of the test set mentioned in line 237, is there a temporal uniformity in this selection? Considering the variations in day-night cycles and seasonal changes in polar regions (line 223), how might this impact the selection?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Intercomparison study of multiple neural network architectures to replace radiative transfer parametrizations inside WRF. They find an RNN to be best based on test data and then couple it to WRF via a Fortran-C++ bridge and find a 4x speed up (of the parametrization scheme) at a loss in accuracy of ~1K in surface temperature.

### Strengths
1) Many baselines are compared
2) The final model is coupled to the WRF model
3) Experiments should be reproducible as code is available and technical details are mentioned in the text

### Weaknesses
1. The loss in accuracy relative to the gained speed up seems too high. Fig. 5 and 6 give a first indication of this. The emulated parametrization can differ significantly from the original one, which would render the speed up not useful. The reported 1K difference in surface temperature is substantial and raises concerns about the practical applicability of the emulator. A more detailed analysis of the spatial and temporal patterns of these errors is needed to understand where the emulator struggles most.
2. Robustness of the models is not assessed. If the proposed emulator is to be used in WRF, it need to be applicable under a wide variety of input combinations. However, this study only considers a very limited study region in high northern latitudes during only a small time period (2015-2016). Moreover, this limitation is not meaningfully discussed. As is, I suspect the parametrization would have significantly decreased skill in most real-world applications and could potentially even be catastrophically wrong (e.g. unphysical). The lack of testing on diverse atmospheric conditions and geographical locations makes it difficult to assess the generalizability of the proposed approach. For example, the model's performance under different cloud regimes, aerosol concentrations, or surface albedos is not explored.
3. There is limited technical novelty in the contribution which makes the work less interesting to the broad readership of ICLR. More specifically, all neural network architectures studied in this work have been previously used, the dataset has been introduced in a different study (Yavich et al. 2024), the concept of emulating radiative transfer has been widely studied and the empirical results are not ground breaking. The specific architecture choices and training procedures do not appear to introduce any novel techniques or insights into the problem of radiative transfer emulation.
4. Many figures could be improved: reduce white space on the sides, use consistent fonts and font sizes, think about what you want to convey with a figure and then think about how to make this message most easily accessible for the reader. The current figures are not optimized for clarity and could be more effective in conveying the key findings of the study. For example, the color scales and axis labels are not always clear and consistent.
5. Many abbreviations not introduced, e.g. SW, LW
6. The tables are difficult to grasp and do not seem to have a clear message, but instead are conveying that many models have been compared and one of them turned out to be best in some cases. Also, what does bold face mean in the tables?
7. Section 2 contains lengthy descriptions of different methods, however it remains unclear how they contribute to the overall story of the paper. The descriptions of the various neural network architectures and training procedures are not well-integrated into the main narrative of the paper. The relevance of each method to the final results is not clearly explained.
8. While the study compares many baselines, it does not compare to any previously published emulators of radiative transfer schemes, which makes it difficult to assess how good the reported metrics are. The lack of comparison to existing state-of-the-art emulators makes it difficult to contextualize the performance of the proposed approach.
9. While reporting RMSE is important, it would be good to also evaluate additional metrics, especially those that give an indication about absolute skill levels, e.g. R^2 or relative RMSE (normalized by variability of targets). The exclusive reliance on RMSE does not provide a complete picture of the model's performance. Additional metrics are needed to assess the model's skill in capturing the variability of the target variables.

### Questions
What kind of study do you intend to do with this model, that the 4x speed up in the radiative transfer parametrization scheme is necessary to make them feasible?

The main goal of this paper seems to be the speed up. However, since you only achieve a speed up at a loss in accuracy it would be important to understand this trade-off in detail. In other words, can you draw a pareto frontier showcasing the loss in accuracy vs. the gain in speed up of multiple models? Ideally with a metric that also allows to assess the accuracy of the original parametrization scheme in WRF?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This study uses a broad range of ML models to create emulators to represent radiative transfer in climate models. Radiative codes are one of the biggest bottlenecks in climate models. Often, radiative schemes reply on large lookup table which are hard coded into climate model fortran code. Even the most modern radiative transfer schemes do not take the full absorption band into consideration and at best rely on idealized absorption in a handful of discrete absorption bands.

The study uses a broad range of ML models, including CatBoost, Neural ODEs, CNNs, GRUs and their polynomial activation counterpart to (1) assess the performance of different architectures in emulating radiation, and (2) plug the best scheme into a regional climate model and assess speedups offered by an ML scheme as opposed to a traditional parameterization

The authors use observations in and over the Pechora Sea region for two years. One year is used for training and one year is used for testing.

More importatly, the architectures are chosen in a physics-inspired way and are categorized into three categories: point-wise (one level input used to prdict one level output), profile-wise (full vertical profile used to predict the full vertical profile) and sequential (using a sequential model like RNN to iterate and solve the radiative flux forcing at each vertical level starting from the boundaries).

The scheme with the least error is embedded into the WRF regional model and if found to provide a 4x speedup in model runtime. This testifies to the effectiveness/potential of ML models to improve traditional physical parameterizations.

### Strengths
The study correctly identifies the importance of radiative transfer for climate models and the fact that radiative codes form a major bottleneck in climate models. The idea that ML can solve this computational deadlock has been known for a while and some works mentioned in the study have also shown some preliminary progress in this direction.

The study has also identified a broad range of models and their appropriate application consistent with the problem domain. Single level prediction is treated as a regression and thus framework like CatBoost has been employed. Profile-wise prediction has been accomplished using multiple models including CNNs, RNNs, Neural ODEs, and polynomial networks. Lastly, inspired from vertical energy propagation, sequential algorithms like GRUs and continuous-time liquid neural nets are used for layer-by-layer prediction.

### Weaknesses
The study appears to fall short on multiple fronts:

1) Novelty: Apart from speedup in radiation emulation, the novelty of the work is not clear to me, since the central idea behind the work has been present by past papers and the paper pretty much uses established neural networks in their out-of-box configuration to emulate radiaton. Moreover, the authors have exhaustively used 19-20 different models of 10-11 different types. These models have not been explained in much detail (which is fine), and also the physical intuition behind simply using these many models is not clearly evident to me. If the focus is just Neural ODEs (as is the title of the submission), why not just compare it to one or two optimal baselines from past studies? I don't see any point in mixing it all up with 20 different types of models? This point is more so relevant as (to my understanding) the Neural ODE model wasn't even eventually coupled with WRF.

2) Clarity: The paper is big on breadth but not on depth. Due to this, reading this paper was a bit of a struggle as the focus has been on introducing the different architectures, and not on why they would work and others would not. Such an interpretation is likewise lacking from the results and discussion section as well. This goes back to my first point that the focus on breadth than depth makes me wonder about the novelty of the work and how it adds value to being accepted at ICLR. Most strikingly, the authors finally choose RNN 64,3 to couple to WRF, but the errors for that model have not been discussed in Table 3.

3) Lacking schematics: It would have been great if the authors would have provided detailed schematics of the main architectures used. for instance, I found figure 1 to be quite nice and I am sure I would not have been able to understand the distinction between the categories without it. For instance, what merits are obtained by choosing both ODEGRU and Liquid Neural networks, and is there solid evidence that polynomial networks might outperform relu activation based models? Or have they been used merely for intellectual curiosity?

### Questions
My questions are more or less integrated with the weaknesses stated above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
It employs the Neuralode method to perform the Atmospheric Radiation Parameterization task.

### Strengths
It will be exciting to see the application of machine learning models in the field of science.

### Weaknesses
This work doesn't seem suited for ICLR, as it primarily appears to apply standard ML modules to AI4Science tasks. While it may perform relatively well in weather forecasting, it lacks novel insights for the ML community. The methods used are previously published and, although adapting an existing method from A to B could reach the level of a Nature/Science paper, it doesn't meet my standards for ICLR: 1 Typically, the main contribution should lie in the methodological design, incorporating modifications based on the specific problem at hand. The comparison should focus on SOTA methods to highlight its novelty. Pursuing SOTA isn't our sole objective; however, comparing only with outdated work makes it difficult to assess the novelty of the proposed method. I can't conduct all the related work and baseline studies independently.
2. If an existing method from area A is applied to area B, it should truly surprise people, as such transfers are generally not considered easy.

I believe this work falls short in both aspects.

### Questions
1.Why not submitting this work to a weather-related journal?
2.Could you elaborate on how you suggest the community learn from your study, beyond the application of neural ODEs in weather forecasting? Additionally, are there any recent works on this topic, aside from basic ML baseline methods discussed here? If so, please include them for comparison. If not, could you explain why? Is the field too niche, or is applying ML to this problem particularly challenging?

### Soundness
2

### Presentation
2

### Contribution
2
