# From Rest to Action: Adaptive Weight Generation for Motor Imagery Classification from Resting-State EEG Using Hypernetworks

- Decision: Reject
- Scores: 1, 5, 3, 3

## Abstract
Existing EEG-based brain-computer interface (BCI) systems require long calibration sessions from the intended users to train the models, limiting their use in real-world applications. Additionally, despite containing user-specific information and features correlating with BCI performance of a user, resting-state EEG data is underutilized, especially in motor imagery decoding tasks. To address the challenge of within and across-user generalisation, we propose a novel architecture, HyperEEGNet, which integrates HyperNetworks (HNs) with the EEGNet architecture to adaptively generate weights for motor imagery classification based on resting-state data. Our approach performs similarly in a Leave-Subject-Out scenario using a dataset with 9 participants, compared to the baseline EEGNet. When the dataset size is scaled, with 33 participants' datasets, the model demonstrates its generalisation capabilities using the information from resting state EEG data, particularly when faced with unseen subjects. Our model can learn robust representations in both cross-session and cross-user scenarios, opening a novel premise to leverage the resting state data for downstream tasks like motor imagery classification. The findings also demonstrate that such models with smaller footprints reduce memory and storage requirements for edge computing. The approach opens up avenues for faster user calibration and better feasibility of edge computing, a favourable combination to push forward the efforts to bring BCIs to real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In this paper, the authors proposed a HyperEEGNet architecture by combining the conventional HyperNetwork and EEGNet to adress cross-user variability for MI-BCI systems. The authors compared the performance of the proposed HyperEEGNet with that of competing EEGNet on various publicly available MI-EEG datasets in both cross-session and cross-user conditions.

### Strengths
This study try to address the important issue of cross-user variability and BCI illiteracy issues in the MI-EEG analysis by adopting the ability of HyperNetwork to adaptive weight generation to learn user-specific representations.

### Weaknesses
There is no substantial innovation in proposed method combining the conventional HyperNetworks and EEGNet. 

The performance improvement of the proposed method over existing EEGNet has not been consistently demonstrated across multiple datasets. This is, the proposed model achieved improved performance on the Dreyer et al. dataset, while its performance degraded on the BCI Competition IV IIa dataset. Furthermore, there has been no meaningful discussion about these conflicting results.

No comparisons were conducted with existing state-of-the-art methods that have addressed the subject variability issue.

### Questions
The proposed model, which simply combines existing HyperNetwork and EEGNet, lacks substantial innovation. In addition, it is difficult to confirm the advantages of the proposed model from comparative experiment results as the performance improvement of the proposed method has not been consistently demonstrated across multiple datasets. This is, the proposed model achieved improved performance on the Dreyer et al. dataset in Table 1, while its performance degraded on the BCI Competition IV IIa dataset in Table 2. Furthermore, there has been no meaningful discussion about these conflicting results.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper aims to show the benefits of using a HyperNet architecture to improve the generalization capabilities of EEGNet for generalization given a large dataset. The authors also use data from the resting state before a trial as a novel input for motor imagery classification.

### Strengths
The paper is original in that they apply a HyperNet architecture to improve the generalization capabilities of an EEG motor imagery classifier. The paper evaluates inter-subject and inter-session performance, which are both important metrics for deployment of a BCI. The authors are fairly clear in how experiments are done, although I had some questions about intersession evaluation for the BCI IV IIa dataset. The work is significant in that a new method is evaluated on EEG data and shows strong generalization performance in a dataset with 42 subjects.

### Weaknesses
1. Claims on the strength of HyperNet + EEGNet would be improved through using a more comprehensive evaluation on the Dreyer et al. dataset. Leave-N-subjects-out train-test split should be done where around a quarter of the subjects are used as test subjects each time. Specifically, the current 5-fold cross-validation does not adequately demonstrate the generalization capability of the proposed method across different subjects. A more rigorous evaluation would involve training on a subset of subjects and testing on a completely held-out group, repeated multiple times with different subject groupings to provide a more robust estimate of inter-subject performance.
2. The HyperNet + EEGNet approach does not seem to work for the BCI IV IIa dataset (one of the two datasets tested). The authors mention that it is evidence that the method does not seem to work unless with a larger dataset. It would be better if there were another dataset that can be tested to show that the HyperNet + EEGNet approach does indeed improve classification given more than 9 subjects. Alternatively, the Dreyer et al. dataset could be evaluated while varying the number of subjects for training, e.g. 8, 16, 24, 32, etc to see if the trend of improving performance given more subjects occurs. This would help to understand the relationship between dataset size and the effectiveness of the HyperNet approach. The lack of improvement on the BCI IV IIa dataset raises concerns about the general applicability of the method, and further investigation is needed to determine the conditions under which it is effective.

