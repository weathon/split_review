# Identifying single molecule force spectroscopy data using deep learning with physics augmentation

- Decision: Reject
- Scores: 8, 5, 1

## Abstract
Deciphering the pathways of protein folding and unfolding under tension is essential for deepening our understanding of fundamental biological mechanisms. Such insights offer the potential to develop treatments for a range of incurable and fatal debilitating conditions, including muscular disorders like Duchenne Muscular Dystrophy and neurodegenerative diseases such as Parkinson’s disease. Single molecule force spectroscopy (SMFS) is a powerful technique for investigating forces when domains in proteins fold and unfold. Currently, manual visual inspection remains the primary method for classifying force curves resulting from single proteins; a time-consuming task demanding significant expertise. In this work, we develop a classification strategy to detect measurements arising from single molecules by augmenting deep learning models with the physics of the protein being investigated. We develop a novel physics-based Monte Carlo engine to generate simulated datasets comprising of force curves that originate from a single molecule, multiple molecules, or failed experiments. We show that pre-training deep learning models with the simulated dataset enables high throughput classification of SMFS experimental data with average accuracies of $75.3 \pm 5.3$\% and ROC-AUC of $0.87 \pm 0.05$. Our physics augmentation strategy does not need expensive expert adjudication of the experimental data where models trained using our strategy show up to 25.9\% higher ROC-AUC over the models trained solely on the limited SMFS experimental data. Furthermore, we show that incorporating a small subset of experimental data ($\sim 100$ examples) through transfer learning improves accuracy by 6.8\% and ROC-AUC by 0.06. We have validated our results on three new SMFS experimental datasets. To facilitate further research in this area, we make our datasets available and provide a Python-based toolbox (\url{https://anonymous.4open.science/r/AFM_ML-2B8C}).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper trains a classifier on time vs. force curves from protein unfolding force measurements. For such measurements, the model classifies whether the measurment came from the type of interaction that is desired to be observed, or from other artifacts that should not be included in the assessment of the protein unfolding forces. This has been done before. The application is useful because practitioners can automatically determine which measurments to include in downstream analyses instead of deciding manually. The papers main novelty is a dataset of simulated protein unfolding measurments which are used to train a better classifier next to training on experimental data. The paper is evaluated on three protein's unfolding measurmeents.

### Strengths
1. The paper introduces an interesting task to the ML conference community (although it is not the first one to address the specific task with ML solutions).
2. Very good explanations of the new application area.
3. Good experimental protocols that  ensure statistical significance of the results.
4. The paper demonstrates that for these measurments, training on synthetic data suffices for obtaining a generalizable classifier that can predict whether force measurements

### Weaknesses
1. Novelty of the application: The paper applies the most basic ML solution to a task. It can still be valuable to introduce a new task to the ML community. The task has been addressed with similar ML tools in previous works. Thus, there is no novelty in application. There is some technical novelty in the creation of a synthetic dataset.
2. I am not completely sure whether this is a weakness since I am not familiar with the task: I would imagine that for most proteins of interest we do not have the same sequence and structure repeating multiple times and then observe the same unfolding pattern of essentially the same protein. Why is there no evaluation for proteins that are not repeating or is this the case for one of your 3 experiments? If this is indeed of interest, and we cannot simply combine a single protein of interest into a chain of repeating proteins, then it seems to me that the evaluations miss the important evaluation and only an easier task is evaluated. The task is easier because classifying whether the same unfolding event and the same pattern occurs in the curve multiple times is easy compared to classifying a single unfolding event.

Minor:
1. The task is very easy. Correct me if I am wrong, but it seems to me that the model could simply classify whether or not there is a repeated pattern in the response measurement.

### Questions
1. Are the molcules attached to something when we "pull" on them?
2. As far as I understand, we pull the proteins and observe their unfolding - how are the proteins attached to the head with which we pull?
3. How do we make sure that he molecules are always attached to the pulling head at the same residue? 
4. Does the medium in which we measure the pulling force affect the force measurement outcomes? 
5. Why would we have the same protein repeated multiple times in a chain? Are they attached together in some fashion?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a method for classifying single-molecule force spectroscopy (SMFS) data using deep learning models enhanced by physics-based simulations. These models classify force curves as originating from no molecule, a single molecule, or multiple molecules, a task traditionally handled through time-consuming expert visual inspection. The authors propose a Monte Carlo simulation framework to create annotated datasets that mimic real-world experimental data, which they use to pre-train deep learning models. The model accuracy improves further with transfer learning on a small subset of experimental data, achieving up to 75.3% accuracy and a ROC-AUC of 0.87 across multiple datasets.

### Strengths
- Originality
  - The originality arises from the proposed physics-augmented simulation framework that enables deep learning models to learn realistic representations of SMFS force curves without relying heavily on annotated experimental data.
- Quality
  - Extensive comparative analysis across deep learning architectures was conducted.
  - The proposed method outperforms previous works.
- Clarity
  - The method is described clearly.
- Significance
  - This study offers a generalizable solution for SMFS data classification, a critical need in the study of protein folding and unfolding mechanisms.
  - The reduction in dependency on expert visual inspection and annotated data also lowers barriers to adoption, making SMFS analysis more accessible to the broader biological research community.

### Weaknesses
- Assumptions in simulation
  - The Monte Carlo (MC) simulation framework assumes identical protein domains across molecules, which could limit the model’s effectiveness for proteins with heterogeneous domains. This assumption may restrict the model’s generalizability, particularly in cases where protein unfolding behavior varies between domains.
- Computational efficiency and scalability
  - MC requires considerable computation for each force curve, which might hinder its scalability, particularly in high-throughput SMFS applications that involve thousands of force curves. While this approach is effective in current datasets, its feasibility for larger datasets remains uncertain.

### Questions
- Impact of Transfer Learning on Model Performance
  - The paper notes that transfer learning with a subset of experimental data improves model accuracy and ROC-AUC. Could you clarify the minimum amount of experimental data required to achieve significant performance gains?
- Data Diversity and Experimental Validation
  - The experimental datasets focus on non-specific pulling for three proteins. Have you considered validating the model on additional proteins or experimental setups (e.g., different solution conditions or functionalized probes)? If not, do you anticipate any limitations when applying this model to other setups?
- Sensitivity to Simulation Parameters
  - How sensitive is the model to variations in key simulation parameters, such as those defined by the DHS model? Does the accuracy vary significantly if the estimated parameters are slightly off?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
1

### Summary
While I recognize the potential significance of the work in understanding protein folding and unfolding using Single Molecule Force Spectroscopy (SMFS) data, I must inform AC and SAC that this specific area is outside my main expertise. Given this, I may not be able to offer detailed or technically relevant feedback that would benefit the review process.

I am happy to provide general comments regarding the manuscript's clarity and structure if necessary, but I wanted to notify you in case you would prefer to reassign this review to someone with more specialized knowledge in SMFS and its related methodologies.

Thank you for your understanding.

### Strengths
None

### Weaknesses
None

### Questions
None

### Soundness
4

### Presentation
4

### Contribution
4