### Questions
1. The term "epoch" seems to be overloaded since they are common terms used in EEG and in machine learning but mean different things. I think it becomes unclear which meaning you use in the paper sometimes, for example here is the term "epoch" used in close proximity, although the former seems to mean a window of data and the latter seems to mean the number of times the HyperNet is trained on all batches: 
>• Motor imagery activity data in the form of an epoch is used to perform the binary class
classification with a forward pass on EEGNet with the generated weights from HyperNet.
• Cross entropy loss is accumulated for a batch of 50 epochs, and backpropagation is performed only on HyperNet parameters. Adam optimiser with learning rate 1e-4 is used." 

It would be better if the term "epoch" is better clarified when used. 

2. >"For the dataset from Dreyer et al. (2023), the ”acquisition runs” from 33 participants are used for training and stratified 5-fold cross-validation is used to select the best model." 

What variables are changed to select the best model? Is it the model architecture? Are hyperparameters tuned at all?

3. Although this passage is from the "2.4.1 Cross-Session Condition", it seems to imply that the train-test split is not split across sessions: 
>"For the BCI IV IIa dataset, the data from all nine participants is divided into five folds with stratified cross-validation; each fold in the iteration is considered as a test set while the other set is split with an 80-20 ratio to choose the best-performing model on the validation set." 

The original work for the BCI competition seems to imply that there are two sessions for each subject. Is there a reason that evaluation across sessions does not seem to be done in the current work?

4. In Table 1, EEGNet without the HyperNet seems to have 4 to 6 times the standard deviation as EEGNet with the HyperNet. Is there an explanation for this, especially when compared to how the ratio of the standard deviation seems to be much closer to 1 for Tables 2 and 3? If the same test in Table 1 is run with multiple seeds and using different subjects (not just the last 9 subjects) as the test set, would we still see such high variation across multiple folds for EEGNet without the HyperNet? 

5. For a practical control interface during deployment, it seems unclear when the resting state would occur, which is the input used in the HyperNet. Would a separate resting state classifier have to be used? Or would some other heuristic to determine resting state be sufficient?

6. What is the current state of the art in terms of performance for these two datasets for the metrics you evaluated?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors introduce a new architecture called HyperEEGNet aimed at enhancing EEG-based brain-computer interface (BCI) systems. This innovation addresses issues related to lengthy calibration sessions and the limited use of resting-state EEG data in motor imagery decoding tasks. By combining HyperNetworks with the EEGNet framework, HyperEEGNet adaptively generates weights for motor imagery classification based on resting-state data. In Leave-Subject-Out scenarios using a dataset of nine participants, its performance is comparable to the baseline EEGNet. However, when applied to larger datasets with 33 participants, HyperEEGNet shows improved generalization capabilities, effectively utilizing resting-state EEG information to manage unseen subjects. The model provides strong representations in both cross-session and cross-user contexts, underscoring the value of resting-state data for tasks such as motor imagery classification. Additionally, the results indicate that HyperEEGNet has a smaller memory and storage footprint, making it well-suited for edge computing. This approach offers faster user calibration and enhances the practicality of real-world BCI applications, representing a significant advancement in the field.

### Strengths
The model exhibits robust generalization capabilities, performing effectively in both Leave-Subject-Out scenarios and with larger datasets, demonstrating its ability to handle unseen subjects. Additionally, this approach promises reduced calibration time, which is essential for real-world BCI applications, thereby enhancing user-friendliness and practicality.

### Weaknesses
The initial evaluations rely on a relatively small dataset comprising just nine participants, which may not adequately reflect the variability found in larger populations. This raises questions about the generalizability of the findings without access to more extensive and diverse datasets. Specifically, the limited sample size may not capture the range of individual differences in EEG signals, such as variations in signal-to-noise ratio, anatomical differences, or cognitive strategies employed during motor imagery tasks. Additionally, while the use of resting-state EEG data is a novel approach, the model's performance may be affected if the quality or relevance of this data varies among different users or sessions. For example, differences in vigilance levels, cognitive states, or even minor movements during resting-state recordings could introduce noise or bias into the hypernetwork's weight generation process. Furthermore, incorporating HyperNetworks adds a layer of complexity to the training and tuning process, potentially necessitating greater computational resources and specialized knowledge for effective implementation. This includes the selection of appropriate hyperparameters for the hypernetwork, the optimization of its architecture, and the management of potential overfitting issues, which may not be straightforward for non-experts. Lastly, like many deep learning models, HyperEEGNet may have limitations in interpretability, making it difficult to ascertain how specific features impact its classification decisions. The black-box nature of the model makes it challenging to understand which aspects of the resting-state EEG are most influential in generating the weights, hindering the ability to refine the model or gain deeper insights into the underlying neurophysiological mechanisms.

### Questions
What specific task-related information do you think should be included to optimize the input frequency and enhance model performance? How might this affect the model's practical deployment?

Why wasn't the optimization of resting-state EEG data representations, especially concerning brain connectivity, explored? What additional features do you believe are important for downstream tasks that current measures do not capture?

What criteria will you use to evaluate the efficacy of HyperEEGNet in comparison to other transfer learning methods? Are there particular metrics or datasets that you consider essential for this assessment?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a novel architecture, HyperEEGNet, to improve EEG-based brain-computer interface (BCI) systems, addressing the limitations of long calibration sessions and the underutilization of resting-state EEG data in motor imagery decoding tasks. By integrating HyperNetworks with the EEGNet architecture, HyperEEGNet adaptively generates weights for motor imagery classification based on resting-state data. In Leave-Subject-Out scenarios using a dataset with nine participants, the model performs comparably to the baseline EEGNet. However, when scaled to datasets with 33 participants, HyperEEGNet demonstrates enhanced generalization capabilities, effectively leveraging resting-state EEG information to handle unseen subjects. The model achieves robust representations in both cross-session and cross-user scenarios, highlighting the potential of resting-state data for downstream tasks like motor imagery classification. Furthermore, the findings indicate that HyperEEGNet's smaller footprint reduces memory and storage requirements, making it suitable for edge computing. This approach promises faster user calibration and improved feasibility for real-world BCI applications, advancing the field significantly.

### Strengths
Robust Generalization: The model demonstrates strong generalization capabilities, performing well in both Leave-Subject-Out scenarios and with larger datasets, indicating its effectiveness in handling unseen subjects.

Reduced Calibration Time: The approach promises faster user calibration, which is crucial for real-world BCI applications, making it more user-friendly.

### Weaknesses
Limited Dataset Size: The initial evaluations involve a relatively small dataset with only nine participants, which may not fully capture the variability present in broader populations. The generalizability of the findings could be questioned without larger, more diverse datasets. Specifically, the dataset lacks diversity in terms of age, gender, and neurological conditions, which could significantly impact the model's performance in real-world scenarios. The absence of a clear justification for the selection of these specific nine participants further weakens the study's conclusions.

Dependence on Resting-State Data: While leveraging resting-state EEG data is innovative, the model's effectiveness might be limited if the quality or relevance of the resting-state data varies across users or sessions. The study does not address potential confounds such as variations in vigilance levels, cognitive states, or environmental factors during resting-state data acquisition, which could introduce noise and bias into the model. Furthermore, the assumption that resting-state data is a stable and reliable predictor of motor imagery performance needs more rigorous validation.

Complexity of HyperNetworks: The integration of HyperNetworks may introduce additional complexity in model training and tuning, potentially requiring more computational resources and expertise to implement effectively. The paper does not provide a detailed analysis of the computational overhead associated with HyperNetworks, making it difficult to assess the practical feasibility of the proposed approach, especially for resource-constrained environments. The lack of a comparison with simpler, more established methods in terms of computational cost is a significant oversight.

Interpretability: As with many deep learning models, the interpretability of HyperEEGNet's decision-making process might be limited, making it challenging to understand how specific features influence classifications. The study does not explore techniques for visualizing or interpreting the learned representations, which hinders the understanding of the underlying mechanisms and limits the ability to diagnose potential issues or biases in the model. The black-box nature of the model raises concerns about its reliability and trustworthiness, particularly in clinical applications.

### Questions
What specific strategies were implemented to mitigate overfitting during training, especially given the observed risks at larger epoch sizes? How do you plan to validate the model's performance in cross-user scenarios beyond the training dataset?

Could you elaborate on the implications of a steep learning curve and rapid convergence in just 50 epochs? What does this suggest about the model's capacity to capture complex patterns in the data?

While the focus on two-class motor imagery classification is noted, what are the plans for extending this model to accommodate multiple classes or different downstream tasks? How do you envision addressing potential challenges in this expansion?

 How do you explain the performance variations among participants, particularly the discrepancy in accuracy for Participant ID 3? What insights can be gained from comparing the weights generated by the HyperNet with those from an EEGNet trained directly on activity data?

Why was the optimization of resting-state EEG data representations not explored, particularly regarding brain connectivity? What additional features do you think might be important for downstream tasks that are not captured by current measures?

What criteria will you use to compare the efficacy of HyperEEGNet against other transfer learning approaches? Are there specific metrics or datasets that you consider critical for this comparison?

What specific task-related information do you believe should be incorporated to optimize the input frequency and further enhance model performance? How will this impact the model's practical deployment?

### Soundness
2

### Presentation
1

### Contribution
2
